#!/usr/bin/env python3
"""Generate Israeli employment contract templates with calculated benefit rates.

Produces a structured employment contract with all mandatory Israeli clauses
pre-filled based on employee details: name, position, salary, start date,
and work percentage.

Usage:
    python generate_contract.py --help
    python generate_contract.py \
        --employee-name "Israel Israeli" \
        --position "Software Engineer" \
        --salary 25000 \
        --start-date 2026-04-01 \
        --work-percent 100

    python generate_contract.py \
        --employee-name "Dana Cohen" \
        --position "Marketing Manager" \
        --salary 15000 \
        --start-date 2026-05-01 \
        --work-percent 60 \
        --output contract_dana.md
"""

import argparse
import sys
from datetime import datetime, timedelta
from typing import Optional


# --- Current rates ---
# Last verified: 2026-05-09. Update annually when extension orders change.
# Sources:
#   Minimum wage: Histadrut announcement, effective 2026-04-01
#     https://global.histadrut.org.il/news/israels-minimum-wage-to-rise-by-3-3/
#   Dmei Havra'a (private sector): Kolzchut -- frozen at 2023 level
#     https://www.kolzchut.org.il/he/%D7%93%D7%9E%D7%99_%D7%94%D7%91%D7%A8%D7%90%D7%94
#   Work hours: Hours of Work and Rest Law, 1951, as amended by extension order
#     effective 2018-04-01 (workweek reduced from 43 to 42 hours)

PENSION_EMPLOYER_RATE = 0.065       # 6.5%
PENSION_EMPLOYEE_RATE = 0.06        # 6%
SEVERANCE_RATE = 0.0833             # 8.33%
HISHTALMUT_EMPLOYER_RATE = 0.075    # 7.5%
HISHTALMUT_EMPLOYEE_RATE = 0.025    # 2.5%
HAVRA_A_DAILY_RATE = 451.5          # NIS per day, private-sector rate for havra'a year 2026
                                    # (1.7.2025-30.6.2026), per the extension order published 18.08.2026.
                                    # A signed agreement to raise it to 451.5 awaits a Ministry of
                                    # Labor extension order, then applies retroactively. Verify before use.
MINIMUM_WAGE_MONTHLY = 6443.85      # NIS, effective 2026-04-01 (prior: 6,247.67)
MINIMUM_WAGE_HOURLY = 35.40         # NIS, based on 182 hours/month (42h x 52 / 12)
STANDARD_WORK_HOURS_DAY = 8.4       # hours per day, 5-day week (5 x 8.4 = 42)
STANDARD_WORK_HOURS_WEEK = 42.0     # hours per week (since 2018-04-01)
STANDARD_WORK_DAYS_WEEK = 5         # days

# Convalescence days by seniority year
HAVRA_A_DAYS = {
    1: 5,
    2: 6, 3: 6,
    4: 7, 5: 7, 6: 7, 7: 7, 8: 7, 9: 7, 10: 7,
    11: 8, 12: 8, 13: 8, 14: 8, 15: 8,
    16: 9, 17: 9, 18: 9, 19: 9,
}
HAVRA_A_DAYS_20_PLUS = 10

# Annual leave days by seniority (5-day work week)
ANNUAL_LEAVE_DAYS = {
    1: 12, 2: 12, 3: 12, 4: 12,
    5: 16,
    6: 18,
}
ANNUAL_LEAVE_DAYS_7_PLUS = 21

SICK_DAYS_PER_MONTH = 1.5
SICK_DAYS_MAX = 90


def get_havra_a_days(seniority_years: int) -> int:
    """Return convalescence days for given seniority."""
    if seniority_years >= 20:
        return HAVRA_A_DAYS_20_PLUS
    return HAVRA_A_DAYS.get(seniority_years, 5)


def get_annual_leave_days(seniority_years: int) -> int:
    """Return minimum annual leave days for given seniority (5-day week)."""
    if seniority_years >= 7:
        return ANNUAL_LEAVE_DAYS_7_PLUS
    return ANNUAL_LEAVE_DAYS.get(seniority_years, 12)


def calculate_notice_period_days(seniority_months: int, pay_basis: str = "monthly") -> int:
    """Calculate notice period in days based on seniority and pay basis.

    The first-year ladder differs by pay basis (Prior Notice for Dismissal and
    Resignation Law, 2001):
      - monthly-paid (oved be'mascoret): months 1-6 = 1 day/month;
        months 7-12 = 6 days + 2.5 days per month from month 7.
      - daily/hourly-paid (oved be'sachar): a flat 1 day per month worked across
        the whole first year (up to 12 days at year-end).
    From year 2 onward both reach 30 days (1 month).
    """
    if seniority_months > 12:
        return 30  # 1 month, both pay bases

    if pay_basis == "hourly":
        # Daily/hourly worker: 1 day per month worked, all 12 months.
        return min(seniority_months, 12)

    # Monthly-paid worker.
    if seniority_months <= 6:
        return seniority_months  # 1 day per month
    months_after_6 = seniority_months - 6
    return 6 + int(months_after_6 * 2.5)


def calculate_benefits(salary: float, work_percent: float) -> dict:
    """Calculate all mandatory benefit amounts."""
    adjusted_salary = salary * (work_percent / 100.0)

    pension_employer = adjusted_salary * PENSION_EMPLOYER_RATE
    pension_employee = adjusted_salary * PENSION_EMPLOYEE_RATE
    severance_component = adjusted_salary * SEVERANCE_RATE
    hishtalmut_employer = adjusted_salary * HISHTALMUT_EMPLOYER_RATE
    hishtalmut_employee = adjusted_salary * HISHTALMUT_EMPLOYEE_RATE
    havra_a_first_year = get_havra_a_days(1) * HAVRA_A_DAILY_RATE

    total_employer_cost = (
        adjusted_salary
        + pension_employer
        + severance_component
        + hishtalmut_employer
    )

    return {
        "adjusted_salary": adjusted_salary,
        "pension_employer": pension_employer,
        "pension_employee": pension_employee,
        "severance_component": severance_component,
        "hishtalmut_employer": hishtalmut_employer,
        "hishtalmut_employee": hishtalmut_employee,
        "havra_a_first_year": havra_a_first_year,
        "total_employer_cost": total_employer_cost,
        "annual_leave_days_year1": get_annual_leave_days(1),
        "sick_days_per_month": SICK_DAYS_PER_MONTH,
        "notice_period_month1": calculate_notice_period_days(1),
        "notice_period_month6": calculate_notice_period_days(6),
        "notice_period_year2": calculate_notice_period_days(24),
        # Daily/hourly-paid (oved be'sachar) first-year notice differs: 1 day/month.
        "notice_period_hourly_month12": calculate_notice_period_days(12, pay_basis="hourly"),
        "notice_period_monthly_month12": calculate_notice_period_days(12, pay_basis="monthly"),
    }


def format_currency(amount: float) -> str:
    """Format amount as NIS currency."""
    return f"{amount:,.2f} NIS"


def generate_contract(
    employee_name: str,
    position: str,
    salary: float,
    start_date: str,
    work_percent: float,
    employer_name: str = "[EMPLOYER NAME]",
    employer_id: str = "[EMPLOYER ID]",
    employee_id: str = "[EMPLOYEE ID]",
) -> str:
    """Generate a full employment contract template."""

    benefits = calculate_benefits(salary, work_percent)
    adj_salary = benefits["adjusted_salary"]

    # Parse start date
    try:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
    except ValueError:
        start_dt = datetime.now()
    start_formatted = start_dt.strftime("%d/%m/%Y")

    # Probation end date (6 months)
    probation_end = start_dt + timedelta(days=180)
    probation_formatted = probation_end.strftime("%d/%m/%Y")

    position_percent = f"{work_percent:.0f}%"
    work_type = "Full-time" if work_percent == 100 else f"Part-time ({position_percent})"

    contract = f"""# Employment Contract / Chozeh Avoda
# חוזה עבודה

---

**Date / Taarich:** {start_formatted}

---

## 1. Parties / HaTzedadim / הצדדים

**Employer / Ma'asik / מעסיק:**
- Name: {employer_name}
- Company ID (Chet-Peh): {employer_id}
- Address: [EMPLOYER ADDRESS]

**Employee / Oved / עובד:**
- Name: {employee_name}
- ID Number (Teudat Zehut): {employee_id}
- Address: [EMPLOYEE ADDRESS]

---

## 2. Position / Tafkid / תפקיד

The Employee is hired for the position of **{position}**.
The Employee shall report to [MANAGER NAME / TITLE].
The Employee's responsibilities include: [DESCRIBE RESPONSIBILITIES].

---

## 3. Start Date and Probation / Taarich Hatchala VeTkufat Nisayon / תאריך התחלה ותקופת ניסיון

- **Start date:** {start_formatted}
- **Employment type:** {work_type}
- **Probation period (Tkufat Nisayon):** 6 months, ending {probation_formatted}
- During probation, either party may terminate; the statutory notice period applies (there is no statutory "shortened notice" during probation).
- Successful completion of probation does not require formal notice; employment continues automatically.

---

## 4. Work Hours / She'ot Avoda / שעות עבודה

- **Work days:** Sunday through Thursday (5-day work week)
- **Daily hours:** {STANDARD_WORK_HOURS_DAY} hours (per Hours of Work and Rest Law, as amended April 2018)
- **Weekly hours:** {STANDARD_WORK_HOURS_WEEK} hours
- **Position scope:** {position_percent} of full-time position
- **Overtime:** Per Hours of Work and Rest Law -- 125% for first 2 extra hours, 150% thereafter.
- **Weekly rest:** Friday-Saturday (at least 36 consecutive hours).

---

## 5. Salary / Sachar / שכר

- **Gross monthly salary:** {format_currency(adj_salary)}
- **Payment date:** No later than the 9th of the following month (per Protection of Wages Law / Chok Haganat HaSachar)
- **Payment method:** Bank transfer to Employee's designated account

---

## 6. Pension and Severance / Pensia VePitzuim / פנסיה ופיצויים

**Pension fund contributions (per Tzav Harchava / Extension Order):**

| Component | Employer | Employee |
|-----------|----------|----------|
| Pension (Tagmulim) | {PENSION_EMPLOYER_RATE*100:.1f}% = {format_currency(benefits['pension_employer'])} | {PENSION_EMPLOYEE_RATE*100:.1f}% = {format_currency(benefits['pension_employee'])} |
| Severance (Pitzuim) | {SEVERANCE_RATE*100:.2f}% = {format_currency(benefits['severance_component'])} | -- |

**Pension fund:** [FUND NAME, e.g., Meitav Dash, Menora, Harel, Migdal]

### Section 14 Arrangement / Hasdarot Saif 14 / הסדרות סעיף 14

In accordance with Section 14 of the Severance Pay Law, 1963, the Employer's
contributions to the pension fund / insurance policy as detailed above shall
constitute full and complete severance pay for the Employee in respect of the
salary on which said contributions were made and for the period they were made.

The Employee hereby agrees and acknowledges that the Employer's contributions
to the pension insurance fund shall come in lieu of the severance pay the
Employee is entitled to for said salary components, such that the Employer
shall be released from any additional severance payment obligation with respect
to these components.

**Employee acknowledgment:** _____________________ Date: __________

**Severance basis (if Section 14 is NOT elected):** Absent a Section 14
arrangement, the Employee's statutory severance under the Severance Pay Law,
1963 (Section 12) is one month's last salary for each year of employment with
the Employer, pro-rated for partial years, payable on termination.

---

## 7. Education Fund / Keren Hishtalmut / קרן השתלמות

| Component | Rate | Monthly Amount |
|-----------|------|----------------|
| Employer contribution | {HISHTALMUT_EMPLOYER_RATE*100:.1f}% | {format_currency(benefits['hishtalmut_employer'])} |
| Employee contribution | {HISHTALMUT_EMPLOYEE_RATE*100:.1f}% | {format_currency(benefits['hishtalmut_employee'])} |

**Fund:** [FUND NAME]
**Vesting:** 6 years (3 years for designated educational purposes)

---

## 8. Convalescence Pay / Dmei Havra'a / דמי הבראה

The Employee shall receive convalescence pay (Dmei Havra'a) per the applicable
extension order, based on seniority:

- **Year 1:** 5 days = {format_currency(5 * HAVRA_A_DAILY_RATE)} (at current daily rate of {format_currency(HAVRA_A_DAILY_RATE)})
- Payment: Annual lump sum, typically in June-July
- Days increase with seniority per the extension order table

---

## 9. Annual Leave / Chofsha Shnatit / חופשה שנתית

Per the Annual Leave Law (1951):
- **Years 1-4:** {get_annual_leave_days(1)} work days per year
- **Year 5:** {get_annual_leave_days(5)} work days per year
- **Year 6:** {get_annual_leave_days(6)} work days per year
- **Year 7+:** {get_annual_leave_days(7)} work days per year

{"Adjusted for part-time: " + str(int(get_annual_leave_days(1) * work_percent / 100)) + " days in year 1" if work_percent < 100 else ""}

---

## 10. Sick Leave / Yemei Machala / ימי מחלה

- **Accrual:** {SICK_DAYS_PER_MONTH} days per month ({SICK_DAYS_PER_MONTH * 12:.0f} days per year)
- **Maximum accumulation:** {SICK_DAYS_MAX} days
- **Payment tiers:**
  - Day 1: No payment
  - Days 2-3: 50% of daily salary
  - Day 4 onward: 100% of daily salary
- **Medical certificate:** Required from day 1 of absence (or per company policy)

---

## 11. Notice Period / Tkufat Hodaa Mukdemet / תקופת הודעה מוקדמת

Either party may terminate this agreement by providing written notice:

| Seniority | Monthly-paid (oved be'mascoret) | Daily/hourly-paid (oved be'sachar) |
|-----------|----------------------------------|-------------------------------------|
| Months 1-6 | 1 day per month of employment | 1 day per month worked (all 12 months) |
| Months 7-12 | 6 days + 2.5 days per additional month | 1 day per month worked (all 12 months) |
| Year 2+ | 30 days (1 month) | 30 days (1 month) |

The first-year ladders differ by pay basis: a daily/hourly-paid worker earns a
flat 1 day of notice per month worked across the whole first year (up to 12 days
at year-end), while a monthly-paid worker earns the 6-days-plus-2.5-per-month
schedule for months 7-12.

---

## 12. Confidentiality / Sodiyut / סודיות

The Employee undertakes to maintain the confidentiality of all proprietary
information, trade secrets, business plans, customer lists, technical data,
and any other confidential information of the Employer, both during and after
the term of employment.

This obligation shall survive the termination of employment for a period of
[DURATION, recommended: 24-36 months].

---

## 13. Intellectual Property / Kinyan Ruchani / קניין רוחני

All intellectual property, inventions, designs, works, software, documentation,
and any other work product created by the Employee during the course of
employment and/or using the Employer's resources shall be the sole and
exclusive property of the Employer.

The Employee hereby assigns to the Employer all rights, title, and interest
in and to such work product, including all patents, copyrights, and other
intellectual property rights.

The Employee shall disclose any pre-existing intellectual property in
Schedule A attached hereto.

**Pre-existing IP disclosure (Schedule A):** [ATTACH OR WRITE "NONE"]

---

## 14. Non-Compete / Ee Tcharut / אי-תחרות

For a period of [RECOMMENDED: 6-12] months following termination of employment,
the Employee shall not directly engage with the following specific competitors:
[LIST SPECIFIC COMPETITORS].

This restriction is limited to [DESCRIBE SPECIFIC SCOPE/FIELD].

Note: Israeli courts enforce non-compete clauses narrowly. This clause is
subject to the balancing test established by Israeli Supreme Court precedent,
weighing the Employer's legitimate business interests against the Employee's
right to earn a livelihood under Basic Law: Human Dignity and Liberty.

---

## 15. General Provisions / Horaot Klaliyot / הוראות כלליות

- **Governing law:** The laws of the State of Israel
- **Jurisdiction:** The Regional Labor Court of [CITY]
- **Entire agreement:** This contract constitutes the entire agreement between
  the parties and supersedes all prior agreements, written or oral
- **Amendments:** Any amendment to this contract must be in writing and signed
  by both parties

---

## Cost Summary for Employer / Sikum Aluyot LeMa'asik / סיכום עלויות למעסיק

| Component | Monthly Amount |
|-----------|----------------|
| Gross salary | {format_currency(adj_salary)} |
| Pension (employer) | {format_currency(benefits['pension_employer'])} |
| Severance (Saif 14) | {format_currency(benefits['severance_component'])} |
| Keren Hishtalmut (employer) | {format_currency(benefits['hishtalmut_employer'])} |
| **Total employer cost** | **{format_currency(benefits['total_employer_cost'])}** |

*Note: Does not include Bituach Leumi (employer portion), Dmei Havra'a,
travel allowance, or other variable costs.*

---

## Signatures / Chatimot / חתימות

**Employer / Ma'asik / מעסיק:**

Name: {employer_name}
Title: ____________________
Signature: ____________________
Date: ____________________

**Employee / Oved / עובד:**

Name: {employee_name}
Signature: ____________________
Date: ____________________

---

*This contract template is generated for informational purposes. It should be
reviewed by a qualified Israeli labor law attorney before execution.*

*תבנית חוזה זו נוצרה למטרות מידע בלבד. יש לבדוק אותה על ידי עורך דין
המתמחה בדיני עבודה ישראליים לפני חתימה.*
"""
    return contract


def main():
    parser = argparse.ArgumentParser(
        description="Generate Israeli employment contract templates with calculated benefit rates.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Examples:
  %(prog)s --employee-name "Israel Israeli" --position "Software Engineer" --salary 25000 --start-date 2026-04-01
  %(prog)s --employee-name "Dana Cohen" --position "Designer" --salary 15000 --start-date 2026-05-01 --work-percent 60
  %(prog)s --employee-name "Test User" --position "QA Lead" --salary 20000 --start-date 2026-04-01 --output contract.md

Current rates (2025-2026):
  Pension (employer):      6.5%%
  Pension (employee):      6.0%%
  Severance (Saif 14):     8.33%%
  Keren Hishtalmut (emp):  7.5%%
  Keren Hishtalmut (ee):   2.5%%
  Dmei Havra'a daily rate: {HAVRA_A_DAILY_RATE:.2f} NIS
  Minimum wage (monthly):  {MINIMUM_WAGE_MONTHLY:.2f} NIS
"""
    )

    parser.add_argument(
        "--employee-name",
        required=True,
        help="Full name of the employee",
    )
    parser.add_argument(
        "--position",
        required=True,
        help="Job title / position",
    )
    parser.add_argument(
        "--salary",
        type=float,
        required=True,
        help="Gross monthly salary in NIS (for 100%% position)",
    )
    parser.add_argument(
        "--start-date",
        required=True,
        help="Employment start date (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--work-percent",
        type=float,
        default=100.0,
        help="Position scope as percentage (default: 100)",
    )
    parser.add_argument(
        "--employer-name",
        default="[EMPLOYER NAME]",
        help="Employer / company name",
    )
    parser.add_argument(
        "--employer-id",
        default="[EMPLOYER ID]",
        help="Employer company ID (Chet-Peh number)",
    )
    parser.add_argument(
        "--employee-id",
        default="[EMPLOYEE ID]",
        help="Employee ID number (Teudat Zehut)",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Output file path (default: print to stdout)",
    )

    args = parser.parse_args()

    # Validate salary against minimum wage
    adjusted_min = MINIMUM_WAGE_MONTHLY * (args.work_percent / 100.0)
    if args.salary * (args.work_percent / 100.0) < adjusted_min:
        print(
            f"WARNING: Adjusted salary ({args.salary * args.work_percent / 100.0:.2f} NIS) "
            f"is below minimum wage for {args.work_percent:.0f}% position "
            f"({adjusted_min:.2f} NIS).",
            file=sys.stderr,
        )

    # Validate date format
    try:
        datetime.strptime(args.start_date, "%Y-%m-%d")
    except ValueError:
        print(
            f"ERROR: Invalid date format '{args.start_date}'. Use YYYY-MM-DD.",
            file=sys.stderr,
        )
        sys.exit(1)

    contract = generate_contract(
        employee_name=args.employee_name,
        position=args.position,
        salary=args.salary,
        start_date=args.start_date,
        work_percent=args.work_percent,
        employer_name=args.employer_name,
        employer_id=args.employer_id,
        employee_id=args.employee_id,
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(contract)
        print(f"Contract written to {args.output}", file=sys.stderr)
    else:
        print(contract)


if __name__ == "__main__":
    main()
