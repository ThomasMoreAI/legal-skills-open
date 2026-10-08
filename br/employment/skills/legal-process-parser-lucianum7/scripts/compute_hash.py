from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .helpers import sha256_file
except ImportError:
    from helpers import sha256_file  # type: ignore


def main() -> int:
    parser = argparse.ArgumentParser(description="Calcula SHA-256 de um arquivo sem alterá-lo.")
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    path = args.file.resolve()
    print(json.dumps({"file": str(path), "size_bytes": path.stat().st_size, "sha256": sha256_file(path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

