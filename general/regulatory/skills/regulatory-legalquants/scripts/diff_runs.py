#!/usr/bin/env python3
"""
diff_runs.py — compare two extractions of the same instrument and report what
moved, filtered to the provisions a note actually rested on.

This is `refresh`. There is no model in it, on purpose: a reported change has to be
a fact about the bytes, so that "the provision behind your answer on territorial
scope has moved" can never turn out to be sampling variance wearing a diff's
clothing.

Where a provision moved, it reports the words that moved. A hash says a section
changed; on a US code section of a thousand words that is close to no
information, and the recorded consequence is that the agent reads both source
texts itself and paraphrases the amendment into the note — where no quote check
can reach it. The words are in the extraction already, and `difflib` is
deterministic, so the comparison hands over the before and after rather than
leaving them to be re-derived by the one component that must never author text.

It does not try to follow a provision to its new home after a renumbering. When
a consolidation shifts everything down by one, the honest report is a column of
orphans and a column of replacements — not a confident and wrong claim that
Article 9 was amended, when in truth Article 9 was repealed and Article 10 moved
into its number. That distinction is drawn mechanically, from the heading:

    amended     the id is in both, the words moved, the heading did not
    retitled    the heading changed over a body that was kept — the citation
                still points at the provision, under a name that is out of date
    replaced    the heading changed and the body did not survive — the citation
                now points at a different provision
    added       the id is only in the later run
    removed     the id is only in the earlier run

`replaced` is the dangerous one and the reason the heading is compared at all. A
note that cites Article 9 does not fail after a renumber; it silently starts
citing something else.

It is also the one that must not be claimed on a heading alone. A publisher that
recaptions a section changes the heading over the same law, and reporting that
as a replacement tells the lawyer to go looking for a repeal that never
happened. Once the body is compared the two are separable, so they are separated
here rather than left for the reader to overrule.

Usage:
    python3 diff_runs.py <earlier>/provisions.json <later>/provisions.json
    python3 diff_runs.py <earlier>/provisions.json <later>/provisions.json \
        --manifest <earlier>/run.json
    python3 diff_runs.py ... --json delta.json

Exit 0 nothing moved. Exit 1 something moved. Exit 2 the comparison could not
be made.

Stdlib only.
"""

from __future__ import annotations

import argparse
import json
import sys
from difflib import SequenceMatcher
from pathlib import Path

# The same normalisation the hash is taken over. Diffing the stored text instead
# would put the two halves of this script at odds: a publisher's re-wrap moves
# no words the hash can see, so it must move no words the report can see either.
from extract_provisions import canonical
from integrity import IntegrityError, require_same_instrument, validate_extraction

CHANGED = ("amended", "retitled", "replaced", "added", "removed")

# How much of the body has to survive for a changed heading to be a recaption
# rather than a replacement. The measurement is not delicate — a recaptioned
# section scores near 1 and a number that has been reused scores near 0 — so the
# line sits in the empty middle, where it decides nothing on its own.
KEPT = 0.5

# Enough of the sentence to place the change and to quote it. Runs closer
# together than STITCH are one change — an amendment that swaps a department's
# name twice in a clause is one edit to a lawyer, not three.
CONTEXT = 6
STITCH = 5

# Printed per provision. A wholesale rewrite is a real result, but scrolling it
# is not, and the complete set is always in --json.
MAX_SHOWN = 8

HEADLINE = {
    "amended": "amended",
    "retitled": "retitled — the heading changed over a body that was kept",
    "replaced": "REPLACED — this number now holds a different provision",
    "added": "new",
    "removed": "gone from the instrument",
}


def die(message: str) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(2)


def load(path: Path) -> dict:
    if not path.exists():
        die(f"No such file: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        die(f"{path} is not readable as JSON: {error}")
    if not payload.get("provisions"):
        die(f"{path} carries no provisions.")
    return payload


def index(payload: dict) -> dict[str, dict]:
    return {p["id"]: p for p in payload["provisions"]}


def describe(payload: dict) -> str:
    """Where this extraction came from, and when. The dates are the product."""
    provenance = payload.get("provenance")
    if not provenance:
        return "no provenance recorded — this extraction cannot say what it is"

    fetch = provenance.get("fetch", {})
    parts = [fetch.get("final_url") or fetch.get("requested_url") or "unknown source"]
    if fetch.get("retrieved_at"):
        parts.append(f"retrieved {fetch['retrieved_at']}")
    if fetch.get("http_date"):
        parts.append(f"publisher date {fetch['http_date']}")

    version = provenance.get("version") or {}
    labels = [f.get("marker") for f in version.get("findings", []) if f.get("marker")]
    if labels:
        parts.append("version markers: " + ", ".join(labels))
    if provenance.get("extracted_over_failed_version_check"):
        parts.append("EXTRACTED OVER A FAILED VERSION CHECK")
    return " | ".join(parts)


def fragment(words: list[str], start: int, stop: int) -> str:
    """A changed run with enough either side of it to be placed and quoted."""
    left, right = max(0, start - CONTEXT), min(len(words), stop + CONTEXT)
    body = " ".join(words[left:right])
    return f"{'… ' if left else ''}{body}{' …' if right < len(words) else ''}"


def word_changes(before: str, after: str) -> list[dict]:
    """The words that moved, over the same form the hash was taken over.

    An insertion has an empty `was` run and a deletion an empty `now` one; both
    still carry their context, because where a clause was added is the question
    a lawyer asks next.
    """
    old, new = canonical(before).split(), canonical(after).split()
    matcher = SequenceMatcher(None, old, new, autojunk=False)
    merged: list[list[int]] = []
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        if merged and i1 - merged[-1][1] <= STITCH:
            merged[-1][1], merged[-1][3] = i2, j2
        else:
            merged.append([i1, i2, j1, j2])
    return [
        {"was": fragment(old, i1, i2), "now": fragment(new, j1, j2)}
        for i1, i2, j1, j2 in merged
    ]


def kept(before: str, after: str) -> float:
    """How much of the body survived, over the form the hash was taken over."""
    old, new = canonical(before).split(), canonical(after).split()
    if not old and not new:
        return 1.0
    return SequenceMatcher(None, old, new, autojunk=False).ratio()


def verdict(before: dict, after: dict, comparable: bool) -> str:
    """Amended, retitled or replaced — decided from the body, not the heading.

    Without both texts the body cannot be read, so a changed heading keeps the
    conservative verdict. `replaced` overstated is a wasted re-read; understated
    it is a citation that quietly resolves to different law.
    """
    if (before["heading"] or "").strip() == (after["heading"] or "").strip():
        return "amended"
    if comparable and kept(before["text"], after["text"]) >= KEPT:
        return "retitled"
    return "replaced"


def term_changes(earlier: dict, later: dict) -> list[dict]:
    """Definitions that appeared, moved or went, from the extractor's own index.

    A new definition reaches every provision that uses the term, including the
    provisions whose own words did not move — so it is the one amendment a word
    diff cannot show, because in those provisions there is nothing to show. The
    index is built at extraction and was never read here.
    """
    before = earlier.get("defined_terms") or {}
    after = later.get("defined_terms") or {}
    changes = []
    for term in sorted({*before, *after}):
        was, now = before.get(term), after.get(term)
        if was == now:
            continue
        changes.append(
            {
                "term": term,
                "status": "newly defined"
                if was is None
                else "no longer defined"
                if now is None
                else "defined elsewhere",
                "provisions": now or was,
                "provisions_was": was if was is not None and now is not None else None,
            }
        )
    return changes


def compare(earlier: dict[str, dict], later: dict[str, dict]) -> list[dict]:
    findings = []
    for id_, before in earlier.items():
        after = later.get(id_)
        if after is None:
            findings.append(
                {
                    "id": id_,
                    "status": "removed",
                    "label": before["label"],
                    "heading": before["heading"],
                }
            )
        elif after["sha256"] != before["sha256"]:
            comparable = "text" in before and "text" in after
            finding = {
                "id": id_,
                "status": verdict(before, after, comparable),
                "label": after["label"],
                "heading": after["heading"],
                "heading_was": before["heading"],
                "sha256_was": before["sha256"],
                "sha256": after["sha256"],
            }
            if comparable:
                finding["changes"] = word_changes(before["text"], after["text"])
            findings.append(finding)
        else:
            findings.append(
                {
                    "id": id_,
                    "status": "unchanged",
                    "label": after["label"],
                    "heading": after["heading"],
                }
            )
    for id_, after in later.items():
        if id_ not in earlier:
            findings.append(
                {
                    "id": id_,
                    "status": "added",
                    "label": after["label"],
                    "heading": after["heading"],
                }
            )
    return findings


def load_manifest(path: Path, before: dict) -> tuple[list[str], list[str]]:
    if not path.exists():
        die(f"No such manifest: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("integrity") != before.get("integrity"):
        die("The earlier manifest no longer matches the earlier extraction.")
    recorded = payload.get("provision_set") or []
    actual = [
        {
            key: provision.get(key)
            for key in ("id", "label", "heading", "class", "sha256")
        }
        for provision in before["provisions"]
    ]
    if recorded != actual:
        die(
            "The earlier manifest does not preserve the complete earlier provision set."
        )
    quoted = [entry["id"] for entry in payload.get("quoted", [])]
    dependencies = [entry["id"] for entry in payload.get("semantic_dependencies", [])]
    if not quoted and not dependencies:
        die(f"{path} names no quoted provisions or semantic dependencies.")
    return quoted, dependencies


def words_moved(finding: dict) -> str:
    """The before and after, ready to be quoted rather than described."""
    changes = finding.get("changes")
    if changes is None:
        return (
            "      words not compared — one of these runs was extracted with "
            "--no-text\n      and carries hashes only"
        )
    shown = []
    for change in changes[:MAX_SHOWN]:
        shown.append(f"      was  {change['was']}")
        shown.append(f"      now  {change['now']}")
        shown.append("")
    if len(changes) > MAX_SHOWN:
        shown.append(
            f"      ... and {len(changes) - MAX_SHOWN} more changes; --json "
            "carries all of them"
        )
    return "\n".join(shown).rstrip()


def line(finding: dict) -> str:
    label = finding["label"] or finding["id"]
    heading = f" — {finding['heading']}" if finding.get("heading") else ""
    text = f"  {label}{heading}: {HEADLINE[finding['status']]}"
    if finding["status"] in ("retitled", "replaced"):
        text += f"\n      was: {finding['heading_was'] or '(no heading)'}"
    if finding["status"] in ("amended", "retitled", "replaced"):
        text += "\n" + words_moved(finding)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("earlier", type=Path)
    parser.add_argument("later", type=Path)
    parser.add_argument(
        "--manifest",
        type=Path,
        help="run.json from the earlier run; filters the report",
    )
    parser.add_argument("--json", type=Path, help="write the delta")
    args = parser.parse_args()

    before, after = load(args.earlier), load(args.later)
    try:
        before_integrity = validate_extraction(before, args.earlier.parent)
        after_integrity = validate_extraction(after, args.later.parent)
        require_same_instrument(before_integrity, after_integrity)
    except IntegrityError as error:
        die(str(error))
    findings = compare(index(before), index(after))
    changed = [f for f in findings if f["status"] in CHANGED]

    quoted, dependencies = (
        load_manifest(args.manifest, before) if args.manifest else ([], [])
    )
    highlighted = sorted({*quoted, *dependencies})
    missing = [id_ for id_ in highlighted if id_ not in {f["id"] for f in findings}]
    if missing:
        die(
            f"The manifest names provisions that are in neither run: "
            f"{', '.join(missing)}.\n"
            "  These runs are not two extractions of the same instrument."
        )

    print(f"earlier  {describe(before)}")
    print(f"later    {describe(after)}\n")

    if highlighted:
        relevant = [f for f in changed if f["id"] in highlighted]
        print(
            f"Previously quoted or identified as a semantic dependency "
            f"({len(highlighted)} provisions)"
        )
        if relevant:
            for finding in relevant:
                print(line(finding))
        else:
            print("  none of these provisions changed")
        print()

        others = [f for f in changed if f["id"] not in highlighted]
        if others:
            print("Other changes in the complete preserved provision set")
            for finding in others:
                print(line(finding))
            print()
    elif changed:
        for finding in changed:
            print(line(finding))
        print()

    terms = term_changes(before, after)
    if terms:
        print("Defined terms")
        for change in terms:
            where = ", ".join(change["provisions"])
            moved = (
                f" (was {', '.join(change['provisions_was'])})"
                if change["provisions_was"]
                else ""
            )
            print(f"  '{change['term']}' — {change['status']}: {where}{moved}")
        print(
            "  A definition reaches every provision that uses the term, including\n"
            "  ones whose own words did not move and are reported unchanged above.\n"
            "  Read those before concluding the earlier answer survives.\n"
        )

    tally = {}
    for finding in findings:
        tally[finding["status"]] = tally.get(finding["status"], 0) + 1
    print("  ".join(f"{count} {name}" for name, count in sorted(tally.items())))

    if any(f["status"] == "retitled" for f in changed):
        print(
            "\nAt least one heading changed over a body that was kept. The earlier\n"
            "note's citation still points at that provision — but the heading it\n"
            "names the provision by is now the publisher's old one."
        )

    if any(f["status"] == "replaced" for f in changed):
        print(
            "\nAt least one number now holds a different provision. Every citation\n"
            "to it in the earlier note points somewhere new — re-read those before\n"
            "anything else, and do not assume the old provision was amended. It may\n"
            "have been repealed while its neighbours moved up."
        )

    if args.json:
        args.json.write_text(
            json.dumps(
                {
                    "earlier": str(args.earlier),
                    "later": str(args.later),
                    "quoted": quoted,
                    "semantic_dependencies": dependencies,
                    "defined_terms": terms,
                    "findings": findings,
                },
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

    if changed:
        print(
            "\nThis compares words, not meaning. It reports exactly which words\n"
            "moved; whether the move matters is the lawyer's call, and a change\n"
            "that reads as tidying may not be."
        )
        return 1
    print(
        "\nNo preserved provision text changed. This does not establish that the "
        "earlier legal conclusion remains valid."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
