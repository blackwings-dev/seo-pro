# E-commerce layer (practices E1–E24)

Covers online stores: categories, brands, products, facets, variants, crawling and indexing; structured data and feeds; Merchant Center and free listings; images; stock and URL lifecycle; internal search; international stores; measurement; and the emerging agentic-commerce surfaces. Read `README.md` in this folder first; it extends core practices 20, 22, 26, 71, 111, 114, 115, 121 and 133–137.

Research snapshot: **18 October 2026**. Feed specifications, structured-data requirements and commerce programmes change often; re-check the official links at the end before changing URLs, canonicals, feeds or markup.

**The thesis.** E-commerce SEO depends on the right pages being findable, understandable and correct **at scale**; on a catalogue that matches real needs; and on price, variant, availability, delivery and returns being consistent from the search result to the checkout. A feed, a markup block or a template can't compensate for chaotic architecture or a low-value catalogue. SEO can't fix an uncompetitive product, price or logistics either.

Format: **Why** · **How** · **Expected result** · **Avoid** · **Verify**, with a confidence label from `../research-method.md` where evidence is mixed. Paid feeds (Shopping ads, Product Ads) are mentioned only to keep them separate from SEO.

## Contents
- The catalogue funnel
- Architecture and crawl control: E1–E6
- Variants and product identity: E7–E8
- Product page content: E9–E12
- Structured data, feeds and policies: E13–E16
- Lifecycle, international and platform: E17–E19
- Other channels: Bing ads feeds and agentic commerce: E20–E21
- Measurement: E22–E23
- Priorities by store model: E24
- E-commerce myths · 90-day sequence · checklist · sources

---

## The catalogue funnel

1. **Discovery** — engines and users find categories, brands, products and content through navigation, links, sitemaps and feeds.
2. **Crawling** — filters, sorting, internal search, variants and parameters can multiply URL combinations.
3. **Processing and indexing** — content, canonical, language, product data and relations between categories, variants and products are interpreted.
4. **Product eligibility** — feeds and markup can enable rich results or free listings if they meet policy. They don't guarantee impressions.
5. **Retrieval and ranking** — a query may show a category, a product, a guide, a shopping unit, or a mix; intent may be to explore, compare, check compatibility or buy.
6. **Click and decision** — total price, variant, stock, delivery, trust and UX decide whether the page keeps the result's promise.
7. **Order and retention** — conversion, returns and repeat purchase are business outcomes; impressions, clicks and positions don't prove them.

The main technical risk is letting the URL space grow faster than the catalogue's editorial value. The main commercial risk is promising in search something the page, checkout or inventory can't deliver.

---

## Architecture and crawl control

### E1. Give every page type a purpose — Critical
- **Why:** there is no single "e-commerce page". Categories serve exploration and broad terms; products serve specific intent; guides, comparisons and reviews serve research; brand, shipping, returns, payment and support pages reduce uncertainty.
- **How:** list page types with their intent, URL pattern, indexation decision and owner. Not every type should be indexed (internal search results, cart, account, most sort orders).
- **Expected result:** stable URLs with a clear role.
- **Verify:** Search Console page-indexing grouped by URL pattern (108).

### E2. Taxonomy with HTML paths to every product — Critical · *Established*
- **Why:** Google recommends product pages be reachable through HTML links from menus, categories and subcategories. Sitemaps and feeds help discovery but don't replace navigation or guarantee indexing.
- **How:** department → category → subcategory with descriptive labels and `<a href>` links. For each relevant category: the intent it covers and its active products; title, heading and a useful introduction that doesn't push the grid down; filters on real catalogue attributes; links to subcategories, brands, guides and priority products. There's no universal text length: a short intro can beat hundreds of generic words, a specialist category may need real advice and specs.
- **Avoid:** trees so deep that key products are orphaned or only reachable through internal search; boilerplate category text that swaps only an adjective or a city.
- **Verify:** crawl with JavaScript off; the auditor's orphan and click-depth checks (17).

### E3. Internal linking by value and demand — High
- **How:** link from home, navigation, categories and editorial content to strategic pages (profitable products, launches, seasonal collections, bestsellers) with descriptive anchors. Audit orphan pages, products reachable only via search or filters, categories without a parent link, giant menus and links to parameter URLs or retired products (24).
- **Avoid:** "more internal links" as a goal in itself.
- **Verify:** inbound internal links per priority URL in the crawl report.

### E4. Pagination, "load more" and infinite scroll — High
- **Why:** Google generally crawls URLs from `href` attributes; it doesn't click buttons or perform every user action.
- **How:** distinct URLs per page with sequential `<a href>` links; a **self-referencing** canonical on each indexable paginated page; progressive loading can coexist with linked pagination (22).
- **Avoid:** canonicalising every page to page 1; `#` fragments as the only pagination mechanism; "load more" with no URL behind it.
- **Verify:** with JavaScript disabled, reach the last page of the largest category.

### E5. Faceted navigation: a policy per URL pattern — Critical · *Established (Google's faceted-navigation guidance)*
- **Why:** filters by size, colour, price, brand, availability and sort help shoppers, and every combination can become a crawlable URL with no demand or distinct content. Google warns faceted URLs can create near-infinite spaces, consume crawl resources and delay discovery of useful URLs.
- **How:** inventory parameters and combinations **before** touching `robots.txt`:

| URL type | Possible treatment | Criterion |
|---|---|---|
| Base category | Indexable | Real inventory, demand, stable intent |
| Filter with its own demand | Curated, indexable landing, often on a clean path | Enough offer, own content and purpose; doesn't duplicate the base category |
| Arbitrary combination, sort or price range | Usually not indexable, with crawl control | Avoid millions of low-value URLs without removing filters for users |
| Tracking parameters | Canonical without them; never link internally with them | Not a new editorial page |
| Impossible filter or zero results | A proper HTTP status — usually 404 | Don't serve an empty 200 page or redirect everything to one page |

  Google notes canonical and `nofollow` are usually less effective long term than explicitly controlling URLs if the goal is saving crawl. But a robots.txt block also stops Google reading a page's `noindex`: if a facet is **already indexed**, plan its removal (noindex, delisting) **before** blocking crawling (20).
- **Avoid:** broad regexes that block categories or products; generic rules copied from another platform without a parameter map.
- **Verify:** the auditor's crawl mode reports parameterised internal links by parameter name; Crawl stats and server logs (124).

### E6. Internal search is a tool, not a landing farm — Medium
- **How:** tolerate synonyms, typos, attributes, SKUs and alternative names; suggest; explain empty results. Measure zero-result queries, reformulations, filter use, listing-to-product clicks, out-of-stock items in results and conversion by query (115).
- **Avoid:** indexing every internal query as a landing page. Promote a query to a curated landing only after checking external demand, inventory, uniqueness and maintenance.
- **Verify:** internal search URLs aren't indexed (`site:` + Page indexing) unless deliberately curated.

---

## Variants and product identity

### E7. Variants: URL strategy plus `ProductGroup` — High · *Established for markup; URL choice depends on the catalogue*
- **How:** represent size, colour, material or capacity either on one page with a selector or on separate variant URLs, according to how people shop, real price/stock differences and whether a variant satisfies a query on its own. Keep IDs, SKU, GTIN and group relations correct. Google documents `ProductGroup` with `variesBy`, `hasVariant` and `productGroupID`; single-page and multi-page variant patterns are marked up differently. Feed links must land on the variant matching the feed's title, image, price and availability, **preselected**.
- **Avoid:** indexing every size and colour by default, or canonicalising all variants to the parent by default. Neither is a universal rule.
- **Verify:** open feed URLs: the right variant loads preselected with the matching price; Rich Results Test for `ProductGroup`.

### E8. Real identifiers — High · *Established*
- **How:** manufacturer and model; brand, SKU, GTIN and MPN where they exist. Google recommends valid identifiers and warns products with an assigned GTIN may get limited visibility if it's omitted. If none exists, use `identifier_exists` correctly.
- **Avoid:** invented GTINs, specs, certifications or reviews; filler values in identifier fields.
- **Verify:** Merchant Center diagnostics; a GTIN checksum check in the catalogue QA.

---

## Product page content

### E9. Information that decides the purchase — High
- **Why:** shoppers get stuck on scale, size choice, images and missing details (Baymard usability testing). That's UX evidence, not a ranking factor, and it's what makes a click convert.
- **How:** per product, as relevant: identity and specs with units; compatibility; dimensions, size, materials and limits of use; what's in the box; condition; available and selected variants; price, currency, stock and restrictions; delivery, pickup, returns, warranty and support.
- **Verify:** test with real users on the top templates; track support questions per product.

### E10. Original text, not only the manufacturer's — High
- **How:** manufacturer copy may be all you have for catalogue items, but it doesn't differentiate the seller. Add real value where you can: usage tests, verified compatibility, comparisons, size guides, care, own photos, instructions, support context. For own-brand products document materials, tolerances, manufacture, care, verifiable claims and differences from alternatives.
- **Avoid:** rewriting the same text with synonyms across hundreds of products; padding to an arbitrary length; claiming hands-on experience a reseller doesn't have.
- **Verify:** sample product pages for unique, decision-relevant content.

### E11. Images, video and accessibility — Medium
- **How:** sharp, representative, current images (angles, scale, texture, inside, label or size, as the category needs); the main image shows the variant sent in the feed and isn't hidden behind promotional overlays; descriptive `alt` when it helps understanding; appropriate resolution and weight without losing the detail needed to decide (122); usage or assembly video with controls and captions/transcript where it resolves real doubts (146); gallery and selector usable by keyboard and assistive tech (35, 36).
- **Avoid:** keyword-stuffed `alt`; a hero image lazy-loaded (13).
- **Verify:** Merchant Center image diagnostics; keyboard test of the gallery.

### E12. Price, total cost, stock and CTA transparency — Critical
- **How:** show the **selected variant's** price, currency, taxes or tax indication, extra costs and availability; explain stock changes between page load and checkout; present subscriptions, deposits, volume or member prices transparently and send the price that meets the requirements for the target audience. Promotional prices are subject to local rules: in the EU, price-reduction announcements generally refer to the lowest price applied in the previous 30 days, with exceptions (check local transposition; myths, 114).
- **Avoid:** false scarcity (111); a price in the result that the checkout doesn't honour.
- **Verify:** price and stock match across page, checkout, JSON-LD and feed (E16).

---

## Structured data, feeds and policies

### E13. Product structured data: the right type, in the initial HTML — High · *Established*
- **How:** Google distinguishes **Product snippets** (product pages or related content such as editorial reviews) from **Merchant listings** (pages where the product can be bought); requirements and properties differ. Use `Product`, `Offer`, `ProductGroup`, `AggregateRating`/`Review` (genuine, visible, policy-compliant) and shipping/return details where applicable. JSON-LD must not show values different from the visible page; update price, currency, stock, condition and variant with the selection; prefer including the main product data in the **server HTML** rather than injecting it later (71).
- **Avoid:** several apps or plugins emitting `Product` at once with contradictory fields; stale data in the initial HTML corrected only after interaction; promising stars or price snippets (Google decides).
- **Verify:** Rich Results Test; Search Console *Product snippets* and *Merchant listings* reports; the auditor's `Product` checks.

### E14. Shipping and return policies — High · *Established (Google, Nov 2025)*
- **How:** since November 2025 Google accepts shipping and return policies **without a Merchant Center account**: configure them in Search Console (*Shipping and returns* settings) or with **organization-level** shipping and return-policy markup nested under `Organization` on the policy page. Precedence: Search Console settings override on-site structured data; product-level shipping markup overrides the organization-level policy for those items. Merchant Center remains the place to manage policies for feeds and listings. Keep the visible policy pages, checkout and every configuration in agreement.
- **Avoid:** markup that says "free returns" while the policy page says otherwise; forgetting per-market differences.
- **Verify:** Search Console settings and enhancement reports; Merchant Center policy status.

### E15. Merchant Center feed and free listings — High
- **Why:** free listings can show products across Google surfaces (Search, Shopping, Maps, Images, Lens, YouTube…) depending on eligibility and region. Activation doesn't guarantee each item is shown; approval doesn't mean organic positions.
- **How:** per item: stable unique `id`; `title`, `description`, item-specific `link`, `image_link`, `price`, `availability`, `condition` and applicable identifiers; `item_group_id` and consistent variant attributes; price and availability per market and currency; shipping, delivery, returns and business details visible on the site and in Merchant Center; the landing loads the right product with the variant preselected; crawlable landing without pop-ups hiding essential data. Monitor rejections, mismatches and update latency.
- **Avoid:** treating the feed as a sitemap or as an "SEO copy" of the catalogue.
- **Verify:** Merchant Center diagnostics; landing-page and price/availability mismatch reports.

### E16. Catalogue reconciliation — Critical
- **How:** derive the site, the JSON-LD and every feed from a master catalogue, or reconcile them automatically, and detect divergence before it ships.

| Field | Master source | Check |
|---|---|---|
| ID/SKU and variants | ERP/PIM | Unique, stable, variants map correctly |
| GTIN/MPN/brand | Manufacturer/PIM | Format, validity, no invented values |
| Price and currency | Commercial catalogue | Page, checkout, JSON-LD and feed agree |
| Availability | Inventory | Landing, selector, cart, feed, restock date |
| URL and language | Store | Canonical, feed, hreflang, selected variant |
| Image | DAM/PIM | Right product and variant, reachable URL, format |
| Shipping/returns | Per-market, per-product policy | Legal page, checkout, Search Console / Merchant Center |

  Match update frequency to the real rate of change: if price or stock changes several times a day, a daily feed isn't enough; sync on events or incrementally and measure discrepancies.
- **Verify:** an automated daily diff with alerts (120).

---

## Lifecycle, international and platform

### E17. Stock states and URL lifecycle — High
- **Why:** a temporarily sold-out product can keep value, links, reviews and demand; auto-removing it or returning 404 when stock hits zero erases useful signals. Keeping hundreds of obsolete pages forever without substitute or use can degrade catalogue quality too.

| State | Possible treatment |
|---|---|
| Temporarily out of stock, restock likely | Keep URL and context; mark out of stock; disable impossible purchase; offer alerts/alternatives; update feed and markup |
| Pre-order / backorder | Reliable date or estimate and the correct status on page and feed; never simulate stock |
| One variant out, others available | Keep the page; clearly disable sold-out options; keep valid routes |
| Discontinued with a direct substitute | Explain end of sale and link the replacement; redirect only if the substitute truly meets the same need |
| Discontinued, no substitute, no residual value | Retire with 404/410; don't redirect everything to the home page |
| Recurring seasonal collection | Keep or retire by demand and calendar; state availability and next season accurately |

- **Avoid:** redirecting a specific model to a generic category (it frustrates whoever searched for it and may be treated as a soft 404).
- **Verify:** check traffic, queries, links, sales and support before retiring URLs.

### E18. International stores — High
- **How:** separate language, currency, price, taxes, stock, shipping, returns and regional availability per market; stable URLs per language/country, `hreflang` between true equivalents, correct canonicals and market-appropriate prices (133–137). Per market verify: feed and landing language; currency and tax treatment; price and reference promo price; shipping, delivery time, pickup and returns; sellable stock; units and sizing; payment, support, warranty and privacy; Merchant Center target.
- **Avoid:** forced IP redirects that block users or crawlers from other versions (133); machine-translating legal text, guides or specs where translation could change meaning or compliance.
- **Verify:** hreflang validation; a test order path per market.

### E19. Platform, apps and performance — Medium
- **How:** fast, stable pages for people, crawlers and inventory updates: sized images, caching, fonts, third-party scripts, layout stability, secure checkout, uptime (6, 14). On SaaS platforms or custom frameworks, URL conventions, canonicals, facets, sitemaps and schema depend on the theme and installed apps: audit the **served HTML** and behaviour when selecting variants. Public product pages, protected checkout; consent and privacy; a WAF that doesn't block legitimate bots (A7).
- **Avoid:** presenting Core Web Vitals as a magic ranking lever; multiple apps generating Product schema or feeds simultaneously.
- **Verify:** the auditor flags duplicate `Product` nodes; logs for crawl explosions.

---

## Other channels

### E20. Bing and Microsoft Merchant Center: keep ads separate — Medium
- **Why:** Microsoft documents Merchant Center and its Content API to manage catalogues for Microsoft Shopping and Product Ads — paid campaigns. A feed can improve ad quality and freshness; it isn't an organic SEO lever, and no Google-equivalent organic catalogue surface on Bing is documented.
- **How:** keep apart (1) organic indexing in Bing and Bing Webmaster Tools (B1–B9), (2) ad catalogues in Microsoft Merchant Center, (3) any new commerce integration, each with its own rules and metrics.
- **Avoid:** selling a Microsoft feed as "Bing SEO".

### E21. Agentic commerce (AI shopping and checkout) — Medium · *Emerging; Hypothesis for SEO impact*
- **What exists (Oct 2026):**
  - **Google — Universal Commerce Protocol (UCP).** An open protocol (launched January 2026, co-developed with retailers and platforms such as Shopify, Etsy, Wayfair, Target and Walmart) that lets AI agents complete purchases. Google's implementation adds checkout in AI Mode and Gemini via Merchant Center (*Settings → UCP integration*), a `native_commerce` attribute on eligible products and a merchant manifest. It is in **early access, rolling out in the US**, with more countries announced.
  - **OpenAI — Agentic Commerce Protocol (ACP)**, with Stripe (Sept 2025, open spec). Since March 2026 OpenAI uses ACP mainly for **product discovery in ChatGPT** (merchant product feeds and promotions, directly or via platforms such as Shopify Catalog); it scaled back the original Instant Checkout and lets merchants use their own checkout or a ChatGPT app.
  - **Microsoft** has announced agentic-commerce initiatives; conditions and markets vary.
- **How:** treat each as a **separate product surface**, not an SEO ranking factor. Keep the foundations that every one of them consumes: an accurate master catalogue (E16), consistent price/stock/policies (E12, E14), crawlable product pages and current feeds. Implement a specific protocol only when it's documented and available in your market, you have the engineering to keep it in sync, and you can measure it (orders, returns, margin per channel).
- **Avoid:** "UCP/ACP will boost our rankings"; publishing a feed or manifest you can't keep in sync (wrong prices in an agent's answer are worse than absence); confusing ChatGPT shopping visibility with `OAI-SearchBot` access, which is a separate decision (A2, A4).
- **Verify:** channel-level orders and errors; the AI observation log (A15) for product answers.

---

## Measurement

### E22. Measure SEO, feeds, UX and business separately — High

| Stage | Metrics | Typical source | Prudent reading |
|---|---|---|---|
| Crawl/index | URLs crawled/indexed, errors, chosen canonicals, orphans | Search Console, Bing Webmaster Tools, logs, crawler | Coverage isn't ranking or demand |
| Organic visibility | Impressions, clicks, CTR, position by query/page/country | Search Console, Bing Webmaster Tools | Aggregate position depends on query and surface mix |
| Commercial eligibility | Approved products, errors, feed status, mismatches | Merchant Center | Approval ≠ impressions or sales |
| Traffic | Organic sessions, landing pages, new/returning | Consented analytics | Privacy and attribution lose part of the channel |
| Commerce | Add-to-cart, checkout started, purchase, revenue, margin | E-commerce analytics/ERP | Separate SEO from promotions, stock and price |
| Experience | Zero-result searches, filter use, variant errors | Product analytics, user tests | Needs context and segmentation |
| Profitability | Margin, return cost, assisted sales, incremental contribution | Finance/CRM | Gross revenue isn't SEO profitability |

- **How:** segment by page type (category, product, brand, guide), brand/non-brand (117), country, device, margin, stock and season. Define the **denominator** for every catalogue rate: active products → public, linked pages → index-eligible → indexed → valid markup → approved in Merchant Center → with impressions/clicks → with add-to-cart → with orders. A high approval rate doesn't imply traffic; a high index rate can include pages without demand.
- **Avoid:** treating Search Console CTR as conversion; a global cart-abandonment average (Baymard's compiled ~70%) as your target: it mixes countries, devices, sectors and definitions.
- **Verify:** one stage-by-stage view combining Search Console, logs, Merchant Center, analytics and ERP.

### E23. Experiments on cohorts — Medium
- **How:** hypotheses linking change and outcome (e.g. "a compatibility table reduces zero-result internal searches and lifts add-to-cart from generic queries"); comparable groups; control for season, stock, price and promotions; date every deployment; separate SEO from UX/sales effects; label low-volume results as directional. Test representative templates first and validate canonical, markup, variant, pagination and feed.
- **Avoid:** shipping template, feed, URL and content changes across the whole catalogue at once.
- **Verify:** a change log tied to cohorts.

---

## E24. Priorities by store model

| Model | Special priorities |
|---|---|
| Small catalogue / own brand | Originality, comparison guides, own images, correct product data, useful categories, genuine reviews |
| Large retailer / big catalogue | Taxonomy governance, PIM, facets, crawl control, frequent feeds, stock, variant deduplication, automated QA |
| Marketplace | Seller identity, content attribution, duplicate control, offer vs product URLs, review policies, seller pages |
| Fashion and footwear | Size system, colour, fit guide, visible variant, stock per size, material, scale images, returns |
| Electronics | Exact model, compatibility, generation, normalised specs, SKU differences, warranty |
| Food / beauty / health | Ingredients, allergens, volume, restrictions, verifiable claims, regulatory compliance |
| Personalised products | Configurable price, limits, production time, examples, preselectable URL, clear returns |
| B2B / volume | Minimum quantity, unit price, availability, support, data sheet, quotes, trade access |
| Omnichannel | Stock per store, pickup, local prices, local inventory feeds, store pages where available (`local.md`) |

---

## E-commerce myths

| Claim | Assessment | Defensible practice |
|---|---|---|
| "Index every filter URL to capture long-tail" | Can explode duplicate or empty combinations | Index facets with distinct demand, offer and content (E5) |
| "Block every facet in robots.txt" | Can block useful pages or hide a `noindex` | Audit parameters and index status; a policy per pattern |
| "Every colour and size needs an indexable URL" | Depends on intent, UX, inventory and design | Stable URLs where they add value and you can maintain them (E7) |
| "Schema guarantees stars or price snippets" | Google decides and applies policies | Truthful data, validation, monitoring |
| "The feed lifts organic rankings" | Feeds power listings and ads; not organic ranking | Treat each destination as a separate channel (E15, E20) |
| "Delete every sold-out product" | Can destroy demand, links and useful alternatives | Distinguish temporary, permanent, substitute and seasonal (E17) |
| "More words per product = more SEO" | No universal length; repeated filler hurts | Answer real questions with specs and evidence (E9, E10) |
| "Search Console CTR measures SEO conversions" | Clicks/impressions, not purchases or margin | Join analytics, ERP and Search Console with explicit attribution |
| "The average abandonment rate is our benchmark" | The aggregate mixes categories and reasons | Your own funnel by device, market, channel and checkout |
| "A plugin solves technical SEO automatically" | Apps can duplicate data or mishandle facets and variants | Verify HTML, feed, URLs, canonicals and schema |
| "UCP/ACP or an AI shopping feed is the new SEO" | Separate commerce channels with their own eligibility; no documented organic-ranking effect | Keep catalogue data accurate; adopt a protocol when available and measurable (E21) |

## 90-day sequence (not a traffic forecast)

- **Days 1–15 — catalogue map and baseline:** export URLs, categories, products, variants, stock, canonicals and feeds; pick segments by demand, margin, lifetime value and organic potential; measure indexing, queries, clicks, approvals, sales and returns by page type; map parameters, filters, internal search, pagination and orphans.
- **Days 16–35 — blockers and data:** fix robots/noindex/canonicals, broken links, pagination and rendering; correct price, currency, stock, GTIN, brand, variant, image and feed landing; review shipping, returns, contact, payment, taxes and security per country; remove contradictory JSON-LD or feed sources.
- **Days 36–60 — priority pages:** improve a representative group of categories and products; add specs, compatibility, images and help content with real value; review internal search, filters and the mobile flow with analytics and user tests; write the policy for sold-out, substitutes, discontinued and seasonal URLs.
- **Days 61–90 — measure, learn, scale:** one stage-by-stage view (Search Console, logs, Merchant Center, analytics, ERP); compare treated cohorts with comparable groups; note stock, price, campaign, season and platform changes; scale low-risk wins; set alerts for price/stock/feed and automated QA on critical pages.

## Executive checklist

- [ ] A master source for products, variants, IDs, prices and stock.
- [ ] Important categories and products reachable through HTML links.
- [ ] Listing pages have a purpose, real inventory and clear navigation.
- [ ] Facets, sort orders and internal search have an explicit crawl/index policy.
- [ ] Pagination and progressive loading let crawlers reach the whole catalogue.
- [ ] Each product has coherent URL, canonical and variant representation.
- [ ] Text, price, currency, image and stock match across page, checkout, feed and markup.
- [ ] GTIN/MPN/brand/SKU are real, correct and stable.
- [ ] Pages describe specs, compatibility, limits and conditions.
- [ ] Images show the product and variant, with quality and accessibility.
- [ ] `Product`, `Offer`, `ProductGroup`, reviews and shipping/return markup meet current requirements.
- [ ] Shipping and return policies agree across pages, Search Console and Merchant Center.
- [ ] Merchant Center and Bing are monitored without confusing ad feeds with organic ranking.
- [ ] A process for sold-out, pre-order, substitutes, closures and redirects.
- [ ] Shipping, returns, contact, payment and legal information are clear per market.
- [ ] Measurement separates crawl, index, impression, click, cart, order, margin and return.
- [ ] Changes are tested on cohorts, noting stock, price, promotions and season.

## Sources

Google (level A): [Ecommerce SEO best practices](https://developers.google.com/search/docs/specialty/ecommerce) · [Help Google understand your site structure](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure) · [Managing crawling of faceted navigation URLs](https://developers.google.com/crawling/docs/faceted-navigation) · [Pagination and incremental page loading](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading) · [URL structure for ecommerce sites](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites) · [Share product data with Google](https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google) · [Product structured data](https://developers.google.com/search/docs/appearance/structured-data/product) · [Product variant structured data](https://developers.google.com/search/docs/appearance/structured-data/product-variants) · [More ways to share shipping and returns policies (Nov 2025)](https://developers.google.com/search/blog/2025/11/more-ways-to-share-shipping) · [Write high-quality reviews](https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews) · [Launching a new ecommerce site](https://developers.google.com/search/docs/specialty/ecommerce/how-to-launch-an-ecommerce-website) · Merchant Center: [product data specification](https://support.google.com/merchants/answer/7052112), [unique product identifiers](https://support.google.com/merchants/answer/160161), [landing page requirements](https://support.google.com/merchants/answer/4752265), [free listings](https://support.google.com/merchants/answer/13889434), [return policies](https://support.google.com/merchants/answer/14011730), [UCP integration in Merchant Center](https://developers.google.com/merchant/ucp/guides/tools/merchant-center/overview).

Microsoft and OpenAI (level A): [Content API for Microsoft Merchant Center](https://learn.microsoft.com/en-us/advertising/shopping-content/) · [Microsoft Merchant Center help](https://help.ads.microsoft.com/apex/index/3/en/60048) · [OpenAI — Powering product discovery in ChatGPT (Mar 2026)](https://openai.com/index/powering-product-discovery-in-chatgpt/) · [Agentic Commerce Protocol repository](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol).

UX research (level B, not ranking evidence): [Baymard — checkout usability](https://baymard.com/research/checkout-usability) · [product page UX](https://baymard.com/research-articles/current-state-ecommerce-product-page-ux) · [product listing page UX](https://baymard.com/blog/product-listing-page-plp-ux) · [filter UI](https://baymard.com/blog/ecommerce-filter-ui).

Regulation (starting point): [European Commission guidance on price-reduction announcements](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52021XC1229%2806%29).
