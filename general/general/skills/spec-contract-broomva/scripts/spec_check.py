#!/usr/bin/env python3
"""spec_check — the deterministic half of the spec contract.

Reads a design doc (markdown or HTML) and checks the invariants that a script
can decide on its own. Everything it cannot decide — whether a decision is
*actually* expensive to reverse, whether an alternative is real or a strawman —
is out of scope by construction and belongs to ``references/rubric.md``.

The checks are a synthesis of five primary sources, each cited on the check that
carries it:

  LYNCH   Michael Lynch, "How to Write an Effective Software Design Document"
          (refactoringenglish.com, 2026-06-24) + the Little Moments worked example
  GOOGLE  Malte Ubl, "Design Docs at Google" (industrialempathy.com)
  RUST    rust-lang/rfcs 0000-template.md
  NYGARD  Michael Nygard, "Documenting Architecture Decisions" (2011)
  OXIDE   Oxide Computer RFD 1, "Requests for Discussion"

Usage:
    spec_check.py DOC [DOC ...] [--profile adr|spec|plan|rfd] [--json]
                  [--strict] [--check-links]

Exit codes: 0 all required checks pass · 1 a required check failed
            2 bad invocation.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable

# --------------------------------------------------------------------------
# Section vocabulary.
#
# One producer for every synonym set. A corpus does not use canonical headings —
# "Missing features", "What this is not" and "Out of scope" are all the same
# section — so the checker resolves heading text to a CLASS, never to a name.
# Adding a synonym here is the only supported way to widen a class.
# --------------------------------------------------------------------------

SECTION_CLASSES: dict[str, tuple[str, ...]] = {
    "objective": ("objective", "summary", "purpose", "tl;dr", "tldr", "overview"),
    "context": ("background", "context", "motivation", "problem", "why now"),
    "goals": ("goals", "requirements", "outcomes", "what we want"),
    "non_goals": (
        "non-goals", "non goals", "nongoals", "out of scope", "not in scope",
        "what this is not", "missing features", "explicitly excluded",
        "deliberately omitted", "exclusions",
    ),
    "design": ("design", "decision", "architecture", "approach", "proposal",
               "solution", "implementation", "mechanism", "how it works",
               "the actual design", "reference-level explanation"),
    "alternatives": (
        "alternatives", "alternatives considered", "rationale and alternatives",
        "options considered", "why not", "other approaches", "prior art",
        "considered and rejected", "options rejected", "rejected options",
        # Bare "rejected" is deliberately absent: it is an ordinary past
        # participle, and as a suffix it made "06 Unit economics — and why the
        # generic clone was rejected" (a pricing table) an alternatives section.
        # A section class needs a noun phrase, not a verb that ends a sentence.
    ),
    "drawbacks": (
        "drawbacks", "consequences", "costs", "downsides", "risks",
        "trade-offs", "tradeoffs", "limitations", "what this costs",
        "negative consequences", "what we give up",
    ),
    "open_questions": (
        "open issues", "open questions", "unresolved questions", "unresolved",
        "unknowns", "to decide", "tbd", "outstanding",
    ),
    "acceptance": (
        "acceptance", "acceptance criteria", "service level objectives", "slo",
        "slos", "success criteria", "definition of done", "how we will know",
        "test plan", "rollout criteria",
        # "validation" and "measurement" are deliberately absent: in a spec they
        # name INPUT validation and instrumentation far more often than an
        # acceptance bar, and classifying them here produced a hard C8 failure
        # on sections that were never making a claim about done-ness.
    ),
}

# Profile → (required, recommended). A profile is a claim about which
# reversal-cost axes this document type exists to pin down; it is not a style.
#
# The required set is deliberately small and is the intersection of what the
# five sources agree is load-bearing. `alternatives` is required everywhere
# because all five say so in the same words — GOOGLE calls it "one of the most
# important" sections, RUST makes it a template heading, LYNCH, NYGARD and OXIDE
# each make the comparison the point of the document. A missing recommended
# section warns; the doc still passes.
#
# The split is derived from the five sources, NOT from a measurement. An earlier
# version of this comment claimed the opposite — that requiring all nine classes
# passed 1/105 and the split was "what made the contract a bar a new doc can
# clear." Cross-model review challenged the attribution and the re-measurement
# refuted it: on this workspace's 105 existing specs/plans/ADRs (2026-09-16),
# BOTH arms pass 0/105. The split buys exactly zero existing documents.
#
# What the split is actually for: `required` is the intersection of what all
# five sources independently call load-bearing, so failing it means failing a
# published consensus rather than a local preference. The calibration evidence
# is the other direction — LYNCH's own worked example passes at `--profile spec`
# with zero failures, which is what distinguishes a demanding gate from a
# miscalibrated one. The corpus number says only that this corpus does not meet
# the bar; it is not evidence about where the bar belongs.
PROFILES: dict[str, dict[str, tuple[str, ...]]] = {
    "adr": {
        "required": ("context", "design", "alternatives", "drawbacks"),
        "recommended": ("objective", "acceptance"),
    },
    "spec": {
        "required": ("objective", "design", "non_goals", "alternatives"),
        "recommended": ("context", "goals", "drawbacks", "acceptance",
                        "open_questions"),
    },
    "plan": {
        # A plan with no definition of done is a wish list, so acceptance is
        # required here and merely recommended on a spec.
        "required": ("objective", "goals", "acceptance"),
        "recommended": ("non_goals", "design", "open_questions"),
    },
    "rfd": {
        "required": ("objective", "design", "alternatives", "drawbacks"),
        "recommended": ("context", "open_questions", "acceptance"),
    },
    "note": {
        # For short docs that are still design-bearing. The floor, not a pass.
        "required": ("design",),
        "recommended": ("objective", "alternatives"),
    },
}


def required(profile: str) -> tuple[str, ...]:
    return PROFILES[profile]["required"]


def recommended(profile: str) -> tuple[str, ...]:
    return PROFILES[profile]["recommended"]

# NYGARD: proposed/accepted/deprecated/superseded, "if a decision is reversed we
# will keep the old one around, but mark it as superseded".
# OXIDE: prediscussion/ideation/discussion/published/committed/abandoned.
# The union below is deliberately permissive; the constraint that bites is that
# a terminal state must name its successor.
# NYGARD's four, OXIDE's six, and the states this workspace's own documents
# actually carry. The last group is not a concession: a checker whose vocabulary
# is narrower than its corpus reports "no status field" about documents that
# visibly have one, which is a false statement, not a strict standard. Measured:
# requiring only the first two groups produced 34 such failures across 105 docs.
VALID_STATUSES = {
    # NYGARD
    "proposed", "accepted", "deprecated", "superseded",
    # OXIDE
    "prediscussion", "ideation", "discussion", "published", "committed",
    "abandoned",
    # in use in this corpus
    "draft", "in-review", "review", "implemented", "rejected", "approved",
    "final", "current", "active", "living", "archived", "historical",
    "wip", "complete", "shipped", "done", "planned", "exploratory",
    "design-complete", "proposal",
}
STATUS_NEEDS_POINTER = {"superseded", "deprecated"}

# GOOGLE: "non-goals aren't negated goals like 'The system shouldn't crash', but
# rather things that could reasonably be goals, but are explicitly chosen not to
# be goals." A bare negation is the defect this detects.
NEGATION_HEAD = re.compile(
    r"^\W*(?:the\s+\w+\s+)?(?:should\s+not|shouldn'?t|must\s+not|mustn'?t|"
    r"will\s+not|won'?t|cannot|can'?t|does\s+not|doesn'?t|is\s+not|isn'?t|"
    r"never|avoid(?:ing)?|prevent(?:ing)?)\b",
    re.I,
)
# The discriminator is the MODAL, not the word "no". A declined goal is a noun
# phrase — "No support for albums", "Location-aware caching" — and never reaches
# NEGATION_HEAD, which matches only modal/auxiliary negations. An earlier cut
# added a noun-phrase exemption on top and it suppressed a true positive ("Must
# not lose data": "not lose" read as a noun phrase), so the exemption is gone.

# Every alternation branch needs BOTH boundaries. The first cut lost the closing
# \b when the Pro/Con idiom was added, and "but" then matched "Butterfly" — so a
# bare list of product names read as a list of reasoned rejections.
REJECTION_MARKERS = re.compile(
    r"\b(?:but|however|rejected?|lock-?in|expensive|costly|complexity|overkill|"
    r"doesn'?t|don'?t|can'?t|cannot|wouldn'?t|lacks?|missing|instead|downside|"
    r"drawback|risk|slower|unsupported|discarded|dismissed|cons?)\b"
    r"|\btoo\s+\w+|\bnot\s+worth\b|\bruled\s+out\b",
    re.I,
)

# GOOGLE's implementation-manual anti-pattern: "If a doc basically says 'This is
# how we are going to implement it' without going into trade-offs, alternatives,
# and explaining decision making … it would probably have been a better idea to
# write the actual program right away."
TRADEOFF_LANGUAGE = re.compile(
    r"\b(?:trade-?offs?|instead\s+of|rather\s+than|at\s+the\s+cost\s+of|"
    r"we\s+rejected|versus|vs\.?|downside|upside|alternative|in\s+exchange|"
    r"we\s+chose|we\s+considered|weighed|compared\s+(?:to|with)|"
    r"the\s+cost\s+is|pros?\s+and\s+cons?|one-?way\s+door|two-?way\s+door)\b",
    re.I,
)

# LYNCH's SLO section: "A well-defined SLO prevents ambiguity by expressing goals
# in concrete, objective terms." A number with a unit, a percentage, or a
# runnable command all count as concrete; adjectives do not.
# Every unit needs a closing boundary: without one, "3 ministers" measured as
# "3 min". And a percentile NAME is not a target — "p50 latency should feel
# fast" names the metric and states no threshold — so p50 only counts when a
# comparator and a number follow it.
MEASURABLE = re.compile(
    r"\b\d+(?:\.\d+)?\s?%"
    r"|\b\d+(?:\.\d+)?\s?"
    r"(?:ms|s|sec|secs|seconds?|min|mins|minutes?|h|hrs?|hours?|days?|weeks?|"
    r"[KMGT]B|rps|qps|LOC|lines|px|USD)\b"
    r"|\b\d+(?:\.\d+)?\s?req/s"
    r"|\bp\d{2}\b[^.\n]{0,40}?(?:<=?|>=?|=|≤|≥|under|below|within|at\s+most)"
    r"\s*\d"
    r"|\b\d+\s*/\s*\d+(?!\s*/)\b(?<!\d{4}/\d\d/\d\d)|\$\s?\d"
    r"|`[^`\n]*(?:test|check|pytest|cargo|make|npm|bun|curl|gh)\b[^`\n]*`",
    re.I,
)

# NYGARD: "All consequences should be listed here, not just the positive ones."
# This is a COST vocabulary, deliberately distinct from TRADEOFF_LANGUAGE above:
# a drawbacks section states what the chosen design costs, which is not the same
# utterance as comparing it to an option that was not chosen.
COST_LANGUAGE = re.compile(
    r"\b(?:cost(?:s|ly)?|expensive|doubles?|increases?|grows?|slower|slows?|"
    r"harder|more\s+\w+|loses?|lose|losing|give[s]?\s+up|gave\s+up|"
    r"sacrific\w+|at\s+the\s+expense|penalt\w+|degrad\w+|regress\w+|"
    r"no\s+longer|breaks?|limits?|limitation|risk|downside|drawback|"
    r"trade-?off|we\s+accept|requires?\s+(?:more|extra|additional)|"
    r"overhead|complexity|debt|churn|coupling|lock-?in|cannot|can'?t|"
    r"won'?t\s+\w+|fragile|brittle)\b",
    re.I,
)

# LYNCH on open issues: each entry should say "What is the immediate next step
# for resolving the issue?"
NEXT_STEP = re.compile(
    r"\b(?:next\s+step|proposed(?:\s+solution)?|resolution|decide\s+by|owner|"
    r"we\s+will|plan(?:ned)?\s+to|action|ask\s+\w+|spike|prototype|measure|"
    r"benchmark|investigate|defer(?:red)?\s+to)\b",
    re.I,
)

# GOOGLE: "The sweet spot for a larger project seems to be around 10-20ish pages.
# If you get way beyond that, it might make sense to split up the problem."
# ~500 words/page.
# One expression clears it. A floor of 2 was added to stop the metadata line
# this skill RECOMMENDS ("Reversal cost: two-way door") switching the check off
# by itself — but `body_prose` already strips metadata lines, so the floor was
# a second defence against a hazard already closed, and it was doing real harm:
# it turned 15 one-expression documents into failures, and review found most of
# them visibly arguing a trade-off. Measured on the 105: floor 2 → 28 failures,
# floor 1 → 13, and all 13 have literally zero trade-off vocabulary in prose.
MIN_TRADEOFF_HITS = 1

# Characters of prose an alternative must carry beyond its own name.
MIN_JUSTIFICATION = 12

# A leading comment is front matter when it carries at least one of these at
# column zero. An editorial note has no keys; a deploy snippet nests its keys
# under another, so neither qualifies.
FRONT_MATTER_KEYS = {
    "status", "title", "type", "date", "slug", "author", "created", "updated",
    "tickets", "ticket", "owner", "version", "layer", "id",
}

# A heading answers one question per conjunction-separated segment of its title;
# the bound is len(segments), not a constant.

WORDS_PER_PAGE = 500
MAX_PAGES = 20
MIN_WORDS = 250

PLACEHOLDER = re.compile(
    r"^\W*(?:tbd|tba|todo|t\.b\.d\.?|\?+|n/?a|none|unknown|unclear|"
    r"to\s+be\s+(?:decided|determined)|pending|later|\.{3}|—|-)\W*$", re.I)

# Anchored to the start of a line (after optional list/emphasis punctuation).
# Unanchored, "HTTP status: 200 is returned on success." satisfied C2 — the
# check's only blocking arm, discharged by an HTTP code in body prose.
STATUS_LINE = re.compile(
    r"(?:^|[·|])[ \t]{0,8}(?:[-*+]\s*)?[*_`]{0,2}status[*_`]{0,2}\s*[:\-–—]\s*"
    r"([^\n<·|]{1,80})",
    re.I | re.M,
)
# Either a labelled field, or an explicit one-way/two-way door phrase. The bare
# word "door" used to qualify, so a sentence about a literal door satisfied the
# one check `--strict` promotes to blocking.
REVERSAL_LINE = re.compile(
    r"\b(?:reversal[\s-]cost|reversibility|decision[\s-]class)\b"
    r"\s*[:\-–—]?\s*([^\n<·|]{0,60})"
    r"|\b((?:one|two)-?way\s+door[^\n<·|]{0,60})",
    re.I,
)
ONE_WAY = re.compile(r"\bone-?way\b", re.I)
TWO_WAY = re.compile(r"\btwo-?way\b", re.I)
URL_RE = re.compile(r"https?://[^\s<>\"'\)\]]+")


@dataclass
class Section:
    level: int
    title: str
    body: str
    cls: str | None = None
    # Byte offset of this heading in the parsed text. Recorded at parse time
    # because the title is whitespace-collapsed and the text is not, so
    # searching for one inside the other silently fails on any heading
    # containing an inline tag.
    offset: int = -1
    # Every class this heading satisfies. A combined heading — "Goals and
    # non-goals", "Alternatives and drawbacks" — is one section answering two
    # questions, and scoring only the first made the doc fail for a section it
    # actually had. `cls` stays as the primary for reporting.
    classes: tuple[str, ...] = ()
    # Body PLUS every nested subsection, down to the next heading at or above
    # this one's level. Every content check reads `subtree`, never `body`:
    # a doc that puts its SLO numbers under `### Latency` beneath
    # `## Service level objectives` has a section whose own body is empty, and
    # a check that reads `body` would score it as having said nothing.
    subtree: str = ""
    # The subtree with every nested HEADING removed. C6 and C8 read this: an
    # empty `## Trade-offs` heading must not answer the question it poses, but
    # the SLO numbers nested under `### Latency` must still be seen.
    subtree_body: str = ""

    @property
    def items(self) -> list[str]:
        """Bullet items in the section subtree, or paragraphs when it has none."""
        src = self.subtree or self.body
        bullets = [
            re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", ln).strip()
            for ln in src.splitlines()
            if re.match(r"^\s*(?:[-*+]|\d+\.)\s+\S", ln)
        ]
        if bullets:
            return bullets
        return [p.strip() for p in re.split(r"\n\s*\n", src) if p.strip()]


@dataclass
class Finding:
    check: str
    severity: str  # "fail" | "warn"
    message: str
    evidence: str = ""


@dataclass
class Report:
    path: str
    profile: str
    words: int
    sections: dict[str, str] = field(default_factory=dict)
    findings: list[Finding] = field(default_factory=list)

    @property
    def failed(self) -> bool:
        return any(f.severity == "fail" for f in self.findings)


# --------------------------------------------------------------------------
# Parsing. Two entry surfaces — markdown and HTML — and every check runs over
# the same Section list, so neither surface can drift into being unchecked.
# --------------------------------------------------------------------------

# A markdown fence and an HTML <pre> are EXAMPLES, not document structure. Left
# in, a file that is nothing but a fenced sample of a good doc parsed as that
# good doc and passed every check.
FENCE_RE = re.compile(r"(?ms)^[ \t]{0,3}(`{3,}|~{3,})[^\n]*\n.*?^[ \t]{0,3}\1[ \t]*$")

# Typographic quotes are what a word processor, a CMS and most humans actually
# emit. Matching only the ASCII form let "The system shouldn't crash" through
# C4 on the strength of one character.
_QUOTES = (("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'),
           ("\u2032", "'"))


def fold_quotes(s: str) -> str:
    for a, b in _QUOTES:
        s = s.replace(a, b)
    return s


# Case-insensitive (`<!doctype html>` is what this corpus writes) and willing to
# look past a leading provenance note: a document may open with
# `<!-- Broomva workspace · P18 -->` before its metadata block.
LEADING_COMMENTS = re.compile(
    r"(?is)\A\s*(?:<!DOCTYPE[^>]*>\s*)?((?:<!--.*?-->\s*)+)")
ONE_COMMENT = re.compile(r"(?s)<!--(.*?)-->")


def strip_comments(raw: str) -> str:
    """Remove HTML comments, terminated or not.

    `(?s)<!--.*?-->` alone requires a terminator, and HTML5 does not: an
    unterminated `<!--` comments out the rest of the document, which a browser
    honours and which therefore hid every remaining section from a reader while
    leaving them visible to the checker.
    """
    raw = re.sub(r"(?s)<!--.*?-->", " ", raw)
    return re.sub(r"(?s)<!--.*\Z", " ", raw)


def _unsafe_target(url: str) -> str:
    """Name the reason a URL must not be resolved, or "" when it is safe.

    `--check-links` resolves URLs written in the document under review, so it is
    a request forgery primitive unless the destination is constrained: a spec
    could name `http://169.254.169.254/…` and have CI fetch cloud credentials
    for it (CWE-918). Refuses by resolved address, not by hostname text, so
    `localtest.me` and friends cannot spell their way past it.
    """
    import ipaddress
    import socket
    from urllib.parse import urlsplit

    parts = urlsplit(url)
    if parts.scheme not in ("http", "https"):
        return f"non-http scheme ({parts.scheme or 'none'})"
    host = parts.hostname
    if not host:
        return "hostless URL"
    try:
        infos = socket.getaddrinfo(host, None)
    except OSError:
        return ""  # unresolvable: the request below will fail honestly
    for info in infos:
        try:
            ip = ipaddress.ip_address(info[4][0])
        except ValueError:
            continue
        if (ip.is_private or ip.is_loopback or ip.is_link_local
                or ip.is_reserved or ip.is_multicast or ip.is_unspecified):
            return f"private/loopback address ({ip})"
    return ""


def _status_head(val: str) -> str:
    """The bare state word from a status value, emphasis and punctuation removed."""
    return re.split(r"[\s,(]", val.strip().lower().strip("*_`~ "))[0].strip(" .*_`~")


# Level-2 headings that are still part of the header rather than the body. A doc
# may carry its status inside an explicit `## Metadata` block — Lynch's own
# worked example does — and treating the first level-2 heading as the body
# boundary reported that document as having no status at all.
METADATA_HEADINGS = {
    "metadata", "meta", "front matter", "frontmatter", "contents",
    "table of contents", "toc", "about", "document control", "header",
}


def _metadata_region_end(sections: list[Section], text: str) -> int:
    """Offset where the document's header block ends.

    The body starts at the first level-2-or-deeper heading that is not itself a
    metadata block. A document with no such heading is all header.
    """
    for sec in sections:
        if sec.level < 2 or not sec.title:
            continue
        t = re.sub(r"^[\d.\s]+", "", sec.title).strip().lower().rstrip(":")
        t = re.sub(r"[🔗#]", "", t).strip()
        if t in METADATA_HEADINGS:
            continue
        if sec.offset >= 0:
            return sec.offset
        # No recorded offset: fail CLOSED. A region that cannot be located must
        # not silently become the whole document, which is how this check
        # switched itself off on 5 of 105 real files.
        return 0
    return len(text)


def _is_status(val: str) -> bool:
    """Does this value name a state a document could be superseded FROM?

    Matched on the leading hyphen-separated token as well as the whole head, so
    a compound like `draft-for-decision` resolves to `draft` rather than being
    reported as no status at all.
    """
    head = _status_head(val)
    return head in VALID_STATUSES or head.split("-")[0] in VALID_STATUSES


def hoist_front_matter(raw: str) -> str:
    """YAML front matter carried in a leading HTML comment, as plain text.

    This is the carrier P18 names for `.html` artifacts, and the catch-all tag
    strip erases it wholesale. Measured before this existed: 41 of 67 real HTML
    documents in this workspace carried a `status:` field that the checker could
    not see, so much of the corpus calibration was the gate being unable to read
    the format `make-spec` emits rather than the documents being deficient.
    """
    block = LEADING_COMMENTS.search(raw)
    if not block:
        return ""
    # Each leading comment in turn, not just the first: a document may open with
    # a provenance note before its metadata block, and a lazy single-regex
    # "skip up to N" prefers skipping none, so it never looked past comment one.
    for cand in ONE_COMMENT.findall(block.group(1)):
        got = _front_matter_from(cand)
        if got:
            return got
    return ""


def _front_matter_from(comment: str) -> str:
    inner = comment.strip("- \n\t")
    # The discriminator is COLUMN-ZERO keys, not `---` delimiters. This corpus
    # writes undelimited YAML in the comment (`title:` / `date:` / `type:` /
    # `status: approved`), so requiring a fence rejected 12 real documents. It
    # is also the right rule: a deploy snippet nests `status: enabled` UNDER
    # `deploy snippet:`, and an editorial note has no keys at all — accepting
    # any `word:` line anywhere made both of them document metadata.
    # Up to eight columns of indent, matching STATUS_LINE's own tolerance. A
    # column-zero rule rejected 9 real documents whose header comment indents
    # its keys, while the status reader would happily have parsed them — two
    # halves of one feature disagreeing about whether indentation is legal.
    keys = {k.strip().rstrip(": ").lower()
            for k in re.findall(r"^[ \t]{0,8}([A-Za-z][\w-]*)\s*:", inner, re.M)}
    # Key NAMES are conventional; status VALUES are not. That asymmetry is the
    # whole cut: gating on a recognised key name is a closed set that holds,
    # while gating on the value was an open set that produced false failures.
    if not keys & FRONT_MATTER_KEYS:
        return ""
    return inner + "\n"


def _strip_html(raw: str) -> str:
    s = re.sub(r"(?is)<(script|style|svg|head|pre)[^>]*>.*?</\1>", " ", raw)
    # Preserve what later checks read OUT of the markup rather than through it.
    # <code>make check</code> is the HTML spelling of `make check`, and a
    # successor link lives in an href, not in the link text. Dropping both made
    # the two entry surfaces disagree on identical documents.
    s = re.sub(r"(?is)<code[^>]*>(.*?)</code>", r"`\1`", s)
    s = re.sub(r"""(?is)<a[^>]*\shref\s*=\s*["']([^"']+)["'][^>]*>(.*?)</a>""",
               r"\2 (\1)", s)
    s = re.sub(r"(?is)<br\s*/?>", "\n", s)
    # <th> is marked so table_rows can tell a real header from a first data
    # row. Lowering both to "|" made a headerless HTML table lose its first
    # option, which is a C5-thin-alternatives failure on a valid document.
    s = re.sub(r"(?is)</th>", " |\u241f ", s)
    s = re.sub(r"(?is)</td>", " | ", s)
    s = re.sub(r"(?is)</tr>", "\n", s)
    s = re.sub(r"(?is)</(p|div|li|h[1-6]|blockquote|span|strong|em|b|i)>", "\n", s)
    # Leading newline is load-bearing: without it the first <li> of a list is
    # glued to whatever preceded it and parses one indent deeper than its
    # siblings, which silently discarded it as a continuation line.
    s = re.sub(r"(?is)<li[^>]*>", "\n- ", s)
    s = re.sub(r"(?s)<[^>]+>", " ", s)
    for a, b in (("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">"), ("&quot;", '"'),
                 ("&#39;", "'"), ("&nbsp;", " "), ("&mdash;", "—"),
                 ("&ndash;", "–"), ("&hellip;", "…")):
        s = s.replace(a, b)
    # Numeric entities, which hid `Obj&#101;ctive` from the classifier.
    s = re.sub(r"&#(\d{1,5});", lambda m: chr(int(m.group(1))), s)
    s = re.sub(r"&#x([0-9a-fA-F]{1,5});", lambda m: chr(int(m.group(1), 16)), s)
    return s


def parse(raw: str, is_html: bool) -> tuple[list[Section], str]:
    """Return (sections, plain_text). Plain text keeps the front matter."""
    raw = fold_quotes(raw)
    if not is_html:
        raw = FENCE_RE.sub("", raw)
    front = ""
    if is_html:
        # The hoist must run BEFORE comments are stripped, or it rescues nothing.
        front = hoist_front_matter(raw)
    # Comments are stripped on BOTH surfaces, and BEFORE any tag matching.
    # Only-in-HTML meant a markdown doc could hide its non-goals and alternatives
    # in <!-- --> and exit 0; after-the-tag-strip meant the word "<pre>" appearing
    # inside a comment matched the tag stripper and erased every section up to
    # the next real </pre>.
    raw = strip_comments(raw)
    if is_html:
        raw = re.sub(r"(?is)<(script|style|svg|head|pre|template)[^>]*>.*?</\1>",
                     " ", raw)
    if is_html:
        heading_re = re.compile(r"(?is)<h([1-6])[^>]*>(.*?)</h\1>")
        marks: list[tuple[int, int, int, str]] = []
        for m in heading_re.finditer(raw):
            title = _strip_html(m.group(2))
            marks.append((m.start(), m.end(), int(m.group(1)),
                          re.sub(r"\s+", " ", title).strip()))
        sections = []
        base = len(front)
        for i, (_s, e, lvl, title) in enumerate(marks):
            end = marks[i + 1][0] if i + 1 < len(marks) else len(raw)
            sec = Section(lvl, title, _strip_html(raw[e:end]))
            # Offset in TEXT space, not raw space: the two differ by everything
            # the stripper removes, and searching a collapsed title inside
            # uncollapsed text silently failed on any heading with an inline tag.
            sec.offset = base + len(_strip_html(raw[:_s]))
            sections.append(sec)
        # Front matter goes FIRST so it falls inside the metadata region, and
        # the "visible status wins" rule is carried by taking the LAST in-region
        # candidate rather than by text order. Appending it instead put it past
        # the region boundary, where it could not be seen at all.
        return sections, front + _strip_html(raw)

    lines = raw.splitlines()
    sections, cur, buf = [], None, []
    pos = 0
    for ln in lines:
        m = re.match(r"^(#{1,6})\s+(.*\S)\s*$", ln)
        if m:
            if cur:
                cur.body = "\n".join(buf)
                sections.append(cur)
            cur, buf = Section(len(m.group(1)), m.group(2).strip(), ""), []
            cur.offset = pos
        elif cur is not None:
            buf.append(ln)
        pos += len(ln) + 1
    if cur:
        cur.body = "\n".join(buf)
        sections.append(cur)
    return sections, raw


def attach_subtrees(sections: list[Section]) -> None:
    """Fill `subtree` for every section: its own body plus all nested ones."""
    for i, sec in enumerate(sections):
        parts = [sec.body]
        bodies = [sec.body]
        for nxt in sections[i + 1:]:
            if nxt.level <= sec.level:
                break
            parts.append(nxt.title)
            parts.append(nxt.body)
            bodies.append(nxt.body)
        sec.subtree = "\n".join(parts)
        sec.subtree_body = "\n".join(bodies)


def _boundary_before(t: str, i: int) -> bool:
    """True when position `i` starts a word (or the string)."""
    return i == 0 or not (t[i - 1].isalnum() or t[i - 1] == "-")


def _boundary_after(t: str, i: int) -> bool:
    """True when position `i` ends a word (or the string)."""
    return i >= len(t) or not (t[i].isalnum() or t[i] == "-")


def _score_segment(t: str) -> dict[str, int]:
    scored: dict[str, int] = {}
    for cls, names in SECTION_CLASSES.items():
        for name in names:
            if t == name:
                score = 1000
            elif t.endswith(name) and _boundary_before(t, len(t) - len(name)):
                # The head of an English noun phrase is its LAST word: "design
                # goals" is a goals section, not a design section. Ranking
                # suffix above prefix is what separates them.
                #
                # The boundary check is what stops "conflict resolution" being a
                # design section on the strength of "solution", "Oslo" being an
                # acceptance section on "slo", and "…the generic clone was
                # rejected" being an alternatives section.
                score = 700 + len(name)
            elif t.startswith(name) and _boundary_after(t, len(name)):
                score = 500 + len(name)
            elif re.search(rf"\b{re.escape(name)}\b", t):
                score = len(name)
            else:
                continue
            scored[cls] = max(scored.get(cls, 0), score)
    return scored


def classify(sections: Iterable[Section]) -> None:
    """Assign each heading the class(es) it answers.

    A heading may answer two questions — "Goals and non-goals", "Alternatives
    and drawbacks" — so the title is split on an explicit conjunction and each
    SEGMENT is classified on its own. A score floor was tried first and does not
    work: "Design goals and non-goals" starts with "design", so `design` scored
    506 and one heading discharged three required classes. Segmenting gives
    ["design goals", "non-goals"] → goals + non_goals, which is what the heading
    actually says.
    """
    for sec in sections:
        t = re.sub(r"^[\d.\s]+", "", sec.title).strip().lower().rstrip(":")
        t = re.sub(r"[🔗#]", "", t).strip()
        # A comma needs no leading space — "Objective, goals and acceptance
        # criteria" did not split at the comma and lost `objective`, turning the
        # round-2 false negative into a false positive on a doc that has the
        # section.
        segments = [x.strip()
                    for x in re.split(r"\s*[,;]\s*|\s+(?:and|&|/|\+)\s+", t)
                    if x.strip()] or [t]
        picked: dict[str, int] = {}
        for seg in segments:
            best = _score_segment(seg)
            if not best:
                continue
            top = max(best, key=lambda c: best[c])
            picked[top] = max(picked.get(top, 0), best[top])
        if not picked:  # no segment resolved; fall back to the whole title
            picked = _score_segment(t)
        # Bounded by the number of conjunction-separated segments, not a
        # constant: "Objective, goals and acceptance criteria" asks three
        # questions, and a cap of two made the doc fail for a section it has.
        sec.classes = tuple(sorted(picked, key=lambda c: -picked[c])
                            )[:max(1, len(segments))]
        sec.cls = sec.classes[0] if sec.classes else None


TABLE_SEP = re.compile(r"^\s*\|?[\s:|-]*-[\s:|-]*\|?\s*$")


def table_rows(src: str) -> list[tuple[str, str]]:
    """Data rows of a pipe table as (label, blurb), header and rule excluded.

    Both surfaces reach this: `_strip_html` lowers `</td>` to ` | ` and `</tr>`
    to a newline, so an HTML comparison table arrives in the same shape as a
    markdown one. Before that, an HTML table exploded into one line per cell and
    its header row was read as an option — which is how the deleted per-entry
    check earned a precision of 0/2.
    """
    lines = [ln for ln in src.splitlines() if ln.count("|") >= 2]
    if len(lines) < 2:
        return []
    # A header is a markdown separator rule, or an HTML row that carried <th>.
    header_at = next((i for i, ln in enumerate(lines) if "\u241f" in ln), None)
    lines = [ln.replace("\u241f", "") for ln in lines]
    rule_at = next((i for i, ln in enumerate(lines) if TABLE_SEP.match(ln)), None)
    if rule_at is None and header_at is None:
        # Headerless: every row is data.
        out0: list[tuple[str, str]] = []
        for ln in lines:
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            cells = [c for c in cells if c]
            if len(cells) >= 2:
                out0.append((cells[0], " ".join(cells[1:])))
        return out0
    if rule_at is None and header_at is not None:
        lines = lines[header_at:]
    if rule_at is not None:
        # The table begins at its header, one line above the separator rule.
        # Everything before that is prose that happens to contain pipes.
        lines = lines[rule_at - 1:] if rule_at >= 1 else lines
        rule_at = 1 if rule_at >= 1 else rule_at
    out: list[tuple[str, str]] = []
    for i, ln in enumerate(lines):
        if TABLE_SEP.match(ln):
            continue
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        cells = [c for c in cells if c]
        if len(cells) < 2:
            continue
        # The header is row 0 — of the TABLE, which is why the slice above
        # matters. The previous version tested `i == 0` against the section's
        # whole pipe-bearing line list, so a prose line containing two pipes
        # shifted the index and the real header became an option: the exact
        # shape that got the per-entry check deleted for 0/2 precision.
        if i == 0:
            continue
        out.append((cells[0], " ".join(cells[1:])))
    return out


def alternative_entries(sections: list[Section],
                        alts: list[Section]) -> list[tuple[str, str]]:
    """Discrete (label, blurb) pairs for each option the doc considered.

    Two idioms, both real. A bullet list — ``- Redis: another process`` — and
    nested sub-headings, which is what the Little Moments doc uses. Returning
    PAIRS rather than a bag of strings is what lets C5 demand a reason from each
    option instead of from the section as a whole.
    """
    entries: list[tuple[str, str]] = []
    for sec in alts:
        start = next(i for i, x in enumerate(sections) if x is sec)
        subs = []
        for nxt in sections[start + 1:]:
            if nxt.level <= sec.level:
                break
            subs.append(nxt)
        if subs:
            # Only the shallowest nested level names options; anything deeper is
            # detail belonging to the option above it.
            top = min(x.level for x in subs)
            for i, x in enumerate(subs):
                if x.level != top:
                    continue
                blurb = [x.body]
                for y in subs[i + 1:]:
                    if y.level <= top:
                        break
                    blurb += [y.title, y.body]
                entries.append((x.title, "\n".join(blurb)))
            continue
        src = sec.subtree_body or sec.body

        rows = table_rows(src)
        if rows:
            entries += rows
            continue

        # Indentation carries the structure: a top-level bullet names an
        # option, and everything indented under it is that option's blurb.
        bullets: list[tuple[int, str]] = []
        for ln in src.splitlines():
            m = re.match(r"^([ \t]*)(?:[-*+]|\d+\.)\s+(\S.*)$", ln)
            if m:
                bullets.append((len(m.group(1).expandtabs(4)), m.group(2).strip()))
                continue
            # An indented line that is NOT a bullet continues the bullet above
            # it. Dropping these read "- Redis\n  an extra process to operate"
            # as an option with no justification.
            cont = re.match(r"^([ \t]+)(\S.*)$", ln)
            if cont and bullets:
                bullets.append((len(cont.group(1).expandtabs(4)) + 1000,
                                cont.group(2).strip()))
        if bullets:
            base = min(d for d, _ in bullets)  # continuations carry +1000, never the base
            cur: list[str] | None = None
            for depth, txt in bullets:
                if depth <= base:
                    if cur:
                        entries.append((cur[0], "\n".join(cur[1:]) or cur[0]))
                    label, sep, rest = txt.partition(":")
                    if sep and len(label) <= 60:
                        cur = [label.strip(), rest.strip()] if rest.strip() \
                            else [label.strip()]
                    else:
                        # No colon (or a colon so late it is punctuation, not a
                        # label): the option is named by its opening words and
                        # the WHOLE bullet is its blurb. Treating the sentence as
                        # a label stripped the justification off the entry that
                        # contained it.
                        cur = [" ".join(txt.split()[:4]), txt]
                elif cur:
                    cur.append(txt)
            if cur:
                entries.append((cur[0], "\n".join(cur[1:]) or cur[0]))
            continue
        for para in (x.strip() for x in re.split(r"\n\s*\n", src)):
            if len(para) < 4:
                continue
            label, _, rest = para.partition(":")
            entries.append((label.strip()[:60] or para[:40], rest.strip() or para))
    return entries


def prose(secs: list[Section]) -> str:
    """Subtree text with every heading excluded — what the author actually wrote.

    C6 and C8 read this rather than `subtree` so a heading cannot answer the
    question its own section poses (an empty `## Trade-offs` is not a
    trade-off), while nested content — the SLO numbers under `### Latency` —
    still counts.
    """
    return "\n".join(x.subtree_body or x.body for x in secs)


METADATA_LINE = re.compile(
    r"^\s*(?:status|reversal[\s-]cost|reversibility|decision[\s-]class|author|"
    r"created|updated|url|owner|reviewers?|date)\b\s*[:\-–—]", re.I)


def body_prose(sections: list[Section]) -> str:
    """The document's prose: no headings, no metadata lines.

    C9 reads this. Reading the raw text let the `Reversal cost: two-way door`
    line this skill RECOMMENDS satisfy the trade-off detector on its own — a
    gate switched off by its own house style.
    """
    out = []
    for sec in sections:
        for line in sec.body.splitlines():
            if not METADATA_LINE.match(line):
                out.append(line)
    return "\n".join(out)


def infer_profile(path: Path) -> str:
    """Profile from the PATH only.

    An earlier cut downgraded any document under 700 words to `note`, reasoning
    that GOOGLE blesses the "1-3 page mini design doc". That was an automatic
    exemption, and cross-model review found the consequence: a thirteen-word
    implementation manual committing a one-way door exited 0, and the cheapest
    way to pass the gate was to delete words until you crossed the threshold.
    SKILL.md's own anti-rationalization table says "Small is a size, not an
    exemption"; this function used to contradict it.

    `note` is still available and still right for a short design-bearing doc —
    it is now opt-in via `--profile note`, which is a choice someone makes and
    a reviewer can see, rather than a silent property of word count.
    """
    p = str(path).lower()
    if "/adrs/" in p or "-adr-" in p or p.endswith("adr.md"):
        return "adr"
    if "/plans/" in p:
        return "plan"
    if "/rfd" in p or "/rfcs/" in p:
        return "rfd"
    return "spec"


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------

def check(path: Path, profile: str | None, strict: bool,
          check_links: bool) -> Report:
    raw = path.read_text(encoding="utf-8", errors="replace")
    is_html = path.suffix.lower() in (".html", ".htm")
    sections, text = parse(raw, is_html)
    attach_subtrees(sections)
    classify(sections)
    words = len(re.findall(r"\b[\w'-]+\b", text))
    prof = profile or infer_profile(path)
    if prof not in PROFILES:
        raise SystemExit(f"unknown profile {prof!r}; pick from {sorted(PROFILES)}")

    by_cls: dict[str, list[Section]] = {}
    for s in sections:
        for c in (s.classes or ((s.cls,) if s.cls else ())):
            by_cls.setdefault(c, []).append(s)

    rep = Report(str(path), prof, words,
                 {c: "; ".join(s.title for s in v) for c, v in by_cls.items()})
    add = rep.findings.append

    # --- C1 required sections (LYNCH inclusion rule, per-profile) ------------
    for cls in required(prof):
        if cls not in by_cls:
            add(Finding(
                "C1-missing-section", "fail",
                f"profile {prof!r} requires a {cls.replace('_', ' ')} section; "
                f"none of {SECTION_CLASSES[cls][:4]}… matched any heading",
            ))
    for cls in recommended(prof):
        if cls not in by_cls:
            add(Finding(
                "C1-missing-recommended", "warn",
                f"profile {prof!r} recommends a {cls.replace('_', ' ')} section",
            ))

    # --- C2 status (NYGARD supersession, OXIDE state machine) ----------------
    # A status FIELD is metadata, so it must appear in the metadata region —
    # front matter, or the header block before the first section. Anything
    # deeper is prose that happens to contain the word: "- Status: 200 on
    # success" inside a Design section is an HTTP code, not a document state.
    head_end = _metadata_region_end(sections, text)
    # NYGARD's ADR template — the source C2 cites — puts the state under a
    # `## Status` heading, not after a colon. Read that shape too.
    status_sections = [x for x in sections
                       if re.fullmatch(r"\s*status\s*:?\s*", x.title, re.I)
                       and x.body.strip()]
    candidates = [c for c in STATUS_LINE.finditer(text) if c.start() < head_end
                  and not PLACEHOLDER.match(c.group(1).strip())]
    # LAST, not first: front matter leads the text, so a visible `Status:` in
    # the header block comes after it and wins — which is the point. A status
    # hidden in an HTML comment must not shadow one a reader can see.
    m = candidates[-1] if candidates else None
    heading_status = (status_sections[0].body.strip().splitlines()[0]
                      if status_sections else None)
    if m is not None and not _is_status(m.group(1)):
        # Recognised vs unrecognised is a WARN, never the blocking arm. The
        # status vocabulary of a real workspace is open; enumerating it and
        # failing the remainder produced 5 false failures in a sample of 8.
        add(Finding("C2-bad-status", "warn",
                    f"status {_status_head(m.group(1))!r} is outside the known "
                    "state set; supersession checks only run on known states",
                    evidence=m.group(0).strip()[:100]))
    if m is None and heading_status:
        head = _status_head(heading_status)
        if head in STATUS_NEEDS_POINTER and not URL_RE.search(heading_status) \
                and not re.search(r"[\w/.-]+\.(?:md|html)\b", heading_status):
            add(Finding("C2-dangling-supersede", "fail",
                        f"status {head!r} names no successor; NYGARD requires a "
                        "reference to the replacement",
                        evidence=heading_status[:120]))
    elif not m:
        add(Finding("C2-no-status", "fail",
                    "no 'Status:' field; a doc with no state cannot be "
                    "superseded, and a doc that cannot be superseded silently "
                    "becomes a false description of what shipped"))
    else:
        # `m` is already the first candidate whose value names a known state —
        # emphasis stripped by _status_head, so `Status: **superseded**` cannot
        # fall out of the set into a mere warning and skip the pointer check.
        head = _status_head(m.group(1))
        # Supersession enforcement only applies to states we recognise; an
        # unrecognised value already warned above.
        if head in STATUS_NEEDS_POINTER:
            # The successor must be ON the status line. Scanning 400 characters
            # ahead let an unrelated link — an author's homepage two lines down —
            # satisfy the requirement.
            line_end = text.find("\n", m.start())
            line = text[m.start(): line_end if line_end != -1 else len(text)]
            if not (URL_RE.search(line)
                    or re.search(r"\b(?:by|→|->|supersedes?|replaced\s+by)\b"
                                 r"\s*\S{3,}", line, re.I)
                    or re.search(r"[\w/.-]+\.(?:md|html)\b", line)):
                add(Finding("C2-dangling-supersede", "fail",
                            f"status {head!r} names no successor on the status "
                            "line; NYGARD requires a reference to the replacement",
                            evidence=line.strip()[:120]))

    # --- C3 reversal cost declared (LYNCH's inclusion rule, made explicit) ---
    rm = REVERSAL_LINE.search(text)
    rm_val = ((rm.group(1) or rm.group(2) or "") if rm else "")
    if rm is not None and PLACEHOLDER.match(rm_val.strip()):
        rm = None  # "Reversal cost: TBD" answers nothing; treat it as unanswered
    if not rm:
        sev = "fail" if strict else "warn"
        add(Finding("C3-no-reversal-cost", sev,
                    "no reversal-cost / one-way-vs-two-way-door declaration; "
                    "LYNCH's inclusion rule ('what's the penalty for being "
                    "wrong?') is the reason this document exists"))
    elif not (ONE_WAY.search(rm.group(0)) or TWO_WAY.search(rm.group(0))
              or re.search(r"\b(?:high|low|medium|irreversible|cheap|expensive)\b",
                           rm_val, re.I)):
        add(Finding("C3-vague-reversal-cost", "warn",
                    "reversal cost is named but not graded",
                    evidence=rm.group(0).strip()))

    # --- C4 non-goals are not negated goals (GOOGLE) -------------------------
    for sec in by_cls.get("non_goals", []):
        for item in sec.items:
            head = item.strip()
            if not head or len(head) < 8:
                continue
            if NEGATION_HEAD.match(head):
                add(Finding(
                    "C4-negated-goal", "warn",
                    "non-goal reads as a negated requirement, not a goal "
                    "deliberately declined (GOOGLE: non-goals 'aren't negated "
                    "goals like \"The system shouldn't crash\"')",
                    evidence=head[:160]))

    # --- C5 alternatives: >=2, each with a reason (RUST, GOOGLE, LYNCH) ------
    alts = by_cls.get("alternatives", [])
    if alts:
        entries = alternative_entries(sections, alts)
        if len(entries) < 2:
            add(Finding("C5-thin-alternatives", "fail",
                        f"alternatives section names {len(entries)} option(s); "
                        "RUST asks 'what other designs have been considered and "
                        "what is the rationale for not choosing them?' — one "
                        "option is not a comparison"))
        # ONE check, at the only level a script can decide: does the section
        # state, anywhere, why something was NOT chosen?
        #
        # There was a second, per-entry check here — "is this option justified
        # at all, or is it a bare name?" — and it is deleted rather than fixed.
        # Measured precision on its live firings across 105 real documents was
        # 0/2: both were the HEADER ROW of a comparison table ("Alternative |
        # Why rejected"), which is the commonest real idiom for this section and
        # which a structural heuristic cannot distinguish from an option. A rule
        # wrong on every firing it produces is not a rule with a bug. Whether an
        # individual option is argued WELL is rubric R2, which is where a
        # judgement belongs.
        if not REJECTION_MARKERS.search(" ".join(b for _, b in entries)):
            add(Finding("C5-no-rejection-reason", "fail",
                        "no alternative states why it was NOT chosen; a list of "
                        "options with descriptions is a survey, not a rationale"))

    # --- C6 drawbacks of the CHOSEN design (RUST 'Drawbacks', NYGARD) --------
    if "drawbacks" in required(prof) + recommended(prof):
        dsec = by_cls.get("drawbacks", [])
        # Advisory everywhere, not just where the class is recommended. Audited
        # on all 4 live firings: at best 2 are true. Costs are stated in open
        # vocabulary ("far less to build than OpenRaft") and enumerating it is
        # the mistake the status vocabulary already made. Whether the stated
        # consequences are honest is rubric R4.
        sev_d = "warn"
        if dsec and not COST_LANGUAGE.search(prose(dsec)):
            add(Finding("C6-drawbacks-without-cost", sev_d,
                        "drawbacks/consequences section states no cost; NYGARD: "
                        "'All consequences should be listed here, not just the "
                        "positive ones'"))

    # --- C7 open questions carry a next step (LYNCH) ------------------------
    for sec in by_cls.get("open_questions", []):
        body = sec.subtree.strip()
        if not body or re.fullmatch(r"[-*\s]*(none|n/?a|nothing)\.?", body, re.I):
            continue
        if not NEXT_STEP.search(body):
            add(Finding("C7-open-question-without-next-step", "warn",
                        "open questions state no next step; LYNCH requires "
                        "'what is the immediate next step for resolving the "
                        "issue?'", evidence=sec.title))

    # --- C8 acceptance is measurable (LYNCH SLOs) ---------------------------
    if "acceptance" in required(prof) + recommended(prof):
        asec = by_cls.get("acceptance", [])
        sev_a = "fail" if "acceptance" in required(prof) else "warn"
        if asec and not MEASURABLE.search(prose(asec)):
            add(Finding("C8-unmeasurable-acceptance", sev_a,
                        "acceptance/SLO section contains no number, unit or "
                        "runnable command; LYNCH: a well-defined SLO 'prevents "
                        "ambiguity by expressing goals in concrete, objective "
                        "terms'"))

    # --- C9 implementation-manual detector (GOOGLE) -------------------------
    hits = len(TRADEOFF_LANGUAGE.findall(body_prose(sections)))
    if hits < MIN_TRADEOFF_HITS and words > MIN_WORDS:
        add(Finding("C9-implementation-manual", "fail",
                    f"only {hits} trade-off expression(s) in the document's "
                    f"prose, below the floor of {MIN_TRADEOFF_HITS}; GOOGLE: a "
                    "doc that says 'this is how we are going to implement it' "
                    "without trade-offs 'would probably have been a better idea "
                    "to write the actual program right away'"))

    # --- C10 size (GOOGLE 10-20 pages) --------------------------------------
    pages = words / WORDS_PER_PAGE
    if pages > MAX_PAGES:
        add(Finding("C10-oversized", "warn",
                    f"~{pages:.0f} pages ({words} words); GOOGLE puts the sweet "
                    f"spot at 10-20 and suggests splitting the problem beyond it"))
    elif words < MIN_WORDS:
        add(Finding("C10-stub", "warn",
                    f"{words} words — below the {MIN_WORDS}-word floor; this "
                    "reads as a stub, not a design doc"))

    # --- C11 link liveness (opt-in; keeps the default gate hermetic) --------
    if check_links:
        import urllib.error
        import urllib.request
        seen: set[str] = set()
        for url in URL_RE.findall(text):
            url = url.rstrip(".,;:)")
            if url in seen:
                continue
            seen.add(url)
            blocked = _unsafe_target(url)
            if blocked:
                add(Finding("C11-unsafe-link", "fail",
                            f"refusing to resolve a {blocked} target; "
                            "--check-links fetches URLs written in the document "
                            "under review, so it must not be usable to probe "
                            "internal networks", evidence=url))
                continue
            try:
                req = urllib.request.Request(
                    url, method="HEAD",
                    headers={"User-Agent": "spec-check/1.0"})
                urllib.request.urlopen(req, timeout=8)
            except urllib.error.HTTPError as exc:
                if exc.code in (403, 405, 429):
                    continue  # blocked to bots, not dead
                add(Finding("C11-dead-link", "fail",
                            f"link returns HTTP {exc.code}", evidence=url))
            except Exception as exc:  # noqa: BLE001 - network shapes vary
                add(Finding("C11-dead-link", "warn",
                            f"link unreachable: {type(exc).__name__}",
                            evidence=url))

    return rep


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def render(rep: Report) -> str:
    out = [f"{rep.path}  [profile={rep.profile} words={rep.words} "
           f"classes={len(rep.sections)}/{len(SECTION_CLASSES)}]"]
    if not rep.findings:
        out.append("  ok — every required check passed")
    for f in sorted(rep.findings, key=lambda x: (x.severity != "fail", x.check)):
        mark = "FAIL" if f.severity == "fail" else "warn"
        out.append(f"  [{mark}] {f.check}: {f.message}")
        if f.evidence:
            out.append(f"         ↳ {f.evidence}")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="spec_check", description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docs", nargs="+", type=Path)
    ap.add_argument("--profile", choices=sorted(PROFILES),
                    help="override the profile inferred from the path")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true",
                    help="promote the reversal-cost warning to a failure")
    ap.add_argument("--check-links", action="store_true",
                    help="resolve every http(s) URL (network; off by default)")
    ns = ap.parse_args(argv)

    reports = []
    for doc in ns.docs:
        if not doc.is_file():
            what = "is a directory" if doc.is_dir() else "no such file"
            print(f"spec_check: {what}: {doc}", file=sys.stderr)
            return 2
        reports.append(check(doc, ns.profile, ns.strict, ns.check_links))

    if ns.json:
        print(json.dumps([asdict(r) for r in reports], indent=2))
    else:
        print("\n\n".join(render(r) for r in reports))
        bad = sum(1 for r in reports if r.failed)
        if len(reports) > 1:
            print(f"\n{len(reports) - bad}/{len(reports)} documents pass")

    return 1 if any(r.failed for r in reports) else 0


if __name__ == "__main__":
    sys.exit(main())
