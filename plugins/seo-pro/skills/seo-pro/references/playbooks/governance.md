# Governance and operations playbook (G1–G14)

The operating model that turns SEO recommendations into decisions with owners, processes that reach production, controls proportional to risk, recurring maintenance and a transparent way to decide what comes first. It expands core practices 119, 120, 123, 149, 152, 155 and 156 and the plan format in `SKILL.md`. Read `README.md` in this folder first.

Research snapshot: **18 October 2026**. Google and Bing documentation set concrete limits and controls; meeting rhythms, matrices and templates here are operating-design recommendations each organisation must adapt. There is no universal cadence and no priority formula that predicts SEO results with certainty.

Format: **Why** · **How** · **Avoid** · **Verify**.

## Contents
- Principles: G1
- Roles and decisions: G2
- Backlog and flow: G3–G4
- Prioritisation: G5
- Editorial flow: G6
- Technical flow and releases: G7–G8
- Maintenance: G9
- Quality gates, incidents and change log: G10–G11
- Operating metrics: G12
- Agencies, suppliers and AI: G13
- Templates and maturity: G14
- 90-day rollout · governance checklist · sources

---

## G1. Principles — Critical
1. **One owner for every decision and every critical page.** Shared work mustn't mean nobody answers.
2. **SEO joins when the change is defined, not only at final QA.** URLs, architecture, templates, content and tracking are product and platform decisions.
3. **Quality has observable criteria.** "Reviewed" isn't "approved" without evidence, owner, date or test result.
4. **Priority is an explicit decision** — expected impact, confidence, effort, risk, dependencies and opportunity cost.
5. **Not everything is solved with more content.** Sometimes the right action is to improve, merge, retire, block, correct or not create a page.
6. **Risk and compliance can block a launch.** Traffic urgency doesn't override safety, privacy, accessibility or regulatory review.
7. **Automate repeatable checks; keep human judgement for exceptions.** A crawler finds a broken canonical; it doesn't decide whether to merge two articles or whether a medical claim is safe.
8. **Every important change leaves evidence:** ticket, owner, URL/template, date, approval, QA result and later measurement.
9. **Tools inform; the organisation decides.** Search Console, analytics, crawlers and external scores have limits.
10. **Blameless continuous improvement.** Fix the failure and study which control, flow or assumption failed.

## G2. Roles, RACI and escalation — Critical

| Role | Core responsibility | Decisions they must be able to make |
|---|---|---|
| Sponsor / leadership | Goals, budget, priorities, cross-functional conflicts | Accept trade-offs, unblock capacity |
| SEO lead / owner | Strategy, standards, analysis, backlog, impact evaluation | Define SEO requirements, approve technical/editorial exceptions |
| Editor / content lead | Editorial plan, quality, tone, updates, publication | Approve content; retire valueless or outdated pieces |
| Domain specialist | Clinical, financial, legal, product or sector accuracy | Review claims needing specific expertise |
| Product manager | Experience, roadmap, flows, acceptance | Prioritise product, set functional criteria |
| Engineering / CMS / platform | Rendering, indexing, performance, data, releases, rollback | Implement and operate technical changes |
| Analytics / BI | Definitions, instrumentation, models, dashboards, data quality | Approve metrics and comparable methods |
| Design / UX / accessibility | Navigation, content, readability, forms, patterns | Validate experience and accessibility requirements |
| Legal / compliance / privacy | Obligations, advertising, consent, data, regulatory risk | Approve or stop communications/changes under control |
| Support / operations / sales | Voice of the customer, availability, processes, real conversion | Confirm promises, prices and support match operations |
| Agency / supplier | Contracted deliverables, evidence, documentation, handover | Recommend; never own the client's site, data or risk |

  One person can hold several roles, but each ticket says which role they're playing, and who validates high-risk decisions.

**Reference RACI** (R executes · A accountable · C consulted · I informed — exactly **one A** per decision):

| Activity | SEO | Editor | Product | Engineering | Analytics | Domain/Legal | Sponsor |
|---|---|---|---|---|---|---|---|
| SEO roadmap and prioritisation | R | C | C | C | C | C | A |
| Brief and content architecture | C | A/R | C | I | C | C | I |
| Review of sensitive claims | C | R | I | I | I | A/R | I |
| Redirects / canonicals / indexing | A | I | C | R | I | I | I |
| Template / CMS release | C | C | A | R | C | C* | I |
| Instrumentation / KPIs | C | I | C | R | A/R | C* | I |
| Standard article publication | C | A/R | I | I | I | I | I |
| Retiring critical content | R | A | C | R | C | C/A* | I |
| SEO / security incident | C | I | C | A/R | C | C | I |
| Post-launch evaluation | A/R | C | C | C | R | I | I |

  \* Legal/compliance can be accountable where a policy or regulation requires it.

**Escalation:** reversible, low-impact → area owner decides with a checklist; many URLs or a key template → SEO + product + engineering review impact and validation plan; sensitive claims, data, advertising or critical accessibility → specialist/compliance may stop it until resolved; general indexing, security, privacy or revenue incident → incident owner and sponsor, one person communicates and another implements; exceptions to a standard → recorded reason, scope, expiry and condition to return.

---

## Backlog and flow

### G3. Intake from many sources; tickets that describe a problem — High
- **Sources:** technical audits, crawls, logs, Search Console and Bing Webmaster Tools; query research, demand and SERP changes; sales, support, CRM, internal search and customer feedback; product, CMS, navigation, branding, market or regulatory changes; expiring content, stale data, broken links, page conflicts; revenue, margin, retention, brands and new markets; security, privacy, spam, reputation or accessibility fixes; earlier experiments.
- **Minimum fields:** problem and evidence · desired outcome (coverage, discovery, experience, conversion, revenue or risk) · affected unit (URLs, templates, directories, markets, queries, users, processes) · hypothesis/mechanism · scope and out-of-scope · expected impact (absolute range, horizon, assumptions) · confidence · effort per discipline incl. QA, dependencies and maintenance · risk/guardrails and rollback · one executing owner and one approver · metric and baseline · dependencies · status and date.
- **Avoid:** "add keywords" as a ticket.

### G4. Flow states and WIP limits — Medium
- `Idea → Triage → Discovery → Ready → In progress → Review/QA → Scheduled → Released → Measure → Done`, plus `Blocked`, `Rejected/Not now`, `Needs evidence`, `Incident`. **Done** means shipped, QA passed, a follow-up owner exists and the learning loop closed — not merely merged. Set WIP limits per team or specialty and renegotiate before starting more; nothing is "in progress" while it still waits for an unapproved decision or brief.

---

## G5. Prioritise by impact, effort and risk — Critical
- **Mandatory filters first** (they don't compete with a CTR tweak): (1) security, privacy, compliance and potential harm to users — by severity and obligation; (2) availability/indexing blockers or errors hurting current revenue — urgent diagnosis and mitigation; (3) launch debt and imminent high-risk changes — tests and rollback before the release date; (4) strategic improvement — by value, confidence, cost and opportunity.
- **Heuristic score for non-urgent work:**

```text
Indicative priority = (Impact × Confidence × Reach) / Effort
```

  Score each 1–5 with written level definitions and a named scorer; reach can be pages/templates or users affected. Keep negative risk, dependency, real urgency and maintenance **separate** — averaging them hides blockers. The formula is a conversation aid, **not** a probability of success or a return forecast; pair it with effect horizon, absolute segment value, opportunity cost and capacity, reversibility and blast radius, enabling tasks, time to learn, user and compliance impact, and baseline quality. This is the same impact × confidence × reach ÷ effort/risk ordering the SEO plan uses (`SKILL.md`, step 2).

|  | Low effort | High effort |
|---|---|---|
| **High potential impact** | Do soon after validating and reviewing risks | Plan as a project, split milestones, secure an executive owner |
| **Low potential impact** | Batch, automate or do alongside other work | Deprioritise unless obligation, dependency or relevant non-SEO benefit |

  Examples: a wrong canonical on 300 valuable pages — high evidence, small, testable fix → high priority. Rewriting 600 articles — high reach, medium/low evidence, big effort, editorial risk → split by template or test on a sample first. A low-traffic page with a wrong safety instruction → small SEO impact, but human and regulatory impact makes it immediate.
- **Re-prioritise** when traffic, market, costs, platform, evidence or dates change; review which work entered through false urgency, which tickets lacked owners and which scores predicted badly. Sunk cost isn't a reason to continue.

---

## G6. Editorial flow — High
- **Brief:** user, need and decision stage; page purpose and why this site should answer it; intent group and representative queries (not a list to repeat); angle and original contribution — experience, data or tool; sources and reviewing expert; overlap with existing content and the decision to create vs update/merge (46, 54); conversion/CTA and its limits; jurisdiction, language, risk and disclosure; architecture, internal links, canonical, indexing and template; owner, review date, success and guardrails (55).
- **Production and review:** the author delivers content **with sources**; the editor checks usefulness, originality, structure, language, duplication and intent; the expert validates claims in their field; SEO checks purpose, visible content, URL and architecture cohere — without adding empty sections to cover variants; legal/compliance reviews claims, promotions, privacy, disclosures and CTAs when risk requires (`../verticals/regulated.md`); product/operations confirm prices, services, times, stock and forms exist; design/accessibility checks readability and navigation. Reviews record **approved / changes required / rejected** with concrete notes and an owner ("missing current source for the legal deadline claim", not "looks good").
- **Editorial definition of done:** solves the stated purpose and adds value beyond existing content; verifiable claims have source, context, authorship and date; not unhelpfully duplicative or produced at scale without oversight (scaled content abuse applies whatever wrote it); metadata, headings, schema, image and CTA don't promise more than the text; canonical, indexability, linking, sitemap, language and redirects validated; review date and maintenance owner where the topic needs them; functional, analytics and accessibility tests passed; no `noindex`, staging, broken critical links, placeholder text or ownerless forms.
- **Publishing:** schedule with owner and window; capture version and target URLs; QA the HTML/response and the real experience after deploy; check canonicals, robots, sitemap, schema, links and events; tell support, sales, legal and others about important changes; log the date in the change timeline (G11); review metrics over a window that fits crawl, conversion and editorial cycles.

---

## Technical flow and releases

### G7. SEO early in product, QA by blast radius — Critical
- **Include SEO in discovery, architecture and acceptance:** URLs and identifiers, navigation, pagination, parameters, filters and canonicalisation; SSR/rendered HTML, links, metadata, structured data, hreflang and sitemaps; migrations, redirects, CDN, caching, robots, `noindex`, error responses and logs; field performance, images, JavaScript and interaction states; per-template testing and potential URL volume; measurement (events, consent, channel definition, annotations). Turn these into reusable SEO acceptance criteria per feature type (new template, URL change, programmatic content, internal search, internationalisation) instead of a late exceptional review.
- **QA levels:**

| Level | Example | Minimum controls |
|---|---|---|
| Q0 — local edit | Typo fix with no URL or claim change | Editorial and visual review |
| Q1 — single page | Rewriting an important landing or title | Before/after, indexability, metadata, links, CTA, analytics |
| Q2 — template/section | Template, navigation or facet-rule change | Crawl of a sample and the full segment, edge cases, performance, rollback |
| Q3 — site/domain | Migration, global robots, CMS, global canonical | Staging parity, URL map, mass tests, staged rollout, on-call, rollback (`migrations.md`) |
| Q4 — high regulatory/safety impact | Automated clinical or financial claims, sensitive forms | Specialist approval, functional and legal QA, reinforced monitoring, stop-ship |

  Levels combine: one URL on a high-risk topic can need Q4.

### G8. Technical release checklist — High
- What exactly changed and which URLs/templates does it touch? Are `robots.txt`, `noindex`, canonicals and sitemaps as expected? Are responses right on desktop/mobile, for bots and users, with consent where relevant? Any 4xx/5xx, chains, loops, irrelevant redirects or soft 404s? Main content and links in processable HTML? Schema and metadata match visible content? Languages, campaign URLs, images, PDFs and feeds preserved? Do events pass a test purchase/form without duplication? Any robots, header, WAF or CDN changes affecting legitimate crawlers? Is there a rollback, an activation criterion and an on-call owner?
- **Verify:** `scripts/seo_audit.py` before and after on the affected templates; `--fail-on critical` as a CI gate.

---

## G9. Maintain existing content — High
- **A living inventory:** URL, purpose, type, owner, audience, market, publish/review dates, sources, performance, technical state, risk, links and planned action — every active URL type, not just blog posts. States: **keep** · **update** (verifiable changes) · **merge** (real overlap; main page + relevant redirects) · **relocate** (architecture/ownership changes; URL strategy) · **retire** (no longer useful/safe/true; 404/410 or substitution by equivalence) · **noindex** (needed by users, not for Search; the directive must be crawlable) · **investigate**. Google recommends reviewing published content, updating it when needed and removing it when no longer relevant — not changing everything on a calendar or bumping dates without substantive change (147).
- **Suggested cadence (not a Google requirement):**

| Type | Suggested review | Off-calendar triggers |
|---|---|---|
| Stable technical guides | Semi-annual/annual | Product, standard or system behaviour change |
| Prices, products, catalogue | Continuous / per release | Price, stock, terms, availability |
| Health, finance, legal, safety | Per professional policy; always on relevant events | New guideline, rule, alert, risk or reported error |
| News and trends | Per editorial cycle | Fact updates and public relevance |
| High-traffic/revenue pages | Quarterly performance; content per validity | Sudden drop, conversions, competition, SERP changes |
| UGC, comments, forums | Moderation by risk and volume | Spam, safety, abuse, coordinated accounts (132) |

- **Maintenance debt** by class — technical, content, measurement, documentation, security, accessibility, indexing, reputation — each with an owner and a next-action date. Ownerless content becomes risk.

---

## Quality gates, incidents and change log

### G10. Quality gates; automate the repeatable — High
- **Gates:** intake (problem, audience, owner, scope) → evidence (the opportunity/problem is real) → editorial (approved brief, no duplication or unsupported claims) → specialist (professional/legal risk reviewed where applicable) → technical (requirements, data, URLs and measurement defined) → release (tests, rollback, deploy owner) → learning (results, incidents and post-release decision recorded). Use checklists and async review for low risk; not every gate needs a meeting.
- **Automate:** status codes, chains, canonicals, missing/duplicate metadata, robots, sitemaps, valid schema, broken hrefs, hreflang, synthetic performance, missing events, unchanged dates, mass content changes, internal links to redirects (`scripts/seo_audit.py`, 152). **Needs competent judgement:** accuracy, originality, claims, intent, real usefulness, sufficiency of evidence, advice risk, equivalence of a redirect, whether to merge pages, conflicts, plain language, complaint responses. Automated checks have false positives and negatives: give each an owner, severity, sample, threshold and exception process so teams don't learn to ignore them.

### G11. Incident severity, rituals and the change log — High

| Severity | Example | Suggested first response |
|---|---|---|
| SEV-1 | Site down, hack, accidental global robots/noindex, broken checkout, potentially dangerous advice spreading | Activate immediately, assign an incident lead, mitigate/pause, communicate |
| SEV-2 | Important section/template returning 5xx, mis-mapped redirects, material drop in forms/events or indexability | Same-business-day diagnosis; technical and SEO owners |
| SEV-3 | Limited URL group, defective schema or metadata without general harm | Prioritised ticket within the agreed sprint |
| SEV-4 | Improvement/opportunity, no incident | Normal backlog with score and periodic review |

  Exact times depend on coverage; define support hours and never promise an SLA the team can't meet.
- **Light rituals:** weekly triage (30–45 min: new entries, urgencies, dependencies); fortnightly/monthly backlog review by capacity, impact, confidence and risk; release sync on upcoming technical changes, tests and owners; monthly content review (updates, cannibalisation, obsolete pages, errors, new needs); quarterly business review (results, assumptions, cancelled initiatives, risks, next priorities); retrospective after incidents and migrations (root cause, controls, blameless learning). Don't duplicate forums that already decide; every meeting has an agenda, a required decision, an owner and an accessible record.
- **Central change timeline:** CMS/template releases, domains, navigation and crawl rules; relevant content changes and consolidations; campaigns, prices, inventory, consent, tags and experience; incidents, platform updates and seasonal windows; experiments, controls, dates and decisions. It's the first thing to read in a traffic-drop investigation (159, `measurement.md` X14).

---

## G12. Operating metrics — Medium
- **Flow:** intake → decision time; ready → release time; share of blocked tickets and why; work reopened by QA or incomplete requirements; SLA compliance by severity; initiatives finished/cancelled vs started; capacity per discipline and WIP. A shorter cycle time isn't success if defects or harm rise.
- **Quality and maintenance:** share of critical pages with an owner and next review; test coverage by template and high-risk change; errors by class and severity (canonical, indexing, schema, 404/5xx, events); time to detect and resolve; stale, orphaned, duplicate or unsupported content; repeat incidents and root causes addressed.
- **SEO and business results:** Search Console by query, page, country, device and search type; analytics/CRM sessions, outcomes and quality after the click; activation, margin, renewal and conversion by landing for subscription/e-commerce; field technical metrics; incremental results where a defensible experiment exists (`measurement.md`). Don't make every movement a team target.

## G13. Agencies, suppliers and AI — High
- **Contracts and briefs state:** scope, deliverables, owner and acceptance; access to and ownership of accounts, content, data and tools; method and the evidence they'll present; restrictions on links, scaled content, reviews, affiliates and personal data; client/professional review of claims and content; notice and approval before production changes; documentation, training and handover at the end. Brand and compliance accountability can't be delegated because "the agency recommended it". Hosting third-party content mainly to exploit the host's signals is **site reputation abuse**, even if the brand controls or reviews part of it (`reputation.md` R9).
- **Generative AI policy:** allowed tasks, data that must never be entered, citation and source checks, human review, attribution, archiving and criteria for **not** publishing. Volume doesn't replace original contribution or editorial control; spam policies judge purpose and value, not the tool (`../verticals/regulated.md` Y14 for high-risk topics).

## G14. Templates and maturity — Medium

**Initiative ticket**
```markdown
## Problem
## Evidence / baseline
## Users, URLs and templates affected
## Hypothesis and mechanism
## Primary outcome and guardrails
## Expected impact + confidence
## Effort per discipline
## Risk / reversibility
## Dependencies
## Owner / approver
## QA and acceptance criteria
## Release date / annotation
## Result and post-release decision
```

**Editorial brief**
```markdown
## User and need
## Page purpose
## Intent / reference queries
## Original value and format
## Existing content to update/merge
## Sources and claims to verify
## Author / reviewer / jurisdiction
## CTA and commercial relationship
## URL, linking, metadata and schema
## Maintenance owner / next review
```

**Post-release report**
```markdown
## What changed and when
## What we expected
## What happened (sources, segments, windows)
## Failures and guardrails
## Limitations / concurrent events
## Decision: keep, revert, iterate, expand or retire
## Owner and next review date
```

**Maturity** (not team size or tool sophistication — a small operation can be mature if it has ownership, quality, traceability and the ability to correct):
1. **Reactive** — incidents found by chance; SEO after publication; no stable owners. *First step:* owners for Search Console/BWT, a priority-page list, a technical–editorial contact and a change log.
2. **Repeatable** — intake, content/release checklists, owners per discipline, baseline, prioritised backlog. *First step:* agree RACI, definition of done, states and severity criteria.
3. **Integrated** — SEO in product discovery; per-template tests, roadmap, content governance and consistent measurement. *First step:* automate checks with thresholds; connect releases, Search Console, BI and CRM.
4. **Adaptive** — the team learns from experiments, incidents and demand; maintenance triggered by risk/change; priorities respond to capacity and results. *First step:* evaluate causal impact where possible, audit assumptions, cancel valueless work.

---

## 90-day rollout

- **Days 1–15 — responsibilities and visibility:** name sponsor and SEO owner; map stakeholders and owners for content, platform and data; inventory backlog, high-value pages, releases and critical risks; turn on Search Console and Bing Webmaster Tools notifications to named recipients.
- **Days 16–35 — flow and criteria:** intake, ticket, RACI and states; QA levels Q0–Q4, definition of done and gates; severity, escalation and rollback criteria; a calendar for content reviews and platform changes.
- **Days 36–60 — prioritisation and automation:** apply the heuristic score; separate compliance/incidents from the improvement backlog; automate crawl, status, canonical, sitemap, link and event tests; baseline flow, quality and results.
- **Days 61–90 — learning and adjustment:** run one initiative end to end and one incident drill; measure failures, blocks, cycle time and post-release results; reduce WIP and drop redundant gates; review priorities, partners, documentation and page ownership.

## Governance checklist

**People and decisions**
- [ ] Sponsor, SEO owner, editor, engineering, analytics and specialists identified.
- [ ] Every project and critical page has a single accountable owner.
- [ ] Explicit authority to stop a release for technical, editorial or regulatory risk.
- [ ] Exceptions have a reason, scope and expiry.

**Flow and quality**
- [ ] The backlog holds evidence-backed problems with owners.
- [ ] Briefs cover intent, original value, sources, URL, CTA and maintenance.
- [ ] Approvals are recorded with concrete criteria.
- [ ] QA is proportional to scope and blast radius.
- [ ] Releases have rollback and measurement where relevant.

**Maintenance and data**
- [ ] An inventory with owner and next review exists.
- [ ] Changes are reviewed on triggers, not only dates.
- [ ] Tools have owners and active alerts.
- [ ] Dashboards separate Search Console, analytics and business data.
- [ ] Operating metrics include quality, not just speed or volume.

**Prioritisation**
- [ ] Incidents, risks and compliance are separated from ordinary opportunities.
- [ ] Impact has a unit, segment and explicit hypothesis.
- [ ] Effort includes QA, dependencies and maintenance.
- [ ] Confidence and reversibility affect the decision.
- [ ] Work is cancelled or reordered when evidence or priorities change.

## Sources

Google (level A): [SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) · [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [Spam policies (scaled content abuse, site reputation abuse)](https://developers.google.com/search/docs/essentials/spam-policies) · [Using Search Console and Google Analytics data](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console) · [Get started with Search Console](https://developers.google.com/search/docs/monitor-debug/search-console-start) · [Search Console reports at a glance](https://support.google.com/webmasters/answer/9133276) · [Prevent user-generated spam](https://developers.google.com/search/docs/monitor-debug/prevent-abuse).

Microsoft (level A): [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) · [Notification Center](https://www.bing.com/webmasters/help/using-the-notifications-center-2d8ad7ca) · [Site Scan](https://www.bing.com/webmasters/help/site-scan-623520c9).
