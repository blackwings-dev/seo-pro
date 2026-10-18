#!/usr/bin/env python3
"""
crawl_logs.py — what search engines and AI agents actually crawl, from your server logs.
Python 3.9+ standard library only. Part of the seo-pro skill by blackwings.dev — MIT License.

Reads access logs (Apache/Nginx combined or common, IIS/W3C, or JSON lines from Cloudflare Logpush,
Vercel, Fastly and similar; .gz is fine), recognises search, AI and SEO-tool crawlers by user agent,
verifies that the requests really come from their operators (published IP ranges and/or reverse DNS),
and reports per bot: hits, status codes, sections, crawl waste, daily trend, and impostors.

Usage:
  python3 crawl_logs.py access.log access.log.1.gz --output crawl.md --json crawl.json
  python3 crawl_logs.py logs/*.gz --verify ranges            # default: official IP-range files
  python3 crawl_logs.py access.log --verify dns --dns-limit 300   # reverse + forward DNS (slower)
  python3 crawl_logs.py access.log --ranges-dir ./ranges     # offline: JSON range files you downloaded
  python3 crawl_logs.py access.log --sitemap-urls urls.txt   # which sitemap URLs Googlebot never fetched
  python3 crawl_logs.py cf.jsonl --format jsonl --host www.example.com

Exit code: 0 on success, 3 on an error (missing file, nothing parseable).
Logs contain IP addresses (personal data in the EU): process them where they live, keep reports aggregated,
and don't paste raw log lines into chats or tickets.
"""
from __future__ import annotations

import argparse
import gzip
import ipaddress
import json
import os
import re
import socket
import sys
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from typing import Iterable, Optional

__version__ = "1.0.0"

# Bot catalogue. Order matters: the first pattern that matches wins (specific tokens before generic ones).
# kind: search · ai-search · ai-training · ai-user (user-triggered fetch) · seo-tool · other
# ranges: official IP-range files; rdns: reverse-DNS suffixes the operator documents.
BOTS = [
    {"name": "Google-InspectionTool", "re": r"Google-InspectionTool", "operator": "Google", "kind": "search",
     "ranges": ["google-common"], "rdns": [".googlebot.com", ".google.com"]},
    {"name": "Googlebot-Image", "re": r"Googlebot-Image", "operator": "Google", "kind": "search",
     "ranges": ["google-common"], "rdns": [".googlebot.com", ".google.com"]},
    {"name": "Googlebot-Video", "re": r"Googlebot-Video", "operator": "Google", "kind": "search",
     "ranges": ["google-common"], "rdns": [".googlebot.com", ".google.com"]},
    {"name": "Googlebot-News", "re": r"Googlebot-News", "operator": "Google", "kind": "search",
     "ranges": ["google-common"], "rdns": [".googlebot.com", ".google.com"]},
    {"name": "Storebot-Google", "re": r"Storebot-Google", "operator": "Google", "kind": "search",
     "ranges": ["google-common"], "rdns": [".googlebot.com", ".google.com"]},
    {"name": "GoogleOther", "re": r"GoogleOther", "operator": "Google", "kind": "other",
     "ranges": ["google-common"], "rdns": [".googlebot.com", ".google.com"]},
    {"name": "AdsBot-Google", "re": r"AdsBot-Google|Mediapartners-Google", "operator": "Google", "kind": "other",
     "ranges": ["google-special"], "rdns": [".google.com"]},
    {"name": "Google user fetch", "re": r"Google-Read-Aloud|FeedFetcher-Google|Google-Site-Verification|GoogleProducer|Google-PageRenderer",
     "operator": "Google", "kind": "ai-user", "ranges": ["google-user", "google-user-gcp", "google-agents"],
     "rdns": [".google.com", ".googleusercontent.com"]},
    {"name": "Googlebot", "re": r"Googlebot", "operator": "Google", "kind": "search",
     "ranges": ["google-common"], "rdns": [".googlebot.com", ".google.com"]},
    {"name": "Bingbot", "re": r"bingbot|BingPreview|msnbot", "operator": "Microsoft", "kind": "search",
     "ranges": ["bing"], "rdns": [".search.msn.com"]},
    {"name": "OAI-SearchBot", "re": r"OAI-SearchBot", "operator": "OpenAI", "kind": "ai-search", "ranges": ["openai-search"], "rdns": []},
    {"name": "ChatGPT-User", "re": r"ChatGPT-User", "operator": "OpenAI", "kind": "ai-user", "ranges": ["openai-user"], "rdns": []},
    {"name": "GPTBot", "re": r"GPTBot", "operator": "OpenAI", "kind": "ai-training", "ranges": ["openai-gptbot"], "rdns": []},
    {"name": "Claude-SearchBot", "re": r"Claude-SearchBot", "operator": "Anthropic", "kind": "ai-search", "ranges": ["anthropic"], "rdns": []},
    {"name": "Claude-User", "re": r"Claude-User", "operator": "Anthropic", "kind": "ai-user", "ranges": ["anthropic"], "rdns": []},
    {"name": "ClaudeBot", "re": r"ClaudeBot|anthropic-ai", "operator": "Anthropic", "kind": "ai-training", "ranges": ["anthropic"], "rdns": []},
    {"name": "PerplexityBot", "re": r"PerplexityBot", "operator": "Perplexity", "kind": "ai-search", "ranges": ["perplexity-bot"], "rdns": []},
    {"name": "Perplexity-User", "re": r"Perplexity-User", "operator": "Perplexity", "kind": "ai-user", "ranges": ["perplexity-user"], "rdns": []},
    {"name": "Applebot", "re": r"Applebot", "operator": "Apple", "kind": "search", "ranges": ["apple"], "rdns": [".applebot.apple.com"]},
    {"name": "DuckDuckBot", "re": r"DuckDuckBot|DuckAssistBot", "operator": "DuckDuckGo", "kind": "search", "ranges": [], "rdns": []},
    {"name": "YandexBot", "re": r"Yandex(Bot|Images|Video|Mobile|RenderResources|Additional)", "operator": "Yandex", "kind": "search",
     "ranges": [], "rdns": [".yandex.ru", ".yandex.net", ".yandex.com"]},
    {"name": "Baiduspider", "re": r"Baiduspider", "operator": "Baidu", "kind": "search", "ranges": [], "rdns": [".baidu.com", ".baidu.jp"]},
    {"name": "Yeti (Naver)", "re": r"\bYeti/", "operator": "Naver", "kind": "search", "ranges": [], "rdns": [".naver.com"]},
    {"name": "SeznamBot", "re": r"SeznamBot", "operator": "Seznam", "kind": "search", "ranges": [], "rdns": [".seznam.cz"]},
    {"name": "Qwantbot", "re": r"Qwantbot|Qwantify", "operator": "Qwant", "kind": "search", "ranges": [], "rdns": []},
    {"name": "Brave", "re": r"Bravebot", "operator": "Brave", "kind": "search", "ranges": [], "rdns": []},
    {"name": "Amazonbot", "re": r"Amazonbot", "operator": "Amazon", "kind": "ai-training", "ranges": [], "rdns": [".crawl.amazonbot.amazon"]},
    {"name": "Meta AI", "re": r"meta-externalagent|meta-externalfetcher|FacebookBot", "operator": "Meta", "kind": "ai-training", "ranges": [], "rdns": []},
    {"name": "Bytespider", "re": r"Bytespider", "operator": "ByteDance", "kind": "ai-training", "ranges": [], "rdns": []},
    {"name": "CCBot", "re": r"CCBot", "operator": "Common Crawl", "kind": "ai-training", "ranges": [], "rdns": [".crawl.commoncrawl.org"]},
    {"name": "Mistral", "re": r"MistralAI-User", "operator": "Mistral", "kind": "ai-user", "ranges": [], "rdns": []},
    {"name": "AhrefsBot", "re": r"AhrefsBot|AhrefsSiteAudit", "operator": "Ahrefs", "kind": "seo-tool", "ranges": [], "rdns": [".ahrefs.com", ".ahrefs.net"]},
    {"name": "SemrushBot", "re": r"SemrushBot|SiteAuditBot", "operator": "Semrush", "kind": "seo-tool", "ranges": [], "rdns": []},
    {"name": "MJ12bot", "re": r"MJ12bot", "operator": "Majestic", "kind": "seo-tool", "ranges": [], "rdns": []},
    {"name": "DotBot", "re": r"DotBot", "operator": "Moz", "kind": "seo-tool", "ranges": [], "rdns": []},
    {"name": "Screaming Frog", "re": r"Screaming Frog", "operator": "Screaming Frog", "kind": "seo-tool", "ranges": [], "rdns": []},
]
for _b in BOTS:
    _b["rx"] = re.compile(_b["re"], re.I)

# Official IP-range files (October 2026). Override or work offline with --ranges-dir <dir>/<key>.json.
RANGE_URLS = {
    "google-common": "https://developers.google.com/static/crawling/ipranges/common-crawlers.json",
    "google-special": "https://developers.google.com/static/crawling/ipranges/special-crawlers.json",
    "google-user": "https://developers.google.com/static/crawling/ipranges/user-triggered-fetchers-google.json",
    "google-user-gcp": "https://developers.google.com/static/crawling/ipranges/user-triggered-fetchers.json",
    "google-agents": "https://developers.google.com/static/crawling/ipranges/user-triggered-agents.json",
    "bing": "https://www.bing.com/toolbox/bingbot.json",
    "openai-search": "https://openai.com/searchbot.json",
    "openai-user": "https://openai.com/chatgpt-user.json",
    "openai-gptbot": "https://openai.com/gptbot.json",
    "anthropic": "https://claude.com/crawling/bots.json",
    "perplexity-bot": "https://www.perplexity.com/perplexitybot.json",
    "perplexity-user": "https://www.perplexity.com/perplexity-user.json",
    "apple": "https://search.developer.apple.com/applebot.json",
}
KIND_LABEL = {"search": "Search", "ai-search": "AI search", "ai-training": "AI training", "ai-user": "User-triggered fetch",
              "seo-tool": "SEO tool", "other": "Other"}
STATIC_EXT = re.compile(r"\.(css|js|mjs|map|png|jpe?g|gif|webp|avif|svg|ico|woff2?|ttf|eot|mp4|webm|pdf|zip|json|xml|txt)$", re.I)
TRACKING = re.compile(r"^(utm_\w+|gclid|gbraid|wbraid|fbclid|msclkid|mc_cid|mc_eid|_ga|igshid|yclid|srsltid)$", re.I)

# ------------------------------------------------------------------------------------------- parsing

COMBINED = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] "(?P<req>[^"]*)" (?P<status>\d{3}) (?P<bytes>\S+)'
    r'(?: "(?P<ref>[^"]*)" "(?P<ua>[^"]*)")?')
# Some proxies prepend the virtual host: "example.com:443 1.2.3.4 - - [...]"
VHOST_COMBINED = re.compile(r'^(?P<vhost>\S+) (?P<rest>\S+ \S+ \S+ \[.*)$')
JSON_KEYS = {
    "ip": ("ClientIP", "client_ip", "clientIp", "ip", "remote_addr", "remoteAddr", "c-ip", "proxyClientIp"),
    "path": ("ClientRequestURI", "ClientRequestPath", "request_uri", "requestPath", "path", "uri", "url", "cs-uri-stem"),
    "query": ("ClientRequestQuery", "query", "cs-uri-query"),
    "host": ("ClientRequestHost", "host", "request_host", "requestHost", "cs-host"),
    "status": ("EdgeResponseStatus", "OriginResponseStatus", "status", "statusCode", "status_code", "responseStatusCode", "sc-status"),
    "ua": ("ClientRequestUserAgent", "user_agent", "userAgent", "ua", "http_user_agent", "cs(User-Agent)"),
    "time": ("EdgeStartTimestamp", "timestamp", "time", "@timestamp", "date", "datetime"),
    "method": ("ClientRequestMethod", "method", "request_method", "cs-method"),
}


def _open(path: str):
    if path.endswith(".gz"):
        return gzip.open(path, "rt", encoding="utf-8", errors="replace")
    return open(path, encoding="utf-8-sig", errors="replace")


def _parse_time(s) -> Optional[datetime]:
    if s is None or s == "":
        return None
    if isinstance(s, (int, float)) or (isinstance(s, str) and s.isdigit()):
        v = float(s)
        if v > 1e17:   # nanoseconds (Cloudflare)
            v /= 1e9
        elif v > 1e14:  # microseconds
            v /= 1e6
        elif v > 1e11:  # milliseconds
            v /= 1e3
        return datetime.fromtimestamp(v, tz=timezone.utc)
    s = str(s).strip()
    for fmt in ("%d/%b/%Y:%H:%M:%S %z", "%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d %H:%M:%S"):
        try:
            d = datetime.strptime(s.replace("Z", "+0000") if fmt.endswith("%z") else s, fmt)
            return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    try:
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def _pick(obj: dict, names) -> object:
    for n in names:
        if n in obj and obj[n] not in (None, ""):
            return obj[n]
    return None


def parse_lines(lines: Iterable[str], fmt: str = "auto"):
    """Yield dicts {ip, method, path, status, ua, time, host}; None for unparseable lines."""
    w3c_fields = None
    for line in lines:
        line = line.rstrip("\n")
        if not line.strip():
            continue
        if line.startswith("#Fields:"):
            w3c_fields = line[len("#Fields:"):].split()
            continue
        if line.startswith("#"):
            continue
        if fmt in ("auto", "jsonl") and line.lstrip().startswith("{"):
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                yield None
                continue
            path = _pick(obj, JSON_KEYS["path"]) or ""
            q = _pick(obj, JSON_KEYS["query"])
            if q and "?" not in str(path):
                path = f"{path}{'' if str(q).startswith('?') else '?'}{q}"
            if str(path).startswith("http"):
                sp = urllib.parse.urlsplit(str(path))
                path = sp.path + (f"?{sp.query}" if sp.query else "")
            try:
                status = int(_pick(obj, JSON_KEYS["status"]) or 0)
            except (TypeError, ValueError):
                status = 0
            yield {"ip": str(_pick(obj, JSON_KEYS["ip"]) or ""), "method": str(_pick(obj, JSON_KEYS["method"]) or "GET"),
                   "path": str(path) or "/", "status": status, "ua": str(_pick(obj, JSON_KEYS["ua"]) or ""),
                   "time": _parse_time(_pick(obj, JSON_KEYS["time"])), "host": str(_pick(obj, JSON_KEYS["host"]) or "")}
            continue
        if w3c_fields and fmt in ("auto", "w3c"):
            parts = line.split()
            if len(parts) == len(w3c_fields):
                rec = dict(zip(w3c_fields, parts))
                path = rec.get("cs-uri-stem", "/")
                q = rec.get("cs-uri-query", "-")
                if q and q != "-":
                    path += "?" + q
                t = _parse_time(f"{rec.get('date', '')} {rec.get('time', '')}".strip())
                try:
                    status = int(rec.get("sc-status", 0))
                except ValueError:
                    status = 0
                yield {"ip": rec.get("c-ip", ""), "method": rec.get("cs-method", "GET"), "path": path, "status": status,
                       "ua": urllib.parse.unquote_plus(rec.get("cs(User-Agent)", "").replace("+", " ")), "time": t,
                       "host": rec.get("cs-host", "")}
                continue
        m = COMBINED.match(line)
        host = ""
        if not m:
            v = VHOST_COMBINED.match(line)
            if v:
                m = COMBINED.match(v.group("rest"))
                host = v.group("vhost").split(":")[0]
        if not m:
            yield None
            continue
        req = m.group("req").split()
        method, path = (req[0], req[1]) if len(req) >= 2 else ("-", "-")
        if path.startswith("http"):
            sp = urllib.parse.urlsplit(path)
            host = host or (sp.hostname or "")
            path = sp.path + (f"?{sp.query}" if sp.query else "")
        yield {"ip": m.group("ip"), "method": method, "path": path, "status": int(m.group("status")),
               "ua": m.group("ua") or "", "time": _parse_time(m.group("time")), "host": host}


def classify(ua: str) -> Optional[dict]:
    for b in BOTS:
        if b["rx"].search(ua or ""):
            return b
    return None

# ------------------------------------------------------------------------------------- verification


def _networks_from_json(data) -> list:
    """Collect every CIDR / IP string anywhere in a range file (formats differ between operators)."""
    nets, stack = [], [data]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            stack.extend(cur.values())
        elif isinstance(cur, list):
            stack.extend(cur)
        elif isinstance(cur, str) and re.fullmatch(r"[0-9a-fA-F:.]+(/\d{1,3})?", cur) and (":" in cur or "." in cur):
            try:
                nets.append(ipaddress.ip_network(cur, strict=False))
            except ValueError:
                pass
    return nets


class Verifier:
    def __init__(self, mode: str, ranges_dir: Optional[str], cache_dir: str, dns_limit: int, timeout: float):
        self.mode = mode
        self.ranges_dir = ranges_dir
        self.cache_dir = cache_dir
        self.dns_limit = dns_limit
        self.timeout = timeout
        self.networks: dict[str, list] = {}
        self.range_status: dict[str, str] = {}
        self._dns_done = 0
        self._cache: dict[tuple, Optional[bool]] = {}
        parts = [m for m in ("ranges", "dns") if mode in (m, "both")]
        if ranges_dir and "ranges" not in parts:
            parts.insert(0, "ranges")
        self.label = (" + ".join(parts) + (" (local range files)" if ranges_dir else "")) if parts else "none"

    def _load_ranges(self, key: str) -> list:
        if key in self.networks:
            return self.networks[key]
        data = None
        if self.ranges_dir:
            p = os.path.join(self.ranges_dir, f"{key}.json")
            if os.path.exists(p):
                with open(p, encoding="utf-8-sig") as fh:
                    data = json.load(fh)
                self.range_status[key] = f"local file {p}"
        if data is None and self.mode in ("ranges", "both"):
            cache = os.path.join(self.cache_dir, f"{key}.json")
            fresh = os.path.exists(cache) and time.time() - os.path.getmtime(cache) < 86400
            if fresh:
                with open(cache, encoding="utf-8") as fh:
                    data = json.load(fh)
                self.range_status[key] = "cached (<24 h)"
            else:
                try:
                    req = urllib.request.Request(RANGE_URLS[key], headers={"User-Agent": f"seo-pro-crawl-logs/{__version__}"})
                    with urllib.request.urlopen(req, timeout=self.timeout) as r:
                        raw = r.read().decode("utf-8", "replace")
                    data = json.loads(raw)
                    os.makedirs(self.cache_dir, exist_ok=True)
                    with open(cache, "w", encoding="utf-8") as fh:
                        fh.write(raw)
                    self.range_status[key] = "downloaded"
                except Exception as e:  # network blocked, file moved, not JSON
                    if os.path.exists(cache):
                        with open(cache, encoding="utf-8") as fh:
                            data = json.load(fh)
                        self.range_status[key] = f"stale cache ({type(e).__name__})"
                    else:
                        self.range_status[key] = f"unavailable ({type(e).__name__}: {str(e)[:80]})"
        self.networks[key] = _networks_from_json(data) if data is not None else []
        return self.networks[key]

    def _in_ranges(self, ip: str, keys: list) -> Optional[bool]:
        nets = [n for k in keys for n in self._load_ranges(k)]
        if not nets:
            return None
        try:
            addr = ipaddress.ip_address(ip)
        except ValueError:
            return False
        return any(addr in n for n in nets if n.version == addr.version)

    def _dns(self, ip: str, suffixes: list) -> Optional[bool]:
        if not suffixes or self._dns_done >= self.dns_limit:
            return None
        self._dns_done += 1
        old = socket.getdefaulttimeout()
        socket.setdefaulttimeout(self.timeout)
        try:
            host = socket.gethostbyaddr(ip)[0].lower().rstrip(".")
            if not any(host.endswith(s) for s in suffixes):
                return False
            forward = {ai[4][0] for ai in socket.getaddrinfo(host, None)}
            return ip in forward
        except (socket.herror, socket.gaierror, OSError):
            return False
        finally:
            socket.setdefaulttimeout(old)

    def verify(self, ip: str, bot: dict) -> Optional[bool]:
        """True = genuine, False = impostor, None = can't tell (operator publishes nothing usable)."""
        key = (ip, bot["name"])
        if key in self._cache:
            return self._cache[key]
        res = None
        if self.mode in ("ranges", "both") or self.ranges_dir:
            if bot["ranges"]:
                res = self._in_ranges(ip, bot["ranges"])
        if (res is None or (res is False and self.mode == "both")) and self.mode in ("dns", "both"):
            d = self._dns(ip, bot["rdns"])
            res = d if d is not None else res
        self._cache[key] = res
        return res

# ------------------------------------------------------------------------------------------- analysis


def _section(path: str) -> str:
    p = path.split("?", 1)[0]
    seg = [s for s in p.split("/") if s]
    if not seg:
        return "/"
    if STATIC_EXT.search(p):
        return "(static assets)"
    return f"/{seg[0]}/" if len(seg) > 1 or p.endswith("/") else f"/{seg[0]}"


def _param_kind(path: str) -> str:
    if "?" not in path:
        return ""
    keys = [k for k, _ in urllib.parse.parse_qsl(path.split("?", 1)[1], keep_blank_values=True)]
    if keys and all(TRACKING.match(k) for k in keys):
        return "tracking"
    return "parameters"


class Analysis:
    def __init__(self):
        self.total = 0
        self.unparsed = 0
        self.first: Optional[datetime] = None
        self.last: Optional[datetime] = None
        self.bots: dict[str, dict] = {}
        self.human_hits = 0
        self.impostor_ips: Counter = Counter()

    def bot(self, b: dict) -> dict:
        if b["name"] not in self.bots:
            self.bots[b["name"]] = {"operator": b["operator"], "kind": b["kind"], "hits": 0, "verified": 0, "impostor": 0,
                                    "unknown": 0, "status": Counter(), "sections": Counter(), "urls": Counter(),
                                    "days": Counter(), "waste": Counter(), "params": Counter(), "ips": set(),
                                    "ok_paths": set()}
        return self.bots[b["name"]]


def analyze(records, verifier: Verifier, host: str = "") -> Analysis:
    a = Analysis()
    for r in records:
        a.total += 1
        if r is None:
            a.unparsed += 1
            continue
        if host and r["host"] and r["host"].lower() != host.lower():
            continue
        t = r["time"]
        if t:
            a.first = t if a.first is None or t < a.first else a.first
            a.last = t if a.last is None or t > a.last else a.last
        b = classify(r["ua"])
        if not b:
            a.human_hits += 1
            continue
        s = a.bot(b)
        v = verifier.verify(r["ip"], b)
        if v is False:
            s["impostor"] += 1
            a.impostor_ips[(r["ip"], b["name"])] += 1
            continue  # impostors are reported apart and excluded from the bot's crawl figures
        s["verified" if v else "unknown"] += 1
        s["hits"] += 1
        s["ips"].add(r["ip"])
        st = r["status"]
        s["status"][f"{st // 100}xx" if st else "?"] += 1
        path = r["path"] or "/"
        s["sections"][_section(path)] += 1
        s["urls"][path] += 1
        if 200 <= st < 300:
            s["ok_paths"].add(path.split("?", 1)[0])
        if t:
            s["days"][t.strftime("%Y-%m-%d")] += 1
        pk = _param_kind(path)
        if pk:
            for k, _ in urllib.parse.parse_qsl(path.split("?", 1)[1], keep_blank_values=True):
                s["params"][k] += 1
        if 300 <= st < 400:
            s["waste"]["redirects (3xx)"] += 1
        elif st in (404, 410):
            s["waste"]["not found (404/410)"] += 1
        elif 400 <= st < 500:
            s["waste"]["other 4xx"] += 1
        elif st >= 500:
            s["waste"]["server errors (5xx)"] += 1
        elif pk == "tracking":
            s["waste"]["tracking-parameter URLs"] += 1
        elif pk:
            s["waste"]["other parameter URLs"] += 1
    return a

# -------------------------------------------------------------------------------------------- report


def _pct(n, d) -> str:
    return f"{(100 * n / d):.1f}%" if d else "—"


def render_markdown(a: Analysis, verifier: Verifier, files: list, sitemap_urls: Optional[set]) -> str:
    span = f"{a.first:%Y-%m-%d %H:%M} → {a.last:%Y-%m-%d %H:%M} UTC" if a.first and a.last else "unknown"
    bot_hits = sum(s["hits"] for s in a.bots.values())
    imp = sum(s["impostor"] for s in a.bots.values())
    L = [f"# Crawl log analysis", "",
         f"_Generated {time.strftime('%Y-%m-%d %H:%M')} by crawl_logs.py {__version__} (seo-pro) · files: {len(files)} · "
         f"verification: {verifier.label}_", "",
         "| | |", "|---|---|",
         f"| Period | {span} |", f"| Lines read | {a.total:,} |", f"| Unparsed lines | {a.unparsed:,} ({_pct(a.unparsed, a.total)}) |",
         f"| Requests from recognised bots | {bot_hits:,} |", f"| Requests with a bot user agent from the wrong IPs (impostors) | {imp:,} |",
         f"| Other requests (people, unrecognised agents) | {a.human_hits:,} |", ""]
    if a.unparsed and a.unparsed > 0.2 * max(a.total, 1):
        L += ["> ⚠️ More than 20% of lines couldn't be parsed. Check the log format (`--format`) before trusting the figures.", ""]

    L += ["## Bots", "", "| Bot | Operator | Kind | Hits | Share of bot hits | Verified | Not verifiable | Impostor hits | 2xx | 3xx | 4xx | 5xx | Unique URLs |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    order = sorted(a.bots.items(), key=lambda kv: -(kv[1]["hits"] + kv[1]["impostor"]))
    for name, s in order:
        L.append(f"| {name} | {s['operator']} | {KIND_LABEL[s['kind']]} | {s['hits']:,} | {_pct(s['hits'], bot_hits)} | "
                 f"{s['verified']:,} | {s['unknown']:,} | {s['impostor']:,} | {s['status'].get('2xx', 0):,} | {s['status'].get('3xx', 0):,} | "
                 f"{s['status'].get('4xx', 0):,} | {s['status'].get('5xx', 0):,} | {len(s['urls']):,} |")
    L += ["", "_Impostor hits are excluded from every other figure. \"Not verifiable\" means the operator publishes no IP ranges "
          "or reverse-DNS rule the tool could use (or `--verify none`): treat those as claimed, not proven._", ""]

    kinds = Counter()
    for s in a.bots.values():
        kinds[s["kind"]] += s["hits"]
    if kinds:
        L += ["## By purpose", "", "| Purpose | Hits | Share |", "|---|---|---|"]
        L += [f"| {KIND_LABEL[k]} | {v:,} | {_pct(v, bot_hits)} |" for k, v in kinds.most_common()]
        L += ["", "_Search agents decide whether you can appear; training agents don't; user-triggered fetches happen when "
              "someone asks an assistant about a page (`engines/ai-search.md` A2)._", ""]

    for name in ("Googlebot", "Bingbot"):
        s = a.bots.get(name)
        if not s or not s["hits"]:
            continue
        waste = sum(s["waste"].values())
        L += [f"## {name}", "", f"- Hits: {s['hits']:,} · unique URLs: {len(s['urls']):,} · distinct IPs: {len(s['ips']):,}",
              f"- Crawl spent on redirects, errors and parameter URLs: **{waste:,} ({_pct(waste, s['hits'])})**", ""]
        if s["waste"]:
            L += ["| Where crawl goes to waste | Hits | Share of this bot's hits |", "|---|---|---|"]
            L += [f"| {k} | {v:,} | {_pct(v, s['hits'])} |" for k, v in s["waste"].most_common()]
            L.append("")
        L += ["| Section | Hits | Share |", "|---|---|---|"]
        L += [f"| `{k}` | {v:,} | {_pct(v, s['hits'])} |" for k, v in s["sections"].most_common(15)]
        L += ["", "| Most-crawled URL | Hits |", "|---|---|"]
        L += [f"| `{k[:120]}` | {v:,} |" for k, v in s["urls"].most_common(15)]
        if s["params"]:
            L += ["", "| Parameter | Hits |", "|---|---|"]
            L += [f"| `{k}` | {v:,} |" for k, v in s["params"].most_common(15)]
        L.append("")

    ai = [(n, s) for n, s in order if s["kind"].startswith("ai") and s["hits"]]
    if ai:
        L += ["## AI agents", "", "| Agent | Kind | Hits | Top section | Most-fetched URL |", "|---|---|---|---|---|"]
        for n, s in ai:
            sec = s["sections"].most_common(1)[0][0] if s["sections"] else ""
            url = s["urls"].most_common(1)[0][0][:90] if s["urls"] else ""
            L.append(f"| {n} | {KIND_LABEL[s['kind']]} | {s['hits']:,} | `{sec}` | `{url}` |")
        L += ["", "_Compare with your robots.txt decisions: an AI search agent that never visits can't cite you; a training "
              "agent you meant to block that still gets 200s means the block isn't working (A2, A7)._", ""]

    days = sorted({d for s in a.bots.values() for d in s["days"]})
    top = [n for n, s in order if s["hits"]][:6]
    if days and top:
        L += ["## Daily hits", "", "| Day | " + " | ".join(top) + " |", "|---|" + "---|" * len(top)]
        for d in days[-62:]:
            L.append(f"| {d} | " + " | ".join(f"{a.bots[n]['days'].get(d, 0):,}" for n in top) + " |")
        L.append("")

    if sitemap_urls is not None and "Googlebot" in a.bots:
        crawled = a.bots["Googlebot"]["ok_paths"]
        never = sorted(u for u in sitemap_urls if u not in crawled)
        extra = sorted({u for u in crawled if u not in sitemap_urls and not STATIC_EXT.search(u)})
        L += ["## Sitemap coverage (Googlebot)", "",
              f"- Sitemap URLs: {len(sitemap_urls):,} · fetched by Googlebot in this period: {len(sitemap_urls) - len(never):,} "
              f"({_pct(len(sitemap_urls) - len(never), len(sitemap_urls))})",
              f"- Never fetched with a 200: {len(never):,} · pages crawled with a 200 but missing from the sitemap: {len(extra):,}", ""]
        if never:
            L += ["Never fetched (first 30):", ""] + [f"- `{u}`" for u in never[:30]] + [""]
        if extra:
            L += ["Crawled but not in the sitemap (first 30):", ""] + [f"- `{u}`" for u in extra[:30]] + [""]

    if a.impostor_ips:
        L += ["## Impostors", "", "| IP | Claimed bot | Hits |", "|---|---|---|"]
        L += [f"| {ip} | {b} | {n:,} |" for (ip, b), n in a.impostor_ips.most_common(20)]
        L += ["", "_A bot user agent from an IP outside the operator's published ranges. Rate-limit or block these at the "
              "WAF by IP + user agent; never block the real operator ranges (A7)._", ""]

    if verifier.range_status:
        L += ["## Verification sources", "", "| Range file | Status |", "|---|---|"]
        L += [f"| {k} ({RANGE_URLS.get(k, '')}) | {v} |" for k, v in sorted(verifier.range_status.items())]
        L.append("")
    L += ["---", "Read with `references/phase-3-authority.md` 124 (log analysis), 20 (parameters), 23 (redirects), "
          "`engines/ai-search.md` A2/A7 and `playbooks/programmatic.md` (crawl at scale). Logs show requests, not indexing "
          "or rankings: confirm with Search Console and Bing Webmaster Tools crawl reports."]
    return "\n".join(L) + "\n"


def to_json(a: Analysis, verifier: Verifier) -> dict:
    out = {"total_lines": a.total, "unparsed": a.unparsed, "other_requests": a.human_hits,
           "first": a.first.isoformat() if a.first else None, "last": a.last.isoformat() if a.last else None,
           "verification": verifier.label, "range_status": verifier.range_status, "bots": {},
           "impostors": [{"ip": ip, "bot": b, "hits": n} for (ip, b), n in a.impostor_ips.most_common(200)]}
    for n, s in a.bots.items():
        out["bots"][n] = {"operator": s["operator"], "kind": s["kind"], "hits": s["hits"], "verified": s["verified"],
                          "not_verifiable": s["unknown"], "impostor_hits": s["impostor"], "status": dict(s["status"]),
                          "waste": dict(s["waste"]), "sections": dict(s["sections"].most_common(50)),
                          "top_urls": dict(s["urls"].most_common(100)), "params": dict(s["params"].most_common(50)),
                          "days": dict(sorted(s["days"].items())), "unique_urls": len(s["urls"]), "distinct_ips": len(s["ips"])}
    return out

# ---------------------------------------------------------------------------------------------- main


def main(argv=None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="Search and AI crawler analysis from server logs (seo-pro by blackwings.dev)")
    ap.add_argument("files", nargs="+", help="Access log files (.gz accepted)")
    ap.add_argument("--format", choices=["auto", "combined", "jsonl", "w3c"], default="auto")
    ap.add_argument("--verify", choices=["ranges", "dns", "both", "none"], default="ranges",
                    help="ranges = official IP-range files (default); dns = reverse + forward DNS; both; none")
    ap.add_argument("--ranges-dir", help="Directory with range files named <key>.json (offline use); keys: " + ", ".join(RANGE_URLS))
    ap.add_argument("--cache-dir", default=os.path.join(os.path.expanduser("~"), ".cache", "seo-pro", "ranges"))
    ap.add_argument("--dns-limit", type=int, default=500, help="Maximum DNS verifications (distinct IP + bot pairs)")
    ap.add_argument("--timeout", type=float, default=15)
    ap.add_argument("--host", help="Only count requests for this host (logs that record it)")
    ap.add_argument("--sitemap-urls", help="File with one URL or path per line: report which ones Googlebot never fetched")
    ap.add_argument("--output", help="Write the Markdown report here")
    ap.add_argument("--json", help="Write the figures as JSON here")
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = ap.parse_args(argv)

    verifier = Verifier(args.verify, args.ranges_dir, args.cache_dir, args.dns_limit, args.timeout)

    def records():
        for f in args.files:
            with _open(f) as fh:
                yield from parse_lines(fh, args.format)

    a = analyze(records(), verifier, args.host or "")
    if a.total == 0 or a.total == a.unparsed:
        print("error: no parseable log lines (check --format)", file=sys.stderr)
        return 3
    sm = None
    if args.sitemap_urls:
        with open(args.sitemap_urls, encoding="utf-8-sig") as fh:
            sm = set()
            for line in fh:
                u = line.strip()
                if u and not u.startswith("#"):
                    sm.add((urllib.parse.urlsplit(u).path or "/") if u.startswith("http") else u.split("?", 1)[0])
    report = render_markdown(a, verifier, args.files, sm)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(report)
        print(f"Report written to {args.output}")
    else:
        print(report)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(to_json(a, verifier), fh, ensure_ascii=False, indent=2)
    return 0


def _main_safe(argv=None) -> int:
    try:
        return main(argv)
    except KeyboardInterrupt:
        return 130
    except Exception as e:
        print(f"error: {type(e).__name__}: {e}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(_main_safe())
