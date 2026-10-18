# Phase 2 — Content, on-page, AI search and user experience (practices 41–85)

Goal: every important URL serves a specific search intent better than reasonable alternatives, is clearly represented to search engines, and helps users complete their task.

Review criteria: a query-to-URL map with intentional distinctions; indexable pages with descriptive titles, useful headings and correct canonicals; content that adds value beyond current alternatives; eligible and accurate structured data; useful internal links; and a baseline for monitoring. These criteria do not guarantee impressions or rankings.

Format: **Why** · **How** · **Expected result** · **Avoid** · **Verify**.

## Contents
- Content strategy and keywords: 41–55
- Advanced on-page and AI search: 56–71
- User experience and engagement: 72–81
- Internal linking and content curation: 82–85

## How to approach content as an AI (read before writing)

1. **Never write without studying the SERP.** With web search available, look at the top 5–10 results for the target query: page type (guide, list, product page, tool, comparison), format, depth, angle, what's missing. Without access, ask the user or state the assumption explicitly.
2. **Look for real differentiators:** first-hand experience, proprietary data, accurate prices, original images, case studies, or accountable expert analysis where available. Do not fabricate these. Generic copy may be less useful, but do not claim a search engine can reliably identify how a text was authored.
3. **Never invent** figures, studies, quotes, reviews, authors or credentials. When data is missing, leave a visible `[TODO: …]` placeholder and list them all for the user at the end.
4. **Make information easy to evaluate:** answer the user's question clearly, define terms, identify sources for factual claims, and use tables when they improve comparison. No structure guarantees inclusion in an AI answer.
5. **Deliver the full package per URL:** title, meta description, slug, H1, H2/H3 outline, body, proposed internal links (in and out), JSON-LD, image alt text, and the list of pending data.

---

## Content strategy and keywords

### 41. Start with low-competition long-tail — High
- **Why:** a new domain lacks the authority to compete for broad terms; specific searches convert better and are reachable.
- **How:** idea sources: Search Console (queries with impressions in positions 8–30), Google autocomplete, "People also ask", forums (Reddit, niche communities), real customer questions (support, sales), tools (Ahrefs, Semrush, Sistrix, Keyword Planner). Signs of low competition: the top 10 includes forums, old pages, small sites, or results that don't answer well.
- **Expected result:** a focused set of opportunities to test; timing and rankings are uncertain.
- **Avoid:** obsessing over tools' monthly volume (they tend to underestimate long-tail and the sum of variants); creating one page per tiny variation (cannibalisation, 46).
- **Verify:** track query impressions and clicks in Search Console over a comparison window suited to baseline volume, seasonality and the change made; avoid treating a short window as causal proof.

### 42. Satisfy search intent — Critical
- **Why:** it is the single most decisive factor. If Google shows comparisons and you offer a product page, you won't get in no matter how good your page is.
- **How:** classify the intent (informational, commercial investigation, transactional, navigational, local) and the **dominant format** of the top 10. Answer the main question and the immediate follow-ups (142). Match what the top results have in common and beat them where nobody does it well.
- **Expected result:** the page fits the type of result Google already considers appropriate.
- **Avoid:** copying the top 10 so closely that you add nothing new.
- **Verify:** stable CTR and position; reasonable engagement (scroll, conversion).

### 43. Strong H1 and introductions — High
- **Why:** the H1 confirms to users they've landed where they wanted; the introduction decides whether they stay.
- **How:** use a clear main heading and a logical heading hierarchy; one H1 is a useful authoring convention, not a search requirement. Align the heading with the page and user intent. Open with a 2–4 sentence introduction: direct answer or promise + who it's for + what they'll find.
- **Expected result:** few quick returns to the SERP (76).
- **Avoid:** filler openings ("In today's fast-paced world…"), competing main headings, the logo as H1.
- **Verify:** the auditor reports missing or multiple H1s as review prompts, not defects.

### 44. H2/H3 hierarchy — High
- **Why:** headings help scanning, help machines (including AIs extracting passages) understand structure, and can generate jump links in the SERP.
- **How:** H2 = main sections, H3 = subsections, no skipped levels. Descriptive headings, ideally phrased as a question or as a statement that summarises the section.
- **Expected result:** a readable outline from the headings alone.
- **Avoid:** using headings for visual styling (that's what CSS is for); generic headings ("Introduction", "More info").
- **Verify:** the auditor detects skipped levels.

### 45. Topic clusters (pillar + supporting pages) — High
- **Why:** demonstrates deep topical coverage and distributes internal authority.
- **How:** a broad pillar page on the topic (e.g. "E-invoicing for freelancers") linked to each specific supporting page ("E-invoicing deadlines by country", "How to issue a credit note"); each supporting page links back to the pillar and to relevant siblings with descriptive anchors. Reflect it in URLs or breadcrumbs when it makes sense.
- **Expected result:** the pillar ranks for the broad term, the supporting pages for the specific ones.
- **Avoid:** pillars that are just a list of links with no content of their own.
- **Verify:** cluster internal links with the auditor's `--crawl`.

### 46. Avoid keyword cannibalisation — High
- **Why:** if several of your URLs compete for the same intent, Google alternates between them and none consolidates.
- **How:** keep a **keyword → URL map** (54). Detect cannibalisation in Search Console: filter by query and check the Pages tab; if several URLs get impressions and the position fluctuates, merge into the strongest (301 the others), differentiate their intents, or adjust internal linking.
- **Expected result:** one stable main URL per intent.
- **Avoid:** confusing cannibalisation with having two results in the top 10 (that's good).
- **Verify:** after the change, one dominant URL per query in Search Console.

### 47. FAQ sections — Medium
- **Why:** they capture conversational and follow-up queries and provide passages AIs cite easily.
- **How:** include genuine customer questions when answering them improves the page. Keep answers accurate and concise. Add `FAQPage` structured data only if it accurately describes visible content and another current use case justifies it; do not assume a search feature benefit.
- **Expected result:** useful answers to real questions; search visibility is not guaranteed.
- **Avoid:** expecting FAQ rich results in Google Search; the feature stopped appearing on 7 May 2026. Also avoid invented questions stuffed with keywords.
- **Verify:** question-style queries in Search Console.

### 48. Table of contents — Medium
- **Why:** improves navigation in long articles, and Google **may** show "Jump to" links in the result.
- **How:** on articles longer than ~1,200 words, anchor links (`<a href="#section">`) to the H2s, with stable, readable `id`s on the headings.
- **Expected result:** better navigation; occasionally jump links in the SERP.
- **Avoid:** JavaScript-generated TOCs that don't exist in the HTML; random `id`s that change every build.
- **Verify:** the links work without JavaScript.

### 49. Trends — Medium
- **Why:** getting to an emerging topic before the competition lets you rank with little authority.
- **How:** Google Trends (compare and filter by country), Search Console (new queries with impressions), industry news, regulatory changes (deadlines, new laws). Publish a solid piece quickly and update it as things evolve.
- **Expected result:** traffic spikes and natural links.
- **Avoid:** trending topics unrelated to your business (traffic that doesn't convert and dilutes the site's topical focus).
- **Verify:** URL impressions in the following days.

### 50. Comparison and "alternatives" content — High
- **Why:** captures users in the decision stage.
- **How:** honest comparisons with explicit criteria, a summary table, who each option suits best, and a review date. If you compare against your own product, say so.
- **Expected result:** high-intent traffic and conversions.
- **Avoid:** self-promotional "best of" rankings where you always win and there's no methodology: Google has tightened its treatment of these lists and using them to manipulate AI answers falls under its spam policies; false claims about competitors can also be unlawful comparative advertising.
- **Verify:** assisted conversions from these pages.

### 51. "People also ask" questions — Medium
- **Why:** these are questions Google already associates with the query.
- **How:** collect them (manually or with tools), group them by intent, and answer them as H2/H3s where they fit the page. Adapt the wording to natural language; no need to copy them verbatim.
- **Expected result:** appearances in the PAA box and broader semantic coverage.
- **Avoid:** bolting 20 unrelated questions onto every page.
- **Verify:** new queries with impressions for those questions.

### 52. Glossaries — Low/Medium
- **Why:** capture informational searches ("what is X") and give internal links a destination for technical terms.
- **How:** a dedicated page per term only when the term has demand and supports a useful answer (definition + example + relation to your service); for the rest, a glossary index page with anchors. `DefinedTerm`/`DefinedTermSet` JSON-LD is optional.
- **Expected result:** rankings for "what is…" queries and natural internal linking.
- **Avoid:** hundreds of one-line pages (thin content, 26).
- **Verify:** glossary pages with impressions; if none after 6 months, merge them.

### 53. Micro-moments (know, go, do, buy) — Medium
- **Why:** each stage of the customer journey has different searches and formats.
- **How:** map each service or product to at least one piece per stage: know (guide), do (tutorial), go (location page with map and hours), buy (product or landing page with price and CTA). Link them in logical order.
- **Expected result:** full-funnel coverage.
- **Avoid:** mixing every stage into one page (see 78).
- **Verify:** navigation paths between those pages in analytics.

### 54. Keyword → URL map — Critical
- **Why:** it's the tool that prevents cannibalisation, gaps and pages without a purpose.
- **How:** a sheet or file (`docs/seo/keyword-map.csv` in the repo) with columns: URL, intent, primary keyword, secondary keywords, page type, cluster/pillar, status (planned, published, needs review), last review date. Each primary keyword appears **only once**.
- **Expected result:** every new page is born with a clear goal and doesn't compete with another.
- **Avoid:** maps nobody updates.
- **Verify:** quarterly review against Search Console.

### 55. Content brief before writing — High
- **Why:** writing without a brief produces generic text.
- **How:** for each URL: target query and intent, what the top 3 offer and what they lack, differentiating angle, H2/H3 outline, questions to answer, entities and terms that must appear (62), proprietary data or experiences to request from the business, inbound and outbound internal links, CTA, Schema, and an indicative length (whatever the intent needs, not a magic number).
- **Expected result:** differentiated content on the first attempt.
- **Avoid:** setting a word count as the goal: length is not a ranking factor.
- **Verify:** brief checklist completed before publishing.

---

## Advanced on-page and AI search

### 56. Title and meta description — Critical
- **Why:** the title is one of the most important on-page elements and, together with the description, drives the click.
- **How:** write a unique, descriptive title that accurately reflects the page; keep it concise, since display truncation depends on device and query (heuristic: the first ~50–60 characters usually display in full, so put the main topic first and the brand last). Write a useful, page-specific meta description as a possible snippet source; Google and Bing may instead generate a query-specific snippet from page content (heuristic: ~140–160 characters usually avoids truncation). Use templates only where they remain accurate and distinct.
- **Expected result:** clearer representation in results and a relevant reason to visit; neither CTR nor display is guaranteed.
- **Avoid:** duplicate or empty titles, keyword stuffing, titles that promise something the page doesn't deliver (Google rewrites them and users bounce).
- **Verify:** inspect title/description quality and duplicates during a crawl; compare Search Console CTR by page and query while accounting for position, demand and SERP changes.

### 57. Clean URLs — Medium
- **Why:** readable, more shareable, and they add some context.
- **How:** lowercase, words separated by hyphens, short, no dates for evergreen content, no parameters for indexable content, in the content's language. Hierarchy when it helps (`/services/web-development`).
- **Expected result:** URLs that stay stable over time.
- **Avoid:** changing URLs that already rank just to "optimise" them (you lose more than you gain; if you must, 301 per 23); excessive stop words or kilometre-long URLs.
- **Verify:** the auditor flags uppercase, underscores and parameters in internal URLs.

### 58. Images: file names and alt text — Medium
- **Why:** Google Images and Lens are traffic sources; `alt` is accessibility and context.
- **How:** descriptive file names (`body-jet-repair-valencia.webp`), `alt` that describes the image in context (not a keyword list), images near the related text, real `<img>` elements (not CSS `background-image` for content images). Include important images in the sitemap if they load in a non-standard way.
- **Expected result:** images indexed and Google Images traffic.
- **Avoid:** empty `alt` on informative images; `alt="image"`; images containing important text with no text alternative.
- **Verify:** the auditor counts images without `alt`.

### 59. Structured data (Schema) — High
- **Why:** structured data describes page entities and can make eligible pages qualify for supported search features.
- **How:** JSON-LD in the served HTML, with types that describe visible page content and follow the current eligibility rules of each search feature. Common choices: `Article`/`BlogPosting` (author as a `Person`, `datePublished`/`dateModified`), `Product` + `Offer` (`AggregateRating` only with genuine reviews of that product), `BreadcrumbList`, `LocalBusiness`, `Event`, `JobPosting`, `VideoObject`. Structured data does not guarantee display or ranking.
- **Expected result:** valid markup and eligibility for supported search features where applicable.
- **Avoid:** expecting rich results from unsupported or retired features, or marking up content that is false, misleading, or not representative of visible page content.
- **Verify:** the auditor validates that JSON-LD is valid JSON and lists the types; Rich Results Test and validator.schema.org.

### 60. Featured snippets — Medium
- **Why:** featured snippets can give a page prominent presentation for some queries; selection is controlled by Google and can change.
- **How:** under a heading that states the question, answer accurately and directly (a starting heuristic is 40–60 words), then expand; use a list or table when that format serves the user. Do not force a word count or assume a featured snippet format predicts AI citations.
- **Expected result:** content that's clear and useful; featured snippet selection is not guaranteed.
- **Avoid:** ambiguous answers that depend on the previous paragraph to make sense.
- **Verify:** manual search for the query; Search Console.

### 61. Optimise for AI search (GEO) — High
- **Why:** generative search products may show links, citations, or summaries, but their retrieval and reporting differ and continue to change.
- **How:** identify the actual product and its crawler/access policies (37 and `engines/`). Then the foundations: indexable and well-ranked pages are the usual retrieval pool; content available in the served HTML without JavaScript (25); clear answers early (64); self-contained, sourced passages (69); visible authorship (102); Bing presence for Copilot (5, `engines/bing.md`). Monitor first-party reporting where it exists (Bing AI Performance, Search Console). The full AI layer — access-to-citation funnel, per-platform controls, evidence table and measurement protocol — is `engines/ai-search.md` (A1–A18). See `references/research-method.md` before making claims about AI visibility.
- **Expected result:** a technically accessible, useful site; citations and referral visits are uncertain outcomes, not deliverables.
- **Avoid:** promising citations or traffic from formatting alone, assuming classic rank is always required for retrieval, or using hidden instructions and deceptive bot-specific content.
- **Verify:** 148 (AI visibility monitoring).

### 62. Cover related entities and concepts — High
- **Why:** search engines understand topics and entities, not just strings; a complete page mentions what an expert would mention.
- **How:** list the subtopics, entities (organisations, regulations, brands, places, people) and terms that appear in the best pages and in real questions; cover them where they add value. Link to authoritative sources for key entities (88).
- **Expected result:** rankings for many variants without creating new pages.
- **Avoid:** forced "LSI keyword" lists (LSI as applied to Google is a myth).
- **Verify:** number of distinct queries with impressions per URL in Search Console.

### 63. Natural language — Medium
- **Why:** queries are increasingly long and conversational; natural text reads better and gets cited more.
- **How:** clear sentences, active voice, second person where it fits, the customer's vocabulary (not only the technical one), answers that sound right read aloud.
- **Expected result:** better readability and engagement.
- **Avoid:** repeating the exact-match keyword unnaturally.
- **Verify:** read it aloud; user feedback.

### 64. Inverted pyramid — High
- **Why:** the user (and the AI) gets the answer immediately; whoever wants more keeps reading.
- **How:** first sentence = answer; then nuances, detail, examples and context.
- **Expected result:** fewer returns to the SERP and more citations.
- **Avoid:** delaying the answer to "increase time on page" (the user goes to another result).
- **Verify:** scroll maps (110).

### 65. Ordered lists for processes — Medium
- **Why:** numbered steps are easy to follow, extract and cite.
- **How:** an `<ol>` with one step per item, each starting with a verb, prerequisites before the list and expected outcome after.
- **Expected result:** list snippets in the SERP and in AI answers.
- **Avoid:** lists built from paragraphs with hand-typed numbers or `div`s.
- **Verify:** semantic HTML in the source.

### 66. No filler — High
- **Why:** Google's quality systems (the "helpful content" system became part of the core algorithm in 2024) assess whether content is made for people or for search engines.
- **How:** remove generic intros, repetition, obvious definitions and paragraphs that answer nothing. Every section should answer a specific question.
- **Expected result:** shorter, more useful text.
- **Avoid:** padding to reach a word count.
- **Verify:** every H2 answers a question identifiable in the brief.

### 67. No hidden content or cloaking — Critical
- **Why:** it's a direct violation of spam policies and can lead to manual actions.
- **How:** content in tabs, accordions or "read more" **is allowed** and gets indexed if it's in the HTML. What's forbidden is hiding text or links to manipulate (same colour as background, zero font size, off-screen) and showing bots something different from users.
- **Expected result:** no manual actions.
- **Avoid:** cloaking aimed at AI crawlers too (37).
- **Verify:** "Manual actions" in Search Console.

### 68. AI-generated content: review and original value — Critical
- **Why:** Google doesn't penalise content because AI wrote it; it penalises low-value content. Mass-publishing pages to capture searches without review is *scaled content abuse*, one of its spam policies.
- **How:** AI (including you) produces drafts; the business contributes and validates data, experience, examples and opinion. Fact-check every figure and claim. A sustainable publishing pace. A real, accountable author (102).
- **Expected result:** content an expert would put their name to.
- **Avoid:** generating hundreds of programmatic pages (city × service) with the same text and the name swapped; publishing without review.
- **Verify:** sample pages: does it add anything that isn't already in the top 10?

### 69. Be citable by AI — High
- **Why:** clear, specific, verifiable passages are easier for readers and systems to interpret and attribute. *Confidence: Supported as editorial practice; a Hypothesis as a citation lever* — benchmarks found many rewriting tactics ineffective, and early research suggests retrieval matters more than page features (`engines/ai-search.md`, evidence table).
- **How:** one idea per paragraph; name the subject in each passage (not "this", "the above"); figures with unit, date and source; "X is…" definitions; HTML comparison tables; a visible "updated on" date matching `dateModified`; an "About" page and authorship that let readers verify who is speaking; original data (surveys, proprietary statistics, prices) that exists nowhere else (89).
- **Expected result:** information that's easier for readers and systems to interpret; citations remain outside the publisher's control.
- **Avoid:** "nobody's opinion" content with no data and no author.
- **Verify:** 148.

### 70. Hero image and LCP — High
- **Why:** on most pages the LCP element is an image; it is also the image Google and social networks use as a thumbnail.
- **How:** hero image served as AVIF/WebP with `srcset`/`sizes`, `fetchpriority="high"`, not lazy, dimensions declared, served from your domain or CDN. A 1200×630 `og:image` for social and, for Discover, images at least 1200 px wide with `max-image-preview:large`.
- **Expected result:** LCP < 2.5 s and correct thumbnails on Google, Discover and social.
- **Avoid:** full-screen carousels as the LCP element; 4000 px images served to phones.
- **Verify:** the auditor checks `og:image`, `fetchpriority` and lazy loading on the first image.

### 71. E-commerce: product pages and Merchant Center — High (if you sell online)
- **Why:** free Google Shopping listings, rich product results (price, availability, shipping, returns) and the Shopping tab are a major source of transactional traffic.
- **How:** `Product` + `Offer` (price, currency, availability, `shippingDetails`, `hasMerchantReturnPolicy`) on every product page; Google Merchant Center with a feed or automatic crawling; unique titles and descriptions (not the manufacturer's); out-of-stock handling (keep the URL marked "out of stock" if it will return; 301 to a substitute or 404 if not).
- **Expected result:** product results with price and availability in the SERP; products on Shopping.
- **Avoid:** Schema prices that don't match the visible ones (Merchant Center suspends the account); manufacturer descriptions copied across thousands of products.
- **Verify:** "Product snippets" and "Merchant listings" reports in Search Console.

---

## User experience and engagement

### 72. User satisfaction, not "dwell time" — High
- **Why:** Google confirmed in the US antitrust trial that it uses interaction signals with results (clicks, returns to the SERP) in its ranking systems; what matters is that the user ends up **satisfied**, not that they spend more time (a quick, correct answer is also a success).
- **How:** videos, infographics, calculators or tables **when they help solve the task**, not as filler to retain people.
- **Expected result:** fewer returns to the SERP and more conversions.
- **Avoid:** tricks to inflate time (unnecessary text before the answer, autoplay videos).
- **Verify:** engagement rate and conversions in analytics.

### 73. Interstitials and pop-ups — High
- **Why:** "bounce rate" isn't a ranking factor (GA4 now uses engagement rate instead), but intrusive mobile interstitials are a negative page-experience signal and drive users away.
- **How:** no pop-ups covering content on arrival from search; if you need them (newsletter), show them after interaction or on exit intent, small and easy to dismiss. Legally required notices (cookies, age verification) are allowed.
- **Expected result:** the user sees the content they expected instantly.
- **Avoid:** full-screen pop-ups on load on mobile.
- **Verify:** test on a phone from a Google result.

### 74. Readable typography and white space — Medium
- **Why:** easier reading, especially on mobile.
- **How:** body text ≥ 16 px, line height 1.5–1.7, 60–80 characters per line on desktop, 2–4 line paragraphs, frequent subheadings, sparing bold.
- **Expected result:** deeper reading.
- **Avoid:** light grey text on white.
- **Verify:** Lighthouse (legible font sizes); scroll maps.

### 75. Internal calls to action — High
- **Why:** SEO traffic only matters if it leads somewhere: another relevant page or a conversion.
- **How:** one primary CTA per page that matches intent (informational → related content or lead magnet; transactional → buy or request a quote); "read next" links at the end; CTA visible without scrolling on transactional pages.
- **Expected result:** more pages per session and more organic conversions.
- **Avoid:** five CTAs competing with each other.
- **Verify:** conversions by organic landing page.

### 76. Prevent pogo-sticking — High
- **Why:** bouncing straight back to the SERP to pick another result signals the page didn't solve the need.
- **How:** the first thing visible confirms the search (H1 consistent with the title) and starts solving it; fast loading; no interstitials; no clickbait titles.
- **Expected result:** stable or rising positions.
- **Avoid:** titles that promise more than the page delivers.
- **Verify:** engagement of organic sessions by landing page.

### 77. Intuitive navigation menu — Medium
- **Why:** distributes internal authority to key pages and helps users find their way.
- **How:** 5–7 main items reflecting what users search for most and what the business sells most; crawlable HTML links; a footer with secondary, legal and contact links; the same menu on mobile.
- **Expected result:** menu pages are the most internally linked.
- **Avoid:** mega menus with hundreds of links; menus that only exist after JavaScript runs.
- **Verify:** `curl` shows the menu links.

### 78. Separate learning from buying — High
- **Why:** each intent needs its own page; mixing them weakens both.
- **How:** informational guides that link to the commercial page; commercial pages focused on benefits, price, social proof and CTA, with a link to the guide for those who need more context.
- **Expected result:** each page ranks for its intent and converts better.
- **Avoid:** blog posts plastered with sales banners.
- **Verify:** keyword map (54) with each URL's intent.

### 79. Useful interactive elements — Medium
- **Why:** tools, calculators and configurators earn links, repeat use and differentiation.
- **How:** only when they solve a real need (price calculator, payment simulator, eligibility check). Make sure the result and a text explanation are also in indexable HTML; mobile-friendly and accessible.
- **Expected result:** natural links and conversions.
- **Avoid:** heavy widgets that tank INP.
- **Verify:** tool usage in analytics; the page's INP.

### 80. Contrast and visual hierarchy — Medium
- **Why:** accessibility and readability.
- **How:** WCAG AA contrast (4.5:1), a clear size hierarchy, distinguishable link colour, buttons that look like buttons.
- **Expected result:** no contrast errors in Lighthouse/axe.
- **Avoid:** text over images without a contrast overlay.
- **Verify:** Lighthouse Accessibility.

### 81. Dark mode — Low
- **Why:** a comfort feature, **not an SEO factor**. Add it only if it suits the audience and design.
- **How:** `prefers-color-scheme` with CSS variables; no flash on load (theme resolved before first paint).
- **Expected result:** comfort for those who use it.
- **Avoid:** prioritising it over anything else in this guide.
- **Verify:** no CLS or flash when loading in dark mode.

---

## Internal linking and content curation

### 82. Strategic internal linking — Critical
- **Why:** it's the most under-used SEO lever and the one you fully control: it distributes authority and tells search engines which pages matter and what they're about.
- **How:** every new page gets links from 3–5 relevant, already-ranking pages (find them in Search Console by impressions); descriptive, varied anchors ("e-invoicing guide", not "click here"); links in the body content, not only in menus or footers.
- **Expected result:** new pages indexed sooner and ranking faster.
- **Avoid:** always using the same exact-match anchor; `nofollow` on internal links.
- **Verify:** the auditor's `--crawl` shows internal inbound links per URL.

### 83. Modular content — Low/Medium
- **Why:** data that changes (prices, deadlines, requirements) stays consistent when updated in one place.
- **How:** reusable components or blocks fed by a single source (CMS, JSON, database), rendered on the server.
- **Expected result:** consistency and easy updates.
- **Avoid:** the shared block becoming **most** of the content on many pages (near-duplicate content).
- **Verify:** every page keeps unique main content.

### 84. Prune zombie content with judgement — Medium
- **Why:** pages with no traffic or value dilute site quality, but deleting blindly destroys links and conversions.
- **How:** with 12 months of data (Search Console + analytics + external links): **improve** if the topic has demand; **merge** with a 301 if there's overlap; **noindex** if it's useful for users but not for search; **delete** (404/410) only if it has no traffic, links, conversions or function.
- **Expected result:** fewer URLs, same or more visits.
- **Avoid:** deleting new pages (give them 6–12 months) or pages that convert despite low traffic.
- **Verify:** total site traffic three months after pruning.

### 85. Real reviews — High
- **Why:** reviews build trust, add original content and drive conversions.
- **How:** collect verifiable reviews (Google Business Profile, third-party platforms, verified buyers); display them on the site stating their source; use `AggregateRating`/`Review` only on **product** pages (or pages about a specific item) with reviews from customers of that item.
- **Expected result:** useful trust and product feedback; a review rich result is eligible only when it meets current engine rules and is never guaranteed.
- **Avoid:** fabricated reviews or unsupported claims about verification. Consumer-protection rules differ by jurisdiction; check current local requirements (for example, [EU law](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L2161), [UK CMA guidance](https://www.gov.uk/government/publications/fake-reviews), or the [US FTC rule](https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers)). Google's [review snippet policy](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) excludes self-serving reviews for `Organization`/`LocalBusiness`.
- **Verify:** "Review snippets" report in Search Console.
