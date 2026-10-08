#!/usr/bin/env python3
"""Parse an Australian case citation and report the verification route.

Offline helper: it parses citation text and maps the court identifier or
report series to the skill that can verify it. It makes no network requests
and proves nothing about whether the cited decision exists.
"""

from __future__ import annotations

import argparse
import json
import re
import sys

NEUTRAL = re.compile(
    r"\[(?P<year>1[89]\d\d|20\d\d)\]\s+(?P<court>[A-Za-z][A-Za-z0-9]*[A-Za-z]|[A-Za-z]+)\s+(?P<number>\d+)"
)
REPORTED = re.compile(
    r"\((?P<year>1[89]\d\d|20\d\d)\)\s+(?P<volume>\d+)\s+(?P<series>[A-Z][A-Za-z ]*?)\s+(?P<page>\d+)"
)

# Court identifier -> (court name, jurisdiction, verification skill).
# A None skill means the court is recognised but not yet supported.
COURTS: dict[str, tuple[str, str, str | None]] = {
    "HCA": ("High Court of Australia", "Commonwealth", "verify-hca-judgment"),
    "FCA": ("Federal Court of Australia", "Commonwealth", "verify-federal-judgment"),
    "FCAFC": ("Federal Court of Australia, Full Court", "Commonwealth", "verify-federal-judgment"),
    "FEDCFAMC1A": (
        "Federal Circuit and Family Court (Division 1), Appellate",
        "Commonwealth",
        "verify-federal-judgment",
    ),
    "FEDCFAMC1F": (
        "Federal Circuit and Family Court (Division 1)",
        "Commonwealth",
        "verify-federal-judgment",
    ),
    "FEDCFAMC2F": (
        "Federal Circuit and Family Court (Division 2), Family",
        "Commonwealth",
        "verify-federal-judgment",
    ),
    "FEDCFAMC2G": (
        "Federal Circuit and Family Court (Division 2), General",
        "Commonwealth",
        "verify-federal-judgment",
    ),
    "FCCA": ("Federal Circuit Court of Australia (historical)", "Commonwealth", "verify-federal-judgment"),
    "FAMCA": ("Family Court of Australia (historical)", "Commonwealth", "verify-federal-judgment"),
    "FAMCAFC": (
        "Family Court of Australia, Full Court (historical)",
        "Commonwealth",
        "verify-federal-judgment",
    ),
    "NSWSC": ("Supreme Court of New South Wales", "New South Wales", "verify-nsw-judgment"),
    "NSWCA": ("Court of Appeal of New South Wales", "New South Wales", "verify-nsw-judgment"),
    "NSWCCA": ("Court of Criminal Appeal of New South Wales", "New South Wales", "verify-nsw-judgment"),
    "NSWDC": ("District Court of New South Wales", "New South Wales", "verify-nsw-judgment"),
    "NSWLC": ("Local Court of New South Wales", "New South Wales", "verify-nsw-judgment"),
    "NSWLEC": (
        "Land and Environment Court of New South Wales",
        "New South Wales",
        "verify-nsw-judgment",
    ),
    "NSWIC": ("Industrial Court of New South Wales", "New South Wales", "verify-nsw-judgment"),
    "NSWCATAP": ("NSW Civil and Administrative Tribunal, Appeal Panel", "New South Wales", "verify-nsw-judgment"),
    "NSWCATAD": (
        "NSW Civil and Administrative Tribunal, Administrative and Equal Opportunity",
        "New South Wales",
        "verify-nsw-judgment",
    ),
    "VSC": ("Supreme Court of Victoria", "Victoria", None),
    "VSCA": ("Court of Appeal of Victoria", "Victoria", None),
    "QSC": ("Supreme Court of Queensland", "Queensland", None),
    "QCA": ("Court of Appeal of Queensland", "Queensland", None),
    "WASC": ("Supreme Court of Western Australia", "Western Australia", None),
    "WASCA": ("Court of Appeal of Western Australia", "Western Australia", None),
    "SASC": ("Supreme Court of South Australia", "South Australia", None),
    "SASCA": ("Court of Appeal of South Australia", "South Australia", None),
    "TASSC": ("Supreme Court of Tasmania", "Tasmania", None),
    "ACTSC": ("Supreme Court of the Australian Capital Territory", "Australian Capital Territory", None),
    "NTSC": ("Supreme Court of the Northern Territory", "Northern Territory", None),
}

# Report series -> (series name, resolution hint).
SERIES: dict[str, tuple[str, str]] = {
    "CLR": ("Commonwealth Law Reports", "verify-hca-judgment"),
    "ALJR": ("Australian Law Journal Reports", "verify-hca-judgment"),
    "FCR": ("Federal Court Reports", "verify-federal-judgment"),
    "NSWLR": ("New South Wales Law Reports", "verify-nsw-judgment"),
}


def matched_int(match: re.Match[str], group: str) -> int:
    try:
        return int(match.group(group))
    except (IndexError, ValueError) as exc:
        raise ValueError(f"invalid numeric citation group {group!r}") from exc


def parse(text: str) -> dict[str, object]:
    """Parse one citation string into a routing record."""
    neutral = NEUTRAL.search(text)
    if neutral:
        court_id = neutral.group("court").upper()
        court = COURTS.get(court_id)
        record: dict[str, object] = {
            "input": text.strip(),
            "citation_type": "medium-neutral",
            "year": matched_int(neutral, "year"),
            "court_id": neutral.group("court"),
            "number": matched_int(neutral, "number"),
        }
        if court is None:
            record["route"] = None
            record["note"] = f"unrecognised court identifier {court_id!r}"
        else:
            name, jurisdiction, skill = court
            record["court"] = name
            record["jurisdiction"] = jurisdiction
            record["route"] = skill
            if skill is None:
                record["note"] = f"{name} is recognised but not yet supported by a verification skill"
        return record

    reported = REPORTED.search(text)
    if reported:
        series_id = reported.group("series").strip().upper().replace(" ", "")
        series = SERIES.get(series_id)
        record = {
            "input": text.strip(),
            "citation_type": "reported",
            "year": matched_int(reported, "year"),
            "volume": matched_int(reported, "volume"),
            "series_id": reported.group("series").strip(),
            "page": matched_int(reported, "page"),
        }
        if series is None:
            record["route"] = None
            record["note"] = "unrecognised report series; resolve to a medium-neutral citation before verification"
        else:
            name, skill = series
            record["series"] = name
            record["route"] = skill
            record["note"] = (
                "reported citation: resolve to a medium-neutral citation at the "
                "official publisher before treating the decision as verified"
            )
        return record

    return {
        "input": text.strip(),
        "citation_type": "unknown",
        "route": None,
        "note": "no medium-neutral or reported citation found; search the court publisher by case name",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("citation", nargs="+", help="citation text, for example '[2023] HCA 12'")
    args = parser.parse_args()
    records = [parse(citation) for citation in args.citation]
    json.dump(records if len(records) > 1 else records[0], sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
