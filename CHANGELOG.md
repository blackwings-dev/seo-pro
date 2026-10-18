# Changelog

## 1.4.0 — 2026-10-19

Measure what the skill used to only recommend: server logs, field Core Web Vitals and JavaScript rendering — and keep the sources from going stale.

- New `scripts/crawl_logs.py` 1.0.0 (dependency-free): reads Apache/Nginx combined or common logs, IIS/W3C and JSON lines (Cloudflare Logpush, Vercel, Fastly), `.gz` included. Recognises about 35 search, AI and SEO-tool crawlers; verifies Google, Bing, OpenAI, Anthropic, Perplexity and Apple bots against the operators' published IP-range files (cached daily, `--ranges-dir` for offline use) or by reverse + forward DNS; reports impostors apart. Per bot: hits, status codes, sections, most-crawled URLs, parameters, daily trend and crawl spent on redirects, errors and parameter URLs; AI agents by purpose; sitemap URLs Googlebot never fetched (`--sitemap-urls`).
- `search_data.py` 1.1.0: `crux` (Chrome UX Report API: p75 LCP, INP, CLS, FCP and TTFB per URL or origin and form factor, good share, pass/fail, `--fallback-origin`, weekly `--history`) and `psi` (PageSpeed Insights field data with origin fallback plus one lab run: performance score, LCP, CLS, TBT).
- `seo_audit.py` 1.4.0: `--render` loads each page in headless Chromium (optional Playwright) and reports what only exists after JavaScript — text, internal links, title, description, canonical, robots, H1 and JSON-LD — and client-side redirects; `--html` writes a self-contained report with a "fix first" list, filterable findings, light and dark themes. Fix: a relative `Sitemap:` line in robots.txt crashed the audit; it is now reported and resolved.
- New `tools/check_skill.py`: practice IDs cited vs defined (references and the scripts' findings), backticked paths, relative links, table columns, SKILL.md frontmatter, manifests and version consistency.
- New `tools/check_links.py` and a weekly GitHub Actions job that checks every source link and opens, updates or closes a "Broken source links" issue.
- New test suite (`tests/`, standard library `unittest`): log parsing and verification, CrUX/PSI against local mock APIs, a fixture site for the auditor (including a JavaScript-only page for `--render`), and the integrity checks. CI runs it on Python 3.9 and 3.13.
- References: practices 6, 25, 124 and 127, `engines/ai-search.md` A7 and SKILL.md point to the new tools; two new evals (server logs, SPA performance and rendering).

## 1.3.1 — 2026-10-18

Fixes from real-world testing (Windows 11, live Shopify, WordPress, Cloudflare and Vercel sites, real Search Console API).

- `seo_audit.py` 1.3.1:
  - `--crawl` now works when the start URL redirects (apex→www, old→new domain, http→https): it crawls the host the start URL lands on and no longer reports false sitemap orphans.
  - Product checks skip reference-only nodes (`{"@type":"Product","url":…}`, e.g. Shopify `ProductGroup.hasVariant`) and let variants inherit group-level name, image, brand and description — removes hundreds of false "Product without name/image/offers" findings.
  - Pages over 5 MB gzip-compressed no longer crash the run (truncated bodies are decompressed as far as possible).
  - `--urls` and redirect-map files accept a UTF-8 BOM (Notepad, PowerShell 5.1).
  - Redirect maps compare URLs exactly, trailing slash included: `/a` → `/a/` is a redirect, not an "unchanged URL".
  - `hreflang` accepts language-script-region codes such as `zh-hans-cn` and UN M.49 regions (`es-419`).
  - The non-existent-URL probe follows redirects: a trailing-slash hop ending in 404 is info, not a warning; a redirect ending in 200 is reported as a soft 404.
  - "First image is lazy-loaded" looks at the first image in `<main>` (or outside nav/header/footer/aside) and is reported once per image, not on every crawled page.
  - Sitemap samples that only redirect are a warning, not critical.
  - Exit code `3` for errors (missing input file, unexpected failure), distinct from `1` (findings) and `2` (start URL unreachable).
  - Report output is UTF-8 on every console (no more `UnicodeEncodeError` on Windows cp1252).
  - `--delay` (default 0.5 s) between page fetches in crawl mode.
  - Warns when a page's HTML exceeds 5 MB and was truncated for analysis.
  - Lint: removed unused variables and placeholder-less f-strings.
- `search_data.py` 1.0.1: Bing `/Date(ms±hhmm)/` values are converted to the day of their own offset; `--urls` accepts a BOM; non-JSON API responses (proxies, HTML error pages) raise a clear error; timeouts and dropped connections are retried; CSV on stdout no longer doubles line endings on Windows; `compare --map` skips `#` comment rows; exit code `3` for file and input errors.
- Content: Baidu rendering stated as documented (`Baiduspider-render/2.0`) with the rest marked *Unconfirmed*; exact SeznamBot user agent; Q&A removal (L8) cites the API change log and Google's forum announcement; nine stale or moved source links updated (Google-Extended, crawl budget, YouTube recommendations, Apple Business, rater guidelines, Abogacía code, Screaming Frog, Zyppy, Onely).
- SKILL.md: shorter description; "Always avoid" now names expecting FAQ rich results (retired 7 May 2026).
- Evaluated: with the skill, answers scored 4.65/5 vs 4.00/5 without it across the 13 evals (won all 13); no claims refuted in a source check of 219 links.
- README rewritten in the blackwings.dev format (icon, "Why this exists", features, usage table, security, contributing rules, maintainer note); new `assets/` with the project icon; GitHub Actions workflow that compiles the scripts and validates the manifests on Python 3.9 and 3.13.
- README: fixed an unclosed code fence; exit codes; how to get a Search Console token with your own OAuth Desktop client; Windows/PowerShell notes; remove a hand-copied `~/.claude/skills/seo-pro` when switching to the plugin.

## 1.3.0 — 2026-10-18

An operating plan by business type; layers by business model (local, e-commerce, SaaS and services, publishers, regulated topics); new engine layers (video and images, other engines); cross-cutting playbooks (migrations, measurement, reputation, programmatic pages, governance); a redirect-map validator and Search Console/Bing data tools.

- New `references/verticals/` folder with a README that maps business-model layers onto engines (Google, Bing/Microsoft, Apple, AI answer engines) and applies the conflict rule to verticals.
- New `verticals/local.md` (L1–L22): business models and eligibility, real names, categories, address/pin/service area, profile data, ownership governance, photos and the Maps AI "Ask" feature that replaces Q&A (removal announced Dec 2025), a review programme within platform rules (no gating or incentives; EU 2019/2161, FTC rule, UK CMA as starting points), location and service-area pages, `LocalBusiness` per location, a master location record, selective citations, Bing Places and Apple Business (formerly Apple Business Connect), per-location and per-surface measurement, geo-grids as samples, test design, priorities by model, local myths, a 90-day sequence and a checklist.
- New `verticals/ecommerce.md` (E1–E24): page types, taxonomy and HTML paths, internal linking, pagination, a faceted-navigation policy per URL pattern, internal search, variants with `ProductGroup`, identifiers, product content, images, price/stock transparency, Product snippets vs Merchant listings, shipping and returns via Search Console or organization-level markup (Nov 2025), Merchant Center free listings, catalogue reconciliation, stock lifecycle, international stores, platform apps, Microsoft feeds as ads, agentic commerce (Google UCP early access, OpenAI ACP product discovery), stage-by-stage catalogue metrics, cohort experiments, priorities by store model, myths, a 90-day sequence and a checklist.
- Core practices 20, 22, 28, 71, 98 and 121, Bing B15, AI A18, the engines matrix (product feeds, shipping and returns, Apple Business) and `myths.md` link to the new layers.
- `seo_audit.py` 1.3.0: `LocalBusiness` checks (address, telephone, phone visible on the page, opening hours, self-serving ratings), `Product` checks (offers, price, currency, availability, identifiers, duplicate Product nodes), and in crawl mode a report of parameterised internal links by parameter (facets, sorting, tracking).
- New `verticals/publishers.md` (P1–P20): editorial transparency, dates and corrections, headlines and previews, syndication, Discover images, Preferred sources, stable sections and permanent URLs, live blogs, archives, publisher migrations, Google News without submission (automatic publication pages since March 2025), News sitemap two-day window, `NewsArticle` as descriptive markup, Discover and the February 2026 Discover core update, paywall markup, sponsored content, Bing PubHub retirement, AI crawler and licensing decisions, separate Search / News / Discover reporting.
- New `verticals/regulated.md` (Y1–Y16): YMYL and E-E-A-T explained correctly, risk by the decision a page induces, responsibility records, roles and separation of duties, editorial flow, claims ledger, evidence proportionality, safe wording, verifiable authors and reviewers, health / finance / legal / other sector rules with EU, Spain and US examples, snippets and schema, decision design, generative-AI controls, review triggers, corrections and versioning, harm incidents.
- New `playbooks/` folder: `migrations.md` (M1–M18: change classes, scope matrix, inventory, master URL file, mapping and redirect rules, Change of Address for all domain variants per Google's June 2026 update, HTTPS and hosting moves, template parity, phases A–F with go/no-go, monitoring old + new, rollback), `measurement.md` (X1–X16: measurement contracts, event quality, GSC vs analytics, attribution vs causation, branded queries filter, cohorts, incrementality designs, SEO experiment protocol, change analysis, T0–T4 alert tiers, metric contracts), `reputation.md` (R1–R14: digital PR, outreach, sponsorships, mentions, earned links, site reputation abuse, disavow, review programmes, PR measurement, incidents) and `governance.md` (G1–G14: RACI, backlog, prioritisation, editorial and release flow, QA levels Q0–Q4, content lifecycle, quality gates, incident severity, change log, agencies and AI, templates, maturity).
- New `references/operating-plan.md` (O1–O14), now the entry point for any engagement: how to use it, a 10-day diagnosis, a playbook selector by dominant business model with hybrid rules, the common operating base, playbooks A–F (local, e-commerce, publisher, SaaS, lead generation, YMYL) with 0–30/31–60/61–90 phases, indicators, cadences and what not to prioritise, network (multi-location) and international modules, migration/measurement/reputation modules, a common 90-day rollout, recurring rhythm, balanced executive dashboard, minimum QA, rules against useless work and a quarterly plan template.
- New `verticals/saas-services.md` (S1–S14): SaaS search journey, use-case pages, crawlable docs and pricing, app/preview/version indexing control, honest comparisons, activation cohorts, docs for tasks and AI retrieval, integration pages; lead-generation service matrix, verifiable capacity, forms, CRM lead quality, reputation and measurement.
- New `playbooks/programmatic.md` (D1–D12): data asset first, legitimacy test against scaled content and doorway abuse, data-conditional templates, indexing thresholds and 404 for empty combinations, canonicals, hubs, crawl at scale, launch in waves with cohorts, AI pipelines, structured data per page, pruning, third-party page sets.
- New `engines/video-images.md` (V1–V14): watch pages and Video mode, `VideoObject` (incl. `creator`, Sep 2026), thumbnails, video sitemaps, key moments, livestreams, SafeSearch, YouTube ranking and recommendations, chapters, captions, auto-dubbing, Test & compare (watch-time share), AI disclosure, Google image practices (`<img src>`, AVIF, consistent URLs), preferred images for Search/Discover (Mar 2026), image licensing and IPTC/C2PA provenance.
- New `engines/other-engines.md` (W1–W12): IndexNow participants, Yandex (Clean-param, no Host, YandexAdditional for AI answers, DNS verification), Baidu (server HTML, no documented hreflang, ICP, AI search), Naver (Yeti, AI Briefing), Seznam, local map platforms, Brave, DuckDuckGo/Yahoo, the Ecosia–Qwant European index, Mojeek, Kagi, Applebot and Applebot-Extended; secondary-source claims labelled.
- `seo_audit.py`: `--redirect-map file.csv` validates a migration map (no redirect, temporary redirects, chains, loops, unexpected destinations, home-page catch-alls, non-200 destinations, retired URLs still 200, duplicates and planned chains in the map) with its own report section; usable on its own or with a site audit.
- New `scripts/search_data.py` (dependency-free): Search Console search analytics with paging and filters, URL Inspection, sitemaps and sites; Bing Webmaster query/page/traffic/crawl stats with Microsoft date parsing; `compare` (before/after or old vs new URLs via the redirect map) and `brand-split`.
- Fix: Bing B23 and the engines matrix no longer recommend Bing News PubHub, which Microsoft retired.
- Core 101, 102, 107, 117, 147, 153, 159 and 160 link to the new layers; 117 uses Search Console's branded queries filter; myths gain publisher, migration, measurement, authority and YMYL entries.
- `seo_audit.py` 1.3.0 also checks `NewsArticle`/`Article` (missing fields, `dateModified` before `datePublished`, `max-image-preview:large`, paywall markup without `hasPart`).
- Spanish studies on local SEO, e-commerce, publishers, migrations, measurement, reputation, regulated topics and governance, and the operating plan, added to `docs/`.

## 1.2.0 — 2026-10-18

Evidence-led refinement and a new layer for AI answer engines.

- New `engines/ai-search.md` (A1–A18) for Google AI Overviews / AI Mode, ChatGPT Search, Perplexity and Claude: the seven-stage access-to-citation funnel, per-operator search / training / user-fetch decisions with a robots template, Search Console's Search generative AI control (global since 31 Aug 2026), ChatGPT (`OAI-SearchBot`, `noindex`, `utm_source=chatgpt.com`, Atlas ARIA), Perplexity user fetches that ignore robots.txt, Claude agents and IP verification, WAF rules, an evidence table (established / supported / hypothesis / myth), a query panel, an observation log, eight metrics, a test protocol, priorities by site type, a 90-day sequence and sources graded A–E.
- Engines matrix gains AI controls; AI myths added (`llms.txt`, AI schema, chunking, the "40% GEO" misreading, GPTBot vs OAI-SearchBot, robots.txt as privacy).
- Practices 37, 61, 69 and 148 link to the AI layer; 69 is now labelled a hypothesis as a citation lever.
- `seo_audit.py`: crawlers grouped by purpose (search, AI search, training, user fetch), `Perplexity-User` and `Google-Extended` added, warning when AI search agents are blocked.
- Spanish AI-search study added to `docs/`.

- New `references/research-method.md`: evidence hierarchy, confidence labels (Established / Supported / Hypothesis / Unknown), how to assess a claim, a 20-source register with limitations, and current platform references.
- Plans now carry a Confidence column and are prioritised by impact × confidence × reach ÷ effort/risk; verified issues are separated from inferred impact.
- Heuristics (title and description length, one H1, featured-snippet answer length, timelines) are kept as labelled defaults instead of rules.
- AI-search guidance states clearly that citations and referrals are uncertain outcomes; crawler-specific access is checked per product.
- Jurisdiction-aware legal guidance for reviews, scarcity and reference prices, with primary sources (EU, UK CMA, US FTC, European Commission).
- `seo_audit.py` 1.2.0: title length, meta-description length and H1 count are review prompts (info), not defects; clearer FAQPage message.
- Spanish research synthesis added to `docs/` (not loaded by the skill).

## 1.1.0 — 2026-10-18

Engine-aware SEO, starting with Bing and Microsoft Copilot.

- New `references/engines/` layer: target-engine selection, a Google ↔ Bing decision matrix and a conflict-resolution rule (do both → stricter wins → user-facing truth wins → document the trade-off).
- New `engines/bing.md` with practices B1–B24 based on Bing's Copilot-era Webmaster Guidelines: verification, streamed IndexNow, ETag freshness, Bingbot access, 302 timing, crawl-delay vs Crawl Control, client-side rendering, `noarchive`/`nocache`/`nosnippet` and Copilot grounding, AI Performance report, published ranking parameters, hosting/language signals, Bing Places, abuse (prompt injection, artificial social promotion), BWT toolbox, mRSS, PubHub, measuring beyond clicks.
- Coverage map of a 160-point Bing checklist onto the core practices, plus Bing-specific myths.
- `SKILL.md`: step 1 is now "decide the target engines"; new principle "satisfy every target engine".
- `seo_audit.py` 1.1.0: Bing checks (Bingbot blocked, crawl-delay, Copilot directives, 302/307 hops, BWT verification, `--indexnow-key`) and a "Bing & Copilot" report section.

## 1.0.0 — 2026-10-18

Initial release.

- `seo-pro` skill with a five-step workflow: diagnose → prioritised plan → implement → verify → follow up.
- 160 practices across three phases (technical, content, authority), each with Why / How / Expected result / Avoid / Verify.
- Myths and outdated-advice reference (FAQ rich results retirement, Indexing API limits, disavow, date bumping, review stars…).
- Next.js App Router implementation guide and equivalents for Astro, WordPress, SPAs, Nginx, Apache, Cloudflare and Vercel/Netlify.
- `seo_audit.py`: dependency-free auditor with crawl mode, JSON output and CI-friendly exit codes.
