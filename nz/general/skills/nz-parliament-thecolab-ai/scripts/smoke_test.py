#!/usr/bin/env python3
"""Live read-only smoke tests for the nz-parliament skill (bills.parliament.nz).

Keyless; no browser. Network/upstream errors are treated as SKIP, not failures.
"""
import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
CLI = SKILL_DIR / "scripts" / "cli.py"


def run(args, timeout=45):
    return subprocess.run(
        [sys.executable, str(CLI)] + args,
        capture_output=True, text=True, cwd=str(SKILL_DIR), timeout=timeout,
    )


def test(name, fn):
    try:
        ok = fn()
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        return ok
    except Exception as e:  # noqa: BLE001
        print(f"[FAIL] {name}\n  error: {e}")
        return False


def is_transient(stderr):
    low = stderr.lower()
    return any(s in low for s in ("network error", "http 5", "timeout", "timed out"))


results = []
captured = {}


def test_bill_summary_fixture():
    import importlib.util

    spec = importlib.util.spec_from_file_location("nz_parliament_cli", CLI)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    record = module.normalise_summary(
        {
            "id": "synthetic-bill",
            "title": "Synthetic Amendment Bill",
            "billNumber": "123-1",
            "itemType": "Government",
            "billCurrentStageName": "First reading",
            "lastStageDate": "2026-07-19T01:02:03Z",
        }
    )
    assert record["id"] == "synthetic-bill"
    assert record["status"] == "First reading"
    assert record["url"].endswith("/synthetic-bill")
    print("[PASS] fixture Parliament bill-summary normalisation")
    return True


results.append(test("fixture bill summary parser", test_bill_summary_fixture))


def test_help():
    return run(["--help"]).returncode == 0


results.append(test("--help exits 0", test_help))


def test_bills():
    r = run(["bills", "--limit", "5", "--json"])
    if r.returncode != 0:
        if is_transient(r.stderr):
            print(f"  [SKIP] upstream unavailable: {r.stderr.strip()[:140]}")
            return True
        print(f"  stderr: {r.stderr[:200]}")
        return False
    d = json.loads(r.stdout)
    items = d.get("results")
    if not isinstance(items, list) or not items:
        print(f"  stdout: {r.stdout[:200]}")
        print("  Expected non-empty results[] of bills")
        return False
    first = items[0]
    if not all(k in first for k in ("id", "title", "bill_number", "type")):
        print(f"  Missing keys in bill: {first}")
        return False
    captured["bill_number"] = first["bill_number"]
    return True


results.append(test("bills lists current bills", test_bills))


def test_keyword():
    r = run(["bills", "--keyword", "amendment", "--all", "--limit", "3", "--json"])
    if r.returncode != 0:
        if is_transient(r.stderr):
            print(f"  [SKIP] upstream unavailable: {r.stderr.strip()[:140]}")
            return True
        print(f"  stderr: {r.stderr[:200]}")
        return False
    d = json.loads(r.stdout)
    if not isinstance(d.get("results"), list):
        print("  Expected results[] for keyword search")
        return False
    return True


results.append(test("bills keyword search", test_keyword))


def test_bill_detail():
    num = captured.get("bill_number")
    if not num:
        print("  [SKIP] no bill number captured from list step")
        return True
    r = run(["bill", num, "--json"])
    if r.returncode != 0:
        if is_transient(r.stderr):
            print(f"  [SKIP] upstream unavailable: {r.stderr.strip()[:140]}")
            return True
        print(f"  stderr: {r.stderr[:200]}")
        return False
    d = json.loads(r.stdout)
    if not d.get("title") or "stages" not in d:
        print(f"  stdout: {r.stdout[:200]}")
        print("  Expected bill detail with title and stages[]")
        return False
    return True


results.append(test("bill <number> returns detail + stages", test_bill_detail))

if all(results):
    print("[PASS] live smoke assertions completed")
    sys.exit(0)
print(f"{results.count(False)} test(s) failed.")
sys.exit(1)
