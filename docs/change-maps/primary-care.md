# Primary Care — Change Map

## Implementation Log — 2026-09-16: Full rebuild per V4 FINAL First-Time-Right implementation doc

**Source:** `docs/specialty-pages/Primary Care/Billed_Right_Primary_Care_FINAL_First_Time_Right_V4_RCM_SEO_AEO_Enterprise_Implementation.md` (601 lines, read in full)

**Governing standard:** `docs/Billed_Right_Specialty_Page_Framework_V2.md`, `docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`

This was a full rebuild, not a targeted cleanup — the prior live page followed the older CPT/modifier-25-tutorial template (preventive vs. sick visit billing, denial reasons, payer-specific considerations) rather than the V4 enterprise-lead framework. Rebuilt as a 20-section flow per the doc's §33 Final Page Flow.

### Case Study — Priority Specialty Status

Primary Care is treated as a priority specialty per this task's explicit instruction. **Note on priority-specialty list discrepancy:** `docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md` lists the four priority specialties as **Cardiology, Pain Management, Internal Medicine, Behavioral Health** — it does not include Primary Care. The task instruction for this rebuild asserted the four priority specialties are **Cardiology, Primary Care, Pain Management, Behavioral Health**. This is flagged here rather than silently resolved; the guardrails doc was not edited. Whichever list is authoritative, Primary Care's case-study status is reported in full below regardless.

**Status: REAL, VERIFIED, and already live elsewhere on the site — was NOT being used on the specialty page before this rebuild.**

- A real, non-composite Primary Care case study already exists at `/case-studies/primary-care/` and is marked **VERIFIED** in `docs/claims-register.md` (row 53), sourced directly from that published page.
- Client: two-provider Primary Care group, Central Florida, full RCM engagement. Client sought Billed Right after their long-term office manager left unexpectedly, leaving unpaid/denied claims, no reconciliation process and no billing visibility.
- Verified results over 6 months: collection rate 84% → 95%, charges +32%, denials −59%, A/R 31–90 days −51%.
- **Before this rebuild, the live specialty page did not use this real case study at all.** Its "Resources & Insights" section instead linked a card titled "Primary Care Practice Reduces Denials and Recovers Lost Revenue" explicitly described as *"A composite look at how a multi-provider primary care practice tightened wellness visit coding and CCM documentation..."* — a composite/illustrative substitute sitting on the page while a real, verified case study existed and was already published elsewhere on the site. This is exactly the defect doc §18 and §29 ("fake/composite cases") warn against.
- **Fix:** Rebuilt Section 15 ("Real Primary Care Case Study") using the verified facts above, structured per doc §18 as Client Environment → Starting Problem → Billed Right Scope/Action → Verified Results → Executive Meaning, with a "Read the Full Case Study" link to `/case-studies/primary-care/`. Did not copy any case-study figures from memory — verified directly against the published case-study page source before use. Added a disclaimer that results are specific to this client and not a guarantee for any other practice. Added `docs/claims-register.md` note that this case study is now also used on the specialty page (previously homepage-only).

### Testimonial

**Status: No genuine Primary Care-specific testimonial exists — omitted per doc §19.**

- The prior live page displayed a testimonial ("...significant increase in collections since switching to them 8 months ago...") attributed to **"Internal Medicine Physician"** — confirmed against the master `pages/testimonials.html`, where this exact quote is attributed to Internal Medicine, not Primary Care. It was mislabeled/misapplied on the Primary Care page.
- This same testimonial is legitimately and correctly used on `pages/internal-medicine-rcm-services.html` ("Authentic Internal Medicine Client Proof" section), confirming it is Internal Medicine's real testimonial, not Primary Care's.
- No Primary Care-tagged testimonial exists anywhere in `pages/testimonials.html`.
- Per doc §19 ("Use only an authentic, approved, specialty-relevant Primary Care testimonial. If none exists, omit it. The real case study is stronger proof.") — the testimonial section was **omitted entirely**. The real, verified case study (above) is used as the page's proof instead.

### Keep / Rewrite / New / Remove

**Removed (old CPT-tutorial template, replaced by V4 framework):**
- "Common Pain Areas" / "Primary Care Solutions" bullet lists (modifier 25, AWV/preventive visit mechanics)
- "Top Denial Reasons" 5-card grid (CPT/modifier-25 mechanics)
- "Payer-Specific Considerations" paragraph
- "What to Expect" 6-step implementation timeline containing unverified turnaround promises: *"we follow up within 24-48 hours and appeal denied claims on the same timeline"* and *"claims go out under full account management, same business day"* — these specific quantified turnaround claims are not part of any verified Billed Right fact in the V4 doc and were not carried forward
- Numeric KPI grid (97% collections, 20-day A/R reduction, 1% error ratio, <48hr TAT, <1% no-response, 28-day TAT, 20 years experience) — per doc §20 KPI Governance: *"Do not automatically preserve old-page metrics. If unverified, use qualitative language."* None of these figures appear as verified/locked in the V4 doc, so they were not preserved. Replaced with 7 qualitative outcome cards (stronger claim quality, earlier exception identification, disciplined denial follow-up, prioritized A/R, stronger diagnosis-capture review, recurring provider education, clearer financial visibility) — same treatment already applied to Nephrology and Gastroenterology in their live-page feedback passes.
- Mismatched Internal Medicine testimonial (see Testimonial section above)
- "Resources & Insights" 3-card section, including the composite-case-study card described above and two other cards linking to generic `/blog/` and `/resources/` hub URLs for content that doesn't exist yet — same defect pattern found and removed on Gastroenterology/Nephrology. Per doc's V4 Resource Publication Rule (§25): *"Do not show 'coming soon,' placeholder, or future resource cards on the commercial pillar."* Omitted entirely rather than publishing unpublished-content cards.
- "We work with all major EMR" generic claim and the four-EMR grid on Internal Medicine's page — doc §15 is explicit: *"Do not add other EMRs merely for SEO breadth."* Only eClinicalWorks (eCW) is verified for Primary Care.
- "Reviewed by Billed Right's primary care billing team, 18+ years in primary care RCM" attribution line — not a verified fact in the V4 doc.
- Second lead-generation form ("Download Our Brochure") — doc §27 V4 CTA Discipline requires exactly one primary conversion journey with one final major conversion section.

**New (per V4 doc, not previously on the page):**
- Signature FFS + Managed Care section (doc §8) with two parallel workflow visuals: FFS (VERIFY→SUBMIT→MONITOR→RESOLVE→COLLECT→ANALYZE) and Managed Care (CAPTURE→SCRUB→AUDIT→EDUCATE→REVIEW→IMPROVE)
- Managed Care workflow detail section (doc §9)
- Standard Primary Care RCM Model, 10-step (doc §11): VERIFY→CAPTURE→SCRUB→SUBMIT→MONITOR→PRIORITIZE→RESOLVE→POST→ANALYZE→IMPROVE
- Preventive & Chronic Care Context section (doc §12), with explicit disclaimer that Billed Right does not own clinical care-gap closure, disease management, clinical outreach or population-health management
- Quarterly Coding Audits & Provider Education feedback loop (doc §13): CLAIMS→PATTERNS→AUDIT→PROVIDER EDUCATION→STRONGER FUTURE EXECUTION
- Intelligent RCM section (doc §14) with PREVENT→DETECT→PRIORITIZE→AUTOMATE→ACT→LEARN visual and required "AI does not replace experienced Primary Care revenue-cycle professionals" callout
- Data-to-Decisions section (doc §16) with WHAT CHANGED?→WHERE?→WHY?→FINANCIAL IMPACT→ACTION visual
- Enterprise/multi-location scale section (doc §17)
- Real case study section (see above)

**Kept/reused (structurally consistent with prior page and other specialties):**
- Hero pattern, "Our Specialties" mega-link footer, single lead-capture form pattern, FAQ accordion pattern, breadcrumb pattern

### EMR

Only **eClinicalWorks (eCW)** is named, per doc §15 ("Do not add other EMRs merely for SEO breadth"). No partnership/certification/proprietary-integration claim made.

### KPI Governance

No numeric KPI in the V4 doc is locked/verified for Primary Care specifically (unlike, e.g., the exact case-study percentages, which are separately sourced from the published case study page). Per doc §20, used qualitative-only KPI cards site-consistent with the Nephrology/Gastroenterology treatment. Added disclaimer: "Billed Right does not publish invented Primary Care performance numbers. Where a metric is shown, it includes a defined metric, value, unit/time basis and applicable population."

### SEO

- Title: `Primary Care Revenue Cycle Management & Billing | Billed Right` (locked, doc §22)
- Meta description: `Primary Care RCM since 2006 for small to large practices. FFS and managed-care support, coding audits, provider education, eCW expertise and intelligent workflows.` (locked, doc §22)
- URL unchanged: `/specialties/primary-care-rcm-services/`
- Updated OG/Twitter tags to match
- Updated `Service` schema description, added `PrimaryCare` to `MedicalBusiness.medicalSpecialty`, rebuilt `FAQPage` schema to match the new on-page FAQ content (doc §24, verbatim)
- One H1 only: "Primary Care Revenue Cycle Management Services"

### Internal-to-Public Copy Firewall (doc §1)

Checked the rendered page for any internal-implementation language (e.g. "validate with Arun," "placeholder," "internal scope note," "validated/unvalidated"). None found — confirmed via grep against the final HTML. Two "placeholder" string matches found are both CSS `::placeholder` pseudo-selectors, not public copy.

### Guardrails enforced

- No SOC 2 claim
- No invented statistics — case study figures verified against source, KPIs qualitative-only
- No CPT/ICD-code dump (previous page's modifier-25/AWV coding mechanics content removed entirely — that content belonged to the old tutorial-style template, not the V4 enterprise-lead framework)
- No competitor attacks
- Core RCM vs. add-on distinction maintained (Additional/Holistic Services section lists Prior Authorization, Medical Coding, Credentialing, Documentation Management, Contract Renegotiation as separately scoped)
- No claim that Billed Right manages the entire value-based program; no clinical population-health/diagnosis claims; explicit statement "Billed Right does not diagnose patients, does not imply automation creates diagnoses, and does not manage the entire value-based care program"
- One final conversion section only (doc §27 V4 CTA Discipline) — Additional/Holistic Services section has no independent CTA button/link, consistent with the doc's requirement to avoid competing conversion funnels
- No unverified turnaround-time promises (24-48hr, same-business-day) carried forward from the old page
- PHI/privacy line and full consent language included in the lead form per doc §28, verbatim

### Build & Verification

- `python3 build.py` succeeded: 259 pages written, no errors
- JSON-LD schema validated (`json.loads` parse check passed)
- Tag balance confirmed: `div` 234/234, `section` 17/17, `main` 1/1
- Banned-phrase grep passed (only false-positive matches: CSS `::placeholder` selectors, a compliant "not a guarantee" disclaimer sentence, and a CSS comment)
- Required-phrase grep passed (since 2006, eClinicalWorks, multi-provider, multi-location, quarterly coding audits, provider education, managed-care report, Central Florida, 84%, 95%)
- Verified live in-browser via local `http.server`: desktop screenshots of hero, FFS/Managed Care signature section, case study section, FAQ, and final CTA/form all render correctly; no console errors
- Fixed one rendering defect found during in-browser QA: the case study's before/after stat display initially reused `.br-cs-bigstat`/`.br-cs-bigstat-arrow`/`.br-cs-after` classes copied from `pages/case-studies/primary-care/index.html`, which are not defined in this page's own stylesheet — rendered as an unstyled, oversized SVG arrow. Replaced with inline-styled markup using only classes/tokens already defined on this page. Re-verified after fix — renders correctly on desktop and mobile (375×812), no console errors.
- Mobile viewport (375×812) checked at hero and case-study sections: clean layout, no horizontal scroll, no console errors

## QA Checklist Results (doc §30 Publish Blockers)

| Item | Status |
|---|---|
| Since-2006 claim | PASS |
| Small-to-large and multi-location experience | PASS |
| eCW | PASS |
| FFS + managed care distinction | PASS |
| Deeper scrubbing | PASS |
| Accurate diagnosis-capture language | PASS |
| Quarterly audits | PASS |
| Provider education | PASS |
| Quarterly managed-care report review | PASS |
| No full value-based-program ownership claim | PASS |
| Medical Coding/PA boundaries | PASS |
| Real case study retrieved and metrics validated | PASS |
| Composite case removed | PASS |
| Authentic testimonial only if available | PASS (none available — correctly omitted) |
| KPI definition/value/unit/time/population verified | PASS (qualitative-only; no unverified numbers published) |
| Concrete AI claims | PASS |
| One final CTA | PASS |
| PHI/privacy | PASS |
| Zoho | UNCONFIRMED — cannot verify CRM lead routing in a local/static environment |
| Mobile click-to-call | PASS (tel: link present and functional in markup; visually confirmed on mobile viewport) |
| Title/meta/canonical/indexability/sitemap/schema/internal links/images | PASS |
| No placeholders/internal notes | PASS |

**Not confirmed / requires live-environment verification (flagged, not actioned):** Zoho lead creation, CRM routing, and notification/sales-follow-up steps described in doc §28's test path (`Submit → Lead Created/Updated → Source/Page Captured → Owner Assigned → Notification → Sales Follow-Up`) cannot be verified from a static local build.

## Conflicts found

None between this V4 doc and the V2 framework or `BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`, aside from the priority-specialty list discrepancy flagged above (Internal Medicine vs. Primary Care as the 4th priority specialty) — flagged, not resolved, since resolving it is outside this task's scope.

## Freeze

Not committed or pushed per explicit instruction. Build succeeded locally; awaiting explicit authorization to push.

## Not in scope / not touched

No other specialty page was modified in this pass.
