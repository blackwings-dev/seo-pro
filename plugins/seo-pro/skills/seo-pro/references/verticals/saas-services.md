# SaaS, software and professional-services layer (practices S1–S14)

Covers two models that sell through evaluation rather than impulse: **software and digital products** (B2B/B2C SaaS, tools, web apps, APIs and their documentation, self-serve platforms — S1–S8) and **lead generation and professional services** (consultancies, agencies, installers, education, real estate, insurance, B2B services, law firms outside sensitive advice — S9–S14). Read `README.md` in this folder first; it implements playbooks D and E of `../operating-plan.md` and extends core practices 25, 26, 42, 45, 50, 54, 102–103, 112, 127 and 154.

Research snapshot: **18 October 2026**. Most of this layer is operating practice built on Google's general guidance (helpful content, spam policies, canonicalisation, crawlable links); platform-specific facts carry their source.

**The thesis.** These buyers search for a **problem**, then a **category of solution**, then **evaluate, compare, implement and get support**. SEO wins when each stage has an honest, useful page and when organic traffic is judged by what it does downstream — activation, qualified leads, closed value — not by sessions or form fills.

Format: **Why** · **How** · **Avoid** · **Verify**.

---

## Software and digital products

### S1. Map the search journey to page types — Critical
- **How:** for each product line, list the stages and the page that serves each: **problem** (guides, explainers, templates, free tools) → **solution category** (category/landing pages: "inventory software for small warehouses") → **evaluation** (features, use cases, industries, pricing, security/compliance, case studies) → **comparison** (vs and alternatives pages, S5) → **implementation** (integrations, migration guides, onboarding, API docs) → **use and support** (documentation, help centre, changelog, community). Keep acquisition content, product documentation and help content as **separate page types** with their own templates, owners and metrics (G2, X7).
- **Avoid:** blog posts trying to be landing pages, or docs stuffed with sales copy.
- **Verify:** a keyword → URL map with one primary page per intent (54) and no stage without a page.

### S2. Use-case, industry and audience pages only when they differ — High
- **How:** create "for [industry/role/use case]" pages only where the offer, workflow, evidence or integrations genuinely differ: specific features, screenshots, templates, customer proof, compliance notes, pricing implications. Link them from the solution page and from relevant docs.
- **Avoid:** dozens of near-identical pages that swap the industry name — that's scaled content abuse / doorway territory (`../playbooks/programmatic.md` D2).
- **Verify:** diff two use-case pages; the differences should be more than the noun.

### S3. Public, crawlable, useful content — Critical
- **Why:** documentation, guides, integration pages and pricing are often the most linked and most cited pages of a SaaS — and the most likely to be invisible because they live in a JavaScript app or behind login.
- **How:** server-rendered or static HTML for docs, pricing, integrations and solution pages (25, 127); real `<a href>` navigation and a docs sitemap; readable code samples as text, not images; stable URLs per page and per anchor-worthy section; `lastmod` that changes only with real edits. A public changelog and status page can help users; decide their indexing deliberately.
- **Avoid:** pricing only rendered client-side or behind "contact us" when the price is public elsewhere; docs reachable only through in-app search.
- **Verify:** `curl -s URL` shows the docs content; the auditor's word-count and JS-dependency findings.

### S4. Indexing control for apps, versions and private spaces — Critical
- **How:** keep the app (`app.`, dashboards, user workspaces, shared links, internal search, user-generated pages) out of the index with authentication and `noindex` — robots.txt alone isn't access control (21, A2). For **versioned docs**, choose one current version as the canonical/indexed target, keep old versions reachable for users with `noindex` or a canonical to the current equivalent where content is truly equivalent, and a visible version switcher; don't let five versions of the same page compete. Staging and preview deployments: password-protected and `X-Robots-Tag: noindex`.
- **Avoid:** customer data or shared documents indexed by accident; canonicalising a version-specific page to a current page that no longer describes the same API.
- **Verify:** `site:` checks for app and preview subdomains; Search Console page indexing per host.

### S5. Honest comparisons and alternatives — High
- **How:** "X vs Y" and "alternatives to X" pages with explicit criteria, method, date, scope, pricing as of a date, where each option is the better choice, and your commercial interest disclosed (50). Use verifiable sources for competitor facts and update them on a schedule.
- **Avoid:** feigned objectivity, invented competitor weaknesses, outdated pricing, hidden affiliate relationships; superiority claims you can't prove (comparative advertising rules apply in many jurisdictions).
- **Verify:** each claim about a competitor links to a source and has a check date.

### S6. Connect organic search to trials, activation and retention — High
- **How:** instrument sign-up, activation (the event that represents real value), trial start/end, conversion to paid, expansion and churn (X2); join organic landing cohorts with CRM/product data (X10); judge templates by activation and retention, not only sign-ups. Long sales cycles mean SEO often **assists**; the last session doesn't describe its impact (X8).
- **Avoid:** ranking or traffic as a substitute for activation; crediting all branded sign-ups to SEO (X9).
- **Verify:** a cohort view: organic sign-ups → activated → paid at 30/90 days.

### S7. Documentation that serves tasks, people and AI retrieval — High
- **How:** one task per page where possible, clear titles stating the task, prerequisites, steps, expected result, error messages users actually search for, version and date; examples that run; links between concept, how-to and reference pages. These same qualities help AI answer engines retrieve and cite docs accurately (A8–A10); `llms.txt` is optional documentation tooling, not a Google ranking lever (A12). Measure doc success by task completion, support deflection and search exits, plus citations/referrals as a variable complementary signal (A14–A16).
- **Avoid:** marketing copy in reference docs; outdated screenshots; feature pages for deprecated features left indexed without notice.

### S8. Programmatic and integration pages with real substance — High
- **How:** integration directories, template galleries and "connect X to Y" pages are legitimate when each page carries **specific** substance: what the integration does, setup steps, data synced, limits, pricing tier, screenshots, real examples. Follow the programmatic playbook (`../playbooks/programmatic.md`) for data thresholds, indexing rules and rollout in waves.
- **Avoid:** combinatorial "X + Y" pages for integrations that don't exist or that say nothing beyond the two names.

---

## Lead generation and professional services

### S9. Map intent to service, place, sector and stage — Critical
- **How:** a matrix of service × location served × sector × client size × decision stage; one service page per real service (what it is, for whom, process, deliverables, timing, price range or factors, proof, FAQs about objections); informational articles linked to the service they support. Location pages only where you can genuinely serve that area (`local.md` L12–L13).
- **Avoid:** landing pages for places or services you can't deliver; one page trying to rank for every service.

### S10. Verifiable capacity and trust — Critical
- **How:** real team with roles and credentials (102), the process step by step, authorised case studies with measurable outcomes and dates, service limits and areas served, certifications and memberships that can be checked, visible company details (106, 157). Testimonials only with consent, attributed and representative (R11).
- **Avoid:** invented clients, logos without permission, stock "team" photos, outcome claims you can't support. Professional advertising rules may apply (lawyers, healthcare, finance — `regulated.md`).

### S11. Forms that respect people and can be measured — High
- **How:** short, accessible forms (labels, errors, keyboard; 35–36, 112); explain what happens next and how data is used (consent and privacy notice per jurisdiction); offer phone or email where it fits; measure starts, errors, abandonment and **successful server-side submissions** with a deduplication ID (X3); spam protection that doesn't block real users (31).
- **Avoid:** counting button clicks as leads; hidden pre-ticked consent; forms that break silently (alert on submission drops, X15).

### S12. Judge SEO by lead quality from the CRM — Critical
- **How:** import CRM states back into analysis — valid, contacted, qualified, opportunity, won, value — and report by landing page, query group and segment (X6, X8). Agree with sales what "qualified" means and a follow-up SLA; deduplicate; minimise and protect personal data in the join.
- **Avoid:** optimising pages that generate volume without quality; reporting raw submissions as the KPI.
- **Verify:** a monthly table: organic leads → qualified → won, per service page.

### S13. Reputation through results, not shortcuts — High
- **How:** publish verifiable outcomes and methods, join and contribute to real associations, earn coverage with useful data or expertise (`../playbooks/reputation.md` R2–R4), request reviews neutrally from all eligible clients (R11). B2B buyers also check third-party review platforms and analyst listings: keep those profiles accurate.
- **Avoid:** bought links or "guaranteed coverage", review gating, fake case studies.

### S14. Measure, test and maintain — Medium
- **Indicators:** valid and qualified leads; contact and opportunity rates; cost/value where reliably measured; traffic by intent; landing conversion; form errors; response time; relevant mentions and referring links. **Cadence:** forms and SLA weekly; lead quality monthly; service pages and reputation quarterly. Test CTAs and forms with guardrails on lead quality (X12); fix pages that attract volume without quality; keep service pages current when offers, prices or team change (G9).

---

## Myths

| Claim | Assessment | Defensible practice |
|---|---|---|
| "Publish a page for every keyword combination" | Near-duplicate pages without distinct substance risk scaled content abuse | Pages only where offer, evidence or task differ (S2, S8) |
| "Docs don't matter for SEO" | Docs are often the most linked, searched and cited pages | Crawlable, task-based, versioned docs (S3, S4, S7) |
| "A comparison page should always declare us the winner" | Readers and regulators see through it | Criteria, sources, dates, disclosure (S5) |
| "More form fills means SEO works" | Volume without quality wastes sales time | CRM-qualified leads and value (S12) |
| "Gating every resource behind a form maximises leads" | Gated content isn't indexed | Indexable landing per resource; gate selectively (144) |
| "AI answer visibility is a SaaS KPI on its own" | Variable, partially measurable | Track citations alongside activation and pipeline (S6, S7) |

## Sources

Google (level A): [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [Spam policies (scaled content abuse, doorways)](https://developers.google.com/search/docs/essentials/spam-policies) · [Canonicalisation](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) · [Block indexing with `noindex`](https://developers.google.com/search/docs/crawling-indexing/block-indexing) · [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) · [Link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) · [Guidance on generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content). Measurement and reputation sources: `../playbooks/measurement.md`, `../playbooks/reputation.md`.
