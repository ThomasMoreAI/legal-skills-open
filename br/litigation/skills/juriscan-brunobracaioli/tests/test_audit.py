"""Unit tests for scripts/audit.py and scripts/cleanup_audit.py."""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import pytest

SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from audit import AuditLogger, hash_input, new_run_id  # noqa: E402
from cleanup_audit import cleanup, find_stale  # noqa: E402


def test_new_run_id_is_unique():
    a, b = new_run_id(), new_run_id()
    assert a != b
    assert len(a) == 36  # UUID v4


def test_hash_input_deterministic():
    assert hash_input("hello") == hash_input("hello")
    assert hash_input("hello") != hash_input("world")
    assert hash_input(b"bytes") == hash_input("bytes")
    assert len(hash_input("x")) == 16


def test_logger_writes_jsonl(tmp_path: Path):
    run_id = "test-run-1"
    logger = AuditLogger(run_id, root=tmp_path)

    logger.log_invocation(
        agent="segmenter",
        subagent_name="juriscan-segmenter",
        model_hint="haiku",
        input_hash=hash_input("raw text"),
        output_path=tmp_path / "seg.json",
        latency_ms=1234,
        schema_valid=True,
    )
    logger.log_invocation(
        agent="parser",
        subagent_name="juriscan-parser",
        latency_ms=2345,
        schema_valid=False,
        error="schema violation: missing field 'tipo_peca'",
    )

    audit_file = tmp_path / f"{run_id}.jsonl"
    assert audit_file.exists()

    lines = audit_file.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 2

    entry1 = json.loads(lines[0])
    assert entry1["agent"] == "segmenter"
    assert entry1["subagent_name"] == "juriscan-segmenter"
    assert entry1["latency_ms"] == 1234
    assert entry1["schema_valid"] is True
    assert entry1["error"] is None
    assert entry1["run_id"] == run_id
    assert "timestamp" in entry1
    assert "T" in entry1["timestamp"]  # ISO format

    entry2 = json.loads(lines[1])
    assert entry2["agent"] == "parser"
    assert entry2["schema_valid"] is False
    assert "schema violation" in entry2["error"]


def test_logger_is_append_only(tmp_path: Path):
    run_id = "test-run-2"
    logger_a = AuditLogger(run_id, root=tmp_path)
    logger_a.log_invocation(agent="a", subagent_name="juriscan-a")

    # Simulate a second process writing to the same run
    logger_b = AuditLogger(run_id, root=tmp_path)
    logger_b.log_invocation(agent="b", subagent_name="juriscan-b")
    logger_b.log_invocation(agent="c", subagent_name="juriscan-c")

    entries = logger_b.read_all()
    assert [e["agent"] for e in entries] == ["a", "b", "c"]


def test_logger_read_all_empty_when_file_absent(tmp_path: Path):
    logger = AuditLogger("no-file", root=tmp_path)
    logger.path.unlink(missing_ok=True)
    assert logger.read_all() == []


def test_logger_preserves_unicode(tmp_path: Path):
    logger = AuditLogger("u", root=tmp_path)
    logger.log_invocation(
        agent="parser",
        subagent_name="juriscan-parser",
        extra={"descricao": "sentença com acórdão e petição"},
    )
    raw = logger.path.read_text(encoding="utf-8")
    assert "sentença" in raw
    assert "acórdão" in raw


def test_cleanup_dry_run_does_not_delete(tmp_path: Path):
    old_file = tmp_path / "old.jsonl"
    old_file.write_text("{}\n")
    very_old = time.time() - 120 * 86400
    import os
    os.utime(old_file, (very_old, very_old))

    removed, total = cleanup(tmp_path, max_age_days=90, dry_run=True)
    assert total == 1
    assert removed == 0
    assert old_file.exists()


def test_cleanup_removes_stale_files(tmp_path: Path):
    import os

    fresh = tmp_path / "fresh.jsonl"
    fresh.write_text("{}\n")

    stale = tmp_path / "stale.jsonl"
    stale.write_text("{}\n")
    ancient = time.time() - 100 * 86400
    os.utime(stale, (ancient, ancient))

    removed, _ = cleanup(tmp_path, max_age_days=90, dry_run=False)
    assert removed == 1
    assert fresh.exists()
    assert not stale.exists()


def test_cleanup_ignores_non_jsonl(tmp_path: Path):
    import os

    other = tmp_path / "stale.txt"
    other.write_text("nope")
    ancient = time.time() - 200 * 86400
    os.utime(other, (ancient, ancient))

    stale_list = find_stale(tmp_path, max_age_days=90)
    assert stale_list == []


def test_cleanup_missing_root(tmp_path: Path):
    ghost = tmp_path / "does-not-exist"
    removed, total = cleanup(ghost, max_age_days=90, dry_run=False)
    assert removed == 0
    assert total == 0
