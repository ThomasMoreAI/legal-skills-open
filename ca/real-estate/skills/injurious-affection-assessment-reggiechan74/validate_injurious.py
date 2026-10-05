#!/usr/bin/env python3
"""
JSON Schema Validator for Injurious Affection Calculator Inputs

Features:
- Validates input files against JSON Schema (Draft 2020-12)
- Auto-fixes common issues (missing defaults, type conversions)
- Comprehensive error reporting
- Dry-run mode for validation without modification

Usage:
    python validate_injurious.py input.json                    # Validate only
    python validate_injurious.py input.json --fix              # Validate and auto-fix
    python validate_injurious.py input.json --fix --output fixed.json

Author: Claude Code
Version: 1.0.0
Date: 2025-11-15
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Dict, Any, List, Tuple
from jsonschema import validate, ValidationError, Draft202012Validator
from jsonschema.exceptions import SchemaError


# Color codes for terminal output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def load_schema() -> Dict[str, Any]:
    """Load JSON schema from file"""
    schema_path = Path(__file__).parent / 'injurious_affection_input_schema.json'

    if not schema_path.exists():
        print(f"{Colors.RED}✗ Schema file not found: {schema_path}{Colors.END}")
        sys.exit(1)

    with open(schema_path, 'r') as f:
        return json.load(f)


def load_input(input_path: str) -> Dict[str, Any]:
    """Load input JSON file"""
    if not Path(input_path).exists():
        print(f"{Colors.RED}✗ Input file not found: {input_path}{Colors.END}")
        sys.exit(1)

    with open(input_path, 'r') as f:
        return json.load(f)


def auto_fix_input(data: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    """
    Auto-fix common issues in input data

    Returns:
        Tuple of (fixed_data, list_of_fixes_applied)
    """
    fixes = []
    fixed_data = data.copy()

    # Ensure property section exists
    if 'property' not in fixed_data:
        print(f"{Colors.RED}✗ Missing required 'property' section{Colors.END}")
        sys.exit(1)

    # Ensure construction section exists
    if 'construction' not in fixed_data:
        print(f"{Colors.RED}✗ Missing required 'construction' section{Colors.END}")
        sys.exit(1)

    # Fix property defaults
    property_defaults = {
        'rental_income_monthly': 0.0,
        'distance_to_construction_m': 0.0,
        'number_of_units': 1,
        'business_type': None,
        'annual_revenue': 0.0,
        'background_noise_dba': 50.0
    }

    for key, default_value in property_defaults.items():
        if key not in fixed_data['property']:
            fixed_data['property'][key] = default_value
            fixes.append(f"Added default property.{key} = {default_value}")

    # Fix construction defaults
    construction_defaults = {
        'equipment': [],
        'dust_impact_zone': 'moderate',
        'vibration_ppv_mms': 0.0,
        'traffic_reduction_pct': 0.0,
        'construction_hours_per_day': 8,
        'night_work': False
    }

    for key, default_value in construction_defaults.items():
        if key not in fixed_data['construction']:
            fixed_data['construction'][key] = default_value
            fixes.append(f"Added default construction.{key} = {default_value}")

    # Fix equipment list defaults
    if 'equipment' in fixed_data['construction']:
        for i, equip in enumerate(fixed_data['construction']['equipment']):
            if 'days_per_week' not in equip:
                equip['days_per_week'] = 5
                fixes.append(f"Added default construction.equipment[{i}].days_per_week = 5")

    # Convert string numbers to floats/ints where needed
    numeric_conversions = [
        ('property', 'property_value', float),
        ('property', 'rental_income_monthly', float),
        ('property', 'distance_to_construction_m', float),
        ('property', 'number_of_units', int),
        ('property', 'annual_revenue', float),
        ('property', 'background_noise_dba', float),
        ('construction', 'duration_months', float),
        ('construction', 'vibration_ppv_mms', float),
        ('construction', 'traffic_reduction_pct', float),
        ('construction', 'construction_hours_per_day', int)
    ]

    for section, field, conversion_type in numeric_conversions:
        if section in fixed_data and field in fixed_data[section]:
            try:
                if isinstance(fixed_data[section][field], str):
                    original = fixed_data[section][field]
                    fixed_data[section][field] = conversion_type(original)
                    fixes.append(
                        f"Converted {section}.{field} from string '{original}' to "
                        f"{conversion_type.__name__}"
                    )
            except ValueError:
                pass

    # Convert equipment numeric fields
    if 'equipment' in fixed_data.get('construction', {}):
        for i, equip in enumerate(fixed_data['construction']['equipment']):
            equip_conversions = [
                ('dba_at_15m', float),
                ('hours_per_day', float),
                ('days_per_week', int)
            ]
            for field, conversion_type in equip_conversions:
                if field in equip and isinstance(equip[field], str):
                    try:
                        original = equip[field]
                        equip[field] = conversion_type(original)
                        fixes.append(
                            f"Converted construction.equipment[{i}].{field} from string "
                            f"'{original}' to {conversion_type.__name__}"
                        )
                    except ValueError:
                        pass

    # Ensure property_address is string
    if 'property_address' in fixed_data and not isinstance(fixed_data['property_address'], str):
        fixed_data['property_address'] = str(fixed_data['property_address'])
        fixes.append("Converted property_address to string")

    return fixed_data, fixes


def validate_input(
    data: Dict[str, Any],
    schema: Dict[str, Any],
    verbose: bool = False
) -> Tuple[bool, List[str]]:
    """
    Validate input against schema

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []

    try:
        validator = Draft202012Validator(schema)
        validation_errors = sorted(validator.iter_errors(data), key=lambda e: e.path)

        for error in validation_errors:
            path = '.'.join(str(p) for p in error.path) if error.path else 'root'
            errors.append(f"{path}: {error.message}")

        if not errors:
            return True, []

        return False, errors

    except SchemaError as e:
        errors.append(f"Schema error: {e.message}")
        return False, errors
    except Exception as e:
        errors.append(f"Validation error: {str(e)}")
        return False, errors


def main():
    parser = argparse.ArgumentParser(
        description='Validate and auto-fix injurious affection calculator input files'
    )
    parser.add_argument(
        'input_file',
        help='Path to input JSON file'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Auto-fix common issues'
    )
    parser.add_argument(
        '--output',
        help='Output path for fixed file (default: overwrite input)',
        default=None
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )

    args = parser.parse_args()

    # Load schema and input
    print(f"{Colors.BOLD}Loading schema and input...{Colors.END}")
    schema = load_schema()
    data = load_input(args.input_file)
    print(f"{Colors.GREEN}✓ Loaded successfully{Colors.END}\n")

    # Initial validation
    print(f"{Colors.BOLD}Validating input...{Colors.END}")
    is_valid, errors = validate_input(data, schema, args.verbose)

    if is_valid:
        print(f"{Colors.GREEN}✓ Input is valid!{Colors.END}")
        return 0

    # Display errors
    print(f"{Colors.RED}✗ Validation failed with {len(errors)} error(s):{Colors.END}")
    for i, error in enumerate(errors, 1):
        print(f"  {i}. {error}")
    print()

    if not args.fix:
        print(f"{Colors.YELLOW}Run with --fix to attempt auto-repair{Colors.END}")
        return 1

    # Auto-fix
    print(f"{Colors.BOLD}Attempting auto-fix...{Colors.END}")
    fixed_data, fixes = auto_fix_input(data)

    if fixes:
        print(f"{Colors.BLUE}Applied {len(fixes)} fix(es):{Colors.END}")
        for i, fix in enumerate(fixes, 1):
            print(f"  {i}. {fix}")
        print()

    # Validate fixed data
    print(f"{Colors.BOLD}Validating fixed input...{Colors.END}")
    is_valid, errors = validate_input(fixed_data, schema, args.verbose)

    if is_valid:
        print(f"{Colors.GREEN}✓ Fixed input is valid!{Colors.END}\n")

        # Save fixed data
        output_path = args.output if args.output else args.input_file
        with open(output_path, 'w') as f:
            json.dump(fixed_data, f, indent=2)

        print(f"{Colors.GREEN}✓ Saved fixed input to: {output_path}{Colors.END}")
        return 0

    else:
        print(f"{Colors.RED}✗ Fixed input still has {len(errors)} error(s):{Colors.END}")
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        print()
        print(f"{Colors.YELLOW}Manual fixes required - see errors above{Colors.END}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
