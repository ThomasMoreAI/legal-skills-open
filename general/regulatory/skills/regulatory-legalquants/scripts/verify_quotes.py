#!/usr/bin/env python3
"""
verify_quotes.py — check that every quotation in a note came from the fetched
text, and is cited to the provision the words actually live in.

This exists because of one asymmetry: a paraphrase of a statutory provision
reads exactly as well as the provision. Every other error in this skill
announces itself — a fetch fails, a version marker fires, a convention looks
wrong. A quote that was taken from a web-fetch rendering, from a search result
or from memory looks perfect, survives review, and is the sentence the lawyer
puts in front of a client.

So the check is mechanical and has no model in it. The note's quotes are matched
character by character against `provisions.json`, and the citation attached to
each one is matched against the provision that actually contains those words.

Six findings, in the order they matter:

    not-in-text          the words are not in the instrument at all
    misattributed        the words are real, the citation names somewhere else
    recital-as-operative recital or preamble words cited as though operative
    uncited              a quote with no provision citation
    superseded-as-current  the words are the earlier edition's, quoted as though
                         they were today's
    unquoted-instrument-text  the instrument's own words carried outside
                         quotation marks, where this check cannot see them

And one about the note as a whole: `unlinked`, when the note does not carry the
address the text was fetched from. A reader who has to ask where a quote came
from has been handed a claim rather than a source, and the URL is already in the
fetch receipt — so this is transcription, not research.

`refresh` quotes two editions, so `--earlier` takes the earlier run's extraction
and quotes are checked against both. Without it, every `was` side of an
amendment — the half `diff_runs.py` exists to hand over — reports as a
fabrication, which is the accusation least likely to be true here and the one
most likely to be worked around rather than answered.

The contract this enforces — blockquote plus em-dash cite line, ellipsis for
elision, double quotes reserved for the instrument's own words — is written for
humans in references/run-format.md. Change one and change the other.

Usage:
    python3 verify_quotes.py <note.md> <provisions.json>
    python3 verify_quotes.py <note.md> <provisions.json> --json findings.json
    python3 verify_quotes.py <note.md> <later>/provisions.json \
        --earlier <earlier>/provisions.json

Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections.abc import Sequence
from pathlib import Path

from extract_provisions import CITATION_NUMBER
from integrity import IntegrityError, require_saved_file, validate_extraction

# Publishers' editorial apparatus, stripped on both sides. Same rule as
# extract_provisions.py: ▼M1 marks which amending act a passage came from, and
# it is not part of the wording.
EDITORIAL_MARKER = re.compile(r"[►◄▼▲]\s*[A-Z]?\d*")
WHITESPACE = re.compile(r"\s+")

# Typography renderers change freely. Folded so that a quote copied through a
# terminal is not reported as a misquote for want of a curly apostrophe. Dashes
# are deliberately NOT folded — an en dash between two numbers is a range.
TYPOGRAPHY = {
    "‘": "'",
    "’": "'",
    "‚": "'",
    "‛": "'",
    "“": '"',
    "”": '"',
    "„": '"',
    "‟": '"',
    " ": " ",
    " ": " ",
    " ": " ",
}

ELLIPSIS = re.compile(r"\s*(?:\.\.\.|…|\[\s*\.\.\.\s*\])\s*")
FENCE = re.compile(r"^\s*(```|~~~)")
BLOCKQUOTE = re.compile(r"^\s{0,3}>\s?(.*)$")
CITE_LINE = re.compile(r"^\s*(?:—|–|--)\s*(.+)$")
# Matched inside a single paragraph, so a quotation may wrap over lines — which
# it usually does — without running into the next one.
INLINE_QUOTE = re.compile(r"\"([^\"]{8,600})\"|“([^”]{8,600})”")

# An inline run shorter than this is a defined term, a term of art, or a word
# the writer is holding at arm's length — not a quotation of the instrument.
INLINE_MIN_WORDS = 5

# Abbreviations a house citation style may use. The label word is allowed to
# vary; the number is not.
ABBREVIATIONS = {
    "article": ["article", "art"],
    "regulation": ["regulation", "reg"],
    "section": ["section", "sec", "s", "§"],
    "§": ["§", "section", "sec", "s"],
    "rule": ["rule", "r"],
    "clause": ["clause", "cl"],
    "paragraph": ["paragraph", "para", "par"],
    "recital": ["recital", "rec"],
    "annex": ["annex", "anx"],
    "schedule": ["schedule", "sch"],
    "appendix": ["appendix", "app"],
    "preamble": ["preamble", "recitals"],
}

# The number grammar is imported rather than restated. The two halves of this
# package have disagreed about a label the package itself produced twice now —
# once over `§ 1798.100` spacing, once over New Hampshire's `91-A:4`, which the
# extractor issued and this file could not parse, so every correct quotation
# from that chapter came back `uncited`. A finding that reads as a citation
# error and is not one invites the repair this skill must never make: retyping
# the publisher's headings until the tools agree.
#
# The word boundary belongs to the word branch only. `\b` after `§` needs a word
# character next to the symbol, so `§1798.100` parsed and `§ 1798.100` did not.
LABEL = re.compile(
    rf"^\s*(§+|[A-Za-z]+\b)\s*\.?\s*\(?\s*({CITATION_NUMBER}|[IVXLCDM]+)?",
    re.I,
)

# California and its imitators print the number alone — `1798.100.` is the whole
# heading, with no word in front of it — so extract_provisions.py has no word to
# put in the label. LABEL needs one, and returned nothing, which made every
# quotation from a source of that shape report `uncited`. That is the finding
# that reads as a citation error, is not one, and is fixed by retyping the
# publisher's headings — the exact repair this skill must never make.
BARE_NUMBER = re.compile(rf"^\s*({CITATION_NUMBER})\s*\.?\s*$")

RECITAL_CLASSES = {"recital", "preamble"}
RECITAL_WORDS = re.compile(r"\b(recital|recitals|preamble)\b", re.I)

# Same shape as the recital rule: words that live somewhere particular are cited
# as living there. A quotation of the text as it read before is not wrong, but
# read as current law it is worse than a misquote, because every word of it is
# genuine. The cite has to say which edition it is.
SUPERSEDED_WORDS = re.compile(
    r"\b(former|formerly|earlier|previous|previously|prior|repealed|superseded|"
    r"as enacted|as it read|before the amendment|before amendment|until "
    r"amended)\b",
    re.I,
)

# A code span is not a quotation, and that is the problem. Scanned at the same
# length as an inline quote, inside a paragraph so that a span may wrap — every
# note in this skill wraps at eighty columns, and a section heading set as code
# will cross a line more often than not. Reported only when the words turn out
# to be the instrument's own.
CODE_SPAN = re.compile(r"`([^`]{8,600})`")


def fold(text: str) -> str:
    """The form compared on both sides: wording, and nothing else."""
    text = unicodedata.normalize("NFC", text)
    text = text.translate(str.maketrans(TYPOGRAPHY))
    return WHITESPACE.sub(" ", EDITORIAL_MARKER.sub(" ", text)).strip()


def loosen(text: str) -> str:
    """A deliberately sloppy form, used only to word a failure message.

    If a quote matches under this and not under fold(), the writer retyped the
    publisher's punctuation rather than inventing the passage — a different
    mistake, and worth saying so instead of "not in the instrument".
    """
    return re.sub(r"[^a-z0-9 ]+", "", fold(text).lower())


def fragments(quote: str) -> list[str]:
    """A quote is its fragments, in order. Elision must be marked."""
    return [f for f in (fold(p) for p in ELLIPSIS.split(quote)) if f]


def contains(haystack: str, parts: list[str]) -> bool:
    position = 0
    for part in parts:
        found = haystack.find(part, position)
        if found < 0:
            return False
        position = found + len(part)
    return True


def cite_patterns(provision: dict) -> list[re.Pattern]:
    label = provision.get("label") or ""
    bare = BARE_NUMBER.match(label)
    if bare:
        # The number carries the citation on its own, so the section word is
        # optional: `§ 1798.100`, `Section 1798.100` and a bare `1798.100` all
        # name this provision. The boundaries still do the work — 1798.100 must
        # not answer for 1798.1005.
        words = "|".join(re.escape(f) for f in ABBREVIATIONS["section"])
        return [
            re.compile(
                rf"(?<![0-9A-Za-z.])(?:(?:{words})\s*\.?\s*)?"
                rf"{re.escape(bare.group(1))}(?![0-9A-Za-z.])",
                re.I,
            )
        ]
    match = LABEL.match(label)
    if not match:
        return []
    word, number = match.group(1).lower(), match.group(2)
    forms = ABBREVIATIONS.get(word, [word])
    alternation = "|".join(re.escape(f) for f in forms)
    if not number:
        return [re.compile(rf"(?<![0-9a-z])(?:{alternation})(?![0-9a-z])", re.I)]
    # The boundary is what keeps Article 4 from matching Article 40, and
    # Annex I from matching Annex II.
    return [
        re.compile(
            rf"(?<![0-9a-z])(?:{alternation})\s*\.?\s*\(?\s*{re.escape(number)}"
            rf"(?![0-9A-Za-z])",
            re.I,
        )
    ]


def cited(cite: str, provision: dict) -> bool:
    return any(rx.search(cite) for rx in cite_patterns(provision))


def attribution(quote: dict, provision: dict) -> tuple[str, str]:
    """Check explicit subdivisions; ambiguous structure never receives a pass."""
    match = next(
        (m for rx in cite_patterns(provision) if (m := rx.search(quote["cite"]))), None
    )
    if match is None:
        return "misattributed", "provision not cited"
    tail = quote["cite"][match.end() :]
    if "(" in match.group(0) and tail.startswith(")"):
        tail = tail[1:]
    suffix = re.match(r"((?:\s*\([a-zA-Z0-9]+\))+)", tail)
    if suffix is None:
        if (
            quote["kind"] != "inline"
            and tail.strip()
            and not tail.lstrip().startswith(",")
        ):
            return (
                "attribution-unverified",
                "unsupported pinpoint syntax; check manually",
            )
        return "ok", "article/provision level only; no subdivision cited"
    keys = re.findall(r"\(([a-zA-Z0-9]+)\)", suffix.group(1))
    remaining = tail[suffix.end() :].lstrip()
    if (
        remaining
        and not remaining.startswith(",")
        and (quote["kind"] != "inline" or remaining[0] in "(–-—")
    ):
        return (
            "attribution-unverified",
            "compound or ranged pinpoint requires a separate check",
        )
    scope = provision["text"]
    for key in keys:
        # Only line-start markers are structural; inline cross-references are not.
        #
        # Case is never folded. US drafting nests (a)(1)(A)(i), so (A) and (a)
        # are two live series inside one provision and matching case-insensitively
        # would merge them. Reading uppercase points as lowercase-only, which is
        # what this did, made every (A) — the ordinary US lettered point —
        # permanently unverifiable.
        #
        # Letters and romans share one class because (i) is on sight a member of
        # both. Enumerating both is what makes the slice stop at the real next
        # sibling — (ii) rather than the following letter — and what makes a
        # provision carrying both series report the ambiguity instead of guessing.
        if key.isdigit():
            token = r"\d+"
        elif key.isupper():
            token = r"(?:[IVXLCDM]+|[A-Z])"
        else:
            token = r"(?:[ivxlcdm]+|[a-z])"
        # The dotted form must be followed by space. `45 C.F.R. 160.103` wraps
        # onto a new line often enough to matter, and `C.` read as a lettered
        # point gives the provision two (C)s and reports every real one as
        # ambiguous. A marker is separated from its text; an abbreviation is not.
        #
        # A marker is also structural when it runs straight on from the markers
        # above it — `(D)(1) A state or local agency shall…` is how US drafting
        # opens a subdivision that has only one child, and reading only line
        # starts found no `(1)` inside `(D)` at all. That reported a correct
        # `(D)(1)` pinpoint as unlocatable, and the recorded repair was to
        # broaden the citation to the section until the checker stopped
        # objecting: the note then cited a thousand words for a sentence. The
        # chain has to be unbroken from the line start, so a cross-reference in
        # the middle of a sentence is still not a marker.
        markers = list(
            re.finditer(
                rf"(?m)^\s*(?:\([A-Za-z0-9]+\)[ \t]*)*?"
                rf"(?:\((?P<paren>{token})\)\s*|(?P<dot>{token})\.\s+)",
                scope,
            )
        )
        matches = [
            i
            for i, m in enumerate(markers)
            if (m.group("paren") or m.group("dot")) == key
        ]
        if len(matches) != 1:
            return (
                "attribution-unverified",
                "pinpoint not uniquely located in extracted structure; "
                "check saved source",
            )
        i = matches[0]
        # The slice keeps its own marker. US subdivisions are ordinarily quoted
        # with them — `(b) A widget dealer shall…` is how the provision reads —
        # and cutting the marker off made a correct quote carrying a correct
        # pinpoint report as misattributed. The drafter's only way out was to
        # damage the quote or the citation, which is the churn this check exists
        # to prevent. Leading extra text costs nothing: the comparison is a
        # substring search, so a quote that omits the marker still matches.
        scope = scope[
            markers[i].start() : markers[i + 1].start()
            if i + 1 < len(markers)
            else len(scope)
        ]
    if not contains(fold(scope), fragments(quote["text"])):
        return (
            "misattributed",
            "words occur in the article/provision but not the cited subdivision",
        )
    return "ok", "wording and explicit cited subdivisions checked"


def strip_fences(lines: list[str]) -> list[bool]:
    """True for lines inside a code fence, which are examples, not prose."""
    inside, flags = False, []
    for line in lines:
        if FENCE.match(line):
            inside = not inside
            flags.append(True)
        else:
            flags.append(inside)
    return flags


def collect(note: str) -> list[dict]:
    """Every quotation in the note, with its citation and where it sits."""
    lines = note.split("\n")
    fenced = strip_fences(lines)
    quotes: list[dict] = []

    index = 0
    while index < len(lines):
        if fenced[index]:
            index += 1
            continue

        match = BLOCKQUOTE.match(lines[index])
        if match:
            start, body = index, []
            while index < len(lines) and not fenced[index]:
                inner = BLOCKQUOTE.match(lines[index])
                if not inner:
                    break
                body.append(inner.group(1))
                index += 1
            cite_match = CITE_LINE.match(body[-1]) if body else None
            text = "\n".join(body[:-1] if cite_match else body)
            quotes.append(
                {
                    "kind": "blockquote",
                    "line": start + 1,
                    "text": text,
                    "cite": cite_match.group(1) if cite_match else "",
                }
            )
            continue

        paragraph, start = [], index
        while index < len(lines) and lines[index].strip() and not fenced[index]:
            if BLOCKQUOTE.match(lines[index]):
                break
            paragraph.append(lines[index])
            index += 1
        if not paragraph:
            index += 1
            continue

        block = "\n".join(paragraph)
        for found in INLINE_QUOTE.finditer(block):
            text = found.group(1) or found.group(2)
            if len(text.split()) < INLINE_MIN_WORDS:
                continue
            offset = block[: found.start()].count("\n")
            quotes.append(
                {
                    "kind": "inline",
                    "line": start + offset + 1,
                    "text": text,
                    # An inline quote is cited by the paragraph it sits in.
                    "cite": block,
                }
            )
    return quotes


def load_provisions(payload: dict, path: Path) -> list[dict]:
    provisions = payload.get("provisions") or []
    if not provisions:
        sys.exit(f"No provisions in {path}.")
    if any("text" not in p for p in provisions):
        sys.exit(
            f"{path} carries hashes but no text (built with --no-text).\n"
            "  Quotes can only be checked against the words. Re-run\n"
            "  extract_provisions.py without --no-text."
        )
    return provisions


def earlier_edition(quote: dict, holders: list[dict]) -> dict:
    """A quotation of the text as it read before, checked against the earlier run.

    `refresh` has to show the words that moved, and the `was` side of every
    amendment is by construction absent from today's extraction. Checked against
    the later run alone it comes back as a fabrication — and the recorded repair
    was not to delete the quote but to delete its quotation marks, which left
    the words in the note and took them out of this check.
    """
    finding = {
        **quote,
        "edition": "earlier",
        "holders": [p["id"] for p in holders],
        "named": [p["id"] for p in holders if cited(quote["cite"], p)],
    }
    if not finding["named"]:
        return {
            **finding,
            "finding": "uncited",
            "detail": "the citation does not name a provision the earlier run has",
        }
    if not SUPERSEDED_WORDS.search(quote["cite"]):
        return {
            **finding,
            "finding": "superseded-as-current",
            "detail": "these are the earlier edition's words; the cite has to say "
            "so — 'as it read', 'former', 'before the amendment'",
        }
    # Checked to the same depth as a current quote. A superseded quotation that
    # only had to name its section would be the cheaper of the two to write, and
    # the pinpoint is what a reader uses to set the two editions side by side.
    checks = [
        attribution(quote, p) for p in holders if p["id"] in set(finding["named"])
    ]
    status, coverage = next((c for c in checks if c[0] == "ok"), checks[0])
    if status != "ok":
        return {**finding, "finding": status, "detail": coverage}
    return {
        **finding,
        "finding": "ok",
        "detail": f"earlier edition, quoted as superseded — {coverage}",
    }


def unquoted_instrument_text(note: str, editions: list[str]) -> list[dict]:
    """The instrument's own words carried as code, where nothing checks them.

    A quotation that fails can be made to pass by taking the quotation marks
    off it. That is not a repair. The words stay in the note saying exactly what
    they said, the check stops seeing them, and the coverage falls with nothing
    reporting that it fell — recorded once, on two section headings restyled as
    code spans after they failed, which took the note from four checked
    quotations to two and then exited 0.
    """
    lines = note.split("\n")
    fenced = strip_fences(lines)
    found = []
    start = 0
    while start < len(lines):
        if fenced[start] or not lines[start].strip():
            start += 1
            continue
        stop = start
        while stop < len(lines) and lines[stop].strip() and not fenced[stop]:
            stop += 1
        block = "\n".join(lines[start:stop])
        for span in CODE_SPAN.finditer(block):
            text = span.group(1)
            if len(text.split()) < INLINE_MIN_WORDS:
                continue
            if any(fold(text) in edition for edition in editions):
                found.append(
                    {
                        "kind": "code-span",
                        "line": start + block[: span.start()].count("\n") + 1,
                        "text": text,
                        "cite": "",
                        "finding": "unquoted-instrument-text",
                        "detail": "these are the instrument's own words, set as "
                        "code where the quote check cannot see them — quote them",
                        "holders": [],
                        "named": [],
                    }
                )
        start = stop
    return found


def judge(
    quote: dict,
    provisions: list[dict],
    source: str | None,
    superseded: Sequence[dict] = (),
) -> dict:
    parts = fragments(quote["text"])
    holders = [p for p in provisions if contains(fold(p["text"]), parts)]
    named = [p for p in provisions if cited(quote["cite"], p)]

    def finding(kind: str, detail: str) -> dict:
        return {
            **quote,
            "finding": kind,
            "detail": detail,
            "holders": [p["id"] for p in holders],
            "named": [p["id"] for p in named],
        }

    if not holders:
        kept = [p for p in superseded if contains(fold(p["text"]), parts)]
        if kept:
            return earlier_edition(quote, kept)
        if len(parts) == 1 and any(
            loosen(quote["text"]) in loosen(p["text"]) for p in provisions
        ):
            return finding(
                "not-in-text",
                "the words match a provision except for punctuation — copy the "
                "quote from the fetched text rather than retyping it",
            )
        if len(parts) > 1 and any(
            all(f in fold(p["text"]) for f in parts) for p in provisions
        ):
            return finding(
                "not-in-text",
                "the fragments are in the instrument but not in this order in "
                "any one provision",
            )
        if source is not None and contains(source, parts):
            return finding(
                "not-in-text",
                "the words are in the fetched file but outside every numbered "
                "provision — check the numbering convention before quoting them",
            )
        return finding(
            "not-in-text",
            "not in the fetched text; a rendering or a recollection, not the "
            "instrument",
        )

    if all(p["class"] in RECITAL_CLASSES for p in holders) and not RECITAL_WORDS.search(
        quote["cite"]
    ):
        return finding(
            "recital-as-operative",
            f"these words are {holders[0]['label']}; a recital is cited as a "
            "recital, or not quoted",
        )

    if not named:
        return finding(
            "uncited",
            "no provision cited — the cite is the last line of the blockquote "
            "and opens with an em dash"
            if not quote["cite"].strip()
            else "the citation does not name a provision this instrument has",
        )

    overlap = {p["id"] for p in holders} & {p["id"] for p in named}
    if not overlap:
        return finding(
            "misattributed",
            f"cited to {', '.join(p['label'] for p in named)}; the words are in "
            f"{', '.join(p['label'] for p in holders)}",
        )

    checks = [attribution(quote, p) for p in holders if p["id"] in overlap]
    status, coverage = next((c for c in checks if c[0] == "ok"), checks[0])
    if status != "ok":
        return finding(status, coverage)
    return {
        **quote,
        "finding": "ok",
        "detail": coverage,
        "holders": [p["id"] for p in holders],
        "named": sorted(overlap),
    }


def write_manifest(
    args,
    payload: dict,
    provisions: list[dict],
    results: list[dict],
    failures: list[dict],
    dependencies: list[dict],
) -> None:
    """The provisions this note rests on, for a later `refresh` to filter by.

    Written only from a clean verification. A manifest built over failing quotes
    would pin the skill's re-check to provisions the note never really used, and
    the lawyer would be told their reading still holds when it never did.
    """
    if not results:
        print(
            "\n  No manifest written: this note quotes nothing, so it has proved "
            "no\n  reliance for a later refresh to filter on. Semantic "
            "dependencies record\n  what an established reading rests on besides "
            "its quotes; they cannot be\n  the whole of it."
        )
        return

    if failures:
        print(
            "\n  No manifest written: it would record a reliance on "
            "provisions this\n  note does not actually quote correctly."
        )
        return

    counts: dict[str, int] = {}
    for result in results:
        # A quote of the text as it read before proves reliance on the earlier
        # run, not on this one, and a later refresh filtered by it would re-check
        # provisions this note never quoted as current law.
        if result.get("edition") == "earlier":
            continue
        for id_ in result["named"]:
            counts[id_] = counts.get(id_, 0) + 1

    by_id = {p["id"]: p for p in provisions}
    quoted = [
        {
            "id": id_,
            "label": by_id[id_]["label"],
            "class": by_id[id_]["class"],
            "sha256": by_id[id_]["sha256"],
            "quotes": count,
        }
        for id_, count in sorted(counts.items())
    ]
    relied_ids = sorted({*counts, *(item["id"] for item in dependencies)})
    args.manifest.write_text(
        json.dumps(
            {
                "note": args.note.name,
                "provisions": args.provisions.name,
                "source": payload.get("source"),
                "provenance": payload.get("provenance"),
                "verification_coverage": [r["detail"] for r in results],
                "integrity": payload.get("integrity"),
                "provision_set": [
                    {
                        key: provision.get(key)
                        for key in ("id", "label", "heading", "class", "sha256")
                    }
                    for provision in provisions
                ],
                "quoted": quoted,
                "semantic_dependencies": dependencies,
                "relied_on": [
                    {
                        "id": id_,
                        "label": by_id[id_]["label"],
                        "class": by_id[id_]["class"],
                        "sha256": by_id[id_]["sha256"],
                        "quotes": counts.get(id_, 0),
                    }
                    for id_ in relied_ids
                ],
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        f"\n  Manifest: {len(counts)} quoted and {len(dependencies)} "
        f"semantic dependencies -> {args.manifest}"
    )


def recorded_urls(payload: dict) -> list[str]:
    """The addresses the fetch receipt says these bytes came from."""
    fetch = (payload.get("provenance") or {}).get("fetch") or {}
    seen = []
    for key in ("final_url", "requested_url"):
        url = fetch.get(key)
        if url and url not in seen:
            seen.append(url)
    return seen


def link_finding(note_text: str, payload: dict) -> str | None:
    """Absent provenance there is no address to require; absent a link, say so."""
    urls = recorded_urls(payload)
    if not urls or any(url in note_text for url in urls):
        return None
    return (
        "The note does not link the source.\n"
        f"  Fetched from: {urls[0]}\n"
        "  A reader should never have to ask where a quotation came from, and the\n"
        "  saved run is usually deleted after delivery — so the note is the only\n"
        "  place the address survives. references/run-format.md, 'Sources'."
    )


def parse_dependencies(values: list[str], provisions: list[dict]) -> list[dict]:
    by_id = {provision["id"]: provision for provision in provisions}
    dependencies = []
    for value in values:
        id_, separator, reason = value.partition("=")
        if id_ not in by_id:
            sys.exit(f"Unknown semantic dependency: {id_}")
        if not separator or not reason.strip():
            sys.exit("A semantic dependency must use id=reason.")
        provision = by_id[id_]
        dependencies.append(
            {
                "id": id_,
                "label": provision["label"],
                "class": provision["class"],
                "sha256": provision["sha256"],
                "reason": reason.strip(),
            }
        )
    return dependencies


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("note", type=Path)
    parser.add_argument("provisions", type=Path)
    parser.add_argument(
        "--earlier",
        type=Path,
        help="the earlier run's extraction, so a refresh may quote the text as "
        "it read before",
    )
    parser.add_argument("--json", type=Path, help="write the findings")
    parser.add_argument(
        "--manifest",
        type=Path,
        help="write the provisions this note rests on, for diff_runs.py to "
        "filter a later re-check by",
    )
    parser.add_argument(
        "--depends-on",
        action="append",
        default=[],
        metavar="ID=REASON",
        help="record an unquoted definition, exception, scope, or date dependency",
    )
    args = parser.parse_args()

    doors = [(args.note, "The note"), (args.provisions, "The extraction")]
    if args.earlier:
        doors.append((args.earlier, "The earlier extraction"))
    for path, label in doors:
        if not path.exists():
            sys.exit(f"No such file: {path}")
        try:
            require_saved_file(path, label)
        except IntegrityError as error:
            sys.exit(str(error))

    payload = json.loads(args.provisions.read_text(encoding="utf-8"))
    provisions = load_provisions(payload, args.provisions)
    try:
        validate_extraction(payload, args.provisions.parent)
    except IntegrityError as error:
        sys.exit(
            f"{error}\nSaved text changed or the provenance chain is incomplete; "
            "no quote or reliance record was accepted."
        )
    source_path = args.provisions.parent / payload.get("source", {}).get("path", "")
    source = (
        fold(source_path.read_text(encoding="utf-8", errors="replace"))
        if source_path.name and source_path.is_file()
        else None
    )

    superseded: list[dict] = []
    if args.earlier:
        earlier_payload = json.loads(args.earlier.read_text(encoding="utf-8"))
        superseded = load_provisions(earlier_payload, args.earlier)
        try:
            validate_extraction(earlier_payload, args.earlier.parent)
        except IntegrityError as error:
            sys.exit(
                f"{error}\nThe earlier run's saved text changed or its provenance "
                "chain is incomplete; it cannot stand behind a superseded quote."
            )

    note_text = args.note.read_text(encoding="utf-8")
    quotes = collect(note_text)
    results = [judge(q, provisions, source, superseded) for q in quotes]
    results += unquoted_instrument_text(
        note_text, [fold(p["text"]) for p in (*provisions, *superseded)]
    )
    failures = [r for r in results if r["finding"] != "ok"]
    unlinked = link_finding(note_text, payload)
    dependencies = parse_dependencies(args.depends_on, provisions)

    for result in results:
        head = (result["text"].strip().split("\n")[0])[:60]
        if result["finding"] == "ok":
            print(
                f"  ok   {args.note.name}:{result['line']}  "
                f'{", ".join(result["named"])}  "{head}..."'
            )
        else:
            print(
                f"  FAIL {args.note.name}:{result['line']}  "
                f'{result["finding"]}  "{head}..."\n'
                f"       {result['detail']}"
            )

    if unlinked:
        print(f"  FAIL {args.note.name}  unlinked\n       {unlinked.splitlines()[0]}")

    if args.json:
        args.json.write_text(
            json.dumps(
                {
                    "note": str(args.note),
                    "quotes": len(results),
                    "failures": len(failures),
                    "unlinked": bool(unlinked),
                    "findings": results,
                },
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

    if args.manifest:
        write_manifest(args, payload, provisions, results, failures, dependencies)

    print()
    if not results:
        print(
            "No quotes found in this note.\n"
            "  Either nothing was quoted — in which case the note is asserting "
            "what the\n  instrument says without showing it — or the quotes are "
            "not in the format\n  references/run-format.md describes, and are "
            "therefore unchecked."
        )
        return 1
    if failures:
        print(
            f"{len(failures)} of {len(results)} quotes failed. Fix or delete "
            f"them; a caveat on an unverified quote is still an unverified "
            f"quote, and restyling one is not fixing it."
        )
        return 1
    if unlinked:
        print(unlinked)
        return 1
    print(f"{len(results)} quotations matched against {args.provisions.name}.")
    for coverage in sorted({r["detail"] for r in results}):
        print(
            f"Coverage: {coverage}. Source lineage checked; "
            "legal analysis not validated."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
