# Vascular Surgery — Change Map

## Implementation Log — 2026-09-16: Full rebuild per V4 FINAL First-Time-Right implementation doc

**Source:** `docs/specialty-pages/Vascular Surgery/Billed_Right_Vascular_Surgery_FINAL_First_Time_Right_V4_RCM_SEO_AEO_Enterprise_Implementation.md` (1,108 lines, read in full)

**Governing standard:** `docs/specialty-pages/Billed_Right_Specialty_Page_Framework_V2.md`, `docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`

This was a full rebuild, not a targeted cleanup. The prior live page followed the older CPT/modifier-tutorial template (open vs. endovascular approach codes, global surgery period modifiers, bilateral/assistant-surgeon modifiers) rather than the V4 enterprise-lead framework. Rebuilt as a 21-section flow per the doc's §40 Final Page Flow.

### Case Study

**Status: No case study exists, and this document does not supply one.**

- No `pages/case-studies/vascular-surgery/` (or similarly named) directory exists anywhere in the repo — confirmed by directory listing.
- No claims-register entry (prior to this session) references any Vascular Surgery case study, composite or otherwise.
- The prior live page's "Resources & Insights" section carried a card titled "Vascular Surgery Practice Reduces Denials and Recovers Lost Revenue," explicitly self-described as *"A composite look at how a multi-provider vascular surgery practice tightened approach coding and global period billing..."* — a composite case study, exactly what doc §18 instructs against: *"Do not use composite case studies, hypothetical results, illustrative vascular groups or fabricated 'representative outcomes.'"*
- **Fix:** The composite case-study card was removed entirely (along with the rest of the old "Resources & Insights" section — see Removed, below). No case-study section was rebuilt in its place, per the doc's proof hierarchy (§18): Real Case Study > Real Current-Client Proof > Authentic Testimonial > No Case Study. Since no real case study or testimonial exists (see below), the page relies on the doc's next tier: real current-client proof.

### Testimonial

**Status: No genuine Vascular Surgery testimonial currently exists — despite the implementation doc's own assumption that one does.**

- The doc (§2, §17) states: *"If the current Vascular testimonial is live, it is considered accurate... Before reusing it, verify exact wording, source, reviewer/client role, permission/public-use status and any star rating shown."* This phrasing assumes a live testimonial exists.
- Checked both the prior live specialty page (`pages/vascular-surgery-rcm-services.html`, pre-rebuild) and the master `pages/testimonials.html` (searched for `data-cat="vascular"` and any Vascular Surgery-tagged card): **neither contains a Vascular Surgery testimonial.** The prior live page had no testimonial section of any kind — it went directly from the KPI grid to the FAQ section.
- This is a factual discrepancy between the doc's assumption and the actual state of the codebase, being reported per this task's explicit instruction to report if none exists rather than silently fabricating one. No testimonial was invented to fill this gap, consistent with doc §34's explicit ban on "fake testimonials."
- Per the doc's own proof hierarchy (§18), with no case study and no testimonial available, the page relies on **real current-client proof** (below) as its proof mechanism — the doc itself explicitly sanctions this: *"If a real case study is not available, current-client proof plus authentic testimonial is sufficient"* (and by extension, current-client proof alone when no testimonial exists either).

### Real Current-Client Proof (doc §2, §16)

The doc names three current vascular/cardiovascular clients as verified facts: Heart, Vascular & Metabolic Institute; Heart & Vascular Clinic of Clermont; Southern Vascular of Panama City — with the explicit caution that these organizations are not all identical in specialty composition and must not be mislabeled as pure Vascular Surgery practices, and that "current-client names [should be used] only where Billed Right has approved public use." The doc's own §16 "Public Proof Direction" is conditional: *"If all three names are approved for public use, create a restrained proof section..."*

Since no separate confirmation of public-use approval for these three specific organization names exists anywhere in the repo (no claims-register entry, no other doc reference), I did **not** name any of the three organizations on the public page. Instead, I used the doc's own suggested generic, restrained language verbatim from §16: *"Current vascular experience spans dedicated vascular-surgery organizations and broader cardiovascular/interventional environments, including multi-location groups and procedure-heavy practices."* This satisfies the doc's requirement for real current-client proof while erring toward the safer, non-name-specific option the doc itself offers, consistent with its own "do not mislabel" and "only if approved" guardrails. If leadership later confirms public-use approval for the three specific organization names, this section can be updated to name them.

### Keep / Rewrite / New / Remove

**Removed (old CPT/modifier-tutorial template, replaced by V4 framework):**
- "Common Pain Areas" / "Vascular Surgery Solutions" bullet lists (open vs. endovascular approach mechanics, global period mechanics)
- "Top Denial Reasons" 5-card grid (approach code selection, modifier 78/50/80 mechanics)
- "Payer-Specific Considerations" paragraph naming specific CPT codes (EVAR 33880-33886, peripheral interventions 37220-37235, carotid endarterectomy 35301, duplex ultrasound 93971) and global-period day-count rules
- "What to Expect" 6-step implementation timeline containing unrevalidated turnaround promises: *"we will follow up within 24-48 hours and appeal any denied claims within the same timeframe"* and *"claims go out under full account management, same business day"* — doc §34 explicitly forbids "unsupported 24–48-hour SLA" and "same-business-day universal promise," and neither is a verified fact in this doc
- Numeric KPI grid (97% collections, 20-day A/R reduction, 1% error ratio, <48hr TAT, <1% no-response, 28-day TAT, **"20 years of experience"**) — doc §34/§35 explicitly forbid "unsupported '20 years' Vascular claim" (the verified figure is since 2010, i.e. ~15-16 years) and require every KPI to be independently validated. None of these figures are validated for Vascular Surgery in this doc, so none were preserved. Replaced with 6 qualitative outcome cards, consistent with every other specialty rebuilt this session.
- "We work with all major EMR" generic claim — doc §14/§34 explicit: only eClinicalWorks (eCW), athenahealth and IMS are verified for Vascular; "Do not use 'all major EMRs.'"
- "Reviewed by Billed Right's vascular surgery billing team — 18+ years in vascular surgery RCM" authority line — not a verified fact in this doc, and inconsistent with the doc's "since 2010" positioning (18+ years would imply since ~2008, not the verified 2010 start)
- CPT/modifier FAQs (global surgery period mechanics, open vs. endovascular coding, bilateral modifier 50, assistant surgeon modifier 80, modifier 78 return-to-OR) — replaced by the doc's own locked FAQ set (§24), which contains no CPT/modifier content
- Composite case-study card and the other two "Resources & Insights" cards (linking to generic `/blog/` and `/resources/` hub URLs for content that doesn't exist yet) — doc §26 V4 Resource Publication Rule, same treatment as every other specialty rebuilt this session
- Second lead-generation form ("Download Our Brochure") — doc §30 requires exactly one final conversion section with no second major CTA block
- "Since 2006" claim — corrected to **since 2010** per doc §2/§34, the single most load-bearing factual correction in this rebuild

**New (per V4 doc, not previously on the page):**
- Cath Lab / Procedure Billing section (doc §8) — the doc's own "core differentiator" — with PROCEDURE→CAPTURE→SCRUB→SUBMIT→MONITOR→RESOLVE→RECONCILE→ANALYZE visual and an explicit scope-boundary disclaimer (Billed Right does not operate the cath lab, perform clinical documentation, determine medical necessity, manage clinical scheduling or manage hospital facility billing)
- Arterial + Venous/Endovascular Revenue-Cycle Experience section (doc §9), deliberately using broad executive language rather than a procedure-code list
- Office + Hospital Professional Billing section (doc §10), using "professional billing" language only, with an explicit scope callout
- Prior Authorization scope-clarification section (doc §11), explicitly separately scoped, no guarantee of approval
- Coding Education section (doc §12) with CLAIMS→PATTERNS→REVIEW→PROVIDER EDUCATION→STRONGER EXECUTION visual
- Standard RCM workflow, 10-step (doc §7): VERIFY→CAPTURE→SCRUB→SUBMIT→MONITOR→PRIORITIZE→RESOLVE→POST→ANALYZE→IMPROVE
- Intelligent RCM section (doc §13) with PREVENT→DETECT→PRIORITIZE→AUTOMATE→ACT→LEARN visual and required "AI does not replace experienced Vascular revenue-cycle professionals" callout
- Data-to-Decisions section (doc §15) with WHAT CHANGED?→WHERE?→WHY?→FINANCIAL IMPACT→ACTION visual
- Current-Client / Multi-Location Proof section (doc §16) — see above

**Kept/reused (structurally consistent with prior page and other specialties):**
- Hero pattern, "Our Specialties" mega-link footer, single lead-capture form pattern, FAQ accordion pattern, breadcrumb pattern

### EMR

All three verified platforms named: **eClinicalWorks (eCW), athenahealth, and IMS** (doc §14). No partnership/certification/proprietary-integration claim made.

### KPI Governance

No numeric KPI in the V4 doc is locked/verified for Vascular Surgery. Per doc §19, used qualitative-only KPI cards (stronger claim quality, disciplined denial follow-up, prioritized high-value A/R, more consistent procedure billing, clearer multi-location visibility, stronger executive reporting), consistent with every other specialty rebuilt this session. Added disclaimer: "Where a metric is shown, it includes a defined metric, value, unit/time basis, applicable population and source" — forward-looking public-copy phrasing, not an internal-sounding disclaimer, per doc §19's explicit instruction that internal language explaining why metrics are missing must not appear on the public page.

### SEO

- Title: `Vascular Surgery Revenue Cycle Management & Billing | Billed Right` (locked, doc §22)
- Meta description: `Vascular RCM since 2010 with cath-lab and procedure billing, office and hospital professional billing, arterial/venous expertise and specialty EMR experience.` (locked, doc §22)
- URL unchanged: `/specialties/vascular-surgery-rcm-services/`
- Updated OG/Twitter tags to match
- Updated `Service` schema description, added `VascularSurgery` to `MedicalBusiness.medicalSpecialty`, rebuilt `FAQPage` schema to match the new on-page FAQ content (doc §24, verbatim)
- One H1 only: "Vascular Surgery Revenue Cycle Management Services"

### Internal-to-Public Copy Firewall (doc §33)

Checked the rendered page for internal-implementation language (e.g. "current client names approved?", "verify testimonial source," "publish blocker," "do not mislabel," "unverified," "future content idea," "if approved for public use"). None found — confirmed via grep against the final HTML, and confirmed the three specific client organization names do not appear anywhere on the page. The only "placeholder" and "unverified" matches are a CSS `::placeholder` pseudo-selector and a compliant guardrail sentence ("does not promise unverified dashboard functionality"), respectively. Developer-facing HTML source comments marking omitted sections are not rendered text, consistent with the convention used throughout this session.

### Guardrails enforced

- No SOC 2 claim
- No invented statistics — no fabricated testimonial or case study; current-client proof kept generic pending public-use approval confirmation
- No CPT/modifier dump (the prior page's entire approach-code/global-period/modifier-mechanics content was removed; that content belonged to the old tutorial-style template, not the V4 enterprise-lead framework)
- No competitor attacks
- Core RCM vs. add-on distinction maintained — Prior Authorization and Medical Coding both explicitly presented as separately scoped, never implied as core RCM
- No hospital facility billing overclaim — "professional billing" language used throughout, with explicit scope disclaimers
- No unverified turnaround-time promises (24-48hr, same-business-day) carried forward from the old page
- No client mislabeling — no specific client organization named without confirmed public-use approval
- One final conversion section only (doc §30) — no competing CTA blocks
- PHI/privacy line and full consent language included in the lead form per doc §31, verbatim

### Build & Verification

- `python3 build.py` succeeded: 259 pages written, no errors
- JSON-LD schema validated (`json.loads` parse check passed)
- Tag balance confirmed: `div` 189/189, `section` 17/17, `main` 1/1
- All CSS classes used in the new markup confirmed already defined in this page's own stylesheet
- Banned-phrase grep passed (remaining matches are all false positives: the sitewide Organization schema's own 2006 founding date, a developer-facing HTML comment, CSS `::placeholder`, and compliant guardrail disclaimers — "authorization approval is never guaranteed" and "does not promise unverified dashboard functionality")
- Confirmed via grep that none of the three specific client organization names (Heart, Vascular & Metabolic Institute; Heart & Vascular Clinic of Clermont; Southern Vascular of Panama City) appear anywhere on the rebuilt page
- Required-phrase grep passed (since 2010, eClinicalWorks, athenahealth, IMS)
- Verified live in-browser via local `http.server`: desktop screenshots of hero, current-client proof section, qualitative KPI section, and final CTA/form all render correctly; no console errors
- Mobile viewport (375×812) checked: clean layout, no horizontal scroll, no console errors

## QA Checklist Results (doc §35 First-Time-Right Publish Blockers)

| Item | Status |
|---|---|
| Since 2010 | PASS |
| No "since 2006" | PASS |
| Current client names used only if public-use approved | PASS (no specific client names published, pending confirmed approval) |
| Client specialty labels accurate | PASS (no client-specific labels published) |
| Cath-lab/procedure billing accurate | PASS |
| Arterial/venous/endovascular scope accurate | PASS |
| Office professional billing accurate | PASS |
| Hospital professional billing accurate | PASS |
| No facility overclaim | PASS |
| PA separately scoped | PASS |
| Medical Coding separately scoped | PASS |
| Coding education accurate | PASS |
| eCW | PASS |
| athenahealth | PASS |
| IMS | PASS |
| No unsupported EMRs | PASS |
| No "all major EMRs" | PASS |
| Current-client proof accurate | PASS (generic, restrained framing per doc's own fallback language) |
| Testimonial source verified | N/A — no testimonial exists (reported, not fabricated) |
| Star presentation matches source | N/A — no testimonial exists |
| No composite case | PASS |
| Every metric fully validated | PASS (qualitative-only; no unvalidated numeric metric published) |
| Old-template KPI/SLA claims removed if unsupported | PASS |
| No internal KPI notes public | PASS |
| Technology → signal → human action → financial problem | PASS |
| No roadmap capability presented as live | PASS |
| Exactly one final conversion section | PASS |
| Four-field form | PASS (Name, Work Email, Phone, Practice/Organization) |
| PHI warning | PASS |
| Privacy link | PASS |
| Approved consent | PASS |
| Zoho routing | UNCONFIRMED — cannot verify CRM lead routing in a local/static environment |
| Mobile click-to-call | PASS (tel: link present and functional in markup; visually confirmed on mobile viewport) |
| One H1 | PASS |
| Title/meta | PASS |
| Canonical | PASS |
| Indexability | PASS (`robots: index, follow` unchanged) |
| Internal links | PASS |
| Schema | PASS |
| Mobile | PASS |
| No internal notes | PASS |
| No unpublished resource cards | PASS |
| No broken links | PASS (all links point to existing pages: `/privacy-policy/`, `tel:`, in-page anchor, specialty mega-links) |

**Not confirmed / requires action outside this rebuild:**
- Zoho lead creation, CRM routing, and notification/sales-follow-up steps (doc §31's test path) cannot be verified from a static local build.
- **Whether the three named current clients (Heart, Vascular & Metabolic Institute; Heart & Vascular Clinic of Clermont; Southern Vascular of Panama City) are approved for public naming on the website** — this rebuild deliberately did not name them, using the doc's own generic fallback language instead, since no separate confirmation of public-use approval exists in the repo. If approval is later confirmed, the Current-Client Proof section (§14 in the page flow) can be updated to name them specifically, per doc §16.
- **Whether a genuine Vascular Surgery testimonial exists anywhere outside this codebase** — the implementation doc assumes one is currently live, but none was found on the specialty page or the master testimonials page. Recommend confirming with marketing/leadership whether a Vascular Surgery testimonial exists elsewhere (e.g., not yet added to the site) before concluding none exists at all.

## Conflicts found

The implementation doc's own factual assumption (§2, §17: "If the current Vascular testimonial is live, it is considered accurate") does not match the actual repository state (no such testimonial exists on the live page or master testimonials page). Flagged above rather than silently resolved or fabricated.

## Freeze

Per doc §38 Freeze Criteria and §41, this page is ready for freeze once live QA (Zoho/CRM routing) is confirmed post-deploy, and once leadership confirms (a) whether the three named clients may be published by name and (b) whether a genuine Vascular Surgery testimonial exists to add. Pushed to GitHub per explicit instruction with commit message "Rebuild Vascular Surgery specialty page per V2 framework spec."

## Not in scope / not touched

No other specialty page was modified in this pass.
