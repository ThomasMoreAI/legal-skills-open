#!/usr/bin/env python3
"""Smoke tests for nz-ai-policy skill."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CLI = ROOT / "skills" / "nz-ai-policy" / "scripts" / "cli.py"


def run_cmd(*args: str, timeout: int = 30) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CLI), *args],
        cwd=str(ROOT),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )


def require_json(proc: subprocess.CompletedProcess[str]) -> dict:
    if proc.returncode != 0:
        raise AssertionError(f"command failed: {proc.args}\nSTDOUT={proc.stdout}\nSTDERR={proc.stderr}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise AssertionError(f"invalid JSON from {proc.args}: {exc}\n{proc.stdout[:500]}") from exc


def main() -> int:
    sources = require_json(run_cmd("sources", "--json"))
    assert sources["count"] >= 20, sources["count"]
    ids = {s["id"] for s in sources["sources"]}
    for expected in {"digital-ai-framework", "data-algorithm-charter", "privacy-ai", "mbie-ai-strategy", "psc-oia-ai-policy"}:
        assert expected in ids, expected

    briefing = require_json(run_cmd("briefing", "public-sector", "--json"))
    assert briefing["topic"] == "public-sector"
    assert briefing["sources"], "briefing must cite sources"
    assert "Not legal advice" in briefing["disclaimer"]

    search = require_json(run_cmd("search", "human oversight", "--json"))
    assert search["count"] >= 1, search
    assert any("human oversight" in " ".join(r.get("snippets", [])).lower() or r["source"]["id"] in {"digital-accountability", "data-algorithm-charter"} for r in search["results"])

    checklist = require_json(run_cmd("checklist", "agency-genai-policy", "--json"))
    assert len(checklist["items"]) >= 8
    assert any("privacy" in item.lower() for item in checklist["items"])

    # Live fetch of a source known to permit plain HTTP in normal environments.
    fetch = require_json(run_cmd("fetch", "privacy-ai", "--json", timeout=45))
    if not fetch.get("ok"):
        # Upstream/network flakiness should not fail CI for a source-map skill.
        print(f"SKIP live fetch check: {fetch.get('error')} {fetch.get('detail', '')}")
    else:
        assert fetch["url"].startswith("https://www.privacy.org.nz/")
        assert fetch.get("preview") or fetch.get("metadata_only")
        print("[PASS] live official privacy AI source retrieval")

    # Edge case: unknown source must fail clearly, not stack trace.
    bad = run_cmd("fetch", "not-a-source", "--json")
    assert bad.returncode != 0
    assert "unknown source id" in bad.stderr

    print("[PASS] fixture policy source map, briefing, search, checklist and error handling")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
