#!/usr/bin/env python3
"""CLI for Sejm Rzeczypospolitej Polskiej official open data.

Fetches official public data from the Polish Parliament (Sejm RP) API:
- Posłowie (Members of Parliament) details, clubs, districts, committees
- Głosowania (Votings) results, roll-call votes, club breakdown
- Druki sejmowe (Parliamentary prints)
- Proces legislacyjny (Legislative processes and stages)
- Interpelacje poselskie (Interpellations and replies)

Official API: https://api.sejm.gov.pl/
Zero external dependencies (Python 3.8+ standard library only).

Copyright (c) 2026 Michell Hoduń <mhodun@gmail.com> (https://github.com/b44x)
Licensed under the MIT License.
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

API_BASE_URL = "https://api.sejm.gov.pl/sejm"
USER_AGENT = "ai-polish-skills-sejm/1.0.0 (+https://github.com/b44x/ai-polish-skills)"
DEFAULT_TERM = 10

# Embedded terms catalogue (terms 1-10) for fast offline lookup and metadata validation
KNOWN_TERMS = [
    {"num": 1, "from": "1991-11-25", "to": "1993-05-31", "current": False},
    {"num": 2, "from": "1993-10-14", "to": "1997-10-19", "current": False},
    {"num": 3, "from": "1997-10-20", "to": "2001-10-18", "current": False},
    {"num": 4, "from": "2001-10-19", "to": "2005-10-18", "current": False},
    {"num": 5, "from": "2005-10-19", "to": "2007-11-04", "current": False},
    {"num": 6, "from": "2007-11-05", "to": "2011-11-07", "current": False},
    {"num": 7, "from": "2011-11-08", "to": "2015-11-11", "current": False},
    {"num": 8, "from": "2015-11-12", "to": "2019-11-11", "current": False},
    {"num": 9, "from": "2019-11-12", "to": "2023-11-12", "current": False},
    {"num": 10, "from": "2023-11-13", "to": None, "current": True},
]

DIACRITICS_MAP = {
    "ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n",
    "ó": "o", "ś": "s", "ź": "z", "ż": "z",
}


def normalize_search(text: str) -> str:
    """Normalize Polish text for case- and accent-insensitive search."""
    text = text.lower().strip()
    for char, replacement in DIACRITICS_MAP.items():
        text = text.replace(char, replacement)
    return text


def error_exit(message: str, error_type: str = "error", code: int = 64) -> None:
    """Print structured error JSON to stderr and exit."""
    json.dump({"error": message, "type": error_type}, sys.stderr, ensure_ascii=False)
    sys.stderr.write("\n")
    sys.exit(code)


def get_fixtures_path() -> Path:
    """Get path to offline fixtures JSON."""
    return Path(__file__).resolve().parent.parent / "resources" / "fixtures.json"


def load_fixture(fixture_key: str) -> Any:
    """Load sample fixture data for offline contract testing."""
    fpath = get_fixtures_path()
    if not fpath.is_file():
        error_exit(f"Plik danych testowych fixture nie istnieje: {fpath}", "not_found", 2)
    try:
        data = json.loads(fpath.read_text(encoding="utf-8"))
        if fixture_key in data:
            return data[fixture_key]
        error_exit(f"Klucz fixture '{fixture_key}' nie znaleziony w {fpath}", "not_found", 2)
    except Exception as e:
        error_exit(f"Błąd odczytu fixture: {e}", "parse_error", 69)


def fetch_api(endpoint: str, timeout: int = 15) -> Any:
    """Execute GET request against Sejm API."""
    url = f"{API_BASE_URL}/{endpoint.lstrip('/')}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/json",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = resp.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError as e:
        body = ""
        try:
            body = e.read().decode("utf-8")
        except Exception:
            pass

        if e.code == 404:
            error_exit(
                f"Nie znaleziono danych w Sejm API dla podanego zapytania (404 Not Found): {body or url}",
                "not_found",
                2,
            )
        elif e.code == 400:
            error_exit(f"Nieprawidłowe zapytanie do Sejm API (400 Bad Request): {body}", "bad_request", 64)
        else:
            error_exit(f"Błąd serwera Sejmu RP (HTTP {e.code}): {body}", "server_error", 69)
    except urllib.error.URLError as e:
        error_exit(f"Błąd połączenia z serwerem Sejmu RP: {e.reason}", "network_error", 69)
    except json.JSONDecodeError as e:
        error_exit(f"Błąd parsowania JSON z Sejm API: {e}", "parse_error", 69)
    except Exception as e:
        error_exit(f"Nieoczekiwany błąd: {str(e)}", "unknown_error", 69)
    return None


def fetch_mp_committees(term: int, mp_id: int) -> List[Dict[str, Any]]:
    """Fetch committees and find which ones the MP belongs to."""
    try:
        committees_data = fetch_api(f"term{term}/committees", timeout=10)
    except Exception:
        return []

    if not isinstance(committees_data, list):
        return []

    member_committees = []
    for c in committees_data:
        c_code = c.get("code")
        c_name = c.get("name")
        c_type = c.get("type")
        raw_members = c.get("members", [])
        for m in raw_members:
            if m.get("id") == mp_id:
                member_committees.append({
                    "code": c_code,
                    "name": c_name,
                    "type": c_type,
                    "function": m.get("function") or "członek",
                    "joinDate": m.get("joinDate"),
                })
                break
    return member_committees


def cmd_mps(args: argparse.Namespace) -> None:
    """Fetch and search Members of Parliament (Posłowie)."""
    term = args.term or DEFAULT_TERM

    if args.offline:
        fix = load_fixture("mp")
        print(json.dumps({"count": 1, "term": term, "source": "Sejm RP (Fixture)", "mps": [fix]}, ensure_ascii=False, indent=2))
        return

    # Specific MP by ID
    if args.id:
        data = fetch_api(f"term{term}/MP/{args.id}")
        committees = fetch_mp_committees(term, args.id)
        result = {
            "id": data.get("id"),
            "firstLastName": data.get("firstLastName"),
            "firstName": data.get("firstName"),
            "secondName": data.get("secondName"),
            "lastName": data.get("lastName"),
            "club": data.get("club"),
            "districtNum": data.get("districtNum"),
            "districtName": data.get("districtName"),
            "voivodeship": data.get("voivodeship"),
            "email": data.get("email"),
            "birthDate": data.get("birthDate"),
            "birthLocation": data.get("birthLocation"),
            "educationLevel": data.get("educationLevel"),
            "profession": data.get("profession"),
            "active": data.get("active", True),
            "numberOfVotes": data.get("numberOfVotes"),
            "oathDate": data.get("oathDate"),
            "committees": committees,
            "term": term,
            "source": "Kancelaria Sejmu Rzeczypospolitej Polskiej (api.sejm.gov.pl)",
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    # Fetch full list of MPs
    raw_mps = fetch_api(f"term{term}/MP")
    if not isinstance(raw_mps, list):
        error_exit("Otrzymano nieprawidłowy format listy posłów.", "server_error", 69)

    q_search = normalize_search(args.search) if args.search else None
    q_club = normalize_search(args.club) if args.club else None
    q_district = normalize_search(args.district) if args.district else None

    filtered = []
    for mp in raw_mps:
        fl_name = mp.get("firstLastName", "")
        club = mp.get("club", "")
        dist_name = mp.get("districtName", "")

        if q_search and q_search not in normalize_search(fl_name):
            continue
        if q_club and q_club != normalize_search(club):
            continue
        if q_district and q_district not in normalize_search(dist_name):
            continue

        filtered.append({
            "id": mp.get("id"),
            "firstLastName": fl_name,
            "club": club,
            "districtName": dist_name,
            "districtNum": mp.get("districtNum"),
            "voivodeship": mp.get("voivodeship"),
            "email": mp.get("email"),
            "active": mp.get("active", True),
            "profession": mp.get("profession"),
        })

    if args.limit and args.limit > 0:
        filtered = filtered[:args.limit]

    output = {
        "count": len(filtered),
        "totalTermMPs": len(raw_mps),
        "term": term,
        "source": "Kancelaria Sejmu Rzeczypospolitej Polskiej (api.sejm.gov.pl)",
        "mps": filtered,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def cmd_voting(args: argparse.Namespace) -> None:
    """Fetch detailed voting results, roll-call votes, and club summaries."""
    term = args.term or DEFAULT_TERM
    sitting = args.sitting
    num = args.number

    if sitting <= 0 or num <= 0:
        error_exit("Numer posiedzenia i numer głosowania muszą być liczbami dodatnimi.", "bad_request", 64)

    if args.offline:
        fix = load_fixture("voting")
        print(json.dumps(fix, ensure_ascii=False, indent=2))
        return

    data = fetch_api(f"term{term}/votings/{sitting}/{num}")
    if not isinstance(data, dict):
        error_exit("Otrzymano nieprawidłową odpowiedź dla wskazanego głosowania.", "server_error", 69)

    votes_list = data.get("votes", [])

    # Calculate club breakdown
    club_stats: Dict[str, Dict[str, int]] = {}
    for v in votes_list:
        c = v.get("club", "niezrzeszeni")
        v_type = v.get("vote", "UNKNOWN")
        if c not in club_stats:
            club_stats[c] = {"total": 0, "yes": 0, "no": 0, "abstain": 0, "absent": 0, "other": 0}
        club_stats[c]["total"] += 1
        if v_type == "YES":
            club_stats[c]["yes"] += 1
        elif v_type == "NO":
            club_stats[c]["no"] += 1
        elif v_type == "ABSTAIN":
            club_stats[c]["abstain"] += 1
        elif v_type in ("ABSENT", "NOT_PARTICIPATING"):
            club_stats[c]["absent"] += 1
        else:
            club_stats[c]["other"] += 1

    # Filter specific MP vote if requested
    mp_vote = None
    if args.mp:
        q_mp = normalize_search(args.mp)
        for v in votes_list:
            full_n = f"{v.get('firstName', '')} {v.get('lastName', '')}"
            v_mp_id = str(v.get("MP", ""))
            if q_mp == v_mp_id or q_mp in normalize_search(full_n):
                mp_vote = {
                    "id": v.get("MP"),
                    "name": full_n.strip(),
                    "club": v.get("club"),
                    "vote": v.get("vote"),
                }
                break
        if not mp_vote:
            error_exit(f"Nie znaleziono głosu posła '{args.mp}' w tym głosowaniu.", "not_found", 2)

    output = {
        "term": term,
        "sitting": data.get("sitting"),
        "votingNumber": data.get("votingNumber"),
        "date": data.get("date"),
        "title": data.get("title"),
        "topic": data.get("topic") or data.get("description"),
        "totalVoted": data.get("totalVoted"),
        "majorityVotes": data.get("majorityVotes"),
        "majorityType": data.get("majorityType"),
        "results": {
            "yes": data.get("yes"),
            "no": data.get("no"),
            "abstain": data.get("abstain"),
            "notParticipating": data.get("notParticipating"),
        },
        "clubSummary": club_stats,
        "mpVote": mp_vote,
        "source": "Kancelaria Sejmu Rzeczypospolitej Polskiej (api.sejm.gov.pl)",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def cmd_votings(args: argparse.Namespace) -> None:
    """List and search votings on sittings."""
    term = args.term or DEFAULT_TERM
    sitting = args.sitting

    # If sitting not specified, detect the latest proceeding with votings
    if not sitting:
        all_sittings = fetch_api(f"term{term}/votings")
        if isinstance(all_sittings, list) and all_sittings:
            # Pick latest
            latest = all_sittings[-1]
            sitting = latest.get("proceeding") or latest.get("sitting") or 1
        else:
            sitting = 1

    raw_votings = fetch_api(f"term{term}/votings/{sitting}")
    if not isinstance(raw_votings, list):
        error_exit(f"Brak listy głosowań dla posiedzenia {sitting}.", "not_found", 2)

    q_search = normalize_search(args.search) if args.search else None
    results = []
    for v in raw_votings:
        title = v.get("title", "")
        topic = v.get("topic", "") or v.get("description", "")

        if q_search and q_search not in normalize_search(title) and q_search not in normalize_search(topic):
            continue

        results.append({
            "votingNumber": v.get("votingNumber"),
            "date": v.get("date"),
            "title": title,
            "topic": topic,
            "yes": v.get("yes"),
            "no": v.get("no"),
            "abstain": v.get("abstain"),
            "totalVoted": v.get("totalVoted"),
        })

    if args.limit and args.limit > 0:
        results = results[:args.limit]

    output = {
        "term": term,
        "sitting": sitting,
        "count": len(results),
        "source": "Kancelaria Sejmu Rzeczypospolitej Polskiej (api.sejm.gov.pl)",
        "votings": results,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def cmd_prints(args: argparse.Namespace) -> None:
    """Fetch and search parliamentary prints (Druki sejmowe)."""
    term = args.term or DEFAULT_TERM

    # Specific print by number
    if args.number:
        pnum = str(args.number).strip()
        data = fetch_api(f"term{term}/prints/{pnum}")
        output = {
            "term": term,
            "number": data.get("number"),
            "title": data.get("title"),
            "documentDate": data.get("documentDate"),
            "deliveryDate": data.get("deliveryDate"),
            "changeDate": data.get("changeDate"),
            "attachments": data.get("attachments", []),
            "processPrint": data.get("processPrint", []),
            "source": "Kancelaria Sejmu Rzeczypospolitej Polskiej (api.sejm.gov.pl)",
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    raw_prints = fetch_api(f"term{term}/prints")
    if not isinstance(raw_prints, list):
        error_exit("Otrzymano nieprawidłowy format listy druków.", "server_error", 69)

    q_search = normalize_search(args.search) if args.search else None
    results = []
    # Prints are typically returned oldest to newest, reverse to show latest first
    for p in reversed(raw_prints):
        title = p.get("title", "")
        pnum = str(p.get("number", ""))

        if q_search and q_search not in normalize_search(title) and q_search != pnum:
            continue

        results.append({
            "number": pnum,
            "title": title,
            "documentDate": p.get("documentDate"),
            "deliveryDate": p.get("deliveryDate"),
            "attachments": p.get("attachments", []),
        })

        if args.limit and len(results) >= args.limit:
            break

    output = {
        "term": term,
        "count": len(results),
        "totalPrintsInTerm": len(raw_prints),
        "source": "Kancelaria Sejmu Rzeczypospolitej Polskiej (api.sejm.gov.pl)",
        "prints": results,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def cmd_process(args: argparse.Namespace) -> None:
    """Fetch legislative process and stages for a bill or resolution (Proces legislacyjny)."""
    term = args.term or DEFAULT_TERM
    num = str(args.number).strip()

    if args.offline:
        fix = load_fixture("process")
        print(json.dumps(fix, ensure_ascii=False, indent=2))
        return

    data = fetch_api(f"term{term}/processes/{num}")
    if not isinstance(data, dict):
        error_exit(f"Nie znaleziono procesu legislacyjnego dla druku nr {num}.", "not_found", 2)

    stages_raw = data.get("stages", [])
    stages = []
    for s in stages_raw:
        stages.append({
            "date": s.get("date"),
            "stageName": s.get("stageName"),
            "stageType": s.get("stageType"),
            "printNumber": s.get("printNumber"),
            "sitting": s.get("sitting"),
        })

    output = {
        "term": term,
        "number": data.get("number"),
        "title": data.get("title"),
        "titleFinal": data.get("titleFinal"),
        "documentType": data.get("documentType"),
        "processStartDate": data.get("processStartDate"),
        "closureDate": data.get("closureDate"),
        "passed": data.get("passed"),
        "displayAddress": data.get("displayAddress"),
        "stagesCount": len(stages),
        "stages": stages,
        "links": data.get("links", []),
        "source": "Kancelaria Sejmu Rzeczypospolitej Polskiej (api.sejm.gov.pl)",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def cmd_interpellations(args: argparse.Namespace) -> None:
    """Fetch and search interpellations (Interpelacje poselskie)."""
    term = args.term or DEFAULT_TERM

    # Specific interpellation by number
    if args.number:
        inum = args.number
        data = fetch_api(f"term{term}/interpellations/{inum}")
        output = {
            "term": term,
            "number": data.get("num"),
            "title": data.get("title"),
            "receiptDate": data.get("receiptDate"),
            "sentDate": data.get("sentDate"),
            "fromMpIds": data.get("from", []),
            "toRecipients": data.get("to", []),
            "repliesCount": len(data.get("replies", [])),
            "replies": [
                {
                    "from": r.get("from"),
                    "receiptDate": r.get("receiptDate"),
                    "lastModified": r.get("lastModified"),
                }
                for r in data.get("replies", [])
            ],
            "links": data.get("links", []),
            "source": "Kancelaria Sejmu Rzeczypospolitej Polskiej (api.sejm.gov.pl)",
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    # List with optional query params
    params = []
    if args.mp_id:
        params.append(f"from={args.mp_id}")
    limit = args.limit or 50
    params.append(f"limit={min(limit * 2 if args.search else limit, 200)}")

    query_str = "?" + "&".join(params) if params else ""
    raw_list = fetch_api(f"term{term}/interpellations{query_str}")
    if not isinstance(raw_list, list):
        error_exit("Otrzymano nieprawidłowy format listy interpelacji.", "server_error", 69)

    q_search = normalize_search(args.search) if args.search else None
    results = []
    for it in raw_list:
        title = it.get("title", "")
        if q_search and q_search not in normalize_search(title):
            continue

        results.append({
            "number": it.get("num"),
            "title": title,
            "receiptDate": it.get("receiptDate"),
            "sentDate": it.get("sentDate"),
            "fromMpIds": it.get("from", []),
            "toRecipients": it.get("to", []),
            "repliesCount": len(it.get("replies", [])),
        })
        if args.limit and len(results) >= args.limit:
            break

    output = {
        "term": term,
        "count": len(results),
        "source": "Kancelaria Sejmu Rzeczypospolitej Polskiej (api.sejm.gov.pl)",
        "interpellations": results,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def cmd_terms(args: argparse.Namespace) -> None:
    """Fetch or display Sejm terms catalogue (supports offline)."""
    if args.offline:
        data = KNOWN_TERMS
    else:
        try:
            data = fetch_api("term", timeout=6)
        except Exception:
            data = KNOWN_TERMS

    output = {
        "count": len(data),
        "currentTerm": 10,
        "terms": data,
        "source": "Kancelaria Sejmu Rzeczypospolitej Polskiej (api.sejm.gov.pl)",
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Oficjalne dane Sejmu Rzeczypospolitej Polskiej (posłowie, głosowania, druki, proces legislacyjny, interpelacje)."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # mp / mps
    p_mp = subparsers.add_parser("mps", aliases=["mp"], help="Baza posłów: wyszukiwanie, okręgi, kluby, komisje")
    p_mp.add_argument("--id", type=int, help="Identyfikator posła (zwraca pełne szczegóły i komisje)")
    p_mp.add_argument("--search", help="Szukaj posła po imieniu lub nazwisku")
    p_mp.add_argument("--club", help="Filtruj wg klubu lub koła (np. PiS, KO, Polska2050, Konfederacja, Lewica)")
    p_mp.add_argument("--district", help="Filtruj wg okręgu wyborczego (np. Gdańsk, Warszawa, Kraków)")
    p_mp.add_argument("--limit", type=int, default=50, help="Maksymalna liczba wyników (domyślnie 50)")
    p_mp.add_argument("--term", type=int, default=DEFAULT_TERM, help=f"Numer kadencji Sejmu (domyślnie {DEFAULT_TERM})")
    p_mp.add_argument("--offline", action="store_true", help="Tryb testowy offline (zwraca dane testowe fixture)")
    p_mp.set_defaults(func=cmd_mps)

    # voting
    p_voting = subparsers.add_parser("voting", help="Szczegóły pojedynczego głosowania i wyniki imienne")
    p_voting.add_argument("sitting", type=int, help="Numer posiedzenia Sejmu")
    p_voting.add_argument("number", type=int, help="Numer głosowania na danym posiedzeniu")
    p_voting.add_argument("--mp", help="Sprawdź jak głosował konkretny poseł (imię, nazwisko lub ID)")
    p_voting.add_argument("--term", type=int, default=DEFAULT_TERM, help=f"Numer kadencji Sejmu (domyślnie {DEFAULT_TERM})")
    p_voting.add_argument("--offline", action="store_true", help="Tryb testowy offline (zwraca dane testowe fixture)")
    p_voting.set_defaults(func=cmd_voting)

    # votings
    p_votings = subparsers.add_parser("votings", help="Lista głosowań na danym posiedzeniu Sejmu")
    p_votings.add_argument("--sitting", type=int, help="Numer posiedzenia Sejmu (domyślnie ostatnie posiedzenie)")
    p_votings.add_argument("--search", help="Filtruj głosowania po tytule lub temacie")
    p_votings.add_argument("--limit", type=int, default=30, help="Maksymalna liczba głosowań (domyślnie 30)")
    p_votings.add_argument("--term", type=int, default=DEFAULT_TERM, help=f"Numer kadencji Sejmu (domyślnie {DEFAULT_TERM})")
    p_votings.set_defaults(func=cmd_votings)

    # prints
    p_prints = subparsers.add_parser("prints", aliases=["print"], help="Druki sejmowe (projekty ustaw, uchwał, sprawozdania)")
    p_prints.add_argument("--number", help="Numer druku (np. 1)")
    p_prints.add_argument("--search", help="Szukaj w tytule druku")
    p_prints.add_argument("--limit", type=int, default=20, help="Maksymalna liczba wyników (domyślnie 20)")
    p_prints.add_argument("--term", type=int, default=DEFAULT_TERM, help=f"Numer kadencji Sejmu (domyślnie {DEFAULT_TERM})")
    p_prints.set_defaults(func=cmd_prints)

    # process
    p_proc = subparsers.add_parser("process", help="Przebieg procesu legislacyjnego i etapy prac nad drukiem/ustawą")
    p_proc.add_argument("number", help="Numer druku procesu legislacyjnego (np. 1)")
    p_proc.add_argument("--term", type=int, default=DEFAULT_TERM, help=f"Numer kadencji Sejmu (domyślnie {DEFAULT_TERM})")
    p_proc.add_argument("--offline", action="store_true", help="Tryb testowy offline (zwraca dane testowe fixture)")
    p_proc.set_defaults(func=cmd_process)

    # interpellations
    p_interp = subparsers.add_parser("interpellations", aliases=["interpellation"], help="Interpelacje poselskie i odpowiedzi")
    p_interp.add_argument("--number", type=int, help="Numer interpelacji")
    p_interp.add_argument("--mp-id", type=int, help="Filtruj interpelacje wg ID posła-autora")
    p_interp.add_argument("--search", help="Filtruj po słowach kluczowych w tytule interpelacji")
    p_interp.add_argument("--limit", type=int, default=20, help="Maksymalna liczba wyników (domyślnie 20)")
    p_interp.add_argument("--term", type=int, default=DEFAULT_TERM, help=f"Numer kadencji Sejmu (domyślnie {DEFAULT_TERM})")
    p_interp.set_defaults(func=cmd_interpellations)

    # terms
    p_terms = subparsers.add_parser("terms", help="Wykaz kadencji Sejmu RP (od I do X)")
    p_terms.add_argument("--offline", action="store_true", help="Zwróć wbudowany katalog kadencji offline")
    p_terms.set_defaults(func=cmd_terms)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
