# AI answer engines layer (practices A1–A18)

Covers search experiences that retrieve web content to answer and sometimes cite: **Google AI Overviews / AI Mode** (and generative features in Discover), **ChatGPT Search**, **Perplexity**, and **Claude with web search**. **Microsoft Copilot** is covered by `bing.md` (B8, B9), since it is grounded on Bing's index. Read `README.md` in this folder first, and `../research-method.md` before making claims about AI visibility.

Research snapshot: **18 October 2026**. Names, agents, IP lists, reports and policies change; re-check the official links at the end before editing robots, WAF or structured data.

**The thesis.** The most defensible strategy is to make a source accessible, relevant, trustworthy and useful for a real need, then measure separately whether systems retrieve it, cite it, send visits and drive business results. No technique guarantees a mention or citation in every AI engine. "GEO", "AEO" and "AI SEO" are working labels, not disciplines with an agreed algorithm to optimise.

Format: **Why** · **How** · **Expected result** · **Avoid** · **Verify**, plus a confidence label from `research-method.md` where the evidence is mixed.

## Contents
- The funnel: from page to answer
- Platform controls at a glance
- Goal and access: A1–A7
- Content and reputation: A8–A13
- Measurement: A14–A17
- Priorities by site type: A18
- Evidence table: supported, hypothesis, myth
- 90-day sequence and executive checklist
- Sources with evidence levels

---

## The funnel: from page to answer

Diagnose AI visibility as seven separate stages. Fix the earliest failing stage first: an editorial change can't help if the crawler never reached the page.

1. **Access** — the system can request the URL (robots, WAF/CDN, authentication, geo-blocking, HTTP errors and rendering don't stop it).
2. **Discovery** — it learns the URL through links, crawling, sitemaps, feeds, a search, or a user's request.
3. **Processing and indexing** — it gets readable content and interprets page, language, entity, date and relations. A bot downloading a page doesn't prove it was indexed.
4. **Retrieval** — for a query, the system fetches candidate pages or data, possibly after rewriting the query or running sub-searches.
5. **Selection and generation** — it decides what material to use; it may also answer from prior knowledge without retrieving your page.
6. **Citation and presentation** — a link, an attribution, a brand mention, a card, or nothing. A mention is not a citation to your site.
7. **Visit and impact** — the user may click, remember, search the brand later, convert, or do nothing. A citation alone proves none of these.

"The bot can crawl the site" is an access condition, not a strategy. "The AI mentioned us" doesn't identify which URL was used or its role.

## Platform controls at a glance

| Surface | Search / citation agent | Training agent | User-initiated fetch | Owner reporting | Key nuance |
|---|---|---|---|---|---|
| Google AI Overviews, AI Mode, Discover gen-AI | `Googlebot` (normal Search eligibility: indexed and snippet-eligible) | `Google-Extended` (doesn't affect Search inclusion or ranking) | — | Search Console **Generative AI performance** report (impressions, pages, country, device, date; global since 31 Aug 2026) | Site-level **Search generative AI control** in Search Console (A3). No special markup, `llms.txt` or page length needed |
| Microsoft Copilot / Bing AI | `bingbot` | — (controlled with `noarchive`/`nocache`) | — | Bing **AI Performance** (preview): citations, cited pages, grounding queries, topics (beta) | See `bing.md` B8, B9 |
| ChatGPT Search | `OAI-SearchBot` | `GPTBot` | `ChatGPT-User` (robots.txt may not apply) | None comparable to Search Console; referrals carry `utm_source=chatgpt.com` | robots.txt changes for search take ~24 h; separate agents, separate decisions |
| Perplexity | `PerplexityBot` | — (not used for training) | `Perplexity-User` (generally ignores robots.txt) | None; logs, referrers, manual checks | Protect private content with authentication, not robots.txt |
| Claude with web search | `Claude-SearchBot` | `ClaudeBot` | `Claude-User` | None; logs and manual checks | Respects robots.txt; IP blocking is an unreliable opt-out because the bot can't read robots.txt |

All operators above publish IP ranges for verification (OpenAI per-agent JSON files, Anthropic `claude.com/crawling/bots.json`, Perplexity `perplexitybot.json` / `perplexity-user.json`, plus Google and Bing verification methods).

---

## Goal and access

### A1. Define the goal and the surfaces that matter — Critical
- **Why:** citations are not a business outcome. The goal decides the metric and whether opening content to some uses is even desirable.
- **How:** state the value sought (brand discovery, referral visit, lead, purchase, support deflection, inclusion as an educational source). Pick priority surfaces by audience, language, market and business model — don't start by "optimising for every AI".
- **Expected result:** a one-paragraph objective and a ranked list of surfaces in the plan.
- **Avoid:** optimising for mentions with no link to a business outcome.
- **Verify:** the plan's "How we will measure" section names the outcome metric, not only citations.

### A2. Decide access per agent purpose — Critical
- **Why:** search, training and user-initiated fetching are different uses with different controls. Copying another company's robots.txt block applies someone else's business decision.
- **How:** answer and document, per operator: (1) do we want public content to appear as a source in this platform's search? → allow its **search** agent; (2) do we allow training? → a separate decision on its **training** agent; (3) do we allow user-initiated fetches? → weigh product, content and extraction risk (some user agents ignore robots.txt); (4) is there private content? → authentication, never robots.txt. A common configuration for a business that wants AI visibility without training use (adapt, don't paste):
  ```
  User-agent: OAI-SearchBot
  Allow: /
  User-agent: PerplexityBot
  Allow: /
  User-agent: Claude-SearchBot
  Allow: /
  User-agent: GPTBot
  Disallow: /
  User-agent: ClaudeBot
  Disallow: /
  User-agent: Google-Extended
  Disallow: /
  ```
  Repeat per subdomain; record the review date.
- **Expected result:** a written decision per agent, reflected in robots.txt, headers, WAF and authentication.
- **Avoid:** blocking search agents while expecting citations; treating robots.txt as security; assuming a block on one agent affects another product.
- **Verify:** the auditor's crawler table groups agents by purpose; test with each agent's user agent and check logs.

### A3. Google: Search generative AI control and eligibility — Critical
- **Why:** Google requires pages to be indexed and snippet-eligible, **and** the site to be included via the **Search generative AI control** in Search Console (Settings → Search generative AI; global since 31 August 2026; default *Include*). *Exclude* removes the site's links and content from AI Overviews, AI Mode and Discover's generative features, and from grounding them.
- **How:** check the control on every property (and that child properties inherit what you intend). Keep pages snippet-eligible: `nosnippet` and very restrictive `max-snippet` limit how content can be shown. `Google-Extended` governs certain AI uses outside Search and does not affect Search inclusion or ranking.
- **Expected result:** a deliberate setting, documented in the plan.
- **Avoid:** flipping the control to "protect content" without measuring the traffic impact in the Generative AI performance report first.
- **Verify:** Search Console → Settings → Search generative AI; Generative AI performance report.

### A4. ChatGPT Search — High
- **Why:** sites appear in ChatGPT search only if `OAI-SearchBot` can access them; `GPTBot` (training) and `ChatGPT-User` (user actions) are independent.
- **How:** allow `OAI-SearchBot`. To keep a page out of ChatGPT search, use `noindex` and leave it crawlable (a disallowed page found elsewhere can still appear as a bare link and title). Tag analytics for `utm_source=chatgpt.com` referrals. For agentic browsing (ChatGPT Atlas), descriptive ARIA roles, labels and states on interactive elements help it operate the site.
- **Expected result:** eligibility for ChatGPT search; measurable referrals.
- **Avoid:** expecting changes to apply instantly (allow ~24 h for robots.txt changes to take effect for search).
- **Verify:** logs for `OAI-SearchBot` hits verified against OpenAI's published IPs; analytics segment for `chatgpt.com`.

### A5. Perplexity — Medium
- **Why:** `PerplexityBot` surfaces and links sites in results (not used for training); `Perplexity-User` fetches pages when a user asks and generally ignores robots.txt.
- **How:** allow `PerplexityBot` if you want to appear; put anything private behind authentication; allow both agents in the WAF by matching user agent **and** published IP ranges.
- **Expected result:** eligibility for Perplexity citations; no private data exposed by user fetches.
- **Avoid:** relying on robots.txt to keep content out of user-initiated fetches.
- **Verify:** logs; referral segment for `perplexity.ai`.

### A6. Claude with web search — Medium
- **Why:** `Claude-SearchBot` indexes for search quality, `Claude-User` retrieves pages for user questions, `ClaudeBot` collects training data; each honours robots.txt.
- **How:** allow `Claude-SearchBot` and `Claude-User` if you want visibility; decide on `ClaudeBot` separately. Opt out with robots.txt per subdomain, not IP blocks (blocking IPs also stops the bot reading robots.txt).
- **Expected result:** eligibility for Claude's web answers.
- **Avoid:** IP-level blocks as the opt-out mechanism.
- **Verify:** logs verified against `claude.com/crawling/bots.json`; referral segment for `claude.ai`.

### A7. Let legitimate bots through the WAF/CDN — High
- **Why:** many "invisible in AI" cases are bot-protection challenges, not content problems.
- **How:** allow-rules that match the documented user agent **and** the operator's published IP list, refreshed automatically; never trust the user agent alone (it's trivially spoofed). Review "block AI bots" toggles in Cloudflare and similar (shared 37).
- **Expected result:** 200 responses to verified search and user agents.
- **Avoid:** allowing by user agent alone into sensitive areas.
- **Verify:** WAF event logs; test requests; server logs.

---

## Content and reputation

### A8. Content readable without interaction — Critical
- **Why:** the access and processing stages fail if the main content needs JavaScript, clicks or login to appear.
- **How:** shared 25 and 127 (served HTML, standard `<a href>` links, no content behind interactions crawlers can't perform).
- **Verify:** `curl` the URL; the auditor's served-HTML word count.

### A9. Original, verifiable evidence — High · *Supported (impact varies by query and platform)*
- **Why:** first-hand data, documentation and experience aren't interchangeable with generic pages.
- **How:** publish evidence with provenance, method and limits; define terms, dates, units, scope and sources; put conclusions next to the context that explains them; link primary sources (shared 89, 103, 69).
- **Avoid:** invented studies, statistics or "case studies".
- **Verify:** every figure on priority pages has a source and date.

### A10. Entity clarity and consistency — High · *Supported*
- **Why:** answers combine text, images, video, product data and local data; contradictions reduce confidence (Bing makes the same point).
- **How:** one official name per product/company with consistent variants; prices, stock, hours and specs consistent across pages, feeds, profiles and structured data (shared 104, 140).
- **Avoid:** repeating the brand name to "teach" the model.

### A11. Build reputation without manipulating it — Critical
- **Why:** source selection may depend on retrieval and on a system's familiarity with entities; research is early, but manufactured signals are both risky and harmful (recent work shows source contamination is an attack surface).
- **How:** genuine editorial coverage, transparent collaborations, useful public documentation, community participation, independent third-party references (shared 86–101, 128).
- **Avoid:** paid fake mentions, "guaranteed AI mentions", seeded posts on low-barrier platforms, fabricated "best of" lists, content designed to plant fictional facts in answers.

### A12. Structured data only for its real purpose — Medium · *Myth if sold as an AI lever*
- **Why:** Google states no special markup is needed for its AI features; a 2026 vendor study of 1,885 pages adding schema found AI citations barely moved.
- **How:** shared 59 — supported types, true and visible values, for rich-result eligibility and entity clarity.
- **Avoid:** "GEO schema", AI-specific markup or `llms.txt` promised as citation levers (Google ignores `llms.txt`).

### A13. Freshness only when something changed — Medium
- **How:** show effective dates on prices, versions, availability, hours, rules and statistics, and update them when they change (shared 147). Recency matters for some time-sensitive queries; it's not proven that newer always wins.
- **Avoid:** simulated freshness.

---

## Measurement

### A14. A fixed query panel — High
- **How:** a stable set of representative queries, each with its reason for inclusion, stratified by intent (learn, compare, buy, fix, find local), category, decision stage, language/market, brand vs competitor vs category, and high-risk topics. Small sites: a panel you can check by hand; large sites: a stratified sample. Don't present the panel size as statistically sufficient without sampling design.

### A15. An observation log — High
- **How:** one row per run with: engine and surface; date/time and market; literal query; mode/session (web on, new session, device; model if known); result type; own URL cited and the claim attributed to it; source role (direct citation, context, unlinked mention, navigational link); **fidelity** (does the page support the claim: yes / partly / no / can't tell); presentation (position, number of sources); competitors and external domains; downstream outcome (clicks, sessions, leads). Repeat on different dates, keep negative results, respect each product's terms, and don't mass-automate queries.

### A16. Metrics with your own definitions — High
1. **Accessibility:** % of priority URLs reachable by each target agent (tests + logs).
2. **Panel citation coverage:** eligible runs citing at least one own URL ÷ eligible runs observed (publish denominator, period, engines, protocol).
3. **Page coverage:** own pages cited, by section, intent and engine.
4. **Citation share within the panel:** own citations ÷ all citations recorded — not market share.
5. **Attribution fidelity:** share of citations where the page really supports the claim (human sampling).
6. **Official platform visibility:** Search Console Generative AI performance; Bing AI Performance — within each product's scope.
7. **Attributable visits:** referral sessions from AI products (`utm_source=chatgpt.com`, `perplexity.ai`, `copilot.microsoft.com`, `gemini.google.com`, `claude.ai`…); attribution is incomplete.
8. **Business outcome:** sales, qualified leads, revenue, support cost, separating assisted and direct conversions with a stated window.

Don't merge metrics with different definitions into one "AI visibility score" without documenting weights, coverage and bias. This complements shared 148.

### A17. Test changes like experiments — High
- **How:** a specific hypothesis; comparable pages with an untouched control group where possible; one substantive change at a time, logged with date and URLs; the same panel repeated several times; check the funnel stage affected (access → retrieval → citation → traffic → business); account for seasonality, product changes, engine updates, brand campaigns and analytics changes; accept null results and call small or uncontrolled findings *directional*.

---

## A18. Priorities by site type

| Site type | Reasonable priorities | Interpretation risk |
|---|---|---|
| Editorial / media | Per-bot access policy, rights and licensing, authorship, primary sources, original data; measure impressions, citations and traffic | A citation can replace a visit; separate brand value, traffic and revenue model |
| E-commerce | Exact product, price, stock, shipping and returns data; accessible pages; current feeds; transparent comparisons; agentic-commerce channels (ChatGPT product feeds via ACP, Google UCP) as separate products (`../verticals/ecommerce.md` E21) | Product schema doesn't raise citations by itself; stale price/stock can make answers wrong |
| SaaS / documentation | Public crawlable docs, clear versions, working examples, limits and compatibility; links between product, docs and support | Docs behind login or code only inside the app can't be retrieved |
| Local | Consistent name, address, phone, area, hours, services; official profiles (GBP, Bing Places, Apple Business); genuine reviews; customer FAQs on the website, which Google Maps' AI "Ask" feature can draw on (`../verticals/local.md` L8) | Wrong hours or availability cause direct harm; monitor answers |
| Health, finance, legal (YMYL) | Verifiable credentials, professional review, primary sources, dates, limits, correction process, compliance | Summaries lose nuance; audit critical claims; a citation isn't professional endorsement |
| B2B / manufacturers | Specs, compatibility, current certifications, versioned downloadable sheets, verifiable cases, stable entity vocabulary | Little-known products may not surface in familiarity-driven answers; don't manufacture mentions |

---

## Evidence table: supported, hypothesis, myth

| Claim | Assessment | Prudent application |
|---|---|---|
| Public, crawlable, indexable, useful, well-linked pages have more chances of being considered by search-based AI systems | **Established** as a foundation; no citation guarantee | Fix crawling, canonicals, rendering, internal links and quality before AI-specific tactics |
| Original research, data, documentation and experience add non-interchangeable information | **Supported**; impact varies by query and platform | Publish verifiable evidence with method and limits |
| Precise headings, defined terms, readable tables and direct answers help people and may ease extraction | **Supported** as editorial practice; **not** a proven universal citation lever | Do it for comprehension; measure; don't fragment mechanically |
| Special schema to appear in AI answers | **Not supported**; Google says no special markup is needed | Use structured data only for supported features, describing visible truth |
| `llms.txt` makes Google cite you more | **Myth** for Google Search, which ignores it | Optional for documentation tooling; never a substitute for sitemaps, robots or readable HTML |
| Paragraphs of X words, pages of Y words, "chunk everything into 300-word blocks" | **No universal standard**; Google says no chunking is required | Structure by task and user |
| Repeat the brand, mimic prompts, add "best brands" lists | **Not shown; risks quality and manipulation** | Work on real intent and entity clarity; don't fabricate comparisons |
| An AI citation equals a backlink or a Google position | **False equivalence** | Log citations as their own event with surface and query |
| More citations prove more sales | **Not shown** | Connect exposure to sessions and conversions; acknowledge dark traffic |
| The KDD 2024 GEO paper guarantees "up to 40% more visibility" | **Misreading** | The 40% is a maximum relative gain on that paper's metric and benchmark; C-SEO Bench (NeurIPS 2025) found many rewriting methods ineffective or harmful, while classic SEO that raised the chance of entering the context worked better there |
| Retrieval matters more than page features for citations | **Hypothesis** (October 2026 preprint, two markets, ~468k citations) | Prioritise access, indexing and ranking work; test page-level changes |

---

## 90-day sequence (evidence, not a growth promise)

- **Days 1–15 — define and measure:** goal and surfaces (A1); bot, robots, WAF, privacy and rights review (A2–A7); Search Console generative AI control (A3); query panel and baseline (A14, A15); analytics referrers and attribution limits.
- **Days 16–35 — fix access and priority pages:** HTTP errors, accidental blocks, canonicals, internal links, rendering (A8); readable text, no orphans; product, business, author and date inconsistencies (A10). No mass content rewrite without a usefulness audit.
- **Days 36–65 — add original evidence:** a small set of high-value pages; add experience, method, sources, real comparisons or proprietary data (A9); keep comparable pages untouched as a control.
- **Days 66–90 — review and decide:** rerun the panel and technical checks with the same protocol; reconcile Search Console and Bing reports with logs and analytics; review citation fidelity, clicks, leads and revenue; document null, positive and adverse effects; stop changes that only increase empty mentions (A16, A17).

## Executive checklist

- [ ] Goal and priority surfaces defined.
- [ ] Search, training and user-fetch decisions taken separately per operator.
- [ ] robots.txt, `noindex`, canonicals, WAF, authentication and subdomains reflect the real policy; Search Console generative AI control checked.
- [ ] Legitimate crawler access verified in logs against current official IP lists.
- [ ] Priority pages discoverable, linked and readable without opaque interactions.
- [ ] Content carries original evidence where relevant; prices, versions, hours and dates current and contextualised.
- [ ] Authors, entities, sources and conflicts of interest presented accurately.
- [ ] Schema and auxiliary files not sold internally as citation guarantees.
- [ ] A fixed query panel exists and negative results are recorded.
- [ ] Metrics separate crawling, indexing, retrieval, citation, session and conversion.
- [ ] AI-generated claims about the business are reviewed for fidelity, especially in sensitive areas.
- [ ] Third-party tactics are judged by method, date, sample, commercial interest and replicability.

---

## Sources with evidence levels

Levels: **A** official platform documentation/tools · **B** peer-reviewed research · **C** preprint · **D** vendor/observational · **E** practitioner.

| Level | Source | Use |
|---|---|---|
| A | [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) | Eligibility and reporting for Search AI features |
| A | [Google: optimizing for generative AI features](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) | No special markup, files, length or chunking required |
| A | [Search Console: Search generative AI control](https://support.google.com/webmasters/answer/16908024) | Site-level include/exclude (global since 31 Aug 2026) |
| A | [Search Console: Generative AI performance reports](https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports) | Impressions, pages, country, device, date |
| A | [Google-Extended](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended) | AI-use token, separate from Search |
| A | [Google: robots.txt introduction](https://developers.google.com/search/docs/crawling-indexing/robots/intro) | robots.txt isn't access control |
| A | [OpenAI crawlers](https://developers.openai.com/api/docs/bots) · [Publishers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) | Agents, ~24 h propagation, IP lists, `utm_source=chatgpt.com`, `noindex` |
| A | [Anthropic crawlers](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler) | ClaudeBot, Claude-User, Claude-SearchBot, `bots.json` |
| A | [Perplexity crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers) | PerplexityBot, Perplexity-User, IP lists, WAF rules |
| A | [Bing AI Performance](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/) · [AI visibility insights](https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/) · [Topics Portfolio beta](https://blogs.bing.com/webmaster/2026/10/introducing-topics-portfolio-beta-in-ai-performance/) | Copilot citation data; directional, not ranking |
| B | Aggarwal et al., [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) (KDD 2024) | Founding benchmark; "up to 40%" is a situated metric |
| B | Puerto et al., [C-SEO Bench](https://papers.neurips.cc/paper_files/paper/2025/hash/27aa3aeff0f8460a7b43d30fa6c5c032-Abstract-Datasets_and_Benchmarks_Track.html) (NeurIPS 2025) | Limits of rewriting tactics |
| C | Chen & Koudas, [What Drives AI Citations?](https://arxiv.org/abs/2610.15033) (Oct 2026) | Retrieval vs page properties; not peer-reviewed |
| C | Liu et al., [From Public Posts to AI-Search Citations](https://arxiv.org/abs/2610.11932) (Oct 2026) | Source concentration and contamination risk — a risk, not a tactic |
| C | [Optimizing Visibility in Generative Engines: A Critical Survey (2023–2026)](https://arxiv.org/abs/2607.14035) | Heterogeneous metrics, little durable causal evidence |
| D | Ahrefs, [We Tracked 1,885 Pages Adding Schema](https://ahrefs.com/blog/schema-ai-citations/) (2026) | Signal against the schema-for-AI hypothesis |
| B | Marketing Science, [ChatGPT Referrals to E-Commerce Websites](https://doi.org/10.1287/mksc.2025.0489) | Referral traffic in an e-commerce sample |

Before changing robots, WAF, structured data or editorial policy, re-read the primary source and note the date, scope, region, and whether the feature is public or beta.
