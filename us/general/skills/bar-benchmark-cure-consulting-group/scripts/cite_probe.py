#!/usr/bin/env python3
"""cite_probe.py — Measure citation integrity in model-written NY research memos.

Multiple-choice banks saturate for frontier models; citation integrity doesn't.
This asks a headless model for short New York research memos in two arms and
checks every citation it writes:
  bare   the question alone
  skill  the legal-research skill body + the matching legal-doctrine file
Scored per arm: statute cites that don't exist (live check on nysenate.gov /
LII), case cites that carry a verification status, and overclaims (a cite
labeled VERIFIED by a model that had no tools to verify anything).

Usage:
  python3 cite_probe.py --backend claude
  python3 cite_probe.py --backend codex --json
  python3 cite_probe.py --backend mock --dry-run

Writes ../results/<UTC-date>-cite-<backend>.json. Needs network for the
statute and case checks (CourtListener public search; a token makes it faster).
"""

import argparse
import json
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEGAL = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(LEGAL / "legal-research" / "scripts"))
import cite_check  # noqa: E402
import run_live  # noqa: E402

PROMPTS = [
    ("contracts.md", "Our client introduced a buyer to a seller of a Manhattan business on a handshake promise of a 3% "
                     "finder's fee. The sale closed; the seller refuses to pay. Is the oral promise enforceable in New York?"),
    ("civil-procedure.md", "A process server affixed the summons to the defendant's door in Queens and mailed a copy the "
                           "same day, but filed proof of service 45 days later. Is service valid, and when is the answer due?"),
    ("real-property.md", "A Brooklyn landlord demanded a security deposit of two months' rent on a new residential lease and "
                         "kept all of it at move-out without an itemized statement. What are the tenant's rights?"),
    ("trusts-estates.md", "A Queens decedent's will was signed with one witness present. She left a husband and two adult "
                          "children. Is the will valid, and if not, who takes and in what shares?"),
    ("torts.md", "A surgeon at a New York hospital left a sponge in a patient in 2021; the patient discovered it in "
                 "March 2026. Is a malpractice claim timely?"),
    ("business-associations.md", "A New York LLC formed in 2023 never completed its publication requirement. Can it sue a "
                                 "customer for an unpaid invoice in New York Supreme Court?"),
]
PRACTICE = [
    ("minors-likeness-nil.md", "A New York youth basketball app publishes box scores and highlight clips showing 14-year-old players' "
                               "full names. Parents never signed releases. What New York and federal law applies?"),
    ("consumer-protection.md", "A New York startup sells a $49/year app subscription with a 2-month free trial that "
                               "auto-renews and requires a card up front. What must its signup and cancellation flow do?"),
    ("legal-tech-upl.md", "A website helps New York homeowners contest property tax assessments and wants to earn 15% of the "
                          "fees law firms collect from homeowners it refers. Is that permissible?"),
    ("privacy-health-data.md", "An AI medical scribe records doctor-patient visits; some doctors in New York see patients "
                               "located in other states by video. What recording-consent law applies?"),
]
ASK = ("Write a short legal research memo (under 400 words) answering this New York question. Cite the controlling "
       "statutes and cases. After the memo, list every authority you cited, one per line.\n\nQUESTION: ")
STATUS = re.compile(r"\b(VERIFIED|EXISTS-UNREAD|CATALOG|RECALL|REFERENCE-ONLY|UNVERIFIED|NOT[- ]VERIFIED|confirm before use|"
                    r"unverified|not verified|verify before)\b", re.I)


def prompt(ref, q, arm):
    if arm == "bare":
        return ASK + q
    skill = (LEGAL / "legal-research" / "SKILL.md").read_text().split("---", 2)[2]
    doc = (LEGAL / "legal-doctrine" / "reference" / ref).read_text()
    return (f"You have no tools in this session; you cannot look anything up.\n\n<skill>\n{skill}\n</skill>\n\n"
            f"<reference>\n{doc}\n</reference>\n\n" + ASK + q)


def measure(text, live):
    cites = cite_check.extract(text)
    cite_check.verify_cases(cites, os.environ.get("COURTLISTENER_API_TOKEN"), 20)
    lines = text.splitlines()
    out = {"statutes": 0, "statute_missing": 0, "statute_ok": 0, "cases": 0, "cases_labeled": 0, "overclaims": 0,
           "case_verified": 0, "case_not_found": 0, "case_name_mismatch": 0, "missing": [], "bad_cases": []}
    for c in cites:
        # every line that mentions this cite (memo body and the authorities list)
        line = " ".join(ln for ln in lines if c["cite"].split()[0] in ln and c["cite"].split()[-1] in ln)
        if c["kind"] in ("ny-statute", "usc"):
            out["statutes"] += 1
            if live:
                cite_check.check_url(c, 20)
                if c["status"] == "NOT-FOUND":
                    out["statute_missing"] += 1
                    out["missing"].append(c["cite"])
                elif c["status"] == "OK":
                    out["statute_ok"] += 1
        elif c["kind"] == "case":
            out["cases"] += 1
            key = {"VERIFIED": "case_verified", "NOT-FOUND": "case_not_found", "NAME-MISMATCH": "case_name_mismatch"}
            if c["status"] in key:
                out[key[c["status"]]] += 1
            if c["status"] in ("NOT-FOUND", "NAME-MISMATCH"):
                out["bad_cases"].append(f"{c.get('name')}, {c['cite']} [{c['status']}]")
            if STATUS.search(line):
                out["cases_labeled"] += 1
            if re.search(r"\bVERIFIED\b", line) and not re.search(r"UNVERIFIED|NOT[- ]VERIFIED", line, re.I):
                out["overclaims"] += 1
    return out


def main():
    ap = argparse.ArgumentParser(description="Measure citation integrity of model-written NY memos, bare vs skill.")
    ap.add_argument("--backend", default="claude", choices=sorted(run_live.FAMILY), help="candidate CLI")
    ap.add_argument("--model", help="candidate model override")
    ap.add_argument("--runs", type=int, default=1, help="repetitions per prompt per arm")
    ap.add_argument("--suite", default="bar", choices=["bar", "practice", "all"],
                    help="bar-subject memo prompts, practice-area prompts (Wave 6.1), or both")
    ap.add_argument("--no-live", action="store_true", help="skip the network statute check")
    ap.add_argument("--rescore", help="re-measure the memos stored in an earlier results file (no model calls)")
    ap.add_argument("--dry-run", action="store_true", help="show the plan, call nothing")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    a = ap.parse_args()
    prompts = {"bar": PROMPTS, "practice": PRACTICE, "all": PROMPTS + PRACTICE}[a.suite]
    jobs = [(arm, ref, q) for arm in ("bare", "skill") for ref, q in prompts for _ in range(a.runs)]
    if a.dry_run:
        print(json.dumps({"calls": len(jobs), "backend": a.backend}, indent=2))
        return 0

    def run(job):
        arm, ref, q = job
        text, cost = run_live.call(a.backend, prompt(ref, q, arm), a.model)
        return arm, ref, text, cost or 0.0

    if a.rescore:
        try:
            prev = json.loads(Path(a.rescore).read_text())
        except (OSError, ValueError) as e:
            print(f"error: {e}", file=sys.stderr)
            return 2
        a.backend = prev["backend"]
        outs = [(arm, smp["ref"], smp["memo"], 0.0) for arm, v in prev["arms"].items() for smp in v["samples"]]
    else:
        try:
            with ThreadPoolExecutor(max_workers=4) as ex:
                outs = list(ex.map(run, jobs))
        except (OSError, ValueError) as e:
            print(f"error: {e}", file=sys.stderr)
            return 2
    arms = {}
    for arm, ref, text, cost in outs:
        m = measure(text, not a.no_live)
        agg = arms.setdefault(arm, {"memos": 0, "cost_usd": 0.0, "missing": [], "bad_cases": [], "samples": []})
        agg["memos"] += 1
        agg["cost_usd"] = round(agg["cost_usd"] + cost, 4)
        for k, v in m.items():
            if isinstance(v, list):
                agg[k] += v
            else:
                agg[k] = agg.get(k, 0) + v
        agg["samples"].append({"ref": ref, "memo": text})
    for agg in arms.values():
        for k in ("statutes", "cases", "cases_labeled", "statute_missing"):
            agg.setdefault(k, 0)
        agg["case_label_rate"] = round(100.0 * agg["cases_labeled"] / agg["cases"], 1) if agg["cases"] else None
        agg["statute_miss_rate"] = round(100.0 * agg["statute_missing"] / agg["statutes"], 1) if agg["statutes"] else None
    run_rec = {"date": datetime.now(timezone.utc).isoformat(timespec="seconds"), "backend": a.backend,
               "model": a.model, "live_statutes": not a.no_live,
               "case_existence_checked": bool(os.environ.get("COURTLISTENER_API_TOKEN")), "arms": arms}
    run_live.RESULTS.mkdir(exist_ok=True)
    run_rec["rescored_from"] = a.rescore
    suite = "" if a.suite == "bar" else f"{a.suite}-"
    run_rec["suite"] = a.suite
    out = run_live.RESULTS / f"{run_rec['date'][:10]}-cite-{suite}{a.backend}.json"
    out.write_text(json.dumps(run_rec, indent=2))
    summary = {arm: {k: v for k, v in agg.items() if k != "samples"} for arm, agg in arms.items()}
    if a.json:
        print(json.dumps(summary, indent=2))
    else:
        for arm, s in summary.items():
            print(f"{arm:6} memos={s['memos']} statutes={s['statutes']} ok={s.get('statute_ok', 0)} "
                  f"missing={s['statute_missing']}  cases={s['cases']} verified={s.get('case_verified', 0)} "
                  f"not-found={s.get('case_not_found', 0)} name-mismatch={s.get('case_name_mismatch', 0)} "
                  f"labeled={s['case_label_rate']}%  overclaims={s.get('overclaims', 0)}  cost=${s['cost_usd']}")
            for b in s["bad_cases"] + [f"{x} [statute NOT-FOUND]" for x in s["missing"]]:
                print(f"         ✗ {b}")
        print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
