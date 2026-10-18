import gzip
import io
import json
import os
import shutil
import tempfile
import unittest
from contextlib import redirect_stdout

from _paths import FIXTURES
import crawl_logs as cl


def run(*args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = cl.main(list(args))
    return code, buf.getvalue()


class CrawlLogsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def figures(self, *extra):
        out = os.path.join(self.tmp, "r.json")
        code, _ = run(str(FIXTURES / "access.log"), "--ranges-dir", str(FIXTURES / "ranges"), "--verify", "none",
                      "--json", out, "--output", os.path.join(self.tmp, "r.md"), *extra)
        self.assertEqual(code, 0)
        with open(out, encoding="utf-8") as fh:
            return json.load(fh)

    def test_counts_and_impostors(self):
        d = self.figures()
        self.assertEqual(d["total_lines"], 15)
        self.assertEqual(d["unparsed"], 1)
        g = d["bots"]["Googlebot"]
        self.assertEqual(g["hits"], 6)
        self.assertEqual(g["verified"], 6)
        self.assertEqual(g["impostor_hits"], 2)  # 203.0.113.9 claims to be Googlebot
        self.assertEqual(d["bots"]["GPTBot"]["impostor_hits"], 1)  # outside the GPTBot range
        self.assertEqual(d["bots"]["ClaudeBot"]["not_verifiable"], 1)  # no range file supplied
        self.assertEqual(g["status"], {"2xx": 4, "3xx": 1, "4xx": 1})

    def test_waste_and_params(self):
        g = self.figures()["bots"]["Googlebot"]
        self.assertEqual(g["waste"]["redirects (3xx)"], 1)
        self.assertEqual(g["waste"]["not found (404/410)"], 1)
        self.assertEqual(g["waste"]["tracking-parameter URLs"], 1)
        self.assertEqual(g["waste"]["other parameter URLs"], 1)
        self.assertIn("utm_source", g["params"])

    def test_sitemap_coverage(self):
        _, md = run(str(FIXTURES / "access.log"), "--ranges-dir", str(FIXTURES / "ranges"), "--verify", "none",
                    "--sitemap-urls", str(FIXTURES / "sitemap-urls.txt"))
        self.assertIn("Never fetched with a 200: 1", md)
        self.assertIn("`/about`", md)

    def test_gzip_and_jsonl_with_host_filter(self):
        gz = os.path.join(self.tmp, "a.log.gz")
        with open(FIXTURES / "access.log", "rb") as src, gzip.open(gz, "wb") as dst:
            dst.write(src.read())
        code, md = run(gz, "--verify", "none")
        self.assertEqual(code, 0)
        self.assertIn("| Googlebot |", md)
        out = os.path.join(self.tmp, "j.json")
        run(str(FIXTURES / "cf.jsonl"), "--host", "www.example.com", "--verify", "none", "--json", out, "--output", os.devnull)
        with open(out, encoding="utf-8") as fh:
            d = json.load(fh)
        self.assertEqual(d["bots"]["Googlebot"]["hits"], 1)  # cdn.example.com line filtered out
        self.assertEqual(d["bots"]["Googlebot"]["params"], {"page": 1})

    def test_w3c_format(self):
        lines = ["#Fields: date time c-ip cs-method cs-uri-stem cs-uri-query sc-status cs(User-Agent)",
                 "2026-10-10 06:25:01 157.55.39.10 GET /a - 200 Mozilla/5.0+(compatible;+bingbot/2.0;+http://www.bing.com/bingbot.htm)"]
        recs = list(cl.parse_lines(lines))
        self.assertEqual(recs[0]["path"], "/a")
        self.assertEqual(cl.classify(recs[0]["ua"])["name"], "Bingbot")

    def test_classification_order(self):
        self.assertEqual(cl.classify("Mozilla/5.0 (compatible; Googlebot-Image/1.0)")["name"], "Googlebot-Image")
        self.assertEqual(cl.classify("Mozilla/5.0; compatible; OAI-SearchBot/1.3")["name"], "OAI-SearchBot")
        self.assertIsNone(cl.classify("Mozilla/5.0 (Windows NT 10.0) Chrome/130"))

    def test_range_file_formats(self):
        nets = cl._networks_from_json({"prefixes": [{"ipv4Prefix": "1.2.3.0/24"}, {"ipv6Prefix": "2001:db8::/32"}],
                                       "other": ["5.6.7.8", "not-an-ip"]})
        self.assertEqual(len(nets), 3)

    def test_unparseable_input_exits_3(self):
        bad = os.path.join(self.tmp, "bad.log")
        with open(bad, "w") as fh:
            fh.write("nothing here\n")
        self.assertEqual(cl._main_safe([bad, "--verify", "none"]), 3)
        self.assertEqual(cl._main_safe([os.path.join(self.tmp, "missing.log")]), 3)


if __name__ == "__main__":
    unittest.main()
