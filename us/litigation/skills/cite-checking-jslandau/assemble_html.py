#!/usr/bin/env python3
"""
assemble_html.py — assemble the interactive cite-check HTML report.

Reads `explorer-template.html` (the canonical, dependency-free explorer UI,
shipped alongside this script) and inlines a JSON payload into its
`<script type="application/json" id="cite-check-data">` block. Writes the
combined result as a single self-contained HTML file the user opens in a
browser.

Used by the cite-checking skill's Stage 8 (Report Generation), invoked once
per run as a subprocess.

Dependencies: stdlib only.

Usage:

    python3 assemble_html.py \\
        --json  brief-cite-check.json \\
        --out   brief-cite-check.html

The template path defaults to `explorer-template.html` in the same directory
as this script; override with `--template` if needed.
"""
from __future__ import annotations

import argparse
import os
import pathlib
import re
import sys


_PLACEHOLDER_RE = re.compile(
    r'(<script type="application/json" id="cite-check-data">)[^<]*(</script>)',
    re.DOTALL,
)


def assemble(template_path: pathlib.Path, json_path: pathlib.Path, out_path: pathlib.Path) -> None:
    template = template_path.read_text(encoding="utf-8")
    data = json_path.read_text(encoding="utf-8").rstrip()
    new_html, n = _PLACEHOLDER_RE.subn(
        lambda m: m.group(1) + "\n" + data + "\n" + m.group(2),
        template,
        count=1,
    )
    if n != 1:
        raise SystemExit(
            f"ERROR: explorer template at {template_path} is missing the "
            '`<script type="application/json" id="cite-check-data">` block.'
        )
    out_path.write_text(new_html, encoding="utf-8")


def main(argv: list[str]) -> int:
    here = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
    parser = argparse.ArgumentParser(
        description="Inline a cite-check JSON payload into the explorer HTML template.",
    )
    parser.add_argument("--json", required=True, help="Path to the cite-check JSON file.")
    parser.add_argument("--out", required=True, help="Path to write the assembled HTML.")
    parser.add_argument(
        "--template",
        default=str(here / "explorer-template.html"),
        help="Path to explorer-template.html (default: alongside this script).",
    )
    args = parser.parse_args(argv)

    assemble(
        template_path=pathlib.Path(args.template),
        json_path=pathlib.Path(args.json),
        out_path=pathlib.Path(args.out),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
