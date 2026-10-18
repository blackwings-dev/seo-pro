# News and publishers layer (practices P1–P20)

Covers newsrooms, magazines, local media and digital publications on Google Search (web results, Top Stories, the News tab), Google News (news.google.com and apps), Discover, Bing / Microsoft surfaces, and AI answers that cite journalism. Includes breaking news, live coverage, service journalism, analysis and evergreen; sections, article pages, paywalls, syndication, images, sitemaps and measurement. Read `README.md` in this folder first; it extends core practices 2, 22, 59, 102–103, 146, 147 and 160, Bing B2 and B23, and AI A2–A6.

Research snapshot: **18 October 2026**. Publisher Center, Discover policies and AI controls change often; re-check the official links at the end before changing paywall, crawler or sitemap behaviour.

**The thesis.** Publisher SEO is the coordination of original, reliable journalism; crawlable, transparent pages; correct technical distribution; and an audience model that doesn't depend on one platform. Success isn't measured only in clicks: returning readers, registrations, subscriptions, trust and editorial value count too. A corporate blog doesn't become a news publisher by calling itself one.

Format: **Why** · **How** · **Expected result** · **Avoid** · **Verify**, with confidence labels from `../research-method.md` where evidence is mixed.

## Contents
- Surfaces and the discovery funnel
- Editorial policy and trust: P1–P6
- Architecture and technical SEO: P7–P11
- Google News, News sitemaps and markup: P12–P14
- Discover: P15
- Paywalls and monetisation: P16–P17
- Bing and AI answers: P18–P19
- Measurement: P20
- Publisher myths · 90-day sequence · checklist · sources

---

## Surfaces and the discovery funnel

| Surface | Experience | What it can bring | How to measure |
|---|---|---|---|
| Google Search web results | Active search: news, primary source, analysis, guide | Direct clicks per query and page | Search Console Performance (Web) |
| Top Stories / news features | Coverage blocks for news-intent queries | Temporary visibility and clicks | Search Console + SERP checks; not a stable web ranking |
| News tab in Search | Results in Search's News tab | News-search clicks and impressions | Search Console Performance, search type **News** |
| Google News app / news.google.com | Aggregated, personalised news | Readers in the News product, returns, subscriptions | Search Console **News** report (doesn't include the Search News tab) |
| Google Discover | Interest-based feed, no query | Incremental reach, often spiky | Search Console **Discover** report |
| Bing / Microsoft surfaces | News in Bing, Microsoft Start, Edge | Another ecosystem's discovery | Bing Webmaster Tools + own analytics; **PubHub is retired** |
| AI answers | Conversational summaries with possible citations | Mention, citation, referral, or use without a visit | Labelled referrals, logs, query panel (A14–A16); incomplete data |

Funnel: discovery → crawl → index → eligibility → selection on the surface → impression → click → reading/return → registration/subscription/revenue. Improving one step doesn't guarantee the next; a mention without a click isn't a visit, a visit without reading isn't attention, an impression isn't revenue.

---

## Editorial policy and trust

### P1. Visible identity and accountability — Critical · *Established (Google News policies)*
- **Why:** Google News policies ask for clear dates and bylines; information about authors, the publication and the publisher; the company or network behind it; and contact details. Readers need the same to judge trust.
- **How:** maintained pages for: who we are, ownership and funding; authors, editors and contributors with truthful profiles (102); standards, methodology and corrections policy; newsroom contact, corrections and right of reply; sponsored content, affiliate and conflicts of interest; editorial use of AI and human controls where relevant; privacy and cookies. Bylines may be a person, team, agency or correspondent, described accurately.
- **Avoid:** fictitious authors, an empty "About us", attributing authorship to a journalist who didn't take part.
- **Verify:** from any article, a reader reaches author, publisher, policies and contact in one or two clicks.

### P2. Dates, updates and corrections — Critical
- **How:** publication date and time where relevant, with a clear time zone for live events. On substantive change, show an update time and what changed; keep `datePublished` as the original and use `dateModified` for real changes (147). Important corrections are visible and explain the error without erasing the history. In developing stories, separate the new fact from earlier information and keep old headlines from contradicting the current state.
- **Avoid:** changing dates without substantive edits — it misleads people and systems.
- **Verify:** dates agree across visible page, `NewsArticle` markup and sitemap.

### P3. Headlines and previews that keep their promise — High
- **How:** the headline states the news and its core fact. `<title>`, H1, social metadata and the visible headline stay coherent; justified editorial differences are fine, four contradictory versions aren't. Discover's policies ask you to avoid titles and images that exaggerate, hide essential context or exploit outrage.
- **Avoid:** clickbait, keyword stuffing, truncated or ambiguous headlines, headline changes that alter the fact. CTR helps diagnose; it never justifies inaccuracy.

### P4. Originality, attribution and syndication — High
- **How:** distinguish original reporting from wire copy, summaries, translations, press releases, licensed and republished content. Attribute sources, links, images and documents clearly. For full-article syndication, agree with partners whether the republished copy should be blocked from indexing so the original can be identified (per Google News guidance). Don't keep several identical URLs on the same domain without editorial need.
- **Avoid:** incremental rewrites of someone else's story or a press release with minimal changes as a substitute for reporting.

### P5. Images and media — High
- **How:** images directly related to the story, with rights and credits. For Discover: large images at least **1,200 px wide**, more than 300,000 px in total, and `max-image-preview:large` to be eligible for a large preview (no guarantee); Google reads both schema.org image markup and `og:image`. Verify framing, context, captions, authorship, and labels for synthetic or manipulated imagery when policy requires. Video, audio, galleries and charts get an accessible page with context, transcript or description (146).
- **Avoid:** generic logos as the article image; relying on Google to interpret a video or social post without the journalism around it.

### P6. Preferred sources and direct relationship — Medium · *Established feature; impact varies*
- **Why:** Google's **Preferred sources** lets users choose outlets to see more of in Top Stories (documented January 2026; all Search languages since April 2026; also in AI Overviews and AI Mode since May 2026). Google publishes instructions for a "set as preferred source" button.
- **How:** offer the preferred-source button where it fits the audience; build owned channels (newsletter, push, app, registration) so the relationship doesn't depend on one platform.
- **Avoid:** dark patterns pushing users to add you; treating the button as a ranking lever.
- **Verify:** track usage of the button and owned-channel growth, not just Search clicks.

---

## Architecture and technical SEO

### P7. Stable sections and crawlable links — Critical
- **How:** stable sections by editorial area, topic, region and format; articles linked from home, sections, related topics and explainers with real `<a href>` (25). Google News notes that changing section URLs makes it harder to identify what's new. Illustrative pattern (stability matters, not the template): `/country/topic/` → `/country/topic/article-slug/` → `/author/name/` → `/topics/entity/`.
- **Avoid:** links only inside JavaScript, buttons or text-less images.

### P8. One permanent URL per article — Critical · *Established (Google News technical guidelines)*
- **How:** a unique, permanent URL per article; headline and publication time recognisable; body visible to crawlers without JavaScript (127). Don't republish each update under a new URL: a stable URL keeps links, shares, references and correction history.
- **Verify:** `curl -s URL` shows headline, date and body.

### P9. Breaking news and live blogs — High
- **How:** a permanent URL for the live page, readable content in clear chronological order, a time on every update, the opening clearly separated from later updates, links to background, primary sources and the rest of the coverage. Publish a **new** piece only when there's a new editorial need, linking both ways.
- **Avoid:** a new URL for every short update; rewriting the same article as if each edit were a new event.

### P10. Canonicals, duplicates and archives — High
- **How:** coherent canonicals for print versions, parameters, mobile, legacy AMP, republications and newsletter formats. Tag and author archives are indexable only when they're useful, unique and maintained pages; a list of repeated headlines may not deserve indexing (26). Consistent policy for section pagination, author aggregates and topics (22).
- **Avoid:** canonicalising a story to the home or a category; indexable internal search and infinite tag combinations.

### P11. Publisher migrations — Critical
- **How:** follow the migration playbook (`../playbooks/migrations.md`) and, for publishers specifically, preserve authorship, dates, canonicals, pagination and article routes; decide for live pages and archives whether they keep their URL, are archived or consolidated; keep News sitemaps and internal links current. Rights policies may limit availability of some pages.
- **Avoid:** combining CMS change, redesign, editorial merger, paywall change and URL change in one release.

---

## Google News, News sitemaps and markup

### P12. Google News needs no "approval" — High · *Established*
- **Why:** Google says publishers don't need to submit their site to be eligible for Google News surfaces: content is discovered through Search technology and policy compliance is considered. Since **March 2025** Google News generates publication pages automatically and no longer uses the sections, RSS feeds and web locations configured in Publisher Center for that. Publisher Center keeps specific functions (e.g. News Showcase, Reader Revenue Manager); it isn't a CMS or a ranking lever.
- **How:** focus on crawlability, policies, transparency (P1), article pages (P8) and original coverage; check crawl and indexing in Search Console. Use Publisher Center only for the functions you actually need.
- **Avoid:** spending effort on an "approval" process or on old Publisher Center section setups.

### P13. News sitemap: discovery, not inclusion — High · *Established*
- **How:** a News sitemap (inside the general sitemap or separate; separate is easier to monitor) with only articles created in the **last two days** in the News fields; update the same file as you publish rather than generating a new sitemap per change; drop News metadata from older articles while keeping their URLs in the general sitemap; publication name and language exactly as the spec defines; submit in Search Console and watch errors. At scale, validate the XML automatically and diff it against the published inventory.
- **Avoid:** listing `noindex`, 404, redirected or canonicalised-elsewhere URLs; using the sitemap to refresh dates or relaunch old content. Google crawls News sitemaps at the same rate as the rest of the site.
- **Verify:** Search Console Sitemaps report; the auditor's sitemap checks.

### P14. `NewsArticle` / `Article` markup is descriptive — Medium · *Established: not required for Top Stories*
- **How:** declare `headline`, `image`, `datePublished`, `dateModified` and `author` (real people with `url`) matching the visible article. Google says there is **no structured-data requirement** for Top Stories eligibility; markup helps understanding and presentation.
- **Avoid:** markup that disagrees with the page; expecting rich results from it.
- **Verify:** Rich Results Test; served vs rendered HTML.

---

## P15. Discover: opportunity with variance — High · *Supported; outcomes volatile*
- **Why:** Discover is personalised by activity and interests, can show older content that's still relevant, and can't be scheduled. Google's **February 2026 Discover core update** (from 5 Feb 2026, US English first, other markets later) aims to show more content from sites in the user's country, reduce sensationalism and clickbait, and favour in-depth, original, timely content from sites with expertise in the topic.
- **How:** timely, well-told or original stories; titles and previews faithful to the article (P3); a large relevant image and `max-image-preview:large` (P5); identifiable author, publisher and dates; respect Discover's content policies; analyse by topic, audience, device, date and article type.
- **Diagnosis when Discover drops:** check together technical errors and template changes; topic, competition, seasonality and publishing volume; title and image quality; policies, manual actions and security; distribution across landings; Discover vs Search data kept separate. A spike and a drop alone don't prove a penalty.
- **Avoid:** promising Discover traffic; turning every story into high-emotion content because the surface is personalised.

---

## Paywalls and monetisation

### P16. Paywalls without accidental cloaking — Critical
- **How:** make clear to readers what's free and what needs access. Mark paywalled content with Google's current paywall structured data (`isAccessibleForFree`, `hasPart` with `cssSelector` for the gated section) so it's distinguished from cloaking. Choose the model deliberately (metered, freemium, registration, hard paywall, membership, B2B licence): the SEO treatment depends on access policy, preview value, allowed indexing and consent.
- **Avoid:** serving Googlebot the full article and users a completely different page without paywall markup.
- **Verify:** Rich Results Test on gated articles; compare user and crawler views.

### P17. Sponsored, affiliate and commercial content — High
- **How:** distinguish editorial, sponsored, affiliate, syndicated and user-generated content visibly; qualify paid links (`rel="sponsored"`, 101). Google News prohibits presenting sponsored content as independent journalism without clear disclosure, and promotional content mustn't outweigh editorial on those pages.
- **Avoid:** hosting third-party pages in editorial sections to exploit the outlet's reputation — Google's **site reputation abuse** policy targets exactly that (`../playbooks/reputation.md` R9).

---

## Bing and AI answers

### P18. Bing: PubHub is retired — High · *Established*
- **Why:** Microsoft has retired Bing News PubHub (announced 2025): it no longer accepts submissions, and Bing News relies on automated discovery evaluating authority, originality, relevance, freshness, location and language.
- **How:** verify the site in Bing Webmaster Tools (B1); keep sitemaps and internal links correct; send new and updated URLs via IndexNow (B2); use Open Graph for article thumbnails; monitor clicks and impressions in BWT and AI Performance (B9).
- **Avoid:** old tutorials telling you to "submit to PubHub"; assuming IndexNow guarantees Microsoft Start or Bing News presence (it signals change, nothing more).

### P19. Crawler and licensing decisions for AI — High
- **How:** decide separately per operator for **search**, **training**, **user fetch** and **licensing** (A2), with editorial, legal, distribution, product and engineering at the table. Google Search features follow Google Search controls (A3); `Google-Extended` doesn't affect Search. ChatGPT search uses `OAI-SearchBot`, Perplexity `PerplexityBot`, Claude `Claude-SearchBot`. Log bots, verify IPs, separate human visits from crawls, and track volume, cost and rights.
- **Avoid:** blocking Googlebot to stop a training crawler; treating a citation as a visit or a licence. Evidence on AI referrals is growing (e.g. a preregistered August 2026 field experiment with 1,100 participants found AI Overviews/AI Mode reduced clicks to publishers in its setting — a **preprint**, not consensus); measure your own.

---

## P20. Measurement for publishers — High

Search Console reports are separate and must not be summed blindly: **Search Performance** (with search type *News* for the News tab), **News Performance** (news.google.com and the Google News apps; excludes the Search News tab) and **Discover Performance**.

| Goal | Suggested metrics |
|---|---|
| Discovery | URLs crawled/indexed; time from publication to first impression; undiscovered pages |
| Search presence | Clicks/impressions by query type, article, section, country, device |
| News / Top Stories | News Performance; Search type News; documented test queries |
| Discover | Impressions, clicks, CTR, pages, topic, format, image, time cohorts |
| Audience quality | Engaged reading (well-defined), returns, multi-article sessions, newsletter/push opt-in |
| Subscription | Registration, conversion, churn, retention, LTV, search-assisted contribution |
| Revenue | Revenue per session, ad yield, subscription, clearly labelled affiliate, licensing |
| Resilience | Share of direct/owned audience vs search, social, aggregators and chatbots |
| Integrity | Corrections, right-of-reply requests, broken links, complaints, manual actions, duplicates |

- **How:** group by story type (breaking, service, live, analysis, opinion, explainer, evergreen, local, sport, finance, culture) and compare **life cycles**, not just day one. Join with the measurement playbook (`../playbooks/measurement.md`).
- **Avoid:** dashboards that reward volume and speed at the expense of verification; crediting SEO for a viral story or an editorial campaign.

---

## Publisher myths

| Claim | Assessment | Prudent alternative |
|---|---|---|
| "We must apply for Google News approval" | Outdated: no submission needed; Publisher Center changed in 2025 | Indexing, policies, transparency, structure (P12) |
| "`NewsArticle` is required for Top Stories" | Google says there's no markup requirement | Use it as descriptive data, validated (P14) |
| "A News sitemap forces inclusion" | It helps discover recent URLs; guarantees nothing | Keep it correct and linked (P13) |
| "Publishing daily makes Discover stable" | Personalisation and demand make it volatile | Diversify, measure, focus on faithful stories (P15) |
| "Changing the date makes Google treat it as new" | Misleading; not a substantive update | Keep the original date; declare real changes (P2) |
| "Republishing every wire story adds SEO URLs" | Duplicates, can hide the original or cannibalise | Add editorial value or handle syndication with partners (P4) |
| "Submit to Bing PubHub" | PubHub is retired | BWT + sitemaps + IndexNow (P18) |
| "An AI citation equals a visit or a licence" | It may produce no click; crawling isn't licensing | Separate citation, referral, contract and revenue (P19) |
| "News SEO is dead" | Distribution changes; search and news surfaces still drive discovery | Treat Search as important, not exclusive |
| "News SEO is about keywords" | Context, relevance, freshness, authority and usefulness matter more | Reporting, structure, transparency, technique, reader experience |

## 90-day sequence (no growth guarantee)

- **Days 1–15 — inventory and baseline:** sections, templates, articles, authors, archives, content types, paywall; separate metrics for Search, News, Discover, Bing, social, email and direct; review News and general sitemaps, robots, canonicals, structured data and logs.
- **Days 16–35 — remove blockers and ambiguity:** fix non-permanent URLs, unreadable content, inaccessible links and ambiguous dates; strengthen transparency pages, profiles, policies and disclosures; validate paywall, canonical/syndication and bot status with stakeholders; remove PubHub and "Google News approval" steps from the process.
- **Days 36–60 — editorial experience and distribution:** linking between sections, context pieces, features and live coverage; standards for headlines, dates, corrections, images and markup; News sitemap and IndexNow if they fit; a pilot for Discover/newsletter/registration without mass simultaneous changes.
- **Days 61–90 — measure value and diversify:** compare by story type, topic, channel and cohort; review AI referrals, crawls, cost, citations and licensing decisions; analyse returning and converting readers; document nulls and adverse effects; set a quarterly review of platform policies.

## Executive checklist

- [ ] Search, Google News, Top Stories, Discover and Bing/Microsoft are distinguished.
- [ ] No dependence on an obsolete approval or on retired PubHub.
- [ ] Stable section URLs; unique, permanent article URLs.
- [ ] Articles and headlines readable in HTML and linked with `<a href>`.
- [ ] Dates and bylines clear, correct and consistent between page and markup.
- [ ] Real information about authors, publisher, company, contact and policies.
- [ ] Sponsorship, affiliate, syndication and commercial material identified.
- [ ] Corrections and substantive changes explained without rewriting history.
- [ ] News sitemap respects the two-day window and updates correctly.
- [ ] Paywall markup and crawler access reflect the chosen editorial/legal policy.
- [ ] Discover images relevant, large and faithful; no clickbait.
- [ ] Search, News, Discover, Bing, AI referrals and owned traffic reported separately.
- [ ] Success includes returning readers, conversion, trust and revenue.
- [ ] No volume incentives that weaken verification or corrections.

## Sources

Google (level A): [Help Google News discover your content](https://support.google.com/news/publisher-center/answer/9606634) · [Google News policies](https://support.google.com/news/publisher-center/answer/6204050) · [Technical guidelines](https://support.google.com/news/publisher-center/answer/9606708) · [Automatic publication pages](https://support.google.com/news/publisher-center/answer/15898024) · [Google News ranking](https://support.google.com/news/publisher-center/answer/9607025) · [Content that must be blocked from Google News](https://support.google.com/news/publisher-center/answer/9520026) · [News sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap) · [Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article) · [Discover and your website](https://developers.google.com/search/docs/appearance/google-discover) · [February 2026 Discover core update](https://developers.google.com/search/blog/2026/02/discover-core-update) · [Paywalled content](https://developers.google.com/search/docs/appearance/flexible-sampling) · [News Performance report](https://support.google.com/news/publisher-center/answer/10252664) · [Search documentation updates (preferred sources, Discover images)](https://developers.google.com/search/updates) · [News Showcase](https://support.google.com/news/publisher-center/answer/10018888).

Microsoft (level A/B): [PubHub guidelines page (retirement notice)](https://www.bing.com/webmasters/help/pubhub-publisher-guidelines-32ce5239) · [PPC Land on the PubHub retirement](https://ppc.land/microsoft-retires-bing-pubhub-submission-platform/) · [Sitemaps in AI-powered search](https://blogs.bing.com/webmaster/2025/7/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search/) · [AI Performance preview](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/).

Audience and AI research (levels B–D): [Reuters Institute Digital News Report 2026](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary) (survey of declared habits; social and video networks overtook other sources for the first time) · [Spain, DNR 2026](https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/spain) · [Trends and predictions 2026](https://reutersinstitute.politics.ox.ac.uk/journalism-media-and-technology-trends-and-predictions-2026) · [Wang et al., AI in Search Reduces Publisher Referrals (arXiv preprint, Aug 2026)](https://arxiv.org/abs/2608.18352) · [SPJ Code of Ethics](https://www.spj.org/ethicscode.asp).
