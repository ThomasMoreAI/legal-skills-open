#!/usr/bin/env python3
"""
applicability_check.py — Deterministic threshold engine for US state privacy laws.

Usage:
    python applicability_check.py --input intake.json
    python applicability_check.py --input intake.json --output report.json

Input: JSON conforming to assets/applicability-questions.json schema.
Output: A per-state applicability verdict with reasoning, plus a list of inputs
needed to resolve any "Insufficient Info" verdicts.

This script is deterministic. It does not invoke an LLM, does not infer missing
inputs, and does not "soften" close calls. It is intended as a sanity check on
the threshold analysis, not a replacement for considered judgment.

Part of the us-state-privacy-navigator skill.
"""

import argparse
import json
import sys
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Optional


class Verdict(str, Enum):
    APPLIES = "Applies"
    LIKELY_APPLIES = "Likely Applies"
    DOES_NOT_APPLY = "Does Not Apply"
    INSUFFICIENT = "Insufficient Info"


@dataclass
class StateResult:
    state: str
    statute: str
    effective: str
    verdict: Verdict
    reasoning: str
    needed_inputs: list = field(default_factory=list)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def get_state_count(intake: dict, state_code: str) -> Optional[int]:
    """Return the consumer count for a state, or None if unknown."""
    by_state = intake.get("consumers", {}).get("by_state", {}) or {}
    val = by_state.get(state_code.upper())
    if val is None:
        return None
    try:
        return int(val)
    except (TypeError, ValueError):
        return None


def revenue(intake: dict) -> Optional[float]:
    val = intake.get("revenue", {}).get("annual_gross")
    if val is None:
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def percent_revenue_from_sale(intake: dict) -> Optional[float]:
    val = intake.get("sale_practices", {}).get("percent_revenue_from_sale")
    if val is None:
        return None
    try:
        return float(val)
    except (TypeError, ValueError):
        return None


def sells(intake: dict) -> Optional[bool]:
    return intake.get("sale_practices", {}).get("sells_pd")


def any_sale_revenue(intake: dict) -> Optional[bool]:
    return intake.get("sale_practices", {}).get("any_revenue_from_sale")


def sectoral_entity_exempt(intake: dict, state_code: str) -> tuple[bool, str]:
    """Identify entity-level exemptions. Returns (exempt, reason)."""
    s = intake.get("sectoral_overlay", {}) or {}
    # Entity-level GLBA exemptions:
    glba_entity_states = {"VA", "CT", "UT", "TN", "KY", "IA", "IN", "NJ", "TX", "NE"}
    if s.get("glba_financial_institution") and state_code in glba_entity_states:
        return True, f"Entity-level GLBA exemption applies in {state_code}."
    # Entity-level HIPAA exemptions:
    hipaa_entity_states = {"VA", "CT", "UT", "TN", "KY", "IA", "IN", "NJ", "TX", "NE"}
    if s.get("hipaa_covered_entity_or_ba") and state_code in hipaa_entity_states:
        return True, f"Entity-level HIPAA exemption applies in {state_code}."
    # Non-profits — varies. Most states exempt; DE, OR, MD, MN, MD do not (or partially).
    np_exempt_states = {"VA", "CT", "UT", "TN", "KY", "IA", "IN", "NJ", "TX", "NE", "MT", "NH", "RI"}
    if s.get("non_profit") and state_code in np_exempt_states:
        return True, f"Non-profit exemption applies in {state_code}."
    # Higher ed — most states exempt
    he_exempt_states = {"VA", "CT", "UT", "TN", "KY", "IA", "IN", "TX", "NE", "MT", "NH"}
    if s.get("higher_ed_institution") and state_code in he_exempt_states:
        return True, f"Higher-education exemption applies in {state_code}."
    # Government — universally exempt
    if s.get("government_entity"):
        return True, "Government-entity exemption applies."
    return False, ""


# ---------------------------------------------------------------------------
# State threshold tests
# ---------------------------------------------------------------------------


def test_ca(intake: dict) -> StateResult:
    rev = revenue(intake)
    cnt = get_state_count(intake, "CA")
    pct = percent_revenue_from_sale(intake)
    s = intake.get("sectoral_overlay", {}) or {}
    if not intake.get("entity", {}).get("for_profit", True):
        if s.get("non_profit"):
            return StateResult(
                state="CA",
                statute="Cal. Civ. Code §§ 1798.100 et seq.",
                effective="Jan 2020; CPRA Jan 2023",
                verdict=Verdict.DOES_NOT_APPLY,
                reasoning="CCPA generally applies only to for-profit entities. Note: certain CCPA amendments expand non-profit obligations narrowly; verify against current law.",
            )
    needed = []
    if rev is None:
        needed.append("annual_gross_revenue")
    if cnt is None:
        needed.append("CA_consumer_count")
    if pct is None and sells(intake) is True:
        needed.append("percent_revenue_from_sale")
    if needed:
        return StateResult(
            state="CA",
            statute="Cal. Civ. Code §§ 1798.100 et seq.",
            effective="Jan 2020; CPRA Jan 2023",
            verdict=Verdict.INSUFFICIENT,
            reasoning="Cannot evaluate without specified inputs.",
            needed_inputs=needed,
        )
    reasons = []
    triggered = False
    # Threshold 1: $25M revenue (note adjusted to $26.625M effective Jan 2025; conservative reading uses $25M)
    if rev is not None and rev >= 25_000_000:
        triggered = True
        reasons.append(f"Revenue (${rev:,.0f}) ≥ $25M threshold.")
    # Threshold 2: ≥100k CA consumers
    if cnt is not None and cnt >= 100_000:
        triggered = True
        reasons.append(f"CA consumer count ({cnt:,}) ≥ 100,000 threshold.")
    # Threshold 3: ≥50% revenue from sale or sharing
    if pct is not None and pct >= 50.0:
        triggered = True
        reasons.append(f"Sale/share revenue share ({pct}%) ≥ 50% threshold.")
    if triggered:
        return StateResult(
            state="CA",
            statute="Cal. Civ. Code §§ 1798.100 et seq.",
            effective="Jan 2020; CPRA Jan 2023",
            verdict=Verdict.APPLIES,
            reasoning=" ".join(reasons) + " Cal. Civ. Code § 1798.140(d).",
        )
    return StateResult(
        state="CA",
        statute="Cal. Civ. Code §§ 1798.100 et seq.",
        effective="Jan 2020; CPRA Jan 2023",
        verdict=Verdict.DOES_NOT_APPLY,
        reasoning=f"None of the thresholds met. Revenue ${rev:,.0f} < $25M; CA consumers {cnt:,} < 100,000; sale revenue share {pct}% < 50%.",
    )


def _two_tier_test(
    intake: dict,
    state_code: str,
    statute: str,
    effective: str,
    primary_threshold: int,
    secondary_threshold: int,
    secondary_pct_threshold: Optional[float] = None,
    use_any_sale_revenue: bool = False,
    revenue_floor: Optional[float] = None,
) -> StateResult:
    """Generic two-tier threshold test.

    primary_threshold: consumer count for tier 1 (no revenue percent test).
    secondary_threshold: consumer count for tier 2.
    secondary_pct_threshold: revenue-percent-from-sale required at tier 2 (None if NJ-style "any revenue").
    use_any_sale_revenue: NJ/MN-style activity test instead of percent.
    revenue_floor: UT/TN-style mandatory minimum revenue (None if no floor).
    """
    exempt, reason = sectoral_entity_exempt(intake, state_code)
    if exempt:
        return StateResult(
            state=state_code,
            statute=statute,
            effective=effective,
            verdict=Verdict.DOES_NOT_APPLY,
            reasoning=reason,
        )
    rev = revenue(intake)
    cnt = get_state_count(intake, state_code)
    pct = percent_revenue_from_sale(intake)
    any_sale = any_sale_revenue(intake)
    sells_flag = sells(intake)

    needed = []
    if cnt is None:
        needed.append(f"{state_code}_consumer_count")
    if revenue_floor is not None and rev is None:
        needed.append("annual_gross_revenue")
    if needed:
        return StateResult(
            state=state_code,
            statute=statute,
            effective=effective,
            verdict=Verdict.INSUFFICIENT,
            reasoning="Cannot evaluate without specified inputs.",
            needed_inputs=needed,
        )

    reasons = []
    if revenue_floor is not None and (rev is None or rev < revenue_floor):
        return StateResult(
            state=state_code,
            statute=statute,
            effective=effective,
            verdict=Verdict.DOES_NOT_APPLY,
            reasoning=f"Revenue ${rev:,.0f} below mandatory ${revenue_floor:,.0f} floor.",
        )

    triggered = False
    if cnt >= primary_threshold:
        triggered = True
        reasons.append(f"{state_code} consumer count ({cnt:,}) ≥ {primary_threshold:,} primary threshold.")

    # Tier 2
    if cnt >= secondary_threshold:
        if use_any_sale_revenue:
            if any_sale or sells_flag:
                triggered = True
                reasons.append(
                    f"{state_code} consumer count ({cnt:,}) ≥ {secondary_threshold:,} AND any sale revenue (NJ-style activity test)."
                )
            elif sells_flag is None and any_sale is None:
                # Insufficient — could go either way
                return StateResult(
                    state=state_code,
                    statute=statute,
                    effective=effective,
                    verdict=Verdict.INSUFFICIENT,
                    reasoning="Tier-2 activity threshold reached but sale-revenue input missing.",
                    needed_inputs=["any_revenue_from_sale or sells_pd"],
                )
        else:
            if pct is None and sells_flag in (True, None):
                if not triggered:
                    return StateResult(
                        state=state_code,
                        statute=statute,
                        effective=effective,
                        verdict=Verdict.INSUFFICIENT,
                        reasoning="Tier-2 consumer threshold reached but percent-of-revenue-from-sale missing.",
                        needed_inputs=["percent_revenue_from_sale"],
                    )
            elif pct is not None and secondary_pct_threshold is not None and pct >= secondary_pct_threshold:
                triggered = True
                reasons.append(
                    f"{state_code} consumer count ({cnt:,}) ≥ {secondary_threshold:,} AND sale revenue {pct}% ≥ {secondary_pct_threshold}%."
                )
    if triggered:
        return StateResult(
            state=state_code,
            statute=statute,
            effective=effective,
            verdict=Verdict.APPLIES,
            reasoning=" ".join(reasons),
        )
    return StateResult(
        state=state_code,
        statute=statute,
        effective=effective,
        verdict=Verdict.DOES_NOT_APPLY,
        reasoning=f"Neither threshold met. Consumer count {cnt:,}; revenue ${rev:,.0f}" + (f"; sale revenue share {pct}%." if pct is not None else "."),
    )


def test_va(intake): return _two_tier_test(intake, "VA", "Va. Code §§ 59.1-575 to -585", "Jan 2023", 100_000, 25_000, 50.0)
def test_co(intake): return _two_tier_test(intake, "CO", "Colo. Rev. Stat. §§ 6-1-1301 et seq.", "Jul 2023", 100_000, 25_000, use_any_sale_revenue=True)
def test_ct(intake): return _two_tier_test(intake, "CT", "Conn. Gen. Stat. §§ 42-515 et seq.", "Jul 2023", 100_000, 25_000, 25.0)
def test_ut(intake): return _two_tier_test(intake, "UT", "Utah Code §§ 13-61-101 et seq.", "Dec 2023", 100_000, 25_000, 50.0, revenue_floor=25_000_000)
def test_or(intake): return _two_tier_test(intake, "OR", "Or. Rev. Stat. §§ 646A.570 et seq.", "Jul 2024", 100_000, 25_000, 25.0)
def test_mt(intake): return _two_tier_test(intake, "MT", "Mont. Code §§ 30-14-2801 et seq.", "Oct 2024", 50_000, 25_000, 25.0)
def test_ia(intake): return _two_tier_test(intake, "IA", "Iowa Code §§ 715D.1 et seq.", "Jan 2025", 100_000, 25_000, 50.0)
def test_in(intake): return _two_tier_test(intake, "IN", "Ind. Code §§ 24-15 et seq.", "Jan 2026", 100_000, 25_000, 50.0)
def test_tn(intake): return _two_tier_test(intake, "TN", "Tenn. Code §§ 47-18-3201 et seq.", "Jul 2025", 175_000, 25_000, 50.0, revenue_floor=25_000_000)
def test_de(intake): return _two_tier_test(intake, "DE", "Del. Code tit. 6, ch. 12D", "Jan 2025", 35_000, 10_000, 20.0)
def test_nj(intake): return _two_tier_test(intake, "NJ", "N.J. Stat. §§ 56:8-166.4 et seq.", "Jan 2025", 100_000, 25_000, use_any_sale_revenue=True)
def test_nh(intake): return _two_tier_test(intake, "NH", "N.H. Rev. Stat. ch. 507-H", "Jan 2025", 35_000, 10_000, 25.0)
def test_ky(intake): return _two_tier_test(intake, "KY", "Ky. Rev. Stat. §§ 367.3611 et seq.", "Jan 2026", 100_000, 25_000, 50.0)
def test_md(intake): return _two_tier_test(intake, "MD", "Md. Code Com. Law §§ 14-4601 et seq.", "Oct 2025", 35_000, 10_000, 20.0)
def test_mn(intake): return _two_tier_test(intake, "MN", "Minn. Stat. ch. 325O", "Jul 2025", 100_000, 25_000, 25.0)
def test_ri(intake): return _two_tier_test(intake, "RI", "R.I. Gen. Laws §§ 6-48.1-1 et seq.", "Jan 2026", 35_000, 10_000, 20.0)


def test_tx(intake: dict) -> StateResult:
    """Texas/Nebraska SBA-based test with sensitive-data carve-out."""
    return _sba_test(intake, "TX", "Tex. Bus. & Com. Code §§ 541.001 et seq.", "Jul 2024")


def test_ne(intake: dict) -> StateResult:
    return _sba_test(intake, "NE", "Neb. Rev. Stat. §§ 87-1101 et seq.", "Jan 2025")


def _sba_test(intake: dict, state_code: str, statute: str, effective: str) -> StateResult:
    exempt, reason = sectoral_entity_exempt(intake, state_code)
    if exempt:
        return StateResult(state=state_code, statute=statute, effective=effective, verdict=Verdict.DOES_NOT_APPLY, reasoning=reason)

    sells_flag = sells(intake)
    sells_sensitive_no_consent = intake.get("sale_practices", {}).get("sells_sensitive_data_without_consent")
    naics = intake.get("entity", {}).get("naics_code")
    rev = revenue(intake)

    if sells_flag is None:
        return StateResult(state=state_code, statute=statute, effective=effective, verdict=Verdict.INSUFFICIENT, reasoning="Cannot evaluate without sale-practice input.", needed_inputs=["sells_pd"])
    # TDPSA/NDPA apply if the entity "processes or engages in the sale of PD." Processing is
    # interpreted broadly — any entity with consumer accounts, marketing data, or analytics
    # generally satisfies "processes." Only flag DOES_NOT_APPLY if intake explicitly indicates
    # the entity has no PD-processing footprint at all.
    state_count = get_state_count(intake, state_code)
    has_any_data = bool(intake.get("data_categories")) or (state_count is not None and state_count > 0)
    if not sells_flag and not has_any_data and intake.get("data_categories") is not None:
        return StateResult(state=state_code, statute=statute, effective=effective, verdict=Verdict.DOES_NOT_APPLY, reasoning="Entity does not process or sell PD per inputs.")

    if sells_sensitive_no_consent:
        return StateResult(
            state=state_code,
            statute=statute,
            effective=effective,
            verdict=Verdict.APPLIES,
            reasoning=(
                "Sale of sensitive data without consent eliminates the SBA small-business carve-out. "
                "Statute applies regardless of size. (See per-state notes for citations.)"
            ),
        )
    if naics is None or rev is None:
        return StateResult(
            state=state_code,
            statute=statute,
            effective=effective,
            verdict=Verdict.INSUFFICIENT,
            reasoning="SBA size status cannot be evaluated without NAICS code and revenue.",
            needed_inputs=["entity.naics_code", "annual_gross_revenue"],
        )
    # Heuristic only — real SBA size determination requires lookup against the SBA size standards table.
    return StateResult(
        state=state_code,
        statute=statute,
        effective=effective,
        verdict=Verdict.LIKELY_APPLIES if rev >= 47_000_000 else Verdict.INSUFFICIENT,
        reasoning=(
            f"NAICS {naics}, revenue ${rev:,.0f}. SBA small-business status must be determined "
            "against the SBA NAICS size standards table — this script does not maintain that table. "
            "If the entity exceeds the relevant SBA threshold, statute applies (subject to other carve-outs)."
        ),
        needed_inputs=["sba_size_status_for_naics_code"] if rev < 47_000_000 else [],
    )


def test_fl(intake: dict) -> StateResult:
    """Florida FDBR — narrow $1B + activity-prong test."""
    rev = revenue(intake)
    if rev is None:
        return StateResult(state="FL", statute="Fla. Stat. §§ 501.701 et seq.", effective="Jul 2024", verdict=Verdict.INSUFFICIENT, reasoning="Cannot evaluate without revenue.", needed_inputs=["annual_gross_revenue"])
    if rev < 1_000_000_000:
        return StateResult(state="FL", statute="Fla. Stat. §§ 501.701 et seq.", effective="Jul 2024", verdict=Verdict.DOES_NOT_APPLY, reasoning=f"Revenue ${rev:,.0f} below $1B FDBR threshold. FDBR targets large platform-scale entities only.")
    # Activity prongs — the script cannot infer; flag for review.
    return StateResult(
        state="FL",
        statute="Fla. Stat. §§ 501.701 et seq.",
        effective="Jul 2024",
        verdict=Verdict.LIKELY_APPLIES,
        reasoning=(
            "Revenue ≥ $1B threshold met. FDBR additionally requires one of three activity prongs: "
            "(i) ≥50% revenue from online ad sales; (ii) operates a smart-speaker / voice service with "
            "cloud assistant; or (iii) operates an app store / digital distribution platform with "
            "≥250,000 software apps. Confirm activity prong before final verdict."
        ),
        needed_inputs=["fl_activity_prong_status"],
    )


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


STATE_TESTS = [
    test_ca, test_va, test_co, test_ct, test_ut, test_tx, test_or, test_mt,
    test_fl, test_ia, test_de, test_nj, test_nh, test_ne, test_mn, test_md,
    test_tn, test_in, test_ky, test_ri,
]


def run(intake: dict) -> dict:
    results = [t(intake) for t in STATE_TESTS]
    summary = {
        "applies": [r.state for r in results if r.verdict == Verdict.APPLIES],
        "likely_applies": [r.state for r in results if r.verdict == Verdict.LIKELY_APPLIES],
        "does_not_apply": [r.state for r in results if r.verdict == Verdict.DOES_NOT_APPLY],
        "insufficient": [r.state for r in results if r.verdict == Verdict.INSUFFICIENT],
    }
    return {"summary": summary, "results": [asdict(r) for r in results]}


def main():
    p = argparse.ArgumentParser(description="US State Privacy Navigator — applicability checker.")
    p.add_argument("--input", required=True, help="Path to intake JSON.")
    p.add_argument("--output", help="Optional output JSON path.")
    args = p.parse_args()
    with open(args.input, "r") as f:
        intake = json.load(f)
    out = run(intake)
    text = json.dumps(out, indent=2, default=str)
    if args.output:
        with open(args.output, "w") as f:
            f.write(text)
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
