# Change Map — Pain Management Specialty Page

`/specialties/pain-management-rcm-services/` (`pages/pain-management-rcm-services.html`)

## Implementation Log

**2026-09-15 — Full rebuild per
`docs/specialty-pages/Pain Management/Billed_Right_Pain_Management_FINAL_V2_Cumulative_RCM_SEO_AI_Implementation.md`
(FINAL V2 — single source of truth, supersedes prior Pain Management docs).**

Rebuilt the page from a CPT/coding-heavy specialty explainer into a 16-section
commercial RCM pillar page (the doc's expanded architecture, built on top of
the V2 framework's 13-section base plus three Pain-Management-specific major
sections): Hero+Proof, Why Financially Different, Revenue Leaks, How Billed
Right Helps, Intelligent RCM, Authorization & Insurance Verification,
Workers' Comp & Accident Cases, Core RCM vs. Additional/Holistic, Common
Denials, EMR & Technology, Verified KPIs, Data-to-Decisions, Built for
Growth, Real Client Perspective, Resources, Buyer FAQs, Final CTA. All
Cumulative Update lessons from Psychiatry/Cardiology were applied from the
start (single final conversion section, no artificial "Reviewed by," KPI
governance, real-proof hierarchy) rather than requiring a follow-up cleanup
pass.

### RETAIN
- Established URL (`/specialties/pain-management-rcm-services/`).
- Existing verified Pain Management KPIs (97% collections, 20-day A/R
  reduction, 1% error ratio, <48hr TAT, <1% no-response, 28-day payment
  TAT) — values and labels unchanged from the live page, per the doc's KPI
  Governance rule (no relabeling without Arun/internal sign-off on this
  pass). Only the rolling "Years of experience" tile was replaced with
  "Since 2006 — Pain Management RCM Experience," which is an explicitly
  locked instruction in the doc, not a discretionary edit.
- Genuine California Pain Management testimonial (CEO, Pain Management —
  CA) — kept verbatim from `pages/why-billed-right.html`, not rewritten or
  given invented attribution detail.
- Denial-table concepts (authorization, eligibility, documentation,
  procedure-related, payer-policy, Workers' Comp/accident-case,
  underpayments) — restructured into the doc's exact buyer-level table.

### REWRITE
- Hero, opening copy, "Why Different," Revenue Leaks, denial table, EMR
  language, FAQs, final CTA — replaced with the doc's locked copy, adapted
  into existing page CSS components (`.br-services-grid`, `.br-feature-list`,
  `.br-compare-table`, `.br-tech-grid`, `.br-faq-item`, `.br-callout`).
- Lead form: merged First/Last Name into a single required `name` field,
  removed the "Number of Providers" dropdown, reframed from "Download Our
  Brochure" to "Schedule a Revenue Cycle Assessment." Form
  name/`formSource` renamed `pain-management-brochure-request`/
  `pain-management-brochure` → `pain-management-assessment-request`/
  `pain-management-assessment` so `zoho-lead.js`'s `isBrochureForm` check
  (keyed off the `-brochure` suffix) no longer mislabels this as a
  brochure-download lead.

### NEW
- Immediate-proof hero stat row (Since 2006, Workers' Comp experience,
  Multi-Provider support, AI/Automation).
- **Authorization & Insurance Verification** — major new section (doc §11)
  framing authorization/eligibility as upstream actions with downstream
  financial impact; Prior Authorization clearly labeled as a separately
  scoped Holistic Service, not core RCM.
- **Workers' Compensation & Accident Cases** — major new section (doc §12),
  the primary Pain Management differentiator called out in the doc. Kept as
  a supporting capability (per Cumulative Update #6) rather than dominating
  the hero, SEO title or majority of the page. Guardrail callout included:
  no legal advice, no liability determination, no payment guarantee, no
  unsupported recovery-rate claims, no implication that every case follows
  the same process.
- Specialty-specific Intelligent RCM section (claim quality → denial
  pattern detection → A/R prioritization → eligibility automation →
  authorization exceptions where separately scoped → Workers' Comp/
  accident-case exception identification → Data-to-Decisions), passing the
  Intelligent RCM Quality Test (each capability states what it
  detects/prioritizes/automates, what it surfaces, what the human team does
  with it, and what revenue-cycle problem it addresses).
- Data-to-Decisions and Built-for-Growth sections (did not exist before).
- EMR & Technology section naming the three locked platforms
  (eClinicalWorks, IMS, AdvancedMD) — deliberately a flatter, single
  tech-grid treatment (no dedicated "flagship EMR" section like Cardiology's
  eClinicalWorks section), per the doc's explicit instruction not to
  position eClinicalWorks as a dominant or singular Pain Management
  differentiator.
- "Additional / Holistic Services" callout distinguishing Prior
  Authorization, Medical Coding, Credentialing, Documentation Management,
  and Contract Renegotiation from core RCM.

### REMOVE / REDUCE
- All CPT/HCPCS code references (62322–62323, 64483–64484, 64490–64495,
  77003, 63650–63685, 99213–99215) and the associated modifier/fluoroscopy/
  injection-level coding education, "Payer-Specific Considerations"
  paragraph, and CPT-driven FAQ set — removed entirely rather than reduced,
  consistent with the doc's explicit instruction to avoid CPT lookup/
  modifier-tutorial content as the primary page identity.
- "18+ years in pain management RCM" (footer line) — replaced with "Since
  2006" per the locked evergreen-language decision; no rolling-year claim
  remains anywhere on the page.
- "Reviewed by Billed Right's pain management billing team..." — replaced
  with "Billed Right has supported Pain Management revenue cycle management
  since 2006," per Cumulative Update #2 (implemented from the start, not as
  a later cleanup).
- "Download Our Brochure" as the primary conversion framing (see REWRITE).
- Duplicate ending CTAs — built as exactly **one** final conversion section
  from the start (per Cumulative Update #1), with Our Specialties moved to
  its own section immediately below and no other major CTA after it.

### CASE STUDY / PROOF HIERARCHY (doc §19, Cumulative Update #4)
Checked `pages/case-studies/` — only Allergy, Cardiology, Credentialing and
Primary Care case studies exist. **No real, approved Pain Management case
study exists in the project**, confirming the gap the user flagged. The
previously live page's Resources card ("Pain Management Practice Reduces
Denials and Recovers Lost Revenue") explicitly self-described as "a
composite look" — this has been **removed entirely and not replaced with
any illustrative/hypothetical placeholder.** This is stricter than the
Psychiatry treatment (which used a clearly labeled "Illustrative Scenario"
as a fallback) because this doc's own Cumulative Update #4 explicitly
instructs: "remove the composite case study and elevate the approved
authentic California Pain Management testimonial" — no hypothetical
replacement offered as an option here.

**Outcome: no case-study section on the page.** The "Real Client
Perspective" section carries only the genuine testimonial. **This remains a
confirmed gap** — if Billed Right develops a real, approved Pain Management
case study in the future, the doc's structure (starting situation →
challenge → Billed Right action → verified outcome → link to full case
study) is ready to receive it, following the same pattern used for
Cardiology's real case study.

### TESTIMONIAL (doc §19, Cumulative Update #4)
Real Pain Management testimonial exists (sourced from
`pages/why-billed-right.html`) and was elevated to its own section. Kept
exactly as approved: **"CEO, Pain Management — CA."**

**Flag for Marketing/Legal:** `docs/claims-register.md` lists this exact
testimonial as `NEEDS VERIFICATION` (row: "Testimonial — 'CEO, Pain
Management, CA'" — homepage/Testimonials, HOLD pending permission,
wording, and active-client-relationship confirmation). This is the same
unresolved HOLD pattern already flagged for the Psychiatry and Cardiology
testimonials. The user's task instructions and this implementation doc both
explicitly direct using this testimonial, so it has been used here (as it
already appears on `pages/why-billed-right.html` and the prior live version
of this page) — but it should not be treated as a fully cleared claim until
Client Success/Legal resolves the register HOLD. Attribution was **not**
upgraded to a named "Dr. [First Name]" format, since only a role-based
attribution ("CEO") is on file/approved — inventing a name or city detail
was avoided.

### AI / GUARDRAILS
- No "revolutionary AI," "fully autonomous RCM," "eliminates denials," or
  "guaranteed faster payments" language used.
- No future-roadmap capability presented as live.
- Every Intelligent RCM capability answers the four-question quality test
  (detect/prioritize/automate what; surfaces what; human team does what;
  addresses what revenue-cycle problem).
- No SOC 2 claim or badge anywhere on the page.
- No PE-backed claim (doc explicitly said not to claim PE-backed Pain
  Management expertise unless separately validated — omitted entirely,
  unlike Cardiology's page which has an approved PE-backed section).

### SEO
- Title: `Pain Management Revenue Cycle Management & Billing Services |
  Billed Right` (doc's primary recommended title, not the shorter
  alternative).
- Meta description: doc's exact locked copy — "Pain Management RCM for
  growing and multi-provider organizations. Improve A/R, denials, payer
  visibility and revenue-cycle performance with Billed Right." (155
  characters, fits typical SERP display width without truncation).
- Canonical/URL: unchanged.
- Schema: `Service` name/description rewritten to reflect RCM positioning
  (claim quality, denial pattern detection, A/R prioritization, eligibility
  workflows, Workers' Comp/accident-case experience, Data-to-Decisions;
  Prior Authorization/Medical Coding called out as separately scoped)
  instead of the prior CPT-heavy description. `FAQPage` replaced with the
  doc's 9 buyer-intent questions (§21). `BreadcrumbList` and org-level
  `Organization`/`MedicalBusiness`/`WebSite` nodes unchanged (shared
  site-wide schema, out of this page's scope).
- Internal links added/kept: `/services/authorizations/`,
  `/services/medical-coding/`, `/services/credentialing/`,
  `/services/documentation-management/`,
  `/services/contract-renegotiation/`, `/services/denial-management/`,
  `/services/ar-follow-up/`, `/services/`, `/contact/`, `/testimonials/`.

## Final QA Checklist Results
(Section 33 of the implementation doc — see full pass/fail/unconfirmed
report delivered in-conversation.) Summary: all implementable content,
guardrail, structural, and SEO items **pass**. Zoho lead creation, CRM
routing, and mobile carrier-level click-to-call behavior are **unconfirmed**
— cannot be verified in this local/static environment (no live Netlify
Functions/Zoho endpoint), consistent with every prior specialty-page QA
report.

## Not in scope / not touched
- `netlify/functions/zoho-lead.js`, `build.py`, `templates/nav-template.html`,
  `templates/footer-template.html`, `sitemap.xml` — unchanged.
- No other specialty page touched (Cardiology remains frozen per its own
  change map; Psychiatry unchanged).
- `pages/thank-you/pain-management/` — left as-is; shared generic
  thank-you template, not named in the implementation doc's section list.
