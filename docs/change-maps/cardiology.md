# Change Map — Cardiology Specialty Page

`/specialties/cardiology-rcm-services/` (`pages/cardiology-rcm-services.html`)

## Implementation Log

**2026-09-15 — Final cleanup pass (page frozen after this).** Targeted
revision only, per direct chat instructions — no rebuild, no SEO/content
changes beyond what's listed:

1. **Consolidated the two ending conversion sections into one.** Merged
   the "Talk to a Cardiology RCM Expert" form section and the separate
   "Find Out Where..." Final CTA into a single section with the exact
   requested heading/copy. Form fields unchanged (Name, Work Email,
   Phone, Organization/Practice — `specialty` still captured via hidden
   input). Added "Prefer to talk? Talk to a Cardiology RCM Expert —
   407-217-9281" as a one-click `tel:` secondary conversion beneath the
   submit button (reused the page's existing "Talk to a Cardiology RCM
   Expert" phrase rather than inventing new copy). **Our Specialties**
   moved to its own section directly below, with no CTA in it and no
   major CTA after it.
2. **"Reviewed by" statement replaced** with the exact requested copy:
   "Billed Right has supported Cardiology revenue cycle management
   since 2006."
3. **KPI labels — conservative pass only.** The request explicitly
   gates the fuller relabel ("Collection Rate," adding "Days" to the
   28-figure) on Arun confirming what each number specifically measures,
   and says not to add "Net," "Days," or other definitions without that
   confirmation. Since that confirmation isn't available in this
   session, applied only safe, non-definitional grammar cleanup to the
   4 labels named as awkward — "Achieving Collections up to" →
   "Collections Up To," "Reduction in days in AR" → "Reduction in Days
   in A/R," "Reduce 'No Response'" → "No-Response Reduction," "TAT for
   Payment" → "Payment TAT" — none of which assert a specific metric
   definition beyond what the original label already implied. **All 7
   KPI values themselves are byte-identical to before.** Flagging for
   Marketing: the deeper relabel (confirming 97% is specifically
   "Collection Rate" vs. some other definition, confirming the 28-figure
   is in days) still needs Arun's sign-off before those exact labels
   from the request's examples can be applied.
4. **Prior Authorization language in the case study — validated, not
   changed, plus a scope note added.** Confirmed both statements
   ("took full ownership of the prior authorization workflow" and
   "auth-related denials on interventional procedures eliminated")
   against the source: they're pulled directly from the published,
   verified case study page (`pages/case-studies/cardiology/index.html`)
   and match `docs/claims-register.md`'s VERIFIED entry for this case
   study word-for-word. No factual issue found. Added one clarifying
   sentence directly beneath the case-study card: "Prior Authorization
   support was part of this client's specific engagement scope. It is
   not automatically included in Billed Right's standard core RCM
   service—see Additional / Add-On Services above." — addresses the
   scoping concern without altering the verified facts.
5. **Intelligent RCM section: untouched**, confirmed via grep (PREVENT/
   DETECT/PRIORITIZE/AUTOMATE/ACT/LEARN and all specific capability
   language still present verbatim; no banned AI phrases introduced).
6. **No other SEO/content rewrite.** H1, meta title/description,
   canonical, schema, eClinicalWorks section, PE-backed/growth section,
   Data-to-Decisions, FAQs, and overall architecture confirmed unchanged
   via DOM inspection after build.

**QA after deployment:** desktop and mobile layouts checked in-browser;
form payload confirmed correct (merged `name`, hidden `specialty`,
`page_url` autofill); `tel:` link confirmed one-click; internal links
(eClinicalWorks page, real case-study page) confirmed present; schema
confirmed still valid JSON-LD; no console errors. **Not verified**
(same limitation as prior passes): live Zoho CRM lead creation, Sales
notification, and lead routing — no live Netlify Functions/Zoho
endpoint available in this environment; client-side payload structure
is correct.

**Page frozen after this pass per direct instruction.** Further
Cardiology SEO work should go into supporting authority content and
internal linking (per the original implementation doc's Section 30
content cluster), not further edits to this page.

---

**2026-09-15 — Flagship rebuild per
`docs/specialty-pages/Billed_Right_Specialty_Page_Framework_V2.md` and
`docs/specialty-pages/cardiology/Billed_Right_Cardiology_Flagship_RCM_SEO_Implementation_V2_AI_Automation.md`.**

This page was explicitly directed to go beyond the standard V2 13-section
template ("Do not treat this as a normal specialty-page rewrite... Cardiology
should establish the Billed Right specialty authority model"). The
implementation doc's own Section 4 architecture expands several V2 slots
into dedicated sections (Intelligent RCM/AI, Core RCM vs. Add-On, eCW,
Other EMRs, Built for Any Size, PE-Backed/Acquisition are each their own
section rather than folded together). Built to that richer 17-section
architecture; all 13 V2 framework concepts are present, several just get
their own dedicated section here as directed.

### RETAIN
- Existing verified Cardiology KPIs (97% collections, 20-day A/R
  reduction, 1% error ratio, <48hr TAT, <1% no-response, 28-day payment
  TAT) — values unchanged, per locked decision, pending Arun's refresh.
- Strongest existing denial content — restructured into the Denial /
  Root Cause / Billed Right Approach table using the doc's exact
  7-row table (verbatim).
- Existing URL, specialty cross-link list, resources-section pattern.

### REWRITE
- Hero, "Why Different," Revenue Leaks, Denials presentation, FAQs,
  Final CTA — per the implementation doc's provided copy.
- "Payer-Specific Considerations" paragraph and the FAQ set were both
  heavily CPT-code-dense (cited 93000, 93306, 93454, 99213-99215,
  modifiers -26/-59/-76) — removed entirely rather than reduced, since
  the new Denials table and "Why Different" section already demonstrate
  the same expertise conceptually, without codes.
- Lead form: merged First/Last Name into a single required `name`
  field, removed "Number of Providers," reframed from "Download Our
  Brochure" to "Schedule a Revenue Cycle Assessment." Netlify form
  name/`formSource` renamed `cardiology-brochure-request`/
  `cardiology-brochure` → `cardiology-assessment-request`/
  `cardiology-assessment` (same reasoning as the Psychiatry rebuild —
  `zoho-lead.js`'s `isBrochureForm` check keys off the `-brochure`
  suffix, and this is no longer a brochure-download form). Relocated to
  its own anchored section (`#cardiology-assessment-form`) rather than
  beside the hero.

### NEW (flagship sections not on Psychiatry's page)
- **Intelligent RCM: AI & Automation** — 7 capability write-ups (claim
  quality, denial pattern detection, A/R prioritization, eligibility
  automation, authorization risk tracking, exception surfacing,
  Data-to-Decisions) plus the doc's exact PREVENT/DETECT/PRIORITIZE/
  AUTOMATE/ACT/LEARN 6-part visual and required callout ("AI does not
  replace experienced Cardiology revenue-cycle professionals..."). Every
  banned phrase from the doc's guardrail list (revolutionary AI,
  cutting-edge, next-generation, fully autonomous, zero-touch,
  eliminates denials, guaranteed faster payments) — confirmed absent via
  grep.
- **eClinicalWorks competitive-advantage section** — standalone,
  prominent, linking to `/services/eclinicalworks-billing-services/`.
- **Other EMR/Technology section** — athenahealth, CareCloud, IMS only
  (per this doc — deliberately *not* Psychiatry's 6-platform list,
  since CentralReach etc. aren't Cardiology-relevant per this doc).
- **Built for Any Size** and **PE-Backed & Fast-Growing Cardiology** as
  two distinct sections (doc explicitly separates them, unlike
  Psychiatry's combined "Built for Growth"), including the 7-question
  acquisition/integration use-case list verbatim.
- **Additional/Holistic Services** callout with linked services
  (Medical Coding, Prior Authorization, Credentialing, Documentation
  Management, Contract Renegotiation).
- Data-to-Decisions section, including "Procedure/Service-Line Trends"
  (a Cardiology-specific addition not present in Psychiatry's list).

### REMOVE / REDUCE
- All CPT/HCPCS/modifier references (93000, 93306, 93454, 99213-99215,
  -26/-59/-76) — previously in the FAQ schema, visible FAQs, and the
  "Payer-Specific Considerations" paragraph.
- "18+ years in cardiology RCM" (page footer note) and the KPI grid's
  "20 / Years of experience" tile — both replaced with "Since 2006" /
  "Cardiology RCM Experience," per the same rolling-year-claim guardrail
  used on Psychiatry. This is the one KPI-grid value changed; all other
  KPI numbers are untouched.
- The old Resources-section "Case Study" teaser card, which was
  literally mislabeled — see CASE STUDY below.

## CASE STUDY (per the same rule as Psychiatry)
**Outcome: a real, approved Cardiology case study already exists — used
it, per the instruction's first-priority outcome.** Confirmed via
`docs/claims-register.md` (row: "Cardiology case study — claims
submitted 24-72h / PA denials eliminated / coding accuracy improved" —
status **VERIFIED**, sourced from `pages/case-studies/cardiology/index.html`,
a 4-provider Central Florida practice, $1.7M baseline, engaged 2015).

The **previously live page had this backwards**: its only case-study
presence was a small Resources teaser card titled "Cardiology Practice
Reduces Denials and Recovers Lost Revenue" whose own description read
"A composite look at how a multi-provider cardiology practice tightened
documentation..." — i.e., a real, verified case study existed elsewhere
on the site while this page displayed a composite-labeled placeholder
in its place and linked to the generic `/case-studies/` hub instead of
the real page.

**Fixed:** built a full "Real Cardiology Revenue-Cycle Experience"
section using the doc's exact recommended structure (Starting Situation
→ Challenges → Billed Right Action → Results), using **only** facts
pulled directly from the published, verified case study page — no
invented details. Results are stated exactly as the source page states
them (qualitative — "eliminated," "established," "improved," "positioned
for" — no percentage figures), matching the claims-register's own
instruction ("Present as qualitative outcomes only, no percentage
figures"). Links to `/case-studies/cardiology/` (the real page), not
the generic hub. Removed the old mislabeled Resources teaser card
entirely to avoid duplicating/undercutting the new dedicated section.

## TESTIMONIAL
**Outcome: no genuine, approved, Cardiology-specific testimonial
currently exists — reporting this rather than presenting one.** The
previously live page's testimonial section displayed a quote attributed
to "Manager, Multi-Specialty Group, CA" — not from a Cardiology
practice at all, and the same quote is independently flagged in
`docs/claims-register.md` as `NEEDS VERIFICATION` / `HOLD pending
permission and attribution confirmation`. Presenting it here as "the
Cardiology testimonial" would have misrepresented a generic,
unverified, non-Cardiology quote as specialty-specific proof.

**Removed it from this page** rather than keep a misattributed
testimonial or invent a properly-attributed one. The real case study's
own "Why This Client Chose Billed Right" section (on the case-study
page itself) already carries authentic client sentiment tied to the one
verified Cardiology client. **Action item for Marketing:** source a
real, approved, Cardiology-specific testimonial (ideally from the
Central Florida case-study client or another Cardiology client) using
the `Dr. [First Name] — Cardiology — [City, State]` attribution format
once permission is confirmed.

## FAQ scope note
Excluded one FAQ from the doc's Section 21 list: "Can Billed Right
manage legacy A/R during a transition or acquisition?" — the doc itself
says "If not yet confirmed, do not publish this FAQ until internally
validated." No confirmation of this capability was found in
`docs/capability-register.md` or `docs/claims-register.md`, so it was
left out. Published the other 12 of the doc's 13 FAQs.

## SEO
- Title: `Cardiology Revenue Cycle Management & Billing Services | Billed Right`
  (doc's recommended starting title, used verbatim).
- Meta description: doc's exact recommended copy, verbatim.
- Canonical/URL: unchanged (`/specialties/cardiology-rcm-services/`).
- Schema: `Service` name/description rewritten to name the any-size/
  PE-backed/eClinicalWorks positioning and remove the coding-inclusion
  implication; `FAQPage` replaced with the 12 published buyer-intent
  questions; `BreadcrumbList` and org-level schema nodes unchanged.
- Internal links added: `/services/eclinicalworks-billing-services/`,
  `/case-studies/cardiology/`, `/services/denial-management/`,
  `/services/ar-follow-up/`, `/services/medical-coding/`,
  `/services/authorizations/`, `/services/credentialing/`,
  `/services/documentation-management/`,
  `/services/contract-renegotiation/`, `/contact/`.

## Not in scope / not touched
- `netlify/functions/zoho-lead.js`, `build.py`, `templates/nav-template.html`,
  `templates/footer-template.html`, `sitemap.xml`, `pages/case-studies/cardiology/index.html`
  (the real case study page itself — read from, not edited) — all unchanged.
- No other specialty page touched.
- `pages/thank-you/cardiology/index.html` — left as-is, shared generic
  thank-you template.
- Section 30 (SEO content cluster: eCW article, PE-backed article,
  denial-management article, A/R article, etc.) and Sections 33-34
  (content freshness cadence, measurement dashboard) are
  organization/process recommendations in the doc, not page content —
  out of scope for this page-build pass.
