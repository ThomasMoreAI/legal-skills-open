#!/usr/bin/env python3
"""Deterministic parser assertions plus a bounded live consultation probe."""

import json
import subprocess
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL.parents[1] / "lib"))

from govt_consultations import parse_consultations  # noqa: E402

SOURCE = "https://www.govt.nz/browse/engaging-with-government/consultations-have-your-say/consultations-listing/"
rows = parse_consultations(
    (SKILL / "tests" / "fixtures" / "consultations.html").read_text(encoding="utf-8"),
    SOURCE,
    "2026-07-19T00:00:00Z",
)
assert len(rows) == 2
assert rows[0]["agency"] == "Maritime New Zealand"
assert rows[0]["opens_on"] == "2026-06-15" and rows[0]["closes_on"] == "2026-07-28"
assert rows[0]["id"] == "coastal-navigation" and rows[0]["status"] == "open"
assert rows[0]["detail_url"].endswith("coastal-navigation")
assert rows[0]["submission_url"].endswith("coastal-navigation/submit")
assert rows[1]["status"] == "closed"
print("[PASS] fixture consultation fields, dates, status and canonical link")

completed = subprocess.run(
    [sys.executable, str(SKILL / "scripts" / "cli.py"), "open", "--limit", "2", "--json"],
    capture_output=True,
    text=True,
    timeout=45,
    check=False,
)
if completed.returncode == 0:
    payload = json.loads(completed.stdout)
    assert payload["schema_version"] == "1" and payload["source"]["url"] == SOURCE
    assert all(row["status"] == "open" for row in payload["data"])
    print("[PASS] live official consultation listing")
elif completed.returncode in {4, 5}:
    print(f"[SKIP] consultation source unavailable: {completed.stderr.strip()}")
else:
    print(completed.stderr, file=sys.stderr)
    raise SystemExit(1)
