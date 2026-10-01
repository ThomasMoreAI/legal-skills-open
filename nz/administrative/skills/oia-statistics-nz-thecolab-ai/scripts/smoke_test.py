#!/usr/bin/env python3
"""Smoke tests for oia-statistics-nz.

Network-dependent commands return upstream_unavailable on blocked/outage states and
are treated as skip conditions.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "cli.py"


def run(args: list[str], timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(CLI), *args], text=True, capture_output=True, timeout=timeout)


def parse_json_output(proc: subprocess.CompletedProcess[str]) -> dict:
    payload = (proc.stdout or proc.stderr).strip()
    return json.loads(payload or "{}") if payload else {}


def is_upstream_skip(proc: subprocess.CompletedProcess[str]) -> tuple[bool, str]:
    if proc.returncode != 2:
        return False, ""
    try:
        data = parse_json_output(proc)
    except Exception:
        return False, ""
    if data.get("error") == "upstream_unavailable":
        return True, str(data.get("message", ""))
    return False, ""


def main() -> int:
    import importlib.util

    spec = importlib.util.spec_from_file_location("oia_statistics_cli", CLI)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    record = module.row_enriched(
        {
            "OrgID": "42",
            "Agency": "Synthetic Agency",
            "Agency_Type": "Department",
            "SurveyPeriodEndDate": "2025-12-31T00:00:00",
            "OIA_RequestsHandled": "200",
            "OIAs_CompletedWithinTimeframe": "180",
            "OIA_refused": "10",
        }
    )
    if record["org_id"] != 42 or record["timeliness_pct"] != 90.0 or record["refusals_pct"] != 5.0:
        print("[FAIL] fixture OIA CSV row normalisation", file=sys.stderr)
        return 1
    print("[PASS] fixture OIA CSV row normalisation")

    help_proc = run(["--help"], timeout=20)
    if help_proc.returncode != 0 or "list-agencies" not in (help_proc.stdout or ""):
        print("FAIL: --help should list available commands", file=sys.stderr)
        print(help_proc.stdout)
        print(help_proc.stderr, file=sys.stderr)
        return 1

    periods = run(["periods", "--limit", "1", "--json"])
    if periods.returncode == 2:
        skip, message = is_upstream_skip(periods)
        if skip:
            print(f"SKIP: upstream unavailable ({message})")
            return 0
        print(periods.stderr or periods.stdout, file=sys.stderr)
        return 1
    if periods.returncode != 0:
        print(periods.stderr or periods.stdout, file=sys.stderr)
        return 1

    periods_data = parse_json_output(periods)
    if periods_data.get("kind") != "oia-periods" or not isinstance(periods_data.get("periods"), list):
        print("FAIL: periods command did not return expected JSON shape", file=sys.stderr)
        print(periods.stdout, file=sys.stderr)
        return 1
    latest_period = periods_data.get("latest_period")
    print(f"[PASS] live periods returned {periods_data.get('count')} period(s)")

    agencies = run(["list-agencies", "--limit", "3", "--json"])
    if agencies.returncode == 2:
        skip, message = is_upstream_skip(agencies)
        if skip:
            print(f"SKIP: upstream unavailable ({message})")
            return 0
        print(agencies.stderr or agencies.stdout, file=sys.stderr)
        return 1
    if agencies.returncode != 0:
        print(agencies.stderr or agencies.stdout, file=sys.stderr)
        return 1
    agencies_data = parse_json_output(agencies)
    agency_rows = agencies_data.get("agencies") or []
    if agencies_data.get("kind") != "oia-list-agencies" or not agency_rows:
        print("FAIL: list-agencies command did not return expected agency rows", file=sys.stderr)
        print(agencies.stdout, file=sys.stderr)
        return 1

    org_id = agency_rows[0].get("org_id")
    if isinstance(org_id, int):
        agency = run(["agency", str(org_id), "--json"], timeout=180)
        if agency.returncode == 2:
            skip, message = is_upstream_skip(agency)
            if skip:
                print(f"SKIP: upstream unavailable ({message})")
                return 0
            print(agency.stderr or agency.stdout, file=sys.stderr)
            return 1
        if agency.returncode != 0:
            print(agency.stderr or agency.stdout, file=sys.stderr)
            return 1
        agency_data = parse_json_output(agency)
        if agency_data.get("kind") != "oia-agency" or not agency_data.get("records"):
            print("FAIL: agency command did not return expected records", file=sys.stderr)
            print(agency.stdout, file=sys.stderr)
            return 1
        print(f"[PASS] live agency lookup by OrgID {org_id} returned {len(agency_data['records'])} rows")

    totals = run(["totals", "--period", latest_period or "latest", "--json"], timeout=120)
    if totals.returncode == 2:
        skip, message = is_upstream_skip(totals)
        if skip:
            print(f"SKIP: upstream unavailable ({message})")
            return 0
        print(totals.stderr or totals.stdout, file=sys.stderr)
        return 1
    if totals.returncode != 0:
        print(totals.stderr or totals.stdout, file=sys.stderr)
        return 1
    totals_data = parse_json_output(totals)
    if totals_data.get("kind") != "oia-totals" or not isinstance(totals_data.get("totals"), dict):
        print("FAIL: totals command did not return expected shape", file=sys.stderr)
        print(totals.stdout, file=sys.stderr)
        return 1
    if totals_data['totals'].get('requests_handled', 0) <= 0:
        print("FAIL: totals command returned no handled requests", file=sys.stderr)
        return 1
    print(f"[PASS] live totals returned requests_handled={totals_data['totals'].get('requests_handled')}")

    complaints = run(["complaints", "--period", latest_period or "latest", "--sort", "complaints", "--limit", "5", "--json"], timeout=120)
    if complaints.returncode != 0:
        print(complaints.stderr or complaints.stdout, file=sys.stderr)
        return 1
    complaints_data = parse_json_output(complaints)
    records = complaints_data.get("records", [])
    if any((r.get("org_id") in (0, None)) or r.get("agency_type") == "Agency Type Totals" for r in records):
        print("FAIL: complaints includes aggregate rows", file=sys.stderr)
        return 1
    counts = [r.get("complaints", 0) for r in records]
    if counts != sorted(counts, reverse=True):
        print("FAIL: complaints sort is not descending", file=sys.stderr)
        return 1
    print("[PASS] live complaints excludes aggregate rows and sorts descending")

    return 0


if __name__ == "__main__":
    sys.exit(main())
