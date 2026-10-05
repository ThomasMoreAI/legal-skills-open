#!/usr/bin/env python3
"""build_manifest.py - Stage 1 walk: inventory a data-room folder into manifest.json.

Hashes every file (sha256 -> stable doc ID), probes PDFs for page count and
per-page text-extraction yield, classifies readability (native / scanned /
encrypted / corrupt), and fails loudly if the counts do not reconcile with
the walk. Poppler's pdfinfo/pdftotext are used when installed; without them
pages is null and a stdlib content-stream scan supplies the yield.
Output is deterministic: sorted keys, documents sorted by id, no timestamps,
no absolute paths.

Usage:
    python3 build_manifest.py --root <data-room-dir> --out manifest.json
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zlib
from typing import Any

from document_text import docx_text, xlsx_text

HAVE_PDFINFO = shutil.which("pdfinfo") is not None
HAVE_PDFTOTEXT = shutil.which("pdftotext") is not None

# A page "yields" if its extracted text contains any alphanumeric character;
# scanned pages extract as empty or whitespace-only.
ALNUM = re.compile(rb"[A-Za-z0-9]")
TEXT_PROBE_BYTES = 65536


def structural_truncation_reason(head, tail=None):
    """Return a strong markup-truncation receipt, else None.

    SEC exhibits commonly use SGML wrappers even with a .txt suffix. Missing
    closing wrappers and EOF inside a tag are objective completeness failures;
    ordinary unmarked plain text is not guessed incomplete. Large files are
    checked with separate head and tail samples so a close marker beyond the
    first probe window is not mistaken for a missing marker.
    """
    tail = head if tail is None else tail
    for tag in ("document", "html", "body"):
        if re.search(rf"<{tag}\b", head, re.I) and not (
            re.search(rf"</{tag}\s*>", head, re.I)
            or re.search(rf"</{tag}\s*>", tail, re.I)
        ):
            return f"missing </{tag.upper()}> close marker"
    if re.search(r"<[^>]*\Z", tail.rstrip(), re.S):
        return "EOF inside markup tag"
    return None


def sha256_id(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()[:12]


def probe_pdf_info(path):
    """Return pdfinfo's structural result without requiring pdftotext."""
    info = subprocess.run(
        ["pdfinfo", path], capture_output=True, text=True, errors="replace"
    )
    if info.returncode != 0:
        return None, "corrupt", 0.0, "unparseable by pdfinfo"
    fields = {}
    for line in info.stdout.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip()
    if fields.get("Encrypted", "").lower().startswith("yes"):
        pages = int(fields["Pages"]) if fields.get("Pages", "").isdigit() else None
        return pages, "encrypted", 0.0, None
    if not fields.get("Pages", "").isdigit():
        return None, "corrupt", 0.0, "no page count"
    pages = int(fields["Pages"])
    if pages == 0:
        return 0, "corrupt", 0.0, "zero pages"
    return pages, None, 0.0, None


def probe_pdf_poppler(path):
    """(pages, readability, yield, note) via pdfinfo + per-page pdftotext.
    note is a short failure reason for corrupt files, None otherwise."""
    pages, readability, _yield, note = probe_pdf_info(path)
    if readability is not None:
        return pages, readability, 0.0, note
    yielding = 0
    for p in range(1, pages + 1):
        r = subprocess.run(
            ["pdftotext", "-q", "-f", str(p), "-l", str(p), path, "-"],
            capture_output=True,
        )
        if r.returncode == 0 and ALNUM.search(r.stdout):
            yielding += 1
    y = yielding / pages
    return pages, ("native" if y >= 0.5 else "scanned"), y, None


def probe_pdf_hybrid(path):
    """Use pdfinfo for structure/pages and stdlib only for text yield.

    Modern PDFs may store page objects in compressed object streams that the
    deliberately small stdlib scanner cannot enumerate. A successful pdfinfo
    receipt therefore controls structural validity; stdlib failure merely
    routes the document to the image-reading lane.
    """
    pages, readability, _yield, note = probe_pdf_info(path)
    if readability is not None:
        return pages, readability, 0.0, note
    _stdlib_pages, stdlib_readability, text_yield, _stdlib_note = probe_pdf_stdlib(path)
    if stdlib_readability == "native":
        return pages, "native", text_yield, None
    return pages, "scanned", 0.0, None


def _pdf_objects(data):
    return {
        int(m.group(1)): m.group(2)
        for m in re.finditer(rb"(?m)^(\d+)\s+\d+\s+obj\b(.*?)endobj", data, re.S)
    }


def _stream_bytes(body):
    m = re.search(rb"stream\r?\n(.*?)endstream", body, re.S)
    if not m:
        return b""
    raw = m.group(1)
    if b"/FlateDecode" in body:
        try:
            raw = zlib.decompress(raw.rstrip(b"\r\n"))
        except zlib.error:
            return b""
    return raw


def probe_pdf_stdlib(path):
    """Degraded probe when poppler is absent: raw/Flate content-stream scan.
    Pages stays null (pdfinfo is the page-count authority per the design)."""
    with open(path, "rb") as f:
        data = f.read()
    if not data.startswith(b"%PDF-"):
        return None, "corrupt", 0.0, "not a PDF"
    if b"%%EOF" not in data[-1024:]:
        return None, "corrupt", 0.0, "truncated stream"
    if b"/Encrypt" in data:
        return None, "encrypted", 0.0, None
    objs = _pdf_objects(data)
    page_bodies = [b for b in objs.values() if re.search(rb"/Type\s*/Page[^s]", b)]
    if not page_bodies:
        return None, "corrupt", 0.0, "no page objects"
    yielding = 0
    for body in page_bodies:
        m = re.search(rb"/Contents\s+(\d+)\s+\d+\s+R", body)
        content = _stream_bytes(objs.get(int(m.group(1)), b"")) if m else b""
        shown = b""
        if b"Tj" in content or b"TJ" in content:
            shown = b"".join(re.findall(rb"\((?:[^()\\]|\\.)*\)", content))
        if ALNUM.search(shown):
            yielding += 1
    y = yielding / len(page_bodies)
    return None, ("native" if y >= 0.5 else "scanned"), y, None


def probe_other(path):
    """Non-PDF: decodable text is native; opaque binary maps to scanned
    (the schema has no fifth class; scanned = needs stronger extraction).
    Legacy encodings (latin-1 emails) are text too: on a UTF-8 failure,
    decode latin-1 and require a high printable ratio, since latin-1
    never fails and would otherwise call any binary native."""
    suffix = path.casefold()
    if suffix.endswith((".docx", ".xlsx")):
        extractor = docx_text if suffix.endswith(".docx") else xlsx_text
        try:
            text = extractor(path)
        except OSError as error:
            return None, "corrupt", 0.0, str(error)
        if re.search(r"[A-Za-z0-9]", text):
            return None, "native", 1.0, None
        return None, "scanned", 0.0, None
    try:
        with open(path, "rb") as f:
            head_bytes = f.read(TEXT_PROBE_BYTES)
            size = os.fstat(f.fileno()).st_size
            if size > TEXT_PROBE_BYTES:
                f.seek(max(0, size - TEXT_PROBE_BYTES))
                tail_bytes = f.read(TEXT_PROBE_BYTES)
            else:
                tail_bytes = head_bytes
    except OSError:
        return None, "scanned", 0.0, None
    try:
        text = head_bytes.decode("utf-8")
        tail = tail_bytes.decode("utf-8", errors="replace")
    except UnicodeDecodeError:
        text = head_bytes.decode("latin-1")
        tail = tail_bytes.decode("latin-1")
        printable = sum(1 for c in text if c.isprintable() or c in "\r\n\t")
        if text and printable / len(text) < 0.9:
            return None, "scanned", 0.0, None
    reason = structural_truncation_reason(text, tail)
    if reason:
        return None, "suspect", 1.0, reason
    if re.search(r"[A-Za-z0-9]", text):
        return None, "native", 1.0, None
    return None, "scanned", 0.0, None


def walk_files(root):
    found = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith("."))
        for name in sorted(filenames):
            if name.startswith(".") or name == ".DS_Store":
                continue
            found.append(os.path.join(dirpath, name))
    return found


def main():
    parser = argparse.ArgumentParser(
        description="Walk a data-room folder and write manifest.json."
    )
    parser.add_argument("--root", required=True, help="Data-room folder to walk.")
    parser.add_argument("--out", required=True, help="Path for manifest.json.")
    parser.add_argument(
        "--extractor",
        choices=["auto", "stdlib"],
        default="auto",
        help="PDF probe selection. auto prefers poppler when installed; "
        "stdlib forces the fallback probe (evals pin this for "
        "environment-independent expected outputs).",
    )
    parser.add_argument(
        "--gaps",
        default=None,
        help="Optional gap-report.json to append the manifest stage's "
        "duplicate and unreadable entries to (merged and deduplicated "
        "if it exists).",
    )
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"FATAL: --root is not a directory: {args.root}", file=sys.stderr)
        sys.exit(2)

    files = walk_files(root)
    documents: list[dict[str, Any]] = []
    gap_entries = []
    counts = {
        "files": 0,
        "native": 0,
        "scanned": 0,
        "suspect": 0,
        "encrypted": 0,
        "corrupt": 0,
    }
    for path in files:
        rel = os.path.relpath(path, root).replace(os.sep, "/")
        ext = os.path.splitext(path)[1].lstrip(".").lower()
        if ext == "pdf":
            if args.extractor == "stdlib" or not HAVE_PDFINFO:
                probe = probe_pdf_stdlib
            elif HAVE_PDFTOTEXT:
                probe = probe_pdf_poppler
            else:
                probe = probe_pdf_hybrid
            pages, readability, y, note = probe(path)
        else:
            pages, readability, y, note = probe_other(path)
        if readability == "corrupt":
            gap_entries.append(
                {
                    "type": "unreadable",
                    "detail": f"{rel} could not be parsed ({note or 'unreadable'})",
                    "evidence": "readability=corrupt",
                }
            )
        elif readability == "encrypted":
            gap_entries.append(
                {
                    "type": "unreadable",
                    "detail": f"{rel} is encrypted",
                    "evidence": "readability=encrypted",
                }
            )
        elif readability == "suspect":
            gap_entries.append(
                {
                    "type": "unreadable",
                    "detail": (
                        f"{rel} appears truncated ({note or 'structural mismatch'})"
                    ),
                    "evidence": "readability=suspect",
                }
            )
        documents.append(
            {
                "id": sha256_id(path),
                "path": rel,
                "bytes": os.path.getsize(path),
                "ext": ext,
                "pages": pages,
                "readability": readability,
                "text_yield": round(y, 2),
            }
        )
        counts["files"] += 1
        counts[readability] += 1

    documents.sort(key=lambda d: (d["id"], d["path"]))
    corpus_id = hashlib.sha256(
        "\n".join(sorted({d["id"] for d in documents})).encode("utf-8")
    ).hexdigest()[:16]
    readability_total = sum(
        counts[key] for key in ("native", "scanned", "suspect", "encrypted", "corrupt")
    )
    if (
        counts["files"] != len(documents)
        or counts["files"] != len(files)
        or counts["files"] != readability_total
    ):
        print(
            f"FATAL: manifest does not reconcile with walk: walked {len(files)} "
            f"files, {len(documents)} manifest rows, counts.files={counts['files']}. "
            "Zero unreconciled items is an invariant; refusing to write.",
            file=sys.stderr,
        )
        sys.exit(2)

    # A byte-duplicate file yields two manifest rows sharing one id; per
    # schemas.md that is a duplicate gap entry, not an edge. The first row
    # in (id, path) order is the canonical path.
    paths_by_id = {}
    for d in documents:
        paths_by_id.setdefault(d["id"], []).append(d["path"])
    for did, dpaths in sorted(paths_by_id.items()):
        for extra in dpaths[1:]:
            gap_entries.append(
                {
                    "type": "duplicate",
                    "detail": f"{extra} is a byte duplicate of {dpaths[0]}",
                    "evidence": f"same sha256 as {did}",
                }
            )

    manifest = {
        "corpus_id": corpus_id,
        "root_label": os.path.basename(root),
        "documents": documents,
        "counts": counts,
    }
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    if args.gaps:
        entries = []
        if os.path.exists(args.gaps):
            with open(args.gaps, encoding="utf-8") as f:
                entries = json.load(f).get("entries", [])
        entries.extend(gap_entries)
        seen, deduped = set(), []
        for e in entries:
            key = json.dumps(e, sort_keys=True)
            if key not in seen:
                seen.add(key)
                deduped.append(e)
        deduped.sort(
            key=lambda e: (
                e.get("type", ""),
                e.get("detail", ""),
                e.get("evidence", ""),
            )
        )
        with open(args.gaps, "w", encoding="utf-8") as f:
            f.write(json.dumps({"entries": deduped}, indent=2, sort_keys=True) + "\n")
        print(
            f"Wrote {args.gaps}: {len(gap_entries)} manifest-stage entries, "
            f"{len(deduped)} total after merge/dedup"
        )
    print(
        f"Wrote {args.out}: {counts['files']} files "
        f"(native {counts['native']}, scanned {counts['scanned']}, "
        f"suspect {counts['suspect']}, encrypted {counts['encrypted']}, "
        f"corrupt {counts['corrupt']}); corpus_id {corpus_id}"
    )
    if args.extractor == "auto" and HAVE_PDFINFO and not HAVE_PDFTOTEXT:
        print(
            "note: pdftotext not found; used pdfinfo for PDF structure/page "
            "counts and the stdlib scanner for text yield",
            file=sys.stderr,
        )
    elif args.extractor == "auto" and not HAVE_PDFINFO:
        print(
            "note: pdfinfo not found; used stdlib PDF probe, pages reported as null",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
