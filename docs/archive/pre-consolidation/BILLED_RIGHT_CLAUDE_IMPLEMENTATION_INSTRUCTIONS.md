# Claude Code --- Billed Right Website Implementation Instructions

## Mission

Work on the **existing Billed Right website**. Do not create a new
website from scratch.

Treat `BILLED_RIGHT_WEBSITE_2026_MASTER.md` as the governing strategy.
Read it before strategic content, IA, SEO, CTA, schema, navigation,
footer or template changes.

## Non-negotiable rules

1.  Do not rebuild the design system.
2.  Preserve useful components, responsive behavior, typography, motion,
    templates and SEO assets.
3.  Position Billed Right as an **Enterprise Revenue Performance
    Partner** while keeping Revenue Cycle Management clear.
4.  Never invent facts, metrics, results, certifications, security
    claims, AI features, integrations, guarantees, testimonials or
    timelines.
5.  **Billed Right is NOT SOC 2 certified. Never state or imply SOC 2
    certification.**
6.  Never present future Revenue Intelligence/AI capabilities as live.
7.  Do not mass-generate thin SEO pages/blogs.
8.  Do not keyword-stuff.
9.  Do not change URLs without
    redirects/canonical/internal-link/sitemap/analytics review.
10. Every major indexable page needs purpose, one clear H1, unique
    metadata, hierarchy, internal links and conversion path.

## Required first action

Before broad editing, create `/docs/website-audit.md` covering: -
routes/URLs - navigation/footer - templates - H1/H2 structure and
missing/duplicate H1s - duplicate titles - flat/orphan pages -
sitemap/robots - schema - canonicals - forms/CTAs and mobile CTA
behavior - analytics/tracking - blog/article and author structure -
breadcrumbs - claims/metrics - AI/automation claims -
security/compliance claims - staging/Netlify references that could leak
into production

## Claims register

Create `/docs/claims-register.md` with:
`Claim | URL/Component | Status | Evidence Needed | Owner | Publish Action`

Statuses: VERIFIED; NEEDS VERIFICATION; COMPLIANCE REVIEW; REMOVE;
FUTURE VISION.

## Capability register

Create `/docs/capability-register.md`. Classify every
AI/automation/platform capability: LIVE / PRODUCTION; LIMITED USE;
PILOT; UNDER DEVELOPMENT; FUTURE VISION.

Public copy must match status.

## Change map before each major page

Create `/docs/change-maps/<page-slug>.md` with:

### Page

Current URL; proposed URL; audience; search intent; conversion goal;
approved H1; primary topic; supporting topics.

### RETAIN

Existing components/content that remain.

### REPOSITION

Layout remains; messaging changes.

### ADD

Only genuinely required new sections/components.

### REMOVE

Weak, duplicate or unsubstantiated content.

### VALIDATE

Claims/metrics/compliance/security/AI/testimonials/integrations
requiring approval.

### SEO

Title; meta description; canonical; breadcrumb; links in/out; schema;
sitemap status.

### MOBILE CONVERSION

Primary mobile CTA; call action; form behavior; sticky behavior.

### COMPONENT CHANGES

Only changes required for strategy, accessibility, performance,
hierarchy or conversion.

## Homepage

Narrative order: 1. Hero 2. Enterprise credibility 3. Business
challenges 4. Billed Right operating model 5. Revenue Intelligence /
automation / AI 6. Outcomes 7. Capabilities 8. Who We Serve 9.
Specialty/platform experience 10. Client proof 11. Compliance/trust 12.
Executive CTA

Hero: - Eyebrow: `Enterprise Revenue Performance Partner` - H1:
`Transform Revenue Operations. Strengthen Financial Performance.` - Core
message:
`We help healthcare organizations achieve stronger financial performance by transforming the way revenue operations are managed.` -
Primary CTA: `Schedule an Executive Conversation` - Secondary CTA:
`Explore Our Approach`

Do not lead with small-practice/traditional billing language.

## Hierarchy and URL changes

Conceptual navigation: Solutions; Who We Serve; Technology & Revenue
Intelligence; Specialties; Client Results; Resources; Company; Contact.

Do not automatically change URLs. Map existing URLs first.

For any changed URL: 1. old URL 2. new canonical URL 3. permanent
redirect 4. update internal links 5. update sitemap 6. update canonical
7. update breadcrumbs 8. verify analytics 9. ensure no redirect chain

## H1 rules

Each indexable page needs one clear primary H1 unless a compelling
semantic reason exists. H1 describes main purpose. Use logical H2/H3.
Never use headings only for styling or hidden SEO headings.

## Breadcrumbs

Use visible breadcrumbs on nested commercial/resource pages and matching
BreadcrumbList schema.

## Footer

Build a structured site tree: Solutions; Who We Serve; Technology &
Revenue Intelligence; Specialties; Resources; Company. Do not dump every
URL.

## sitemap.xml / robots.txt

Sitemap includes canonical indexable URLs only. Exclude redirects,
duplicates, noindex, staging and unwanted utility/search pages. Review
robots rules and ensure production behavior is intentional. Never let
production canonicals reference staging.

## llms.txt

Create `/llms.txt` with concise factual links to authoritative Company,
Enterprise RCM, Revenue Intelligence, Solutions, Who We Serve,
Specialties, Results, Leadership, Trust and Insights pages.

Do not invent an OKF file without a valid supplied specification. Do not
claim llms.txt is required by Google.

## Schema

Audit first. Use only accurate visible-content schema such as
Organization, WebSite, WebPage, BreadcrumbList, Person,
Article/BlogPosting, VideoObject. No fabricated ratings/reviews.

## Blog inventory

Do not blindly rewrite blogs. Classify each: KEEP; UPDATE; CONSOLIDATE;
REDIRECT; NOINDEX; REMOVE.

For retained/updated articles: identify intent; one H1; improve
usefulness; add real expertise; author/reviewer; meaningful updated
date; internal links; contextual CTA; title/meta; accurate schema;
preserve URL equity; no fabricated data/filler.

## Revenue Intelligence page

Create/revise an authority page covering business problem; Billed Right
philosophy; Analyze/Predict/Prevent/Automate/Escalate/Learn/Optimize;
current capabilities; human oversight; executive intelligence; future
platform; related solutions/results; CTA. Separate future vision
carefully.

## Enterprise RCM page

Create/revise a deep pillar covering scale, multi-location,
multi-specialty, acquisitions, transition, governance, SLAs, reporting,
compliance, integrations, scalability, executive engagement and verified
outcomes. Do not clone generic RCM copy.

## Mobile conversion

Every page needs a conversion path. Where appropriate use persistent
non-obstructive CTA, one-tap `tel:`, short consultation/assessment
action, thumb-friendly controls and accessible focus. No intrusive
full-screen popups or sticky elements covering content.

## Forms

Audit mobile usability, accessibility, spam protection, validation,
privacy language, conversion tracking, source attribution and
success/error states.

## Performance/accessibility

Check Core Web Vitals, breakpoints, semantic HTML, keyboard navigation,
labels, focus, contrast, image dimensions/alt text/lazy loading, JS
weight, layout shifts, broken links, console errors and status codes.

## Analytics

Track primary CTA, mobile CTA, phone clicks, form starts/submits,
assessment conversions, case-study engagement, Revenue Intelligence
engagement, organic landing conversions, source and qualified lead
classification where possible.

## Per-page SEO QA

-   [ ] Unique title
-   [ ] Unique meta description
-   [ ] One clear H1
-   [ ] Logical H2/H3
-   [ ] Correct canonical
-   [ ] Correct index/noindex
-   [ ] Breadcrumb if appropriate
-   [ ] Internal links in/out
-   [ ] No orphan status
-   [ ] Appropriate schema
-   [ ] Sitemap status correct
-   [ ] Images optimized
-   [ ] Meaningful alt text
-   [ ] Mobile CTA works
-   [ ] Form/call action works
-   [ ] Claims verified
-   [ ] AI capability status accurate
-   [ ] No SOC 2 certification implication
-   [ ] No staging URL leakage
-   [ ] Responsive/accessibility checked
-   [ ] No broken links/errors

## Production-ready standard

Do not mark complete until enterprise positioning is consistent;
hierarchy is not flat; H1/title/meta are intentional;
breadcrumbs/internal links/footer reinforce hierarchy;
sitemap/robots/canonicals are correct; llms.txt is factual; blogs are
inventoried; Revenue Intelligence and Enterprise RCM have authoritative
destinations; mobile conversion is intentional; claims have
evidence/status; SOC 2 is never claimed/implied; analytics measure
qualified conversion; and useful existing design is preserved.
