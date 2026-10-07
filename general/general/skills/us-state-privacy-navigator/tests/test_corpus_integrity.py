#!/usr/bin/env python3
"""Test: corpus integrity.

Validates that references/enforcement_actions.json is well-formed and
internally consistent. Run from any directory:

    python tests/test_corpus_integrity.py
    python -m unittest tests.test_corpus_integrity

These tests will fail loudly if a corpus expansion breaks invariants —
they are the safety net that lets the corpus be edited without manual
checking each time.
"""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORPUS_PATH = ROOT / "references" / "enforcement_actions.json"

REQUIRED_FIELDS = {
    "id",
    "case_name",
    "year",
    "regulator",
    "respondent",
    "statutes",
    "violation_theories",
    "factual_pattern",
    "operational_lessons",
}

# Loose pattern — every entry should at minimum reference a statute or court
# code structure, except the advisory entry which is exempt.
ID_PATTERN = re.compile(r"^[a-z0-9][a-z0-9\-]*[a-z0-9]$")


class CorpusIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(CORPUS_PATH, "r", encoding="utf-8") as f:
            cls.corpus = json.load(f)
        cls.actions = cls.corpus["actions"]
        cls.taxonomy = set(cls.corpus["_meta"]["violation_theory_tags"])

    # -------- structural --------

    def test_corpus_loads_and_has_meta(self):
        self.assertIn("_meta", self.corpus)
        self.assertIn("corpus_version", self.corpus["_meta"])
        self.assertIn("violation_theory_tags", self.corpus["_meta"])
        self.assertIn("actions", self.corpus)
        self.assertGreater(len(self.actions), 50, "Corpus should have substantial action coverage")

    def test_all_ids_unique(self):
        ids = [a["id"] for a in self.actions]
        duplicates = [i for i in set(ids) if ids.count(i) > 1]
        self.assertEqual(duplicates, [], f"Duplicate action IDs: {duplicates}")

    def test_id_format(self):
        bad_ids = [a["id"] for a in self.actions if not ID_PATTERN.match(a["id"])]
        self.assertEqual(bad_ids, [], f"Action IDs should be lowercase-with-hyphens; bad: {bad_ids}")

    def test_required_fields_present(self):
        for a in self.actions:
            missing = REQUIRED_FIELDS - set(a.keys())
            self.assertEqual(
                missing, set(), f"Action {a.get('id', '?')} missing required fields: {missing}"
            )

    def test_year_is_plausible(self):
        for a in self.actions:
            self.assertIsInstance(a["year"], int, f"{a['id']}: year should be int")
            self.assertGreaterEqual(a["year"], 2018, f"{a['id']}: year too early")
            self.assertLessEqual(a["year"], 2027, f"{a['id']}: year too far in future")

    # -------- taxonomy --------

    def test_violation_theories_in_taxonomy(self):
        for a in self.actions:
            for tag in a.get("violation_theories", []):
                self.assertIn(
                    tag,
                    self.taxonomy,
                    f"Action {a['id']} uses tag '{tag}' not in taxonomy",
                )

    def test_advisory_entry_tags_empty(self):
        """Advisory entry should have no violation_theories — it's a meta-entry."""
        advisory = next(
            (a for a in self.actions if a["id"].startswith("advisory-")), None
        )
        if advisory is not None:
            self.assertEqual(
                advisory["violation_theories"],
                [],
                "Advisory entries should not assign violation theories",
            )

    # -------- known-good anchors --------

    def test_anchor_actions_present(self):
        """Spot-check that a curated set of high-stakes anchors haven't been lost in edits."""
        anchor_ids = {
            "ca-sephora-2022",         # foundational CA AG action
            "ca-cppa-honda-2025",      # first CPPA action
            "ca-ag-healthline-2025",   # largest CCPA settlement (2025)
            "tx-allstate-arity-2025",  # first state-AG comprehensive law lawsuit
            "ct-ticketnetwork-2025",   # first CTDPA monetary penalty
            "ca-cipa-kaiser-2025",     # largest healthcare-pixel settlement
            "ftc-cerebral-2024",       # FTC telehealth pixel anchor
            "il-bipa-google-2022",     # foundational BIPA settlement
        }
        present = {a["id"] for a in self.actions}
        missing = anchor_ids - present
        self.assertEqual(
            missing, set(), f"Anchor actions missing from corpus: {missing}"
        )

    # -------- field-shape sanity --------

    def test_regulator_is_list(self):
        for a in self.actions:
            self.assertIsInstance(a["regulator"], list, f"{a['id']}: regulator must be list")
            self.assertGreater(len(a["regulator"]), 0, f"{a['id']}: regulator list empty")

    def test_statutes_is_list(self):
        for a in self.actions:
            self.assertIsInstance(a["statutes"], list, f"{a['id']}: statutes must be list")

    def test_operational_lessons_substantive(self):
        """Every action must have at least one operational lesson — that's the value-add."""
        for a in self.actions:
            lessons = a.get("operational_lessons", [])
            self.assertIsInstance(lessons, list, f"{a['id']}: operational_lessons must be list")
            self.assertGreater(
                len(lessons),
                0,
                f"{a['id']}: must include at least one operational lesson",
            )
            for lesson in lessons:
                self.assertIsInstance(lesson, str)
                self.assertGreater(
                    len(lesson),
                    20,
                    f"{a['id']}: lesson too short to be useful: '{lesson}'",
                )

    def test_monetary_amount_type(self):
        for a in self.actions:
            amt = a.get("monetary_amount_usd")
            self.assertTrue(
                amt is None or isinstance(amt, (int, float)),
                f"{a['id']}: monetary_amount_usd must be number or null, got {type(amt).__name__}",
            )
            if isinstance(amt, (int, float)):
                self.assertGreaterEqual(
                    amt, 0, f"{a['id']}: monetary amount cannot be negative"
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
