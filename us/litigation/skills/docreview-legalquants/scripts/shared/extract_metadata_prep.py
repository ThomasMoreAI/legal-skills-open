#!/usr/bin/env python3
"""Prepare receipted regex evidence and the mandatory document read plan.

For each unique manifest hash, this script extracts an opening-plus-tail text
surface and writes a non-canonical regex record. Fully receipted records may be
banked; ten percent are deterministically reassigned to an isolated reader
audit. Every other readable document requires an isolated reader. Canonical
metadata is written only by merge_metadata_reads.py after receipt validation.

Usage:
    python3 extract_metadata_prep.py --manifest manifest.json \
        --room-root <data-room-dir> --outdir <run-dir> [--pages 4]
"""

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import zlib

from document_text import (
    clean_text,
    extract_document_text,
    looks_like_markup,
    visible_text,
)

HAVE_PDFINFO = shutil.which("pdfinfo") is not None
HAVE_PDFTOTEXT = shutil.which("pdftotext") is not None

MONTHS = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}
MONTH_RE = (
    r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|"
    r"Dec(?:ember)?)"
)
DATE_RE = re.compile(
    rf"(?:(?P<m1>{MONTH_RE})\s+(?P<d1>\d{{1,2}})(?:st|nd|rd|th)?,?\s+(?P<y1>\d{{4}})"
    rf"|(?P<d2>\d{{1,2}})(?:st|nd|rd|th)?\s+(?:day\s+of\s+)?(?P<m2>{MONTH_RE}),?\s+(?P<y2>\d{{4}})"
    r"|(?P<y3>\d{4})-(?P<mo3>\d{2})-(?P<d3>\d{2})"
    r"|(?P<mo4>\d{1,2})/(?P<d4>\d{1,2})/(?P<y4>\d{2,4}))",
    re.IGNORECASE,
)
# Unnamed date alternation for embedding inside larger patterns.
DATE_ANY = (
    rf"(?:{MONTH_RE}\s+\d{{1,2}}(?:st|nd|rd|th)?,?\s+\d{{4}}"
    rf"|\d{{1,2}}(?:st|nd|rd|th)?\s+(?:day\s+of\s+)?{MONTH_RE},?\s+\d{{4}}"
    r"|\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{2,4})"
)
# A party name: run of capitalized words ("Bolt Industries LLC" stops at
# "amends"); capitalized sentence-starters are blocked as continuations so
# "... LLC. The parties" does not bleed into the name.
SENT = r"(?:The|This|Each|In|If|It|Whereas|Now|Dated|Any|All|Such|No)"
ORG = rf"[A-Z][\w.&'-]*(?:[ \t]+(?!{SENT}\b)[A-Z][\w.&'-]*)*"
# Standard drafting decorates each name: 'between Acme Corp, a Delaware
# corporation ("Provider"), and Bolt Industries LLC, a ...'. The optional
# parenthetical defined term and the appositive (', a <jurisdiction>
# <entity-form>') are consumed but not captured, so the clean names on both
# sides of between/and land in the groups.
PAREN = r"(?:\s*\([^)]*\))?"
APPOS = r"(?:,\s*an?\s+[^()]*?)?"
PARTIES_RE = re.compile(rf"between\s+({ORG}){PAREN}{APPOS}{PAREN}\s*,?\s+and\s+({ORG})")
REF_RE = re.compile(
    r"Amendment\s+No\.?\s*(\w+)\s+to\s+(?:the\s+)?"
    rf"([A-Z][A-Za-z0-9 .&'\n-]*?)\s+dated\s+({DATE_ANY})"
    rf"(?:\s*,?\s*(?:by\s+and\s+)?between\s+({ORG}(?:\s+and\s+{ORG})?))?"
)
# General references: 'pursuant to / under / entered into under the <Title>
# dated <date>'. The title is a run of capitalized words on one line; inline
# citations do not wrap mid-title, and a multiline grab would swallow prose.
TITLE_WORDS = r"[A-Z][A-Za-z0-9.&'-]*(?: [A-Z][A-Za-z0-9.&'-]*)*"
REF_UNDER_RE = re.compile(
    rf"(?:pursuant\s+to|under)\s+the\s+({TITLE_WORDS})\s+dated\s+({DATE_ANY})"
)
# Standalone 'Exhibit B' / 'Schedule 2' language, with an optional
# 'to the <Title>' tail. Regex never turns these into gaps; their presence
# forces an isolated reader to decide whether a distinct instrument exists.
REF_EXHIBIT_RE = re.compile(
    rf"\b(?:Exhibit|Schedule)\s+[A-Z0-9]+\b(?:\s+to\s+the\s+{TITLE_WORDS})?"
)
# Ordered: most specific first (an amendment to an MSA mentions both).
DOC_TYPE_HINTS = [
    ("amendment", re.compile(r"AMENDMENT\s+NO\.?\s*\w+\s+TO\b", re.I)),
    ("sow", re.compile(r"STATEMENT\s+OF\s+WORK", re.I)),
    ("guaranty", re.compile(r"\bGUARANT(?:Y|EE)\b", re.I)),
    ("agreement", re.compile(r"MASTER\s+SERVICES\s+AGREEMENT", re.I)),
    ("schedule", re.compile(r"^\s*SCHEDULE\b", re.I | re.M)),
    ("exhibit", re.compile(r"^\s*EXHIBIT\b", re.I | re.M)),
]
BOILER = re.compile(
    r"^(execution\s+(version|copy)|conformed\s+copy|confidential(ity)?\b.*"
    r"|privileged\b.*|draft|final|page\s+\d+.*|\d+)$",
    re.I,
)


def month_num(name):
    name = name.lower()
    if name in MONTHS:
        return MONTHS[name]
    for full, n in MONTHS.items():
        if full.startswith(name):
            return n
    return None


def to_iso(m):
    g = m.groupdict()
    if g["m1"]:
        mo, d, y = month_num(g["m1"]), int(g["d1"]), int(g["y1"])
    elif g["m2"]:
        mo, d, y = month_num(g["m2"]), int(g["d2"]), int(g["y2"])
    elif g["y3"]:
        mo, d, y = int(g["mo3"]), int(g["d3"]), int(g["y3"])
    else:
        mo, d, y = int(g["mo4"]), int(g["d4"]), int(g["y4"])  # assume M/D/Y
        if y < 100:
            y += 2000 if y < 70 else 1900
    if not mo or not (1 <= mo <= 12) or not (1 <= d <= 31):
        return None
    return f"{y:04d}-{mo:02d}-{d:02d}"


def find_dated_claim(text):
    """Return (ISO date, exact date quote), using the same preference rules."""
    first = plain_dated = None
    for match in DATE_RE.finditer(text):
        iso = to_iso(match)
        if not iso:
            continue
        claim = (iso, match.group(0))
        pre = text[max(0, match.start() - 40) : match.start()].lower()
        if re.search(r"(made|dated|entered\s+into|effective)\s+as\s+of\s*$", pre):
            return claim
        if plain_dated is None and re.search(r"\bdated\s*$", pre):
            plain_dated = claim
        if first is None:
            first = claim
    return plain_dated or first or (None, None)


def find_doc_type_claim(text, filename):
    for kind, pattern in DOC_TYPE_HINTS:
        match = pattern.search(text)
        if match:
            return kind, match.group(0)
    for kind, pattern in DOC_TYPE_HINTS:
        if pattern.search(filename):
            return kind, None
    return None, None


def title_from_filename(rel_path):
    base = os.path.splitext(os.path.basename(rel_path))[0]
    base = re.sub(r"^\d+(\.\d+)*[\s._-]*", "", base)
    words = [w for w in re.split(r"[-_\s]+", base) if w]
    return " ".join(w.capitalize() for w in words) or None


def guess_title_claim(text, rel_path):
    for raw_line in text.splitlines():
        line = " ".join(raw_line.split())
        if not line or len(re.findall(r"[A-Za-z]", line)) < 3:
            continue
        if BOILER.match(line) or DATE_RE.fullmatch(line):
            continue
        if re.match(r"^(?:type|sequence|filename|description|text)\b", line, re.I):
            continue
        if re.match(r"^exhibit\s+10(?:\.\d+)?$", line, re.I):
            continue
        return line[:120], line
    return title_from_filename(rel_path), None


def find_party_claims(text):
    match = PARTIES_RE.search(text)
    if not match:
        return [], []
    parties = []
    evidence = []
    for index in (1, 2):
        value = " ".join(match.group(index).split()).strip(" .,;")
        if value and value not in parties:
            parties.append(value)
            evidence.append({"value": value, "quote": match.group(index)})
    return parties, evidence


def find_references(text):
    refs = []
    for m in REF_RE.finditer(text):
        # quote stays verbatim; the text field is a normalized reference string
        parent_title = " ".join(m.group(2).split())
        date_str = " ".join(m.group(3).split())
        parties = " ".join(m.group(4).split()) if m.group(4) else ""
        ref_text = f"{parent_title} dated {date_str}"
        if parties:
            ref_text += f" between {parties.strip(' .,;')}"
        refs.append(
            {
                "gap_eligible": True,
                "kind": "parent-agreement",
                "quote": m.group(0),
                "source": "regex",
                "text": ref_text,
            }
        )
    for m in REF_UNDER_RE.finditer(text):
        parent_title = " ".join(m.group(1).split())
        date_str = " ".join(m.group(2).split())
        refs.append(
            {
                "gap_eligible": True,
                "kind": "parent-agreement",
                "quote": m.group(0),
                "source": "regex",
                "text": f"{parent_title} dated {date_str}",
            }
        )
    seen, out = set(), []
    for r in sorted(refs, key=lambda r: (r["text"], r["quote"])):
        key = (r["text"], r["quote"])
        if key not in seen:
            seen.add(key)
            out.append(r)
    return out


def pdftotext_range(path, first, last):
    r = subprocess.run(
        ["pdftotext", "-q", "-f", str(first), "-l", str(last), path, "-"],
        capture_output=True,
    )
    return r.stdout.decode("utf-8", errors="replace") if r.returncode == 0 else ""


def pdf_text_stdlib(path, n_pages):
    """Degraded extractor when poppler is absent: paren strings from Tj/TJ ops
    in raw/Flate page content streams, first n_pages plus the last page."""
    with open(path, "rb") as f:
        data = f.read()
    objs = {
        int(m.group(1)): m.group(2)
        for m in re.finditer(rb"(?m)^(\d+)\s+\d+\s+obj\b(.*?)endobj", data, re.S)
    }
    pages = []
    for _num, body in sorted(objs.items()):
        if not re.search(rb"/Type\s*/Page[^s]", body):
            continue
        m = re.search(rb"/Contents\s+(\d+)\s+\d+\s+R", body)
        content = b""
        if m and m.group(1) and int(m.group(1)) in objs:
            sm = re.search(rb"stream\r?\n(.*?)endstream", objs[int(m.group(1))], re.S)
            if sm:
                content = sm.group(1)
                if b"/FlateDecode" in objs[int(m.group(1))]:
                    try:
                        content = zlib.decompress(content.rstrip(b"\r\n"))
                    except zlib.error:
                        content = b""
        strings = re.findall(rb"\(((?:[^()\\]|\\.)*)\)\s*T[jJ]", content)
        text = b"\n".join(strings).decode("latin-1")
        text = re.sub(r"\\([()\\])", r"\1", text)
        pages.append(text)
    keep = pages[:n_pages]
    if len(pages) > n_pages:
        keep.append(pages[-1])
    return "\n".join(keep)


def extract_text(path, ext, manifest_pages, n_pages):
    if ext != "pdf":
        try:
            if ext.casefold() in {"docx", "xlsx", "eml"}:
                whole = extract_document_text(path)
                return whole[:12000] + (
                    "\n" + whole[-2000:] if len(whole) > 12000 else ""
                )
            with open(path, encoding="utf-8", errors="replace") as f:
                whole = f.read()
            if looks_like_markup(path, whole):
                whole = visible_text(whole)
            else:
                whole = clean_text(whole)
            return whole[:12000] + ("\n" + whole[-2000:] if len(whole) > 12000 else "")
        except OSError:
            return ""
    if HAVE_PDFTOTEXT:
        total = manifest_pages
        if total is None and HAVE_PDFINFO:
            info = subprocess.run(
                ["pdfinfo", path], capture_output=True, text=True, errors="replace"
            )
            pm = re.search(r"^Pages:\s+(\d+)", info.stdout, re.M)
            total = int(pm.group(1)) if pm else None
        if not total:
            return ""
        text = pdftotext_range(path, 1, min(n_pages, total))
        if total > n_pages:
            text += "\n" + pdftotext_range(path, total, total)
        return text
    return pdf_text_stdlib(path, n_pages)


def regex_record(doc, path, n_pages):
    text = extract_text(path, doc["ext"], doc.get("pages"), n_pages)
    filename = os.path.basename(doc["path"])
    doc_type, doc_type_quote = find_doc_type_claim(text, filename)
    title, title_quote = guess_title_claim(text, doc["path"])
    dated, dated_quote = find_dated_claim(text)
    parties, party_evidence = find_party_claims(text)
    references = find_references(text)
    evidence = {
        "dated": ({"quote": dated_quote, "source": "regex"} if dated_quote else None),
        "doc_type": (
            {"quote": doc_type_quote, "source": "regex"} if doc_type_quote else None
        ),
        "parties": [{**item, "source": "regex"} for item in party_evidence],
        "title": ({"quote": title_quote, "source": "regex"} if title_quote else None),
    }
    bankable = bool(
        doc_type
        and title
        and dated
        and doc_type_quote
        and title_quote
        and dated_quote
        and parties
        and len(party_evidence) == len(parties)
        and all(item.get("quote") for item in party_evidence)
        and all(ref.get("quote") for ref in references)
    )
    reasons = []
    if not bankable:
        reasons.append("identity-fields-not-fully-receipted")
    if REF_EXHIBIT_RE.search(text):
        bankable = False
        reasons.append("exhibit-language-requires-reader")
    return (
        {
            "id": doc["id"],
            "doc_type": doc_type,
            "title": title,
            "parties": parties,
            "dated": dated,
            "references": references,
            "evidence": evidence,
            "status": "regex-banked" if bankable else "metadata-incomplete",
        },
        sorted(set(reasons)),
        text,
    )


def audit_ids(banked_ids):
    if not banked_ids:
        return set()
    count = max(1, math.ceil(len(banked_ids) * 0.10))
    ranked = sorted(
        banked_ids,
        key=lambda doc_id: hashlib.sha256(
            ("diligence-regex-audit-v1\0" + doc_id).encode()
        ).hexdigest(),
    )
    return set(ranked[:count])


def hash_id(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return "sha256:" + digest.hexdigest()[:12]


def main():
    parser = argparse.ArgumentParser(
        description="Write regex evidence plus the mandatory document read plan."
    )
    parser.add_argument("--manifest", required=True, help="manifest.json path.")
    parser.add_argument("--room-root", required=True, help="Data-room folder.")
    parser.add_argument(
        "--outdir",
        required=True,
        help="Run dir for regex-metadata/ and read-plan.json.",
    )
    parser.add_argument(
        "--include-ids",
        default=None,
        help=(
            "Optional JSON scope: an ID array, {'ids': [...]}, or a "
            "messages.json whose non_messages array should be planned."
        ),
    )
    parser.add_argument(
        "--pages", type=int, default=4, help="First N pages to read (default 4)."
    )
    parser.add_argument(
        "--extractor",
        choices=["auto", "stdlib"],
        default="auto",
        help="PDF text extraction. auto prefers poppler when installed; "
        "stdlib forces the fallback (evals pin this).",
    )
    parser.add_argument(
        "--expand-bank",
        action="store_true",
        help=(
            "Convert every otherwise bankable regex record to reader-required. "
            "Use only after metadata-merge-report flags an audit disagreement."
        ),
    )
    parser.add_argument(
        "--defer-non-unit-metadata",
        action="store_true",
        help=(
            "Defer standalone metadata reads when review units do not depend "
            "on canonical metadata and the lawyer will approve that policy "
            "during review setup."
        ),
    )
    args = parser.parse_args()
    if args.extractor == "stdlib":
        global HAVE_PDFTOTEXT
        HAVE_PDFTOTEXT = False

    with open(args.manifest, encoding="utf-8") as f:
        manifest = json.load(f)
    meta_dir = os.path.join(args.outdir, "regex-metadata")
    input_dir = os.path.join(args.outdir, "reader-inputs")
    os.makedirs(meta_dir, exist_ok=True)
    os.makedirs(input_dir, exist_ok=True)

    by_id = {}
    for doc in manifest["documents"]:
        by_id.setdefault(doc["id"], []).append(doc)
    scope_ids = None
    if args.include_ids:
        with open(args.include_ids, encoding="utf-8") as handle:
            scope = json.load(handle)
        if isinstance(scope, list):
            scope_ids = scope
        elif isinstance(scope, dict) and isinstance(scope.get("ids"), list):
            scope_ids = scope["ids"]
        elif isinstance(scope, dict) and isinstance(scope.get("non_messages"), list):
            scope_ids = scope["non_messages"]
        else:
            sys.exit("include-ids must be an ID array, ids object, or messages.json")
        if any(not isinstance(doc_id, str) for doc_id in scope_ids):
            sys.exit("include-ids contains a non-string ID")
        if len(scope_ids) != len(set(scope_ids)):
            sys.exit("include-ids contains duplicate IDs")
        unknown = sorted(set(scope_ids) - set(by_id))
        if unknown:
            sys.exit(
                "include-ids contains IDs absent from manifest: " + ", ".join(unknown)
            )
        scope_ids = set(scope_ids)
    plan_rows = []
    banked = []
    records = {}
    planned_ids = sorted(scope_ids if scope_ids is not None else by_id)
    for doc_id in planned_ids:
        aliases = sorted(row["path"] for row in by_id[doc_id])
        doc = min(by_id[doc_id], key=lambda row: row["path"])
        readability = doc.get("readability")
        base = {
            "aliases": aliases,
            "canonical_path": doc["path"],
            "id": doc_id,
            "reader_input": None,
            "read_mode": ("image" if readability == "scanned" else "text"),
            "readability": readability,
        }
        if readability not in ("native", "scanned"):
            plan_rows.append(
                {
                    **base,
                    "disposition": "parked-unreadable",
                    "reason": f"readability={readability}",
                }
            )
            continue
        path = os.path.join(args.room_root, doc["path"])
        if not os.path.isfile(path):
            plan_rows.append(
                {
                    **base,
                    "disposition": "parked-unreadable",
                    "reason": "manifest-path-missing",
                }
            )
            continue
        try:
            actual_id = hash_id(path)
        except OSError:
            actual_id = None
        if actual_id != doc_id:
            plan_rows.append(
                {
                    **base,
                    "disposition": "parked-unreadable",
                    "reason": (
                        "manifest-identity-changed"
                        if actual_id is not None
                        else "manifest-path-unreadable"
                    ),
                }
            )
            continue
        record, reasons, reader_text = regex_record(doc, path, args.pages)
        text_chars = len(reader_text)
        records[doc_id] = record
        with open(os.path.join(meta_dir, f"{doc_id}.json"), "w", encoding="utf-8") as f:
            f.write(json.dumps(record, indent=2, sort_keys=True) + "\n")
        if readability == "native" and not args.defer_non_unit_metadata:
            input_name = doc_id.split(":", 1)[-1] + ".txt"
            with open(os.path.join(input_dir, input_name), "w", encoding="utf-8") as f:
                f.write(reader_text.rstrip() + "\n")
            base["reader_input"] = f"reader-inputs/{input_name}"
        if args.defer_non_unit_metadata:
            disposition = "deferred-to-review"
            reason = "no-active-canonical-metadata-consumer"
        elif readability == "native" and record["status"] == "regex-banked":
            banked.append(doc_id)
            disposition = "regex-banked"
            reason = "all-regex-claims-receipted"
        else:
            disposition = "reader-required"
            reason = ",".join(reasons) or f"readability={readability}"
        plan_rows.append(
            {
                **base,
                "disposition": disposition,
                "estimated_text_chars": text_chars,
                "reason": reason,
            }
        )

    audited = set(banked) if args.expand_bank else audit_ids(banked)
    for row in plan_rows:
        if row["id"] in audited:
            row["disposition"] = (
                "reader-required" if args.expand_bank else "regex-audit"
            )
            row["reason"] = (
                "regex-bank-expanded-after-audit-disagreement"
                if args.expand_bank
                else "deterministic-10-percent-regex-audit"
            )
    counts = {}
    for row in plan_rows:
        counts[row["disposition"]] = counts.get(row["disposition"], 0) + 1
    estimated_text_chars = sum(
        row.get("estimated_text_chars", 0)
        for row in plan_rows
        if row["disposition"] in {"reader-required", "regex-audit"}
    )
    read_plan = {
        "audit_rate": 0.10,
        "audit_seed": "diligence-regex-audit-v1",
        "bank_mode": "expanded" if args.expand_bank else "sampled",
        "documents": plan_rows,
        "scope": {
            "ids": planned_ids,
            "kind": "include-ids" if scope_ids is not None else "manifest",
        },
        "summary": {
            "dispositions": counts,
            "estimated_input_tokens": math.ceil(estimated_text_chars / 4),
            "estimated_text_chars": estimated_text_chars,
            "unique_documents": len(plan_rows),
        },
        "version": 1,
    }
    if args.defer_non_unit_metadata:
        read_plan["deferral_policy"] = "defer-non-unit-metadata"
    read_plan["plan_id"] = hashlib.sha256(
        json.dumps(read_plan, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()[:16]
    with open(os.path.join(args.outdir, "read-plan.json"), "w", encoding="utf-8") as f:
        f.write(json.dumps(read_plan, indent=2, sort_keys=True) + "\n")
    needs_reader = sorted(
        row["id"]
        for row in plan_rows
        if row["disposition"] in {"reader-required", "regex-audit"}
    )
    print(
        f"Wrote {len(records)} regex records and a {len(plan_rows)}-document "
        f"read plan; {len(needs_reader)} require fresh reader contexts"
    )
    if not HAVE_PDFTOTEXT:
        print(
            "note: pdftotext not found; used stdlib PDF text extraction",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
