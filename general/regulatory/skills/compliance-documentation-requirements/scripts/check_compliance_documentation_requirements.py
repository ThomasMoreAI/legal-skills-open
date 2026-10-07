#!/usr/bin/env python3
"""Checker script for Compliance Documentation Requirements skill.

Checks Salesforce metadata for common compliance documentation anti-patterns,
including hardcoded API credentials in Named Credentials, missing Field Audit Trail
configuration, and improper KYC object field tracking.

Uses stdlib only — no pip dependencies.

Usage:
    python3 check_compliance_documentation_requirements.py [--help]
    python3 check_compliance_documentation_requirements.py --manifest-dir path/to/metadata
"""

from __future__ import annotations

import argparse
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check Salesforce metadata for compliance documentation anti-patterns. "
            "Covers KYC object configuration, Named Credential authentication type, "
            "field history tracking on compliance objects, and hardcoded credentials."
        ),
    )
    parser.add_argument(
        "--manifest-dir",
        default=".",
        help="Root directory of the Salesforce metadata (default: current directory).",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_files(root: Path, pattern: str) -> list[Path]:
    return list(root.rglob(pattern))


def parse_xml(path: Path) -> ET.Element | None:
    try:
        tree = ET.parse(path)
        return tree.getroot()
    except ET.ParseError:
        return None


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

KYC_OBJECTS = {
    "PartyIdentityVerification",
    "IdentityDocument",
    "PartyProfileRisk",
    "PartyScreeningSummary",
}

# Fields on KYC objects that should have history tracking enabled for compliance
KYC_TRACKED_FIELDS = {
    "PartyProfileRisk": {"RiskCategory", "RiskScore", "RiskReason", "RiskReviewDate"},
    "PartyIdentityVerification": {"VerificationStatus", "VerificationDate"},
    "PartyScreeningSummary": {"ScreeningStatus"},
}

# Patterns that suggest hardcoded credentials in Named Credential URL or body
CREDENTIAL_PATTERNS = [
    "apikey=",
    "api_key=",
    "token=",
    "secret=",
    "password=",
    "Authorization: Basic",
]


def check_named_credential_auth_type(manifest_dir: Path) -> list[str]:
    """Warn when Named Credentials use Per-User authentication.

    Per-User auth fails in batch, scheduled, and Platform Event contexts —
    all common execution paths for AML screening integrations.
    """
    issues: list[str] = []

    nc_files = find_files(manifest_dir, "*.namedCredential")
    nc_files += find_files(manifest_dir, "*.namedCredential-meta.xml")

    for nc_file in nc_files:
        root = parse_xml(nc_file)
        if root is None:
            continue
        # Strip namespace if present
        tag_map: dict[str, str] = {}
        for elem in root.iter():
            local = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
            tag_map[local] = elem.text or ""

        auth_type = tag_map.get("oauthType", "") or tag_map.get("principalType", "")
        label = tag_map.get("label", nc_file.name)

        if auth_type.lower() in ("nameduser", "per-user", "peruser"):
            issues.append(
                f"Named Credential '{label}' uses Per-User authentication. "
                "AML screening integrations run in batch/scheduled contexts where "
                "Per-User auth fails — use Named Principal (org-level) auth instead. "
                f"[{nc_file}]"
            )

    return issues


def check_hardcoded_credentials_in_named_credentials(manifest_dir: Path) -> list[str]:
    """Detect Named Credential metadata that may contain hardcoded secrets."""
    issues: list[str] = []

    nc_files = find_files(manifest_dir, "*.namedCredential")
    nc_files += find_files(manifest_dir, "*.namedCredential-meta.xml")

    for nc_file in nc_files:
        try:
            content = nc_file.read_text(encoding="utf-8", errors="ignore").lower()
        except OSError:
            continue
        for pattern in CREDENTIAL_PATTERNS:
            if pattern.lower() in content:
                issues.append(
                    f"Named Credential file '{nc_file.name}' may contain a hardcoded "
                    f"credential (found pattern: '{pattern}'). Use External Credentials "
                    f"with encrypted secrets instead. [{nc_file}]"
                )
                break  # One warning per file is enough

    return issues


def check_field_history_tracking(manifest_dir: Path) -> list[str]:
    """Warn when key KYC object fields are not tracked for field history."""
    issues: list[str] = []

    object_dirs = find_files(manifest_dir, "*.object")
    object_dirs += find_files(manifest_dir, "*.object-meta.xml")

    tracked_by_object: dict[str, set[str]] = {}

    for obj_file in object_dirs:
        # Determine object name from file name
        obj_name = obj_file.stem.replace("-meta", "").replace(".object", "")
        # Strip namespace prefix (e.g., FinServ__PartyProfileRisk__c → PartyProfileRisk)
        bare_name = obj_name.split("__")[-1].replace("__c", "")
        if bare_name not in KYC_TRACKED_FIELDS:
            continue

        root = parse_xml(obj_file)
        if root is None:
            continue

        tracked_fields: set[str] = set()
        for field_elem in root.iter():
            local_tag = field_elem.tag.split("}")[-1] if "}" in field_elem.tag else field_elem.tag
            if local_tag == "fields":
                name_elem = field_elem.find(".//{*}fullName") or field_elem.find("fullName")
                tracking_elem = (
                    field_elem.find(".//{*}trackHistory")
                    or field_elem.find("trackHistory")
                )
                if name_elem is not None and tracking_elem is not None:
                    if (tracking_elem.text or "").lower() == "true":
                        short_name = (name_elem.text or "").split("__")[0]
                        tracked_fields.add(short_name)

        tracked_by_object[bare_name] = tracked_fields

    for obj_name, required_fields in KYC_TRACKED_FIELDS.items():
        tracked = tracked_by_object.get(obj_name, set())
        missing = required_fields - tracked
        if missing:
            issues.append(
                f"Object '{obj_name}' is missing field history tracking on: "
                f"{', '.join(sorted(missing))}. These fields are required for "
                f"compliance audit trail. Enable trackHistory on each field, and "
                f"note that tracking is capped at 18 months without Salesforce Shield "
                f"Field Audit Trail."
            )

    return issues


def check_aml_apex_for_hardcoded_endpoints(manifest_dir: Path) -> list[str]:
    """Detect Apex classes with hardcoded AML vendor URLs or API tokens."""
    issues: list[str] = []

    SUSPICIOUS_STRINGS = [
        "onfido.com",
        "refinitiv.com",
        "lexisnexis.com",
        "worldcheck",
        "fircosoft",
        "accuity.com",
        "complyadvantage.com",
        "apikey",
        "api_key",
        "Authorization: Token",
    ]

    apex_files = find_files(manifest_dir, "*.cls")
    apex_files += find_files(manifest_dir, "*.cls-meta.xml")

    for apex_file in apex_files:
        try:
            content = apex_file.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        content_lower = content.lower()
        for pattern in SUSPICIOUS_STRINGS:
            if pattern.lower() in content_lower:
                # Skip metadata files that just declare the class
                if apex_file.suffix == ".xml":
                    continue
                issues.append(
                    f"Apex class '{apex_file.name}' may contain a hardcoded AML vendor "
                    f"endpoint or credential (found: '{pattern}'). Use Named Credentials "
                    f"for all external callouts. [{apex_file}]"
                )
                break

    return issues


def check_party_profile_risk_risk_category_picklist(manifest_dir: Path) -> list[str]:
    """Warn if PartyProfileRisk RiskCategory has no picklist values defined.

    An unconfigured picklist defaults to an empty or single-value set, which
    cannot represent the regulatory risk tier definitions (Low/Medium/High/Prohibited).
    """
    issues: list[str] = []

    object_files = find_files(manifest_dir, "*.object")
    object_files += find_files(manifest_dir, "*.object-meta.xml")

    for obj_file in object_files:
        obj_name = obj_file.stem.replace("-meta", "")
        if "PartyProfileRisk" not in obj_name and "partyprofileRisk" not in obj_name.lower():
            continue

        root = parse_xml(obj_file)
        if root is None:
            continue

        for field_elem in root.iter():
            local_tag = field_elem.tag.split("}")[-1] if "}" in field_elem.tag else field_elem.tag
            if local_tag != "fields":
                continue
            name_elem = field_elem.find(".//{*}fullName") or field_elem.find("fullName")
            if name_elem is None:
                continue
            field_name = (name_elem.text or "").lower()
            if "riskcategory" not in field_name:
                continue
            # Check for valueSet or picklist values
            value_elements = list(field_elem.iter("{*}value")) + list(field_elem.iter("value"))
            if not value_elements:
                issues.append(
                    f"PartyProfileRisk.RiskCategory has no picklist values defined in "
                    f"'{obj_file.name}'. Define at least Low, Medium, High, and Prohibited "
                    f"values to meet regulatory risk tier documentation requirements."
                )

    return issues


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def check_compliance_documentation_requirements(manifest_dir: Path) -> list[str]:
    """Return a list of issue strings found in the manifest directory."""
    issues: list[str] = []

    if not manifest_dir.exists():
        issues.append(f"Manifest directory not found: {manifest_dir}")
        return issues

    issues.extend(check_named_credential_auth_type(manifest_dir))
    issues.extend(check_hardcoded_credentials_in_named_credentials(manifest_dir))
    issues.extend(check_field_history_tracking(manifest_dir))
    issues.extend(check_aml_apex_for_hardcoded_endpoints(manifest_dir))
    issues.extend(check_party_profile_risk_risk_category_picklist(manifest_dir))

    return issues


def main() -> int:
    args = parse_args()
    manifest_dir = Path(args.manifest_dir)
    issues = check_compliance_documentation_requirements(manifest_dir)

    if not issues:
        print("No compliance documentation issues found.")
        return 0

    for issue in issues:
        print(f"WARN: {issue}", file=sys.stderr)

    return 1


if __name__ == "__main__":
    sys.exit(main())
