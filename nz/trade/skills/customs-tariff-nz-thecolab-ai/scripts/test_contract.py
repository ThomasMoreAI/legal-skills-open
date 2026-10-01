#!/usr/bin/env python3
"""Deterministic repository contract test for this skill."""
import importlib
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "lib"))

run_contract_test = importlib.import_module("contract_test").run_contract_test

if __name__ == "__main__":
    raise SystemExit(run_contract_test(Path(__file__).resolve().parents[1]))
