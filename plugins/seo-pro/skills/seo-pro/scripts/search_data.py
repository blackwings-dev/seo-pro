#!/usr/bin/env python3
"""
search_data.py — pull and compare search data from Google Search Console and Bing Webmaster Tools,
and field Core Web Vitals from PageSpeed Insights and the Chrome UX Report (CrUX).
Python 3.9+ standard library only. Part of the seo-pro skill by blackwings.dev — MIT License.

Authentication (never paste secrets into chat or commit them):
  Google  — an OAuth access token with scope https://www.googleapis.com/auth/webmasters.readonly in GSC_ACCESS_TOKEN.
            e.g. gcloud auth application-default login --client-id-file=client.json \
                   --scopes=https://www.googleapis.com/auth/webmasters.readonly,https://www.googleapis.com/auth/cloud-platform
                 export GSC_ACCESS_TOKEN="$(gcloud auth application-default print-access-token)"   # valid ~1 hour
  Bing    — an API key from Bing Webmaster Tools (Settings → API Access → API Key) in BING_API_KEY.
  CrUX    — a Google Cloud API key with the Chrome UX Report API enabled in CRUX_API_KEY (required).
  PSI     — optional PSI_API_KEY (PageSpeed Insights works without a key at a low shared quota).

Usage:
  python3 search_data.py gsc-sites
  python3 search_data.py gsc-query --site sc-domain:example.com --start 2026-07-01 --end 2026-09-30 \
          --dimensions page,query --type web --out gsc.csv [--filter "query:excludingRegex:(?i)acme"]
  python3 search_data.py gsc-inspect --site https://example.com/ --urls urls.txt --out inspect.csv
  python3 search_data.py gsc-sitemaps --site sc-domain:example.com
  python3 search_data.py bing --method GetPageStats --site https://example.com/ --out bing-pages.csv
  python3 search_data.py compare --before before.csv --after after.csv --key page --out delta.csv
  python3 search_data.py brand-split --input gsc.csv --brand-regex "(?i)acme ?tools|acmetools"
  python3 search_data.py crux --origin https://example.com --form-factor PHONE
  python3 search_data.py crux --urls templates.txt --form-factor PHONE --fallback-origin --out crux.csv
  python3 search_data.py crux --url https://example.com/product/x --history --out crux-history.csv
  python3 search_data.py psi --urls templates.txt --strategy mobile --out psi.csv

Data limits worth stating in any report: Search Console hides anonymised queries, returns top rows only and uses
Pacific Time; Bing query/page stats are weekly buckets. Clicks are not sessions (playbooks/measurement.md X5).
CrUX is a 28-day rolling p75 of real Chrome users, only for pages and origins with enough traffic; PSI lab scores are one
simulated load and are not what Google uses (practice 6).
"""
from __future__ import annotations

import argparse
import csv
import http.client
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timedelta, timezone

__version__ = "1.1.0"

GSC_BASE = os.environ.get("GSC_API_BASE", "https://www.googleapis.com/webmasters/v3")
GSC_INSPECT = os.environ.get("GSC_INSPECT_URL", "https://searchconsole.googleapis.com/v1/urlInspection/index:inspect")
BING_BASE = os.environ.get("BING_API_BASE", "https://ssl.bing.com/webmaster/api.svc/json")
GSC_TYPES = ("web", "image", "video", "news", "googleNews", "discover")
GSC_DIMS = ("query", "page", "country", "device", "searchAppearance", "date", "hour")
BING_METHODS = ("GetQueryStats", "GetPageStats", "GetRankAndTrafficStats", "GetCrawlStats", "GetUrlSubmissionQuota")
CRUX_BASE = os.environ.get("CRUX_API_BASE", "https://chromeuxreport.googleapis.com/v1")
PSI_BASE = os.environ.get("PSI_API_BASE", "https://www.googleapis.com/pagespeedonline/v5/runPagespeed")
# Core Web Vitals thresholds at p75 (good ≤ first, poor > second). CLS is unitless.
CWV = {"largest_contentful_paint": ("LCP_ms", 2500, 4000), "interaction_to_next_paint": ("INP_ms", 200, 500),
       "cumulative_layout_shift": ("CLS", 0.1, 0.25), "first_contentful_paint": ("FCP_ms", 1800, 3000),
       "experimental_time_to_first_byte": ("TTFB_ms", 800, 1800)}
CORE = ("largest_contentful_paint", "interaction_to_next_paint", "cumulative_layout_shift")


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
                raw = r.read().decode("utf-8", "replace") or "{}"
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                raise ApiError(f"Non-JSON response from {url.split('?')[0]}: {raw[:200]!r}") from None
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
        except (TimeoutError, http.client.HTTPException, ConnectionError) as e:
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
                continue
            raise ApiError(f"Network error for {url.split('?')[0]}: {type(e).__name__}: {e}") from None
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
    if not out and hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", newline="")  # Windows consoles: no \r\r\n, no cp1252
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
    with open(args.urls, encoding="utf-8-sig") as fh:
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
            tz = timezone.utc
            if m.group(2):  # the offset tells which local day the value refers to
                sign = 1 if m.group(2)[0] == "+" else -1
                tz = timezone(sign * timedelta(hours=int(m.group(2)[1:3]), minutes=int(m.group(2)[3:5])))
            return datetime.fromtimestamp(int(m.group(1)) / 1000, tz=tz).strftime("%Y-%m-%d")
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


# ------------------------------------------------------------------------------------ Core Web Vitals

def _rating(metric: str, v) -> str:
    if v is None or v == "":
        return ""
    _, good, poor = CWV[metric]
    v = float(v)
    return "good" if v <= good else ("poor" if v > poor else "needs improvement")


def _targets(args) -> list[tuple[str, str]]:
    out = []
    if getattr(args, "origin", None):
        out.append(("origin", args.origin.rstrip("/")))
    if getattr(args, "url", None):
        out.append(("url", args.url))
    if getattr(args, "urls", None):
        with open(args.urls, encoding="utf-8-sig") as fh:
            out += [("url", l.strip()) for l in fh if l.strip() and not l.startswith("#")]
    if not out:
        raise ApiError("Give --origin, --url or --urls.")
    return out


def _origin_of(url: str) -> str:
    sp = urllib.parse.urlsplit(url)
    return f"{sp.scheme}://{sp.netloc}"


def _crux_query(endpoint: str, scope: str, target: str, form_factor: str, extra: dict | None = None) -> dict | None:
    key = os.environ.get("CRUX_API_KEY")
    if not key:
        raise ApiError("Set CRUX_API_KEY to a Google Cloud API key with the Chrome UX Report API enabled.")
    body = {scope: target, "metrics": list(CWV)}
    if form_factor != "ALL":
        body["formFactor"] = form_factor
    body.update(extra or {})
    try:
        return _request(f"{CRUX_BASE}/records:{endpoint}?key={urllib.parse.quote(key)}", "POST", body)
    except ApiError as e:
        if "HTTP 404" in str(e):  # not enough Chrome users for this page/origin and form factor
            return None
        raise


def _period(p: dict) -> str:
    def d(x):
        return f"{x.get('year')}-{x.get('month'):02d}-{x.get('day'):02d}" if x else ""
    return f"{d(p.get('firstDate'))}..{d(p.get('lastDate'))}"


def crux(args):
    """Field Core Web Vitals (p75 of real Chrome users, 28-day rolling) per URL or origin."""
    rows = []
    for scope, target in _targets(args):
        if args.history:
            data = _crux_query("queryHistoryRecord", scope, target, args.form_factor,
                               {"collectionPeriodCount": args.periods})
            if not data:
                rows.append({"target": target, "scope": scope, "form_factor": args.form_factor, "note": "no CrUX data"})
                continue
            rec = data.get("record", {})
            periods = rec.get("collectionPeriods", [])
            for i, p in enumerate(periods):
                row = {"target": target, "scope": scope, "form_factor": args.form_factor, "period": _period(p)}
                for m, (col, _, _) in CWV.items():
                    series = rec.get("metrics", {}).get(m, {}).get("percentilesTimeseries", {}).get("p75s", [])
                    v = series[i] if i < len(series) else None
                    row[col] = v if v is not None else ""
                    row[col + "_rating"] = _rating(m, v)
                rows.append(row)
            continue
        data = _crux_query("queryRecord", scope, target, args.form_factor)
        used_scope, used_target = scope, target
        if not data and scope == "url" and args.fallback_origin:
            used_scope, used_target = "origin", _origin_of(target)
            data = _crux_query("queryRecord", used_scope, used_target, args.form_factor)
        if not data:
            rows.append({"target": target, "scope": scope, "form_factor": args.form_factor,
                         "note": "no CrUX data (not enough Chrome traffic)"})
            continue
        rec = data.get("record", {})
        row = {"target": target, "scope": used_scope + (" (fallback)" if used_scope != scope else ""),
               "form_factor": args.form_factor, "period": _period(rec.get("collectionPeriod", {}))}
        passes = True
        for m, (col, _, _) in CWV.items():
            met = rec.get("metrics", {}).get(m)
            v = met.get("percentiles", {}).get("p75") if met else None
            row[col] = v if v is not None else ""
            row[col + "_rating"] = _rating(m, v)
            if m in CORE and row[col + "_rating"] != "good":
                passes = False
            if met and met.get("histogram"):
                row[col + "_good_share"] = round(float(met["histogram"][0].get("density", 0) or 0), 4)
        row["core_web_vitals"] = "pass" if passes else "fail"
        rows.append(row)
        time.sleep(args.pause)  # CrUX quota: 150 queries/minute per project
    cols = ["target", "scope", "form_factor", "period"]
    for col, _, _ in CWV.values():
        cols += [col, col + "_rating"] + ([] if args.history else [col + "_good_share"])
    cols += ([] if args.history else ["core_web_vitals"]) + ["note"]
    print("CrUX = p75 of real Chrome users over 28 days; pages without enough traffic have no data. "
          "A pass needs LCP, INP and CLS all good (practice 6).", file=sys.stderr)
    _write_csv(rows, args.out, cols)


PSI_FIELD = {"LARGEST_CONTENTFUL_PAINT_MS": ("LCP_ms", 1), "INTERACTION_TO_NEXT_PAINT": ("INP_ms", 1),
             "CUMULATIVE_LAYOUT_SHIFT_SCORE": ("CLS", 100), "FIRST_CONTENTFUL_PAINT_MS": ("FCP_ms", 1),
             "EXPERIMENTAL_TIME_TO_FIRST_BYTE": ("TTFB_ms", 1)}
PSI_CAT = {"FAST": "good", "AVERAGE": "needs improvement", "SLOW": "poor"}


def psi(args):
    """PageSpeed Insights: field data (CrUX, page or origin) plus one Lighthouse lab run per URL and strategy."""
    key = os.environ.get("PSI_API_KEY")
    strategies = ["mobile", "desktop"] if args.strategy == "both" else [args.strategy]
    rows = []
    for scope, target in _targets(args):
        if scope == "origin":
            target = target + "/"
        for strat in strategies:
            qs = [("url", target), ("strategy", strat), ("category", "performance")]
            if key:
                qs.append(("key", key))
            try:
                data = _request(f"{PSI_BASE}?{urllib.parse.urlencode(qs)}")
            except ApiError as e:
                rows.append({"url": target, "strategy": strat, "note": str(e)[:200]})
                continue
            row = {"url": target, "strategy": strat}
            le = data.get("loadingExperience") or {}
            src = "page"
            if not le.get("metrics"):
                le, src = data.get("originLoadingExperience") or {}, "origin"
            row["field_scope"] = src if le.get("metrics") else "none"
            for k, (col, div) in PSI_FIELD.items():
                met = (le.get("metrics") or {}).get(k)
                if met:
                    v = met.get("percentile")
                    row[col] = round(v / div, 3) if div != 1 else v
                    row[col + "_rating"] = PSI_CAT.get(met.get("category"), met.get("category", ""))
            row["field_overall"] = PSI_CAT.get(le.get("overall_category", ""), le.get("overall_category", ""))
            lh = data.get("lighthouseResult") or {}
            perf = (lh.get("categories") or {}).get("performance", {}).get("score")
            row["lab_performance_score"] = round(perf * 100) if isinstance(perf, (int, float)) else ""
            audits = lh.get("audits") or {}
            for aid, col in (("largest-contentful-paint", "lab_LCP_ms"), ("cumulative-layout-shift", "lab_CLS"),
                             ("total-blocking-time", "lab_TBT_ms")):
                nv = (audits.get(aid) or {}).get("numericValue")
                row[col] = round(nv, 3) if isinstance(nv, (int, float)) else ""
            rows.append(row)
            time.sleep(args.pause)
    cols = ["url", "strategy", "field_scope"]
    for col, _ in PSI_FIELD.values():
        cols += [col, col + "_rating"]
    cols += ["field_overall", "lab_performance_score", "lab_LCP_ms", "lab_CLS", "lab_TBT_ms", "note"]
    print("Field data (real users) decides Core Web Vitals; the lab score is one simulated load for debugging only.",
          file=sys.stderr)
    _write_csv(rows, args.out, cols)


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
            old = (r.get("old_url") or r.get("old") or "").strip()
            if old and not old.startswith("#"):
                mapping[old] = (r.get("new_url") or r.get("new") or "").strip()
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
    s = sub.add_parser("crux", help="Field Core Web Vitals from the Chrome UX Report API (CRUX_API_KEY)")
    s.add_argument("--origin"); s.add_argument("--url"); s.add_argument("--urls", help="File with one URL per line")
    s.add_argument("--form-factor", default="PHONE", choices=["PHONE", "DESKTOP", "TABLET", "ALL"])
    s.add_argument("--fallback-origin", action="store_true", help="Use origin data when a URL has none")
    s.add_argument("--history", action="store_true", help="Weekly p75 time series (CrUX History API)")
    s.add_argument("--periods", type=int, default=25, help="History periods, 1-40 (default 25)")
    s.add_argument("--pause", type=float, default=0.5); s.add_argument("--out"); s.set_defaults(fn=crux)
    s = sub.add_parser("psi", help="PageSpeed Insights field + lab data (optional PSI_API_KEY)")
    s.add_argument("--origin"); s.add_argument("--url"); s.add_argument("--urls", help="File with one URL per line")
    s.add_argument("--strategy", default="mobile", choices=["mobile", "desktop", "both"])
    s.add_argument("--pause", type=float, default=1.0); s.add_argument("--out"); s.set_defaults(fn=psi)

    args = ap.parse_args(argv)
    try:
        args.fn(args)
    except ApiError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
    except (OSError, ValueError) as e:  # missing files, bad CSV/filters: exit 3, distinct from API errors (2)
        print(f"error: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(3)
