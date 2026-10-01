#!/usr/bin/env python3
"""Two deterministic checks for Israeli wills and inheritance.

Offline, stdlib-only. It does NOT give legal advice; it applies two black-letter rules
from the Succession Law so an agent does not get them backwards:

1. order  -- which inheritance order to request (succession, probate, or BOTH where the
   will covers only part of the property, Section 66(b)).
2. witness -- whether Section 35 would void a bequest because a witness, or a person who
   wrote the will or took part in making it (--preparers), is a beneficiary or the spouse
   of a beneficiary. It compares NAMES only: it cannot know a relationship it was not
   told about, and it cannot check a witness's age or capacity (Section 24).

Exit codes: the witness check exits 1 when a bequest would be void under Section 35, a
witness is duplicated, or there are fewer than two distinct witnesses, so a caller can branch on the result.

Usage:
  python3 scripts/inheritance_helper.py order --has-will yes
  python3 scripts/inheritance_helper.py order --has-will no
  python3 scripts/inheritance_helper.py order --has-will partial
  python3 scripts/inheritance_helper.py witness --beneficiaries "דנה כהן,יוסי לוי" \
      --beneficiary-spouses "רות לוי" --witnesses "השכן רון,ד״ר אבני" \
      --preparers "יוסי לוי"
"""

import argparse
import re
import sys

TRANSFER_GROUNDS = (
    "an objection to the application was filed (67א(a)(1));",
    "the State or one of its institutions is a party (67א(a)(2));",
    "the Attorney General or their representative opened or joined a proceeding (67א(a)(3));",
    "the Public Trustee represents a person whose property it manages (67א(a)(4));",
    "the Registrar saw fit to transfer the application (67א(a)(8)).",
)

FILE_AT = (
    "file at: the Inheritance Registrar (הרשם לענייני ירושה), "
    "online portal inheritance.justice.gov.il"
)


def normalise(name: str) -> str:
    """Collapse internal whitespace and strip, so 'דנה  כהן ' == 'דנה כהן'."""
    return re.sub(r"\s+", " ", name).strip()


def split_names(raw: str) -> list:
    return [n for n in (normalise(p) for p in raw.split(",")) if n]


def print_forum_note():
    print("note: the Registrar issues most orders. A file moves to the Family Court only on a")
    print("Section 67א ground, of which an objection is just one:")
    for g in TRANSFER_GROUNDS:
        print(f"  - {g}")


def cmd_order(has_will: str) -> int:
    hw = normalise(has_will).lower()
    if hw in ("yes", "y", "true", "כן"):
        print("order: צו קיום צוואה (probate / will-execution order)")
        print("reason: a will exists and covers the estate, so it must be given binding effect.")
        print("check: confirm the will actually disposes of ALL the property. If it does not,")
        print("       re-run with --has-will partial (Section 66(b)).")
    elif hw in ("no", "n", "false", "לא"):
        print("order: צו ירושה (succession order)")
        print("reason: no will, so heirs are determined by law.")
    elif hw in ("partial", "part", "חלקי", "חלקית"):
        print("order: BOTH orders are needed (Section 66(b))")
        print("  1. צו קיום צוואה (probate order) over the part the will disposes of;")
        print("  2. צו ירושה (succession order) over the remainder.")
        print("reason: Section 66(b): ציווה המוריש חלק מנכסיו, יינתן על אותו חלק צו קיום,")
        print("        ועל הנותר - צו ירושה.")
        print("check: the legal heirs must be set out for the intestate remainder, as in a")
        print("       no-will file.")
    else:
        print(
            f"unknown value for --has-will: {has_will!r} (use yes, no, or partial)",
            file=sys.stderr,
        )
        return 1
    print(FILE_AT)
    print_forum_note()
    return 0


def cmd_witness(beneficiaries: str, witnesses: str, beneficiary_spouses: str,
                preparers: str = "") -> int:
    bens = set(split_names(beneficiaries))
    spouses = set(split_names(beneficiary_spouses))
    wits = split_names(witnesses)
    preps = set(split_names(preparers))

    failed = False

    seen = set()
    duplicates = []
    distinct = []
    for w in wits:
        if w in seen:
            duplicates.append(w)
        else:
            seen.add(w)
            distinct.append(w)

    if duplicates:
        failed = True
        print(f"INVALID: the same person is listed twice as a witness: {', '.join(duplicates)}")
        print("Two signatures by one person are one witness, not two (Section 20).")

    if len(distinct) < 2:
        failed = True
        print(
            f"INVALID: a witnessed will needs two distinct witnesses, found "
            f"{len(distinct)}."
        )

    bad_ben = [w for w in distinct if w in bens]
    bad_spouse = [w for w in distinct if w in spouses]

    bad_prep = sorted(p for p in preps if p in bens or p in spouses)

    if bad_ben:
        failed = True
        print(f"VOID bequest: these witnesses are beneficiaries: {', '.join(bad_ben)}")
    if bad_spouse:
        failed = True
        print(
            "VOID bequest: these witnesses are the spouse of a beneficiary: "
            f"{', '.join(bad_spouse)}"
        )
    if bad_prep:
        failed = True
        print(
            "VOID bequest: these people took part in preparing the will and are a "
            f"beneficiary or a beneficiary's spouse: {', '.join(bad_prep)}"
        )

    if bad_ben or bad_spouse or bad_prep:
        print("Section 35: a bequest in favour of whoever wrote the will, witnessed it, or")
        print("otherwise took part in making it, or in favour of that person's spouse, is void.")
        print("Section 35 does not apply to an oral will (צוואה בעל פה).")
        print("Fix: neutral adult witnesses who inherit nothing, and a preparer who inherits")
        print("nothing. Have an advocate review the draft before anyone signs.")

    if failed:
        print("result: FAIL")
        return 1

    print("no Section 35 conflict among the NAMES given. This is not a finding that the")
    print("will is valid.")
    print(f"checked {len(distinct)} distinct witnesses and {len(preps)} preparers against "
          f"{len(bens)} beneficiaries and {len(spouses)} beneficiary spouses.")
    print("Still confirm by hand: each witness is an adult and not פסול דין (Section 24);")
    print("every person who wrote or helped prepare the will was passed in --preparers;")
    print("and every beneficiary's spouse was passed in --beneficiary-spouses. Matching is")
    print("exact after whitespace normalisation, so a nickname or a missing surname, or a")
    print("spouse you did not list, will not be caught.")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Israeli wills/inheritance deterministic checks.")
    sub = p.add_subparsers(dest="cmd", required=True)

    o = sub.add_parser("order", help="Which inheritance order to request.")
    o.add_argument("--has-will", required=True, help="yes, no, or partial")

    w = sub.add_parser("witness", help="Check witnesses are not beneficiaries or their spouses.")
    w.add_argument("--beneficiaries", required=True, help="comma-separated names")
    w.add_argument("--witnesses", required=True, help="comma-separated names")
    w.add_argument(
        "--beneficiary-spouses",
        default="",
        help="comma-separated names of the beneficiaries' spouses (Section 35)",
    )
    w.add_argument(
        "--preparers",
        default="",
        help="comma-separated names of anyone who wrote the will or took part in making it",
    )

    args = p.parse_args()
    if args.cmd == "order":
        return cmd_order(args.has_will)
    if args.cmd == "witness":
        return cmd_witness(args.beneficiaries, args.witnesses, args.beneficiary_spouses,
                           args.preparers)
    return 1


if __name__ == "__main__":
    sys.exit(main())
