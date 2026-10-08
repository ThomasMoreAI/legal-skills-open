from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Marca páginas sem texto nativo ou com texto suspeito.")
    parser.add_argument("pages_json", type=Path)
    args = parser.parse_args()
    data = json.loads(args.pages_json.read_text(encoding="utf-8"))
    result = {"scanned_or_problematic_pages": [i + 1 for i, text in enumerate(data.get("pages", [])) if len(text.strip()) < 30]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

