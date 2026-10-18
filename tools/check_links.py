#!/usr/bin/env python3
"""
check_links.py — find source links that have died or moved. Standard library only.

  python3 tools/check_links.py                    # skill references, README and docs/
  python3 tools/check_links.py --output links.md  # Markdown report (used by the weekly workflow)

Statuses:
  broken   404 or 410 — the source is gone: replace it or remove the claim it supports
  error    5xx, DNS or connection failures — often temporary; broken if it repeats next week
  moved    redirects to a different path — update the link if the new page is the same document
  blocked  401, 403 or 429 — the site refuses automated checks; verify by hand only if it matters
  ok       2xx

Exit code: 1 when any link is broken, 0 otherwise (errors and redirects are reported, not fatal).
"""
from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
URL_RX = re.compile(r"https?://[^\s)>\]`\"'|]+")
SKIP = re.compile(r"(example\.(com|org)|localhost|127\.0\.0\.1|\{|<|your-|claude\.ai/code)", re.I)
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36 "
      "(compatible; seo-pro-link-check; +https://github.com/blackwings-dev/seo-pro)")


def collect(paths: list[Path]) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    for base in paths:
        files = [base] if base.is_file() else sorted(base.rglob("*.md"))
        for f in files:
            for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
                for u in URL_RX.findall(line):
                    u = u.rstrip(".,;:*_")
                    if SKIP.search(u):
                        continue
                    found.setdefault(u, []).append(f"{f.relative_to(ROOT)}:{i}")
    return found


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


def check(url: str, timeout: float) -> tuple[str, str]:
    opener = urllib.request.build_opener()
    final = url
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with opener.open(req, timeout=timeout) as r:
                final = r.geturl()
                code = r.status
            break
        except urllib.error.HTTPError as e:
            code = e.code
            if method == "HEAD" and code in (400, 403, 404, 405, 406, 429, 500, 501, 503):
                continue  # many servers mishandle HEAD: confirm with GET
            break
        except Exception as e:  # DNS, TLS, timeout, reset
            if method == "HEAD":
                continue
            return "error", f"{type(e).__name__}: {str(e)[:120]}"
    if code in (404, 410):
        return "broken", str(code)
    if code in (401, 403, 429):
        return "blocked", str(code)
    if code >= 500:
        return "error", str(code)
    a, b = urllib.parse.urlsplit(url), urllib.parse.urlsplit(final)
    if (a.netloc.lower().removeprefix("www."), a.path.rstrip("/")) != (b.netloc.lower().removeprefix("www."), b.path.rstrip("/")):
        return "moved", final
    return "ok", str(code)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check the source links in seo-pro")
    ap.add_argument("paths", nargs="*", help="Files or folders (default: skill, README.md, docs/)")
    ap.add_argument("--output", help="Write a Markdown report here")
    ap.add_argument("--timeout", type=float, default=20)
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args(argv)
    paths = [Path(p).resolve() for p in args.paths] or [ROOT / "plugins", ROOT / "README.md", ROOT / "docs"]
    links = collect([p for p in paths if p.exists()])
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        results = dict(zip(links, ex.map(lambda u: check(u, args.timeout), links)))
    order = ["broken", "error", "moved", "blocked", "ok"]
    counts = {s: sum(1 for v in results.values() if v[0] == s) for s in order}
    lines = [f"# Source link check — {time.strftime('%Y-%m-%d')}", "",
             " · ".join(f"{s}: {counts[s]}" for s in order) + f" · total: {len(results)}", ""]
    for s in order[:-1]:
        rows = [(u, d) for u, (st, d) in sorted(results.items()) if st == s]
        if not rows:
            continue
        lines += [f"## {s.capitalize()} ({len(rows)})", "", "| Link | Detail | Cited in |", "|---|---|---|"]
        lines += [f"| {u} | {d} | {', '.join(links[u][:3])}{' …' if len(links[u]) > 3 else ''} |" for u, d in rows]
        lines.append("")
    lines += ["_Broken links need a replacement source or the claim they support must be re-checked "
              "(`references/research-method.md`). Blocked links refuse automated checks and are usually fine._"]
    report = "\n".join(lines) + "\n"
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
    print(report)
    return 1 if counts["broken"] else 0


if __name__ == "__main__":
    sys.exit(main())
