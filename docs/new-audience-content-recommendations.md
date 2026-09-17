# Content Gap Recommendations — Target Audience: C-Suite Decision Makers (CEO/CFO/COO)

**Scope:** This pass evaluates the existing site structure against the needs of executive buyers (CEOs, CFOs, COOs) at organizations matching the Primary ICP (25–100 providers, $25M–$250M revenue) as well as PE-backed platform executives, per `CLAUDE.md`. Recommendation-only — nothing below has been built.

**Method:**
1. Mapped every page's title + H1/H2 structure (no full-body reads) across `pages/*.html` and `content/blog/*.md` frontmatter titles (176 posts).
2. Identified coverage/gaps from that structural map alone.
3. Read full text (stripped of markup) of the 8 pages most relevant to an executive audience: [home.html](pages/home.html), [private-equity/index.html](pages/private-equity/index.html), [why-billed-right.html](pages/why-billed-right.html), [resources.html](pages/resources.html), [recognition/index.html](pages/recognition/index.html), [case-studies.html](pages/case-studies.html), [credentialing.html](pages/credentialing.html), [faq.html](pages/faq.html).

---

## Current Coverage Summary

**Strong, already-executive-grade:**
- [home.html](pages/home.html) — Leads with P&L framing ("Numbers that move the P&L, not vanity metrics"), MGMA/HBMA benchmarking, an explicit "Weak Executive Visibility" pain point, and a "Revenue Intelligence" roadmap (Auto-coding / Real-time / Predictive / Auto-app). This is genuinely CEO/CFO-toned copy, not generic vendor marketing.
- [private-equity/index.html](pages/private-equity/index.html) — A full persona-specific landing page for PE operating partners: EBITDA impact, exit readiness, portfolio reporting visibility, three engagement tiers (Advisory / Platform / Asset-level), and investment-lifecycle staging (Diligence → Transition → Value Creation). This is the most sophisticated executive asset on the site.
- [recognition/index.html](pages/recognition/index.html) — ISO 9001, ISO 27001, HIPAA compliance detail with an FAQ block, correctly stops short of any SOC 2 claim (consistent with `docs/BILLED_RIGHT_FACTS_AND_GUARDRAILS.md`).
- [why-billed-right.html](pages/why-billed-right.html) — Includes a CEO-attributed testimonial (Pain Management) and COO-relevant "Relationships"/"Advisor" value pillars.
- [case-studies.html](pages/case-studies.html) — Quantified before/after results (collections %, A/R days, denial reduction) with named roles (CEO, COO, Practice Administrator) — the right format for executive proof, just thin on specialty coverage (see gaps).
- [resources.html](pages/resources.html) — 7 self-serve tools ("No email gate to browse"), well-matched to an operational buyer, but none are framed for a financial executive (see gaps).

**Blog (176 posts):** Overwhelmingly operational/tactical — KPI tracking, denial coding, staff training, compliance checklists, credentialing how-tos. A small handful touch executive-adjacent financial topics (*Financial Literacy in Healthcare*, *Why Financial Benchmarks Should Guide Every RCM Review*, *Understanding Revenue Cycle Management in Large Practices*, *Master Payer Contract Negotiation*), but none address M&A integration, multi-site standardization economics, or board-level reporting — the topics a CEO/CFO/COO actually searches for.

---

## Content Gaps Identified

1. **No case studies for two of the four priority specialties.** `case-studies.html` covers Cardiology (x2), Behavioral Health, Orthopedics, Pediatrics, and Multispecialty — but **Pain Management** and **Internal Medicine** (both explicit priority specialties in `CLAUDE.md`) have zero case studies, while Orthopedics and Pediatrics (non-priority) do. An Internal Medicine or Pain Management CFO evaluating the site sees no proof point in their own specialty.

2. **No calculator or tool speaks the language of a financial executive.** All 7 tools in `resources.html` (Credentialing Timeline, Revenue Leak, Billing ROI, Denial Cost, CAQH Reminder, Enrollment Tracker, Billing Cost) are operational/staff-level. None model **EBITDA impact**, **multi-site consolidation savings**, or **cost-of-capital / opportunity-cost framing** — despite `private-equity/index.html` explicitly naming EBITDA impact as a core investment thesis. The PE landing page makes the claim; there's no self-serve tool backing it up.

3. **No downloadable board/executive reporting artifact.** `home.html` names "Weak Executive Visibility" as a top pain point and both `home.html` and `private-equity/index.html` reference dashboards and "consolidated reporting," but nothing in `resources.html` or elsewhere lets a prospect see a sample board-level KPI report or dashboard mockup before engaging.

4. **No persona landing page for a non-PE, multi-site health system or group-practice executive.** `private-equity/index.html` proves the site can build a sharp persona page. There is no equivalent for a CFO/COO at a growing, non-PE-backed multi-site group (the core ICP per `CLAUDE.md`) who cares about scaling revenue ops across locations/specialties without an investor lens.

5. **No M&A / practice-acquisition integration content.** `home.html` names "Acquisition Integration" as a Where We Help pillar and `private-equity/index.html` names a "Transition" investment-lifecycle stage, but there is no standalone guide, checklist, or landing page on integrating an acquired practice's billing operations — a topic a growing organization's CEO/COO would specifically search for and one that reinforces the "Growth & Scale" pillar already on the homepage.

6. **No published, citable benchmark data.** The site repeatedly claims to beat MGMA/HBMA benchmarks (`<24d` A/R vs. "industry 40+ days", `<1%` error ratio) but there is no standalone, linkable benchmark report presenting this data by specialty/revenue band. This is both a content gap and a missed AI-discoverability opportunity — a structured, citable benchmark asset is exactly the kind of source AI answer engines (and analysts, and journalists) pull from and link to, per `docs/TECHNICAL_SEO_AND_AI_SEARCH_STANDARD.md` priorities.

7. **FAQ is practice-manager-level, not executive-level.** All 17 questions in `faq.html` concern claim mechanics, staffing, and system compatibility. None address financial-executive concerns: contract terms/exit clauses, pricing model impact on EBITDA, how RCM performance is reported to a board, or how a transition is de-risked during a merger.

---

## Recommended New Resources

### 1. Case Study: Pain Management Practice
- **Format:** Case study (page), matching existing `pages/case-studies/*/index.html` template
- **Rationale:** Pain Management is one of four named priority specialties, and `why-billed-right.html` already carries a Pain Management CEO testimonial — meaning the raw material/relationship likely exists to source a real (or composite, HIPAA-safe per the existing pattern) result. Closing this gap directly answers "does this company understand practices like mine" for a segment currently proven only by a passing quote, not a full result set.
- **Target URL:** `/case-studies/pain-management/`

### 2. Case Study: Internal Medicine Practice
- **Format:** Case study (page), same template
- **Rationale:** Same logic as above — Internal Medicine is a named priority specialty with zero case-study representation, while two non-priority specialties (Orthopedics, Pediatrics) currently have one each. Parity here removes an obvious credibility gap for a segment the business has explicitly prioritized.
- **Target URL:** `/case-studies/internal-medicine/`

### 3. EBITDA Impact Calculator
- **Format:** Calculator, added to `resources.html`'s tool grid
- **Rationale:** `private-equity/index.html` builds its entire investment case on EBITDA impact ("Billing inefficiencies cut into EBITDA margins directly") but backs it with narrative only. A calculator that converts denial rate, A/R days, and net collection rate into an estimated EBITDA-margin impact — using the same "no email required" self-serve pattern as the existing Revenue Leak Assessment — gives PE operating partners and CFOs a quantified, shareable number to bring into an internal investment-committee or board conversation, and gives the private-equity landing page a concrete tool to link to instead of just prose.
- **Target URL:** `/resources/ebitda-impact-calculator/` (linked prominently from `/private-equity/`)

### 4. Guide: RCM Integration Playbook for Practice Acquisitions
- **Format:** Guide (gated PDF download, following the existing Enrollment Tracker Template's download pattern)
- **Rationale:** Both `home.html` ("Acquisition Integration... Newly acquired practices with inconsistent billing standards that create revenue gaps") and `private-equity/index.html` ("Transition: Integration planning...") name this exact problem, but a CEO/COO mid-acquisition has nothing concrete to download today. A step-by-step playbook (credentialing timeline, EHR/PM standardization, claim-edit rule migration, reporting consolidation) turns an existing sales narrative into a lead-generating asset and gives sales a natural "want the full playbook?" close on private-equity and growth-focused conversations.
- **Target URL:** `/resources/rcm-integration-playbook/`

### 5. Landing Page: Revenue Cycle Partner for Multi-Site Health Systems & Groups
- **Format:** Landing page, structured like `private-equity/index.html` but for a non-PE buyer
- **Rationale:** `private-equity/index.html` proves the site can execute a sharp, persona-specific executive page — but it only exists for the investor audience. The Primary ICP in `CLAUDE.md` (25–100 providers, $25M–$250M revenue) is far more likely to be an independently owned or health-system-affiliated multi-site group than a PE portfolio company. This page would speak directly to that CEO/COO's actual concerns — standardizing billing across locations, executive visibility across sites, scaling without adding headcount — using the same "Where We Help" pillars already on the homepage (Growth & Scale, Performance Improvement, Transformation) but built out at persona-page depth instead of a homepage summary.
- **Target URL:** `/multi-site-groups/` or `/executive-partners/`

### 6. Report: Annual RCM Performance Benchmark Report
- **Format:** Guide/report (gated PDF + a public summary landing page for SEO/AI discoverability)
- **Rationale:** The site already claims specific, favorable benchmark numbers against MGMA/HBMA ("<24d" A/R vs. "industry 40+ days," <1% error ratio, 94-97% first-pass) scattered across `home.html`, `why-billed-right.html`, and `faq.html`. Consolidating this into one citable, dated, methodology-backed report — broken out by specialty and revenue band where the underlying data supports it — turns a marketing claim into a linkable, quotable source. This directly serves the "AI Discoverability" and "Executive Credibility" mandate in `CLAUDE.md`: a structured benchmark report with clear sourcing is the kind of asset AI answer engines and industry press cite, and it gives a CFO a defensible number to bring to their own board when justifying an RCM change.
- **Target URL:** `/resources/rcm-benchmark-report/` (summary page), with the full report as a gated download

### 7. FAQ Section: "For Executives & Investors"
- **Format:** New FAQ category added to the existing `faq.html` structure (which already has category tabs: About Billed Right / Services & Specialties / Claims & Billing / Our Team / Compliance & Security)
- **Rationale:** All 17 existing FAQ entries are operational (claim timing, staffing model, system compatibility). Adding a category with questions a CFO/COO/board actually asks before signing — "How is RCM performance reported to leadership?", "What happens to billing continuity during a merger or system migration?", "How does the pricing model affect our margins as we scale?", "What's the transition timeline when switching vendors mid-fiscal-year?" — closes the FAQ gap cheaply (no new page, no new template) while giving AI search systems and skimming executives direct, citable answers to the questions that actually govern a vendor decision at their level.
- **Target URL:** No new URL — new tab/category within `/faq/`

---

## Sequencing Note (not a build instruction — for planning only)

If prioritized, items #1 and #2 (the two missing priority-specialty case studies) are the lowest-effort, highest-credibility-per-dollar fixes since they reuse an existing template exactly. Item #3 (EBITDA calculator) and #5 (multi-site landing page) most directly extend proven-successful patterns already on the site (`resources.html`'s calculator grid and `private-equity/index.html`'s persona-page approach, respectively). Per `CLAUDE.md`, any of these should still go through the standard change-map process (`docs/change-maps/`) and claims/capability verification before being built.
