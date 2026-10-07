#!/usr/bin/env python3
"""Test runner for the us-state-privacy-navigator skill.

Discovers all test_*.py files in the tests/ directory and runs them.
Returns exit 0 if all pass, exit 1 if any fail.

Usage:
    python tests/run_all.py             # run all tests
    python tests/run_all.py -v          # verbose
    python -m unittest discover tests   # equivalent stdlib invocation

Run from any directory; the script resolves paths relative to itself.
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TESTS_DIR = ROOT / "tests"


def main() -> int:
    verbose = "-v" in sys.argv or "--verbose" in sys.argv
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(TESTS_DIR), pattern="test_*.py")
    runner = unittest.TextTestRunner(verbosity=2 if verbose else 1)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
