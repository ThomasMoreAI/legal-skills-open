#!/usr/bin/env python3
"""
extract_provisions.py — split an instrument's text into addressable, hashed
provisions.

This is the deterministic half of /regulatory. It does not read, interpret or
summarise the law. It cuts the text at its own numbering convention and takes a
SHA-256 of each piece, so that every later claim about the instrument can be
anchored to an exact provision and a later run can prove, without a model in the
loop, whether that provision has moved.

Detection mirrors /redline's calibrate-first rule: instruments number themselves
differently (Article / Section / § / Regulation / Rule / Clause / bare decimal),
so the script counts how often each convention appears, picks the winner, and
reports the choice for a human to confirm before anything is built on it.

Every provision is also classed — recital, preamble, operative, annex, schedule
— by position rather than by reading. Recitals sit before the first operative
heading; annexes and schedules sit after the last one. The class is what stops a
recital being quoted as though it imposed a duty, which is the most common error
in regulatory writing and is invisible once the text is out of context.

Provenance travels with the hashes. Point --provenance at the directory
fetch_source.py wrote and the fetch record is copied into the output, so a
provisions file can always answer "which retrieval of which version is this?".
If read_version.py found the text superseded or incomplete, this refuses to
build on it. Historical selection requires a bound, dated version receipt.

The text kept for reading is normalised conservatively — trailing whitespace,
runs of blank lines, leading and trailing blank lines. The hash is taken over
less than that: all layout collapsed, wording only. Reformatting the source must
not manufacture a change; rewording it must always show as one.

Usage:
    python3 extract_provisions.py <instrument> --calibrate-only
    python3 extract_provisions.py <instrument> provisions.json
    python3 extract_provisions.py <instrument> provisions.json --pattern article
    python3 extract_provisions.py <instrument> provisions.json --provenance <fetchdir>

Input: .txt, .md, .html/.htm natively. Extract PDF text with the host document
tools first. Stdlib only.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path

from integrity import (
    IntegrityError,
    extraction_integrity,
    require_saved_file,
    validate_extraction_input,
    validate_version,
)

# One number grammar, shared by every convention that carries a number, because
# a citation is one token however it is introduced. States do not agree on the
# separator — `25-19-101`, `91-A:4`, `40.25.110`, `4–201` — and they suffix
# letters at any depth: `92F-1`, `132-1.3A`, `10006A`. A grammar that stops at
# the last digit does not lose a character, it names a different section of the
# same chapter: North Carolina's 132-1.3A filed as § 132-1.3, Hawaii's whole
# chapter 92F filed as § 92.
#
# A segment is digits with an optional letter, or a lone letter. The lookahead is
# what keeps `Section 10: Inspection of records` from reading `Inspection` as a
# segment `I` — a letter segment is a letter, not the start of a word.
SEGMENT = r"(?:\d+[A-Za-z]?|[A-Za-z]\d*)(?![A-Za-z])"
CITATION_NUMBER = rf"\d+[A-Za-z]?(?![A-Za-z])(?:[.\-–—:]{SEGMENT})*"

# The same number, but only where it is compound. A bare `1.` is a list marker,
# so the convention that reads a citation with no word in front of it requires
# at least one separator before it will call the line a heading.
CITATION_COMPOUND = rf"\d+[A-Za-z]?(?![A-Za-z])(?:[.\-–—:]{SEGMENT})+"

# What a citation looks like when it carries on past where the match stopped.
# A separator followed by a space is punctuation and ends the number; a
# separator followed by a character continues it.
CITATION_CONTINUES = re.compile(r"^(?:[0-9A-Za-z]|[.\-–—:/][0-9A-Za-z])")

# Ordered coarsest first. Selection walks this list in order, so an instrument
# with 113 Articles containing 512 numbered paragraphs is read as Articles —
# the paragraphs are subdivisions of provisions, not provisions.
PATTERNS: list[tuple[str, str, str]] = [
    ("article", "art", rf"^(Article\s+({CITATION_NUMBER}))\b\s*(.*)$"),
    ("regulation", "reg", rf"^(Regulation\s+({CITATION_NUMBER}))\b\s*(.*)$"),
    (
        "section",
        "sec",
        rf"^((?:SECTION|Section|SEC\.|Sec\.)\s+({CITATION_NUMBER})\.?)\s*(.*)$",
    ),
    ("us-code", "s", rf"^(§+\s*({CITATION_NUMBER}))\s*(.*)$"),
    ("rule", "rule", rf"^(Rule\s+({CITATION_NUMBER}))\b\s*(.*)$"),
    ("clause", "cl", rf"^(Clause\s+({CITATION_NUMBER}))\b\s*(.*)$"),
    ("paragraph", "para", rf"^(Paragraph\s+({CITATION_NUMBER}))\b\s*(.*)$"),
    # How most US states number a code: the citation alone at the head of the
    # line, with no word in front of it. `25-19-101.` in Arkansas, `16-4-201.` in
    # Wyoming, `2-6-1003` in Montana, `91-A:4` in New Hampshire, `47:1A-1.1` in
    # New Jersey. Seven of nineteen states that returned no output at all did so
    # because nothing here admitted this one shape.
    ("codified", "s", rf"^(({CITATION_COMPOUND})\.?)\s*(.*)$"),
    # Trailing text is optional for the same reason it is optional for recitals:
    # California prints `1798.100.` alone on its line and begins the text on the
    # next one. Requiring text after the number refused every CCPA section page,
    # and refused the `--pattern numbered` that the refusal itself offered — so
    # the only apparent way forward was to edit the statute until it matched.
    ("numbered", "p", r"^((\d+(?:\.\d+)*)\.)\s*(.*)$"),
]

MARKDOWN_HEADING = re.compile(r"^\s{0,3}#{1,6}\s*")
BLANK_RUN = re.compile(r"\n{3,}")
WHITESPACE = re.compile(r"\s+")

# EUR-Lex prints consolidated texts with the amending act marked inline — ▼B for
# the basic act, ▼M1 for the first amendment, ►C1 ... ◄ around a corrigendum.
# It is editorial apparatus, and useful to read, but it appears in every Article
# of a consolidated text and in none of an OJ text. Verified on the AI Act: left
# in the hash it reports all 113 shared Articles as amended, burying the 48 that
# really are. Stripped from the hash only; it stays in the text.
EDITORIAL_MARKER = re.compile(r"[►◄▼▲]\s*[A-Z]?\d*")

# Annexes and schedules are operative and are where the thresholds usually live,
# but they are not part of the numbered body and must not be swallowed by the
# last Article. Matched only on short heading-shaped lines, so a sentence that
# begins "Annex I sets out..." does not open a new region.
ANNEX_HEADING = re.compile(
    r"^(ANNEX(?:ES)?|SCHEDULE(?:S)?|APPENDIX|APPENDICES)\b\s*"
    r"([IVXLCDM]+|\d+[A-Za-z]?)?\s*(.*)$",
    re.I,
)
ANNEX_CLASS = {
    "annex": "annex",
    "annexes": "annex",
    "schedule": "schedule",
    "schedules": "schedule",
    "appendix": "annex",
    "appendices": "annex",
}

# EU-style recitals. EUR-Lex puts the number on its own line and the text on the
# next, so the trailing text is optional. Applied only inside the preamble, where
# a bare "(12)" cannot be an article paragraph or an annex point.
RECITAL = re.compile(r"^\((\d+)\)(?:\s+(\S.*))?$")

# A heading can be impersonated by a sentence that opens with a cross-reference,
# and a wrapped line is where that happens — "Article 18 of Regulation (EU)
# 2019/1020 shall apply ..." and Oregon's "192.005 to 192.170" both begin a line
# with something shaped exactly like a heading. Two signals separate them
# reliably: a cross-reference continues in lower case, or it continues the
# sentence it interrupts with a comma or semicolon. Both are tested everywhere.
CONTINUATION = ",;"

# The weaker signals — a long line, a caption that ends in a full stop — are
# applied only where the label does not announce itself. A § at the head of the
# line, or the full stop US drafting closes a section number with, is a claim to
# be a heading that prose does not make: `SEC. 2.` in a California chaptered act,
# `Section 101.  Short title.` in a Pennsylvania act, `§92F-1  Short title. This
# chapter shall be known ...` in Hawaii, where caption and body share one line.
# Judged on length and the closing full stop, all three read as prose, and
# refusing them is what put Pennsylvania and Hawaii in the failed column.
LONG_LINE = 120
LONG_CAPTION = 80

NON_BREAKING = {ord("\xa0"): " ", ord(" "): " ", ord(" "): " "}

# "'provider' means ..." / '"regulated service" has the meaning given by ...'
#
# Two US forms cost the index its most important entries when they are missing.
# Definition by reference — "has the same meaning as in section 1.59 of the
# Revised Code" — defines the term as firmly as any words of its own, and Ohio
# RC 1349.19 defines "Person" that way and only that way. The inclusive form —
# '"Data collector" may include, but is not limited to, government agencies' —
# is how a state act defines the entity the whole act is addressed to; missing
# it means the note never learns that the act's central word is not being used
# in its ordinary sense, which is the one thing this index exists to say.
OPEN_QUOTE = "‘“'\""
CLOSE_QUOTE = "’”'\""
DEFINITION_PATTERNS = [
    re.compile(
        rf"[{OPEN_QUOTE}]([^{OPEN_QUOTE}{CLOSE_QUOTE}\n]{{2,60}})[{CLOSE_QUOTE}]"
        rf"\s+(?:(?:may|shall)\s+)?"
        rf"(?:means?|includes?|ha(?:s|ve) the (?:same )?meaning)\b"
    )
]

HTML_BLOCK_BREAK = re.compile(
    r"(?i)</(p|div|h[1-6]|li|tr|section|article)\s*>|<br\s*/?>"
)
HTML_DROP = re.compile(r"(?is)<(script|style)\b.*?</\1\s*>")
HTML_TAG = re.compile(r"(?s)<[^>]+>")


def read_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return _read_pdf(path)
    raw = path.read_text(encoding="utf-8", errors="replace")
    if suffix in {".html", ".htm", ".xhtml"}:
        raw = HTML_DROP.sub(" ", raw)
        raw = HTML_BLOCK_BREAK.sub("\n", raw)
        raw = HTML_TAG.sub("", raw)
        raw = html.unescape(raw)
    # Non-breaking and narrow spaces are typesetting, not wording. Publishers use
    # them inconsistently between renderings of the same text, so folding them
    # here keeps a reformat from showing up as an amendment.
    raw = raw.translate(NON_BREAKING)
    return raw.replace("\r\n", "\n").replace("\r", "\n")


def _read_pdf(path: Path) -> str:
    sys.exit(
        f"PDF input is not extracted by this stdlib script ({path}). Use the host's "
        "document tools or a firm-approved OCR service, then pass text or markdown."
    )


def probe(line: str) -> str:
    """The form of a line used for heading detection only."""
    return MARKDOWN_HEADING.sub("", line).strip()


def normalise(text: str) -> str:
    """Conservative normalisation. Layout noise out, wording untouched."""
    lines = [ln.rstrip() for ln in text.split("\n")]
    return BLANK_RUN.sub("\n\n", "\n".join(lines)).strip()


def canonical(text: str) -> str:
    """The form that is hashed: wording only, every line break collapsed.

    Two renderings of one instrument break lines in different places — HTML
    extraction alone puts them wherever the publisher's markup does. Hashing the
    wrapped form reports an amendment every time a stylesheet changes, and a
    re-check that cries wolf stops being read. An amendment changes characters;
    re-wrapping does not.
    """
    return WHITESPACE.sub(" ", EDITORIAL_MARKER.sub(" ", text)).strip()


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def announced(candidate: str, match: re.Match) -> bool:
    """A § or a closing full stop is the label claiming to be a heading."""
    if candidate.lstrip().startswith("§"):
        return True
    after = candidate[match.end(2) :]
    return after[:1] == "." and after[1:2] in ("", " ", "\t")


def heading_shaped(candidate: str, remainder: str, strong: bool) -> bool:
    """A heading is a label and at most a title. A cross-reference runs on."""
    rest = remainder.strip()
    if not rest:
        return True
    if rest[0] in CONTINUATION or rest[0].islower():
        return False
    if strong:
        return True
    return len(candidate) <= LONG_LINE and not (
        rest.endswith(".") and len(rest) > LONG_CAPTION
    )


def truncates_citation(candidate: str, match: re.Match) -> bool:
    """True when the match stopped in the middle of the printed citation.

    This is the check the skill was missing. Every other refusal here is loud;
    a citation read short is silent, and it does not produce a broken label —
    it produces a different valid one. North Carolina's § 132-1.3A arrived as
    `§ 132-1.3`, which is a real neighbouring section, and the id allocator gave
    it `s-132-1-3-2` without comment. Nothing downstream can recover from that,
    so a grammar that does not fit this source must refuse it rather than round
    it to the nearest section it does fit.
    """
    return bool(CITATION_CONTINUES.match(candidate[match.end(1) :]))


def heading_match(rx: re.Pattern, line: str):
    candidate = probe(line)
    match = rx.match(candidate)
    if not match:
        return None
    if truncates_citation(candidate, match):
        return None
    if not heading_shaped(candidate, match.group(3), announced(candidate, match)):
        return None
    return match


def count_matches(lines: list[str]) -> dict[str, int]:
    counts = {}
    probes = [probe(ln) for ln in lines]
    for name, _prefix, pattern in PATTERNS:
        rx = re.compile(pattern)
        counts[name] = sum(1 for p in probes if heading_match(rx, p))
    return counts


def choose_convention(counts: dict[str, int]) -> str | None:
    """Coarsest convention that is really present, not the most frequent one.

    Frequency picks the finest grain, which is wrong: the same instrument
    rendered two ways can flip between Articles and bare paragraph numbers
    depending only on whether the publisher put "1." on its own line. The floor
    keeps a stray cross-reference from beating a document's real structure.
    """
    best = max(counts.values(), default=0)
    if best < 2:
        return None
    floor = max(2, best * 0.05)
    for name, _prefix, _pattern in PATTERNS:
        if counts[name] >= floor:
            return name
    return None


def slug(prefix: str, number: str) -> str:
    """The id is the citation, carrying no queue position and no history.

    The counter this used to append — `s-132-1-3-2`, once `s-132-1-3` was taken —
    was the only place a broken identity ever surfaced, and appending to it is
    what buried the break. Saved research and change tracking are keyed by this
    string, so it has to be derivable from the citation alone: a later run of the
    same chapter must produce the same id for the same section, and must not be
    able to produce it for a different one.
    """
    body = re.sub(r"[^a-z0-9]+", "-", number.lower()).strip("-")
    return f"{prefix}-{body}" if body else prefix


def infer_heading(inline: str, following: list[str]) -> str:
    """Heading is either trailing text on the label line, or a short line under it."""
    trimmed = inline.strip().lstrip("—–-:.").strip()
    if trimmed:
        return trimmed
    for line in following:
        candidate = probe(line)
        if not candidate:
            continue
        if len(candidate) <= 80 and not candidate.endswith("."):
            return candidate
        return ""
    return ""


def annex_heading_at(line: str) -> tuple[str, str, str] | None:
    """(class, number, trailing text) if this line opens an annex or schedule."""
    candidate = probe(line)
    if not candidate or len(candidate) > 80 or candidate.endswith("."):
        return None
    match = ANNEX_HEADING.match(candidate)
    if not match:
        return None
    word, number, remainder = match.group(1), match.group(2) or "", match.group(3)
    return ANNEX_CLASS[word.lower()], number, remainder


def make(
    prefix: str,
    number: str,
    label: str,
    heading: str,
    klass: str,
    lines: list[str],
    start: int,
    end: int,
) -> dict:
    body = normalise("\n".join(lines[start:end]))
    return {
        "id": slug(prefix, number),
        "label": label,
        "heading": heading,
        "class": klass,
        "line_start": start + 1,
        "line_end": end,
        "sha256": sha256(canonical(body)),
        "text": body,
    }


def split_preamble(lines: list[str], end: int) -> list[dict]:
    """Recitals if the preamble numbers itself, otherwise one undivided block."""
    if end <= 0:
        return []

    starts = [
        (i, m.group(1))
        for i, line in enumerate(lines[:end])
        if (m := RECITAL.match(probe(line)))
    ]
    if len(starts) < 2:
        text = normalise("\n".join(lines[:end]))
        if not text:
            return []
        return [make("preamble", "", "Preamble", "", "preamble", lines, 0, end)]

    provisions = []
    head = normalise("\n".join(lines[: starts[0][0]]))
    if head:
        provisions.append(
            make("preamble", "", "Preamble", "", "preamble", lines, 0, starts[0][0])
        )
    for position, (index, number) in enumerate(starts):
        stop = starts[position + 1][0] if position + 1 < len(starts) else end
        provisions.append(
            make(
                "recital",
                number,
                f"Recital ({number})",
                "",
                "recital",
                lines,
                index,
                stop,
            )
        )
    return provisions


def split_provisions(lines: list[str], convention: str) -> list[dict]:
    prefix, pattern = next((p, pat) for name, p, pat in PATTERNS if name == convention)
    rx = re.compile(pattern)

    starts: list[tuple[int, str, str, str]] = []
    for index, line in enumerate(lines):
        match = heading_match(rx, line)
        if match:
            label, number, remainder = match.group(1), match.group(2), match.group(3)
            starts.append((index, label.strip(), number, remainder))

    if not starts:
        sys.exit(f"No '{convention}' headings found in this instrument.")

    # Annexes are the ones that follow the whole numbered body. Restricting to
    # headings after the last operative start ignores tables of contents and
    # in-text cross-references, which is where the false positives are.
    annexes = [
        (index, found)
        for index, line in enumerate(lines)
        if index > starts[-1][0] and (found := annex_heading_at(line))
    ]
    body_end = annexes[0][0] if annexes else len(lines)

    provisions = split_preamble(lines, starts[0][0])

    for position, (index, label, number, remainder) in enumerate(starts):
        end = starts[position + 1][0] if position + 1 < len(starts) else body_end
        provisions.append(
            make(
                prefix,
                number,
                label,
                infer_heading(remainder, lines[index + 1 : index + 4]),
                "operative",
                lines,
                index,
                end,
            )
        )

    for position, (index, (klass, number, remainder)) in enumerate(annexes):
        end = annexes[position + 1][0] if position + 1 < len(annexes) else len(lines)
        provisions.append(
            make(
                klass,
                number,
                probe(lines[index]),
                infer_heading(remainder, lines[index + 1 : index + 4]),
                klass,
                lines,
                index,
                end,
            )
        )
    return provisions


def index_defined_terms(provisions: list[dict]) -> dict[str, list[str]]:
    """Terms the instrument defines, and where. Not what they mean."""
    terms: dict[str, list[str]] = {}
    for provision in provisions:
        if provision["class"] == "recital":
            continue
        for rx in DEFINITION_PATTERNS:
            for match in rx.finditer(provision["text"]):
                term = WHITESPACE.sub(" ", match.group(1)).strip()
                if term and provision["id"] not in terms.setdefault(term, []):
                    terms[term].append(provision["id"])
    return dict(sorted(terms.items(), key=lambda kv: kv[0].lower()))


HUMAN_NAMES = {
    "article": "Articles (Article 1, Article 2, ...)",
    "regulation": "Regulations (Regulation 1, Regulation 2, ...)",
    "section": "Sections (Section 1, Section 2, ...)",
    "us-code": "section symbols (§ 1798.140, US Code style)",
    "rule": "Rules (Rule 1, Rule 2, ...)",
    "clause": "Clauses (Clause 1, Clause 2, ...)",
    "paragraph": "Paragraphs (Paragraph 1, Paragraph 2, ...)",
    "codified": "bare code citations (25-19-101., 91-A:4, US state style)",
    "numbered": "plain numbers (1. , 2. , 3. ...)",
}


def single_heading(counts: dict[str, int]) -> str | None:
    """The convention to offer when the file holds exactly one heading.

    Overlapping grammars read one line twice — `4412.100.` is a plain number and
    a bare code citation both — so counting conventions rather than headings
    withdraws the offer exactly where a single published section needs it. What
    has to be true is that nothing matched twice. What is offered is then the
    convention selection itself would have taken.
    """
    if max(counts.values(), default=0) != 1:
        return None
    return next((name for name, _p, _r in PATTERNS if counts[name]), None)


# Appended to every branch that builds nothing. Testing found the same recovery
# every time: the agent read the refusal as a formatting problem, edited the
# publisher's headings until they matched, and carried on. That silently makes
# the model the author of the text the whole skill exists to quote verbatim —
# and each workaround broke something further down, so the run cost 2-3x in
# tokens and minutes without ever answering the question. Naming the moves is
# what stops them; a refusal that only says "no" gets treated as an obstacle.
NOT_A_FORMATTING_PROBLEM = [
    "",
    "Do not edit the source to match. Rewriting the publisher's headings, fetching a",
    "larger document to raise the count, hand-writing provisions.json, or piping text",
    "in are all ways of making this message go away without making it true, and each",
    "one puts words in the instrument's mouth that the publisher did not print.",
    "",
    "Naming a convention above is the only supported way past this. Otherwise stop",
    "and say what the file looks like — an unextractable source is a finding, not a",
    "failure to work around.",
]


def identity_report(path: Path, provisions: list[dict]) -> str | None:
    """Refuse a run in which two provisions cannot be told apart.

    A citation names a provision by its label, and everything the skill saves
    about a provision — a note's reliance, a re-check's before and after — is
    keyed by its id. Two provisions under one name is the one failure with no
    downstream signal at all: the note reads correctly and cites a real section,
    just not the one the words came from. So it is refused here or never.
    """
    for key in ("label", "id"):
        groups: dict[str, list[dict]] = {}
        for provision in provisions:
            groups.setdefault(provision[key], []).append(provision)
        clashes = [(name, group) for name, group in groups.items() if len(group) > 1]
        if not clashes:
            continue
        listed = [
            f"  {name or '(blank)'} — lines "
            + ", ".join(str(p["line_start"]) for p in group)
            for name, group in clashes[:6]
        ]
        if len(clashes) > 6:
            listed.append(f"  ... and {len(clashes) - 6} more")
        return "\n".join(
            [
                f"{path.name} issues the same {key} to more than one provision:",
                "",
                *listed,
                "",
                "Nothing was written. A quotation from either of two provisions "
                "sharing a",
                f"{key} verifies against a citation of the other, and a later "
                "re-check cannot",
                "say which of them moved — so the wrong section can be quoted, "
                "cited and",
                "tracked without anything reporting a problem.",
                "",
                "This is usually one of two things:",
                "",
                "  The page carries its furniture as well as its text, and a "
                "heading is",
                "  repeated in a breadcrumb, a contents list or a row of download "
                "links.",
                "  Fetch the section or chapter itself rather than an index or "
                "search view.",
                "",
                "  Or the convention is coarser than the document. Re-run with "
                "--calibrate-only",
                "  and name the one the text really uses.",
                *NOT_A_FORMATTING_PROBLEM,
            ]
        )
    return None


def calibration_report(path: Path, counts: dict[str, int], chosen: str | None) -> str:
    found = [f"  {HUMAN_NAMES[n]} — {counts[n]}" for n, _p, _r in PATTERNS if counts[n]]

    if chosen is not None and not counts[chosen]:
        return "\n".join(
            [
                f"Calibration failed: nothing in {path.name} is numbered like "
                f"{HUMAN_NAMES[chosen].split(' (')[0]}.",
                "",
                *(
                    ["What the file does have:", *found, ""]
                    if found
                    else ["No convention matched anything at all.", ""]
                ),
                "Nothing was built. A forced convention that matches nothing "
                "would cut the",
                "instrument into a single undivided block and cite every quote to it.",
                "",
                "Check that this is the file you meant to extract, then either name "
                "a convention",
                "the text actually uses or say what it uses and I will add it.",
                *NOT_A_FORMATTING_PROBLEM,
            ]
        )

    if chosen is None:
        alone = single_heading(counts)
        if alone:
            return "\n".join(
                [
                    f"{path.name} has exactly one heading — "
                    f"{HUMAN_NAMES[alone].split(' (')[0].rstrip('s')} — and "
                    "automatic",
                    "detection needs two before it will commit.",
                    "",
                    "The floor is there because a single line that reads like a "
                    "heading is more",
                    "often a cross-reference than a structure, and taking it would "
                    "silently make",
                    "one stray sentence the whole instrument.",
                    "",
                    "If this really is a single section — one provision saved on "
                    "its own page,",
                    "which is how most code sections are published — confirm it and "
                    "I will use it:",
                    "",
                    f"    --pattern {alone}",
                    "",
                    "Extraction then runs normally on that one section and keeps "
                    "its subdivisions.",
                    *NOT_A_FORMATTING_PROBLEM,
                ]
            )
        return "\n".join(
            [
                f"I could not work out how {path.name} divides itself up.",
                "",
                *(["Near misses:", *found, ""] if found else []),
                "How does the document in front of you number its parts — "
                "Articles, Sections,",
                "Rules, Clauses, or something else? Tell me and I will use that.",
                "",
                "If it has no numbering at all, this skill cannot anchor "
                "questions to it, and",
                "that is worth knowing before we go further.",
                *NOT_A_FORMATTING_PROBLEM,
            ]
        )

    if counts[chosen] == 1:
        return "\n".join(
            [
                f"{path.name} is being read as a single "
                f"{HUMAN_NAMES[chosen].split(' (')[0].rstrip('s').lower()}, on "
                "your confirmation.",
                "",
                "Check that the file really is one provision and not a longer "
                "document whose",
                "other headings this convention missed — that is the failure this "
                "confirmation",
                "can hide, and it looks like a clean run.",
            ]
        )

    lines = [
        f"{path.name} looks like it divides into "
        f"{HUMAN_NAMES[chosen].split(' (')[0]} — I found {counts[chosen]} of them.",
        "",
        "Please check that against the document in front of you: is that how it",
        "numbers its parts?",
        "",
    ]

    others = [
        (name, counts[name])
        for name, _p, _r in PATTERNS
        if counts[name] and name != chosen
    ]
    if others:
        lines.append("I also saw, and am treating as text inside those parts:")
        for name, count in others:
            lines.append(f"  {count} lines numbered like {HUMAN_NAMES[name]}")
        lines.append("")

    lines.extend(
        [
            "Why this matters: this choice decides how every later question cites the",
            "text, and how a future re-check knows which part is which. If it "
            "is wrong,",
            "nothing fails loudly — the questions just point at the wrong slices.",
            "",
            "If it is right, nothing to do. If it is wrong, say what the "
            "document really",
            "uses and I will re-run it.",
        ]
    )
    return "\n".join(lines)


def load_provenance(directory: Path, instrument: Path) -> tuple[dict, dict, dict]:
    """Validate and return the exact fetch, version, and integrity chain."""
    try:
        chain = validate_extraction_input(directory, instrument)
        version = validate_version(directory, chain)
        fetch = json.loads((directory / "fetch.json").read_text(encoding="utf-8"))
    except (IntegrityError, OSError, UnicodeError, json.JSONDecodeError) as error:
        sys.exit(str(error))
    return {"fetch": fetch, "version": version}, chain, version


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("instrument", type=Path)
    parser.add_argument("out", type=Path, nargs="?")
    parser.add_argument(
        "--provenance",
        type=Path,
        help="directory written by fetch_source.py; its fetch record travels "
        "into the output",
    )
    parser.add_argument(
        "--pattern",
        choices=[name for name, _p, _r in PATTERNS],
        help="force a numbering convention instead of auto-detecting",
    )
    parser.add_argument(
        "--calibrate-only",
        action="store_true",
        help="report the detected convention and stop",
    )
    parser.add_argument(
        "--no-text",
        action="store_true",
        help="omit provision text from the output (hashes only)",
    )
    args = parser.parse_args()

    if not args.instrument.exists():
        sys.exit(f"No such file: {args.instrument}")
    try:
        require_saved_file(args.instrument, "The instrument")
    except IntegrityError as error:
        sys.exit(str(error))

    text = read_text(args.instrument)
    lines = text.split("\n")
    counts = count_matches(lines)
    chosen = args.pattern or choose_convention(counts)

    if args.calibrate_only:
        print(calibration_report(args.instrument, counts, chosen))
        return 0 if chosen and counts[chosen] else 1

    if chosen is None:
        sys.exit(
            "Could not detect a numbering convention (nothing matched twice).\n\n"
            + calibration_report(args.instrument, counts, None)
        )
    if not counts[chosen]:
        sys.exit(calibration_report(args.instrument, counts, chosen))
    if not args.out:
        sys.exit("An output path is required unless --calibrate-only is used.")

    provenance_bundle = (
        load_provenance(args.provenance, args.instrument) if args.provenance else None
    )
    provenance = provenance_bundle[0] if provenance_bundle else None

    provisions = split_provisions(lines, chosen)
    clash = identity_report(args.instrument, provisions)
    if clash:
        sys.exit(clash)
    defined_terms = index_defined_terms(provisions)
    for provision in provisions:
        if args.no_text:
            provision.pop("text")

    payload = {
        "source": {
            "path": args.instrument.name,
            "sha256": sha256(canonical(text)),
        },
        "provenance": provenance,
        "convention": {"chosen": chosen, "counts": counts},
        "defined_terms": defined_terms,
        "provisions": provisions,
    }
    if provenance_bundle:
        payload["integrity"] = extraction_integrity(
            provenance_bundle[1], provenance_bundle[2], provisions
        )
    args.out.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    tally = {}
    for provision in provisions:
        tally[provision["class"]] = tally.get(provision["class"], 0) + 1
    breakdown = ", ".join(f"{count} {name}" for name, count in sorted(tally.items()))

    print(
        f"{len(provisions)} provisions -> {args.out} "
        f"(convention: {chosen}; source sha {payload['source']['sha256'][:12]})\n"
        f"  classes         {breakdown}\n"
        f"  defined terms   {len(defined_terms)}"
    )
    if provenance_bundle is None:
        print(
            "\n  No provenance. These hashes do not record where the text came "
            "from or\n  which version it is — pass --provenance <fetchdir> so the "
            "pin travels\n  with them."
        )
    else:
        version = provenance_bundle[2]
        if version["state"] == "historical_selected":
            print(
                f"\n  Using historical text effective {version['effective_date']} "
                f"because this research concerns {version['research_date']}."
            )
        else:
            print("\n  Using official text with a confirmed version record.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
