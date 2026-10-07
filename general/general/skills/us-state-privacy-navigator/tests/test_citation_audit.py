#!/usr/bin/env python3
"""Test: citation_audit script.

Two layers:

1. Fixture tests — confirm the auditor flags the planted issues in
   memo_with_errors.md and produces zero errors against memo_clean.md.

2. Reference-doc audits — run the auditor against every reference markdown
   file the skill ships. These should all pass clean. If a contributor adds a
   substantive claim without proper citation, this test will catch it.
"""

import json
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "citation_audit.py"
FIXTURES = ROOT / "tests" / "fixtures"


def run_audit(target: Path, strict: bool = False) -> tuple[int, dict]:
    """Run audit; return (exit_code, parsed_output_dict)."""
    args = ["python3", str(SCRIPT), "--input", str(target)]
    if strict:
        args.append("--strict")
    # Use --output for structured JSON
    output_path = target.parent / f"_test_output_{target.stem}.json"
    args.extend(["--output", str(output_path)])
    result = subprocess.run(args, capture_output=True, text=True, timeout=30)
    parsed = {}
    if output_path.exists():
        with open(output_path) as f:
            parsed = json.load(f)
        output_path.unlink()
    return result.returncode, parsed


class CitationAuditFixtureTests(unittest.TestCase):
    """Test the auditor against intentionally good and bad fixtures."""

    def test_clean_memo_passes(self):
        """memo_clean.md cites every claim properly; should produce no errors."""
        exit_code, out = run_audit(FIXTURES / "memo_clean.md")
        self.assertEqual(
            exit_code, 0,
            f"Clean memo should pass cleanly; got exit {exit_code}, findings: {out}",
        )

    def test_dirty_memo_flags_errors(self):
        """memo_with_errors.md has planted issues; auditor must flag them."""
        exit_code, out = run_audit(FIXTURES / "memo_with_errors.md")
        # We expect the auditor to detect at least one error (orphaned citation
        # marker, missing citations, or implausible section numbers)
        findings = out.get("findings", [])
        self.assertGreater(
            len(findings), 0,
            "Dirty memo should produce at least one finding"
        )
        # The orphaned [citation needed] marker should always be detected
        orphaned = [
            f for f in findings
            if "citation needed" in str(f).lower() or "orphaned" in str(f).lower()
        ]
        self.assertGreater(
            len(orphaned), 0,
            "Auditor should flag the [citation needed] orphan marker",
        )

    def test_planted_implausible_section_flagged(self):
        """The auditor should flag implausibly-large CCPA section numbers.

        Section-existence check produces a WARNING (not an error), so we
        check the full findings list rather than relying on exit code.
        """
        exit_code, out = run_audit(FIXTURES / "memo_with_errors.md")
        findings = out.get("findings", [])
        # Look for either a warning about CCPA range, or any mention of "999"
        flagged_implausible = any(
            "1798.99" in str(f) or "outside the CCPA codified range" in str(f).lower()
            for f in findings
        )
        self.assertTrue(
            flagged_implausible,
            f"Auditor should flag § 1798.999999 as outside CCPA range; got findings: {findings}",
        )


class CitationAuditReferenceDocsTests(unittest.TestCase):
    """Run the auditor against every reference doc the skill ships."""

    def _audit(self, path: Path):
        exit_code, out = run_audit(path)
        # In quiet mode without strict, exit 0 means clean (errors == 0).
        # Warnings are allowed by default; only errors block.
        if exit_code != 0:
            self.fail(
                f"Audit failed for {path.name}:\n"
                f"  Exit code: {exit_code}\n"
                f"  Findings: {json.dumps(out.get('findings', []), indent=2)[:2000]}"
            )

    def test_applicability_matrix_clean(self):
        self._audit(ROOT / "references" / "applicability-matrix.md")

    def test_controller_duties_clean(self):
        self._audit(ROOT / "references" / "controller-duties.md")

    def test_rights_comparison_clean(self):
        self._audit(ROOT / "references" / "rights-comparison.md")

    def test_sensitive_data_clean(self):
        self._audit(ROOT / "references" / "sensitive-data.md")

    def test_universal_opt_out_clean(self):
        self._audit(ROOT / "references" / "universal-opt-out.md")

    def test_kids_and_teens_clean(self):
        self._audit(ROOT / "references" / "kids-and-teens.md")


if __name__ == "__main__":
    unittest.main(verbosity=2)
