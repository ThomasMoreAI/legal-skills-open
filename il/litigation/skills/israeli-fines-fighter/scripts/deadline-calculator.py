#!/usr/bin/env python3
"""
Israeli Fine Appeal Deadline Calculator

Calculates remaining days in the appeal window based on fine receipt date.
Supports both parking fines (30-day window) and traffic fines (90-day window).

Usage:
    python deadline-calculator.py --date 2026-03-15 --type parking
    python deadline-calculator.py --date 2026-03-15 --type traffic
    python deadline-calculator.py --help
"""

import argparse
from datetime import datetime, timedelta
import sys

# Cancellation window: 30 days, applies to BOTH parking and traffic fines.
# Court-hearing window: 90 days from receipt, also for both.
#
# SURCHARGE: this script deliberately reports only the DATE from which a
# late-payment addition can start accruing, never a percentage, because the
# rate depends on which track the fine is on and that is not knowable from a
# date alone. On the administrative track (Administrative Traffic Violations
# Law) it is 30% of the unpaid fine under s.10(b)(1), plus interest. On the
# criminal track the schedule differs. Which track applies is decided by the
# OFFENCE date, not by today's date. Direct the user to the Fines Collection
# Center or the payment notice for the actual balance. Collection enforcement
# is separate and typically begins only around month 12 via Hotza'a Lapoal.
PARKING_CANCEL_DAYS = 30
TRAFFIC_CANCEL_DAYS = 30
COURT_HEARING_DAYS = 90
SURCHARGE_STARTS_DAYS = 90  # a late-payment addition can accrue from this day onward

# NOTE on parking model limitation: parking fines technically share the same
# 30/90-day windows as traffic fines, but municipal practice varies. Some
# municipalities apply their own internal "reconsideration" timelines on top
# of the statutory 30-day cancellation window, and surcharge schedules can
# differ slightly per municipality. Treat this calculator's parking output as
# a baseline; verify with the specific municipality for edge cases.


def calculate_deadline(receipt_date: str, fine_type: str) -> dict:
    """Calculate appeal and surcharge milestones for an Israeli fine."""
    try:
        date = datetime.strptime(receipt_date, "%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date format '{receipt_date}'. Use YYYY-MM-DD.")
        sys.exit(1)

    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    cancel_window = PARKING_CANCEL_DAYS if fine_type == "parking" else TRAFFIC_CANCEL_DAYS
    # All three tracks share 30/90; the labels and the available remedies differ.
    appeal_deadline = date + timedelta(days=cancel_window)
    court_deadline = date + timedelta(days=COURT_HEARING_DAYS)
    surcharge_deadline = date + timedelta(days=SURCHARGE_STARTS_DAYS)

    days_to_appeal = (appeal_deadline - today).days
    days_to_court = (court_deadline - today).days
    days_to_surcharge = (surcharge_deadline - today).days

    return {
        "receipt_date": date.strftime("%Y-%m-%d"),
        "fine_type": fine_type,
        "appeal_deadline": appeal_deadline.strftime("%Y-%m-%d"),
        "days_remaining_appeal": max(days_to_appeal, 0),
        "can_appeal": days_to_appeal > 0,
        # Kept for backwards compatibility with earlier CLI consumers.
        "late_payment_deadline": court_deadline.strftime("%Y-%m-%d"),
        "days_remaining_late": max(days_to_court, 0),
        "court_hearing_deadline": court_deadline.strftime("%Y-%m-%d"),
        "days_remaining_court": max(days_to_court, 0),
        "surcharge_deadline": surcharge_deadline.strftime("%Y-%m-%d"),
        "days_until_surcharge": max(days_to_surcharge, 0),
        "surcharge_started": days_to_surcharge <= 0,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Calculate Israeli fine appeal deadlines"
    )
    parser.add_argument(
        "--date",
        required=True,
        help="Date fine was received (YYYY-MM-DD)",
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=["parking", "traffic", "administrative"],
        help=(
            "parking (municipal) or traffic (police/camera) = criminal track: 30-day "
            "bakasha le-bitul, 90-day bakasha le-hishafet. administrative = Administrative "
            "Traffic Violations Law track: 30-day hasagah (90 if you were not the driver), "
            "90-day arar to the traffic tribunal, and NO request to be tried. Which track "
            "applies is decided by the OFFENCE date, not today's date."
        ),
    )

    args = parser.parse_args()
    result = calculate_deadline(args.date, args.type)

    fine_label = {
        "parking": "Parking fine",
        "traffic": "Traffic fine",
        "administrative": "Administrative traffic violation",
    }[result["fine_type"]]
    admin = result["fine_type"] == "administrative"

    print(f"\n{'='*50}")
    print(f"  {fine_label} Appeal Deadline Calculator")
    print(f"{'='*50}")
    print(f"  Receipt date:           {result['receipt_date']}")
    if admin:
        print(f"  Hasagah window:         30 days (90 if you were not the driver, s.8(a))")
        print(f"  Hasagah deadline:       {result['appeal_deadline']}")
        print(f"  Arar deadline:          {result['court_hearing_deadline']} (to the traffic tribunal, 90 days, s.19(b))")
        print(f"                          or 30 days from the decision on the hasagah")
        print(f"  Note:                   there is NO bakasha le-hishafet on this track")
    else:
        print(f"  Cancellation window:    30 days (bakasha le-bitul)")
        print(f"  Cancellation deadline:  {result['appeal_deadline']}")
        print(f"  Court-hearing deadline: {result['court_hearing_deadline']} (bakasha le-hishafet, 90 days)")
    print(f"  Late-payment addition:  can start {result['surcharge_deadline']} (rate depends on track)")

    if result["can_appeal"]:
        label = "HASAGAH" if admin else "CANCELLATION"
        print(f"  Status:                 WITHIN 30-DAY {label} WINDOW")
        print(f"  Days remaining:         {result['days_remaining_appeal']} days")
    elif not result["surcharge_started"]:
        first = "HASAGAH" if admin else "CANCELLATION"
        second = "arar" if admin else "court request"
        print(f"  Status:                 {first} WINDOW EXPIRED, {second} window still open")
        print(f"  Days to {second:<15}{result['days_remaining_court']} days")
    else:
        print(f"  Status:                 LATE-PAYMENT ADDITION MAY HAVE STARTED")
        print(f"  Action:                 Check the real balance with the Fines Collection Center,")
        print(f"                          or document a justified-delay exception.")

    print(f"{'='*50}\n")


if __name__ == "__main__":
    main()
