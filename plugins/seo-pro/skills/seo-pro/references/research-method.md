# SEO research and evidence method

Use this file whenever a recommendation depends on a search engine's current behavior, a disputed ranking claim, an AI search feature, or a forecast. Search systems change; verify time-sensitive claims against current primary documentation when browsing is available. Research snapshot for this skill: **18 October 2026**. Links are starting points, not a substitute for checking the page's current date and scope.

## Contents

- Evidence hierarchy
- How to assess a claim
- Confidence labels
- Source register and limitations
- Current platform references

## Evidence hierarchy

Rank evidence by how directly it answers the question. Different evidence types answer different questions; don't flatten them into a single "authority" score.

1. **Observed site data** — Search Console, Bing Webmaster Tools, analytics, server logs, crawl/render tests, and controlled site experiments. Best for what happened on this property; observational data alone does not prove causation.
2. **Primary platform documentation and announcements** — Google Search Central, Bing Webmaster documentation/blog, and official product documentation. Best for published requirements, eligibility, tool definitions, and stated behavior. They do not disclose the full ranking systems or guarantee outcomes.
3. **Replicable research with disclosed methods** — studies with a defined sample, dates, controls, and data. Check whether the result generalizes to the site's market and period.
4. **Independent practitioner analysis and case studies** — useful for diagnosis and generating hypotheses. Look for the actual artifact/data, alternative explanations, and whether the author separates observation from inference.
5. **Vendor research and tool metrics** — useful for that vendor's dataset and product, not automatically a measure of Google's/Bing's internal systems. Check sample, definitions, selection effects, and commercial incentives.
6. **Anecdote or social post** — a lead to investigate, not a basis for a broad rule.

If sources conflict, state what each source can establish. A platform's documentation is strongest about its published policy; first-party Search Console data is stronger about this site's observed performance; neither alone proves why rankings changed.

## Cross-source synthesis

The 20-source review behind this method found that this list is not 20 independent votes. The durable overlap across official documentation, industry coverage, vendors, and practitioner work supports a small set of operating principles:

- Make important URLs discoverable, crawlable, indexable, and technically coherent. A diagnosed blocker deserves attention before speculative micro-optimisation.
- Match content to a real user task and add accurate, original value. Search intent and SERP formats are observations that should be rechecked by market and query, not copied mechanically.
- Use descriptive titles, useful page content, clear internal links, and accurate structured data. Treat display features as eligibility, not a promise.
- Avoid deceptive link schemes, fabricated business facts, and scaled pages whose purpose is ranking manipulation. Policies vary by engine; quote the applicable platform's current wording.
- Measure outcomes with first-party property data and preserve a baseline. Rankings and traffic can change for reasons outside the implementation being evaluated.

The review found weaker agreement on the causal effect of particular on-page formulas, exact title/description lengths, the value of named "GEO" tactics, how AI answers select sources, and the timing or impact of updates. Present these as hypotheses or unknowns, then test them. A vendor correlation or expert case study can inform a test; it cannot establish a universal ranking factor by itself.

The full Spanish-language synthesis behind this method lives outside the skill, in the repository's `docs/research-bible-2026-es.md` (with companion studies on AI search, local SEO, e-commerce, publishers, migrations, measurement, reputation, regulated topics and governance in the same folder), so it doesn't load into context. The operational instructions in `SKILL.md`, the phase and engine references, and current platform documentation take precedence when details change.

## How to assess a claim

For every high-impact or time-sensitive claim, record:

- **Claim:** one falsifiable statement, scoped to a search engine, surface, country, and date where relevant.
- **Evidence:** direct source links and the exact data or statement that supports it.
- **Type:** policy/eligibility, measurement, correlation, causal test, expert interpretation, or forecast.
- **Limitations:** sample size, selection bias, confounders, product rollout, and what the source cannot establish.
- **Action:** what to change, what should remain a hypothesis, and how to measure the result.

Prefer the latest official page for current product behavior. For a volatile claim, inspect its last-updated date and changelog; don't rely on an old blog article or a vendor summary when the primary source is available. Cite links close to claims in user-facing research. If browsing is unavailable, say so and avoid presenting a potentially stale fact as current.

## Confidence labels

Use them in every plan (a "Confidence" column) and in answers about disputed or time-sensitive behaviour.

- **Established:** supported by current official documentation or repeated direct evidence, within a stated scope.
- **Supported:** credible evidence exists, but important limits or conflicting observations remain.
- **Hypothesis:** plausible explanation or tactic without enough evidence to generalize; test on a limited set.
- **Unknown:** available sources do not settle the question.

Do not convert these labels into numeric scores, ranking guarantees, or false precision. Separate a verified issue (for example, a page returns `noindex`) from an inferred impact (how much traffic it costs).

## Source register: 20 references and how to use them

This is a curated reading map, not 20 independent confirmations. Several sources share authors, data, or commercial incentives. Use official docs for platform rules, independent data for broader patterns, and property data for decisions.

| Source | Best use | Limitation to keep in view |
|---|---|---|
| [Google Search Central documentation](https://developers.google.com/search/docs) | Published Google requirements, crawling, indexing, structured data, Search Console | Does not disclose full ranking weights or promise indexing/ranking |
| [Google Search Central blog](https://developers.google.com/search/blog) | Official announcements and clarifications | Announcement scope is not a quantified impact study |
| [Google Search Status Dashboard](https://status.search.google.com/) | Confirming reported incidents and updates | A status incident does not explain an individual site's change |
| [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) | Bing's published quality and technical guidance | Guidance is not a guarantee of ranking |
| [Bing Webmaster Blog](https://blogs.bing.com/webmaster/) | Bing product and policy announcements | Product claims and previews have specific availability and definitions |
| [Search Engine Land](https://searchengineland.com/) | Industry reporting, interviews, practical context | Secondary reporting; verify platform claims in primary sources |
| [Search Engine Journal](https://www.searchenginejournal.com/) | Tutorials and industry coverage | Editorial quality and evidence strength vary by author/article |
| [Search Engine Roundtable](https://www.seroundtable.com/) | Practitioner reports and volatility observations | Forum reports are anecdotal and may be unrepresentative |
| [SISTRIX blog](https://www.sistrix.com/blog/) | Visibility datasets and European market analysis | Visibility metrics are modeled and not first-party rank data |
| [Ahrefs blog](https://ahrefs.com/blog/) | Link, keyword, and content research using Ahrefs data | Vendor dataset and definitions; commercial product context |
| [Moz blog](https://moz.com/blog) | SEO education and tool-based studies | Verify older advice and methodology before applying it |
| [Semrush blog](https://www.semrush.com/blog/) | Competitive research and market datasets | Vendor data, sampling, and product definitions matter |
| [Onely](https://www.onely.com/blog/) | Technical SEO and rendering research | Specialist analysis; validate findings on the target stack |
| [Marie Haynes](https://www.mariehaynes.com/blog/) | Quality systems and update analysis | Expert interpretation, not inside knowledge of algorithm weights |
| [Aleyda Solis](https://www.aleydasolis.com/en/blog/) | International, technical SEO and practical frameworks | Practitioner experience; adapt advice to the site's data |
| [Lily Ray](https://lilyray.nyc/) | Quality, trust, and update analysis, especially YMYL | Case analysis and interpretation; distinguish from official policy |
| [Glenn Gabe](https://www.gsqi.com/marketing-blog/) | Technical diagnostics and observed update patterns | Case observations are not controlled causal evidence |
| [Cyrus Shepard](https://zyppy.com/) | On-page and ranking experiments | Check study design, sample, and date for each claim |
| [Kevin Indig](https://www.kevin-indig.com/) | Growth strategy, market analysis, and SEO experiments | Strategic interpretation; claims vary in evidence type |
| [Eli Schwartz](https://www.elischwartz.co/) | Product-led SEO and international growth strategy | Business framework, not a confirmed platform ranking signal |

## Current platform references (snapshot date above)

- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide): foundational practices; no magic word count or ranking guarantee.
- [Google Search Essentials: spam policies](https://developers.google.com/search/docs/essentials/spam-policies): read for current policy language; the policies apply to Search, including generative AI responses.
- [Google generative AI features guide](https://developers.google.com/search/docs/appearance/ai-features): Google's current advice for AI features; do not add unsupported "GEO hacks".
- [Google generative AI performance reports](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports): Search Console visibility reporting. Impressions/pages are not citation quality, clicks, or causal ranking impact.
- [Google title links](https://developers.google.com/search/docs/appearance/title-link) and [snippets](https://developers.google.com/search/docs/appearance/snippet): titles/descriptions are not fixed character-count fields in the SERP; truncation varies by display.
- [Google FAQ rich result deprecation](https://developers.google.com/search/updates): FAQ rich results stopped appearing in Search on 7 May 2026. FAQ content can still be useful to people; don't claim the markup provides a search benefit without current evidence.
- [Google review snippet eligibility](https://developers.google.com/search/docs/appearance/structured-data/review-snippet): current supported types, requirements, and self-serving review restrictions.
- [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a): use for Bing-specific policies and technical advice.
- [Bing AI Performance public preview](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/): read metric definitions and preview status before making comparisons.
- AI answer engines (OpenAI, Anthropic, Perplexity crawler docs; Search Console generative AI control; GEO research with evidence levels): see the source table at the end of `engines/ai-search.md`.
- Local SEO (Google Business Profile guidelines, Bing Places, Apple Business, review rules) and e-commerce (Google ecommerce and product docs, Merchant Center, UCP, ACP, Baymard): see the source lists at the end of `verticals/local.md` and `verticals/ecommerce.md`. Publishers, regulated topics, SaaS and services, migrations, measurement, reputation, programmatic pages, governance, video and images, and other engines: the source lists at the end of each file in `verticals/`, `playbooks/` and `engines/`. Where an official console couldn't be read (Baidu, Naver, Seznam in this snapshot), the layer marks claims as *Supported* or *Unconfirmed*. Expert surveys such as Whitespark's *Local Search Ranking Factors* are level C: practitioner opinion, not weights.
- [Bing sitemaps and IndexNow](https://blogs.bing.com/webmaster/2025/7/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search/): complementary discovery mechanisms; neither guarantees crawling, indexing, citation, or rank.

For legal or consumer-protection questions, use current jurisdiction-specific primary sources rather than this SEO reference. Starting points include [EU Directive 2019/2161](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L2161), [UK CMA fake review guidance](https://www.gov.uk/government/publications/fake-reviews), the [US FTC review rule guidance](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers), and the [European Commission's price-reduction rules](https://commission.europa.eu/topics/consumers/consumer-rights-and-complaints/enforcement-consumer-protection/sweeps_en). These are starting points; applicability depends on facts and jurisdiction.
