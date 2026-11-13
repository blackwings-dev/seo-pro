import functools
import io
import json
import os
import shutil
import tempfile
import threading
import unittest
from contextlib import redirect_stdout
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

from _paths import FIXTURES
import seo_audit


class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def chromium_available() -> bool:
    try:
        import playwright.sync_api  # noqa: F401
    except ImportError:
        return False
    return bool(os.environ.get("SEO_PRO_CHROMIUM")) or os.environ.get("SEO_PRO_TEST_RENDER") == "1"


class AuditTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        handler = functools.partial(Quiet, directory=str(FIXTURES / "site"))
        cls.srv = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=cls.srv.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.srv.server_address[1]}/"
        cls.tmp = tempfile.mkdtemp()

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()
        shutil.rmtree(cls.tmp)

    def audit(self, *extra):
        j = os.path.join(self.tmp, "a.json")
        h = os.path.join(self.tmp, "a.html")
        with redirect_stdout(io.StringIO()):
            code = seo_audit.main([self.base, "--crawl", "5", "--delay", "0", "--skip-variants", "--json", j,
                                   "--html", h, "--output", os.path.join(self.tmp, "a.md"), *extra])
        with open(j, encoding="utf-8") as fh:
            data = json.load(fh)
        with open(h, encoding="utf-8") as fh:
            html = fh.read()
        return code, data, html

    def test_crawl_findings_and_reports(self):
        code, data, html = self.audit()
        self.assertEqual(code, 0)
        msgs = [f["message"] for f in data["findings"]]
        self.assertTrue(any("not an absolute URL" in m and "Sitemap" in m for m in msgs))  # relative Sitemap: no crash
        self.assertTrue(any("content may depend on JavaScript" in m for m in msgs))         # spa.html served empty
        self.assertEqual(data["version"], seo_audit.__version__)
        self.assertEqual(len(data["pages"]), 3)
        self.assertIn("<h1>SEO audit</h1>", html)
        self.assertIn("Fix first", html)
        self.assertNotIn("<script src", html)  # self-contained

    def test_fail_on_exit_code(self):
        with redirect_stdout(io.StringIO()):
            code = seo_audit.main([self.base, "--skip-variants", "--skip-sitemap", "--fail-on", "warning"])
        self.assertEqual(code, 1)

    def test_missing_input_exits_3(self):
        with redirect_stdout(io.StringIO()):
            self.assertEqual(seo_audit._main_safe(["--urls", os.path.join(self.tmp, "nope.txt")]), 3)

    @unittest.skipUnless(chromium_available(), "Playwright/Chromium not available (set SEO_PRO_CHROMIUM to run)")
    def test_render_comparison(self):
        _, data, html = self.audit("--render", "--render-wait", "200")
        spa = data["site"]["render"][self.base + "spa.html"]
        self.assertGreater(spa["rendered_words"], 300)
        self.assertEqual(spa["served_words"], 0)
        for k in ("canonical", "title", "h1", "words", "links_only_after_js", "jsonld_only_after_js"):
            self.assertIn(k, spa["differences"])
        self.assertEqual(data["site"]["render"][self.base]["differences"], {})
        self.assertIn("Served HTML vs rendered DOM", html)


    def test_nomodule_and_module_scripts_do_not_block(self):
        p = seo_audit.PageParser()
        p.feed('<html><head><script src="/a.js"></script><script src="/poly.js" nomodule></script>'
               '<script type="module" src="/m.js"></script><script src="/d.js" defer></script></head><body></body></html>')
        self.assertEqual(seo_audit.blocking_scripts(p.scripts), ["/a.js"])

    def test_redirect_map_skips_header_in_any_language(self):
        m = os.path.join(self.tmp, "map.csv")
        with open(m, "w", encoding="utf-8") as fh:
            fh.write(f"origen,destino\n{self.base}index.html,{self.base}index.html\n")
        j = os.path.join(self.tmp, "m.json")
        with redirect_stdout(io.StringIO()):
            seo_audit.main(["--redirect-map", m, "--json", j])
        with open(j, encoding="utf-8") as fh:
            rm = json.load(fh)["site"]["redirect_map"]
        self.assertEqual(rm["rows"], 1)
        self.assertEqual(rm["counts"].get("critical", 0), 0)


if __name__ == "__main__":
    unittest.main()
