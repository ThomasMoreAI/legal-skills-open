#!/usr/bin/env python3
"""reconcile_index.py - diff a VDR index (CSV/TSV/XLSX) against manifest.json.

Heuristically detects the index's name/title column and optional number
column (values like 3.2.1), matches each row to a manifest file by
normalized token overlap (with acronym folding so "Master Services
Agreement" matches acme-msa.pdf), and appends an index-missing gap entry
for every row with no matching file. Files absent from the index are noted
on stderr only. Merges into an existing gap-report.json, deduplicating
identical entries. XLSX is read with stdlib only (zip + sheet1.xml +
sharedStrings.xml).

Usage:
    python3 reconcile_index.py --index index.csv --manifest manifest.json \
        --out gap-report.json
"""

import argparse
import csv
import json
import os
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

XLSX_NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
NAMEISH = {
    "name",
    "title",
    "document",
    "description",
    "doc",
    "file",
    "filename",
    "item",
}
NUMISH = {"no", "no.", "number", "num", "index", "ref", "#", "id"}
SIZEISH = {"bytes", "byte size", "size in bytes", "file bytes"}
NUM_RE = re.compile(r"^\d+(\.\d+)*\.?$")
IDX_PREFIX = re.compile(r"^\d+(\.\d+)*[\s._-]+")
STOP = {"a", "an", "and", "of", "the", "to", "for"}


def col_index(ref):
    n = 0
    for ch in ref:
        if not ch.isalpha():
            break
        n = n * 26 + (ord(ch.upper()) - 64)
    return n - 1


def read_xlsx(path):
    with zipfile.ZipFile(path) as z:
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(
                XLSX_NS + "si"
            ):
                shared.append("".join(t.text or "" for t in si.iter(XLSX_NS + "t")))
        rows = []
        for row in ET.fromstring(z.read("xl/worksheets/sheet1.xml")).iter(
            XLSX_NS + "row"
        ):
            cells = {}
            for c in row.iter(XLSX_NS + "c"):
                idx = col_index(c.get("r", ""))
                if idx < 0:
                    idx = len(cells)
                if c.get("t") == "inlineStr":
                    val = "".join(t.text or "" for t in c.iter(XLSX_NS + "t"))
                else:
                    v = c.find(XLSX_NS + "v")
                    val = v.text if v is not None and v.text else ""
                    if c.get("t") == "s" and val:
                        val = shared[int(val)]
                cells[idx] = val
            width = max(cells) + 1 if cells else 0
            rows.append([cells.get(i, "") for i in range(width)])
        return rows


def read_rows(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".xlsx":
        return read_xlsx(path)
    delim = "\t" if ext in (".tsv", ".tab") else ","
    with open(path, newline="", encoding="utf-8-sig") as f:
        sample = f.read(4096)
        f.seek(0)
        try:
            delim = csv.Sniffer().sniff(sample, delimiters=",\t;").delimiter
        except csv.Error:
            pass
        return list(csv.reader(f, delimiter=delim))


def detect_columns(rows):
    """Returns body rows, name/number/byte columns, and first body row."""
    header = [c.strip().lower() for c in rows[0]] if rows else []
    name_col = num_col = size_col = None
    has_header = False
    for i, h in enumerate(header):
        if name_col is None and h in NAMEISH:
            name_col, has_header = i, True
        if num_col is None and h in NUMISH:
            num_col, has_header = i, True
        if size_col is None and h in SIZEISH:
            size_col, has_header = i, True
    body = rows[1:] if has_header else rows
    body = [r for r in body if any(c.strip() for c in r)]
    width = max((len(r) for r in body), default=0)
    if num_col is None:
        for i in range(width):
            vals = [r[i].strip() for r in body if i < len(r) and r[i].strip()]
            if vals and sum(bool(NUM_RE.match(v)) for v in vals) / len(vals) >= 0.6:
                num_col = i
                break
    if name_col is None:
        best = -1.0
        for i in range(width):
            if i == num_col:
                continue
            vals = [r[i].strip() for r in body if i < len(r) and r[i].strip()]
            alpha = [v for v in vals if re.search(r"[A-Za-z]", v)]
            score = sum(len(v.split()) for v in alpha) / len(vals) if vals else 0.0
            if score > best:
                best, name_col = score, i
    return body, name_col, num_col, size_col, 2 if has_header else 1


def parse_exact_bytes(value):
    value = re.sub(r"[\s,]", "", value or "")
    return int(value) if re.fullmatch(r"\d+", value) else None


def write_manifest(path, manifest):
    directory = os.path.dirname(os.path.abspath(path))
    fd, temporary = tempfile.mkstemp(prefix="manifest.", suffix=".tmp", dir=directory)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(manifest, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except OSError:
            pass
        raise


def norm_token(t):
    t = t.casefold()
    return t[:-1] if len(t) > 3 and t.endswith("s") else t  # plural fold


def name_tokens(s):
    return [norm_token(t) for t in re.findall(r"[A-Za-z0-9]+", s)]


def file_tokens(rel_path):
    """Tokens of every path segment, with per-segment index-number prefixes
    ('3.2 Supplier Agreements') stripped: numbering is structure, not content."""
    toks = set()
    for seg in rel_path.split("/"):
        toks.update(name_tokens(IDX_PREFIX.sub("", seg)))
    return toks


def coverage(raw_toks, ftoks):
    """Fraction of the row's content tokens found in the file's tokens.
    A contiguous window's initialism counting as a file token covers the whole
    window, so 'Master Services Agreement' is covered by a file token 'msa'."""
    content = {t for t in raw_toks if t not in STOP}
    if not content:
        return 0.0, 0
    covered = {t for t in content if t in ftoks}
    for i in range(len(raw_toks)):
        for j in range(i + 2, min(i + 6, len(raw_toks)) + 1):
            win = raw_toks[i:j]
            if all(w.isalpha() for w in win) and "".join(w[0] for w in win) in ftoks:
                covered.update(t for t in win if t not in STOP)
    return len(covered) / len(content), len(covered)


def match_row(number, name, manifest_docs, ftoks_by_path):
    raw_toks = name_tokens(name)
    best_path, best_cov = None, 0.0
    for doc in manifest_docs:
        path = doc["path"]
        if number:
            segs = [os.path.splitext(s)[0] for s in path.split("/")]
            if any(
                IDX_PREFIX.match(s + " ") and s.split()[0].rstrip(".") == number
                for s in segs
                if s
            ):
                return path
        cov, n_cov = coverage(raw_toks, ftoks_by_path[path])
        need = min(2, len({t for t in raw_toks if t not in STOP}))
        if cov >= 0.6 and n_cov >= need and cov > best_cov:
            best_path, best_cov = path, cov
    return best_path


def main():
    parser = argparse.ArgumentParser(
        description="Reconcile a VDR index against manifest.json into gap-report.json."
    )
    parser.add_argument("--index", required=True, help="Index file (CSV, TSV, XLSX).")
    parser.add_argument("--manifest", required=True, help="manifest.json path.")
    parser.add_argument(
        "--out", required=True, help="gap-report.json path (merged if it exists)."
    )
    args = parser.parse_args()

    with open(args.manifest, encoding="utf-8") as f:
        manifest = json.load(f)
    docs = manifest["documents"]
    ftoks_by_path = {d["path"]: file_tokens(d["path"]) for d in docs}

    rows = read_rows(args.index)
    if not rows:
        print(f"FATAL: no rows parsed from {args.index}", file=sys.stderr)
        sys.exit(2)
    body, name_col, num_col, size_col, first_row = detect_columns(rows)
    if name_col is None:
        print(f"FATAL: no name/title column detected in {args.index}", file=sys.stderr)
        sys.exit(2)

    index_base = os.path.basename(args.index)
    new_entries = []
    matched_paths = set()
    docs_by_path = {doc["path"]: doc for doc in docs}
    manifest_changed = False
    for offset, row in enumerate(body):
        name = row[name_col].strip() if name_col < len(row) else ""
        number = (
            row[num_col].strip() if num_col is not None and num_col < len(row) else ""
        )
        if not name and not number:
            continue
        hit = match_row(number, name, docs, ftoks_by_path)
        if hit:
            matched_paths.add(hit)
            expected_bytes = (
                parse_exact_bytes(row[size_col])
                if size_col is not None and size_col < len(row)
                else None
            )
            document = docs_by_path[hit]
            if (
                expected_bytes is not None
                and expected_bytes != document.get("bytes")
                and document.get("readability") in {"native", "scanned"}
            ):
                previous = document["readability"]
                document["readability"] = "suspect"
                manifest["counts"][previous] -= 1
                manifest["counts"]["suspect"] = manifest["counts"].get("suspect", 0) + 1
                manifest_changed = True
                new_entries.append(
                    {
                        "type": "unreadable",
                        "detail": (
                            f"{hit} byte size differs from {index_base} row "
                            f"{first_row + offset}: expected {expected_bytes}, "
                            f"actual {document.get('bytes')}"
                        ),
                        "evidence": "readability=suspect; exact index byte mismatch",
                    }
                )
            continue
        label = f"Index row {number} '{name}'" if number else f"Index row '{name}'"
        new_entries.append(
            {
                "type": "index-missing",
                "detail": f"{label} has no matching file",
                "evidence": f"{index_base} row {first_row + offset}",
            }
        )

    for doc in docs:
        if doc["path"] not in matched_paths:
            print(
                f"note: file not matched by any index row: {doc['path']}",
                file=sys.stderr,
            )

    if manifest_changed:
        write_manifest(args.manifest, manifest)

    entries = []
    if os.path.exists(args.out):
        with open(args.out, encoding="utf-8") as f:
            entries = json.load(f).get("entries", [])
    entries.extend(new_entries)
    seen, deduped = set(), []
    for e in entries:
        key = json.dumps(e, sort_keys=True)
        if key not in seen:
            seen.add(key)
            deduped.append(e)
    deduped.sort(
        key=lambda e: (e.get("type", ""), e.get("detail", ""), e.get("evidence", ""))
    )

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(json.dumps({"entries": deduped}, indent=2, sort_keys=True) + "\n")
    print(
        f"Wrote {args.out}: {len(new_entries)} new index-missing entries, "
        f"{len(deduped)} total after merge/dedup"
    )


if __name__ == "__main__":
    main()
