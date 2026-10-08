#!/usr/bin/env python3
"""bar_bench.py — Score answers against the NY bar-style benchmark bank.

Loads the bundled question sets (MBE-, NYLE-, MPRE-, MEE-style) plus any local
overlay, grades an answer file, and reports per component against the proxy
pass marks, with remediation targets naming the reference file that should
have carried each missed rule.

Usage:
  python3 bar_bench.py stats
  python3 bar_bench.py list --component nyle          # exam mode: no answers
  python3 bar_bench.py template > answers.json
  python3 bar_bench.py score answers.json [--json]
  python3 bar_bench.py key --set mpre
  python3 bar_bench.py sources

Answer file: {"MBE-CP-001": "C", ..., "MEE-TORT-001": 7.5}
Essay answers are rubric scores out of 10 (from a grader); absent = ungraded.

Overlays (licensed NCBE banks, project-applied sets) — never commit them here:
  .claude/bar-benchmark/questions/  under the working directory
  BAR_BENCHMARK_QUESTIONS=dir1:dir2
  --questions <dir>                  repeatable
An overlay item whose id matches a bundled one replaces it.
"""

import argparse
import json
import os
import sys
from pathlib import Path

QDIR = Path(__file__).resolve().parent.parent / "benchmark" / "questions"

# Proxy pass marks, deliberately above the real ones (MBE ≈60–65% raw, NYLE 60%,
# MPRE scaled 85) because the bundled bank is self-authored. Not predictive.
PASS = {"mbe": 70.0, "nyle": 75.0, "mpre": 80.0, "mee": 70.0}
# UBE weights MBE 50 / MEE 30 / MPT 20. There is no MPT here, so the proxy
# renormalises MBE:MEE to 62.5:37.5 and gates NYLE and MPRE separately, as NY does.
UBE_W = {"mbe": 0.625, "mee": 0.375}
COMPONENTS = ["mbe", "mee", "nyle", "mpre"]


def question_dirs(extra):
    dirs = [QDIR]
    auto = Path.cwd() / ".claude" / "bar-benchmark" / "questions"
    if auto.exists():
        print(f"note: loading project overlay questions from {auto}", file=sys.stderr)
        dirs.append(auto)
    for d in os.environ.get("BAR_BENCHMARK_QUESTIONS", "").split(":"):
        if d.strip():
            dirs.append(Path(d.strip()).resolve())
    dirs += [Path(d).resolve() for d in extra or []]
    out, seen = [], set()
    for d in dirs:
        if d in seen:
            continue
        seen.add(d)
        if d.exists():
            out.append(d)
        else:
            print(f"warning: question directory not found, skipping: {d}", file=sys.stderr)
    return out


def load(args):
    """Return (sets, questions) after overlay resolution and filters."""
    sets, by_id = [], {}
    for d in question_dirs(args.questions):
        for f in sorted(d.glob("*.json")):
            try:
                s = json.loads(f.read_text())
            except (OSError, ValueError) as e:
                raise SystemExit(f"error: cannot read {f}: {e}")
            src = "bundled" if d == QDIR else str(d)
            sets.append({"set": s["set"], "n": len(s["questions"]), "source": src})
            if args.set and s["set"] != args.set:
                continue
            for q in s["questions"]:
                q = {**q, "set": s["set"], "component": s.get("component", "mbe"),
                     "jurisdiction": s.get("jurisdiction", "multistate"), "source": src}
                if args.component and q["component"] != args.component:
                    continue
                if args.subject and args.subject.lower() not in q["subject"].lower():
                    continue
                by_id[q["id"]] = q
    return sets, list(by_id.values())


def grade(q, given):
    if given in (None, ""):
        return None if q["type"] == "essay" else False
    if q["type"] == "essay":
        try:
            return max(0.0, min(10.0, float(given)))
        except (TypeError, ValueError):
            return None
    return str(given).strip().upper()[:1] == str(q["answer"]).upper()


def pct(n, d):
    return round(100.0 * n / d, 1) if d else 0.0


def score(qs, answers):
    comp, missed, ungraded = {}, [], []
    for q in qs:
        r = grade(q, answers.get(q["id"]))
        c = comp.setdefault(q["component"], {"right": 0.0, "n": 0, "subjects": {}})
        sub = c["subjects"].setdefault(q["subject"], [0.0, 0])
        if q["type"] == "essay":
            if r is None:
                ungraded.append(q["id"])
                continue
            c["right"] += r / 10.0
            sub[0] += r / 10.0
        else:
            c["right"] += 1 if r else 0
            sub[0] += 1 if r else 0
            if not r:
                missed.append({"id": q["id"], "subject": q["subject"], "area": q.get("area", ""),
                               "given": answers.get(q["id"]), "answer": q["answer"],
                               "cite": q.get("cite", ""), "ref": q.get("ref", "")})
        c["n"] += 1
        sub[1] += 1
    report = {"components": {}, "missed": missed, "ungraded_essays": ungraded}
    for k, c in comp.items():
        p = pct(c["right"], c["n"])
        report["components"][k] = {
            "score": p, "n": c["n"], "pass_mark": PASS[k], "pass": p >= PASS[k],
            "by_subject": {s: pct(a, b) for s, (a, b) in sorted(c["subjects"].items())}}
    comps = report["components"]
    if all(k in comps and comps[k]["n"] for k in UBE_W):
        report["ube_proxy"] = round(sum(comps[k]["score"] * w for k, w in UBE_W.items()), 1)
    report["overall_pass"] = bool(comps) and all(v["pass"] for v in comps.values())
    return report


def print_report(rep):
    line = "═" * 70
    print(line)
    print("  NY BAR BENCHMARK (proxy — self-authored bank; not a bar-passage prediction)")
    print(line)
    for k in COMPONENTS:
        v = rep["components"].get(k)
        if not v:
            continue
        mark = "PASS" if v["pass"] else "FAIL"
        print(f"\n  {k.upper():5} {v['score']:5.1f}%  n={v['n']:<4} {mark} (mark {v['pass_mark']:.0f})")
        for s, p in v["by_subject"].items():
            bar = "█" * round(p / 5) + "░" * (20 - round(p / 5))
            print(f"        {bar} {p:5.1f}%  {s}")
    if "ube_proxy" in rep:
        print(f"\n  UBE-weighted proxy (MBE:MEE 62.5:37.5): {rep['ube_proxy']}%")
    if rep["ungraded_essays"]:
        print(f"\n  Ungraded essays: {', '.join(rep['ungraded_essays'])}")
    if rep["missed"]:
        print(f"\n  Missed ({len(rep['missed'])}) — remediation targets")
        for m in rep["missed"]:
            print(f"    ✗ {m['id']:<14} got {m['given']!s:<3} key {m['answer']}  "
                  f"[{m['subject']} · {m['area']}]  → reference/{m['ref']}")
    print(f"\n  OVERALL: {'PASS' if rep['overall_pass'] else 'FAIL'}")


def main():
    ap = argparse.ArgumentParser(description="Score and inspect the NY bar-style benchmark bank.")
    ap.add_argument("cmd", choices=["stats", "list", "template", "key", "score", "sources"],
                    help="what to do")
    ap.add_argument("answers", nargs="?", help="answer JSON file (score only)")
    ap.add_argument("--set", help="restrict to one set name")
    ap.add_argument("--component", choices=COMPONENTS, help="restrict to one component")
    ap.add_argument("--subject", help="restrict to subjects containing this text")
    ap.add_argument("--questions", action="append", help="extra overlay directory (repeatable)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    sets, qs = load(args)
    if args.cmd == "score":
        if not args.answers:
            print("error: score needs an answers file", file=sys.stderr)
            return 2
        try:
            answers = json.loads(Path(args.answers).read_text())
        except (OSError, ValueError) as e:
            print(f"error: cannot read answers: {e}", file=sys.stderr)
            return 2
        rep = score(qs, answers)
        print(json.dumps(rep, indent=2)) if args.json else print_report(rep)
        return 0 if rep["overall_pass"] else 1

    if args.cmd == "stats":
        agg = {}
        for q in qs:
            agg.setdefault(q["component"], {}).setdefault(q["subject"], 0)
            agg[q["component"]][q["subject"]] += 1
        if args.json:
            print(json.dumps({"total": len(qs), "by_component": agg}, indent=2))
        else:
            print(f"Total items: {len(qs)}")
            for c in COMPONENTS:
                if c in agg:
                    print(f"\n{c.upper()} ({sum(agg[c].values())})")
                    for s, n in sorted(agg[c].items(), key=lambda x: -x[1]):
                        print(f"  {n:4}  {s}")
        return 0

    if args.cmd == "sources":
        out = {"dirs": [str(d) for d in question_dirs(args.questions)], "sets": sets}
        if args.json:
            print(json.dumps(out, indent=2))
        else:
            for s in sets:
                print(f"  {s['n']:4}  {s['set']:<32} {s['source']}")
            print(f"  {len(qs):4}  total after id resolution")
        return 0

    if args.cmd == "template":
        print(json.dumps({q["id"]: "" for q in qs}, indent=2))
        return 0

    if args.cmd == "list":
        if args.json:
            print(json.dumps([{k: q[k] for k in ("id", "component", "subject", "type", "q", "choices")
                               if k in q} for q in qs], indent=2))
            return 0
        for q in qs:
            print(f"## {q['id']}  [{q['component'].upper()} · {q['subject']} · {q['type']}]")
            print(q["q"])
            for k, v in (q.get("choices") or {}).items():
                print(f"   {k}. {v}")
            print()
        return 0

    # key
    for q in qs:
        ans = q.get("answer", "(essay — see rubric)")
        print(f"{q['id']}  →  {ans}\n    cite: {q.get('cite', '')}\n    why:  {q.get('why', q.get('model_answer', ''))[:400]}\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyError as e:
        print(f"error: question file missing field {e}", file=sys.stderr)
        sys.exit(2)
