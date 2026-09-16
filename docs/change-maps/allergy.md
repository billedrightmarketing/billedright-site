# Allergy & Immunology — Change Map

## Implementation Log — 2026-09-16: Full rebuild per V4 FINAL First-Time-Right implementation doc

**Source:** `docs/specialty-pages/allergy/Billed_Right_Allergy_Immunology_FINAL_First_Time_Right_V4_RCM_SEO_AEO_Enterprise_Implementation.md` (1,341 lines, read in full)

**Governing standard:** `docs/specialty-pages/Billed_Right_Specialty_Page_Framework_V2.md`, `docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`

This was a full rebuild, not a targeted cleanup. The prior live page followed the older CPT/J-code-tutorial template (serum-preparation/injection CPT codes, named biologics with J-codes, skin/patch testing codes, spirometry billing) rather than the V4 enterprise-lead framework. Rebuilt as a 20-section flow per the doc's §41 Final Page Flow.

### Case Study

**Status: A real, verified case study already exists and was already published elsewhere on the site (`/case-studies/allergy/`, and on the homepage), but was not being used on the specialty page before this rebuild.**

- The published Allergy case study is confirmed `VERIFIED` in `docs/claims-register.md` (pre-existing row, sourced directly from the published case study page): a two-provider Allergy & Immunology practice in Winter Park, Florida, full RCM engagement, collection rate 87% → 94% within 5 months, denials −13%, A/R 31–90 days −32%, A/R 41–90 days −57%.
- Read the full case study source (`pages/case-studies/allergy/index.html`) and verified every figure and the time period against the doc's own "Approved Published Results" section (§18) before using them — the figures match exactly, and none were retyped from memory without this check.
- **Before this rebuild, the specialty page did not use this real case study at all.** Its "Resources & Insights" section instead linked a card titled "Allergy Practice Fixes Immunotherapy Billing and Recovers Lost Revenue," explicitly described in its own copy as *"A composite look at how a multi-provider allergy practice corrected immunotherapy and biologic documentation gaps..."* — a composite substitute sitting on the page while a real, verified case study existed and was already published elsewhere on the site. This is the same defect pattern found and fixed on the Primary Care specialty page earlier in this session.
- **Fix:** Rebuilt Section 15 ("Real Winter Park Allergy Case Study") using the verified facts above, with a "Read the Full Case Study" link to `/case-studies/allergy/`. Added a disclaimer that results are specific to this client and not a guarantee for any other practice. Per the doc's own "Important" note (§18), did **not** generalize the case study's client-specific "24–48 hour" denial-workflow detail into any company-wide SLA claim anywhere on the rebuilt page. Updated `docs/claims-register.md` to note this case study is now also used on the specialty page (previously homepage/case-study-page only).

### Testimonial

**Status: A real, Allergy-tagged testimonial exists and was added as secondary proof (the prior live page had no testimonial section at all).**

- One genuine Allergy & Immunology testimonial exists on the master `pages/testimonials.html` (tagged `data-cat="allergy"`): *"The doctor values our partnership and the knowledge we share. She appreciates that the Billed Right team has been with the practice guiding them, and she would not be able to do this work alone. She is glad to have us as a partner."* — attributed to "Practice Manager, FL," with a 5-star display on the source page.
- The doc (§19) instructs: *"Use a separate Allergy testimonial only if authentic, approved and source-verified. Do not force a testimonial if the real case study already provides stronger proof."* This is not a prohibition on using a real testimonial alongside the case study — it only cautions against manufacturing one if none exists. Since a genuine, Allergy-specific testimonial does exist, and the real case study is used as primary proof (matching the V2 framework's Section 10 pattern of case study + testimonial together), the testimonial was added as secondary proof directly after the case study section.
- The prior live specialty page had **no testimonial section at all** — this is new to the page, not a change to an existing selection.
- Star display (5 stars) matches the source page's existing presentation — not artificially added.
- Added a `docs/claims-register.md` entry (previously no Allergy testimonial row existed in the register), flagged `NEEDS VERIFICATION` for permission-to-publish-on-specialty-page and current-relationship status, consistent with the hold pattern used on every other testimonial-carrying specialty page in this session.

### Keep / Rewrite / New / Remove

**Removed (old CPT/J-code-tutorial template, replaced by V4 framework):**
- "Common Pain Areas" / "Allergy & Immunology Solutions" bullet lists (two-part immunotherapy billing mechanics, biologic J-code mechanics)
- "Top Denial Reasons" 5-card grid (serum prep vs. administration splitting, biologic PA, skin/patch testing codes, spirometry documentation)
- "Payer-Specific Considerations" paragraph, which named specific biologics with J-codes: **omalizumab (Xolair, J2357), mepolizumab (Nucala, J2182), benralizumab (Fasenra), dupilumab (Dupixent, J0222)** — doc §10 is explicit and severe here: *"Do not position biologic or infusion billing as a verified Billed Right Allergy capability... If biologics are mentioned at all, they may be described only as broader industry context, not a Billed Right capability. Preferred approach: omit them from the commercial pillar until verified."* This is a user-confirmed non-capability, not merely an unverified one, so all biologic/J-code references were removed entirely rather than softened.
- "What to Expect" 6-step implementation timeline containing unrevalidated turnaround promises: *"we will follow up within 24-48 hours and appeal any denied claims within the same timeframe"* and *"claims go out under full account management, same business day"* — doc §35 explicitly lists both as "Do Not Publish," and the doc separately warns (§18) that the case study's own client-specific 24–48-hour work example must not be generalized into a universal SLA
- Numeric KPI grid (97% collections, 20-day A/R reduction, 1% error ratio, <48hr TAT, <1% no-response, 28-day TAT, **"20 years of experience"**) — doc §2 explicitly caps Allergy experience at "more than 15 years," and §35 explicitly forbids a "20-year Allergy claim." Per doc §20 KPI Governance, none of these general KPI figures are validated for Allergy specifically, so none were preserved. Replaced with the real case study (above) plus the testimonial, consistent with the doc's own instruction: "If no validated general Allergy KPI exists, use the real case study plus qualitative outcomes."
- "We work with all major EMR" generic claim — doc §15/§35 explicit: only eClinicalWorks (eCW) and IMS are verified for Allergy; do not use "all major EMRs."
- "Reviewed by Billed Right's allergy and immunology billing team, 18+ years in allergy RCM" authority line — conflicts with the doc's locked "15+ years" figure and was removed.
- Biologic/PA FAQ ("Do biologics for severe asthma require prior authorization?") and the Medicare Part B biologics FAQ — both named specific drugs and J-codes and implied biologic billing as a Billed Right capability; replaced by the doc's own locked FAQ set (§25), which explicitly instructs to omit a biologic-capability FAQ rather than publish a non-affirmative one
- Composite case-study card and the other two "Resources & Insights" cards (linking to generic `/blog/` and `/resources/` hub URLs for content that doesn't exist yet) — doc §27 V4 Resource Publication Rule, same treatment as every other specialty rebuilt this session
- Second lead-generation form ("Download Our Brochure") — doc §31 requires exactly one final conversion section with no second major CTA block

**New (per V4 doc, not previously on the page):**
- Allergen Immunotherapy / Injection Billing section (doc §8) — the doc's own "core specialty differentiator" — with PREPARE→ADMINISTER→CAPTURE→SCRUB→SUBMIT→MONITOR→RESOLVE visual and an explicit scope-boundary disclaimer (Billed Right does not prepare serum, administer injections, determine clinical treatment or manage clinical immunotherapy protocols)
- Allergy Testing commercial-positioning section (doc §9), deliberately kept at executive level with no CPT list
- Prior Authorization scope-clarification section (doc §11), explicitly separately scoped, no guarantee of approval
- Office + Hospital Professional Billing section (doc §12), using "professional billing" language only, with an explicit scope callout
- Coding Education section (doc §13) with CLAIMS→PATTERNS→REVIEW→PROVIDER EDUCATION→STRONGER EXECUTION visual
- Standard RCM workflow, 10-step (doc §7): VERIFY→CAPTURE→SCRUB→SUBMIT→MONITOR→PRIORITIZE→RESOLVE→POST→ANALYZE→IMPROVE
- Intelligent RCM section (doc §14) with PREVENT→DETECT→PRIORITIZE→AUTOMATE→ACT→LEARN visual and required "AI does not replace experienced Allergy & Immunology revenue-cycle professionals" callout
- Data-to-Decisions section (doc §16) with WHAT CHANGED?→WHERE?→WHY?→FINANCIAL IMPACT→ACTION visual
- "Honest Scale Positioning" section (doc §17) — deliberately does not claim category dominance, does not disclose client count, and uses the doc's own exact recommended sentence verbatim: "Billed Right brings longstanding Allergy & Immunology revenue-cycle experience and a structured operating model that can support practices as their financial and operational needs evolve."

**Kept/reused (structurally consistent with prior page and other specialties):**
- Hero pattern, "Our Specialties" mega-link footer, single lead-capture form pattern, FAQ accordion pattern, breadcrumb pattern

### Honest Scale Positioning (doc §1, §17)

This is the most distinctive instruction in this particular doc relative to every other specialty rebuilt this session: Allergy is explicitly **not** one of Billed Right's largest specialties, and the doc is unusually direct that the page must communicate credible specialty depth "without pretending category dominance." Checked the rebuilt page for any of the doc's explicitly banned phrases — "one of our largest specialties," "hundreds of Allergy practices," "leading Allergy RCM platform," "enterprise Allergy specialist" — none appear anywhere (confirmed via grep). No current client count is disclosed anywhere on the page (also confirmed via grep for "one client," "current client," etc. — no matches).

### EMR

Both verified platforms named: **eClinicalWorks (eCW) and IMS** (doc §15). No partnership/certification/proprietary-integration claim made. No other EMRs added.

### KPI Governance

No general numeric KPI in the V4 doc is locked/verified for Allergy independent of the case study. Per doc §20 ("If no validated general Allergy KPI exists, use the real case study plus qualitative outcomes"), no separate qualitative-outcome-card section was added on top of the case study and testimonial — the doc's guidance here differs from every other specialty rebuilt this session (which used qualitative KPI cards in the absence of validated numbers) because Allergy specifically has a strong, validated case study to lead with instead. No internal-sounding disclaimer sentence (e.g., "Billed Right does not publish invented Allergy KPIs") was added anywhere, per the doc's explicit instruction (§20) that this exact phrasing is an internal instruction, not website copy.

### SEO

- Title: `Allergy & Immunology Revenue Cycle Management | Billed Right` (locked, doc §23)
- Meta description: `15+ years of Allergy & Immunology RCM experience with immunotherapy billing, eClinicalWorks and IMS expertise, denial/A/R management and hospital professional billing.` (locked, doc §23)
- URL unchanged: `/specialties/allergy-rcm-services/`
- Updated OG/Twitter tags to match
- Updated `Service` schema description, added `Allergy` to `MedicalBusiness.medicalSpecialty`, rebuilt `FAQPage` schema to match the new on-page FAQ content (doc §25, verbatim) — the biologic-capability FAQ was omitted from schema as well, consistent with omitting it from the visible page
- One H1 only: "Allergy & Immunology Revenue Cycle Management Services"

### Internal-to-Public Copy Firewall (doc §34)

Checked the rendered page for internal-implementation language (e.g. "only one current client," "not a big specialty," "verify with Saurin/team," "publish blocker," "unverified," "do not claim," "pending confirmation," "case-study metric needs validation"). None found — confirmed via grep against the final HTML. The only "placeholder" and "unverified" matches are a CSS `::placeholder` pseudo-selector and a compliant guardrail sentence ("does not promise unverified dashboard functionality"), respectively — not public-copy firewall violations. Developer-facing HTML source comments marking omitted sections are not rendered text, consistent with the convention used throughout this session.

### Guardrails enforced

- No SOC 2 claim
- No invented statistics — case study figures verified against source, testimonial verified against source
- No CPT-code dump (the prior page's entire serum-prep/J-code/spirometry-mechanics content was removed; that content belonged to the old tutorial-style template, not the V4 enterprise-lead framework)
- No competitor attacks
- Core RCM vs. add-on distinction maintained — Prior Authorization and Medical Coding both explicitly presented as separately scoped, never implied as core RCM
- No biologic/infusion billing claimed as a verified Billed Right Allergy capability anywhere on the page
- No buy-and-bill, specialty-pharmacy or drug-inventory claims
- No unverified turnaround-time promises (24-48hr, same-business-day) carried forward from the old page, and the case study's own client-specific 24-48-hour detail was not generalized into a universal SLA
- No category-dominance overstatement; no current client count disclosed
- One final conversion section only (doc §31) — no competing CTA blocks
- PHI/privacy line and full consent language included in the lead form per doc §32, verbatim

### Build & Verification

- `python3 build.py` succeeded: 259 pages written, no errors
- JSON-LD schema validated (`json.loads` parse check passed)
- Tag balance confirmed: `div` 208/208, `section` 18/18, `main` 1/1
- All CSS classes used in the new markup confirmed already defined in this page's own stylesheet (the case-study before/after stat display reused the inline-styled approach established during the Primary Care rebuild, not the undefined `.br-cs-bigstat` classes that caused a rendering defect there — avoided proactively this time)
- Banned-phrase grep passed (remaining matches are all false positives or compliant guardrail disclaimers: the sitewide Organization schema's own 2006 founding date, CSS `::placeholder`, and "not a guarantee of results for any other practice" / "does not promise unverified dashboard functionality" disclaimers)
- Required-phrase grep passed (15+ years, eClinicalWorks, IMS, Winter Park, 87%, 94%, testimonial quote and attribution)
- Verified live in-browser via local `http.server`: desktop screenshots of hero, case study section (including the before/after stat display and all three outcome metric cards), testimonial section, and final CTA/form all render correctly; no console errors
- Mobile viewport (375×812) checked: clean layout, no horizontal scroll, no console errors

## QA Checklist Results (doc §36 First-Time-Right Publish Blockers)

| Item | Status |
|---|---|
| 15+ years used accurately | PASS |
| No unsupported exact start year | PASS (no "since [year]" claim made for Allergy specifically) |
| No current client-count disclosure | PASS |
| No false category-dominance language | PASS |
| Immunotherapy/injection billing accurately represented | PASS |
| Serum-preparation billing context accurate | PASS |
| Biologic/infusion capability not claimed | PASS |
| Office/hospital professional scope accurate | PASS |
| eCW included | PASS |
| IMS included | PASS |
| No unsupported Allergy EMRs | PASS |
| No "all major EMRs" | PASS |
| PA separately scoped | PASS |
| Medical Coding separately scoped | PASS |
| Coding education accurately described | PASS |
| Credentialing not automatically core | PASS |
| Real Winter Park case study used | PASS |
| Exact metrics rechecked against approved case source | PASS |
| Case-study time period accurate | PASS (5 months) |
| No guarantee language | PASS |
| No composite case | PASS |
| General KPIs independently validated | PASS (none published; case study + testimonial used instead, per doc §20) |
| Case-study metrics clearly presented as case results | PASS |
| No internal validation notes public | PASS |
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
| No broken links | PASS (all links point to existing pages: `/case-studies/allergy/`, `/testimonials/`, `/privacy-policy/`, `tel:`, in-page anchor, specialty mega-links) |

**Not confirmed / requires action outside this rebuild:**
- Zoho lead creation, CRM routing, and notification/sales-follow-up steps (doc §32's test path) cannot be verified from a static local build.
- The "Practice Manager, FL" testimonial's permission-to-publish-on-the-specialty-page and current-relationship status are newly flagged `NEEDS VERIFICATION` in `docs/claims-register.md` — this is a new usage (the prior specialty page had no testimonial at all), not a pre-existing hold being carried forward.

## Conflicts found

None between this V4 doc and the V2 framework or `BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`.

## Freeze

Per doc §39 Freeze Criteria and §42, this page is ready for freeze once live QA (Zoho/CRM routing) and the new testimonial's publish-permission verification are cleared. Pushed to GitHub per explicit instruction with commit message "Rebuild Allergy/Immunology specialty page per V2 framework spec."

## Not in scope / not touched

No other specialty page was modified in this pass.
