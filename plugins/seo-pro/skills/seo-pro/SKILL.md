---
name: seo-pro
description: End-to-end SEO for websites — technical SEO, on-page, content strategy, authority and visibility in AI search (Google AI Overviews and AI Mode, Bing and Microsoft Copilot, ChatGPT, Perplexity) — with 160 verifiable practices, code-level implementation guides and an automated auditor. Use this skill whenever the user wants to rank a website, audit SEO, launch a new domain, fix indexing, improve Core Web Vitals, metadata, sitemaps, robots.txt, canonicals, hreflang, structured data/Schema/JSON-LD, internal linking, keyword strategy, content for Google or for AI (GEO), backlinks, E-E-A-T, Search Console, Bing Webmaster Tools, IndexNow, Bing Places, or organic traffic drops — even if they never say "SEO" (e.g. "Google isn't indexing my site", "I want to show up on Google", "get the site ready for production", "review the homepage before launch").
license: MIT
---

# SEO Pro

A working method for Claude Code to do SEO the way a senior consultant would: **audit with evidence, implement in the project's code, verify that every change works, and measure the outcome.**

The core idea: SEO that works today is **a technically clean site that Google and AI search engines can crawl and understand effortlessly, with content that satisfies search intent better than the competition, backed by real trust signals.** Everything else is a shortcut that either doesn't work or gets you penalized. This skill therefore favours what can be verified over textbook advice, and explicitly flags popular advice that is no longer true (see `references/myths.md`).

## How it is organised

| File | Contents | When to read it |
|---|---|---|
| `references/phase-1-technical.md` | Practices 1–40: indexing, crawling, performance, architecture, security, legal, measurement | Launches, technical audits, "Google won't index", Core Web Vitals |
| `references/phase-2-content.md` | Practices 41–85: keywords, intent, on-page, AI search (GEO), UX, internal linking | Writing or optimising pages, content strategy, metadata, Schema |
| `references/phase-3-authority.md` | Practices 86–160: links, E-E-A-T, analytics, CRO, automation, international, maintenance | Indexed sites that need to grow, link building, multilingual, monitoring |
| `references/engines/README.md` | Which engines to target, the Google ↔ Bing decision matrix and the rule for resolving conflicts | **Always**, at the start of a job, to decide the target engines |
| `references/engines/bing.md` | Practices B1–B24: Bing Webmaster Tools, IndexNow, Copilot directives (`noarchive`/`nocache`), AI Performance, Bing Places, and a map of a 160-point Bing checklist onto the core | Whenever Bing/Copilot is a target (by default it is) |
| `references/myths.md` | Popular SEO advice that is false, outdated or dangerous, and what to do instead | **Always** before recommending something "from the textbook" you are not sure about |
| `references/nextjs.md` | Concrete Next.js (App Router) implementation: metadata, sitemap.ts, robots.ts, JSON-LD, next/image, next/font, headers, redirects | If the project uses Next.js (check `package.json`) |
| `references/other-stacks.md` | Equivalents for static HTML, SPAs, Astro, WordPress, Nginx, Apache, Cloudflare, Vercel/Netlify | Any other stack |
| `scripts/seo_audit.py` | Dependency-free automated audit (Python 3.9+) of a URL or a whole site; the report cites practice numbers | At the start of any job, and again to verify after changes |

The core practices (1–160) apply to every search engine. Engine layers add only what differs, with their own IDs (B1… for Bing), so the core is never duplicated.

Every practice in the references follows the same format: **Why → How → Expected result → Avoid → Verify**. Don't read all three phases at once: work out what the user needs and open the relevant section.

## Workflow

Pick the mode that matches the request. If it's unclear, start with step 1: without a diagnosis, any "optimisation" is guesswork.

### 1. Diagnose (always first)

1. **Decide the target engines.** Google and Bing by default (Bing's index also feeds Microsoft Copilot and other products); add others when the market calls for them. Read `references/engines/README.md`: for every change, apply the core practice **and** the engine layers, and when engines disagree follow the conflict-resolution rule there (do both → stricter wins → user-facing truth wins → document the trade-off).
2. **Understand the project.** Stack (`package.json`, `composer.json`, `astro.config.*`, `wp-config.php`…), production domain, target language(s) and country(ies), business type (local, e-commerce, SaaS, publisher, services) and whether the site is already live.
3. **Audit what is live** if there is a reachable URL:
   ```bash
   python3 "${CLAUDE_SKILL_DIR}/scripts/seo_audit.py" https://example.com --crawl 50 --output seo-report.md
   ```
   If the site isn't in production yet, run a production build locally (`npm run build && npm start` — not the dev server, which doesn't reflect minification, caching or real headers) and audit `http://localhost:3000`.
4. **Audit the code**: where `<title>`, meta description, canonical, sitemap, robots, JSON-LD, redirects and headers are generated. Look for pages rendered only on the client (content missing from `curl -s URL`).
5. **Ask for what you cannot know**: Search Console and Bing Webmaster Tools access (exports of "Performance" and "Page indexing"), real business data (legal name, address, phone, opening hours, real reviews), competitors the user considers benchmarks. **Never invent business data, reviews, authors or figures** to fill Schema or content: it is deceptive, and fake reviews are illegal in the EU, the UK and the US.

### 2. Prioritised plan

Deliver findings ordered by **impact × ease**, not by practice number. Typical order:

1. **Indexing blockers** (accidental noindex, robots.txt blocking, canonical to another URL, JavaScript-only content, 5xx errors, redirect chains, broken sitemap). A single blocker cancels everything else.
2. **Technical fundamentals** (HTTPS, mobile, Core Web Vitals, unique titles and descriptions, one H1, internal linking, basic Organization/WebSite structured data).
3. **Content and intent** (which pages are missing for the searches that matter, which pages cannibalise each other, which content is weak).
4. **Authority and growth** (links, brand, E-E-A-T, internationalisation, automation).

Plan format:

```markdown
# SEO plan — example.com
## Summary (3-5 lines: current state, the most serious problem, the biggest opportunity)
## Blockers (fix now)
| # | Problem | Evidence | Practice | Fix | Effort |
## High / medium / low priority (same table)
## What we will NOT do, and why (practices that don't apply here)
## How we will measure (KPIs and review date)
```

The "what we will NOT do" section matters: a good SEO also says which textbook items don't apply (hreflang on a single-language site, Google Business Profile for a SaaS with no physical location, etc.).

### 3. Implement

- Read the stack reference (`nextjs.md` or `other-stacks.md`) before touching code. Use the framework's native APIs (e.g. the Next.js Metadata API) instead of hand-written loose tags: they stay consistent and avoid duplicates.
- **Centralise** SEO configuration (base URL, site name, locale, organisation data) in a single module and reuse it, so you never end up with canonicals on different hosts or inconsistent brand names.
- Small, verifiable changes: one group of practices per commit, with a message that cites the numbers (`seo: absolute canonicals and dynamic sitemap (#2, #18)`).
- Don't break what works: before changing URLs, build the 301 redirect map; before adding `noindex`, check in Search Console that those pages don't bring traffic.

### 4. Verify (mandatory)

Don't assume an SEO change works because the code compiles. Verify each one with evidence:

- Re-run `${CLAUDE_SKILL_DIR}/scripts/seo_audit.py` and compare with the first audit.
- `curl -sI URL` for headers and redirects; `curl -s URL | grep -iE "<title|canonical|robots|ld\+json"` to confirm the important bits are in the served HTML (not only after JavaScript runs).
- JSON-LD: valid JSON (the script checks this) and, with internet access, recommend running the URL through Google's Rich Results Test and the schema.org validator.
- Performance: `npx lighthouse URL --only-categories=performance,seo,accessibility --output=json` if Lighthouse is available. Remind the user that field data (CrUX, the Search Console Core Web Vitals report) is what counts and takes ~28 days to reflect changes.

### 5. Follow up

Leave the user with: what to check in Search Console and Bing Webmaster Tools (including AI Performance citations) and when (indexing: 1–2 weeks; rankings: 4–12 weeks; authority: months), and the recurring tasks (monthly audit, quarterly refresh of pillar content, broken-link review). If asked, automate them (see 120, 123, 131, 152).

## Realistic expectations

State these up front, because timelines are where SEO disappoints most:

- A new domain can take days to weeks to get indexed and **months** to rank for competitive queries. The three phases are a logical order of work, not a guaranteed calendar.
- No technique "forces" Google to index or rank a page. You make its job easier and give it reasons.
- Google rewrites titles and descriptions when it thinks they don't describe the page well; a good title makes that less likely, it doesn't prevent it.

## Principles (and why)

1. **First make it possible for Google; then make Google want it.** Crawlability and indexability before content; content before links. Building backlinks to pages that can't be indexed is money thrown away.
2. **The served HTML is the truth.** Whatever isn't in the server's initial response (or takes long to render) is fragile for Google and practically invisible to many AI crawlers, which don't execute JavaScript. Server-side rendering or static generation for everything indexable.
3. **One URL, one intent, one canonical version.** Most "we don't rank" problems on mid-size sites are duplicates, cannibalisation or uncontrolled parameters.
4. **Write for the answer, not for the keyword.** AI search engines cite passages that answer on their own, precisely and verifiably. That is exactly what classic ranking rewards too.
5. **Nothing you couldn't show a search-engine reviewer.** If a tactic requires hiding something (hidden text, fake reviews, bought links, different content for bots, mass-produced unreviewed content, dates changed without real changes), don't do it. Since May 2026 Google explicitly applies its spam policies to AI Overviews and AI Mode as well, including cloaking aimed at AI crawlers and inauthentic brand mentions; Bing's guidelines name prompt injection and AI manipulation outright.
6. **Satisfy every target engine.** The core works everywhere; where engines differ, do what satisfies all of them (e.g. 301 rather than long-lived 302s for Bing, `hreflang` plus `lang` for Bing, no `noarchive` on content meant for Copilot).
7. **Measure before and after.** Every significant recommendation needs a metric and a baseline; otherwise nobody will know whether it worked.

## Always avoid

- Recommending anything listed in `references/myths.md` (Indexing API for regular pages, bumping publish dates without real changes, pre-emptive disavows, expecting FAQ rich results or star ratings for your own business, fake urgency or scarcity…).
- Mass-generating AI content to "cover keywords" without human review or original value: that is the definition of *scaled content abuse*.
- Adding `noindex`, editing `robots.txt`, deleting pages or changing URLs in production without the user's confirmation: these changes take weeks to undo.
- Blocking CSS/JS in robots.txt, putting `loading="lazy"` on the main image (hurts LCP), or using `robots.txt` to "de-index" (it doesn't; for that use `noindex` on a crawlable URL).
- Filling Schema with data that isn't visible on the page.

## When the user just wants a quick answer

Not everything needs the full workflow. For specific questions ("how long should a title be?", "should paginated pages have a canonical?"), answer directly from the relevant practice and cite its number so they can dig deeper.
