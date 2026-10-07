#!/usr/bin/env python3
"""
Data Validation Script for Due Diligence Templates

Validates that all required fields are present before template population.
This ensures deterministic, predictable output.

Usage:
    python validate_data.py <template_name> <data.json>

Example:
    python validate_data.py document-request-list data.json
"""

import json
import sys
import re
from pathlib import Path
from datetime import datetime

# Required fields for each template type
TEMPLATE_SCHEMAS = {
    "document-request-list": {
        "required": [
            "INVESTOR_NAME",
            "COMPANY_NAME",
            "REQUEST_DATE"
        ],
        "optional": [
            "INVESTOR_CONTACT",
            "INVESTOR_EMAIL",
            "COMPANY_STATE",
            "ENTITY_TYPE",
            "INVESTMENT_TYPE",
            "RESPONSE_DEADLINE",
            "ADDITIONAL_NOTES"
        ]
    },
    "diligence-report": {
        "required": [
            "COMPANY_NAME",
            "REPORT_DATE",
            "PREPARED_BY",
            "INVESTMENT_STAGE"
        ],
        "optional": [
            "COMPANY_STATE",
            "ENTITY_TYPE",
            "FOUNDING_DATE",
            "INVESTMENT_AMOUNT",
            "PRE_MONEY_VALUATION",
            "EXECUTIVE_SUMMARY",
            "CORPORATE_FINDINGS",
            "CAP_TABLE_FINDINGS",
            "IP_FINDINGS",
            "EMPLOYMENT_FINDINGS",
            "CONTRACT_FINDINGS",
            "COMPLIANCE_FINDINGS",
            "LITIGATION_FINDINGS",
            "FINANCIAL_FINDINGS",
            "CRITICAL_ISSUES",
            "MATERIAL_ISSUES",
            "MINOR_ISSUES",
            "RECOMMENDATIONS",
            "OPEN_ITEMS"
        ]
    },
    "issue-summary": {
        "required": [
            "COMPANY_NAME",
            "REVIEW_DATE",
            "REVIEWER_NAME"
        ],
        "optional": [
            "TOTAL_CRITICAL",
            "TOTAL_MATERIAL",
            "TOTAL_MINOR",
            "ISSUE_LIST"
        ]
    },
    "cap-table-memo": {
        "required": [
            "COMPANY_NAME",
            "ANALYSIS_DATE",
            "PREPARED_BY"
        ],
        "optional": [
            "FOUNDERS_EQUITY",
            "OPTION_POOL_SIZE",
            "SAFE_NOTES_TOTAL",
            "CONVERTIBLE_NOTES_TOTAL",
            "FULLY_DILUTED_SHARES",
            "PRO_FORMA_OWNERSHIP",
            "CAP_TABLE_ISSUES",
            "RECOMMENDATIONS"
        ]
    }
}

# Field format validators
FIELD_VALIDATORS = {
    "DATE": lambda v: bool(re.match(r'^\d{4}-\d{2}-\d{2}$', str(v))),
    "EMAIL": lambda v: bool(re.match(r'^[^@]+@[^@]+\.[^@]+$', str(v))),
    "PERCENTAGE": lambda v: isinstance(v, (int, float)) and 0 <= v <= 100,
    "CURRENCY": lambda v: isinstance(v, (int, float)) and v >= 0,
}


def get_field_type(field_name: str) -> str | None:
    """Infer field type from naming convention."""
    if field_name.endswith("_DATE") or field_name == "REPORT_DATE" or field_name == "REQUEST_DATE":
        return "DATE"
    if field_name.endswith("_EMAIL"):
        return "EMAIL"
    if "PERCENTAGE" in field_name or "PERCENT" in field_name:
        return "PERCENTAGE"
    if "AMOUNT" in field_name or "VALUATION" in field_name:
        return "CURRENCY"
    return None


def validate_field_format(field_name: str, value) -> tuple[bool, str]:
    """Validate field value format based on field type."""
    field_type = get_field_type(field_name)
    if field_type and field_type in FIELD_VALIDATORS:
        if not FIELD_VALIDATORS[field_type](value):
            return False, f"Invalid format for {field_type}"
    return True, ""


def validate(template_name: str, data: dict) -> tuple[bool, dict]:
    """
    Validate data against template schema.

    Args:
        template_name: Name of the template (without extension)
        data: Dictionary of field values

    Returns:
        Tuple of (is_valid, details)
        details contains: missing_required, invalid_fields, warnings
    """
    result = {
        "is_valid": True,
        "missing_required": [],
        "invalid_fields": [],
        "warnings": [],
        "template": template_name
    }

    # Check if template schema exists
    if template_name not in TEMPLATE_SCHEMAS:
        result["warnings"].append(f"No schema defined for template '{template_name}', skipping validation")
        return True, result

    schema = TEMPLATE_SCHEMAS[template_name]

    # Check required fields
    for field in schema["required"]:
        if field not in data or data[field] is None or str(data[field]).strip() == "":
            result["missing_required"].append(field)
            result["is_valid"] = False

    # Validate field formats
    for field, value in data.items():
        is_valid, error_msg = validate_field_format(field, value)
        if not is_valid:
            result["invalid_fields"].append({"field": field, "error": error_msg, "value": value})
            result["is_valid"] = False

    # Check for unknown fields (warnings only)
    known_fields = set(schema["required"]) | set(schema.get("optional", []))
    for field in data.keys():
        if field not in known_fields:
            result["warnings"].append(f"Unknown field '{field}' - will be ignored if no matching placeholder")

    return result["is_valid"], result


def main():
    """CLI entry point."""
    if len(sys.argv) != 3:
        print("Usage: python validate_data.py <template_name> <data.json>")
        print("\nAvailable templates:")
        for name in TEMPLATE_SCHEMAS.keys():
            print(f"  - {name}")
        sys.exit(1)

    template_name = sys.argv[1]
    data_path = sys.argv[2]

    # Load data
    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: Data file not found: {data_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        sys.exit(1)

    # Validate
    is_valid, details = validate(template_name, data)

    # Output results
    if is_valid:
        print(f"VALID: Data passes validation for template '{template_name}'")
        if details["warnings"]:
            print("\nWarnings:")
            for warning in details["warnings"]:
                print(f"  - {warning}")
    else:
        print(f"INVALID: Data fails validation for template '{template_name}'")
        if details["missing_required"]:
            print("\nMissing required fields:")
            for field in details["missing_required"]:
                print(f"  - {field}")
        if details["invalid_fields"]:
            print("\nInvalid field formats:")
            for item in details["invalid_fields"]:
                print(f"  - {item['field']}: {item['error']} (value: {item['value']})")

        sys.exit(1)


if __name__ == "__main__":
    main()
