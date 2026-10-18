# SEO myths and outdated advice

Popular SEO advice that is false, outdated or dangerous, and what to do instead. Check this list before recommending anything "from the textbook". Reviewed October 2026.

Severity: 🔴 can cause harm (penalty, legal exposure, traffic loss) · 🟠 false or outdated (wastes time) · 🟡 important nuance.

| Common advice | Reality | Do this instead | See | Severity |
|---|---|---|---|---|
| "Use the Google Indexing API to get any page crawled in minutes" | It is only permitted for `JobPosting` and `BroadcastEvent` pages. Using it for anything else breaches its terms | Sitemap with real `lastmod`, internal links, URL Inspection, IndexNow for Bing | 3, 5 | 🔴 |
| "Host on a local server/IP to rank in a country" | Server IP isn't a meaningful geotargeting signal; latency is what matters | Region close to users and database + CDN; geotarget with language, hreflang, domain and local data | 10 | 🟡 |
| "Block URL parameters in robots.txt" | If you block a URL that has a canonical, Google never sees the canonical; it may stay indexed without content | Don't link to valueless parameters + canonical; robots.txt only for infinite spaces | 20 | 🟡 |
| "Infinite scroll is bad for SEO" | It's fine if crawlable paginated URLs exist and are linked. `rel=next/prev` is no longer used | Paginate with `<a href>` and a self-canonical on each page | 22 | 🟡 |
| "Security headers / CSP boost rankings" | Not ranking signals; they prevent hacks, which do destroy SEO | Implement them for security | 29, 30 | 🟡 |
| "Privacy policies prevent quality penalties" | No such penalty exists; they're a legal obligation and a trust signal | Have them for compliance and trust | 33 | 🟠 |
| "Add FAQ Schema to get the FAQ dropdown" | Google stopped showing FAQ rich results for all sites on 7 May 2026 (since 2023 only government and health sites). HowTo was retired in 2023 | FAQs as useful content; `FAQPage` markup can stay (Google still reads it) without expecting the dropdown | 47, 59 | 🟠 |
| "A table of contents creates sitelinks" | It can generate jump links; nothing is guaranteed | Build it for UX | 48 | 🟡 |
| "GEO = put a summary at the top" | Broader: indexing, no-JS accessibility, allowing AI search bots, Bing, authorship, verifiable data. Manipulating AI answers is spam since May 2026 | Follow the AI-search practices | 61, 37, 68, 69, 148 | 🟡 |
| "Use LSI keywords" | Google doesn't use LSI; topic and entity coverage is what matters | Cover subtopics and entities naturally | 62 | 🟠 |
| "Increase dwell time" | What counts is satisfaction; a quick correct answer is also a success | Don't pad content to retain users | 72 | 🟡 |
| "Lower bounce rate to rank higher" | Bounce rate isn't a ranking factor. Intrusive interstitials do matter | Avoid intrusive pop-ups; measure engagement and conversions | 73 | 🟠 |
| "Dark mode reduces abandonment / helps SEO" | Not an SEO factor | Optional, low priority | 81 | 🟠 |
| "Delete every page with zero visits" | Can destroy links, conversions or new pages not yet matured | Improve / merge / noindex / delete based on 12 months of data | 84 | 🔴 |
| "Add review Schema to get stars" | Reviews about your own business in `Organization`/`LocalBusiness` haven't shown stars since 2019. Fake reviews are illegal in the EU, UK and US | Real, verifiable reviews; `AggregateRating` only on products | 85 | 🔴 |
| "Build natural-looking link triangles / exchanges" | Any organised scheme to manipulate links is a link scheme (spam) | Links with editorial justification | 95, 101 | 🔴 |
| "Prioritise backlinks from your country's TLD" | The linking domain's TLD is a weak signal; relevance matters | Links from your real market and industry | 99 | 🟡 |
| "Post job openings to look legitimate" | Marginal SEO benefit; fake openings violate `JobPosting` policies | Real openings only | 105 | 🔴 if fake |
| "Add countdown timers and 'only 2 left'" | If not true, these are unfair commercial practices and banned dark patterns | Only with real data | 111 | 🔴 |
| "Show crossed-out prices to anchor value" | CRO, not SEO. Fictitious "was" prices are illegal in the EU | Real reference prices (lowest of the last 30 days in the EU) | 114 | 🟡 |
| "Put price and stock in product titles" | Causes mismatches with the SERP and rewrites; the right channel is `Offer` Schema | Stable title templates + `Product`/`Offer` | 121 | 🟡 |
| "304 responses save massive crawl budget" | Useful, but crawl budget only matters for large sites | Implement ETag/Last-Modified without expecting miracles | 125 | 🟡 |
| "Block hotlinking" | Misconfigured, it blocks Google Images | Only if there's a real cost; allow-list search engines | 129 | 🔴 if Google is blocked |
| "hreflang prevents duplicate content penalties" | There's no duplicate penalty across languages; hreflang picks the right version | Implement it to serve the right version | 137 | 🟡 |
| "Gate resources behind a form to collect leads" | Content behind a form isn't indexed | An indexable landing page for each resource | 144 | 🟡 |
| "Bump the publish date to today to look fresh" | Google explicitly advises against changing dates without substantial changes | Update for real and set `dateModified` | 147 | 🔴 |
| "Brackets in titles dramatically increase CTR" | Based on old studies; Google rewrites titles | Test and measure | 151 | 🟠 |
| "Disavow toxic links regularly" | Google ignores most junk; mass disavows can remove helpful links | Only after a manual action or a known link purchase | 153 | 🔴 |
| "Rank in 30/60/90 days" | Ranking for competitive queries takes months | Phases are an order of work, not a calendar | SKILL.md | 🟡 |

## Other claims users often raise

- **"You need to publish X articles a month"**: quality and coverage of demand matter, not frequency.
- **"An article must be 2,000 words"**: length isn't a ranking factor; use what the intent requires.
- **"Ideal keyword density is 2 %"**: it doesn't exist; write naturally.
- **"Meta keywords help"**: Google has ignored them since 2009.
- **"Duplicate content is penalised"**: there's no penalty except deliberate spam copying; the problem is that Google picks one version and splits signals (fix it with canonicals).
- **"Add `nofollow` to every external link"**: only on paid (`sponsored`) or user (`ugc`) links; linking to good sources is positive.
- **"llms.txt is required to appear in AI answers"**: it's a proposal with no confirmed adoption by the major engines; not a ranking lever.
- **"AI-written content is penalised"**: low-value content and mass generation to manipulate rankings (scaled content abuse) are penalised, not the tool.
- **"Google Ads improves SEO"**: it doesn't affect organic rankings (though Ads data helps find keywords that convert).
- **"Social signals are a ranking factor"**: not directly; social helps distribution, link earning and brand building.
