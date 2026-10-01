#!/usr/bin/env python3
"""render_legal_pdf.py — rende un deliverable markdown in un file .pdf con fpdf2.

La logica fpdf2 (sanitize per windows-1252, slug del nome file, scrittura del file
e ritorno del path) è COPIATA da src/tools/legal_citations.py (NON importata) per
mantenere lo skill autonomo dal server MCP. Niente LibreOffice (non installato).

Uso:
    python render_legal_pdf.py --input deliverable.md \
        [--title "Titolo"] [--slug nome-file] [--dir /cartella/attiva]

In alternativa il markdown arriva da stdin:
    cat deliverable.md | python render_legal_pdf.py --title "Parere"

Output: <dir>/<slug>.pdf — il path assoluto viene stampato su stdout.
"""

import argparse
import os
import re
import sys
import unicodedata

from fpdf import FPDF
from fpdf.enums import XPos, YPos


# ---------------------------------------------------------------------------
# Helpers copied from legal_citations.py (do NOT import that module)
# ---------------------------------------------------------------------------

def _sanitize_for_pdf(text: str) -> str:
    """Replace characters not in windows-1252 for fpdf2 built-in fonts."""
    replacements = {
        "–": "-",
        "—": "--",
        "‘": "'",
        "’": "'",
        "“": '"',
        "”": '"',
        "…": "...",
        " ": " ",
        "​": "",
        "•": "-",  # bullet glyph -> hyphen for built-in fonts
        "«": '"',  # «
        "»": '"',  # »
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.encode("windows-1252", errors="replace").decode("windows-1252")


def _safe_filename(name: str) -> str:
    """Convert a title to a safe filename (mirror of legal_citations._safe_filename)."""
    return re.sub(r"[^\w\-.]", "_", name.replace("/", "-").replace(" ", "_"))[:80]


def _slugify(value: str) -> str:
    """Lowercase, accent-stripped, hyphenated slug for the output file name."""
    base = unicodedata.normalize("NFKD", value or "documento")
    base = base.encode("ascii", "ignore").decode("ascii").lower()
    base = re.sub(r"[^a-z0-9]+", "-", base).strip("-")
    return (base or "documento")[:80]


# ---------------------------------------------------------------------------
# Minimal markdown stripping for inline emphasis / code
# ---------------------------------------------------------------------------

_INLINE_RE = re.compile(r"\*\*(.+?)\*\*|__(.+?)__|\*(.+?)\*|_(.+?)_|`([^`]+)`")


def _strip_inline(text: str) -> str:
    """Drop inline markdown markers, keep the content (PDF uses built-in fonts)."""

    def repl(m: "re.Match") -> str:
        return next(g for g in m.groups() if g is not None)

    return _INLINE_RE.sub(repl, text)


# ---------------------------------------------------------------------------
# PDF generation — fpdf2 "write file, return path" pattern from legal_citations
# ---------------------------------------------------------------------------

def _cell(pdf: FPDF, height: float, text: str) -> None:
    """multi_cell that always returns the cursor to the left margin on the next
    line. Without forcing XPos/YPos, fpdf2 may leave x at the right edge, so a
    subsequent multi_cell(w=0) computes a near-zero width and raises
    'Not enough horizontal space to render a single character'."""
    pdf.multi_cell(0, height, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


def _generate_pdf_from_markdown(title: str, markdown: str, output_path: str) -> None:
    """Render markdown to PDF with fpdf2, mapping a small block subset to styles."""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 14)
    _cell(pdf, 8, _sanitize_for_pdf(title))
    pdf.ln(4)

    lines = markdown.replace("\r\n", "\n").split("\n")
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        i += 1

        if line == "":
            pdf.ln(3)
            continue

        # Horizontal rule
        if re.match(r"^([-*_]\s*){3,}$", line):
            y = pdf.get_y()
            pdf.line(pdf.l_margin, y, pdf.w - pdf.r_margin, y)
            pdf.ln(3)
            continue

        # Headings
        h = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h:
            level = min(len(h.group(1)), 3)
            size = {1: 13, 2: 12, 3: 11}[level]
            pdf.ln(2)
            pdf.set_font("Helvetica", "B", size)
            _cell(pdf, 6, _sanitize_for_pdf(_strip_inline(h.group(2).strip())))
            pdf.ln(1)
            continue

        # Blockquote — indent via left/right margins so multi_cell wraps safely,
        # then always restore the original margins.
        if re.match(r"^>\s?", line):
            content = re.sub(r"^>\s?", "", line)
            pdf.set_font("Helvetica", "I", 10)
            orig_l, orig_r = pdf.l_margin, pdf.r_margin
            pdf.set_left_margin(orig_l + 8)
            pdf.set_right_margin(orig_r + 8)
            pdf.set_x(pdf.l_margin)
            _cell(pdf, 5, _sanitize_for_pdf(_strip_inline(content)))
            pdf.set_left_margin(orig_l)
            pdf.set_right_margin(orig_r)
            pdf.set_x(orig_l)
            continue

        # List items (unordered or ordered)
        ul = re.match(r"^[-*+]\s+(.*)$", line)
        ol = re.match(r"^(\d+)[.)]\s+(.*)$", line)
        if ul:
            pdf.set_font("Helvetica", "", 10)
            _cell(pdf, 5, _sanitize_for_pdf("- " + _strip_inline(ul.group(1))))
            continue
        if ol:
            pdf.set_font("Helvetica", "", 10)
            _cell(pdf, 5, _sanitize_for_pdf(f"{ol.group(1)}. " + _strip_inline(ol.group(2))))
            continue

        # Table row -> render as a single line with pipe separators preserved
        if "|" in line and not re.match(r"^\s*\|?\s*:?-{2,}", line):
            pdf.set_font("Helvetica", "", 9)
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            _cell(pdf, 5, _sanitize_for_pdf(_strip_inline("  |  ".join(cells))))
            continue
        # Skip table separator rows
        if re.match(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$", line):
            continue

        # Default: body paragraph
        pdf.set_font("Helvetica", "", 10)
        _cell(pdf, 5, _sanitize_for_pdf(_strip_inline(line)))

    pdf.output(output_path)


def _read_input(input_path: str | None) -> str:
    if input_path:
        with open(input_path, "r", encoding="utf-8") as fh:
            return fh.read()
    return sys.stdin.read()


def _derive_title(markdown: str) -> str:
    for raw in markdown.split("\n"):
        h = re.match(r"^#{1,6}\s+(.*)$", raw.strip())
        if h:
            return h.group(1).strip()
    return "Documento"


def main() -> int:
    parser = argparse.ArgumentParser(description="Render markdown to PDF (fpdf2).")
    parser.add_argument("--input", "-i", default=None, help="Markdown file (stdin if omitted)")
    parser.add_argument("--title", "-t", default=None, help="Document title")
    parser.add_argument("--slug", "-s", default=None, help="Output file slug")
    parser.add_argument("--dir", "-d", default=None, help="Active folder (cwd if omitted)")
    args = parser.parse_args()

    markdown = _read_input(args.input)
    if not markdown or not markdown.strip():
        print("FAIL: nessun contenuto markdown fornito (usa --input o stdin).", file=sys.stderr)
        return 1

    title = args.title or _derive_title(markdown)
    slug = _slugify(args.slug or title)
    out_dir = os.path.abspath(args.dir) if args.dir else os.getcwd()
    os.makedirs(out_dir, exist_ok=True)
    output_path = os.path.join(out_dir, f"{slug}.pdf")

    _generate_pdf_from_markdown(_strip_inline(title), markdown, output_path)

    # Echo the absolute path so the skill can report it.
    print(output_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
