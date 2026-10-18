# seo-pro

**End-to-end SEO for [Claude Code](https://claude.com/claude-code).** A skill that turns Claude into a senior SEO consultant that audits with evidence, implements changes in your codebase, and verifies that every change actually works.

[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)
![Claude Code plugin](https://img.shields.io/badge/Claude%20Code-plugin-e0873f)
![Python 3.9+](https://img.shields.io/badge/auditor-Python%203.9%2B%2C%20zero%20deps-131316)

Built by [blackwings.dev](https://github.com/blackwings-dev).

---

## Why

Most SEO checklists are a mix of solid fundamentals, outdated folklore and tactics that can get a site penalised. `seo-pro` gives Claude a method instead of a list:

1. **Diagnose** — automated audit of the live site or a local production build, plus a review of where metadata, sitemaps, robots, structured data and redirects are generated in the code.
2. **Plan** — findings prioritised by impact × effort, including what *not* to do.
3. **Implement** — using your framework's native APIs (Next.js Metadata API, `sitemap.ts`, `robots.ts`, JSON-LD…), centralised and consistent.
4. **Verify** — every change checked with `curl`, the auditor and the right Google tools. No "it compiles, so it works".
5. **Follow up** — realistic timelines, KPIs and recurring checks.

It is **engine-aware**: a shared core of 160 practices that works everywhere, plus a layer per search engine for what genuinely differs, and a conflict-resolution rule so a site meets the standard of every target engine at once. It ships with layers for **Google**, **Bing / Microsoft Copilot**, **video and images** (Google video, YouTube, Google Images) and **other engines** (Yandex, Baidu, Naver, Seznam, Brave, the Ecosia/Qwant index, Applebot), covers AI search (Google AI Overviews and AI Mode, Copilot, ChatGPT, Perplexity, Claude), and is up to date with 2026 changes such as the retirement of FAQ rich results, Google's spam policies applying to its AI features, and Bing's Copilot-era guidelines and AI Performance report.

It starts from an **operating plan by business type**: a 10-day diagnosis, a playbook selector for local, e-commerce, publisher, SaaS, lead-generation and YMYL businesses (and hybrids), 0–90-day phases, indicators, cadences, a balanced dashboard and a quarterly plan template.

It is also **business-model-aware**: layers for **local businesses** (Google Business Profile, Maps, Bing Places, Apple Business, reviews within the rules, location pages), **online stores** (faceted navigation, variants, product data, Merchant Center, stock lifecycle, shipping and returns, agentic commerce), **SaaS and professional services** (solution pages, docs, comparisons, activation, lead quality), **news publishers** (Google News, Top Stories, Discover, paywalls, syndication, corrections) and **health, finance and legal topics** (risk by decision, professional review, claims ledger, safe wording), so a clinic, a plumber, a newsroom and a 50,000-SKU shop each get the practices that apply to them.

And it ships **playbooks** for the work every site eventually faces: **migrations** (redesigns, CMS, domain and hosting moves with go/no-go and rollback), **measurement** (attribution vs causation, cohorts, SEO experiments, alerts), **reputation** (digital PR, earned links, reviews, disavow), **programmatic pages** (data thresholds, legitimacy test, launch in waves) and **governance** (RACI, prioritisation, QA levels, maintenance, incidents).

## What's inside

```
plugins/seo-pro/skills/seo-pro/
├── SKILL.md                       # The workflow and principles
├── references/
│   ├── operating-plan.md          # O1–O14: start here — diagnosis, playbook selector, 90-day plan, dashboard, quarterly template
│   ├── phase-1-technical.md       # 1–40   indexing, crawling, performance, architecture, security, legal, measurement
│   ├── phase-2-content.md         # 41–85  keywords, intent, on-page, AI search (GEO), UX, internal linking
│   ├── phase-3-authority.md       # 86–160 links, E-E-A-T, analytics, CRO, automation, international, maintenance
│   ├── engines/
│   │   ├── README.md              # Target engines, Google ↔ Bing decision matrix, conflict-resolution rule
│   │   ├── video-images.md        # V1–V14: watch pages, VideoObject, key moments, YouTube, images, licensing, C2PA
│   │   ├── other-engines.md       # W1–W12: IndexNow network, Yandex, Baidu, Naver, Seznam, Brave, EUSP, Applebot
│   │   ├── ai-search.md           # A1–A18: AI answer engines — access funnel, per-agent controls, measurement protocol
│   │   └── bing.md                # B1–B24: Bing Webmaster Tools, IndexNow, Copilot directives, AI Performance, Bing Places
│   ├── verticals/
│   │   ├── README.md              # Business-model layers and how they map onto engines
│   │   ├── local.md               # L1–L22: eligibility, profiles (Google, Bing, Apple), reviews, location pages, measurement
│   │   ├── ecommerce.md           # E1–E24: facets, variants, product data, Merchant Center, stock lifecycle, agentic commerce
│   │   ├── saas-services.md       # S1–S14: SaaS journey, docs, comparisons, activation; lead-gen services and lead quality
│   │   ├── publishers.md          # P1–P20: transparency, permanent URLs, Google News, News sitemaps, Discover, paywalls
│   │   └── regulated.md           # Y1–Y16: YMYL risk, professional review, claims ledger, health/finance/legal rules
│   ├── playbooks/
│   │   ├── README.md              # When to use each playbook
│   │   ├── migrations.md          # M1–M18: inventory, URL map, redirects, Change of Address, parity, go/no-go, rollback
│   │   ├── measurement.md         # X1–X16: events, attribution vs causation, cohorts, experiments, alerts, dashboards
│   │   ├── reputation.md          # R1–R14: digital PR, mentions, earned links, disavow, reviews, incidents
│   │   ├── programmatic.md        # D1–D12: data assets, legitimacy test, thresholds, hubs, waves, AI pipelines, pruning
│   │   └── governance.md          # G1–G14: RACI, backlog, prioritisation, QA levels Q0–Q4, maintenance, incidents
│   ├── research-method.md         # Evidence hierarchy, confidence labels, 20-source register, platform links
│   ├── myths.md                   # Popular advice that is false, outdated or dangerous — and what to do instead
│   ├── nextjs.md                  # Next.js App Router implementation with code
│   └── other-stacks.md            # Astro, WordPress, SPAs, Nginx, Apache, Cloudflare, Vercel/Netlify
└── scripts/
    ├── seo_audit.py               # Dependency-free auditor (Markdown/JSON report, CI exit codes, redirect-map validator)
    └── search_data.py             # Search Console + Bing Webmaster API exports, before/after and old-vs-new comparison, brand split
```

Each of the **160 practices** follows the same format: **Why → How → Expected result → Avoid → Verify**, with a priority level.

## Evidence and scope

Recommendations are labelled by confidence (*Established*, *Supported*, *Hypothesis*, *Unknown*) using the evidence hierarchy in `research-method.md`: first-party site data and official search-engine documentation first, vendor studies and practitioner analysis as context. Its 20-source register is a reading map, not 20 independent confirmations. The full Spanish research syntheses behind it — [`docs/research-bible-2026-es.md`](docs/research-bible-2026-es.md) (general SEO) and [`docs/ai-search-study-2026-es.md`](docs/ai-search-study-2026-es.md) (AI answer engines), [`docs/local-maps-study-2026-es.md`](docs/local-maps-study-2026-es.md) (local SEO and maps), [`docs/ecommerce-study-2026-es.md`](docs/ecommerce-study-2026-es.md) (e-commerce), [`docs/publishers-study-2026-es.md`](docs/publishers-study-2026-es.md) (news), [`docs/regulated-study-2026-es.md`](docs/regulated-study-2026-es.md) (YMYL), [`docs/migrations-study-2026-es.md`](docs/migrations-study-2026-es.md), [`docs/measurement-study-2026-es.md`](docs/measurement-study-2026-es.md), [`docs/reputation-study-2026-es.md`](docs/reputation-study-2026-es.md) and [`docs/governance-study-2026-es.md`](docs/governance-study-2026-es.md), plus the operating plan [`docs/operating-plan-2026-es.md`](docs/operating-plan-2026-es.md) — live outside the skill so they don't load into context.

Rankings, traffic and AI citations are uncertain outcomes, never promises. Heuristics such as title length or one H1 are presented as useful defaults, not ranking rules.

The auditor checks HTML and HTTP signals. It doesn't execute JavaScript, confirm that a page is indexed, measure field Core Web Vitals or predict rankings: its findings are prompts for review.

## Install

### As a plugin (recommended)

Inside Claude Code:

```
/plugin marketplace add blackwings-dev/seo-pro
/plugin install seo-pro@blackwings-dev
```

### As a standalone skill

```bash
git clone https://github.com/blackwings-dev/seo-pro.git
# for all your projects
cp -r seo-pro/plugins/seo-pro/skills/seo-pro ~/.claude/skills/
# or for a single project (versioned with the repo)
cp -r seo-pro/plugins/seo-pro/skills/seo-pro .claude/skills/
```

## Usage

The skill activates automatically when you ask for anything SEO-related — even without saying "SEO":

- "Audit the SEO of https://example.com and give me a prioritised plan"
- "We launch on Monday — make sure the site is ready for Google"
- "Google isn't indexing our product pages, find out why"
- "Add sitemap, robots, canonicals and JSON-LD to this Next.js project"
- "Write the service page for web development in Valencia, optimised for Google and for AI answers"
- "Organic traffic dropped 40% since the 12th"
- "Why aren't we showing up in Bing or getting cited by Copilot?"
- "Should we block GPTBot? And how do we know if ChatGPT or Perplexity cite us?"
- "We have three clinics and only one shows up on Google Maps"
- "Our store has a million filter URLs crawled but not indexed — what do we block?"
- "We're moving from WordPress to a headless CMS and a new domain next month"
- "Our Discover traffic collapsed and Google News stopped showing us"
- "Leadership wants to know how much revenue SEO actually generated"
- "Review our clinic's treatment pages before we publish them"
- "We want 5,000 city pages for our booking platform — is that programmatic SEO or spam?"
- "We're launching in Russia and South Korea — what changes?"
- "Plan our SEO for the next quarter — we're a B2B SaaS"

As a plugin you can also invoke it explicitly with `/seo-pro:seo-pro`.

## The auditor

`seo_audit.py` runs anywhere with Python 3.9+ — no packages to install.

```bash
python3 seo_audit.py https://example.com --crawl 100 --output report.md --json report.json
python3 seo_audit.py http://localhost:3000 --crawl 50          # audit a local production build
python3 seo_audit.py --urls critical-urls.txt --fail-on critical # cron/CI: exit code 1 on critical findings
python3 seo_audit.py --redirect-map redirects.csv --fail-on critical  # validate a migration's old→new map
```

It checks:

- **Indexability** — http/https/www variants and redirect chains, robots.txt (including AI crawlers), sitemap validity and non-200 URLs, `noindex` and `X-Robots-Tag`, canonicals, soft 404s.
- **On-page** — title and meta description, H1 and heading hierarchy, `lang`, viewport, hreflang, Open Graph, favicon, JSON-LD validity and types.
- **Performance and rendering** — images without `alt` or dimensions, lazy-loaded hero images, render-blocking scripts, JavaScript-dependent content, DOM size, compression, ETag/304.
- **Security headers** — HSTS, CSP, clickjacking protection, `nosniff`, Referrer-Policy.
- **AI crawlers** — every major search, training and user-fetch agent with its purpose, and a warning when AI search agents are blocked.
- **Bing & Copilot** — Bingbot blocks, `crawl-delay`, `noarchive`/`nocache`/`nosnippet` and their Copilot effect, 302s Bing treats as too long-lived, Bing Webmaster Tools verification, IndexNow key file (`--indexnow-key`).
- **Local, product and article data** — `LocalBusiness` address, phone (and whether it's visible on the page), opening hours and self-serving ratings; `Product` offers, price, currency, availability, identifiers and duplicate Product markup from competing plugins; `NewsArticle`/`Article` fields, `dateModified` before `datePublished`, `max-image-preview:large` for Discover and paywall markup without `hasPart`.
- **Redirect maps** (`--redirect-map file.csv`) — every old URL: permanent single hop, expected destination returning 200, no home-page catch-alls, retired pages answering 404/410, duplicates and planned chains in the map.
- **Crawl mode** (`--crawl N`) — broken internal links, links to redirects, duplicate titles and descriptions, click depth, orphaned sitemap URLs and parameterised internal links grouped by parameter (facets, sorting, tracking).

Every finding cites the practice number to read in the references.

## Search Console and Bing data

`search_data.py` (also dependency-free) pulls Search Console search analytics (paged, any search type incl. Discover and News), URL Inspection and sitemaps with your own OAuth token, and Bing Webmaster query, page, traffic and crawl stats with your API key. `compare` gives per-page deltas before/after a release or old vs new URLs after a migration; `brand-split` separates brand and non-brand. Credentials stay in environment variables — never in the repo or the chat.

```bash
export GSC_ACCESS_TOKEN="$(gcloud auth application-default print-access-token)"   # scope webmasters.readonly
python3 search_data.py gsc-query --site sc-domain:example.com --start 2026-07-01 --end 2026-09-30 --dimensions page,query --out gsc.csv
export BING_API_KEY=...   # Bing Webmaster Tools → Settings → API Access
python3 search_data.py bing --method GetPageStats --site https://example.com/ --out bing.csv
``` It doesn't execute JavaScript or measure field Core Web Vitals — use PageSpeed Insights and Search Console for those.

## Principles

- **Make it possible for Google before making Google want it.** Crawlability → content → links.
- **The served HTML is the truth.** Many AI crawlers don't run JavaScript.
- **One URL, one intent, one canonical version.**
- **Write for the answer, not the keyword.** That's what both classic and AI search reward.
- **Nothing you couldn't show a Google reviewer.** No hidden text, fake reviews, bought links, cloaking or unreviewed mass content.
- **Measure before and after.**

## Contributing

Issues and pull requests are welcome — especially new stack guides, engine or vertical layers, auditor checks and updates when search engines change their rules. Please cite an official source for any change to a factual claim.

## License

[MIT](LICENSE) © 2026 blackwings.dev
