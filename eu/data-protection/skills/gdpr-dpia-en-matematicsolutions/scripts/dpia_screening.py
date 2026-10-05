#!/usr/bin/env python3
"""DPIA screening - deterministic threshold test for GDPR/RODO Art. 35. Offline, zero deps.

Decides whether a Data Protection Impact Assessment is REQUIRED, based on:
- the EDPB WP248 rev.01 nine criteria (rule of thumb: >=2 met => DPIA), and
- the Art. 35(3) mandatory cases (any one => DPIA).

This is a clerical screening aid. A "not required" result is NOT a clearance - the controller
still documents the reasoning, and a single strong criterion can warrant a DPIA. The legal call
stays with the controller / DPO.

The nine EDPB criteria (pass the keys that apply via --criteria):
  evaluation        - evaluation or scoring (incl. profiling and predicting)
  automated         - automated decision-making with legal/significant effect (Art. 22)
  monitoring        - systematic monitoring
  sensitive         - sensitive data or data of a highly personal nature
  largescale        - data processed on a large scale
  matching          - matching or combining datasets
  vulnerable        - data on vulnerable subjects (children, employees, patients)
  innovation        - innovative use / new technology (AI, IoT, biometrics)
  blocking          - processing that prevents a right or use of a service/contract

Art. 35(3) mandatory cases (pass via --mandatory):
  systematic_eval   - systematic and extensive evaluation incl. profiling (35(3)(a))
  special_largescale- large-scale special-category or criminal data (35(3)(b))
  public_monitoring - large-scale systematic monitoring of a public area (35(3)(c))

Usage:
  python dpia_screening.py --criteria evaluation,sensitive,largescale
  python dpia_screening.py --mandatory public_monitoring
  python dpia_screening.py --criteria innovation
"""

from __future__ import annotations

import argparse
import json
import sys

NINE = {
    "evaluation": "ocena lub scoring / evaluation or scoring (Art. 35; WP248)",
    "automated": "decyzje zautomatyzowane ze skutkiem prawnym / automated decisions (Art. 22)",
    "monitoring": "systematyczne monitorowanie / systematic monitoring",
    "sensitive": "dane wrazliwe lub wysoce osobiste / sensitive or highly personal data",
    "largescale": "duza skala / large scale",
    "matching": "laczenie lub zestawianie zbiorow / matching or combining datasets",
    "vulnerable": "osoby wymagajace szczegolnej opieki / vulnerable data subjects",
    "innovation": "nowa technologia / innovative use (AI, IoT, biometria)",
    "blocking": "uniemozliwienie realizacji prawa lub uslugi / preventing a right or service",
}
MANDATORY = {
    "systematic_eval": "Art. 35(3)(a) - systematyczna kompleksowa ocena (profilowanie)",
    "special_largescale": "Art. 35(3)(b) - dane szczegolne/karne na duza skale",
    "public_monitoring": "Art. 35(3)(c) - monitoring miejsc publicznych na duza skale",
}


def screen(criteria: list[str], mandatory: list[str]) -> dict:
    bad_c = [c for c in criteria if c not in NINE]
    bad_m = [m for m in mandatory if m not in MANDATORY]
    if bad_c or bad_m:
        raise SystemExit(f"error: nieznane klucze {bad_c + bad_m}; patrz --help")
    met = sorted(set(criteria))
    mand = sorted(set(mandatory))
    n = len(met)
    if mand:
        verdict, basis = "required", "Art. 35(3) - przypadek obligatoryjny / mandatory case"
    elif n >= 2:
        verdict, basis = "required", f"WP248 - spelnione {n} kryteria (reguła >=2) / {n} criteria met"
    elif n == 1:
        verdict, basis = "recommended", "1 kryterium - rozwaz DPIA i udokumentuj decyzje / 1 criterion - consider"
    else:
        verdict, basis = "not_required", "brak kryteriow - udokumentuj brak DPIA / no criteria - document the decision"
    return {
        "verdict": verdict,
        "basis": basis,
        "criteria_met": [{k: NINE[k]} for k in met],
        "criteria_count": n,
        "mandatory_cases": [{k: MANDATORY[k]} for k in mand],
        "note": "Wynik to przesiew, nie zwolnienie. Pojedyncze silne kryterium tez moze uzasadniac DPIA. "
                "Decyzja i dokumentacja: administrator/IOD. / Screening only - the controller decides and documents.",
    }


def _split(s: str | None) -> list[str]:
    return [x.strip() for x in s.split(",")] if s else []


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="DPIA screening (Art. 35)")
    p.add_argument("--criteria", help="comma-separated EDPB criteria keys")
    p.add_argument("--mandatory", help="comma-separated Art. 35(3) case keys")
    args = p.parse_args(argv)
    if not args.criteria and not args.mandatory:
        p.error("pass --criteria and/or --mandatory (see --help for keys)")
    print(json.dumps(screen(_split(args.criteria), _split(args.mandatory)), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
