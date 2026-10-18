# Analytics and experimentation playbook (X1–X16)

Instrumentation, attribution, cohorts, incrementality and change alerts for organic search. It expands core practices 40, 107, 108, 116–120, 131 and 159, and is the shared method behind the measurement sections of other layers (AI A14–A17, local L19–L21, e-commerce E22–E23, publishers P20). Read `README.md` in this folder first.

Research snapshot: **18 October 2026**. GA4, Search Console and consent tooling change names, limits and defaults; re-check the official links before building on them. This is methodology, not legal advice: tagging, identifiers, consent and retention in the EU and other regulated markets need privacy/legal review.

**The thesis.** Positions, clicks and sessions don't answer the question that usually matters: what value the work added, what changed because of the intervention, and what would have happened without it. Keep four operations apart — **observation** (what happened), **attribution** (which channel gets credit under a rule), **prediction** (what we expect) and **causal inference** (what extra result an intervention produced against a counterfactual). No analytics platform turns correlation into causation.

Format: **Why** · **How** · **Avoid** · **Verify**.

## Contents
- The measurement chain
- Instrumentation: X1–X4
- Search metrics and segmentation: X5–X7
- Attribution: X8–X9
- Cohorts: X10
- Incrementality and experiments: X11–X13
- Change analysis and alerts: X14–X15
- Dashboards and metric contracts: X16
- Interpretation myths · 90-day sequence · checklist · sources

---

## The measurement chain

| Stage | Question | Frequent sources | Metrics |
|---|---|---|---|
| Technical health | Can the engine access and process? | Logs, crawl, Search Console, uptime monitor | 4xx/5xx, latency, blocked URLs, coverage, canonical |
| Visibility | Which searches does the site appear for? | Search Console, Bing Webmaster Tools | Impressions, queries, average position, appearance |
| Entry | How many visits arrive? | Search Console, analytics, logs | Clicks, organic sessions, landing pages |
| Experience | Does the page help complete a task? | Event analytics, UX tests | Internal search use, interaction, return, defined engagement |
| Outcome | What important action happens? | Analytics, CRM, commerce, subscriptions | Lead, purchase, margin, subscription, retention |
| Incrementality | What extra result did SEO produce? | Experiment or causal model + business data | Net lift vs control, uncertainty interval |

The chain locates problems; it isn't strictly linear — people discover, return through another channel, convert weeks later or switch devices.

---

## Instrumentation

### X1. A measurement contract before tags — Critical
- **How:** a dictionary for every event and metric: name (GA4 recommended event where one fits, e.g. `generate_lead`); description ("form successfully submitted", not "button clicked"); firing moment (server confirmation or app success state); allowed parameters (`form_type`, `page_type`, `lead_category` — never free personal text); deduplication ID (internal non-identifying `lead_id` or technical token); value (amount, unit, currency); source of truth (CRM, order platform, backend or analytics); owner; QA (acceptance test, expected event, duplication condition); decision use (primary KPI, diagnostic, exploratory only). Keep names and parameters stable; version any change of meaning with date and logic, or history stops being comparable.

### X2. Business-oriented events — High
- **E-commerce:** list and product views, cart, checkout start, confirmed purchase, refund, value, currency, items and quantity. The backend/payment platform is the source of truth for sales; GA4 is for behaviour, not accounting.
- **Lead generation:** form start, error, successful submission, qualified call, accepted lead, closed sale. A form view or a click isn't a lead.
- **SaaS:** sign-up, activation (the event that represents real value), recurring use, trial start/end, subscription, expansion, cancellation — cohort windows aligned to activation and sales cycles.
- **Publisher:** registration, newsletter sign-up, engaged read (internal definition), paywall, subscription, renewal, churn (`../verticals/publishers.md` P20).
- **Local service:** click-to-call, booking, submitted request and **attended** appointment; keep micro-conversions apart from confirmed sales (`../verticals/local.md` L19).

### X3. Event quality rules — Critical
- **How:** fire success events after confirmation so double clicks, reloads or payment returns don't create two purchases/leads; include a transaction ID to deduplicate and reconcile; define currency, taxes, discounts, shipping, refunds, gross/net and recognition moment; validate parameters, formats, nulls and schema changes in DebugView/Realtime, logs and later reports; separate user events from automatic/infrastructure events; exclude internal, QA and bot traffic with verifiable criteria; check consent actually changes collection as configured — modelled data isn't observation; document time zone, currency, attribution, lookback and conversion window.
- **Verify:** daily ratio of analytics purchases to backend orders within an agreed tolerance; alert when it drifts (X15).

### X4. Data architecture and retention — High
- **How:** name the source of truth per metric. For long-term analysis, user cohorts, CRM joins or more detail than standard reports, export to a warehouse (GA4 → BigQuery; Search Console bulk export, 118) and keep aggregated copies; validate cost, retention, freshness, schema, consent handling and permissions. GA4 user/event retention for explorations is configurable and limited (up to 14 months on standard properties at the time of writing); set it deliberately before relying on historical cohorts. Export can't restore data that was never collected.

---

## Search metrics and segmentation

### X5. Read search metrics by their definitions — High
- **Impressions:** exposure as each report/surface defines it — not total market demand.
- **Clicks:** interactions with a Google result, with rules per result type.
- **CTR:** clicks ÷ impressions; varies by query, position, device, SERP, brand and layout; never read alone.
- **Average position:** an aggregate of observed positions — not one stable position for everyone.
- **Coverage/indexing:** URL states as Search Console reports them; not a traffic KPI.
- **Estimated share of clicks / visibility:** needs a vendor model; document coverage and assumptions.
- **GSC vs analytics:** an impression isn't a visit; a Search Console click isn't necessarily a GA4 session (incomplete loads, consent, blockers, multiple tabs, time zone, processing, redirects, canonicals, limits, privacy). Search Console hides anonymised low-volume queries, limits rows and filtering by query or URL changes totals. Compare **trends and equivalent segments**, not exact totals, and label these differences on every panel.

### X6. Business metrics with clear denominators — High
- **How:** organic revenue, contribution margin, purchases, qualified leads, pipeline, activation, subscriptions, retention, refunds, cost to serve, time to conversion. A primary SEO KPI must be influenceable by SEO, measurable with reasonable stability and connected to business. Add **guardrails** that must not worsen: lead quality, return rate, speed, satisfaction, revenue per user, purchase errors, cancellations, non-organic pages affected. More visits with less value per user isn't success.

### X7. Segment before averaging — High
- **How:** report at least by query (brand/non-brand and intent groups); URL and template (product, category, article, landing, location, docs); search type/surface, country/language and device; new vs historical page, conversion type, new vs returning customer; intervention type and deployment date. Define groups **before** looking at the result where possible; groups created after seeing the data are exploratory.

---

## Attribution

### X8. Credit isn't causation — Critical
- **Why:** an attribution model distributes credit across touchpoints (GA4 offers data-driven and last-click among available models). Results depend on observable identity, windows, channels, configuration, consent and modelling. Attribution answers "under this rule, which channel gets credit for the observed or modelled conversion?"; causality answers "how much would conversions have changed without this intervention?" The second needs a valid comparison or counterfactual assumptions.
- **How — five separate views:** (1) demand and presence (Search Console); (2) session acquisition (analytics landings); (3) attributed outcomes under a **declared** model and window — show more than one model when a decision depends on it; (4) reconciled business results from transactional systems; (5) incrementality from an experiment or quasi-experiment, visually separate from attribution.
- **Avoid:** summing figures from different tools; "SEO generated X" when X is last-click credit — write "GA4 assigns X to organic under [model/window]".

### X9. Brand and non-brand — High · *Established tool, approximate split*
- **How:** Search Console's **branded queries filter** (announced November 2025; top-level domain properties with enough query volume; classifies brand names, misspellings and brand products/services; works across web, image, video and news, and adds a branded/non-branded card to Insights). Because anonymised queries are excluded from query filtering, the split is approximate. Keep your own transparent classification too (regex with variants, typos and product brands — 117) for cohorts and ambiguous queries.
- **Avoid:** crediting all later branded searches to the entry channel, or all to "brand": discovery via non-brand search often returns via brand search.

---

## X10. Cohorts: acquisition, return and value over time — High
- **Define:** unit (user, session, lead, account, order), entry date, acquisition criterion, return event, window, metric and exclusions. SEO examples: users whose first observable visit was organic; users who first landed on a template or intent group; users acquired in a week/month and country; leads from an organic landing later qualified in CRM; customers whose first product came from a given organic page. Don't mix first-acquisition cohort with the channel of the converting session.

| Outcome | Denominator | Reading |
|---|---|---|
| Return at day 7 / week 4 / month 3 | Eligible cohort members | Share returning in the period |
| Activation | New eligible accounts/leads | Share reaching the value milestone in the window |
| Cumulative conversion | Cohort users or leads | Share converting by time since acquisition |
| Cumulative revenue | Cohort members | Observed/recognised revenue by month N |
| Margin / LTV | Eligible customers | Net value with explicit retention and cost assumptions |
| Time to outcome | Eligible users/leads | Median/percentiles to first purchase, qualification or subscription |

- **How:** match the window to the buying cycle (a six-month B2B SaaS sale isn't a daily-use app); compare equivalent cohorts by season, market, device and product, controlling price, promotion, inventory and onboarding changes; handle **censored** cohorts — recent ones haven't had time to convert, so use cohort age or survival curves; report cohort size and absolute values, not just percentages. GA4 Cohort Exploration uses device data, not User-ID, with cohort and dimension limits; cross-source persistent IDs belong in CRM/warehouse with legal basis, security and minimisation.

---

## Incrementality and experiments

### X11. The counterfactual question and the designs — Critical
- The incremental effect is the difference between the result with the intervention and the result the same unit would have had without it — the second isn't observed and must be estimated. Simple difference-in-differences:

```text
Estimated effect = (Treatment_after − Treatment_before) − (Control_after − Control_before)
```

  Causal only if the groups would have followed comparable trends without treatment and suffer no relevant differential shocks; a pre-trend check helps but doesn't prove it.

| Design | SEO use | Strength | Key risk/assumption |
|---|---|---|---|
| Randomised by URL / page group | Titles, internal links, content or template on a random sample of URLs | Reduces confounding if groups and measurement are valid | Interference via internal links, global changes, canonicalisation, heterogeneous pages |
| Randomised by user | Landing UX, CTA, navigation, CRO after the click | Estimates UX/conversion impact | Doesn't estimate ranking/impressions if Google sees one variant |
| Randomised staggered rollout | Phased implementation in random order | Everyone gets the change; temporal comparisons | Time, seasonality and anticipation confound weak designs |
| Difference-in-differences / event study | Intervention on a URL group with a comparable control | Uses history when randomising isn't possible | Parallel trends, no differential shocks, stable composition |
| Synthetic control / interrupted time series | One site, section or market treated, with predictive controls | Broad interventions without a clear control unit | Pre-period fit, stable relationships, uncontaminated predictors |
| Simple before/after | Small operational changes, early monitoring | Quick | Confuses intervention with season, demand, competition, SERP and updates |

  In SEO the experimental unit is usually a **page group, category or query cluster**, not a person — Google decides which version it crawls and shows. Avoid splitting a template or entity so treated and control pages pass signals through links, canonicals or duplicate content. Site-wide interventions (architecture, platform, indexing policy) contaminate internal controls: use an external control or time series and lower the confidence label.

### X12. SEO experiment protocol — High
1. **Causal hypothesis:** the concrete change and expected mechanism.
2. **One primary outcome,** predefined (e.g. organic clicks per eligible URL in a window, qualified conversions, margin), chosen by mechanism and latency.
3. **Guardrails:** indexability, 404/5xx, conversion, quality, speed, untreated pages.
4. **Unit and population:** eligible pages; inclusion/exclusion rules fixed before assignment.
5. **Assignment:** random where possible, stratified by template, baseline traffic, position, age, demand, country and seasonality.
6. **Control:** keep the current experience; prevent unplanned changes; log contamination.
7. **Pre and post periods:** long enough for variance and crawl lag; rules for weekends, seasonality, launches and updates.
8. **MDE and power:** the minimum change worth the cost; estimate sample and variance first. Low traffic may make the result inconclusive — don't change the rule after looking.
9. **Pre-registration:** date, hypothesis, URLs, treatment, metrics, exclusions, analysis, stopping rule and decision owner.
10. **Analysis:** intention-to-treat by original assignment; absolute and relative effect, confidence/credible interval, sample size and assumptions.
11. **Decision:** ship, iterate or reject against the predefined threshold and guardrails. "Not significant" doesn't prove zero effect.
12. **Replication** on another set/period before scaling a big decision.

  Worked example: breadcrumbs and contextual links updated on 120 pages of one template — stratify by prior clicks/impressions, age, intent and position; assign comparable pages to treatment and control; freeze other changes in both; measure impressions and clicks per URL (mechanism), landing conversions (value) and errors/canonicals (guardrails). A site-wide link change or a core update during the test is documented contamination; the honest result may be "promising but inconclusive".

### X13. Errors that invalidate experiments — High
- Picking "winning" pages after seeing their later performance; changing several elements and crediting one; stopping when the chart looks good (peeking) or extending until significant; ignoring seasonality, pre-trends, updates, campaigns, stock, news or SERP changes; using sessions as the denominator when treatment changes impressions/clicks (post-treatment outcome); contaminating control through links, shared templates, redirects, sitemap or global changes; many cuts with only the favourable one reported; confusing a detectable effect with one that pays for its cost and risk.

---

## Change analysis and alerts

### X14. Investigate a change in this order — High
1. Mark the exact date of release, rollout, content, robots, CDN, consent, tag manager and business changes (governance change log, G11).
2. Technical health first: response, indexing, canonical, sitemap, rendering, logs and measurement.
3. Separate Search, Discover, News, Images and Video where relevant.
4. Decompose by page, query, template, country, device and brand/non-brand to find the arithmetic origin of the total.
5. Compare with the previous period **and** the same period last year; check weekdays, holidays, campaigns, stock and category demand.
6. Review SERP changes, competition, ranking updates and documentation changes — date correlation is context, not proof.
7. Contrast GSC clicks with organic sessions and CRM/sales; diagnose discrepancies before attributing.
8. For a causal claim, find an experimental control or counterfactual; otherwise present it as observational with assumptions (core 159).

### X15. Alerts that detect change without noise — High

| Alert tier | Examples | Channel and response |
|---|---|---|
| T0 — availability/security | Domain down, TLS expired, general 5xx, robots blocking everything, hack | Immediate page; assign on-call; check from outside |
| T1 — lost indexability | Global `noindex`, canonical to staging, invalid sitemap, valid URLs falling, mass 404 | Immediate/same day; reproduce and scope affected pages |
| T2 — visibility change | Clicks/impressions below the seasonal range; anomalous CTR or coverage by template | Daily/weekly alert with segment and baseline |
| T3 — business and quality | Accepted leads, organic sales, margin, activation or return falling | Weekly/monthly, matched to the conversion cycle |
| T4 — opportunity | Impressions without clicks, emerging queries, pages gaining visibility | SEO/editorial digest; review a sample before acting |

- **Statistical design:** a baseline that accounts for seasonality, weekday and expected volume (a fixed "−20%" doesn't mean the same at 10 and 100,000 clicks); absolute relevance (clicks, URLs or value affected) as well as relative change; persistence (e.g. two consecutive windows) for non-critical alerts — a global technical failure doesn't wait; per-cohort/template impact, not the site total when sections move in opposite directions; an action, owner and target time per alert; log false positives/negatives, cause and resolution, and recalibrate. An anomaly alert detects a deviation; it never identifies the cause.
- **Exports:** `scripts/search_data.py` pulls Search Console (search analytics, URL Inspection, sitemaps) and Bing Webmaster Tools data with your own token/key, and `compare` / `brand-split` give per-page deltas and brand splits for X9 and X14.
- **Tools:** GA4 Insights and custom anomaly conditions (in-app and email); Search Console messages for major events; an external monitor for uptime, DNS, TLS, robots, sitemap and key-page status (core 120, 131; `scripts/seo_audit.py --urls … --fail-on critical` in cron/CI); logs and observability for 4xx/5xx, rendering and crawling; GSC API exports for breakdowns; Bing Webmaster Tools; backend transaction/lead checks for event drops; a calendar of releases, campaigns, inventory, publications and consent changes.

---

## X16. Dashboards and metric contracts — High
- **Executive view (one page):** organic clicks and visibility by market/surface with seasonal comparison; observed and attributed sales/leads/margin labelled by method; estimated incremental trend and evidence level where a valid study exists; quality, experience and brand-dependence guardrails; recent incidents and relevant changes.
- **Operational view:** performance by query, page, template, country, device and result type; organic cohorts and return/activation/value curves; coverage, canonicals, sitemaps, errors, robots, CWV and release markers; an experiments panel (hypothesis, design, status, sample, result, confidence, decision); tracking health (events per session/page, duplicates, analytics vs backend purchase ratio, consent coverage).
- **Metric contract per KPI:** name, question, numerator, denominator, unit, source, filters, window, delay, owner, definition changes, caveat and permitted use. "Attributed organic conversions" is not interchangeable with "incremental sales from SEO". Show magnitude **and** uncertainty, not just a percentage change.

---

## Interpretation myths

| Claim | Correction |
|---|---|
| "GA4 says SEO generated the sale" | GA4 assigns credit under a model, window and available identity; causality needs a counterfactual |
| "GSC and GA4 must match" | Clicks and sessions have different definitions and coverage; compare trends, diagnose gaps |
| "Clicks went up, so SEO improved" | Could be demand, SERP, brand, distribution, measurement or season; decompose and validate |
| "Average position fell, so we lost traffic" | The metric aggregates a changing basket of queries/URLs; analyse pages and queries |
| "GA4 retention proves loyalty" | Depends on observable identity, return definition, consent and window; check against CRM |
| "No p < 0.05 means the change doesn't work" | May lack power or duration; report intervals, MDE and inconclusive results |
| "Diff-in-diff removes every external factor" | Only under parallel trends and no relevant differential shocks |
| "An anomaly alert identifies the cause" | It detects a deviation; diagnosis is later work |
| "More organic sessions is always better" | Not if quality, margin, activation, conversion or experience fall |

## 90-day sequence

- **Days 1–15 — definitions and diagnosis:** business goals per page type and funnel; audit consent, tags, events, sources of truth, time zones, attribution and retention; compare GSC/GA4/backend and document expected gaps; event dictionary and KPI contracts with owners.
- **Days 16–35 — instrumentation and quality:** fix critical events and deduplication; reconcile e-commerce/leads with business systems; brand/non-brand and intent groups with transparent rules; export and keep the aggregates needed for history and cohorts; privacy, access, retention and release QA controls.
- **Days 36–60 — cohorts, dashboards and alerts:** organic cohorts by template, intent, market and new/returning; executive and operational views with stage-specific metrics; T0/T1 technical and T2/T3 business alerts with owners and baselines; check conversion latency and cohort maturity.
- **Days 61–90 — experimentation:** pick a bounded SEO intervention with an eligible sample and explicit mechanism; design control, pre-registration, MDE, guardrails and decision rule; run it and document effect, uncertainty, contamination and learning; if randomisation isn't viable, use a quasi-experimental design with reviewable assumptions and cautious language.

## Executive checklist

- [ ] Every important metric has a definition, source, denominator and owner.
- [ ] GSC visibility/clicks, analytics sessions and business sales/leads are kept apart.
- [ ] Implementation measures confirmed actions and prevents duplicates.
- [ ] Conversions, key events and micro-conversions are labelled and used consistently.
- [ ] Consent, modelling, privacy, access and retention are considered in analysis.
- [ ] Attribution states model, window, channel and identity; never presented as causality.
- [ ] Cohorts specify unit, entry date, return, window, censoring and sample.
- [ ] Tests fix hypothesis, unit, control, primary outcome, guardrails and stopping rule.
- [ ] Before/after analyses include seasonal comparison and concurrent events.
- [ ] Alerts separate technical emergency, visibility change, business value and anomaly; each has an owner and action.
- [ ] Dashboards show magnitude and uncertainty, not just a percentage change.

## Sources

Google Search and Analytics (level A): [Using Search Console and Google Analytics data for SEO](https://developers.google.com/search/docs/monitor-debug/google-analytics-search-console) · [About Search Console data](https://support.google.com/webmasters/answer/96568) · [Performance report filtering and comparison](https://support.google.com/webmasters/answer/17011165) · [Evaluating performance changes](https://support.google.com/webmasters/answer/17010961) · [Debug Google Search traffic drops](https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops) · [Branded queries filter (Nov 2025)](https://developers.google.com/search/blog/2025/11/search-console-branded-filter) · [Conversions vs key events](https://support.google.com/analytics/answer/13965727) · [Attribution](https://support.google.com/analytics/answer/10596866) · [Cohort exploration](https://support.google.com/analytics/answer/9670133) · [Configuration limits](https://support.google.com/analytics/answer/12229528) · [Set up events](https://developers.google.com/analytics/devguides/collection/ga4/events) · [Recommended events](https://developers.google.com/analytics/devguides/collection/ga4/reference/recommended-events) · [Measure ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce) · [Analytics Insights](https://support.google.com/analytics/answer/9443595) · [Anomaly detection](https://support.google.com/analytics/answer/9517187) · [Consent mode](https://developers.google.com/tag-platform/security/guides/consent).

Causal inference (level B): [Brodersen et al. (2015), CausalImpact](https://research.google/pubs/inferring-causal-impact-using-bayesian-structural-time-series-models/) · [Callaway, Goodman-Bacon & Sant'Anna, DiD with a continuous treatment (AER)](https://www.aeaweb.org/articles?id=10.1257/aer.20240137) · [Roth et al., What's trending in difference-in-differences? (J. Econometrics)](https://www.sciencedirect.com/science/article/pii/S0304407623001318).
