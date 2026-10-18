# Operating plan by business type (O1–O14)

The entry point for any engagement bigger than a quick question. It turns every layer of this skill — the 160 core practices, the engine layers, the verticals and the playbooks — into an executable system: a 10-day diagnosis, a playbook chosen by how the business creates value, a common 90-day rollout, a recurring operating rhythm, a balanced dashboard and a quarterly plan template.

**Operating thesis.** SEO is organised around the business model, the user's need and the risk of each change. The technical and measurement base is shared; priority, editorial rhythm, conversions and controls change with the way the organisation creates value.

This is a working framework, not a ranking forecast or a recipe that replaces diagnosis. Time windows and cadences are **starting values**: adjust them to size, buying cycle, resources, seasonality, jurisdiction and the site's real data. Official guidance describes requirements and possibilities, not every ranking factor; studies generate hypotheses; the meetings, scores and cadences here are operating-design decisions to validate against your own data (`research-method.md`).

## Contents
- O1. How to use the plan
- O2. The 10-day diagnosis
- O3. Playbook selector and hybrid businesses
- O4. Common operating base
- O5–O10. Playbooks A–F
- O11. Network module (chains, franchises, multi-location)
- O12. International and multilingual module
- O13. Migration and measurement modules
- O14. 90-day rollout, recurring rhythm, dashboard, QA, rules and quarterly template

---

## O1. How to use the plan

1. **Pick the main model** in the selector (O3). If the business combines models, choose one main playbook (the dominant revenue mechanism) and add the modules that describe its real operations.
2. **Run the 10-day diagnosis** (O2) before promising results or setting publishing volumes.
3. **Define a baseline and a business outcome** per initiative; impressions or positions are never an automatic substitute for sales, leads, visits or subscriptions.
4. **Apply the 30/60/90 plan** (O14) with an owner, acceptance criteria and post-release review for each relevant change.
5. **Review priorities monthly** and the whole system quarterly. A technical outage, a risk to users or an imminent migration reorders the backlog.

For a quick question or a single fix, skip this file and answer from the relevant practice.

## O2. The 10-day diagnosis

Don't start by writing more content. Build a verifiable picture of the site, the business and its economics.

| Day | Activity | Evidence that must remain | Usual owner |
|---|---|---|---|
| 1 | Business model, offer, markets, audiences, goals and constraints | Context sheet and conversion definitions | Business + SEO |
| 2 | Inventory properties, subdomains, CMS, templates, languages, locations and planned changes | Map of sites, systems and owners | SEO + product/engineering |
| 3 | Access to Search Console, Bing Webmaster Tools, analytics, CRM, Merchant Center, local profiles and logs | Access, coverage and data-limits matrix | Analytics + SEO |
| 4 | Technical crawl: crawlability, indexability, responses, canonicals, links, sitemap, rendering, templates (`scripts/seo_audit.py --crawl`) | Findings with example URL, template, severity and evidence | Technical SEO |
| 5 | Join queries, pages and conversions, segmented by country, device, template and brand/non-brand where possible | Baseline, noting definition differences between systems (X5) | Analytics |
| 6 | Classify the page inventory: create, improve, keep, merge, retire or protect | URL–intent–value–risk–owner map (G9) | SEO + content/product |
| 7 | Compare with visible results and real alternatives for the user's tasks | Sample of SERP / Maps / News / AI answers and observable gaps (A14) | SEO + business specialists |
| 8 | Seasonality, launches, expiries, catalogue or policy changes and risks | Commercial / editorial / regulatory calendar | Business + operations |
| 9 | Score initiatives: dependencies, effort, confidence, impact, reversibility (G5) | 90-day backlog and hypothesis register | SEO + functional owners |
| 10 | Agree owners, QA, alerts and rituals; publish the plan | RACI, goals, dashboard and review date (G2) | Sponsor + SEO lead |

If data is missing, document the limitation and use an explicit proxy — never invent a baseline. Third-party rank trackers aren't visits or business results. Separate errors that **prevent discovery or indexing** from opportunities that could only improve performance.

## O3. Playbook selector

| Dominant model / condition | Differential SEO priority | Main conversion or outcome | Use |
|---|---|---|---|
| Local service with in-person attention | Correct presence per location, local relevance, offline experience | Qualified calls, appointments, visits, local sales | Playbook A (O5) + `verticals/local.md` |
| E-commerce / transactional catalogue | Crawlable architecture, useful catalogue pages, product/price/stock consistency | Organic margin or revenue, orders, contribution by category | Playbook B (O6) + `verticals/ecommerce.md` |
| Publisher / media / magazine | Reliable publishing, editorial speed, archive architecture, direct audience relationship | Qualified reading, return visits, registration, subscription, revenue | Playbook C (O7) + `verticals/publishers.md` |
| SaaS / software / digital product | Evaluation and usage tasks, useful docs, problem/solution architecture | Qualified trials and demos, activation, retention (attributed cautiously) | Playbook D (O8) + `verticals/saas-services.md` S1–S8 |
| Lead generation / professional services | Capture qualified demand and prove trust and capacity to deliver | Valid leads, contact rate, opportunities, closed value | Playbook E (O9) + `verticals/saas-services.md` S9–S14 |
| Health, finance, legal or other high impact | Accuracy, evidence, professional control and safety before amplification | Safe access to information/service, valid leads, user outcomes | Playbook F (O10) + `verticals/regulated.md` — **added to any other** |
| Franchise / chain / multi-location | Governed local data and pages, consistent yet genuinely specific | Appointments, visits, calls or sales per location | Network module (O11) on top of A/E |
| International / multilingual | Fit of language, market, offer and local compliance | Results per market, not an aggregate | International module (O12) |
| New domain, redesign, CMS or new URLs | Continuity risk, preserved equivalences, validated infrastructure | Traffic and conversion of migrated pages, coverage, errors | Migration module (O13) + `playbooks/migrations.md` |

**Hybrid businesses** (a clinic is local and regulated; a publisher monetises with e-commerce; a SaaS has a local directory; a retailer sells in stores and online): the main playbook follows the **dominant revenue mechanism**; high-risk modules apply even if they cover a small share of pages; goals are set **per surface and page type** — never one average across local pack, product categories, news and docs; each template or business unit has an owner, with one person accountable for the portfolio.

## O4. Common operating base

**Work sequence for every business:**
1. **Make valuable pages discoverable** — crawling, internal links, response, rendering, sitemap, access to needed resources (phase 1).
2. **Choose what deserves indexing** — clear purpose, enough content for that purpose, one coherent canonical; keep filters, parameters, internal search and duplicates from creating an uncontrolled space (18, 20, 26).
3. **Solve a real need** — each page mapped to an intent, audience and task, with a reason it beats the available alternatives (42, 54).
4. **Show trust proportional to risk** — who publishes, who reviews, evidence, contact, policies, visible corrections where relevant (102–103, 157, Y8).
5. **Enable measurable actions** — forms, calls, purchase, registration, booking, return reading or a completed task (X1–X2).
6. **Earn independent recognition** — work worth references, coverage, honest reviews or citations; no bought shortcuts or fabricated signals (`playbooks/reputation.md`).
7. **Measure and maintain** — validate deployments, log changes, detect degradation, renew or retire pages by validity and usefulness (G9–G11).

**Prioritisation:** first anything blocking crawl or indexing, critical pages with wrong answers, security/privacy problems, content that could harm someone, and high-risk irreversible changes; then compare by impact, confidence, reach, effort, time to signal, opportunity cost and reversibility with the heuristic `(impact × confidence × reach) / effort` scored 1–5 with written assumptions (G5). A high score on weak evidence earns a small test, not a broad launch. Every initiative uses the minimum ticket (G3) and the rituals in G11 — small teams can replace meetings with an async report.

---

## O5. Playbook A — Local business and map presence

**Examples:** restaurants, clinics, garages, law firms, home services, shops with premises, practitioners seeing clients in person.

**Priorities:** (1) confirm eligibility and real representation of each location; keep profile data, categories, special hours, phone, URL, services and status current (L1–L6); (2) align name, address and phone across site, profiles and priority sources; fix duplicates and closed locations; no cities or keywords in the name unless they're part of the real name (L3, L16–L17); (3) a useful page per served location when there are real differences — team, services, access, hours, coverage, photos, directions, contact — never clones that swap the city name (L12–L13); (4) make honest reviews easy after a real experience, reply per policy, escalate complaints; no bought reviews, conditioned rewards or filtered invitations (L9–L10, R11); (5) measure calls, bookings, directions, forms and sales per location; inspect geographic samples and never read one coordinate as a universal rank (L19–L20).

| Phase | Work |
|---|---|
| 0–30 days | Inventory and verify profiles; fix critical data and duplicates; measure conversions; review location pages and service coverage; define the holiday-hours and review-reply processes |
| 31–60 days | Improve priority location pages; add proof of real service (team, cases, original photos, availability); improve mobile experience and calls; train location managers |
| 61–90 days | Compare results by area/service and demand; fix weak locations by cause; evaluate legitimate local references and partnerships; update the operating playbook and plan seasonality |

**Indicators:** verified, complete profiles; open discrepancies/duplicates; valid calls and bookings; clicks and actions per location; attended leads; new reviews and replies, with sentiment as context, not a target; local organic traffic to location pages. **Cadence:** incidents and hours weekly; conversions and profiles monthly; location audit quarterly or on opening, closing or rebrand. **Don't prioritise:** geo-landing pages without real service, coordinates as representative rankings, keywords in the name, duplicate listings or incentivised review campaigns.

## O6. Playbook B — E-commerce and catalogues

**Examples:** retailers, DTC brands, marketplaces with editorial control, B2B catalogues with purchase or quote requests.

**Priorities:** (1) an inventory of products, categories, brands, variants, facets and lifecycle states with defined indexing rules (E1, E5, E17); (2) important categories reachable through HTML links — engines don't type into your search box — and pagination/incremental loading that lets products be discovered (E2, E4); (3) facets crawled/indexed only where a combination answers a distinct intent with enough offer and content; control valueless combinations and duplicates (E5); (4) price, currency, availability, variant, delivery and returns agree across page, structured data, feed and checkout; handle sold-out, discontinued and substitutes by demand and inbound links (E12–E17); (5) product pages that help choose — specs, compatibility, dimensions, use, limits, own images, genuine reviews — never filler that repeats keywords (E9–E11); (6) organic revenue or margin by category/product where possible, plus clicks, queries, availability and conversion; segment branded/non-branded and control for price, stock and promotion changes (E22, X9).

| Phase | Work |
|---|---|
| 0–30 days | Map catalogue and templates; detect orphans, infinite facets, duplicates and product mismatches; validate sitemap, canonicals and links; audit feeds, structured data and the highest-value commercial pages |
| 31–60 days | Fix priority architecture; improve strategic categories and products; set variant, stock and retirement rules; reconcile feed and site; automated QA for price, availability and markup |
| 61–90 days | Run tests on product/category groups (X12); scale changes that improve outcomes, with guardrails; improve editorial–commercial linking; plan season, launches and the international catalogue |

**Indicators:** coverage and indexing by template; linked vs orphan products; impressions and clicks by category and product; organic sessions/revenue/margin; conversion and return rate as guardrails; feed–page mismatches; rich-result errors; availability and inventory coverage. **Cadence:** stock/feed/critical changes daily or per integration; errors and coverage weekly; performance and catalogue monthly; facets, lifecycle and season quarterly. **Don't prioritise:** indexing every facet, canonicalising everything to the root category without analysis, mass-copying manufacturer descriptions, markup that contradicts the page, or treating the ads feed as SEO.

## O7. Playbook C — News, media and publishers

**Examples:** general news, specialist publications, local journalism, magazines, subscription information sites.

**Priorities:** (1) SEO built into planning and the CMS while preserving editorial judgement — naming conventions, entity/place, links, photos, attribution, section paths (P7); (2) breaking, live, analysis and service/evergreen coverage each with purpose, update policy and coherent URLs (P8–P9); (3) protected article pages — faithful headline, real published/modified dates, transparent authorship, sources, licensed images, readable HTML; `Article` markup where it fits, without promising surface eligibility (P1–P5, P14); (4) archives, taxonomies, pagination, tags, author pages and syndicated content designed to avoid redundant URLs and keep pages with value, links or queries (P4, P10); (5) clear paywall/registration for users and engines, with substantive-update and public-correction rules (P2, P16); (6) audience beyond the click — returning readers, registration, subscription, depth/recirculation, commercial contribution — with explicit editorial definitions (P20).

| Phase | Work |
|---|---|
| 0–30 days | Audit CMS and templates; review sitemaps, canonicals, responses, rendering, robots and publishing errors; identify high-traffic pages, valuable archive and date/authorship problems; instrument editorial milestones |
| 31–60 days | Publishing and update QA; taxonomy clean-up; stronger links to context and explainers; better images, author pages and policies; review subscription experience and measurement |
| 61–90 days | Test service and in-depth formats; strengthen recirculation and direct return; technical/editorial on-call for big events; evaluate by story type, section and traffic source |

**Indicators:** technical time-to-publish; critical errors on articles; indexing and performance by page type; returning readers; registrations/subscriptions with declared methodology; pages with pending corrections; update speed on live stories. **Cadence:** continuous automated QA; breaking-news review per shift; performance weekly; archive and sections monthly; taxonomy, paywall and templates quarterly. **Don't prioritise:** stories produced for query volume, date changes without real changes, Discover as a guaranteed channel, `NewsArticle` filled with invented data, or speed at the cost of accuracy.

## O8. Playbook D — SaaS, software and digital products

**Examples:** B2B/B2C SaaS, tools, web apps, APIs and their documentation, self-serve platforms.

**Priorities:** (1) map the search journey — problem, solution category, evaluation, comparison, implementation, use, support — keeping acquisition content, product documentation and help content apart (S1); (2) use-case and audience pages only where the offer and evidence differ; no hundreds of near-identical programmatic pages (S2, S8); (3) useful public content crawlable — docs, guides, integrations, pricing, solution pages — with indexing control and authentication for private spaces, internal search and user data (S3–S4); (4) comparisons and alternatives with method, date, scope and commercial conflicts — no feigned objectivity or hidden affiliation (S5); (5) organic search connected to trial/demo, activation and retention through consistent events, cohorts and CRM — the last session doesn't describe the impact of long cycles (S6, X10); (6) content ready for retrieval and AI answers through clarity, accuracy, authorship and evidence; citations/referrals measured as a complementary, variable signal (S7, A14–A16).

| Phase | Work |
|---|---|
| 0–30 days | Map public and private pages, queries and events; review docs, product routes, accidental indexing, versions and subdomains; define qualified conversions with sales/product |
| 31–60 days | Prioritise solution, use-case, integration and documentation pages; improve differentiated content; instrument trial/demo and activation by cohort; review claims, comparisons and expired features |
| 61–90 days | Test templates and conversion paths; feed support/sales feedback into content; optimise docs by task completion and discovery; evaluate AI-answer presence with a repeatable sample |

**Indicators:** queries and pages by problem/solution; qualified demos or trials; activation and conversion by cohort; documentation use; assisted visits; leads advancing in CRM; indexing errors on private environments. **Cadence:** releases and docs per product cycle; queries/conversions monthly; claims and features on every change; strategy quarterly. **Don't prioritise:** pages from keyword combinations without a distinct product, unproven superiority claims, accidentally blocked valuable docs, or rankings as a substitute for activation.

## O9. Playbook E — Lead generation and professional services

**Examples:** consultancies, agencies, installers, education, real estate, insurance, B2B services, law firms when not giving sensitive advice.

**Priorities:** (1) map intent to service, location, sector, client size and decision stage; keep service pages separate from informational articles (S9); (2) show verifiable capacity — team, process, authorised cases, service limits, areas served, contact and real credentials (S10); (3) short, accessible forms that explain data use, with error/abandonment measured and phone or email alternatives where appropriate (S11); (4) bring lead quality from CRM into evaluation — valid, contacted, qualified, opportunity, client and value — deduplicated, with personal data protected (S12); (5) reputation through verifiable results, associations and relevant PR; neutral review requests; compliance with advertising and testimonial rules (S13, R11).

| Phase | Work |
|---|---|
| 0–30 days | Classify services, geographies, pages and CRM states; audit indexing and forms; define what counts as a qualified lead and the follow-up SLA |
| 31–60 days | Improve service and proof pages; close trust gaps; content that answers objections; connect web analytics and CRM with appropriate privacy |
| 61–90 days | Evaluate quality and value by landing page, query and segment; test CTA/forms with guardrails; fix pages that attract volume without quality; expand legitimate partnerships and editorial PR |

**Indicators:** valid and qualified leads; contact and opportunity rates; cost/value where reliably measured; traffic by intent; landing conversion; form errors; response time; relevant mentions and referring links. **Cadence:** forms and SLA weekly; lead quality monthly; pages and reputation quarterly. **Don't prioritise:** raw submissions as the only metric, bought links, testimonials without consent or invented clients, local landing pages for places you can't serve.

## O10. Playbook F — Health, finance, legal and other sensitive areas

**Cross-cutting: added to any playbook above.** Editorial decisions and risk management come before publishing and optimisation (`verticals/regulated.md`).

**Mandatory controls by risk:** classify each page by the plausible harm if someone acts on it, not by the sector label (Y1); assign author, professional reviewer, jurisdiction, scope and review date, verifying licences/credentials without overstating them (Y3, Y8); keep a ledger of important claims with primary source, date, limits, conflicts and approver (Y5); review commercial claims, testimonials, comparisons, calculators, tools and CTAs with professionals and local compliance where relevant; a fast route for harm reports, errors, regulatory change or new evidence — correct, communicate, withdraw or block, documented (Y15–Y16); AI only as internal help with human control, never publishing unverified advice or putting sensitive personal data into unapproved systems (Y14); no traffic goal overrides privacy, safety, accessibility, legality or accuracy.

| Editorial risk | Examples | Minimum recommended review |
|---|---|---|
| Low | Glossary, institutional history, non-actionable description | Editing, sources and clarity; review per subject |
| Moderate | General guide to options, services, rights or products | Specialist review, country/date and a maintenance process |
| High | Diagnosis, treatment, specific investment, credit, legal deadlines, eligibility or personalised decisions | Professional and compliance approval; primary evidence; visible limits; reinforced versioning and monitoring |
| Critical / immediate | Instructions that could cause physical harm, serious loss, loss of rights or fraud | Pause and escalate to a qualified owner; don't publish until resolved; immediate, logged correction |

**Indicators:** sensitive pages with owner and next review; verified claims; corrections and time to resolve; escalated complaints/harm reports; accuracy of authors and sources; valid leads/actions with guardrail metrics. Never reward traffic volume if safety or quality worsens.

---

## O11. Network module — franchises, chains and multi-location

- A master record per location: identifier, status, address, contact, hours, services and URL; permissions limited by role (L16, L7).
- Central immutable fields and reviewed locally editable fields; hour and season changes published with a local owner and central control.
- Templates with common components, but local content reserved for verifiable information about that location; no mass duplication (L12).
- Watch duplicates, unauthorised changes, closed locations, reviews and correct routing of calls and forms.
- Measure coverage and results per location, group and region; never hide a weak location inside the national average (L19).
- **Rhythm:** data sync as frequent as the risk requires; weekly anomaly report; monthly quality audit; quarterly location and content strategy.

## O12. International and multilingual module

- Only for languages or markets you genuinely serve. Agree per-locale URLs, equivalences between versions, visible language, `hreflang` where it applies, coherent canonicals, currency, availability, privacy, taxes, offer, support and regulation (133–137, B12, E18).
- Literal translation doesn't replace localisation and native review (136); in regulated topics, expert translation is mandatory (Y9).
- A local owner per market; record which content is adapted, which isn't offered and how versions are updated when the product or the rule changes.
- **Measure** clicks, conversions and value per country/language; equivalence coverage; hreflang/localisation errors; qualified leads/sales per market. Never sum languages and markets into an aggregate that hides mismatches.

## O13. Migration and measurement modules

- **Migration** — activate before changing domain, URLs, CMS, hosting, CDN, rendering, analytics, templates, navigation or taxonomy; a hosting move without URL changes can still affect crawling and availability. Gates: *before* (inventory and baseline, one-to-one map where equivalence exists, staging protected, parity checks, rollback owner), *launch* (agreed window, DNS/TLS/responses, sample templates and critical URLs, permanent redirects without chains, internal links and sitemaps updated, no staging leftovers), *after* (compare by template and URL group, fix 5xx/loops/404/noindex/canonicals, logs and search tools, old infrastructure kept until the new site serves users and crawlers). Don't close the project because the deploy finished — close it when QA, coverage, performance, conversions and risks have an agreed review. Full detail: `playbooks/migrations.md` (M1–M18).
- **Measurement** — the chain discovery → behaviour → conversion → value → causality, each with its own source and declared limits; never swap Search Console clicks for analytics sessions. Minimum alerts: availability, 5xx, robots/noindex/canonical and certificate changes; rising exclusions or falling indexable URLs by template; impressions/clicks/conversions outside a seasonal baseline; failed events or CRM, rejected feeds, broken forms, untracked calls; inconsistent price/stock; wrong location hours or contacts; overdue professional reviews or pending corrections. An alert triggers investigation, not a diagnosis. Tests: hypothesis, unit, population, primary metric, guardrails, duration/stopping rule and analysis fixed before deploying; a simple before/after describes a change, it doesn't prove incrementality. Full detail: `playbooks/measurement.md` (X1–X16).
- **Reputation and AI answers** support every playbook but aren't a universal package: turn real work, data and service into material others can cite; measure coverage, references, valid links, brand searches and assisted conversions as distinct signals; keep pages crawlable, clear, reliable and evidence-backed; measure identifiable referrals, sampled mentions/citations and conversions separately — no visible referral doesn't prove no exposure (`playbooks/reputation.md`, `engines/ai-search.md`).

---

## O14. Rollout, rhythm, dashboard, QA, rules and quarterly template

**Common 90-day rollout** (starts after the diagnosis; sprints may overlap, but high-risk changes keep their QA gates):
- **Days 1–30 — control and fundamentals:** name sponsor, SEO owner and owners of templates, content and data; fix verifiable blockers (downtime, accidental robots/noindex, canonicals, server errors, orphaned critical pages, broken measurement); agree baseline, conversion, market, segments, alerts and change log; pick a manageable number of priority initiatives with real effort estimates; put the playbook-specific controls in place (local profiles, catalogue, editorial CMS, CRM, professional review…). *Exit:* approved backlog, URL/template map, minimum QA, clear owners.
- **Days 31–60 — close value gaps:** architecture, links and content on the highest-value, best-evidenced templates or pages; complete trust, conversion and service information on priority pages; automate repeatable checks with human review for exceptions; launch bounded tests where a measurable hypothesis exists, logging concurrent changes; prepare commercial, editorial and maintenance calendars. *Exit:* changes deployed with tests; first readings without extrapolating early results.
- **Days 61–90 — learning and controlled scale:** review indexing, queries, conversion, lead/customer quality and guardrails by segment; keep, fix or revert by QA and evidence; scale only what worked in the tested context; prioritise maintenance and pages needing updates; remove debt and duplication with judgement; estimate next quarter's resources by opportunity and risk; present results with limitations, concurrent changes and recommended decisions. *Exit:* results-and-learning report, next quarter's backlog and maintenance plan.

**Recurring rhythm:**

| Frequency | Routine work | Expected output |
|---|---|---|
| Daily / continuous | Availability, publishing, stock, feeds, sensitive incidents and business events per model | Actionable incidents, not just a dashboard |
| Weekly | Critical errors, coverage, anomalies, blocked tickets, editorial/local QA | Owner and date for every material anomaly |
| Monthly | Performance by page/template/intent/market, conversions and backlog | Decisions: fix, investigate, keep, expand or stop |
| Quarterly | Inventory, content, authority, risks, automation and budget | Revised plan and reserved capacity |
| Yearly / on material change | Strategy, compliance, goals, suppliers and platform dependence | Updated goals and risks |

**Balanced executive dashboard** — never one combined "SEO score": (1) technical health (availability, errors by template, indexing of target URLs, rendering, page performance); (2) visibility (impressions/clicks and queries by page type, intent, brand, device, country and surface, with visible definitions); (3) business outcome (sales, margin, qualified leads, appointments, subscriptions, return visits or useful task, per model); (4) quality and risk (content errors, complaints, feed/profile mismatches, ownerless pages, overdue reviews, privacy or compliance issues); (5) operations (initiatives finished, blocks, cycle time, regressions, share with QA and post-analysis); (6) learning (hypotheses tested, result confidence, limitations, decisions). Separate Google / Bing / Maps / News / AI, organic / paid and new / returning where relevant and measurable; annotate algorithm updates and product changes as context, not automatic explanations (X16).

**Minimum QA.** *New or updated page:* clear purpose, audience, intent and expected outcome; evidence, sources and differentiation proportional to risk; author, reviewer, jurisdiction and next review when needed; URL, title, canonical, indexing, internal links, image and structured data correct where they apply; CTA, form, phone, purchase or next step working and measurable; mobile reading, accessibility, privacy and reviewed claims; maintenance owner and change log. *Technical release:* tests of responses, redirects, canonicals, robots, sitemap, links, rendering and schema on representative URLs; baseline vs production comparison on the most exposed templates; rollback and on-call for wide changes; logged date, change and later result (G7–G8). Automate deterministic checks; keep human judgement for usefulness, accuracy, consolidation, risk and experience — passing a validator doesn't prove a page is useful.

**Rules against useless or harmful work:**
- No publishing to a quota; there's no magic number of articles per week.
- No pages per city, product or keyword without differentiated usefulness.
- No buying links, reviews, fake mentions or interactions.
- No deleting pages or changing URLs without assessing value, equivalence, dependencies and reversibility.
- No `noindex`, robots rules, canonicals or structured data as a generic fix without checking effect and policy.
- No blaming an engine update without checking tracking, releases, demand and segments.
- No automated sensitive publishing without qualified review.
- No treating E-E-A-T, helpful content or GEO as a score to fill in.
- No promising positions, traffic or recovery windows; communicate ranges as hypotheses and review with your own data.

**Quarterly plan template** (use with the plan format in `SKILL.md` for the findings tables):

```markdown
# SEO plan — [business / domain] — [quarter]

## Context
- Main model and secondary modules:
- Countries / languages / locations:
- Priority offer and audience:
- Changes, dates and constraints:

## Baseline and definitions
- Business conversion:
- Primary metric and source:
- Segments and window:
- Data limitations:

## Risks and blockers
| Problem | Evidence | URLs/templates | Consequence | Owner | Date |

## Prioritised initiatives
| Initiative | Hypothesis | Impact/confidence | Effort/risk | Owner | QA | Result |

## Maintenance
- Overdue reviews:
- Priority content / catalogue / profiles:
- Alerts and owners:

## Decisions at close
- Keep / expand / iterate / revert / retire:
- Evidence and limitations:
- Next review date:
```

**Closing idea.** An operating SEO plan starts by choosing the work system that fits the business. What's common: diagnose before acting, fix access and architecture, write for a real need, show trust, instrument outcomes and maintain what you publish. What's specific: a retailer governs thousands of URLs and catalogue truth; a publisher balances accuracy, speed and return readership; a local business represents real locations and converts nearby demand; a SaaS connects problems to product and activation; a lead-gen business optimises quality, not form fills; a sensitive sector adds editorial and professional controls proportional to possible harm. Maturity isn't the number of dashboards, pages or meetings — it's the ability to choose well, deploy with control, detect problems, learn from imperfect evidence and put resources where users and the business get value.

## Sources

Google (level A): [Ecommerce SEO](https://developers.google.com/search/docs/specialty/ecommerce) · [Ecommerce site structure](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure) · [Share product data](https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google) · [Local ranking](https://support.google.com/business/answer/7091) · [Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article) · [Discover](https://developers.google.com/search/docs/appearance/google-discover) · [Hosting moves](https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes) and [URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) · [Helpful, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content). Microsoft: [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a). Each linked layer and playbook carries its own source list.
