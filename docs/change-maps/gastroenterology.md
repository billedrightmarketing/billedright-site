# Change Map — Gastroenterology Specialty Page

`/specialties/gastroenterology-rcm-services/` (`pages/gastroenterology-rcm-services.html`)

## Implementation Log

**2026-09-16 — Full rebuild per
`docs/specialty-pages/gastroenterology/Billed_Right_Gastroenterology_FINAL_First_Time_Right_RCM_SEO_AEO_Implementation.md`
(FINAL — Implementation Source of Truth).**

Rebuilt the page from a CPT/NCCI-bundling/infusion-code-heavy specialty
explainer into an 17-section commercial RCM pillar page following the
doc's Final Page Flow (§32): Hero+Proof, Since-2006 GI Experience, One
Specialty/Multiple Revenue Paths, Revenue Leaks, GI Revenue-Cycle Model
(10-step workflow), Endoscopy & Colonoscopy, Professional vs. Facility
Revenue, Pathology, Hospital GI Revenue, Intelligent RCM, EMR
(eCW/IMS/AdvancedMD), Data-to-Decisions, KPIs/Outcomes, Authentic
Testimonial, Resources, FAQs, one Final CTA. Applied every Cumulative
Specialty-Page Standard item from the start (single final conversion
section, no artificial "Reviewed by" line, strict real-proof hierarchy).

### RETAIN
- Established URL (`/specialties/gastroenterology-rcm-services/`).
- The specialty's "since 2006" experience claim (already accurate and
  consistent with the company's own founding date, per the doc's
  explicit locked positioning).

### REWRITE
- Hero, opening framing, revenue-leak section, FAQs, final CTA —
  replaced with the doc's locked copy and structure, adapted into
  existing page CSS components (`.br-services-grid`, `.br-feature-list`,
  `.br-tech-grid`, `.br-callout`, `.br-faq-item`).
- Lead form: merged First/Last Name into a single required `name` field,
  removed the "Number of Providers" dropdown, reframed from "Download Our
  Brochure" to "Request a Revenue Cycle Assessment" (doc's exact locked
  primary CTA). Form name/`formSource` renamed
  `gastroenterology-brochure-request`/`gastroenterology-brochure` →
  `gastroenterology-assessment-request`/`gastroenterology-assessment` so
  `zoho-lead.js`'s `isBrochureForm` check no longer mislabels this as a
  brochure-download lead. Consent checkbox and PHI-warning line updated
  to the current sitewide-approved privacy wording (doc §22), matching
  the correction already applied to Internal Medicine, Nephrology, and
  the site's published Privacy Policy.
- "Reviewed by Billed Right's gastroenterology billing team, 18+ years in
  gastroenterology RCM" replaced with the doc's exact locked evergreen
  statement (§16, §26): "Billed Right has supported Gastroenterology
  revenue cycle management since 2006."

### NEW — Gastroenterology-specific major sections (not on any other
specialty page, per the doc's explicit instruction that this page must
communicate the full professional GI revenue cycle rather than looking
like any prior specialty rebuild)
- **Endoscopy & Colonoscopy Authority Section** (doc §8) — specialty
  authority section framed around financial-workflow complexity, with no
  CPT/modifier table (per the doc's explicit "Do not create a large
  CPT/modifier table" instruction), ending in the doc's exact commercial
  message callout.
- **Professional vs. Facility Revenue — Mandatory Scope Clarity** (doc
  §9) — dedicated section with the doc's exact required scope statement
  verbatim: "Billed Right's confirmed Gastroenterology surgical-center
  experience is primarily professional billing for the physician.
  Facility billing, when requested, should be separately evaluated and
  scoped based on the organization and service requirements." No
  end-to-end ASC facility-billing claim made anywhere on the page.
- **Pathology — Important Differentiator** (doc §10) — new section (no
  pathology content existed on the prior live page at all) explaining
  pathology professional-component billing and the lab-entity-support
  experience, with the doc's exact scope statement, avoiding any claim of
  pathology interpretation, clinical lab management, or lab compliance
  consulting.
- **Hospital GI Revenue** (doc §11) — new section on hospital
  professional revenue, deliberately avoiding place-of-service code
  lists per the doc's instruction.
- **GI Revenue-Cycle Model** — a 10-step workflow visual (VERIFY →
  CAPTURE → SUBMIT → MONITOR → PRIORITIZE → RESOLVE → POST → ANALYZE →
  EDUCATE → IMPROVE), matching the doc's exact specified sequence (§7),
  the same length/pattern used on the Nephrology rebuild.

### REMOVE / REDUCE
- **All infusion/biologic billing positioning removed entirely**, per
  the doc's explicit §18 instruction ("Remove existing GI
  infusion/biologic billing positioning... Do not replace removed
  content simply to preserve page length"). This included: the hero
  callout's infusion-billing sentence, a "Pain Areas" bullet about IBD
  biologic infusion, a "Solutions" bullet referencing infusion claims, a
  full FAQ + matching schema entry about biologic infusion billing
  (96413/96415/J-codes), and a denial-reasons card about missing prior
  authorization for biologic infusion. **This is the single largest
  content removal of any specialty rebuild this session** — infusion/
  biologic billing was previously presented as a verified GI capability,
  and the doc is explicit that Billed Right does not want this presented
  as verified.
- All CPT/HCPCS/G-code references (45378, 45380, 45385, 43239–43259,
  G0121, G0105, 96413, 96415) and the associated NCCI-bundling-rules
  coding paragraph and CPT-driven FAQ set — removed entirely, consistent
  with the doc's repeated instruction not to build a CPT/modifier
  reference page (§1, §8, §26, §33).
- "18+ years in gastroenterology RCM" / "Reviewed by..." footer line (see
  REWRITE above).
- "Download Our Brochure" as the primary conversion framing (see REWRITE
  above).
- Duplicate ending CTAs — built as exactly **one** final conversion
  section from the start, with Our Specialties moved to its own section
  immediately below and no other major CTA after it.
- Generic "We work with all major EMR" line — replaced with the doc's
  locked three-platform list (see EMR section below).

### CASE STUDY / PROOF HIERARCHY (doc §16)
Checked `pages/case-studies/` — only Allergy, Cardiology, Credentialing
and Primary Care case studies exist. **No real, approved Gastroenterology
case study exists in the project.** The prior live page's Resources card
("Gastroenterology Practice Reduces Denials and Recovers Lost Revenue")
explicitly self-described as "a composite look" — **removed entirely,
with no illustrative/hypothetical replacement**, per the doc's Proof
Hierarchy rule: "Real Gastroenterology Case Study > Authentic
Gastroenterology Testimonial > No Case Study," and its explicit
instruction "Do not invent a GI case study from Billed Right's
experience."

**Outcome: no case-study section on the page.** This remains a confirmed
gap — if Billed Right develops a real, approved Gastroenterology case
study in the future, a dedicated section can be added following the
pattern used for Cardiology's real case study.

### TESTIMONIAL (doc §16) — found on a different page than expected
Unlike Nephrology (whose genuine testimonial was already live directly
on the specialty page) or Internal Medicine, the prior live
Gastroenterology specialty page had **no testimonial section at all**.
Searched the rest of the site and found **two genuine, already-published
Gastroenterology testimonials on `/testimonials/`** (tagged
`data-cat="gastroenterology"`):
1. "Practice Administrator, FL" — on the quality of a billing-company
   transition.
2. "Practice Manager, FL" — on billing/verification satisfaction.

The implementation doc's §16 only instructs generically to include "an
authentic Gastroenterology testimonial" if available, and says "If no
approved GI testimonial/case study is available, omit the section" — it
does not name or bless a specific quote the way the Nephrology doc did.

**Decision:** used testimonial #1 (the more substantive quote) on the
rebuilt specialty page, re-attributed from "Practice Administrator, FL"
to "Practice Administrator, Gastroenterology Practice, Florida" to match
the contextual attribution format used on every other specialty page.
Quotation text kept 100% verbatim. **Flag for Marketing:** this
testimonial was already public on the sitewide testimonials page but had
never been used on a specialty page or logged in the claims register —
added a new `NEEDS VERIFICATION` row (weaker sign-off than Nephrology's
`VERIFIED` row, since this doc doesn't explicitly bless this specific
quote for specialty-page use the way Nephrology's did). The second
testimonial ("Practice Manager, FL") remains available on
`/testimonials/` if Marketing prefers it instead.

### EMR (doc §13, §27)
Locked list used exactly as specified: **eClinicalWorks (eCW), IMS, and
AdvancedMD** — no Athena or CareCloud added, per the doc's instruction
not to add other EMRs without verification. Copy accurately reflects the
doc's nuance that eCW and IMS are the most common among GI clients, with
AdvancedMD as additional verified experience (not an equal-weight
three-way list implying identical usage frequency).

### KPI / RESULTS SECTION (doc §15) — same deliberate deviation as
Nephrology, flagged clearly
Consistent with the Nephrology rebuild's precedent, this doc explicitly
states existing published KPI numbers "are not automatically approved"
and provides a fallback: "Until validated, use qualitative outcomes such
as stronger claim quality, disciplined denial follow-up, earlier
exception identification, prioritized A/R, clearer service-line
visibility and better decision support." Since no KPI validation
occurred in this session, the numeric KPI grid (97% collections, 20-day
A/R reduction, etc.) was **removed and replaced with six qualitative
outcome categories** drawn directly from the doc's own listed examples,
with a note that specialty-specific KPI figures will be added once
validated.

**Action item for Raul/Arun:** if the shared KPI figures are in fact
already approved for Gastroenterology specifically, provide that
confirmation and the numeric grid can be restored to match the treatment
used on Psychiatry, Cardiology, Pain Management and Internal Medicine.

### AI / GUARDRAILS
- No "revolutionary AI," generic AI hype, guarantees, zero-touch claims,
  or roadmap capabilities presented as live.
- Every Intelligent RCM capability (claim-quality automation, eligibility
  automation, denial classification/pattern detection, A/R
  prioritization, authorization exception visibility, Data-to-Decisions)
  states technology → signal → human action → revenue problem, passing
  the doc's four-question AI Quality Test.
- No SOC 2 claim, invented certification, guaranteed collections,
  guaranteed denial reduction, clinical advice, or legal advice anywhere
  on the page.
- No competitor attacks.
- No blanket ASC facility-billing claim (see Professional vs. Facility
  Revenue section above).

### SEO
- Title: `Gastroenterology Revenue Cycle Management & Billing | Billed
  Right` (doc's exact locked title).
- Meta description: doc's exact locked copy — "Gastroenterology RCM
  since 2006 across office, hospital, endoscopy, colonoscopy, procedures,
  surgery and pathology professional billing."
- Canonical/URL: unchanged.
- Schema: `Service` name/description rewritten to reflect the RCM
  positioning (office/hospital/endoscopy/colonoscopy/procedures/surgery/
  pathology; Prior Authorization/Medical Coding called out as separately
  scoped) instead of the prior NCCI-bundling/infusion-heavy description.
  `FAQPage` replaced with the doc's 10 buyer-intent questions (§20).
  `BreadcrumbList` and org-level `Organization`/`MedicalBusiness`/
  `WebSite` nodes unchanged (shared site-wide schema, out of this page's
  scope). No fake Review or AggregateRating schema added.
- Internal links added/kept: `/services/authorizations/`,
  `/services/medical-coding/`, `/services/credentialing/`,
  `/services/documentation-management/`, `/services/`, `/contact/`,
  `/testimonials/`, `/privacy-policy/`.

## Gastroenterology-Specific QA — First-Time-Right Publish Blockers (doc §27)
- **Experience/Scope:** Since-2006 accurate — PASS. Office/hospital/
  endoscopy/colonoscopy/procedure/surgery professional experience clear
  — PASS. ASC professional-vs-facility distinction clear — PASS.
  Pathology primarily professional-component clear — PASS. Lab
  experience not overstated — PASS (mentioned once, framed as
  supporting/secondary, not a primary GI story). Infusion/biologic
  positioning removed — PASS.
- **EMR:** Only eCW, IMS, AdvancedMD present — PASS. No unsupported
  integration/certification claim — PASS.
- **Services:** Prior Authorization separately scoped — PASS. Medical
  Coding separately scoped — PASS. No clinical-service implication —
  PASS.
- **Proof/KPI:** No composite case — PASS. Testimonial used is authentic
  (already public on `/testimonials/`) but its specialty-page use is
  flagged `NEEDS VERIFICATION`, not fully cleared — see TESTIMONIAL
  section above. Numeric KPI grid removed and replaced with qualitative
  outcomes per the doc's explicit fallback — PASS (no unvalidated number
  displayed).
- **AI:** Every AI statement passes technology → signal → human action →
  financial problem — PASS. No roadmap capability presented as live —
  PASS.
- **Privacy/Conversion:** PHI warning present — PASS. Old "not shared
  with third parties" wording removed — PASS. Privacy Policy linked —
  PASS. Exactly one final conversion section — PASS. Short (4-field) form
  — PASS. Zoho routing and mobile click-to-call **UNCONFIRMED** — cannot
  be verified in this local/static environment (no live Netlify
  Functions/Zoho endpoint), consistent with every prior specialty-page QA
  report.
- **Technical:** Unique H1 — PASS. Title/meta complete — PASS. Canonical
  correct — PASS. Indexability unchanged (`index, follow`) — PASS.
  Schema validates (JSON-LD parsed without error) — PASS. Tag balance
  verified (div/section/main all balanced) — PASS. Sitemap inclusion,
  page-speed/Core Web Vitals, and image compression **not independently
  re-verified** in this pass (image asset itself was not changed). No
  placeholders or internal notes left in the visible copy — PASS.

## Not in scope / not touched
- `netlify/functions/zoho-lead.js`, `build.py`, `templates/nav-template.html`,
  `templates/footer-template.html`, `sitemap.xml`, `pages/testimonials.html`
  — unchanged (the testimonial used was read from, not edited on, the
  testimonials page).
- No other specialty page touched.
- `pages/thank-you/gastroenterology/` — left as-is; shared generic
  thank-you template, not named in the implementation doc's section list.
