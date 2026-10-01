from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import ClassVar

import pytest

SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT = SKILL_DIR / "scripts" / "legal_readiness.py"
EXAMPLE = SKILL_DIR / "assets" / "legal-readiness.example.json"


def load_script_module():
    spec = importlib.util.spec_from_file_location("legal_readiness_under_test", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture()
def valid_manifest() -> dict:
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    data["project"] = {
        "name": "Mothlight Notes",
        "repository": "https://github.com/mothlight/notes",
        "base_url": "https://mothlight.test",
        "template": False,
    }
    return data


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        text=True,
        capture_output=True,
        check=False,
    )


def write_manifest(tmp_path: Path, data: dict) -> Path:
    path = tmp_path / "legal-readiness.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def test_completed_structure_passes(valid_manifest: dict, tmp_path: Path) -> None:
    result = run_cli("check", str(write_manifest(tmp_path, valid_manifest)))
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.startswith("PASS")


def test_bundled_template_is_refused(tmp_path: Path) -> None:
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "project.template" in result.stdout


def test_check_json_is_machine_readable(valid_manifest: dict, tmp_path: Path) -> None:
    result = run_cli("check", str(write_manifest(tmp_path, valid_manifest)), "--json")
    payload = json.loads(result.stdout)
    assert result.returncode == 0
    assert payload["ok"] is True
    assert payload["errors"] == []


def test_wrong_type_scope_returns_machine_readable_errors(tmp_path: Path) -> None:
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    data["scope"] = "wrong-type"
    result = run_cli("check", str(write_manifest(tmp_path, data)), "--json")
    payload = json.loads(result.stdout)
    assert result.returncode == 1
    assert payload["ok"] is False
    assert any("scope: object required" in error for error in payload["errors"])


def test_supported_claim_requires_evidence(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["claims"][0]["verdict"] = "supported"
    data["claims"][0]["evidence"] = []
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "at least one evidence item is required" in result.stdout


def test_qualified_claim_requires_caveat_gate_and_risk(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    claim = data["claims"][0]
    claim.update(
        {
            "verdict": "qualified",
            "evidence": [
                {
                    "kind": "repo",
                    "locator": "pricing.tsx:1",
                    "verified_by": "reviewer",
                    "observed_at": "2026-08-10T00:00:00-05:00",
                    "sha256": "a" * 64,
                }
            ],
            "risk_ids": [],
        }
    )
    claim.pop("next_gate", None)
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "qualification" in result.stdout
    assert "next_gate" in result.stdout
    assert "unresolved claim must link" in result.stdout


def test_qualified_claim_rejects_self_negating_caveat(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["claims"][0].update(
        {
            "verdict": "qualified",
            "qualification": "No qualification applies.",
            "next_gate": "No further review is needed.",
            "evidence": [
                {
                    "kind": "repo",
                    "locator": "pricing.tsx:1",
                    "verified_by": "reviewer",
                    "observed_at": "2026-08-10T00:00:00-05:00",
                    "sha256": "a" * 64,
                }
            ],
        }
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "must describe a real caveat" in result.stdout
    assert "must describe a real follow-up gate" in result.stdout


def test_qualified_claim_needs_structured_gate_and_open_risk(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    claim = data["claims"][0]
    claim.update(
        {
            "verdict": "qualified",
            "qualification": "Some evidence is incomplete.",
            "next_gate": "Verify the incomplete evidence.",
            "evidence": [
                {
                    "kind": "repo",
                    "locator": "pricing.tsx:1",
                    "verified_by": "reviewer",
                    "observed_at": "2026-08-10T00:00:00-05:00",
                    "sha256": "a" * 64,
                }
            ],
        }
    )
    risk = data["residual_risks"][1]
    risk["status"] = "closed"
    risk["evidence"] = [
        {
            "kind": "test",
            "locator": "tests/pricing.py",
            "verified_by": "reviewer",
            "observed_at": "2026-08-10T00:00:00-05:00",
            "sha256": "b" * 64,
        }
    ]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "qualification_type" in result.stdout
    assert "structured gate" in result.stdout
    assert "non-closed residual risk" in result.stdout


def test_supported_legal_obligation_requires_primary_or_counsel_evidence(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    claim = data["claims"][0]
    claim["type"] = "legal-obligation"
    claim["verdict"] = "supported"
    claim["source_ids"] = []
    claim["evidence"] = [
        {
            "kind": "repo",
            "locator": "terms.tsx:1",
            "verified_by": "test reviewer",
            "observed_at": "2026-08-09T18:00:00-05:00",
            "sha256": "b" * 64,
        }
    ]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "binding source or counsel coverage for every jurisdiction" in result.stdout


def test_non_primary_source_does_not_close_legal_obligation(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["sources"] = [
        {
            "id": "src-guidance",
            "authority": "Example regulator",
            "url": "https://regulator.example/guidance",
            "jurisdiction": "Example",
            "primary": True,
            "authority_type": "regulator-guidance",
            "binding_status": "nonbinding",
            "provision_or_scope": "Nonbinding guidance only",
            "verified_by": "test reviewer",
            "retrieved_at": "2026-08-09T18:00:00-05:00",
            "content_sha256": "a" * 64,
        }
    ]
    claim = data["claims"][0]
    claim["type"] = "legal-obligation"
    claim["verdict"] = "supported"
    claim["source_ids"] = ["src-guidance"]
    claim["evidence"] = [
        {
            "kind": "repo",
            "locator": "terms.tsx:1",
            "verified_by": "test reviewer",
            "observed_at": "2026-08-09T18:00:00-05:00",
            "sha256": "b" * 64,
        }
    ]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "binding source or counsel coverage for every jurisdiction" in result.stdout


def test_malformed_source_reference_fails_closed(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["claims"][0]["source_ids"] = [{"id": "src-ftc-substantiation"}]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "source ids must be strings" in result.stdout


def test_time_sensitive_evidence_requires_timezone(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["claims"][0]["verdict"] = "supported"
    data["claims"][0]["evidence"] = [
        {
            "kind": "repo",
            "locator": "pricing.tsx:1",
            "verified_by": "test reviewer",
            "observed_at": "2026-08-09T18:00:00",
            "sha256": "b" * 64,
        }
    ]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "ISO timestamp required for repo evidence" in result.stdout


def test_supported_closure_overclaim_is_rejected(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["claims"][0]["claim"] = "The service is legally secure."
    data["claims"][0]["verdict"] = "supported"
    data["claims"][0]["evidence"] = [
        {
            "kind": "repo",
            "locator": "security.ts:1",
            "verified_by": "test reviewer",
            "observed_at": "2026-08-09T18:00:00-05:00",
            "sha256": "b" * 64,
        }
    ]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "unsupported closure phrase 'legally secure'" in result.stdout


def test_unverified_overclaim_can_be_recorded(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    assert "fully compliant" in data["claims"][1]["claim"]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 0, result.stdout


def test_contradicted_claim_requires_contrary_evidence(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["claims"][0]["verdict"] = "contradicted"
    data["claims"][0]["evidence"] = []
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "at least one evidence item is required" in result.stdout


def test_wrong_evidence_container_fails_closed(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["claims"][0]["evidence"] = {"kind": "repo"}
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "claims[0].evidence: must be an array" in result.stdout


def test_not_applicable_claim_requires_evidence(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["claims"][0]["verdict"] = "not-applicable"
    data["claims"][0]["evidence"] = []
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "at least one evidence item is required" in result.stdout


def test_not_applicable_control_requires_evidence(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["controls"][0]["status"] = "not-applicable"
    data["controls"][0]["evidence"] = []
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "at least one evidence item is required" in result.stdout


def test_not_applicable_coverage_rejects_unrelated_repo_evidence(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    row = data["coverage"]["issue_areas"][0]
    row.update(
        {
            "status": "not-applicable",
            "basis_kind": "legal-determination",
            "jurisdiction_ids": ["jurisdiction-unresolved"],
            "source_ids": [],
            "evidence": [
                {
                    "kind": "repo",
                    "locator": "README.md:1",
                    "verified_by": "owner",
                    "observed_at": "2026-08-09T18:00:00-05:00",
                    "sha256": "a" * 64,
                }
            ],
        }
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "legal inapplicability needs binding" in result.stdout


def test_claim_source_requires_jurisdiction_nexus(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["scope"]["jurisdictions"].append(
        {
            "id": "jurisdiction-other",
            "name": "Other jurisdiction",
            "status": "unknown",
            "basis": "No verified nexus.",
            "evidence": [],
            "next_gate": "Determine nexus.",
        }
    )
    data["sources"] = [
        {
            "id": "src-other",
            "authority": "Other legislature",
            "url": "https://law.example.test/instrument",
            "jurisdiction": "Other",
            "jurisdiction_ids": ["jurisdiction-other"],
            "primary": True,
            "authority_type": "legislation",
            "binding_status": "binding",
            "provision_or_scope": "Section 1",
            "verified_by": "legal researcher",
            "retrieved_at": "2026-08-09T18:00:00-05:00",
            "content_sha256": "a" * 64,
        }
    ]
    data["claims"][0]["source_ids"] = ["src-other"]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "no declared nexus" in result.stdout


def test_missing_coverage_area_fails_closed(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["coverage"]["claim_surfaces"].pop()
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "missing required coverage ids" in result.stdout


@pytest.mark.parametrize(
    "overclaim",
    [
        "The product has complete legal compliance.",
        "All applicable laws are satisfied.",
        "The product is lawful in every market.",
        "The product is approved to launch.",
        "No material legal gaps remain.",
        "Every gap has been resolved.",
        "The compliance audit is complete.",
    ],
)
def test_completion_overclaim_synonyms_are_rejected(
    valid_manifest: dict, tmp_path: Path, overclaim: str
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["completion_statement"] = (
        f"{overclaim} Overall legal compliance is not claimed."
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "fixed bounded statement" in result.stdout


def test_launch_rationale_overclaim_is_rejected(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["launch_disposition"]["rationale"] = "The product is approved to launch."
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "checker-defined bounded rationale" in result.stdout


def test_open_p0_blocks_ready_disposition(valid_manifest: dict, tmp_path: Path) -> None:
    data = copy.deepcopy(valid_manifest)
    data["launch_disposition"]["status"] = "ready-for-counsel-review"
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "open p0 risks require blocked or limited" in result.stdout


def test_verified_operator_needs_registry_or_counsel(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["scope"]["operator"] = {
        "status": "verified",
        "name": "Example LLC",
        "evidence": [{"kind": "repo", "locator": "config.ts:2"}],
    }
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "registry or counsel evidence" in result.stdout


def test_unknown_jurisdiction_requires_next_gate(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["scope"]["jurisdictions"][0].pop("next_gate")
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "next_gate: required" in result.stdout


def test_not_applicable_jurisdiction_rejects_generic_evidence(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    row = data["scope"]["jurisdictions"][0]
    row.update(
        {
            "status": "not-applicable",
            "basis_kind": "legal-determination",
            "source_ids": [],
            "evidence": [
                {
                    "kind": "repo",
                    "locator": "README.md:1",
                    "verified_by": "owner",
                    "observed_at": "2026-08-09T18:00:00-05:00",
                    "sha256": "a" * 64,
                }
            ],
        }
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert (
        "legal inapplicability needs binding source or counsel coverage"
        in result.stdout
    )


def test_counsel_evidence_requires_jurisdiction_scope(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    claim = data["claims"][0]
    claim.update(
        {
            "type": "legal-obligation",
            "verdict": "supported",
            "evidence": [
                {
                    "kind": "counsel",
                    "locator": "private-record:memo-1",
                    "verified_by": "legal owner",
                    "observed_at": "2026-08-09T18:00:00-05:00",
                    "sha256": "a" * 64,
                }
            ],
        }
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "counsel evidence needs explicit jurisdiction scope" in result.stdout


def test_counsel_evidence_rejects_unknown_jurisdiction_scope(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["scope"]["operator"] = {
        "status": "verified",
        "name": "Mothlight LLC",
        "evidence": [
            {
                "kind": "counsel",
                "locator": "private-record:operator-memo",
                "verified_by": "legal owner",
                "jurisdiction_ids": ["fabricated-jurisdiction"],
                "observed_at": "2026-08-10T00:00:00-05:00",
                "sha256": "a" * 64,
            }
        ],
    }
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "unknown jurisdiction id 'fabricated-jurisdiction'" in result.stdout


def test_legal_claim_needs_coverage_for_every_jurisdiction(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["scope"]["jurisdictions"].append(
        {
            "id": "jurisdiction-second",
            "name": "Second jurisdiction",
            "status": "unknown",
            "basis": "Potential customers.",
            "evidence": [],
            "next_gate": "Determine applicability.",
        }
    )
    data["sources"] = [
        {
            "id": "src-first",
            "authority": "First legislature",
            "url": "https://law.example.test/first",
            "jurisdiction": "First",
            "jurisdiction_ids": ["jurisdiction-unresolved"],
            "primary": True,
            "authority_type": "legislation",
            "binding_status": "binding",
            "provision_or_scope": "Section 1",
            "verified_by": "legal researcher",
            "retrieved_at": "2026-08-09T18:00:00-05:00",
            "content_sha256": "a" * 64,
        }
    ]
    claim = data["claims"][0]
    claim.update(
        {
            "type": "legal-obligation",
            "verdict": "supported",
            "source_ids": ["src-first"],
            "jurisdiction_ids": ["jurisdiction-unresolved", "jurisdiction-second"],
            "evidence": [
                {
                    "kind": "repo",
                    "locator": "policy.ts:1",
                    "verified_by": "reviewer",
                    "observed_at": "2026-08-09T18:00:00-05:00",
                    "sha256": "b" * 64,
                }
            ],
        }
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "coverage for every jurisdiction" in result.stdout


def test_unverified_operator_requires_p0_residual(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["residual_risks"] = []
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "unverified operator requires an explicit p0 operator risk" in result.stdout


def test_unverified_operator_requires_open_p0_residual(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    risk = data["residual_risks"][0]
    risk["status"] = "closed"
    risk["evidence"] = [
        {
            "kind": "registry",
            "locator": "private-record:operator-check",
            "verified_by": "registry reviewer",
            "observed_at": "2026-08-09T18:00:00-05:00",
            "sha256": "a" * 64,
        }
    ]
    data["launch_disposition"]["status"] = "ready-for-counsel-review"
    data["launch_disposition"]["rationale"] = (
        "Engineering evidence is ready for counsel review; no launch or compliance approval is claimed."
    )
    data["completion_statement"] = (
        "Overall legal compliance is not claimed. Launch disposition: "
        "ready-for-counsel-review. See the claim, coverage, control, residual-risk, "
        "and lifecycle records."
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "unverified operator requires an explicit p0 operator risk" in result.stdout


def test_limited_launch_needs_structured_enforced_constraint(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["launch_disposition"].update(
        {
            "status": "limited",
            "rationale": "Launch is limited by the linked residual risks and evidenced enforced constraints.",
            "constraints": ["Everything remains available; no restriction is needed."],
        }
    )
    data["completion_statement"] = (
        "Overall legal compliance is not claimed. Launch disposition: limited. "
        "See the claim, coverage, control, residual-risk, and lifecycle records."
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "constraints[0]: must be an object" in result.stdout


def test_limited_constraint_control_must_link_the_same_risk(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    control = data["controls"][1]
    control["status"] = "implemented"
    control["enforcement_predicate"] = (
        "checkout returns 503 while operator is unverified"
    )
    control.update(
        {
            "effect": "disabled-feature",
            "action": "disable",
            "target": "self-service-checkout",
            "enforced_value": False,
        }
    )
    control["evidence"] = [
        {
            "kind": "test",
            "locator": "tests/security_surface.py",
            "verified_by": "security reviewer",
            "observed_at": "2026-08-09T18:00:00-05:00",
            "sha256": "a" * 64,
        }
    ]
    data["launch_disposition"].update(
        {
            "status": "limited",
            "rationale": "Launch is limited by the linked residual risks and evidenced enforced constraints.",
            "constraints": [
                {
                    "id": "constraint-operator",
                    "restriction": "Self-service sales are disabled.",
                    "effect": "disabled-feature",
                    "action": "disable",
                    "target": "self-service-checkout",
                    "enforced_value": False,
                    "enforcement_predicate": "checkout returns 503 while operator is unverified",
                    "owner": "commercial owner",
                    "control_ids": ["control-security-surface"],
                    "risk_ids": ["risk-operator-unverified"],
                    "evidence": [
                        {
                            "kind": "test",
                            "locator": "tests/checkout_gate.py",
                            "verified_by": "commercial reviewer",
                            "observed_at": "2026-08-09T18:00:00-05:00",
                            "sha256": "b" * 64,
                        }
                    ],
                }
            ],
        }
    )
    data["completion_statement"] = (
        "Overall legal compliance is not claimed. Launch disposition: limited. "
        "See the claim, coverage, control, residual-risk, and lifecycle records."
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "no referenced implemented control is linked" in result.stdout


def test_limited_constraint_ids_must_be_strings(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["launch_disposition"].update(
        {
            "status": "limited",
            "rationale": "Launch is limited by the linked residual risks and evidenced enforced constraints.",
            "constraints": [
                {
                    "id": "constraint-bad-ids",
                    "restriction": "Checkout is disabled.",
                    "effect": "disabled-feature",
                    "action": "disable",
                    "target": "checkout",
                    "enforced_value": False,
                    "enforcement_predicate": "checkout is disabled",
                    "owner": "commercial owner",
                    "control_ids": [{"id": "control-self-service-sales"}],
                    "risk_ids": [{"id": "risk-operator-unverified"}],
                    "evidence": [
                        {
                            "kind": "test",
                            "locator": "tests/checkout.py",
                            "verified_by": "reviewer",
                            "observed_at": "2026-08-10T00:00:00-05:00",
                            "sha256": "a" * 64,
                        }
                    ],
                }
            ],
        }
    )
    data["completion_statement"] = (
        "Overall legal compliance is not claimed. Launch disposition: limited. "
        "See the claim, coverage, control, residual-risk, and lifecycle records."
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "control ids must be strings" in result.stdout
    assert "risk ids must be strings" in result.stdout


def test_limited_constraint_rejects_non_limiting_prose(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    control = data["controls"][0]
    control.update(
        {
            "status": "implemented",
            "enforcement_predicate": "checkout disabled",
            "effect": "disabled-feature",
            "action": "disable",
            "target": "checkout",
            "enforced_value": False,
            "evidence": [
                {
                    "kind": "test",
                    "locator": "tests/checkout.py",
                    "verified_by": "reviewer",
                    "observed_at": "2026-08-10T00:00:00-05:00",
                    "sha256": "a" * 64,
                }
            ],
        }
    )
    data["launch_disposition"].update(
        {
            "status": "limited",
            "rationale": "Launch is limited by the linked residual risks and evidenced enforced constraints.",
            "constraints": [
                {
                    "id": "constraint-contradictory",
                    "restriction": "Commercial operation proceeds without limitation.",
                    "effect": "disabled-feature",
                    "action": "disable",
                    "target": "checkout",
                    "enforced_value": False,
                    "enforcement_predicate": "checkout disabled",
                    "owner": "commercial owner",
                    "control_ids": ["control-self-service-sales"],
                    "risk_ids": ["risk-operator-unverified"],
                    "evidence": [
                        {
                            "kind": "test",
                            "locator": "tests/checkout.py",
                            "verified_by": "reviewer",
                            "observed_at": "2026-08-10T00:00:00-05:00",
                            "sha256": "b" * 64,
                        }
                    ],
                }
            ],
        }
    )
    data["completion_statement"] = (
        "Overall legal compliance is not claimed. Launch disposition: limited. "
        "See the claim, coverage, control, residual-risk, and lifecycle records."
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "must describe an actual limiting condition" in result.stdout


def test_limited_constraint_rejects_enabled_disable_tuple(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    control = data["controls"][0]
    control.update(
        {
            "status": "implemented",
            "effect": "disabled-feature",
            "action": "disable",
            "target": "self-service-checkout",
            "enforced_value": True,
            "enforcement_predicate": "checkout enabled for every request",
            "evidence": [
                {
                    "kind": "test",
                    "locator": "tests/checkout.py",
                    "verified_by": "reviewer",
                    "observed_at": "2026-08-10T00:00:00-05:00",
                    "sha256": "a" * 64,
                }
            ],
        }
    )
    data["launch_disposition"].update(
        {
            "status": "limited",
            "rationale": "Launch is limited by the linked residual risks and evidenced enforced constraints.",
            "constraints": [
                {
                    "id": "constraint-enabled",
                    "restriction": "Checkout state is enforced.",
                    "effect": "disabled-feature",
                    "action": "disable",
                    "target": "self-service-checkout",
                    "enforced_value": True,
                    "enforcement_predicate": "checkout enabled for every request",
                    "owner": "commercial owner",
                    "control_ids": ["control-self-service-sales"],
                    "risk_ids": ["risk-operator-unverified"],
                    "evidence": [
                        {
                            "kind": "test",
                            "locator": "tests/checkout.py",
                            "verified_by": "reviewer",
                            "observed_at": "2026-08-10T00:00:00-05:00",
                            "sha256": "b" * 64,
                        }
                    ],
                }
            ],
        }
    )
    data["completion_statement"] = (
        "Overall legal compliance is not claimed. Launch disposition: limited. "
        "See the claim, coverage, control, residual-risk, and lifecycle records."
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "do not form a limiting tuple" in result.stdout


def test_all_evidence_kinds_require_timestamp_and_digest(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["claims"][0]["verdict"] = "supported"
    data["claims"][0]["evidence"] = [
        {"kind": "other", "locator": "owner assertion", "verified_by": "owner"}
    ]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "observed_at" in result.stdout
    assert "sha256" in result.stdout


def test_stale_evidence_and_source_retrieval_are_rejected(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["claims"][0].update(
        {
            "verdict": "supported",
            "evidence": [
                {
                    "kind": "repo",
                    "locator": "pricing.tsx:1",
                    "verified_by": "reviewer",
                    "observed_at": "2000-01-01T00:00:00Z",
                    "sha256": "a" * 64,
                }
            ],
        }
    )
    data["sources"] = [
        {
            "id": "src-stale",
            "authority": "Legislature",
            "url": "https://law.example.test/instrument",
            "jurisdiction": "Unresolved",
            "jurisdiction_ids": ["jurisdiction-unresolved"],
            "primary": True,
            "authority_type": "legislation",
            "binding_status": "binding",
            "provision_or_scope": "Section 1",
            "verified_by": "researcher",
            "retrieved_at": "2000-01-01T00:00:00Z",
            "content_sha256": "b" * 64,
        }
    ]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "re-observed within 370 days" in result.stdout
    assert "source must be rechecked within 370 days" in result.stdout


def test_template_flag_flip_does_not_clear_placeholders(tmp_path: Path) -> None:
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    data["project"]["template"] = False
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "template_marker" in result.stdout
    assert "placeholder value" in result.stdout


def test_malformed_source_url_is_rejected(valid_manifest: dict, tmp_path: Path) -> None:
    data = copy.deepcopy(valid_manifest)
    data["sources"] = [
        {
            "id": "src-bogus",
            "authority": "Bogus",
            "url": "https:bogus",
            "jurisdiction": "Unresolved",
            "jurisdiction_ids": ["jurisdiction-unresolved"],
            "primary": False,
            "authority_type": "other",
            "binding_status": "unknown",
            "provision_or_scope": "none",
            "verified_by": "reviewer",
            "retrieved_at": "2026-08-09T18:00:00-05:00",
            "content_sha256": "a" * 64,
        }
    ]
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "absolute HTTP(S) URL required" in result.stdout


def test_sector_specific_coverage_extension_is_allowed(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["coverage"]["issue_areas"].append(
        {
            "id": "sector:health-medical-device",
            "description": "Medical-device and health-data regimes",
            "status": "not-audited",
            "owner": "Health counsel",
            "evidence": [],
            "next_gate": "Determine whether product behavior triggers a regulated health regime.",
        }
    )
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 0, result.stdout


def test_probe_resolves_once_and_connects_only_to_validated_address(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    module = load_script_module()
    dns_calls = 0
    connection_targets: list[tuple[str, int]] = []

    def fake_getaddrinfo(*args, **kwargs):
        nonlocal dns_calls
        dns_calls += 1
        address = "93.184.216.34" if dns_calls == 1 else "127.0.0.1"
        return [(2, 1, 6, "", (address, 80))]

    def fake_create_connection(target, timeout):
        connection_targets.append(target)
        raise OSError("stop after target selection")

    monkeypatch.setattr(module.socket, "getaddrinfo", fake_getaddrinfo)
    monkeypatch.setattr(module.socket, "create_connection", fake_create_connection)
    with pytest.raises(OSError):
        module._pinned_request(
            "http://rebind.example/terms",
            timeout=1,
            allow_private_network=False,
        )
    assert dns_calls == 1
    assert connection_targets == [("93.184.216.34", 80)]


@pytest.mark.parametrize("timeout", ["nan", "inf", "-1", "0"])
def test_probe_rejects_non_finite_or_nonpositive_timeout(
    valid_manifest: dict, tmp_path: Path, timeout: str
) -> None:
    result = run_cli(
        "probe",
        str(write_manifest(tmp_path, valid_manifest)),
        "--timeout",
        timeout,
    )
    assert result.returncode == 2
    assert "finite positive number" in result.stderr


def test_deployed_state_requires_full_receipt_chain(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["lifecycle"] = {
        "state": "deployed",
        "receipts": [
            {
                "kind": "deployment",
                "locator": "https://deploy.example/1",
                "observed_at": "2026-08-09T18:00:00-05:00",
            }
        ],
    }
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "requires receipt kinds" in result.stdout
    assert "pull-request" in result.stdout


def test_future_lifecycle_receipt_is_rejected(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["lifecycle"] = {
        "state": "committed",
        "receipts": [
            {
                "kind": "commit",
                "locator": "deadbeef",
                "observed_at": "2099-08-09T18:00:00-05:00",
                "issuer": "test harness",
                "sha256": "a" * 64,
            }
        ],
    }
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "future receipt is not evidence" in result.stdout


def test_lifecycle_receipts_must_share_release_and_order(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["lifecycle"] = {
        "state": "merged",
        "release_id": "release-42",
        "receipts": [
            {
                "kind": "commit",
                "locator": "a" * 40,
                "release_id": "release-42",
                "observed_at": "2026-08-09T20:00:00-05:00",
                "issuer": "git",
                "sha256": "a" * 64,
            },
            {
                "kind": "pull-request",
                "locator": "https://github.com/mothlight/notes/pull/42",
                "release_id": "different-release",
                "observed_at": "2026-08-09T19:00:00-05:00",
                "issuer": "github",
                "sha256": "b" * 64,
            },
            {
                "kind": "merge",
                "locator": "c" * 40,
                "release_id": "release-42",
                "observed_at": "2026-08-09T21:00:00-05:00",
                "issuer": "github",
                "sha256": "c" * 64,
            },
        ],
    }
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "must match lifecycle.release_id" in result.stdout
    assert "must follow commit, PR, merge" in result.stdout


def test_non_string_expected_content_type_is_rejected(
    valid_manifest: dict, tmp_path: Path
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["surfaces"][0]["expect_content_type"] = 123
    result = run_cli("check", str(write_manifest(tmp_path, data)))
    assert result.returncode == 1
    assert "expect_content_type: non-empty string required" in result.stdout


def test_init_copies_example_and_refuses_overwrite(tmp_path: Path) -> None:
    output = tmp_path / "nested" / "legal-readiness.json"
    first = run_cli("init", str(output))
    second = run_cli("init", str(output))
    forced = run_cli("init", str(output), "--force")
    assert first.returncode == 0
    assert second.returncode == 2
    assert forced.returncode == 0
    assert json.loads(output.read_text(encoding="utf-8"))["schema_version"] == 1


class _SurfaceHandler(BaseHTTPRequestHandler):
    requested_paths: ClassVar[list[str]] = []
    redirect_target: str | None = None

    def do_GET(self) -> None:
        self.__class__.requested_paths.append(self.path)
        if self.path == "/terms":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"terms")
            return
        if self.path == "/.well-known/security.txt":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Contact: mailto:security@example.com")
            return
        if self.path == "/redirected-terms":
            self.send_response(302)
            self.send_header("Location", "/terms")
            self.end_headers()
            return
        if self.path == "/cross-origin":
            self.send_response(302)
            self.send_header("Location", str(self.__class__.redirect_target))
            self.end_headers()
            return
        self.send_response(404)
        self.end_headers()

    def log_message(self, format: str, *args: object) -> None:
        return


@pytest.fixture()
def surface_server() -> str:
    _SurfaceHandler.requested_paths = []
    _SurfaceHandler.redirect_target = None
    server = ThreadingHTTPServer(("127.0.0.1", 0), _SurfaceHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join(timeout=2)
        server.server_close()


def test_probe_emits_bounded_receipt(
    valid_manifest: dict, tmp_path: Path, surface_server: str
) -> None:
    manifest = write_manifest(tmp_path, valid_manifest)
    receipt = tmp_path / "receipt.json"
    result = run_cli(
        "probe",
        str(manifest),
        "--base-url",
        surface_server,
        "--allow-private-network",
        "--output",
        str(receipt),
    )
    payload = json.loads(receipt.read_text(encoding="utf-8"))
    assert result.returncode == 0, result.stdout + result.stderr
    assert payload["ok"] is True
    assert len(payload["observations"]) == 2
    assert "does not establish" in payload["boundary"]
    assert len(payload["manifest_sha256"]) == 64
    assert len(payload["expectations_sha256"]) == 64


def test_probe_fails_on_missing_required_header(
    valid_manifest: dict, tmp_path: Path, surface_server: str
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["surfaces"][0]["expect_headers"] = {"X-Required": "present"}
    manifest = write_manifest(tmp_path, data)
    result = run_cli(
        "probe",
        str(manifest),
        "--base-url",
        surface_server,
        "--allow-private-network",
    )
    payload = json.loads(result.stdout)
    assert result.returncode == 1
    assert payload["ok"] is False
    assert "missing header X-Required" in payload["observations"][0]["errors"]


def test_probe_rejects_redirect_by_default(
    valid_manifest: dict, tmp_path: Path, surface_server: str
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["surfaces"] = [
        {
            "path": "/redirected-terms",
            "expect_status": 200,
            "expect_content_type": "text/html",
            "expect_headers": {},
        }
    ]
    result = run_cli(
        "probe",
        str(write_manifest(tmp_path, data)),
        "--base-url",
        surface_server,
        "--allow-private-network",
    )
    payload = json.loads(result.stdout)
    assert result.returncode == 1
    assert "got 302" in payload["observations"][0]["errors"][0]
    assert "/terms" not in _SurfaceHandler.requested_paths


def test_probe_allows_declared_same_origin_redirect(
    valid_manifest: dict, tmp_path: Path, surface_server: str
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["surfaces"] = [
        {
            "path": "/redirected-terms",
            "expect_status": 200,
            "expect_content_type": "text/html",
            "expect_headers": {},
            "allow_redirects": True,
        }
    ]
    result = run_cli(
        "probe",
        str(write_manifest(tmp_path, data)),
        "--base-url",
        surface_server,
        "--allow-private-network",
    )
    payload = json.loads(result.stdout)
    assert result.returncode == 0
    assert payload["observations"][0]["final_url"].endswith("/terms")
    assert "/terms" in _SurfaceHandler.requested_paths


def test_probe_accepts_declared_http_error_status(
    valid_manifest: dict, tmp_path: Path, surface_server: str
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["surfaces"] = [
        {
            "path": "/not-found",
            "expect_status": 404,
            "expect_headers": {},
        }
    ]
    result = run_cli(
        "probe",
        str(write_manifest(tmp_path, data)),
        "--base-url",
        surface_server,
        "--allow-private-network",
    )
    payload = json.loads(result.stdout)
    assert result.returncode == 0
    assert payload["observations"][0]["status"] == 404


def test_probe_checks_headers_on_declared_http_error(
    valid_manifest: dict, tmp_path: Path, surface_server: str
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["surfaces"] = [
        {
            "path": "/not-found",
            "expect_status": 404,
            "expect_headers": {"X-Required": "present"},
        }
    ]
    result = run_cli(
        "probe",
        str(write_manifest(tmp_path, data)),
        "--base-url",
        surface_server,
        "--allow-private-network",
    )
    payload = json.loads(result.stdout)
    assert result.returncode == 1
    assert "missing header X-Required" in payload["observations"][0]["errors"]


def test_probe_refuses_private_network_without_explicit_opt_in(
    valid_manifest: dict, tmp_path: Path, surface_server: str
) -> None:
    result = run_cli(
        "probe",
        str(write_manifest(tmp_path, valid_manifest)),
        "--base-url",
        surface_server,
    )
    assert result.returncode == 2
    assert "non-global target refused" in result.stderr
    assert _SurfaceHandler.requested_paths == []


def test_probe_refuses_invalid_absolute_surface_before_network(
    valid_manifest: dict, tmp_path: Path, surface_server: str
) -> None:
    data = copy.deepcopy(valid_manifest)
    data["surfaces"] = [
        {
            "path": "http://127.0.0.1:9/escaped",
            "expect_status": 200,
            "expect_headers": {},
        }
    ]
    result = run_cli(
        "probe",
        str(write_manifest(tmp_path, data)),
        "--base-url",
        surface_server,
        "--allow-private-network",
    )
    assert result.returncode == 2
    assert "same-origin route" in result.stderr
    assert _SurfaceHandler.requested_paths == []


def test_probe_refuses_cross_origin_redirect_before_second_request(
    valid_manifest: dict, tmp_path: Path, surface_server: str
) -> None:
    target_hits: list[str] = []

    class _TargetHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            target_hits.append(self.path)
            self.send_response(200)
            self.end_headers()

        def log_message(self, format: str, *args: object) -> None:
            return

    target_server = ThreadingHTTPServer(("127.0.0.1", 0), _TargetHandler)
    target_thread = threading.Thread(target=target_server.serve_forever, daemon=True)
    target_thread.start()
    try:
        _SurfaceHandler.redirect_target = (
            f"http://127.0.0.1:{target_server.server_port}/escaped"
        )
        data = copy.deepcopy(valid_manifest)
        data["surfaces"] = [
            {
                "path": "/cross-origin",
                "expect_status": 200,
                "expect_headers": {},
                "allow_redirects": True,
            }
        ]
        result = run_cli(
            "probe",
            str(write_manifest(tmp_path, data)),
            "--base-url",
            surface_server,
            "--allow-private-network",
        )
    finally:
        target_server.shutdown()
        target_thread.join(timeout=2)
        target_server.server_close()
    payload = json.loads(result.stdout)
    assert result.returncode == 1
    assert "cross-origin redirect refused" in payload["observations"][0]["errors"][0]
    assert target_hits == []


def test_probe_refuses_receipt_overwrite_without_force(
    valid_manifest: dict, tmp_path: Path, surface_server: str
) -> None:
    manifest = write_manifest(tmp_path, valid_manifest)
    receipt = tmp_path / "receipt.json"
    first = run_cli(
        "probe",
        str(manifest),
        "--base-url",
        surface_server,
        "--allow-private-network",
        "--output",
        str(receipt),
    )
    original = receipt.read_bytes()
    second = run_cli(
        "probe",
        str(manifest),
        "--base-url",
        surface_server,
        "--allow-private-network",
        "--output",
        str(receipt),
    )
    assert first.returncode == 0
    assert second.returncode == 2
    assert "refusing to overwrite" in second.stderr
    assert receipt.read_bytes() == original


# --------------------------------------------------------------------------
# Adversarial suite (BRO-2265). The skill's stated boundary is an audit
# "without claiming compliance or replacing counsel". These cases attack that
# boundary directly rather than exercising the happy path, because the defect
# they were written for produced PASS and exit 0 on a manifest asserting GDPR
# compliance with zero legal sources and every coverage row `not-audited`.
# --------------------------------------------------------------------------

COMPLIANCE_ASSERTIONS = [
    "The service is GDPR compliant.",
    "We are fully SOC 2 compliant.",
    "The platform remains PCI DSS compliant.",
    "The product complies with the DSA.",
    "Our processing is in compliance with UK GDPR.",
    "The service meets all statutory requirements.",
    "Storing this data is lawful.",
    "The banner does not violate the ePrivacy Directive.",
    "No further legal review is required.",
]

NON_LEGAL_CLAIMS = [
    "The public credit allocation matches billing enforcement.",
    "Checkout is disabled pending operator verification.",
    "The pricing page lists three plans.",
    "We ship a compliance-readiness checklist as a reference doc.",
    "Counsel review is scheduled for Q3.",
]


def _sole_claim(manifest: dict, text: str, claim_type: str = "factual") -> dict:
    manifest = copy.deepcopy(manifest)
    manifest["claims"] = [{
        "id": "claim-under-test",
        "claim": text,
        "surface": "public marketing",
        "type": claim_type,
        "verdict": "supported",
        "applicability": "All users.",
        "jurisdiction_ids": ["jurisdiction-unresolved"],
        "source_ids": [],
        "evidence": [{
            "kind": "repo",
            "locator": "docs/note.md",
            "sha256": "a" * 64,
            "observed_at": "2026-08-23T00:00:00Z",
            "verified_by": "Founder",
        }],
        "risk_ids": [],
        "owner": "Founder",
        "next_gate": "None.",
    }]
    return manifest


@pytest.mark.parametrize("text", COMPLIANCE_ASSERTIONS)
def test_a_compliance_assertion_cannot_be_supported_by_relabelling_its_type(
    valid_manifest: dict, tmp_path: Path, text: str
) -> None:
    """Every legal guard in the script keys off `type == "legal-obligation"`,
    and the type is author-supplied. Typing a compliance assertion `factual`
    skipped the binding-source requirement entirely, so the boundary was opt-in
    by the party it constrains."""
    result = run_cli("check", str(write_manifest(tmp_path, _sole_claim(valid_manifest, text))))
    assert result.returncode != 0, result.stdout
    assert "legal-obligation" in result.stdout


@pytest.mark.parametrize("text", NON_LEGAL_CLAIMS)
def test_an_ordinary_claim_is_not_forced_into_the_legal_path(
    valid_manifest: dict, tmp_path: Path, text: str
) -> None:
    """POSITIVE CONTROL. Without it the rule above is satisfied by a check that
    rejects every claim, which would make the skill unusable for the commercial
    and factual claims it exists to inventory."""
    manifest = _sole_claim(valid_manifest, text)
    result = run_cli("check", str(write_manifest(tmp_path, manifest)))
    assert "must be typed 'legal-obligation'" not in result.stdout, result.stdout


def test_ready_for_counsel_review_needs_at_least_one_source(
    valid_manifest: dict, tmp_path: Path
) -> None:
    manifest = copy.deepcopy(valid_manifest)
    manifest["sources"] = []
    manifest["launch_disposition"]["status"] = "ready-for-counsel-review"
    result = run_cli("check", str(write_manifest(tmp_path, manifest)))
    assert result.returncode != 0
    assert "at least one source" in result.stdout


def test_ready_for_counsel_review_needs_an_audited_surface(
    valid_manifest: dict, tmp_path: Path
) -> None:
    """Every surface `not-audited` means the review examined nothing, which must
    not produce the same disposition as a review that examined everything."""
    manifest = copy.deepcopy(valid_manifest)
    for row in manifest["coverage"]["claim_surfaces"]:
        row["status"] = "not-audited"
    manifest["launch_disposition"]["status"] = "ready-for-counsel-review"
    result = run_cli("check", str(write_manifest(tmp_path, manifest)))
    assert result.returncode != 0
    assert "not-audited" in result.stdout


def test_ready_for_counsel_review_rejects_unresolved_claims(
    valid_manifest: dict, tmp_path: Path
) -> None:
    manifest = copy.deepcopy(valid_manifest)
    manifest["claims"][0]["verdict"] = "unverified"
    manifest["launch_disposition"]["status"] = "ready-for-counsel-review"
    result = run_cli("check", str(write_manifest(tmp_path, manifest)))
    assert result.returncode != 0
    assert "unresolved" in result.stdout


def test_the_bundled_example_still_passes(valid_manifest: dict, tmp_path: Path) -> None:
    """POSITIVE CONTROL for all four gates above: they must reject the
    adversarial shapes without rejecting the shipped example, or the skill
    cannot be used at all."""
    result = run_cli("check", str(write_manifest(tmp_path, valid_manifest)))
    assert result.returncode == 0, result.stdout + result.stderr
