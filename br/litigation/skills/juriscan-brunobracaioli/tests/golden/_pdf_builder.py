"""Deterministic stdlib-only PDF builder for golden fixtures.

Emits a minimal PDF 1.4 file from plain text. Helvetica + WinAnsiEncoding —
covers all Portuguese accents we need for synthetic legal filings.

Usage:
    from _pdf_builder import build_pdf
    build_pdf(text, output_path)

Or as CLI:
    python tests/golden/_pdf_builder.py source.txt output.pdf
"""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path


PAGE_WIDTH = 612   # Letter size in points
PAGE_HEIGHT = 792
MARGIN_X = 50
MARGIN_TOP = 750
FONT_SIZE = 10
LINE_HEIGHT = 12
LINES_PER_PAGE = 60
CHARS_PER_LINE = 90


def _escape_pdf_string(s: str) -> bytes:
    """Escape a string for inclusion in a PDF (...) literal and encode to Latin-1.

    WinAnsiEncoding covers Latin-1 range, so Portuguese accents survive.
    Characters outside Latin-1 are replaced with '?'.
    """
    # Escape backslash, parens
    s = s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    return s.encode("latin-1", errors="replace")


def _wrap_text(text: str) -> list[str]:
    """Wrap text to CHARS_PER_LINE, preserving blank lines."""
    out: list[str] = []
    for raw_line in text.splitlines():
        if not raw_line.strip():
            out.append("")
            continue
        wrapped = textwrap.wrap(
            raw_line,
            width=CHARS_PER_LINE,
            break_long_words=True,
            break_on_hyphens=False,
        ) or [""]
        out.extend(wrapped)
    return out


def _paginate(lines: list[str]) -> list[list[str]]:
    """Split wrapped lines into pages.

    A literal form-feed (\\f) character forces a page break.
    """
    pages: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if line == "\f":
            if current:
                pages.append(current)
                current = []
            continue
        if len(current) >= LINES_PER_PAGE:
            pages.append(current)
            current = []
        current.append(line)
    if current:
        pages.append(current)
    if not pages:
        pages = [[""]]
    return pages


def _build_content_stream(page_lines: list[str]) -> bytes:
    """Emit a PDF content stream that draws the lines of one page."""
    out = bytearray()
    out += b"BT\n"
    out += f"/F1 {FONT_SIZE} Tf\n".encode("ascii")
    out += f"{LINE_HEIGHT} TL\n".encode("ascii")
    out += f"{MARGIN_X} {MARGIN_TOP} Td\n".encode("ascii")
    for line in page_lines:
        out += b"("
        out += _escape_pdf_string(line)
        out += b") Tj T*\n"
    out += b"ET\n"
    return bytes(out)


def build_pdf(text: str, output: Path | str) -> Path:
    """Build a multi-page PDF from the given text and write to `output`.

    Returns the output path.
    """
    # Pre-process text: respect explicit \f as page break marker
    raw_lines: list[str] = []
    for raw in text.splitlines():
        if raw.strip() == "\f" or raw == "\x0c":
            raw_lines.append("\f")
        else:
            raw_lines.append(raw)
    wrapped = _wrap_text("\n".join(raw_lines).replace("\n\f\n", "\n\f\n"))
    # After wrapping, form-feed lines may have been stripped; re-insert markers
    final_lines: list[str] = []
    for line in wrapped:
        final_lines.append(line)
    pages = _paginate(final_lines)

    # Object numbering:
    #   1 = Catalog
    #   2 = Pages
    #   3 = Font
    #   4..(4+N-1) = Page objects
    #   (4+N)..(4+2N-1) = Content streams
    num_pages = len(pages)
    page_obj_ids = list(range(4, 4 + num_pages))
    content_obj_ids = list(range(4 + num_pages, 4 + 2 * num_pages))

    body = bytearray()
    offsets: list[int] = []

    header = b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    body += header

    def write_obj(obj_id: int, contents: bytes) -> None:
        offsets.append(len(body))
        body.extend(f"{obj_id} 0 obj\n".encode("ascii"))
        body.extend(contents)
        if not contents.endswith(b"\n"):
            body.extend(b"\n")
        body.extend(b"endobj\n")

    # 1: Catalog
    write_obj(1, b"<< /Type /Catalog /Pages 2 0 R >>\n")

    # 2: Pages
    kids = " ".join(f"{pid} 0 R" for pid in page_obj_ids)
    pages_obj = f"<< /Type /Pages /Kids [{kids}] /Count {num_pages} >>\n".encode("ascii")
    write_obj(2, pages_obj)

    # 3: Font
    font_obj = b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>\n"
    write_obj(3, font_obj)

    # 4..: Page objects
    for page_idx, page_obj_id in enumerate(page_obj_ids):
        content_id = content_obj_ids[page_idx]
        page_dict = (
            f"<< /Type /Page /Parent 2 0 R "
            f"/MediaBox [0 0 {PAGE_WIDTH} {PAGE_HEIGHT}] "
            f"/Resources << /Font << /F1 3 0 R >> >> "
            f"/Contents {content_id} 0 R >>\n"
        ).encode("ascii")
        write_obj(page_obj_id, page_dict)

    # Content streams
    for page_idx, content_id in enumerate(content_obj_ids):
        stream_bytes = _build_content_stream(pages[page_idx])
        stream_obj = bytearray()
        stream_obj += f"<< /Length {len(stream_bytes)} >>\n".encode("ascii")
        stream_obj += b"stream\n"
        stream_obj += stream_bytes
        stream_obj += b"endstream\n"
        write_obj(content_id, bytes(stream_obj))

    # Xref
    xref_offset = len(body)
    total_objs = 3 + 2 * num_pages  # 1,2,3 + pages + contents
    body += f"xref\n0 {total_objs + 1}\n".encode("ascii")
    body += b"0000000000 65535 f \n"
    for off in offsets:
        body += f"{off:010d} 00000 n \n".encode("ascii")

    # Trailer
    body += f"trailer\n<< /Size {total_objs + 1} /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n".encode("ascii")

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(bytes(body))
    return output_path


def main() -> int:
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} source.txt output.pdf", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    text = src.read_text(encoding="utf-8")
    out = build_pdf(text, dst)
    print(f"wrote {out} ({out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
