#!/usr/bin/env python3
"""Bind a derived text file to the exact saved publisher bytes. Stdlib only."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from integrity import SCHEMA, IntegrityError, sha256_file, validate_fetch


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, help="saved instrument directory")
    parser.add_argument("derived", type=Path, help="derived text in that directory")
    parser.add_argument(
        "--method", required=True, help="conversion method, such as PDF text extraction"
    )
    parser.add_argument("--tool", required=True, help="exact tool and version")
    args = parser.parse_args()

    if args.derived.parent.resolve() != args.directory.resolve():
        sys.exit("The derived text must be inside the saved instrument directory.")
    receipt_path = args.directory / "transformation.json"
    if receipt_path.exists():
        sys.exit("Refusing to overwrite the existing transformation receipt.")
    try:
        fetch, _source, _identity = validate_fetch(args.directory)
        derived_hash = sha256_file(args.derived)
    except IntegrityError as error:
        sys.exit(str(error))
    receipt = {
        "schema": SCHEMA,
        "publisher_bytes_sha256": fetch["integrity"]["publisher_bytes_sha256"],
        "derived_text_sha256": derived_hash,
        "derived_name": args.derived.name,
        "method": args.method.strip(),
        "tool": args.tool.strip(),
    }
    if not receipt["method"] or not receipt["tool"]:
        sys.exit("Transformation method and exact tool/version are required.")
    receipt_path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(f"Recorded the conversion to {args.derived.name}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
