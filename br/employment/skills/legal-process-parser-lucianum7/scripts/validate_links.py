"""Validate local Markdown/assets links in a generated process bundle."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")


def validate_links(root: Path) -> list[str]:
    errors: list[str] = []
    for markdown_path in sorted(root.rglob("*.md")):
        if "versions" in markdown_path.relative_to(root).parts:
            continue
        try:
            text = markdown_path.read_text(encoding="utf-8-sig")
        except OSError as exc:
            errors.append(f"{markdown_path.relative_to(root)}: leitura falhou ({exc})")
            continue
        for target in LINK_RE.findall(text):
            target = target.strip().split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "data:", "#")):
                continue
            candidate = (markdown_path.parent / target.replace("\\", "/")).resolve()
            try:
                candidate.relative_to(root.resolve())
            except ValueError:
                errors.append(f"{markdown_path.relative_to(root)}: link fora do pacote: {target}")
                continue
            if not candidate.exists():
                errors.append(f"{markdown_path.relative_to(root)}: asset ausente: {target}")

    image_index_path = root / "images" / "index.json"
    if image_index_path.is_file():
        try:
            index = json.loads(image_index_path.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"images/index.json inválido: {exc}")
        else:
            for item in index.get("unique_images", []):
                for field in ("relative_path", "zoom_relative_path"):
                    relative = item.get(field)
                    if not relative:
                        continue
                    candidate = (root / str(relative)).resolve()
                    try:
                        candidate.relative_to(root.resolve())
                    except ValueError:
                        errors.append(f"images/index.json: caminho fora do pacote: {relative}")
                        continue
                    if not candidate.exists():
                        errors.append(f"images/index.json: asset ausente: {relative}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida links Markdown e assets locais do pacote processual.")
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    errors = validate_links(args.root.resolve())
    if errors:
        print("\n".join(f"ERRO: {error}" for error in errors))
        return 1
    print("OK: links Markdown e assets locais válidos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
