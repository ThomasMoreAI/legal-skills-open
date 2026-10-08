#!/usr/bin/env python3
"""validate_bank.py — Structural lint for the bar-benchmark question bank.

Checks every question file for: required fields, unique ids across sets,
exactly four choices A–D on MCQs, a key that is one of them, a cite and a
why, essay rubrics summing to 10, a `ref` that exists in legal-doctrine's
reference folder, per-file answer-letter balance, and answer text leaked
verbatim into the stem.

Usage:
  python3 validate_bank.py                 # bundled bank
  python3 validate_bank.py --dir <path>    # an overlay directory
  python3 validate_bank.py --json

Exit 0 clean (warnings allowed), 1 on errors, 2 on unreadable input.
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
QDIR = HERE / "benchmark" / "questions"
REFDIR = HERE.parent / "legal-doctrine" / "reference"
COMPONENTS = {"mbe", "nyle", "mpre", "mee"}
TYPES = {"mcq", "essay"}
DIFF = {"remember", "application", "analysis"}


def check_file(path, seen, refs):
    errs, warns = [], []
    try:
        s = json.loads(path.read_text())
    except (OSError, ValueError) as e:
        return [f"{path.name}: unreadable JSON ({e})"], []
    for k in ("set", "title", "component", "questions"):
        if k not in s:
            errs.append(f"{path.name}: set missing '{k}'")
    if s.get("component") not in COMPONENTS:
        errs.append(f"{path.name}: component must be one of {sorted(COMPONENTS)}")
    letters = Counter()
    for q in s.get("questions", []):
        qid = q.get("id", "?")
        where = f"{path.name}:{qid}"
        if qid in seen:
            errs.append(f"{where}: duplicate id (also in {seen[qid]})")
        seen[qid] = path.name
        for k in ("id", "subject", "type", "q", "cite", "ref"):
            if not q.get(k):
                errs.append(f"{where}: missing '{k}'")
        if q.get("type") not in TYPES:
            errs.append(f"{where}: type must be mcq or essay")
        if q.get("difficulty") and q["difficulty"] not in DIFF:
            warns.append(f"{where}: unknown difficulty '{q['difficulty']}'")
        if refs is not None and q.get("ref") and q["ref"] not in refs:
            errs.append(f"{where}: ref '{q['ref']}' not found in legal-doctrine/reference/")
        if q.get("type") == "mcq":
            ch = q.get("choices") or {}
            if sorted(ch) != ["A", "B", "C", "D"]:
                errs.append(f"{where}: MCQ needs exactly choices A–D")
            if q.get("answer") not in ch:
                errs.append(f"{where}: answer '{q.get('answer')}' is not a choice")
            if not q.get("why"):
                errs.append(f"{where}: missing 'why'")
            letters[q.get("answer")] += 1
            text = ch.get(q.get("answer"), "")
            if len(text) > 25 and text.lower() in q.get("q", "").lower():
                warns.append(f"{where}: correct choice text appears verbatim in the stem")
            if any(v.strip().lower() in ("all of the above", "none of the above") for v in ch.values()):
                errs.append(f"{where}: all/none-of-the-above choice")
        elif q.get("type") == "essay":
            rub = q.get("rubric") or []
            tot = sum(p.get("weight", 0) for p in rub)
            if abs(tot - 10) > 1e-6:
                errs.append(f"{where}: rubric weights sum to {tot}, need 10")
            if not q.get("model_answer"):
                errs.append(f"{where}: essay missing model_answer")
    n = sum(letters.values())
    if n >= 8:
        for L in "ABCD":
            share = letters.get(L, 0) / n
            if share < 0.12 or share > 0.38:
                warns.append(f"{path.name}: answer letter {L} is {share:.0%} of keys (target 20–30%)")
    return errs, warns


def main():
    ap = argparse.ArgumentParser(description="Lint the bar-benchmark question bank.")
    ap.add_argument("--dir", action="append", help="question directory (default: bundled bank)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()
    dirs = [Path(d) for d in args.dir] if args.dir else [QDIR]
    refs = {p.name for p in REFDIR.glob("*.md")} if REFDIR.exists() else None
    errs, warns, seen, files = [], [], {}, 0
    for d in dirs:
        if not d.is_dir():
            print(f"error: not a directory: {d}", file=sys.stderr)
            return 2
        for f in sorted(d.glob("*.json")):
            files += 1
            e, w = check_file(f, seen, refs)
            errs += e
            warns += w
    out = {"files": files, "items": len(seen), "errors": errs, "warnings": warns}
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"{files} files, {len(seen)} items: {len(errs)} errors, {len(warns)} warnings")
        for e in errs:
            print(f"  ERROR  {e}")
        for w in warns:
            print(f"  warn   {w}")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
