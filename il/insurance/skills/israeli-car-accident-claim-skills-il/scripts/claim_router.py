#!/usr/bin/env python3
"""Route an Israeli car-accident claim to the right insurance / fund and surface time limits.

This does NOT compute compensation amounts (the non-pecuniary head is a share of a
CPI-linked statutory maximum, and lasting disability is assessed by a court-appointed
medical expert). It tells the user which regime applies, where to claim, and which
deadlines matter, based on Israel's PLATD Law 1975, the Insurance Contract Law, the
Limitation Law, and the Traffic Regulations.

Usage:
  python3 claim_router.py --damage none --injuries --my-fault no
  python3 claim_router.py --damage property --my-fault yes --other-insured yes
  python3 claim_router.py --damage property --hit-and-run --injuries --my-insured no --role pedestrian
  python3 claim_router.py --injuries --my-insured no --role passenger --other-insured yes
  python3 claim_router.py --example
"""

import argparse
import json
import sys

# TWO regimes, deliberately separate constants. Merging them into one number is the
# error that time-bars a user's own comprehensive claim at year four.
# Insurance Contract Law Section 31: a claim for insurance benefits against your own
# insurer prescribes three years after the insured event.
INSURANCE_BENEFITS_LIMITATION_YEARS = 3
# Limitation Law Section 5: the tort claim against the at-fault driver and the PLATD
# bodily-injury claim prescribe in seven years.
TORT_AND_PLATD_LIMITATION_YEARS = 7
# Limitation Law Section 10 suspends the clock while the claimant is a minor, so the
# seven-year tort figure is available until roughly this age. Derived, not statutory.
MAJORITY_AGE = 18
MINOR_CLAIM_UNTIL_AGE = MAJORITY_AGE + TORT_AND_PLATD_LIMITATION_YEARS
# PLATD Section 5(b): urgent payment due within 60 days of a written demand.
URGENT_PAYMENT_DAYS = 60
# PLATD Section 5e(b): no urgent payment for a period beyond two years from the accident.
URGENT_PAYMENT_MAX_YEARS = 2


def route(injuries, hit_and_run, damage, my_fault, other_insured, my_comprehensive,
          my_compulsory=True, role=None):
    out = {"notice": ("General routing under PLATD, not legal advice and not a determination "
                      "of your entitlement. Confirm with a lawyer before relying on it."),
           "bodily_injury": None, "property_damage": None, "police": None,
           "time_limits": [], "notes": []}

    # Bodily injury: no-fault (PLATD). Claim from your OWN compulsory insurer regardless
    # of fault. Karnit is available ONLY where the victim has no insurer of their own,
    # which is the express condition in PLATD Section 12(a).
    if injuries:
        untraced_or_uninsured = hit_and_run or other_insured is False
        base = ("Bodily injury is no-fault under PLATD: liability is absolute and there is no "
                "contributory-negligence reduction (Section 2(c)). ")
        if role == "pedestrian":
            if untraced_or_uninsured:
                out["bodily_injury"] = base + (
                    "As a pedestrian or cyclist hit by an untraced or uninsured vehicle you "
                    "have no insurer to claim from, so Karnit (קרנית) is the address "
                    "(Section 12(a)(1)-(2)). Karnit also pays the hospital its treatment costs."
                )
            else:
                out["bodily_injury"] = base + (
                    "As a pedestrian or cyclist, claim from the compulsory insurer of the "
                    "vehicle that hit you (Section 2(a)); if several vehicles were involved, "
                    "all their drivers are liable jointly and severally (Section 3(b)). "
                    "Karnit is not the address while that insurer exists."
                )
            if untraced_or_uninsured:
                out["bodily_injury"] += (
                    " If ANOTHER vehicle involved in the same accident was traced and insured, "
                    "you can claim from its insurer instead (Section 3(b) makes all involved "
                    "drivers liable jointly and severally), and Karnit is then closed to you."
                )
        elif my_compulsory is not False:
            out["bodily_injury"] = base + (
                "You were in an insured vehicle, so you (driver or passenger) claim from THAT "
                "vehicle's compulsory insurance (ביטוח חובה), regardless of who caused the "
                "accident (Section 3(a); in a single-vehicle accident, Section 2(a))."
            )
            if role is None:
                out["bodily_injury"] += (
                    " This assumes you were INSIDE an insured vehicle. If you were a pedestrian "
                    "or cyclist, re-run with --role pedestrian: a car you own at home does not "
                    "make you insured for this accident."
                )
            if untraced_or_uninsured:
                out["bodily_injury"] += (
                    " The other driver being untraced or uninsured does NOT send you to "
                    "Karnit: you have an insurer to claim from, and Section 12(a) opens Karnit "
                    "only to a victim who has none."
                )
        elif role == "passenger":
            out["bodily_injury"] = base + (
                "You were a passenger in an UNINSURED vehicle. Under Section 3(a) only that "
                "vehicle's driver is liable to its occupants, even if the other vehicle is "
                "insured and traced, and that driver has no insurer, so the claim generally "
                "goes to Karnit (Section 12(a)(2)). Exception: a passenger who knew the vehicle "
                "was being used without permission (for example stolen) is excluded "
                "(Section 7(2))."
            )
        elif role == "driver":
            out["bodily_injury"] = (
                "As the driver of an uninsured vehicle, PLATD Section 7(5) may exclude you from "
                "compensation altogether (an owner who let someone else drive uninsured and was "
                "hurt on that drive is excluded too, Section 7(6)). Exceptions exist: Section 7A "
                "lets a driver who drove with the owner's permission and neither knew nor could "
                "reasonably have known there was no insurance claim from Karnit, and under "
                "Section 7B dependants may claim from Karnit even where the victim could not. "
                "Whether any exception applies to you is a question for a lawyer; this tool "
                "does not decide it."
            )
        else:
            out["bodily_injury"] = base + (
                "You said you have no compulsory insurer of your own. The route depends on "
                "--role: a pedestrian or cyclist claims from the insurer of the vehicle that "
                "hit them (Karnit only if it is untraced or uninsured); an occupant of an "
                "uninsured vehicle goes to Karnit even if the other vehicle is insured "
                "(Sections 3(a), 12(a)(2)). Re-run with --role."
            )
        # Section 8(a) bars tort only for a person the accident GIVES a PLATD cause of
        # action. A Section 7-excluded person has none, and Section 8(c) expressly
        # preserves the tort claim of such a person, so the flat "no tort claim" note
        # must not reach him.
        if my_compulsory is False and role == "driver":
            out["notes"].append(
                "Do not assume the tort route is closed either. Section 8(a) bars a tort "
                "claim only for a person to whom the accident gives a PLATD cause of "
                "action, and Section 8(c) preserves the tort claim of a person who has "
                "none. Whether a Section 7-excluded driver falls inside Section 8(c) is a "
                "case-law question for a lawyer; this tool does not decide it."
            )
        else:
            out["notes"].append(
                "The PLATD claim is exclusive (Section 8): you have no tort claim against the "
                "other driver for bodily injury, except where someone caused the accident "
                "deliberately."
            )
        out["notes"].append(
            "Lasting disability is assessed by a single medical expert appointed by the court "
            "(Section 6a), NOT by a ועדה רפואית. Beware Section 6b: a disability percentage "
            "fixed under any other law (typically a Bituach Leumi work-injury determination) "
            "before the evidence stage binds this claim too. Take legal advice first."
        )
        out["notes"].append(
            "A bodily-injury claim with lasting disability usually needs a lawyer. The fee is "
            "capped by statute (Section 16(a)) at 8% of an agreed sum, or 13% where there were "
            "legal proceedings, and any overpayment is refundable. This skill helps document "
            "and understand rights, it does not replace a lawyer."
        )

    # Property damage: fault-based, and outside PLATD entirely.
    if damage == "property":
        if my_fault == "yes":
            out["property_damage"] = (
                "Property damage is fault-based and sits outside PLATD (Torts Ordinance). As "
                "the at-fault driver, the other party claims against your third-party (צד ג') "
                "cover. Your OWN car's damage is covered only by your comprehensive (מקיף) "
                "policy, not by compulsory insurance."
            )
        elif hit_and_run:
            out["property_damage"] = (
                "The driver who damaged your car is untraced, so there is nobody to claim the "
                "property damage from. Only your own comprehensive (מקיף) covers it; Karnit pays "
                "bodily injury only, never property."
                if my_comprehensive else
                "The driver who damaged your car is untraced and you have no comprehensive "
                "policy, so the property damage is in practice unrecoverable unless the driver "
                "is later identified. Karnit pays bodily injury only, never property."
            )
        elif my_fault == "no":
            if my_comprehensive:
                out["property_damage"] = (
                    "Property damage is fault-based and you are not at fault. Fastest path: claim "
                    "from your own comprehensive (מקיף), pay the deductible (השתתפות עצמית); your "
                    "insurer then recovers from the at-fault party by subrogation (שיבוב) under "
                    "Insurance Contract Law Section 62 and refunds your deductible once paid in "
                    "full. Alternative: claim directly against the at-fault driver's third-party "
                    "cover, or sue them."
                )
            elif other_insured is False:
                out["property_damage"] = (
                    "Property damage is fault-based and you are not at fault. The other driver "
                    "has no compulsory insurance; third-party (צד ג') property cover is a "
                    "separate policy, so ask whether they hold one and claim against it if so. "
                    "Otherwise sue the driver personally (small claims for smaller sums). Karnit "
                    "pays bodily injury only, never property."
                )
            else:
                out["property_damage"] = (
                    "Property damage is fault-based and you are not at fault, but you have no "
                    "comprehensive policy. Claim directly against the at-fault driver's third-party "
                    "(צד ג') cover, or sue the at-fault driver (small claims for smaller sums)."
                )
        else:
            out["property_damage"] = (
                "Property damage is fault-based: whoever caused the damage (or their insurer) pays. "
                "Determine fault first, then claim from the at-fault party's third-party cover or "
                "your own comprehensive."
            )

    # Police involvement.
    if injuries or hit_and_run:
        out["police"] = (
            "Police involvement is MANDATORY: stop, render aid, and report. A police confirmation "
            "(אישור משטרתי) is a precondition for the compensation claim. The gov.il online "
            "light-accident report only applies when there are no injuries (or injured released "
            "within 24 hours). If anyone was hurt, ATTACH the medical documents: the police page "
            "warns that a report filed without them is classified as a damage-only event and not "
            "as a road accident, which can matter against insurers and in civil claims."
        )
    else:
        out["police"] = (
            "Property-only with no injuries: exchange details on the spot. If the vehicle you hit "
            "was parked or its owner absent, leave a written note AND report to the police within "
            "24 hours. You can file the gov.il online light-accident report to obtain the police "
            "confirmation for the claim."
        )

    out["time_limits"] = [
        "Notify your insurer immediately after the accident (Insurance Contract Law Section 22).",
        f"Claim for insurance benefits against YOUR OWN insurer (including a comprehensive "
        f"property claim): {INSURANCE_BENEFITS_LIMITATION_YEARS} years from the accident "
        f"(Insurance Contract Law Section 31). It runs from the insured event, NOT from the "
        f"insurer's rejection, and handing the claim in does not stop the clock.",
        f"Tort claim against the at-fault driver, and the PLATD bodily-injury claim: "
        f"{TORT_AND_PLATD_LIMITATION_YEARS} years (Limitation Law Section 5). A minor's clock is "
        f"suspended below {MAJORITY_AGE}, so on that figure a minor can sue until about age "
        f"{MINOR_CLAIM_UNTIL_AGE}.",
        "Liability insurance (a third-party route) does not prescribe while the third party's "
        "claim against the insured is still alive (Insurance Contract Law Section 70), so it "
        "tracks the longer period.",
        "Your insurer must warn you in writing 12 months and again 3 months before the period "
        "ends (Insurance Contract Law Section 31a). Do not rely on that warning arriving.",
    ]
    if injuries:
        out["time_limits"].insert(1, (
            f"URGENT PAYMENT (תשלום תכוף, PLATD Section 5): the liable party and their insurer "
            f"must pay medical and hospitalization expenses plus monthly living and nursing costs "
            f"within {URGENT_PAYMENT_DAYS} days of a written demand with an affidavit. If the "
            f"{URGENT_PAYMENT_DAYS} days pass, apply to the Magistrates' Court, separately from "
            f"the main claim if you wish (Section 5a). Late payment carries linkage plus 12% "
            f"annual interest (Section 5d). No urgent payment is awarded for a period beyond "
            f"{URGENT_PAYMENT_MAX_YEARS} years from the accident (Section 5e), and a repeat "
            f"application needs 6 months plus changed circumstances. This is the only deadline "
            f"that runs AGAINST the insurer, so raise it early."
        ))
        out["time_limits"].append(
            "If it is also a work accident, claim from Bituach Leumi as well: it does not "
            "subrogate against the motor insurer, the benefit is simply deducted from the award "
            "(National Insurance Law Section 328a(b))."
        )
    out["notes"].append(
        "Dispute with the insurer: complain to the Public Inquiries Unit at the Capital Market, "
        "Insurance and Savings Authority (does not bar court), or file in small claims."
    )
    out["notes"].append(
        "Electric bikes and scooters are not motor vehicles under PLATD per the case law, so an "
        "injured rider has no no-fault claim: the routes are ordinary negligence or דמי תאונה "
        "לנפגעי תאונות אישיות from Bituach Leumi."
    )
    return out


def main():
    p = argparse.ArgumentParser(description="Israeli car-accident claim router")
    p.add_argument("--injuries", action="store_true", help="Anyone injured")
    p.add_argument("--hit-and-run", action="store_true", help="Other driver fled / untraced")
    p.add_argument("--damage", choices=["property", "none", "unknown"], default="unknown",
                   help="Was there property damage. Default 'unknown' so an injury-only "
                        "accident does not silently get a property-damage plan.")
    p.add_argument("--my-fault", choices=["yes", "no", "unknown"], default="unknown")
    p.add_argument("--other-insured", choices=["yes", "no", "unknown"], default="unknown")
    p.add_argument("--my-insured", choices=["yes", "no"], default="yes",
                   help="Was the vehicle you were IN covered by compulsory insurance "
                        "(no for an occupant of an uninsured vehicle). Ignored with --role "
                        "pedestrian. With Section 12(a), this gates Karnit.")
    p.add_argument("--role", choices=["driver", "passenger", "pedestrian"], default=None,
                   help="Your position in the accident. Needed with --my-insured no: a "
                        "pedestrian or cyclist and an occupant of an uninsured vehicle route "
                        "differently (PLATD Sections 2(a), 3, 12(a)).")
    p.add_argument("--my-comprehensive", action="store_true", help="You hold a comprehensive (מקיף) policy")
    p.add_argument("--example", action="store_true")
    args = p.parse_args()

    if args.example:
        demo = route(True, False, "property", "no", True, True, True)
        print(json.dumps(demo, ensure_ascii=False, indent=2))
        return 0

    other_insured = {"yes": True, "no": False, "unknown": None}[args.other_insured]
    my_compulsory = args.my_insured == "yes"
    result = route(args.injuries, args.hit_and_run, args.damage, args.my_fault,
                   other_insured, args.my_comprehensive, my_compulsory, args.role)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
