#!/usr/bin/env python3
"""
verzugszins_rechner.py
======================

Rechnet Verzugszinsen nach §§ 286, 288 BGB aus.

* Bei Rechtsgeschaeften mit Verbraucherbeteiligung: Basiszinssatz + 5 Prozentpunkte (§ 288 Abs. 1 BGB).
* Bei reinen B2B-Forderungen (kein Verbraucher beteiligt): Basiszinssatz + 9 Prozentpunkte (§ 288 Abs. 2 BGB).

Eingabe
-------

* Hauptforderung in EUR
* Verzugsbeginn (JJJJ-MM-TT)
* Verzugsende (JJJJ-MM-TT, optional, sonst heute)
* Art (b2c | b2b)

Ausgabe
-------

Tabelle der angewendeten Basiszinsperioden mit Zinslauf, daraus
Tageszins, daraus aufgelaufener Zins.

Quelle Basiszinssatz
--------------------

§ 247 BGB: jeweils 1. Januar und 1. Juli, festgestellt von der
Deutschen Bundesbank. Die Tabelle `BASISZINS` listet die historisch
veroeffentlichten Werte; bei neuen Periodengrenzen ist sie zu
ergaenzen.

Lizenz / Verantwortung
----------------------

Der Rechner ist Berechnungshilfe; die rechtliche Bewertung der
Verzugsvoraussetzungen (§ 286 BGB: Mahnung / Kalendermahnung /
Entbehrlichkeit) bleibt im Einzelfall beim Anwalt.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import List, Optional, Tuple


# ---------------------------------------------------------------------------
# Basiszinssatz nach Paragraf 247 BGB (amtlicher Stand bis 31.12.2026)
# Liste: (gueltig_ab, satz_in_prozent)
# Quelle: Bundesbank-Veroeffentlichungen.
# ---------------------------------------------------------------------------

BASISZINS: List[Tuple[date, float]] = [
    (date(2002, 1, 1), 2.57),
    (date(2002, 7, 1), 2.47),
    (date(2003, 1, 1), 1.97),
    (date(2003, 7, 1), 1.22),
    (date(2004, 1, 1), 1.14),
    (date(2004, 7, 1), 1.13),
    (date(2005, 1, 1), 1.21),
    (date(2005, 7, 1), 1.17),
    (date(2006, 1, 1), 1.37),
    (date(2006, 7, 1), 1.95),
    (date(2007, 1, 1), 2.70),
    (date(2007, 7, 1), 3.19),
    (date(2008, 1, 1), 3.32),
    (date(2008, 7, 1), 3.19),
    (date(2009, 1, 1), 1.62),
    (date(2009, 7, 1), 0.12),
    (date(2011, 7, 1), 0.37),
    (date(2012, 1, 1), 0.12),
    (date(2013, 1, 1), -0.13),
    (date(2013, 7, 1), -0.38),
    (date(2014, 1, 1), -0.63),
    (date(2014, 7, 1), -0.73),
    (date(2015, 1, 1), -0.83),
    (date(2016, 7, 1), -0.88),
    (date(2023, 1, 1), 1.62),
    (date(2023, 7, 1), 3.12),
    (date(2024, 1, 1), 3.62),
    (date(2024, 7, 1), 3.37),
    (date(2025, 1, 1), 2.27),
    (date(2025, 7, 1), 1.27),
    (date(2026, 1, 1), 1.27),
    (date(2026, 7, 1), 1.52),
]

BASISZINS_GUELTIG_BIS = date(2026, 12, 31)


def basiszins_an(tag: date) -> float:
    """Liefert den am `tag` gueltigen Basiszinssatz."""
    if tag < BASISZINS[0][0]:
        raise ValueError(f"Datum {tag} liegt vor erstem hinterlegten Basiszins-Eintrag.")
    if tag > BASISZINS_GUELTIG_BIS:
        raise ValueError(
            f"Datum {tag} liegt nach dem amtlich hinterlegten Stand "
            f"{BASISZINS_GUELTIG_BIS}. Basiszinssatz der Bundesbank ergänzen."
        )
    aktuell = BASISZINS[0][1]
    for grenze, satz in BASISZINS:
        if tag >= grenze:
            aktuell = satz
        else:
            break
    return aktuell


# ---------------------------------------------------------------------------
# Berechnung
# ---------------------------------------------------------------------------

@dataclass
class Periode:
    von: date
    bis: date  # inklusive
    basiszins: float
    aufschlag: float
    forderung: float

    @property
    def tage(self) -> int:
        return (self.bis - self.von).days + 1

    @property
    def zinssatz(self) -> float:
        return self.basiszins + self.aufschlag

    @property
    def zinsen(self) -> float:
        # Das Werkzeug verwendet die verbreitete 365-Tage-Konvention.
        # Abweichende vertragliche oder gesetzliche Berechnungsvorgaben gehen vor.
        return round(self.forderung * (self.zinssatz / 100.0) * self.tage / 365.0, 2)


def periodisieren(beginn: date, ende: date) -> List[Tuple[date, date, float]]:
    """Zerlegt das Intervall [beginn, ende] in Stuecke konstanten Basiszinses."""
    if beginn > ende:
        raise ValueError("Verzugsbeginn liegt nach Verzugsende.")
    grenzen = [g for g, _ in BASISZINS if beginn < g <= ende]
    stuecke: List[Tuple[date, date, float]] = []
    von = beginn
    while True:
        # naechste Grenze finden, sonst ende
        naechste = None
        for g in grenzen:
            if g > von:
                naechste = g
                break
        bis = (naechste - timedelta(days=1)) if naechste else ende
        if bis > ende:
            bis = ende
        stuecke.append((von, bis, basiszins_an(von)))
        if not naechste or naechste > ende:
            break
        von = naechste
    return stuecke


def berechne(hauptforderung: float, beginn: date, ende: date, art: str) -> Tuple[List[Periode], float, float]:
    if hauptforderung <= 0:
        raise ValueError("Hauptforderung muss > 0 sein.")
    if art not in ("b2c", "b2b"):
        raise ValueError("Art muss 'b2c' oder 'b2b' sein.")
    aufschlag = 5.0 if art == "b2c" else 9.0
    perioden = [
        Periode(von=von, bis=bis, basiszins=zins, aufschlag=aufschlag, forderung=hauptforderung)
        for von, bis, zins in periodisieren(beginn, ende)
    ]
    summe = round(sum(p.zinsen for p in perioden), 2)
    gesamt = round(hauptforderung + summe, 2)
    return perioden, summe, gesamt


# ---------------------------------------------------------------------------
# Formatierung
# ---------------------------------------------------------------------------

def _de(value: float, dezimal: int = 2) -> str:
    s = f"{value:,.{dezimal}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def tabelle(perioden: List[Periode]) -> str:
    zeilen = []
    zeilen.append("Von         Bis         Tage  Basis  +Aufschlag  Satz    Zinsen")
    zeilen.append("-" * 70)
    for p in perioden:
        zeilen.append(
            f"{p.von.isoformat()}  {p.bis.isoformat()}  {p.tage:>4}  "
            f"{p.basiszins:>5.2f}  {p.aufschlag:>9.2f}  "
            f"{p.zinssatz:>5.2f}  {_de(p.zinsen):>10} EUR"
        )
    return "\n".join(zeilen)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_datum(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Verzugszins-Rechner nach §§ 286, 288 BGB.")
    parser.add_argument("--forderung", required=True, type=float, help="Hauptforderung in EUR.")
    parser.add_argument("--beginn", required=True, type=parse_datum, help="Verzugsbeginn JJJJ-MM-TT.")
    parser.add_argument("--ende", type=parse_datum, default=None, help="Verzugsende JJJJ-MM-TT (Default heute).")
    parser.add_argument("--art", choices=("b2c", "b2b"), default="b2c",
                        help="b2c = §288 Abs. 1 (+5 Pkt.), b2b = §288 Abs. 2 (+9 Pkt.).")
    args = parser.parse_args(argv)

    ende = args.ende if args.ende else date.today()
    try:
        perioden, summe, gesamt = berechne(args.forderung, args.beginn, ende, args.art)
    except ValueError as exc:
        print(f"FEHLER: {exc}", file=sys.stderr)
        return 1

    print(f"Hauptforderung:   {_de(args.forderung):>14} EUR")
    print(f"Verzugsbeginn:    {args.beginn.isoformat()}")
    print(f"Verzugsende:      {ende.isoformat()}")
    print(f"Art:              {args.art} (Aufschlag {'5' if args.art == 'b2c' else '9'} Prozentpunkte)")
    print()
    print(tabelle(perioden))
    print("-" * 70)
    print(f"Verzugszinsen:    {_de(summe):>14} EUR")
    print(f"Gesamtforderung:  {_de(gesamt):>14} EUR")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
