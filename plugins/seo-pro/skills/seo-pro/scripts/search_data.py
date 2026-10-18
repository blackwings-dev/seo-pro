#!/usr/bin/env python3
"""
search_data.py — pull and compare search data from Google Search Console and Bing Webmaster Tools.
Python 3.9+ standard library only. Part of the seo-pro skill by blackwings.dev — MIT License.

Authentication (never paste secrets into chat or commit them):
  Google  — an OAuth access token with scope https://www.googleapis.com/auth/webmasters.readonly in GSC_ACCESS_TOKEN.
            e.g. gcloud auth application-default login --client-id-file=client.json \
                   --scopes=https://www.googleapis.com/auth/webmasters.readonly,https://www.googleapis.com/auth/cloud-platform
                 export GSC_ACCESS_TOKEN="$(gcloud auth application-default print-access-token)"   # valid ~1 hour
  Bing    — an API key from Bing Webmaster Tools (Settings → API Access → API Key) in BING_API_KEY.

Usage:
  python3 search_data.py gsc-sites
  python3 search_data.py gsc-query --site sc-domain:example.com --start 2026-07-01 --end 2026-09-30 \
          --dimensions page,query --type web --out gsc.csv [--filter "query:excludingRegex:(?i)acme"]
  python3 search_data.py gsc-inspect --site https://example.com/ --urls urls.txt --out inspect.csv
  python3 search_data.py gsc-sitemaps --site sc-domain:example.com
  python3 search_data.py bing --method GetPageStats --site https://example.com/ --out bing-pages.csv
  python3 search_data.py compare --before before.csv --after after.csv --key page --out delta.csv
  python3 search_data.py brand-split --input gsc.csv --brand-regex "(?i)acme ?tools|acmetools"

Data limits worth stating in any report: Search Console hides anonymised queries, returns top rows only and uses
Pacific Time; Bing query/page stats are weekly buckets. Clicks are not sessions (playbooks/measurement.md X5).
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone

__version__ = "1.0.0"

GSC_BASE = os.environ.get("GSC_API_BASE", "https://www.googleapis.com/webmasters/v3")
GSC_INSPECT = os.environ.get("GSC_INSPECT_URL", "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect")
BING_BASE = os.environ.get("BING_API_BASE", "https://ssl.bing.com/webmaster/api.svc/json")
GSC_TYPES = ("web", "image", "video", "news", "googleNews", "discover")
GSC_DIMS = ("query", "page", "country", "device", "searchAppearance", "date", "hour")
BING_METHODS = ("GetQueryStats", "GetPageStats", "GetRankAndTrafficStats", "GetCrawlStats", "GetUrlSubmissionQuota")


class ApiError(RuntimeError):
    pass


def _request(url: str, method: str = "GET", body: dict | None = None, headers: dict | None = None,
             retries: int = 3) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    hdrs = {"Accept": "application/json", "User-Agent": f"seo-pro-search-data/{__version__}"}
    if data is not None:
        hdrs["Content-Type"] = "application/json; charset=utf-8"
    hdrs.update(headers or {})
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                raw = r.read().decode("utf-8") or "{}"
                return json.loads(raw)
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")[:500]
            if e.code in (429, 500, 503) and attempt < retries - 1:
                time.sleep(2 ** attempt * 2)
                continue
            raise ApiError(f"HTTP {e.code} for {url.split('?')[0]}: {detail}") from None
        except urllib.error.URLError as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise ApiError(f"Network error for {url.split('?')[0]}: {e.reason}") from None
    raise ApiError("unreachable")


def _gsc_headers() -> dict:
    token = os.environ.get("GSC_ACCESS_TOKEN")
    if not token:
        raise ApiError("Set GSC_ACCESS_TOKEN to an OAuth token with the webmasters.readonly scope (see --help).")
    return {"Authorization": f"Bearer {token}"}


def _site_path(site: str) -> str:
    return urllib.parse.quote(site, safe="")


def _write_csv(rows: list[dict], out: str | None, fields: list[str] | None = None):
    fields = fields or (list(rows[0].keys()) if rows else [])
    fh = open(out, "w", newline="", encoding="utf-8") if out else sys.stdout
    w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
    if out:
        fh.close()
        print(f"{len(rows)} rows written to {out}", file=sys.stderr)


# ------------------------------------------------------------------------------------------- Google

def gsc_sites(args):
    data = _request(f"{GSC_BASE}/sites", headers=_gsc_headers())
    _write_csv(data.get("siteEntry", []), args.out, ["siteUrl", "permissionLevel"])


def gsc_sitemaps(args):
    data = _request(f"{GSC_BASE}/sites/{_site_path(args.site)}/sitemaps", headers=_gsc_headers())
    rows = []
    for s in data.get("sitemap", []):
        sub = sum(int(c.get("submitted", 0) or 0) for c in s.get("contents", []))
        rows.append({"path": s.get("path"), "lastSubmitted": s.get("lastSubmitted"), "lastDownloaded": s.get("lastDownloaded"),
                     "isPending": s.get("isPending"), "errors": s.get("errors"), "warnings": s.get("warnings"),
                     "submitted": sub})
    _write_csv(rows, args.out)


def _parse_filters(specs: list[str]) -> list[dict]:
    filters = []
    for spec in specs or []:
        dim, op, expr = spec.split(":", 2)
        if dim not in ("country", "device", "page", "query", "searchAppearance"):
            raise ApiError(f"Unsupported filter dimension: {dim}")
        filters.append({"dimension": dim, "operator": op, "expression": expr})
    return [{"groupType": "and", "filters": filters}] if filters else []


def gsc_query(args):
    dims = [d.strip() for d in args.dimensions.split(",") if d.strip()]
    bad = [d for d in dims if d not in GSC_DIMS]
    if bad:
        raise ApiError(f"Unsupported dimensions: {bad}")
    if args.type not in GSC_TYPES:
        raise ApiError(f"--type must be one of {GSC_TYPES}")
    body = {"startDate": args.start, "endDate": args.end, "dimensions": dims, "type": args.type,
            "rowLimit": min(args.row_limit, 25000), "startRow": 0, "dataState": args.data_state}
    fg = _parse_filters(args.filter)
    if fg:
        body["dimensionFilterGroups"] = fg
    if args.aggregation:
        body["aggregationType"] = args.aggregation
    url = f"{GSC_BASE}/sites/{_site_path(args.site)}/searchAnalytics/query"
    rows, page = [], 0
    while True:
        data = _request(url, "POST", body, _gsc_headers())
        batch = data.get("rows", [])
        for r in batch:
            rec = {d: k for d, k in zip(dims, r.get("keys", []))}
            rec.update({"clicks": r.get("clicks", 0), "impressions": r.get("impressions", 0),
                        "ctr": round(r.get("ctr", 0), 6), "position": round(r.get("position", 0), 2)})
            rows.append(rec)
        page += 1
        if len(batch) < body["rowLimit"] or len(rows) >= args.max_rows:
            break
        body["startRow"] += body["rowLimit"]
    _write_csv(rows[: args.max_rows], args.out, dims + ["clicks", "impressions", "ctr", "position"])


def gsc_inspect(args):
    with open(args.urls, encoding="utf-8") as fh:
        urls = [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    rows = []
    for u in urls:
        try:
            data = _request(GSC_INSPECT, "POST", {"inspectionUrl": u, "siteUrl": args.site}, _gsc_headers())
        except ApiError as e:
            rows.append({"url": u, "error": str(e)})
            continue
        res = data.get("inspectionResult", {}).get("indexStatusResult", {})
        rows.append({"url": u, "verdict": res.get("verdict"), "coverageState": res.get("coverageState"),
                     "indexingState": res.get("indexingState"), "robotsTxtState": res.get("robotsTxtState"),
                     "pageFetchState": res.get("pageFetchState"), "googleCanonical": res.get("googleCanonical"),
                     "userCanonical": res.get("userCanonical"), "lastCrawlTime": res.get("lastCrawlTime"),
                     "crawledAs": res.get("crawledAs"), "error": ""})
        time.sleep(args.pause)  # URL Inspection quota: 600/min and 2,000/day per site
    _write_csv(rows, args.out, ["url", "verdict", "coverageState", "indexingState", "robotsTxtState", "pageFetchState",
                                "googleCanonical", "userCanonical", "lastCrawlTime", "crawledAs", "error"])


# --------------------------------------------------------------------------------------------- Bing

_BING_DATE = re.compile(r"/Date\((-?\d+)([+-]\d{4})?\)/")


def _bing_value(v):
    if isinstance(v, str):
        m = _BING_DATE.search(v)
        if m:
            return datetime.fromtimestamp(int(m.group(1)) / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
    return v


def bing(args):
    key = os.environ.get("BING_API_KEY")
    if not key:
        raise ApiError("Set BING_API_KEY to your Bing Webmaster Tools API key (Settings → API Access).")
    if args.method not in BING_METHODS:
        raise ApiError(f"--method must be one of {BING_METHODS}")
    qs = urllib.parse.urlencode({"siteUrl": args.site, "apikey": key})
    data = _request(f"{BING_BASE}/{args.method}?{qs}")
    d = data.get("d", data)
    items = d if isinstance(d, list) else [d]
    rows = [{k: _bing_value(v) for k, v in (it or {}).items() if k != "__type"} for it in items]
    if args.method == "GetPageStats":
        for r in rows:
            r["Page"] = r.pop("Query", "")
    _write_csv(rows, args.out)


# ------------------------------------------------------------------------------------------ Analysis

def _load(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def _num(v) -> float:
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0


def _aggregate(rows: list[dict], key: str) -> dict:
    agg = defaultdict(lambda: {"clicks": 0.0, "impressions": 0.0, "pos_x_impr": 0.0})
    for r in rows:
        k = r.get(key, "")
        a = agg[k]
        imp = _num(r.get("impressions") or r.get("Impressions"))
        a["clicks"] += _num(r.get("clicks") or r.get("Clicks"))
        a["impressions"] += imp
        a["pos_x_impr"] += _num(r.get("position") or r.get("AvgImpressionPosition")) * imp
    return agg


def compare(args):
    """Per-key deltas between two exports (e.g. before/after a release, or old vs new URLs with --map)."""
    before, after = _aggregate(_load(args.before), args.key), _aggregate(_load(args.after), args.key)
    mapping = {}
    if args.map:
        for r in _load(args.map):
            mapping[r.get("old_url") or r.get("old")] = r.get("new_url") or r.get("new")
    rows = []
    for k in set(before) | set(after) | set(mapping):
        target = mapping.get(k, k)
        b = before.get(k, {"clicks": 0, "impressions": 0, "pos_x_impr": 0})
        a = after.get(target, {"clicks": 0, "impressions": 0, "pos_x_impr": 0})
        if args.map and k not in mapping:
            continue
        rows.append({args.key: k, "after_key": target, "clicks_before": int(b["clicks"]), "clicks_after": int(a["clicks"]),
                     "clicks_delta": int(a["clicks"] - b["clicks"]),
                     "impr_before": int(b["impressions"]), "impr_after": int(a["impressions"]),
                     "impr_delta": int(a["impressions"] - b["impressions"]),
                     "pos_before": round(b["pos_x_impr"] / b["impressions"], 2) if b["impressions"] else "",
                     "pos_after": round(a["pos_x_impr"] / a["impressions"], 2) if a["impressions"] else ""})
    rows.sort(key=lambda r: r["clicks_delta"])
    tb, ta = sum(r["clicks_before"] for r in rows), sum(r["clicks_after"] for r in rows)
    print(f"Total clicks: {tb} → {ta} ({ta - tb:+d}). Biggest losers first. Observational only: check releases, "
          "seasonality and demand before attributing a cause (playbooks/measurement.md X14).", file=sys.stderr)
    _write_csv(rows, args.out)


def brand_split(args):
    rx = re.compile(args.brand_regex)
    tot = {"brand": [0.0, 0.0], "non-brand": [0.0, 0.0]}
    for r in _load(args.input):
        q = r.get("query") or r.get("Query") or ""
        seg = "brand" if rx.search(q) else "non-brand"
        tot[seg][0] += _num(r.get("clicks") or r.get("Clicks"))
        tot[seg][1] += _num(r.get("impressions") or r.get("Impressions"))
    rows = [{"segment": s, "clicks": int(c), "impressions": int(i), "ctr": round(c / i, 4) if i else ""}
            for s, (c, i) in tot.items()]
    print("Approximate: anonymised queries are missing from query-level exports (X9).", file=sys.stderr)
    _write_csv(rows, args.out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Search Console / Bing Webmaster data for seo-pro")
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("gsc-sites"); s.add_argument("--out"); s.set_defaults(fn=gsc_sites)
    s = sub.add_parser("gsc-sitemaps"); s.add_argument("--site", required=True); s.add_argument("--out"); s.set_defaults(fn=gsc_sitemaps)
    s = sub.add_parser("gsc-query")
    s.add_argument("--site", required=True, help="https://example.com/ or sc-domain:example.com")
    s.add_argument("--start", required=True); s.add_argument("--end", required=True)
    s.add_argument("--dimensions", default="page,query")
    s.add_argument("--type", default="web", help="web, image, video, news, googleNews, discover")
    s.add_argument("--filter", action="append", help="dimension:operator:expression (repeatable, ANDed)")
    s.add_argument("--aggregation", choices=["auto", "byPage", "byProperty", "byNewsShowcasePanel"])
    s.add_argument("--data-state", default="final", choices=["final", "all", "hourly_all"])
    s.add_argument("--row-limit", type=int, default=25000); s.add_argument("--max-rows", type=int, default=500000)
    s.add_argument("--out"); s.set_defaults(fn=gsc_query)
    s = sub.add_parser("gsc-inspect")
    s.add_argument("--site", required=True); s.add_argument("--urls", required=True)
    s.add_argument("--pause", type=float, default=0.2); s.add_argument("--out"); s.set_defaults(fn=gsc_inspect)
    s = sub.add_parser("bing")
    s.add_argument("--method", required=True, help=", ".join(BING_METHODS))
    s.add_argument("--site", required=True); s.add_argument("--out"); s.set_defaults(fn=bing)
    s = sub.add_parser("compare")
    s.add_argument("--before", required=True); s.add_argument("--after", required=True)
    s.add_argument("--key", default="page"); s.add_argument("--map", help="CSV old_url,new_url to compare old vs new URLs")
    s.add_argument("--out"); s.set_defaults(fn=compare)
    s = sub.add_parser("brand-split")
    s.add_argument("--input", required=True); s.add_argument("--brand-regex", required=True)
    s.add_argument("--out"); s.set_defaults(fn=brand_split)

    args = ap.parse_args(argv)
    try:
        args.fn(args)
    except ApiError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
