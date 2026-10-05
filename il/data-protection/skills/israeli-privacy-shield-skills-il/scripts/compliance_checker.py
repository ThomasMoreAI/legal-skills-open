#!/usr/bin/env python3
"""
Israeli Privacy Protection Law, Compliance Checker

Standalone script that walks through a compliance assessment for the
Israeli Privacy Protection Law 1981 and 2017 Security Regulations.

Usage:
    python compliance_checker.py --example
    python compliance_checker.py --json '{"record_count":50000,"has_sensitive":true,"is_government":false,"is_health_finance":true,"is_direct_marketing":false,"is_credit_service":false,"has_cross_border":true}'
    python compliance_checker.py --output report.json
"""

import argparse
import json
import sys
from datetime import datetime


def determine_security_level(record_count: int, has_sensitive: bool,
                              is_government: bool, is_health_finance: bool,
                              authorized_users: int = 0) -> str:
    """Determine the required security level per the 2017 regulations.

    Two corrections made in v1.6.0, both of which the tool previously got wrong in a way
    that mattered:

    1. The 100-or-more-authorized-users trigger is documented in this skill's own Step 1
       table and had NO input here, so a 20,000-record database with 150 authorized users
       scored MEDIUM when the skill's own prose puts it at HIGH. That under-implements a
       penetration test, a risk survey, an incident-response plan and an external audit.
    2. Sector membership alone no longer forces HIGH. A 500-patient clinic was being told
       to commission an external audit and a penetration test. Health, insurance and
       financial-sector databases are treated here as reaching MEDIUM on sector alone and
       HIGH only when they also cross a count threshold. THIS IS A JUDGEMENT ABOUT THE
       SCHEDULE AND IT IS NOT VERIFIED IN THIS SKILL: read the regulations' schedule for a
       real determination, and treat this tool as a first sort rather than an answer.
    """
    if is_government or record_count >= 100_000 or authorized_users >= 100:
        return "high"
    if record_count >= 10_000 or has_sensitive or is_health_finance:
        return "medium"
    return "basic"


def check_registration_required(record_count: int, has_sensitive: bool,
                                 is_data_broker: bool, is_public_body: bool,
                                 is_credit_service: bool) -> bool:
    """Check if database registration with the Privacy Protection Authority is required.

    Amendment 13 (in force 2025-08-14) NARROWED registration. It is now required ONLY for:
      (a) a public body, or
      (b) a data broker: a database of 10,000+ individuals whose PRIMARY purpose is
          disclosing personal data to third parties as a business or for value.
    The pre-Amendment triggers were ABOLISHED: a credit-information service no longer
    forces registration on its own, and "any sensitive database over a threshold" no
    longer applies. has_sensitive and is_credit_service therefore do NOT force registration.
    CORRECTED in v1.6.0. is_direct_marketing was previously used as a proxy for the
    data-broker test. That resurrected the very pre-Amendment trigger this docstring says
    was abolished: any e-commerce or SaaS company that markets to its own customers
    answered yes and was told to register. Direct marketing to your OWN customers is not
    data brokerage. Registration now requires the explicit is_data_broker input.
    """
    if is_public_body:
        return True
    if record_count >= 10_000 and is_data_broker:
        return True
    return False


def check_notification_required(record_count: int, has_sensitive: bool) -> bool:
    """Separate from registration: a controller of a NON-registered database holding
    especially-sensitive data on MORE THAN 100,000 individuals must file a notification
    with the PPA within 30 days (Amendment 13)."""
    return record_count > 100_000 and has_sensitive


def build_checklist(security_level: str) -> list:
    """Build compliance checklist based on security level."""
    base_checklist = [
        {"item": "Physical security of premises", "level": "basic"},
        {"item": "Access control (user authentication)", "level": "basic"},
        {"item": "Activity logging", "level": "basic"},
        {"item": "Backup procedures", "level": "basic"},
        {"item": "Written security procedures document", "level": "basic"},
        {"item": "Employee awareness training", "level": "basic"},
        {"item": "Privacy policy published (Hebrew)", "level": "basic"},
        {"item": "Consent mechanisms in place", "level": "basic"},
        {"item": "Data subject request handling process", "level": "basic"},
    ]

    medium_additions = [
        {"item": "Encryption of data at rest and in transit", "level": "medium"},
        {"item": "Security officer (memune al bitachon meida) appointed", "level": "medium"},
        {"item": "Periodic access review", "level": "medium"},
        {"item": "Enhanced logging and monitoring", "level": "medium"},
        {"item": "Incident response procedures", "level": "medium"},
        {"item": "Third-party access controls", "level": "medium"},
        {"item": "Data processing agreements with service providers", "level": "medium"},
        {"item": "Cross-border transfer safeguards", "level": "medium"},
    ]

    high_additions = [
        {"item": "Annual security audit by external auditor", "level": "high"},
        {"item": "Comprehensive incident response plan", "level": "high"},
        {"item": "Data Protection Officer (DPO) appointed", "level": "high"},
        {"item": "Penetration testing conducted", "level": "high"},
        {"item": "Advanced encryption standards", "level": "high"},
        {"item": "Detailed data flow mapping", "level": "high"},
        {"item": "Regular employee training program", "level": "high"},
        {"item": "Business continuity plan", "level": "high"},
    ]

    checklist = list(base_checklist)
    if security_level in ("medium", "high"):
        checklist.extend(medium_additions)
    if security_level == "high":
        checklist.extend(high_additions)
    return checklist


def run_interactive_assessment() -> dict:
    """Run an interactive compliance assessment."""
    print("=" * 60)
    print("Israeli Privacy Protection Law, Compliance Assessment")
    print("=" * 60)
    print()
    print("DISCLAIMER: This tool provides guidance only. It does not")
    print("replace legal counsel. Consult a privacy attorney for")
    print("specific compliance decisions.")
    print()

    # Gather information
    org_name = input("Organization name: ").strip() or "Unknown"

    try:
        record_count = int(input("Number of records in your database(s): ").strip())
    except ValueError:
        record_count = 0

    has_sensitive = input("Contains sensitive data? (health, genetics, political, criminal) [y/n]: ").strip().lower() == "y"
    is_government = input("Is this a government/public body? [y/n]: ").strip().lower() == "y"
    is_health_finance = input("Health or financial sector? [y/n]: ").strip().lower() == "y"
    is_direct_marketing = input("Used for direct marketing? [y/n]: ").strip().lower() == "y"
    is_data_broker = input("Is the database's MAIN purpose disclosing personal data to third\n  parties as a business or for value (data brokerage)? Marketing to your own\n  customers is NOT data brokerage. [y/n]: ").strip().lower() == "y"
    try:
        authorized_users = int(input("How many people hold authorised access to the database? [0]: ").strip() or "0")
    except ValueError:
        authorized_users = 0
    is_credit_service = input("Credit/financial information service? [y/n]: ").strip().lower() == "y"
    has_cross_border = input("Transfers data outside Israel? [y/n]: ").strip().lower() == "y"

    # Determine results
    security_level = determine_security_level(record_count, has_sensitive,
                                               is_government, is_health_finance,
                                               authorized_users)
    registration_required = check_registration_required(record_count, has_sensitive,
                                                         is_data_broker,
                                                         is_government or False,
                                                         is_credit_service)
    notification_required = check_notification_required(record_count, has_sensitive)
    checklist = build_checklist(security_level)

    # Build report
    report = {
        "assessment_date": datetime.now().isoformat(),
        "organization": org_name,
        "inputs": {
            "record_count": record_count,
            "has_sensitive_data": has_sensitive,
            "is_government": is_government,
            "is_health_finance": is_health_finance,
            "is_direct_marketing": is_direct_marketing,
            "is_data_broker": is_data_broker,
            "authorized_users": authorized_users,
            "is_credit_service": is_credit_service,
            "has_cross_border_transfer": has_cross_border,
        },
        "results": {
            "security_level": security_level,
            "registration_required": registration_required,
            "ppa_notification_required_100k_sensitive": notification_required,
            "cross_border_review_needed": has_cross_border,
        },
        "checklist": checklist,
    }

    # Display results
    print()
    print("=" * 60)
    print("ASSESSMENT RESULTS")
    print("=" * 60)
    print(f"Organization: {org_name}")
    print(f"Security Level Required: {security_level.upper()}")
    print(f"Database Registration Required: {'YES' if registration_required else 'NO'}")
    # This line was COMPUTED and never printed before v1.6.0. A controller of a 400,000-person
    # sensitive database saw only "Registration: NO" and filed nothing, missing a statutory
    # notification. Registration and notification are separate duties and either can apply
    # without the other.
    print(f"PPA Notification (100,000+ especially-sensitive): {'REQUIRED' if notification_required else 'not applicable'}")
    print(f"Cross-Border Transfer Review: {'NEEDED' if has_cross_border else 'N/A'}")
    print()
    print("COMPLIANCE CHECKLIST:")
    print("-" * 40)
    for i, item in enumerate(checklist, 1):
        print(f"  [ ] {i}. {item['item']} ({item['level']} level)")

    if notification_required:
        print()
        print("ACTION REQUIRED: file a notification with the Privacy Protection Authority")
        print("  within 30 days. This is SEPARATE from registration and is owed even when")
        print("  registration is not required, because the database holds especially-sensitive")
        print("  data on more than 100,000 people.")

    if registration_required:
        print()
        print("ACTION REQUIRED: Register database with Privacy Protection Authority")
        print("URL: https://www.gov.il/he/departments/the_privacy_protection_authority")

    if has_cross_border:
        print()
        print("ACTION REQUIRED: Review cross-border transfer safeguards")
        print("Ensure recipient country has adequate protection or contractual safeguards")

    print()
    print("REMINDER: Consult a licensed privacy attorney (orech din)")
    print("for specific compliance decisions.")

    return report


def run_from_json(json_input: str, org_name: str = "Unknown") -> dict:
    """Run compliance assessment from JSON input (non-interactive).

    Args:
        json_input: JSON string with assessment parameters.
        org_name: Organization name.

    Returns:
        Assessment report dictionary.
    """
    try:
        params = json.loads(json_input)
    except json.JSONDecodeError:
        print("Error: Invalid JSON input.", file=sys.stderr)
        sys.exit(1)

    # REJECT unknown keys rather than defaulting them away. Silently ignoring a
    # misspelled key is the worst failure this tool can have: passing {"records":150000,
    # "sensitive":true} instead of {"record_count":150000,"has_sensitive":true} used to
    # return BASIC with 9 checklist items for a 150,000-record sensitive health database
    # that actually requires HIGH with 25, with no error and no warning. An organisation
    # acting on that under-implements into exactly the fines this skill documents.
    KNOWN = {
        "record_count", "has_sensitive", "is_government", "is_health_finance",
        "is_direct_marketing", "is_credit_service", "has_cross_border",
        "is_data_broker", "authorized_users",
    }
    if not isinstance(params, dict):
        print(f"Error: --json must be a JSON object, got {type(params).__name__}.", file=sys.stderr)
        sys.exit(1)
    unknown = sorted(set(params) - KNOWN)
    if unknown:
        print(f"Error: unrecognised key(s) in --json: {', '.join(unknown)}", file=sys.stderr)
        print(f"       Valid keys are: {', '.join(sorted(KNOWN))}", file=sys.stderr)
        print("       Refusing to assess rather than silently treating the value as absent,", file=sys.stderr)
        print("       which would downgrade the required security level.", file=sys.stderr)
        sys.exit(1)
    if "record_count" not in params:
        print("Error: record_count is required. It is the main determinant of the security", file=sys.stderr)
        print("       level, and omitting it would default the assessment to BASIC.", file=sys.stderr)
        sys.exit(1)

    record_count = params.get("record_count", 0)
    if not isinstance(record_count, int) or isinstance(record_count, bool) or record_count < 0:
        print(f"Error: record_count must be a non-negative integer, got {record_count!r}.", file=sys.stderr)
        sys.exit(1)
    for key in ("has_sensitive", "is_government", "is_health_finance",
                "is_direct_marketing", "is_credit_service", "has_cross_border",
                "is_data_broker"):
        if key in params and not isinstance(params[key], bool):
            print(f"Error: {key} must be true or false, got {params[key]!r}.", file=sys.stderr)
            sys.exit(1)

    has_sensitive = params.get("has_sensitive", False)
    is_government = params.get("is_government", False)
    is_health_finance = params.get("is_health_finance", False)
    is_direct_marketing = params.get("is_direct_marketing", False)
    is_data_broker = params.get("is_data_broker", False)
    authorized_users = params.get("authorized_users", 0)
    if not isinstance(authorized_users, int) or isinstance(authorized_users, bool) or authorized_users < 0:
        print(f"Error: authorized_users must be a non-negative integer, got {authorized_users!r}.", file=sys.stderr)
        sys.exit(1)
    is_credit_service = params.get("is_credit_service", False)
    has_cross_border = params.get("has_cross_border", False)

    security_level = determine_security_level(record_count, has_sensitive,
                                               is_government, is_health_finance,
                                               authorized_users)
    registration_required = check_registration_required(record_count, has_sensitive,
                                                         is_data_broker,
                                                         is_government,
                                                         is_credit_service)
    notification_required = check_notification_required(record_count, has_sensitive)
    checklist = build_checklist(security_level)

    report = {
        "assessment_date": datetime.now().isoformat(),
        "organization": org_name,
        "inputs": {
            "record_count": record_count,
            "has_sensitive_data": has_sensitive,
            "is_government": is_government,
            "is_health_finance": is_health_finance,
            "is_direct_marketing": is_direct_marketing,
            "is_data_broker": is_data_broker,
            "authorized_users": authorized_users,
            "is_credit_service": is_credit_service,
            "has_cross_border_transfer": has_cross_border,
        },
        "results": {
            "security_level": security_level,
            "registration_required": registration_required,
            "ppa_notification_required_100k_sensitive": notification_required,
            "cross_border_review_needed": has_cross_border,
        },
        "checklist": checklist,
    }

    print(f"Organization: {org_name}")
    print(f"Security Level Required: {security_level.upper()}")
    print(f"Database Registration Required: {'YES' if registration_required else 'NO'}")
    # This line was COMPUTED and never printed before v1.6.0. A controller of a 400,000-person
    # sensitive database saw only "Registration: NO" and filed nothing, missing a statutory
    # notification. Registration and notification are separate duties and either can apply
    # without the other.
    print(f"PPA Notification (100,000+ especially-sensitive): {'REQUIRED' if notification_required else 'not applicable'}")
    print(f"Cross-Border Transfer Review: {'NEEDED' if has_cross_border else 'N/A'}")
    print(f"Checklist items: {len(checklist)}")
    if notification_required:
        print()
        print("ACTION REQUIRED: file a notification with the Privacy Protection Authority")
        print("  within 30 days. SEPARATE from registration and owed even when registration")
        print("  is not required, because the database holds especially-sensitive data on")
        print("  more than 100,000 people.")
    if registration_required:
        print()
        print("ACTION REQUIRED: register the database with the Privacy Protection Authority.")
    if has_cross_border:
        print()
        print("ACTION REQUIRED: review cross-border transfer conditions. A lawful basis is not")
        print("  by itself sufficient: see SKILL.md Step 4, and read the Transfer of Data to")
        print("  Databases Abroad Regulations, whose additional conditions this skill does not")
        print("  carry in full.")

    return report


def run_example() -> dict:
    """Run a demo assessment with example data."""
    print("=== Example: Israeli Health-Tech Startup ===")
    print()
    example_json = json.dumps({
        "record_count": 50000,
        "has_sensitive": True,
        "is_government": False,
        "is_health_finance": True,
        "is_direct_marketing": False,
        "is_data_broker": False,
        "authorized_users": 0,
        "is_credit_service": False,
        "has_cross_border": True,
    })
    report = run_from_json(example_json, org_name="Example Health-Tech Startup")
    print()
    print("COMPLIANCE CHECKLIST:")
    print("-" * 40)
    for i, item in enumerate(report["checklist"], 1):
        print(f"  [ ] {i}. {item['item']} ({item['level']} level)")
    return report


def main():
    parser = argparse.ArgumentParser(
        description="Israeli Privacy Protection Law Compliance Checker"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path for JSON report",
        default=None
    )
    parser.add_argument(
        "--json",
        help='JSON string with parameters (non-interactive mode)',
        default=None
    )
    parser.add_argument(
        "--org-name",
        help="Organization name (used with --json)",
        default="Unknown"
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Run example assessment"
    )
    args = parser.parse_args()

    if args.example:
        report = run_example()
    elif args.json:
        report = run_from_json(args.json, args.org_name)
    else:
        report = run_interactive_assessment()

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"\nReport saved to: {args.output}")


if __name__ == "__main__":
    main()
