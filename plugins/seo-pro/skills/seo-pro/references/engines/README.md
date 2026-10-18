# Search engines: how seo-pro handles more than one

The 160 practices in `phase-1/2/3` are the **shared core**: they work for every major search engine because all of them crawl, index and rank on the same foundations (crawlable HTML, canonical URLs, clear content, real authority). Each engine then has a thin layer of its own: different tools, a few different directives, different emphasis. This folder holds those layers.

| File | Engine(s) | Practice IDs | Status |
|---|---|---|---|
| `bing.md` | Bing, Microsoft Copilot, and products that license Bing results | B1–B24 | Available |

New engines are added as their own file with their own ID prefix (e.g. `chatgpt.md` → C1…), plus a row in this table and a column in the matrix below. Never renumber the shared core.

## Step 0 of every job: decide the target engines

Ask (or infer from the market) which engines matter. Defaults:

- **Every site:** Google + Bing. Bing is small in many markets, but its index also feeds Microsoft Copilot and several other search and AI products, so ignoring it means ignoring a whole family of surfaces.
- **Markets with other leaders** (e.g. Yandex, Naver, Baidu, Seznam): flag that the skill doesn't yet have a layer for them and apply the shared core.

Then read the shared practice **and** the engine layer for anything you implement. The engine layer only lists what changes.

## Conflict-resolution rule

When two engines want different things, choose the option that **satisfies both**, in this order:

1. **Do both** when they don't interfere (e.g. Search Console *and* Bing Webmaster Tools; sitemap *and* IndexNow; `hreflang` *and* `content-language`).
2. **Pick the stricter requirement** when one is a subset of the other (e.g. Bing wants 302s only for changes under ~2 days; Google tolerates longer → use 301/308 for anything that isn't truly a couple of days).
3. **Prefer the user-facing truth** when they genuinely conflict: the version that's best for users and honest about the content wins, because every engine's guidelines converge there.
4. **Document the trade-off** in the plan under "What we will NOT do" when a choice helps one engine at the other's expense.

## Google vs Bing — decision matrix

Only rows where behaviour differs or each engine has its own tool. Everything else follows the shared practice.

| Topic | Google | Bing | What seo-pro does | Practices |
|---|---|---|---|---|
| Webmaster tool | Search Console | Bing Webmaster Tools (can import from Search Console) | Verify both on day one | 1, B1 |
| Fast discovery | Sitemap + internal links + URL Inspection; Indexing API only for jobs/livestreams | IndexNow (streamed, not batched) + sitemap + URL Submission | Sitemap for all; IndexNow on publish/update/delete | 2, 3, 5, B2 |
| Freshness signals | `lastmod` (if trustworthy) | `lastmod` **and** ETag/validation headers explicitly named | Accurate `lastmod` + ETag/Last-Modified + 304s | 2, 125, B3 |
| Temporary redirects | 302/307 for temporary; long-lived 302s eventually treated as permanent | 302 only for very short changes (< ~2 days); use redirects, not canonicals, for moves | 301/308 unless genuinely a couple of days | 23, B5 |
| `crawl-delay` in robots.txt | Ignored | Honoured; overrides the Crawl Control setting | Don't set it unless Bingbot load is a real problem; use Crawl Control instead | 4, B6 |
| JavaScript rendering | Renders, deferred | Renders less reliably; guidelines warn against hiding critical content behind client-side rendering | SSR/SSG for everything indexable (already the core rule) | 25, 127, B7 |
| Snippet / AI directives | `nosnippet`, `max-snippet`, `data-nosnippet`; `noarchive` has no AI effect | `noarchive` → **excluded from Copilot answers and grounding**; `nocache` → Copilot may use only URL, title and snippet; `nosnippet`/`data-nosnippet` limit citation quality | Never add `noarchive`/`nocache` to content that should be cited; use them deliberately to opt out | 37, B8 |
| AI training opt-out | `Google-Extended` (doesn't affect AI Overviews) | No separate token; control via `noarchive`/`nocache` | Document the decision per engine | 37, B8 |
| AI visibility reporting | AI Overviews/AI Mode counted inside Search Console performance | **AI Performance** report: citations, cited pages, grounding queries (preview, Feb 2026) | Track both; Bing gives the richer citation data | 148, B9 |
| Ranking factors (published) | No ordered list | Publishes main parameters: relevance, quality & credibility, user engagement, freshness, location & language, page load time | Shared core already covers them; Bing makes engagement, freshness and speed explicit | B10 |
| Hosting location | Not a meaningful signal | "Where the page is hosted" listed under location | Host in-market or use a CDN with local edge; keep ccTLD/hreflang/lang signals | 10, 11, B11 |
| Language/region signals | `hreflang` (primary), content | `<html lang>`, `content-language`, content; Bing has historically treated hreflang as a weaker hint | Emit `hreflang` **and** correct `lang` (+ optional `content-language`) | 134–137, B12 |
| Exact wording | Heavy synonym/semantic matching | Relevance defined with "matching terms, link phrases, synonyms"; more literal | Use the searcher's exact wording in title/H1/anchors where natural | 56, 82, B13 |
| Meta keywords | Ignored | Ignored for ranking; stuffing can be a spam signal | Don't use | myths, B14 |
| Local listings | Google Business Profile | Bing Places for Business (bing.com/forbusiness; can import from GBP) | Maintain both with identical NAP | 28, B15 |
| Link guidance | Spam policies | Link schemes **and** "artificial social promotion" named | Earned links only; no fake social signals | 101, B16 |
| AI manipulation | Spam policies cover AI Overviews/AI Mode (May 2026) | "Prompt injection and AI manipulation" explicitly named | No hidden instructions to models, anywhere | 61, 67, B17 |
| Crawl control & tools | Crawl stats; no rate setting | Crawl Control (hourly rate), Block URLs, robots.txt tester, Verify Bingbot, Site Scan, Keyword Research, Backlinks, Recommendations, Clarity | Use them in audits | B18–B21 |
| Video / news | Video sitemaps, `VideoObject`; Publisher Center | mRSS feeds; Bing News PubHub | Implement the engine-specific feed only if video/news matters | 146, B22, B23 |
