#!/usr/bin/env python3
"""Live read-only smoke tests for the nz-comcom skill (comcom.govt.nz).

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


def cards_ok(stdout, key="results"):
    d = json.loads(stdout)
    items = d.get(key)
    if not isinstance(items, list) or not items:
        return None
    first = items[0]
    return first if all(k in first for k in ("title", "url")) else None


results = []
captured = {}


def test_card_parser_fixture():
    import importlib.util

    spec = importlib.util.spec_from_file_location("nz_comcom_cli", CLI)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    source = """
    <article class="card card--has-link">
      <a class="card__link" href="/case-register/synthetic-case"><strong>Synthetic case</strong></a>
      <div class="card__status">Open</div>
      <div class="card__summary">A synthetic &amp; deterministic summary.</div>
      <div class="card__info">Updated July 2026</div>
    </article>
    """
    records = module.parse_cards(source, 5)
    assert len(records) == 1
    assert records[0]["title"] == "Synthetic case"
    assert records[0]["status"] == "Open"
    assert records[0]["url"] == "https://www.comcom.govt.nz/case-register/synthetic-case"
    print("[PASS] fixture Commerce Commission card parser")
    return True


results.append(test("fixture listing card parser", test_card_parser_fixture))


def test_help():
    return run(["--help"]).returncode == 0


results.append(test("--help exits 0", test_help))


def test_search():
    r = run(["search", "grocery", "--limit", "5", "--json"])
    if r.returncode != 0:
        if is_transient(r.stderr):
            print(f"  [SKIP] upstream unavailable: {r.stderr.strip()[:140]}")
            return True
        print(f"  stderr: {r.stderr[:200]}")
        return False
    first = cards_ok(r.stdout)
    if not first:
        print(f"  stdout: {r.stdout[:200]}")
        print("  Expected non-empty results[] with title+url")
        return False
    return True


results.append(test("search returns result cards", test_search))


def test_cases():
    r = run(["cases", "--limit", "5", "--json"])
    if r.returncode != 0:
        if is_transient(r.stderr):
            print(f"  [SKIP] upstream unavailable: {r.stderr.strip()[:140]}")
            return True
        print(f"  stderr: {r.stderr[:200]}")
        return False
    first = cards_ok(r.stdout)
    if not first:
        print(f"  stdout: {r.stdout[:200]}")
        print("  Expected non-empty case register results[]")
        return False
    captured["case_url"] = first["url"]
    return True


results.append(test("cases lists case register entries", test_cases))


def test_news():
    r = run(["news", "--limit", "5", "--json"])
    if r.returncode != 0:
        if is_transient(r.stderr):
            print(f"  [SKIP] upstream unavailable: {r.stderr.strip()[:140]}")
            return True
        print(f"  stderr: {r.stderr[:200]}")
        return False
    if not cards_ok(r.stdout):
        print(f"  stdout: {r.stdout[:200]}")
        print("  Expected non-empty news results[]")
        return False
    return True


results.append(test("news lists media releases", test_news))


def test_page():
    url = captured.get("case_url", "https://www.comcom.govt.nz/about-us/our-role/competition-studies/")
    r = run(["page", url, "--json"])
    if r.returncode != 0:
        if is_transient(r.stderr):
            print(f"  [SKIP] upstream unavailable: {r.stderr.strip()[:140]}")
            return True
        print(f"  stderr: {r.stderr[:200]}")
        return False
    d = json.loads(r.stdout)
    if not d.get("title") or "documents" not in d:
        print(f"  stdout: {r.stdout[:200]}")
        print("  Expected page detail with title and documents[]")
        return False
    return True


results.append(test("page returns detail + documents", test_page))

if all(results):
    print("[PASS] live smoke assertions completed")
    sys.exit(0)
print(f"{results.count(False)} test(s) failed.")
sys.exit(1)
