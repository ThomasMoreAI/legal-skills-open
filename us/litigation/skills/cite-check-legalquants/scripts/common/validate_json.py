#!/usr/bin/env python3
"""Check that a file is readable UTF-8 JSON syntax.

This helper deliberately performs no JSON Schema validation.  Schema checks
belong to the report/worker contract validators, while this command provides a
small, dependency-free encoding and syntax preflight for host runtimes.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_json.py <file>", file=sys.stderr)
        return 2

    path = Path(argv[1])

    if not path.exists():
        print(f"missing: {path}", file=sys.stderr)
        return 1

    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"unreadable: {exc}", file=sys.stderr)
        return 1
    except UnicodeDecodeError as exc:
        print(f"invalid utf-8: {exc}", file=sys.stderr)
        return 1

    try:
        json.loads(text)
    except json.JSONDecodeError as exc:
        print(f"invalid json: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
