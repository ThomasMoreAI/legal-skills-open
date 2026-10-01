#!/usr/bin/env python3
"""Build and sanity-check a renovation payment schedule.

Pure local arithmetic. No network, no third-party packages, no file writes.

This helper is OPTIONAL. Every check it performs is stated in SKILL.md Step 5 and in
references/scope-and-terms.md so an agent that cannot execute scripts (Claude.ai, ChatGPT, Manus,
Grok) does exactly the same arithmetic inline. Nothing here supplies a default percentage split:
there is no statutory or standard split for an Israeli renovation, and inventing one would be the
single worst failure available in this domain. The caller passes the numbers the parties chose;
this script only checks that they are internally coherent.

Usage:
  python3 payment_schedule.py --total 120000 --vat included \\
      --stage "mobilisation:10" --stage "first fix:20" --stage "tiling:25" \\
      --stage "carpentry:20" --stage "practical completion:15" --retention 10

  python3 payment_schedule.py --example
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

# A mobilisation payment larger than this is worth flagging: it front-loads the job and erodes the
# leverage the schedule exists to create. It is a WARNING threshold for discussion, not a rule of
# law, and the script says so in its output.
MOBILISATION_WARN_PCT = 15.0

# Below this, a retention is too small to make the deduct-and-self-cure right in s.4 collectable.
# Again a discussion threshold, not a legal minimum.
RETENTION_WARN_PCT = 5.0


@dataclass
class Stage:
    name: str
    pct: float

    @property
    def is_pre_work(self) -> bool:
        """True for a payment that falls due before any work is verifiable."""
        n = self.name.strip().lower()
        return any(k in n for k in ("mobilis", "mobiliz", "advance", "deposit", "signature",
                                    "מקדמה", "חתימה"))


def parse_stage(raw: str) -> Stage:
    if ":" not in raw:
        raise ValueError(f"stage {raw!r} must be in the form 'name:percent'")
    name, _, pct = raw.rpartition(":")
    try:
        value = float(pct)
    except ValueError:
        raise ValueError(f"stage {raw!r} has a non-numeric percentage {pct!r}") from None
    if value <= 0:
        raise ValueError(f"stage {raw!r} must have a positive percentage")
    if not name.strip():
        raise ValueError(f"stage {raw!r} must have a name")
    return Stage(name.strip(), value)


def build(total: float, stages: list[Stage], retention: float, vat: str) -> tuple[str, list[str]]:
    findings: list[str] = []
    allocated = sum(s.pct for s in stages) + retention

    # Check 1, the arithmetic must close exactly. Tolerance is for float noise only.
    if abs(allocated - 100.0) > 0.01:
        findings.append(
            f"BLOCKER: stages plus retention total {allocated:.2f} percent, not one hundred. "
            f"{'Over-allocated by' if allocated > 100 else 'Unallocated:'} "
            f"{abs(allocated - 100.0):.2f}%."
        )

    # Check 2, front-loading.
    for s in stages:
        if s.is_pre_work and s.pct > MOBILISATION_WARN_PCT:
            findings.append(
                f"WARNING: '{s.name}' is {s.pct:g}% and falls due before any work can be verified. "
                f"Above about {MOBILISATION_WARN_PCT:g}% this stops being mobilisation and starts "
                f"being an unsecured loan to the contractor. Discuss, this is not a legal limit."
            )

    # Check 3, the retention must exist and must be worth something.
    if retention <= 0:
        findings.append(
            "BLOCKER: no retention. Without money still unpaid after handover, the right in "
            "s.4 of the Contract for Services Law to deduct or to self-cure is theoretical."
        )
    elif retention < RETENTION_WARN_PCT:
        findings.append(
            f"WARNING: retention is {retention:g}%, which may be too small to cover putting a "
            f"defect right. Discuss, this is not a legal minimum."
        )

    # Check 4, every stage needs an objectively verifiable trigger. The script cannot judge this,
    # so it says so rather than pretending to have checked.
    findings.append(
        "MANUAL CHECK: every stage trigger below must be verifiable by looking at the property. "
        "'After the kitchen carpentry is installed and doors aligned' is verifiable. "
        "'After three weeks' is not, it pays for elapsed time rather than for work."
    )

    vat_note = {
        "included": 'total is KOLEL MA"AM (VAT included)',
        "excluded": 'total is BETOSEFET MA"AM (VAT is added on top)',
        "unknown": 'VAT TREATMENT NOT STATED, this must be resolved before signature',
    }[vat]

    lines = [
        f"Total: {total:,.2f} NIS  ({vat_note})",
        "",
        f"{'Stage':<38}{'%':>8}{'Amount (NIS)':>16}",
        "-" * 62,
    ]
    running = 0.0
    for s in stages:
        amount = total * s.pct / 100.0
        running += amount
        lines.append(f"{s.name:<38}{s.pct:>7g}%{amount:>16,.2f}")
    ret_amount = total * retention / 100.0
    lines.append(f"{'Retention (released after acceptance)':<38}{retention:>7g}%{ret_amount:>16,.2f}")
    lines.append("-" * 62)
    lines.append(f"{'TOTAL':<38}{allocated:>7g}%{running + ret_amount:>16,.2f}")
    return "\n".join(lines), findings


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--total", type=float, help="agreed total price in NIS")
    p.add_argument("--stage", action="append", default=[], metavar="NAME:PCT",
                   help="a payment stage, repeatable, e.g. --stage 'first fix:20'")
    p.add_argument("--retention", type=float, default=0.0,
                   help="percent held back until after acceptance")
    p.add_argument("--vat", choices=("included", "excluded", "unknown"), default="unknown",
                   help="whether --total already includes VAT")
    p.add_argument("--example", action="store_true", help="run a worked example and exit")
    args = p.parse_args(argv)

    if args.example:
        args.total, args.vat, args.retention = 120000.0, "included", 10.0
        args.stage = ["mobilisation:10", "first fix:20", "tiling:25",
                      "carpentry:20", "practical completion:15"]

    if args.total is None or not args.stage:
        p.error("--total and at least one --stage are required (or use --example)")
    if args.total <= 0:
        p.error("--total must be positive")

    try:
        stages = [parse_stage(s) for s in args.stage]
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    table, findings = build(args.total, stages, args.retention, args.vat)
    print(table)
    print()
    for f in findings:
        print(f"  - {f}")
    print()
    print("  This schedule is a draft for personal preparation. It is not legal advice, and no "
          "law supplies a standard split for an Israeli renovation.")
    return 1 if any(f.startswith("BLOCKER") for f in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
