"""Tiny local stand-ins for the CrUX, PageSpeed Insights and DataForSEO APIs, used by the tests (no network, no keys)."""
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

# DataForSEO: the same responses for every call; the last request received is kept for the assertions.
DFS_LAST: dict = {}


def dfs_envelope(result, cost=0.0125, task_code=20000):
    return {"version": "0.1", "status_code": 20000, "status_message": "Ok.", "cost": cost, "tasks_count": 1,
            "tasks_error": 0 if task_code == 20000 else 1,
            "tasks": [{"status_code": task_code, "status_message": "Ok." if task_code == 20000 else "Payment Required.",
                       "cost": cost, "result": result}]}


def dfs_serp(keyword):
    def org(rank, url, title):
        return {"type": "organic", "rank_group": rank, "rank_absolute": rank + 1, "url": url, "title": title,
                "domain": url.split("/")[2]}
    if keyword == "vacio":
        return [{"keyword": keyword, "items": [{"type": "people_also_ask", "rank_group": 1}]}]
    items = [org(1, "https://www.a.com/guia/", "Guia A"),
             {"type": "paid", "rank_group": 1, "url": "https://ads.example/"},
             org(2, "https://www.google.com/goto?url=https%3A%2F%2Fb.com%2Fpost%3Fx%3D1", "Post B"),
             org(3, "https://c.com/", "C"), org(4, "https://d.com/", "D"),
             org(5, "https://a.com/guia", "Guia A repetida"), org(11, "https://fuera.com/", "Fuera del top 10")]
    return [{"keyword": keyword, "items": items}]


DFS_VOLUME = [{"keyword": "seo", "search_volume": 5400, "cpc": 1.2, "competition": "LOW", "competition_index": 12,
               "low_top_of_page_bid": 0.5, "high_top_of_page_bid": 2.1},
              {"keyword": "sin datos", "search_volume": None, "cpc": None, "competition": None,
               "competition_index": None}]
DFS_IDEAS = [{"seed_keywords": ["seo"], "items": [
    {"keyword": "seo local", "keyword_info": {"search_volume": 880, "cpc": 0.9, "competition": 0.3,
                                             "competition_level": "LOW"},
     "keyword_properties": {"keyword_difficulty": 31}, "search_intent_info": {"main_intent": "commercial"}},
    {"keyword": "que es seo", "keyword_info": {"search_volume": 2400, "cpc": None, "competition_level": None},
     "keyword_properties": None, "search_intent_info": None}]}]


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

    def _dfs(self, req):
        task = req[0]
        DFS_LAST.update(path=self.path, auth=self.headers.get("Authorization"), task=task)
        if self.headers.get("Authorization") is None:
            return self._send(401, {"status_message": "unauthorized"})
        if "search_volume" in self.path:
            return self._send(200, dfs_envelope(DFS_VOLUME))
        if "keyword_ideas" in self.path:
            return self._send(200, dfs_envelope(DFS_IDEAS))
        if task.get("keyword") == "sinsaldo":
            return self._send(200, dfs_envelope(None, cost=0, task_code=40200))
        return self._send(200, dfs_envelope(dfs_serp(task["keyword"])))

    def do_POST(self):
        req = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
        if self.path.startswith("/dfs/"):
            return self._dfs(req)
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
