"""Tests for scripts/report_metrics.py — Phase 7 Step 7.1."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from report_metrics import (  # noqa: E402
    _percentile,
    enforce_budget,
    summarize_run,
)


def _entry(agent: str, latency: int | None = None, *, error: str | None = None,
           schema_valid: bool | None = True, ts: str = "2026-04-11T12:00:00+00:00") -> dict:
    return {
        "timestamp": ts,
        "run_id": "test",
        "agent": agent,
        "subagent_name": f"juriscan-{agent}",
        "model_hint": "haiku",
        "input_hash": "x",
        "output_path": "/tmp/x.json",
        "latency_ms": latency,
        "schema_valid": schema_valid,
        "error": error,
        "extra": {},
    }


# ---------- percentile helper ----------

def test_percentile_p50_odd():
    assert _percentile([1, 2, 3, 4, 5], 0.5) == 3


def test_percentile_p95():
    xs = list(range(1, 101))  # 1..100
    assert _percentile(xs, 0.95) == pytest.approx(95.05, rel=0.05)


def test_percentile_empty():
    assert _percentile([], 0.5) == 0.0


# ---------- summarize ----------

def test_summarize_single_agent():
    entries = [
        _entry("segmenter", 100),
        _entry("segmenter", 200),
        _entry("segmenter", 300),
    ]
    s = summarize_run(entries)
    assert s["total_invocations"] == 3
    assert s["unique_agents"] == 1
    assert s["per_agent"]["segmenter"]["invocations"] == 3
    assert s["per_agent"]["segmenter"]["latency_p95_ms"] == 290.0


def test_summarize_skips_meta_entries():
    entries = [
        _entry("__meta__", None, ts="2026-04-11T12:00:00+00:00"),
        _entry("segmenter", 100),
        _entry("parser", 150),
    ]
    s = summarize_run(entries)
    assert s["total_invocations"] == 2
    assert "__meta__" not in s["per_agent"]


def test_summarize_counts_errors_and_schema_invalid():
    entries = [
        _entry("parser", 100),
        _entry("parser", 200, error="timeout"),
        _entry("parser", 300, schema_valid=False),
    ]
    s = summarize_run(entries)
    assert s["error_count"] == 1
    assert s["schema_invalid_count"] == 1
    assert s["per_agent"]["parser"]["errors"] == 1


def test_summarize_elapsed_wall():
    entries = [
        _entry("__meta__", None, ts="2026-04-11T12:00:00+00:00"),
        _entry("segmenter", 100, ts="2026-04-11T12:00:05+00:00"),
        _entry("parser", 200, ts="2026-04-11T12:00:15+00:00"),
    ]
    s = summarize_run(entries)
    assert s["elapsed_wall_ms"] == 15000.0


def test_summarize_handles_missing_latency():
    entries = [
        _entry("parser", None),
        _entry("parser", None),
    ]
    s = summarize_run(entries)
    # All None latencies → per-agent latency stats are None
    assert s["per_agent"]["parser"]["latency_p50_ms"] is None


# ---------- budget gate ----------

def test_enforce_budget_latency_pass():
    summary = {
        "latency_p95_ms": 5000,
        "total_invocations": 10,
    }
    violations = enforce_budget(summary, max_p95_ms=10000, max_invocations=20)
    assert violations == []


def test_enforce_budget_latency_fail():
    summary = {
        "latency_p95_ms": 15000,
        "total_invocations": 10,
    }
    violations = enforce_budget(summary, max_p95_ms=10000, max_invocations=20)
    assert len(violations) == 1
    assert "latency p95" in violations[0]


def test_enforce_budget_invocations_fail():
    summary = {
        "latency_p95_ms": 5000,
        "total_invocations": 40,
    }
    violations = enforce_budget(summary, max_p95_ms=10000, max_invocations=30)
    assert len(violations) == 1
    assert "invocations" in violations[0]


def test_enforce_budget_both_fail():
    summary = {"latency_p95_ms": 20000, "total_invocations": 50}
    violations = enforce_budget(summary, max_p95_ms=10000, max_invocations=30)
    assert len(violations) == 2


# ---------- CLI integration ----------

def test_cli_json_output(tmp_path):
    root = tmp_path / "audit"
    root.mkdir()
    run_id = "fakeuuid"
    path = root / f"{run_id}.jsonl"
    lines = [
        _entry("__meta__", None),
        _entry("segmenter", 500),
        _entry("parser", 700),
        _entry("parser", 800),
    ]
    path.write_text("\n".join(json.dumps(l) for l in lines), encoding="utf-8")

    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "report_metrics.py"),
         "--root", str(root), "--run-id", run_id, "--json"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0, r.stderr
    data = json.loads(r.stdout)
    assert run_id in data
    assert data[run_id]["total_invocations"] == 3


def test_cli_enforce_exits_nonzero_on_violation(tmp_path):
    root = tmp_path / "audit"
    root.mkdir()
    run_id = "overbudget"
    path = root / f"{run_id}.jsonl"
    entries = [_entry("parser", 999999)] * 50
    path.write_text("\n".join(json.dumps(e) for e in entries), encoding="utf-8")

    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "report_metrics.py"),
         "--root", str(root), "--run-id", run_id, "--enforce",
         "--max-p95-ms", "1000", "--max-invocations", "10"],
        capture_output=True, text=True,
    )
    assert r.returncode == 1
    assert "BUDGET FAIL" in r.stderr
