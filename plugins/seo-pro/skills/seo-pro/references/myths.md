# SEO myths and outdated advice

Popular SEO advice that is false, outdated or dangerous, and what to do instead. Check this list before recommending anything "from the textbook". Reviewed 18 October 2026; re-check platform behaviour against current official documentation (see `research-method.md`).

Severity: 🔴 can cause harm (penalty, legal exposure, traffic loss) · 🟠 false or outdated (wastes time) · 🟡 important nuance.

| Common advice | Reality | Do this instead | See | Severity |
|---|---|---|---|---|
| "Use the Google Indexing API to get any page crawled in minutes" | It is only permitted for `JobPosting` and `BroadcastEvent` pages. Using it for anything else breaches its terms | Sitemap with real `lastmod`, internal links, URL Inspection, IndexNow for Bing | 3, 5 | 🔴 |
| "Host on a local server/IP to rank in a country" | Server IP isn't a meaningful geotargeting signal; latency is what matters | Region close to users and database + CDN; geotarget with language, hreflang, domain and local data | 10 | 🟡 |
| "Block URL parameters in robots.txt" | If you block a URL that has a canonical, Google never sees the canonical; it may stay indexed without content | Don't link to valueless parameters + canonical; robots.txt only for infinite spaces | 20 | 🟡 |
| "Infinite scroll is bad for SEO" | It's fine if crawlable paginated URLs exist and are linked. `rel=next/prev` is no longer used | Paginate with `<a href>` and a self-canonical on each page | 22 | 🟡 |
| "Security headers / CSP boost rankings" | Not ranking signals; they prevent hacks, which do destroy SEO | Implement them for security | 29, 30 | 🟡 |
| "Privacy policies prevent quality penalties" | No such penalty exists; they're a legal obligation and a trust signal | Have them for compliance and trust | 33 | 🟠 |
| "Add FAQ Schema to get the FAQ dropdown" | Google FAQ rich results stopped appearing in Search on 7 May 2026 (since 2023 only government and health sites); HowTo was retired in 2023 | Use FAQs when they help visitors; don't add markup solely for a retired Google feature | 47, 59 | 🟠 |
| "A table of contents creates sitelinks" | It can generate jump links; nothing is guaranteed | Build it for UX | 48 | 🟡 |
| "GEO = put a summary at the top" | No format guarantees retrieval or citation; the foundations are indexing, no-JS accessibility, crawler access, Bing presence, authorship and verifiable data. Google's spam policies cover its AI features and Bing names AI manipulation as abuse | Follow the AI-search practices and engine layers; measure where first-party reporting exists | 61, 37, 68, 69, 148 | 🟡 |
| "Use LSI keywords" | Google doesn't use LSI; topic and entity coverage is what matters | Cover subtopics and entities naturally | 62 | 🟠 |
| "Increase dwell time" | What counts is satisfaction; a quick correct answer is also a success | Don't pad content to retain users | 72 | 🟡 |
| "Lower bounce rate to rank higher" | Bounce rate isn't a ranking factor. Intrusive interstitials do matter | Avoid intrusive pop-ups; measure engagement and conversions | 73 | 🟠 |
| "Dark mode reduces abandonment / helps SEO" | Not an SEO factor | Optional, low priority | 81 | 🟠 |
| "Delete every page with zero visits" | Can destroy links, conversions or new pages not yet matured | Improve / merge / noindex / delete based on 12 months of data | 84 | 🔴 |
| "Add review Schema to get stars" | Google's [review snippet policy](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) excludes self-serving reviews for `Organization`/`LocalBusiness`. Fake-review rules differ by jurisdiction | Genuine, verifiable reviews and current eligibility rules; check local law before advising on review practices | 85 | 🔴 |
| "Build natural-looking link triangles / exchanges" | Any organised scheme to manipulate links is a link scheme (spam) | Links with editorial justification | 95, 101 | 🔴 |
| "Prioritise backlinks from your country's TLD" | The linking domain's TLD is a weak signal; relevance matters | Links from your real market and industry | 99 | 🟡 |
| "Post job openings to look legitimate" | Marginal SEO benefit; fake openings violate `JobPosting` policies | Real openings only | 105 | 🔴 if fake |
| "Add countdown timers and 'only 2 left'" | False scarcity misleads users and can breach consumer-protection rules, depending on jurisdiction | Show only accurate, supportable stock and deadline information; check applicable law | 111 | 🔴 |
| "Show crossed-out prices to anchor value" | CRO, not SEO. EU price-reduction announcements generally must use the lowest prior price over at least 30 days; local rules vary ([European Commission](https://commission.europa.eu/topics/consumers/consumer-rights-and-complaints/enforcement-consumer-protection/sweeps_en)) | Use a truthful reference price and verify current local requirements | 114 | 🟡 |
| "Put price and stock in product titles" | Causes mismatches with the SERP and rewrites; the right channel is `Offer` Schema | Stable title templates + `Product`/`Offer` | 121 | 🟡 |
| "304 responses save massive crawl budget" | Useful, but crawl budget only matters for large sites | Implement ETag/Last-Modified without expecting miracles | 125 | 🟡 |
| "Block hotlinking" | Misconfigured, it blocks Google Images | Only if there's a real cost; allow-list search engines | 129 | 🔴 if Google is blocked |
| "hreflang prevents duplicate content penalties" | There's no duplicate penalty across languages; hreflang picks the right version | Implement it to serve the right version | 137 | 🟡 |
| "Gate resources behind a form to collect leads" | Content behind a form isn't indexed | An indexable landing page for each resource | 144 | 🟡 |
| "Bump the publish date to today to look fresh" | Google explicitly advises against changing dates without substantial changes | Update for real and set `dateModified` | 147 | 🔴 |
| "Brackets in titles dramatically increase CTR" | Based on old studies; Google rewrites titles | Test and measure | 151 | 🟠 |
| "Disavow toxic links regularly" | Google ignores most junk; mass disavows can remove helpful links | Only after a manual action or a known link purchase | 153 | 🔴 |
| "Rank in 30/60/90 days" | Timing depends on the site, query, market, competition, crawling and the changes made; competitive queries usually take months, but no fixed timeline is reliable | Set a baseline and review window; report uncertainty | SKILL.md | 🟡 |

Engine-specific myths live in each engine layer (e.g. `engines/bing.md` → "Bing-specific myths"); business-model myths live in `verticals/local.md` ("Local myths") and `verticals/ecommerce.md` ("E-commerce myths"). The most common ones:

| Claim | Reality | See |
|---|---|---|
| "Put the city and service in the business name" | Breaches Google's guidelines unless it's the real name; risks suspension | L3 |
| "Open a listing in every city you want to rank in" | Only real, eligible locations; use genuine area pages | L2, L13 |
| "Ask only happy customers for reviews" | Review gating; can breach platform rules and consumer law | L9 |
| "`LocalBusiness` schema ranks you in Maps" | Describes data; no eligibility or ranking effect | L15 |
| "Index every filter URL for long-tail" | Near-infinite duplicate/empty URLs; curate facets with demand | E5 |
| "Block all facets in robots.txt" | Can hide `noindex` on facets already indexed and block useful pages | E5, 20 |
| "The product feed lifts organic rankings" | Feeds power listings and ads, not organic ranking | E15, E20 |
| "Delete every sold-out product" | Destroys demand, links and alternatives; handle by stock state | E17 |
| "Apply for Google News / submit to Bing PubHub" | Google News needs no submission; PubHub is retired | P12, P18 |
| "`NewsArticle` is required for Top Stories" | Google says no markup is required | P14 |
| "A 301 keeps 100% of traffic" / "redirect everything to the home" | Strong move signal, not a guarantee; irrelevant redirects can be soft 404s | M7, M8 |
| "GA4 says SEO generated the sale" | That's credit under an attribution model, not causation | X8 |
| "Domain Authority is a ranking factor" | A vendor estimate, not a Google metric | R1 |
| "Programmatic SEO is penalised" / "AI text makes each generated page unique" | Google targets scaled pages without value, whatever produced them | D2, D9 |
| "YouTube tags matter a lot" | YouTube says tags play a minimal role | V8 |
| "Yandex needs the `Host` directive" / "hreflang works on Baidu" | `Host` is gone from Yandex docs; Baidu isn't documented to support hreflang | W2, W4 |
| "E-E-A-T is a score" / "a disclaimer lets us say anything" | Not a ranking factor or scale; disclaimers don't change substance or regulation | Y1, Y8 |

## AI search myths

| Claim | Reality | Do this | See |
|---|---|---|---|
| "Add `llms.txt` so Google cites you" | Google Search ignores it | Optional for docs tooling only | A12 |
| "There's special schema for AI answers" | Google: no special markup needed; a 2026 study of 1,885 pages adding schema saw AI citations barely move | Schema only for supported features | A12 |
| "Chunk every page into 300-word blocks" | No universal standard; Google says chunking isn't required | Structure for the reader's task | A12, 69 |
| "GEO gives up to 40% more visibility" | That's a maximum relative gain on one benchmark's metric; later benchmarks found many rewriting tactics ineffective or harmful | Treat as a hypothesis; test | A-evidence table |
| "An AI citation is like a backlink / a ranking" | Different event, different surface | Log citations separately | A15 |
| "Blocking GPTBot removes us from ChatGPT search" | Search uses `OAI-SearchBot`; GPTBot is training | Decide each agent separately | A2, A4 |
| "robots.txt keeps our private pages out of AI answers" | User-initiated fetchers may ignore it, and it's public | Authentication | A2, A5 |

## Other claims users often raise

- **"You need to publish X articles a month"**: quality and coverage of demand matter, not frequency.
- **"An article must be 2,000 words"**: length isn't a ranking factor; use what the intent requires.
- **"Ideal keyword density is 2 %"**: it doesn't exist; write naturally.
- **"Meta keywords help"**: Google has ignored them since 2009.
- **"Duplicate content is penalised"**: there's no penalty except deliberate spam copying; the problem is that Google picks one version and splits signals (fix it with canonicals).
- **"Add `nofollow` to every external link"**: only on paid (`sponsored`) or user (`ugc`) links; linking to good sources is positive.
- **"llms.txt is required to appear in AI answers"**: it's a proposal with no confirmed adoption by the major engines; not a ranking lever.
- **"AI-written content is automatically penalised"**: Google's policy targets scaled content abuse and intent to manipulate, regardless of how content is produced (Bing likewise names unreviewed auto-generated content at scale). That doesn't make every AI-assisted page safe or useful.
- **"Google Ads improves SEO"**: it doesn't affect organic rankings (though Ads data helps find keywords that convert).
- **"Social signals are a ranking factor"**: not directly; social helps distribution, link earning and brand building.
