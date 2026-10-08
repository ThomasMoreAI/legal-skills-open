#!/usr/bin/env python3
"""
Phase 10.7 — Run all Phase 10 Python tests sequentially.

Runs:
  1. test_build_cross_references.py — citation regex extraction tests
  2. test_monitor_rss.py            — RSS monitor parsing/classification tests
  3. test_regulations_fts.py        — regulations FTS5 end-to-end tests

Exit code 0 if all pass, non-zero on first failure.
"""
import subprocess
import sys
from pathlib import Path

TESTS = [
    'scripts/test_build_cross_references.py',
    'scripts/test_monitor_rss.py',
    'scripts/test_regulations_fts.py',
]

def main() -> int:
    print('=' * 60)
    print('Phase 10 — Running all Python tests')
    print('=' * 60)
    print()
    repo_root = Path(__file__).parent.parent
    failed = []
    for test in TESTS:
        test_path = repo_root / test
        if not test_path.exists():
            print(f'❌ MISSING: {test}')
            failed.append(test)
            continue
        print(f'▶ Running: {test}')
        result = subprocess.run(
            [sys.executable, str(test_path)],
            cwd=str(repo_root),
            capture_output=False,
        )
        print()
        if result.returncode != 0:
            print(f'❌ FAILED: {test}')
            failed.append(test)
        else:
            print(f'✅ PASSED: {test}')
        print('-' * 60)

    print()
    if failed:
        print(f'❌ {len(failed)} test file(s) failed: {failed}')
        return 1
    print(f'✅ All {len(TESTS)} test files passed')
    return 0

if __name__ == '__main__':
    sys.exit(main())
