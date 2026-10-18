<div align="center">

<img src="./assets/icono-seo-pro.png" alt="seo-pro" width="128" height="128">

# seo-pro

**An SEO skill for Claude Code that audits with evidence, fixes the code and checks that
every change actually works — for Google, Bing, AI answer engines and the rest.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-%E2%89%A5%203.9-brightgreen.svg)](https://www.python.org)
[![Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)](#the-auditor)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-8A2BE2.svg)](#installation)
[![Practices](https://img.shields.io/badge/practices-160-orange.svg)](#what-it-knows)

</div>

---

## Why this exists

**Most SEO advice is a mix of solid fundamentals, outdated folklore and tactics that can
get a site penalised.** Checklists don't tell you which is which, don't know whether you
are a plumber, a newsroom or a 50,000-product shop, and stop at "add a meta description".

`seo-pro` gives your assistant a method instead of a list:

```
"Organic traffic dropped 40% since the 12th — find out why and fix it"

→ diagnose   audit the live site and the code that generates metadata, sitemaps, redirects
→ plan       findings ranked by impact × effort, including what NOT to do
→ implement  with your framework's native APIs, centralised and consistent
→ verify     curl, the auditor and the right Search Console / Bing reports
→ follow up  realistic timelines, KPIs and recurring checks
```

Every recommendation is labelled by how sure we can be of it, and every number in the
references points to a source you can check.

---

## Features

- **Engine-aware.** A shared core of 160 practices that works everywhere, a layer per
  engine for what genuinely differs, and a conflict rule so one site meets the standard of
  every target engine at once: **Google**, **Bing / Microsoft Copilot**, **AI answer
  engines** (AI Overviews, AI Mode, ChatGPT, Perplexity, Claude), **video and images**
  (Google video, YouTube, Google Images) and **other engines** (Yandex, Baidu, Naver,
  Seznam, Brave, the Ecosia/Qwant index, Applebot).
- **Business-model-aware.** Layers for **local businesses**, **online stores**, **SaaS and
  professional services**, **news publishers** and **health, finance and legal topics** —
  a clinic and a shop don't get the same advice.
- **Starts with an operating plan.** A 10-day diagnosis, a playbook selector by business
  type (and hybrids), 0–90-day phases, indicators, cadences, a balanced dashboard and a
  quarterly plan template.
- **Playbooks for the hard moments.** Migrations with go/no-go and rollback, measurement
  and SEO experiments, reputation and digital PR, programmatic pages, governance.
- **Evidence-led.** Claims are *Established*, *Supported*, *Hypothesis* or *Unknown*;
  official documentation and first-party data come first, vendor studies are context.
- **Myths called out.** A list of popular advice that is false, outdated or dangerous —
  and what to do instead.
- **A real auditor, not a prompt.** `seo_audit.py` crawls the site, validates migration
  redirect maps and exits with CI-friendly codes. Python 3.9+, no packages.
- **Sees what JavaScript hides.** `--render` loads every page in headless Chromium and
  shows what only exists after JavaScript — text, links, title, canonical, structured data —
  which most AI crawlers never see.
- **A report you can hand over.** `--html` writes one self-contained page with a
  "fix first" list, every finding filterable, light and dark.
- **What bots really do.** `crawl_logs.py` reads your server logs and tells you what
  Googlebot, Bingbot and the AI agents actually crawl, how much of it is wasted, and which
  "Googlebots" are impostors — checked against each operator's published IP ranges.
- **Your own data.** `search_data.py` pulls Search Console and Bing Webmaster data,
  field Core Web Vitals from CrUX and PageSpeed Insights, compares before/after or old/new
  URLs and splits brand from non-brand.
- **Implements, doesn't just advise.** Next.js App Router code, plus Astro, WordPress,
  SPAs, Nginx, Apache, Cloudflare and Vercel/Netlify.
- **Up to date with 2026.** FAQ rich results retired, spam policies applied to AI
  features, Bing's AI Performance report, Q&A removed from Google Maps, and more.

---

## Prerequisites

| | |
|---|---|
| **Claude Code** | Any recent version with plugin support. |
| **Python** | **≥ 3.9**, only for the scripts. No packages to install. |
| **Playwright** | Optional, only for `seo_audit.py --render`: `pip install playwright && python -m playwright install chromium`. |
| **Search Console / Bing / CrUX** | Optional. Your own OAuth token or API keys, only for `search_data.py`. |

---

## Installation

### As a plugin (recommended)

Inside Claude Code:

```
/plugin marketplace add blackwings-dev/seo-pro
/plugin install seo-pro@blackwings-dev
```

> ⚠️ **Switching from a hand-copied version?** Delete `~/.claude/skills/seo-pro` first.
> Otherwise the old standalone copy may be picked instead of the plugin.

### As a standalone skill

```bash
git clone https://github.com/blackwings-dev/seo-pro.git
# for all your projects
cp -r seo-pro/plugins/seo-pro/skills/seo-pro ~/.claude/skills/
# or for a single project (versioned with the repo)
cp -r seo-pro/plugins/seo-pro/skills/seo-pro .claude/skills/
```

---

## Usage

The skill activates by itself for anything SEO-related — even if you never say "SEO". As
a plugin you can also call it explicitly with `/seo-pro:seo-pro`.

| What you say | What happens |
|---|---|
| *"Audit https://example.com and give me a prioritised plan"* | Auditor + code review → plan by impact × effort |
| *"We launch on Monday — is the site ready for Google?"* | Pre-launch checks, then verification of each fix |
| *"Google isn't indexing our product pages"* | Indexing diagnosis: robots, canonicals, sitemaps, soft 404s, rendering |
| *"Add sitemap, robots, canonicals and JSON-LD to this Next.js project"* | Implementation with the Metadata API, `sitemap.ts`, `robots.ts` |
| *"Organic traffic dropped 40% since the 12th"* | Change analysis with Search Console data, causes ranked by evidence |
| *"Why aren't we in Bing or cited by Copilot?"* | Bing layer: Webmaster Tools, IndexNow, Copilot directives |
| *"Should we block GPTBot? Does ChatGPT cite us?"* | Per-agent decisions and a measurement protocol for AI citations |
| *"We have three clinics and only one shows up on Maps"* | Local layer: profiles, categories, location pages, reviews within the rules |
| *"A million filter URLs crawled but not indexed"* | Faceted-navigation policy per URL pattern |
| *"Moving from WordPress to headless and a new domain next month"* | Migration playbook + redirect-map validation before go-live |
| *"How much revenue did SEO actually generate?"* | Attribution vs causation, cohorts, an experiment design |
| *"Review our clinic's treatment pages before we publish"* | YMYL layer: claims ledger, professional review, safe wording |
| *"5,000 city pages — programmatic SEO or spam?"* | Legitimacy test, data thresholds, launch in waves |
| *"Plan our SEO for next quarter — we're a B2B SaaS"* | Operating plan: diagnosis, playbook, 90-day phases, dashboard |
| *"Here are our Nginx logs — is Googlebot wasting its crawl?"* | `crawl_logs.py`: verified bots, crawl waste, sections, sitemap URLs never fetched |
| *"Our React site scores 94 in Lighthouse, so speed is fine?"* | Field data with `crux` + `--render` to show what only exists after JavaScript |

Habits worth having:

- **Give it the real URL or the repository.** It audits what is served, not what you
  remember.
- **Say who the site is for and where.** Business model and country change the advice.
- **Ask it to verify.** Every change should end with a check, not with "it compiles".

---

## What it knows

```
plugins/seo-pro/skills/seo-pro/
├── SKILL.md                       the workflow and principles
├── references/
│   ├── operating-plan.md          O1–O14  start here: diagnosis, playbook selector, 90-day plan
│   ├── phase-1-technical.md       1–40    indexing, crawling, performance, architecture, security
│   ├── phase-2-content.md         41–85   intent, on-page, AI search, UX, internal linking
│   ├── phase-3-authority.md       86–160  links, E-E-A-T, analytics, CRO, international
│   ├── engines/
│   │   ├── README.md              target engines, decision matrix, conflict rule
│   │   ├── bing.md                B1–B24  Webmaster Tools, IndexNow, Copilot, Bing Places
│   │   ├── ai-search.md           A1–A18  access funnel, per-agent controls, measurement
│   │   ├── video-images.md        V1–V14  watch pages, YouTube, images, licensing, C2PA
│   │   └── other-engines.md       W1–W12  Yandex, Baidu, Naver, Seznam, Brave, Applebot
│   ├── verticals/
│   │   ├── local.md               L1–L22  profiles, reviews, location pages
│   │   ├── ecommerce.md           E1–E24  facets, variants, Merchant Center, stock
│   │   ├── saas-services.md       S1–S14  docs, comparisons, activation, lead quality
│   │   ├── publishers.md          P1–P20  Google News, Discover, paywalls, corrections
│   │   └── regulated.md           Y1–Y16  YMYL risk, professional review, claims ledger
│   ├── playbooks/
│   │   ├── migrations.md          M1–M18  URL map, redirects, go/no-go, rollback
│   │   ├── measurement.md         X1–X16  attribution vs causation, experiments, alerts
│   │   ├── reputation.md          R1–R14  digital PR, earned links, disavow, reviews
│   │   ├── programmatic.md        D1–D12  legitimacy test, thresholds, waves
│   │   └── governance.md          G1–G14  RACI, prioritisation, QA levels, incidents
│   ├── research-method.md         evidence hierarchy and confidence labels
│   ├── myths.md                   popular advice that is false, outdated or dangerous
│   ├── nextjs.md                  Next.js App Router implementation with code
│   └── other-stacks.md            Astro, WordPress, SPAs, Nginx, Apache, Cloudflare, Vercel
└── scripts/
    ├── seo_audit.py               the auditor (optional JavaScript rendering, HTML report)
    ├── crawl_logs.py              server-log analysis: search and AI bots, verified
    └── search_data.py             Search Console, Bing Webmaster and Core Web Vitals data
```

Each practice follows the same format: **Why → How → Expected result → Avoid → Verify**,
with a priority level. References load only when a task needs them, so the skill stays
light in context.

---

## The auditor

`seo_audit.py` runs anywhere with Python 3.9+ — nothing to install.

```bash
python3 seo_audit.py https://example.com --crawl 100 --output report.md --json report.json
python3 seo_audit.py http://localhost:3000 --crawl 50              # a local production build
python3 seo_audit.py --urls critical-urls.txt --fail-on critical    # cron/CI
python3 seo_audit.py --redirect-map redirects.csv --fail-on critical  # a migration's old→new map
python3 seo_audit.py https://example.com --crawl 30 --render --html report.html  # raw vs rendered, client report
```

| Area | What it checks |
|---|---|
| **Indexability** | http/https/www variants and chains, robots.txt, sitemaps, `noindex`, `X-Robots-Tag`, canonicals, soft 404s |
| **On-page** | Title, description, H1 and headings, `lang`, viewport, hreflang, Open Graph, JSON-LD validity |
| **Performance** | Images without `alt` or size, lazy-loaded hero images, render-blocking scripts, DOM size, compression |
| **Security headers** | HSTS, CSP, clickjacking, `nosniff`, Referrer-Policy |
| **AI crawlers** | Every major search, training and user-fetch agent, with a warning when AI search agents are blocked |
| **Bing & Copilot** | Bingbot blocks, `crawl-delay`, snippet directives, long-lived 302s, IndexNow key |
| **Structured data** | `LocalBusiness`, `Product` (incl. `ProductGroup` variants), `NewsArticle`, paywall markup |
| **Redirect maps** | Permanent single hops, expected 200 destinations, no home-page catch-alls, retired pages 404/410 |
| **Crawl mode** | Broken links, links to redirects, duplicates, click depth, sitemap orphans, parameter URLs |
| **Rendering** (`--render`) | Text, internal links, title, description, canonical, robots, H1 and JSON-LD that only exist after JavaScript; client-side redirects |

Every finding cites the practice to read. Exit codes: `0` nothing at the `--fail-on`
level, `1` findings at that level, `2` start URL unreachable, `3` the check itself failed —
so CI can tell *"the site has problems"* from *"the check didn't run"*.

> **What it does not do.** It reads HTML and HTTP, and executes JavaScript only with
> `--render`. It doesn't confirm that a page is indexed, measure field Core Web Vitals
> (that's `search_data.py crux`) or predict rankings; treat its findings as prompts for review.

---

## Server logs

`crawl_logs.py` (dependency-free) reads Apache/Nginx combined or common logs, IIS/W3C and
JSON lines from Cloudflare Logpush, Vercel or Fastly — `.gz` included — and answers what no
crawler tool can: what search engines and AI agents **actually** fetch.

```bash
python3 crawl_logs.py access.log* --output crawl.md --json crawl.json
python3 crawl_logs.py access.log --sitemap-urls urls.txt     # sitemap URLs Googlebot never fetched
python3 crawl_logs.py cf.jsonl --format jsonl --host www.example.com
python3 crawl_logs.py access.log --verify dns                 # reverse + forward DNS instead of IP ranges
```

| It reports | |
|---|---|
| **Per bot** | Hits, share, status codes, unique URLs — about 35 search, AI and SEO-tool crawlers |
| **Verification** | Each claimed Googlebot, Bingbot, OpenAI, Anthropic, Perplexity or Applebot request checked against the operator's published IP ranges (or DNS); impostors reported apart and excluded |
| **Crawl waste** | Hits spent on redirects, 404/410, other errors, tracking and other parameter URLs |
| **Where it goes** | Sections, most-crawled URLs, parameters, daily trend |
| **AI agents** | Search, training and user-triggered agents separately, to check robots.txt decisions are working |
| **Sitemap coverage** | Sitemap URLs never fetched with a 200, and crawled pages missing from the sitemap |

Range files are downloaded once a day and cached; `--ranges-dir` works fully offline.
Logs contain IP addresses — personal data in the EU — so run it where the logs live and
share only the aggregated report.

---

## Search Console and Bing data

`search_data.py` (also dependency-free) pulls Search Console search analytics (paged, any
search type including Discover and News), URL Inspection and sitemaps, and Bing Webmaster
query, page, traffic and crawl stats. `compare` gives per-page deltas before/after a
release or old vs new URLs after a migration; `brand-split` separates brand and non-brand.
`crux` gets field Core Web Vitals (p75 of real Chrome users, per URL or origin, with a weekly
history) and `psi` adds PageSpeed Insights field and lab data.

```bash
export GSC_ACCESS_TOKEN="$(gcloud auth application-default print-access-token)"   # webmasters.readonly
python3 search_data.py gsc-query --site sc-domain:example.com --start 2026-07-01 --end 2026-09-30 --dimensions page,query --out gsc.csv
export BING_API_KEY=...   # Bing Webmaster Tools → Settings → API Access
python3 search_data.py bing --method GetPageStats --site https://example.com/ --out bing.csv
export CRUX_API_KEY=...   # Google Cloud API key with the Chrome UX Report API enabled
python3 search_data.py crux --urls templates.txt --form-factor PHONE --fallback-origin --out crux.csv
python3 search_data.py crux --origin https://example.com --history --out cwv-trend.csv
```

<details>
<summary><b>Getting a Search Console token</b></summary>

gcloud's built-in OAuth client is usually shown as "app blocked" for the
`webmasters.readonly` scope. Create your own **Desktop app** OAuth client in a Google Cloud
project, download its JSON and run:

```bash
gcloud auth application-default login --client-id-file=client.json \
  --scopes=https://www.googleapis.com/auth/webmasters.readonly,https://www.googleapis.com/auth/cloud-platform
gcloud auth application-default print-access-token
```

</details>

<details>
<summary><b>Windows / PowerShell</b></summary>

- Set variables with `$env:GSC_ACCESS_TOKEN = (gcloud auth application-default print-access-token)`
  and `$env:BING_API_KEY = ...`.
- Read secrets without echoing them with `Read-Host -AsSecureString` (`-MaskInput` doesn't
  exist in PowerShell 5.1).
- Use `py` if `python3` isn't on the PATH.
- PowerShell 5.1's `Set-Content -Encoding utf8` writes a BOM. Both scripts accept
  BOM-prefixed URL and CSV files, but gcloud rejects a client JSON saved that way — save it
  with `-Encoding ascii` or straight from the browser download.

</details>

---

## Evidence and scope

Recommendations follow the evidence hierarchy in `research-method.md`: first-party site
data and official search-engine documentation first, vendor studies and practitioner
analysis as context. **Rankings, traffic and AI citations are uncertain outcomes, never
promises.** Heuristics such as title length or one H1 are useful defaults, not ranking
rules.

The full research behind the skill, in Spanish, lives in [`docs/`](./docs) — general SEO,
AI answer engines, local, e-commerce, publishers, YMYL, migrations, measurement,
reputation, governance and the operating plan. It stays outside the skill so it never
loads into context.

---

## Security

- **Credentials stay in environment variables** — never in the repository, never in a
  report, never in the chat.
- **Read-only by design.** `search_data.py` only reads; the Search Console scope it needs
  is `webmasters.readonly`.
- **The auditor only makes GET requests**, identifies itself in its user agent and waits
  between pages (`--delay`, 0.5 s by default). Audit sites you own or are allowed to test.
- **Nothing you couldn't show a Google reviewer.** The skill will not suggest hidden text,
  fake reviews, bought links, cloaking or unreviewed mass content.

---

## Principles

- **Make it possible for Google before making Google want it.** Crawlability → content → links.
- **The served HTML is the truth.** Many AI crawlers don't run JavaScript.
- **One URL, one intent, one canonical version.**
- **Write for the answer, not the keyword.** That's what both classic and AI search reward.
- **Measure before and after.**

---

## Contributing

Issues and pull requests are welcome.

1. Fork the repository and create a branch: `git checkout -b feature/what-it-does`.
2. Make your change. `python tools/check_skill.py`, `python -m unittest discover -s tests`
   and `claude plugin validate .` must pass. The tests use local fixtures and mock APIs —
   no network, no keys.
3. Open a pull request describing **what changed, why, and how you verified it**.

Please keep the rules that hold the skill together:

- **Every factual claim cites an official source**, or is labelled as a hypothesis. A
  weekly job checks every source link and opens an issue when one dies.
- **Practice IDs are stable.** Add new ones at the end; never renumber.
- **No dependencies in the scripts.** Standard library only, Python 3.9+.
- **Nothing that could get a site penalised**, however well it "works".

Good first contributions: new stack guides, auditor checks, and updates when a search
engine changes its rules.

### Reporting a security issue

Please do **not** open a public issue. Contact the maintainers privately first.

---

## License

[MIT](./LICENSE) — do what you like, no warranty.

---

## Who maintains this

Built and maintained by [Black Wings](https://blackwings.dev) — software, AI and
managed IT for companies, from Valencia, Spain. We wrote this because we needed it:
we build and run sites for very different businesses, and no SEO checklist could tell a
clinic, a shop and a newsroom apart.

If it saves you the same afternoon it saved us, that is the whole point. Other things
we have released are listed at [blackwings.dev/codigo-abierto](https://blackwings.dev/codigo-abierto)
(in English: [blackwings.dev/en/open-source](https://blackwings.dev/en/open-source)).
