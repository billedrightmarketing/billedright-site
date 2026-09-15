# Change Map — Psychiatry Specialty Page

`/specialties/psychiatry-rcm-services/` (`pages/psychiatry-rcm-services.html`)

## Implementation Log

**2026-09-15 — Full rebuild per `docs/specialty-pages/Billed_Right_Specialty_Page_Framework_V2.md`
and `docs/specialty-pages/psychiatry/Billed_Right_Psychiatry_RCM_Final_Implementation.md`.**

Rebuilt the page into the V2 framework's 13-section order (Hero, Why
Psychiatry RCM Is Different, Revenue Leaks, How Billed Right Helps +
Add-On Services, Common Denials, EMR & Technology, Verified KPIs, Data to
Decisions, Built for Growth, Case Study/Testimonial, Resources, FAQs,
Final CTA), replacing the prior flatter two-column layout.

### RETAIN
- Existing verified Psychiatry KPIs (97% collections, 20-day A/R
  reduction, 1% error ratio, <48hr TAT, <1% no-response, 28-day payment
  TAT) — values unchanged, per locked decision, pending Arun's refresh.
- Genuine Psychiatry testimonial ("Psychiatry Provider, Florida") —
  kept verbatim, not rewritten. **Not upgraded** to the `Dr. [First Name]
  — Psychiatry — [City, State]` attribution format specified in the
  framework, because `docs/claims-register.md` lists this exact
  testimonial as `NEEDS VERIFICATION` / `HOLD pending permission and
  attribution confirmation` (row: "Testimonial — 'Psychiatry Provider,
  Florida'"). Adding a name/city would require detail that isn't
  currently on file or approved. **Action item for Marketing/Legal:**
  resolve the HOLD in the claims register before this testimonial (used
  here, on the homepage, and on `pages/welcome-cbs/index.html`) can be
  considered fully cleared, or before richer attribution is added.
- Strongest existing denial content (documentation, E/M level, telehealth
  modifier, missing PA, medical necessity) — restructured into the
  Denial / Root Cause / Billed Right Approach table format.
- Existing URL, resources-section pattern, and specialty cross-link list.

### REWRITE
- Hero, "Why Different," Revenue Leaks, Denials presentation, FAQs, Final
  CTA — per the implementation doc's provided copy, adapted into existing
  page CSS components (`.br-love-grid`, `.br-service-card`,
  `.br-compare-table`, `.br-tech-grid`, `.br-faq-item`, `.br-final-cta`).
- Lead form: merged First/Last Name into a single required `name` field
  (matches the fallback-split logic already in `zoho-lead.js`), removed
  the "Number of Providers" dropdown (excessive qualification per
  framework §17), reframed from "Download Our Brochure" to "Schedule a
  Revenue Cycle Assessment." Netlify form name/`formSource` renamed
  `psychiatry-brochure-request`/`psychiatry-brochure` →
  `psychiatry-assessment-request`/`psychiatry-assessment` so the CRM lead
  description no longer mislabels this as a brochure-download lead (see
  `zoho-lead.js`'s `isBrochureForm` check, which keys off the
  `-brochure` suffix). Relocated the form to its own anchored section
  (`#psychiatry-assessment-form`) rather than beside the hero, so the
  hero itself stays fast/text-plus-CTA per framework §2 ("reduce generic
  marketing language above the fold").

### NEW
- Immediate-proof hero stat row ("Since 2006," 97%, <1%).
- "Additional / Add-On Services" callout distinguishing Medical Coding,
  Prior Authorization, Credentialing, Documentation Management, and
  Contract Renegotiation from core RCM (with internal links to each
  service page) — the live page previously implied Prior Authorization
  was performed as standard scope (an FAQ answered "Yes. We track
  authorization requirements per payer and submit and follow up on
  IOP... authorizations" with no add-on framing).
- Data-to-Decisions and Built-for-Growth sections (did not exist before).
- EMR & Technology section naming the six locked platforms
  (eClinicalWorks, athenahealth, AdvancedMD, IMS, CentralReach,
  CareCloud) — the live page previously said only "all major EMR...
  systems" generically.
- Illustrative case-study block (see CASE STUDY below).

### REMOVE / REDUCE
- All CPT/HCPCS code references (90791, 90834/90837, 90833/90836/90838,
  99213–99215, 99492–99494) — previously appeared in the FAQ schema and
  a "Payer-Specific Considerations" paragraph. Removed entirely rather
  than "reduced," since the framework's 13 canonical sections have no
  dedicated coding-complexity slot and the same expertise is now
  demonstrated conceptually in "Why Psychiatry RCM Is Different" and the
  denial table without code lists.
- "18+ years in psychiatric RCM" (page footer note) and the KPI grid's
  "20 / Years of experience" tile — both replaced with "Since 2006" /
  "Psychiatry RCM Experience," per the locked decision against rolling
  year-count claims. This is the one KPI-grid value changed; all other
  KPI numbers are untouched.
- "Download Our Brochure" as the primary conversion framing (see REWRITE).

### CASE STUDY (implementation doc §15)
Checked `pages/case-studies/` — only Allergy, Cardiology, Credentialing,
and Primary Care case studies exist; **no real, approved Psychiatry case
study exists in the project.** The previously live page had no full case
study section, only a small Resources teaser card titled "Psychiatry
Practice Reduces Denials and Recovers Lost Revenue" (description already
called it "a composite look," but the card title itself read as a real
result, and it linked to the generic `/case-studies/` hub with no actual
matching page).

**Outcome taken: labeled clearly as "Illustrative Psychiatry
Revenue-Cycle Scenario"** (option 2 of the three specified in the task),
built as its own Section 10 block with an explicit red disclaimer line
("This is an illustrative scenario for explanatory purposes and does not
represent a specific client or verified result") before any narrative,
using the Starting Situation → Revenue-Cycle Problem → Billed Right
Action → Outcome structure. The "Outcome" is written qualitatively only
("greater visibility... a documented process...") with no invented
numbers, since a hypothetical scenario can't carry a "Verified Outcome."
The old redundant Resources-card link to `/case-studies/` was replaced
with two other on-topic (non-case-study) resource topics.

### TESTIMONIAL (implementation doc §16)
Real Psychiatry testimonial exists and was kept — see RETAIN above for
why the attribution format was not upgraded.

### SEO
- Title: `Psychiatry Revenue Cycle Management Services | Billed Right`
- Meta description: implementation doc's exact locked copy (186
  characters — flagging that it will likely truncate in the SERP snippet
  at Google's typical ~155–160 char display width; copy itself was not
  shortened since it was given as locked wording).
- Canonical/URL: unchanged (`/specialties/psychiatry-rcm-services/`).
- Schema: `Service` name/description rewritten to remove the implication
  that E/M/psychotherapy coding is automatically included; `FAQPage`
  replaced with the 10 new buyer-intent questions; `BreadcrumbList` and
  org-level `Organization`/`MedicalBusiness`/`WebSite` nodes unchanged
  (shared site-wide schema, out of this page's scope).
- Internal links added: `/services/denial-management/`,
  `/services/ar-follow-up/`, `/services/medical-coding/`,
  `/services/authorizations/`, `/services/credentialing/`,
  `/services/documentation-management/`, `/services/contract-renegotiation/`,
  `/contact/`, `/testimonials/`.

## Not in scope / not touched
- `netlify/functions/zoho-lead.js`, `build.py`, `templates/nav-template.html`,
  `templates/footer-template.html`, `sitemap.xml` — unchanged.
- No other specialty page touched.
- `pages/thank-you/psychiatry/index.html` — left as-is; it's a shared
  generic thank-you template, not named in the implementation doc's
  section list.
