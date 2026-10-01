#!/usr/bin/env python3
"""Live smoke test for companies-office-nz skill.

Hits real Companies Office NZ endpoints. Requires network access.
Exits 0 on success, 1 if any test fails.
"""
import json
import importlib.util
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
CLI = SKILL_DIR / "scripts" / "cli.py"

XERO_ID = "1830488"
XERO_NZBN = "9429034042984"
TRADEME_ID = "973228"


def run(args: list) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(CLI)] + args,
        capture_output=True,
        text=True,
        cwd=str(SKILL_DIR),
        timeout=60,
    )


def ok(name: str, fn) -> bool:
    try:
        result = fn()
        status = "PASS" if result else "FAIL"
        print(f"[{status}] {name}")
        return bool(result)
    except Exception as exc:
        print(f"[FAIL] {name}")
        print(f"  exception: {exc}")
        return False


results: list[bool] = []


def test_fixture_normalizers():
    spec = importlib.util.spec_from_file_location("companies_office_cli", CLI)
    cli = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = cli
    spec.loader.exec_module(cli)
    return (
        cli._compact_addr(["Level 1", None, "Wellington"]) == "Level 1, Wellington"
        and cli._status_label(50) == "REGISTERED"
        and cli._strip_html("<b>Example</b>  Company") == "Example Company"
    )


results.append(ok("fixture company status, address and HTML normalization", test_fixture_normalizers))


# --help
def test_help():
    r = run(["--help"])
    return r.returncode == 0

results.append(ok("--help exits 0", test_help))


# search by name returns results with company_number
def test_search_name():
    r = run(["search", "xero", "--limit", "3", "--json"])
    if r.returncode != 0:
        print(f"  stderr: {r.stderr[:300]}")
        return False
    data = json.loads(r.stdout)
    results_list = data.get("results") or []
    if not results_list:
        print(f"  no results: {r.stdout[:200]}")
        return False
    if not results_list[0].get("company_number"):
        print("  missing company_number")
        return False
    return True

results.append(ok("search 'xero' returns results with company_number", test_search_name))


# search by company number
def test_search_by_number():
    r = run(["search", XERO_ID, "--limit", "1", "--json"])
    if r.returncode != 0:
        return False
    data = json.loads(r.stdout)
    hits = data.get("results") or []
    return any(h.get("company_number") == XERO_ID for h in hits)

results.append(ok(f"search by company number {XERO_ID} returns XERO", test_search_by_number))


# entity lookup by company number
def test_entity():
    r = run(["entity", XERO_ID, "--json"])
    if r.returncode != 0:
        print(f"  stderr: {r.stderr[:300]}")
        return False
    data = json.loads(r.stdout)
    e = data.get("entity") or {}
    if e.get("company_number") != XERO_ID:
        print(f"  wrong company number: {e.get('company_number')}")
        return False
    if not e.get("name"):
        print("  missing name")
        return False
    if not e.get("status"):
        print("  missing status")
        return False
    return True

results.append(ok(f"entity {XERO_ID} returns name and status", test_entity))


# entity lookup by NZBN
def test_entity_nzbn():
    r = run(["entity", "--nzbn", XERO_NZBN, "--json"])
    if r.returncode != 0:
        print(f"  stderr: {r.stderr[:300]}")
        return False
    data = json.loads(r.stdout)
    e = data.get("entity") or {}
    return e.get("company_number") == XERO_ID

results.append(ok(f"entity --nzbn {XERO_NZBN} resolves to company {XERO_ID}", test_entity_nzbn))


# directors
def test_directors():
    r = run(["directors", XERO_ID, "--json"])
    if r.returncode != 0:
        print(f"  stderr: {r.stderr[:300]}")
        return False
    data = json.loads(r.stdout)
    dirs = data.get("directors") or []
    if len(dirs) < 1:
        print(f"  no directors returned: {r.stdout[:300]}")
        return False
    if not dirs[0].get("name"):
        print("  first director missing name")
        return False
    return True

results.append(ok(f"directors {XERO_ID} returns at least one director with name", test_directors))


# shareholders
def test_shareholders():
    r = run(["shareholders", XERO_ID, "--json"])
    if r.returncode != 0:
        print(f"  stderr: {r.stderr[:300]}")
        return False
    data = json.loads(r.stdout)
    sh = data.get("shareholders") or {}
    allocs = sh.get("allocations") or []
    if not allocs:
        print(f"  no allocations returned: {r.stdout[:300]}")
        return False
    if not allocs[0].get("shares"):
        print("  first allocation missing shares")
        return False
    return True

results.append(ok(f"shareholders {XERO_ID} returns allocation with shares", test_shareholders))


# documents
def test_documents():
    r = run(["documents", XERO_ID, "--limit", "5", "--json"])
    if r.returncode != 0:
        print(f"  stderr: {r.stderr[:300]}")
        return False
    data = json.loads(r.stdout)
    docs = data.get("documents") or {}
    items = docs.get("documents") or []
    if not items:
        print(f"  no documents: {r.stdout[:300]}")
        return False
    if not items[0].get("type"):
        print("  first document missing type")
        return False
    total = docs.get("total", 0)
    if total < 100:
        print(f"  suspiciously low total: {total}")
        return False
    return True

results.append(ok(f"documents {XERO_ID} returns items with type and large total", test_documents))


# full command
def test_full():
    r = run(["full", TRADEME_ID, "--json"])
    if r.returncode != 0:
        print(f"  stderr: {r.stderr[:300]}")
        return False
    data = json.loads(r.stdout)
    if not data.get("entity", {}).get("name"):
        print("  full missing entity.name")
        return False
    if data.get("directors") is None:
        print("  full missing directors")
        return False
    if data.get("shareholders") is None:
        print("  full missing shareholders")
        return False
    if data.get("documents") is None:
        print("  full missing documents")
        return False
    return True

results.append(ok(f"full {TRADEME_ID} returns entity, directors, shareholders, documents", test_full))


# human output search
def test_human_search():
    r = run(["search", "trade me", "--limit", "3"])
    return r.returncode == 0 and "TRADE ME" in r.stdout.upper()

results.append(ok("human search output contains TRADE ME", test_human_search))


# human output entity
def test_human_entity():
    r = run(["entity", XERO_ID])
    return r.returncode == 0 and "XERO" in r.stdout.upper() and "REGISTERED" in r.stdout.upper()

results.append(ok("human entity output contains XERO and REGISTERED", test_human_entity))


# negative: unknown company number
def test_bad_id():
    r = run(["entity", "0000001"])
    return r.returncode != 0 or "error" in r.stderr.lower() or "no company" in r.stderr.lower() or len(r.stdout.strip()) == 0

results.append(ok("entity 0000001 (invalid) fails gracefully", test_bad_id))


if all(results):
    print("[PASS] live smoke assertions completed")
    sys.exit(0)
else:
    failed = results.count(False)
    print(f"\n{failed} test(s) failed.")
    sys.exit(1)
