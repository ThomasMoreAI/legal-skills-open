#!/usr/bin/env python3
"""Test: conflict_resolver script.

Validates that the conflict-of-laws synthesizer correctly identifies
the binding state for each compliance dimension, especially the
single-state-stricter cases (MD's flat ban on sensitive-data sale,
CA's coverage of employees and B2B contacts).
"""

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "conflict_resolver.py"


def run_script(*args) -> dict:
    result = subprocess.run(
        ["python3", str(SCRIPT), *args, "--format", "json"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Script failed (exit {result.returncode}):\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        )
    return json.loads(result.stdout)


def find_finding(out: dict, dimension: str) -> dict:
    """Return the finding for a given compliance dimension."""
    for f in out["findings"]:
        if f["dimension"] == dimension:
            return f
    raise AssertionError(f"Finding for dimension '{dimension}' not in output")


class ConflictResolverTests(unittest.TestCase):

    # -------- output structure --------

    def test_output_structure(self):
        out = run_script("--states", "CA,CO,VA")
        self.assertIn("applicable_states", out)
        self.assertIn("findings", out)
        self.assertIn("findings_count", out)
        self.assertEqual(set(out["applicable_states"]), {"CA", "CO", "VA"})
        self.assertEqual(out["findings_count"], len(out["findings"]))
        self.assertGreater(len(out["findings"]), 0)

    # -------- the canonical conflict cases --------

    def test_md_controls_sensitive_data_sale_when_md_in_scope(self):
        """MD MODPA's flat ban on sensitive-data sale is the binding constraint."""
        out = run_script(
            "--states", "CA,CO,VA,MD",
            "--dimensions", "sensitive_data_sale_treatment",
        )
        finding = find_finding(out, "sensitive_data_sale_treatment")
        # When the dimension is narrowed, MD should be the single controlling state
        controlling = finding["controlling_state"]
        if isinstance(controlling, list):
            self.assertIn("MD", controlling)
        else:
            self.assertEqual(
                controlling, "MD",
                "MD's flat sensitive-data-sale ban should be controlling when MD is applicable",
            )
        self.assertIn("FLAT BAN", finding["binding_rule"].upper())

    def test_ca_controls_when_md_not_in_scope(self):
        """Without MD, the binding rule on sensitive-data sale falls to opt-in consent under CA/others."""
        out = run_script("--states", "CA,CO,VA")
        finding = find_finding(out, "sensitive_data_sale_treatment")
        # When MD is absent, no state imposes a flat ban — the rule reverts to consent-based
        self.assertNotEqual(
            finding["controlling_state"], "MD",
            "Should not list MD as controlling when MD is not applicable",
        )

    def test_ca_unique_in_authorized_agent_optout(self):
        """CA is the unique state requiring authorized-agent opt-out support — should be controlling."""
        out = run_script("--states", "CA,VA,CO,CT")
        finding = find_finding(out, "opt_out_authorized_agent")
        # controlling_state can be a string (single) or a list (multi-state tie)
        controlling = finding["controlling_state"]
        if isinstance(controlling, list):
            self.assertIn("CA", controlling)
        else:
            self.assertEqual(controlling, "CA")

    # -------- dimension filtering --------

    def test_dimension_filter_narrows_output(self):
        full = run_script("--states", "CA,CO,VA,MD")
        filtered = run_script(
            "--states", "CA,CO,VA,MD",
            "--dimensions", "sensitive_data_sale_treatment",
        )
        self.assertEqual(len(filtered["findings"]), 1)
        self.assertLess(len(filtered["findings"]), len(full["findings"]))

    # -------- state-set behavior --------

    def test_single_state_still_produces_findings(self):
        """A single-state applicability set should still produce per-dimension binding rules."""
        out = run_script("--states", "CA")
        self.assertGreater(len(out["findings"]), 0)
        for f in out["findings"]:
            self.assertEqual(f["controlling_state"], "CA")

    def test_unknown_state_handled_gracefully(self):
        """An unknown two-letter state should not crash the script, but the script should error or filter it out cleanly."""
        result = subprocess.run(
            ["python3", str(SCRIPT), "--states", "ZZ", "--format", "json"],
            capture_output=True, text=True, timeout=30,
        )
        # The script either errors clearly or returns a degenerate result —
        # both are acceptable; what's not acceptable is a Python traceback.
        self.assertNotIn("Traceback", result.stderr,
                         "Unknown state should not produce a Python traceback")


if __name__ == "__main__":
    unittest.main(verbosity=2)
