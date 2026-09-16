# Behavioral Health — Change Map

## Implementation Log — 2026-09-16: Full rebuild per V4 FINAL First-Time-Right implementation doc

**Source:** `docs/specialty-pages/behavioral health/Billed_Right_Behavioral_Health_FINAL_First_Time_Right_V4_RCM_SEO_AEO_Enterprise_Implementation.md` (1,301 lines, read in full)

**Governing standard:** `docs/specialty-pages/Billed_Right_Specialty_Page_Framework_V2.md`, `docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`

This was a full rebuild, not a targeted cleanup. The prior live page followed the older CPT/parity-tutorial template (psychotherapy CPT codes, named carve-out payers, IOP/PHP prior-authorization claims, mental-health-parity mechanics) rather than the V4 enterprise-lead framework. Rebuilt as a 17-section flow per the doc's §38 Final Page Flow.

### Case Study — Priority Specialty Status

Behavioral Health is one of the four priority specialties per `docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md` (Cardiology, Pain Management, Internal Medicine, Behavioral Health — this list matches the guardrails doc directly, unlike the Primary Care task earlier this session where the user's stated priority list diverged from the guardrails doc).

**Status: No real case study exists. The "prior case-study coverage" the task refers to was an invented composite figure, already identified and removed sitewide for lack of authenticity — it is not being lost, it is being correctly kept removed.**

- No `pages/case-studies/behavioral-health/` directory exists anywhere in the repo — confirmed by directory listing.
- `docs/claims-register.md` (row 50, pre-existing from an earlier session) documents that a composite statistic — "Behavioral Health +44% / 22d A/R / -54% denials" — was already flagged `SUPERSEDED` and `REMOVED` from the homepage on 2026-08-27, with the explicit register note: *"no Behavioral Health case study exists to source this from."* This is almost certainly the "case-study coverage" referenced in this task's instructions — it was invented/composite data, not a real case study, and its earlier removal from the homepage was the correct action, not a loss of legitimate proof.
- The prior live specialty page's own "Resources & Insights" section carried a card titled "Behavioral Health Practice Reduces Denials and Recovers Lost Revenue," explicitly self-described as *"A composite look at how a multi-provider behavioral health practice tightened documentation and recovered lost revenue"* — the same category of composite defect already corrected sitewide once before, but never fixed on this specific page until now.
- The V4 doc is explicit and severe on this point (§15): *"Do not use CCSN on this page... Do not use composite case studies, hypothetical case studies, illustrative client stories, 'representative results.'... If no suitable proof exists, the page can remain strong without forcing a case study."*
- **Fix:** The composite case-study card was removed entirely (along with the rest of the old "Resources & Insights" section — see Removed, below). No case study section was rebuilt in its place. Per the doc's proof hierarchy (Real Case Study > Real Testimonial > No Case Study), the real, previously-in-use testimonial (below) remains the page's proof.
- **Conclusion for this task's specific question:** nothing legitimate was lost. The only prior "case-study coverage" for Behavioral Health was ever a composite figure, and it has now been correctly removed from the last remaining place it appeared (the specialty page itself), consistent with its earlier removal from the homepage.

### Testimonial

**Status: Real testimonial kept (same one already live on the page pre-rebuild); flagged for the same pending verification already on record.**

- The page already displayed the testimonial attributed to **"CEO, Behavioral Health Group, CT"** — *"We started using Billed Right as our outsourced payment partner and since we have brought them on, we have seen a meaningful improvement in timeliness, accuracy, and an overall reduction in long outstanding A/R. We have been particularly impressed with their ability to learn our EMR and familiarize themselves with Behavioral Health billing and CPT requirements. Their implementation team was open to working with us to develop a process that was reflective of our business model."* — cross-checked identical (full, untruncated quote) against the master `pages/testimonials.html` (tagged `data-cat="behavioral"`).
- This is **not** CCSN — confirmed via repo-wide grep for "CCSN," which returns zero matches anywhere in the project. The doc's exclusion is satisfied trivially since this testimonial was never CCSN to begin with.
- The doc does not name a specific Behavioral Health testimonial to use (unlike, e.g., Nephrology's or Rheumatology's docs, which named an exact attribution) — it only requires "an approved Behavioral Health testimonial... other than CCSN... used only after source verification." Four other genuine Behavioral Health testimonials exist on `/testimonials/` (data-cat="behavioral"): "Behavioral Health Provider" (18-month growth story, no location), two quotes both attributed to "CEO, NC," and one attributed to "Director, FL." None of these is more specific or verifiable than the CT CEO quote already in use, which names concrete, checkable claims (EMR/CPT familiarity, A/R reduction) consistent with the level of specificity used on other specialty pages this session.
- Kept the existing testimonial rather than swapping it, since it was already the specialty page's live selection, is not CCSN, and matches the source page exactly. Updated the pre-existing `docs/claims-register.md` row (previously flagged `NEEDS VERIFICATION` on 2026-08-27, before this session) to note its continued specialty-page use — the verification hold itself is unchanged and still open.
- Star display (5 stars) matches the source page's own presentation — not artificially added.

### Keep / Rewrite / New / Remove

**Removed (old CPT/parity-tutorial template, replaced by V4 framework):**
- "Common Pain Areas" / "Behavioral Health Solutions" bullet lists (parity violations, carve-out plan navigation)
- "Top Denial Reasons" 5-card grid, which named **Magellan, Optum Behavioral and Beacon by name** and asserted **IOP/PHP prior-authorization tracking as a delivered capability** ("Yes. We track authorization requirements per payer and submit and follow up on... authorizations before claims go out") — doc §2 and §30 both explicitly forbid naming carve-out payers and claiming IOP/PHP support until verified, and neither is a verified fact in this V4 doc
- "Payer-Specific Considerations" paragraph, which repeated the same carve-out payer names and a long CPT-code list (90837, 90834, 90832, 90791, 90853, 96156/96158, H-codes)
- "What to Expect" 6-step implementation timeline containing unrevalidated turnaround promises: *"we will follow up within 24-48 hours and appeal any denied claims within the same timeframe"* and *"claims go out under full account management, same business day"* — neither is a verified fact in the V4 doc
- Numeric KPI grid (97% collections, 20-day A/R reduction, 1% error ratio, <48hr TAT, <1% no-response, 28-day TAT, **"20 years of experience"**) — doc §2 is unusually explicit and cautionary on this exact number: Billed Right itself has 10+ years of direct Behavioral Health experience; the "20+ years" figure belongs to a separately acquired organization and must never be presented as Billed Right's own direct history without explicit leadership approval, which this doc does not grant. The old page's "20 years of experience" KPI card was exactly this conflation. Removed and replaced with 6 qualitative outcome cards, consistent with every other specialty rebuilt this session.
- "We work with all major EMR" generic claim — doc §12/§30 explicit: real first-party platform experience (eCW, CentralReach, IMS, AdvancedMD) is available, so generic "all major EMR" filler must not be used.
- "Reviewed by Billed Right's behavioral health billing team, 18+ years in behavioral health RCM" authority line — repeats the same 18-20-year conflation problem above; not a verified fact in this doc.
- CPT-code FAQ ("What CPT codes are most commonly used in behavioral health billing?") and the carve-out-payer FAQ ("Do you work with carve-out plans like Magellan, Optum Behavioral, and Beacon?") — both replaced by the doc's own locked FAQ set (§21), which contains neither CPT-code lists nor named carve-out payers
- IOP/PHP prior-authorization FAQ ("Do you handle prior authorizations for IOP and PHP levels of care?") — doc explicitly instructs not to add IOP/PHP claims until verified
- Composite case-study card and the other two "Resources & Insights" cards (linking to generic `/blog/` and `/resources/` hub URLs for content that doesn't exist yet) — doc §23 V4 Resource Publication Rule: *"A resource may appear on the commercial page only when: it exists; the destination is published..."* Omitted entirely, same treatment as every other specialty rebuilt this session
- Second lead-generation form ("Download Our Brochure") — doc §27 requires exactly one final conversion section with no second major CTA block

**New (per V4 doc, not previously on the page):**
- Provider Education section (doc §9) with CLAIMS→PATTERNS→REVIEW→PROVIDER EDUCATION→STRONGER FUTURE EXECUTION visual
- Prior Authorization scope-clarification section (doc §10), explicitly separately scoped, with no separate CTA
- Standard RCM workflow, 10-step (doc §8): VERIFY→CAPTURE→SCRUB→SUBMIT→MONITOR→PRIORITIZE→RESOLVE→POST→ANALYZE→IMPROVE
- Intelligent RCM section (doc §11) with PREVENT→DETECT→PRIORITIZE→AUTOMATE→ACT→LEARN visual and required "AI does not replace experienced Behavioral Health revenue-cycle professionals" callout
- Data-to-Decisions section (doc §13) with WHAT CHANGED?→WHERE?→WHY?→FINANCIAL IMPACT→ACTION visual
- Enterprise/multi-location positioning section (doc §14)
- Explicit 4-platform EMR section (eClinicalWorks, CentralReach, IMS, AdvancedMD) replacing the old generic claim

**Kept/reused (structurally consistent with prior page and other specialties):**
- Hero pattern, "Our Specialties" mega-link footer, single lead-capture form pattern, FAQ accordion pattern, breadcrumb pattern
- Real testimonial (see above)

### Behavioral Health vs. Psychiatry vs. ABA Separation (doc §3)

Confirmed via grep: no ABA-specific terminology (BCBA, RBT, unit-utilization, therapy-hour authorization) appears anywhere on the rebuilt page. No psychiatrist/medication-management-heavy positioning was introduced. Psychiatry is referenced exactly once, in the FAQ, using the doc's own locked answer ("Billed Right has a dedicated Psychiatry RCM service page..."). No cross-link to a dedicated ABA page was added, since the doc's suggested cross-link language ("Looking for ABA Therapy RCM?...") is conditioned on that dedicated ABA page existing, and no `pages/aba-*.html` currently exists in the repo — adding the cross-link now would point to a non-existent page, violating the same "no broken links" publish blocker (doc §32).

### EMR

All four verified platforms named: **eClinicalWorks (eCW), CentralReach, IMS, AdvancedMD** (doc §12). No partnership/certification/proprietary-integration claim made. CentralReach is presented in Behavioral Health RCM terms only, not reframed as an ABA story, per the doc's explicit caution.

### KPI Governance

No numeric KPI in the V4 doc is locked/verified for Behavioral Health. Per doc §16, used qualitative-only KPI cards (stronger claim quality, earlier issue identification, disciplined denial follow-up, prioritized A/R, clearer executive visibility, recurring provider education), consistent with every other specialty rebuilt this session. Added disclaimer: "Where a metric is shown, it includes a defined metric, value, unit/time basis, applicable population and source" — phrased as forward-looking public copy per doc §16's explicit instruction that internal language such as "we do not publish invented numbers" must not appear on the public page (unlike the phrasing used on some earlier specialty pages this session, which did include that internal-sounding sentence — this doc is the first to explicitly flag it as a firewall violation, so the wording here was adjusted accordingly).

### SEO

- Title: `Behavioral Health Revenue Cycle Management & Billing | Billed Right` (locked, doc §19)
- Meta description: `Behavioral Health RCM backed by 10+ years of Billed Right experience, specialty EMR expertise, denial/A/R management, practical automation and executive financial visibility.` (locked, doc §19)
- URL unchanged: `/specialties/behavioral-health-rcm-services/`
- Updated OG/Twitter tags to match
- Updated `Service` schema description, added `BehavioralHealth` to `MedicalBusiness.medicalSpecialty`, rebuilt `FAQPage` schema to match the new on-page FAQ content (doc §21, verbatim)
- One H1 only: "Behavioral Health Revenue Cycle Management Services"

### Internal-to-Public Copy Firewall (doc §31)

Checked the rendered page for internal-implementation language (e.g. "validate," "publish blocker," "verify before use," "do not invent," "placeholder," "pending confirmation"). The only matches found are: (1) a pre-existing, unrelated CSS comment ("Guarantee seal pulse") from the shared site stylesheet, (2) CSS `::placeholder` pseudo-selectors, (3) a pre-existing WordPress-integration comment referencing "functions.php" (matched "PHP" as a substring, unrelated to Partial Hospitalization Program), and (4) developer-facing HTML source comments marking omitted sections (e.g. "REAL PROOF ONLY — no real case study exists yet... VALIDATED KPIs — none validated..."), which are not rendered text — consistent with the same convention used on every other specialty rebuild this session. No actual public-copy firewall violation found.

### Guardrails enforced

- No SOC 2 claim
- No invented statistics — testimonial verified against source, KPIs qualitative-only
- No CPT-code dump (the prior page's entire CPT/parity-mechanics content was removed; that content belonged to the old tutorial-style template, not the V4 enterprise-lead framework)
- No competitor attacks
- Core RCM vs. add-on distinction maintained — Prior Authorization and Medical Coding both explicitly presented as separately scoped, never implied as core RCM; Credentialing not presented as automatically core anywhere
- No unverified turnaround-time promises (24-48hr, same-business-day) carried forward from the old page
- No named carve-out payers, no IOP/PHP capability claim, no CCSN, no ABA-specific complexity, no psychiatrist-heavy positioning
- No conflation of the acquired company's 20+ years with Billed Right's own 10+ years of direct experience
- One final conversion section only (doc §27) — no competing CTA blocks
- PHI/privacy line and full consent language included in the lead form per doc §28, verbatim

### Build & Verification

- `python3 build.py` succeeded: 259 pages written, no errors
- JSON-LD schema validated (`json.loads` parse check passed)
- Tag balance confirmed: `div` 178/178, `section` 15/15, `main` 1/1
- All CSS classes used in the new markup confirmed already defined in this page's own stylesheet
- Banned-phrase grep passed (remaining matches are all false positives: a pre-existing CSS comment, CSS `::placeholder`, a WordPress `functions.php` reference, and this task's own developer-facing HTML comments marking omitted sections)
- Required-phrase grep passed (10+ years, eClinicalWorks, CentralReach, IMS, AdvancedMD, testimonial quote and attribution)
- Verified live in-browser via local `http.server`: desktop screenshots of hero, testimonial section, EMR technology section, and final CTA/form all render correctly; no console errors
- Mobile viewport (375×812) checked: clean layout, no horizontal scroll, no console errors

## QA Checklist Results (doc §32 First-Time-Right Publish Blockers)

| Item | Status |
|---|---|
| 10+ years accurately stated | PASS |
| Acquired-company 20+ years not misrepresented as Billed Right's direct history | PASS |
| No unsupported client-size claim | PASS |
| No CCSN reference | PASS |
| Behavioral Health distinct from Psychiatry | PASS |
| ABA excluded except optional simple cross-link | PASS (cross-link omitted entirely since no dedicated ABA page exists yet — see note above) |
| IOP/PHP excluded unless verified | PASS |
| Named carve-out payer claims excluded until verified | PASS |
| eCW accurate | PASS |
| CentralReach accurate | PASS |
| IMS accurate | PASS |
| AdvancedMD accurate | PASS |
| No "all major EMRs" filler | PASS |
| Prior Authorization separately scoped | PASS |
| Medical Coding separately scoped | PASS |
| Coding education accurate | PASS |
| Credentialing not implied as automatically core | PASS |
| No composite case | PASS |
| No CCSN testimonial | PASS |
| Any testimonial source verified | PARTIAL — quote matches the source page exactly (verified for accuracy), but permission-to-publish and current-client-relationship status remain the pre-existing `NEEDS VERIFICATION` hold in `docs/claims-register.md`, not newly resolved by this rebuild |
| Star presentation matches original source | PASS |
| Every number has definition/value/unit/time/population/source | PASS (qualitative-only; no unverified numeric metric published) |
| Unverified metrics removed | PASS |
| No internal KPI-validation language visible | PASS |
| Technology → signal → human action → financial problem | PASS |
| No roadmap capabilities presented as live | PASS |
| One final conversion section | PASS |
| Four-field form | PASS (Name, Work Email, Phone, Practice/Organization) |
| PHI warning | PASS |
| Privacy Policy link | PASS |
| Approved consent | PASS |
| Zoho routing | UNCONFIRMED — cannot verify CRM lead routing in a local/static environment |
| Click-to-call | PASS (tel: link present and functional in markup; visually confirmed on mobile viewport) |
| One H1 | PASS |
| Title/meta | PASS |
| Canonical | PASS |
| Indexability | PASS (`robots: index, follow` unchanged) |
| Internal links | PASS |
| Schema | PASS |
| Mobile | PASS |
| No broken links | PASS (all links point to existing site sections/pages: `/testimonials/`, `/privacy-policy/`, `tel:`, in-page anchor, specialty mega-links; no ABA link added since no ABA page exists) |
| No placeholders/internal notes | PASS |
| No unpublished resource cards | PASS |

**Not confirmed / requires action outside this rebuild:**
- Zoho lead creation, CRM routing, and notification/sales-follow-up steps (doc §28's test path) cannot be verified from a static local build.
- The "CEO, Behavioral Health Group, CT" testimonial's permission-to-publish and current-relationship status remain an open item already on record in `docs/claims-register.md` since 2026-08-27 — this rebuild did not newly introduce this testimonial and did not resolve the pre-existing hold.

## Conflicts found

None between this V4 doc and the V2 framework or `BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`. Behavioral Health's priority-specialty status here is consistent with both the guardrails doc and this task's instructions (no discrepancy, unlike the Primary Care task earlier this session).

## Freeze

Per doc §35 Freeze Criteria and §39, this page is ready for freeze once live QA (Zoho/CRM routing) and the pre-existing testimonial verification hold are cleared. Pushed to GitHub per explicit instruction with commit message "Rebuild Behavioral Health specialty page per V2 framework spec."

## Not in scope / not touched

No other specialty page was modified in this pass.
