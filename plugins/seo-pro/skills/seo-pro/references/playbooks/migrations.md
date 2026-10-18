# Migrations and platform changes playbook (M1–M18)

For redesigns, CMS and e-commerce platform changes, domain and URL changes, HTTPS, hosting/CDN/DNS moves, architecture changes, internationalisation changes, site consolidation and rebrands. It expands core practice **160** (and 23, 24, 133–137, 159) into a full prepare → launch → recover process. Read `README.md` in this folder first.

Research snapshot: **18 October 2026** (Google's site-move guide was extended in June 2026 to cover all domain variants for Change of Address). No checklist can guarantee that traffic or rankings stay the same; this playbook reduces risk and time to detect problems.

Format: **Why** · **How** · **Avoid** · **Verify**.

## Contents
- Classify the change: M1–M3
- Inventory and baseline: M4–M6
- URL strategy: M7–M10
- Domain, protocol and hosting: M11–M13
- CMS, templates and content parity: M14
- Launch plan, go/no-go and stabilisation: M15–M16
- Monitoring, diagnosis and rollback: M17–M18
- Special migrations · myths · exit checklist · sources

---

## Classify the change

### M1. Name every layer that changes — Critical
- **Why:** "migration" covers changes that alter different signals and need different controls. Google separates site moves **with** URL changes from hosting changes **without** them, and recommends, where reasonable, not combining domain, CMS and design changes in one step.

| Class | Examples | Visible URLs change? | Typical SEO risk |
|---|---|---|---|
| Infrastructure | Hosting, server, CDN, DNS, WAF | Not necessarily | HTTP errors, latency, bot blocks, downtime |
| Protocol and host | HTTP→HTTPS, www↔non-www, new domain or subdomain | Yes | Lost URL continuity, incomplete redirects, certificates |
| Paths and architecture | Directory reorganisation, taxonomy, slugs | Yes | Incomplete mapping, broken links, changed intent or hierarchy |
| Platform / CMS | WordPress → headless, Magento → Shopify | Sometimes | Rendering, metadata, canonicals, pagination, facets, content |
| Design and templates | Redesign, navigation, components, JS rendering | Maybe not | Omitted content, uncrawlable links, altered titles or markup |
| Content | Pruning, rewriting, consolidation, deletion | Maybe not | Lost relevance, topical coverage, links or usefulness |
| Consolidation / rebrand | Domain merger, acquisition, product split | Yes or no | Redirects without equivalence, lost context, mixed signals |
| Measurement and consent | New analytics, CMP, tags, event model | No | Non-comparable data that hides failures or fakes drops |

- **Verify:** a scope matrix (M2) exists before budget and date are approved.

### M2. A scope matrix with owners and exit controls — High
- **How:** for each dimension — domain/hostname, protocol, URL/path, CMS/server, navigation/architecture, content and metadata, internationalisation, analytics/consent, business operations (forms, checkout, login, subscriptions, feeds, APIs) — record before, after, whether it changes, the owner and the exit control (e.g. "DNS, TLS, variants, Change of Address if applicable"; "map, response and destination for every old URL"; "HTML, headers, rendering").

### M3. Prioritise controls by impact × likelihood × detectability — High
- **How:** highest risk usually combines a large share of URLs with demand or backlinks, weak editorial equivalences, wildcard redirect rules, JavaScript-dependent main content, exploding parameters, little monitoring, and no access to the old domain. Classify URLs at least into: top organic entries (clicks, impressions, conversions); URLs with valuable external links or referral traffic; revenue/lead pages (products, categories, articles, services, local pages); seasonal pages; legal, support, login, checkout and downloads that must not break even without organic traffic.
- **Avoid:** assuming low-traffic URLs are expendable — they may carry links, be seasonal, or be suffering from an earlier incident.

---

## Inventory and baseline

### M4. A multi-source URL inventory — Critical
- **Why:** no single source holds every relevant URL; a crawl of today's site misses unlinked, deleted, externally linked and seasonal URLs.
- **How:** combine (1) a full CMS/database export including archived entries; (2) current and historical sitemaps; (3) a crawl of HTML, links, canonicals, status codes, robots, hreflang, metadata, pagination and images; (4) Search Console performance by page/query/country/device, indexing, sitemaps and links; (5) analytics organic landings, conversions and revenue, year on year; (6) server/CDN logs (verify bot identity for sensitive decisions); (7) backlinks (linked URL, referring domain, context, referral visits — third-party tools are estimates); (8) business data: catalogue and variants, campaign redirects, app links, feeds, PDFs, externally served content. Record date, time zone, filters and export method; Search Console has row limits and isn't a census.

### M5. A master URL file — Critical
- **How:** at minimum `old_url` (absolute, normalised, keeping relevant parameters) · `new_url` (exact destination, unchanged, or empty if removed without substitute) · `old_status` / `new_status` · `template` / `content_type` · `indexability` / `canonical` · `clicks`, `impressions`, `conversions`, `revenue` · `external_links`, `referral_visits` · `mapping_reason` (equivalence, consolidation, retirement, no replacement) · `priority` / `owner` · `test_result` / `last_checked`. The file must detect duplicates, non-existent destinations, loops, chains, default redirects to another language/country and destinations with a different intent. Keep editorial decisions ("consolidate") separate from technical rules ("301 to X").

### M6. A comparable baseline — High
- **How:** keep at least **8–16 weeks** of data where the cycle allows, plus the same period last year for seasonal businesses: clicks, impressions, CTR and position by search type, URL and query; organic sessions/users, landing, business-defined engagement, leads, transactions and revenue; coverage (valid, excluded, crawled-not-indexed, errors, chosen canonicals); per-template availability, field LCP/INP/CLS where volume allows, 4xx/5xx and latency; owned media (brand, direct, email, referral, subscriptions, app, campaigns).
- **Avoid:** plotting analytics "organic sessions" and Search Console clicks as if they were one metric (`measurement.md` X5).

---

## URL strategy

### M7. Mapping rules — Critical · *Established (Google redirects guidance)*
- **How:** a successor with equivalent content/intent → redirect directly to it; several pages genuinely merged into one that covers their function → redirect to the consolidated page; no reasonable substitute and permanently removed → **404 or 410**, don't invent equivalences; one canonical version of domain, protocol, host, case and trailing slash, consolidated with one coherent permanent redirect; destinations return 200, are indexable when they should be, carry the main content and self-canonicalise.
- **Avoid:** sending large groups to the home or a generic category to avoid 404s — Google warns irrelevant redirects can be treated as soft 404s; conditional redirects by user agent, country or referrer that give crawlers a different destination than users.

### M8. Redirect or not — High

| Situation | Response |
|---|---|
| URL changed permanently, equivalent content | Server-side 301 or 308 straight to the final destination |
| URL temporarily moved | 302/307 if the original should remain preferred (Bing: only for very short changes, B5) |
| Page retired, no replacement | 404 or 410, internal links updated |
| Genuinely consolidated content | Redirect to the consolidated page, with checkable equivalence |
| Duplicate URL kept for function | Coherent canonical — not a substitute for a permanent move |
| Old domain you don't control | Resolve ownership/hosting/access before launch; without it you can't serve reliable redirects |

  Google says permanent redirects don't lose PageRank and are a strong canonicalisation signal; that doesn't guarantee every query, ranking, user or conversion transfers one-to-one. Keep redirects **at least a year**; for people and old links, indefinitely is often better.

### M9. Parameters, facets and pagination on the new platform — High
- **How:** define the indexing policy for each parameter family; keep the indexable URLs of categories and products that already have an organic role; stop filters without demand from producing thousands of indexable pages; coordinate canonical, internal links, sitemap and robots; never block with robots.txt pages that must be crawled to read a `noindex` or canonical; check how the platform renders next pages, filters and empty states (20, 22, `../verticals/ecommerce.md` E4–E5).

### M10. Internationalisation — High
- **How:** update `hreflang` with full new URLs, correct codes and reciprocity; each alternate returns 200 and self-canonicalises; no automatic IP or language redirects that prevent choosing another version (133); document the destination of retired markets or languages — don't send every region to a version that doesn't serve it.

---

## Domain, protocol and hosting

### M11. Domain or subdomain move — Critical · *Established (Google site-move guide, updated June 2026)*
1. Verify old and new in Search Console **and** Bing Webmaster Tools.
2. Keep every relevant Search Console variant: HTTP/HTTPS, www/non-www and subdomains in use.
3. TLS and DNS for the new domain; keep the old domain live to serve redirects.
4. Redirect URL by URL or with demonstrably correct rules, without dropping paths that don't match.
5. Submit **Change of Address** in Search Console for eligible domain/subdomain moves — since June 2026 Google's guide asks you to file it for **all verified variants** of the old domain (subdomains, www/non-www, even inactive ones) to the matching new domain. It doesn't apply to protocol changes, www↔non-www on the same domain, or path changes within a domain.
6. New sitemap; update canonicals, links and hreflang; monitor both properties.
7. Keep redirects at least a year (M8).

  Change of Address communicates the move; it doesn't replace redirects or build the new site.

### M12. HTTP → HTTPS and host normalisation — High
- **How:** valid certificates, chain, renewals, subdomains and resources; HTTP→HTTPS in **one** hop keeping path and useful parameters; update canonical, sitemap, internal links, hreflang, feeds and resource references; remove mixed content; check callbacks, APIs and third-party domains. Pick one convention for www, case and trailing slash and apply it in a single rule; test protocol × host × case × slash × query × encoded paths so CDN, app and CMS normalisation don't create chains. No Change of Address for protocol changes.

### M13. Hosting, server, CDN and DNS without URL changes — High
- **Before:** test from different networks and regions (IPv4/IPv6); lower DNS TTL in advance (it shortens caches, it doesn't control every resolver); test certificates, redirects, headers, compression, caching, 404/5xx pages, content and critical resources; check WAF, rate limits, bot management, CDN and geo-blocking rules so legitimate crawlers aren't challenged (A7, B4); keep Search Console verification, analytics, CMP, sitemap, robots and static files; provision capacity — Google may crawl the new environment more than usual during a move.
- **During and after:** confirm DNS resolution from several locations and providers; compare old and new origin logs; watch 5xx, timeouts, latency, TLS errors, robots, blank pages and blocked resources; keep the old origin while it still serves legitimate requests; shut it down only once users and relevant bots get the right content.

---

## M14. CMS, templates and content parity — Critical
- **Why:** a platform can produce different HTML with identical URLs. Parity must be checked per template and per data field, not by a quick visual review.
- **Template parity (old vs staging/new):** HTTP status (live 200, retired 404/410, no soft 404s); indexing (robots.txt, meta robots, `X-Robots-Tag`, login walls); canonical (absolute, no staging host, no unwanted parameters or cross-canonicals); title and description (expected content and uniqueness, no empty fields or literal template variables); headings and main text (topic, specs, availability, authorship, body and key links kept); internal links (navigation rendered as HTML links to final destinations); structured data (valid, matches page); hreflang (new hosts/paths, reciprocal); sitemap (only canonical, indexable, final-200 URLs); robots/resources (Googlebot and Bingbot reach content and needed resources); rendering (main content present without broken JS); media (images, videos, PDFs keep URLs or have a map); UX/business (search, filters, cart, checkout, forms, login, consent work).
- **Frequent CMS failures:** SEO fields migrated to the wrong or ignored field; slugs with different accent, encoding or normalisation; titles duplicated by templates or suffixes; 200 pages with error, empty content or loading text; JS hiding body, links or metadata until interaction; images and PDFs on old paths without redirects; staging indexed or production with `noindex` / robots blocking everything; out-of-sync inventory, prices, availability, authors or dates; pagination and filters changing pattern and multiplying URLs; analytics tags duplicated, lost or blocked by consent.
- **Four parities:** technical (status, indexability, canonical, sitemap, rendering) · informational (topic, answers, attributes, entities, evidence) · navigational (discovery paths, categories, breadcrumbs, contextual links) · conversion (actions and events linking organic traffic to business goals). Document what is retired, kept, merged and why; don't rewrite every priority page during a domain move if those changes can be separated.
- **Verify:** run `scripts/seo_audit.py --crawl` against old and staging, compare reports per template; diff titles, canonicals, H1s, word counts and JSON-LD types from the JSON output. After launch, `scripts/seo_audit.py --redirect-map redirects.csv` validates every row of the master URL file (M5) and `scripts/search_data.py compare --before old.csv --after new.csv --map redirects.csv` reads old + new performance per URL (M17).

---

## Launch plan, go/no-go and stabilisation

### M15. Phases A–F — Critical
- **A. Discovery and governance (T−8 to T−4 weeks):** name the decision owner and leads for SEO, product, engineering, infrastructure, analytics, content, QA and support; define exact scope, dependencies, markets, domains and success/rollback criteria; build the inventory and baseline (M4–M6); decide whether to split domain, CMS, design and editorial clean-up into separate launches; secure access to old domain, DNS, hosting, CMS, Search Console, BWT and analytics; publish an approved map with owners and documented exceptions; freeze unreviewed new rules near launch.
- **B. Build and test (T−4 to T−1):** staging protected by access control and/or `noindex` (robots.txt controls crawling, it isn't authentication or `noindex`); crawl staging and compare against old per template; test every redirect pattern plus every top-value URL; confirm analytics and events (ordering, consent, attribution); rehearse deployment and rollback with realistic infrastructure; a launch dashboard with alerts for 5xx, 404 rate, organic traffic, payments/leads, events and bot logs.
- **C. Go/no-go — don't launch if any fails:** nobody reachable owns the old domain or redirects can't be served; priority destinations missing or irrelevant; unplanned global block in new production (`noindex`, robots, auth, firewall); TLS/DNS, checkout, forms, login or critical analytics broken; sitemaps or canonicals pointing to staging or the wrong domain; no working rollback and no one able to trigger it.
- **D. Launch:** a low-risk window with technical and editorial support available; for hosting-only moves switch DNS after parity tests; for URL changes activate redirects and the new site together; within minutes confirm home, top pages, domain variants, status codes, certificates, `robots.txt`, canonicals, sitemaps, Search Console, BWT and analytics; check a wide sample of old URLs redirects **once** to the planned destination and crawl the full list automatically; submit the new sitemap and, for eligible domain moves, Change of Address on every required variant; update internal links, campaigns, profiles, feeds, integrations and owned links.
- **E. Stabilisation:** 0–2 h continuous technical monitoring of route, status, canonical, robots and conversion on priority URLs; 2–24 h logs, 5xx, latency, 404s, chains, bot access, analytics and checkout/forms; days 2–7 crawl redirects and links, review Search Console reports, sitemaps and indexing, fix mapping errors; weeks 2–8+ watch impressions/clicks transfer between old/new sets, coverage by template, queries, conversions and server results. Google says a medium site can take weeks or more; large sites longer.
- **F. Retrospective:** what changed, what failed, time to fix, pages affected, observed impact and which control would have caught it earlier; keep the map, rules and checklist as living architecture documentation.

### M16. QA level matches blast radius — High
- Use the governance QA levels (`governance.md` G7): a migration is **Q3** (site/domain) at minimum; Q4 if regulated claims or sensitive forms change.

---

## Monitoring, diagnosis and rollback

### M17. Monitor by level and read old + new together — Critical

| Level | Signals | Question |
|---|---|---|
| Availability | 5xx, timeouts, TLS, DNS, latency | Does the site serve stable responses? |
| Transport | 3xx, 4xx, loops, chains, destinations | Does every old URL reach the right destination? |
| Crawling | Logs, Crawl stats, robots, rendering | Can bots request and process the new site? |
| Indexing | Chosen canonical, sitemaps, indexed/excluded | Do engines recognise the expected new URLs? |
| Visibility | Impressions, queries, clicks, CTR, position | Is organic demand transferring by page type? |
| Business | Leads, transactions, revenue, subscriptions | Does search produce the expected outcome? |
| Experience | Field CWV, UX errors, internal search | Do users complete their task? |

- **How:** annotate the launch; compare old URL vs its new URL by cohorts and priority pages; by directory, template, language, device, country, brand/non-brand and intent; GSC clicks/impressions plus analytics sessions and conversions; current week, previous period and the right seasonal comparison; direct/referral traffic to catch broken external URLs and campaigns. During a successful move the old property falls and the new one rises gradually: evaluate **old + new**, the mapping and business.

| Symptom | Check first |
|---|---|
| Many new URLs "Discovered – currently not indexed" | Quality/coverage, internal links, sitemap, response/duplication, crawl capacity |
| New domain gets no impressions, old still active | Redirects, canonical, links, Change of Address, sitemap, variants |
| Many new 404s | URL map, slugs, parameters, encoding, route rules |
| Sitemap with redirected or non-canonical URLs | Destination sitemap, canonicals, CMS, generation date |
| Valid pages but clicks collapse for one template | Content, intent, title, indexability, navigation, experience, demand |
| Sudden drop at launch | Robots/noindex, 5xx, DNS/TLS, canonical to staging, JS, WAF, tags, redirects |
| Analytics drops but Search Console doesn't | Consent, tag, channel, attribution, property, time zone |
| Search Console drops but organic sessions hold | Definitions, canonical/property, URL tracking, report delays, other engines |

- **Avoid:** blaming a "sandbox" or a penalty automatically; normalising a drop that continues or worsens.

### M18. Rollback is a plan, not a reflex — High
- **How:** before launch, define the triggers (failed payments, sustained 5xx, widespread blocks, wrong destinations at scale), thresholds and duration to avoid reacting to noise; who decides, executes and communicates; whether to restore the old platform keeping the new domain or revert DNS; what happens to forms, orders, inventory, published content and events created in the window; how to keep redirects coherent for users and engines; how to preserve logs, baseline and incident evidence. Once some URLs have been crawled, inconsistent reversal of DNS, canonicals and redirects can prolong the problem. If one template or pattern is affected, a targeted fix usually beats a full revert; don't keep diagnosing in production when the site is down or a global block is obvious.

---

## Special migrations

- **Redesign without URL changes:** compare served content, navigation, links, headings, structured data, images, metadata and mobile behaviour before and after — a page can keep its path and lose content, links or a useful answer.
- **Domain mergers and acquisitions:** map by intent and entity, not everything to the buyer's home; keep useful pages; retire content without equivalent with the right status; keep context explaining brands, products and entities; separate legal/commercial integration from editorial and SEO equivalence.
- **Rebrand:** inventory old and new brand queries, product names, social profiles, backlinks, emails and campaigns; keep redirects, update owned references, keep identity metadata (38, 104), monitor both query families — old brand demand doesn't automatically become new brand demand.
- **E-commerce:** also compare IDs, variants, categories, stock, prices, currency, taxes, availability, reviews, feeds, filters, pagination and product markup; define the destination of discontinued items (`../verticals/ecommerce.md` E17).
- **Publishers:** preserve authorship, dates, canonicals, pagination and article routes; decide live pages and archives; keep News sitemaps current (`../verticals/publishers.md` P11).

## Myths

| Claim | Assessment | Correct criterion |
|---|---|---|
| "A 301 keeps 100% of traffic" | Unverifiable and false as a promise | A strong move signal; results depend on destination, content, demand and processing |
| "Redirect everything to the home to keep authority" | Irrelevant destinations can be soft 404s | Map equivalences; 404/410 without replacement |
| "A migration plugin handles the SEO" | It implements part of the task | Audit served output, routes, indexing, business and measurement |
| "Rankings will drop for exactly two weeks" | No universal timeline | Measure by URL and segment; weeks or more depending on scale and crawl |
| "The Search Console property migrates itself" | Verification and data belong to specific properties | Verify old/new and all variants; Change of Address only where eligible |
| "Staging blocked by robots means production is safe" | Config gets copied; robots isn't access control | Independent production QA; protected staging; explicit list of directives to remove |
| "We don't need to keep the old domain" | Without it you can't redirect or protect users | Keep ownership, DNS and the redirect service |
| "A crawl of the current site is the full inventory" | Misses unlinked, deleted, external and seasonal URLs | Cross CMS, sitemaps, logs, analytics, Search Console and backlinks |
| "A hosting change is SEO-neutral" | Only if the technical experience stays stable | Compare availability, DNS, TLS, latency, bots, content and responses |

## Exit checklist

**Scope and governance**
- [ ] Every change classified: URL, domain, infrastructure, CMS, design, content, analytics.
- [ ] One owner and an escalation channel during launch.
- [ ] Organic, commercial, technical and indexing baseline captured.
- [ ] Decided which changes to separate for attribution and reversibility.

**Data and mapping**
- [ ] Inventory combines CMS, crawl, sitemaps, Search Console, analytics, logs and backlinks.
- [ ] Every important URL has an approved destination or a documented 404/410.
- [ ] No missing destinations, loops, avoidable chains or generic redirects.
- [ ] Images, documents, videos, feeds and resources included.

**New site**
- [ ] TLS, DNS, availability, firewall and capacity validated.
- [ ] Production not blocked by accidental `noindex`, robots or authentication.
- [ ] Canonicals, hreflang, links, breadcrumbs and sitemaps point to final URLs.
- [ ] Templates keep main content, links and needed functions.
- [ ] Forms, checkout, login, consent and analytics verified.

**Launch and follow-up**
- [ ] Search Console and Bing Webmaster Tools verify the relevant properties.
- [ ] Change of Address only for eligible moves, on every required variant.
- [ ] New sitemaps submitted; no staging, redirects or `noindex` in them.
- [ ] Monitoring of 3xx, 4xx, 5xx, canonicals, indexing, logs and conversions.
- [ ] A rehearsed rollback with thresholds, owners and DNS/redirect decisions.
- [ ] The old domain and its redirects stay live as long as needed.

## Sources

Google (level A): [Site moves with URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) · [Hosting changes without URL changes](https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes) · [Redirects and Google Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects) · [Canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) · [Troubleshoot crawling errors](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors) · [Block indexing with `noindex`](https://developers.google.com/search/docs/crawling-indexing/block-indexing) · [robots.txt introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro) · [Change of Address tool](https://support.google.com/webmasters/answer/9370220) · [Search documentation updates (17 Jun 2026: domain variants)](https://developers.google.com/search/updates).

Microsoft (level A): [Website migration with Bing](https://blogs.bing.com/webmaster/2020/12/Website-Migration-with-Bing/) (check against current BWT docs) · [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) · [IndexNow](https://www.bing.com/webmasters/help/indexnow-0z209wby).

Practitioner (level C, subordinate to official docs): [Aleyda Solis — SEO migration checklist](https://www.aleydasolis.com/en/seo/seo-migration-checklist/) · [Screaming Frog — website migration guide](https://www.screamingfrog.co.uk/seo-spider/tutorials/website-migration-guide/).
