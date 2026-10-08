from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .helpers import extract_pages_with_ocr
except ImportError:
    from helpers import extract_pages_with_ocr  # type: ignore


def main() -> int:
    parser = argparse.ArgumentParser(description="Extrai texto página a página; não executa conteúdo do PDF.")
    parser.add_argument("file", type=Path)
    parser.add_argument("--output", type=Path, default=Path("pages.json"))
    parser.add_argument("--ocr", action="store_true", help="Tenta OCR em páginas sem texto útil")
    parser.add_argument("--ocr-language", default="por+eng")
    parser.add_argument("--ocr-dpi", type=int, default=200)
    args = parser.parse_args()
    pages, warnings, ocr_pages = extract_pages_with_ocr(args.file.resolve(), args.ocr, args.ocr_language, args.ocr_dpi)
    args.output.write_text(json.dumps({"pages": pages, "warnings": warnings, "ocr_pages": ocr_pages}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0 if pages or not warnings else 2


if __name__ == "__main__":
    raise SystemExit(main())
