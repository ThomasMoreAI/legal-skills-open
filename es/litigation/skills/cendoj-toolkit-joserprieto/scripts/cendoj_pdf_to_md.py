#!/usr/bin/env python3
"""
cendoj_pdf_to_md.py — Convert downloaded CENDOJ PDFs to markdown.

Thin CLI orchestrator. All provider-specific logic lives behind the
`converters/` package (Strategy pattern + `ConversionResult` ACL).

Usage:
    # Use docling (structure-preserving, recommended for court decisions)
    python cendoj_pdf_to_md.py --input-dir ./pdfs/ --output-dir ./markdown/ --engine docling

    # Use pdfminer.six (text-only, fast)
    python cendoj_pdf_to_md.py --input-dir ./pdfs/ --output-dir ./markdown/ --engine pdfminer

    # List available engines (i.e. installed)
    python cendoj_pdf_to_md.py --list-engines
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import datetime
from pathlib import Path

# Ensure the script can import its sibling `converters/` package whether it is
# launched directly or via `python -m`.
_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

from converters import (  # type: ignore[import-not-found]  # noqa: E402
    ConverterUnavailableError,
    available_converters,
    get_converter,
    list_converters,
)
from converters.base import ConversionResult  # type: ignore[import-not-found]  # noqa: E402


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def make_md_doc(
    pdf_path: Path,
    result: ConversionResult,
    pdf_sha256: str,
) -> str:
    """Wrap the converter's normalized output in a markdown document with frontmatter."""
    pdf_name = pdf_path.name
    pdf_size = pdf_path.stat().st_size
    now_iso = datetime.now().isoformat(timespec="seconds")
    title = pdf_path.stem.replace("-", " ")

    front = [
        "---",
        f'title: "{title}"',
        f'source-pdf: "{pdf_name}"',
        f'source-sha256: "{pdf_sha256}"',
        f"source-bytes: {pdf_size}",
        f'engine: "{result.engine_name}"',
        f'engine-version: "{result.engine_version}"',
        f"page-count: {result.page_count if result.page_count is not None else 'null'}",
        f"has-tables: {str(result.has_tables).lower()}",
        f"has-images: {str(result.has_images).lower()}",
        f'converted-at: "{now_iso}"',
        'lang: "es"',
        "---",
        "",
    ]

    header = [
        f"# {title}",
        "",
        "## Cabecera",
        "",
        f"- **PDF original**: `{pdf_name}`",
        f"- **SHA-256**: `{pdf_sha256}`",
        f"- **Bytes**: {pdf_size:,}",
        f"- **Motor de conversión**: {result.engine_name} v{result.engine_version}",
        f"- **Páginas**: {result.page_count if result.page_count is not None else 'n/a'}",
        f"- **Tablas detectadas**: {'sí' if result.has_tables else 'no'}",
        f"- **Imágenes detectadas**: {'sí' if result.has_images else 'no'}",
        f"- **Fecha de conversión**: {now_iso}",
        "",
    ]

    if result.warnings:
        header += ["## Advertencias del motor", ""]
        header += [f"- {w}" for w in result.warnings]
        header += [""]

    body = [
        "## Contenido",
        "",
        result.markdown,
        "",
        "---",
        "",
        f"*Convertido por cendoj-toolkit ({result.engine_name} v{result.engine_version}). "
        f"NORMA 9.bis: el PDF original permanece en filesystem; este `.md` derivado puede commitearse.*",
        "",
    ]

    return "\n".join(front + header + body)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Convert directory of CENDOJ PDFs to markdown using the Strategy "
            "pattern + ConversionResult ACL. Provider-specific deps loaded lazily."
        ),
    )
    parser.add_argument(
        "--input-dir",
        help="Directory containing PDF files",
    )
    parser.add_argument(
        "--output-dir",
        help="Output directory for .md files",
    )
    parser.add_argument(
        "--engine",
        choices=sorted(list_converters().keys()),
        default="docling",
        help=(
            "Conversion engine. 'docling' preserves structure (recommended for "
            "court decisions). 'pdfminer' is fast plain-text only. Default: docling."
        ),
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing .md files",
    )
    parser.add_argument(
        "--list-engines",
        action="store_true",
        help="List registered engines and exit (✓ marks engines with deps installed)",
    )
    args = parser.parse_args()

    if args.list_engines:
        registry = list_converters()
        available = set(available_converters())
        print("Available conversion engines:")
        for name, cls in sorted(registry.items()):
            mark = "✓" if name in available else "✗"
            print(f"  {mark} {name:12s} — {cls.description}")
        print()
        print("Engines marked ✗ are registered but their dependencies are not installed.")
        print("See SKILL.md prerequisites for installation steps.")
        return 0

    if not args.input_dir or not args.output_dir:
        parser.error("--input-dir and --output-dir are required (or use --list-engines).")

    in_dir = Path(args.input_dir)
    out_dir = Path(args.output_dir)
    if not in_dir.exists():
        print(f"ERROR: input directory not found: {in_dir}", file=sys.stderr)
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(p for p in in_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"ERROR: no PDF files found in {in_dir}", file=sys.stderr)
        return 1

    try:
        converter = get_converter(args.engine)
    except ConverterUnavailableError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        if args.engine == "docling":
            print("  Install with: pip install docling", file=sys.stderr)
        elif args.engine == "pdfminer":
            print("  Install with: pip install pdfminer.six", file=sys.stderr)
        return 2
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    print(
        f"[{datetime.now().isoformat(timespec='seconds')}] "
        f"Converting {len(pdf_files)} PDFs with engine={args.engine}",
        file=sys.stderr,
    )

    ok = 0
    skipped = 0
    fail = 0
    for i, pdf_path in enumerate(pdf_files, 1):
        md_path = out_dir / (pdf_path.stem + ".md")
        if md_path.exists() and not args.overwrite:
            print(f"[{i}/{len(pdf_files)}] SKIP (exists): {md_path.name}", file=sys.stderr)
            skipped += 1
            continue

        print(
            f"[{i}/{len(pdf_files)}] [{datetime.now().isoformat(timespec='seconds')}] "
            f"Converting {pdf_path.name}",
            file=sys.stderr,
        )
        try:
            result = converter.convert(pdf_path)
        except Exception as e:
            print(f"  FAIL: {type(e).__name__}: {e}", file=sys.stderr)
            fail += 1
            continue

        sha = sha256_file(pdf_path)
        md_doc = make_md_doc(pdf_path, result, sha)
        md_path.write_text(md_doc, encoding="utf-8")
        print(
            f"  OK: {md_path.name} ({len(result.markdown):,} chars, "
            f"pages={result.page_count}, tables={result.has_tables}, images={result.has_images})",
            file=sys.stderr,
        )
        ok += 1

    print("=" * 60, file=sys.stderr)
    print(
        f"Summary (engine={args.engine}): OK {ok} / SKIP {skipped} / FAIL {fail} / total {len(pdf_files)}",
        file=sys.stderr,
    )
    print("=" * 60, file=sys.stderr)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
