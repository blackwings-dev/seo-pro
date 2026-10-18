# Changelog

## 1.2.0 — unreleased

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
