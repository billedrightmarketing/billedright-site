# Website Audit

Baseline audit of the live build (`dist/`, built from `pages/` + `templates/`
via `build.py`), run per `CLAUDE.md` → "Required First Action." This is a
read-only inventory — **no website code or content was changed to produce
this report.** Findings are ranked by priority; use this as the baseline
`docs/change-maps/home.md` and future change maps get executed against.

Audited: 70 built routes, 2026-08-27.

---

## Priority Findings (act on these first)

### ✅ RESOLVED (2026-08-27) — ISO certification claims
`recognition/index.html` states Billed Right holds **ISO 9001:2015** and
**ISO 27001:2022** certifications. Flagged as an unverified,
SOC-2-equivalent risk at audit time; leadership has since confirmed
(2026-08-27) both certifications are genuinely held. Marked `VERIFIED` in
`docs/claims-register.md` and approved to remain live. Outstanding
housekeeping only: attach the certificate numbers/issuing body/scope to the
claims-register row for the record, and set a revalidation cadence (defaulted
to 2027-08-27, adjust to match actual renewal dates).

### ✅ RESOLVED (2026-08-27) — Nav links out to the Netlify staging domain
`templates/nav-template.html` hardcodes `https://billedright.netlify.app/...`
for the Psychiatry and Cardiology specialty links (desktop dropdown line 103,
108; mobile menu line 245, 250) instead of relative paths. This means, on
every one of the 70 live production pages, two nav links send visitors and
crawlers off `billedright.com` to a staging deployment — exactly the
"production canonicals/links must never reference staging" rule in
`docs/TECHNICAL_SEO_AND_AI_SEARCH_STANDARD.md`.
→ Fix: change both hrefs to relative paths (`/psychiatry-rcm-services/`,
`/cardiology-rcm-services/`) once implementation is approved.

### ✅ RESOLVED (2026-08-27) — Indexable pages missing from sitemap.xml
`sitemap.xml` listed 34 URLs against 70 built routes. Excluding the 16
`thank-you/*` confirmation pages and 3 legal-utility pages (privacy-policy,
terms-and-conditions, sms-consent) — all confirmed `noindex` and correctly
excluded — 18 pages that are set `<meta name="robots" content="index,
follow">` were missing, including all 4 case studies:
`account-management`, `authorizations`, `awards`, `case-studies/allergy`,
`case-studies/cardiology`, `case-studies/credentialing`,
`case-studies/primary-care`, `contract-renegotiation`,
`documentation-management`, `eclinicalworks-billing-services`,
`emr-billing-platforms`, `faq`, `leadership`, `locations`, `private-equity`,
`recognition`, `careers-us`, `careers-india`. All 18 added to
`sitemap.xml` (34 → 52 URLs). Re-verified against the live `dist/` build:
the sitemap now contains every `index, follow` page and nothing else —
only the 16 thank-you pages and 3 `noindex` legal pages remain excluded,
which is correct.

### 🟠 P1 — Unvalidated financial/outcome claims are live, not just staged
`docs/claims-register.md` was populated from the pre-consolidation
governance doc under the assumption these were staging-only. They are
**live in production today**:
- `$2B+ billed to date`, `94% collections lift`, `94% client retention /
  4-year tenure` — homepage hero, homepage metric cards, and a shared FAQ
  JSON-LD block reused verbatim across `about`, `blog`, `case-studies`,
  `contact`, `credentialing`, `resources`, `services`, `specialties`
  (9 pages + homepage = 10).
- `eclinicalworks-billing-services` independently states `94%+ Client
  Retention Rate`.
- `private-equity` states **`$4.2B+ Combined Client Revenue Managed`** —
  a figure that conflicts with the `$2B+` used everywhere else on the site.
  This is not just unverified, it's internally inconsistent.
→ These need immediate rows/updates in `docs/claims-register.md` marked
LIVE + NEEDS VERIFICATION (done for the first three; `$4.2B+` and the
eClinicalWorks-page `94%+` restatement should be added).

### 🟠 P1 — "HIPAA Compliant" / "AAPC Certified" badges hardcoded sitewide
`templates/footer-template.html` renders `<span>HIPAA Compliant</span>
<span>AAPC Certified</span>` in the footer of **all 70 pages** (via the
shared footer template). `AAPC Certified` is already tracked in
`docs/claims-register.md` as NEEDS VERIFICATION ("clarify whether individual
coders hold credentials — organizations are not casually described this
way"). This confirms the claim isn't a one-off — it's the most widely
distributed unverified claim on the site by page count.

### ✅ RESOLVED (2026-08-27) — No analytics/tracking installed
Google Tag Manager container `GTM-K8DSPBH` installed sitewide (head
snippet + body noscript fallback) via `scripts/add_gtm.py`, using the
existing billedright.com GTM/GA4 accounts (continuity with historical
data). Confirmed live in all 70 pages' `dist/` output and verified in
browser that `window.dataLayer` initializes with the `gtm.js` start event.

**Update (same day):** GA4 was already connected inside this GTM container
from before (confirmed via the user's GTM dashboard screenshot — "Google
tag" → destinations `G-GQ3J093V4D` and Google Ads `AW-960274332`), so no
manual GA4-connection step was actually needed.

**Event tracking installed.** Added `assets/js/br-analytics-events.js`
(loaded sitewide — via `templates/nav-template.html` for the 55 templated
pages, and a direct `<script>` tag on the 15 standalone `thank-you/*`
pages that don't use the shared template) pushing structured `dataLayer`
events via event delegation, so tracking survives future copy changes:
- `cta_click` — any `.br-btn-red` / `.br-btn-outline` / `.br-btn-outline-dark`
  link click, with `cta_text`, `cta_href`, `cta_style` (primary/secondary)
- `phone_click` — any `tel:` link click, with `phone_number`, `link_text`
- `form_submit` — any `<form>` submission (currently just `/contact/`'s
  Netlify form), with `form_name`
- `newsletter_signup_click` — footer subscribe button

Verified end-to-end on a real local HTTP server (`.claude/launch.json`'s
`dist-static-server` config — the file:// preview sandbox can't resolve
root-relative asset paths, so that's the only way to test this
correctly): all three event types fire with correct payloads, confirmed
`gtm.js`/`gtag.js` load live from Google's CDN, and a live Google Ads
view-through-conversion pixel request was observed firing automatically.

**Still needs a manual step, not code:** these are custom `dataLayer`
events, not yet GA4 Events — someone needs to create GA4 Event tags inside
GTM triggered on the custom event names above (`cta_click`, `phone_click`,
`form_submit`, `newsletter_signup_click`), mapping the event parameters
(`cta_text`, `phone_number`, `form_name`, etc.) so they show up in GA4
reporting. This requires the GTM dashboard, which isn't something this
session can access.

**Update (same day) — fully closed.** User created all 4 GA4 Event tags
in GTM (`GA4 - CTA Click`, `GA4 - Form Submit`, `GA4 - Newsletter Signup`,
`GA4 - Phone Click`), each wired to its matching Custom Event trigger
(`CE - CTA Click`, `CE - Form Submit`, `CE - Newsletter Signup`,
`CE - Phone Click`) with event names matching the `dataLayer` events
pushed by `assets/js/br-analytics-events.js`. Confirmed via screenshot.
Analytics — both pageview-level (GTM/GA4 container) and event-level (CTA/
phone/form/newsletter clicks) — is now fully instrumented sitewide,
pending the user publishing the GTM workspace changes.

### ✅ RESOLVED (2026-08-27) — Schema/visible-content breadcrumb mismatch
**Correction to the original finding:** the initial audit spot-check (2
pages, a narrow `class="...breadcrumb..."` grep) missed that all 46 pages
carrying `BreadcrumbList` schema already had a real visible breadcrumb in
the hero — it just isn't wrapped in a semantically-named class, which is
why the first pass didn't find it. There was no missing-UI problem.

The real problem, found once all 46 were compared programmatically: 31 of
the 46 had schema **text that didn't match** the visible breadcrumb —
either different wording (schema: "Cardiology Medical Billing Services",
visible: "Cardiology") or a different item count (schema skipped the
visible "Home / Services / X" middle step on 15 service pages, e.g.
`account-management`, `charge-posting`, `denial-management`). Fixed by
regenerating each page's `BreadcrumbList` JSON-LD from its own real visible
breadcrumb text (`scripts/fix_breadcrumb_schema.py`) — no visible markup
was touched, zero visual/layout risk. Verified programmatically that all
46 pages now have exact schema/visible parity, and spot-checked in-browser
that the visible breadcrumb is unchanged and not duplicated. Bonus: this
also fixed a pre-existing mojibake character in `terms-and-conditions`'
schema name, which was regenerated from the correctly-encoded visible text.

(Note: an earlier attempt in this session inserted a *second*, duplicate
breadcrumb bar based on the flawed original finding — that was caught via
in-browser screenshot before shipping and fully reverted before the schema
fix above was applied. Mentioned here for the audit trail, not because it
shipped.)

### 🟡 P2 — Small-practice tone surviving on non-homepage pages
The homepage hero/H1 already reflects the enterprise rewrite ("Transform
Revenue Operations. Strengthen Financial Performance."), but several other
indexed pages still carry small-practice, fear-based, or "practice owner"
framing that the governing docs now discourage as primary audience
language:
- `specialties/index.html` H1: *"One generic biller costs you 6-figures a
  year."*
- `resources/index.html` H1: *"Free Tools, Calculators & Guides for
  Practice Owners"*
- `contact/index.html` H1: *"See Exactly What Your Practice Is Leaving
  Behind."*
- Homepage `<title>`/meta description themselves still lead with "Medical
  Billing" and "Free billing review" rather than the enterprise RCM /
  financial-performance framing defined in `docs/
  BILLED_RIGHT_WEBSITE_2026_MASTER.md`.
These are candidates for their own change maps before copy changes — not
fixed by this audit.

---

## Full Inventory

### Routes / URLs
70 built routes (`dist/**/index.html`), all clean-URL folders (no `.html`
extensions), generated from `pages/*.html` via `build.py`'s
`PAGE_OUTPUT_PATHS` map. Full route list captured during this audit; no
duplicate output paths found.

### Navigation / Footer
Shared via `templates/nav-template.html` and `templates/footer-template.html`,
injected at build time. Nav staging-link issue: see P0 above (resolved).

**✅ RESOLVED (2026-08-27) — Footer structure.** Footer rebuilt to match the
`Solutions | Who We Serve | Technology & Revenue Intelligence | Specialties
| Resources | Company` tree specified in `docs/
TECHNICAL_SEO_AND_AI_SEARCH_STANDARD.md` (previous columns were "Main
Links," "Company," "Useful Links" — external CMS.gov/AAPC/WHO/HHS links —
and "Follow Us," with Testimonials duplicated across two columns). Legal
links (Privacy Policy, Terms & Conditions, SMS Consent) and the Sitemap
link moved into the bottom bar alongside the copyright line, separate from
the six primary categories. The external CMS.gov/AAPC/WHO/HHS links were
dropped — they didn't fit any of the six governed categories. "Who We
Serve" and "Technology & Revenue Intelligence" are populated only with
pages that actually exist today (`/private-equity/`, `/why-billed-right/`,
`/emr-billing-platforms/`, `/eclinicalworks-billing-services/`) — both
columns are thin because the site doesn't yet have dedicated landing pages
for those categories (e.g. no MSO/multi-location/physician-group pages, no
standalone Revenue Intelligence page). Building those out is separate,
future work — flagged in `docs/BILLED_RIGHT_WEBSITE_2026_MASTER.md`'s
preserved "Executive Problem Pages" / Revenue Intelligence authority page
guidance, not done here. **✅ RESOLVED (2026-08-27) — Nav restructure.** Rebuilt to: Why Billed
Right → Solutions → Credentialing (standalone quick link) → Who We Serve →
Technology & Revenue Intelligence → Specialties → Client Results →
Resources → About, with "Let's Connect" / phone CTA on the right. Every
link that existed before still exists — this was a relabel/regroup only,
confirmed via `git diff`-style review before rebuild. Notable moves:
"Case Studies" (was buried inside the old "Resources" dropdown) and
"Testimonials" (was buried inside the old "Home" dropdown) now form a new
"Client Results" section together. "EMR Billing Platforms" and
"eClinicalWorks Billing" (previously inside the old "Who We Serve" RCM
list) now form the new "Technology & Revenue Intelligence" section. The
old "Home" text/dropdown was removed — the logo already serves as the home
link, and Home's former children (Why Billed Right, About, FAQ,
Testimonials, Company links) were redistributed into the categories above.
Same gap as the footer: "Who We Serve" stays thin (CPAs and Private
Practices both still point to the generic `/services/` page — pre-existing
behavior, not introduced here — plus Private Equity) because no dedicated
MSO/physician-group/multi-location pages exist yet. Verified in-browser at
desktop (1440px, no horizontal overflow) and mobile (375px) widths, all six
dropdown panels and the mobile accordion confirmed rendering correctly.

### Templates
Two shared templates (`nav-template.html`, `footer-template.html`) plus 70
page sources under `pages/`. Build system is documented and understood (see
prior conversation turn covering `build.py`).

### H1 / H2 Structure
All 70 pages have exactly one `<h1>` — no missing or duplicate H1s found.
H2/H3 nesting not exhaustively audited page-by-page in this pass; spot
checks showed logical hierarchy. Tone/positioning issues noted under P2
above are content, not structural, problems.

### Duplicate Titles / Meta Descriptions
No duplicate `<title>` or `<meta name="description">` values found across
any of the 70 pages — each is unique.

### Flat / Orphan Pages
Not exhaustively link-graphed in this pass. The sitemap gap (P1) is a
reasonable proxy — the 17 flagged pages are indexable but not linked from
the sitemap; whether they're linked from nav/footer/other pages needs a
follow-up crawl-based check before calling them true orphans.

### Sitemap / Robots
`sitemap.xml`: 34 URLs, all `https://billedright.com/...` (correct
production domain, no staging leakage in the sitemap itself). See P1 gap
above. `robots.txt` is minimal and correct: `Allow: /` for all agents,
sitemap directive present, nothing blocking render resources.

### Schema
Broad and mostly appropriate coverage: `Organization`, `WebSite`,
`MedicalBusiness`, `LocalBusiness`, `Service`/`Offer`/`OfferCatalog`,
`FAQPage` (`Question`/`Answer`), `BreadcrumbList`, `Person`, `JobPosting`,
`AboutPage`, `ImageObject`, `ContactPoint`, `PostalAddress`,
`GeoCoordinates`. `MedicalBusiness` (49 occurrences) is worth a policy
question: it schema-classifies Billed Right as a medical business/practice
rather than a B2B revenue-cycle services company — minor, but worth
confirming intentional. Breadcrumb schema/visible-content mismatch: see P2
above. No fabricated ratings/reviews schema found.

### Canonicals
Present and correct on every page audited; all resolve to
`https://billedright.com/...` — no staging canonicals found.

### Forms / CTAs / Mobile CTA
`tel:` phone links present on effectively every live page except the 16
`thank-you/*` confirmation pages (expected — those are post-conversion).
Primary/secondary CTA button copy not exhaustively catalogued in this pass;
recommend a dedicated CTA-copy inventory before executing
`docs/change-maps/home.md`.

### Analytics / Tracking
None detected. See P2 above.

### Blog / Article & Author Structure
`blog/index.html` exists as a listing page; individual article pages were
not enumerated as part of the 70 routes in this build (no `blog/<slug>/`
routes found), meaning the blog currently has no published articles in this
build, or articles live outside this build pipeline. Needs confirmation
before `docs/CONTENT_AND_BLOG_STANDARD.md` can be applied to real content.

### Breadcrumbs
See P2 above — schema present, visible UI not confirmed present.

### Claims / Metrics
See P1 above and the now-updated `docs/claims-register.md`.

### AI / Automation Claims
No "24/7 claim bots," "AI-powered coding," or similar autonomous-AI language
found live in this pass (grep across all pages for SOC 2 / "100% secure" /
"zero breaches" / "independently audited" also returned no matches) — this
category appears to have already been cleaned up, consistent with the
"Remove SOC 2 claims sitewide" commit visible in git history.

### Security / Compliance Claims
SOC 2 and absolute-security language: clean (see above). ISO
9001/27001 claims: see P0 above — this is now the site's highest compliance
risk item, structurally identical to the SOC 2 issue that was already
remediated.

### Staging / Netlify References
See P0 above — confined to two specialty links in the nav template, but
repeated across all 70 pages via the shared template.

---

## Not Yet Audited (flag for a follow-up pass)
- Full link graph / true orphan-page detection
- H2/H3 hierarchy on every page (only spot-checked)
- Full CTA copy inventory across all 70 pages
- Accessibility (contrast, focus states, alt text coverage, keyboard nav)
- Core Web Vitals / performance (image weight, JS payload, layout shift)
- Form field/validation/spam-protection audit
- `llms.txt` (does not currently exist at repo root — confirm intentional
  before treating as a gap; `docs/TECHNICAL_SEO_AND_AI_SEARCH_STANDARD.md`
  calls for one)

## llms.txt Status
Not present in the repo. Per `docs/TECHNICAL_SEO_AND_AI_SEARCH_STANDARD.md`
this should exist as a concise factual guide to authoritative content —
flagged here as a gap, not created in this pass (documentation-only audit).
