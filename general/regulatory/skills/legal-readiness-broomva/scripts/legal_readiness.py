#!/usr/bin/env python3
"""Deterministic checks for an evidence-first legal-readiness record.

This tool validates evidence structure and probes declared web surfaces. It does
not decide which law applies, interpret legal text, or issue a legal opinion.
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import ipaddress
import itertools
import json
import math
import re
import shutil
import socket
import ssl
import sys
import urllib.error
import urllib.parse
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

VERDICTS = {
    "supported",
    "qualified",
    "contradicted",
    "unverified",
    "not-audited",
    "not-applicable",
}
CLAIM_TYPES = {
    "factual",
    "legal-obligation",
    "commercial",
    "security-control",
    "recommendation",
}
CONTROL_STATUSES = {
    "implemented",
    "partial",
    "open",
    "blocked-external",
    "not-applicable",
}
JURISDICTION_STATUSES = {"applicable", "potential", "not-applicable", "unknown"}
COVERAGE_STATUSES = {"audited", "not-audited", "not-applicable"}
CLAIM_SURFACE_AREAS = {
    "audit-handoffs",
    "code-config-tests",
    "legal-policies",
    "machine-readable-docs",
    "pricing-checkout",
    "product-ui-api",
    "public-marketing",
    "sales-contracts",
    "security-disclosures",
    "signup-auth-consent",
    "vendors-operations",
    "historical-state",
}
ISSUE_AREA_IDS = {
    "accessibility-marketing-export",
    "ai-transparency-safety",
    "children-minors",
    "insurance-msa-dpa-sla",
    "ip-open-source",
    "operator-authority",
    "payments-renewals",
    "privacy-authorization",
    "product-commercial-claims",
    "retention-rights",
    "security-incidents",
    "tax-registrations",
    "terms-assent",
    "vendors-transfers",
}
SOURCE_AUTHORITY_TYPES = {
    "legislation",
    "regulation",
    "court",
    "regulator-guidance",
    "standard",
    "counsel",
    "contract",
    "other",
}
BINDING_STATUSES = {"binding", "nonbinding", "unknown", "not-applicable"}
LAUNCH_STATUSES = {"blocked", "limited", "ready-for-counsel-review", "not-assessed"}
LIFECYCLE_STATES = (
    "worktree",
    "committed",
    "pr-open",
    "merged",
    "deployed",
    "live-verified",
)
RECEIPT_REQUIREMENTS = {
    "committed": {"commit"},
    "pr-open": {"commit", "pull-request"},
    "merged": {"commit", "pull-request", "merge"},
    "deployed": {"commit", "pull-request", "merge", "deployment"},
    "live-verified": {"commit", "pull-request", "merge", "deployment", "live-probe"},
}
#: Claim TEXT that asserts legal compliance, lawfulness, or legal advice.
#:
#: The `type` field is author-supplied, and every legal guard in this file hangs
#: off `type == "legal-obligation"`. So a claim reading "The service is GDPR
#: compliant." typed `factual` skipped the binding-source requirement entirely
#: and validated as `supported` with zero legal sources — the tool's stated
#: boundary ("without claiming compliance") broken by relabelling a field.
#:
#: Detected on what the claim SAYS, because that is what a reader acts on; the
#: declared type is a routing hint, not evidence about the sentence.
LEGAL_ASSERTION_PATTERNS = {
    "compliance assertion": re.compile(
        # up to three intervening words so "is GDPR compliant", "is fully SOC 2
        # compliant" and "remains PCI DSS compliant" are all caught -- the
        # framework name sits exactly there, and a pattern that only allowed
        # "fully"/"now" missed every real-world phrasing of this claim
        r"\b(?:is|are|remains?|stays?)\s+(?:\S+\s+){0,3}compliant\b"
        r"|\bcompl(?:ies|y|iant)\s+with\b"
        r"|\bin\s+compliance\s+with\b"
        r"|\bmeets?\s+(?:all\s+)?(?:the\s+)?(?:legal\s+|regulatory\s+|statutory\s+)"
        r"(?:requirements?|obligations?|duties)\b",
        re.IGNORECASE,
    ),
    "lawfulness assertion": re.compile(
        r"\b(?:is|are)\s+(?:legal|lawful|permitted by law|authorised by law|authorized by law)\b"
        r"|\bdoes not (?:violate|breach|infringe)\b"
        r"|\bno (?:legal )?liability\b",
        re.IGNORECASE,
    ),
    "legal advice": re.compile(
        r"\b(?:you|we|the company) (?:may|can|are entitled to) lawfully\b"
        r"|\bno (?:further )?legal review (?:is )?(?:required|needed)\b",
        re.IGNORECASE,
    ),
}


FORBIDDEN_CLOSURE_PATTERNS = {
    "legally secure": re.compile(r"\blegally secure\b", re.IGNORECASE),
    "fully compliant": re.compile(r"\bfully compliant\b", re.IGNORECASE),
    "verified compliance": re.compile(
        r"\bverified (?:legal )?compliance\b", re.IGNORECASE
    ),
    "all gaps fixed": re.compile(
        r"\ball (?:identified )?gaps? (?:are )?(?:fixed|closed)\b", re.IGNORECASE
    ),
    "compliance guaranteed": re.compile(
        r"\bcompliance (?:is )?guaranteed\b", re.IGNORECASE
    ),
    "zero vulnerabilities": re.compile(r"\bzero vulnerabilities\b", re.IGNORECASE),
    "legal standing configured": re.compile(
        r"\blegal standing (?:is )?configured\b", re.IGNORECASE
    ),
    "complete legal compliance": re.compile(
        r"\bcomplete legal compliance\b", re.IGNORECASE
    ),
    "all laws satisfied": re.compile(
        r"\b(?:all applicable laws? (?:are )?satisfied|complies? with all applicable laws?)\b",
        re.IGNORECASE,
    ),
    "lawful in every market": re.compile(r"\blawful in every market\b", re.IGNORECASE),
    "approved to launch": re.compile(r"\bapproved to launch\b", re.IGNORECASE),
    "no material legal gaps": re.compile(
        r"\bno material legal gaps? (?:remain|exists?)?\b", re.IGNORECASE
    ),
    "every gap resolved": re.compile(
        r"\bevery gap (?:is |has been )?resolved\b", re.IGNORECASE
    ),
    "audit complete": re.compile(
        r"\b(?:legal |compliance )?audit (?:is )?complete\b", re.IGNORECASE
    ),
    "no legal issues or launch risks": re.compile(
        r"\bno (?:material )?(?:legal issues?|launch risks?)\b", re.IGNORECASE
    ),
    "every duty conclusively met": re.compile(
        r"\b(?:all|every) (?:governing |applicable |legal )?(?:dut(?:y|ies)|requirements?|obligations?) (?:has |have )?(?:been )?(?:conclusively )?(?:met|satisfied)\b",
        re.IGNORECASE,
    ),
    "legal guarantee": re.compile(
        r"\b(?:guarantee[ds]?|definitive binding legal opinion)\b", re.IGNORECASE
    ),
}
EVIDENCE_KINDS = {
    "repo",
    "live",
    "test",
    "law",
    "regulator",
    "registry",
    "contract",
    "counsel",
    "dashboard",
    "policy",
    "invoice",
    "other",
}
TIME_SENSITIVE_EVIDENCE = EVIDENCE_KINDS
HASH_REQUIRED_EVIDENCE = EVIDENCE_KINDS
SHA256_RE = re.compile(r"^[0-9a-f]{64}$", re.IGNORECASE)
MAX_CLOCK_SKEW = timedelta(minutes=5)
MAX_EVIDENCE_AGE = timedelta(days=370)
CUSTOM_COVERAGE_ID_RE = re.compile(r"^(?:sector|custom):[a-z0-9][a-z0-9-]*$")
LEGAL_BOUNDARY_STATEMENT = (
    "This record organizes engineering and legal issue spotting. It is not legal "
    "advice or a legal opinion, does not approve launch, and does not replace "
    "licensed counsel."
)
LAUNCH_RATIONALES = {
    "blocked": "Launch is blocked by the linked residual risks.",
    "limited": "Launch is limited by the linked residual risks and evidenced enforced constraints.",
    "ready-for-counsel-review": "Engineering evidence is ready for counsel review; no launch or compliance approval is claimed.",
    "not-assessed": "Launch has not been assessed.",
}
CONSTRAINT_EFFECTS = {
    "disabled-feature",
    "geofenced-territory",
    "blocked-processing",
    "read-only-mode",
    "restricted-customer-type",
    "restricted-channel",
}
CONSTRAINT_ACTIONS = {"deny", "disable", "geofence", "read-only", "restrict"}
PLACEHOLDER_MARKER = "REMOVE-BEFORE-VALIDATION"
PLACEHOLDER_VALUES = {
    "Replace with project name",
    "https://github.com/example/example-project",
    "https://example.com",
}


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ValueError(f"cannot read {path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise TypeError("manifest root must be a JSON object")
    return data


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _iso_datetime(value: Any) -> bool:
    if not _nonempty(value):
        return False
    try:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return False
    return parsed.tzinfo is not None


def _future_datetime(value: Any) -> bool:
    if not _iso_datetime(value):
        return False
    parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    return parsed.astimezone(timezone.utc) > datetime.now(timezone.utc) + MAX_CLOCK_SKEW


def _stale_datetime(value: Any) -> bool:
    if not _iso_datetime(value):
        return False
    parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    return (
        parsed.astimezone(timezone.utc) < datetime.now(timezone.utc) - MAX_EVIDENCE_AGE
    )


def _list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _absolute_http_url(value: Any) -> bool:
    if not _nonempty(value):
        return False
    parsed = urllib.parse.urlparse(str(value))
    return (
        parsed.scheme in {"http", "https"}
        and bool(parsed.hostname)
        and bool(parsed.netloc)
        and parsed.username is None
        and parsed.password is None
    )


def _validate_evidence(
    evidence: Any,
    path: str,
    errors: list[str],
    *,
    required: bool = False,
) -> list[dict[str, Any]]:
    if evidence is None:
        rows: list[Any] = []
    elif not isinstance(evidence, list):
        errors.append(f"{path}: must be an array")
        return []
    else:
        rows = evidence
    if required and not rows:
        errors.append(f"{path}: at least one evidence item is required")
    for index, item in enumerate(rows):
        item_path = f"{path}[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{item_path}: must be an object")
            continue
        kind = item.get("kind")
        if kind not in EVIDENCE_KINDS:
            errors.append(f"{item_path}.kind: expected one of {sorted(EVIDENCE_KINDS)}")
        if not _nonempty(item.get("locator")):
            errors.append(f"{item_path}.locator: non-empty locator required")
        if not _nonempty(item.get("verified_by")):
            errors.append(f"{item_path}.verified_by: accountable verifier required")
        if kind in TIME_SENSITIVE_EVIDENCE and not _iso_datetime(
            item.get("observed_at")
        ):
            errors.append(
                f"{item_path}.observed_at: ISO timestamp required for {kind} evidence"
            )
        elif kind in TIME_SENSITIVE_EVIDENCE and _future_datetime(
            item.get("observed_at")
        ):
            errors.append(
                f"{item_path}.observed_at: future observation is not evidence"
            )
        elif kind in TIME_SENSITIVE_EVIDENCE and _stale_datetime(
            item.get("observed_at")
        ):
            errors.append(
                f"{item_path}.observed_at: evidence must be re-observed within 370 days"
            )
        if kind in HASH_REQUIRED_EVIDENCE and not SHA256_RE.fullmatch(
            str(item.get("sha256", ""))
        ):
            errors.append(
                f"{item_path}.sha256: 64-character artifact digest required for {kind}"
            )
        if kind == "counsel":
            jurisdiction_ids = item.get("jurisdiction_ids")
            if (
                not isinstance(jurisdiction_ids, list)
                or not jurisdiction_ids
                or not all(_nonempty(ref) for ref in jurisdiction_ids)
            ):
                errors.append(
                    f"{item_path}.jurisdiction_ids: counsel evidence needs explicit jurisdiction scope"
                )
    return [row for row in rows if isinstance(row, dict)]


def _validate_unique_ids(
    rows: Any, path: str, errors: list[str]
) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    seen: set[str] = set()
    if not isinstance(rows, list):
        errors.append(f"{path}: must be an array")
        return output
    for index, row in enumerate(rows):
        row_path = f"{path}[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{row_path}: must be an object")
            continue
        row_id = row.get("id")
        if not _nonempty(row_id):
            errors.append(f"{row_path}.id: non-empty id required")
        elif row_id in seen:
            errors.append(f"{row_path}.id: duplicate id {row_id!r}")
        else:
            seen.add(row_id)
        output.append(row)
    return output


def _record_indexes(
    data: dict[str, Any],
) -> tuple[dict[str, dict[str, Any]], set[str]]:
    sources = {
        row.get("id"): row
        for row in _list(data.get("sources"))
        if isinstance(row, dict) and _nonempty(row.get("id"))
    }
    scope = data.get("scope")
    scope_rows = scope.get("jurisdictions") if isinstance(scope, dict) else []
    jurisdictions = {
        row.get("id")
        for row in _list(scope_rows)
        if isinstance(row, dict) and _nonempty(row.get("id"))
    }
    return sources, jurisdictions


def _validate_reference_ids(
    row: dict[str, Any],
    path: str,
    errors: list[str],
    *,
    sources: dict[str, dict[str, Any]],
    jurisdictions: set[str],
    require_sources: bool = False,
) -> tuple[list[str], list[str]]:
    source_ids = row.get("source_ids")
    if not isinstance(source_ids, list):
        errors.append(f"{path}.source_ids: must be an array")
        source_refs: list[str] = []
    else:
        source_refs = [ref for ref in source_ids if isinstance(ref, str)]
        if len(source_refs) != len(source_ids):
            errors.append(f"{path}.source_ids: source ids must be strings")
        for ref in source_refs:
            if ref not in sources:
                errors.append(f"{path}.source_ids: unknown source id {ref!r}")
    if require_sources and not source_refs:
        errors.append(f"{path}.source_ids: legal determination needs a source")

    jurisdiction_ids = row.get("jurisdiction_ids")
    if not isinstance(jurisdiction_ids, list) or not jurisdiction_ids:
        errors.append(f"{path}.jurisdiction_ids: non-empty array required")
        jurisdiction_refs: list[str] = []
    else:
        jurisdiction_refs = [ref for ref in jurisdiction_ids if isinstance(ref, str)]
        if len(jurisdiction_refs) != len(jurisdiction_ids):
            errors.append(f"{path}.jurisdiction_ids: jurisdiction ids must be strings")
        for ref in jurisdiction_refs:
            if ref not in jurisdictions:
                errors.append(
                    f"{path}.jurisdiction_ids: unknown jurisdiction id {ref!r}"
                )

    for ref in source_refs:
        source_jurisdictions = sources.get(ref, {}).get("jurisdiction_ids")
        if not isinstance(source_jurisdictions, list) or not set(
            jurisdiction_refs
        ).intersection(source_jurisdictions):
            errors.append(
                f"{path}.source_ids: source {ref!r} has no declared nexus to the row jurisdictions"
            )
    return source_refs, jurisdiction_refs


def _validate_inapplicability(
    row: dict[str, Any],
    evidence: list[dict[str, Any]],
    path: str,
    errors: list[str],
    *,
    sources: dict[str, dict[str, Any]],
    jurisdictions: set[str],
) -> None:
    basis_kind = row.get("basis_kind")
    if basis_kind not in {"factual-absence", "legal-determination"}:
        errors.append(
            f"{path}.basis_kind: not-applicable needs factual-absence or legal-determination"
        )
        return
    source_refs, jurisdiction_refs = _validate_reference_ids(
        row,
        path,
        errors,
        sources=sources,
        jurisdictions=jurisdictions,
        require_sources=basis_kind == "legal-determination"
        and not any(item.get("kind") == "counsel" for item in evidence),
    )
    if basis_kind == "factual-absence" and not any(
        item.get("kind") in {"repo", "live", "test", "dashboard"} for item in evidence
    ):
        errors.append(
            f"{path}.evidence: factual absence needs repo, live, test, or dashboard evidence"
        )
    if basis_kind == "legal-determination":
        covered_jurisdictions: set[str] = set()
        for ref in source_refs:
            source = sources.get(ref, {})
            if (
                source.get("primary") is True
                and source.get("authority_type")
                in {"legislation", "regulation", "court"}
                and source.get("binding_status") == "binding"
            ):
                covered_jurisdictions.update(_list(source.get("jurisdiction_ids")))
        for item in evidence:
            if item.get("kind") == "counsel":
                covered_jurisdictions.update(_list(item.get("jurisdiction_ids")))
        if not set(jurisdiction_refs).issubset(covered_jurisdictions):
            errors.append(
                f"{path}: legal inapplicability needs binding source or counsel coverage for every jurisdiction"
            )


def _validate_counsel_scopes(data: dict[str, Any], errors: list[str]) -> None:
    """Validate every nested counsel evidence row against declared scope."""
    _, jurisdiction_ids = _record_indexes(data)

    def walk(node: Any, path: str) -> None:
        if isinstance(node, dict):
            if node.get("kind") == "counsel":
                refs = node.get("jurisdiction_ids")
                if isinstance(refs, list):
                    for ref in refs:
                        if not isinstance(ref, str) or ref not in jurisdiction_ids:
                            errors.append(
                                f"{path}.jurisdiction_ids: unknown jurisdiction id {ref!r}"
                            )
            for key, value in node.items():
                walk(value, f"{path}.{key}" if path else str(key))
        elif isinstance(node, list):
            for index, value in enumerate(node):
                walk(value, f"{path}[{index}]")

    walk(data, "")


def _validate_scope(data: dict[str, Any], errors: list[str]) -> None:
    scope = data.get("scope")
    if not isinstance(scope, dict):
        errors.append("scope: object required")
        return

    operator = scope.get("operator")
    if not isinstance(operator, dict):
        errors.append("scope.operator: object required")
    else:
        status = operator.get("status")
        if status not in {"verified", "unverified"}:
            errors.append("scope.operator.status: expected 'verified' or 'unverified'")
        if status == "verified":
            if not _nonempty(operator.get("name")):
                errors.append("scope.operator.name: required when operator is verified")
            evidence = _validate_evidence(
                operator.get("evidence"),
                "scope.operator.evidence",
                errors,
                required=True,
            )
            if not any(row.get("kind") in {"registry", "counsel"} for row in evidence):
                errors.append(
                    "scope.operator.evidence: verified operator needs registry or counsel evidence"
                )
        else:
            _validate_evidence(
                operator.get("evidence"), "scope.operator.evidence", errors
            )

    sources, jurisdiction_ids = _record_indexes(data)
    jurisdictions = _validate_unique_ids(
        scope.get("jurisdictions"), "scope.jurisdictions", errors
    )
    if not jurisdictions:
        errors.append("scope.jurisdictions: at least one jurisdiction entry required")
    for index, jurisdiction in enumerate(jurisdictions):
        path = f"scope.jurisdictions[{index}]"
        if not isinstance(jurisdiction, dict):
            errors.append(f"{path}: must be an object")
            continue
        if not _nonempty(jurisdiction.get("name")):
            errors.append(f"{path}.name: required")
        if jurisdiction.get("status") not in JURISDICTION_STATUSES:
            errors.append(
                f"{path}.status: expected one of {sorted(JURISDICTION_STATUSES)}"
            )
        if not _nonempty(jurisdiction.get("basis")):
            errors.append(
                f"{path}.basis: state the factual nexus or reason it is unresolved"
            )
        if jurisdiction.get("status") in {"potential", "unknown"} and not _nonempty(
            jurisdiction.get("next_gate")
        ):
            errors.append(
                f"{path}.next_gate: required for potential or unknown applicability"
            )
        evidence = _validate_evidence(
            jurisdiction.get("evidence"),
            f"{path}.evidence",
            errors,
            required=jurisdiction.get("status") in {"applicable", "not-applicable"},
        )
        if jurisdiction.get("status") == "not-applicable":
            applicability_row = dict(jurisdiction)
            applicability_row["jurisdiction_ids"] = [jurisdiction.get("id")]
            _validate_inapplicability(
                applicability_row,
                evidence,
                path,
                errors,
                sources=sources,
                jurisdictions=jurisdiction_ids,
            )

    for field in ("channels", "customer_types", "data_roles", "sales_territories"):
        values = scope.get(field)
        if (
            not isinstance(values, list)
            or not values
            or not all(_nonempty(v) for v in values)
        ):
            errors.append(f"scope.{field}: non-empty string array required")


def _validate_claims(data: dict[str, Any], errors: list[str]) -> None:
    claims = _validate_unique_ids(data.get("claims"), "claims", errors)
    if not claims:
        errors.append(
            "claims: inventory at least one public, contractual, or audit claim"
        )
    sources, jurisdiction_ids = _record_indexes(data)
    risk_rows = {
        row.get("id"): row
        for row in _list(data.get("residual_risks"))
        if isinstance(row, dict) and _nonempty(row.get("id"))
    }
    risk_ids = set(risk_rows)
    for index, claim in enumerate(claims):
        path = f"claims[{index}]"
        if not _nonempty(claim.get("claim")):
            errors.append(f"{path}.claim: required")
        if not _nonempty(claim.get("surface")):
            errors.append(f"{path}.surface: required")
        verdict = claim.get("verdict")
        if verdict not in VERDICTS:
            errors.append(f"{path}.verdict: expected one of {sorted(VERDICTS)}")
        claim_type = claim.get("type")
        if claim_type not in CLAIM_TYPES:
            errors.append(f"{path}.type: expected one of {sorted(CLAIM_TYPES)}")
        # Every legal guard below keys off `legal-obligation`, and the type is
        # author-supplied, so a sentence asserting compliance must be typed as
        # one no matter what its author wrote. Otherwise the guard is opt-in by
        # the party it constrains.
        claim_text = claim.get("claim") if isinstance(claim.get("claim"), str) else ""
        asserted = sorted(
            name for name, rx in LEGAL_ASSERTION_PATTERNS.items() if rx.search(claim_text)
        )
        if asserted and claim_type != "legal-obligation":
            errors.append(
                f"{path}.type: this claim states a {asserted[0]} and must be typed "
                "'legal-obligation' so that binding-source or counsel coverage is required "
                f"(declared {claim_type!r})"
            )
            claim_type = "legal-obligation"
        if not _nonempty(claim.get("applicability")):
            errors.append(f"{path}.applicability: required")
        evidence = _validate_evidence(
            claim.get("evidence"),
            f"{path}.evidence",
            errors,
            required=verdict
            in {"supported", "qualified", "contradicted", "not-applicable"},
        )
        if verdict == "qualified" and not _nonempty(claim.get("qualification")):
            errors.append(f"{path}.qualification: qualified verdict needs exact caveat")
        elif verdict == "qualified" and re.search(
            r"\b(?:no qualification|no caveat|unqualified|none required)\b",
            str(claim.get("qualification", "")),
            re.IGNORECASE,
        ):
            errors.append(f"{path}.qualification: must describe a real caveat")
        if verdict == "qualified":
            if claim.get("qualification_type") not in {
                "factual",
                "legal",
                "operational",
                "evidence",
                "temporal",
            }:
                errors.append(
                    f"{path}.qualification_type: qualified verdict needs a typed unresolved condition"
                )
            gate = claim.get("gate")
            if not isinstance(gate, dict):
                errors.append(f"{path}.gate: qualified verdict needs a structured gate")
            else:
                if gate.get("action") not in {
                    "verify",
                    "obtain-counsel",
                    "implement",
                    "test",
                    "reconcile",
                    "disable",
                }:
                    errors.append(f"{path}.gate.action: unknown gate action")
                if not _nonempty(gate.get("target")):
                    errors.append(f"{path}.gate.target: required")
                if not _nonempty(gate.get("owner")):
                    errors.append(f"{path}.gate.owner: required")
        if verdict in {
            "qualified",
            "contradicted",
            "unverified",
            "not-audited",
        } and not _nonempty(claim.get("next_gate")):
            errors.append(
                f"{path}.next_gate: required for unresolved verdict {verdict!r}"
            )
        elif verdict == "qualified" and re.search(
            r"\b(?:no further (?:review|action)|none required|already complete)\b",
            str(claim.get("next_gate", "")),
            re.IGNORECASE,
        ):
            errors.append(f"{path}.next_gate: must describe a real follow-up gate")
        if not _nonempty(claim.get("owner")):
            errors.append(f"{path}.owner: required")
        refs, claim_jurisdictions = _validate_reference_ids(
            claim,
            path,
            errors,
            sources=sources,
            jurisdictions=jurisdiction_ids,
        )
        claim_risks = claim.get("risk_ids")
        if verdict in {"qualified", "contradicted", "unverified", "not-audited"} and (
            not isinstance(claim_risks, list) or not claim_risks
        ):
            errors.append(
                f"{path}.risk_ids: unresolved claim must link a residual risk"
            )
        if isinstance(claim_risks, list):
            for risk_id in claim_risks:
                if not isinstance(risk_id, str) or risk_id not in risk_ids:
                    errors.append(
                        f"{path}.risk_ids: unknown residual risk id {risk_id!r}"
                    )
            if verdict in {
                "qualified",
                "contradicted",
                "unverified",
                "not-audited",
            } and not any(
                isinstance(risk_id, str)
                and risk_rows.get(risk_id, {}).get("status") != "closed"
                for risk_id in claim_risks
            ):
                errors.append(
                    f"{path}.risk_ids: unresolved claim needs at least one non-closed residual risk"
                )
        if claim_type == "legal-obligation" and verdict in {
            "supported",
            "qualified",
            "not-applicable",
        }:
            covered_jurisdictions: set[str] = set()
            for ref in refs:
                source = sources.get(ref, {})
                if (
                    source.get("primary") is True
                    and source.get("authority_type")
                    in {"legislation", "regulation", "court"}
                    and source.get("binding_status") == "binding"
                ):
                    covered_jurisdictions.update(_list(source.get("jurisdiction_ids")))
            for row in evidence:
                if row.get("kind") == "counsel":
                    covered_jurisdictions.update(_list(row.get("jurisdiction_ids")))
            if not set(claim_jurisdictions).issubset(covered_jurisdictions):
                errors.append(
                    f"{path}: legal-obligation verdict needs binding source or counsel coverage for every jurisdiction"
                )
        if verdict == "not-applicable":
            _validate_inapplicability(
                claim,
                evidence,
                path,
                errors,
                sources=sources,
                jurisdictions=jurisdiction_ids,
            )
        if verdict in {"supported", "qualified"}:
            text = str(claim.get("claim", ""))
            for label, pattern in FORBIDDEN_CLOSURE_PATTERNS.items():
                if pattern.search(text):
                    errors.append(f"{path}.claim: unsupported closure phrase {label!r}")


def _validate_sources(data: dict[str, Any], errors: list[str]) -> None:
    sources = _validate_unique_ids(data.get("sources"), "sources", errors)
    _, jurisdiction_ids = _record_indexes(data)
    for index, source in enumerate(sources):
        path = f"sources[{index}]"
        if not _nonempty(source.get("authority")):
            errors.append(f"{path}.authority: required")
        url = source.get("url")
        if not _absolute_http_url(url):
            errors.append(f"{path}.url: absolute HTTP(S) URL required")
        if not _nonempty(source.get("jurisdiction")):
            errors.append(f"{path}.jurisdiction: required")
        source_jurisdictions = source.get("jurisdiction_ids")
        if not isinstance(source_jurisdictions, list) or not source_jurisdictions:
            errors.append(f"{path}.jurisdiction_ids: non-empty array required")
        else:
            for ref in source_jurisdictions:
                if not isinstance(ref, str) or ref not in jurisdiction_ids:
                    errors.append(
                        f"{path}.jurisdiction_ids: unknown jurisdiction id {ref!r}"
                    )
        if not isinstance(source.get("primary"), bool):
            errors.append(f"{path}.primary: boolean required")
        if source.get("authority_type") not in SOURCE_AUTHORITY_TYPES:
            errors.append(
                f"{path}.authority_type: expected one of {sorted(SOURCE_AUTHORITY_TYPES)}"
            )
        if source.get("binding_status") not in BINDING_STATUSES:
            errors.append(
                f"{path}.binding_status: expected one of {sorted(BINDING_STATUSES)}"
            )
        if not _nonempty(source.get("provision_or_scope")):
            errors.append(f"{path}.provision_or_scope: required")
        if not _nonempty(source.get("verified_by")):
            errors.append(f"{path}.verified_by: accountable verifier required")
        if not _iso_datetime(source.get("retrieved_at")):
            errors.append(f"{path}.retrieved_at: ISO timestamp required")
        elif _future_datetime(source.get("retrieved_at")):
            errors.append(f"{path}.retrieved_at: future retrieval is not evidence")
        elif _stale_datetime(source.get("retrieved_at")):
            errors.append(
                f"{path}.retrieved_at: source must be rechecked within 370 days"
            )
        if not SHA256_RE.fullmatch(str(source.get("content_sha256", ""))):
            errors.append(f"{path}.content_sha256: 64-character digest required")


def _validate_controls(data: dict[str, Any], errors: list[str]) -> None:
    controls = _validate_unique_ids(data.get("controls"), "controls", errors)
    if not controls:
        errors.append(
            "controls: inventory at least one implemented, open, or inapplicable control"
        )
    risk_ids = {
        row.get("id")
        for row in _list(data.get("residual_risks"))
        if isinstance(row, dict) and _nonempty(row.get("id"))
    }
    sources, jurisdiction_ids = _record_indexes(data)
    for index, control in enumerate(controls):
        path = f"controls[{index}]"
        if not _nonempty(control.get("area")):
            errors.append(f"{path}.area: required")
        status = control.get("status")
        if status not in CONTROL_STATUSES:
            errors.append(f"{path}.status: expected one of {sorted(CONTROL_STATUSES)}")
        if not _nonempty(control.get("applicability")):
            errors.append(f"{path}.applicability: required")
        evidence = _validate_evidence(
            control.get("evidence"),
            f"{path}.evidence",
            errors,
            required=status in {"implemented", "not-applicable"},
        )
        if status == "not-applicable":
            _validate_inapplicability(
                control,
                evidence,
                path,
                errors,
                sources=sources,
                jurisdictions=jurisdiction_ids,
            )
        if not _nonempty(control.get("owner")):
            errors.append(f"{path}.owner: required")
        if status in {"partial", "open", "blocked-external"}:
            if not _nonempty(control.get("next_gate")):
                errors.append(f"{path}.next_gate: required for unresolved control")
            control_risks = control.get("risk_ids")
            if not isinstance(control_risks, list) or not control_risks:
                errors.append(
                    f"{path}.risk_ids: unresolved control must link a residual risk"
                )
        control_risks = control.get("risk_ids", [])
        if not isinstance(control_risks, list):
            errors.append(f"{path}.risk_ids: must be an array")
        else:
            for risk_id in control_risks:
                if not isinstance(risk_id, str) or risk_id not in risk_ids:
                    errors.append(
                        f"{path}.risk_ids: unknown residual risk id {risk_id!r}"
                    )


def _validate_coverage_rows(
    rows: Any,
    path: str,
    required_ids: set[str],
    errors: list[str],
    *,
    sources: dict[str, dict[str, Any]],
    jurisdictions: set[str],
) -> None:
    entries = _validate_unique_ids(rows, path, errors)
    observed_ids = {row.get("id") for row in entries if _nonempty(row.get("id"))}
    missing = required_ids - observed_ids
    unknown = {
        row_id
        for row_id in observed_ids - required_ids
        if not CUSTOM_COVERAGE_ID_RE.fullmatch(str(row_id))
    }
    if missing:
        errors.append(f"{path}: missing required coverage ids {sorted(missing)}")
    if unknown:
        errors.append(f"{path}: unknown coverage ids {sorted(unknown)}")
    for index, row in enumerate(entries):
        row_path = f"{path}[{index}]"
        if row.get("id") not in required_ids and not _nonempty(row.get("description")):
            errors.append(
                f"{row_path}.description: custom/sector coverage needs a description"
            )
        status = row.get("status")
        if status not in COVERAGE_STATUSES:
            errors.append(
                f"{row_path}.status: expected one of {sorted(COVERAGE_STATUSES)}"
            )
        if not _nonempty(row.get("owner")):
            errors.append(f"{row_path}.owner: required")
        evidence = _validate_evidence(
            row.get("evidence"),
            f"{row_path}.evidence",
            errors,
            required=status in {"audited", "not-applicable"},
        )
        if status == "not-applicable":
            _validate_inapplicability(
                row,
                evidence,
                row_path,
                errors,
                sources=sources,
                jurisdictions=jurisdictions,
            )
        if status == "not-audited" and not _nonempty(row.get("next_gate")):
            errors.append(
                f"{row_path}.next_gate: required when coverage is not audited"
            )


def _validate_coverage(data: dict[str, Any], errors: list[str]) -> None:
    coverage = data.get("coverage")
    if not isinstance(coverage, dict):
        errors.append("coverage: object required")
        return
    sources, jurisdictions = _record_indexes(data)
    _validate_coverage_rows(
        coverage.get("claim_surfaces"),
        "coverage.claim_surfaces",
        CLAIM_SURFACE_AREAS,
        errors,
        sources=sources,
        jurisdictions=jurisdictions,
    )
    _validate_coverage_rows(
        coverage.get("issue_areas"),
        "coverage.issue_areas",
        ISSUE_AREA_IDS,
        errors,
        sources=sources,
        jurisdictions=jurisdictions,
    )


def _validate_residual_risks(data: dict[str, Any], errors: list[str]) -> None:
    risks = _validate_unique_ids(data.get("residual_risks"), "residual_risks", errors)
    if not risks:
        errors.append("residual_risks: at least one bounded residual risk is required")
    for index, risk in enumerate(risks):
        path = f"residual_risks[{index}]"
        if risk.get("severity") not in {"p0", "p1", "p2", "p3"}:
            errors.append(f"{path}.severity: expected p0, p1, p2, or p3")
        for field in ("risk", "owner", "closure_evidence"):
            if not _nonempty(risk.get(field)):
                errors.append(f"{path}.{field}: required")
        status = risk.get("status")
        if status not in {"open", "accepted", "closed"}:
            errors.append(f"{path}.status: expected open, accepted, or closed")
        evidence = _validate_evidence(
            risk.get("evidence"),
            f"{path}.evidence",
            errors,
            required=status == "closed",
        )
        if status == "accepted":
            if risk.get("severity") == "p0":
                errors.append(
                    f"{path}: p0 risk cannot be accepted; close it or block launch"
                )
            if not _nonempty(risk.get("accepted_by")):
                errors.append(f"{path}.accepted_by: required for accepted risk")
            if not _iso_datetime(risk.get("accepted_at")) or _future_datetime(
                risk.get("accepted_at")
            ):
                errors.append(
                    f"{path}.accepted_at: current timezone-aware timestamp required"
                )
        if status != "closed" and evidence:
            errors.append(
                f"{path}.evidence: closure evidence belongs only on a closed risk"
            )

    operator = (
        data.get("scope", {}).get("operator", {})
        if isinstance(data.get("scope"), dict)
        else {}
    )
    if isinstance(operator, dict) and operator.get("status") == "unverified":
        has_operator_risk = any(
            row.get("severity") == "p0"
            and row.get("status") == "open"
            and "operator" in str(row.get("risk", "")).lower()
            for row in risks
        )
        if not has_operator_risk:
            errors.append(
                "residual_risks: unverified operator requires an explicit p0 operator risk"
            )


def _validate_launch_disposition(data: dict[str, Any], errors: list[str]) -> None:
    launch = data.get("launch_disposition")
    if not isinstance(launch, dict):
        errors.append("launch_disposition: object required")
        return
    status = launch.get("status")
    if status not in LAUNCH_STATUSES:
        errors.append(
            f"launch_disposition.status: expected one of {sorted(LAUNCH_STATUSES)}"
        )
    if not _nonempty(launch.get("owner")):
        errors.append("launch_disposition.owner: required")
    expected_rationale = LAUNCH_RATIONALES.get(str(status))
    if launch.get("rationale") != expected_rationale:
        errors.append(
            "launch_disposition.rationale: must equal the checker-defined bounded "
            f"rationale {expected_rationale!r}"
        )
    risk_rows = [
        row for row in _list(data.get("residual_risks")) if isinstance(row, dict)
    ]
    risk_ids = {row.get("id") for row in risk_rows if _nonempty(row.get("id"))}
    refs = launch.get("risk_ids")
    if not isinstance(refs, list):
        errors.append("launch_disposition.risk_ids: must be an array")
        refs = []
    for risk_id in refs:
        if not isinstance(risk_id, str) or risk_id not in risk_ids:
            errors.append(
                f"launch_disposition.risk_ids: unknown residual risk id {risk_id!r}"
            )
    open_p0 = {
        row.get("id")
        for row in risk_rows
        if row.get("severity") == "p0" and row.get("status") != "closed"
    }
    open_risk_ids = {
        row.get("id") for row in risk_rows if row.get("status") != "closed"
    }
    if status == "limited":
        constraints = launch.get("constraints")
        if not isinstance(constraints, list) or not constraints:
            errors.append(
                "launch_disposition.constraints: limited status needs structured enforced constraints"
            )
        else:
            covered_p0: set[str] = set()
            control_rows = {
                row.get("id"): row
                for row in _list(data.get("controls"))
                if isinstance(row, dict) and _nonempty(row.get("id"))
            }
            for index, constraint in enumerate(constraints):
                path = f"launch_disposition.constraints[{index}]"
                if not isinstance(constraint, dict):
                    errors.append(f"{path}: must be an object")
                    continue
                for field in ("id", "restriction", "owner"):
                    if not _nonempty(constraint.get(field)):
                        errors.append(f"{path}.{field}: required")
                if constraint.get("effect") not in CONSTRAINT_EFFECTS:
                    errors.append(
                        f"{path}.effect: expected one of {sorted(CONSTRAINT_EFFECTS)}"
                    )
                if constraint.get("action") not in CONSTRAINT_ACTIONS:
                    errors.append(
                        f"{path}.action: expected one of {sorted(CONSTRAINT_ACTIONS)}"
                    )
                if not _nonempty(constraint.get("target")):
                    errors.append(f"{path}.target: required")
                enforced_value = constraint.get("enforced_value")
                if not isinstance(enforced_value, (bool, str)) or (
                    isinstance(enforced_value, str) and not enforced_value.strip()
                ):
                    errors.append(
                        f"{path}.enforced_value: non-empty string or boolean required"
                    )
                effect = constraint.get("effect")
                action = constraint.get("action")
                compatible = (
                    (
                        effect == "disabled-feature"
                        and action == "disable"
                        and enforced_value is False
                    )
                    or (
                        effect == "blocked-processing"
                        and action == "deny"
                        and enforced_value is False
                    )
                    or (
                        effect == "read-only-mode"
                        and action == "read-only"
                        and enforced_value == "read-only"
                    )
                    or (
                        effect == "geofenced-territory"
                        and action == "geofence"
                        and _nonempty(enforced_value)
                    )
                    or (
                        effect in {"restricted-customer-type", "restricted-channel"}
                        and action == "restrict"
                        and _nonempty(enforced_value)
                    )
                )
                if not compatible:
                    errors.append(
                        f"{path}: effect, action, and enforced_value do not form a limiting tuple"
                    )
                if not _nonempty(constraint.get("enforcement_predicate")):
                    errors.append(f"{path}.enforcement_predicate: required")
                if re.search(
                    r"\b(?:no restriction|without limitation|all (?:sales|processing|features?|channels?) (?:remain |are )?enabled|everything remains (?:publicly )?available)\b",
                    str(constraint.get("restriction", "")),
                    re.IGNORECASE,
                ):
                    errors.append(
                        f"{path}.restriction: must describe an actual limiting condition"
                    )
                evidence = _validate_evidence(
                    constraint.get("evidence"),
                    f"{path}.evidence",
                    errors,
                    required=True,
                )
                if not any(
                    row.get("kind") in {"repo", "live", "test", "dashboard", "policy"}
                    for row in evidence
                ):
                    errors.append(
                        f"{path}.evidence: constraint needs enforcement evidence"
                    )
                control_ids = constraint.get("control_ids")
                valid_controls: list[dict[str, Any]] = []
                if not isinstance(control_ids, list) or not control_ids:
                    errors.append(f"{path}.control_ids: non-empty array required")
                else:
                    for control_id in control_ids:
                        if not isinstance(control_id, str):
                            errors.append(
                                f"{path}.control_ids: control ids must be strings"
                            )
                            continue
                        control = control_rows.get(control_id)
                        if not isinstance(control, dict):
                            errors.append(
                                f"{path}.control_ids: unknown control id {control_id!r}"
                            )
                        elif control.get("status") != "implemented":
                            errors.append(
                                f"{path}.control_ids: constraint control {control_id!r} is not implemented"
                            )
                        elif control.get("enforcement_predicate") != constraint.get(
                            "enforcement_predicate"
                        ):
                            errors.append(
                                f"{path}.control_ids: control {control_id!r} does not share the constraint enforcement predicate"
                            )
                        elif any(
                            control.get(field) != constraint.get(field)
                            for field in (
                                "effect",
                                "action",
                                "target",
                                "enforced_value",
                            )
                        ):
                            errors.append(
                                f"{path}.control_ids: control {control_id!r} does not share the structured enforcement tuple"
                            )
                        else:
                            valid_controls.append(control)
                constraint_risks = constraint.get("risk_ids")
                if not isinstance(constraint_risks, list) or not constraint_risks:
                    errors.append(f"{path}.risk_ids: non-empty array required")
                else:
                    for risk_id in constraint_risks:
                        if not isinstance(risk_id, str):
                            errors.append(f"{path}.risk_ids: risk ids must be strings")
                            continue
                        if risk_id not in open_risk_ids:
                            errors.append(
                                f"{path}.risk_ids: {risk_id!r} is not an open risk"
                            )
                        else:
                            if risk_id not in refs:
                                errors.append(
                                    f"{path}.risk_ids: {risk_id!r} is not linked by launch_disposition.risk_ids"
                                )
                            if risk_id in open_p0:
                                covered_p0.add(risk_id)
                            if not any(
                                risk_id in _list(control.get("risk_ids"))
                                for control in valid_controls
                            ):
                                errors.append(
                                    f"{path}: no referenced implemented control is linked to risk {risk_id!r}"
                                )
            if not open_p0.issubset(covered_p0):
                errors.append(
                    "launch_disposition.constraints: every open p0 needs an evidenced enforced constraint"
                )
    elif "constraints" in launch and launch.get("constraints") not in (None, []):
        errors.append(
            "launch_disposition.constraints: constraints are permitted only for limited status"
        )
    # `ready-for-counsel-review` says engineering evidence is READY. Only open
    # p0 risks constrained it, so it was reachable with an unknown jurisdiction,
    # zero sources, every coverage row `not-audited` and every claim unresolved
    # — a status asserting readiness over a body of work that had not begun.
    # "Nothing was examined" and "everything was examined and is clean" must not
    # produce the same disposition.
    if status == "ready-for-counsel-review":
        if not _list(data.get("sources")):
            errors.append(
                "launch_disposition.status: ready-for-counsel-review needs at least one "
                "source; a review with no sources examined nothing"
            )
        rows = _list((data.get("coverage") or {}).get("claim_surfaces"))
        if rows and not any(
            isinstance(row, dict) and row.get("status") not in {None, "not-audited"}
            for row in rows
        ):
            errors.append(
                "launch_disposition.status: ready-for-counsel-review needs at least one "
                "audited claim surface; every surface is 'not-audited'"
            )
        unresolved = [
            row.get("id")
            for row in _list(data.get("claims"))
            if isinstance(row, dict) and row.get("verdict") in {"unverified", "not-audited"}
        ]
        if unresolved:
            errors.append(
                "launch_disposition.status: ready-for-counsel-review with unresolved "
                f"claim(s) {sorted(x for x in unresolved if x)}; resolve or downgrade to limited"
            )

    if open_p0:
        if status not in {"blocked", "limited"}:
            errors.append(
                "launch_disposition.status: open p0 risks require blocked or limited"
            )
        if not open_p0.issubset(set(refs)):
            errors.append(
                "launch_disposition.risk_ids: every open p0 risk must be linked"
            )


def _validate_lifecycle(data: dict[str, Any], errors: list[str]) -> None:
    lifecycle = data.get("lifecycle")
    if not isinstance(lifecycle, dict):
        errors.append("lifecycle: object required")
        return
    state = lifecycle.get("state")
    if state not in LIFECYCLE_STATES:
        errors.append(f"lifecycle.state: expected one of {list(LIFECYCLE_STATES)}")
        return
    receipts_value = lifecycle.get("receipts")
    if not isinstance(receipts_value, list):
        errors.append("lifecycle.receipts: must be an array")
        receipts: list[Any] = []
    else:
        receipts = receipts_value
    kinds: set[str] = set()
    receipt_times: dict[str, datetime] = {}
    release_id = lifecycle.get("release_id")
    if state != "worktree" and not _nonempty(release_id):
        errors.append("lifecycle.release_id: required after worktree state")
    for index, receipt in enumerate(receipts):
        path = f"lifecycle.receipts[{index}]"
        if not isinstance(receipt, dict):
            errors.append(f"{path}: must be an object")
            continue
        kind = receipt.get("kind")
        if kind not in {"commit", "pull-request", "merge", "deployment", "live-probe"}:
            errors.append(f"{path}.kind: unknown lifecycle receipt kind")
        else:
            if kind in kinds:
                errors.append(f"{path}.kind: duplicate lifecycle receipt kind {kind!r}")
            kinds.add(str(kind))
        locator = receipt.get("locator")
        if not _nonempty(locator):
            errors.append(f"{path}.locator: required")
        elif kind in {"commit", "merge"} and not re.fullmatch(
            r"[0-9a-f]{7,64}", str(locator), re.IGNORECASE
        ):
            errors.append(f"{path}.locator: commit or merge locator must be a git hash")
        elif kind in {
            "pull-request",
            "deployment",
            "live-probe",
        } and not _absolute_http_url(locator):
            errors.append(f"{path}.locator: absolute HTTP(S) receipt URL required")
        if not _iso_datetime(receipt.get("observed_at")):
            errors.append(f"{path}.observed_at: ISO timestamp required")
        elif _future_datetime(receipt.get("observed_at")):
            errors.append(f"{path}.observed_at: future receipt is not evidence")
        elif kind in RECEIPT_REQUIREMENTS["live-verified"]:
            receipt_times[str(kind)] = datetime.fromisoformat(
                str(receipt.get("observed_at")).replace("Z", "+00:00")
            ).astimezone(timezone.utc)
        if not _nonempty(receipt.get("issuer")):
            errors.append(f"{path}.issuer: required")
        if not SHA256_RE.fullmatch(str(receipt.get("sha256", ""))):
            errors.append(f"{path}.sha256: 64-character receipt digest required")
        if state != "worktree" and receipt.get("release_id") != release_id:
            errors.append(
                f"{path}.release_id: must match lifecycle.release_id {release_id!r}"
            )
    missing = RECEIPT_REQUIREMENTS.get(str(state), set()) - kinds
    if missing:
        errors.append(
            f"lifecycle.receipts: state {state!r} requires receipt kinds {sorted(missing)}"
        )
    required_order = [
        kind
        for kind in ("commit", "pull-request", "merge", "deployment", "live-probe")
        if kind in RECEIPT_REQUIREMENTS.get(str(state), set())
    ]
    ordered_times = [
        receipt_times[kind] for kind in required_order if kind in receipt_times
    ]
    if any(later < earlier for earlier, later in itertools.pairwise(ordered_times)):
        errors.append(
            "lifecycle.receipts: receipt observations must follow commit, PR, merge, deployment, live-probe order"
        )


def validate_manifest(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if data.get("schema_version") != 1:
        errors.append("schema_version: expected integer 1")
    project = data.get("project")
    if not isinstance(project, dict) or not _nonempty(project.get("name")):
        errors.append("project.name: required")
    else:
        if project.get("template") is not False:
            errors.append(
                "project.template: set to false only after replacing placeholders and recording gaps"
            )
        if project.get("template_marker") == PLACEHOLDER_MARKER:
            errors.append("project.template_marker: remove the initialization marker")
        for field in ("name", "repository", "base_url"):
            if project.get(field) in PLACEHOLDER_VALUES:
                errors.append(f"project.{field}: replace the bundled placeholder value")
        for field in ("repository", "base_url"):
            if field in project and not _absolute_http_url(project.get(field)):
                errors.append(f"project.{field}: absolute HTTP(S) URL required")

    _validate_scope(data, errors)
    _validate_counsel_scopes(data, errors)
    _validate_sources(data, errors)
    _validate_coverage(data, errors)
    _validate_claims(data, errors)
    _validate_controls(data, errors)
    _validate_residual_risks(data, errors)
    _validate_launch_disposition(data, errors)
    _validate_lifecycle(data, errors)

    statement = data.get("completion_statement")
    launch_status = (
        data.get("launch_disposition", {}).get("status")
        if isinstance(data.get("launch_disposition"), dict)
        else "not-assessed"
    )
    expected_statement = (
        "Overall legal compliance is not claimed. "
        f"Launch disposition: {launch_status}. "
        "See the claim, coverage, control, residual-risk, and lifecycle records."
    )
    if statement != expected_statement:
        errors.append(
            "completion_statement: must equal the fixed bounded statement for the "
            f"structured launch status: {expected_statement!r}"
        )
    if data.get("legal_boundary") != LEGAL_BOUNDARY_STATEMENT:
        errors.append(
            "legal_boundary: must equal the checker-defined no-advice/no-launch-approval boundary"
        )

    surfaces = data.get("surfaces", [])
    if not isinstance(surfaces, list):
        errors.append("surfaces: must be an array")
    else:
        for index, surface in enumerate(surfaces):
            path = f"surfaces[{index}]"
            if not isinstance(surface, dict):
                errors.append(f"{path}: must be an object")
                continue
            route = surface.get("path")
            parsed_route = urllib.parse.urlparse(str(route or ""))
            if (
                not _nonempty(route)
                or not str(route).startswith("/")
                or str(route).startswith("//")
                or parsed_route.scheme
                or parsed_route.netloc
                or parsed_route.fragment
            ):
                errors.append(
                    f"{path}.path: same-origin route beginning with one / required"
                )
            if not isinstance(surface.get("expect_status", 200), int):
                errors.append(f"{path}.expect_status: integer required")
            headers = surface.get("expect_headers", {})
            if not isinstance(headers, dict) or not all(
                _nonempty(k) and isinstance(v, str) for k, v in headers.items()
            ):
                errors.append(
                    f"{path}.expect_headers: object with non-empty header names and string values required"
                )
            if "allow_redirects" in surface and not isinstance(
                surface.get("allow_redirects"), bool
            ):
                errors.append(f"{path}.allow_redirects: boolean required")
            content_type = surface.get("expect_content_type")
            if content_type is not None and not _nonempty(content_type):
                errors.append(f"{path}.expect_content_type: non-empty string required")
    return errors


def check_manifest(path: Path, *, as_json: bool) -> int:
    try:
        data = load_json(path)
        errors = validate_manifest(data)
    except (AttributeError, KeyError, TypeError, ValueError) as exc:
        errors = [str(exc)]
    result = {"ok": not errors, "manifest": str(path), "errors": errors}
    if as_json:
        print(json.dumps(result, indent=2, sort_keys=True))
    elif errors:
        print(f"FAIL {path} ({len(errors)} issue(s))")
        for error in errors:
            print(f"- {error}")
    else:
        print(
            f"PASS {path}: schema-valid with explicit gaps; evidence authenticity, "
            "claim completeness, and legal sufficiency were not verified"
        )
    return 0 if not errors else 1


def init_manifest(output: Path, *, force: bool) -> int:
    source = (
        Path(__file__).resolve().parent.parent
        / "assets"
        / "legal-readiness.example.json"
    )
    if output.exists() and not force:
        print(f"refusing to overwrite {output}; pass --force", file=sys.stderr)
        return 2
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, output)
    print(f"initialized {output}")
    return 0


def _header_lookup(headers: Any, name: str) -> str | None:
    return headers.get(name) if hasattr(headers, "get") else None


def _origin(url: str) -> tuple[str, str, int]:
    parsed = urllib.parse.urlparse(url)
    default_port = 443 if parsed.scheme == "https" else 80
    return (
        parsed.scheme.lower(),
        str(parsed.hostname or "").lower(),
        parsed.port or default_port,
    )


def _network_target_error(url: str, *, allow_private_network: bool) -> str | None:
    _, error = _resolved_target_addresses(
        url, allow_private_network=allow_private_network
    )
    return error


def _resolved_target_addresses(
    url: str, *, allow_private_network: bool
) -> tuple[list[str], str | None]:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        return [], "target must be an absolute HTTP(S) URL"
    if parsed.username is not None or parsed.password is not None:
        return [], "target URL must not contain credentials"
    try:
        addresses = sorted(
            {
                str(ipaddress.ip_address(result[4][0]))
                for result in socket.getaddrinfo(
                    parsed.hostname,
                    parsed.port or (443 if parsed.scheme == "https" else 80),
                    type=socket.SOCK_STREAM,
                )
            }
        )
    except (OSError, ValueError) as exc:
        return [], f"cannot resolve target host: {exc}"
    if not allow_private_network:
        unsafe = sorted(
            address
            for address in addresses
            if not ipaddress.ip_address(address).is_global
        )
        if unsafe:
            return [], (
                "private, loopback, link-local, reserved, or non-global target "
                f"refused: {unsafe}"
            )
    return addresses, None


def _pinned_request(
    url: str,
    *,
    timeout: float,
    allow_private_network: bool,
) -> tuple[int, Any]:
    """Request one URL using the exact addresses that passed the safety check."""
    parsed = urllib.parse.urlparse(url)
    addresses, error = _resolved_target_addresses(
        url, allow_private_network=allow_private_network
    )
    if error:
        raise OSError(error)
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    last_error: OSError | None = None
    for address in addresses:
        raw: socket.socket | None = None
        connection: http.client.HTTPConnection | None = None
        try:
            raw = socket.create_connection((address, port), timeout=timeout)
            peer = str(ipaddress.ip_address(raw.getpeername()[0]))
            if peer != address:
                raise OSError(
                    f"connected peer {peer} did not match pinned address {address}"
                )
            if not allow_private_network and not ipaddress.ip_address(peer).is_global:
                raise OSError(f"connected peer {peer} is not globally routable")
            if parsed.scheme == "https":
                raw = ssl.create_default_context().wrap_socket(
                    raw, server_hostname=str(parsed.hostname)
                )
            connection = http.client.HTTPConnection(
                str(parsed.hostname), port, timeout=timeout
            )
            connection.sock = raw
            request_path = urllib.parse.urlunparse(
                ("", "", parsed.path or "/", parsed.params, parsed.query, "")
            )
            connection.request(
                "GET",
                request_path,
                headers={"User-Agent": "legal-readiness-probe/1"},
            )
            response = connection.getresponse()
            response.read(1024 * 1024)
            status = response.status
            headers = response.headers
            connection.close()
            return status, headers
        except (OSError, ssl.SSLError, http.client.HTTPException) as exc:
            last_error = OSError(str(exc))
            if connection is not None:
                connection.close()
            elif raw is not None:
                raw.close()
    raise last_error or OSError("no resolved address was reachable")


def _request_surface(
    url: str,
    *,
    allow_redirects: bool,
    base_origin: tuple[str, str, int],
    timeout: float,
    allow_private_network: bool,
) -> tuple[int, Any, str]:
    current = url
    for _ in range(6):
        status, headers = _pinned_request(
            current,
            timeout=timeout,
            allow_private_network=allow_private_network,
        )
        location = _header_lookup(headers, "Location")
        if status not in {301, 302, 303, 307, 308} or not location:
            return status, headers, current
        if not allow_redirects:
            return status, headers, current
        target = urllib.parse.urljoin(current, location)
        if _origin(target) != base_origin:
            raise OSError("cross-origin redirect refused")
        current = target
    raise OSError("redirect limit exceeded")


def probe_manifest(
    path: Path,
    *,
    base_url: str | None,
    output: Path | None,
    timeout: float,
    force: bool,
    allow_private_network: bool,
) -> int:
    if not math.isfinite(timeout) or timeout <= 0:
        print("probe timeout must be a finite positive number", file=sys.stderr)
        return 2
    try:
        data = load_json(path)
    except (TypeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    manifest_errors = validate_manifest(data)
    if manifest_errors:
        print("probe refused an invalid manifest:", file=sys.stderr)
        for error in manifest_errors:
            print(f"- {error}", file=sys.stderr)
        return 2
    manifest_digest = hashlib.sha256(
        json.dumps(data, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    if output and output.exists() and not force:
        print(f"refusing to overwrite {output}; pass --force", file=sys.stderr)
        return 2
    configured = base_url or data.get("project", {}).get("base_url")
    parsed = urllib.parse.urlparse(str(configured or ""))
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        print(
            "probe requires project.base_url or --base-url with absolute HTTP(S) URL",
            file=sys.stderr,
        )
        return 2
    declared_surfaces = [
        surface
        for surface in _list(data.get("surfaces"))
        if isinstance(surface, dict) and _nonempty(surface.get("path"))
    ]
    if not declared_surfaces:
        print("probe requires at least one declared surface", file=sys.stderr)
        return 2
    target_error = _network_target_error(
        str(configured), allow_private_network=allow_private_network
    )
    if target_error:
        print(f"probe refused base URL: {target_error}", file=sys.stderr)
        return 2

    observations: list[dict[str, Any]] = []
    all_ok = True
    for surface in declared_surfaces:
        url = urllib.parse.urljoin(
            str(configured).rstrip("/") + "/", str(surface["path"]).lstrip("/")
        )
        expected_status = surface.get("expect_status", 200)
        expected_headers = surface.get("expect_headers", {})
        observed: dict[str, Any] = {
            "path": surface["path"],
            "url": url,
            "expected_status": expected_status,
            "expected_headers": expected_headers,
        }
        try:
            status, headers, final_url = _request_surface(
                url,
                allow_redirects=surface.get("allow_redirects", False),
                base_origin=_origin(str(configured)),
                timeout=timeout,
                allow_private_network=allow_private_network,
            )
            observed["status"] = status
            observed["final_url"] = final_url
            observed["content_type"] = _header_lookup(headers, "Content-Type")
            observed["headers"] = {
                name: _header_lookup(headers, name) for name in expected_headers
            }
            errors: list[str] = []
            if status != expected_status:
                errors.append(f"expected status {expected_status}, got {status}")
            for name, expected_fragment in expected_headers.items():
                value = _header_lookup(headers, name)
                if value is None:
                    errors.append(f"missing header {name}")
                elif (
                    _nonempty(expected_fragment)
                    and str(expected_fragment).lower() not in value.lower()
                ):
                    errors.append(
                        f"header {name} does not contain {expected_fragment!r}"
                    )
            expected_content_type = surface.get("expect_content_type")
            if _nonempty(expected_content_type):
                content_type = _header_lookup(headers, "Content-Type") or ""
                if str(expected_content_type).lower() not in content_type.lower():
                    errors.append(
                        f"Content-Type does not contain {expected_content_type!r}"
                    )
            observed["ok"] = not errors
            observed["errors"] = errors
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            observed.update({"ok": False, "errors": [f"request failed: {exc}"]})
        all_ok = all_ok and bool(observed.get("ok"))
        observations.append(observed)

    receipt = {
        "schema_version": 1,
        "kind": "legal-surface-probe",
        "base_url": configured,
        "manifest_sha256": manifest_digest,
        "expectations_sha256": hashlib.sha256(
            json.dumps(
                {"base_url": configured, "surfaces": declared_surfaces},
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest(),
        "observed_at": datetime.now().astimezone().isoformat(),
        "ok": all_ok,
        "observations": observations,
        "boundary": (
            "Reachability and declared header/content-type checks only; this receipt does not "
            "establish the legal sufficiency of page contents or overall compliance."
        ),
    }
    rendered = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        try:
            with output.open("w" if force else "x", encoding="utf-8") as handle:
                handle.write(rendered)
        except FileExistsError:
            print(f"refusing to overwrite {output}; pass --force", file=sys.stderr)
            return 2
        print(f"{'PASS' if all_ok else 'FAIL'} probe receipt: {output}")
    else:
        print(rendered, end="")
    return 0 if all_ok else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate and probe an evidence-first legal-readiness manifest."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="copy the bundled example manifest")
    init.add_argument("output", type=Path)
    init.add_argument("--force", action="store_true")

    check = sub.add_parser("check", help="validate a manifest")
    check.add_argument("manifest", type=Path)
    check.add_argument("--json", action="store_true", dest="as_json")

    probe = sub.add_parser("probe", help="probe declared web surfaces")
    probe.add_argument("manifest", type=Path)
    probe.add_argument("--base-url")
    probe.add_argument("--output", type=Path)
    probe.add_argument("--timeout", type=float, default=10.0)
    probe.add_argument("--force", action="store_true")
    probe.add_argument(
        "--allow-private-network",
        action="store_true",
        help="allow explicit localhost/private targets for trusted development manifests",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "init":
        return init_manifest(args.output, force=args.force)
    if args.command == "check":
        return check_manifest(args.manifest, as_json=args.as_json)
    if args.command == "probe":
        return probe_manifest(
            args.manifest,
            base_url=args.base_url,
            output=args.output,
            timeout=args.timeout,
            force=args.force,
            allow_private_network=args.allow_private_network,
        )
    raise AssertionError(args.command)


if __name__ == "__main__":
    raise SystemExit(main())
