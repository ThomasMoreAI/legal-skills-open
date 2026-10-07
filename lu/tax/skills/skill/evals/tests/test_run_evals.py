"""Tests unitaires basiques pour run_evals.py (parsing, cache, agrégation)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import run_evals  # noqa: E402


def test_cache_key_stable():
    k1 = run_evals.cache_key("hello", "skill", "claude-sonnet-4-5")
    k2 = run_evals.cache_key("hello", "skill", "claude-sonnet-4-5")
    assert k1 == k2
    assert len(k1) == 16


def test_cache_key_different():
    k1 = run_evals.cache_key("a", "skill", "model")
    k2 = run_evals.cache_key("b", "skill", "model")
    assert k1 != k2


def test_load_config():
    cfg = run_evals.load_config()
    assert "subject_model" in cfg
    assert "judge_model" in cfg
    assert "skills" in cfg
    assert len(cfg["skills"]) == 6


def test_load_test_cases_existing():
    data = run_evals.load_test_cases("notaire")
    assert data["skill"] == "notaire"
    assert len(data["cases"]) > 0
    for c in data["cases"]:
        assert "id" in c
        assert "prompt" in c


def test_load_test_cases_unknown():
    data = run_evals.load_test_cases("nonexistent-skill")
    assert data["cases"] == []


if __name__ == "__main__":
    import traceback

    failures = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"  ✓ {name}")
            except AssertionError:
                print(f"  ✗ {name}")
                traceback.print_exc()
                failures += 1
    raise SystemExit(failures)
