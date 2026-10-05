#!/usr/bin/env python3
"""parse_messages.py - Stage 2 (disputes) intake: manifest documents -> messages.json.

Reads the Stage 1 manifest (build_manifest.py), detects which documents are
RFC-822 messages (.eml extension, or extensionless files whose leading bytes
look like message headers), and parses each with email.parser: from, to, cc,
date (ISO, UTC-normalized), subject, message-id, in-reply-to, references,
has_attachments, plus a whitespace-normalized body fingerprint used by the
downstream copy-quorum gap detector. Custodian is the first path segment
under the room root (maildir convention). Non-message documents are listed
under "non_messages" and flow to the diligence-style document path later.
Output is deterministic: sorted keys, no timestamps, no absolute paths.

Usage:
    python3 parse_messages.py --manifest manifest.json --root <room-dir> \\
        --out messages.json
"""

import argparse
import datetime
import hashlib
import json
import os
import re
from email import policy
from email.parser import BytesParser
from email.utils import getaddresses, parsedate_to_datetime

# datetime.UTC was added in Python 3.11. The packaged skill otherwise runs on
# the older stdlib Python shipped by some managed macOS environments.
UTC = getattr(datetime, "UTC", datetime.timezone.utc)  # noqa: UP017

# Header sniff for extensionless maildir files: first non-blank line must be
# a plausible RFC-5322 header line and a core message header must be present.
HEADER_LINE = re.compile(rb"^[\x21-\x39\x3b-\x7e]+:")
CORE_HEADERS = ("message-id", "from", "received", "date", "return-path")

MID_TOKEN = re.compile(r"<[^<>\s]+>")


def looks_like_message(path, ext):
    if ext == "eml":
        return True
    if ext != "":
        return False
    try:
        with open(path, "rb") as f:
            head = f.read(8192)
    except OSError:
        return False
    for line in head.splitlines():
        if not line.strip():
            continue
        if not HEADER_LINE.match(line):
            return False
        break
    low = head.lower()
    return any((h.encode() + b":") in low for h in CORE_HEADERS)


def addr_list(msg, header):
    vals = msg.get_all(header) or []
    out, seen = [], set()
    for _, addr in getaddresses([str(v) for v in vals]):
        a = addr.strip().lower()
        if a and a not in seen:
            seen.add(a)
            out.append(a)
    return out


def iso_dates(msg):
    """(utc_iso, local_iso): UTC-normalized and original-offset forms.
    Calendar rollups use the local form; collections are cut in the
    sender's local time."""

    raw = msg.get("Date")
    if not raw:
        return None, None
    try:
        dt = parsedate_to_datetime(str(raw))
    except (TypeError, ValueError):
        return None, None
    if dt is None:
        return None, None
    if dt.tzinfo is None:
        # -0000 and bare dates parse naive; treat as UTC
        dt = dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC).isoformat(), dt.isoformat()


def mid_tokens(msg, header):
    vals = msg.get_all(header) or []
    out, seen = [], set()
    for v in vals:
        for tok in MID_TOKEN.findall(str(v)):
            if tok not in seen:
                seen.add(tok)
                out.append(tok)
    return out


def body_text(msg):
    if msg.is_multipart():
        parts = []
        for part in msg.walk():
            if part.get_content_maintype() != "text":
                continue
            if (part.get_content_disposition() or "") == "attachment":
                continue
            payload = part.get_payload(decode=True)
            if payload is not None:
                parts.append(payload.decode("utf-8", errors="replace"))
        return "\n".join(parts)
    payload = msg.get_payload(decode=True)
    if payload is None:
        payload = b""
    return payload.decode("utf-8", errors="replace")


def has_attachments(msg):
    if not msg.is_multipart():
        return False
    for part in msg.walk():
        if part.get_filename():
            return True
        if (part.get_content_disposition() or "") == "attachment":
            return True
    return False


def parse_one(path, rel):
    with open(path, "rb") as f:
        msg = BytesParser(policy=policy.compat32).parse(f)
    segs = rel.split("/")
    custodian = segs[0] if len(segs) > 1 else None
    folder = "/".join(segs[1:-1])
    frm = addr_list(msg, "From")
    body = re.sub(r"\s+", " ", body_text(msg)).strip()
    subject = re.sub(r"\s+", " ", str(msg.get("Subject") or "")).strip()
    date_utc, date_local = iso_dates(msg)
    return {
        "path": rel,
        "custodian": custodian,
        "folder": folder,
        "from": frm[0] if frm else None,
        "to": addr_list(msg, "To"),
        "cc": addr_list(msg, "Cc"),
        "date": date_utc,
        "date_local": date_local,
        "subject": subject,
        "message_id": (mid_tokens(msg, "Message-ID") or [None])[0],
        "in_reply_to": mid_tokens(msg, "In-Reply-To"),
        "references": mid_tokens(msg, "References"),
        "has_attachments": has_attachments(msg),
        "body_fp": hashlib.sha256(body.encode("utf-8")).hexdigest()[:12],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--manifest", required=True, help="Stage 1 manifest.json.")
    ap.add_argument("--root", required=True, help="Room root the manifest walked.")
    ap.add_argument("--out", required=True, help="Path for messages.json.")
    args = ap.parse_args()

    with open(args.manifest, encoding="utf-8") as f:
        manifest = json.load(f)
    root = os.path.abspath(args.root)

    messages = {}
    non_messages = []
    # byte duplicates share an id; the first (id, path) row is canonical
    rows = sorted(manifest["documents"], key=lambda d: (d["id"], d["path"]))
    for doc in rows:
        did = doc["id"]
        rel = doc["path"]
        if did in messages:
            messages[did]["duplicate_paths"].append(rel)
            continue
        path = os.path.join(root, rel.replace("/", os.sep))
        ext = doc.get("ext", "")
        if not looks_like_message(path, ext):
            if did not in non_messages:
                non_messages.append(did)
            continue
        rec = parse_one(path, rel)
        rec["duplicate_paths"] = []
        messages[did] = rec

    out = {"messages": messages, "non_messages": sorted(non_messages)}
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(
        f"Wrote {args.out}: {len(messages)} messages, {len(non_messages)} non-messages"
    )


if __name__ == "__main__":
    main()
