---
description: Content brief for a target keyword built from the real Google top 10 (titles, URLs, intent) and Search Console data when available
argument-hint: <target keyword> [--location-code 2724 --language-code es]
---

Write a content brief for `$ARGUMENTS` with the **seo-pro** skill. Load the skill first and follow practices 42 and 55 in `references/phase-2-content.md` (intent, then brief). The SERP and the numbers come from the scripts; anything you did not measure is labelled **assumption** in the brief. Never invent volumes, competitors, rankings or quotes.

Needs `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD` (paid per request; never print them). Defaults are Spain and Spanish (`--location-code 2724`, `--language-code es`); ask if the market is unclear. The steps below make three paid requests: say so before running them.

1. **Measure the keyword and its neighbours:**
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/keyword_data.py" kw-volume --keywords "target keyword" --out volume.csv
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/keyword_data.py" kw-ideas --keywords "target keyword" --limit 30 --min-volume 10 --out ideas.csv
   ```
2. **Get the real top 10:**
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/keyword_data.py" serp --keywords "target keyword" --format json --out serp.json
   ```
3. **Read the competing pages** (the top results, at least 5) with `curl -s URL` or a fetch tool: headings (H1 to H3), format, depth, what they answer first, structured data present. Record only what you actually read; if a page cannot be fetched, say so.
4. **Search Console, only if the user can provide it** (`GSC_ACCESS_TOKEN`): the queries and pages the site already gets for this topic, to avoid cannibalisation (practice 46):
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/search_data.py" gsc-query --site sc-domain:example.com --start YYYY-MM-DD --end YYYY-MM-DD --dimensions page,query --out gsc.csv
   ```
   If there is no token, write "not measured: no Search Console data".
5. **Write the brief** with these sections:
   - **Keyword data**: volume, CPC and competition as returned (empty means no data, not zero), related ideas worth covering.
   - **Intent**, read from the SERP: what types of pages rank (guides, product pages, tools, forums), with the evidence (titles and URLs). State the main intent and any secondary one.
   - **SERP table**: position, domain, title, URL, format.
   - **Outline**: H1 and H2s that cover what the ranking pages cover, plus gaps you observed; each item marked `seen in N of 10` or `assumption`.
   - **Required elements**: facts the page must support with sources, internal links to add, structured data that fits (see `/seo-pro:schema`), who should author or review it (practice 55; YMYL topics also need the regulated layer).
   - **Do not**: copy competitors, pad to a word count, or promise a ranking.
   - **Assumptions and unknowns**, listed apart.
