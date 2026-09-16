# Change Map — Nephrology Specialty Page

`/specialties/nephrology-rcm-services/` (`pages/nephrology-rcm-services.html`)

## Implementation Log

**2026-09-16 — Full rebuild per
`docs/specialty-pages/nephrology/Billed_Right_Nephrology_FINAL_First_Time_Right_RCM_SEO_AEO_Implementation.md`
(FINAL — Implementation Source of Truth).**

Rebuilt the page from a CPT/dialysis-code-heavy specialty explainer into a
17-section commercial RCM pillar page following the doc's Final Page Flow
(§36): Hero+Proof, Nephrology Experience/Enterprise Proof, Why Different,
Revenue Leaks, How Billed Right Manages the Revenue Cycle (10-step
workflow), Dialysis & MCP Expertise, Medicare & Payer Coordination,
Procedures/Surgery/Transplant/Complex Services, Intelligent RCM, Coding
Education, EMR (eClinicalWorks & Epic), Data-to-Decisions, KPIs/Outcomes,
Authentic Testimonial, Resources, FAQs, one Final CTA. Applied every
Cumulative Specialty-Page Standard item from the start (single final
conversion section, no artificial "Reviewed by" line, no rolling-year
claims, strict real-proof hierarchy).

### RETAIN
- Established URL (`/specialties/nephrology-rcm-services/`).
- Genuine, doc-confirmed Florida Nephrology Office Manager testimonial —
  kept verbatim, not rewritten. See TESTIMONIAL section below for the
  doc's explicit confirmation.

### REWRITE
- Hero, opening framing, revenue-leak section, denial content, FAQs,
  final CTA — replaced with the doc's locked copy and structure, adapted
  into existing page CSS components (`.br-services-grid`,
  `.br-feature-list`, `.br-tech-grid`, `.br-callout`, `.br-faq-item`).
- Lead form: merged First/Last Name into a single required `name` field,
  removed the "Number of Providers" dropdown, reframed from "Download Our
  Brochure" to "Request a Revenue Cycle Assessment" (doc's exact locked
  primary CTA — deliberately different wording from other specialty
  pages' "Schedule a Revenue Cycle Assessment," per this doc's own
  wording). Form name/`formSource` renamed
  `nephrology-brochure-request`/`nephrology-brochure` →
  `nephrology-assessment-request`/`nephrology-assessment` so
  `zoho-lead.js`'s `isBrochureForm` check no longer mislabels this as a
  brochure-download lead. Consent checkbox and PHI-warning line updated
  to the current sitewide-approved privacy wording (doc §24), matching
  the correction already applied to Internal Medicine and the site's
  published Privacy Policy.
- "Reviewed by Billed Right's nephrology billing team, 18+ years in
  nephrology RCM" replaced with the doc's locked evergreen statement
  (§30): "More than 15 years of Nephrology RCM experience." Per the
  doc's explicit instruction, this was NOT converted into a "since YEAR"
  formulation, since the doc only confirms "more than 15 years," not a
  specific start year.

### NEW — Nephrology-specific major sections (not on any other specialty
page, per the doc's explicit instruction not to make this page look like
Cardiology, Pain Management or Internal Medicine)
- **Dialysis & MCP Expertise** (doc §11) — dedicated specialty-authority
  section explaining ESRD Monthly Capitation Payment revenue-cycle
  complexity conceptually, with no CPT/HCPCS code table (per the doc's
  explicit "Do not publish a large 909xx CPT table" instruction).
- **Medicare & Payer Coordination** (doc §12) — dedicated section on
  ESRD Medicare Secondary Payer coordination, framed as a revenue-cycle
  visibility issue, not legal/compliance advice, with the doc's exact
  executive callout: "In Nephrology, knowing who should pay can be as
  important as knowing what to bill."
- **Procedures / Surgery / Transplant / Complex Services** (doc §13) —
  five-pill visual (Procedures & Surgery, Hospital Services,
  Transplant-Related Revenue, Research-Related Revenue Workflows, Drug/
  Infusion Revenue Where Applicable) with the doc's explicit guardrail
  paragraph verbatim (no transplant clinical coordination, no organ
  allocation, no clinical research administration, no clinical care, no
  pharmacy management, no standard Medical Coding).
- **How Billed Right Manages the Revenue Cycle** — a 10-step workflow
  visual (VERIFY → CAPTURE → SUBMIT → MONITOR → PRIORITIZE → RESOLVE →
  POST → ANALYZE → EDUCATE → IMPROVE), longer than any prior specialty
  page's workflow visual, per the doc's exact specified sequence (§10).
- **Coding Education** (doc §15) — dedicated section keeping the
  boundary explicit between provider coding education (which Billed
  Right provides) and Medical Coding as a service (separately scoped),
  using the doc's exact locked scope statement.

### REMOVE / REDUCE
- All CPT/HCPCS code references (90960–90962, 90935/90937, 90945/90947,
  99213–99215, J0881/J0882, J0885/J0886, Q0136) and the associated
  "Payer-Specific Considerations" coding paragraph and CPT-driven FAQ
  set — removed entirely, consistent with the doc's repeated instruction
  not to build a CPT-code library or dialysis-coding tutorial (§1, §11,
  §30).
- "18+ years in nephrology RCM" / "Reviewed by..." footer line (see
  REWRITE above).
- "Download Our Brochure" as the primary conversion framing (see
  REWRITE above).
- Duplicate ending CTAs — built as exactly **one** final conversion
  section from the start, with Our Specialties moved to its own section
  immediately below and no other major CTA after it.
- Generic "We work with all major EMR" line — replaced with the doc's
  locked two-platform list (see EMR section below).
- **Managed-care positioning entirely absent** — the doc explicitly
  states (§2): "Managed-care positioning is not appropriate for this
  specialty page based on Billed Right's current Nephrology experience."
  No managed-care language of any kind was introduced (unlike Internal
  Medicine, whose doc explicitly called for a managed-care/FFS
  distinction — Nephrology's doc explicitly forbids it). Flagging this
  because it's a meaningful, deliberate divergence between two
  specialty docs that a future reader might otherwise assume was an
  oversight.

### CASE STUDY / PROOF HIERARCHY (doc §19, §31)
Checked `pages/case-studies/` — only Allergy, Cardiology, Credentialing
and Primary Care case studies exist. **No real, approved Nephrology case
study exists in the project.** The prior live page's Resources card
("Nephrology Practice Fixes MCP Billing and Recovers Lost Revenue")
explicitly self-described as "a composite look" — **removed entirely,
with no illustrative/hypothetical replacement**, per the doc's Proof
Hierarchy rule: "Real Nephrology Case Study > Authentic Nephrology
Testimonial > No Case Study." The doc explicitly forbids turning the
verified 30+ provider Epic enterprise client relationship into a "case
study" with invented results — that fact is referenced only in the
Hero, Executive Proof, EMR, and FAQ sections as confirmed enterprise
experience, with no invented financial outcome attached to it anywhere.

**Outcome: no case-study section on the page.** This remains a
confirmed gap — if Billed Right develops a real, approved Nephrology
case study in the future, a dedicated section can be added following
the pattern used for Cardiology's real case study.

### TESTIMONIAL (doc §2, §19)
Unlike every prior specialty rebuild this session, this implementation
doc explicitly confirms the testimonial's approval status as a
**"VERIFIED BILLED RIGHT FACT"** (§2): "The existing Florida Nephrology
Office Manager testimonial is authentic and approved. It may remain on
the page, subject to normal formatting and contextual placement." The
quotation was kept exactly as it appeared on the prior live page, with
no rewriting — including retaining "Account Managers" in the client's
own words, since the doc explicitly says "Do not rewrite the quotation
to make it stronger." Attribution updated from "Nephrology Office
Manager, FL" to the doc's suggested context label "Office Manager |
Nephrology Practice | Florida" (rendered as "Office Manager, Nephrology
Practice, Florida"), matching the contextual attribution format used on
prior specialty pages.

Added a new row to `docs/claims-register.md` for governance consistency
(this testimonial had never been logged there) — marked **VERIFIED**,
not `NEEDS VERIFICATION`, since this is the first specialty-page doc in
this series to explicitly assert authenticity/approval as a stated fact
rather than a conditional ("if still validated"/"if approved"). This is
a stronger sign-off than any other specialty-page testimonial's current
register status.

### EMR (doc §16, §31)
Locked list used exactly as specified: **eClinicalWorks (eCW)** and
**Epic** only — no Athena, AdvancedMD, IMS, or CareCloud added, per the
doc's explicit instruction not to add other EMRs for SEO padding. No
certification, partnership, or proprietary-integration claim made for
either platform.

### KPI / RESULTS SECTION (doc §18) — deliberate deviation from prior
specialty pages, flagged clearly
Every prior specialty rebuild this session (Psychiatry, Cardiology, Pain
Management, Internal Medicine) kept the existing shared numeric KPI grid
(97% collections, 20-day A/R reduction, 1% error ratio, <48hr TAT, <1%
no-response, 28-day payment TAT) unchanged, reasoning that these are
already-published, company-wide figures reused consistently sitewide.

**This doc explicitly overrides that precedent for Nephrology.** §18
states: "If the current page contains numbers, they are not
automatically approved simply because they are already published,"
requires Arun/internal-data-owner validation of metric definition +
value + unit/time basis before display, and gives an explicit fallback:
**"Until Validated: Use qualitative outcome categories rather than
invented numbers."** Since no such validation occurred in this session,
the numeric KPI grid was **removed and replaced with the doc's exact
seven qualitative outcome categories** (stronger claim quality, earlier
identification of denials and exceptions, disciplined A/R follow-up,
improved financial visibility, better prioritization of revenue-cycle
work, fewer recurring operational problems, clearer executive decision
support), with a note that specialty-specific KPI figures will be added
once validated.

**Action item for Raul/Arun:** if the shared KPI figures are in fact
already approved for Nephrology specifically (not just company-wide),
provide that confirmation and the numeric grid can be restored to match
the other specialty pages' treatment.

### AI / GUARDRAILS
- No "revolutionary AI," "cutting-edge AI," "zero-touch RCM," "fully
  autonomous billing," "AI eliminates denials," "guaranteed clean
  claims," or "guaranteed faster payment" language used.
- No future-roadmap capability presented as live.
- Every Intelligent RCM capability (claim-quality automation,
  eligibility/coverage automation, denial classification/pattern
  detection, A/R prioritization, authorization exception visibility,
  Data-to-Decisions) states technology → signal → human action →
  revenue problem, passing the doc's four-question AI Quality Test.
- No SOC 2 claim, invented certification, guaranteed collections,
  guaranteed denial reduction, guaranteed transplant reimbursement,
  clinical advice, or legal advice anywhere on the page.
- No competitor attacks.

### SEO
- Title: `Nephrology Revenue Cycle Management & Billing | Billed Right`
  (doc's exact locked title).
- Meta description: doc's exact locked copy — "Nephrology RCM for CKD,
  ESRD, dialysis/MCP, procedures, transplant-related services and
  complex payer workflows. 15+ years of Nephrology experience."
- Canonical/URL: unchanged.
- Schema: `Service` name/description rewritten to reflect the RCM
  positioning (CKD/ESRD/dialysis-MCP, procedures, transplant-related
  services, Medicare/payer coordination, enterprise scale; Prior
  Authorization/Medical Coding called out as separately scoped) instead
  of the prior CPT/drug-code-heavy description. `FAQPage` replaced with
  the doc's 10 buyer-intent questions (§22). `BreadcrumbList` and
  org-level `Organization`/`MedicalBusiness`/`WebSite` nodes unchanged
  (shared site-wide schema, out of this page's scope). No fake Review,
  AggregateRating, or fabricated star-rating schema added — the doc
  explicitly warns the authentic testimonial does not automatically
  justify AggregateRating schema (§27), and none was added.
- Internal links added/kept: `/services/authorizations/`,
  `/services/medical-coding/`, `/services/credentialing/`,
  `/services/documentation-management/`, `/services/`, `/contact/`,
  `/testimonials/`, `/privacy-policy/`.

## Nephrology-Specific QA — First-Time-Right Publish Blockers (doc §31)
- **Proof:** Florida testimonial confirmed and copied exactly — PASS.
  No composite case study remains — PASS. 30+ provider enterprise
  client referenced only with confirmed facts, no invented financial
  result — PASS.
- **EMR:** Only eCW and Epic presented — PASS. No unsupported
  integration/certification claims — PASS.
- **Scope:** Prior Authorization clearly separately scoped — PASS.
  Medical Coding clearly separately scoped — PASS. Coding education
  accurately described — PASS. Transplant/research language limited to
  RCM experience — PASS. No managed-care language — PASS.
- **KPI:** No unvalidated number displayed — PASS (numeric grid removed
  and replaced with qualitative categories per doc's explicit fallback;
  see KPI section above for the flagged deviation from prior pages).
- **AI:** Every technology statement passes the four-question AI
  Quality Test — PASS. No roadmap feature presented as live — PASS.
  Human action remains visible — PASS.
- **Privacy:** PHI warning present on form — PASS. Old "not shared with
  third parties" wording removed — PASS. Privacy Policy linked — PASS.
  Form wording matches current sitewide-approved language — PASS.
- **Conversion:** Exactly one final major conversion section — PASS.
  Short (4-field) form inside it — PASS. Zoho routing and mobile
  click-to-call **UNCONFIRMED** — cannot be verified in this
  local/static environment (no live Netlify Functions/Zoho endpoint),
  consistent with every prior specialty-page QA report.
- **Technical:** H1 present and unique — PASS. Title/meta complete —
  PASS. Canonical correct — PASS. No noindex — PASS (page uses
  `index, follow`, unchanged from before). Schema validates (JSON-LD
  parsed without error) — PASS. Tag balance verified (div/section/main
  all balanced) — PASS. Sitemap inclusion, page-speed/Core Web Vitals,
  and image compression **not independently re-verified** in this pass
  (image asset itself was not changed).

## Not in scope / not touched
- `netlify/functions/zoho-lead.js`, `build.py`, `templates/nav-template.html`,
  `templates/footer-template.html`, `sitemap.xml` — unchanged.
- No other specialty page touched.
- `pages/thank-you/nephrology/` — left as-is; shared generic thank-you
  template, not named in the implementation doc's section list.
