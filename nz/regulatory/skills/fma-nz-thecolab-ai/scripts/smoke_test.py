#!/usr/bin/env python3
"""Outage-tolerant smoke test for fma-nz."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
CLI = SKILL_DIR / "scripts" / "cli.py"


def run(args: list[str], timeout: int = 60):
    return subprocess.run(
        [sys.executable, str(CLI), *args],
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def parse_json(process: subprocess.CompletedProcess[str]) -> dict:
    payload_text = process.stdout.strip() or process.stderr.strip()
    return json.loads(payload_text)


def check_json_result(process: subprocess.CompletedProcess[str], expected_kind: str | None = None) -> dict:
    payload = parse_json(process)
    if expected_kind and payload.get("kind") != expected_kind:
        raise AssertionError(f"expected kind={expected_kind}, got={payload.get('kind')}")
    return payload


def maybe_skip_upstream(process: subprocess.CompletedProcess[str], label: str) -> bool:
    try:
        payload = parse_json(process)
    except json.JSONDecodeError:
        return False
    if process.returncode == 2 and payload.get("error") == "upstream_unavailable":
        print(f"SKIP: {label}: {payload.get('message', 'upstream blocked')}" )
        return True
    return False


def main() -> int:
    import importlib.util

    spec = importlib.util.spec_from_file_location("fma_nz_cli", CLI)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    record = module.parse_list_item(
        """
        <h3><a href="/library/warnings-and-alerts/synthetic-warning/">Synthetic warning</a></h3>
        <p>Synthetic warning summary.</p>
        <span class="search-results-semantic__date">19 July 2026</span>
        """,
        "https://www.fma.govt.nz/library/warnings-and-alerts/",
    )
    if not record or record["id"] != "synthetic-warning" or record["date"] != "2026-07-19":
        print("[FAIL] fixture FMA warning-list parser")
        return 1
    print("[PASS] fixture FMA warning-list parser")

    help_proc = run(["--help"], timeout=20)
    if help_proc.returncode != 0 or "warnings" not in help_proc.stdout:
        print(help_proc.stdout)
        print(help_proc.stderr)
        print("FAIL: --help")
        return 1

    warnings_list = run(["warnings", "list", "--limit", "1", "--json"], timeout=90)
    if maybe_skip_upstream(warnings_list, "warnings list"):
        return 0
    if warnings_list.returncode != 0:
        print(warnings_list.stdout)
        print(warnings_list.stderr)
        print("FAIL: warnings list")
        return 1

    payload = check_json_result(warnings_list, expected_kind="fma_warnings_search")
    if not isinstance(payload.get("records"), list):
        print(payload)
        print("FAIL: warnings list records not list")
        return 1

    warnings_get = run(["warnings", "get", "deepfake-video-scam-warning", "--json"], timeout=90)
    if warnings_get.returncode == 2:
        if not maybe_skip_upstream(warnings_get, "warnings get"):
            print(warnings_get.stdout)
            print("FAIL: warnings get")
            return 1
    elif warnings_get.returncode != 0:
        print(warnings_get.stdout)
        print(warnings_get.stderr)
        print("FAIL: warnings get")
        return 1

    if warnings_get.returncode == 0:
        warn_payload = check_json_result(warnings_get, expected_kind="fma_warning_detail")
        if not warn_payload.get("record", {}).get("source_url"):
            print(warn_payload)
            print("FAIL: warnings get missing source_url")
            return 1

    providers_sources = run(["providers", "sources", "--type", "crowdfunding", "--json"], timeout=60)
    if providers_sources.returncode == 2 and not maybe_skip_upstream(providers_sources, "providers sources"):
        print("FAIL: providers sources returned upstream code 2")
        return 1
    if providers_sources.returncode == 0:
        src_payload = check_json_result(providers_sources, expected_kind="fma_provider_sources")
        if not src_payload.get("sources"):
            print(src_payload)
            print("FAIL: providers sources has no entries")
            return 1

    providers_list = run(["providers", "list", "--type", "crowdfunding", "--limit", "2", "--json"], timeout=90)
    if providers_list.returncode == 2 and maybe_skip_upstream(providers_list, "providers list"):
        return 0
    if providers_list.returncode != 0:
        print(providers_list.stdout)
        print(providers_list.stderr)
        print("FAIL: providers list")
        return 1

    list_payload = check_json_result(providers_list, expected_kind="fma_provider_search")
    if not isinstance(list_payload.get("records"), list):
        print(list_payload)
        print("FAIL: providers list records")
        return 1

    print("[PASS] live FMA search and register assertions completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
