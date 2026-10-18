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

It covers classic search **and AI search** (Google AI Overviews and AI Mode, ChatGPT, Perplexity, Copilot), and it is up to date with 2026 changes such as the retirement of FAQ rich results and Google's spam policies now applying to its AI features.

## What's inside

```
plugins/seo-pro/skills/seo-pro/
├── SKILL.md                       # The workflow and principles
├── references/
│   ├── phase-1-technical.md       # 1–40   indexing, crawling, performance, architecture, security, legal, measurement
│   ├── phase-2-content.md         # 41–85  keywords, intent, on-page, AI search (GEO), UX, internal linking
│   ├── phase-3-authority.md       # 86–160 links, E-E-A-T, analytics, CRO, automation, international, maintenance
│   ├── myths.md                   # Popular advice that is false, outdated or dangerous — and what to do instead
│   ├── nextjs.md                  # Next.js App Router implementation with code
│   └── other-stacks.md            # Astro, WordPress, SPAs, Nginx, Apache, Cloudflare, Vercel/Netlify
└── scripts/
    └── seo_audit.py               # Dependency-free auditor (Markdown/JSON report, CI exit codes)
```

Each of the **160 practices** follows the same format: **Why → How → Expected result → Avoid → Verify**, with a priority level.

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

As a plugin you can also invoke it explicitly with `/seo-pro:seo-pro`.

## The auditor

`seo_audit.py` runs anywhere with Python 3.9+ — no packages to install.

```bash
python3 seo_audit.py https://example.com --crawl 100 --output report.md --json report.json
python3 seo_audit.py http://localhost:3000 --crawl 50          # audit a local production build
python3 seo_audit.py --urls critical-urls.txt --fail-on critical # cron/CI: exit code 1 on critical findings
```

It checks:

- **Indexability** — http/https/www variants and redirect chains, robots.txt (including AI crawlers), sitemap validity and non-200 URLs, `noindex` and `X-Robots-Tag`, canonicals, soft 404s.
- **On-page** — title and meta description, H1 and heading hierarchy, `lang`, viewport, hreflang, Open Graph, favicon, JSON-LD validity and types.
- **Performance and rendering** — images without `alt` or dimensions, lazy-loaded hero images, render-blocking scripts, JavaScript-dependent content, DOM size, compression, ETag/304.
- **Security headers** — HSTS, CSP, clickjacking protection, `nosniff`, Referrer-Policy.
- **Crawl mode** (`--crawl N`) — broken internal links, links to redirects, duplicate titles and descriptions, click depth and orphaned sitemap URLs.

Every finding cites the practice number to read in the references. It doesn't execute JavaScript or measure field Core Web Vitals — use PageSpeed Insights and Search Console for those.

## Principles

- **Make it possible for Google before making Google want it.** Crawlability → content → links.
- **The served HTML is the truth.** Many AI crawlers don't run JavaScript.
- **One URL, one intent, one canonical version.**
- **Write for the answer, not the keyword.** That's what both classic and AI search reward.
- **Nothing you couldn't show a Google reviewer.** No hidden text, fake reviews, bought links, cloaking or unreviewed mass content.
- **Measure before and after.**

## Contributing

Issues and pull requests are welcome — especially new stack guides, auditor checks and updates when search engines change their rules. Please cite an official source for any change to a factual claim.

## License

[MIT](LICENSE) © 2026 blackwings.dev
