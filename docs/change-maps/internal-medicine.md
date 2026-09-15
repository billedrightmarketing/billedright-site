# Change Map — Internal Medicine Specialty Page

`/specialties/internal-medicine-rcm-services/` (`pages/internal-medicine-rcm-services.html`)

## Implementation Log

**2026-09-15 — Full rebuild per
`docs/specialty-pages/Internal Medicine/Billed_Right_Internal_Medicine_FINAL_Flagship_RCM_SEO_AI_Implementation.md`
(FINAL — single source of truth).**

Rebuilt the page from a CPT/E-M-coding-heavy specialty explainer into a
17-section commercial RCM pillar page following the doc's Recommended Page
Architecture (§7): Hero+Proof, Why Financially Different, Managed Care vs.
Fee-for-Service, Where Financial Performance Can Break Down, How Billed
Right Supports the Revenue Cycle, Diagnosis Capture & Provider Education,
Intelligent RCM, Managed-Care Performance Reporting, End-to-End
Fee-for-Service RCM, Data-to-Decisions for CFOs & COOs, Core RCM vs.
Additional/Custom Services, EMR & Technology, Verified KPIs, Built for
Multi-Provider & Multi-Location Organizations, Authentic Client Proof,
Resources, Buyer FAQs, one Final CTA. All Cumulative Specialty-Page
Standard items (§36) — carried forward from Psychiatry, Cardiology and
Pain Management — were applied from the start: single final conversion
section, no artificial "Reviewed by" line, conservative KPI handling, and
the strict real-proof hierarchy.

### RETAIN
- Established URL (`/specialties/internal-medicine-rcm-services/`).
- Existing verified KPIs (97% collections, 20-day A/R reduction, 1% error
  ratio, <48hr TAT, <1% no-response, 28-day payment TAT) — values and
  labels unchanged from the live page, per the doc's Verified KPI rule
  (§21: do not change approved numbers, do not add words like
  Net/Average/Days/Hours/Reduction/Rate without validation). Only the
  rolling "20 / Years of experience" tile was replaced, per the doc's
  explicit locked instruction.
- Genuine Florida Internal Medicine testimonial ("Internal Medicine
  Provider, FL") — kept verbatim, not rewritten or given invented
  attribution detail.
- Denial/pain-point concepts (E/M documentation, prior authorization,
  chronic care management billing, split/shared visit documentation,
  referral medical necessity) — reframed at buyer level throughout
  "Where Financial Performance Can Break Down" rather than as a
  CPT-code table.

### REWRITE
- Hero, opening framing, revenue-leak section, FAQs, final CTA — replaced
  with the doc's locked copy and structure, adapted into existing page CSS
  components (`.br-services-grid`, `.br-feature-list`, `.br-tech-grid`,
  `.br-callout`, `.br-faq-item`).
- Lead form: merged First/Last Name into a single required `name` field,
  removed the "Number of Providers" dropdown, reframed from "Download Our
  Brochure" to "Schedule a Revenue Cycle Assessment." Form
  name/`formSource` renamed `internal-medicine-brochure-request`/
  `internal-medicine-brochure` → `internal-medicine-assessment-request`/
  `internal-medicine-assessment` so `zoho-lead.js`'s `isBrochureForm`
  check (keyed off the `-brochure` suffix) no longer mislabels this as a
  brochure-download lead.
- "Reviewed by Billed Right's internal medicine billing team, 18+ years…"
  replaced with the doc's exact locked evergreen statement (§6): "Billed
  Right has supported Internal Medicine revenue cycle management since
  its earliest years, with client relationships dating to 2007." This is
  a deliberately different claim from other specialty pages' "since 2006"
  company-founding language — the doc specifically ties Internal Medicine
  client relationships to 2007, not the company's 2006 founding date, and
  that distinction was preserved rather than flattened to match the other
  pages.

### NEW — Internal Medicine's distinctive sections (not present on any
other specialty page, per the doc's explicit instruction not to just make
this page "look like Cardiology or Pain Management")
- **Managed Care vs. Fee-for-Service** (doc §9) — flagship differentiator
  section with the VERIFY → CLASSIFY → PROCESS → MEASURE → IDENTIFY GAPS
  → ACT workflow visual, explicitly disclaiming that Billed Right does
  not determine clinical eligibility, actuarial risk, or legal plan
  status.
- **Diagnosis Capture & Provider Education** (doc §12) — major
  differentiator section explaining Billed Right's role in monitoring
  diagnosis-capture patterns and educating providers, paired with a
  compliance callout matching the doc's guardrails verbatim (no
  encouraging undocumented coding, no risk-adjustment-coding claim, no
  clinical-diagnosis-determination claim) and the doc's locked principle:
  "Accurate documentation first. Appropriate diagnosis capture second.
  Financial visibility follows."
- **Managed-Care Performance Reporting** (doc §15) — CFO/COO-focused
  section using the doc's exact locked sentence ("Billed Right helps
  practices identify performance shortfalls and take informed action
  toward meeting applicable program requirements and capturing available
  incentive opportunities") with an explicit no-guarantee disclaimer
  (no bonus, quality-score, risk-score, or clinical-outcome guarantees).
- **End-to-End Fee-for-Service RCM** (doc §16) — VERIFY → CAPTURE → SUBMIT
  → MONITOR → RESOLVE → POST → COLLECT → INFORM workflow visual, replacing
  a flat service list.
- **Custom Analytics / Additional Data Support** callout (doc §18) — a
  new, Internal-Medicine-specific addition to the Core-RCM-vs-Additional
  section, distinct from the standard Holistic Services list, explicitly
  labeling patient-care/population-oriented analytics as not part of
  standard RCM unless contracted.

### REMOVE / REDUCE
- All CPT/HCPCS/modifier references (99213–99215, 99490, 99491, 99487,
  G0438, G0439, modifier 25) and the associated "Payer-Specific
  Considerations" coding paragraph and CPT-driven FAQ set — removed
  entirely, consistent with the doc's explicit instruction not to open
  with or center the page on CPT/ICD tutorials (§4, §36).
- "18+ years in internal medicine RCM" — replaced with the doc's locked
  evergreen/2007 language (see REWRITE above).
- "Download Our Brochure" as the primary conversion framing (see REWRITE).
- Duplicate ending CTAs — built as exactly **one** final conversion
  section from the start, with Our Specialties moved to its own section
  immediately below and no other major CTA after it.

### CASE STUDY / PROOF HIERARCHY (doc §23)
Checked `pages/case-studies/` — only Allergy, Cardiology, Credentialing
and Primary Care case studies exist. **No real, approved Internal
Medicine case study exists in the project**, confirming the gap
previously flagged. The prior live page's Resources card ("Internal
Medicine Practice Reduces Denials and Recovers Lost Revenue") explicitly
self-described as "a composite look" — **removed entirely, with no
illustrative/hypothetical replacement**, per the doc's Proof Hierarchy
rule: "Real Internal Medicine case study > Authentic Internal Medicine
testimonial > No case study." No fallback illustrative-scenario option
was offered for this doc (same stricter standard as Pain Management).

**Outcome: no case-study section on the page.** The "Authentic Internal
Medicine Client Proof" section carries only the genuine testimonial.
**This remains a confirmed gap** — if Billed Right develops a real,
approved Internal Medicine case study in the future, the doc's structure
(practice context → managed-care/FFS challenge → operational or
diagnosis-capture issue → Billed Right actions → verified outcome → time
period/context) is ready to receive it.

### TESTIMONIAL (doc §23)
Real Internal Medicine testimonial exists (already live on the page
pre-rebuild, attributed "Internal Medicine Provider, FL") and was
elevated to its own section, kept exactly as approved.

**Flag for Marketing/Legal:** this testimonial had **never been added to
`docs/claims-register.md`** prior to this rebuild — unlike the Psychiatry,
Cardiology and Pain Management testimonials, which already carried
`NEEDS VERIFICATION` rows. Added a new row today (2026-09-15) so it now
carries the same governance tracking and HOLD status as the others. It
was used here per the doc's explicit instruction ("Use the exact approved
wording if still validated"), but should not be treated as a fully
cleared claim until Client Success/Legal resolves the new HOLD.

### EMR & TECHNOLOGY (doc §20) — action item, not resolved
The doc explicitly states: "Do not assume the Cardiology or Pain
Management EMR order applies to Internal Medicine... Before publication,
Raul must validate the Internal Medicine EMR list with operations... Do
not invent 'deep expertise' in a platform without first-party support."
**No EMR list was provided in the doc for Internal Medicine** (unlike
Cardiology's eClinicalWorks-flagship treatment or Pain Management's
eClinicalWorks/IMS/AdvancedMD list). Rather than inventing one, this
section uses only generic positioning ("a wide range of existing
practice-management and EMR environments") with an explicit
`[CONFIRM CURRENT CAPABILITY]` placeholder noting that a validated,
prioritized EMR list is pending internal confirmation.
**Action item for Raul/Operations:** supply the actual Internal
Medicine EMR list (with priority order) so this section can be completed
with named, verified platforms.

### AI / GUARDRAILS
- No "revolutionary AI," "fully autonomous RCM," "eliminates denials," or
  "guaranteed faster payment" language used.
- No future-roadmap capability presented as live.
- Every Intelligent RCM capability (claim quality, denial pattern
  detection, A/R prioritization, eligibility automation, diagnosis/
  documentation exception visibility, Data-to-Decisions) is framed to
  answer the doc's four-question quality test (§14).
- No SOC 2 claim or badge anywhere on the page.
- No risk-adjustment-consulting, managed-care-contracting, or
  clinical-outcomes-management claim.
- No bonus/quality-score/risk-score guarantee language.
- No PE-backed claim (not raised in this doc; omitted).

### SEO
- Title: `Internal Medicine Revenue Cycle Management & Billing Services |
  Billed Right` (doc's primary recommended title).
- Meta description: doc's exact locked copy — "Internal Medicine RCM for
  managed-care and fee-for-service practices. Improve revenue-cycle
  execution, diagnosis visibility and financial insight with Billed
  Right."
- Canonical/URL: unchanged.
- Schema: `Service` name/description rewritten to reflect the managed-care
  / fee-for-service / diagnosis-capture / Data-to-Decisions positioning
  (Prior Authorization/Medical Coding called out as separately scoped)
  instead of the prior E/M-and-CCM-coding description. `FAQPage` replaced
  with the doc's 10 buyer-intent questions (§28). `BreadcrumbList` and
  org-level `Organization`/`MedicalBusiness`/`WebSite` nodes unchanged
  (shared site-wide schema, out of this page's scope).
- Internal links added/kept: `/services/authorizations/`,
  `/services/medical-coding/`, `/services/credentialing/`,
  `/services/documentation-management/`,
  `/services/contract-renegotiation/`, `/services/`, `/contact/`,
  `/testimonials/`.

## Internal-Medicine-Specific QA Checklist Results
(Doc §34 "Pre-Publish Validation" — full pass/fail/unconfirmed report
delivered in-conversation.) Summary: all implementable content, guardrail,
structural and SEO items **pass**. Two items are explicitly **flagged as
open action items, not failures**: (1) the Internal Medicine EMR list
requires Raul/Operations validation before specific platforms can be
named (see EMR & TECHNOLOGY above); (2) the "Internal Medicine
Provider, FL" testimonial's claims-register HOLD is newly opened, not yet
resolved. Zoho lead creation, CRM routing, and mobile carrier-level
click-to-call behavior are **unconfirmed** — cannot be verified in this
local/static environment (no live Netlify Functions/Zoho endpoint),
consistent with every prior specialty-page QA report.

## Not in scope / not touched
- `netlify/functions/zoho-lead.js`, `build.py`, `templates/nav-template.html`,
  `templates/footer-template.html`, `sitemap.xml` — unchanged.
- No other specialty page touched (Cardiology remains frozen per its own
  change map; Psychiatry and Pain Management unchanged).
- `pages/thank-you/internal-medicine/` — left as-is; shared generic
  thank-you template, not named in the implementation doc's section list.
