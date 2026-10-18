# Phase 3 — Authority, analytics, automation and international (practices 86–160)

Goal: with a sound technical base and content that answers, **scale**: legitimate external authority, trust signals, data-driven decisions, fine-grained crawl control, international expansion and automated processes that prevent regressions.

"Phase running" criteria: sustained growth in non-brand clicks and brand searches, a natural and growing link profile, citations in AI answers, automated alerts in place and an established review cadence.

Format: **Why** · **How** · **Expected result** · **Avoid** · **Verify**. Minor practices use a condensed format.

## Contents
- Authority and links: 86–101
- E-E-A-T and trust: 102–106
- Analytics and CRO: 107–119
- Automation and advanced crawl control: 120–132
- International, entities and formats: 133–148
- Growth and maintenance: 149–160

## The golden rule of links

A link is worth having if **a human would add it even if Google didn't exist** (because it cites your data, recommends your tool or reports on your company). Buying links, mass link exchanges, private blog networks, sponsored posts without `rel="sponsored"`, or paid "mentions" to get cited by AIs are all covered by Google's spam policies. The cost of a manual action is far greater than the gain. When the user asks to "get backlinks", propose tactics from this list, never purchases.

---

## Authority and external links

### 86. Quality backlinks from day one — High
- **How:** suppliers, customers, partners and associations you already have a real relationship with (customer/partner pages, case studies), local media, content collaborations with sites in your industry. Prioritise topical relevance and real traffic of the linking site over third-party metrics (DA/DR).
- **Expected result:** first relevant links within 1–3 months. **Avoid:** "100 links for $50" packages. **Verify:** the "Links" report in Search Console.

### 87. Competitors' broken links (broken link building) — Medium
- **How:** find competitor pages that return 404 and still have external links (Ahrefs/Semrush "Best by links" filtered by 404); create an equivalent or better resource; write to the linking sites offering your URL as a replacement, personally.
- **Avoid:** mass templated emails. **Verify:** reply rate and links earned.

### 88. Cite authoritative sources — Medium
- **How:** link to the primary source (official gazettes, regulators, studies, official documentation) when you state a fact. It helps users, verification and trust.
- **Avoid:** linking to aggregators instead of the source; blanket `nofollow` on legitimate outbound links.

### 89. Link bait with original data — High
- **How:** studies using the business's own (anonymised) data, surveys, price indexes, calculators, maps, charts under a reuse licence that asks for attribution links. Publish the methodology.
- **Expected result:** links and citations from media and AIs. **Avoid:** "studies" without methodology or with made-up data.

### 90. Podcasts, interviews and talks — Medium
- **How:** identify industry podcasts, webinars and events; pitch a specific topic where you bring experience; ask for a link in the show notes or event page.
- **Expected result:** authoritative links plus brand and experience (E-E-A-T) signals.

### 91. Unlinked brand mentions — Medium
- **How:** alerts (Google Alerts, Talkwalker, Mention, SEO tools) for the brand, products and executives' names; when a positive mention has no link, politely ask for one.
- **Avoid:** being pushy; unlinked mentions still help build the entity.

### 92. Anchor text diversity — Medium
- **How:** you don't control anchors of natural links, and that's good. Where you do have influence (partners, collaborations), favour brand, URL and natural descriptions.
- **Avoid:** most external links using the same exact-match keyword (a typical pattern of artificial links).

### 93. Links from pages that already rank — Medium
- **How:** in collaborations, suggest adding the link to existing, related content that already has traffic (editorial, free link insertion), explaining which sentence it adds value to for the reader.
- **Avoid:** paying for insertions into articles (still buying links).

### 94. Reclaim lost links — Medium
- **How:** review lost links monthly (SEO tools). Common causes: you changed a URL without a 301 (fix it yourself), the linking page was redesigned (write to the author), or the link was removed on purpose (accept it).
- **Expected result:** most technically lost links recovered.

### 95. Avoid excessive link exchanges — High
- **How:** linking to real partners and being linked by them is normal; the problem is systematic "you link me, I link you" swaps or orchestrated three-way schemes (A→B→C) designed to look natural. Any organised scheme to manipulate links is still a link scheme.
- **Verify:** every link has an editorial justification.

### 96. Press releases built on real data — Medium
- **How:** the release itself (on distribution wires) brings no useful links; what matters is journalists writing their own piece. Send exclusive data and a story to specific journalists who cover the topic, with charts and a spokesperson available.
- **Avoid:** press releases with optimised anchor links (ignored or treated as spam by Google).

### 97. Brand searches — High
- **How:** a memorable brand, presence where the audience is, advertising, newsletters, community, a product people recommend. Track brand searches in Search Console (117).
- **Expected result:** growth in brand and navigational queries — one of the strongest signals that the business is real and relevant.

### 98. Niche directories — Low/Medium
- **How:** only directories your customers would actually use (professional bodies, industry associations, chambers of commerce, sector marketplaces, established local directories). NAP identical to the site and Google Business Profile.
- **Avoid:** mass generic directories and "submit to 500 directories" packages. Local businesses: master location data and citation priorities in `verticals/local.md` L16–L17.

### 99. Local links — Low/Medium
- **How:** links from sites in your target country and language matter because they usually come from your real market; the linking domain's TLD (e.g. `.es`, `.de`) is a weak signal by itself. Prioritise genuine topical and geographic relevance (media, associations and customers in your area).
- **Avoid:** chasing country TLDs unrelated to your business.

### 100. Outbound link policy — Medium
- **How:** link to quality sources; `rel="sponsored"` on paid or affiliate links; `rel="ugc"` on user content; periodically check that linked domains haven't expired or changed hands (links to spam or gambling sites via re-registered domains).
- **Verify:** the auditor's `--crawl` lists external links.

### 101. No paid links or mentions to manipulate rankings — Critical
- **Why:** link schemes intended to manipulate rankings can violate search engine spam policies. Google's published policies also apply to its generative AI responses; check the relevant platform's current policy before making broader claims.
- **How:** for sponsorships, mark the link `rel="sponsored"`; be wary of any agency promising "newspaper links" at a fixed price. Don't rent out sections of your site to third parties exploiting its signals (site reputation abuse). Earned-PR process, review programmes and disavow decisions: `playbooks/reputation.md`.
- **Verify:** no issues under "Manual actions" in Search Console.

---

## E-E-A-T, trust and business signals

E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) is a quality-evaluation concept, not a single score or switch. Google's quality raters use it to assess search result quality; their ratings do not directly control individual rankings. Make trust, authorship, and evidence visible where it helps people, especially for high-impact topics.

### 102. Real authors — High
- **How:** a visible byline with real name, photo, role and relevant background; an author page with bio and links to professional profiles; `Person` JSON-LD as `author` with `url` and `sameAs`. For YMYL topics, review by a professional ("Reviewed by…") with verifiable credentials.
- **Avoid:** invented authors or stock photos (deceptive, and easy to detect). High-impact topics: reviewer roles, claims ledger and corrections in `verticals/regulated.md`; news bylines and transparency in `verticals/publishers.md` P1.

### 103. Experience and empirical evidence — High
- **How:** your own photos of the product or work, case studies with results, tests you've run, real attributed quotes from professionals, "how we do it" explanations. This is exactly what generic AI text can't provide.
- **Avoid:** generic quotes from unnamed "experts".

### 104. Consistent brand identity — Medium
- **How:** same name, logo, short description, NAP and URL across the site, social profiles, directories, Google Business Profile, Wikidata (only if you meet its notability criteria) and `sameAs` (38).
- **Expected result:** a knowledge panel, or at least consistent recognition of the entity in search engines and AIs.

### 105. Job postings — Low
- **How:** if you are genuinely hiring, publish openings on your site with `JobPosting` (they appear in Google for Jobs) and remove them or set `validThrough` once filled. Useful for recruiting; any "legitimacy" benefit for SEO is marginal.
- **Avoid:** fake or expired openings to look bigger: they violate `JobPosting` policies and can lead to a manual action.

### 106. Visible company registration details — High (mandatory in many countries)
- **How:** in the legal notice (and summarised in the footer): legal name, company/tax ID, registered address, company registry entry, professional body and licence number where applicable, regulatory authorisations. Required in much of the EU (e.g. Spain, Germany) and a trust signal everywhere.

---

## Advanced analytics and conversion optimisation (CRO)

### 107. Join Search Console with analytics — High
- **See also:** event contracts, attribution vs causation, cohorts and experiments in `playbooks/measurement.md`.
- **How:** connect Search Console to GA4 (or export both to Looker Studio/BigQuery) and join by landing page: impressions, clicks and position (GSC) with engagement and conversions (analytics). Prioritise: many impressions + low CTR → title/description; many clicks + low conversion → page content/CTA.
- **Expected result:** a prioritised list of pages to optimise every month.

### 108. Group URLs by page type — Medium
- **How:** segment by URL pattern (`/blog/`, `/product/`, `/category/`, `/services/`) in Search Console (page filter with regex) and in analytics (content groups). Makes it easy to see which page type grows or drops after a change or a Google update.

### 109. Detect content decay — High
- **How:** compare clicks per URL across equivalent periods (last 3 months vs the same 3 months last year, to rule out seasonality); flag sustained drops > 20–30 %. Diagnose before acting: did demand fall (Trends), did SERP intent change, did a better competitor appear, did an AI Overview start answering without a click, or is the page simply out of date?
- **Expected result:** pages updated before they lose their rankings entirely (149).

### 110. Heatmaps and scroll maps — Medium
- **How:** Microsoft Clarity (free) or Hotjar, with consent where they use cookies or recordings. See where people drop off, what they click that isn't a link, and whether the CTA is seen.
- **Avoid:** recording forms with personal data unmasked.

### 111. Scarcity and urgency only when real — Medium
- **How:** show low stock, offer deadlines or limited places **only when true and verifiable**.
- **Avoid:** countdowns that reset, a permanent "only 2 left", or fake urgency: these are unfair commercial practices and dark patterns banned in the EU (Unfair Commercial Practices Directive, DSA) and regulated by the FTC in the US, and they destroy trust.

### 112. Minimal forms — High
- **How:** ask only for what's essential at that step; `autocomplete`, inline validation, clear error messages, an alternative contact option (WhatsApp, phone). Every extra field tends to lower conversion.

### 113. Useful thank-you pages — Medium
- **How:** confirm what happens next and when, offer the next step (content, sharing, booking) and fire the conversion event. Mark them `noindex` (they shouldn't appear in Google or record fake conversions from search visits).

### 114. Price anchoring — Low (CRO, not SEO)
- **How:** in plan tables, present or highlight the premium option first so the middle one looks reasonable — always with real, comparable prices and terms.
- **Avoid:** "was" prices that never existed (in the EU, the reference price must be the lowest of the previous 30 days).

### 115. Internal site search — Medium
- **How:** a search that tolerates typos and synonyms; log searched terms and zero-result terms (analytics events) — they are content and product ideas. Results pages set to `noindex` (26).

### 116. Queries with impressions but no clicks — High
- **How:** in Search Console, filter queries with many impressions, position 1–10 and low CTR for their position. Causes: an unappealing title or one misaligned with intent, a competitor's rich result, or an AI Overview or Google feature absorbing the click. Improve the title/description and, for questions, answer better on the page to become the cited source.

### 117. Separate brand and non-brand — High
- **How:** Search Console's **branded queries filter** (since November 2025, for eligible top-level properties) plus your own regex for the brand, its variants and typos (e.g. `(?i)acme ?tools|acmetools`) and its inverse, for cohorts and properties the filter doesn't cover. Both are approximate (anonymised queries are excluded). Non-brand growth mostly reflects SEO; brand growth mostly reflects awareness (`playbooks/measurement.md` X9).

### 118. Keep Search Console history — Medium
- **Tooling:** `scripts/search_data.py gsc-query` exports Search Console (paged up to 25,000 rows per request) and `bing --method GetPageStats` exports Bing, both dependency-free; `compare` and `brand-split` analyse the exports.
- **How:** Search Console keeps only 16 months. Enable the bulk export to BigQuery or download monthly through the API to keep history and get data beyond the UI's 1,000-row limit.

### 119. Dashboard and cadence — High
- **How:** KPIs: non-brand clicks, impressions, indexed vs submitted pages, CWV, organic conversions, brand searches, referring domains, and AI visibility only where a product provides usable reporting or a documented manual sample (148). Choose a cadence suited to the site's scale and change rate; a sensible default is weekly (alerts and drops), monthly (audit, 152), quarterly (content, 149), yearly (strategy).

---

## Automation and advanced crawl control

### 120. De-indexing alerts — High
- **How:** a scheduled script (cron, GitHub Actions, Vercel Cron) that fetches critical URLs and checks: status 200, no `noindex` (meta or `X-Robots-Tag` header), correct canonical, robots.txt without `Disallow: /`. On failure, alert by email/Slack. `scripts/seo_audit.py --urls critical.txt --fail-on critical` is a ready-made base (non-zero exit code on failure).
- **Expected result:** a deploy that breaks SEO is caught in minutes, not weeks.

### 121. Dynamic title templates for e-commerce — Medium
- **How:** a template per page type (`{Product} {Key attribute} – {Brand} | {Store}`), with manual overrides for important pages.
- **Avoid:** price or stock in the title when they change often (mismatch between what Google shows and the page; Google may rewrite). For price and availability in the SERP, the right channel is `Offer` Schema (71). Category and facet titles: `verticals/ecommerce.md` E2, E5.

### 122. Automatic image conversion — High
- **How:** server- or CDN-side optimisation (Next.js `next/image`, Cloudflare Images, Vercel Image Optimization, imgproxy, Thumbor) serving AVIF/WebP at the right size for each device.
- **Avoid:** image URLs that change on every deploy (Google Images loses history).

### 123. Scheduled broken-link crawls — Medium
- **How:** `scripts/seo_audit.py URL --crawl 500` on a monthly schedule, or a scheduled Screaming Frog/Sitebulb crawl; open an issue with the broken links found.

### 124. Server log analysis — Medium (High on large sites)
- **How:** analyse Googlebot hits: which sections it crawls, how often, which status codes it gets, which useless URLs consume crawling. **Verify it's the real Googlebot** (reverse DNS ending in `googlebot.com`/`google.com` plus forward confirmation, or Google's published IP ranges) — many bots impersonate it. On Vercel/Cloudflare use log drains/Logpush.
- **Expected result:** discover ignored sections or crawl traps. Most useful on sites with > 10,000 URLs.

### 125. 304 responses / conditional requests — Medium
- **How:** have the server send `ETag` or `Last-Modified` and respond `304 Not Modified` to `If-None-Match`/`If-Modified-Since` when nothing changed. Googlebot uses this and it saves resources on both sides.
- **Verify:** the auditor repeats the request with the conditional header and checks for a 304. Crawl-budget impact only matters on large sites.

### 126. DOM size — Medium
- **How:** Lighthouse warns above ~800 nodes and flags it as a problem above ~1,400. Remove needless wrapper `div`s, virtualise long lists, don't render huge hidden menus on every page.
- **Verify:** the auditor counts the elements in the served HTML.

### 127. Server-side rendering (SSR/SSG) — Critical for JavaScript frameworks
- **How:** static or incremental generation (SSG/ISR) for content that rarely changes; SSR for content that changes per request; server components (React Server Components) to minimise client JavaScript. See `nextjs.md`.
- **Expected result:** complete HTML in the first response (25).

### 128. Orphaned image clean-up — Low (maintenance, not SEO)
- **How:** remove unreferenced images from storage to shrink backups and costs. No direct ranking effect.
- **Avoid:** deleting images that other sites still link to or that are indexed in Google Images without checking.

### 129. Hotlinking — Low
- **How:** only worth blocking if it causes real bandwidth costs. Block by `Referer` while allowing empty referers, your own domain and **search engines** (or Google Images and other platforms will stop showing your images).
- **Avoid:** rules that return 403 to Googlebot-Image.

### 130. Load testing — Medium
- **How:** before campaigns or launches, test the main journeys with k6, Artillery or Locust at realistic volume. If the server returns sustained 5xx/429, Google reduces its crawl rate.
- **Avoid:** load-testing production without telling the provider or outside low-traffic hours.

### 131. 5xx alerts — High
- **How:** uptime monitoring (UptimeRobot, Better Stack, Checkly) and error tracking (Sentry, provider logs) with alerts. Also check Crawl stats → responses by status in Search Console.

### 132. `rel="ugc"` on user content — Medium
- **How:** `rel="ugc nofollow"` on links in comments, forums and profiles; pre-moderation for new users; `noindex` on empty profiles.

---

## International SEO, entities and formats

### 133. No automatic redirects by IP or language — High
- **How:** Googlebot crawls mostly from the US and without `Accept-Language`; redirect by IP and it may never see your other versions. Show a banner or selector ("Prefer the English version?") and remember the choice; every version has its own URL reachable by everyone.

### 134. International URL structure — High
- **How:** subfolders (`/es/`, `/en/`, `/es-mx/`) are the simplest and concentrate authority; ccTLDs (`.es`, `.mx`) give the strongest geographic signal but multiply the work; subdomains sit in between. Never parameters (`?lang=en`).

### 135. hreflang in the sitemap — Medium (alternative to 137)
- **How:** useful on large sites: `xhtml:link rel="alternate" hreflang="…"` in each `<url>` of the sitemap, listing every version including itself. Choose **one** method (HTML, header or sitemap) and be consistent.

### 136. Localise keywords for each market — High
- **How:** research per country, not translation: "ordenador" (ES) vs "computadora" (MX), "flat" (UK) vs "apartment" (US). Localise prices, currency, date formats, examples and regulations too.
- **Avoid:** unreviewed machine translation.
- **See also:** the international module in `operating-plan.md` (O12) and, for Yandex, Baidu, Naver and Seznam markets, `engines/other-engines.md`.

### 137. Correct hreflang — High (if you have multiple language/country versions)
- **How:** ISO 639-1 language codes and optional ISO 3166-1 region codes (`es`, `es-ES`, `es-MX`, `en`); each page links to all its alternates **and to itself**; reciprocal links (if A points to B, B must point to A); `x-default` for the selector or default version; absolute canonical URLs. hreflang doesn't prevent "duplicate content penalties" (they don't exist); it ensures the right language version is shown.
- **Avoid:** `en-UK` or `es-EU` (invalid; it's `en-GB`); hreflang pointing to URLs canonicalised elsewhere; hreflang on a single-language site.
- **Verify:** the auditor lists hreflang tags and checks `x-default` and self-reference.

### 138. Answers for voice assistants — Low
- **How:** short, self-contained answers (60, 69) cover voice too. There's no profitable voice-specific optimisation beyond that.

### 139. Unconventional screens — Low
- **How:** fluid layouts with `max-width` for reading content, container queries, testing on foldables and ultra-wide monitors. Product quality; indirect SEO impact.

### 140. Entity hierarchy — Medium
- **How:** name the relevant entities (organisations, regulations, places, brands, people) explicitly and consistently, and relate them in the text and in Schema (`about`, `mentions`, `areaServed`, `sameAs` to Wikidata/Wikipedia when they exist).

### 141. Map your industry's knowledge graph — Medium
- **How:** identify the concepts Google associates with your topic (related searches, "People also ask", knowledge panels, Wikipedia categories) and make sure you have content connecting them to your services.

### 142. Implicit searches (the next question) — High
- **How:** at the end of each section or page, answer or link to the logical next question ("how much does it cost?", "how long does it take?", "what do I need?"). It's also how AI Mode conversations work.

### 143. Synonyms and variations — Medium
- **How:** use the variants your customers use (you'll see them in each URL's Search Console queries) naturally in headings and text.

### 144. Downloadable resources — Medium
- **How:** templates, PDF guides, spreadsheets. If you require sign-up, keep an **indexable landing page** that describes the resource with useful content of its own; Google can't index what sits behind a form. Indexable PDFs need a title and real text.
- **Avoid:** the site's only valuable content being behind a form.

### 145. Forum participation — Medium
- **How:** Google surfaces Reddit, forums and communities more and more. Participate with your real profile, answer with value, mention your site only when it's the best answer, and follow each community's rules.
- **Avoid:** fake accounts or mention campaigns (spam, and "inauthentic mentions" for AI features).

### 146. Video — Medium
- **How:** embed videos where they help; for Google to index a video as such, it must be **the main content** of a page (its own watch page) with `VideoObject` (title, description, thumbnail, `uploadDate`, duration) and, if long, `Clip`/key moments. YouTube brings its own visibility in Google.
- **Avoid:** expecting video results from a decorative video in an article.
- **Full layer:** watch pages, `VideoObject`, key moments, livestreams, YouTube ranking, chapters, captions, Test & compare, AI disclosure: `engines/video-images.md` (V1–V11).

### 147. Update content for real (not just the date) — High
- **How:** periodically review the articles with the most traffic or in decay (109): data, screenshots, links, new questions. When the change is **substantial**, update `dateModified` and the visible "Updated on…" date; keep the original publish date.
- **Avoid:** changing the publish date to "today" without real changes to look fresh: Google explicitly advises against it and it can be treated as manipulation. Lifecycle states and review cadence by content type: `playbooks/governance.md` G9.

### 148. Monitor AI visibility — High
- **See also:** the full measurement protocol (query panel, observation log, eight metrics, test design) is `engines/ai-search.md` A14–A17.
- **How:** (1) a fixed, stratified query panel (A14) checked on a schedule across the surfaces that matter, logging each run (A15); (2) the official reports — Search Console **Generative AI performance** and Bing **AI Performance**; (3) analytics segments for AI referrals (`utm_source=chatgpt.com`, `perplexity.ai`, `copilot.microsoft.com`, `gemini.google.com`, `claude.ai`…); (4) commercial AI-visibility trackers only if volume justifies them, reading their definitions first.
- **Expected result:** knowing which topics get you cited and which don't, so you can strengthen content (69) and authority.
- **Avoid:** drawing conclusions from a single test: answers vary by user, location and time.

---

## Growth and maintenance

### 149. Update calendar — High
- **How:** quarterly for pillar pages and the top 20 URLs by traffic; yearly for the rest; immediately when a regulation or price changes. Record the review date in the keyword map (54).

### 150. Triggers in titles — Medium
- **How:** numbers, the year when the content depends on it ("2026"), a concrete benefit, specificity ("in 15 minutes", "no lock-in"). Test and measure (116).
- **Avoid:** clickbait and empty superlatives ("incredible", "ultimate") the page doesn't live up to.

### 151. Brackets and parentheses in titles — Low
- **How:** they can help a result stand out ("[Free template]", "(2026 guide)"), but the oft-quoted CTR uplift comes from old studies and Google frequently rewrites titles. Test on a few pages and compare CTR before/after over 4 weeks.

### 152. Monthly audit — High
- **How:** `scripts/seo_audit.py URL --crawl 500 --output audit-YYYY-MM.md` + a Search Console review (indexing, CWV, enhancements, manual actions, security) + comparison with the previous month.

### 153. Disavow only when needed — Low
- **How:** Google automatically ignores the vast majority of junk links. Use the disavow tool **only** if you have a manual action for unnatural links or know of a large past link purchase (e.g. by a previous agency) that could trigger one.
- **Avoid:** mass-disavowing "toxic links" based on a tool's score: you may remove links that were helping you. Five-step process: `playbooks/reputation.md` R10.

### 154. Linkable assets — High
- **How:** the asset your industry would cite: a free tool, an annual study, a reference template, a definitive guide kept up to date, a public dataset. Promote it actively (86, 96).

### 155. Maintain the clusters — Medium
- **How:** each new piece is assigned to a cluster in the map (54) and linked to its pillar and siblings on publication; the pillar is updated to link to the new piece.

### 156. Technical, content and UX together — (principle)
- Not a task but the principle behind this whole skill: a problem in any of the three layers caps the other two. Hence the workflow order (diagnose → blockers → fundamentals → content → authority).

### 157. Corporate E-E-A-T — High
- **How:** an "About" page (real team, history, location), contact with several real channels, legal notice (106, 39), policies (privacy, cookies, returns and shipping if you sell), all linked from the footer of every page.

### 158. Performance under real traffic — Medium
- **How:** monitor RUM (real-user data): the CrUX report, Vercel Speed Insights, Cloudflare Web Analytics, or the `web-vitals` library sending metrics to your analytics. Review the 75th percentile per page template and device.

### 159. Traffic-drop protocol — High
- **How:** 1) is it real? (compare with analytics; rule out tracking or consent problems); 2) when did it start? (exact date in Search Console); 3) does it coincide with a deploy (check noindex, robots, canonicals, redirects, 5xx), a Google update (Search Status Dashboard) or seasonality?; 4) which pages, queries, countries and devices are dropping? (segment); 5) did AI Overviews or other features appear on those SERPs?; 6) any manual actions or security issues?; 7) act on the cause, not the symptoms.
- **Avoid:** rewriting the whole site in a panic during a core update (let it finish, then analyse).
- **See also:** the change-analysis order and alert design in `playbooks/measurement.md` (X14–X15), the change log in `playbooks/governance.md` (G11) and, after a migration, `playbooks/migrations.md` M17.

### 160. Migrations and redesigns without losing traffic — Critical
- **How:** before: full crawl of the old site, export of URLs with traffic and links, a 1:1 redirect map, a staging environment with `noindex`/password, checks of metadata and Schema on the new version. During: 301s live the same day, staging `noindex` removed, new sitemap submitted, Change of Address in Search Console if the domain changes. After: daily monitoring of 404s, indexing and traffic for 4–8 weeks; keep the old sitemap for a while to speed up redirect discovery.
- **Avoid:** changing domain, URL structure, design and content at once (if something fails, you won't know what).
- **Validate the map:** `scripts/seo_audit.py --redirect-map redirects.csv --fail-on critical` (single-hop 301/308, destination 200, no home catch-alls, retired pages 404/410); `scripts/search_data.py compare --map redirects.csv` compares old vs new URL performance.
- **Full playbook:** inventory sources, master URL file, mapping rules, Change of Address for **all** domain variants (Google, June 2026), hosting/CDN moves, template parity, go/no-go, stabilisation, monitoring old + new and rollback: `playbooks/migrations.md` (M1–M18).
