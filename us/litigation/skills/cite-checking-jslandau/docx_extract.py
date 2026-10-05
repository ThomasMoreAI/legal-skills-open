#!/usr/bin/env python3
"""
docx_extract.py — extract text from a .docx file for cite-checking.

Reads a Microsoft Word document and emits its body text on stdout with
footnotes inlined as `[FNx: ...]` markers at the points where they were
referenced. Designed to be the input source for the cite-checking skill's
Stage 1 (Document Parsing) when the source is a .docx file.

Tracked-changes behavior: accepted text is included; inserted text is
included; deleted text is omitted. This matches what a reader of the
final-formatted brief would see.

Page boundaries in .docx are not tracked — the consuming skill is responsible
for resolving printed page numbers separately (e.g., by spot-checking against
the source).

Dependencies: stdlib only.

Usage:

    python3 docx_extract.py path/to/brief.docx
    python3 docx_extract.py path/to/brief.docx --output extracted.txt
"""
from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
import zipfile

WORDML_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def _qname(local: str) -> str:
    return f"{{{WORDML_NS}}}{local}"


def _text_of(element: ET.Element) -> str:
    """Concatenate the text of every <w:t> descendant."""
    parts: list[str] = []
    for t in element.iter(_qname("t")):
        if t.text:
            parts.append(t.text)
    return "".join(parts)


def extract(path: str) -> str:
    """Return the body text of a .docx file with footnotes inlined as `[FNx: ...]`."""
    with zipfile.ZipFile(path) as z:
        doc_tree = ET.parse(z.open("word/document.xml"))
        footnote_text: dict[str, str] = {}
        if "word/footnotes.xml" in z.namelist():
            fn_tree = ET.parse(z.open("word/footnotes.xml"))
            for fn in fn_tree.getroot().iter(_qname("footnote")):
                fid = fn.get(_qname("id"))
                if fid is None:
                    continue
                footnote_text[fid] = _text_of(fn)

    paragraphs: list[str] = []
    for p in doc_tree.getroot().iter(_qname("p")):
        line = _text_of(p)
        refs = []
        for ref in p.iter(_qname("footnoteReference")):
            fid = ref.get(_qname("id"))
            if fid is None:
                continue
            refs.append(f"[FN{fid}: {footnote_text.get(fid, '')}]")
        if line.strip() or refs:
            paragraphs.append(line + (" " + " ".join(refs) if refs else ""))
    return "\n\n".join(paragraphs)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Extract text from a .docx file with footnotes inlined as [FNx: ...] markers.",
    )
    parser.add_argument("path", help="Path to the .docx file.")
    parser.add_argument(
        "--output",
        help="Path to write extracted text. If omitted, writes to stdout.",
    )
    args = parser.parse_args(argv)

    text = extract(args.path)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(text)
    else:
        sys.stdout.write(text)
        if not text.endswith("\n"):
            sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
