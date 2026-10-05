#!/usr/bin/env python3
"""DPA clause check - deterministic Art. 28(3) processor-contract checklist. Offline, zero deps.

A processor contract (DPA) MUST bind the processor to the eight obligations in GDPR/RODO
Art. 28(3)(a)-(h). This tool takes the clauses you found present and reports which mandatory
ones are MISSING - so the redline targets exactly the gaps.

The eight mandatory clauses (pass present ones via --present, keys a..h):
  a - process only on the controller's documented instructions (incl. transfers)
  b - confidentiality of authorised persons
  c - security measures (Art. 32)
  d - sub-processor conditions (authorisation + flow-down)
  e - assist with data subject rights (Chapter III)
  f - assist with Art. 32-36 (security, breaches, DPIA)
  g - delete or return the data at the end
  h - make available information and allow audits/inspections

Usage:
  python dpa_clause_check.py --present a,b,c,g
  python dpa_clause_check.py --present a,b,c,d,e,f,g,h   # complete
"""

from __future__ import annotations

import argparse
import json
import sys

CLAUSES = {
    "a": "Art. 28(3)(a) - wylacznie na udokumentowane polecenie / only on documented instructions",
    "b": "Art. 28(3)(b) - poufnosc osob upowaznionych / confidentiality of authorised persons",
    "c": "Art. 28(3)(c) - srodki bezpieczenstwa (Art. 32) / security measures",
    "d": "Art. 28(3)(d) - warunki podpowierzenia / sub-processor conditions",
    "e": "Art. 28(3)(e) - pomoc w prawach osob / assist with data subject rights",
    "f": "Art. 28(3)(f) - pomoc Art. 32-36 / assist with Art. 32-36",
    "g": "Art. 28(3)(g) - usuniecie lub zwrot danych / delete or return data",
    "h": "Art. 28(3)(h) - informacje i audyty / information and audits",
}


def check(present: list[str]) -> dict:
    bad = [c for c in present if c not in CLAUSES]
    if bad:
        raise SystemExit(f"error: nieznane klauzule {bad}; dozwolone a..h")
    have = sorted(set(present))
    missing = [k for k in CLAUSES if k not in have]
    complete = not missing
    return {
        "verdict": "complete" if complete else "incomplete",
        "present": [{k: CLAUSES[k]} for k in have],
        "missing": [{k: CLAUSES[k]} for k in missing],
        "missing_count": len(missing),
        "note": ("Wszystkie 8 klauzul obecne - sprawdz tez przedmiot/czas/cel (Art. 28(3) zd. 1) "
                 "i transfery rozdz. V. / All 8 present - also check subject/duration/purpose and Ch. V transfers."
                 if complete else
                 "Brakujace klauzule = cel redline. Umowa bez nich narusza Art. 28. "
                 "/ Missing clauses are the redline target; a DPA without them breaches Art. 28."),
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="DPA clause check (Art. 28(3))")
    p.add_argument("--present", default="", help="comma-separated present clause keys a..h")
    args = p.parse_args(argv)
    present = [x.strip() for x in args.present.split(",") if x.strip()]
    print(json.dumps(check(present), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
