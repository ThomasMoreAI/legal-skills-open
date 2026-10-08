#!/usr/bin/env python3
"""
cendoj_download.py — Download PDFs from a CENDOJ search inventory.

Reads the JSON inventory produced by cendoj_search.py and downloads each PDF
from the public CENDOJ endpoint, respecting Crawl-delay: 5s as a hard minimum.
Validates each downloaded file is a valid PDF, computes SHA-256, generates an
INVENTARIO.md summary table.

CENDOJ legal notice (uso particular only) is enforced — see SKILL.md.

Usage:
    python cendoj_download.py --input results.json --output-dir ./pdfs/
    python cendoj_download.py --input results.json --output-dir ./pdfs/ --max-downloads 30
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime
from pathlib import Path

# Ensure the script can import its sibling `cendoj_lib` whether launched
# directly or via `python -m`.
_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

from cendoj_lib import (  # type: ignore[import-not-found]  # noqa: E402
    BROWSER_UA,
    COOPERATIVE_UA,
    DEFAULT_MAX_DOWNLOADS,
    HARD_CAP_MAX_DOWNLOADS,
    LEGAL_NOTICE,
    MIN_DELAY_SECONDS,
    is_pdf,
    safe_filename,
    sha256_file,
)


def print_legal_notice() -> None:
    print(LEGAL_NOTICE, file=sys.stderr)


def download_pdf(
    url: str,
    out_path: Path,
    user_agent: str,
    timeout: int = 60,
) -> tuple[bool, str | None]:
    """Download a PDF. Returns (success, error_message)."""
    import requests  # type: ignore[import-not-found]

    headers = {
        "User-Agent": user_agent,
        "Accept": "application/pdf,*/*",
        "Referer": "https://www.poderjudicial.es/search/indexAN.jsp",
    }
    try:
        r = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
        r.raise_for_status()
        out_path.write_bytes(r.content)
    except Exception as e:
        return False, str(e)

    if not is_pdf(out_path):
        return False, "downloaded file is not a valid PDF"

    return True, None


def generate_inventory_md(
    entries: list[dict],
    output_dir: Path,
    query: str,
    started_at: str,
) -> Path:
    """Generate INVENTARIO.md summary table for the downloaded set."""
    md_lines = [
        "---",
        f'title: "Inventario CENDOJ - búsqueda {query!r}"',
        f'date: "{datetime.now().strftime("%Y-%m-%d")}"',
        f'query: "{query}"',
        f'downloaded_at: "{started_at}"',
        'lang: "es"',
        'version: "0.1.0"',
        "---",
        "",
        f"# Inventario CENDOJ — búsqueda libre {query!r}",
        "",
        f"Total entradas descargadas: {sum(1 for e in entries if e.get('downloaded'))}",
        f"Total entradas en inventario: {len(entries)}",
        "",
        "## Tabla resumen",
        "",
        "| # | ROJ | Tribunal | Fecha | Ponente | Recurso | Resumen | SHA-256 PDF | Archivo |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for i, e in enumerate(entries, 1):
        if not e.get("downloaded"):
            continue
        sha = e.get("sha256", "")
        sha_short = f"`{sha[:16]}...`" if sha else ""
        summary = (e.get("summary") or "").replace("|", "\\|")[:80]
        ponente = (e.get("ponente") or "").replace("|", "\\|")[:40]
        md_lines.append(
            f"| {i} | {e.get('roj','')} | {e.get('tribunal','')} | "
            f"{e.get('date_iso','')} | {ponente} | {e.get('appeal_number','')} | "
            f"{summary} | {sha_short} | `{e.get('filename','')}` |"
        )

    md_lines += ["", "---", "", "## Detalle por pieza", ""]

    for i, e in enumerate(entries, 1):
        md_lines.append(f"### {i}. {e.get('title','')}")
        md_lines.append("")
        md_lines.append(f"- **ECLI**: `{e.get('ecli','')}`")
        md_lines.append(f"- **ROJ**: {e.get('roj','')}")
        md_lines.append(f"- **Tribunal**: {e.get('tribunal','')}")
        md_lines.append(f"- **Fecha resolución**: {e.get('date_iso','')}")
        md_lines.append(f"- **Municipio**: {e.get('city','')}")
        md_lines.append(f"- **Ponente**: {e.get('ponente','')}")
        md_lines.append(f"- **Nº Resolución**: {e.get('resolution_number','')}")
        md_lines.append(f"- **Nº Recurso**: {e.get('appeal_number','')}")
        md_lines.append(f"- **Resumen**: {e.get('summary','')}")
        if e.get("downloaded"):
            md_lines.append(f"- **Archivo**: `{e.get('filename','')}`")
            md_lines.append(f"- **SHA-256**: `{e.get('sha256','')}`")
            md_lines.append(f"- **Bytes**: {e.get('size_bytes','')}")
        else:
            md_lines.append(
                f"- **Estado**: ⚠️ no descargado ({e.get('download_error','reason unknown')})"
            )
        md_lines.append(f"- **URL PDF**: {e.get('pdf_url','')}")
        md_lines.append(f"- **URL openDocument**: {e.get('open_document_url','')}")
        md_lines.append("")

    md_lines += [
        "---",
        "",
        "*Generado por cendoj-toolkit. Material para uso particular.*",
        "",
    ]

    out_path = output_dir / "INVENTARIO.md"
    out_path.write_text("\n".join(md_lines), encoding="utf-8")
    return out_path


def main() -> int:
    print_legal_notice()

    parser = argparse.ArgumentParser(
        description="Download CENDOJ PDFs from a search inventory JSON.",
    )
    parser.add_argument("--input", required=True, help="Input JSON (from cendoj_search.py)")
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Output directory for PDFs + INVENTARIO.md",
    )
    parser.add_argument(
        "--max-downloads",
        type=int,
        default=DEFAULT_MAX_DOWNLOADS,
        help=(
            f"Maximum PDFs to download in this execution "
            f"(default {DEFAULT_MAX_DOWNLOADS}, hard cap {HARD_CAP_MAX_DOWNLOADS})"
        ),
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=MIN_DELAY_SECONDS,
        help=f"Seconds between downloads (min {MIN_DELAY_SECONDS}, default {MIN_DELAY_SECONDS})",
    )
    parser.add_argument(
        "--user-agent",
        choices=["browser", "cooperative"],
        default="browser",
        help=(
            "Which User-Agent to send. 'browser' (Mozilla/Chrome) works around CENDOJ "
            "filtering of generic UA. 'cooperative' identifies as cendoj-toolkit "
            "(may be rejected). Default: browser."
        ),
    )
    parser.add_argument(
        "--force-large",
        action="store_true",
        help=f"Allow exceeding default --max-downloads up to {HARD_CAP_MAX_DOWNLOADS}",
    )
    parser.add_argument(
        "--query",
        default="(query)",
        help="Original search query (for INVENTARIO.md metadata)",
    )
    args = parser.parse_args()

    if args.delay < MIN_DELAY_SECONDS:
        print(
            f"ERROR: --delay cannot be less than {MIN_DELAY_SECONDS} seconds "
            f"(CENDOJ robots.txt Crawl-delay).",
            file=sys.stderr,
        )
        return 2

    if args.max_downloads > HARD_CAP_MAX_DOWNLOADS:
        print(
            f"ERROR: --max-downloads cannot exceed hard cap {HARD_CAP_MAX_DOWNLOADS}. "
            f"For larger downloads, request formal authorization from CGPJ.",
            file=sys.stderr,
        )
        return 2

    if args.max_downloads > DEFAULT_MAX_DOWNLOADS and not args.force_large:
        print(
            f"ERROR: --max-downloads {args.max_downloads} exceeds default cap "
            f"{DEFAULT_MAX_DOWNLOADS}. Add --force-large to confirm (still subject "
            f"to hard cap {HARD_CAP_MAX_DOWNLOADS}).",
            file=sys.stderr,
        )
        return 2

    user_agent = BROWSER_UA if args.user_agent == "browser" else COOPERATIVE_UA

    inp = Path(args.input)
    if not inp.exists():
        print(f"ERROR: input file not found: {inp}", file=sys.stderr)
        return 1

    entries = json.loads(inp.read_text(encoding="utf-8"))
    if not isinstance(entries, list):
        print("ERROR: input JSON must be a list of search results", file=sys.stderr)
        return 1

    if len(entries) > args.max_downloads:
        print(
            f"WARNING: inventory has {len(entries)} entries, "
            f"will download first {args.max_downloads}",
            file=sys.stderr,
        )

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    started_at = datetime.now().isoformat(timespec="seconds")
    print(
        f"[{started_at}] Downloading up to {args.max_downloads} PDFs to {output_dir} "
        f"(delay {args.delay}s, UA={args.user_agent})",
        file=sys.stderr,
    )

    ok = 0
    fail = 0
    skipped = 0
    to_download = entries[: args.max_downloads]

    for i, entry in enumerate(to_download, 1):
        pdf_url = entry.get("pdf_url")
        if not pdf_url:
            print(f"[{i}/{len(to_download)}] SKIP: missing pdf_url", file=sys.stderr)
            fail += 1
            entry["downloaded"] = False
            entry["download_error"] = "missing pdf_url"
            continue

        filename = safe_filename(entry, i)
        entry["filename"] = filename
        out_path = output_dir / filename

        if out_path.exists() and is_pdf(out_path):
            sha = sha256_file(out_path)
            size = out_path.stat().st_size
            entry["downloaded"] = True
            entry["sha256"] = sha
            entry["size_bytes"] = size
            print(f"[{i}/{len(to_download)}] SKIP (exists): {filename}", file=sys.stderr)
            skipped += 1
            continue

        print(
            f"[{i}/{len(to_download)}] [{datetime.now().isoformat(timespec='seconds')}] "
            f"Downloading {filename}",
            file=sys.stderr,
        )
        success, err = download_pdf(pdf_url, out_path, user_agent=user_agent)
        if success:
            sha = sha256_file(out_path)
            size = out_path.stat().st_size
            entry["downloaded"] = True
            entry["sha256"] = sha
            entry["size_bytes"] = size
            print(f"  OK: {size} bytes, SHA-256 {sha[:16]}...", file=sys.stderr)
            ok += 1
        else:
            entry["downloaded"] = False
            entry["download_error"] = err
            print(f"  FAIL: {err}", file=sys.stderr)
            fail += 1

        # Respect crawl-delay between downloads
        if i < len(to_download):
            time.sleep(args.delay)

    inv_path = generate_inventory_md(
        to_download,
        output_dir,
        query=args.query,
        started_at=started_at,
    )

    finished_at = datetime.now().isoformat(timespec="seconds")
    print("=" * 60, file=sys.stderr)
    print(f"[{finished_at}] Summary:", file=sys.stderr)
    print(f"  Downloaded: {ok}", file=sys.stderr)
    print(f"  Skipped (already exist): {skipped}", file=sys.stderr)
    print(f"  Failed: {fail}", file=sys.stderr)
    print(f"  Total processed: {ok + skipped + fail} / {len(to_download)}", file=sys.stderr)
    print(f"  Output dir: {output_dir}", file=sys.stderr)
    print(f"  Inventory: {inv_path}", file=sys.stderr)
    print("=" * 60, file=sys.stderr)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
