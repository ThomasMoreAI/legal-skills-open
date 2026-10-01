#!/usr/bin/env python3
import contextlib,importlib.util,io,json,subprocess,sys
from pathlib import Path
S=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(S.parents[1]/"lib"))
from hansard_transcript import oral_question_excerpt,parse_listing,parse_transcript  # noqa: E402
r=parse_transcript((S/"tests/fixtures/transcript.html").read_text(),"https://hansard.parliament.nz/hansard-transcript/2025-10-15","2026-07-19T00:00:00Z")
assert r["volume"]=="787" and r["sitting_date_text"]=="15 October 2025" and len(r["turns"])==3
q=oral_question_excerpt(r); assert q[0]["title"]=="Question No. 1—Prime Minister" and "Third Reading" not in q[0]["text"]
assert "Prime Minister" in q[0]["text"] and all(turn["source_url"].startswith("https://hansard.parliament.nz/") for turn in r["turns"])
assert len(r["turns"]) == 3 and all("Debate resumed" not in turn["text"] for turn in r["turns"])
assert r["turns"][0]["speaker"] == "Rt Hon CHRIS HIPKINS"
assert r["turns"][0]["role_or_party"] == "Leader of the Opposition"
assert r["turns"][0]["speaker_as_published"] == "Rt Hon CHRIS HIPKINS (Leader of the Opposition)"
assert r["turns"][0]["retrieved_at"] == "2026-07-19T00:00:00Z" and r["turns"][0]["transcript_status"] == "official"
listing_html=(S/"tests/fixtures/listing.html").read_text()
transcript_html=(S/"tests/fixtures/transcript.html").read_text()
listing=parse_listing(listing_html,"https://hansard.parliament.nz/","2026-07-19T00:00:00Z");assert [row["id"] for row in listing]==["2025-10-15","2025-10-14"]
print("[PASS] fixture Hansard sitting metadata, speaker turns and oral-question boundary")
spec=importlib.util.spec_from_file_location("nz_hansard_cli",S/"scripts/cli.py");cli=importlib.util.module_from_spec(spec);spec.loader.exec_module(cli)
calls=[]
def fake_fetch(url):
 calls.append(url)
 return listing_html if url==cli.HOME else transcript_html
cli._fetch=fake_fetch
old_argv=sys.argv
try:
 sys.argv=[str(S/"scripts/cli.py"),"search","Prime Minister","--sittings","2","--limit","10","--json"]
 output=io.StringIO()
 with contextlib.redirect_stdout(output):assert cli.main()==0
finally:sys.argv=old_argv
payload=json.loads(output.getvalue());assert len(payload["data"])==2 and len({row["transcript_source_url"] for row in payload["data"]})==2
assert calls==[cli.HOME,"https://hansard.parliament.nz/hansard-transcript/2025-10-15","https://hansard.parliament.nz/hansard-transcript/2025-10-14"]
print("[PASS] undated Hansard search covers the requested bounded sitting corpus")
invalid=subprocess.run([sys.executable,str(S/"scripts/cli.py"),"search","budget","--date","not-a-date","--json"],capture_output=True,text=True,timeout=10)
assert invalid.returncode==2 and "valid YYYY-MM-DD" in invalid.stderr
print("[PASS] Hansard dates fail before source retrieval")
run=subprocess.run([sys.executable,str(S/"scripts/cli.py"),"oral-questions","--date","2025-10-15","--json"],capture_output=True,text=True,timeout=45)
if run.returncode==0:
 p=json.loads(run.stdout); assert p["source"]["url"].endswith("2025-10-15") and p["data"]; print("[PASS] live official Hansard transcript")
elif run.returncode in {4,5}: print(f"[SKIP] Hansard blocked/unavailable: {run.stderr.strip()}")
else: print(run.stderr,file=sys.stderr); raise SystemExit(1)
