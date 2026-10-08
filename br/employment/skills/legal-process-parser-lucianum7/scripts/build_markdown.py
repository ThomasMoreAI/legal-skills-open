from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .helpers import build_pages, build_structured_markdown, classify_process
except ImportError:
    from helpers import build_pages, build_structured_markdown, classify_process  # type: ignore


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera Markdown com separador e referência para cada página.")
    parser.add_argument("pages_json", type=Path)
    parser.add_argument("--output", type=Path, default=Path("processo_estruturado.md"))
    args = parser.parse_args()
    data = json.loads(args.pages_json.read_text(encoding="utf-8"))
    pages, _ = build_pages(data.get("pages", []))
    args.output.write_text(build_structured_markdown(pages, classify_process(pages)), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

