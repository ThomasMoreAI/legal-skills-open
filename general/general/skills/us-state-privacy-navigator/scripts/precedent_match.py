#!/usr/bin/env python3
"""
precedent_match.py — Given a gap (or a list of gaps), return the most analogous
enforcement actions from the structured corpus in
references/enforcement_actions.json.

Usage:
    # CLI lookup by violation theory tag
    python precedent_match.py --tag gpc_not_honored

    # CLI lookup by free-text query (matched against violation theories,
    # factual patterns, and statutes)
    python precedent_match.py --query "session replay wiretap"

    # JSON in, JSON out (for orchestrated calls from a memo generator)
    python precedent_match.py --gaps gaps.json --output precedents.json

Input format for --gaps:
    [
      {"id": "01", "tags": ["gpc_not_honored", "no_donotsell_link"], "states": ["CA"]},
      {"id": "02", "tags": ["sensitive_data_no_consent"], "states": ["CO", "CT"]}
    ]

Output: For each gap, the top N matching actions ranked by:
    1. Tag overlap (intersection of gap.tags with action.violation_theories).
    2. State match (action regulator/statute matches an applicable state).
    3. Recency (newer actions weighted slightly higher).
    4. Headline severity (settlement size, presence of injunctive remedies).

This script is deterministic. It does not call an LLM. The corpus is loaded
once and ranked with a transparent scoring function.

Part of the us-state-privacy-navigator skill.
"""

import argparse
import json
import os
import re
import sys
from typing import Any


# ---------------------------------------------------------------------------
# Corpus loading
# ---------------------------------------------------------------------------


def load_corpus(path: str | None = None) -> dict:
    if path is None:
        here = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(here, "..", "references", "enforcement_actions.json")
    with open(path, "r") as f:
        return json.load(f)


def state_match(action: dict, gap_states: list[str]) -> bool:
    """Determine whether an action's regulator or statutes touch a gap-state."""
    if not gap_states:
        return False
    text = " ".join([
        " ".join(action.get("regulator", [])),
        " ".join(action.get("statutes", [])),
    ]).lower()
    state_terms = {
        "CA": ("california", "cal.", "cppa", "cipa"),
        "VA": ("virginia", "va.",),
        "CO": ("colorado", "colo.",),
        "CT": ("connecticut", "conn.",),
        "UT": ("utah",),
        "TX": ("texas", "tex.",),
        "OR": ("oregon", "or.",),
        "MT": ("montana", "mont.",),
        "FL": ("florida", "fla.",),
        "IA": ("iowa",),
        "DE": ("delaware", "del.",),
        "NJ": ("new jersey", "n.j.",),
        "NH": ("new hampshire", "n.h.",),
        "NE": ("nebraska", "neb.",),
        "MN": ("minnesota", "minn.",),
        "MD": ("maryland", "md.",),
        "TN": ("tennessee", "tenn.",),
        "IN": ("indiana", "ind.",),
        "KY": ("kentucky", "ky.",),
        "RI": ("rhode island", "r.i.",),
        "IL": ("illinois", "ill.", "bipa"),
        "WA": ("washington", "wash.", "mhmda"),
    }
    for s in gap_states:
        for term in state_terms.get(s.upper(), ()):
            if term in text:
                return True
    return False


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------


def score(action: dict, gap_tags: set[str], gap_states: list[str], current_year: int = 2026) -> tuple[int, dict]:
    """Compute a transparent score for ranking. Returns (score, breakdown)."""
    breakdown = {}

    # 1. Tag overlap is the dominant signal — 100 points per overlapping tag.
    action_tags = set(action.get("violation_theories", []))
    overlap = gap_tags & action_tags
    tag_score = 100 * len(overlap)
    breakdown["tag_overlap"] = list(overlap)
    breakdown["tag_score"] = tag_score

    # 2. State proximity — 35 points if a regulator/statute matches any gap state.
    state_score = 35 if state_match(action, gap_states) else 0
    breakdown["state_score"] = state_score

    # 3. Recency — newer actions slightly more useful as analogs (max 20 points,
    #    decaying linearly across a 10-year window).
    year = action.get("year") or 2018
    recency_score = max(0, 20 - 2 * (current_year - year))
    breakdown["recency_score"] = recency_score

    # 4. Severity — present where settlement amount is large or injunctive
    #    remedies are imposed. Capped at 25 points.
    amt = action.get("monetary_amount_usd") or 0
    if amt >= 1_000_000_000:
        severity_score = 25
    elif amt >= 100_000_000:
        severity_score = 20
    elif amt >= 10_000_000:
        severity_score = 15
    elif amt >= 1_000_000:
        severity_score = 10
    elif amt > 0:
        severity_score = 5
    else:
        severity_score = 0
    if action.get("remediation_imposed"):
        severity_score = min(25, severity_score + 5)
    breakdown["severity_score"] = severity_score

    total = tag_score + state_score + recency_score + severity_score
    return total, breakdown


def rank_actions(corpus: dict, gap_tags: set[str], gap_states: list[str], top_n: int = 5) -> list[dict]:
    actions = corpus.get("actions", [])
    scored = []
    for a in actions:
        s, b = score(a, gap_tags, gap_states)
        if s == 0:
            continue
        scored.append({
            "id": a.get("id"),
            "case_name": a.get("case_name"),
            "year": a.get("year"),
            "regulator": a.get("regulator"),
            "respondent": a.get("respondent"),
            "factual_pattern": a.get("factual_pattern"),
            "monetary_amount_usd": a.get("monetary_amount_usd"),
            "violation_theories": a.get("violation_theories"),
            "operational_lessons": a.get("operational_lessons", []),
            "citation": a.get("citation"),
            "url": a.get("url"),
            "score": s,
            "breakdown": b,
        })
    scored.sort(key=lambda r: r["score"], reverse=True)
    return scored[:top_n]


# ---------------------------------------------------------------------------
# Free-text query (fallback when no tag is provided)
# ---------------------------------------------------------------------------


def text_query(corpus: dict, query: str, top_n: int = 5) -> list[dict]:
    """Lower-precision string match across action text fields."""
    q_terms = [t for t in re.split(r"\W+", query.lower()) if len(t) >= 3]
    results = []
    for a in corpus.get("actions", []):
        haystack = " ".join([
            a.get("case_name", ""),
            a.get("factual_pattern", ""),
            " ".join(a.get("violation_theories", [])),
            " ".join(a.get("statutes", [])),
            " ".join(a.get("operational_lessons", [])),
        ]).lower()
        hits = sum(1 for t in q_terms if t in haystack)
        if hits == 0:
            continue
        results.append({
            "id": a.get("id"),
            "case_name": a.get("case_name"),
            "year": a.get("year"),
            "monetary_amount_usd": a.get("monetary_amount_usd"),
            "factual_pattern": a.get("factual_pattern"),
            "violation_theories": a.get("violation_theories"),
            "operational_lessons": a.get("operational_lessons", []),
            "citation": a.get("citation"),
            "score": hits,
        })
    results.sort(key=lambda r: r["score"], reverse=True)
    return results[:top_n]


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def main() -> int:
    p = argparse.ArgumentParser(description="Match gaps to analogous enforcement actions.")
    p.add_argument("--corpus", help="Path to enforcement_actions.json. Defaults to skill location.")
    p.add_argument("--tag", action="append", default=[], help="Violation theory tag (repeatable).")
    p.add_argument("--state", action="append", default=[], help="Applicable state (repeatable).")
    p.add_argument("--query", help="Free-text query (used when no --tag is provided).")
    p.add_argument("--gaps", help="Path to a JSON file containing a list of gap objects.")
    p.add_argument("--top", type=int, default=5, help="Top-N matches per gap.")
    p.add_argument("--output", help="Optional output JSON path.")
    args = p.parse_args()

    corpus = load_corpus(args.corpus)

    if args.gaps:
        with open(args.gaps, "r") as f:
            gaps = json.load(f)
        out: dict[str, Any] = {"matches": []}
        for g in gaps:
            tags = set(g.get("tags", []))
            states = g.get("states", [])
            ranked = rank_actions(corpus, tags, states, top_n=args.top)
            out["matches"].append({
                "gap_id": g.get("id"),
                "tags": list(tags),
                "states": states,
                "matches": ranked,
            })
    elif args.tag:
        tags = set(args.tag)
        states = args.state
        out = {"tags": list(tags), "states": states, "matches": rank_actions(corpus, tags, states, top_n=args.top)}
    elif args.query:
        out = {"query": args.query, "matches": text_query(corpus, args.query, top_n=args.top)}
    else:
        p.error("Provide --tag (one or more), --query, or --gaps.")

    text = json.dumps(out, indent=2, default=str)
    if args.output:
        with open(args.output, "w") as f:
            f.write(text)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
