#!/usr/bin/env python3
import json,subprocess,sys
from pathlib import Path
S=Path(__file__).resolve().parents[1];sys.path.insert(0,str(S.parents[1]/"lib"))
from select_committees import parse_detail,parse_listing  # noqa: E402
rows=parse_listing((S/"tests/fixtures/open.html").read_text(),"https://www3.parliament.nz/en/pb/sc/make-a-submission/open/","2026-07-19T00:00:00Z")
assert len(rows)==2 and rows[0]["date"]=="2026-07-19" and rows[0]["status"]=="open" and rows[0]["source_url"].startswith("https://www3.parliament.nz/")
assert rows[0]["closing_at"].startswith("2026-07-19T23:59:00+") and rows[0]["timezone"]=="Pacific/Auckland"
detail=parse_detail((S/"tests/fixtures/detail.html").read_text(),rows[0]["source_url"],"2026-07-19T00:00:00Z")
assert detail["membership"][0]["role"]=="Chairperson" and detail["evidence"][0]["url"].endswith("evidence.pdf")
navigation=parse_listing((S/"tests/fixtures/navigation-only.html").read_text(),"https://www3.parliament.nz/en/pb/sc/make-a-submission/open/","2026-07-19T00:00:00Z")
empty=parse_listing((S/"tests/fixtures/empty-reports.html").read_text(),"https://www3.parliament.nz/en/pb/sc/reports/all/","2026-07-19T00:00:00Z")
assert navigation==[] and empty==[]
print("[PASS] fixture select-committee title, deadline, status and canonical URL")
for invalid in (("reports","--since","not-a-date"),("reports","--since","2026-02-30")):
 run=subprocess.run([sys.executable,str(S/"scripts/cli.py"),*invalid,"--json"],capture_output=True,text=True,timeout=10)
 assert run.returncode==2 and "valid YYYY-MM-DD" in run.stderr
print("[PASS] select-committee dates fail before source retrieval")
run=subprocess.run([sys.executable,str(S/"scripts/cli.py"),"open-submissions","--limit","2","--json"],capture_output=True,text=True,timeout=45)
if run.returncode==0:
 p=json.loads(run.stdout);assert p["source"]["url"].endswith("/open/");print("[PASS] live official open-submissions listing")
elif run.returncode in {4,5}:print(f"[SKIP] Parliament blocked/unavailable: {run.stderr.strip()}")
else:print(run.stderr,file=sys.stderr);raise SystemExit(1)
