#!/usr/bin/env python3
"""Report the STATUTORY majority threshold for an Israeli urban renewal track.

This prints published thresholds and, optionally, plain arithmetic against a signature
count the user supplies. It does NOT decide whether any owner's refusal is reasonable,
does NOT determine that anyone is a "dayar sarvan", and does NOT value anything. Those
questions are for the court (pinui-binui) or the mefake'ach (strengthening track), on
evidence, and for the owner's own advocate.

Pure local logic. No network, no third-party packages.

Sources:
  pinui-binui   Chok pinui u-vinui (idud mizmei pinui u-vinui), 2006, s.1
                https://www.nevo.co.il/law_html/law00/73988.htm
  strengthening Chok ha-mekarkein (chizuk batim meshutafim mipnei re'idot adama), 2008,
                s.5, s.5a   https://www.nevo.co.il/law_html/law01/999_901.htm

Usage:
  python3 majority_threshold.py --track pinui-binui --apartments 24
  python3 majority_threshold.py --track chizuk --work demolition --apartments 8
  python3 majority_threshold.py --track chizuk --work new-apartment --apartments 6 --signed 4
  python3 majority_threshold.py --example
"""

import argparse
import math
import sys

DISCLAIMER = (
    "This is a general statement of published thresholds, not legal advice, and not a "
    "finding about any person. Reaching a threshold does not by itself bind a dissenting "
    "owner: it is what lets the consenting owners bring the matter to the court "
    "(pinui-binui) or the mefake'ach (strengthening track), which then decides. Check the "
    "statute and consult your own advocate."
)

TIKKUN_8_DATE = "1.7.2023"


def ceil_fraction(total, numerator, denominator):
    """Smallest whole number of apartments that is at least the given fraction of total."""
    return math.ceil(total * numerator / denominator)


def pinui_binui(apartments_in_building, apartments_in_complex=None):
    lines = []
    lines.append("Track: pinui-binui. Statute: Chok pinui u-vinui (idud mizmei pinui")
    lines.append("u-vinui), 2006, s.1, definition of 'rov meyuchas mibein baalei ha-dirot'.")
    lines.append("")
    lines.append("The special majority is a COMPOSITE. All three limbs must hold at once:")
    lines.append("")
    if apartments_in_complex:
        need = ceil_fraction(apartments_in_complex, 2, 3)
        lines.append(
            "  1. At least two thirds of all apartments in the makbetz: "
            "%d of %d apartments." % (need, apartments_in_complex)
        )
    else:
        lines.append("  1. At least two thirds of all apartments in the makbetz (complex).")
        lines.append("     Pass --complex-apartments to compute this limb.")

    n = apartments_in_building
    if n in (4, 5):
        lines.append(
            "  2. This building has %d apartments, so the special rule applies: at least "
            "THREE apartments," % n
        )
        lines.append(
            "     and the building must have more than two owners. (The three-fifths rule "
            "does not apply at this size.)"
        )
        limb2 = 3
    else:
        limb2 = ceil_fraction(n, 3, 5)
        lines.append(
            "  2. At least three fifths of the apartments in THIS beit meshutaf: "
            "%d of %d apartments." % (limb2, n)
        )
    lines.append("  3. More than half of the common property in this beit meshutaf attached")
    lines.append("     to their apartments. This is a property share, not an apartment count,")
    lines.append("     and is read off the beit meshutaf register, not inferred from limb 2.")
    return lines, limb2


def chizuk(work, apartments):
    lines = []
    lines.append("Track: strengthening. Statute: Chok ha-mekarkein (chizuk batim meshutafim")
    lines.append("mipnei re'idot adama), 2008. Forum: the mefake'ach al ha-batim ha-meshutafim.")
    lines.append("")
    if work == "new-apartment":
        need = ceil_fraction(apartments, 2, 3)
        lines.append("Work: building one or more new apartments in the common property (s.5(a)).")
        lines.append("")
        lines.append(
            "  Threshold: two thirds of the apartments, that is %d of %d, PLUS two thirds "
            "of the" % (need, apartments)
        )
        lines.append("  common property attached to their apartments.")
        lines.append("  The mefake'ach must give every owner an opportunity to argue their case.")
        return lines, need

    # demolition
    lines.append("Work: demolition of the existing building and rebuilding it (s.5a).")
    lines.append("")
    if apartments < 4:
        lines.append("  This building has %d apartments." % apartments)
        lines.append("  The s.5a(a) route requires a building of at least four apartments and")
        lines.append("  more than two owners, so that route is not available at this size.")
        return lines, None
    need = ceil_fraction(apartments, 2, 3)
    lines.append(
        "  Threshold: two thirds of the apartments, that is %d of %d, PLUS two thirds of the"
        % (need, apartments)
    )
    lines.append("  common property, in a building of at least four apartments with more than")
    lines.append("  two owners.")
    lines.append("")
    lines.append("  TEMPORAL NOTE: before tikkun 8, in force %s, this threshold was" % TIKKUN_8_DATE)
    lines.append(
        "  FOUR FIFTHS (%d of %d) plus four fifths of the common property. The older figure"
        % (ceil_fraction(apartments, 4, 5), apartments)
    )
    lines.append("  still governs matters measured under the old regime, and it is the source")
    lines.append("  of the '80 percent' figure still published as though it were current.")
    if apartments >= 6:
        lines.append("")
        lines.append("  SIX OR MORE APARTMENTS: s.5a(a1) applies s.4 of the pinui-binui law to the")
        lines.append("  COMPUTATION of this majority. That does NOT change the two-thirds threshold.")
        lines.append("  s.4 is a discount rule: an owner holding more than 30 percent of the")
        lines.append("  apartments is counted as holding 30 percent plus one third of the excess.")
        lines.append("  Pass --largest-owner-apartments to see that arithmetic.")
    return lines, need


def section4_discount(apartments, owned):
    """s.4 of the pinui-binui law: in a beit meshutaf of six apartments or more, an
    owner of more than 30 percent of the apartments counts as 30 percent plus one
    third of the excess over 30 percent. Returns (raw_pct, counted_pct) or None
    when the rule does not bite."""
    if apartments < 6:
        return None
    raw = owned / apartments * 100.0
    if raw <= 30.0:
        return (raw, raw)
    excess = raw - 30.0
    return (raw, 30.0 + excess / 3.0)


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Report statutory majority thresholds for Israeli urban renewal tracks."
    )
    p.add_argument("--track", choices=["pinui-binui", "chizuk"])
    p.add_argument(
        "--work",
        choices=["new-apartment", "demolition"],
        help="Strengthening track only: which work type.",
    )
    p.add_argument("--apartments", type=int, help="Apartments in this beit meshutaf.")
    p.add_argument(
        "--complex-apartments",
        type=int,
        help="Pinui-binui only: total apartments across the makbetz.",
    )
    p.add_argument("--signed", type=int, help="How many apartments have signed, for arithmetic only.")
    p.add_argument(
        "--largest-owner-apartments",
        type=int,
        help="How many apartments the single largest owner holds. Shows the s.4 discount "
             "in a beit meshutaf of six apartments or more.",
    )
    p.add_argument("--example", action="store_true", help="Run a worked example and exit.")
    args = p.parse_args(argv)

    if args.example:
        return main(["--track", "chizuk", "--work", "demolition", "--apartments", "8"])

    if not args.track or not args.apartments:
        p.error("--track and --apartments are required (or use --example)")
    if args.apartments < 1:
        p.error("--apartments must be at least 1")
    if args.track == "chizuk" and not args.work:
        p.error("--work is required for the strengthening track")

    if args.track == "pinui-binui":
        lines, threshold = pinui_binui(args.apartments, args.complex_apartments)
    else:
        lines, threshold = chizuk(args.work, args.apartments)

    print("\n".join(lines))

    if args.largest_owner_apartments is not None:
        d = section4_discount(args.apartments, args.largest_owner_apartments)
        print("")
        if d is None:
            print("  s.4 discount does not apply: it bites only at six apartments or more.")
        else:
            raw, counted = d
            if abs(raw - counted) < 1e-9:
                print("  Largest owner holds %d of %d (%.2f percent), at or under 30 percent," %
                      (args.largest_owner_apartments, args.apartments, raw))
                print("  so the s.4 discount does not reduce their weight.")
            else:
                print("  s.4 discount (six or more apartments): the largest owner holds %d of %d," %
                      (args.largest_owner_apartments, args.apartments))
                print("  a raw %.2f percent, but is COUNTED at %.2f percent" % (raw, counted))
                print("  (30 percent, plus one third of the %.2f percent excess)." % (raw - 30.0))

    if args.signed is not None:
        print("")
        if args.signed > args.apartments:
            print(
                "  You gave --signed %d for a building of %d apartments. Check the numbers."
                % (args.signed, args.apartments)
            )
        elif threshold is None:
            print(
                "  Arithmetic is not shown here because the threshold for this case routes to"
            )
            print("  another statute. See the note above.")
        else:
            gap = threshold - args.signed
            print("  Signed: %d. Limb threshold shown above: %d." % (args.signed, threshold))
            if gap > 0:
                print("  That limb is %d apartment(s) short." % gap)
            else:
                print("  That limb is met on the apartment count.")
            print("  Other limbs, including every common-property limb, are NOT checked here.")

    print("")
    print("NOTE: " + DISCLAIMER)
    return 0


if __name__ == "__main__":
    sys.exit(main())
