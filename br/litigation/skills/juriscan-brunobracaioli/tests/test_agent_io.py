"""Unit tests for scripts/agent_io.py — Phase 0 Step 0.3."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "agent_io.py"
FIXTURES = REPO_ROOT / "tests" / "fixtures" / "agent_io"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import agent_io  # noqa: E402


def _run(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        cwd=str(cwd) if cwd else None,
    )


# ---------- validate ----------

def test_validate_echo_valid():
    ok, errors = agent_io.validate_agent_output("echo", FIXTURES / "echo_valid.json")
    assert ok, errors
    assert errors == []


def test_validate_echo_missing_required_field():
    ok, errors = agent_io.validate_agent_output(
        "echo", FIXTURES / "echo_invalid_missing_field.json"
    )
    assert not ok
    assert any("input_echo" in e for e in errors)


def test_validate_echo_wrong_const():
    ok, errors = agent_io.validate_agent_output(
        "echo", FIXTURES / "echo_invalid_wrong_const.json"
    )
    assert not ok
    assert any("ok" in e for e in errors)


def test_validate_segmenter_valid():
    ok, errors = agent_io.validate_agent_output(
        "segmenter", FIXTURES / "segmenter_valid.json"
    )
    assert ok, errors


def test_validate_unknown_agent_raises():
    with pytest.raises(SystemExit):
        agent_io.validate_agent_output("ghost", FIXTURES / "echo_valid.json")


def test_validate_cli_exit_codes():
    r_ok = _run("validate", "--agent", "echo", "--input", str(FIXTURES / "echo_valid.json"))
    assert r_ok.returncode == 0, r_ok.stderr

    r_fail = _run(
        "validate",
        "--agent",
        "echo",
        "--input",
        str(FIXTURES / "echo_invalid_missing_field.json"),
    )
    assert r_fail.returncode == 1
    assert "FAIL" in r_fail.stderr


# ---------- new-run + log ----------

def test_new_run_creates_audit_file(tmp_path):
    audit_root = tmp_path / "audit"
    r = _run("new-run", "--root", str(audit_root))
    assert r.returncode == 0, r.stderr
    run_id = r.stdout.strip()
    assert len(run_id) == 36
    audit_file = audit_root / f"{run_id}.jsonl"
    assert audit_file.exists()
    lines = [json.loads(l) for l in audit_file.read_text().splitlines() if l]
    assert len(lines) == 1
    assert lines[0]["agent"] == "__meta__"


def test_log_appends_entry_with_input_hash(tmp_path):
    audit_root = tmp_path / "audit"
    r1 = _run("new-run", "--root", str(audit_root))
    run_id = r1.stdout.strip()

    r2 = _run(
        "log",
        "--run-id",
        run_id,
        "--agent",
        "echo",
        "--input",
        str(FIXTURES / "echo_valid.json"),
        "--latency-ms",
        "1234",
        "--schema-valid",
        "true",
        "--model-hint",
        "haiku",
        "--root",
        str(audit_root),
    )
    assert r2.returncode == 0, r2.stderr

    audit_file = audit_root / f"{run_id}.jsonl"
    lines = [json.loads(l) for l in audit_file.read_text().splitlines() if l]
    assert len(lines) == 2
    echo_entry = lines[1]
    assert echo_entry["agent"] == "echo"
    assert echo_entry["latency_ms"] == 1234
    assert echo_entry["schema_valid"] is True
    assert echo_entry["model_hint"] == "haiku"
    assert echo_entry["input_hash"] is not None
    assert len(echo_entry["input_hash"]) == 16


# ---------- extract-field ----------

def test_extract_field_scalar():
    value = agent_io.extract_field(FIXTURES / "echo_valid.json", ".agent")
    assert value == "juriscan-echo"


def test_extract_field_nested_array():
    value = agent_io.extract_field(
        FIXTURES / "segmenter_valid.json", ".chunks[0].id"
    )
    assert value == "c00"


def test_extract_field_array_root():
    value = agent_io.extract_field(FIXTURES / "segmenter_valid.json", ".chunks[1].tipo_provavel")
    assert value == "SENTENÇA"


def test_extract_field_missing_key_errors():
    with pytest.raises(SystemExit):
        agent_io.extract_field(FIXTURES / "echo_valid.json", ".nonexistent")


def test_extract_field_cli():
    r = _run(
        "extract-field",
        "--input",
        str(FIXTURES / "segmenter_valid.json"),
        "--jq",
        ".chunks[0].id",
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == "c00"
