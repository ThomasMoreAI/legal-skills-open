#!/usr/bin/env python3
"""
eligibility_intake.py - build a structured ancestry-and-documents worksheet for a
European citizenship-by-descent / restitution case, from the Israeli side.

This does NOT decide eligibility and contains no legal thresholds or country
rules (those live in SKILL.md and change often). It only organizes the family
chain and produces a starting document checklist the user can take to the
relevant consulate or a lawyer.

Usage:
    python eligibility_intake.py            # interactive if a TTY, else blank
    python eligibility_intake.py --blank    # print an empty worksheet to fill in
    python eligibility_intake.py --interactive   # force the prompts even with no TTY
    python eligibility_intake.py --case case.json  # fill the worksheet from a file
    python eligibility_intake.py --anchor "paternal grandfather" --origin Poland ...

An agent harness usually runs this with stdin closed, so the old TTY sniff
silently downgraded every run to --blank and the worksheet was never filled.
Pass --case / the per-field flags (preferred for agents), or --interactive.
"""

import argparse
import json
import sys

GENERIC_DOCS = [
    "Anchor ancestor's birth certificate (or archival birth record)",
    "Anchor ancestor's marriage certificate (if relevant to the chain)",
    "Anchor ancestor's proof of emigration / loss or denial of citizenship "
    "(ship manifest, naturalization file, expulsion or persecution record, "
    "Yad Vashem or national-archive reference)",
    "Each intermediate link's birth and marriage certificates (unbroken chain)",
    "Your own birth certificate",
    "Your Israeli population-registry extract (tamtzit rishum, standard or extended)",
    "Your valid Israeli passport / teudat zehut",
    "Name-equivalence (same-person) notarized affidavit if any name is spelled "
    "differently across documents",
]

NEXT_STEPS = [
    "Identify the candidate route(s) by matching the family story to the country "
    "table in SKILL.md (a family can qualify under more than one).",
    "For each document above, determine the correct Israeli apostille authority "
    "(courts / Ministry of Justice channel for notarized and court documents; "
    "Ministry of Foreign Affairs for other public documents).",
    "Confirm the destination country's translation rule: an Israeli notarial "
    "translation, or a sworn/court translator registered in that country.",
    "Check the relevant consulate's current published requirements and timeline.",
    "For a contested lineage or a broken chain, consult a licensed immigration "
    "lawyer before filing.",
]


def field(label):
    try:
        return input(f"{label}: ").strip()
    except EOFError:
        return ""


FIELDS = ["anchor", "origin", "residence", "story", "docs_have", "chain", "prior_filing"]

PROMPTS = {
    "anchor": "Anchor ancestor (name + relationship, e.g. 'paternal grandfather')",
    "origin": "Their country/region of origin",
    "residence": "Where they LIVED 1933-1945 (city, country), separately from citizenship",
    "story": "What happened and when (emigration / flight / persecution / loss of citizenship + dates)",
    "docs_have": "Documents you already have (comma-separated)",
    "chain": "Living chain from the ancestor to you (each birth/marriage/name change)",
    "prior_filing": "Any prior filing, booked consular appointment or court case, and its date",
}


def render(case):
    print("== Ancestry and documents worksheet ==\n")
    anchor = case.get("anchor", "")
    origin = case.get("origin", "")
    residence = case.get("residence", "")
    story = case.get("story", "")
    docs_have = case.get("docs_have", "")
    chain = case.get("chain", "")
    prior = case.get("prior_filing", "")

    print("\n----------------------------------------")
    print("CASE SUMMARY")
    print("----------------------------------------")
    print(f"Anchor ancestor : {anchor or '(fill in)'}")
    print(f"Origin          : {origin or '(fill in)'}")
    print(f"Residence 33-45 : {residence or '(fill in)'}")
    print(f"Family story    : {story or '(fill in)'}")
    print(f"Documents on hand: {docs_have or '(none listed)'}")
    print(f"Chain           : {chain or '(fill in)'}")
    print(f"Prior filing    : {prior or '(none reported)'}")

    print("\n----------------------------------------")
    print("STARTING DOCUMENT CHECKLIST (generic - refine per route)")
    print("----------------------------------------")
    for i, d in enumerate(GENERIC_DOCS, 1):
        print(f"  [ ] {i}. {d}")

    print("\n----------------------------------------")
    print("NEXT STEPS")
    print("----------------------------------------")
    for i, s in enumerate(NEXT_STEPS, 1):
        print(f"  {i}. {s}")
    print("\nNote: this worksheet does not determine eligibility. Confirm every "
          "route-specific rule with the consulate or a licensed lawyer.")


def run_blank():
    print("== Ancestry and documents worksheet (blank) ==\n")
    for label in [
        "Anchor ancestor (name + relationship)",
        "Country/region of origin",
        "Where they lived 1933-1945 (city, country)",
        "What happened and when",
        "Documents you already have",
        "Living chain from the ancestor to you",
        "Any prior filing, booked appointment or court case, and its date",
    ]:
        print(f"{label}:\n    ____________________\n")
    print("Starting document checklist:")
    for i, d in enumerate(GENERIC_DOCS, 1):
        print(f"  [ ] {i}. {d}")


def load_case(path):
    """Read a --case file, failing with a readable message instead of a traceback."""
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
    except OSError as e:
        sys.exit(f"error: cannot read case file {path}: {e.strerror}")
    except json.JSONDecodeError as e:
        sys.exit(f"error: {path} is not valid JSON (line {e.lineno}, column {e.colno})")
    if not isinstance(data, dict):
        sys.exit(f"error: {path} must hold a JSON object with keys: {', '.join(FIELDS)}")
    unknown = sorted(k for k in data if k not in FIELDS)
    if unknown:
        print(f"warning: ignoring unknown keys {unknown}; expected: {', '.join(FIELDS)}",
              file=sys.stderr)
    case = {}
    for f in FIELDS:
        v = data.get(f)
        if isinstance(v, list):
            v = ", ".join(str(x) for x in v)
        if v not in (None, ""):
            case[f] = str(v)
    if not case:
        sys.exit(f"error: {path} has no recognised field; expected: {', '.join(FIELDS)}")
    return case


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--blank", action="store_true", help="print an empty worksheet")
    p.add_argument("--interactive", action="store_true",
                   help="force the interactive prompts even when stdin is not a TTY")
    p.add_argument("--case", help="path to a JSON file with the worksheet fields")
    for f in FIELDS:
        p.add_argument("--" + f.replace("_", "-"), dest=f, default=None)
    args = p.parse_args()

    case = load_case(args.case) if args.case else {}
    for f in FIELDS:
        if getattr(args, f):
            case[f] = getattr(args, f)

    if args.blank:
        run_blank()
    elif case:
        render(case)
    elif args.interactive:
        for f in FIELDS:
            case[f] = field(PROMPTS[f])
        render(case)
    elif sys.stdin.isatty():
        for f in FIELDS:
            case[f] = field(PROMPTS[f])
        render(case)
    else:
        run_blank()


if __name__ == "__main__":
    main()
