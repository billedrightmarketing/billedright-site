# Rheumatology — Change Map

## Implementation Log — 2026-09-16: Full rebuild per V4 FINAL First-Time-Right implementation doc

**Source:** `docs/specialty-pages/rheumatology/Billed_Right_Rheumatology_FINAL_First_Time_Right_V4_RCM_SEO_AEO_Enterprise_Implementation.md` (1,305 lines, read in full)

**Governing standard:** `docs/specialty-pages/Billed_Right_Specialty_Page_Framework_V2.md`, `docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`

This was a full rebuild, not a targeted cleanup. The prior live page followed the older CPT/J-code-tutorial template (biologic J-codes, step-therapy documentation mechanics, infusion CPT codes 96413/96415/96417, Part B vs. Part D coverage rules) rather than the V4 enterprise-lead framework. Rebuilt as a 20-section flow per the doc's §42 Final Page Flow.

### Case Study

**Status: No case-study representation existed before this rebuild, and this document does not supply one.**

- No `pages/case-studies/rheumatology/` directory exists anywhere in the repo — confirmed by directory listing.
- The prior live page's "Resources & Insights" section carried a card titled "Rheumatology Practice Cuts Biologic Denial Rate and Recovers Lost Revenue," explicitly described in its own copy as *"A composite look at how a multi-provider rheumatology practice tightened J-code and prior authorization documentation..."* — a composite case study, exactly what doc §20 instructs to remove: *"The current page includes a composite Rheumatology case study. Remove it."*
- The doc is explicit that no real Rheumatology case study currently exists to substitute in its place (§20 proof hierarchy: "Real Rheumatology Case Study > Authentic Rheumatology Testimonial > No Case Study" and §42 item 16: "Real case study only if later available"). It does not supply one.
- **Fix:** The composite case-study card was removed entirely (along with the rest of the old "Resources & Insights" section — see Removed, below). No case-study section was rebuilt in its place. Per doc's proof hierarchy, the real, verified testimonial (below) is used as the page's proof instead.
- A large PE-backed Rheumatology organization is in active conversation with Billed Right per the doc's internal notes (§2), but the doc explicitly forbids using this prospect as public proof in any form, since it is not yet a signed client. No reference to this prospect appears anywhere on the rebuilt page — confirmed by grep.

### Testimonial

**Status: Real, verified, kept unchanged.**

- The existing testimonial attributed to **"Arthritis and Rheumatism Provider, FL"** — *"I have been extremely pleased and satisfied by the promptness and thoroughness. There is always excellent feedback and quick resolution to any issue."* — is confirmed in the V4 doc (§2, §19) as real, approved proof.
- Cross-checked against the master `pages/testimonials.html` (tagged `data-cat="rheumatology"`): the quote, attribution and 5-star display are identical between the master testimonials page and what was on the prior specialty page. Since the source page (`/testimonials/`) already carries this testimonial with a 5-star display, the star treatment was **kept**, not artificially added — consistent with doc §19's instruction to remove stars only if the original source did not carry them.
- Kept in the rebuilt page's Section 15 ("Real Testimonial"), using the same contextual-attribution and card format used on every other specialty page this session.
- Added a `docs/claims-register.md` entry (previously no Rheumatology row existed in the register).

### Keep / Rewrite / New / Remove

**Removed (old CPT/J-code-tutorial template, replaced by V4 framework):**
- "Common Pain Areas" / "Rheumatology Solutions" bullet lists (J-code, step therapy, Part B/D mechanics)
- "Top Denial Reasons" 5-card grid (J-code errors, step therapy documentation, infusion time documentation, Part B/D mismatch)
- "Payer-Specific Considerations" paragraph naming specific drugs (Humira, Enbrel, Remicade, Cimzia) and J-codes (J1745, J0717, J0135)
- "What to Expect" 6-step implementation timeline containing unrevalidated turnaround promises: *"we will follow up within 24-48 hours and appeal any denied claims within the same timeframe"* and *"claims go out under full account management, same business day"* — doc §3 explicitly lists both as "Do Not Carry Forward Without Revalidation," and neither is a verified fact in the V4 doc
- Numeric KPI grid (97% collections, 20-day A/R reduction, 1% error ratio, <48hr TAT, <1% no-response, 28-day TAT, **"20 years of experience"**) — doc §3 explicitly flags "20 years of experience" as incorrect (correct figure is since 2008, i.e. ~18 years) and §21 KPI Governance requires "Do not automatically reuse the current live-page KPI block... requires full validation before reuse." None of these figures are validated in the doc, so none were preserved. Replaced with 6 qualitative outcome cards, consistent with the treatment already applied to Nephrology, Gastroenterology and Primary Care.
- "We work with all major EMR" generic claim — doc §16 is explicit: only eClinicalWorks (eCW) is verified for Rheumatology; "Do not add IMS, Athena, AdvancedMD or other Rheumatology EMRs until first-party verified."
- "Reviewed by Billed Right's rheumatology billing team, with 18+ years in rheumatology RCM" authority line — doc §3 and §36 explicitly list this as something that must not carry forward.
- Composite case-study card and the other two "Resources & Insights" cards (linking to generic `/blog/` and `/resources/` hub URLs for content that doesn't exist yet) — doc §28 V4 Resource Publication Rule: *"A resource appears on the page only when: it exists; it is published; the destination works; the content is complete... Do not publish placeholder or 'coming soon' resources."* Omitted entirely, same treatment as Nephrology/Gastroenterology/Primary Care.
- Second lead-generation form ("Download Our Brochure") — doc §32 requires exactly one final conversion section with no second major CTA block.
- "Since 2006" claim — corrected to **since 2008** per doc §2/§3/§36, the single most load-bearing factual correction in this rebuild.

**New (per V4 doc, not previously on the page):**
- Infusion / Biologic Revenue major-differentiator section (doc §9) with explicit scope-boundary disclaimer (no drug purchasing, inventory, white-bagging, specialty-pharmacy sourcing, drug acquisition strategy, wastage, or buy-and-bill financial reconciliation)
- Prior Authorization scope-clarification section (doc §11), explicitly separately scoped, no guarantee of approval
- Office + Hospital Professional Billing section (doc §13), using "professional billing" language only, with an explicit scope callout that this does not extend to hospital facility billing, facility revenue, cost accounting or chargemaster management
- Coding Education section (doc §14) with CLAIMS→PATTERNS→REVIEW→PROVIDER EDUCATION→STRONGER FUTURE EXECUTION visual
- Standard RCM workflow, 10-step (doc §8): VERIFY→CAPTURE→SCRUB→SUBMIT→MONITOR→PRIORITIZE→RESOLVE→POST→ANALYZE→IMPROVE
- Intelligent RCM section (doc §15) with PREVENT→DETECT→PRIORITIZE→AUTOMATE→ACT→LEARN visual and required "AI does not replace experienced Rheumatology revenue-cycle professionals" callout
- Data-to-Decisions section (doc §17) with WHAT CHANGED?→WHERE?→WHY?→FINANCIAL IMPACT→ACTION visual
- Growth-ready operating model section (doc §18), carefully worded per the doc's explicit instruction not to claim "trusted by PE-backed Rheumatology groups" or "serving large Rheumatology platforms" since Billed Right's current Rheumatology clients are smaller practices and the PE-backed organization is not yet signed

**Kept/reused (structurally consistent with prior page and other specialties):**
- Hero pattern, "Our Specialties" mega-link footer, single lead-capture form pattern, FAQ accordion pattern, breadcrumb pattern
- Real testimonial (see above)

### Step Therapy (doc §12)

Billed Right's operational role in step-therapy tracking/documentation is explicitly unconfirmed per the doc. Per instruction, step therapy is **not referenced anywhere on the rebuilt page** — not even as a brief example of payer complexity — since the doc's own FAQ section (§26) instructs to omit the step-therapy FAQ entirely if unconfirmed at launch, and no other section of the doc requires mentioning it. Confirmed via grep: no occurrence of "step therapy" or "step-therapy" anywhere in the rebuilt page.

### Buy-and-Bill (doc §10)

Not overclaimed. The Infusion/Biologic section explicitly states Billed Right does not manage buy-and-bill financial reconciliation, drug inventory, specialty-pharmacy sourcing, white-bagging or wastage — matching the doc's "Not Yet Allowed" list precisely.

### PE-Backed Prospect (doc §2, §18, §36)

Not referenced anywhere on the page. Confirmed via grep for "PE," "prospect," "platform" in relevant contexts — no match referencing the unsigned organization. The page's growth/scale section speaks only to Billed Right's operating model in the abstract, per the doc's approved wording.

### EMR

Only **eClinicalWorks (eCW)** is named, per doc §16 ("Do not add IMS, Athena, AdvancedMD or other Rheumatology EMRs until first-party verified"). No partnership/certification/proprietary-integration claim made.

### KPI Governance

No numeric KPI in the V4 doc is locked/verified for Rheumatology. Per doc §21, used qualitative-only KPI cards (stronger claim quality, disciplined denial follow-up, prioritized high-value A/R, clearer infusion-revenue visibility, earlier exception identification, stronger executive reporting), consistent with the Nephrology/Gastroenterology/Primary Care treatment. Added disclaimer: "Billed Right does not publish invented Rheumatology performance numbers. Where a metric is shown, it includes a defined metric, value, unit/time basis, applicable population and source" (matching doc §21's required 5-part KPI definition, the "Source" element being new relative to earlier specialty docs).

### SEO

- Title: `Rheumatology Revenue Cycle Management & Billing | Billed Right` (locked, doc §24)
- Meta description: `Rheumatology RCM since 2008 with infusion billing, hospital professional billing, eClinicalWorks expertise, denial/A/R management and intelligent revenue-cycle workflows.` (locked, doc §24)
- URL unchanged: `/specialties/rheumatology-rcm-services/`
- Updated OG/Twitter tags to match
- Updated `Service` schema description, added `Rheumatology` to `MedicalBusiness.medicalSpecialty`, rebuilt `FAQPage` schema to match the new on-page FAQ content (doc §26, verbatim) — the step-therapy FAQ was omitted from schema as well, consistent with omitting it from the visible page
- One H1 only: "Rheumatology Revenue Cycle Management Services"

### Internal-to-Public Copy Firewall (doc §35)

Checked the rendered page for internal-implementation language (e.g. "verify with team," "PE prospect," "step therapy pending confirmation," "placeholder," "authority topic idea"). None found — confirmed via grep against the final HTML. The only "placeholder" string match is a CSS `::placeholder` pseudo-selector, not public copy. HTML source comments marking omitted sections (e.g. "REAL CASE STUDY — none exists yet; omitted per doc §20") are developer-facing markup comments, not rendered text — consistent with the same convention used on the Primary Care and Nephrology rebuilds this session.

### Guardrails enforced

- No SOC 2 claim
- No invented statistics — testimonial verified against source, KPIs qualitative-only
- No CPT/J-code dump (the prior page's entire J-code/CPT-mechanics content — J1745, J0717, J0135, 96413/96415/96417 — was removed; that content belonged to the old tutorial-style template, not the V4 enterprise-lead framework)
- No competitor attacks
- Core RCM vs. add-on distinction maintained — Prior Authorization and Medical Coding both explicitly presented as separately scoped, never implied as core RCM
- No unverified turnaround-time promises (24-48hr, same-business-day) carried forward from the old page
- No step-therapy capability claim; no buy-and-bill/inventory/white-bagging/specialty-pharmacy overclaim; no PE-backed-prospect proof
- One final conversion section only (doc §32) — no competing CTA blocks
- PHI/privacy line and full consent language included in the lead form per doc §33, verbatim

### Build & Verification

- `python3 build.py` succeeded: 259 pages written, no errors
- JSON-LD schema validated (`json.loads` parse check passed)
- Tag balance confirmed: `div` 185/185, `section` 17/17, `main` 1/1
- All CSS classes used in the new markup confirmed already defined in this page's own stylesheet (no undefined-class regressions, unlike the transient issue caught and fixed during the Primary Care rebuild)
- Banned-phrase grep passed (remaining matches are all compliant guardrail disclaimers — e.g. "does not manage... white-bagging... buy-and-bill... wastage," "authorization approval is never guaranteed" — or false positives: CSS `::placeholder`, "claims" substring matching "ims", and the sitewide Organization schema's own 2006 founding date, which is a company-wide fact distinct from the Rheumatology-specific "since 2008" claim)
- Required-phrase grep passed (since 2008, eClinicalWorks, infusion, hospital professional, testimonial quote and attribution)
- Verified live in-browser via local `http.server`: desktop screenshots of hero, testimonial section, and final CTA/form all render correctly; no console errors
- Mobile viewport (375×812) checked: clean layout, no horizontal scroll, no console errors

## QA Checklist Results (doc §37 First-Time-Right Publish Blockers)

| Item | Status |
|---|---|
| Since 2008 | PASS |
| Current clients described accurately | PASS (no client-count/scale claims made beyond "smaller practices" framing implied by the growth section; no overstatement) |
| No unsigned prospect presented as client | PASS |
| No invented large-group proof | PASS |
| Infusion billing accurately represented | PASS |
| Hospital professional billing accurately represented | PASS |
| Office/facility distinction accurate | PASS |
| Step therapy not claimed without verification | PASS (omitted entirely) |
| Buy-and-bill not overstated | PASS |
| eCW included | PASS |
| No unsupported Rheumatology EMRs | PASS |
| PA separately scoped | PASS |
| Medical Coding separately scoped | PASS |
| Coding education accurately described | PASS |
| Credentialing not automatically core | PASS (Credentialing not mentioned as core; not presented as standard onboarding anywhere) |
| Real Arthritis and Rheumatism Provider testimonial source verified | PASS |
| Star rating verified before display | PASS (matches source page's existing 5-star presentation) |
| Composite case removed | PASS |
| No prospect proof | PASS |
| Definition + value + unit/time + population + source for every metric | PASS (qualitative-only; no unverified numeric metric published) |
| Old-template metrics removed if not verified | PASS |
| No internal KPI notes public | PASS |
| Technology → signal → human action → financial problem | PASS |
| No roadmap capability presented as live | PASS |
| Exactly one final conversion section | PASS |
| Four-field form | PASS (Name, Work Email, Phone, Practice/Organization) |
| PHI warning | PASS |
| Privacy link | PASS |
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
| No placeholders/internal notes | PASS |
| No unpublished resource cards | PASS |
| No broken links | PASS (all links point to existing site sections/pages: `/testimonials/`, `/contact/`, `/privacy-policy/`, `tel:`, in-page anchor, specialty mega-links) |

**Not confirmed / requires live-environment verification (flagged, not actioned):** Zoho lead creation, CRM routing, and notification/sales-follow-up steps described in doc §33's test path (`Submit → Lead Created/Updated → Source/Page Captured → Owner Assigned → Notification → Sales Follow-Up`) cannot be verified from a static local build.

## Conflicts found

None between this V4 doc and the V2 framework or `BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`.

## Freeze

Per doc §40 Freeze Criteria and §43, this page is ready for freeze once live QA (Zoho/CRM routing) is confirmed post-deploy. Pushed to GitHub per explicit instruction with commit message "Rebuild Rheumatology specialty page per V2 framework spec."

## Not in scope / not touched

No other specialty page was modified in this pass.
