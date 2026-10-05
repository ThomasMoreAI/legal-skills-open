#!/usr/bin/env python3
"""CLI for Polish legal acts from the official ELI API of the Sejm (Dziennik Ustaw, Monitor Polski).

- search: find acts by title words, type, year, in-force status
- act: status, consolidated texts (teksty jednolite), amendments with entry-into-force dates
- article: the wording of one article, always with its source document and freshness info
- codes: offline list of shortcuts for the most used codes and statutes

The API serves HTML only for some documents: newer consolidated texts are often PDF-only,
and the HTML of an amended act is its ORIGINAL wording. `article` therefore reads the newest
consolidated text that has HTML and reports every amendment in force after that date.

Official API: https://api.sejm.gov.pl/eli
Zero external dependencies (Python 3.8+ standard library only).

Copyright (c) 2026 Michell Hoduń <mhodun@gmail.com> (https://github.com/b44x)
Licensed under the MIT License.
"""

import argparse
import datetime
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from typing import Any, Dict, List, Optional, Tuple

API_BASE_URL = "https://api.sejm.gov.pl/eli"
USER_AGENT = "ai-polish-skills-prawo/1.0.0 (+https://github.com/b44x/ai-polish-skills)"
SOURCE = "Kancelaria Sejmu RP — Internetowy System Aktów Prawnych (api.sejm.gov.pl/eli)"
MAX_TEXT_CHARS = 8000

# Shortcuts verified against the ELI API (publisher/year/position of the ORIGINAL act).
CODES: Dict[str, Tuple[str, str, List[str]]] = {
    "konstytucja": ("DU/1997/483", "Konstytucja Rzeczypospolitej Polskiej", ["konstytucja rp"]),
    "kp": ("DU/1974/141", "Kodeks pracy", ["kodeks pracy"]),
    "kc": ("DU/1964/93", "Kodeks cywilny", ["kodeks cywilny"]),
    "kpc": ("DU/1964/296", "Kodeks postępowania cywilnego", ["kodeks postepowania cywilnego"]),
    "kk": ("DU/1997/553", "Kodeks karny", ["kodeks karny"]),
    "kpk": ("DU/1997/555", "Kodeks postępowania karnego", ["kodeks postepowania karnego"]),
    "kks": ("DU/1999/930", "Kodeks karny skarbowy", ["kodeks karny skarbowy"]),
    "ksh": ("DU/2000/1037", "Kodeks spółek handlowych", ["kodeks spolek handlowych"]),
    "kpa": ("DU/1960/168", "Kodeks postępowania administracyjnego", ["kodeks postepowania administracyjnego"]),
    "kro": ("DU/1964/59", "Kodeks rodzinny i opiekuńczy", ["kodeks rodzinny", "kodeks rodzinny i opiekunczy"]),
    "kw": ("DU/1971/114", "Kodeks wykroczeń", ["kodeks wykroczen"]),
    "kodeks-wyborczy": ("DU/2011/112", "Kodeks wyborczy", ["kodeks wyborczy"]),
    "op": ("DU/1997/926", "Ordynacja podatkowa", ["ordynacja podatkowa"]),
    "vat": ("DU/2004/535", "Ustawa o podatku od towarów i usług", ["ustawa o vat", "podatek od towarow i uslug"]),
    "pit": ("DU/1991/350", "Ustawa o podatku dochodowym od osób fizycznych", ["ustawa o pit"]),
    "cit": ("DU/1992/86", "Ustawa o podatku dochodowym od osób prawnych", ["ustawa o cit"]),
    "zus": ("DU/1998/887", "Ustawa o systemie ubezpieczeń społecznych", ["ubezpieczenia spoleczne"]),
    "prawo-przedsiebiorcow": ("DU/2018/646", "Prawo przedsiębiorców", ["prawo przedsiebiorcow"]),
    "prawa-konsumenta": ("DU/2014/827", "Ustawa o prawach konsumenta", ["prawa konsumenta"]),
    "prawo-budowlane": ("DU/1994/414", "Prawo budowlane", ["prawo budowlane"]),
    "ruch-drogowy": ("DU/1997/602", "Prawo o ruchu drogowym", ["prawo o ruchu drogowym", "kodeks drogowy"]),
    "ochrona-danych": ("DU/2018/1000", "Ustawa o ochronie danych osobowych", ["rodo", "ochrona danych osobowych"]),
}

SUPERSCRIPTS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")


def error_exit(message: str, error_type: str = "error", code: int = 64) -> None:
    """Print structured error JSON to stderr and exit."""
    json.dump({"error": message, "type": error_type}, sys.stderr, ensure_ascii=False)
    sys.stderr.write("\n")
    sys.exit(code)


def fold(text: str) -> str:
    """Lowercase and strip Polish diacritics for matching."""
    table = str.maketrans("ąćęłńóśźżĄĆĘŁŃÓŚŹŻ", "acelnoszzACELNOSZZ")
    return " ".join(text.translate(table).lower().split())


def http_get(path: str, as_json: bool = True, timeout: int = 20) -> Any:
    """GET from the ELI API; exits with the repository's exit-code contract on failure."""
    url = f"{API_BASE_URL}/{path.lstrip('/')}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json, text/html"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            return json.loads(body) if as_json else body
    except urllib.error.HTTPError as e:
        if e.code == 404:
            error_exit(f"Nie znaleziono w API ELI: {url}", "not_found", 2)
        if e.code == 400:
            error_exit(f"Nieprawidłowe zapytanie do API ELI (400): {url}", "bad_request", 64)
        error_exit(f"Błąd serwera API ELI (HTTP {e.code})", "server_error", 69)
    except urllib.error.URLError as e:
        error_exit(f"Błąd połączenia z API ELI: {e.reason}", "network_error", 69)
    except json.JSONDecodeError as e:
        error_exit(f"Nieprawidłowa odpowiedź JSON z API ELI: {e}", "parse_error", 69)
    except Exception as e:  # noqa: BLE001 - keep the CLI contract on unexpected failures
        error_exit(f"Nieoczekiwany błąd: {e}", "unknown_error", 69)
    return None


# --------------------------------------------------------------------------- references

def parse_ref(raw: str) -> str:
    """Normalise an act reference to 'DU/2023/1465'.

    Accepts a shortcut (kp, vat…), 'DU/2023/1465', 'MP/2024/10', 'Dz.U. 2023 poz. 1465',
    'Dz.U. 1974 nr 24 poz. 141', 'M.P. 2024 poz. 10' or an ISAP address 'WDU20230001465'.
    """
    text = raw.strip()
    key = fold(text)
    for code, (ref, _name, aliases) in CODES.items():
        if key == code or key in aliases:
            return ref
    m = re.fullmatch(r"(DU|MP)\s*/\s*(\d{4})\s*/\s*(\d+)", text, re.I)
    if m:
        return f"{m.group(1).upper()}/{m.group(2)}/{int(m.group(3))}"
    m = re.fullmatch(r"([WM])(DU|MP)?(\d{4})(\d{3})(\d{4})", text.upper())
    if m and text.upper().startswith(("WDU", "WMP")):
        return f"{text[1:3].upper()}/{m.group(3)}/{int(m.group(5))}"
    m = re.search(r"(Dz\.?\s*U\.?|M\.?\s*P\.?)\s*(?:z\s*)?(\d{4})\s*(?:r\.?)?\s*(?:,?\s*nr\s*\d+)?\s*,?\s*poz\.?\s*(\d+)", text, re.I)
    if m:
        pub = "DU" if m.group(1).upper().startswith("D") else "MP"
        return f"{pub}/{m.group(2)}/{int(m.group(3))}"
    error_exit(
        f"Nie rozpoznano aktu '{raw}'. Użyj skrótu (np. kp, vat — lista: codes), "
        "adresu 'DU/2023/1465' lub 'Dz.U. 2023 poz. 1465'.",
        "bad_request",
        64,
    )
    return ""


def ref_parts(ref: str) -> Tuple[str, int, int]:
    pub, year, pos = ref.split("/")
    return pub, int(year), int(pos)


def links(ref: str, address: Optional[str] = None) -> Dict[str, str]:
    out = {"eli": f"{API_BASE_URL}/acts/{ref}", "pdf": f"{API_BASE_URL}/acts/{ref}/text.pdf"}
    if address:
        out["isap"] = f"https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id={address}"
    return out


def get_act(ref: str) -> Dict[str, Any]:
    return http_get(f"acts/{ref}")


def consolidated_refs(act: Dict[str, Any]) -> List[str]:
    """Consolidated texts (teksty jednolite) of an act, newest first."""
    refs = [r["id"] for r in act.get("references", {}).get("Inf. o tekście jednolitym", []) if r.get("id")]
    return sorted(set(refs), key=ref_parts, reverse=True)


def amendments(act: Dict[str, Any]) -> List[Dict[str, str]]:
    """Amending acts with their entry-into-force dates, newest first."""
    items = [
        {"ref": r["id"], "entryIntoForce": r.get("date")}
        for r in act.get("references", {}).get("Akty zmieniające", [])
        if r.get("id")
    ]
    return sorted(items, key=lambda x: (x["entryIntoForce"] or "", ref_parts(x["ref"])), reverse=True)


def brief(act: Dict[str, Any]) -> Dict[str, Any]:
    ref = f"{act.get('publisher')}/{act.get('year')}/{act.get('pos')}"
    return {
        "ref": ref,
        "displayAddress": act.get("displayAddress"),
        "title": act.get("title"),
        "type": act.get("type"),
        "status": act.get("status"),
        "announcementDate": act.get("announcementDate"),
        "promulgation": act.get("promulgation"),
        "textHTML": act.get("textHTML"),
        "textPDF": act.get("textPDF"),
    }


# --------------------------------------------------------------------------- article extraction

BLOCK_TAGS = {"div", "p", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6", "table", "tr", "section", "article"}
VOID_TAGS = {"br", "img", "hr", "meta", "link", "input", "wbr", "col", "area", "base", "source"}


class ArticleParser(HTMLParser):
    """Collect the text of every element whose data-id equals the wanted article id."""

    def __init__(self, data_id: str) -> None:
        super().__init__(convert_charrefs=True)
        self.data_id = data_id
        self.found: List[Dict[str, Any]] = []
        self.depth = 0
        self.current: Optional[Dict[str, Any]] = None
        self.skip = 0

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        if self.skip:
            if tag not in VOID_TAGS:
                self.skip += 1
            return
        if tag in VOID_TAGS:
            if self.current is not None and tag == "br":
                self.current["parts"].append("\n")
            return
        a = dict(attrs)
        if self.current is None and a.get("data-id") == self.data_id:
            self.current = {"id": a.get("id") or "", "bookmark": a.get("data-bookmark") or "", "parts": []}
            self.depth = 0
        if self.current is not None:
            if "gloss-link" in (a.get("class") or ""):
                self.skip = 1  # footnote marker and its tooltip text ("Ze zmianą wprowadzoną przez…")
                return
            self.depth += 1
            if tag in BLOCK_TAGS:
                self.current["parts"].append("\n")
            if tag == "sup":
                self.current["parts"].append("^")

    def handle_endtag(self, tag: str) -> None:
        if self.skip:
            if tag not in VOID_TAGS:
                self.skip -= 1
            return
        if self.current is None or tag in VOID_TAGS:
            return
        if tag in BLOCK_TAGS:
            self.current["parts"].append("\n")
        self.depth -= 1
        if self.depth == 0:
            self.found.append(self.current)
            self.current = None

    def handle_data(self, data: str) -> None:
        if self.current is not None and not self.skip:
            # Source line breaks are layout only; paragraph breaks come from block tags.
            self.current["parts"].append(data.replace("\r", " ").replace("\n", " "))


def article_id(raw: str) -> Tuple[str, str]:
    """'67^18', '67¹⁸', 'art. 67(18)', '22a' -> ('arti_67_18', '67^18')."""
    text = raw.strip().lower().replace("art.", "").replace("art", "").strip()
    text = text.translate(SUPERSCRIPTS) if re.search(r"[⁰-⁹¹²³]", text) and not re.search(r"[\^_(]", text) else text
    m = re.fullmatch(r"(\d+)([a-z]{0,2})\s*(?:[\^_(]\s*(\d+)\s*\)?)?", text)
    if not m:
        sup = re.fullmatch(r"(\d+?)([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", raw.strip().lower().replace("art.", "").strip())
        if sup:
            return article_id(f"{sup.group(1)}^{sup.group(2).translate(SUPERSCRIPTS)}")
        error_exit(f"Nieprawidłowy numer artykułu '{raw}'. Przykłady: 30, 22a, 67^18.", "bad_request", 64)
    base, letters, sup = m.group(1), m.group(2), m.group(3)
    label = base + letters + (f"^{sup}" if sup else "")
    return f"arti_{base}{letters}" + (f"_{sup}" if sup else ""), label


def pick_article(found: List[Dict[str, Any]], consolidated: bool) -> Optional[Dict[str, Any]]:
    """Choose the article of the act itself, not a same-numbered article of transitional provisions."""
    if not found:
        return None
    if consolidated:
        in_annex = [f for f in found if re.search(r"_z\d+_", f["bookmark"])]
        if in_annex:
            return in_annex[0]
    structural = [f for f in found if "-" in f["id"] and not f["id"].startswith("pass_")]
    return (structural or found)[0]


_UNIT = r"(?:§\s*\d+[a-z]?(?:\^\d+)?|\d+[a-z]?(?:\^\d+)?)\."
LABEL_RE = rf"(?:Art\.\s*\S+\.(?:\s*{_UNIT})?|{_UNIT}|\d+[a-z]?(?:\^\d+)?\)|[a-z](?:\^\d+)?\)|[–-])"


def clean_text(parts: List[str]) -> str:
    raw = html.unescape("".join(parts)).replace("\xa0", " ")
    lines = [re.sub(r"\^\s+", "^", " ".join(line.split())) for line in raw.split("\n")]
    merged: List[str] = []
    for line in (l for l in lines if l):
        # Keep unit labels ("Art. 36.", "§ 1.", "1)", "a)", "–") on the same line as their text.
        if merged and re.fullmatch(LABEL_RE, merged[-1]):
            merged[-1] = f"{merged[-1]} {line}"
        else:
            merged.append(line)
    return "\n".join(merged)


# --------------------------------------------------------------------------- commands

def cmd_codes(_args: argparse.Namespace) -> None:
    rows = [{"code": c, "ref": ref, "name": name, "aliases": aliases} for c, (ref, name, aliases) in CODES.items()]
    print(json.dumps({"count": len(rows), "codes": rows, "source": SOURCE}, ensure_ascii=False, indent=2))


def cmd_search(args: argparse.Namespace) -> None:
    params: Dict[str, Any] = {"title": args.query, "publisher": args.publisher, "limit": args.limit}
    if args.in_force:
        params["inForce"] = 1
    if args.type:
        params["type"] = args.type
    if args.year:
        params["year"] = args.year
    data = http_get("acts/search?" + urllib.parse.urlencode(params))
    items = [brief(a) for a in data.get("items", [])]
    if not items:
        error_exit(f"Brak aktów dla zapytania '{args.query}'.", "not_found", 2)
    print(json.dumps({"query": args.query, "totalCount": data.get("totalCount"), "count": len(items),
                      "results": items, "source": SOURCE}, ensure_ascii=False, indent=2))


def cmd_act(args: argparse.Namespace) -> None:
    ref = parse_ref(args.ref)
    act = get_act(ref)
    tj = consolidated_refs(act)
    latest_tj = None
    if tj:
        t = get_act(tj[0])
        latest_tj = {**brief(t), "links": links(tj[0], t.get("address"))}
    am = amendments(act)
    since = latest_tj["announcementDate"] if latest_tj else act.get("announcementDate")
    after = [a for a in am if since and (a["entryIntoForce"] or "") > since]
    today = datetime.date.today().isoformat()
    refs = act.get("references", {})
    out = {
        **brief(act),
        "inForce": act.get("inForce"),
        "entryIntoForce": act.get("entryIntoForce"),
        "keywords": act.get("keywords", []),
        "latestConsolidatedText": latest_tj,
        "consolidatedTextsCount": len(tj),
        "amendmentsCount": len(am),
        "amendmentsAfterLatestConsolidatedText": after[: args.limit],
        "upcomingAmendments": [a for a in am if (a["entryIntoForce"] or "") > today][: args.limit],
        "constitutionalTribunalRulings": len(refs.get("Orzeczenie TK", [])),
        "implementingActs": len(refs.get("Akty wykonawcze", [])),
        "links": links(ref, act.get("address")),
        "source": SOURCE,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


def cmd_article(args: argparse.Namespace) -> None:
    ref = parse_ref(args.ref)
    data_id, label = article_id(args.article)
    act = get_act(ref)
    tj = consolidated_refs(act)
    am = amendments(act)

    # Newest document with HTML: a consolidated text, or the act itself when it was never amended.
    source_act, consolidated = None, False
    for t_ref in tj:
        t = get_act(t_ref)
        if t.get("textHTML"):
            source_act, consolidated = t, True
            break
    if source_act is None:
        if act.get("textHTML") and (not am or args.original):
            source_act = act
        else:
            pdf = links(tj[0])["pdf"] if tj else links(ref)["pdf"]
            hint = " Tekst pierwotny (bez zmian) zwraca opcja --original." if act.get("textHTML") else ""
            error_exit(
                f"Brak aktualnego tekstu HTML dla {act.get('displayAddress')} ({act.get('title')}). "
                f"Aktualne brzmienie jest dostępne tylko w PDF: {pdf}.{hint}",
                "not_available",
                2,
            )

    src_ref = f"{source_act['publisher']}/{source_act['year']}/{source_act['pos']}"
    page = http_get(f"acts/{src_ref}/text.html", as_json=False)
    parser = ArticleParser(data_id)
    parser.feed(page)
    hit = pick_article(parser.found, consolidated)
    if hit is None:
        error_exit(f"Nie znaleziono art. {label} w {source_act.get('displayAddress')}.", "not_found", 2)

    text = clean_text(hit["parts"])
    truncated = len(text) > MAX_TEXT_CHARS
    source_date = source_act.get("announcementDate") or source_act.get("promulgation")
    after = [a for a in am if source_date and (a["entryIntoForce"] or "") > source_date] if source_act is not act else am
    newer_tj = [r for r in tj if ref_parts(r) > ref_parts(src_ref)] if consolidated else list(tj)
    up_to_date = not after and not newer_tj

    warning = None
    if source_act is act and am:
        warning = "To tekst PIERWOTNY aktu (bez późniejszych zmian) — nie cytuj go jako obowiązującego brzmienia."
    elif not up_to_date:
        warning = (
            f"Brzmienie według tekstu jednolitego z {source_date}. Później weszło w życie {len(after)} zmian"
            + (f", a nowszy tekst jednolity ({newer_tj[0]}) jest dostępny tylko w PDF" if newer_tj else "")
            + ". Przed cytowaniem sprawdź, czy zmiany dotyczą tego artykułu."
        )

    out = {
        "act": {"ref": ref, "title": act.get("title"), "displayAddress": act.get("displayAddress"), "status": act.get("status")},
        "article": label,
        "text": text[:MAX_TEXT_CHARS] + ("…" if truncated else ""),
        "truncated": truncated,
        "sourceDocument": {
            "ref": src_ref,
            "displayAddress": source_act.get("displayAddress"),
            "title": source_act.get("title"),
            "kind": "tekst jednolity" if consolidated else ("tekst pierwotny" if am else "tekst ogłoszony (bez zmian)"),
            "date": source_date,
            "links": links(src_ref, source_act.get("address")),
        },
        "upToDate": up_to_date,
        "amendmentsAfterSource": {"count": len(after), "latest": after[:10]},
        "newerConsolidatedTextsPdfOnly": [{"ref": r, "pdf": links(r)["pdf"]} for r in newer_tj],
        "warning": warning,
        "source": SOURCE,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Oficjalne teksty i status polskich aktów prawnych (Dziennik Ustaw, Monitor Polski) z API ELI Sejmu RP."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("search", help="Wyszukaj akty prawne po słowach z tytułu")
    p.add_argument("query", help="Słowa z tytułu, np. 'Kodeks pracy', 'o podatku od towarów'")
    p.add_argument("--in-force", action="store_true", help="Tylko akty obowiązujące")
    p.add_argument("--type", help="Rodzaj aktu, np. Ustawa, Rozporządzenie, Obwieszczenie")
    p.add_argument("--year", type=int, help="Rok publikacji")
    p.add_argument("--publisher", choices=["DU", "MP"], default="DU", help="DU = Dziennik Ustaw, MP = Monitor Polski")
    p.add_argument("--limit", type=int, default=10, help="Liczba wyników (domyślnie 10)")
    p.set_defaults(func=cmd_search)

    p = sub.add_parser("act", help="Status aktu, teksty jednolite i zmiany z datami wejścia w życie")
    p.add_argument("ref", help="Skrót (kp, vat…), 'DU/2023/1465' lub 'Dz.U. 2023 poz. 1465'")
    p.add_argument("--limit", type=int, default=10, help="Maks. liczba zmian na liście (domyślnie 10)")
    p.set_defaults(func=cmd_act)

    p = sub.add_parser("article", help="Brzmienie artykułu z datą źródła i ostrzeżeniem o późniejszych zmianach")
    p.add_argument("ref", help="Skrót (kp, vat…), 'DU/2023/1465' lub 'Dz.U. 2023 poz. 1465'")
    p.add_argument("article", help="Numer artykułu, np. 30, 22a, 67^18")
    p.add_argument("--original", action="store_true", help="Zezwól na tekst pierwotny zmienionego aktu (historyczny)")
    p.set_defaults(func=cmd_article)

    p = sub.add_parser("codes", help="Lista skrótów najważniejszych kodeksów i ustaw (działa offline)")
    p.set_defaults(func=cmd_codes)

    args = parser.parse_args()
    if getattr(args, "limit", 1) is not None and getattr(args, "limit", 1) < 1:
        error_exit("--limit musi być dodatnie.", "bad_request", 64)
    args.func(args)


if __name__ == "__main__":
    main()
