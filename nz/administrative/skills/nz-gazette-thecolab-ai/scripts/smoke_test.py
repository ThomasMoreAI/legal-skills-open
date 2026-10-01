#!/usr/bin/env python3
"""Deterministic Gazette parser checks plus one bounded live probe."""

import json
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL.parents[1] / "lib"))
from gazette_notices import notice_type_codes, parse_notice, parse_search  # noqa: E402

stamp = "2026-07-19T00:00:00Z"
search = (SKILL / "tests/fixtures/search.html").read_text(encoding="utf-8")
rows = parse_search(search, "https://gazette.govt.nz/home/search?keyword=land", stamp)
assert rows == [{
    "id": "2003-md644", "title": "Project Solutions (NZ) Limited (in liquidation) and",
    "published_on": "2003-01-30", "notice_type": "Meetings/Last Dates for Debts & Claims",
    "acts": ["Companies Act"], "source_url": "https://gazette.govt.nz/notice/id/2003-md644",
    "retrieved_at": stamp, "legal_effect": "not determined by this connector",
}]
assert notice_type_codes(search)["land notices"] == "ln"
detail = parse_notice((SKILL / "tests/fixtures/notice.html").read_text(), "https://gazette.govt.nz/notice/id/2003-md644", stamp)
assert detail["id"] == "2003-md644" and detail["published_on"] == "2003-01-30"
assert detail["pdf_url"].endswith("/pdf") and "Meeting of Creditors" in detail["text"]
assert detail["issuing_authority"] == "Registrar of Companies" and detail["related_notices"][0]["id"] == "2003-md600"
print("[PASS] fixture Gazette search, category and full-notice parsing")

for invalid in (
    ("date", "--from", "not-a-date", "--to", "2026-07-19"),
    ("date", "--from", "2026-07-20", "--to", "2026-07-19"),
):
    completed = subprocess.run(
        [sys.executable, str(SKILL / "scripts/cli.py"), *invalid, "--json"],
        capture_output=True, text=True, timeout=10, check=False,
    )
    assert completed.returncode == 2
print("[PASS] Gazette date input fails before source retrieval")

completed = subprocess.run(
    [sys.executable, str(SKILL / "scripts/cli.py"), "latest", "--limit", "1", "--json"],
    capture_output=True, text=True, timeout=45, check=False,
)
if completed.returncode == 0:
    payload = json.loads(completed.stdout)
    assert payload["schema_version"] == "1" and payload["data"]
    assert payload["data"][0]["source_url"].startswith("https://gazette.govt.nz/notice/id/")
    print("[PASS] live official Gazette search")
elif completed.returncode in {4, 5}:
    print(f"[SKIP] Gazette source unavailable: {completed.stderr.strip()}")
else:
    print(completed.stderr, file=sys.stderr)
    raise SystemExit(1)
