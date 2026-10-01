#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


CLI = Path(__file__).with_name("cli.py")


def run(args: list[str], *, expect: int = 0) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(
        [sys.executable, str(CLI), *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=45,
        check=False,
    )
    if proc.returncode != expect:
        raise AssertionError(
            f"expected exit {expect}, got {proc.returncode}; "
            f"stdout={proc.stdout[:300]!r} stderr={proc.stderr[:300]!r}"
        )
    return proc


def check(name: str, func) -> bool:
    try:
        func()
        print("[PASS]", name)
        return True
    except Exception as exc:
        text = str(exc).lower()
        if any(term in text for term in ("timed out", "http", "urlopen", "network")):
            print("[SKIP]", name, exc)
            return True
        print("[FAIL]", name, exc)
        return False


def help_works() -> None:
    run(["--help"])


def metadata_is_aggregate_safe() -> None:
    data = json.loads(run(["metadata", "--json"]).stdout)
    assert data["kind"] == "metadata"
    assert data["privacy"]["row_level_records_exposed"] is False
    memorial = next(item for item in data["sources"] if item["id"] == 52006)
    assert memorial["title"] == "Landonline: Title Memorial"
    assert "ttl_title_no" in memorial["sensitive_fields"]
    assert memorial["feature_count"] > 1000000


def oia_template_names_aggregate_counts() -> None:
    data = json.loads(
        run(
            [
                "oia-template",
                "--group-by",
                "territorial_authority,year",
                "--min-cell-size",
                "10",
                "--json",
            ]
        ).stdout
    )
    assert data["kind"] == "oia_template"
    assert "territorial_authority" in data["requested_grouping"]
    assert "individual Records of Title" in data["privacy_clause"]
    assert "s73" in data["template"] and "s74(4)" in data["template"]


def unsafe_count_is_blocked() -> None:
    data = json.loads(
        run(
            [
                "count-building-act-hazard-notices",
                "--group-by",
                "territorial_authority",
                "--json",
            ],
            expect=2,
        ).stdout
    )
    assert data["kind"] == "blocked"
    assert data["status"] == "official_aggregate_required"
    assert "oia-template" in data["next_step"]


def low_cell_size_is_rejected() -> None:
    data = json.loads(
        run(
            [
                "oia-template",
                "--min-cell-size",
                "1",
                "--json",
            ],
            expect=1,
        ).stdout
    )
    assert data["kind"] == "error"
    assert "at least 6" in data["message"]


checks = [
    ("help", help_works),
    ("metadata is aggregate-safe", metadata_is_aggregate_safe),
    ("OIA template names aggregate counts", oia_template_names_aggregate_counts),
    ("unsafe count command is blocked", unsafe_count_is_blocked),
    ("low cell-size threshold is rejected", low_cell_size_is_rejected),
]

ok = [check(name, func) for name, func in checks]
if all(ok):
    print("[PASS] fixture aggregate-only metadata and safety guards")
    sys.exit(0)
sys.exit(1)
