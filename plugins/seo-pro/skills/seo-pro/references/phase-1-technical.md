# Phase 1 — Launch, indexing and infrastructure (practices 1–40)

Goal: Google and every other search engine (including AI search) can **discover, crawl, render and index** every page that matters, quickly and unambiguously. Nothing in phases 2 and 3 works if this foundation fails.

"Phase done" criteria: Search Console verified with no critical errors, sitemap accepted, key pages indexed ("Page indexing" report), Core Web Vitals green or on track, clean HTTPS and redirects, and `scripts/seo_audit.py` reporting no critical findings.

Format: **Why** · **How** · **Expected result** · **Avoid** · **Verify**.

## Contents
- Indexing and initial setup: 1–5
- Technical SEO and performance: 6–16
- Site architecture and advanced indexing: 17–26
- Brand, security, legal, accessibility and measurement: 27–40

---

## Indexing and initial setup

### 1. Verify Google Search Console — Critical
- **Why:** it is the only source of truth on how Google sees your site (indexing, queries, errors, manual actions).
- **How:** create a **Domain** property (DNS TXT verification), not a URL-prefix property, so it covers http/https and every subdomain. Add team members with the least privilege they need.
- **Expected result:** property verified on day one; performance data within 24–48 h.
- **Avoid:** verifying only `https://www.` and forgetting the apex; removing the DNS record later (verification is lost).
- **Verify:** `dig TXT example.com +short` shows `google-site-verification=…`; the property is listed as a Domain property.

### 2. Submit an XML sitemap — Critical
- **Why:** speeds up discovery and tells Google which URLs you consider canonical and important.
- **How:** generate the sitemap automatically from the data source (never by hand). Include **only** canonical, indexable URLs that return 200. Use a real `<lastmod>` (date of the last significant content change). Max 50,000 URLs or 50 MB per file; beyond that, a sitemap index. Declare it in `robots.txt` (`Sitemap: https://example.com/sitemap.xml`) and submit it in Search Console.
- **Expected result:** "Success" status in Search Console and discovered URLs ≈ real page count.
- **Avoid:** URLs that are noindexed, redirected, 404, parameterised or non-canonical; `lastmod` set to "now" on every URL (Google stops trusting it); `<priority>` and `<changefreq>` (Google ignores them).
- **Verify:** the auditor downloads the sitemap and checks the status code of a sample of URLs.

### 3. Get new URLs discovered fast — High
- **Why:** you want new and updated pages found quickly.
- **How:** sitemap with accurate `lastmod` + an internal link from a frequently crawled page (home, category hubs) + "URL Inspection → Request indexing" in Search Console for the most important URLs (daily quota applies). For Bing, Yandex and others, IndexNow (5).
- **Expected result:** important pages discovered within hours or days.
- **Avoid:** tools that "force" indexing through the **Google Indexing API**: it is only permitted for pages with `JobPosting` or `BroadcastEvent` embedded in a `VideoObject`. Using it for anything else breaches its terms, can get access revoked, and doesn't guarantee indexing.
- **Verify:** URL Inspection → "URL is on Google".

### 4. Configure robots.txt — Critical
- **Why:** one misplaced `Disallow` can wipe a whole site from search results.
- **How:** at the host root (`/robots.txt`), status 200, `text/plain`. A reasonable minimum:
  ```
  User-agent: *
  Disallow: /api/
  Disallow: /admin/
  Disallow: /*?*sort=
  Sitemap: https://example.com/sitemap.xml
  ```
  Block only areas with no search value (APIs, dashboards, carts, infinite filter spaces). Decide separately what to do about AI crawlers (37).
- **Expected result:** Googlebot can reach everything indexable and every resource (CSS, JS, images) needed to render it.
- **Avoid:** a `Disallow: /` inherited from staging (the most expensive and most common launch mistake); blocking `/_next/`, `/static/`, CSS or JS; using robots.txt to "de-index" (a blocked URL can stay indexed without content; to remove it from Google use `noindex` and keep it crawlable). A robots.txt returning 5xx makes Google pause crawling the site.
- **Verify:** `curl -s https://example.com/robots.txt`; the robots.txt report in Search Console (Settings); the auditor flags blocked important paths.

### 5. IndexNow and Bing Webmaster Tools — High
- **Why:** Bing powers Copilot and part of the search behind other AI assistants; several engines accept IndexNow for instant change notifications.
- **How:** add the site to Bing Webmaster Tools (it can import from Search Console). Implement IndexNow: generate a key, publish it at `https://example.com/<key>.txt`, and `POST` new, updated or deleted URLs to `https://api.indexnow.org/indexnow` on deploy or on publish. Many CMSs and CDNs (e.g. Cloudflare) offer it built in.
- **Expected result:** indexing in Bing within hours; visibility in the products that depend on its index.
- **Avoid:** pinging unchanged URLs in a loop (ignored, and wastes quota).
- **Verify:** 200/202 response from the API; IndexNow report in Bing Webmaster Tools.
- **Bing layer:** verification options, streamed submissions, Copilot directives and AI Performance are in `engines/bing.md` (B1–B9).

---

## Technical SEO and performance

### 6. Core Web Vitals — High
- **Why:** they are part of the page-experience signals and, above all, they affect conversion and abandonment. They don't make up for worse content, but they break ties.
- **How:** targets at the 75th percentile of real users: **LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1** (INP replaced FID in March 2024). Main levers:
  - LCP: hero image served as AVIF/WebP, correctly sized, with `fetchpriority="high"`, **without** `loading="lazy"`, preloaded if the browser discovers it late; fast HTML (TTFB < 0.8 s) through caching/CDN and server rendering.
  - INP: less JavaScript on the main thread, break up long tasks, defer third-party scripts (chat, analytics, tags), don't hydrate components that aren't interactive.
  - CLS: see 14.
- **Expected result:** the Search Console "Core Web Vitals" report green on mobile and desktop.
- **Avoid:** optimising only the Lighthouse lab score while ignoring field data; chasing 100/100 while bigger problems remain.
- **Verify:** PageSpeed Insights (real-user section), Search Console, `npx lighthouse`. Field data takes ~28 days to reflect improvements.

### 7. Mobile-first — Critical
- **Why:** Google indexes every site with its smartphone crawler. Whatever isn't on the mobile version doesn't exist for Google.
- **How:** responsive design with the same content, links, structured data and metadata on mobile and desktop. `<meta name="viewport" content="width=device-width, initial-scale=1">`. Tap targets of at least 24×24 px (ideally 44–48 px) and text readable without zooming.
- **Expected result:** full content parity between mobile and desktop.
- **Avoid:** hiding content on mobile that exists on desktop; separate `m.` sites (maintenance burden and drift); disabling zoom (`user-scalable=no`).
- **Verify:** the auditor checks the viewport; Chrome DevTools device mode; compare `curl` with mobile and desktop user agents if rendering is adaptive.

### 8. HTTPS — Critical
- **Why:** a minor ranking signal, but browsers flag anything without it as "not secure", and there is no HTTP/2-3 or many modern APIs without it.
- **How:** valid certificate (Let's Encrypt or the host/CDN's) covering apex and `www`; 301 from `http://` to `https://` in **a single hop**; `Strict-Transport-Security: max-age=31536000; includeSubDomains` once everything works over HTTPS.
- **Expected result:** every variant (`http`, `https`, with and without `www`) reaches the canonical version in one hop.
- **Avoid:** mixed content (`http://` resources on `https://` pages); chains like `http://example → https://example → https://www.example`; enabling HSTS `preload` unless you're sure (hard to undo).
- **Verify:** the auditor tests the four variants and counts hops; `curl -sIL http://example.com`.

### 9. Eliminate internal 404s — High
- **Why:** 404s themselves don't hurt (they're normal), but **broken internal links** waste crawling and link equity and frustrate users; and old URLs with external links lose their value if they 404.
- **How:** fix internal links to point at valid URLs; for removed URLs that had traffic or external links, 301 to the closest equivalent; for those with no substitute, a clean 404 or 410. A helpful 404 page (search box and links to main sections) that returns **status 404**, not 200.
- **Expected result:** zero broken internal links; URLs with external links redirected.
- **Avoid:** redirecting every 404 to the home page (Google treats it as a soft 404); error pages that return 200.
- **Verify:** the auditor's `--crawl` lists broken links; Search Console Page indexing ("Not found (404)").

### 10. Host close to your users — Medium
- **Why:** server location is no longer a meaningful geotargeting signal for Google, but **latency** does affect TTFB and LCP.
- **How:** choose a hosting/serverless region close to your audience **and close to your database** (server-to-database latency often matters more than user-to-server). Combine with a CDN (11). Geotargeting is expressed through content language, hreflang, domain (ccTLD) and local data — not IP address.
- **Expected result:** TTFB < 0.8 s for your main audience.
- **Avoid:** switching hosts "for SEO" when the real problem is a slow database query.
- **Verify:** TTFB in PageSpeed Insights (field) and in the auditor (lab, from wherever it runs).

### 11. Use a CDN — High
- **Why:** serves HTML and assets from the nearest edge, absorbs traffic spikes, and usually brings HTTP/3, compression and protection.
- **How:** Cloudflare, Vercel, Netlify, Fastly, Bunny… Cache hashed assets aggressively (`Cache-Control: public, max-age=31536000, immutable`) and HTML with revalidation (`s-maxage` + `stale-while-revalidate`, or ISR in Next.js).
- **Expected result:** high cache-hit ratio; stable TTFB.
- **Avoid:** CDN bot protection that blocks or challenges Googlebot ("bot fight" modes, aggressive WAF rules) — check that Googlebot gets a 200, not a challenge; caching personalised or session-cookie pages.
- **Verify:** `cf-cache-status`, `x-vercel-cache`, `age` headers; Crawl stats in Search Console (responses by type).

### 12. Minify CSS and JavaScript — Medium
- **Why:** fewer bytes, less download and parse time.
- **How:** any modern bundler (Next.js, Vite, Astro) already minifies in production. The real win is **shipping less code**: drop heavy dependencies, split by route, load on demand (dynamic `import()`), Brotli or gzip compression on the server.
- **Expected result:** no significant "unminified" or "unused JavaScript" warnings in Lighthouse.
- **Avoid:** spending time on manual minification or plugins when the framework already does it.
- **Verify:** `content-encoding: br|gzip` headers (the auditor checks this); DevTools Coverage panel.

### 13. Lazy loading done right — High
- **Why:** deferring what's off-screen speeds up the initial load; applying it to what's on-screen slows it down.
- **How:** `loading="lazy"` on images and `iframe`s (maps, videos) **below the first viewport**; for YouTube, a facade (thumbnail that loads the player on click). Always with `width` and `height`.
- **Expected result:** fewer initial bytes without hurting LCP.
- **Avoid:** `loading="lazy"` on the hero image or top logo (delays LCP); JavaScript lazy-loading that swaps `src` and leaves Google without an image URL (use the native attribute).
- **Verify:** the auditor warns if the document's first image is lazy; Lighthouse "Largest Contentful Paint image was lazily loaded".

### 14. Minimise CLS — High
- **Why:** layout shifts annoy users, cause mis-clicks, and are one of the three Core Web Vitals.
- **How:** `width`/`height` or `aspect-ratio` on images, videos, iframes and ads; reserve space for banners (cookies, notices) or show them as fixed overlays that don't push content; font fallbacks with `size-adjust`/metric overrides (`next/font` does this) and `font-display: swap` or `optional`; never insert content above what's already painted unless in response to a user action.
- **Expected result:** CLS ≤ 0.1 in field data.
- **Avoid:** a cookie banner that pushes the page down when it appears (a very common cause in Europe).
- **Verify:** the auditor counts images without dimensions; DevTools → Performance → Layout shifts.

### 15. Remove render-blocking resources — Medium
- **Why:** synchronous CSS and scripts in `<head>` delay first paint.
- **How:** scripts with `defer` (or `async` if independent) or `type="module"`; critical CSS inlined or small, the rest deferred; third parties (analytics, chat, pixels) loaded after interaction or in `requestIdleCallback`; `preconnect` only for the 1–2 critical origins.
- **Expected result:** fast FCP; no "Eliminate render-blocking resources" warnings.
- **Avoid:** loading tag managers with dozens of tags synchronously.
- **Verify:** the auditor lists `<script src>` in `<head>` without `async`/`defer`/`module`.

### 16. Optimised web fonts — Medium
- **Why:** web fonts delay text and cause CLS.
- **How:** self-host fonts (saves a connection and, in the EU, avoids sending visitor IPs to third parties), WOFF2, only the subsets and weights you use, a variable font if you use 3+ weights, `preload` for the main one, `font-display: swap`. In Next.js, `next/font` does all of this.
- **Expected result:** text visible immediately with no shift when the font swaps.
- **Avoid:** loading Google Fonts from Google's CDN without consent in the EU (German courts have fined sites for it); loading 8 weights "just in case".
- **Verify:** Network panel (number and size of fonts); Lighthouse.

---

## Site architecture and advanced indexing

### 17. Click depth — High
- **Why:** the closer a page is to the home page, the more crawling and internal link equity it receives.
- **How:** important pages ≤ 3 clicks from home (a guideline, not a law). Tools: main menu with categories, hubs/pillar pages, contextual links, breadcrumbs, linked pagination. No indexable page should be **orphaned** (no internal links pointing to it).
- **Expected result:** depth distribution concentrated at 1–3.
- **Avoid:** cramming hundreds of links into the menu to "flatten" (dilutes and hurts UX).
- **Verify:** the auditor's `--crawl` reports each URL's depth and detects sitemap URLs not reachable via links.

### 18. Canonical tags — Critical
- **Why:** consolidate signals from duplicate or near-duplicate URLs into one.
- **How:** `<link rel="canonical" href="absolute-URL">` on **every** indexable page, self-referencing unless it's a duplicate. Absolute URL with the canonical protocol and host, no tracking parameters. Consistent with the sitemap, internal links and redirects.
- **Expected result:** "Google-selected canonical" = "User-declared canonical" in URL Inspection.
- **Avoid:** canonicalising every page to the home page; relative or `http://` canonicals; canonicalising page 2 of a paginated series to page 1 (each paginated page is its own canonical); combining `noindex` with a canonical to another URL (contradictory signals). Remember it is a **hint**, not a directive.
- **Verify:** the auditor checks presence, absoluteness and whether it points elsewhere.

### 19. Breadcrumbs — Medium
- **Why:** orient users, reinforce internal linking, and Google may show them in the result.
- **How:** visible navigation (`<nav aria-label="Breadcrumb">` with an `<ol>`) + `BreadcrumbList` JSON-LD with the same items. They reflect hierarchy, not browsing history.
- **Expected result:** the Search Console "Breadcrumbs" report with no errors.
- **Avoid:** breadcrumb Schema that doesn't match what's visible.
- **Verify:** the auditor detects `BreadcrumbList`; Rich Results Test.

### 20. Control parameters and facets — High
- **Why:** filters, sorting and internal search generate near-infinite URL combinations that consume crawling and create duplicates.
- **How:** decide per parameter type: (a) **parameters that create pages with their own demand** (e.g. "women's running shoes") → turn them into clean, indexable, linked URLs; (b) **parameters that only sort or filter with no demand** → don't generate crawlable links to them (use buttons/forms or `#` fragments), canonical to the clean version, and if Google still crawls them in bulk, a targeted `Disallow` in robots.txt; (c) tracking parameters (`utm_*`, `gclid`) → canonical without them. Search Console's URL Parameters tool no longer exists (removed in 2022).
- **Expected result:** crawling concentrated on useful URLs (Crawl stats).
- **Avoid:** blocking in robots.txt URLs that already carry a canonical — if Google can't crawl them it never sees the canonical; blocking parameters that do create valuable pages.
- **Verify:** Crawl stats and Page indexing → "Duplicate…"; log analysis (124).

### 21. X-Robots-Tag — Medium
- **Why:** it's the only way to `noindex` non-HTML files (PDFs, images, feeds).
- **How:** HTTP header `X-Robots-Tag: noindex` on paths you don't want indexed (e.g. `/invoices/*.pdf`). Also useful for whole staging environments: `X-Robots-Tag: noindex, nofollow` on the whole pre-production host (better still, password-protect it).
- **Expected result:** those files out of the index.
- **Avoid:** the staging header leaking to production (check on every deploy).
- **Verify:** `curl -sI URL | grep -i x-robots-tag`; the auditor reports it.

### 22. Clean pagination — Medium
- **Why:** Google needs crawlable `<a href>` links to discover items on deep pages.
- **How:** dedicated pagination URLs (`/blog?page=2` or `/blog/page/2`), linked with `<a href>`, each with a self-referencing canonical and a differentiated title ("… – Page 2"). If you use infinite scroll or "load more", those URLs must also exist and be linked. Google no longer uses `rel="next/prev"` (harmless to keep).
- **Expected result:** every listed item discovered and indexable.
- **Avoid:** pagination via JavaScript buttons with no URL; `noindex` on pages 2+ (over time Google stops following their links).
- **Verify:** disable JavaScript and check you can reach the last page.

### 23. Correct redirects — High
- **Why:** they preserve the old URL's signals and prevent losses during migrations.
- **How:** 301 or 308 for permanent moves (302/307 for temporary; Google eventually treats a long-lived 302 as permanent, but don't rely on it). Destination equivalent in content. A single hop. Keep redirects for at least a year (indefinitely if the URL had links).
- **Expected result:** no chains longer than one hop, no loops.
- **Avoid:** JavaScript or `meta refresh` redirects as the main mechanism; redirecting everything to the home page in a migration.
- **Verify:** the auditor follows the chain and counts hops.

### 24. Link internally to final URLs — Medium
- **Why:** every internal link that goes through a redirect adds needless latency and complexity.
- **How:** after any URL change, update internal links, menus, sitemap and canonicals to the final destination. Always link to the canonical variant (trailing slash or not, `www` or not).
- **Expected result:** zero internal links returning 3xx.
- **Avoid:** letting the redirect layer "take care of it".
- **Verify:** the auditor's `--crawl` lists internal links that redirect.

### 25. Content and links visible without JavaScript — Critical
- **Why:** Google renders JavaScript, but deferred and with limits; most AI crawlers (GPTBot, ClaudeBot, PerplexityBot…) and many preview tools **don't execute JavaScript**. Whatever isn't in the initial HTML is fragile.
- **How:** server-side or static rendering for every indexable page (see 127). Links as `<a href="/path">`, never `div`s or `onClick` with `router.push` as the only mechanism. Title, meta, canonical and JSON-LD in the served HTML.
- **Expected result:** `curl -s URL` contains the main content, the H1, navigation links and metadata.
- **Avoid:** SPAs that return an empty `<div id="root"></div>`; main content fetched client-side.
- **Verify:** the auditor measures words of text in the un-rendered HTML and warns when very low; URL Inspection → "View crawled page".

### 26. Manage low-value pages — High
- **Why:** thousands of thin pages (internal search results, tags with one post, empty profiles, filters with no results) dilute the site's perceived quality and waste crawling.
- **How:** `noindex` on internal search results (Google explicitly asks for this); merge or `noindex` thin taxonomies; return a real 404 for empty listings or non-existent items (not a 200 saying "no results" → *soft 404*).
- **Expected result:** an index made of pages that deserve to rank.
- **Avoid:** mass `noindex` without first checking in Search Console which pages bring traffic.
- **Verify:** Page indexing → "Soft 404" and "Crawled – currently not indexed" trending down.

---

## Brand, security, legal, accessibility and measurement

### 27. Social and brand profiles — Medium
- **Why:** they're not links that pass authority (usually nofollow), but they help search engines and AIs recognise your brand as an **entity**, and they bring traffic and mentions.
- **How:** claim the same handle on the networks your audience actually uses (not all of them), with identical name, logo, description and link. Link them from the site and list them in `sameAs` in the `Organization` Schema (38).
- **Expected result:** brand searches dominated by your own properties.
- **Avoid:** abandoned profiles (worse than none).
- **Verify:** search the brand on Google and in an AI assistant.

### 28. Google Business Profile — Critical for local businesses
- **Why:** it determines visibility in the map pack and "near me" searches.
- **How:** only if you serve customers in person (physical location or service area). Precise primary category, NAP (name, address, phone) identical to the site and directories, hours, real photos, services/products, replies to every review. Link to the matching location page, not always the home page. On the site: `LocalBusiness` Schema with the same data.
- **Expected result:** verified, complete profile; appearance in the local pack for brand and category searches in the area.
- **Avoid:** keywords in the business name (against guidelines, triggers suspensions); virtual addresses; bought or incentivised reviews.
- **Verify:** verified status; profile performance metrics.

### 29. Content Security Policy — Medium
- **Why:** not a ranking signal, but a hacked site (injected spam, malicious redirects) destroys SEO: Google security warnings, de-indexing and manual actions. CSP limits the damage of XSS injections.
- **How:** start with `Content-Security-Policy-Report-Only` to see what would break, then enforce. Use nonces or hashes instead of `'unsafe-inline'` where the framework allows.
- **Expected result:** CSP enforced without breaking analytics, fonts or payments.
- **Avoid:** copying a generic policy that blocks your own JavaScript and leaves the page blank for users (and for Google).
- **Verify:** no violations in the browser console; the auditor detects the header.

### 30. Security headers — Medium
- **Why:** same reason as 29: they protect against attacks that end up as SEO and trust problems.
- **How:** `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy` (disable what you don't use) and clickjacking protection via `Content-Security-Policy: frame-ancestors 'self'` (or `X-Frame-Options: SAMEORIGIN` for older browsers).
- **Expected result:** a good grade on securityheaders.com.
- **Avoid:** `Referrer-Policy: no-referrer` if you want other sites to see referral traffic from you (and vice versa).
- **Verify:** the auditor lists present and missing headers.

### 31. Spam-protected forms — Medium
- **Why:** prevents injections, fake sign-ups, and spam profile or comment pages ending up indexed.
- **How:** Cloudflare Turnstile, hCaptcha or reCAPTCHA v3 + honeypot field + server-side rate limiting + server-side validation and sanitisation. If user content is published, moderation and `rel="ugc nofollow"` on its links (132).
- **Expected result:** no spam in the database and no junk pages indexed.
- **Avoid:** relying on browser validation alone; visible CAPTCHAs that tank conversion.
- **Verify:** submission logs; a `site:example.com` search with typical spam terms (casino, pills…).

### 32. Monitor malware and phishing blocklists — Medium
- **Why:** if Google Safe Browsing flags the domain, Chrome shows a red warning screen and traffic drops to zero.
- **How:** Search Console's "Security issues" report emails you; complement with Safe Browsing status (transparencyreport.google.com/safe-browsing/search) and email reputation lists if you send mail from the domain. Keep CMS, plugins and dependencies updated (`npm audit`).
- **Expected result:** "No issues detected".
- **Avoid:** nulled or abandoned plugins and themes.
- **Verify:** monthly review (can be automated, 120).

### 33. Clear, versioned privacy policies — Medium
- **Why:** they are a **legal obligation** (GDPR in the EU, UK GDPR, state privacy laws in the US) and a trust signal for users and quality raters. They don't directly affect rankings.
- **How:** privacy policy, cookie policy and legal notice reachable from the footer of every page, with a "last updated" date and a version history. See 39.
- **Expected result:** legal compliance and trust.
- **Avoid:** generic templates that don't describe what your site actually does.
- **Verify:** links present in the footer of every template.

### 34. A proper favicon — Medium
- **Why:** Google shows it next to your result on mobile and desktop; a recognisable icon improves CTR.
- **How:** `<link rel="icon" href="/favicon.svg">` (or PNG/ICO), square, **a multiple of 48×48 px**, at a stable crawlable URL; one per host; plus a 180×180 `apple-touch-icon`. It must represent the brand and follow Google's policies (nothing offensive or misleading).
- **Expected result:** your favicon in search results (can take weeks).
- **Avoid:** blocking the favicon in robots.txt; changing its URL constantly.
- **Verify:** the auditor detects `link rel="icon"`.

### 35. Accessibility — High
- **Why:** many accessibility practices overlap with SEO (semantic structure, alt text, descriptive links), and since June 2025 the **European Accessibility Act** applies to many e-commerce and digital services sold in the EU.
- **How:** semantic HTML (`header`, `nav`, `main`, `footer`, headings in order), WCAG AA contrast (4.5:1 for body text), `alt` on informative images (`alt=""` on decorative ones), `<label>`s on form fields, descriptive link text, `lang` on `<html>`.
- **Expected result:** Lighthouse Accessibility ≥ 90 and no serious axe errors.
- **Avoid:** automatic accessibility "overlays" (they don't fix the problem and sometimes worsen it).
- **Verify:** the auditor checks `lang`, `alt` and heading order; `npx @axe-core/cli URL`.

### 36. Keyboard navigation — Medium
- **Why:** an accessibility requirement (WCAG) and a sign of an implementation built on semantic elements (which are also what Google understands).
- **How:** every interactive element is an `<a>`, `<button>` or native field; visible focus (`:focus-visible`); a "Skip to content" link; menus and modals operable with the keyboard and `Esc`; logical tab order.
- **Expected result:** the main journey (browse, search, buy or contact) can be completed with the keyboard only.
- **Avoid:** `outline: none` with no alternative; clickable `div`s.
- **Verify:** manual test with Tab/Shift+Tab/Enter/Esc.

### 37. Make a deliberate decision about AI crawlers — High
- **Why:** AI search engines cite the sources they can read. Blocking them protects your content from reuse, but makes you invisible in their answers.
- **How:** distinguish **search/citation** crawlers (`OAI-SearchBot`, `ChatGPT-User`, `PerplexityBot`, `Claude-SearchBot`/`Claude-User`) from **training** crawlers (`GPTBot`, `ClaudeBot`, `CCBot`). `Google-Extended` controls use for training Google's models but does **not** affect AI Overviews or AI Mode, which use Googlebot. For most businesses that want visibility: allow search crawlers and decide with the owner about training crawlers. Example:
  ```
  User-agent: GPTBot
  Disallow: /
  User-agent: OAI-SearchBot
  Allow: /
  ```
  `llms.txt` is a proposal with no confirmed adoption by the major search engines; cheap to add, but not a ranking lever.
- **Expected result:** an explicit, documented decision — not an accidental block inherited from the CDN (some block "AI bots" by default).
- **Avoid:** showing AI crawlers different content from what users see: that is *cloaking*, and since May 2026 Google treats it as spam in its AI features too.
- **Verify:** the auditor lists which AI agents robots.txt allows or blocks; review the CDN's bot settings.
- **Bing layer:** in Bing, `noarchive` removes content from Copilot answers and `nocache` limits citations to URL, title and snippet — see `engines/bing.md` B8.

### 38. Core entity structured data — High
- **Why:** helps Google and AIs identify who is behind the site (name, logo, profiles, contact) and display the site name and logo correctly.
- **How:** on the home page, `Organization` (or `LocalBusiness`/subtype) JSON-LD with `name`, `url`, `logo` (≥ 112×112 px, crawlable URL), `sameAs` (official profiles), `contactPoint`, and where relevant `legalName`, `vatID`, `address`. Plus `WebSite` with `name` and `alternateName` to control the site name in results. A stable `@id` (`https://example.com/#organization`) to reference it from `Article.publisher`, etc.
- **Expected result:** correct site name and logo on Google; no errors in the Rich Results Test.
- **Avoid:** data that doesn't match what's visible (address, phone); `sameAs` pointing to third-party profiles.
- **Verify:** the auditor extracts and validates the JSON-LD; Rich Results Test.

### 39. Legal compliance without hurting SEO — High
- **Why:** many jurisdictions require the site owner to be identified (e.g. Spain's LSSI, Germany's *Impressum*), and GDPR and national data-protection authorities regulate cookie consent. A badly implemented cookie banner is also a frequent cause of poor CLS and INP.
- **How:** a legal notice with legal name, company/tax ID, registered address, company registry details and contact; privacy and cookie policies; a banner with a "Reject" button as prominent as "Accept", and no non-essential cookies before consent. Make the banner an overlay (it must not push content), lightweight, and loaded without blocking rendering.
- **Expected result:** compliance and trust signals (157) without hurting Core Web Vitals.
- **Avoid:** banners that cover all content on mobile (legally required notices are allowed, but keep them unobtrusive).
- **Verify:** CLS and INP with and without the banner; legal notice review.

### 40. Measurement baseline — Critical
- **Why:** without a "before", you can neither prove nor learn anything from the "after".
- **How:** Search Console (queries, pages, countries, devices; it keeps only 16 months, see 118); analytics (GA4 with **Consent Mode v2** in the EEA, or a cookieless alternative such as Plausible, Umami or Matomo) with defined conversions; an annotation with the date of every significant SEO change. Export the starting point (clicks, impressions, CTR, average position, indexed pages, CWV).
- **Expected result:** a document or dashboard with the baseline and measurable conversions.
- **Avoid:** measuring only "traffic" without conversions; changing many things at once without recording when.
- **Verify:** conversion events visible in analytics; Search Console data flowing.
