#!/usr/bin/env python3
"""Quick sanity checks for Israeli employment contract numerical fields.

Validates:
- Pension contribution rates against Mandatory Pension Order 2008 minimums
- Hoda'at mukdemet days against Prior Notice Law 2001 schedule
- Annual vacation days against the higher of Annual Leave Law 1951 and the Shortened Work Week extension order
- Sick days against Sick Pay Law 1976

Usage:
    python contract_sanity_check.py --pension-employer 6.5 --pension-severance 8.33 --pension-employee 6 --notice-days 30 --tenure-months 24 --worker-type monthly --vacation 12 --sick 18
    python contract_sanity_check.py --example
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

MANDATORY_PENSION_EMPLOYER_BENEFITS_MIN = 6.5
MANDATORY_PENSION_SEVERANCE_MIN = 6.0  # Below this is not enough for severance coverage
MANDATORY_PENSION_SEVERANCE_FULL = 8.33  # Standard for full Section 14 waiver
MANDATORY_PENSION_EMPLOYEE_STD = 6.0
MANDATORY_PENSION_EMPLOYEE_MIN = 6.0  # Expansion Order floor. 7% is credit-optimal under s.45a.
KH_EMPLOYER_STD = 7.5
KH_EMPLOYEE_STD = 2.5


@dataclass
class Finding:
    severity: str  # "blocker" | "major" | "minor"
    field: str
    observed: str
    expected: str
    rule: str


def required_notice_days_monthly(tenure_months: int) -> float:
    if tenure_months <= 0:
        return 0
    if tenure_months <= 6:
        return float(tenure_months)
    if tenure_months <= 12:
        return 6 + 2.5 * (tenure_months - 6)
    return 30.0


def required_notice_days_hourly(tenure_months: int) -> float:
    """Statutory advance notice for hourly/daily workers (oved sha'ati/yomi).

    This is a DIFFERENT schedule from monthly workers, per the Prior Notice Law
    2001 as summarized by Kolzchut:
      - Year 1 (months 1-12):  1 day per month worked.
      - Year 2 (months 13-24): 14 days + 1 day for every 2 months worked in year 2.
      - Year 3 (months 25-36): 21 days + 1 day for every 2 months worked in year 3.
      - 3+ years (month 37+):  30 days, flat.
    """
    if tenure_months <= 0:
        return 0
    if tenure_months <= 12:
        return float(tenure_months)
    if tenure_months <= 24:
        months_into_year = tenure_months - 12
        return 14 + (months_into_year // 2)
    if tenure_months <= 36:
        months_into_year = tenure_months - 24
        return 21 + (months_into_year // 2)
    return 30.0


def extension_order_net_vacation_days(tenure_years: int) -> int:
    """Net leave days per the Shortened Work Week extension order (5-day week).

    The order states NET days (actual absence days, excluding the weekly rest):
    12 for years 1-5, 17 for years 6-8, and 23 from year 9. It covers most
    5-day workplaces but NOT domestic work, workplaces with fewer than four
    employees, government or municipal companies, or workplaces whose move to a
    5-day week was settled by a collective agreement.
    """
    if tenure_years <= 5:
        return 12
    if tenure_years <= 8:
        return 17
    return 23


def gross_vacation_days(tenure_years: int) -> int:
    """Statutory gross leave days per Annual Leave Law 1951 s.3(a)."""
    if tenure_years <= 5:
        return 16
    if tenure_years == 6:
        return 18
    if tenure_years == 7:
        return 21
    return min(28, 21 + (tenure_years - 7))


def statutory_net_vacation_days(tenure_years: int) -> int:
    """The statutory gross ladder converted to net absence days on a 5-day week.

    An employee on a 5-day week is absent 5 days for every 7 gross days. The
    part-day is rounded up, because a fraction of entitlement is not forfeited.
    """
    return -(-gross_vacation_days(tenure_years) * 5 // 7)


def required_vacation_days(tenure_years: int, extension_order_applies: bool = True) -> int:
    """Minimum annual leave in NET working days for a 5-day week.

    Two ladders apply and the employee is entitled to the HIGHER of them: the
    Annual Leave Law and, where it covers the workplace, the Shortened Work
    Week extension order. Encoding only the statute understates the minimum
    from year 6 onward for most private-sector employees.
    """
    statutory = statutory_net_vacation_days(tenure_years)
    if not extension_order_applies:
        return statutory
    return max(statutory, extension_order_net_vacation_days(tenure_years))


def check(
    pension_employer_benefits: float,
    pension_severance: float,
    pension_employee: float,
    notice_days: float,
    tenure_months: int,
    worker_type: str,
    vacation_days: int,
    sick_days_per_year: int,
    kh_employer: float | None = None,
    extension_order_applies: bool = True,
) -> list[Finding]:
    findings: list[Finding] = []
    tenure_years = max(1, tenure_months // 12)

    if pension_employer_benefits < MANDATORY_PENSION_EMPLOYER_BENEFITS_MIN:
        findings.append(
            Finding(
                severity="blocker",
                field="Employer pension (benefits component)",
                observed=f"{pension_employer_benefits}%",
                expected=f">= {MANDATORY_PENSION_EMPLOYER_BENEFITS_MIN}%",
                rule="Mandatory Pension Expansion Order 2008",
            )
        )

    if pension_employee < MANDATORY_PENSION_EMPLOYEE_MIN:
        findings.append(
            Finding(
                severity="blocker",
                field="Employee pension (employee component)",
                observed=f"{pension_employee}%",
                expected=f">= {MANDATORY_PENSION_EMPLOYEE_MIN}%",
                rule="Mandatory Pension Expansion Order 2008 (6% is the minimum, not a maximum)",
            )
        )

    if pension_severance < MANDATORY_PENSION_SEVERANCE_MIN:
        findings.append(
            Finding(
                severity="blocker",
                field="Employer pension (severance component)",
                observed=f"{pension_severance}%",
                expected=f">= {MANDATORY_PENSION_SEVERANCE_MIN}%",
                rule="Mandatory Pension Expansion Order 2008",
            )
        )
    elif pension_severance < MANDATORY_PENSION_SEVERANCE_FULL:
        findings.append(
            Finding(
                severity="major",
                field="Employer pension (severance component)",
                observed=f"{pension_severance}%",
                expected=f"{MANDATORY_PENSION_SEVERANCE_FULL}% for full Section 14 waiver",
                rule="Severance Pay Law 1963 Section 14 + General Authorization",
            )
        )

    if pension_employee > 7.0:
        findings.append(
            Finding(
                severity="minor",
                field="Employee pension contribution",
                observed=f"{pension_employee}%",
                expected="6% minimum, 7% is the ceiling that still earns the s.45a credit",
                rule="Income Tax Ordinance s.45a: contributions above 7% earn no further credit",
            )
        )

    required_notice = (
        required_notice_days_monthly(tenure_months)
        if worker_type == "monthly"
        else required_notice_days_hourly(tenure_months)
    )
    if notice_days < required_notice:
        findings.append(
            Finding(
                severity="blocker",
                field="Hoda'at Mukdemet",
                observed=f"{notice_days} days",
                expected=f">= {required_notice} days at tenure {tenure_months} months ({worker_type})",
                rule="Prior Notice of Dismissal and Resignation Law 2001",
            )
        )

    required_vacation = required_vacation_days(tenure_years, extension_order_applies)
    if vacation_days < required_vacation:
        findings.append(
            Finding(
                severity="major",
                field="Annual vacation days",
                observed=f"{vacation_days} days",
                expected=f">= {required_vacation} days at tenure year {tenure_years}",
                rule="Annual Leave Law 1951 + Shortened Work Week extension order (higher of the two)",
            )
        )

    if sick_days_per_year < 18:
        findings.append(
            Finding(
                severity="major",
                field="Sick days per year",
                observed=f"{sick_days_per_year} days",
                expected=">= 18 days per year of accrual (1.5 x 12). This is an accrual figure, NOT a statutory annual cap.",
                rule="Sick Pay Law 1976 s.4 (1.5 days/month accrual, 90-day balance). Check the payment ladder separately: day 1 unpaid, days 2-3 half, day 4+ full (ss.2, 5).",
            )
        )

    if kh_employer is not None and kh_employer < KH_EMPLOYER_STD:
        findings.append(
            Finding(
                severity="minor",
                field="Keren Hishtalmut employer %",
                observed=f"{kh_employer}%",
                expected=f"~{KH_EMPLOYER_STD}% standard split",
                rule="Industry standard (not mandatory)",
            )
        )

    return findings


def format_findings(findings: list[Finding]) -> str:
    if not findings:
        return "No sanity-check issues found. The numerical fields are within Israeli labor law minimums and industry standards."
    lines = ["=== Contract Sanity Check Findings ===", ""]
    by_severity = {"blocker": [], "major": [], "minor": []}
    for f in findings:
        by_severity[f.severity].append(f)
    for sev in ("blocker", "major", "minor"):
        if not by_severity[sev]:
            continue
        lines.append(f"[{sev.upper()}] ({len(by_severity[sev])})")
        for f in by_severity[sev]:
            lines.append(f"  - {f.field}")
            lines.append(f"      Observed: {f.observed}")
            lines.append(f"      Expected: {f.expected}")
            lines.append(f"      Rule: {f.rule}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sanity check numerical fields in an Israeli employment contract")
    parser.add_argument("--pension-employer", type=float, help="Employer pension benefits %%")
    parser.add_argument("--pension-severance", type=float, help="Employer severance contribution %%")
    parser.add_argument("--pension-employee", type=float, help="Employee pension %%")
    parser.add_argument("--notice-days", type=float, help="Hoda'at mukdemet days in contract")
    parser.add_argument("--tenure-months", type=int, help="Expected tenure in months for notice calc")
    parser.add_argument("--worker-type", choices=("monthly", "hourly"), default="monthly")
    parser.add_argument("--vacation", type=int, help="Annual vacation days")
    parser.add_argument("--sick", type=int, help="Annual sick days")
    parser.add_argument("--kh-employer", type=float, help="Keren Hishtalmut employer %%", default=None)
    parser.add_argument(
        "--no-extension-order",
        action="store_true",
        help="The Shortened Work Week extension order does NOT cover this workplace (domestic work, fewer than 4 employees, a government or municipal company, or a 5-day week set by a collective agreement). Scores annual leave on the Annual Leave Law alone.",
    )
    parser.add_argument("--example", action="store_true", help="Run with a sample contract")
    parser.add_argument("--self-test", action="store_true", help="Run golden-case assertions for the notice schedules")
    args = parser.parse_args()

    if args.self_test:
        # Monthly worker golden cases.
        assert required_notice_days_monthly(3) == 3.0, "monthly m3"
        assert required_notice_days_monthly(6) == 6.0, "monthly m6"
        assert required_notice_days_monthly(12) == 21.0, "monthly m12 (6 + 2.5*6)"
        assert required_notice_days_monthly(24) == 30.0, "monthly 2yr flat"
        # Hourly worker golden cases (different schedule).
        assert required_notice_days_hourly(1) == 1.0, "hourly m1"
        assert required_notice_days_hourly(12) == 12.0, "hourly end of year 1"
        assert required_notice_days_hourly(13) == 14.0, "hourly start of year 2 = 14"
        assert required_notice_days_hourly(18) == 17.0, "hourly 1.5yr = 14 + (6//2) = 17"
        assert required_notice_days_hourly(24) == 20.0, "hourly end year 2 = 14 + (12//2) = 20"
        assert required_notice_days_hourly(25) == 21.0, "hourly start year 3 = 21"
        assert required_notice_days_hourly(36) == 27.0, "hourly end year 3 = 21 + (12//2) = 27"
        assert required_notice_days_hourly(37) == 30.0, "hourly 3yr+ flat = 30"
        # Annual Leave Law s.3(a) gross ladder and its 5-day-week net conversion.
        assert gross_vacation_days(1) == 16, "gross y1"
        assert gross_vacation_days(5) == 16, "gross y5 (band is years 1-5, not 1-4)"
        assert gross_vacation_days(6) == 18, "gross y6"
        assert gross_vacation_days(7) == 21, "gross y7"
        assert gross_vacation_days(14) == 28, "gross y14 caps at 28"
        assert gross_vacation_days(30) == 28, "gross cap holds"
        assert statutory_net_vacation_days(1) == 12, "statute net y1 = ceil(16*5/7)"
        assert statutory_net_vacation_days(6) == 13, "statute net y6 = ceil(18*5/7)"
        assert statutory_net_vacation_days(7) == 15, "statute net y7 = 21*5/7"
        # Where the extension order applies it is higher from year 6 on, and it wins.
        assert required_vacation_days(1) == 12, "combined y1"
        assert required_vacation_days(5) == 12, "combined y5"
        assert required_vacation_days(6) == 17, "combined y6, order beats statute"
        assert required_vacation_days(9) == 23, "combined y9, order beats statute"
        assert required_vacation_days(9, extension_order_applies=False) == 17, "statute-only y9 = ceil(23*5/7)"
        # Employee 6 percent is a floor, not a maximum: anything under it must be a blocker.
        low = check(6.5, 6.0, 4.0, 30, 24, "monthly", 12, 18, 7.5)
        assert any(f.severity == "blocker" and "Employee pension" in f.field for f in low), "employee floor"
        print("All notice-schedule golden cases passed.")
        return 0

    if args.example:
        print("Example: 2-year contract, pension 6.5%/8.33%/6%, 30 days notice, 12 days vacation, 18 sick, KH 7.5%")
        print("")
        findings = check(
            pension_employer_benefits=6.5,
            pension_severance=8.33,
            pension_employee=6.0,
            notice_days=30,
            tenure_months=24,
            worker_type="monthly",
            vacation_days=12,
            sick_days_per_year=18,
            kh_employer=7.5,
        )
        print(format_findings(findings))
        print()
        print("Now with a broken contract (low notice, low pension):")
        print("")
        findings = check(
            pension_employer_benefits=5.0,
            pension_severance=6.0,
            pension_employee=6.0,
            notice_days=7,
            tenure_months=24,
            worker_type="monthly",
            vacation_days=10,
            sick_days_per_year=12,
            kh_employer=None,
        )
        print(format_findings(findings))
        return 0

    required = [
        "pension_employer",
        "pension_severance",
        "pension_employee",
        "notice_days",
        "tenure_months",
        "vacation",
        "sick",
    ]
    for r in required:
        if getattr(args, r) is None:
            parser.print_help()
            print(f"\nError: --{r.replace('_', '-')} is required (or use --example)", file=sys.stderr)
            return 1

    findings = check(
        pension_employer_benefits=args.pension_employer,
        pension_severance=args.pension_severance,
        pension_employee=args.pension_employee,
        notice_days=args.notice_days,
        tenure_months=args.tenure_months,
        worker_type=args.worker_type,
        vacation_days=args.vacation,
        sick_days_per_year=args.sick,
        kh_employer=args.kh_employer,
        extension_order_applies=not args.no_extension_order,
    )
    print(format_findings(findings))
    return 0


if __name__ == "__main__":
    sys.exit(main())
