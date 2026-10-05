#!/usr/bin/env python3
"""Work out which Israeli amuta duties a turnover triggers, plus the fee tier and report year.

Pure computation. No network access, so it runs on every host including sandboxed ones.

Every threshold carries a year. The audit threshold is index-linked under s.19(c)(2), but no amount
was gazetted for 2015 to 2025, and the statute does not settle which year's amount a year's turnover
is measured against. For the report years in AUDIT_ZONES the script reports a zone: required on
every reading, required on no reading, or unsettled; for other years it asks for the figure. Pass --audit-threshold only if an accountant or the Registrar has told you
the operative figure.

Usage:
  python3 band_check.py --turnover <amount> --certificate-year 2026
  python3 band_check.py --turnover <amount> --certificate-year 2027 --section-46
  python3 band_check.py --example
"""

import argparse

# s.19(c)(1) base, adjusted to 1996. Index-linked by s.19(c)(2). Only GAZETTED amounts go here.
# Nothing was gazetted for 2015 to 2025; the 2026 notice says it accounts for the 2014-2025 updates.
GAZETTED_AUDIT_AMOUNTS = {
    2014: 1_172_933,  # 1,172,933.01 per Wikisource's annotated text (Y.P. 5774 p.3498), last notice before 2026
    2026: 1_380_630,  # Yalkut HaPirsumim 14348 p.4638, notice dated 12.2.2026, published 11.3.2026
}

# Audit zone per REPORT year: (floor, ceiling). Below the floor no reading requires an audit; above
# the ceiling every reading does. Entered only for years whose bounds were checked, NOT derived from
# a "the amount only rises" premise, because the CPI fell in some years (2014-2016, 2020).
# 2024 and 2025: candidates are the last gazetted 2014 amount, the CPI-linked amount for the year,
# and the 2026 amount; the CPI in 2024 and 2025 sat well above its 2014 level and below its 2026
# level, so all candidates lie between 1,172,933 and 1,380,630.
# 2026: own-year amount 1,380,630; the following-year (2027) amount is not gazetted yet (None).
AUDIT_ZONES = {
    2024: (1_172_933, 1_380_630),
    2025: (1_172_933, 1_380_630),
    2026: (1_380_630, None),
}
FILING_EXEMPTION_THRESHOLD = 500_000  # Forms Regulations reg. 7(e)(2): financial report not FILED
BOOKKEEPING_THRESHOLD = 750_000      # Second Schedule. NOT index-linked.
INTERNAL_AUDIT_THRESHOLD = 10_000_000  # s.30a
FOREIGN_DONATION_THRESHOLD = 300_000   # s.36a
FEE_TURNOVER_THRESHOLD = 300_000

FEES_YEAR = 2026
FEES_2026 = {"reduced": 176, "early": 1338, "standard": 1777}


def report_year(certificate_year):
    """A certificate for year X is granted against the annual reports for year X-2."""
    return certificate_year - 2


def filing_deadline(certificate_year):
    """s.36(d): filed no later than 30 June of the year following the report period."""
    return "30 June %d" % (report_year(certificate_year) + 1)


def audit_zone(report_yr, turnover, override=None):
    """Classify the audit duty for the turnover of `report_yr`.

    Two readings of s.19(c) are live: the turnover is measured against the amount for its own year,
    or against the amount for the following year, in which it is tested ("machzor" is the receipts
    of the last year that passed). AUDIT_ZONES holds the checked bounds per report year.

    Returns (verdict, text). verdict is "required", "not_required", "unsettled" or "unknown".
    """
    if override is not None:
        if turnover > override:
            return "required", "above the %s NIS supplied on the command line" % fmt(override)
        return "not_required", "at or below the %s NIS supplied on the command line" % fmt(override)
    if report_yr not in AUDIT_ZONES:
        return "unknown", ("no checked audit bounds for the %d reports. Find the operative s.19(c) "
                           "amount with the accountant or the Registrar and pass it with "
                           "--audit-threshold. Gazetted amounts on record: %s"
                           % (report_yr, ", ".join("%d = %s NIS" % (y, fmt(v)) for y, v
                                                   in sorted(GAZETTED_AUDIT_AMOUNTS.items()))))
    low, high = AUDIT_ZONES[report_yr]
    if turnover <= low:
        if high is None:
            return "not_required", ("at or below %s NIS, the %d amount. If the %d notice turns out "
                                    "to govern, recheck against it" % (fmt(low), report_yr,
                                                                       report_yr + 1))
        return "not_required", "at or below %s NIS, the lowest amount any reading applies" % fmt(low)
    if high is not None and turnover > high:
        return "required", "above %s NIS, the highest amount any reading applies" % fmt(high)
    if high is None:
        return "required_pending", ("above %s NIS, the %d amount. Required on that amount; only if "
                                    "the %d amount turns out to govern AND exceeds this turnover "
                                    "would it not be. The %d notice is due in February %d"
                                    % (fmt(low), report_yr, report_yr + 1, report_yr + 1,
                                       report_yr + 1))
    return "unsettled", ("between %s NIS and %s NIS. Which amount applies is not settled. The "
                         "conservative course is to appoint an accountant; confirm with the "
                         "amuta's accountant or the Registrar" % (fmt(low), fmt(high)))


def fmt(n):
    """Thousands separators; keep agorot when the amount is not whole, so 750,000.50 never prints
    as 750,000 beside an 'above 750,000' verdict."""
    return format(int(n), ",") if float(n).is_integer() else format(n, ",.2f")


def evaluate(turnover, certificate_year, section_46=False, audit_override=None,
             first_two_years=False, filed_online_small=False, prior_turnover=None):
    out = []
    ry = report_year(certificate_year)
    out.append("Certificate year:      %d" % certificate_year)
    out.append("Annual reports needed: %d  (the X minus 2 rule)" % ry)
    out.append("Statutory deadline:    %s for the verbal report and, unless exempt, the financial "
               "report signed by two board members (s.36(d))" % filing_deadline(certificate_year))
    if first_two_years:
        out.append("  NOTE: a newly registered amuta's first certificate may not follow the X minus 2 "
                   "rule. Confirm with the Registrar which reports it needs.")
    out.append("")
    out.append("Turnover used: %s NIS" % fmt(turnover))
    out.append("")
    out.append("Duties triggered")
    out.append("  Organs: general assembly, board, audit committee (s.19(a)). Applies at any "
               "turnover, including none.")
    out.append("  Balance sheet and income/expenditure statement (s.36(a)). Applies to every amuta; "
               "only the AUDIT is banded.")

    if turnover <= FILING_EXEMPTION_THRESHOLD:
        out.append("  Financial report: still PREPARED (s.36(a)) but not FILED with the Registrar "
                   "(Forms Regulations reg. 7(e)(2), at or below %s NIS). The verbal report is "
                   "still filed." % fmt(FILING_EXEMPTION_THRESHOLD))

    # "Machzor" is the receipts of the last year that passed, so the books kept DURING a year follow
    # the PREVIOUS year's turnover. --turnover (the report year) decides the following year's books.
    if prior_turnover is not None:
        out.append("  Books kept during %d: %s (%d turnover %s NIS; Second Schedule, 750,000 NIS)."
                   % (ry, "double-entry required" if prior_turnover > BOOKKEEPING_THRESHOLD
                      else "receipts-and-payments book is enough", ry - 1, fmt(prior_turnover)))
    else:
        out.append("  Books kept during %d: decided by the %d turnover, not supplied (pass "
                   "--prior-turnover). Above 750,000 NIS: double-entry; otherwise a "
                   "receipts-and-payments book is enough (Second Schedule)." % (ry, ry - 1))
    out.append("  Books for %d, on the %d turnover given: %s."
               % (ry + 1, ry, "double-entry required" if turnover > BOOKKEEPING_THRESHOLD
                  else "receipts-and-payments book is enough"))

    verdict, note = audit_zone(ry, turnover, audit_override)
    if verdict == "required":
        out.append("  Accountant must be appointed and the report audited to the general assembly "
                   "(s.19(c)(1), s.37(a)): turnover %s." % note)
    elif verdict == "not_required":
        out.append("  No mandatory accountant on turnover: %s. Note s.37(b): the Registrar may "
                   "still order an audit." % note)
    elif verdict == "required_pending":
        out.append("  Accountant required (s.19(c)(1), s.37(a)): turnover %s." % note)
    elif verdict == "unsettled":
        out.append("  Audit: UNSETTLED. Turnover is %s." % note)
    else:
        out.append("  Audit: CANNOT DETERMINE, %s." % note)

    if turnover > INTERNAL_AUDIT_THRESHOLD:
        out.append("  Internal auditor required, with the audit committee's agreement (s.30a, above "
                   "%s NIS)." % format(INTERNAL_AUDIT_THRESHOLD, ","))

    if turnover > FOREIGN_DONATION_THRESHOLD:
        out.append("  Annual foreign political-entity statement (s.36a, turnover above %s NIS): state "
                   "whether donations from such entities exceeded 20,000 NIS cumulatively, and if so "
                   "give the details (Form 7a Annex 2)." % format(FOREIGN_DONATION_THRESHOLD, ","))
    out.append("  Quarterly foreign political-entity report (Disclosure Duty Law s.2): due within a week "
               "of the end of any quarter in which such a donation was received, at ANY turnover and "
               "ANY amount.")

    fee_year = certificate_year - 1
    out.append("")
    out.append("Annual fee: the certificate application requires the fee for %d (the year before the "
               "certificate year) to be paid, including arrears from earlier years." % fee_year)
    if fee_year == FEES_YEAR:
        out.append("  %d amounts (Associations (Fees) Regulations):" % FEES_YEAR)
    else:
        out.append("  CANNOT DETERMINE the %d amounts. Those below are the %d ones, shown only for "
                   "shape. The fee is index-linked and updated once a year, so look up the %d "
                   "amounts before quoting any of them." % (fee_year, FEES_YEAR, fee_year))
    # The tier is NOT decided by --turnover: item 2(d) reads the verbal report for the last year whose
    # report fell due before the fee year (fee_year - 2), while --turnover is the report year
    # (fee_year - 1). Quoting a tier from --turnover would test the wrong year.
    if first_two_years or filed_online_small:
        reason = ("first two years after the year of incorporation" if first_two_years
                  else "the %d verbal report showed turnover at or below %s NIS"
                       % (fee_year - 2, format(FEE_TURNOVER_THRESHOLD, ",")))
        out.append("  Reduced tier: %d NIS%s  (%s)" % (FEES_2026["reduced"], "" if fee_year == FEES_YEAR
                   else " (the %d amount)" % FEES_YEAR, reason))
    else:
        out.append("  %s NIS if paid up to 31.03, then %s NIS from 01.04, UNLESS the %d verbal report "
                   "showed turnover at or below %s NIS (then 176 NIS; pass --filed-online-small) or "
                   "the amuta is in its first two years after incorporation (pass --first-two-years)."
                   % (fmt(FEES_2026["early"]), fmt(FEES_2026["standard"]), fee_year - 2,
                      format(FEE_TURNOVER_THRESHOLD, ",")))
        out.append("  Paying the full fee BEFORE filing the online reports forfeits any refund of "
                   "the excess.")
    out.append("  Reduced-tier test (fee schedule item 2(d)): turnover in the verbal report for the "
               "last year whose report fell due before the fee year, i.e. the %d report for the %d "
               "fee. A fee paid after its year ends is charged at the post-March rate of the year "
               "actually paid (item 2(c))." % (fee_year - 2, fee_year))

    if section_46:
        out.append("")
        out.append("Section 46 digital donation reporting")
        out.append("  Mandatory since 1 January 2026 via the Trumot Israel system, for donations AND "
                   "cancellations, from the first shekel, with no minimum.")
        out.append("  The Section 46 approval is CONDITIONAL on complying (execution instruction "
                   "11/2025, s.10).")
        out.append("  Prerequisites: registration for Tax Authority digital services, and a "
                   "morshe-al appointed.")
        out.append("  The duty applies even if the amuta is exempt from issuing receipts.")
        out.append("  There is no April 2026 deadline. The date is 1 January 2026.")
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--turnover", type=float, help="annual turnover in NIS for the reported year")
    p.add_argument("--certificate-year", type=int, help="the year the certificate is sought for")
    p.add_argument("--audit-threshold", type=float, default=None,
                   help="operative s.19(c) amount, only if an accountant or the Registrar has confirmed it")
    p.add_argument("--prior-turnover", type=float, default=None,
                   help="turnover of the year BEFORE the report year, which decides that year's books")
    p.add_argument("--section-46", action="store_true", help="the amuta holds a Section 46 approval")
    p.add_argument("--first-two-years", action="store_true",
                   help="in the FEE year (certificate year minus 1), the amuta is within its first two "
                        "years after the year of incorporation")
    p.add_argument("--filed-online-small", action="store_true",
                   help="the verbal report for the year two before the fee year (e.g. 2024 for the 2026 fee) "
                        "showed turnover at or below 300,000 NIS")
    p.add_argument("--example", action="store_true", help="run a worked example")
    a = p.parse_args()

    if a.example:
        demo = BOOKKEEPING_THRESHOLD + 150_000
        print("Example: turnover between the bookkeeping and audit thresholds, "
              "certificate for 2027, holds Section 46\n")
        for line in evaluate(demo, 2027, section_46=True):
            print(line)
        return
    if a.turnover is None or a.certificate_year is None:
        p.error("--turnover and --certificate-year are required (or use --example)")
    if a.turnover < 0 or (a.prior_turnover is not None and a.prior_turnover < 0):
        p.error("turnover cannot be negative")
    if a.audit_threshold is not None and a.audit_threshold <= 0:
        p.error("--audit-threshold must be positive")
    if a.certificate_year < 2000 or a.certificate_year > 2100:
        p.error("--certificate-year looks wrong: %d" % a.certificate_year)
    for line in evaluate(a.turnover, a.certificate_year, a.section_46, a.audit_threshold,
                         a.first_two_years, a.filed_online_small, a.prior_turnover):
        print(line)


if __name__ == "__main__":
    main()
