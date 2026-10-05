#!/usr/bin/env python3
"""CLI for Polish working days, public holidays, working-time norms and tax/ZUS deadlines.

Deterministic and fully offline. Every rule cites its legal basis:
- public holidays: art. 1 ustawy z 18 stycznia 1951 r. o dniach wolnych od pracy
  (24 grudnia – Wigilia – added by Dz.U. 2024 poz. 1965, in force from 2025-02-01)
- working-time norm: art. 130 § 1–2 Kodeksu pracy
- deadlines shifted to the next working day: art. 12 § 5 Ordynacji podatkowej
  (tax and ZUS) and art. 115 Kodeksu cywilnego (civil-law terms, e.g. invoice payment)
- day counting: art. 111 § 2 Kodeksu cywilnego (the starting day is not counted)

Zero external dependencies (Python 3.8+ standard library only).

Copyright (c) 2026 Michell Hoduń <mhodun@gmail.com> (https://github.com/b44x)
Licensed under the MIT License.
"""

import argparse
import calendar
import datetime
import json
import sys
from typing import Any, Dict, List, Optional, Tuple

RULES_VERIFIED = "2026-09-28"
MIN_YEAR, MAX_YEAR = 1990, 2100
WIGILIA_FROM = datetime.date(2025, 2, 1)
WEEKDAYS = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]
MONTHS = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec",
          "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
HOLIDAYS_BASIS = "art. 1 ustawy z dnia 18 stycznia 1951 r. o dniach wolnych od pracy (Dz.U. 1951 nr 4 poz. 28 ze zm.)"
TAX_SHIFT = "art. 12 § 5 Ordynacji podatkowej"
CIVIL_SHIFT = "art. 115 Kodeksu cywilnego"

# Monthly obligations for a settlement month; day = day of the FOLLOWING month.
DEADLINES: List[Dict[str, Any]] = [
    {"id": "zus-jednostki-budzetowe", "day": 5, "name": "Składki ZUS (DRA/RCA) — jednostki budżetowe i samorządowe zakłady budżetowe",
     "basis": "art. 47 ust. 1 pkt 2 ustawy o systemie ubezpieczeń społecznych"},
    {"id": "zus-osoby-prawne", "day": 15, "name": "Składki ZUS (DRA/RCA) — płatnicy posiadający osobowość prawną (np. sp. z o.o., S.A.)",
     "basis": "art. 47 ust. 1 pkt 3 ustawy o systemie ubezpieczeń społecznych"},
    {"id": "ppk", "day": 15, "name": "Wpłaty do PPK (pobrane za poprzedni miesiąc)",
     "basis": "art. 28 ust. 4 ustawy o pracowniczych planach kapitałowych"},
    {"id": "zus-pozostali", "day": 20, "name": "Składki ZUS (DRA/RCA) — pozostali płatnicy (np. JDG, spółki osobowe)",
     "basis": "art. 47 ust. 1 pkt 4 ustawy o systemie ubezpieczeń społecznych"},
    {"id": "pit-zaliczka", "day": 20, "name": "Zaliczka na PIT przedsiębiorcy (miesięczna)",
     "basis": "art. 44 ust. 6 ustawy o podatku dochodowym od osób fizycznych"},
    {"id": "pit-platnik", "day": 20, "name": "Przekazanie pobranych zaliczek PIT przez płatnika (np. od wynagrodzeń)",
     "basis": "art. 38 ust. 1 ustawy o podatku dochodowym od osób fizycznych"},
    {"id": "cit-zaliczka", "day": 20, "name": "Zaliczka na CIT (miesięczna)",
     "basis": "art. 25 ust. 1a ustawy o podatku dochodowym od osób prawnych"},
    {"id": "vat", "day": 25, "name": "VAT: JPK_V7M (deklaracja z ewidencją) i zapłata podatku za miesiąc",
     "basis": "art. 99 ust. 1 i art. 103 ust. 1 ustawy o podatku od towarów i usług"},
]


def error_exit(message: str, error_type: str = "error", code: int = 64) -> None:
    """Print structured error JSON to stderr and exit."""
    json.dump({"error": message, "type": error_type}, sys.stderr, ensure_ascii=False)
    sys.stderr.write("\n")
    sys.exit(code)


def check_year(year: int) -> int:
    if not MIN_YEAR <= year <= MAX_YEAR:
        error_exit(f"Rok {year} poza obsługiwanym zakresem {MIN_YEAR}–{MAX_YEAR}.", "bad_request", 64)
    return year


def parse_date(text: str) -> datetime.date:
    try:
        d = datetime.date.fromisoformat(text.strip())
    except ValueError:
        error_exit(f"Nieprawidłowa data '{text}'. Oczekiwany format: RRRR-MM-DD.", "bad_request", 64)
    check_year(d.year)
    return d


def parse_month(text: str) -> Tuple[int, int]:
    try:
        year, month = (int(x) for x in text.strip().split("-"))
        datetime.date(year, month, 1)
    except ValueError:
        error_exit(f"Nieprawidłowy miesiąc '{text}'. Oczekiwany format: RRRR-MM.", "bad_request", 64)
    return check_year(year), month


# --------------------------------------------------------------------------- calendar core

def easter(year: int) -> datetime.date:
    """Gregorian Easter Sunday (Anonymous Gregorian / Meeus algorithm)."""
    a, b, c = year % 19, year // 100, year % 100
    d, e = b // 4, b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = c // 4, c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = (h + l - 7 * m + 114) % 31 + 1
    return datetime.date(year, month, day)


def holidays(year: int) -> Dict[datetime.date, str]:
    """Statutory days off (dni ustawowo wolne od pracy) other than ordinary Sundays."""
    e = easter(year)
    days = {
        datetime.date(year, 1, 1): "Nowy Rok",
        datetime.date(year, 1, 6): "Święto Trzech Króli",
        e: "Wielkanoc (pierwszy dzień Wielkiej Nocy)",
        e + datetime.timedelta(days=1): "Poniedziałek Wielkanocny (drugi dzień Wielkiej Nocy)",
        datetime.date(year, 5, 1): "Święto Państwowe (1 Maja)",
        datetime.date(year, 5, 3): "Święto Narodowe Trzeciego Maja",
        e + datetime.timedelta(days=49): "Zielone Świątki (pierwszy dzień)",
        e + datetime.timedelta(days=60): "Boże Ciało",
        datetime.date(year, 8, 15): "Wniebowzięcie Najświętszej Maryi Panny",
        datetime.date(year, 11, 1): "Wszystkich Świętych",
        datetime.date(year, 11, 11): "Narodowe Święto Niepodległości",
        datetime.date(year, 12, 25): "Boże Narodzenie (pierwszy dzień)",
        datetime.date(year, 12, 26): "Boże Narodzenie (drugi dzień)",
    }
    wigilia = datetime.date(year, 12, 24)
    if wigilia >= WIGILIA_FROM:
        days[wigilia] = "Wigilia Bożego Narodzenia"
    return dict(sorted(days.items()))


def holiday_name(d: datetime.date) -> Optional[str]:
    return holidays(d.year).get(d)


def is_working_day(d: datetime.date) -> bool:
    """Monday–Friday that is not a statutory holiday."""
    return d.weekday() < 5 and holiday_name(d) is None


def is_day_off_for_deadlines(d: datetime.date) -> bool:
    """Saturday, Sunday or a statutory holiday (art. 12 § 5 OP, art. 115 KC)."""
    return d.weekday() >= 5 or holiday_name(d) is not None


def next_deadline_day(d: datetime.date) -> datetime.date:
    while is_day_off_for_deadlines(d):
        d += datetime.timedelta(days=1)
    return d


def describe(d: datetime.date) -> Dict[str, Any]:
    return {"date": d.isoformat(), "weekday": WEEKDAYS[d.weekday()], "holiday": holiday_name(d),
            "isWorkingDay": is_working_day(d)}


def days_between(start: datetime.date, end: datetime.date) -> List[datetime.date]:
    return [start + datetime.timedelta(days=i) for i in range((end - start).days + 1)]


def month_bounds(year: int, month: int) -> Tuple[datetime.date, datetime.date]:
    return datetime.date(year, month, 1), datetime.date(year, month, calendar.monthrange(year, month)[1])


# --------------------------------------------------------------------------- commands

def out(data: Dict[str, Any]) -> None:
    data["rulesVerified"] = RULES_VERIFIED
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_holidays(args: argparse.Namespace) -> None:
    year = check_year(args.year or datetime.date.today().year)
    items = [{"date": d.isoformat(), "weekday": WEEKDAYS[d.weekday()], "name": n} for d, n in holidays(year).items()]
    out({"year": year, "count": len(items), "holidays": items,
         "note": "Wszystkie niedziele są również dniami wolnymi od pracy.", "legalBasis": HOLIDAYS_BASIS})


def cmd_day(args: argparse.Namespace) -> None:
    d = parse_date(args.date)
    info = describe(d)
    info["nextWorkingDay"] = next((x.isoformat() for x in (d + datetime.timedelta(days=i) for i in range(1, 15)) if is_working_day(x)), None)
    out(info)


def cmd_workdays(args: argparse.Namespace) -> None:
    start, end = parse_date(args.start), parse_date(args.end)
    if end < start:
        error_exit("Data końcowa jest wcześniejsza niż początkowa.", "bad_request", 64)
    days = days_between(start, end)
    hol = [{"date": d.isoformat(), "weekday": WEEKDAYS[d.weekday()], "name": holiday_name(d)} for d in days if holiday_name(d)]
    out({"from": start.isoformat(), "to": end.isoformat(), "inclusive": True, "calendarDays": len(days),
         "workingDays": sum(1 for d in days if is_working_day(d)), "holidays": hol,
         "definition": "Dzień roboczy = poniedziałek–piątek, który nie jest dniem ustawowo wolnym od pracy."})


def cmd_month(args: argparse.Namespace) -> None:
    year, month = parse_month(args.month)
    first, last = month_bounds(year, month)
    days = days_between(first, last)
    mon_fri = sum(1 for d in days if d.weekday() < 5)
    hol = [(d, n) for d, n in holidays(year).items() if first <= d <= last]
    reducing = [(d, n) for d, n in hol if d.weekday() != 6]
    saturday = [(d, n) for d, n in hol if d.weekday() == 5]
    hours = 8 * mon_fri - 8 * len(reducing)
    out({
        "month": f"{year}-{month:02d}", "monthName": MONTHS[month - 1],
        "calendarDays": len(days),
        "workingDays": sum(1 for d in days if is_working_day(d)),
        "workingTimeNormHours": hours,
        "workingTimeNormDays": hours // 8,
        "holidays": [{"date": d.isoformat(), "weekday": WEEKDAYS[d.weekday()], "name": n} for d, n in hol],
        "saturdayHolidays": [{"date": d.isoformat(), "name": n} for d, n in saturday],
        "calculation": f"8 h × {mon_fri} dni pon.–pt. − 8 h × {len(reducing)} święta poza niedzielą = {hours} h",
        "legalBasis": "art. 130 § 1–2 Kodeksu pracy (pełny etat, okres rozliczeniowy = 1 miesiąc)",
    })


def cmd_add(args: argparse.Namespace) -> None:
    start = parse_date(args.date)
    if args.days < 0 or args.days > 3660:
        error_exit("Liczba dni musi być w zakresie 0–3660.", "bad_request", 64)
    if args.workdays:
        d, left = start, args.days
        while left:
            d += datetime.timedelta(days=1)
            if is_working_day(d):
                left -= 1
        out({"from": start.isoformat(), "workingDaysAdded": args.days, "result": describe(d),
             "rule": "Liczone są tylko dni robocze (pon.–pt. bez świąt); dzień początkowy nie jest liczony."})
        return
    nominal = start + datetime.timedelta(days=args.days)
    final = next_deadline_day(nominal)
    out({
        "from": start.isoformat(), "daysAdded": args.days,
        "nominalEnd": describe(nominal),
        "deadline": describe(final),
        "shifted": final != nominal,
        "rule": "Termin w dniach: dzień początkowy nie jest liczony (art. 111 § 2 KC); jeśli koniec terminu przypada "
                f"w sobotę lub dzień ustawowo wolny, termin upływa następnego dnia roboczego ({CIVIL_SHIFT}, {TAX_SHIFT}).",
    })


def cmd_deadlines(args: argparse.Namespace) -> None:
    year, month = parse_month(args.month)
    due_year, due_month = (year + 1, 1) if month == 12 else (year, month + 1)
    items = []
    for item in DEADLINES:
        if args.only and item["id"] not in args.only:
            continue
        nominal = datetime.date(due_year, due_month, item["day"])
        final = next_deadline_day(nominal)
        items.append({
            "id": item["id"], "obligation": item["name"],
            "nominalDate": nominal.isoformat(), "deadline": final.isoformat(),
            "weekday": WEEKDAYS[final.weekday()], "shifted": final != nominal,
            "shiftReason": (holiday_name(nominal) or WEEKDAYS[nominal.weekday()]) if final != nominal else None,
            "legalBasis": item["basis"],
        })
    if not items:
        error_exit(f"Brak obowiązków o identyfikatorach: {', '.join(args.only)}.", "not_found", 2)
    out({
        "settlementMonth": f"{year}-{month:02d}", "dueMonth": f"{due_year}-{due_month:02d}",
        "count": len(items), "deadlines": sorted(items, key=lambda x: (x["deadline"], x["id"])),
        "shiftRule": f"Termin przypadający w sobotę lub dzień ustawowo wolny przesuwa się na następny dzień roboczy ({TAX_SHIFT}).",
        "disclaimer": "Terminy ogólne dla rozliczeń miesięcznych. Nie obejmują rozliczeń kwartalnych, metody kasowej, "
                      "szczególnych przypadków ani zmian przepisów po dacie rulesVerified. Nie stanowią porady podatkowej.",
    })


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Dni robocze, święta, wymiar czasu pracy i terminy podatkowe/ZUS w Polsce (offline)."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("holidays", help="Dni ustawowo wolne od pracy w danym roku")
    p.add_argument("--year", type=int, help="Rok (domyślnie bieżący)")
    p.set_defaults(func=cmd_holidays)

    p = sub.add_parser("day", help="Czy dany dzień jest roboczy / świętem")
    p.add_argument("date", help="Data RRRR-MM-DD")
    p.set_defaults(func=cmd_day)

    p = sub.add_parser("workdays", help="Liczba dni roboczych między datami (włącznie)")
    p.add_argument("start", help="Data początkowa RRRR-MM-DD")
    p.add_argument("end", help="Data końcowa RRRR-MM-DD")
    p.set_defaults(func=cmd_workdays)

    p = sub.add_parser("month", help="Dni robocze i wymiar czasu pracy w miesiącu")
    p.add_argument("month", help="Miesiąc RRRR-MM")
    p.set_defaults(func=cmd_month)

    p = sub.add_parser("add", help="Termin: data + N dni (np. termin płatności faktury)")
    p.add_argument("date", help="Data początkowa RRRR-MM-DD (np. data wystawienia faktury)")
    p.add_argument("days", type=int, help="Liczba dni")
    p.add_argument("--workdays", action="store_true", help="Licz dni robocze zamiast kalendarzowych")
    p.set_defaults(func=cmd_add)

    p = sub.add_parser("deadlines", help="Terminy ZUS, PIT, CIT, VAT i PPK za dany miesiąc rozliczeniowy")
    p.add_argument("month", help="Miesiąc rozliczeniowy RRRR-MM (terminy przypadają w następnym miesiącu)")
    p.add_argument("--only", nargs="+", choices=[d["id"] for d in DEADLINES], help="Tylko wybrane obowiązki")
    p.set_defaults(func=cmd_deadlines)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
