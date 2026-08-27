# Technical SEO and AI Search Standard

## H1 / Headings
Every important indexable page:
- one clear primary H1
- unique title
- logical H2/H3
- no headings used only for styling
- search terminology used naturally

## Metadata
Every indexable page:
- unique title
- unique meta description
- canonical URL
- correct indexability
- social metadata where appropriate
- meaningful alt text

## Hierarchy
Do not keep site flat. Use parent/child topic clusters.

## Breadcrumbs
Use visible breadcrumbs on appropriate nested pages and matching BreadcrumbList schema.

## Internal Linking
`PROBLEM → SOLUTION → SPECIALTY → TECHNOLOGY → CASE STUDY → INSIGHT → CTA`
Avoid orphan pages.

## Footer
Structured site tree:
Solutions | Who We Serve | Technology & Revenue Intelligence | Specialties | Resources | Company

## sitemap.xml
Include canonical indexable URLs only.
Exclude redirects, duplicates, noindex, staging and unwanted utility/search pages.

## robots.txt
Review intentionally; do not block important render resources.

## URL Changes
For changed URL:
1. old → new map
2. permanent redirect
3. update internal links
4. sitemap
5. canonical
6. breadcrumbs
7. analytics
8. avoid chains

Never let production canonicals point to Netlify staging.

## Schema
Use only accurate visible-content schema:
Organization, WebSite, WebPage, BreadcrumbList, Person, Article/BlogPosting, VideoObject where appropriate.

## llms.txt
Create `/llms.txt` as a concise factual guide to authoritative public content.
Do not treat llms.txt as a Google ranking factor.

## OKF
Do not create an "OKF" file unless a valid specification is supplied and reviewed.

## Performance / Accessibility
Prioritize Core Web Vitals, mobile speed, semantic HTML, keyboard usability, labels, image optimization, low unnecessary JS, stable layouts, correct status codes, no broken links/redirect chains.

Mobile-safe layout requirements (preserved from pre-consolidation standard): provide mobile-safe alternatives for tables, metric grids, and multi-column cards at 320–375px viewport widths (e.g. stacked cards instead of horizontal tables). Support `prefers-reduced-motion` wherever animation/motion is substantial.

## Mobile CTA
Every important page has a conversion path. Use one-tap `tel:` where appropriate, short forms, thumb-friendly controls, and non-obstructive sticky CTAs.

## Search Console
Verify production property, submit sitemap, inspect key URLs, monitor indexing/Core Web Vitals/structured data/query performance and migrations.
