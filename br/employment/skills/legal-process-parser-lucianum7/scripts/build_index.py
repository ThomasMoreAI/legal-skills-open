from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .helpers import build_index_records, build_pages
except ImportError:
    from helpers import build_index_records, build_pages  # type: ignore


def main() -> int:
    parser = argparse.ArgumentParser(description="Cria índice JSONL com texto e metadados de cada página.")
    parser.add_argument("pages_json", type=Path)
    parser.add_argument("--process", default="não identificado")
    parser.add_argument("--output", type=Path, default=Path("index.jsonl"))
    args = parser.parse_args()
    data = json.loads(args.pages_json.read_text(encoding="utf-8"))
    pages, _ = build_pages(data.get("pages", []))
    with args.output.open("w", encoding="utf-8", newline="\n") as handle:
        for record in build_index_records(pages, args.process):
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

