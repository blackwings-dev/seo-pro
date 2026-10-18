#!/usr/bin/env python3
"""
seo_audit.py — dependency-free technical SEO audit (Python 3.9+ standard library only).

Part of the seo-pro skill by blackwings.dev — https://github.com/blackwings-dev/seo-pro
MIT License.

Audits a URL (and optionally crawls the site) and produces a Markdown/JSON report whose
findings cite the practice numbers in the skill's reference files.

Usage:
  python3 seo_audit.py https://example.com
  python3 seo_audit.py https://example.com --crawl 100 --output report.md --json report.json
  python3 seo_audit.py --urls critical.txt --fail-on critical        # for alerts in CI/cron
  python3 seo_audit.py http://localhost:3000 --crawl 50 --skip-variants

Exit code: 0 when there are no findings at the --fail-on level (default "none"), 1 when there are,
2 when the start URL could not be fetched.
"""
from __future__ import annotations

import argparse
import gzip
import json
import re
import socket
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict, deque
from dataclasses import dataclass, field, asdict
from html.parser import HTMLParser
from typing import Optional
from xml.etree import ElementTree

__version__ = "1.2.0"

UA_DEFAULT = ("Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0 Mobile Safari/537.36 (compatible; seo-pro-audit/1.0)")
AI_BOTS = ["Googlebot", "Bingbot", "OAI-SearchBot", "PerplexityBot", "Claude-SearchBot",
           "Google-Extended", "GPTBot", "ClaudeBot", "CCBot",
           "ChatGPT-User", "Perplexity-User", "Claude-User"]
BOT_PURPOSE = {"Googlebot": "search (also Google AI features)", "Bingbot": "search (also Copilot)",
               "OAI-SearchBot": "AI search (ChatGPT)", "PerplexityBot": "AI search (Perplexity)",
               "Claude-SearchBot": "AI search (Claude)", "Google-Extended": "training / AI use (no Search effect)",
               "GPTBot": "training (OpenAI)", "ClaudeBot": "training (Anthropic)", "CCBot": "training (Common Crawl)",
               "ChatGPT-User": "user fetch (robots may not apply)", "Perplexity-User": "user fetch (generally ignores robots)",
               "Claude-User": "user fetch (Claude)"}
SEARCH_AI_BOTS = ("OAI-SearchBot", "PerplexityBot", "Claude-SearchBot")
SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}
SEV_LABEL = {"critical": "🔴 Critical", "warning": "🟠 Warning", "info": "🔵 Info"}

# --------------------------------------------------------------------------------------------- HTTP


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: D401
        return None


def _is_local(host: str) -> bool:
    host = (host or "").lower()
    return host in ("localhost", "127.0.0.1", "::1", "[::1]") or host.endswith(".localhost") or host.endswith(".test")


_ctx = ssl.create_default_context()
_OPENER_PROXY = urllib.request.build_opener(_NoRedirect(), urllib.request.HTTPSHandler(context=_ctx))
_OPENER_DIRECT = urllib.request.build_opener(_NoRedirect(), urllib.request.ProxyHandler({}),
                                             urllib.request.HTTPSHandler(context=_ctx))


@dataclass
class Response:
    url: str
    status: int
    headers: dict
    body: bytes
    elapsed: float
    error: Optional[str] = None

    def header(self, name: str) -> str:
        return self.headers.get(name.lower(), "")


def fetch(url: str, ua: str, timeout: float, method: str = "GET", extra_headers: Optional[dict] = None,
          max_bytes: int = 5_000_000) -> Response:
    host = urllib.parse.urlsplit(url).hostname or ""
    opener = _OPENER_DIRECT if _is_local(host) else _OPENER_PROXY
    headers = {"User-Agent": ua, "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Encoding": "gzip", "Accept-Language": "en;q=0.9,*;q=0.5"}
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, headers=headers, method=method)
    t0 = time.monotonic()
    try:
        resp = opener.open(req, timeout=timeout)
        status, hdrs, raw = resp.status, resp.headers, resp.read(max_bytes)
    except urllib.error.HTTPError as e:  # 3xx (not followed), 4xx, 5xx
        status, hdrs = e.code, e.headers
        try:
            raw = e.read(max_bytes)
        except Exception:  # pragma: no cover
            raw = b""
    except (urllib.error.URLError, socket.timeout, ssl.SSLError, ConnectionError, OSError) as e:
        reason = getattr(e, "reason", e)
        return Response(url, 0, {}, b"", time.monotonic() - t0, error=str(reason))
    elapsed = time.monotonic() - t0
    hmap = {k.lower(): v for k, v in hdrs.items()} if hdrs else {}
    if hmap.get("content-encoding", "").lower() == "gzip" and raw:
        try:
            raw = gzip.decompress(raw)
        except OSError:
            pass
    return Response(url, status, hmap, raw, elapsed)


def fetch_follow(url: str, ua: str, timeout: float, max_hops: int = 10):
    """Follow redirects manually. Returns (final_response, chain[(url, status)])."""
    chain = []
    current = url
    seen = set()
    r = None
    for _ in range(max_hops + 1):
        r = fetch(current, ua, timeout)
        chain.append((current, r.status if not r.error else f"ERROR: {r.error}"))
        if r.error or r.status not in (301, 302, 303, 307, 308):
            return r, chain
        loc = r.header("location")
        if not loc:
            return r, chain
        nxt = urllib.parse.urljoin(current, loc)
        if nxt in seen:
            chain.append((nxt, "LOOP"))
            return r, chain
        seen.add(current)
        current = nxt
    return r, chain


def decode_body(r: Response) -> str:
    ctype = r.header("content-type")
    m = re.search(r"charset=([\w-]+)", ctype or "", re.I)
    enc = m.group(1) if m else "utf-8"
    try:
        return r.body.decode(enc, errors="replace")
    except LookupError:
        return r.body.decode("utf-8", errors="replace")

# ------------------------------------------------------------------------------------- HTML parsing


VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = None
        self._in_title = False
        self.metas = []          # attribute dicts
        self.links = []          # <link>
        self.anchors = []        # (href, rel, text)
        self.images = []         # attribute dicts
        self.headings = []       # (level, text)
        self.scripts = []        # dict(attrs, in_head, content)
        self.html_lang = None
        self.element_count = 0
        self._stack = []
        self._in_head = False
        self._head_closed = False
        self._skip_text = 0
        self._cur_heading = None
        self._cur_anchor = None
        self._cur_script = None
        self.text_parts = []

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v if v is not None else "") for k, v in attrs}
        self.element_count += 1
        if tag == "html":
            self.html_lang = a.get("lang")
        elif tag == "head":
            self._in_head = True
        elif tag == "body":
            self._in_head = False
            self._head_closed = True
        elif tag == "title" and self.title is None:
            self._in_title = True
            self.title = ""
        elif tag == "meta":
            self.metas.append(a)
        elif tag == "link":
            self.links.append(a)
        elif tag == "img":
            a["_index"] = len(self.images)
            self.images.append(a)
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._cur_heading = [int(tag[1]), ""]
        elif tag == "a":
            self._cur_anchor = [a.get("href"), a.get("rel", ""), ""]
        elif tag == "script":
            self._cur_script = {"attrs": a, "in_head": self._in_head and not self._head_closed, "content": ""}
            self._skip_text += 1
        elif tag in ("style", "noscript", "template", "svg"):
            self._skip_text += 1
        if tag not in VOID:
            self._stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID and self._stack and self._stack[-1] == tag:
            self._stack.pop()

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        elif tag == "head":
            self._in_head = False
            self._head_closed = True
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6") and self._cur_heading:
            self.headings.append((self._cur_heading[0], " ".join(self._cur_heading[1].split())))
            self._cur_heading = None
        elif tag == "a" and self._cur_anchor:
            self.anchors.append((self._cur_anchor[0], self._cur_anchor[1], " ".join(self._cur_anchor[2].split())))
            self._cur_anchor = None
        elif tag == "script":
            if self._cur_script is not None:
                self.scripts.append(self._cur_script)
                self._cur_script = None
            self._skip_text = max(0, self._skip_text - 1)
        elif tag in ("style", "noscript", "template", "svg"):
            self._skip_text = max(0, self._skip_text - 1)
        if tag in self._stack:
            while self._stack and self._stack.pop() != tag:
                pass

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._cur_script is not None:
            self._cur_script["content"] += data
            return
        if self._skip_text:
            return
        if self._cur_heading is not None:
            self._cur_heading[1] += data
        if self._cur_anchor is not None:
            self._cur_anchor[2] += data
        if not self._in_head:
            self.text_parts.append(data)

    def meta(self, name: str = None, prop: str = None) -> Optional[str]:
        for m in self.metas:
            if name and m.get("name", "").lower() == name.lower():
                return m.get("content", "")
            if prop and m.get("property", "").lower() == prop.lower():
                return m.get("content", "")
        return None

    def link_rel(self, rel: str):
        return [l for l in self.links if rel in l.get("rel", "").lower().split()]

    @property
    def word_count(self) -> int:
        return len(re.findall(r"\w+", " ".join(self.text_parts), re.UNICODE))

# ------------------------------------------------------------------------------------ Findings


@dataclass
class Finding:
    severity: str
    practices: str
    message: str
    url: str = ""
    evidence: str = ""


@dataclass
class PageResult:
    url: str
    final_url: str
    status: object
    depth: int = 0
    title: str = ""
    description: str = ""
    canonical: str = ""
    noindex: bool = False
    h1: list = field(default_factory=list)
    words: int = 0
    elapsed_ms: int = 0
    internal_links: list = field(default_factory=list)
    external_links: list = field(default_factory=list)
    jsonld_types: list = field(default_factory=list)


class Audit:
    def __init__(self, ua: str, timeout: float):
        self.ua = ua
        self.timeout = timeout
        self.findings: list[Finding] = []
        self.pages: dict[str, PageResult] = {}
        self.site: dict = {}
        self._analyzed_finals: set[str] = set()

    def add(self, severity, practices, message, url="", evidence=""):
        self.findings.append(Finding(severity, practices, message, url, str(evidence)[:300]))

    # ------------------------------------------------------------------ site-level
    def check_variants(self, start_url: str):
        p = urllib.parse.urlsplit(start_url)
        host = p.hostname or ""
        if _is_local(host) or re.fullmatch(r"[\d.]+", host):
            return
        bare = host[4:] if host.startswith("www.") else host
        variants = [f"{s}://{h}/" for s in ("http", "https") for h in (bare, "www." + bare)]
        finals = {}
        for v in variants:
            r, chain = fetch_follow(v, self.ua, self.timeout)
            hops = len(chain) - 1
            finals[v] = (r.url if not r.error else None, chain)
            if r.error:
                if v.startswith("https://"):
                    self.add("warning", "8", "HTTPS variant unreachable (certificate or DNS)", v, r.error)
                continue
            if hops > 1:
                self.add("warning", "8, 23", f"This variant needs {hops} hops to reach the canonical URL (should be 1)",
                         v, " → ".join(f"{u} [{s}]" for u, s in chain))
            if r.url.startswith("http://") and r.status == 200:
                self.add("critical", "8", "Content served over HTTP without redirecting to HTTPS", v)
        targets = {f[0].rstrip("/") for f in finals.values() if f[0]}
        if len(targets) > 1:
            self.add("critical", "8, 18, 23", "http/https/www variants do not converge on a single canonical URL",
                     start_url, "; ".join(sorted(targets)))
        self.site["variants"] = {k: [f"{u} [{s}]" for u, s in v[1]] for k, v in finals.items()}

    def check_robots(self, base: str) -> list[str]:
        url = urllib.parse.urljoin(base, "/robots.txt")
        r = fetch(url, self.ua, self.timeout)
        info = {"url": url, "status": r.status or r.error}
        sitemaps: list[str] = []
        if r.error or r.status >= 500:
            self.add("critical", "4", "robots.txt returns a server error: Google may pause crawling the site", url,
                     r.error or r.status)
            self.site["robots"] = info
            return sitemaps
        if r.status in (301, 302, 307, 308):
            r, _ = fetch_follow(url, self.ua, self.timeout)
        if r.status == 404:
            self.add("info", "4", "No robots.txt (Google treats this as 'allow everything')", url)
            self.site["robots"] = info
            return sitemaps
        text = decode_body(r)
        groups = parse_robots(text)
        sitemaps = re.findall(r"(?im)^\s*sitemap\s*:\s*(\S+)", text)
        info["sitemaps"] = sitemaps
        star = groups.get("*", [])
        gbot = groups.get("googlebot", star)
        if any(rule == ("disallow", "/") for rule in gbot):
            self.add("critical", "4", "robots.txt blocks the ENTIRE site for Googlebot (Disallow: /)", url)
        for res in ("/_next/", "/static/", "/assets/", "/wp-content/", "/wp-includes/", ".css", ".js"):
            if any(kind == "disallow" and val and val != "/" and res.startswith(val.rstrip("*")) and len(val) > 1
                   for kind, val in gbot):
                self.add("critical", "4", f"robots.txt may block resources needed for rendering ({res})", url)
                break
        ai = {}
        for bot in AI_BOTS:
            rules = groups.get(bot.lower(), star)
            ai[bot] = "blocked" if any(rule == ("disallow", "/") for rule in rules) else "allowed"
        info["bots"] = ai
        blocked_search = [b for b in SEARCH_AI_BOTS if ai.get(b) == "blocked"]
        if blocked_search:
            self.add("warning", "37, A2", "AI search agents blocked: the site can't be cited in those products' search answers (fine only if deliberate)",
                     url, ", ".join(blocked_search))
        bbot = groups.get("bingbot", star)
        if any(rule == ("disallow", "/") for rule in bbot):
            self.add("critical", "B4", "[Bing] robots.txt blocks Bingbot entirely (also removes the site from Copilot)", url)
        delays = {ua: v for ua, rules in groups.items() for k, v in rules if k == "crawl-delay"}
        for ua, v in delays.items():
            self.add("warning" if ua in ("bingbot", "*") else "info", "B6",
                     f"[Bing] crawl-delay {v} for '{ua}': Bingbot honours it and it overrides BWT Crawl Control", url)
        info["crawl_delay"] = delays
        if not sitemaps:
            self.add("warning", "2", "robots.txt does not declare the sitemap (Sitemap: line)", url)
        self.site["robots"] = info
        return sitemaps

    def check_sitemaps(self, base: str, sitemaps: list[str], sample: int = 25) -> list[str]:
        if not sitemaps:
            sitemaps = [urllib.parse.urljoin(base, "/sitemap.xml")]
        urls: list[str] = []
        seen_maps = set()
        queue = deque(sitemaps)
        while queue and len(seen_maps) < 30:
            sm = queue.popleft()
            if sm in seen_maps:
                continue
            seen_maps.add(sm)
            r, _chain = fetch_follow(sm, self.ua, self.timeout)
            if r.error or r.status != 200:
                self.add("critical" if len(seen_maps) == 1 else "warning", "2", "Sitemap unreachable", sm,
                         r.error or r.status)
                continue
            body = r.body
            if sm.endswith(".gz"):
                try:
                    body = gzip.decompress(body)
                except OSError:
                    pass
            try:
                root = ElementTree.fromstring(body)
            except ElementTree.ParseError as e:
                self.add("critical", "2", "Sitemap is not valid XML", sm, e)
                continue
            tag = root.tag.split("}")[-1]
            locs = [el.text.strip() for el in root.iter() if el.tag.split("}")[-1] == "loc" and el.text]
            if tag == "sitemapindex":
                queue.extend(locs)
            else:
                urls.extend(locs)
                lastmods = [el.text for el in root.iter() if el.tag.split("}")[-1] == "lastmod" and el.text]
                if lastmods and len(lastmods) > 5 and len(set(d[:10] for d in lastmods)) == 1:
                    self.add("warning", "2", "Every URL in the sitemap has the same lastmod (Google stops trusting it)",
                             sm, lastmods[0])
                if any(el.tag.split("}")[-1] in ("priority", "changefreq") for el in root.iter()):
                    self.add("info", "2", "Sitemap uses priority/changefreq: Google ignores them", sm)
        self.site["sitemap"] = {"files": sorted(seen_maps), "url_count": len(urls)}
        if not urls:
            return urls
        start_host = urllib.parse.urlsplit(base).hostname
        foreign = [u for u in urls if urllib.parse.urlsplit(u).hostname != start_host]
        if foreign:
            self.add("warning", "2, 18", f"{len(foreign)} sitemap URLs are on a different host than the audited one",
                     base, foreign[0])
        bad = []
        step = max(1, len(urls) // sample)
        for u in urls[::step][:sample]:
            r = fetch(u, self.ua, self.timeout)
            if r.error or r.status != 200:
                bad.append(f"{u} [{r.status or r.error}]")
        if bad:
            self.add("critical" if len(bad) > 2 else "warning", "2",
                     f"{len(bad)} URLs from a sitemap sample don't return 200 (sitemaps should only list canonical 200 URLs)",
                     base, "; ".join(bad[:5]))
        return urls

    # ------------------------------------------------------------------ page-level
    def audit_page(self, url: str, depth: int = 0, deep_checks: bool = False) -> Optional[PageResult]:
        r, chain = fetch_follow(url, self.ua, self.timeout)
        final = r.url
        pr = PageResult(url=url, final_url=final, status=r.status if not r.error else f"ERROR {r.error}",
                        depth=depth, elapsed_ms=int(r.elapsed * 1000))
        self.pages[url] = pr
        if r.error:
            self.add("critical", "9, 131", "Page could not be fetched", url, r.error)
            return pr
        hops = len(chain) - 1
        temp = [u for u, st in chain if st in (302, 307)]
        if temp:
            self.add("warning", "23, B5", "[Bing] Temporary redirect (302/307): Bing expects 301/308 unless the change lasts under ~2 days",
                     url, " → ".join(f"{u} [{st}]" for u, st in chain))
        if hops > 1:
            self.add("warning", "23", f"Redirect chain of {hops} hops", url, " → ".join(f"{u} [{s}]" for u, s in chain))
        if r.status >= 500:
            self.add("critical", "131", f"Server error {r.status}", url)
            return pr
        if r.status >= 400:
            if depth == 0:
                self.add("critical", "9", f"Page returns {r.status}", url)
            return pr
        if norm(final) in self._analyzed_finals:
            return pr  # already analysed via another URL (redirect): don't duplicate findings
        self._analyzed_finals.add(norm(final))
        ctype = r.header("content-type")
        if "html" not in ctype:
            return pr
        html = decode_body(r)
        p = PageParser()
        try:
            p.feed(html)
        except Exception as e:  # badly broken HTML
            self.add("warning", "25", "The HTML could not be fully parsed", url, e)

        # ---- indexability
        robots_meta = " ".join(filter(None, [p.meta(name="robots"), p.meta(name="googlebot")])).lower()
        xrobots = r.header("x-robots-tag").lower()
        pr.noindex = "noindex" in robots_meta or "noindex" in xrobots or "none" in robots_meta.split(",")
        if pr.noindex:
            sev = "critical" if depth == 0 else "warning"
            self.add(sev, "4, 21, 120", "Page has noindex (meta robots or X-Robots-Tag)", url, robots_meta or xrobots)
        bing_meta = " ".join(filter(None, [p.meta(name="robots"), p.meta(name="bingbot"), p.meta(name="msnbot")])).lower()
        directives = bing_meta + " " + xrobots
        if not pr.noindex:
            if "noarchive" in directives:
                self.add("warning", "37, B8", "[Bing] noarchive: content is excluded from Copilot answers and grounding", url, directives.strip())
            if "nocache" in directives:
                self.add("warning", "37, B8", "[Bing] nocache: Copilot may only use URL, title and snippet", url, directives.strip())
            if "nosnippet" in directives or "data-nosnippet" in html:
                self.add("info", "B8", "[Bing] nosnippet/data-nosnippet: no captions in Bing and weaker Copilot citations", url)
        canon = p.link_rel("canonical")
        if not canon:
            self.add("warning", "18", "Missing rel=canonical", url)
        else:
            href = canon[0].get("href", "")
            pr.canonical = urllib.parse.urljoin(final, href)
            if len(canon) > 1:
                self.add("critical", "18", "Multiple rel=canonical tags on the page", url)
            if not re.match(r"https?://", href):
                self.add("warning", "18", "Canonical is not an absolute URL", url, href)
            if norm(pr.canonical) != norm(final):
                self.add("info" if not pr.noindex else "warning", "18",
                         "Canonical points to another URL (only correct for an intentional duplicate)", url,
                         pr.canonical)
            if pr.canonical.startswith("http://") and final.startswith("https://"):
                self.add("critical", "8, 18", "Canonical points to http:// on an https page", url, pr.canonical)

        # ---- title / description
        title = " ".join((p.title or "").split())
        pr.title = title
        if not title:
            self.add("critical", "56", "Missing <title>", url)
        elif len(title) < 25:
            self.add("info", "56", f"Short title ({len(title)} characters): review whether it describes the page clearly; length alone is not a defect", url, title)
        elif len(title) > 65:
            self.add("info", "56", f"Long title ({len(title)} characters): truncation depends on the result layout; keep the main topic first", url, title)
        desc = " ".join((p.meta(name="description") or "").split())
        pr.description = desc
        if not desc:
            self.add("warning", "56", "Missing meta description", url)
        elif len(desc) < 50 or len(desc) > 320:
            self.add("info", "56", f"Meta description of {len(desc)} characters: review usefulness (heuristic ~140–160); engines may choose page text instead", url, desc)
        if p.meta(name="keywords"):
            self.add("info", "myths", "Uses meta keywords: ignored by Google and Bing; stuffing can be a Bing spam signal", url)

        # ---- headings
        h1s = [t for lvl, t in p.headings if lvl == 1]
        pr.h1 = h1s
        if not h1s:
            self.add("info", "43", "No H1: review whether the page has a clear main heading and outline", url)
        elif len(h1s) > 1:
            self.add("info", "43", f"{len(h1s)} H1 headings: check the outline is clear (not inherently an SEO defect)", url, " | ".join(h1s[:3]))
        prev = 0
        for lvl, txt in p.headings:
            if prev and lvl > prev + 1:
                self.add("info", "44", f"Heading level skipped H{prev} → H{lvl}", url, txt[:80])
                break
            prev = lvl

        # ---- language, viewport, hreflang, social, favicon
        if not p.html_lang:
            self.add("warning", "35, 136", "Missing lang attribute on <html>", url)
        if not p.meta(name="viewport"):
            self.add("critical", "7", "Missing meta viewport (not mobile-friendly)", url)
        elif "user-scalable=no" in (p.meta(name="viewport") or "").replace(" ", "").lower():
            self.add("warning", "7, 35", "Viewport disables zoom (user-scalable=no)", url)
        alts = [l for l in p.link_rel("alternate") if l.get("hreflang")]
        if alts:
            langs = [l["hreflang"].lower() for l in alts]
            if "x-default" not in langs:
                self.add("info", "137", "hreflang without x-default", url)
            if not any(norm(urllib.parse.urljoin(final, l.get("href", ""))) == norm(final) for l in alts):
                self.add("warning", "137", "hreflang set does not reference the page itself", url)
            for lg in langs:
                if lg in ("en-uk", "es-eu", "en-eu") or not re.fullmatch(r"x-default|[a-z]{2,3}(-[a-z]{2}|-[a-z]{4})?", lg):
                    self.add("warning", "137", f"Invalid hreflang code: {lg}", url)
        if depth == 0 and deep_checks:
            has_meta = bool(p.meta(name="msvalidate.01"))
            bsa = fetch(urllib.parse.urljoin(final, "/BingSiteAuth.xml"), self.ua, self.timeout)
            has_file = bsa.status == 200 and b"<user>" in bsa.body.lower()
            self.site["bing_verification"] = {"msvalidate.01": has_meta, "BingSiteAuth.xml": has_file}
            if not (has_meta or has_file):
                self.add("info", "5, B1", "[Bing] No msvalidate.01 meta or BingSiteAuth.xml found (fine if verified by DNS or GSC import)", url)
        if depth == 0:
            if not p.meta(prop="og:title") or not p.meta(prop="og:image"):
                self.add("info", "70", "Missing Open Graph tags (og:title / og:image)", url)
            if not (p.link_rel("icon") or p.link_rel("shortcut")):
                self.add("info", "34", "No favicon declared with <link rel=icon>", url)

        # ---- JSON-LD
        for s in p.scripts:
            if s["attrs"].get("type", "").lower() == "application/ld+json":
                raw = s["content"].strip()
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError as e:
                    self.add("critical", "59", "JSON-LD is invalid JSON (Google ignores it)", url, e)
                    continue
                pr.jsonld_types.extend(jsonld_types(data))
        types_lower = {t.lower() for t in pr.jsonld_types}
        if depth == 0 and not types_lower & {"organization", "localbusiness", "corporation", "store",
                                              "professionalservice", "onlinestore", "website"}:
            self.add("info", "38", "Start page declares no Organization/WebSite JSON-LD", url)
        if "faqpage" in types_lower:
            self.add("info", "47, 59", "FAQPage markup no longer yields Google FAQ rich results (retired 7 May 2026); keep only if it accurately describes visible Q&A and serves another use", url)
        if "howto" in types_lower:
            self.add("info", "59", "HowTo: Google retired this rich result in 2023", url)

        # ---- images
        imgs = p.images
        no_alt = [i.get("src", "")[:80] for i in imgs if "alt" not in i]
        if no_alt:
            self.add("warning", "35, 58", f"{len(no_alt)} images without an alt attribute", url, ", ".join(no_alt[:3]))
        no_dims = [i.get("src", "")[:80] for i in imgs
                   if not (i.get("width") and i.get("height")) and "aspect-ratio" not in i.get("style", "")
                   and not i.get("src", "").startswith("data:")]
        if no_dims:
            self.add("warning", "14", f"{len(no_dims)} images without width/height (CLS risk)", url,
                     ", ".join(no_dims[:3]))
        content_imgs = [i for i in imgs if not i.get("src", "").startswith("data:")]
        if content_imgs and content_imgs[0].get("loading", "").lower() == "lazy":
            self.add("warning", "13, 70", "The document's first image has loading=lazy (delays LCP if it is the LCP image)",
                     url, content_imgs[0].get("src", "")[:100])

        # ---- render-blocking scripts
        blocking = [s["attrs"].get("src") for s in p.scripts
                    if s["in_head"] and s["attrs"].get("src") and not any(k in s["attrs"] for k in ("async", "defer"))
                    and s["attrs"].get("type", "").lower() != "module"]
        if blocking:
            self.add("warning", "15", f"{len(blocking)} synchronous scripts in <head> block rendering", url,
                     ", ".join(b[:80] for b in blocking[:3]))

        # ---- content without JS / DOM size
        pr.words = p.word_count
        if pr.words < 80 and not pr.noindex:
            self.add("critical" if depth == 0 else "warning", "25, 127",
                     f"Only {pr.words} words in the served HTML: content may depend on JavaScript", url)
        if p.element_count > 1400:
            self.add("warning", "126", f"Large DOM: {p.element_count} elements", url)
        elif p.element_count > 800:
            self.add("info", "126", f"DOM of {p.element_count} elements (Lighthouse warns above ~800)", url)

        # ---- links
        host = urllib.parse.urlsplit(final).hostname
        for href, rel, text in p.anchors:
            if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
                continue
            absu = urllib.parse.urljoin(final, href).split("#")[0]
            if urllib.parse.urlsplit(absu).scheme not in ("http", "https"):
                continue
            if urllib.parse.urlsplit(absu).hostname == host:
                pr.internal_links.append((absu, text, rel))
                if "nofollow" in rel.lower():
                    self.add("info", "82", "Internal link with nofollow", url, absu)
            else:
                pr.external_links.append((absu, text, rel))
        onclick_nav = len(re.findall(r"<(?:div|span|li)[^>]+onclick=[\"'][^\"']*(?:location|navigate|push)", html, re.I))
        if onclick_nav:
            self.add("warning", "25", f"{onclick_nav} elements navigate via onclick instead of <a href> (not crawlable)", url)

        # ---- performance / headers (start page only)
        if deep_checks:
            self.check_headers(url, r)
        if r.elapsed > 1.8:
            self.add("warning", "6, 10, 11", f"Slow response: {int(r.elapsed*1000)} ms (TTFB + download from this machine)", url)
        return pr

    def check_headers(self, url: str, r: Response):
        h = r.headers
        final = r.url
        sec = {
            "strict-transport-security": ("8, 30", "Missing HSTS (Strict-Transport-Security)"),
            "x-content-type-options": ("30", "Missing X-Content-Type-Options: nosniff"),
            "referrer-policy": ("30", "Missing Referrer-Policy"),
        }
        is_https = final.startswith("https://")
        for k, (practices, msg) in sec.items():
            if k == "strict-transport-security" and not is_https:
                continue
            if k not in h:
                self.add("info", practices, msg, url)
        csp = h.get("content-security-policy", "")
        if "x-frame-options" not in h and "frame-ancestors" not in csp:
            self.add("info", "30", "No clickjacking protection (X-Frame-Options or CSP frame-ancestors)", url)
        if not csp:
            self.add("info", "29", "No Content-Security-Policy", url)
        if h.get("content-encoding", "").lower() not in ("gzip", "br", "zstd", "deflate") and len(r.body) > 2000:
            rb = fetch(url, self.ua, self.timeout, extra_headers={"Accept-Encoding": "br, gzip"})
            if rb.header("content-encoding").lower() not in ("gzip", "br", "zstd", "deflate"):
                self.add("warning", "12", "HTML is not served compressed (gzip/brotli)", url)
        etag, lm = h.get("etag"), h.get("last-modified")
        self.site["cache"] = {"cache-control": h.get("cache-control", ""), "etag": bool(etag),
                              "last-modified": bool(lm), "cdn": cdn_hint(h)}
        if etag or lm:
            extra = {"If-None-Match": etag} if etag else {"If-Modified-Since": lm}
            rc = fetch(final, self.ua, self.timeout, extra_headers=extra)
            self.site["cache"]["conditional_304"] = rc.status == 304
            if rc.status != 304:
                self.add("info", "125", f"Conditional request returns {rc.status} instead of 304", url)
        else:
            self.add("info", "125", "No ETag or Last-Modified (304 responses impossible)", url)
        probe = urllib.parse.urljoin(final, "/this-url-should-not-exist-" + str(int(time.time())))
        rp = fetch(probe, self.ua, self.timeout)
        if rp.status == 200:
            self.add("critical", "9, 26", "Non-existent URLs return 200 (soft 404)", probe)
        elif rp.status in (301, 302, 307, 308):
            self.add("warning", "9", "Non-existent URLs redirect instead of returning 404", probe, rp.header("location"))

    def check_indexnow(self, base: str, key: str):
        url = urllib.parse.urljoin(base, f"/{key}.txt")
        r = fetch(url, self.ua, self.timeout)
        ok = r.status == 200 and decode_body(r).strip() == key
        self.site["indexnow"] = {"key_file": url, "valid": ok}
        if not ok:
            self.add("warning", "5, B2", "[Bing] IndexNow key file missing or its content doesn't match the key", url,
                     r.error or r.status)

    # ------------------------------------------------------------------ crawl
    def crawl(self, start: str, limit: int, sitemap_urls: list[str]):
        start_host = urllib.parse.urlsplit(start).hostname
        q = deque([(start, 0)])
        seen = {norm(start)}
        inbound = defaultdict(set)
        while q and len(self.pages) < limit:
            url, depth = q.popleft()
            pr = self.pages.get(url) or self.audit_page(url, depth)
            if not pr:
                continue
            pr.depth = depth
            for link, _text, _rel in pr.internal_links:
                inbound[norm(link)].add(url)
                if norm(link) in seen:
                    continue
                if urllib.parse.urlsplit(link).hostname != start_host:
                    continue
                if re.search(r"\.(pdf|jpe?g|png|gif|webp|avif|svg|zip|docx?|xlsx?|mp4|mp3)$", link, re.I):
                    continue
                seen.add(norm(link))
                q.append((link, depth + 1))
        self.analyze_crawl(inbound, sitemap_urls, len(self.pages) >= limit)

    def analyze_crawl(self, inbound, sitemap_urls, truncated):
        pages = list(self.pages.values())
        broken = [p for p in pages if (isinstance(p.status, int) and p.status >= 400) or isinstance(p.status, str)]
        for p in broken:
            refs = list(inbound.get(norm(p.url), []))[:3]
            self.add("warning", "9, 123", f"Broken internal link ({p.status})", p.url, "Linked from: " + ", ".join(refs))
        redirected = [p for p in pages if norm(p.url) != norm(p.final_url) and p.depth > 0]
        if redirected:
            self.add("warning", "24", f"{len(redirected)} internal links point to URLs that redirect", redirected[0].url,
                     "; ".join(f"{p.url} → {p.final_url}" for p in redirected[:5]))
        ok = [p for p in pages if p.status == 200 and not p.noindex]
        for attr, practices, label in (("title", "56", "titles"), ("description", "56", "meta descriptions")):
            c = Counter(getattr(p, attr) for p in ok if getattr(p, attr))
            dups = {k: v for k, v in c.items() if v > 1}
            if dups:
                k, v = max(dups.items(), key=lambda kv: kv[1])
                self.add("warning", practices + ", 46", f"{len(dups)} duplicate {label} across pages (most repeated: {v} times)",
                         "", k[:120])
        deep = [p for p in pages if p.depth > 3]
        if deep:
            self.add("info", "17", f"{len(deep)} pages more than 3 clicks from the start page", deep[0].url)
        if sitemap_urls and not truncated:
            crawled = {norm(p.url) for p in pages} | {norm(p.final_url) for p in pages}
            orphans = [u for u in sitemap_urls if norm(u) not in crawled]
            if orphans:
                self.add("warning", "17, 82", f"{len(orphans)} sitemap URLs are not reachable by links from the start page (possible orphans)",
                         orphans[0], "; ".join(orphans[:5]))
        ext = Counter(link for p in pages for link, _t, _r in p.external_links)
        self.site["external_links_unique"] = len(ext)

# ------------------------------------------------------------------------------------- helpers


def norm(u: str) -> str:
    s = urllib.parse.urlsplit(u)
    path = s.path or "/"
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return urllib.parse.urlunsplit((s.scheme.lower(), (s.netloc or "").lower(), path, s.query, ""))


def jsonld_types(data) -> list[str]:
    out = []
    if isinstance(data, list):
        for d in data:
            out.extend(jsonld_types(d))
    elif isinstance(data, dict):
        t = data.get("@type")
        if isinstance(t, list):
            out.extend(str(x) for x in t)
        elif t:
            out.append(str(t))
        if "@graph" in data:
            out.extend(jsonld_types(data["@graph"]))
    return out


def parse_robots(text: str) -> dict:
    """Return {lowercase user-agent: [(directive, value)]}. Simplified, but enough to detect blocks."""
    groups: dict[str, list] = {}
    current: list[str] = []
    last_was_ua = False
    for line in text.splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        k, v = (x.strip() for x in line.split(":", 1))
        k = k.lower()
        if k == "user-agent":
            if not last_was_ua:
                current = []
            current.append(v.lower())
            groups.setdefault(v.lower(), [])
            last_was_ua = True
        elif k in ("allow", "disallow", "crawl-delay"):
            last_was_ua = False
            for ua in current:
                groups.setdefault(ua, []).append((k, v))
        else:
            last_was_ua = False
    for ua, rules in groups.items():  # an explicit "Allow: /" cancels "Disallow: /"
        if ("allow", "/") in rules and ("disallow", "/") in rules:
            groups[ua] = [r for r in rules if r != ("disallow", "/")]
    return groups


def cdn_hint(h: dict) -> str:
    for key, name in (("cf-ray", "Cloudflare"), ("x-vercel-id", "Vercel"), ("x-nf-request-id", "Netlify"),
                      ("x-amz-cf-id", "CloudFront"), ("x-served-by", "Fastly")):
        if key in h:
            return name
    return h.get("server", "")

# -------------------------------------------------------------------------------------- report


def _first_num(s: str) -> int:
    m = re.match(r"\d+", s)
    return int(m.group()) if m else 999


def render_markdown(audit: Audit, start: str) -> str:
    f = sorted(audit.findings, key=lambda x: (SEVERITY_ORDER[x.severity], _first_num(x.practices)))
    counts = Counter(x.severity for x in f)
    lines = [f"# SEO audit — {start}", "",
             f"_Generated {time.strftime('%Y-%m-%d %H:%M')} by seo_audit.py {__version__} (seo-pro) · pages analysed: {len(audit.pages)}_", "",
             "| Severity | Count |", "|---|---|"]
    for s in ("critical", "warning", "info"):
        lines.append(f"| {SEV_LABEL[s]} | {counts.get(s, 0)} |")
    lines.append("")
    for s in ("critical", "warning", "info"):
        items = [x for x in f if x.severity == s]
        if not items:
            continue
        lines += [f"## {SEV_LABEL[s]}", "", "| Practice | Finding | URL | Evidence |", "|---|---|---|---|"]
        for x in items:
            ev = x.evidence.replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {x.practices} | {x.message} | {x.url} | {ev} |")
        lines.append("")
    rb = audit.site.get("robots", {})
    if rb.get("bots"):
        lines += ["## Crawlers (per robots.txt)", "", "| User agent | Purpose | Status |", "|---|---|---|"]
        lines += [f"| {k} | {BOT_PURPOSE.get(k, '')} | {v} |" for k, v in rb["bots"].items()]
        lines += ["", "_Decide search, training and user-fetch access separately per operator (practice 37, `engines/ai-search.md` A2). "
                  "robots.txt is public and user fetchers may ignore it: protect private content with authentication. "
                  "Also check the Search Console generative AI control (A3); it isn't visible from outside._", ""]
    bv = audit.site.get("bing_verification")
    if bv or audit.site.get("indexnow") or (rb.get("crawl_delay")):
        lines += ["## Bing & Copilot", ""]
        if bv:
            lines.append(f"- BWT verification: msvalidate.01 {'yes' if bv['msvalidate.01'] else 'no'} · BingSiteAuth.xml {'yes' if bv['BingSiteAuth.xml'] else 'no'}")
        if audit.site.get("indexnow"):
            ix = audit.site["indexnow"]
            lines.append(f"- IndexNow key file: {ix['key_file']} → {'valid' if ix['valid'] else 'INVALID'}")
        if rb.get("crawl_delay"):
            lines.append(f"- crawl-delay: {rb['crawl_delay']}")
        lines += ["", "_See references/engines/bing.md for B-practices._", ""]
    sm = audit.site.get("sitemap")
    if sm:
        lines += ["## Sitemap", "", f"- Files: {', '.join(sm['files'])}", f"- URLs listed: {sm['url_count']}", ""]
    if audit.site.get("cache"):
        c = audit.site["cache"]
        lines += ["## Caching and CDN", "", f"- CDN/server: {c.get('cdn') or 'unknown'}",
                  f"- Cache-Control: `{c.get('cache-control') or '—'}`",
                  f"- ETag: {'yes' if c.get('etag') else 'no'} · Last-Modified: {'yes' if c.get('last-modified') else 'no'}"
                  f" · conditional 304: {'yes' if c.get('conditional_304') else 'no'}", ""]
    lines += ["## Pages", "", "| URL | Status | Depth | ms | Words | Title | H1 | noindex | JSON-LD |",
              "|---|---|---|---|---|---|---|---|---|"]
    for p in sorted(audit.pages.values(), key=lambda x: (x.depth, x.url)):
        t = (p.title[:60] + "…") if len(p.title) > 60 else p.title
        h1 = (p.h1[0][:40] if p.h1 else "—").replace("|", "/")
        lines.append(f"| {p.url} | {p.status} | {p.depth} | {p.elapsed_ms} | {p.words} | {t.replace('|', '/')} | {h1} | "
                     f"{'yes' if p.noindex else ''} | {', '.join(sorted(set(p.jsonld_types)))[:60]} |")
    lines += ["", "---", "Limitations: does not execute JavaScript (it measures what a non-rendering crawler sees), does not "
              "measure field Core Web Vitals (use PageSpeed Insights / Search Console), and latency depends on where it runs."]
    return "\n".join(lines) + "\n"

# ---------------------------------------------------------------------------------------- main


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Technical SEO audit (seo-pro skill by blackwings.dev)")
    ap.add_argument("url", nargs="?", help="Start URL (e.g. https://example.com)")
    ap.add_argument("--crawl", type=int, default=0, help="Crawl up to N internal pages (0 = start URL only)")
    ap.add_argument("--urls", help="File with one URL per line to audit without crawling (alert mode)")
    ap.add_argument("--output", help="Write the Markdown report to this path")
    ap.add_argument("--json", help="Write findings as JSON to this path")
    ap.add_argument("--fail-on", choices=["critical", "warning", "none"], default="none",
                    help="Exit with code 1 if there are findings at this level or above")
    ap.add_argument("--user-agent", default=UA_DEFAULT)
    ap.add_argument("--timeout", type=float, default=20)
    ap.add_argument("--skip-variants", action="store_true", help="Don't test http/https/www variants")
    ap.add_argument("--skip-sitemap", action="store_true", help="Don't download the sitemap")
    ap.add_argument("--indexnow-key", help="IndexNow key to verify at /<key>.txt on the audited host")
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = ap.parse_args(argv)

    if not args.url and not args.urls:
        ap.error("provide a URL or --urls file.txt")
    audit = Audit(args.user_agent, args.timeout)

    if args.urls:
        with open(args.urls, encoding="utf-8") as fh:
            urls = [l.strip() for l in fh if l.strip() and not l.startswith("#")]
        for i, u in enumerate(urls):
            audit.audit_page(u, 0, deep_checks=(i == 0))
        start = urls[0] if urls else ""
    else:
        start = args.url if re.match(r"https?://", args.url) else "https://" + args.url
        first = audit.audit_page(start, 0, deep_checks=True)
        if first is None or isinstance(first.status, str):
            print(render_markdown(audit, start))
            return 2
        base = first.final_url
        if not args.skip_variants:
            audit.check_variants(start)
        sitemaps = audit.check_robots(base)
        sm_urls = [] if args.skip_sitemap else audit.check_sitemaps(base, sitemaps)
        if args.indexnow_key:
            audit.check_indexnow(base, args.indexnow_key)
        if args.crawl > 1:
            audit.crawl(base if norm(base) != norm(start) else start, args.crawl, sm_urls)

    report = render_markdown(audit, start)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(report)
        print(f"Report written to {args.output}")
    else:
        print(report)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"start": start, "site": audit.site, "findings": [asdict(x) for x in audit.findings],
                       "pages": [asdict(p) for p in audit.pages.values()]}, fh, ensure_ascii=False, indent=2, default=str)
    if args.fail_on == "none":
        return 0
    level = SEVERITY_ORDER[args.fail_on]
    return 1 if any(SEVERITY_ORDER[x.severity] <= level for x in audit.findings) else 0


if __name__ == "__main__":
    sys.exit(main())
