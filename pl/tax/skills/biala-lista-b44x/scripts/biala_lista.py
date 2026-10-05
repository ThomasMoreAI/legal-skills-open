#!/usr/bin/env python3
"""CLI for Polish Ministry of Finance White List of VAT Taxpayers (Biała Lista Podatników VAT).

Official API docs: https://www.gov.pl/web/kas/api-wykazu-podatnikow-vat
No external dependencies required (Python 3.8+ stdlib only).

Copyright (c) 2026 Michell Hoduń <mhodun@gmail.com> (https://github.com/b44x)
Licensed under the MIT License.
"""

import argparse
import datetime
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional, Tuple

API_BASE_URL = "https://wl-api.mf.gov.pl/api"
USER_AGENT = "ai-polish-skills-biala-lista/1.0.0 (+https://github.com/b44x/ai-polish-skills)"

# Polish Bank Identifiers (digits 3..6 of NRB / digits 0..4 of BBAN)
POLISH_BANKS: Dict[str, str] = {
    "1010": "Narodowy Bank Polski",
    "1020": "PKO Bank Polski",
    "1030": "Citi Handlowy",
    "1050": "ING Bank Śląski",
    "1060": "BPH",
    "1090": "Santander Bank Polska",
    "1130": "Bank Gospodarstwa Krajowego (BGK)",
    "1140": "mBank",
    "1160": "Bank Millennium",
    "1240": "Bank Pekao SA",
    "1320": "Bank Pocztowy",
    "1470": "Euro Bank",
    "1540": "BOŚ Bank",
    "1580": "Mercedes-Benz Bank Polska",
    "1600": "BNP Paribas Bank Polska",
    "1610": "SGB-Bank",
    "1670": "RBS Bank (Polska)",
    "1680": "Plus Bank",
    "1840": "Societe Generale",
    "1870": "Nest Bank",
    "1910": "Deutsche Bank Polska",
    "1930": "Bank Polskiej Spółdzielczości (BPS)",
    "1940": "Credit Agricole",
    "2030": "BNP Paribas",
    "2120": "Santander Consumer Bank",
    "2160": "Toyota Bank",
    "2190": "DNB Bank Polska",
    "2480": "Alior Bank",
    "2490": "Alior Bank",
    "2770": "Volkswagen Bank",
    "2800": "Aion Bank",
}


def error_exit(message: str, error_type: str = "error", code: int = 64) -> None:
    """Print error JSON to stderr and exit."""
    json.dump({"error": message, "type": error_type}, sys.stderr, ensure_ascii=False)
    sys.stderr.write("\n")
    sys.exit(code)


def sanitize_digits(val: str) -> str:
    """Strip spaces, dashes, dots, and optional country prefix."""
    s = val.strip().replace(" ", "").replace("-", "").replace(".", "")
    if s.upper().startswith("PL"):
        s = s[2:]
    return s


def validate_nip(nip: str) -> Tuple[bool, Optional[str]]:
    """Validate Polish NIP (Tax Identification Number, 10 digits)."""
    digits = sanitize_digits(nip)
    if not digits.isdigit():
        return False, "NIP musi zawierać wyłącznie cyfry."
    if len(digits) != 10:
        return False, f"NIP musi mieć 10 cyfr (podano {len(digits)})."

    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    checksum = sum(int(digits[i]) * weights[i] for i in range(9)) % 11
    if checksum == 10 or checksum != int(digits[9]):
        return False, "Nieprawidłowa suma kontrolna NIP."
    return True, None


def format_nip(nip: str) -> str:
    """Format 10-digit NIP as XXX-XXX-XX-XX."""
    d = sanitize_digits(nip)
    if len(d) == 10:
        return f"{d[:3]}-{d[3:6]}-{d[6:8]}-{d[8:]}"
    return nip


def validate_regon(regon: str) -> Tuple[bool, Optional[str]]:
    """Validate Polish REGON (9 or 14 digits)."""
    digits = sanitize_digits(regon)
    if not digits.isdigit():
        return False, "REGON musi zawierać wyłącznie cyfry."
    if len(digits) not in (9, 14):
        return False, f"REGON musi mieć 9 lub 14 cyfr (podano {len(digits)})."

    if len(digits) == 9:
        weights = [8, 9, 2, 3, 4, 5, 6, 7]
        checksum = sum(int(digits[i]) * weights[i] for i in range(8)) % 11
        control = 0 if checksum == 10 else checksum
        if control != int(digits[8]):
            return False, "Nieprawidłowa suma kontrolna REGON (9 cyfr)."
    else:
        # First 9 digits must also form a valid 9-digit REGON
        valid_first_9, err = validate_regon(digits[:9])
        if not valid_first_9:
            return False, f"Błąd w pierwszych 9 cyfrach REGON: {err}"
        weights = [2, 4, 8, 5, 0, 9, 7, 3, 6, 1, 2, 4, 8]
        checksum = sum(int(digits[i]) * weights[i] for i in range(13)) % 11
        control = 0 if checksum == 10 else checksum
        if control != int(digits[13]):
            return False, "Nieprawidłowa suma kontrolna REGON (14 cyfr)."
    return True, None


def validate_iban(account: str) -> Tuple[bool, Optional[str]]:
    """Validate Polish Bank Account Number (NRB / IBAN, 26 digits)."""
    digits = sanitize_digits(account)
    if not digits.isdigit():
        return False, "Numer rachunku musi zawierać wyłącznie cyfry."
    if len(digits) != 26:
        return False, f"Polski numer rachunku (NRB) musi mieć 26 cyfr (podano {len(digits)})."

    # Polish IBAN control digits check: BBAN (24 digits) + 2521 (PL) + CC (2 control digits) % 97 == 1
    bban = digits[2:]
    cc = digits[:2]
    converted = bban + "2521" + cc
    if int(converted) % 97 != 1:
        return False, "Nieprawidłowa suma kontrolna rachunku bankowego (modulo 97)."
    return True, None


def format_iban(account: str) -> str:
    """Format 26-digit account into standard Polish 2 4 4 4 4 4 4 format."""
    d = sanitize_digits(account)
    if len(d) == 26:
        return f"{d[:2]} {d[2:6]} {d[6:10]} {d[10:14]} {d[14:18]} {d[18:22]} {d[22:]}"
    return account


def get_bank_name(account: str) -> Optional[str]:
    """Identify bank name from the 4-digit bank routing code (digits 3..6)."""
    d = sanitize_digits(account)
    if len(d) >= 6:
        bank_code = d[2:6]
        return POLISH_BANKS.get(bank_code, "Nieznany bank / bank spółdzielczy")
    return None


def fetch_api(endpoint: str, params: Dict[str, str]) -> Dict[str, Any]:
    """Execute GET request against the MF White List API."""
    qs = urllib.parse.urlencode(params)
    url = f"{API_BASE_URL}/{endpoint}?{qs}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        try:
            err_json = json.loads(body)
            msg = err_json.get("message") or err_json.get("code") or body
        except Exception:
            msg = body
        if e.code == 404:
            error_exit(f"Nie znaleziono danych w Wykazie podatników VAT: {msg}", "not_found", 2)
        elif e.code == 400:
            error_exit(f"Błąd zapytania Ministerstwa Finansów: {msg}", "bad_request", 64)
        elif e.code == 429:
            error_exit(
                "Przekroczono limit zapytań do API Ministerstwa Finansów (300 zapytań/dzień).",
                "rate_limit",
                69,
            )
        else:
            error_exit(
                f"Błąd serwera Ministerstwa Finansów (HTTP {e.code}): {msg}",
                "server_error",
                69,
            )
    except urllib.error.URLError as e:
        error_exit(
            f"Błąd połączenia z serwerem Ministerstwa Finansów: {e.reason}",
            "network_error",
            69,
        )
    except Exception as e:
        error_exit(f"Nieoczekiwany błąd: {str(e)}", "unknown_error", 69)
    return {}


def format_subject(subject: Dict[str, Any], meta: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize subject (company) data to clean JSON."""
    raw_nip = subject.get("nip") or ""
    account_numbers = subject.get("accountNumbers") or []
    formatted_accounts = [
        {
            "raw": acc,
            "formatted": format_iban(acc),
            "bank": get_bank_name(acc),
        }
        for acc in account_numbers
    ]

    return {
        "name": subject.get("name"),
        "nip": raw_nip,
        "nipFormatted": format_nip(raw_nip) if raw_nip else None,
        "statusVat": subject.get("statusVat"),
        "isVatActive": (subject.get("statusVat") or "").lower() == "czynny",
        "regon": subject.get("regon"),
        "krs": subject.get("krs"),
        "pesel": subject.get("pesel"),
        "residenceAddress": subject.get("residenceAddress"),
        "workingAddress": subject.get("workingAddress"),
        "registrationLegalDate": subject.get("registrationLegalDate"),
        "hasVirtualAccounts": subject.get("hasVirtualAccounts", False),
        "accountCount": len(account_numbers),
        "accounts": formatted_accounts,
        "representatives": subject.get("representatives") or [],
        "authorizedClerks": subject.get("authorizedClerks") or [],
        "partners": subject.get("partners") or [],
        "registrationDenialDate": subject.get("registrationDenialDate"),
        "registrationDenialBasis": subject.get("registrationDenialBasis"),
        "restorationDate": subject.get("restorationDate"),
        "restorationBasis": subject.get("restorationBasis"),
        "removalDate": subject.get("removalDate"),
        "removalBasis": subject.get("removalBasis"),
        "requestId": meta.get("requestId"),
        "requestDateTime": meta.get("requestDateTime"),
    }


def cmd_nip(args: argparse.Namespace) -> None:
    nip = sanitize_digits(args.nip)
    valid, err = validate_nip(nip)
    if not valid:
        error_exit(f"Błędny NIP '{args.nip}': {err}", "validation_error", 64)

    date_str = args.date or datetime.date.today().isoformat()
    raw = fetch_api(f"search/nip/{nip}", {"date": date_str})
    result = raw.get("result", {})
    subject = result.get("subject")
    if not subject:
        error_exit(f"Podmiot o NIP {nip} nie figuruje w wykazie na dzień {date_str}.", "not_found", 2)

    data = format_subject(
        subject,
        {
            "requestId": result.get("requestId"),
            "requestDateTime": result.get("requestDateTime"),
        },
    )
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_regon(args: argparse.Namespace) -> None:
    regon = sanitize_digits(args.regon)
    valid, err = validate_regon(regon)
    if not valid:
        error_exit(f"Błędny REGON '{args.regon}': {err}", "validation_error", 64)

    date_str = args.date or datetime.date.today().isoformat()
    raw = fetch_api(f"search/regon/{regon}", {"date": date_str})
    result = raw.get("result", {})
    subject = result.get("subject")
    if not subject:
        error_exit(
            f"Podmiot o REGON {regon} nie figuruje w wykazie na dzień {date_str}.",
            "not_found",
            2,
        )

    data = format_subject(
        subject,
        {
            "requestId": result.get("requestId"),
            "requestDateTime": result.get("requestDateTime"),
        },
    )
    print(json.dumps(data, ensure_ascii=False, indent=2))


def cmd_account(args: argparse.Namespace) -> None:
    account = sanitize_digits(args.account)
    valid, err = validate_iban(account)
    if not valid:
        error_exit(f"Błędny numer rachunku '{args.account}': {err}", "validation_error", 64)

    date_str = args.date or datetime.date.today().isoformat()
    raw = fetch_api(f"search/bank-account/{account}", {"date": date_str})
    result = raw.get("result", {})
    subjects = result.get("subjects") or []
    if not subjects:
        error_exit(
            f"Rachunek {format_iban(account)} nie figuruje w wykazie na dzień {date_str}.",
            "not_found",
            2,
        )

    meta = {
        "requestId": result.get("requestId"),
        "requestDateTime": result.get("requestDateTime"),
    }
    output = {
        "account": account,
        "accountFormatted": format_iban(account),
        "bank": get_bank_name(account),
        "subjects": [format_subject(s, meta) for s in subjects],
        "requestId": meta["requestId"],
        "requestDateTime": meta["requestDateTime"],
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def cmd_check(args: argparse.Namespace) -> None:
    nip = sanitize_digits(args.nip)
    nip_valid, nip_err = validate_nip(nip)
    if not nip_valid:
        error_exit(f"Błędny NIP '{args.nip}': {nip_err}", "validation_error", 64)

    account = sanitize_digits(args.account)
    acc_valid, acc_err = validate_iban(account)
    if not acc_valid:
        error_exit(f"Błędny rachunek '{args.account}': {acc_err}", "validation_error", 64)

    date_str = args.date or datetime.date.today().isoformat()
    raw = fetch_api(f"check/nip/{nip}/bank-account/{account}", {"date": date_str})
    result = raw.get("result", {})
    assigned_str = result.get("accountAssigned", "NIE")
    is_assigned = assigned_str.upper() == "TAK"

    output = {
        "nip": nip,
        "nipFormatted": format_nip(nip),
        "account": account,
        "accountFormatted": format_iban(account),
        "bank": get_bank_name(account),
        "accountAssigned": assigned_str,
        "isAssigned": is_assigned,
        "date": date_str,
        "requestId": result.get("requestId"),
        "requestDateTime": result.get("requestDateTime"),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def cmd_validate(args: argparse.Namespace) -> None:
    val = args.value.strip()
    digits = sanitize_digits(val)

    res: Dict[str, Any] = {
        "input": val,
        "digits": digits,
        "length": len(digits),
        "valid": False,
        "type": "unknown",
        "formatted": None,
        "message": None,
    }

    if len(digits) == 10:
        valid, err = validate_nip(digits)
        res["type"] = "nip"
        res["valid"] = valid
        res["formatted"] = format_nip(digits) if valid else None
        res["message"] = "Poprawny NIP" if valid else err
    elif len(digits) in (9, 14):
        valid, err = validate_regon(digits)
        res["type"] = f"regon_{len(digits)}"
        res["valid"] = valid
        res["formatted"] = digits if valid else None
        res["message"] = f"Poprawny REGON ({len(digits)} cyfr)" if valid else err
    elif len(digits) == 26:
        valid, err = validate_iban(digits)
        res["type"] = "iban_pl"
        res["valid"] = valid
        res["formatted"] = format_iban(digits) if valid else None
        res["bank"] = get_bank_name(digits)
        res["message"] = f"Poprawny rachunek bankowy ({res['bank']})" if valid else err
    else:
        res["message"] = (
            f"Nierozpoznana długość ({len(digits)} cyfr). Oczekiwano: NIP (10), "
            "REGON (9/14) lub NRB (26 cyfr)."
        )

    print(json.dumps(res, ensure_ascii=False, indent=2))
    if not res["valid"]:
        sys.exit(64)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sprawdź podmiot w Wykazie podatników VAT Ministerstwa Finansów (Biała Lista VAT)."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # nip
    p_nip = subparsers.add_parser("nip", help="Wyszukaj podmiot po numerze NIP")
    p_nip.add_argument("nip", help="Numer NIP (10 cyfr, kreski dozwolone)")
    p_nip.add_argument("--date", help="Data weryfikacji w formacie RRRR-MM-DD (domyślnie dziś)")
    p_nip.set_defaults(func=cmd_nip)

    # regon
    p_regon = subparsers.add_parser("regon", help="Wyszukaj podmiot po numerze REGON")
    p_regon.add_argument("regon", help="Numer REGON (9 lub 14 cyfr)")
    p_regon.add_argument("--date", help="Data weryfikacji w formacie RRRR-MM-DD (domyślnie dziś)")
    p_regon.set_defaults(func=cmd_regon)

    # account
    p_account = subparsers.add_parser("account", help="Wyszukaj podmiot po numerze konta bankowego")
    p_account.add_argument("account", help="Polski numer rachunku bankowego (26 cyfr, PL dozwolone)")
    p_account.add_argument("--date", help="Data weryfikacji w formacie RRRR-MM-DD (domyślnie dziś)")
    p_account.set_defaults(func=cmd_account)

    # check
    p_check = subparsers.add_parser(
        "check", help="Sprawdź, czy numer rachunku jest przypisany do podmiotu o danym NIP"
    )
    p_check.add_argument("nip", help="Numer NIP kontrahenta")
    p_check.add_argument("account", help="Numer rachunku bankowego (26 cyfr)")
    p_check.add_argument("--date", help="Data weryfikacji w formacie RRRR-MM-DD (domyślnie dziś)")
    p_check.set_defaults(func=cmd_check)

    # validate
    p_val = subparsers.add_parser(
        "validate", help="Matematyczna walidacja sumy kontrolnej NIP, REGON lub rachunku (offline)"
    )
    p_val.add_argument("value", help="Wartość do sprawdzenia (NIP, REGON lub NRB)")
    p_val.set_defaults(func=cmd_validate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
