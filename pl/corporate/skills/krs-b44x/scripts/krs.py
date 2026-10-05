#!/usr/bin/env python3
"""CLI for Krajowy Rejestr Sądowy (KRS) official Ministry of Justice API.

Official API: https://api-krs.ms.gov.pl/
Zero external dependencies (Python 3.8+ stdlib only).

Copyright (c) 2026 Michell Hoduń <mhodun@gmail.com> (https://github.com/b44x)
Licensed under the MIT License.
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

API_BASE_URL = "https://api-krs.ms.gov.pl/api/krs"
USER_AGENT = "ai-polish-skills-krs/1.0.0 (+https://github.com/b44x/ai-polish-skills)"


def error_exit(message: str, error_type: str = "error", code: int = 64) -> None:
    """Print error JSON to stderr and exit."""
    json.dump({"error": message, "type": error_type}, sys.stderr, ensure_ascii=False)
    sys.stderr.write("\n")
    sys.exit(code)


def sanitize_krs(val: str) -> str:
    """Strip spaces, non-digits, and pad to 10 digits."""
    digits = re.sub(r"\D", "", val.strip())
    if not digits:
        error_exit("Numer KRS musi zawierać cyfry.", "validation_error", 64)
    if len(digits) > 10:
        error_exit(f"Numer KRS nie może mieć więcej niż 10 cyfr (podano {len(digits)}).", "validation_error", 64)
    return digits.zfill(10)


def fetch_odpis(krs_10: str, typ_odpisu: str = "OdpisAktualny", register: Optional[str] = None) -> Tuple[Dict[str, Any], str]:
    """Fetch odpis from KRS API trying Przedsiębiorcy (P) then Stowarzyszenia (S)."""
    registers_to_try = [register.upper()] if register else ["P", "S"]

    for rej in registers_to_try:
        url = f"{API_BASE_URL}/{typ_odpisu}/{krs_10}?rejestr={rej}&format=json"
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Accept": "application/json",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data, rej
        except urllib.error.HTTPError as e:
            if e.code == 404:
                continue
            elif e.code == 400:
                error_exit(f"Nieprawidłowe zapytanie do KRS: {e.read().decode('utf-8')}", "bad_request", 64)
            else:
                error_exit(f"Błąd serwera KRS (HTTP {e.code}): {e.read().decode('utf-8')}", "server_error", 69)
        except urllib.error.URLError as e:
            error_exit(f"Błąd połączenia z serwerem KRS: {e.reason}", "network_error", 69)
        except Exception as e:
            error_exit(f"Nieoczekiwany błąd: {str(e)}", "unknown_error", 69)

    error_exit(f"Nie znaleziono podmiotu o numerze KRS {krs_10} w rejestrach P ani S.", "not_found", 2)
    return {}, ""


def format_person_name(item: Any) -> str:
    """Format person name from KRS entry supporting compound surnames and nested dicts."""
    if not isinstance(item, dict):
        return str(item)
    p = item.get("osoba", item)
    if not isinstance(p, dict):
        p = item

    imiona_obj = p.get("imiona", {})
    first = imiona_obj.get("imie", "") if isinstance(imiona_obj, dict) else str(imiona_obj)

    nazwisko_obj = p.get("nazwisko", {})
    if isinstance(nazwisko_obj, dict):
        last = nazwisko_obj.get("nazwiskoICzlon", "")
        if nazwisko_obj.get("nazwiskoIICzlon"):
            last += f"-{nazwisko_obj.get('nazwiskoIICzlon')}"
    else:
        last = str(nazwisko_obj)

    full = f"{first} {last}".strip()
    return full if full else str(item)


def extract_summary(raw_data: Dict[str, Any], register: str) -> Dict[str, Any]:
    """Normalize raw KRS JSON into a structured summary."""
    odpis = raw_data.get("odpis", {})
    naglowek = odpis.get("naglowekA", {})
    dane = odpis.get("dane", {})

    dzial1 = dane.get("dzial1", {})
    dzial2 = dane.get("dzial2", {})
    dzial6 = dane.get("dzial6", {})

    podmiot = dzial1.get("danePodmiotu", {})
    identyfikatory = podmiot.get("identyfikatory", {})
    siedziba_adres = dzial1.get("siedzibaIAdres", {})
    adres = siedziba_adres.get("adres", {})
    siedziba = siedziba_adres.get("siedziba", {})

    kapital_info = dzial1.get("kapital", {}).get("wysokoscKapitaluZakladowego", {})
    kapital_str = None
    if isinstance(kapital_info, dict) and "wartosc" in kapital_info:
        kapital_str = f"{kapital_info.get('wartosc')} {kapital_info.get('waluta', 'PLN')}"

    reprezentacja = dzial2.get("reprezentacja", {})
    sposob_repr = reprezentacja.get("sposobReprezentacji")

    # Zarząd
    sklad_raw = reprezentacja.get("sklad", [])
    board = []
    for m in sklad_raw:
        fn = m.get("funkcjaWOrganie", "Członek organu")
        name = format_person_name(m)
        board.append({"funkcja": fn, "nazwisko": name})

    # Prokurenci
    prokura_obj = dzial2.get("prokurenci") or []
    if isinstance(prokura_obj, dict):
        prokura_raw = prokura_obj.get("sklad", [])
    elif isinstance(prokura_obj, list):
        prokura_raw = prokura_obj
    else:
        prokura_raw = []

    proxies = []
    for p in prokura_raw:
        rodzaj = p.get("rodzajProkury", "Prokura")
        name = format_person_name(p)
        proxies.append({"rodzaj": rodzaj, "nazwisko": name})

    # Rada Nadzorcza / Organ Nadzoru
    organ_nadzoru_obj = dzial2.get("organNadzoru") or []
    supervisory = []
    if isinstance(organ_nadzoru_obj, list):
        for organ in organ_nadzoru_obj:
            organ_nazwa = organ.get("nazwa", "RADA NADZORCZA")
            for s in organ.get("sklad", []):
                fn = s.get("funkcjaWOrganie", organ_nazwa)
                name = format_person_name(s)
                supervisory.append({"organ": organ_nazwa, "funkcja": fn, "nazwisko": name})
    elif isinstance(organ_nadzoru_obj, dict):
        for s in organ_nadzoru_obj.get("sklad", []):
            fn = s.get("funkcjaWOrganie", "Członek organu nadzoru")
            name = format_person_name(s)
            supervisory.append({"organ": "Rada Nadzorcza", "funkcja": fn, "nazwisko": name})

    # Status: likwidacja / upadłość
    in_liquidation = bool(dzial6.get("likwidacja") or dzial6.get("otwarcieLikwidacji"))
    in_bankruptcy = bool(dzial6.get("ogloszenieUpadlosci") or dzial6.get("postepowanieUpadlosciowe"))

    full_addr = f"{adres.get('ulica', '')} {adres.get('nrDomu', '')}".strip()
    if adres.get("nrLokalu"):
        full_addr += f"/{adres.get('nrLokalu')}"
    city_line = f"{adres.get('kodPocztowy', '')} {adres.get('miejscowosc', '')}".strip()

    return {
        "krs": naglowek.get("numerKRS"),
        "rejestr": "Przedsiębiorcy (P)" if register == "P" else "Stowarzyszenia/Fundacje (S)",
        "rejestrKod": register,
        "stanWpisu": naglowek.get("stanWpisu", "Aktualny"),
        "dataOdpisu": naglowek.get("dataOdpisu"),
        "nazwa": podmiot.get("nazwa"),
        "formaPrawna": podmiot.get("formaPrawna"),
        "nip": identyfikatory.get("nip"),
        "regon": identyfikatory.get("regon"),
        "siedziba": siedziba.get("miejscowosc"),
        "adres": {
            "ulica": full_addr,
            "miasto": adres.get("miejscowosc"),
            "kodPocztowy": adres.get("kodPocztowy"),
            "kraj": adres.get("kraj", "POLSKA"),
            "pelny": f"{full_addr}, {city_line}".strip(", "),
        },
        "email": siedziba_adres.get("adresPocztyElektronicznej"),
        "stronaWww": siedziba_adres.get("adresStronyInternetowej"),
        "kapitalZakladowy": kapital_str,
        "sposobReprezentacji": sposob_repr,
        "zarzad": board,
        "zarzadLiczbaOsob": len(board),
        "prokurenci": proxies,
        "radaNadzorcza": supervisory,
        "czyWLikwidacji": in_liquidation,
        "czyWUpadlosci": in_bankruptcy,
    }


def cmd_info(args: argparse.Namespace) -> None:
    krs_10 = sanitize_krs(args.krs)
    data, rej = fetch_odpis(krs_10, "OdpisAktualny", args.rejestr)
    summary = extract_summary(data, rej)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def cmd_representation(args: argparse.Namespace) -> None:
    krs_10 = sanitize_krs(args.krs)
    data, rej = fetch_odpis(krs_10, "OdpisAktualny", args.rejestr)
    summary = extract_summary(data, rej)

    repr_data = {
        "krs": summary["krs"],
        "nazwa": summary["nazwa"],
        "formaPrawna": summary["formaPrawna"],
        "sposobReprezentacji": summary["sposobReprezentacji"],
        "zarzad": summary["zarzad"],
        "prokurenci": summary["prokurenci"],
        "wazneZasady": "Przed podpisaniem umowy zweryfikuj zgodność podpisów ze sposobem reprezentacji.",
    }
    print(json.dumps(repr_data, ensure_ascii=False, indent=2))


def cmd_full(args: argparse.Namespace) -> None:
    krs_10 = sanitize_krs(args.krs)
    typ = "OdpisPelny" if args.history else "OdpisAktualny"
    data, rej = fetch_odpis(krs_10, typ, args.rejestr)
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pobieraj oficjalne odpisy z Krajowego Rejestru Sądowego (KRS) Ministerstwa Sprawiedliwości."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # info
    p_info = subparsers.add_parser("info", help="Zwięzłe podsumowanie spółki (dane rejestrowe, zarząd, kapitał, status)")
    p_info.add_argument("krs", help="Numer KRS spółki (np. 0000006865 lub 6865)")
    p_info.add_argument("--rejestr", choices=["P", "S"], help="Wymuś rejestr: P (Przedsiębiorcy) lub S (Stowarzyszenia)")
    p_info.set_defaults(func=cmd_info)

    # repr
    p_repr = subparsers.add_parser("repr", help="Sposób reprezentacji i uprawnienia do podpisywania umów")
    p_repr.add_argument("krs", help="Numer KRS spółki")
    p_repr.add_argument("--rejestr", choices=["P", "S"], help="Wymuś rejestr: P lub S")
    p_repr.set_defaults(func=cmd_representation)

    # full
    p_full = subparsers.add_parser("full", help="Pobierz pełny odpis JSON z KRS (aktualny lub historyczny)")
    p_full.add_argument("krs", help="Numer KRS spółki")
    p_full.add_argument("--history", action="store_true", help="Pobierz Odpis Pełny z całą historią zmian zamiast Odpisu Aktualnego")
    p_full.add_argument("--rejestr", choices=["P", "S"], help="Wymuś rejestr: P lub S")
    p_full.set_defaults(func=cmd_full)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
