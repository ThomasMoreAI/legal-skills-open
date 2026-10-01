#!/usr/bin/env python3
"""Bounded fixture and live smoke checks for NZ regulatory analysis."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

SKILL_DIR = Path(__file__).resolve().parents[1]
CLI = SKILL_DIR / "scripts" / "cli.py"
PARSER_TEST = SKILL_DIR / "tests" / "test_parser.py"
EMPTY_QUERY = "zzzznosuchregulatoryitem8f3c2d1a"


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-B", *args],
        cwd=SKILL_DIR,
        text=True,
        capture_output=True,
        timeout=45,
        check=False,
    )


def live(args: list[str], label: str) -> tuple[dict[str, Any] | None, bool]:
    try:
        result = run([str(CLI), *args, "--json"])
    except subprocess.TimeoutExpired:
        print(f"[SKIP] live {label} timed out")
        return None, True
    if result.returncode in {4, 5}:
        try:
            payload = json.loads(result.stdout)
            assert payload["ok"] is False
            assert payload["blocked"] is (result.returncode == 4)
        except (AssertionError, json.JSONDecodeError, KeyError, TypeError):
            print(f"[FAIL] live {label} unavailable response violated the error contract")
            return None, False
        print(f"[SKIP] live {label} unavailable with explicit exit {result.returncode}")
        return None, True
    if result.returncode != 0:
        print(f"[FAIL] live {label}")
        print((result.stdout + result.stderr).strip())
        return None, False
    try:
        return json.loads(result.stdout), True
    except json.JSONDecodeError as exc:
        print(f"[FAIL] live {label} returned invalid JSON: {exc}")
        return None, False


def check_empty(source: str) -> bool:
    payload, ok = live(["search", EMPTY_QUERY, "--source", source, "--limit", "3"], f"{source} empty search")
    if not ok:
        return False
    if payload is None:
        return True
    try:
        assert payload["ok"] is True and payload["blocked"] is False
        assert payload["data"]["returned"] == 0
        assert payload["data"]["results"] == []
        assert payload["data"]["source_totals"][source] == 0
        assert payload["source"]["retrieved_at"].endswith("Z")
    except (AssertionError, KeyError, TypeError, ValueError) as exc:
        print(f"[FAIL] live {source} empty result contract: {exc}")
        return False
    print(f"[PASS] live {source} empty search is distinct from blocked/parser failures")
    return True


def main() -> int:
    fixture = run([str(PARSER_TEST)])
    if fixture.returncode != 0:
        print("[FAIL] deterministic fixture/adversarial contracts")
        print((fixture.stdout + fixture.stderr).strip())
        return 1
    print(fixture.stdout.strip())

    help_result = run([str(CLI), "--help"])
    if help_result.returncode != 0 or "{search,inspect}" not in help_result.stdout:
        print("[FAIL] CLI does not expose search and inspect")
        return 1
    print("[PASS] contract CLI help exposes positional search and inspect commands")

    regulation, ok = live(
        ["search", "climate", "--source", "regulation", "--limit", "25"],
        "regulation paginated search",
    )
    if not ok:
        return 1
    if regulation is not None:
        try:
            data = regulation["data"]
            total = data["source_totals"]["regulation"]
            assert regulation["schema_version"] == "1" and regulation["ok"] is True
            assert regulation["query"] == {"command": "search", "text": "climate", "source": "regulation", "limit": 25}
            assert 1 <= data["returned"] <= 25 and total >= data["returned"]
            assert len(data["source_urls"]) > 1 if total > 12 else len(data["source_urls"]) == 1
            assert all(row["url"].startswith("https://www.regulation.govt.nz/") and row["document_type"] for row in data["results"])
        except (AssertionError, KeyError, TypeError, ValueError) as exc:
            print(f"[FAIL] live regulation pagination/total contract: {exc}")
            return 1
        print("[PASS] live regulation search follows pagination and reports an accurate bounded total")
    if not check_empty("regulation"):
        return 1

    environment, ok = live(
        ["search", "freshwater", "--source", "environment", "--limit", "5"],
        "environment normal search",
    )
    if not ok:
        return 1
    if environment is not None:
        try:
            data = environment["data"]
            assert environment["schema_version"] == "1" and environment["ok"] is True
            assert 1 <= data["returned"] <= 5
            assert data["source_totals"]["environment"] >= data["returned"]
            row = data["results"][0]
            assert row["url"].startswith("https://environment.govt.nz/") and row["document_type"]
        except (AssertionError, KeyError, TypeError, ValueError, IndexError) as exc:
            print(f"[FAIL] live environment normal result contract: {exc}")
            return 1
        print("[PASS] live environment normal search returns bounded typed official results")

        detail, detail_ok = live(["inspect", row["url"]], "environment detail inspection")
        if not detail_ok:
            return 1
        if detail is not None:
            try:
                publication = detail["data"]
                assert publication["page_url"].startswith("https://environment.govt.nz/")
                assert publication["title"] and publication["document_count"] == len(publication["documents"])
                if "cabinet paper" not in publication["title"].casefold():
                    assert publication["document_type"] != "cabinet_paper"
            except (AssertionError, KeyError, TypeError, ValueError) as exc:
                print(f"[FAIL] live environment detail/classification contract: {exc}")
                return 1
            print("[PASS] live environment detail inspection does not classify from its directory path")
    if not check_empty("environment"):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
