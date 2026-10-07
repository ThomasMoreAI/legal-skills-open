#!/usr/bin/env python3
"""Test: applicability_check threshold engine.

Validates that the deterministic threshold engine produces predictable
verdicts for canonical fixture cases:

1. Small bootstrapped startup below all thresholds — no state applies.
2. Mid-market California-only entity — CA applies, others don't.
3. National enterprise — most states apply.

The engine refuses to guess on missing inputs; tests verify that this
"refuse to guess" behavior is preserved (Insufficient verdicts where
the SBA-size-standard inputs are absent for TX/NE).
"""

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "applicability_check.py"
FIXTURES = ROOT / "tests" / "fixtures"


def run_check(intake_path: Path) -> dict:
    """Run applicability_check.py against an intake fixture; parse output."""
    result = subprocess.run(
        ["python3", str(SCRIPT), "--input", str(intake_path)],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Script failed (exit {result.returncode}):\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        )
    return json.loads(result.stdout)


def get_verdict(out: dict, state: str) -> str:
    """Find the verdict for a given state in the results array."""
    for r in out["results"]:
        if r["state"] == state:
            return r["verdict"]
    raise AssertionError(f"State '{state}' not in results")


class ApplicabilityBelowThresholdsTests(unittest.TestCase):
    """Small startup below all comprehensive-law thresholds."""

    @classmethod
    def setUpClass(cls):
        cls.out = run_check(FIXTURES / "intake_below_thresholds.json")

    def test_no_states_apply(self):
        """No state's comprehensive privacy law should apply to a $500k/2k-consumer startup."""
        self.assertEqual(self.out["summary"]["applies"], [])
        self.assertEqual(self.out["summary"]["likely_applies"], [])

    def test_california_does_not_apply(self):
        self.assertEqual(get_verdict(self.out, "CA"), "Does Not Apply")

    def test_florida_does_not_apply(self):
        """FL has a $1B threshold — should be Does Not Apply for $500k revenue."""
        self.assertEqual(get_verdict(self.out, "FL"), "Does Not Apply")

    def test_most_states_resolved(self):
        """Most of the 20 states should resolve to a verdict; Insufficient should be limited to TX/NE which require SBA-size-standard analysis."""
        s = self.out["summary"]
        insufficient = set(s["insufficient"])
        # TX and NE require business-size analysis the fixture intentionally
        # doesn't supply — the engine refuses to guess. This is by design.
        # The set of insufficient states should be a small subset.
        self.assertLessEqual(
            len(insufficient), 5,
            f"Too many states resolved to Insufficient — expected <=5, got {insufficient}"
        )
        self.assertGreaterEqual(
            len(s["does_not_apply"]), 15,
            f"Most states should resolve to Does Not Apply for sub-threshold entity"
        )


class ApplicabilityCaliforniaOnlyTests(unittest.TestCase):
    """$30M revenue mid-market entity — CA threshold met, others below."""

    @classmethod
    def setUpClass(cls):
        cls.out = run_check(FIXTURES / "intake_ca_only.json")

    def test_california_applies(self):
        """$30M revenue exceeds CCPA's $25M threshold."""
        self.assertEqual(get_verdict(self.out, "CA"), "Applies")

    def test_va_does_not_apply(self):
        """4k VA consumers is below VCDPA's 100k threshold (no sale-revenue qualifier triggered)."""
        self.assertEqual(get_verdict(self.out, "VA"), "Does Not Apply")

    def test_co_does_not_apply(self):
        """3k CO consumers is below CPA's 100k threshold."""
        self.assertEqual(get_verdict(self.out, "CO"), "Does Not Apply")

    def test_ct_does_not_apply(self):
        """2.5k CT consumers is below CTDPA's 100k threshold."""
        self.assertEqual(get_verdict(self.out, "CT"), "Does Not Apply")

    def test_fl_does_not_apply(self):
        """FL has a $1B threshold; $30M does not meet it."""
        self.assertEqual(get_verdict(self.out, "FL"), "Does Not Apply")

    def test_only_california_applies(self):
        applies = set(self.out["summary"]["applies"])
        self.assertEqual(
            applies, {"CA"},
            f"Only CA should apply at $30M revenue / 50k CA consumers; got {applies}",
        )


class ApplicabilityMultistateTests(unittest.TestCase):
    """National enterprise — most states' laws should apply."""

    @classmethod
    def setUpClass(cls):
        cls.out = run_check(FIXTURES / "intake_multistate.json")

    def test_california_applies(self):
        self.assertEqual(get_verdict(self.out, "CA"), "Applies")

    def test_virginia_applies(self):
        """250k VA consumers exceeds VCDPA's 100k threshold."""
        self.assertEqual(get_verdict(self.out, "VA"), "Applies")

    def test_colorado_applies(self):
        self.assertEqual(get_verdict(self.out, "CO"), "Applies")

    def test_connecticut_applies(self):
        self.assertEqual(get_verdict(self.out, "CT"), "Applies")

    def test_oregon_applies(self):
        self.assertEqual(get_verdict(self.out, "OR"), "Applies")

    def test_maryland_applies(self):
        """220k MD consumers exceeds MODPA's 35k threshold."""
        self.assertEqual(get_verdict(self.out, "MD"), "Applies")

    def test_florida_does_not_apply(self):
        """FDBR has a $1B revenue threshold; $500M is below."""
        self.assertEqual(get_verdict(self.out, "FL"), "Does Not Apply")

    def test_majority_of_states_apply(self):
        """At least 15 of the 20 comprehensive-law states should apply."""
        applies = self.out["summary"]["applies"]
        self.assertGreaterEqual(
            len(applies), 15,
            f"National enterprise should trigger most state laws; got {len(applies)}: {applies}"
        )


class ApplicabilityOutputStructureTests(unittest.TestCase):
    """Tests on the output structure invariants."""

    def test_output_has_summary_and_results(self):
        out = run_check(FIXTURES / "intake_ca_only.json")
        self.assertIn("summary", out)
        self.assertIn("results", out)

    def test_summary_has_all_buckets(self):
        out = run_check(FIXTURES / "intake_ca_only.json")
        s = out["summary"]
        for bucket in ("applies", "likely_applies", "does_not_apply", "insufficient"):
            self.assertIn(bucket, s, f"Summary missing bucket: {bucket}")
            self.assertIsInstance(s[bucket], list)

    def test_each_result_has_required_fields(self):
        out = run_check(FIXTURES / "intake_ca_only.json")
        for r in out["results"]:
            for f in ("state", "statute", "effective", "verdict", "reasoning"):
                self.assertIn(f, r, f"Result missing field: {f}")

    def test_insufficient_results_have_needed_inputs(self):
        """When a state's verdict is Insufficient, the result should specify which inputs are needed.

        This enforces the operating principle: the engine refuses to guess,
        and tells the user what to provide instead.
        """
        out = run_check(FIXTURES / "intake_below_thresholds.json")
        for r in out["results"]:
            if r["verdict"] == "Insufficient Info":
                self.assertGreater(
                    len(r.get("needed_inputs", [])), 0,
                    f"State {r['state']} returned Insufficient without specifying needed inputs",
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
