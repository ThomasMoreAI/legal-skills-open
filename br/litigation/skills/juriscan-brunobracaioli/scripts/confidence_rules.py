"""Deterministic confidence and preservation rules (Phase 3 Step 3.4 + Phase 4 Step 4.3).

Runs AFTER juriscan-sintetizador and BEFORE scripts/finalize.py. Responsibilities:

  1. **Preservation invariant** (Phase 3.4): the synthesizer must not
     shrink `auditor_findings`. `len(synthesis.auditor_findings) >=
     len(auditor_input.auditor_findings)`. If violated, raise
     ConfidenceRuleError — the pipeline aborts.

  2. **Confidence downgrade** (Phase 4.3): for each argument with a
     `citacao_juridica` that has a matching verification, mark the argument:
       - status CONFIRMADO       → no change
       - status DIVERGENTE       → confidence_flag="DIVERGENT"
       - status NAO_ENCONTRADO   → confidence_flag="UNVERIFIED"
     Verifications are matched against arguments by `citacao_original`
     string equality (normalized whitespace-case-insensitive).

  3. **Verification summary** — emit a small aggregated report at
     `output.verification_summary` with counts by status.

Phase 4.3 branch is guarded behind the `verifications` argument: when
Phase 4 isn't live yet, pass `verifications=None` and only the preservation
invariant runs.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path


class ConfidenceRuleError(Exception):
    """Raised when a deterministic confidence rule is violated."""


@dataclass
class VerificationResult:
    citacao: str
    status: str  # CONFIRMADO | DIVERGENTE | NAO_ENCONTRADO
    divergencia: str | None = None


def _normalize_citation(s: str) -> str:
    return " ".join(s.strip().lower().split())


def _index_verifications(verifications: list[dict]) -> dict[str, VerificationResult]:
    index: dict[str, VerificationResult] = {}
    for v in verifications or []:
        raw = v.get("citacao_original")
        if not raw:
            continue
        index[_normalize_citation(raw)] = VerificationResult(
            citacao=raw,
            status=v.get("status", "NAO_ENCONTRADO"),
            divergencia=v.get("divergencia"),
        )
    return index


def assert_preservation(
    synthesizer_output: dict,
    auditor_output: dict,
) -> None:
    """Raise if the synthesizer dropped any auditor findings."""
    input_findings = auditor_output.get("auditor_findings") or []
    output_findings = synthesizer_output.get("auditor_findings") or []
    if len(output_findings) < len(input_findings):
        raise ConfidenceRuleError(
            "preservation invariant violated: synthesizer output has "
            f"{len(output_findings)} auditor_findings but auditor produced "
            f"{len(input_findings)}. The synthesizer is not allowed to drop "
            "findings. Aborting pipeline."
        )


def _apply_downgrade_to_arguments(
    arguments: list[dict],
    verif_index: dict[str, VerificationResult],
    counters: dict[str, int],
) -> None:
    for arg in arguments:
        citation = arg.get("citacao_juridica")
        if not citation:
            continue
        match = verif_index.get(_normalize_citation(citation))
        if match is None:
            counters["no_verification"] += 1
            continue
        if match.status == "CONFIRMADO":
            counters["confirmed"] += 1
        elif match.status == "DIVERGENTE":
            arg["confidence_flag"] = "DIVERGENT"
            if match.divergencia:
                arg["divergencia"] = match.divergencia
            counters["divergent"] += 1
        elif match.status == "NAO_ENCONTRADO":
            arg["confidence_flag"] = "UNVERIFIED"
            counters["unverified"] += 1


def apply_downgrade(
    synthesis: dict,
    verifications: list[dict] | None,
) -> dict:
    """Apply confidence downgrades based on verification status.

    Mutates `synthesis` in place and also returns it for convenience.
    """
    if not verifications:
        synthesis["verification_summary"] = {
            "total_verifications": 0,
            "confirmed": 0,
            "divergent": 0,
            "unverified": 0,
            "no_verification": 0,
        }
        return synthesis

    verif_index = _index_verifications(verifications)
    counters = {
        "confirmed": 0,
        "divergent": 0,
        "unverified": 0,
        "no_verification": 0,
    }

    perspectives = synthesis.get("perspectives") or {}
    for polo_name in ("autor", "reu"):
        polo = perspectives.get(polo_name) or {}
        for bucket in ("forcas", "fraquezas", "recursos_cabiveis"):
            items = polo.get(bucket) or []
            _apply_downgrade_to_arguments(items, verif_index, counters)

    synthesis["verification_summary"] = {
        "total_verifications": len(verifications),
        **counters,
    }
    return synthesis


def run(
    synthesis: dict,
    auditor_output: dict,
    verifications: list[dict] | None = None,
) -> dict:
    """Full rule set: preservation assertion + downgrade + summary."""
    assert_preservation(synthesis, auditor_output)
    apply_downgrade(synthesis, verifications)
    return synthesis


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Apply juriscan deterministic confidence and preservation rules"
    )
    parser.add_argument("--synthesis", required=True,
                        help="Path to juriscan-sintetizador output JSON")
    parser.add_argument("--auditor", required=True,
                        help="Path to juriscan-auditor-processual output JSON")
    parser.add_argument("--verifications", default=None,
                        help="Optional path to juriscan-verificador output JSON")
    parser.add_argument("--output", required=True)
    args = parser.parse_args(argv)

    synthesis = json.loads(Path(args.synthesis).read_text(encoding="utf-8"))
    auditor = json.loads(Path(args.auditor).read_text(encoding="utf-8"))
    verifications = None
    if args.verifications:
        verif_doc = json.loads(Path(args.verifications).read_text(encoding="utf-8"))
        verifications = verif_doc.get("verifications") if isinstance(verif_doc, dict) else verif_doc

    try:
        run(synthesis, auditor, verifications)
    except ConfidenceRuleError as e:
        print(f"[FAIL] confidence_rules: {e}", file=sys.stderr)
        return 1

    Path(args.output).write_text(
        json.dumps(synthesis, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"[OK] confidence rules applied → {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
