# Change Map — Nephrology Specialty Page

`/specialties/nephrology-rcm-services/` (`pages/nephrology-rcm-services.html`)

## Implementation Log

**2026-09-16 — Live-page cleanup & freeze per
`docs/specialty-pages/nephrology/Billed_Right_Nephrology_FINAL_Live_Page_Cleanup_and_Freeze_CORRECTED.md`.**
Targeted revision pass only — no re-rebuild. Cross-referenced every item
against the live page before editing (confirmed each quoted "current"
string matched what was actually on the page). **Note on document
versioning:** the task described this doc as "CORRECTED," implying an
earlier, uncorrected version might exist elsewhere in the project — I
searched the full repository and found no earlier or alternate version
of this feedback anywhere; only this CORRECTED file exists. Flagging
this per the task's own instruction, since there was nothing to
reconcile against.

Changes:

1. **Internal KPI-validation language removed from public copy** (doc §1)
   — removed "Billed Right does not publish invented Nephrology-specific
   performance numbers. Specialty KPI figures will be added here once
   internally validated..." from beneath the qualitative-outcomes KPI
   grid. The qualitative outcome cards themselves are unchanged; no KPI
   placeholder or numbers were added in its place.
2. **"Beyond Office Visits" disclaimer rewritten into customer-facing
   language** (doc §2) — replaced "Billed Right does not perform
   transplant clinical coordination, manage organ allocation, provide
   clinical research administration or manage research protocols,
   provide clinical care, provide pharmacy management, or perform
   Medical Coding as a standard included service. Every statement above
   is tied to revenue-cycle experience." with the doc's exact
   recommended replacement: "Billed Right supports the revenue-cycle
   workflows associated with Nephrology professional services, including
   complex service environments such as transplant- and research-related
   care, within the client's contracted scope. Clinical care, transplant
   coordination and other clinical responsibilities remain with the
   provider organization." Same scope boundary, simplified wording.
3. **Transplant FAQ wording cleaned up** (doc §3) — replaced "Billed
   Right has revenue-cycle experience supporting Nephrology organizations
   that provide transplant-related services. Billed Right's role is
   revenue-cycle focused and does not include clinical transplant
   management unless a separate non-clinical service is explicitly
   contracted and validated." with the doc's exact recommended
   replacement: "Billed Right supports transplant-related professional
   revenue-cycle workflows within the client's contracted scope. Clinical
   transplant coordination and clinical care remain with the provider
   organization." **Applied in both places this text existed** — the
   visible FAQ answer and the matching `FAQPage` JSON-LD schema entry —
   since the doc's own QA checklist (§9) requires "structured data
   matches visible content," and leaving the schema with the old
   "validated" wording while the visible FAQ used the new copy would have
   created exactly the visible/structured-data mismatch the QA is meant
   to catch.
4. **Mid-page Holistic Services CTA removed** (doc §4) — removed the
   "Ask About Holistic Revenue Cycle Services" button from the end of the
   Additional/Holistic Services callout. The scope-clarification callout
   itself (Prior Authorization, Medical Coding, Credentialing,
   Documentation Management list) is unchanged — it now ends after the
   list with no CTA. The page's only conversion path is the final
   "Find Out Where Your Nephrology Revenue Cycle Is Losing Performance"
   section.
5. **Unpublished "Resources & Insights" cards removed** (doc §5) — the
   entire "Nephrology Revenue Cycle Resources" section was removed. All
   three cards ("Nephrology Revenue Cycle Management: Why CKD, ESRD and
   Dialysis Create Different Financial Workflows", "ESRD Monthly
   Capitation Payment...", "Medicare Secondary Payer and ESRD...") had
   specific-sounding titles but linked only to the generic `/blog/` or
   `/resources/` hubs — none is an actual, individually published
   article matching its stated title. Same defect and same fix as
   applied to Gastroenterology's equivalent section in that page's own
   live-feedback pass.
6. **Testimonial star-source verification — flagged, not resolved** (doc
   §6). `docs/claims-register.md` already marks this testimonial's
   general authenticity/approval as **VERIFIED**, sourced from the
   original implementation doc's explicit confirmation ("The existing
   Florida Nephrology Office Manager testimonial is authentic and
   approved"). However, that confirmation does not specifically address
   whether the **original source carried a five-star rating** — a
   narrower question this cleanup doc raises for the first time. I have
   no access to the original review platform/source to confirm this
   specific point, so per the doc's own instruction not to guess in
   either direction, the 5-star display is unchanged pending explicit
   confirmation from Client Success/Legal. This is the same sitewide
   display convention used on every testimonial across the site, not
   something unique to this page.
7. **Confirmed absent, correctly not added** (doc §7) — the doc
   explicitly states an earlier review incorrectly flagged a 24–48 hour
   denial/appeal promise, a same-business-day claims promise, and
   "Reviewed by Billed Right's Nephrology billing team" as present on
   this page. Searched the live page for all three; none exist (the
   "Reviewed by..." rolling-years line was already replaced with the
   evergreen "More than 15 years of Nephrology RCM experience" statement
   during the original rebuild). No changes made — correctly left alone
   per the doc's explicit "do not add these items" instruction.
8. **Section 8 ("Preserve the Strong Live Elements") — verified intact,
   nothing touched.** Confirmed 15+ years experience language, 30+
   provider enterprise proof, eCW/Epic, CKD/ESRD/dialysis-MCP, Medicare/
   payer coordination, procedures/surgery, transplant/research revenue-
   cycle framing, coding education, Medical Coding/Prior Authorization
   scope statements, Intelligent RCM, Data-to-Decisions, four-field form,
   PHI warning, and privacy/consent language are all unchanged from the
   original rebuild.

### Conflicts found
None. Every instruction in this cleanup doc was consistent with the
original implementation doc and the V2 framework — nothing required
choosing between conflicting sources.

### Rule 11 — noted for future specialty builds (not actioned here)
The doc's §11 lists six lessons to carry forward to "Primary Care and all
future specialty MDs" (internal notes never become public copy, words
like "validate"/"publish blocker" stay internal, unpublished resources
never appear as live cards, scope sections shouldn't create competing
CTAs, testimonial stars must match the source, post-build QA must compare
the rendered page against the final MD). These are process rules for
*future* builds, not an instruction to retroactively fix other
already-frozen specialty pages in this pass — no other page was touched,
consistent with this task's explicit scope. (Note: items 2–4 of this list
overlap with lessons already recorded in Gastroenterology's equivalent
cleanup pass from the same review cycle.)

### Freeze
Per the doc's §10, the Nephrology commercial pillar is now frozen
following this cleanup pass, pending the build/push steps below. Future
growth should come from authority content, real proof, eCW/Epic content,
dialysis/MCP content, enterprise Nephrology content, internal linking,
technical SEO, backlinks/PR, and conversion optimization — not further
pillar-page rewrites, absent new verified capabilities/proof or a
material business change.

---

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

## Live-Page Cleanup & Freeze QA (doc §9)
- **Content:** No internal implementation/validation wording visible —
  PASS (removed, items 1–3 above). KPI-validation sentence removed —
  PASS. Transplant scope language customer-facing — PASS. "Beyond Office
  Visits" scope language concise — PASS. No unsupported service
  expansion — PASS. Medical Coding separately scoped — PASS. Prior
  Authorization separately scoped — PASS. Transplant/research language
  stays non-clinical and revenue-cycle focused — PASS. 15+ years accurate
  and unchanged — PASS. 30+ provider enterprise proof remains visible —
  PASS. eCW and Epic remain prominent — PASS. Intelligent RCM remains
  concrete — PASS. Data-to-Decisions remains executive-oriented — PASS.
- **Proof:** Nephrology testimonial source — **UNCONFIRMED** for the
  specific five-star-origin question (see item 6 above); general
  authenticity already VERIFIED in `docs/claims-register.md`. No
  fabricated/composite proof introduced — PASS.
- **Resources:** Every live resource exists / destination published /
  link works — PASS (unpublished section removed entirely rather than
  fixed in place). No future/unpublished resource cards remain — PASS.
- **Conversion:** Holistic Services mid-page CTA removed — PASS. Exactly
  one major final conversion section remains — PASS. Four-field form
  present — PASS. PHI warning present — PASS. Privacy Policy linked —
  PASS. Consent language matches sitewide-approved wording — PASS. Zoho
  lead creation, page/source attribution reaching CRM, assignment/
  notification, and mobile click-to-call — **UNCONFIRMED** — cannot be
  verified in this local/static environment (no live Netlify
  Functions/Zoho endpoint), consistent with every prior specialty-page QA
  report. Chat does not block CTA/form — PASS (verified no layout
  collision).
- **Technical/UX:** One H1 — PASS. Title/meta correct and unchanged —
  PASS. Canonical correct — PASS. Indexable (`index, follow`) — PASS.
  Internal links unaffected by this pass — PASS. Structured data
  (JSON-LD) still parses without error and now matches the visible FAQ
  text exactly (see item 3 above) — PASS. Desktop and mobile layouts
  verified clean via screenshot — PASS. No placeholders, broken links, or
  accidental implementation text remaining — PASS.

## Not in scope / not touched
- `netlify/functions/zoho-lead.js`, `build.py`, `templates/nav-template.html`,
  `templates/footer-template.html`, `sitemap.xml` — unchanged.
- No other specialty page touched.
- `pages/thank-you/nephrology/` — left as-is; shared generic thank-you
  template, not named in the implementation doc's section list.
