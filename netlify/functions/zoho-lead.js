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

// Looks up whether the Leads module has a custom field for "specialty" so
// we can set it directly instead of folding it into Description. Cached
// per warm function instance (module-level) since it can't change
// mid-invocation and there's no need to re-fetch it on every request.
// Falls back to null (meaning: use Description) on any failure — a
// broken metadata lookup should never block lead creation.
let cachedSpecialtyFieldApiName;

async function findSpecialtyFieldApiName(accessToken, dc) {
  if (cachedSpecialtyFieldApiName !== undefined) {
    return cachedSpecialtyFieldApiName;
  }
  try {
    const res = await fetch(
      `https://www.zohoapis.${dc}/crm/v3/settings/fields?module=Leads`,
      { headers: { Authorization: `Zoho-oauthtoken ${accessToken}` } }
    );
    if (!res.ok) {
      cachedSpecialtyFieldApiName = null;
      return null;
    }
    const data = await res.json();
    const fields = (data && data.fields) || [];
    const match = fields.find((f) => {
      const label = (f.field_label || "").toLowerCase();
      const apiName = (f.api_name || "").toLowerCase();
      return label === "specialty" || apiName === "specialty";
    });
    cachedSpecialtyFieldApiName = match ? match.api_name : null;
  } catch (err) {
    console.error(
      "zoho-lead: field metadata lookup failed, falling back to Description:",
      err
    );
    cachedSpecialtyFieldApiName = null;
  }
  return cachedSpecialtyFieldApiName;
}

// Maps the site's form field names to a Zoho Lead record.
// Field name note: the requirements spec this mapping as "company ->
// Company", but none of the site's actual forms collect a field named
// "company" — they collect "practice" (e.g. pages/contact.html, every
// service/specialty form). Mapped both, preferring an explicit "company"
// if a future form ever sends one, falling back to "practice".
function buildLeadPayload(fields, specialtyFieldApiName) {
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
  if (!lastName) {
    lastName = firstName || "Not Provided"; // Zoho requires Last_Name
  }

  const descriptionParts = [];
  const message = fields.message || fields["how-can-we-help"] || fields.challenge;
  if (message) descriptionParts.push(message);

  const lead = {
    Last_Name: lastName,
    Company: fields.company || fields.practice || "Not Provided",
    Lead_Source: "Website Form",
  };
  if (firstName) lead.First_Name = firstName;
  if (fields.email) lead.Email = fields.email;
  if (fields.phone) lead.Phone = fields.phone;

  if (fields.specialty) {
    if (specialtyFieldApiName) {
      lead[specialtyFieldApiName] = fields.specialty;
    } else {
      descriptionParts.push(`Specialty: ${fields.specialty}`);
    }
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

  const specialtyFieldApiName = fields.specialty
    ? await findSpecialtyFieldApiName(accessToken, ZOHO_DC)
    : null;
  const leadRecord = buildLeadPayload(fields, specialtyFieldApiName);

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
