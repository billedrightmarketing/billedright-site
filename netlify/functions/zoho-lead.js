// netlify/functions/zoho-lead.js
//
// Receives a submission from one of the site's forms (contact form,
// per-service "consultation request" forms, per-specialty "brochure
// request" forms, case study forms, the chat widget's contact form) and
// creates a Lead in Zoho CRM via the Zoho CRM v3 REST API.
//
// NOT wired to any form yet — see the report from this pass for what
// still needs to happen before a real submission reaches this function.
//
// Required environment variables (set in Netlify — Site settings >
// Environment variables — never committed to this repo):
//   ZOHO_CLIENT_ID      - OAuth client ID for the Zoho API console app
//   ZOHO_CLIENT_SECRET  - OAuth client secret for that app
//   ZOHO_REFRESH_TOKEN  - Long-lived refresh token used to mint short-lived
//                         access tokens at request time (self-client /
//                         offline access grant)
//   ZOHO_DC             - Zoho data center domain suffix for this account,
//                         e.g. "com" (.com), "eu" (.eu), "in" (.in),
//                         "com.au", "jp" - determines which
//                         accounts.zoho.<DC> / www.zohoapis.<DC> hosts to
//                         call. Get this from which Zoho region the CRM
//                         org was created in.
//
// Uses Node's built-in fetch (available on Netlify's default Node 18+
// function runtime) — no HTTP client dependency needed.

class ZohoRequestError extends Error {
  constructor(message, detail) {
    super(message);
    this.name = "ZohoRequestError";
    this.detail = detail;
  }
}

function getHeader(event, name) {
  const headers = event.headers || {};
  const key = Object.keys(headers).find(
    (k) => k.toLowerCase() === name.toLowerCase()
  );
  return key ? headers[key] : undefined;
}

// Accepts either:
//  - a flat JSON body (whatever a future fetch()-based form submit sends)
//  - a Netlify Forms "outgoing webhook" notification payload, shaped
//    like { payload: { data: { ...fields }, form_name, ... } }
//  - a standard application/x-www-form-urlencoded body (the default
//    encoding for the site's plain <form method="POST"> submissions)
function parseIncomingFields(event) {
  let raw = event.body || "";
  if (event.isBase64Encoded) {
    raw = Buffer.from(raw, "base64").toString("utf8");
  }

  const contentType = (getHeader(event, "content-type") || "").toLowerCase();

  if (contentType.includes("application/json")) {
    const parsed = raw ? JSON.parse(raw) : {};
    if (parsed && parsed.payload && parsed.payload.data) {
      return parsed.payload.data;
    }
    return parsed || {};
  }

  // application/x-www-form-urlencoded (or unspecified — treat as this,
  // since that's the default encoding a plain HTML form POST uses)
  const params = new URLSearchParams(raw);
  const fields = {};
  for (const [key, value] of params.entries()) {
    fields[key] = value;
  }
  return fields;
}

async function getAccessToken({ clientId, clientSecret, refreshToken, dc }) {
  const url = `https://accounts.zoho.${dc}/oauth/v2/token`;
  const body = new URLSearchParams({
    grant_type: "refresh_token",
    client_id: clientId,
    client_secret: clientSecret,
    refresh_token: refreshToken,
  });

  let res;
  try {
    res = await fetch(url, { method: "POST", body });
  } catch (err) {
    throw new ZohoRequestError("Could not reach Zoho's OAuth endpoint", err);
  }

  let data;
  try {
    data = await res.json();
  } catch (err) {
    throw new ZohoRequestError(
      "Zoho's OAuth endpoint returned a non-JSON response",
      { status: res.status }
    );
  }

  if (!res.ok || !data.access_token) {
    // Common causes: revoked/expired refresh token, wrong client id/secret,
    // or ZOHO_DC pointing at the wrong data center for this account.
    throw new ZohoRequestError("Zoho OAuth token refresh failed", {
      status: res.status,
      body: data,
    });
  }

  return data.access_token;
}

// Specialty_Multi_Select is a Multi Select picklist field on the Leads
// module — Zoho requires it be sent as an array of exact, case-sensitive
// picklist values, never a plain string.
//
// Maps every specialty value the site's forms currently send (contact
// form, chat widget, the 14 service-page forms, the 13 specialty-page
// hidden fields, and the 4 case-study forms) to the exact Zoho picklist
// value. Three site values have no clean match and are pinned to "Other"
// on purpose rather than guessed — see the report for this pass:
//   "Family Practice" -> Zoho only has "Family Medicine" (different string)
//   "Multispecialty"  -> Zoho only has "Multi-specialty" (hyphenated)
//   "Vascular Surgery" -> no matching or close Zoho option exists at all
const SPECIALTY_MAP = {
  "Allergy": "Allergy",
  "Behavioral Health": "Behavioral Health",
  "Cardiology": "Cardiology",
  "Family Practice": "Other", // no exact match — see comment above
  "Gastroenterology": "Gastroenterology",
  "Internal Medicine": "Internal Medicine",
  "Multispecialty": "Other", // no exact match — see comment above
  "Nephrology": "Nephrology",
  "Neurology": "Neurology",
  "Ophthalmology": "Ophthalmology",
  "Orthopedics": "Orthopedics",
  "Other": "Other",
  "Pain Management": "Pain Management",
  "Pediatrics": "Pediatrics",
  "Primary Care": "Primary Care",
  "Psychiatry": "Psychiatry",
  "Pulmonary": "Pulmonary",
  "Rheumatology": "Rheumatology",
  "Urgent Care": "Urgent Care",
  "Vascular Surgery": "Other", // no matching Zoho option — see comment above
};

// Maps a site specialty value to the exact Zoho picklist value. Anything
// not in SPECIALTY_MAP (a value none of today's forms send, or a typo/
// future addition) is logged server-side and defaulted to "Other" rather
// than sent as-is, since Zoho would reject an unrecognized picklist value
// outright.
function mapSpecialty(value) {
  if (Object.prototype.hasOwnProperty.call(SPECIALTY_MAP, value)) {
    return SPECIALTY_MAP[value];
  }
  console.warn(
    `zoho-lead: unrecognized specialty value "${value}" — defaulting to "Other"`
  );
  return "Other";
}

// Maps the site's form field names to a Zoho Lead record.
// Field name note: the requirements spec this mapping as "company ->
// Company", but none of the site's actual forms collect a field named
// "company" — they collect "practice" (e.g. pages/contact.html, every
// service/specialty form). Mapped both, preferring an explicit "company"
// if a future form ever sends one, falling back to "practice".
//
// Deliberately has NO fallback defaults (no "Not Provided") — the
// handler validates these are all present before ever reaching Zoho, so
// silently substituting a placeholder here would defeat that check.
function deriveContact(fields) {
  let firstName = (fields["first-name"] || "").trim();
  let lastName = (fields["last-name"] || "").trim();

  if (!firstName && !lastName) {
    const rawName = (fields.name || "").trim();
    const spaceIdx = rawName.indexOf(" ");
    if (spaceIdx === -1) {
      lastName = rawName;
    } else {
      firstName = rawName.slice(0, spaceIdx).trim();
      lastName = rawName.slice(spaceIdx + 1).trim();
    }
  }

  const company = (fields.company || fields.practice || "").trim();

  return { firstName, lastName, company };
}

function buildLeadPayload(fields, contact) {
  const descriptionParts = [];
  // Every form's free-text field goes to Message_From_Lead_Website_Form,
  // not Description: "message" (the chat widget), "challenge"
  // (pages/contact.html), "how-can-we-help" (the 4 case-study forms).
  // No form sends more than one of these, so this is never ambiguous.
  const freeTextMessage = fields.message || fields.challenge || fields["how-can-we-help"];

  const lead = {
    Last_Name: contact.lastName,
    Company: contact.company,
    Lead_Source: "Website Inquiry",
    // Read from a page_url field in the payload rather than the Referer
    // header, which can be stripped by the browser or a proxy and isn't
    // reliable. parseIncomingFields/the handler already warns server-side
    // if it's missing; an empty string here is the documented fallback,
    // not a silent failure.
    Lead_Source_Details: fields.page_url || "",
  };
  if (contact.firstName) lead.First_Name = contact.firstName;
  if (fields.email) lead.Email = fields.email;
  if (fields.phone) lead.Phone = fields.phone;
  if (freeTextMessage) lead.Message_From_Lead_Website_Form = freeTextMessage;

  if (fields.specialty) {
    lead.Specialty_Multi_Select = [mapSpecialty(fields.specialty)];
  }
  if (fields.form_source) {
    descriptionParts.push(`Source Page: ${fields.form_source}`);
  }
  if (descriptionParts.length) {
    lead.Description = descriptionParts.join("\n");
  }

  return lead;
}

async function createZohoLead(accessToken, dc, leadRecord) {
  const res = await fetch(`https://www.zohoapis.${dc}/crm/v3/Leads`, {
    method: "POST",
    headers: {
      Authorization: `Zoho-oauthtoken ${accessToken}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ data: [leadRecord] }),
  });

  const data = await res.json().catch(() => null);
  const result = data && Array.isArray(data.data) ? data.data[0] : null;
  const succeeded = res.ok && result && result.status === "success";

  if (!succeeded) {
    // Surface the raw Zoho response for server-side logging only — e.g.
    // a required-field validation error (see Company handling above) or
    // an org-specific mandatory field this function doesn't know about.
    throw new ZohoRequestError("Zoho Leads API rejected the record", {
      status: res.status,
      body: data,
    });
  }

  return result;
}

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      body: JSON.stringify({ success: false, error: "Method not allowed" }),
    };
  }

  const { ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET, ZOHO_REFRESH_TOKEN, ZOHO_DC } =
    process.env;

  if (!ZOHO_CLIENT_ID || !ZOHO_CLIENT_SECRET || !ZOHO_REFRESH_TOKEN || !ZOHO_DC) {
    console.error(
      "zoho-lead: missing one or more required environment variables " +
        "(ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET, ZOHO_REFRESH_TOKEN, ZOHO_DC)"
    );
    return {
      statusCode: 500,
      body: JSON.stringify({
        success: false,
        error: "Server is not configured correctly.",
      }),
    };
  }

  let fields;
  try {
    fields = parseIncomingFields(event);
  } catch (err) {
    console.error("zoho-lead: failed to parse request body:", err);
    return {
      statusCode: 400,
      body: JSON.stringify({
        success: false,
        error: "Could not parse the submitted form data.",
      }),
    };
  }

  if (!fields.email && !fields.phone) {
    return {
      statusCode: 400,
      body: JSON.stringify({
        success: false,
        error: "Please provide an email address or phone number.",
      }),
    };
  }

  // Fail fast with a clear message instead of letting Zoho reject the
  // lead with an opaque error — Last_Name is a hard Zoho requirement,
  // and First_Name/Company are required by this pass's spec.
  const contact = deriveContact(fields);
  const missing = [];
  if (!contact.firstName) missing.push("first name");
  if (!contact.lastName) missing.push("last name");
  if (!contact.company) missing.push("company/practice name");
  if (missing.length) {
    return {
      statusCode: 400,
      body: JSON.stringify({
        success: false,
        error: `Please provide your ${missing.join(", ")}.`,
      }),
    };
  }

  if (!fields.page_url) {
    console.warn(
      "zoho-lead: request had no page_url field — Lead_Source_Details will be empty"
    );
  }

  let accessToken;
  try {
    accessToken = await getAccessToken({
      clientId: ZOHO_CLIENT_ID,
      clientSecret: ZOHO_CLIENT_SECRET,
      refreshToken: ZOHO_REFRESH_TOKEN,
      dc: ZOHO_DC,
    });
  } catch (err) {
    console.error("zoho-lead: token refresh failed:", err.detail || err);
    return {
      statusCode: 502,
      body: JSON.stringify({
        success: false,
        error: "Unable to reach Zoho right now. Please try again shortly.",
      }),
    };
  }

  const leadRecord = buildLeadPayload(fields, contact);

  try {
    await createZohoLead(accessToken, ZOHO_DC, leadRecord);
  } catch (err) {
    console.error("zoho-lead: Zoho Leads API error:", err.detail || err);
    return {
      statusCode: 502,
      body: JSON.stringify({
        success: false,
        error: "Could not save your submission. Please try again or contact us directly.",
      }),
    };
  }

  return {
    statusCode: 200,
    body: JSON.stringify({ success: true }),
  };
};
