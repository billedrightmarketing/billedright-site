# Change Map — Home

## Implementation Log

**2026-08-27 — Go-live alignment pass.** Executed against `pages/home.html`
after leadership resolved the open claims/capability/case-study questions
this map had flagged. Summary (full detail in `docs/claims-register.md` and
`docs/capability-register.md`):
- Title/meta/OG/Twitter rewritten to enterprise RCM framing (removed
  "Medical Billing"/"Free billing review" lead, removed the unverified 94%
  collections figure).
- Homepage FAQ schema reworded (removed 94% collections claim, removed flat
  "2–3 week" onboarding promise, updated specialty list).
- Hero stat and Proven Results "94% lift in collections" card **removed**
  (not confirmed) — replaced with "94% client retention rate" (hero) and a
  new "400+ team members" card (Proven Results); tenure standardized to
  4.9 years sitewide-on-homepage (was inconsistently 4-year vs. 4.9-year).
- "Inside Billed Right" and AI/Automation sections retoned for executive
  audience; underlying AI/automation capabilities and metrics **kept and
  logged LIVE** in `docs/capability-register.md` per leadership confirmation.
- Denial-recovery "90% recoverable" claim reworded as industry context, not
  a Billed Right-specific outcome.
- Revenue Leak Assessment section reframed as an enterprise Revenue
  Performance Assessment; removed the "$4,200+ / under 10 providers" stat
  (not confirmed, also conflicted with the 25–100 provider ICP). The
  original 60-second calculator remains available at `/resources/`.
- Specialty tile grid replaced: was 12 tiles (6 with no real page behind
  them, all firing the same generic click handler) → now the 12 real
  specialty pages as proper `<a>` links, priority specialties first
  (Cardiology, Pain Management, Internal Medicine, Behavioral Health).
- Client Success Story cards labeled "Composite results" with an explicit
  composite/illustrative disclosure (leadership confirmed these are
  composite, not single verified clients).
- Comparison-table "120-day money-back guarantee" row: confirmed real by
  leadership (2026-08-27) and restored to the table with the specific term.
- MedicalBusiness schema `medicalSpecialty` list corrected to match the
  4 priority specialties (was listing Orthopedic/Pediatric/Psychiatry,
  missing Pain Management/Behavioral Health).

**Still open / not resolved in this pass:**
- API & HL7/FHIR integration claim (Technology Ecosystem section) —
  not covered by the leadership review, still NEEDS VERIFICATION.
- Onboarding timeline — flat "2–3 weeks" claim removed/qualified, but no
  replacement segmented timeline has been confirmed.
- Nav restructure (to Why Billed Right / Solutions / Who We Serve /
  Technology & Revenue Intelligence / Specialties / Client Results /
  Resources / About / Contact) — not done in this pass; homepage content
  only. Nav is a shared template affecting all 70 pages and deserves its
  own change map given the larger blast radius.
- Footer HIPAA Compliant / AAPC Certified badges (sitewide, not homepage-
  specific) — still open per `docs/website-audit.md`.
- $2B+ vs $4.2B+ inconsistency on `/private-equity/` — explicitly deferred
  by the user, tracked separately in `docs/claims-register.md`.


Preserved and reformatted from the pre-consolidation `CLAUDE.md` homepage
implementation map (archived at
`docs/archive/pre-consolidation/CLAUDE_pre-consolidation-2026-08-27.md`).
This is strategic direction, not yet executed — no homepage code/content has
changed as a result of this document. Follow `docs/PAGE_CHANGE_MAP_TEMPLATE.md`
conventions; update this file before touching homepage implementation.

## Page
- Current URL: `/` (`pages/home.html` → `dist/index.html`)
- Proposed URL: unchanged
- Primary audience: CEOs, CFOs, COOs, Revenue Cycle executives, MSO/platform leaders, PE operating partners
- Primary search intent: brand / enterprise RCM partner evaluation
- Primary conversion goal: Schedule an Executive Conversation
- Approved H1: `Transform Revenue Operations. Strengthen Financial Performance.`
- Primary topic: Enterprise Revenue Cycle Management / Revenue Performance
- Supporting semantic topics: see `docs/SEO_MARKETING_AI_STANDARD.md` → Preserved Keyword Semantics

## Section-by-Section Direction

### 1. Global Navigation — REPOSITION
Recommended primary nav: Why Billed Right; Solutions; Who We Serve; Technology & Revenue Intelligence; Specialties; Client Results; Resources; About; Contact/Schedule an Executive Conversation. Under "Who We Serve," prioritize Enterprise Physician Groups; Multi-location & Multi-specialty Organizations; MSOs & Healthcare Platforms; PE-backed Healthcare; Growing/Transforming Practices. Keep CPA/referral content accessible but not homepage-prominent. **Preserve existing indexed URLs — do not rename/remove solely for branding.**

### 2. Hero — REPOSITION (copy only, preserve component)
Eyebrow: `Enterprise Revenue Performance Partner`. H1/body/CTAs as defined in `docs/BILLED_RIGHT_WEBSITE_2026_MASTER.md`. Keep current hero visual treatment, layout, typography, animation, responsive behavior. Primary CTA visually dominant; phone/contact stays secondary utility. Do not use "practice" as the primary audience noun. No invented metric in the hero.

### 3. Top Proof Metrics — VALIDATE (keep section, rewrite labels)
Compact proof band beneath hero using only defensible metrics. See `docs/claims-register.md` rows: $2B+ billed, 94% collections increase, <24d A/R. Replace any unapproved value with `[APPROVED METRIC NEEDED]` rather than guessing.

### 4. RCM Engine — REPOSITION (preserve component architecture)
Reframe from a linear billing-task list to an operating loop: Capture & Validate → Prevent → Execute → Prioritize & Resolve → Collect & Reconcile → Learn & Optimize (feedback loop back to step 1). Section label: "THE BILLED RIGHT OPERATING MODEL." Do not claim autonomous functionality unless status is LIVE (see `docs/capability-register.md`).

### 5. Proven Results — VALIDATE (keep structure, rewrite tone)
H2: "Performance that can be measured." Use 4–6 validated metrics, not 8–10 loosely defined ones. See `docs/claims-register.md` rows for <24d A/R, <1% error ratio, <48h claim TAT, <1% no-response claims, 22d avg payment TAT, 94% retention/4-yr tenure, MGMA/HBMA benchmark. Remove hype phrasing; never convert a best-case/sample result into an "average client" claim.

### 6. Intelligent RCM / Inside Billed Right — REPOSITION
Section label: "INSIDE BILLED RIGHT." H2: "Experienced RCM. Intelligent execution. Executive visibility." Four pillars: Operational Excellence; Strategic Partnership; Revenue Intelligence; Intelligent Automation. Do not use "24/7 claim bots" or "AI-powered coding" unless the capability register marks them approved LIVE.

### 7. Our Journey — REPOSITION (final milestone only)
Keep 2006→Today timeline component; update copy. Recommended milestones: 2006 Founded around provider/practice financial performance; 2010 Expanded to end-to-end RCM; 2015 Deepened specialty-specific expertise; 2020 Scaled operations/partnerships/performance management; Today — integrating data, automation, predictive analytics, AI; Next — building toward an integrated Revenue Intelligence Platform with expert human oversight. Label "Next" as future vision explicitly (future tense).

### 8. Trust & Compliance — REWRITE IMMEDIATELY / COMPLIANCE REVIEW
Section label: "SECURITY, COMPLIANCE & GOVERNANCE." Only display individually verified controls/certifications. **Billed Right is NOT SOC 2 certified — never state, badge, or imply certification.** Never use "100% secure." See `docs/claims-register.md` Trust & Compliance rows and `docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`.

### 9. Built for Outcomes / AI — REPLACE COPY, KEEP VISUAL CONCEPT IF STRONG
Section label: "REVENUE INTELLIGENCE." H2: "Move from reactive RCM to predictive revenue operations." Four outcome cards: Predict & Prevent; Prioritize & Automate; See What Is Changing; Human Oversight Where It Matters. Remove "zero busywork," "crush denials," bot/autonomous claims, and unvalidated before/after charts until evidence is approved (see `docs/claims-register.md`). Every AI statement needs an internal capability-status tag (LIVE/LIMITED/PILOT/UNDER DEVELOPMENT/FUTURE VISION) via `docs/capability-register.md`.

### 10. Client Love / Reasons Clients Stay — REPOSITION, VALIDATE NUMBERS
H2: "Why healthcare organizations build long-term partnerships with Billed Right." Five pillars: Operational Integration; Performance Governance; Specialty & Payer Knowledge; Data-Driven Improvement; Strategic Access. Do not state "4+ years," "20+ playbooks," or "18 years payer intelligence" unless validated (see `docs/claims-register.md`).

### 11. Customized RCM Services — REFRAME AS CAPABILITIES
Section label: "END-TO-END RCM CAPABILITIES." Group into: Revenue Protection (eligibility, authorizations, documentation, coding, claim quality); Revenue Execution (charge capture, claim submission, payment posting, patient A/R); Revenue Recovery (denial management, insurance A/R, underpayment follow-up); Revenue Enablement (credentialing, contract support, reporting, account management, transformation support). Preserve existing service page URLs/cards.

### 12. Specialties — KEEP, STRENGTHEN ENTERPRISE PROOF
H2: "Specialty expertise that scales across complex organizations." Keep specialty cards/pages and current SEO URLs. Add "Multispecialty / Enterprise Groups" as a prominent path. Never add an unconfirmed specialty. Prioritize Cardiology, Pain Management, Internal Medicine, Behavioral Health per current ICP facts.

### 13. Testimonials — KEEP, REORDER, ADD ENTERPRISE PROOF
H2: "Trusted by healthcare leaders to improve revenue performance." Lead with the strongest executive-level testimonial. Prioritize quotes demonstrating financial improvement, scalability, executive visibility, strategic partnership, complex transition/integration, multi-location support. Never fabricate names/titles/org sizes/outcomes.

### 14. Free 60-Second Assessment — MOVE DOWN / SEGMENT / REWRITE FOR ENTERPRISE
Enterprise variant: H2 "Where is your revenue operation leaving performance on the table?" CTA: "Request a Revenue Performance Assessment." Keep the 60-second calculator as a separate tool under Resources for smaller practices — do not feature the "<10 providers" benchmark in the enterprise flow.

### 15. Free Tools — KEEP, REWRITE TONE, SEGMENT
H2: "Revenue cycle tools and decision resources." Preserve tools/URLs; reframe copy away from small-practice tone. Consider "Executive Resources" alongside "Practice Tools."

### 16. Client Success Stories — KEEP FRAMEWORK, VALIDATE OR REPLACE DATA
H2: "Measurable improvement in complex revenue environments." Each case card needs: org type/size (if approved), starting challenge, intervention, measurement period, 2–3 validated outcomes, short executive quote, link to full methodology. See `docs/claims-register.md` for the Cardiology/Behavioral Health/Multispecialty case-study rows — publish only as verified, permissioned case studies; mark any composite/illustrative example clearly.

### 17. Comparison — KEEP IDEA, REWRITE FOR ENTERPRISE, VALIDATE GUARANTEE
H2: "A different operating model for Revenue Cycle Management." Rows: outcome accountability; specialty/payer expertise; executive visibility & governance; scalable operating capacity; data/Revenue Intelligence; intelligent automation; human exception management; EHR/PM integration; continuous improvement; credentialing/support. Columns: In-house / Traditional Outsourced RCM / Billed Right. No unverifiable negative competitor claims. 120-day money-back guarantee requires legal approval before inclusion (see claims register).

### 18. Technology Ecosystem — KEEP, EXPAND WITH ACCURACY
H2: "Designed to work within your healthcare technology ecosystem." Separate "platforms we work in" from "technical integration methods available." Do not infer API/HL7/FHIR integration just because an EHR is supported — only list what engineering confirms.

### 19. Onboarding — KEEP, ENTERPRISE REFRAME, VALIDATE TIMELINE
H2: "A structured transition designed to protect revenue continuity." Steps: Discovery & Baseline; Transition Design; Configuration & Readiness; Controlled Go-Live; Stabilize & Optimize. Remove the universal "2–3 week" claim from the enterprise flow unless a segmented, validated definition is approved.

### 20. Latest Resources — KEEP, EXPAND EXECUTIVE THOUGHT LEADERSHIP, VALIDATE
H2: "Insights for healthcare financial and operational leaders." Priority themes match `docs/CONTENT_AND_BLOG_STANDARD.md`. "90% of denied claims recoverable" needs a sourced citation before publishing (see claims register) — do not present as a Billed Right-specific result.

### 21. Final CTA & Footer — REPLACE COPY, KEEP CONVERSION COMPONENT
H2: "Ready to strengthen your revenue operation?" Primary CTA: Schedule an Executive Conversation. Secondary CTA: Request a Revenue Performance Assessment. Remove "No sales pitch" / "trusted billing advisors" language — use strategic-partner language consistently. Footer structure per `docs/TECHNICAL_SEO_AND_AI_SEARCH_STANDARD.md` → Footer.

## VALIDATE (roll-up)
All items above with a VALIDATE/claims-register cross-reference. See `docs/claims-register.md` for the authoritative, trackable list — do not duplicate claim tracking here.

## SEO
- Title / meta description: must represent RCM + enterprise financial-performance positioning, not medical billing alone
- Canonical: `/`
- Schema: Organization, WebSite/WebPage
- Sitemap status: included

## MOBILE CONVERSION
- Primary mobile CTA: Schedule an Executive Conversation
- One-click call: secondary, non-dominant
- Sticky CTA: non-obstructive if used

## COMPONENT CHANGES
No component/architecture rebuild implied by this map — copy, labeling, and ordering changes within existing components only, per `CLAUDE.md` and `docs/BILLED_RIGHT_WEBSITE_2026_MASTER.md`. Exact files/routes to be identified at implementation time.

## ACCEPTANCE TEST
Would a CEO/CFO/COO of a 300-provider group conclude within seconds that Billed Right is an experienced enterprise RCM organization, that the promise is stronger financial performance, and that technology/AI are mechanisms rather than the product? See full 14-point test preserved in `docs/PAGE_CHANGE_MAP_TEMPLATE.md`.
