---
description: Cluster keywords by shared Google top-10 URLs using real DataForSEO data (volume, ideas, SERPs), with no invented numbers
argument-hint: <seed keywords, comma-separated | file with one keyword per line> [--location-code 2724 --language-code es]
---

Build keyword clusters for `$ARGUMENTS` with the **seo-pro** skill. Load the skill first and follow practices 45, 46 and 54 in `references/phase-2-content.md`. Volumes, SERPs and clusters come from `keyword_data.py`; you only interpret them. You may name a cluster or suggest a page for it, but never add volumes, difficulty or URLs the script did not return.

Needs `DATAFORSEO_LOGIN` and `DATAFORSEO_PASSWORD` (API credentials, paid per request). Never print them or write them to a file. Defaults are Spain and Spanish (`--location-code 2724`, `--language-code es`); ask if the market is unclear.

1. **Read the input.** A path means a keyword file; otherwise treat it as comma-separated seeds. Write the keywords to a file if there are more than a few.
2. **Always dry-run first** and show the user what will be sent and the cap (`--max-keywords`, default 200; the script refuses longer lists, do not raise it without asking):
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/keyword_data.py" kw-cluster --keywords-file kws.txt --dry-run
   ```
   Each keyword costs one SERP request. Tell the user the number of requests and ask before spending when it is more than about 25. The script prints the cost DataForSEO reports after every call; quote it, do not estimate it.
3. **If only seeds were given, expand them** (a paid call, confirm first):
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/keyword_data.py" kw-ideas --keywords "seed one,seed two" --min-volume 10 --out ideas.csv
   ```
   Let the user pick or trim the list before the SERP step.
4. **Volumes, then SERPs, then clusters:**
   ```bash
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/keyword_data.py" kw-volume --keywords-file kws.txt --out volume.csv
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/keyword_data.py" serp --keywords-file kws.txt --format json --out serps.json
   python3 "${CLAUDE_PLUGIN_ROOT}/skills/seo-pro/scripts/keyword_data.py" kw-cluster --serp-file serps.json --volumes volume.csv --min-shared 3 --out clusters.json
   ```
   Saving the SERPs means a different `--min-shared` can be tried without paying again.
5. **Present the result** as a table: cluster (head keyword), keywords, total volume, shared URLs. Then:
   - Clusters with several keywords: one page per cluster is the default; a keyword with no SERP overlap is a separate intent and needs its own page (practice 54).
   - Flag clusters marked `no_serp` (no organic results, so no evidence to group) and keywords whose volume is empty (Google Ads has no data; that is not zero).
   - Say what the method does not prove: overlap is evidence that Google treats keywords as one intent at one moment, in one location; volumes are rounded monthly averages that group close variants.
6. Offer the next step: a keyword-to-URL map, or `/seo-pro:brief` for the head keyword of a cluster.
