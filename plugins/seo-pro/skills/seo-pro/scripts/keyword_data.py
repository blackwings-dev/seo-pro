#!/usr/bin/env python3
"""
keyword_data.py — keyword volume, ideas, live Google SERPs and SERP-overlap clustering from the DataForSEO API.
Python 3.9+ standard library only. Part of the seo-pro skill by blackwings.dev — MIT License.

Every number comes from the API response; nothing is estimated or filled in by the script. Keywords without data
are returned with empty values, never with a guess.

Authentication (never paste secrets into chat or commit them):
  DataForSEO — DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD (the API credentials from app.dataforseo.com/api-access,
               not the account login) in the environment. HTTP basic auth.

Usage:
  python3 keyword_data.py kw-volume --keywords "seo tools,seo audit" [--keywords-file kws.txt] [--out volume.csv]
  python3 keyword_data.py kw-ideas --keywords "seo audit" --limit 200 --out ideas.csv
  python3 keyword_data.py serp --keywords-file kws.txt --format json --out serps.json
  python3 keyword_data.py kw-cluster --serp-file serps.json --volumes volume.csv --min-shared 3 --out clusters.json
  python3 keyword_data.py kw-cluster --keywords-file kws.txt --format csv --out clusters.csv   # fetches the SERPs itself
  Add --dry-run to any call to see the requests that would be sent (no credentials, no network, no cost).

Common options: --location-code (default 2724, Spain) and --language-code (default es); --max-keywords (default 200)
refuses a list longer than the cap instead of silently truncating it. The cost reported by DataForSEO is printed to
stderr after every request and in total (USD, as returned by the API). Live endpoints are rate limited by DataForSEO
(Google Ads live: 12 requests per minute); the script pauses between batches (--pause).

Limits worth stating in any report: Google Ads volumes are monthly averages, rounded, and group close variants;
CPC and competition are paid-search metrics, not organic difficulty; a live SERP is one moment, one location, one
language and one device. Since 31/10/2026 SERP Live returns google.com/goto?url= wrappers for part of the results
(about half, sometimes all): `serp` asks DataForSEO to resolve them (resolve_goto_urls, adds up to 40 s per request;
--no-resolve-goto turns it off). A wrapper that stays opaque is kept with unresolved=true and left out of the
clustering, which reports how many URLs it excluded. Clustering is deterministic (no LLM): keywords whose top 10 share at least --min-shared
URLs are grouped, which is evidence that Google treats them as one intent, not a guarantee.
"""
from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import search_data as _sd  # noqa: E402  (shared HTTP client with retries and CSV writer)

__version__ = "1.0.0"

DFS_BASE = os.environ.get("DATAFORSEO_API_BASE", "https://api.dataforseo.com/v3")
EP_VOLUME = "/keywords_data/google_ads/search_volume/live"
EP_IDEAS = "/dataforseo_labs/google/keyword_ideas/live"
EP_SERP = "/serp/google/organic/live/advanced"
VOLUME_BATCH = 1000   # DataForSEO limit per search_volume request
IDEAS_SEEDS = 200     # DataForSEO limit of seed keywords per keyword_ideas request
ApiError = _sd.ApiError


# ------------------------------------------------------------------------------------------- helpers

def is_goto(url: str) -> bool:
    """True for a Google goto wrapper (google.* host, path /goto), whatever the format of its url parameter."""
    try:
        p = urllib.parse.urlsplit(url or "")
    except ValueError:
        return False
    host = (p.hostname or "").lower()
    return (host == "google.com" or host.startswith("google.") or host.endswith(".google.com")
            or host.startswith("www.google.")) and p.path.rstrip("/") == "/goto"


def unwrap_goto(url: str) -> str:
    """google.com/goto?url=<real> (and country domains) -> the real URL; anything else is returned unchanged."""
    if not url:
        return url
    try:
        p = urllib.parse.urlsplit(url)
    except ValueError:
        return url
    if is_goto(url):
        target = urllib.parse.parse_qs(p.query).get("url", [""])[0]
        if target.startswith(("http://", "https://")):
            return target
    return url


def norm_url(url: str) -> str:
    """Key used to compare URLs across SERPs: scheme-insensitive, no www., no fragment, no trailing slash."""
    p = urllib.parse.urlsplit(unwrap_goto(url).strip())
    host = (p.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = p.path.rstrip("/")
    return host + path + (f"?{p.query}" if p.query else "")


def _host(url: str) -> str:
    return (urllib.parse.urlsplit(url).hostname or "").lower()


def read_keywords(args) -> list[str]:
    """Keywords from --keywords (comma separated) and --keywords-file (one per line); lowercase, unique, ordered."""
    raw: list[str] = []
    if getattr(args, "keywords", None):
        raw += args.keywords.split(",")
    if getattr(args, "keywords_file", None):
        with open(args.keywords_file, encoding="utf-8-sig") as fh:
            raw += fh.read().splitlines()
    seen, out = set(), []
    for k in raw:
        k = " ".join(k.strip().lower().split())
        if k and not k.startswith("#") and k not in seen:
            seen.add(k)
            out.append(k)
    return out


def check_cap(keywords: list[str], cap: int):
    if not keywords:
        raise ApiError("No keywords: pass --keywords and/or --keywords-file.")
    if len(keywords) > cap:
        raise ApiError(f"{len(keywords)} keywords exceed --max-keywords {cap}. Raise the cap on purpose or split the list "
                       "(every extra keyword has a cost).")


def _auth() -> dict:
    login, pw = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not pw:
        raise ApiError("Set DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD (API credentials from app.dataforseo.com/api-access).")
    token = base64.b64encode(f"{login}:{pw}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


class Meter:
    """Adds up the `cost` DataForSEO returns and prints it; never estimates."""

    def __init__(self):
        self.total = 0.0
        self.requests = 0

    def post(self, endpoint: str, task: dict, label: str) -> list[dict]:
        data = _sd._request(DFS_BASE + endpoint, "POST", [task], _auth(), timeout=300 if task.get("resolve_goto_urls") else 60)
        self.requests += 1
        cost = data.get("cost")
        if isinstance(cost, (int, float)):
            self.total += cost
            print(f"[{label}] cost: ${cost:.4f}", file=sys.stderr)
        if data.get("status_code") not in (None, 20000):
            raise ApiError(f"DataForSEO {data.get('status_code')}: {data.get('status_message')}")
        tasks = data.get("tasks") or []
        for t in tasks:
            if t.get("status_code") != 20000:
                raise ApiError(f"DataForSEO task {t.get('status_code')}: {t.get('status_message')}")
        return tasks

    def summary(self):
        print(f"total cost: ${self.total:.4f} in {self.requests} request(s) (as reported by DataForSEO)", file=sys.stderr)


def _loc(args) -> dict:
    return {"location_code": args.location_code, "language_code": args.language_code}


def _dry(args, plan: list[tuple[str, dict]]) -> bool:
    if not args.dry_run:
        return False
    for ep, task in plan:
        shown = dict(task)
        for k in ("keywords",):
            if k in shown:
                shown[k] = f"[{len(shown[k])} keywords: {', '.join(shown[k][:5])}{'…' if len(shown[k]) > 5 else ''}]"
        print(f"DRY RUN  POST {DFS_BASE}{ep}  {json.dumps(shown, ensure_ascii=False)}", file=sys.stderr)
    print(f"DRY RUN  {len(plan)} request(s); nothing sent, nothing charged.", file=sys.stderr)
    return True


# ------------------------------------------------------------------------------------------- parsers

def parse_volume(tasks: list[dict]) -> list[dict]:
    rows = []
    for t in tasks:
        for r in t.get("result") or []:
            rows.append({"keyword": r.get("keyword"), "search_volume": r.get("search_volume"), "cpc": r.get("cpc"),
                         "competition": r.get("competition"), "competition_index": r.get("competition_index"),
                         "low_top_of_page_bid": r.get("low_top_of_page_bid"),
                         "high_top_of_page_bid": r.get("high_top_of_page_bid")})
    return rows


def parse_ideas(tasks: list[dict]) -> list[dict]:
    rows = []
    for t in tasks:
        for res in t.get("result") or []:
            for it in res.get("items") or []:
                ki = it.get("keyword_info") or {}
                kp = it.get("keyword_properties") or {}
                si = it.get("search_intent_info") or {}
                rows.append({"keyword": it.get("keyword"), "search_volume": ki.get("search_volume"), "cpc": ki.get("cpc"),
                             "competition": ki.get("competition"), "competition_level": ki.get("competition_level"),
                             "keyword_difficulty": kp.get("keyword_difficulty"), "main_intent": si.get("main_intent")})
    return rows


def parse_serp(tasks: list[dict], keyword: str, top: int = 10) -> list[dict]:
    """Organic results only (position = rank_group), goto wrappers unwrapped, repeated URLs kept once."""
    rows, seen = [], set()
    for t in tasks:
        for res in t.get("result") or []:
            for it in res.get("items") or []:
                if it.get("type") != "organic" or not it.get("url"):
                    continue
                pos = it.get("rank_group")
                if not isinstance(pos, int) or pos > top:
                    continue
                url = unwrap_goto(it["url"])
                unresolved = is_goto(url)
                key = url if unresolved else norm_url(url)
                if key in seen:
                    continue
                seen.add(key)
                rows.append({"keyword": keyword, "position": pos, "url": url, "title": it.get("title"),
                             "domain": "" if unresolved else (_host(url) or it.get("domain")), "unresolved": unresolved})
    rows.sort(key=lambda r: r["position"])
    return rows


# ------------------------------------------------------------------------------------------- clustering

def cluster_keywords(serps: dict[str, list[str]], min_shared: int = 3, volumes: dict[str, float] | None = None) -> list[dict]:
    """Group keywords whose SERPs share at least `min_shared` URLs. Pure and deterministic.

    Greedy around a head keyword (highest volume, then alphabetical): every unassigned keyword that shares
    >= min_shared URLs with the head joins its cluster. Members are never chained through each other, so one
    ambiguous keyword cannot glue two intents together. A keyword with an empty SERP is its own cluster, flagged
    `no_serp`, because there is no evidence to group it. Unresolved goto wrappers are opaque tokens, not pages: they
    are dropped before comparing and counted in `unresolved_excluded`. Shared URLs are those that appear in at least two
    SERPs of the cluster, most repeated first.
    """
    volumes = volumes or {}
    min_shared = max(1, int(min_shared))
    excluded = {k: sum(1 for u in urls if u and is_goto(unwrap_goto(u))) for k, urls in serps.items()}
    serps = {k: [unwrap_goto(u) for u in urls if u and not is_goto(unwrap_goto(u))] for k, urls in serps.items()}
    sets = {k: {norm_url(u) for u in urls} for k, urls in serps.items()}
    raw = {k: {norm_url(u): u for u in urls} for k, urls in serps.items()}
    order = sorted(sets, key=lambda k: (-(volumes.get(k) or 0), k))
    assigned: set[str] = set()
    out: list[dict] = []
    for head in order:
        if head in assigned:
            continue
        assigned.add(head)
        members = [head]
        if sets[head]:
            for other in order:
                if other not in assigned and len(sets[head] & sets[other]) >= min_shared:
                    assigned.add(other)
                    members.append(other)
        counts: dict[str, int] = {}
        for m in members:
            for u in sets[m]:
                counts[u] = counts.get(u, 0) + 1
        shared = sorted((u for u, c in counts.items() if c >= 2), key=lambda u: (-counts[u], u))
        shared_urls = [next(raw[m][u] for m in members if u in raw[m]) for u in shared]
        vols = [volumes.get(m) for m in members]
        out.append({"cluster": head, "keywords": members, "keyword_count": len(members),
                    "total_volume": int(sum(v for v in vols if v)) if any(v is not None for v in vols) else None,
                    "shared_urls": shared_urls, "no_serp": not sets[head],
                    "unresolved_excluded": sum(excluded[m] for m in members)})
    out.sort(key=lambda c: (-(c["total_volume"] or 0), -c["keyword_count"], c["cluster"]))
    return out


# ------------------------------------------------------------------------------------------- commands

def _emit(rows: list[dict], args, fields: list[str]):
    if args.format == "json":
        text = json.dumps(rows, ensure_ascii=False, indent=2)
        if args.out:
            with open(args.out, "w", encoding="utf-8") as fh:
                fh.write(text + "\n")
            print(f"{len(rows)} rows written to {args.out}", file=sys.stderr)
        else:
            if hasattr(sys.stdout, "reconfigure"):
                sys.stdout.reconfigure(encoding="utf-8")
            print(text)
    else:
        _sd._write_csv(rows, args.out, fields)


def kw_volume(args) -> int:
    kws = read_keywords(args)
    check_cap(kws, args.max_keywords)
    batches = [kws[i:i + VOLUME_BATCH] for i in range(0, len(kws), VOLUME_BATCH)]
    plan = [(EP_VOLUME, {"keywords": b, **_loc(args)}) for b in batches]
    if _dry(args, plan):
        return 0
    meter, rows = Meter(), []
    for i, (ep, task) in enumerate(plan):
        if i:
            time.sleep(args.pause)
        rows += parse_volume(meter.post(ep, task, f"kw-volume {i + 1}/{len(plan)}"))
    meter.summary()
    _emit(rows, args, ["keyword", "search_volume", "cpc", "competition", "competition_index",
                       "low_top_of_page_bid", "high_top_of_page_bid"])
    return 0


def kw_ideas(args) -> int:
    seeds = read_keywords(args)
    check_cap(seeds, min(args.max_keywords, IDEAS_SEEDS))
    task = {"keywords": seeds, **_loc(args), "limit": args.limit, "include_serp_info": False}
    if args.min_volume:
        task["filters"] = ["keyword_info.search_volume", ">=", args.min_volume]
    if _dry(args, [(EP_IDEAS, task)]):
        return 0
    meter = Meter()
    rows = parse_ideas(meter.post(EP_IDEAS, task, "kw-ideas"))
    meter.summary()
    _emit(rows, args, ["keyword", "search_volume", "cpc", "competition", "competition_level",
                       "keyword_difficulty", "main_intent"])
    return 0


def _serp_task(k: str, args) -> dict:
    task = {"keyword": k, **_loc(args), "depth": 10}
    if not getattr(args, "no_resolve_goto", False):
        task["resolve_goto_urls"] = True  # DataForSEO resolves goto wrappers; adds up to 40 s per request
    return task


def fetch_serps(kws: list[str], args, meter: Meter) -> dict[str, list[dict]]:
    out = {}
    for i, k in enumerate(kws):
        if i:
            time.sleep(args.pause)
        task = _serp_task(k, args)
        out[k] = parse_serp(meter.post(EP_SERP, task, f"serp {i + 1}/{len(kws)}"), k)
    return out


def serp(args) -> int:
    kws = read_keywords(args)
    check_cap(kws, args.max_keywords)
    plan = [(EP_SERP, _serp_task(k, args)) for k in kws]
    if _dry(args, plan):
        return 0
    meter = Meter()
    data = fetch_serps(kws, args, meter)
    meter.summary()
    bad = sum(1 for rows in data.values() for r in rows if r["unresolved"])
    if bad:
        print(f"warning: {bad} result(s) still unresolved goto wrappers (unresolved=true); they are excluded from "
              "kw-cluster.", file=sys.stderr)
    if args.format == "json":
        _emit([{"keyword": k, "results": rows} for k, rows in data.items()], args, [])
    else:
        _emit([r for rows in data.values() for r in rows], args,
              ["keyword", "position", "url", "title", "domain", "unresolved"])
    return 0


def _load_serps(path: str) -> dict[str, list[str]]:
    """Accepts the JSON written by `serp --format json` or the CSV written by `serp` (keyword,position,url,...)."""
    with open(path, encoding="utf-8-sig") as fh:
        text = fh.read()
    serps: dict[str, list[str]] = {}
    if text.lstrip().startswith(("[", "{")):
        data = json.loads(text)
        if isinstance(data, dict):  # {keyword: [urls]} or {keyword: [{url:..}]}
            data = [{"keyword": k, "results": v} for k, v in data.items()]
        for item in data:
            res = item.get("results") or []
            serps[item["keyword"].lower()] = [r["url"] if isinstance(r, dict) else r for r in res]
    else:
        for r in csv.DictReader(text.splitlines()):
            serps.setdefault((r.get("keyword") or "").lower(), []).append(r.get("url") or "")
    serps.pop("", None)
    return serps


def _load_volumes(path: str) -> dict[str, float]:
    vols = {}
    with open(path, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            try:
                vols[(r.get("keyword") or "").lower()] = float(r.get("search_volume") or "")
            except ValueError:
                continue
    return vols


def kw_cluster(args) -> int:
    if args.serp_file:
        serps = _load_serps(args.serp_file)
        if not serps:
            raise ApiError(f"No SERPs found in {args.serp_file}.")
        check_cap(sorted(serps), args.max_keywords)
        meter = None
    else:
        kws = read_keywords(args)
        check_cap(kws, args.max_keywords)
        if _dry(args, [(EP_SERP, _serp_task(k, args)) for k in kws]):
            return 0
        meter = Meter()
        serps = {k: [r["url"] for r in rows] for k, rows in fetch_serps(kws, args, meter).items()}
        meter.summary()
    volumes = _load_volumes(args.volumes) if args.volumes else {}
    clusters = cluster_keywords(serps, args.min_shared, volumes)
    skipped = sum(c["unresolved_excluded"] for c in clusters)
    if skipped:
        print(f"warning: {skipped} unresolved goto URL(s) excluded from the overlap; clusters may be under-merged "
              "(re-run `serp`, or without --no-resolve-goto).", file=sys.stderr)
    if args.format == "csv":
        rows = [{"cluster": c["cluster"], "keywords": " | ".join(c["keywords"]), "keyword_count": c["keyword_count"],
                 "total_volume": c["total_volume"], "shared_urls": " | ".join(c["shared_urls"]),
                 "no_serp": c["no_serp"], "unresolved_excluded": c["unresolved_excluded"]} for c in clusters]
        _sd._write_csv(rows, args.out, ["cluster", "keywords", "keyword_count", "total_volume", "shared_urls", "no_serp",
                                        "unresolved_excluded"])
    else:
        _emit(clusters, args, [])
    return 0


# ------------------------------------------------------------------------------------------- CLI

def _common(s, fmt_default: str):
    s.add_argument("--keywords", help="comma-separated keywords")
    s.add_argument("--keywords-file", help="text file, one keyword per line")
    s.add_argument("--location-code", type=int, default=2724, help="DataForSEO location code (default 2724, Spain)")
    s.add_argument("--language-code", default="es", help="language code (default es)")
    s.add_argument("--max-keywords", type=int, default=200, help="refuse a longer list (default 200)")
    s.add_argument("--dry-run", action="store_true", help="show the requests, send nothing, charge nothing")
    s.add_argument("--pause", type=float, default=5.0, help="seconds between requests (default 5)")
    s.add_argument("--format", choices=("csv", "json"), default=fmt_default)
    s.add_argument("--out")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Keyword data from DataForSEO (DATAFORSEO_LOGIN / DATAFORSEO_PASSWORD)")
    ap.add_argument("--version", action="version", version=f"keyword_data {__version__}")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("kw-volume", help="search volume, CPC and competition (Google Ads, live)")
    _common(s, "csv")
    s.set_defaults(fn=kw_volume)
    s = sub.add_parser("kw-ideas", help="keyword ideas from seeds (DataForSEO Labs keyword_ideas)")
    _common(s, "csv")
    s.add_argument("--limit", type=int, default=100, help="ideas to return (default 100, max 1000)")
    s.add_argument("--min-volume", type=int, default=0, help="drop ideas below this monthly volume")
    s.set_defaults(fn=kw_ideas)
    s = sub.add_parser("serp", help="organic top 10 for each keyword (Google SERP live advanced)")
    _common(s, "csv")
    s.add_argument("--no-resolve-goto", action="store_true", help="do not ask DataForSEO to resolve google.com/goto "
                   "wrappers (faster, but about half the URLs stay opaque)")
    s.set_defaults(fn=serp)
    s = sub.add_parser("kw-cluster", help="cluster keywords by shared top-10 URLs (deterministic)")
    _common(s, "json")
    s.add_argument("--no-resolve-goto", action="store_true", help="when fetching SERPs: do not resolve goto wrappers")
    s.add_argument("--serp-file", help="SERPs from `serp` (JSON or CSV); without it the SERPs are fetched (cost)")
    s.add_argument("--volumes", help="CSV from kw-volume (keyword, search_volume) to order clusters and add volume")
    s.add_argument("--min-shared", type=int, default=3, help="shared top-10 URLs needed to group (default 3)")
    s.set_defaults(fn=kw_cluster)
    args = ap.parse_args(argv)
    try:
        return args.fn(args) or 0
    except ApiError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
