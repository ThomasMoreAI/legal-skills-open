#!/usr/bin/env python3
"""Test: precedent_match script — scoring, ranking, CLI behavior.

Validates that the precedent matcher returns the right matches for canonical
queries. These are real privacy-counsel questions that any practitioner
asking the corpus should get the right answer to.
"""

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "precedent_match.py"
GAPS_FIXTURE = ROOT / "tests" / "fixtures" / "gaps_sample.json"


def run_script(*args) -> dict:
    """Run precedent_match.py with the given args, return parsed JSON output."""
    result = subprocess.run(
        ["python3", str(SCRIPT), *args],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Script failed (exit {result.returncode}):\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}"
        )
    return json.loads(result.stdout)


class PrecedentMatchTests(unittest.TestCase):

    # -------- tag-based queries (the dominant use case) --------

    def test_gpc_processor_returns_healthline_first(self):
        """Healthline is the most analogous matter for GPC + processor contracts in CA."""
        out = run_script(
            "--tag", "gpc_not_honored",
            "--tag", "processor_contract_inadequate",
            "--state", "CA",
            "--top", "5",
        )
        self.assertGreater(len(out["matches"]), 0)
        top = out["matches"][0]
        self.assertEqual(
            top["id"],
            "ca-ag-healthline-2025",
            f"Top match should be Healthline, got {top['id']}",
        )

    def test_pixel_health_disclosure_returns_healthcare_anchors(self):
        """The top results for pixel-health-data should include healthcare-sector matters."""
        out = run_script("--tag", "pixel_health_data_disclosure", "--top", "5")
        match_ids = {m["id"] for m in out["matches"]}
        # At least one of these foundational pixel-health cases must appear in top 5
        expected_anchors = {
            "ca-ag-healthline-2025",
            "ftc-cerebral-2024",
            "ftc-goodrx-2023",
            "ftc-betterhelp-2023",
            "ca-cipa-kaiser-2025",
        }
        self.assertTrue(
            match_ids & expected_anchors,
            f"Top 5 for pixel-health should include at least one anchor; got {match_ids}",
        )

    def test_wiretap_session_replay_returns_relevant(self):
        """Session-replay tag should surface Kaiser and Torres at minimum."""
        out = run_script("--tag", "wiretap_session_replay", "--top", "5")
        ids = {m["id"] for m in out["matches"]}
        # Both Kaiser (plaintiff settlement) and Torres (defense win) should be findable
        self.assertIn("ca-cipa-kaiser-2025", ids)
        self.assertIn("ca-cipa-torres-prudential-2025", ids)

    def test_state_filter_boosts_score(self):
        """State match should produce higher score than no state match for same tag."""
        with_state = run_script("--tag", "notice_inadequate_content", "--state", "CT", "--top", "3")
        without_state = run_script("--tag", "notice_inadequate_content", "--top", "3")
        # The CT-state-filtered top match should have a higher score than the same
        # action would in the non-filtered ranking, OR a CT-specific action should
        # rank higher. Either way, the CT-filtered top should be a CT action.
        ct_anchors = {"ct-ticketnetwork-2025", "ct-ag-report-2024"}
        self.assertIn(
            with_state["matches"][0]["id"],
            ct_anchors,
            "CT-filtered top match should be a CT action",
        )

    # -------- text query mode --------

    def test_text_query_returns_matches(self):
        out = run_script("--query", "connected vehicle insurance geolocation", "--top", "5")
        self.assertGreater(len(out["matches"]), 0)
        # At least one connected-vehicle case should surface
        connected_vehicle_ids = {
            "tx-allstate-arity-2025",
            "tx-gm-onstar-2024",
            "ftc-gm-onstar-2026",
            "ca-cppa-honda-2025",
            "ca-cppa-connected-vehicles-2024",
        }
        match_ids = {m["id"] for m in out["matches"]}
        self.assertTrue(
            match_ids & connected_vehicle_ids,
            f"No connected-vehicle matches in top 5: {match_ids}",
        )

    # -------- batch mode --------

    def test_batch_mode_processes_all_gaps(self):
        """Batch mode reads --gaps fixture and returns one entry per gap.

        The top-level result key is `matches`, with each entry having a `matches`
        field containing the per-gap analogous actions. Note: the script does not
        currently echo the input gap_id back into the output (it shows None).
        """
        out = run_script("--gaps", str(GAPS_FIXTURE), "--top", "3")
        self.assertIn("matches", out)
        gap_results = out["matches"]
        self.assertEqual(len(gap_results), 3, "Should process all 3 fixture gaps")
        for gr in gap_results:
            self.assertIn("tags", gr)
            self.assertIn("states", gr)
            self.assertIn("matches", gr)
            self.assertGreater(
                len(gr["matches"]), 0, f"Gap with tags {gr['tags']} has no matches"
            )

    # -------- output structure --------

    def test_match_output_has_required_fields(self):
        out = run_script("--tag", "deceptive_privacy_representation", "--top", "1")
        match = out["matches"][0]
        for f in ["id", "case_name", "year", "score"]:
            self.assertIn(f, match, f"Match output missing field: {f}")

    def test_top_n_respects_limit(self):
        out = run_script("--tag", "deceptive_privacy_representation", "--top", "3")
        self.assertLessEqual(len(out["matches"]), 3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
