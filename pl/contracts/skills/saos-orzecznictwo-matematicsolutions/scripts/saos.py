#!/usr/bin/env python3
"""SAOS connector - Polish court judgments (System Analizy Orzeczen Sadowych).

Otwarte REST API Fundacji ePanstwo. Bez klucza, bez autoryzacji.
Czesc skilla MateMatic `saos-orzecznictwo`.

Uzycie:
    saos.py search --all "RODO" --court SUPREME --from 2023-01-01 --size 10
    saos.py search --case "I ACa 772/13"
    saos.py search --regulation "ustawa o ochronie danych" --judge Kowalski
    saos.py get 352475                 # pelne orzeczenie (JSON)
    saos.py get 352475 --text          # tylko tresc (textContent)
    saos.py case "I ACa 772/13"        # skrot: szukaj po sygnaturze
    saos.py dump --from 2024-01-01 --to 2024-01-31 --size 100 --page 0

Wyjscie domyslnie: zwiezla tabela tekstowa. Flaga --json -> surowy JSON.
"""
import argparse
import json
import sys
import urllib.parse
import urllib.request

# Windows: konsola domyslnie nie-UTF-8 -> polskie znaki jako mojibake.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

API = "https://www.saos.org.pl/api"
UA = {"User-Agent": "MateMatic-SAOS-connector/1.0", "Accept": "application/json"}


def _fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read().decode("utf-8"))


def search(params):
    """params: dict -> Search API. pageSize wymuszony >=10."""
    params = {k: v for k, v in params.items() if v not in (None, "")}
    if int(params.get("pageSize", 10)) < 10:
        params["pageSize"] = 10
    qs = urllib.parse.urlencode(params)
    return _fetch(f"{API}/search/judgments?{qs}")


def get(jid):
    return _fetch(f"{API}/judgments/{jid}")["data"]


def dump(params):
    params = {k: v for k, v in params.items() if v not in (None, "")}
    if int(params.get("pageSize", 100)) < 10:
        params["pageSize"] = 10
    qs = urllib.parse.urlencode(params)
    return _fetch(f"{API}/dump/judgments?{qs}")


def _sig(item):
    cc = item.get("courtCases") or [{}]
    return cc[0].get("caseNumber", "?")


def print_results(data):
    items = data.get("items", [])
    total = data.get("info", {}).get("totalResults", "?")
    if not items:
        print("Brak wynikow.")
        return
    print(f"Trafienia: {total} (pokazano {len(items)})\n")
    for it in items:
        court = ""
        div = it.get("division") or {}
        court = (div.get("court") or {}).get("name", it.get("courtType", ""))
        snippet = (it.get("textContent") or "").strip().replace("\n", " ")[:160]
        print(f"  [{it['id']}] {_sig(it)}  |  {it.get('judgmentDate','?')}  "
              f"|  {it.get('judgmentType','')}  |  {court}")
        print(f"        https://www.saos.org.pl/judgments/{it['id']}")
        if snippet:
            print(f"        {snippet}...")
        print()
    nxt = next((l["href"] for l in data.get("links", [])
                if l.get("rel") == "next"), None)
    if nxt and len(items) < total:
        print(f"Nastepna strona: dodaj --page <n+1>")


def print_judgment(d, text_only=False):
    if text_only:
        print(d.get("textContent", "").strip())
        return
    print(f"Sygnatura : {_sig(d)}")
    print(f"Typ sadu  : {d.get('courtType')}")
    print(f"Data      : {d.get('judgmentDate')}")
    print(f"Typ       : {d.get('judgmentType')}")
    judges = ", ".join(j.get("name", "") for j in d.get("judges", []))
    print(f"Sklad     : {judges}")
    kw = ", ".join(d.get("keywords", []))
    print(f"Slowa klucz: {kw}")
    src = d.get("source") or {}
    print(f"Oryginal  : {src.get('judgmentUrl', '-')}")
    print(f"SAOS      : https://www.saos.org.pl/judgments/{d.get('id')}")
    summ = (d.get("summary") or "").strip()
    if summ:
        print(f"\nStreszczenie:\n{summ}")
    print(f"\nTresc ({len(d.get('textContent',''))} znakow) - uzyj --text "
          f"po pelna tresc.")


def main():
    p = argparse.ArgumentParser(description="Konektor SAOS - orzecznictwo PL")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="przeszukaj baze orzeczen")
    s.add_argument("--all", help="wyszukiwanie pelnotekstowe")
    s.add_argument("--case", dest="caseNumber", help="sygnatura akt")
    s.add_argument("--court", dest="courtType",
                   help="COMMON|SUPREME|CONSTITUTIONAL_TRIBUNAL|"
                        "NATIONAL_APPEAL_CHAMBER")
    s.add_argument("--type", dest="judgmentTypes",
                   help="DECISION|RESOLUTION|SENTENCE|REGULATION|REASONS")
    s.add_argument("--judge", dest="judgeName", help="nazwisko sedziego")
    s.add_argument("--regulation", dest="referencedRegulation",
                   help="przywolany akt prawny")
    s.add_argument("--legal-base", dest="legalBase", help="podstawa prawna")
    s.add_argument("--keywords", help="slowa kluczowe (tagi SAOS)")
    s.add_argument("--from", dest="judgmentDateFrom", help="data od YYYY-MM-DD")
    s.add_argument("--to", dest="judgmentDateTo", help="data do YYYY-MM-DD")
    s.add_argument("--size", dest="pageSize", type=int, default=10,
                   help="wynikow na strone (10-100)")
    s.add_argument("--page", dest="pageNumber", type=int, default=0)
    s.add_argument("--json", action="store_true", help="surowy JSON")

    g = sub.add_parser("get", help="pobierz pelne orzeczenie po id")
    g.add_argument("id")
    g.add_argument("--text", action="store_true", help="tylko tresc")
    g.add_argument("--json", action="store_true", help="surowy JSON")

    c = sub.add_parser("case", help="szybkie szukanie po sygnaturze")
    c.add_argument("signature")
    c.add_argument("--json", action="store_true")

    d = sub.add_parser("dump", help="hurtowe pobranie bazy")
    d.add_argument("--from", dest="judgmentStartDate")
    d.add_argument("--to", dest="judgmentEndDate")
    d.add_argument("--since", dest="sinceModificationDate",
                   help="aktualizacja przyrostowa YYYY-MM-DD")
    d.add_argument("--size", dest="pageSize", type=int, default=100)
    d.add_argument("--page", dest="pageNumber", type=int, default=0)

    a = p.parse_args()
    try:
        if a.cmd == "search":
            params = {k: v for k, v in vars(a).items()
                      if k not in ("cmd", "json")}
            params.setdefault("sortingField", "JUDGMENT_DATE")
            params.setdefault("sortingDirection", "DESC")
            res = search(params)
            print(json.dumps(res, ensure_ascii=False, indent=2)
                  if a.json else None) if a.json else print_results(res)
        elif a.cmd == "get":
            d_ = get(a.id)
            if a.json:
                print(json.dumps(d_, ensure_ascii=False, indent=2))
            else:
                print_judgment(d_, text_only=a.text)
        elif a.cmd == "case":
            res = search({"caseNumber": a.signature, "pageSize": 10})
            print(json.dumps(res, ensure_ascii=False, indent=2)
                  if a.json else None) if a.json else print_results(res)
        elif a.cmd == "dump":
            params = {k: v for k, v in vars(a).items() if k != "cmd"}
            print(json.dumps(dump(params), ensure_ascii=False, indent=2))
    except urllib.error.HTTPError as e:
        print(f"BLAD HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:300]}",
              file=sys.stderr)
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print(f"BLAD: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
