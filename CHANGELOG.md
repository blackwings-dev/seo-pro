# Changelog

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
