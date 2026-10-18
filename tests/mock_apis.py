"""Tiny local stand-ins for the CrUX and PageSpeed Insights APIs, used by the tests (no network, no keys)."""
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

CRUX_RECORD = {"record": {"key": {"origin": "https://example.com"}, "metrics": {
    "largest_contentful_paint": {"histogram": [{"start": 0, "end": 2500, "density": 0.81}], "percentiles": {"p75": 2300}},
    "interaction_to_next_paint": {"histogram": [{"start": 0, "end": 200, "density": 0.62}], "percentiles": {"p75": 260}},
    "cumulative_layout_shift": {"histogram": [{"start": "0.00", "end": "0.10", "density": 0.9}], "percentiles": {"p75": "0.05"}},
    "first_contentful_paint": {"histogram": [{"start": 0, "end": 1800, "density": 0.85}], "percentiles": {"p75": 1500}},
    "experimental_time_to_first_byte": {"histogram": [{"start": 0, "end": 800, "density": 0.7}], "percentiles": {"p75": 900}}},
    "collectionPeriod": {"firstDate": {"year": 2026, "month": 9, "day": 18}, "lastDate": {"year": 2026, "month": 10, "day": 15}}}}
CRUX_HISTORY = {"record": {"key": {"origin": "https://example.com"}, "metrics": {
    "largest_contentful_paint": {"percentilesTimeseries": {"p75s": [2600, 2400]}},
    "interaction_to_next_paint": {"percentilesTimeseries": {"p75s": [None, 180]}},
    "cumulative_layout_shift": {"percentilesTimeseries": {"p75s": ["0.12", "0.08"]}}},
    "collectionPeriods": [{"firstDate": {"year": 2026, "month": 9, "day": 11}, "lastDate": {"year": 2026, "month": 10, "day": 8}},
                          {"firstDate": {"year": 2026, "month": 9, "day": 18}, "lastDate": {"year": 2026, "month": 10, "day": 15}}]}}
PSI = {"loadingExperience": {"metrics": {}},
       "originLoadingExperience": {"overall_category": "AVERAGE", "metrics": {
           "LARGEST_CONTENTFUL_PAINT_MS": {"percentile": 2100, "category": "FAST"},
           "INTERACTION_TO_NEXT_PAINT": {"percentile": 310, "category": "AVERAGE"},
           "CUMULATIVE_LAYOUT_SHIFT_SCORE": {"percentile": 7, "category": "FAST"}}},
       "lighthouseResult": {"categories": {"performance": {"score": 0.72}},
                            "audits": {"largest-contentful-paint": {"numericValue": 3120.5},
                                       "cumulative-layout-shift": {"numericValue": 0.021},
                                       "total-blocking-time": {"numericValue": 410}}}}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, obj):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        req = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        if "nodata" in json.dumps(req):
            return self._send(404, {"error": {"code": 404, "message": "chrome ux report data not found"}})
        if "queryHistoryRecord" in self.path:
            return self._send(200, CRUX_HISTORY)
        return self._send(200, CRUX_RECORD)

    def do_GET(self):
        if "runPagespeed" in self.path or self.path.startswith("/psi"):
            return self._send(200, PSI)
        return self._send(404, {})


def start():
    srv = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv
