#!/usr/bin/env python3
from __future__ import annotations

import json
import importlib.util
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
CLI = SKILL_DIR / "scripts" / "cli.py"
XML_PROBE = "https://www.legislation.govt.nz/act/public/1990/109/en/latest.xml/"


def run(args: list[str], *, env: dict[str, str] | None = None) -> subprocess.CompletedProcess:
    child_env = os.environ.copy()
    if env:
        child_env.update(env)
    return subprocess.run(
        [sys.executable, str(CLI), *args],
        capture_output=True,
        text=True,
        cwd=str(SKILL_DIR),
        timeout=90,
        env=child_env,
    )


def parse_json(args: list[str]) -> dict:
    result = run(args)
    if result.returncode != 0:
        try:
            error = json.loads(result.stdout)
        except json.JSONDecodeError:
            error = {}
        error_code = error.get("error", "")
        error_text = " ".join([error_code, result.stderr, error.get("message", "")])
        if "upstream_" in error_text or "bot-protection" in error_text:
            print(f"[SKIP] upstream unavailable for {' '.join(args)}: {error_text.strip()[:300]}")
            raise SystemExit(0)
        raise AssertionError(
            f"command failed: {' '.join(args)}\nstdout: {result.stdout[:400]}\nstderr: {result.stderr[:400]}"
        )
    return json.loads(result.stdout)


def parse_json_error(args: list[str], *, env: dict[str, str] | None = None) -> dict:
    result = run(args, env=env)
    if result.returncode == 0:
        raise AssertionError(f"expected failure for {' '.join(args)}")
    if "Traceback" in result.stderr:
        raise AssertionError(f"unexpected traceback for {' '.join(args)}: {result.stderr[:400]}")
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise AssertionError(
            f"expected JSON error for {' '.join(args)}\nstdout: {result.stdout[:400]}\nstderr: {result.stderr[:400]}"
        ) from exc


def check(name: str, fn) -> bool:
    try:
        outcome = fn()
        if outcome is False:
            raise AssertionError("check returned False")
        print(f"[PASS] {name}")
        return True
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001
        print(f"[FAIL] {name}\n  error: {exc}")
        return False


def upstream_available() -> bool:
    try:
        req = urllib.request.Request(
            XML_PROBE,
            headers={
                "User-Agent": "thecolab-ai-legislation-nz-smoke/1.0",
                "Accept": "application/xml,text/xml",
            },
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read(120)
            return resp.status == 200 and b"<act" in body
    except Exception as exc:  # noqa: BLE001
        print(f"[SKIP] legislation.govt.nz XML endpoint unavailable: {exc}")
        return False


def test_fixture_legislation_parsers() -> bool:
    spec = importlib.util.spec_from_file_location("legislation_cli", CLI)
    cli = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = cli
    spec.loader.exec_module(cli)
    ref = cli.parse_ref("1990/109")
    feed = cli.parse_atom_feed(b'''<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>Example Act</title><link href="https://www.legislation.govt.nz/act/public/1990/109/en/latest/"/><updated>2026-01-02T00:00:00Z</updated><summary>Updated text</summary></entry></feed>''')
    return ref["year"] == "1990" and ref["number"] == "109" and feed[0]["title"] == "Example Act"


if not check("fixture legislation reference and Atom parsing", test_fixture_legislation_parsers):
    raise SystemExit(1)


if not upstream_available():
    raise SystemExit(0)


results: list[bool] = []

results.append(
    check(
        "--help exits 0",
        lambda: (
            run(["--help"]).returncode == 0
            and "get-section" in run(["--help"]).stdout
            and "list-bills" in run(["--help"]).stdout
        ),
    )
)


def test_get_section() -> None:
    data = parse_json(["get-section", "1990/109", "5", "--json"])
    assert data["command"] == "get-section"
    assert data["status"] == "ok"
    assert data["act"]["title"] == "New Zealand Bill of Rights Act 1990"
    assert data["section"]["label"] == "5"
    assert "demonstrably justified" in data["section"]["text"]
    assert data["section"]["source_url"].endswith("/latest/#DLM225501")


results.append(check("get-section returns official section text", test_get_section))


def test_search() -> None:
    data = parse_json(["search", "Grocery Industry", "--type", "act", "--limit", "2", "--json"])
    assert data["command"] == "search"
    assert data["status"] == "ok"
    assert data["results"], data
    assert any("Grocery Industry Competition Act 2023" in item["title"] for item in data["results"])


results.append(check("search parses keyless official result cards", test_search))


def test_versions() -> None:
    data = parse_json(["versions", "1990/109", "--json"])
    assert data["command"] == "versions"
    assert data["status"] == "ok"
    assert len(data["versions"]) >= 4
    assert data["versions"][0]["as_at"] == "2022-08-30"


results.append(check("versions parses point-in-time versions", test_versions))


def test_list_bills() -> None:
    data = parse_json(["list-bills", "--limit", "2", "--json"])
    assert data["command"] == "list-bills"
    assert data["status"] == "ok"
    assert isinstance(data["results"], list)


results.append(check("list-bills parses current bill search", test_list_bills))


def test_updates() -> None:
    data = parse_json(["updates", "--since", "1900-01-01", "--limit", "2", "--json"])
    assert data["command"] == "updates"
    assert data["status"] == "ok"
    assert isinstance(data["results"], list)
    assert data["source_url"]


results.append(check("updates parses official feed", test_updates))


def test_api_key_required_json() -> None:
    data = parse_json_error(
        ["search", "test", "--source", "api", "--limit", "1", "--json"],
        env={"LEGISLATION_NZ_API_KEY": "", "PCO_API_KEY": ""},
    )
    assert data["command"] == "search"
    assert data["status"] == "error"
    assert data["error"] == "api_key_required"
    assert data["source_url"].endswith("/v0/works/")


results.append(check("api search key-required state is JSON", test_api_key_required_json))


def test_missing_section_edge() -> None:
    data = parse_json_error(["get-section", "1990/109", "9999", "--json"])
    assert data["error"] == "not_found"
    assert "section 9999 not found" in data["message"]


results.append(check("missing section edge case is clear", test_missing_section_edge))


if all(results):
    print("All tests passed.")
    raise SystemExit(0)

print(f"{results.count(False)} test(s) failed.")
raise SystemExit(1)
