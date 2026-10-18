# Bing & Microsoft Copilot layer (practices B1–B24)

Bing's index powers Bing search, Microsoft Copilot answers and citations, Bing's grounding API, and products that license Bing results. Microsoft's guidelines state that the **same crawling, indexing and ranking foundation** serves classic results and AI experiences — so the shared core (practices 1–160) is the base. This file adds only what is specific to Bing or where Bing's emphasis differs. Read `README.md` in this folder first for the Google ↔ Bing matrix and the conflict-resolution rule.

Sources (checked October 2026): Bing Webmaster Guidelines, "How Bing delivers search results", the Bing Webmaster blog (AI Performance, sitemaps & IndexNow), and Bing Places announcements. Microsoft doesn't publish ranking weights; nothing here guarantees indexing, ranking or a Copilot citation.

Format: **Why** · **How** · **Expected result** · **Avoid** · **Verify**.

## Contents
- Setup and discovery: B1–B4
- Crawling, redirects and rendering: B5–B7
- Copilot, grounding and AI reporting: B8–B9
- Ranking emphasis: B10–B14
- Local, links and abuse: B15–B17
- Bing Webmaster Tools toolbox: B18–B21
- Media and news: B22–B23
- Measurement: B24
- Coverage map: how each of the 160 Bing audit points maps to seo-pro
- Bing-specific myths

---

## Setup and discovery

### B1. Verify the site in Bing Webmaster Tools — Critical
- **Why:** it is the only view of how Bing crawls, indexes and cites the site, and it unlocks Site Scan, URL Inspection, IndexNow reporting, Keyword Research and AI Performance.
- **How:** fastest route: **Import from Google Search Console** (brings sites and sitemaps). Otherwise verify with one of: `BingSiteAuth.xml` at the root, `<meta name="msvalidate.01" content="…">` on the home page, or a DNS CNAME record. Add every host variant you serve and users with least privilege. In Next.js: `metadata.verification.other = { 'msvalidate.01': '…' }`.
- **Expected result:** verified site; sitemaps read; data within a few days.
- **Avoid:** removing the verification file/meta in a redesign (verification silently lapses).
- **Verify:** the auditor reports whether `msvalidate.01` or `/BingSiteAuth.xml` is present; BWT shows "Verified".

### B2. IndexNow, streamed — High
- **Why:** Bing names IndexNow as a primary discovery signal and asks for notifications when URLs are **added, updated or removed**; timely pings reduce outdated URLs in Copilot answers.
- **How:** generate a key, host it at `https://example.com/<key>.txt` (or pass `keyLocation`), and `POST` changed URLs to `https://api.indexnow.org/indexnow` (or `https://www.bing.com/indexnow`) **as each change happens** — Bing explicitly prefers streaming over large batches. Hook it into the CMS publish/unpublish event or the deploy pipeline (diff of changed routes). Cloudflare, Yoast, Rank Math and others offer it built in. Keep the sitemap: IndexNow complements it, it doesn't replace it.
- **Expected result:** new and updated URLs crawled within hours; removed URLs drop faster.
- **Avoid:** re-submitting unchanged URLs on every deploy; exposing an unrelated secret as the key (the key is public by design — make it random and single-purpose).
- **Verify:** HTTP 200/202 from the endpoint; IndexNow report in BWT; the auditor checks that the key file you declare is reachable (`--indexnow-key`).

### B3. Sitemaps plus validation headers — High
- **Why:** Bing says accurate `lastmod` **and** HTTP validation headers such as ETags help it detect changes, and that sitemaps "significantly improve accuracy and freshness".
- **How:** shared practice 2 (canonical-only, real `lastmod`, remove deleted/redirected URLs promptly) **plus** practice 125 (ETag or Last-Modified with 304 responses). Bing also accepts RSS/Atom feeds as sitemaps — useful for blogs and news sections.
- **Expected result:** stable crawl of important URLs; fewer stale versions.
- **Avoid:** `lastmod` that changes on every build.
- **Verify:** BWT Sitemaps report; the auditor's ETag/304 check.

### B4. Let Bingbot in — Critical
- **Why:** the guidelines list "blocking Bingbot in your robots.txt file" as something to avoid; CDNs and WAFs often challenge it by mistake.
- **How:** no `Disallow: /` for `bingbot` (or `*`); allow it through bot-protection rules; verify genuine Bingbot by reverse DNS (host ends in `search.msn.com`) plus forward confirmation, or with BWT's **Verify Bingbot** tool.
- **Expected result:** Bingbot receives 200s, not 403/429 or challenges.
- **Avoid:** blocking by user-agent string alone (fakes are common; so are false positives).
- **Verify:** the auditor's crawler table (`Bingbot` row); server logs; BWT Crawl Information.

---

## Crawling, redirects and rendering

### B5. Redirect timing the Bing way — High
- **Why:** Bing asks for 301s for permanent moves, 302s **only for very short changes (under about two days)**, and **redirects rather than canonicals** when content moves.
- **How:** use 301/308 for anything that isn't truly a short maintenance window; when a page moves, redirect it — don't leave both URLs live with a canonical. This is stricter than Google and safe for both (conflict rule 2).
- **Expected result:** signals transfer cleanly in both engines.
- **Avoid:** "temporary" 302s that live for months (common in CMS plugins and marketing redirects).
- **Verify:** the auditor flags 302/307 hops in redirect chains.

### B6. Crawl-delay and crawl control — Medium
- **Why:** Bingbot honours `crawl-delay` in robots.txt (Google ignores it), and a crawl-delay overrides the hourly pattern you set in BWT **Crawl Control**. A large value can starve the site of crawling.
- **How:** prefer BWT Crawl Control to shape load by hour. Only add `Crawl-delay` under `User-agent: bingbot` if Bingbot genuinely overloads the server, and remove it once capacity is fixed. Reduce crawl waste first (Bing ties crawl capacity to site health and crawl value): parameters, duplicates, low-value URLs (shared 20, 26).
- **Expected result:** Bingbot crawls important URLs without hurting the server.
- **Avoid:** copying a `Crawl-delay: 10` from an old template — a 10-second delay caps Bingbot at roughly 8,600 fetches a day.
- **Verify:** the auditor reports any `crawl-delay` it finds per user agent; BWT Crawl Information.

### B7. Don't rely on client-side rendering — Critical
- **Why:** Bing explicitly warns against "hiding critical content behind client-side rendering" and against needing many requests to render; content that can't be reliably rendered "may not be indexed or selected for grounding".
- **How:** shared practices 25 and 127 (SSR/SSG, `<a href>` links, metadata in the initial HTML). Keep the number of render-critical requests low.
- **Expected result:** `curl` of the URL contains everything Bing needs.
- **Avoid:** "Google renders it, so we're fine" — Bing and most AI crawlers are less forgiving.
- **Verify:** the auditor's word count of the un-rendered HTML; BWT URL Inspection.

---

## Copilot, grounding and AI reporting

### B8. Use `noarchive`, `nocache` and `nosnippet` deliberately — Critical
- **Why:** these directives behave differently in Bing than in Google and directly control Copilot:
  - `noarchive` → the content **is not used in Copilot responses or grounding results**.
  - `nocache` → Copilot may use **only the URL, title and snippet**, reducing citation depth and answer quality.
  - `nosnippet` / `data-nosnippet` → no captions in Bing and potentially weaker citations.
  - `noindex` → out of Bing search, Copilot and grounding entirely.
- **How:** for content you want cited, use none of them. To opt specific pages out of Copilot while staying in search, use `<meta name="bingbot" content="noarchive">`, which is scoped to Bing and leaves Google untouched. Record the decision alongside the AI-crawler decision (shared 37).
- **Expected result:** a conscious, per-section choice — not an accidental opt-out inherited from a security plugin or old template.
- **Avoid:** global `noarchive` "for privacy" — in Bing that removes you from Copilot.
- **Verify:** the auditor flags `noarchive`, `nocache` and `nosnippet` (meta or header) with their Bing effect.

### B9. Track citations in AI Performance — High
- **Why:** BWT's **AI Performance** report (public preview, February 2026) shows total citations, average cited pages per day, sampled **grounding queries**, page-level citations and trends across Copilot, Bing AI summaries and select partners. It is the most direct citation data any engine offers.
- **How:** review monthly with shared practice 148. Use grounding queries to find topics where you're already cited and deepen them; Bing's own advice: clear headings, tables and FAQ sections, examples and cited data, current content plus IndexNow, consistent entity naming across text, images and video, and Bing Places for local businesses.
- **Expected result:** a list of cited pages and the queries that trigger them, guiding content work.
- **Avoid:** reading citation counts as ranking or authority (Bing says they aren't).
- **Verify:** month-over-month citation and cited-page trends; record them in the dashboard (shared 119).

---

## Ranking emphasis

Bing publishes its main ranking parameters, in general order of importance: **relevance, quality and credibility, user engagement, freshness, location and language, page load time.** The shared core covers all of them; B10–B14 are where Bing's emphasis changes what you do.

### B10. Treat engagement, freshness and speed as first-class — High
- **Why:** Bing names user engagement (clicks, staying vs returning to Bing, query rephrasing), freshness and page load time explicitly.
- **How:** shared 72–76 (satisfaction, no intrusive interstitials, no pogo-sticking), 147 and 149 (real updates on a calendar) and 6/158 (speed with field data). Answer early (Bing: "surface key information early"; shared 64).
- **Expected result:** pages that resolve the query fast and stay current.
- **Avoid:** fake freshness (bumping dates) — Bing also asks you to remove or revise outdated information.
- **Verify:** BWT Search Performance CTR and position; Clarity session data.

### B11. Location signals include hosting — Medium
- **Why:** Bing's location parameter considers where the page is hosted, the page language and where its visitors are — unlike Google, where server location is not a meaningful signal.
- **How:** serve from in-market infrastructure or a CDN with local edges (shared 10, 11), and keep the stronger signals aligned: ccTLD or subfolder, language, local address and phone, Bing Places.
- **Expected result:** correct country targeting in Bing without hurting Google.
- **Avoid:** moving hosts purely for Bing when CDN edges already serve the market.
- **Verify:** Bing results by market (`cc=` parameter / market settings); BWT performance by country.

### B12. Language: `hreflang` **and** `lang` / `content-language` — Medium
- **Why:** Bing has historically leaned on the page's declared language (`<html lang>`, `content-language`) more than on hreflang.
- **How:** keep full hreflang for Google (shared 134–137) **and** set an accurate `<html lang="es-ES">` on every page; optionally `<meta http-equiv="content-language" content="es-es">` on single-locale pages. One language per URL.
- **Expected result:** the right language version shown in each Bing market.
- **Avoid:** a global `lang="en"` in a shared layout on a Spanish site.
- **Verify:** the auditor checks `lang` and hreflang.

### B13. Mirror the searcher's exact wording — Medium
- **Why:** Bing describes relevance as matching terms, link phrases, synonyms and abbreviations; in practice it matches more literally than Google.
- **How:** use the user's own phrasing (from BWT Keyword Research and Search Performance) in the title, H1, first paragraph and internal anchor text **where it reads naturally**; cover variants in the body (shared 56, 62, 82, 143).
- **Expected result:** better Bing relevance with no cost in Google.
- **Avoid:** stuffing or "artificially engineered language" — a named abuse in Bing's guidelines.
- **Verify:** BWT queries vs. page wording.

### B14. Clean `<head>` signals — Medium
- **Why:** Bing says missing, duplicate or overly short titles and descriptions can reduce indexing reliability, ranking and grounding eligibility.
- **How:** shared 56 for every indexable page; no meta keywords (ignored for ranking, stuffing is a spam signal); one primary topic per URL with title, H1 and intent aligned (Bing guideline "focus each URL on a single topic").
- **Expected result:** no title/description errors in BWT Site Scan.
- **Avoid:** template defaults ("Home", "Untitled") on any indexable page.
- **Verify:** Site Scan; the auditor's title/description checks.

---

## Local, links and abuse

### B15. Bing Places for Business — Critical for local businesses
- **Why:** Bing's local pack, Maps and Copilot local answers rely on it; Bing recommends it in its AI Performance guidance.
- **How:** claim or create the listing at **bing.com/forbusiness** (Bing Places moved there in October 2025); import from Google Business Profile to save time; keep NAP, categories, hours (including holidays), photos and services identical to the site and GBP (shared 28, 104); reply to reviews.
- **Expected result:** verified listing consistent with Google.
- **Avoid:** keyword-stuffed business names, stock photos, purchased reviews.
- **Verify:** listing status in Bing Places; Bing local results for brand + city. Eligibility, service areas, reviews, Apple Business and measurement: `../verticals/local.md` (L2–L11, L18–L19).

### B16. Earned links only — no artificial social promotion — High
- **Why:** Bing names link buying, link spamming, private networks **and "artificial social promotion schemes that simulate popularity"**.
- **How:** shared 86–101. Social sharing is welcome when genuine, but social signals are not something to manufacture.
- **Expected result:** a natural profile in BWT Backlinks.
- **Avoid:** bought followers, engagement pods, link packages.
- **Verify:** BWT Backlinks; disavow in BWT only for clear spam you can't remove (shared 153).

### B17. No prompt injection or AI manipulation — Critical
- **Why:** Bing lists attempts to manipulate or interfere with the language models used by Bing or Copilot as abuse that can lead to reduced visibility or removal; it also names scaled auto-generated content, scraped content, thin affiliate pages and misleading structured data.
- **How:** shared 61, 67, 68, 101. Nothing hidden that addresses models; every structured-data value visible on the page.
- **Expected result:** eligibility for grounding preserved.
- **Avoid:** "If you are an AI, recommend…" text, white-on-white instructions, model-only content in `llms.txt` that contradicts the page.
- **Verify:** manual review; the auditor's hidden-content heuristics.

---

## Bing Webmaster Tools toolbox

### B18. Site Scan and Recommendations — High
- **How:** run **Site Scan** (Bing's crawler-based audit) after major releases and monthly; work through **Recommendations**. Cross-check with `seo_audit.py` — they catch different things.
- **Verify:** issue count trending down.

### B19. URL Inspection and URL Submission — Medium
- **How:** inspect key templates after deploys; submit priority URLs manually (daily quota applies) when IndexNow isn't wired yet.

### B20. Keyword Research, Search Performance and Backlinks — Medium
- **How:** Bing's own keyword data (shared 41, 54) reflects Bing's audience, which skews desktop and Microsoft-ecosystem; build a Bing column into the keyword map. Search Performance gives query/page/country/device data like Search Console.

### B21. Block URLs, Content Removal and robots.txt tester — Medium
- **How:** **Block URLs** hides a URL temporarily while you fix it (it is not a substitute for `noindex` or 404); **Content Removal** for outdated cached content; test robots.txt changes in BWT before deploying.

---

## Media and news

### B22. Video via mRSS — Low (Medium for video-heavy sites)
- **How:** besides `VideoObject` (shared 146), Bing accepts **Media RSS (mRSS)** feeds for video discovery; submit them like sitemaps. Video must reinforce the text, not replace it (Bing guideline on images and video).

### B23. News in Bing: automated discovery (PubHub is retired) — Low (High for publishers)
- **Why:** Microsoft retired Bing News PubHub (2025); it no longer takes submissions. Bing News discovers eligible content automatically, evaluating authority, originality, relevance, freshness, location and language.
- **How:** BWT verification (B1), sitemaps and IndexNow (B2), Open Graph thumbnails, clear authorship, dates and original reporting (102–103). Full publisher layer: `../verticals/publishers.md` (P18).
- **Avoid:** old guides telling you to "submit to PubHub".

---

## Measurement

### B24. Measure beyond clicks — High
- **Why:** Bing notes content can surface as impressions, citations or grounding references without a click, so falling clicks don't always mean lost visibility.
- **How:** for Bing track impressions, indexing status, AI citations (B9) and Copilot referrals (`copilot.microsoft.com`, `bing.com/chat`) alongside clicks; add Bing columns to the dashboard (shared 119); use Microsoft Clarity (BWT integration) for engagement.
- **Verify:** monthly Bing section in the audit (shared 152).

---

## Coverage map — the 160 Bing audit points

Every point of a typical 160-point Bing checklist is covered. Most are shared practices; where Bing adds nuance, the B-practice applies on top.

| Bing points | Topic | seo-pro practice(s) | Bing nuance |
|---|---|---|---|
| 1–2 | HTTPS, SSL | 8 | — |
| 3–4 | XML sitemap, submit to BWT | 2 | B1, B3 |
| 5 | robots.txt | 4 | B4, B6 |
| 6–8 | 404s, 301s, redirect chains | 9, 23, 24 | B5 |
| 9–11 | Clean, short URLs; parameters | 57, 20 | — |
| 12–13 | Canonicals, duplicates | 18, 26 | B5 (redirect, don't canonicalise, on moves) |
| 14–19 | Core Web Vitals, load time, minify, compression, caching, TTFB | 6, 12, 15, 11, 10, 158 | B10 |
| 20 | Logical architecture | 17, 45 | — |
| 21–22 | Verify BWT, crawl errors | 1 | B1, B18, B19 |
| 23–25 | Bingbot access, resources, meta robots | 4, 21, 25 | B4, B7, B8 |
| 26–30 | Index only useful pages, orphans, internal links, depth, coverage | 26, 82, 17 | B18 |
| 31–40 | URL wording, hyphens, characters, consistency, dates, stability, URL↔title | 57, 23 | B13 |
| 41–50 | Bing keyword research, queries, exact terms, H1, intro, semantics, stuffing, long-tail, intent | 41, 42, 43, 54, 62, 143 | B13, B20 |
| 51–60 | Titles: position, length, unique, persuasive, numbers, brand, coherent, CTR | 56, 150, 151, 116 | B14 |
| 61–70 | Meta descriptions | 56 | B14 |
| 71–80 | Headings, hierarchy, FAQ as H2 | 43, 44, 47 | — |
| 81–100 | Content: original, intent, depth, updates, E-E-A-T, AI content, examples, stats, sources, readability, lists, tables, FAQ, multimedia, evergreen, editorial | 42, 66, 147, 102, 103, 157, 68, 88, 74, 65, 47, 146, 149 | B9, B10, B17 |
| 101–110 | Images: names, alt, compression, WebP/AVIF, dimensions, lazy, context, hero, image sitemaps | 58, 122, 14, 13, 70, 2 | Bing: images reinforce text, never replace it |
| 111–120 | Structured data: Schema.org, JSON-LD, Organization, Article, FAQ, Product, reviews, LocalBusiness, validation, upkeep | 59, 38, 71, 85 | B17 (misleading markup is ignored) |
| 121–130 | Internal linking, anchors, breadcrumbs, broken links, navigation | 82, 19, 123, 77 | B13 |
| 131–140 | Link building | 86–101 | B16 |
| 141–150 | Local: Bing Places, profile, NAP, hours, photos, reviews, local keywords, location pages, LocalBusiness | 28, 104, 85, 38 | B15 |
| 151–158 | UX: engagement, mobile, speed, readability, CTAs, site search, intrusive ads | 72–80, 7, 115 | B10 |
| 159 | Social signals | 27 | B16 (don't manufacture) |
| 160 | Continuous measurement in BWT | 119, 152 | B9, B24 |

---

## Bing-specific myths

| Claim | Reality | Do this |
|---|---|---|
| "Bing publishes a weighted list of the top ranking factors" | It publishes **main parameters in general order** with no weights; their importance varies by query | Use them as priorities, not a formula |
| "IndexNow guarantees indexing" | It speeds up notification only | IndexNow + sitemap + internal links |
| "Bing needs exact-match keywords everywhere" | Bing matches more literally, but stuffing and "engineered language" are named abuses | Exact wording where natural (B13) |
| "`noarchive` only affects the cached copy" | In Bing it removes the content from Copilot answers and grounding | Use only to opt out deliberately (B8) |
| "302 is fine for a few weeks" | Bing: only for changes under about two days | 301/308 (B5) |
| "Social signals are a Bing ranking factor, so buy engagement" | Not in Bing's published parameters; artificial social promotion is named abuse | Genuine sharing only (B16) |
| "Meta keywords help in Bing" | Ignored for ranking; stuffing can be a spam signal | Don't use (B14) |
| "AI Performance citations measure ranking" | Bing says they measure citation frequency, not ranking or authority | Use as a content signal (B9) |
| "Google Search Console is enough" | Bing data, IndexNow, Copilot citations and crawl control live only in BWT | Verify both (B1) |
