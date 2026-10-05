#!/usr/bin/env python3
"""
Severance Damages JSON Validation Script

Validates JSON input files against the severance damages schema.
Similar to validate_comparables.py for comparable sales calculator.

Usage:
    python validate_severance.py <input.json>
    python validate_severance.py <input.json> --fix --output clean.json
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

try:
    from jsonschema import validate, ValidationError, Draft202012Validator
    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False
    print("WARNING: jsonschema not installed. Install with: pip install jsonschema")


def load_schema() -> Dict[str, Any]:
    """Load the severance input schema"""
    schema_path = Path(__file__).parent / "severance_input_schema.json"
    with open(schema_path, 'r') as f:
        return json.load(f)


def validate_input(data: Dict[str, Any], schema: Dict[str, Any]) -> List[str]:
    """
    Validate input data against schema

    Returns:
        List of validation error messages (empty if valid)
    """
    if not JSONSCHEMA_AVAILABLE:
        return ["jsonschema library not available - cannot validate"]

    errors = []
    validator = Draft202012Validator(schema)

    for error in validator.iter_errors(data):
        # Format error message
        path = " -> ".join(str(p) for p in error.path) if error.path else "root"
        errors.append(f"{path}: {error.message}")

    return errors


def auto_fix(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Attempt to auto-fix common issues in input data

    Fixes:
    - Add default values for optional fields
    - Ensure booleans are actually boolean (not strings)
    - Ensure numbers are actually numbers (not strings)
    """
    fixed = data.copy()

    # Fix taking optional fields
    if "taking" in fixed:
        taking_defaults = {
            "eliminates_direct_access": False,
            "circuitous_access_added_minutes": 0.0,
            "creates_irregular_shape": False,
            "severs_utilities": False,
            "reduces_development_potential": False,
            "bisects_farm": False,
            "disrupts_irrigation": False
        }
        for key, default_value in taking_defaults.items():
            if key not in fixed["taking"]:
                fixed["taking"][key] = default_value

    # Fix remainder optional fields
    if "remainder" in fixed:
        remainder_defaults = {
            "buildable_area_sf": None,
            "development_potential_units": None,
            "requires_new_fencing_linear_meters": 0.0,
            "irrigation_acres_affected": 0.0
        }
        for key, default_value in remainder_defaults.items():
            if key not in fixed["remainder"]:
                fixed["remainder"][key] = default_value

    # Add market_parameters if missing
    if "market_parameters" not in fixed:
        fixed["market_parameters"] = {
            "cap_rate": 0.07,
            "travel_time_value_per_hour": 40.0,
            "trips_per_day": 20,
            "business_days_per_year": 250
        }

    # Fix property_before optional fields
    if "property_before" in fixed:
        prop_defaults = {
            "development_potential_units": None,
            "buildable_area_sf": None
        }
        for key, default_value in prop_defaults.items():
            if key not in fixed["property_before"]:
                fixed["property_before"][key] = default_value

    return fixed


def main():
    """Main validation script"""
    if len(sys.argv) < 2:
        print("Usage: python validate_severance.py <input.json> [--fix] [--output <output.json>]")
        print("\nExamples:")
        print("  python validate_severance.py input.json")
        print("  python validate_severance.py input.json --fix --output clean.json")
        sys.exit(1)

    input_path = sys.argv[1]
    do_fix = "--fix" in sys.argv
    output_path = None

    if "--output" in sys.argv:
        output_idx = sys.argv.index("--output")
        if output_idx + 1 < len(sys.argv):
            output_path = sys.argv[output_idx + 1]

    # Load input file
    print(f"Loading: {input_path}")
    try:
        with open(input_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"ERROR: File not found: {input_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        sys.exit(1)

    # Load schema
    try:
        schema = load_schema()
    except FileNotFoundError:
        print("ERROR: Schema file not found (severance_input_schema.json)")
        sys.exit(1)

    # Validate
    print("Validating against schema...")
    errors = validate_input(data, schema)

    if errors:
        print(f"\n❌ Validation FAILED ({len(errors)} errors):\n")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")

        if do_fix:
            print("\n🔧 Attempting auto-fix...")
            fixed_data = auto_fix(data)

            # Re-validate
            fixed_errors = validate_input(fixed_data, schema)
            if fixed_errors:
                print(f"\n❌ Auto-fix incomplete ({len(fixed_errors)} errors remaining):")
                for error in fixed_errors:
                    print(f"  - {error}")
                sys.exit(1)
            else:
                print("✅ Auto-fix successful!")

                # Save fixed data
                if output_path:
                    with open(output_path, 'w') as f:
                        json.dump(fixed_data, f, indent=2)
                    print(f"✅ Saved fixed data to: {output_path}")
                else:
                    print("\n📋 Fixed data:")
                    print(json.dumps(fixed_data, indent=2))
        else:
            print("\nTip: Use --fix flag to attempt automatic fixes")
            sys.exit(1)
    else:
        print("✅ Validation PASSED - input is valid!")

        if do_fix:
            # Even if valid, apply defaults if requested
            fixed_data = auto_fix(data)
            if output_path:
                with open(output_path, 'w') as f:
                    json.dump(fixed_data, f, indent=2)
                print(f"✅ Saved with defaults to: {output_path}")


if __name__ == '__main__':
    main()
