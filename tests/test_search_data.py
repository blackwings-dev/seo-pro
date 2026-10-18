import csv
import io
import os
import unittest
from contextlib import redirect_stderr, redirect_stdout

import _paths  # noqa: F401
import mock_apis


class SearchDataTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srv = mock_apis.start()
        port = cls.srv.server_address[1]
        os.environ.update(CRUX_API_BASE=f"http://127.0.0.1:{port}", PSI_API_BASE=f"http://127.0.0.1:{port}/psi",
                          CRUX_API_KEY="test-key")
        import importlib
        import search_data
        cls.sd = importlib.reload(search_data)  # pick up the mock endpoints

    @classmethod
    def tearDownClass(cls):
        cls.srv.shutdown()

    def run_cmd(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = self.sd.main(list(args))
        return code, list(csv.DictReader(io.StringIO(out.getvalue())))

    def test_crux_origin(self):
        code, rows = self.run_cmd("crux", "--origin", "https://example.com", "--pause", "0")
        self.assertEqual(code, 0)
        r = rows[0]
        self.assertEqual(r["LCP_ms_rating"], "good")
        self.assertEqual(r["INP_ms_rating"], "needs improvement")
        self.assertEqual(r["CLS"], "0.05")
        self.assertEqual(r["core_web_vitals"], "fail")
        self.assertEqual(r["period"], "2026-09-18..2026-10-15")

    def test_crux_no_data_and_fallback(self):
        _, rows = self.run_cmd("crux", "--url", "https://example.com/nodata", "--pause", "0")
        self.assertIn("no CrUX data", rows[0]["note"])
        _, rows = self.run_cmd("crux", "--url", "https://example.com/nodata", "--fallback-origin", "--pause", "0")
        self.assertEqual(rows[0]["scope"], "origin (fallback)")

    def test_crux_history_nulls(self):
        _, rows = self.run_cmd("crux", "--origin", "https://example.com", "--history")
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["INP_ms"], "")
        self.assertEqual(rows[1]["CLS_rating"], "good")

    def test_crux_requires_key(self):
        key = os.environ.pop("CRUX_API_KEY")
        try:
            code, _ = self.run_cmd("crux", "--origin", "https://example.com")
            self.assertEqual(code, 2)
        finally:
            os.environ["CRUX_API_KEY"] = key

    def test_psi_origin_fallback_and_cls_scale(self):
        code, rows = self.run_cmd("psi", "--url", "https://example.com/", "--pause", "0")
        self.assertEqual(code, 0)
        r = rows[0]
        self.assertEqual(r["field_scope"], "origin")
        self.assertEqual(r["CLS"], "0.07")  # PSI reports CLS x100
        self.assertEqual(r["lab_performance_score"], "72")

    def test_bing_dates(self):
        self.assertEqual(self.sd._bing_value("/Date(1760054400000-0700)/"), "2025-10-09")


if __name__ == "__main__":
    unittest.main()
