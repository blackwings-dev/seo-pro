---
description: Audit a URL with the seo-pro auditor and summarise the findings by priority, citing the script output
argument-hint: <url> [--crawl N]
---

Run a technical SEO check on `$ARGUMENTS` with the **seo-pro** skill. Load the skill first; its `references/` hold the practices the findings cite. Do not score, grade or estimate anything the script did not compute.

1. If `$ARGUMENTS` has no URL, ask for one and stop. Audit only sites the user owns or may test.
2. Run the auditor on the URL. Add `--render` when the page looks like a JavaScript app (React, Vue, Angular, Next.js client components, an almost empty `curl -s URL`) and Playwright is installed; if `--render` fails because Playwright is missing, say so and run it without. Pass through any extra options the user wrote (e.g. `--crawl 50`).
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/seo_audit.py" $ARGUMENTS --render --output seo-report.md --json seo-report.json
   ```
3. Read `seo-report.md` (and the JSON when you need a detail). Summarise in the user's language:
   - **Blockers** (critical findings: indexing, robots, canonical, 5xx, redirects) first, then warnings, then notes, as the script classifies them.
   - Per finding: what was observed (quote the script line or value), the practice number the script cites, and the fix. Group repeated findings into one line with the count.
   - Anything the script did not measure (field Core Web Vitals, rankings, backlinks, indexing in Search Console) goes under "not verified", with the tool that would measure it (`search_data.py crux`, `gsc-inspect`).
4. Suggest, do not apply: changes to `robots.txt`, `noindex`, redirects or URLs need the user's confirmation.
5. Close with the exact command to re-run the audit after the fixes.
