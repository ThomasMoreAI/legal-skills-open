#!/usr/bin/env python3
"""
fetch_source.py — retrieve an instrument's text from its official publisher and
record what was retrieved, from where, and when.

Why this exists rather than a web-fetch tool: the assistant's built-in fetching
reads a page and hands back a *model's rendering* of it. That is fine for
reading version banners and enough for deciding which URL to use. It is not
fine for quoting. A quote that passed through a summarising model cannot be
proved verbatim, and this skill's entire claim is that nothing is quoted unless
it came from the publisher. So: use the web-fetch tool to find and read the
page, use this script for the bytes anything gets quoted from.

The publisher assertion is the mechanical half of the skill's governing rule.
Pass --publisher with the host the jurisdiction registry names as authoritative;
if redirects land somewhere else, this fails rather than saving. A law firm
summary retrieved by accident is worse than no text at all, because it looks
exactly as citable in the output.

The other half is refusing anything that is not the document. Publishers sit
behind bot protection, and under rate limit they answer the right URL, from the
right host, with a success status and a JavaScript challenge page. That is the
one failure that looks healthy the whole way downstream, so it fails here.
Nothing is saved unless it is a 200 carrying no interstitial signature.

Accept-Encoding is pinned to identity: the saved bytes are the bytes served, so
the sha256 in fetch.json is a hash of something a human can open and check.

A redirect that stays on the publisher's host is reported rather than refused.
Publishers redirect legitimately — to a dated address, to a canonical one — but
they also answer an address they do not hold with 200 and an error page, which
is the same failure class as a bot challenge and just as invisible afterwards.
So the fetch record says whether the path moved, and the run says so on screen.

Usage:
    python3 fetch_source.py <url> <outdir>
    python3 fetch_source.py <url> <outdir> --publisher eur-lex.europa.eu
    python3 fetch_source.py <url> <outdir> --label "consolidated 27/07/2026"

Writes <outdir>/source.<ext> and <outdir>/fetch.json. Stdlib only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from integrity import (
    IntegrityError,
    check_destination_free,
    fetch_integrity,
    identity,
    reserve_destination,
)

# The `Mozilla/5.0 (compatible; <name>; <purpose>)` form is the long-standing
# convention for a client that identifies itself, and it is what public-sector
# WAFs are tuned to let through. A bare product token is refused outright by
# sso.agc.gov.sg and www.ecfr.gov — both verified — which pushes the run onto the
# browser-save path and loses the provenance this script exists to produce. The
# string is recorded in fetch.json, so the fetch record says what was sent.
USER_AGENT = (
    "Mozilla/5.0 (compatible; codex-for-legal/regulatory; "
    "legal research, primary sources)"
)
TIMEOUT = 60

# EUR-Lex answers 202 with an empty body when no Accept header is sent, which
# reads as a dead URL and is not one. Send what a browser sends.
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
    "application/pdf;q=0.9,text/plain;q=0.8,*/*;q=0.7",
    "Accept-Language": "en",
    "Accept-Encoding": "identity",
}

# A bot challenge is served by the right host, at the right URL, with a success
# status, and is not the instrument. It is the worst failure available here
# because everything downstream looks healthy. Observed live: eur-lex.europa.eu
# behind AWS WAF answers 202 with a 2 KB JavaScript challenge under rate limit.
#
# Hard signatures never appear in a legal text. Soft ones could, so they only
# fire on a body too small to be an instrument.
HARD_SIGNATURES = (
    b"awswafintegration",
    b"awswafcookiedomainlist",
    b"challenge-container",
    b"cf-browser-verification",
    b"cf_chl_",
    b"__cf_chl",
    b"_incapsula_resource",
    b"distil_r_captcha",
)
SOFT_SIGNATURES = (
    b"not a robot",
    b"checking your browser",
    b"just a moment...",
    b"enable javascript and then reload",
    b"unusual traffic",
)
SOFT_SIGNATURE_MAX_BYTES = 100_000

EXTENSIONS = {
    "text/html": ".html",
    "application/xhtml+xml": ".html",
    "application/pdf": ".pdf",
    "text/plain": ".txt",
    "application/xml": ".xml",
    "text/xml": ".xml",
    "application/json": ".json",
    "application/rtf": ".rtf",
}


def extension_for(content_type: str) -> str:
    return EXTENSIONS.get(content_type.split(";")[0].strip().lower(), ".bin")


def challenge_signature(body: bytes) -> str | None:
    lowered = body[:200_000].lower()
    for signature in HARD_SIGNATURES:
        if signature in lowered:
            return signature.decode()
    if len(body) <= SOFT_SIGNATURE_MAX_BYTES:
        for signature in SOFT_SIGNATURES:
            if signature in lowered:
                return signature.decode()
    return None


def fetch(url: str) -> tuple[bytes, dict]:
    request = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
            body = response.read()
            return body, {
                "final_url": response.geturl(),
                "status": response.status,
                "content_type": response.headers.get("Content-Type", ""),
                "http_date": response.headers.get("Date"),
                "last_modified": response.headers.get("Last-Modified"),
                "etag": response.headers.get("ETag"),
            }
    except urllib.error.HTTPError as exc:
        sys.exit(
            f"{url}\n  refused with HTTP {exc.code} {exc.reason}.\n"
            "  Report this rather than falling back to a secondary source."
        )
    except urllib.error.URLError as exc:
        sys.exit(f"{url}\n  could not be reached: {exc.reason}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("url")
    parser.add_argument("outdir", type=Path)
    parser.add_argument("--jurisdiction", required=True)
    parser.add_argument("--profile", required=True, help="stable source-profile id")
    parser.add_argument("--instrument-id", required=True, help="stable instrument id")
    parser.add_argument(
        "--publisher",
        help="host the registry names as authoritative; fail if redirects leave it",
    )
    parser.add_argument(
        "--label",
        default="",
        help=(
            "the version this URL is believed to serve, e.g. 'consolidated 27/07/2026'"
        ),
    )
    args = parser.parse_args()

    scheme = urlparse(args.url).scheme.lower()
    if scheme not in {"http", "https"}:
        sys.exit(f"Refusing a non-web URL: {args.url}")

    try:
        instrument_identity = identity(
            args.jurisdiction, args.profile, args.instrument_id
        )
        check_destination_free(args.outdir)
    except IntegrityError as error:
        sys.exit(str(error))

    body, meta = fetch(args.url)
    if not body:
        sys.exit(
            f"{meta['final_url']}\n"
            f"  returned HTTP {meta['status']} with an empty body.\n"
            "  This is the publisher declining, not a dead document. Try the "
            "jurisdiction's\n  preferred URL form from the registry before "
            "concluding the text is unavailable."
        )

    if meta["status"] != 200:
        sys.exit(
            f"{meta['final_url']}\n"
            f"  answered HTTP {meta['status']}, not 200.\n"
            "  A success code other than 200 means the publisher accepted the "
            "request and did\n  not serve the document. Nothing saved. Wait, then "
            "retry; if it persists, try\n  the jurisdiction's other URL form."
        )

    signature = challenge_signature(body)
    if signature:
        sys.exit(
            f"{meta['final_url']}\n"
            f"  served a bot challenge, not the instrument (matched {signature!r}, "
            f"{len(body):,} bytes).\n"
            "  This is the right host at the right URL returning the wrong "
            "document, which is\n  the one failure that looks like success all the "
            "way downstream. Nothing saved.\n\n"
            "  Usually rate limiting. Wait a few minutes and retry. If it "
            "persists, open the\n  URL in a browser, save the page, and pass the "
            "saved file to extract_provisions.py\n  — but record where it came "
            "from, because this script did not."
        )

    host = urlparse(meta["final_url"]).hostname or ""
    if args.publisher and not (
        host == args.publisher or host.endswith("." + args.publisher)
    ):
        sys.exit(
            f"Publisher assertion failed.\n"
            f"  expected: {args.publisher}\n"
            f"  landed on: {host}\n"
            f"  final URL: {meta['final_url']}\n"
            "  Nothing saved. Do not quote from this — find the publisher's own copy."
        )

    # Claimed once there is a document to store, not on the way in. The
    # reservation is what stops a second fetch landing on an earlier capture, and
    # it has to be taken before the first write — but a refused fetch that has
    # already taken it leaves an empty directory that the retry then reads as an
    # existing run. With a retry budget of two, that spends the budget on a
    # destination that holds nothing.
    try:
        reserve_destination(args.outdir)
    except IntegrityError as error:
        sys.exit(str(error))

    saved_as = "source" + extension_for(meta["content_type"])
    (args.outdir / saved_as).write_bytes(body)

    requested_path = urlparse(args.url).path
    landed_path = urlparse(meta["final_url"]).path
    redirected = landed_path != requested_path

    record = {
        "requested_url": args.url,
        "publisher_asserted": args.publisher,
        "publisher_host": host,
        "redirected_within_publisher": redirected,
        "user_agent": USER_AGENT,
        "version_label": args.label,
        "retrieved_at": datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "bytes": len(body),
        "sha256": hashlib.sha256(body).hexdigest(),
        "saved_as": saved_as,
        "integrity": fetch_integrity(body, instrument_identity),
        **meta,
    }
    (args.outdir / "fetch.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(
        f"{record['bytes']:,} bytes -> {args.outdir / saved_as}\n"
        f"  host    {host}\n"
        f"  served  {meta['http_date'] or 'no Date header'}\n"
        f"  sha256  {record['sha256'][:12]}\n"
        f"  label   {args.label or 'UNLABELLED — record which version this is'}"
    )
    if redirected:
        print(
            f"\n  Note: the publisher redirected you.\n"
            f"    asked for {requested_path}\n"
            f"    landed on {landed_path}\n"
            "  Often routine — publishers redirect to a dated or canonical address. "
            "But a\n  publisher that answers an address it does not hold with 200 and "
            "an error page\n  looks identical downstream, so read the saved bytes "
            "before quoting from them.\n"
            "  Observed live: www.govinfo.gov serves its error page this way."
        )
    if not args.label:
        print(
            "\n  An unlabelled fetch is a version you have not established.\n"
            "  Read the page's own version markers before quoting from this."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
