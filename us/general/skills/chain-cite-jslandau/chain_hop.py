#!/usr/bin/env python3
"""
chain_hop.py — mechanical helper for chain-cite.

Two subcommands reflect the skill's Haiku vs. Sonnet split:

  page     Given an opinion JSON file on disk, extract the pincite page's full
           text and return it along with a list of sentence-level chunks. The
           caller (a Sonnet subagent) then picks which sentence carries the
           proposition being traced — a semantic judgment, not a lexical one.
           This subcommand does NO scoring: semantic relevance is not something
           regex can decide.

  anchors  Given an opinion JSON file and a chosen sentence from its
           html_with_citations field, return the outbound citation anchors found
           in or immediately after that sentence. Mechanical regex work —
           Haiku-tier.

Both subcommands emit JSON on stdout.

The script no longer fetches from CourtListener. The skill is responsible for
fetching the opinion via the CourtListener MCP (preferred) or REST API
(fallback) and writing the JSON to a file, then passing the path here with
``--opinion-json``. This keeps the script free of auth/network concerns and
makes it trivially testable with stub fixtures.
"""
import argparse
import json
import os
import re
import sys

# ---------------------------------------------------------------------------
# Load opinion JSON
# ---------------------------------------------------------------------------

def load_opinion(path):
    with open(path) as f:
        return json.load(f)


def pick_text(op):
    """Prefer html_with_citations (retains anchor tags), then plain_text, then html."""
    for k in ("html_with_citations", "plain_text", "html"):
        v = op.get(k) or ""
        if v.strip():
            return k, v
    return None, ""


def strip_tags(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------------------
# Page-span extraction
# ---------------------------------------------------------------------------

PAGE_MARKER_RE = re.compile(
    # Known pagination conventions across CourtListener ingests:
    #   *N                   — Harvard CAP star-pagination in html_with_citations / plain_text
    #   label="N"            — xml_harvard star-pagination attributes
    #   page-label="N"       — variant XML attribute form
    #   \fN                  — form-feed followed by page number; slip-opinion pagination
    #                          from court-direct ingests (SCOTUS slips, circuit en banc PDFs).
    #                          NOTE: \f-paginated text often uses *slip* pagination, not the
    #                          reporter (F.3d / U.S.) pagination the brief cites by. Use the
    #                          `citation-toolkit` upfront pagination-mode detection to decide
    #                          whether this opinion's markers correspond to the brief's cite.
    r'\*(\d+)\b|label="(\d+)"|page-label="(\d+)"|\f(\d+)\b'
)


def find_page_span(text, pincite):
    """Return (start, end) character offsets of the pincite page.

    Start = index of the page marker for this pincite; end = index of the next
    page marker (of any number) after it. No scoring — this is a filter, not a
    judgment about where on the page the relevant passage sits.

    Tries each pagination convention in order. Returns (None, None) if no
    convention finds the page; the caller (the skill, not this script) is
    responsible for falling through to whole-opinion semantic search per the
    match-ladder in citation-toolkit.
    """
    if pincite is None:
        return None, None
    patterns = [
        fr"\*{pincite}\b",
        fr'label="{pincite}"',
        fr'page-label="{pincite}"',
        fr"\f{pincite}\b",
    ]
    start = None
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            start = m.start()
            break
    if start is None:
        return None, None
    next_m = PAGE_MARKER_RE.search(text, start + 10)
    end = next_m.start() if next_m else len(text)
    return start, end


# ---------------------------------------------------------------------------
# Sentence chunking
# ---------------------------------------------------------------------------

SENTENCE_SPLIT_RE = re.compile(
    # Split on ., ?, or ! followed by whitespace and a capital letter or quote.
    # Legal text has lots of "v." and "U.S." and "§" — this is best-effort, not perfect.
    r'(?<=[.!?])(?=\s+(?:[A-Z"\'\u201C\u2018]|\d))',
)


def chunk_sentences(plain_text):
    """Split plain (tag-stripped) page text into sentence-level chunks.

    Returns a list of dicts: {"index": i, "text": s}. Chunks shorter than 20
    characters are merged with the following chunk so "See id., at 280." style
    fragments don't fragment the output.
    """
    raw = [s.strip() for s in SENTENCE_SPLIT_RE.split(plain_text) if s.strip()]
    merged = []
    buf = ""
    for s in raw:
        if buf:
            s = buf + " " + s
            buf = ""
        if len(s) < 20:
            buf = s
            continue
        merged.append(s)
    if buf:
        if merged:
            merged[-1] = merged[-1] + " " + buf
        else:
            merged.append(buf)
    return [{"index": i, "text": s} for i, s in enumerate(merged)]


# ---------------------------------------------------------------------------
# Anchor extraction (mechanical, Haiku-tier)
# ---------------------------------------------------------------------------

CITATION_ANCHOR_RE = re.compile(
    r'<span[^>]*class="citation[^"]*"[^>]*data-id="(\d+)"[^>]*>\s*'
    r'<a[^>]*href="(/opinion/(\d+)/[^"#]*(?:#(\d+))?)"[^>]*>([^<]+)</a>\s*</span>',
    re.DOTALL,
)

NOLINK_CITATION_RE = re.compile(
    r'<span[^>]*class="citation no-link"[^>]*>([^<]+)</span>'
)


def extract_anchors(html, start, end):
    """Find citation anchors within html[start:end]."""
    seg = html[start:end]
    results = []
    for m in CITATION_ANCHOR_RE.finditer(seg):
        results.append({
            "cluster_data_id": m.group(1),
            "href": m.group(2),
            "opinion_id": int(m.group(3)),
            "pincite_page": int(m.group(4)) if m.group(4) else None,
            "text": m.group(5).strip(),
            "offset_in_segment": m.start(),
        })
    for m in NOLINK_CITATION_RE.finditer(seg):
        results.append({
            "cluster_data_id": None,
            "href": None,
            "opinion_id": None,
            "pincite_page": None,
            "text": m.group(1).strip(),
            "offset_in_segment": m.start(),
            "no_link": True,
        })
    results.sort(key=lambda r: r["offset_in_segment"])
    return results


def classify_non_case_citation(text):
    """Return a chain-cite terminal reason if the citation text names a non-case source, else None."""
    t = text.lower()
    if "u. s. c." in t or "u.s.c." in t:
        return "cites_statute"
    if "c. f. r." in t or "c.f.r." in t or "fed. reg." in t:
        return "cites_statute"
    if "fed. r." in t:
        return "cites_statute"
    if "restatement" in t:
        return "cites_restatement"
    if "const." in t or "constitution" in t:
        return "cites_constitution"
    return None


# ---------------------------------------------------------------------------
# Subcommand: page
# ---------------------------------------------------------------------------

def cmd_page(args):
    op = load_opinion(args.opinion_json)
    opinion_id = op.get("id")
    field, text = pick_text(op)
    if not text:
        print(json.dumps({"error": "no_text_fields_populated", "keys": list(op.keys())}))
        return

    page_start, page_end = find_page_span(text, args.pincite)
    if page_start is None:
        # No page marker found — return the whole opinion plain text, caller can fall back
        out = {
            "opinion_id": opinion_id,
            "field_used": field,
            "pincite": args.pincite,
            "page_marker_found": False,
            "note": (
                f"Page marker for pincite={args.pincite} not found in {field}. "
                "Caller should either retry without --pincite (returns whole opinion) "
                "or use CourtListener's page-specific lookup."
            ),
            "full_text": strip_tags(text)[: args.max_chars],
        }
        print(json.dumps(out, indent=2))
        return

    page_html = text[page_start:page_end]
    page_plain = strip_tags(page_html)
    sentences = chunk_sentences(page_plain)

    out = {
        "opinion_id": opinion_id,
        "field_used": field,
        "pincite": args.pincite,
        "page_marker_found": True,
        "page_start_offset": page_start,
        "page_end_offset": page_end,
        "page_length_chars": page_end - page_start,
        "page_plain_text": page_plain,
        "sentences": sentences,
        "usage_note": (
            "This output is the raw pincite page. The caller (a Sonnet-tier subagent) "
            "should compare the proposition being traced against each sentence and pick the "
            "one that carries the same rule — a semantic judgment. The script does NOT score "
            "or rank passages. Once a sentence is chosen, call `chain_hop.py anchors` with "
            "the chosen sentence's substring (passed as --sentence) to extract outbound "
            "citations."
        ),
    }
    print(json.dumps(out, indent=2))


# ---------------------------------------------------------------------------
# Subcommand: anchors
# ---------------------------------------------------------------------------

def cmd_anchors(args):
    op = load_opinion(args.opinion_json)
    opinion_id = op.get("id")
    field, text = pick_text(op)
    if field != "html_with_citations":
        print(json.dumps({
            "error": "anchors subcommand requires html_with_citations field",
            "field_available": field,
        }))
        return

    # Locate the chosen sentence in the HTML. We match on the first ~80 chars of the
    # tag-stripped sentence — should uniquely identify the passage on the page.
    needle_plain = re.sub(r"\s+", " ", args.sentence.strip())[: args.needle_chars]
    # Build a tolerant regex: allow tags between words.
    words = [re.escape(w) for w in needle_plain.split() if w]
    if not words:
        print(json.dumps({"error": "empty sentence"}))
        return
    tolerant = r"(?:<[^>]+>|\s)*".join(words)
    m = re.search(tolerant, text, flags=re.IGNORECASE)
    if not m:
        print(json.dumps({
            "error": "sentence_not_found_in_html",
            "needle": needle_plain,
            "hint": "Pass a verbatim fragment (80+ chars) drawn from the page_plain_text output of the `page` subcommand.",
        }))
        return

    sentence_start = m.start()
    # Grab a generous window after the sentence so string cites are captured.
    scan_end = min(len(text), m.end() + args.forward_chars)
    anchors = extract_anchors(text, sentence_start, scan_end)

    visited = {int(x) for x in args.visited.split(",") if x.strip()} if args.visited else set()

    cycles, usable, non_case = [], [], []
    for a in anchors:
        if a.get("no_link"):
            tr = classify_non_case_citation(a["text"])
            if tr:
                non_case.append({**a, "terminal_reason": tr})
            continue
        oid = a["opinion_id"]
        if oid in visited:
            cycles.append(a)
            continue
        usable.append(a)

    out = {
        "opinion_id": opinion_id,
        "sentence_found_at": sentence_start,
        "sentence_end": m.end(),
        "scan_window_end": scan_end,
        "anchors_in_window": anchors,
        "usable_case_anchors": usable,
        "non_case_anchors": non_case,
        "cycle_anchors": cycles,
    }

    if usable:
        out["next_hop"] = usable[0]
        out["siblings"] = usable[1:]
    elif non_case:
        out["terminal_reason"] = non_case[0]["terminal_reason"]
        out["terminal_citation"] = non_case[0]["text"]
    elif cycles:
        out["terminal_reason"] = "cycle_detected"
        out["cycle_target"] = cycles[0]["opinion_id"]
    else:
        out["terminal_reason"] = "no_outbound_for_proposition"

    print(json.dumps(out, indent=2))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="chain-cite mechanical helper")
    sub = p.add_subparsers(dest="cmd", required=True)

    pp = sub.add_parser("page", help="Extract pincite page text from an opinion JSON file")
    pp.add_argument("--opinion-json", required=True,
                    help="Path to opinion JSON file (fetched by the skill via the CourtListener MCP or REST API). "
                         "Must contain at least one of: html_with_citations, plain_text, html.")
    pp.add_argument("--pincite", type=int, default=None)
    pp.add_argument("--max-chars", type=int, default=30000,
                    help="Max chars to return when no page marker is found (whole-opinion fallback)")
    pp.set_defaults(func=cmd_page)

    pa = sub.add_parser("anchors", help="Extract outbound citation anchors after a chosen sentence")
    pa.add_argument("--opinion-json", required=True,
                    help="Path to opinion JSON file. Must contain html_with_citations.")
    pa.add_argument("--sentence", required=True,
                    help="The verbatim sentence/passage selected by the Sonnet step. "
                         "First ~80 chars are used as a tolerant needle against html_with_citations.")
    pa.add_argument("--visited", default="",
                    help="Comma-separated opinion IDs already in the chain (for cycle detection)")
    pa.add_argument("--forward-chars", type=int, default=1500,
                    help="How far past the sentence to scan for anchored string cites")
    pa.add_argument("--needle-chars", type=int, default=120)
    pa.set_defaults(func=cmd_anchors)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
