// netlify/functions/zoho-lead.js
//
// SCAFFOLD ONLY — no Zoho integration logic yet. This function currently
// just logs whatever payload it receives and returns 200 so it can be
// safely deployed and pointed at before the real Zoho CRM lead-creation
// logic is written.
//
// Intended purpose (not yet implemented): receive a submission from any
// of the site's forms (contact form, per-service "consultation request"
// forms, per-specialty "brochure request" forms, case study forms, the
// chat widget's contact form) and create/update a Lead in Zoho CRM via
// the Zoho CRM REST API.
//
// Required environment variables (set in Netlify — Site settings >
// Environment variables — not committed to this repo):
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
// None of the above are read or used yet — see the TODO below.

exports.handler = async (event, context) => {
  console.log("zoho-lead function invoked");
  console.log("HTTP method:", event.httpMethod);
  console.log("Headers:", JSON.stringify(event.headers));
  console.log("Raw body:", event.body);

  // TODO (next pass): parse event.body (JSON or Netlify Forms-style
  // application/x-www-form-urlencoded payload depending on how this
  // function ends up being invoked), map fields to a Zoho Lead record,
  // obtain an access token via ZOHO_REFRESH_TOKEN, and POST to
  // https://www.zohoapis.<ZOHO_DC>/crm/v2/Leads.

  return {
    statusCode: 200,
    body: JSON.stringify({ received: true }),
  };
};
