from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .helpers import build_pages, identify_pieces
except ImportError:
    from helpers import build_pages, identify_pieces  # type: ignore


def main() -> int:
    parser = argparse.ArgumentParser(description="Identifica transições de peças por heurística conservadora.")
    parser.add_argument("pages_json", type=Path)
    parser.add_argument("--output", type=Path, default=Path("pecas.json"))
    args = parser.parse_args()
    data = json.loads(args.pages_json.read_text(encoding="utf-8"))
    pages, _ = build_pages(data.get("pages", []))
    args.output.write_text(json.dumps({"pieces": identify_pieces(pages)}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

