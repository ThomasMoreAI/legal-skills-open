#!/usr/bin/env python3
import json,subprocess,sys
from pathlib import Path
S=Path(__file__).resolve().parents[1];sys.path.insert(0,str(S.parents[1]/"lib"))
from court_judgments import judge_match_evidence, parse_case_page, parse_judgments, parse_search_results, text_matches_query  # noqa: E402
rows=parse_judgments((S/"tests/fixtures/judgments.html").read_text(),"https://www.courtsofnz.govt.nz/judgments/high-court","2026-07-19T00:00:00Z","NZHC")
assert len(rows)==2 and rows[0]["citation"]=="[2026] NZHC 2040" and rows[0]["date"]=="2026-07-16" and rows[0]["document_url"].endswith("2026-NZHC-2040.pdf")
assert rows[0]["judges"]=="Palmer J" and parse_judgments("<p>No results found</p>","https://www.courtsofnz.govt.nz/judgments/high-court","2026-07-19T00:00:00Z","NZHC",allow_empty=True)==[]
search_url="https://www.courtsofnz.govt.nz/search/SearchForm?Search=Cooke"
hits=parse_search_results((S/"tests/fixtures/search-results.html").read_text(),search_url,"2026-07-19T00:00:00Z","Cooke")
assert len(hits)==1 and hits[0]["citation"]=="[2025] NZCA 650" and hits[0]["search_match_basis"].startswith("official Courts")
detail=parse_case_page((S/"tests/fixtures/case-page.html").read_text(),hits[0]["case_page_url"],"2026-07-19T00:00:00Z")
assert detail["date"]=="2025-12-10" and detail["document_url"].endswith("2025-NZCA-650.pdf") and detail["judges"] is None
assert text_matches_query(detail["summary"],"trade marks") and not text_matches_query(detail["summary"],"Zuru astronaut")
assert "Cooke J" in judge_match_evidence(detail["summary"],"Cooke") and judge_match_evidence(detail["summary"],"Zuru") is None
try:
 parse_search_results("<html>scheduled maintenance</html>",search_url,"2026-07-19T00:00:00Z","Cooke")
 raise AssertionError("maintenance HTML must fail closed")
except ValueError:pass
print("[PASS] fixture court case name, citation, date, summary and PDF provenance")
print("[PASS] fixture canonical search filtering, schema failure and judge-context provenance")
run=subprocess.run([sys.executable,str(S/"scripts/cli.py"),"recent","--court","NZHC","--limit","2","--json"],capture_output=True,text=True,timeout=45)
if run.returncode==0:
 p=json.loads(run.stdout);assert p["data"] and all(r["court"]=="NZHC" for r in p["data"]);print("[PASS] live official High Court public-interest judgments")
elif run.returncode in {4,5}:print(f"[SKIP] Courts source blocked/unavailable: {run.stderr.strip()}")
else:print(run.stderr,file=sys.stderr);raise SystemExit(1)
