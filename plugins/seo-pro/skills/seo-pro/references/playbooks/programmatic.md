# Programmatic and template-driven pages playbook (D1–D12)

For any site that generates many pages from data and templates: location × service pages, product or listing pages, integration directories, comparison matrices, glossaries, job or property listings, travel routes, statistics pages, AI-assisted page sets. It expands core practices 26, 45, 54, 121 and 155 and connects to `../verticals/local.md` L12–L13, `../verticals/ecommerce.md` E5, `../verticals/saas-services.md` S2/S8 and `../verticals/regulated.md` Y12/Y14. Read `README.md` in this folder first.

Research snapshot: **18 October 2026**. Google's spam policies define **scaled content abuse** (many pages generated primarily to manipulate rankings without helping users, however they're produced — automation, AI, humans or a mix) and **doorway abuse** (pages created to rank for specific, similar queries that funnel users elsewhere or offer little distinct value). Google introduced the scaled-content wording in March 2024 and in 2026 states its spam policies apply to AI Overviews and AI Mode too.

**The thesis.** Programmatic SEO is legitimate when **each page answers a distinct need with data the user can't get from the next page** — a real listing, a real route with prices, a real integration, a real location. It's spam when the template is the content and the data is a keyword swap. The question is never "can we generate it?" but "would this page deserve to exist if search engines didn't?"

Format: **Why** · **How** · **Avoid** · **Verify**.

---

### D1. Start from a data asset, not a keyword list — Critical
- **How:** name the data that makes each page unique: inventory, prices, availability, schedules, specifications, reviews you're entitled to show, measurements, first-party statistics, licensed datasets, user-generated content with moderation. Document source, licence, freshness, coverage and error rate. If the only variable is a city or keyword, there's no asset.
- **Avoid:** scraped or unlicensed data; data you can't keep current.
- **Verify:** for a random sample of 20 pages, list the facts that appear only on that page.

### D2. The legitimacy test — Critical · *Established (Google spam policies)*
- **How:** before building, answer for the page type: does it serve a query people actually make with this combination? does each page offer distinct, useful information or functionality? would a user who lands on it be satisfied without going back to search? is the page useful to visitors who arrive from your own navigation? would you build it without search engines? Any "no" means redesign, merge into a hub, or don't build.
- **Avoid:** "best [service] in [city]" pages for places you don't serve; "[tool A] + [tool B]" pages for integrations that don't exist; AI-written filler paragraphs to make thin pages look unique (scaled content abuse applies regardless of the tool).

### D3. Template quality is product quality — High
- **How:** design the template around the user's task: the key data first (price, availability, distance, spec table, map, steps), then context that changes with the data (local regulations, compatibility notes, seasonality), then related options. Text blocks must be **data-conditional** — written for the cases where they're true — not the same paragraph with variables. Include proof elements (photos, reviews, sources, dates) only where real.
- **Avoid:** spun text, filler intros, identical FAQ blocks across thousands of pages, empty-state pages that render a template with no data.

### D4. Indexing thresholds and empty states — Critical
- **How:** set rules per page type: index only when data meets a threshold (e.g. minimum listings, reviews, price points or text that differs); otherwise `noindex` (crawlable, so the directive is read) or don't generate the URL; return **404** for impossible or zero-result combinations rather than an empty 200 (E5, 9). Re-evaluate pages as data grows or decays.
- **Verify:** the share of indexable pages that pass the threshold is 100%; Search Console "Crawled – currently not indexed" and "Duplicate" per page type.

### D5. URL design and canonicalisation — High
- **How:** one clean URL per combination that deserves to exist; a consistent order for combined attributes; canonical to self on indexable pages; parameters for sorting/filters kept out of the index (20). Decide how to handle synonyms and near-duplicates (one URL, others redirect or canonicalise).
- **Avoid:** both `/plumber-valencia/` and `/valencia/plumber/` live; canonicals pointing to a parent that doesn't contain the same information.

### D6. Hubs and internal linking — High
- **How:** organise generated pages under hubs that are useful in themselves (by region, category, integration type), with HTML links down to children and across to genuinely related siblings (45, 155). Link from editorial content where relevant. Keep click depth reasonable for the pages that matter (17).
- **Avoid:** orphaned pages reachable only through the sitemap; giant link blocks of every city in the footer.

### D7. Crawl budget and sitemaps at scale — High
- **How:** segmented sitemaps per page type and update frequency with accurate `lastmod` (2); IndexNow for additions, changes and deletions (B2); server capacity for crawl spikes; logs to see what bots actually crawl (124). Large sites watch the ratio of crawled to valuable URLs.
- **Avoid:** sitemaps listing `noindex`, redirected or below-threshold URLs.

### D8. Launch in waves, measure by cohort — Critical
- **How:** launch a representative sample first (e.g. 5–10% of the planned pages, stratified), with a control group of comparable combinations not yet launched where possible; measure by cohort: indexing rate, impressions and clicks per page, engagement, conversions, complaints (X11–X12). Scale only if the cohort earns indexing and satisfies users; otherwise fix the template or the threshold first.
- **Avoid:** publishing 50,000 pages in one deploy; judging success by pages published.

### D9. AI in programmatic pipelines — Critical
- **How:** use AI for drafting data-conditional text, classification, summarising **your own** data, translation drafts and QA — with human review of templates and a sampling review of outputs; verify every factual statement against the data; log model and prompt versions; block publishing when data fields are missing rather than letting the model invent them. For YMYL topics, apply `../verticals/regulated.md` Y14 — generated advice without qualified review must not be published.
- **Avoid:** using AI to fake uniqueness on thin pages; hallucinated facts (addresses, prices, specs, laws) rendered at scale.

### D10. Structured data that reflects each page — Medium
- **How:** generate markup from the same data as the visible page (`Product`, `JobPosting`, `LocalBusiness`, `Event`, `Dataset`, `BreadcrumbList`…), following each feature's eligibility rules; validate a sample per template on every release (G10).
- **Avoid:** markup values that the page doesn't show; self-serving review markup (85).

### D11. Maintenance, decay and pruning — High
- **How:** data freshness monitors (prices, availability, closed locations, expired jobs or events); automatic status changes (sold, expired, closed) with the right HTTP response and messaging (E17); periodic pruning of pages that never earned impressions or that fall below the threshold — merge, `noindex` or remove with 404/410, assessing links first (26, 84).
- **Avoid:** thousands of stale pages showing wrong prices or closed businesses.

### D12. Third-party and partner page sets — Critical
- **How:** if partners, affiliates or vendors supply page sets on your domain, apply the same legitimacy test and editorial control as your own. Hosting third-party content mainly to exploit your site's ranking signals is **site reputation abuse** (`reputation.md` R9, `governance.md` G13).
- **Avoid:** renting a subfolder to a coupon, loan or "best of" network.

---

## Good and bad patterns

| Pattern | Usually legitimate when… | Usually spam when… |
|---|---|---|
| Location × service | You serve the area and the page shows area-specific proof, coverage, prices or regulations | Only the city name changes; no presence or service there (doorway) |
| Product / listing pages | Each item is real, current and purchasable/viewable | Expired, duplicated or scraped listings |
| Integrations / "connect X to Y" | The integration exists and the page explains what it does and how | Combinatorial pages for non-existent pairs |
| Comparison matrices | Criteria, sources and dates per comparison | Auto-generated "X vs Y" with no real evaluation |
| Glossary / definitions | Expert definitions with examples, linked to deeper content | Thousands of one-line AI definitions |
| Statistics / data pages | First-party or licensed data with method and update date | Copied public data with no added analysis |

## Myths

| Claim | Assessment | Defensible practice |
|---|---|---|
| "AI text makes each programmatic page unique" | Uniqueness of words isn't usefulness; scaled content abuse applies to any production method | Unique data and task value (D1–D3, D9) |
| "Google penalises programmatic SEO" | It targets scaled pages without value, not templates as such | Pass the legitimacy test (D2) |
| "Index everything; Google will sort it out" | Thin URLs waste crawl and can drag perception of the site | Thresholds, 404 for empty combinations (D4) |
| "Launch big to win fast" | No way to learn or roll back | Waves with cohorts and controls (D8) |

## Executive checklist

- [ ] Each page type has a named data asset with source, licence and freshness.
- [ ] The legitimacy test is passed and documented per page type.
- [ ] Templates show key data first and use data-conditional text.
- [ ] Indexing thresholds exist; empty combinations return 404 or aren't generated.
- [ ] One canonical URL per combination; parameters out of the index.
- [ ] Useful hubs with HTML links; no orphan or footer link farms.
- [ ] Segmented sitemaps with accurate `lastmod`; IndexNow for changes.
- [ ] Launch in waves with cohorts and a control; scale on evidence.
- [ ] AI only with data-grounded generation, human review and logs; YMYL excluded without qualified review.
- [ ] Freshness monitors and periodic pruning.
- [ ] No third-party page sets exploiting the site's signals.

## Sources

Google (level A): [Spam policies — scaled content abuse, doorway abuse, site reputation abuse](https://developers.google.com/search/docs/essentials/spam-policies) · [Guidance on generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content) · [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) · [Managing crawling of faceted navigation URLs](https://developers.google.com/crawling/docs/faceted-navigation) · [Large site crawl budget management](https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget) · [Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview). Microsoft: [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) (names unreviewed auto-generated content at scale) · [IndexNow](https://www.bing.com/webmasters/help/indexnow-0z209wby).
