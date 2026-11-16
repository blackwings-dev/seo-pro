import csv
import io
import json
import os
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout

import _paths  # noqa: F401
import mock_apis


class KeywordDataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = mock_apis.start()
        port = cls.srv.server_address[1]
        os.environ.update(DATAFORSEO_API_BASE=f"http://127.0.0.1:{port}/dfs", DATAFORSEO_LOGIN="user",
                          DATAFORSEO_PASSWORD="secret-pass")
        import importlib
        import keyword_data
        cls.kd = importlib.reload(keyword_data)

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()

    def run_cmd(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = self.kd.main(list(args) + ["--pause", "0"])
        return code, out.getvalue(), err.getvalue()

    # ---- goto unwrapping
    def test_unwrap_goto(self):
        u = self.kd.unwrap_goto
        self.assertEqual(u("https://www.google.com/goto?url=https%3A%2F%2Fb.com%2Fp%3Fx%3D1"), "https://b.com/p?x=1")
        self.assertEqual(u("https://www.google.es/goto?url=https://b.com/"), "https://b.com/")
        # only Google hosts are unwrapped, and only to http(s) targets
        self.assertEqual(u("https://b.com/goto?url=https://evil.com/"), "https://b.com/goto?url=https://evil.com/")
        self.assertEqual(u("https://www.google.com/goto"), "https://www.google.com/goto")
        self.assertEqual(u("https://www.google.com/goto?url=javascript:alert(1)"),
                         "https://www.google.com/goto?url=javascript:alert(1)")
        self.assertEqual(u("https://a.com/"), "https://a.com/")
        self.assertEqual(u(""), "")

    def test_norm_url(self):
        n = self.kd.norm_url
        self.assertEqual(n("https://www.A.com/guia/#x"), n("http://a.com/guia"))
        self.assertNotEqual(n("https://a.com/?p=1"), n("https://a.com/?p=2"))

    # ---- clustering
    def test_cluster_empty_and_single(self):
        self.assertEqual(self.kd.cluster_keywords({}), [])
        c = self.kd.cluster_keywords({"a": ["https://x.com/1"]})
        self.assertEqual(len(c), 1)
        self.assertEqual(c[0]["keywords"], ["a"])
        self.assertEqual(c[0]["shared_urls"], [])
        self.assertIsNone(c[0]["total_volume"])

    def test_cluster_threshold_and_volume(self):
        urls = [f"https://s{i}.com/" for i in range(10)]
        serps = {"a": urls[:5], "b": urls[2:7], "c": urls[4:9], "d": urls[:5]}
        res = self.kd.cluster_keywords(serps, 3, {"a": 100, "b": 50, "c": 10, "d": 5})
        # a shares 3 with b and 5 with d, but only 1 with c
        self.assertEqual([k["keywords"] for k in res], [["a", "b", "d"], ["c"]])
        self.assertEqual(res[0]["total_volume"], 155)
        self.assertIn("https://s2.com/", res[0]["shared_urls"])
        strict = self.kd.cluster_keywords(serps, 4, {"a": 100})
        self.assertEqual(sorted(len(k["keywords"]) for k in strict), [1, 1, 2])
        # threshold 1 and the head a: b and c both touch a's URLs? c only through s4, which a also has
        loose = self.kd.cluster_keywords(serps, 1, {"a": 100})
        self.assertEqual(len(loose), 1)

    def test_cluster_no_chaining_and_ties(self):
        # b overlaps a (2) and c (3), a and c do not overlap: with head b both join; with head a, c stays out
        serps = {"a": ["1", "2", "3"], "b": ["2", "3", "4", "5", "6"], "c": ["4", "5", "6"]}
        with_b = self.kd.cluster_keywords(serps, 2, {"b": 10})
        self.assertEqual(with_b[0]["keywords"], ["b", "a", "c"])
        with_a = self.kd.cluster_keywords(serps, 2, {"a": 10})
        self.assertEqual([c["keywords"] for c in with_a], [["a", "b"], ["c"]])
        # input order does not matter, and ties in volume are broken alphabetically
        again = self.kd.cluster_keywords(dict(reversed(list(serps.items()))), 2, {"b": 10})
        self.assertEqual(with_b, again)
        tie = self.kd.cluster_keywords({"zeta": ["1", "2", "3"], "alfa": ["1", "2", "3"]}, 3)
        self.assertEqual(tie[0]["cluster"], "alfa")

    def test_cluster_empty_serp_is_flagged(self):
        res = self.kd.cluster_keywords({"a": [], "b": [], "c": ["1"]}, 3)
        self.assertEqual(len(res), 3)  # empty SERPs never merge with each other
        self.assertTrue(next(r for r in res if r["cluster"] == "a")["no_serp"])
        self.assertFalse(next(r for r in res if r["cluster"] == "c")["no_serp"])

    def test_cluster_goto_urls_match_real(self):
        serps = {"a": ["https://www.google.com/goto?url=https%3A%2F%2Fx.com%2Fp", "https://y.com/", "https://z.com/"],
                 "b": ["https://x.com/p/", "https://y.com", "https://z.com/"]}
        self.assertEqual(len(self.kd.cluster_keywords(serps, 3)), 1)

    # ---- subcommands against the mock
    def test_kw_volume(self):
        code, out, err = self.run_cmd("kw-volume", "--keywords", "SEO, sin datos,seo")
        self.assertEqual(code, 0)
        rows = list(csv.DictReader(io.StringIO(out)))
        self.assertEqual(rows[0]["search_volume"], "5400")
        self.assertEqual(rows[1]["search_volume"], "")  # no data stays empty, never guessed
        self.assertIn("cost: $0.0125", err)
        task = mock_apis.DFS_LAST["task"]
        self.assertEqual(task["keywords"], ["seo", "sin datos"])  # lowercased and deduplicated
        self.assertEqual((task["location_code"], task["language_code"]), (2724, "es"))
        self.assertTrue(mock_apis.DFS_LAST["auth"].startswith("Basic "))
        self.assertNotIn("secret-pass", err + out)

    def test_location_override(self):
        self.run_cmd("kw-volume", "--keywords", "seo", "--location-code", "2840", "--language-code", "en")
        self.assertEqual(mock_apis.DFS_LAST["task"]["location_code"], 2840)

    def test_kw_ideas(self):
        code, out, _ = self.run_cmd("kw-ideas", "--keywords", "seo", "--min-volume", "500", "--limit", "50")
        self.assertEqual(code, 0)
        rows = list(csv.DictReader(io.StringIO(out)))
        self.assertEqual(rows[0]["keyword"], "seo local")
        self.assertEqual(rows[0]["keyword_difficulty"], "31")
        self.assertEqual(rows[1]["main_intent"], "")
        task = mock_apis.DFS_LAST["task"]
        self.assertEqual(task["limit"], 50)
        self.assertEqual(task["filters"], ["keyword_info.search_volume", ">=", 500])

    def test_serp_top10_organic_and_goto(self):
        code, out, _ = self.run_cmd("serp", "--keywords", "seo")
        self.assertEqual(code, 0)
        rows = list(csv.DictReader(io.StringIO(out)))
        # paid, position 11 and the repeated a.com/guia are dropped; the goto wrapper is unwrapped
        self.assertEqual([r["position"] for r in rows], ["1", "2", "3", "4"])
        self.assertEqual(rows[1]["url"], "https://b.com/post?x=1")
        self.assertEqual(rows[1]["domain"], "b.com")

    def test_serp_json_and_no_organic(self):
        code, out, _ = self.run_cmd("serp", "--keywords", "vacio", "--format", "json")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(out), [{"keyword": "vacio", "results": []}])

    def test_kw_cluster_end_to_end(self):
        with tempfile.TemporaryDirectory() as d:
            f = os.path.join(d, "kws.txt")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write("seo\nseo gratis\nvacio\n")
            code, out, err = self.run_cmd("kw-cluster", "--keywords-file", f, "--min-shared", "3")
            self.assertEqual(code, 0)
            clusters = json.loads(out)
            self.assertEqual(clusters[0]["keywords"], ["seo", "seo gratis"])
            self.assertTrue(any(c["no_serp"] and c["cluster"] == "vacio" for c in clusters))
            self.assertIn("total cost", err)
            # from a saved SERP file plus volumes, as CSV
            serp_f, vol_f, out_f = (os.path.join(d, n) for n in ("s.json", "v.csv", "c.csv"))
            self.run_cmd("serp", "--keywords-file", f, "--format", "json", "--out", serp_f)
            with open(vol_f, "w", encoding="utf-8") as fh:
                fh.write("keyword,search_volume\nseo,100\nseo gratis,20\n")
            code, _, _ = self.run_cmd("kw-cluster", "--serp-file", serp_f, "--volumes", vol_f, "--format", "csv",
                                      "--out", out_f)
            self.assertEqual(code, 0)
            with open(out_f, encoding="utf-8") as fh:
                rows = list(csv.DictReader(fh))
            self.assertEqual(rows[0]["total_volume"], "120")
            self.assertEqual(rows[0]["keywords"], "seo | seo gratis")

    def test_serp_csv_feeds_cluster(self):
        with tempfile.TemporaryDirectory() as d:
            f, s = os.path.join(d, "k.txt"), os.path.join(d, "s.csv")
            with open(f, "w", encoding="utf-8") as fh:
                fh.write("seo\nseo gratis\n")
            self.run_cmd("serp", "--keywords-file", f, "--out", s)
            code, out, _ = self.run_cmd("kw-cluster", "--serp-file", s)
            self.assertEqual(json.loads(out)[0]["keyword_count"], 2)

    # ---- safety rails
    def test_max_keywords_cap_refuses(self):
        mock_apis.DFS_LAST.clear()
        code, _, err = self.run_cmd("kw-volume", "--keywords", "a,b,c", "--max-keywords", "2")
        self.assertEqual(code, 2)
        self.assertIn("--max-keywords", err)
        self.assertEqual(mock_apis.DFS_LAST, {})  # nothing was sent

    def test_dry_run_sends_nothing_and_needs_no_credentials(self):
        mock_apis.DFS_LAST.clear()
        saved = {k: os.environ.pop(k) for k in ("DATAFORSEO_LOGIN", "DATAFORSEO_PASSWORD")}
        try:
            for cmd in (["kw-volume"], ["kw-ideas"], ["serp"], ["kw-cluster"]):
                code, out, err = self.run_cmd(*cmd, "--keywords", "a,b", "--dry-run")
                self.assertEqual((code, out), (0, ""), cmd)
                self.assertIn("DRY RUN", err)
        finally:
            os.environ.update(saved)
        self.assertEqual(mock_apis.DFS_LAST, {})

    def test_requires_credentials_and_keywords(self):
        saved = {k: os.environ.pop(k) for k in ("DATAFORSEO_LOGIN", "DATAFORSEO_PASSWORD")}
        try:
            code, _, err = self.run_cmd("kw-volume", "--keywords", "a")
            self.assertEqual(code, 2)
            self.assertIn("DATAFORSEO_LOGIN", err)
        finally:
            os.environ.update(saved)
        code, _, err = self.run_cmd("serp")
        self.assertEqual(code, 2)
        self.assertIn("No keywords", err)

    def test_task_error_is_reported(self):
        code, _, err = self.run_cmd("serp", "--keywords", "sinsaldo")
        self.assertEqual(code, 2)
        self.assertIn("40200", err)


if __name__ == "__main__":
    unittest.main()
