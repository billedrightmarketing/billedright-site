# Urgent Care — Change Map

## Implementation Log — 2026-09-16: Full rebuild per V4 FINAL First-Time-Right implementation doc

**Source:** `docs/specialty-pages/Urgent Care/Billed_Right_Urgent_Care_FINAL_First_Time_Right_V4_RCM_SEO_AEO_Enterprise_Implementation.md` (1,219 lines, read in full)

**Governing standard:** `docs/specialty-pages/Billed_Right_Specialty_Page_Framework_V2.md`, `docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`

This was a full rebuild, not a targeted cleanup. The prior live page followed the older CPT/S-code-tutorial template (facility codes S9083/S9088, E/M level guidelines, laceration repair and X-ray CPT codes) rather than the V4 enterprise-lead framework. Rebuilt as a 20-section flow per the doc's §38 Final Page Flow.

### Case Study

**Status: No case study exists, and this document does not supply one.**

- No `pages/case-studies/urgent-care/` directory exists anywhere in the repo — confirmed by directory listing.
- No claims-register entry (prior to this session) references any Urgent Care case study, composite or otherwise.
- The prior live page's "Resources & Insights" section carried a card titled "Urgent Care Practice Reduces Denials and Recovers Lost Revenue," explicitly self-described as *"A composite look at how a multi-site urgent care practice tightened facility coding and eligibility verification..."* — a composite case study, exactly what doc §16 instructs against: *"Do not use a composite/illustrative case study... If there is no approved real case study, use the verified testimonial and historical experience."*
- **Fix:** The composite case-study card was removed entirely (along with the rest of the old "Resources & Insights" section — see Removed, below). No case-study section was rebuilt in its place, per doc §38 item 16 ("Real case study only if later available") and the doc's proof hierarchy: Real Case Study > Real Testimonial > No Case Study. The real testimonial (below) stands as the page's proof.

### Testimonial

**Status: Real, kept — but corrected to the full, exact wording from the source, since the version previously live on the specialty page had been silently shortened.**

- The doc (§2, §16) confirms: *"The current live Urgent Care testimonial is real... Retain only after source, exact wording and any star presentation are verified."*
- Two genuine Urgent Care testimonials exist on the master `pages/testimonials.html` (both tagged `data-cat="urgent"`): (1) "Practice Administrator of Urgent Care, TN" — a detailed quote about account-manager support and reporting transparency, and (2) "Urgent Care Provider, TN" — a shorter, more generic quote.
- The prior live specialty page used testimonial (1), but **not verbatim**: it dropped two full sentences from the middle of the quote (*"Our AM is a true gem and gift to any client account she manages. Her knowledge and suggestions aid me and my clinic in many ways. I would never have been able to execute a few items without her help. I was not in my current role before they chose to use Billed Right..."*) and altered the attribution format by prepending an em dash. Doing the doc's own required verification step — comparing the specialty page's version against the master source — surfaced this discrepancy directly.
- **Fix:** Restored the full, unabridged quote and standard attribution format ("Practice Administrator of Urgent Care, TN," no em dash prefix) to match `/testimonials/` exactly, consistent with the doc's explicit instruction to verify exact wording before reuse. Star display (5 stars) matches the source page's existing presentation — not artificially added.
- Added a `docs/claims-register.md` entry (previously no Urgent Care testimonial row existed in the register), noting both the verification and the correction.

### Keep / Rewrite / New / Remove

**Removed (old CPT/S-code-tutorial template, replaced by V4 framework):**
- "Common Pain Areas" / "Urgent Care Solutions" bullet lists (facility vs. professional fee mechanics)
- "Top Denial Reasons" 5-card grid (S9083/S9088 vs. E/M code selection, MDM documentation, duplicate claims)
- "Payer-Specific Considerations" paragraph naming specific facility codes and Medicare/Medicaid coverage rules
- "What to Expect" 6-step implementation timeline containing unrevalidated turnaround promises: *"we will follow up within 24-48 hours and appeal any denied claims within the same timeframe"* and *"claims go out under full account management, same business day"* — doc §32 explicitly lists both as "Do Not Publish" ("24–48-hour universal SLA," "same-business-day universal promise"), and neither is a verified fact in this doc
- Numeric KPI grid (97% collections, 20-day A/R reduction, 1% error ratio, <48hr TAT, <1% no-response, 28-day TAT, **"20 years of experience"**) — doc §32/§33 explicitly forbid an unsupported KPI block and require every metric to be independently validated. None of these figures are validated for Urgent Care in this doc, so none were preserved. Replaced with 6 qualitative outcome cards, consistent with every other specialty rebuilt this session.
- "We work with all major EMR" generic claim — doc §13/§32 explicit: only eClinicalWorks (eCW), IMS and athenahealth are verified for Urgent Care; "Do not use 'all major EMRs.'"
- "Reviewed by Billed Right's urgent care billing team — 18+ years in urgent care RCM" authority line — not a verified fact in this doc, and inconsistent with the doc's "since 2010" positioning (18+ years would imply since ~2008, not the verified 2010 start).
- CPT-code FAQs (S9083/S9088 selection, E/M level guidelines, Medicare S-code exclusion, split billing mechanics) — replaced by the doc's own locked FAQ set (§22), which contains no CPT/S-code content
- Composite case-study card and the other two "Resources & Insights" cards (linking to generic `/blog/` and `/resources/` hub URLs for content that doesn't exist yet) — doc §24 V4 Resource Publication Rule, same treatment as every other specialty rebuilt this session
- Second lead-generation form ("Download Our Brochure") — doc §28 requires exactly one final conversion section with no second major CTA block
- "Since 2006" claim — corrected to **since 2010** per doc §2/§32, the second most load-bearing factual correction in this rebuild after the current-client-base issue below

**New (per V4 doc, not previously on the page):**
- Walk-In Verification section (doc §8) — the doc's own "core differentiator" — with WALK-IN→VERIFY→FLAG EXCEPTION→SERVICE→CLAIM→FOLLOW-UP visual and an explicit guardrail against promising a universal verification-turnaround SLA
- Facility-Style + Professional Billing section (doc §9) — the doc's own "signature section" — with PAYER/PLAN→BILLING MODEL→CLAIM LOGIC→SUBMIT→MONITOR→RESOLVE visual
- Workers' Compensation + Auto Liability section (doc §10), presented as a supporting differentiator rather than the page's entire identity, per the doc's explicit instruction
- Coding Knowledge + Provider Education section (doc §11) with CLAIMS→PATTERNS→REVIEW→PROVIDER EDUCATION→STRONGER EXECUTION visual
- Standard RCM workflow, 10-step (doc §7): VERIFY→CAPTURE→SCRUB→SUBMIT→MONITOR→PRIORITIZE→RESOLVE→POST→ANALYZE→IMPROVE
- Intelligent RCM section (doc §12) with PREVENT→DETECT→PRIORITIZE→AUTOMATE→ACT→LEARN visual and required "AI does not replace experienced Urgent Care revenue-cycle professionals" callout
- Data-to-Decisions section (doc §14) with WHAT CHANGED?→WHERE?→WHY?→FINANCIAL IMPACT→ACTION visual
- Multi-Location / Scale Positioning section (doc §15), using the doc's exact recommended historical-framing language

**Kept/reused (structurally consistent with prior page and other specialties):**
- Hero pattern, "Our Specialties" mega-link footer, single lead-capture form pattern, FAQ accordion pattern, breadcrumb pattern
- Real testimonial (see above, corrected)

### No Active Current-Client Implication (doc §1, §2, §15, §31)

This is the single most distinctive instruction in this doc relative to every other specialty rebuilt this session: **Billed Right currently has no active Urgent Care clients**, and this internal fact must never surface as customer-facing copy, while the substantial *historical* experience since 2010 is entirely fair to lead with. Checked the rebuilt page for every phrase the doc explicitly bans — "our current Urgent Care clients," "today we support Urgent Care groups," "our Urgent Care client base," "trusted by current Urgent Care organizations," "we currently have no Urgent Care clients," "historically only," "current-client guardrail" — none appear anywhere (confirmed via grep). Every experience claim on the page uses historical or capability-based framing ("has supported," "has experience," "since 2010," "historically has supported multi-location Urgent Care groups") rather than present-tense client-base language. No current client count is disclosed.

### EMR

All three verified platforms named: **eClinicalWorks (eCW), IMS, and athenahealth** (doc §13). No partnership/certification/proprietary-integration claim made. No other EMRs added despite the doc noting broader (unverified) experience may exist.

### KPI Governance

No numeric KPI in the V4 doc is locked/verified for Urgent Care. Per doc §17, used qualitative-only KPI cards (stronger walk-in verification, fewer preventable claim issues, disciplined denial management, prioritized A/R, more consistent multi-location execution, clearer executive visibility), consistent with every other specialty rebuilt this session. Added disclaimer: "Where a metric is shown, it includes a defined metric, value, unit/time basis, applicable population and source" — forward-looking public-copy phrasing, not an internal-sounding disclaimer, per doc §17's explicit instruction that "Billed Right does not publish invented Urgent Care numbers"-style language must not appear on the public page.

### SEO

- Title: `Urgent Care Revenue Cycle Management & Billing | Billed Right` (locked, doc §20)
- Meta description: `Urgent Care RCM since 2010 with walk-in verification, facility and professional billing, Workers' Comp and auto claims, multi-location experience and specialty EMR expertise.` (locked, doc §20)
- URL unchanged: `/specialties/urgent-care-rcm-services/`
- Updated OG/Twitter tags to match
- Updated `Service` schema description, added `UrgentCare` to `MedicalBusiness.medicalSpecialty`, rebuilt `FAQPage` schema to match the new on-page FAQ content (doc §22, verbatim)
- One H1 only: "Urgent Care Revenue Cycle Management Services"

### Internal-to-Public Copy Firewall (doc §31)

Checked the rendered page for internal-implementation language (e.g. "we currently have no Urgent Care clients," "historically only," "verify with team," "publish blocker," "unverified," "do not claim," "future content idea," "current-client guardrail"). None found — confirmed via grep against the final HTML. The only "placeholder" and "unverified" matches are a CSS `::placeholder` pseudo-selector and a compliant guardrail sentence ("does not promise unverified dashboard functionality"), respectively. Developer-facing HTML source comments marking omitted sections are not rendered text, consistent with the convention used throughout this session.

### Guardrails enforced

- No SOC 2 claim
- No invented statistics — testimonial verified and corrected against source, KPIs qualitative-only
- No CPT/S-code dump (the prior page's entire facility-code/E-M-level/CPT-mechanics content was removed; that content belonged to the old tutorial-style template, not the V4 enterprise-lead framework)
- No competitor attacks
- Core RCM vs. add-on distinction maintained — Medical Coding and Prior Authorization/Credentialing all explicitly presented as separately scoped or supporting, never implied as core RCM
- No unverified turnaround-time promises (24-48hr, same-business-day, universal verification SLA) carried forward from the old page
- No active-current-Urgent-Care-client implication anywhere on the page (the most important guardrail in this specific doc)
- One final conversion section only (doc §28) — no competing CTA blocks
- PHI/privacy line and full consent language included in the lead form per doc §29, verbatim

### Build & Verification

- `python3 build.py` succeeded: 259 pages written, no errors
- JSON-LD schema validated (`json.loads` parse check passed)
- Tag balance confirmed: `div` 192/192, `section` 17/17, `main` 1/1
- All CSS classes used in the new markup confirmed already defined in this page's own stylesheet
- Banned-phrase grep passed (remaining matches are all false positives: the sitewide Organization schema's own 2006 founding date, a developer-facing HTML comment, an unrelated CSS comment, CSS `::placeholder`, and a compliant guardrail disclaimer)
- Required-phrase grep passed (since 2010, eClinicalWorks, IMS, athenahealth, full testimonial quote and attribution)
- Verified live in-browser via local `http.server`: desktop screenshots of hero, full testimonial section, and final CTA/form all render correctly; no console errors
- Mobile viewport (375×812) checked: clean layout, no horizontal scroll, no console errors

## QA Checklist Results (doc §33 First-Time-Right Publish Blockers)

| Item | Status |
|---|---|
| Since 2010 used accurately | PASS |
| No "since 2006" | PASS |
| No active-current-client implication | PASS |
| Multi-location experience framed accurately as historical experience | PASS |
| Walk-in verification accurately described | PASS |
| Facility-style billing accurately described | PASS |
| Professional/E&M billing accurately described | PASS |
| No payer-specific overclaim | PASS |
| Workers' Comp accurately described | PASS |
| Auto-liability accurately described | PASS |
| No unsupported adjuster/legal-service claims | PASS |
| eCW included | PASS |
| IMS included | PASS |
| athenahealth included | PASS |
| No unsupported EMRs | PASS |
| No "all major EMRs" | PASS |
| Medical Coding separately scoped | PASS |
| Coding education accurately represented | PASS |
| PA separately scoped | PASS (not presented as core; not a major page section, per doc's low-emphasis instruction) |
| Credentialing not automatically core | PASS |
| Real testimonial source verified | PASS (verified and corrected to match source exactly) |
| Star treatment matches original source | PASS |
| No composite case | PASS |
| Every metric fully validated | PASS (qualitative-only; no unvalidated numeric metric published) |
| Old-template metrics removed if unsupported | PASS |
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
| No broken links | PASS (all links point to existing pages: `/testimonials/`, `/privacy-policy/`, `tel:`, in-page anchor, specialty mega-links) |

**Not confirmed / requires action outside this rebuild:**
- Zoho lead creation, CRM routing, and notification/sales-follow-up steps (doc §29's test path) cannot be verified from a static local build.
- The testimonial's exact permission-to-publish status is not separately re-flagged since the doc itself already confirms it as real, approved proof (§2, §16) — no additional hold was needed beyond noting the wording correction in the claims register.

## Conflicts found

None between this V4 doc and the V2 framework or `BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`.

## Freeze

Per doc §36 Freeze Criteria and §39, this page is ready for freeze once live QA (Zoho/CRM routing) is confirmed post-deploy. Pushed to GitHub per explicit instruction with commit message "Rebuild Urgent Care specialty page per V2 framework spec."

## Not in scope / not touched

No other specialty page was modified in this pass.
