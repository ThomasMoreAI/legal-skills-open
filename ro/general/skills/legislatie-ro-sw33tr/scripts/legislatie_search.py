#!/usr/bin/env python3
"""
legislatie_search.py v6 — căutare acte pe legislatie.just.ro (API SOAP, http) +
text ÎN VIGOARE și extragere articol (prin lj_core.py, pagini HTML, https).

Rulează din orice director: importă lj_core.py din propriul director.

  python3 legislatie_search.py "OUG 57/2019"                       # metadate
  python3 legislatie_search.py "OUG 57/2019" --fetch --articol 485^1
  python3 legislatie_search.py "Lege 53/2003" --fetch --grep "concediu de odihn"
  python3 legislatie_search.py --id 215925 --articol 56           # fără căutare
  python3 legislatie_search.py "OUG 7/2026" --fetch --api-text     # ultim resort, vezi mai jos
  python3 legislatie_search.py --diagnostic

Coduri ieșire: 0 ok | 2 niciun rezultat | 3 HTTPS blocat din acest mediu (ROUTE_BLOCKED) |
               4 articol negăsit | 5 pagina fără text | 6 id greșit / eroare portal

--api-text: dacă HTTPS e blocat, folosește textul din câmpul `Text` al API-ului SOAP.
ATENȚIE: acela e textul PUBLICAT INIȚIAL, fără modificările ulterioare. Se marchează
explicit în output și nu se citează ca drept în vigoare.
"""

import sys
import os
import re
import json
import argparse
import http.client
import xml.etree.ElementTree as ET
import uuid
import urllib.request
import urllib.error
import ssl
from html.parser import HTMLParser

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lj_core  # noqa: E402

# ── Config ──────────────────────────────────────────────────────────────────
SOAP_HOST = "legislatie.just.ro"
SOAP_PATH = "/apiws/FreeWebService.svc/SOAP"
NS_TEMPURI = "http://tempuri.org/"
NS_DC = "http://schemas.datacontract.org/2004/07/FreeWebService"
NS_WSA = "http://www.w3.org/2005/08/addressing"

CACHE_DIR = lj_core.CACHE_DIR

# ── Tipuri de acte: abrevieri -> valoare SearchTitlu ────────────────────────
ACT_TYPE_MAP = {
    "OUG": "ORDONANTA DE URGENTA",
    "ORDONANTA DE URGENTA": "ORDONANTA DE URGENTA",
    "ORDONANȚĂ DE URGENȚĂ": "ORDONANTA DE URGENTA",
    "OG": "ORDONANTA",
    "ORDONANTA": "ORDONANTA",
    "ORDONANȚĂ": "ORDONANTA",
    "LEGE": "LEGE",
    "LEGEA": "LEGE",
    "L": "LEGE",
    "HG": "HOTARARE",
    "HOTARARE": "HOTARARE",
    "HOTĂRÂRE": "HOTARARE",
    "DECIZIE": "DECIZIE",
    "DECRET": "DECRET",
    "ORDIN": "ORDIN",
    "REGULAMENT": "REGULAMENT",
    "NORME": "NORME",
    "INSTRUCTIUNI": "INSTRUCTIUNI",
    "COD": "COD",
}

# Abrevieri care implică un emitent anume (preferință, nu filtru strict).
AUTO_EMITENT = {
    "HG": "guvern",
    "OUG": "guvern",
    "OG": "guvern",
    "ORDONANTA DE URGENTA": "guvern",
    "ORDONANȚĂ DE URGENȚĂ": "guvern",
    "ORDONANTA": "guvern",
    "ORDONANȚĂ": "guvern",
}


def _norm(s: str) -> str:
    """Normalizează pentru comparații: minuscule, fără diacritice.

    Atenție: API-ul returnează uneori diacriticele ca „?" (ex. „Camera
    Deputa?ilor"), așa că eliminăm tot ce nu e literă de bază sau spațiu.
    """
    s = (s or "").lower()
    for k, v in {"ă": "a", "â": "a", "î": "i", "ș": "s", "ş": "s",
                 "ț": "t", "ţ": "t"}.items():
        s = s.replace(k, v)
    return re.sub(r"[^a-z ]", "", s)


def _matches_emitent(result: dict, emitent: str) -> bool:
    return _norm(emitent) in _norm(result.get("Emitent", ""))


def _matches_year(result: dict, year: str) -> bool:
    for key in ("DataVigoare", "DataActualizare", "Titlu"):
        if year in result.get(key, ""):
            return True
    return False


# ── SOAP / căutare (nemodificate față de v1) ────────────────────────────────
def soap_request(action: str, body: str) -> str:
    """POST SOAP prin urllib (respectă HTTP(S)_PROXY). Încearcă http, apoi https."""
    last_err = None
    for scheme in ("http", "https"):
        soap_url = f"{scheme}://{SOAP_HOST}{SOAP_PATH}"
        envelope = (
            '<?xml version="1.0" encoding="utf-8"?>'
            f'<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">'
            f'<soap-env:Header xmlns:wsa="{NS_WSA}">'
            f"<wsa:Action>{action}</wsa:Action>"
            f"<wsa:MessageID>urn:uuid:{uuid.uuid4()}</wsa:MessageID>"
            f"<wsa:To>{soap_url}</wsa:To>"
            f"</soap-env:Header>"
            f"<soap-env:Body>{body}</soap-env:Body>"
            f"</soap-env:Envelope>"
        ).encode("utf-8")
        headers = {"Content-Type": "text/xml; charset=utf-8", "SOAPAction": f'"{action}"',
                   "User-Agent": lj_core.UA}
        for attempt in range(3):  # API-ul are timeout-uri sporadice
            try:
                req = urllib.request.Request(soap_url, data=envelope, headers=headers, method="POST")
                with lj_core.urlopen(req, timeout=60) as resp:
                    return resp.read().decode("utf-8", errors="replace")
            except urllib.error.HTTPError as e:
                last_err = e
                if e.code < 500:
                    break  # eroare de cerere: nu insistăm pe schema asta
            except (urllib.error.URLError, OSError, lj_core.RouteBlocked) as e:
                last_err = e
    raise RuntimeError(f"API-ul SOAP nu răspunde (http și https): {last_err}")


def get_token() -> str:
    body = f'<GetToken xmlns="{NS_TEMPURI}" />'
    xml_resp = soap_request(f"{NS_TEMPURI}IFreeWebService/GetToken", body)
    root = ET.fromstring(xml_resp)
    el = root.find(f".//{{{NS_TEMPURI}}}GetTokenResult")
    if el is None or not el.text:
        raise RuntimeError("Nu s-a putut obține token-ul de la API.")
    return el.text.strip()


def search(token, search_titlu=None, search_numar=None, search_an=None,
           search_text=None, pagina=1, rezultate=10):
    nil = 'i:nil="true"'
    d = "d4p1"
    titlu_xml = f"<{d}:SearchTitlu>{search_titlu}</{d}:SearchTitlu>" if search_titlu else f"<{d}:SearchTitlu {nil} />"
    numar_xml = f"<{d}:SearchNumar>{search_numar}</{d}:SearchNumar>" if search_numar else f"<{d}:SearchNumar {nil} />"
    an_xml = f"<{d}:SearchAn>{search_an}</{d}:SearchAn>" if search_an else f"<{d}:SearchAn {nil} />"
    text_xml = f"<{d}:SearchText>{search_text}</{d}:SearchText>" if search_text else f"<{d}:SearchText {nil} />"

    body = (
        f'<Search xmlns="{NS_TEMPURI}">'
        f'<SearchModel xmlns:{d}="{NS_DC}" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">'
        f"<{d}:NumarPagina>{pagina}</{d}:NumarPagina>"
        f"<{d}:RezultatePagina>{rezultate}</{d}:RezultatePagina>"
        f"{an_xml}{numar_xml}{text_xml}{titlu_xml}"
        f"</SearchModel>"
        f"<tokenKey>{token}</tokenKey>"
        f"</Search>"
    )
    xml_resp = soap_request(f"{NS_TEMPURI}IFreeWebService/Search", body)
    root = ET.fromstring(xml_resp)
    results = []
    for legi in root.findall(f".//{{{NS_DC}}}Legi"):
        entry = {}
        for child in legi:
            tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
            entry[tag] = (child.text or "").strip()
        results.append(entry)
    return results


def parse_act_reference(text):
    text = text.strip()
    m = re.match(r"^(.+?)\s+(?:nr\.?\s*)?(\d+)\s*/\s*(\d{4})$", text, re.IGNORECASE)
    if not m:
        return None
    tip = m.group(1).strip().upper()
    return {
        "SearchTitlu": ACT_TYPE_MAP.get(tip, tip),
        "SearchNumar": m.group(2),
        "SearchAn": m.group(3),
        "_auto_emitent": AUTO_EMITENT.get(tip),
    }


def search_paged(token, search_titlu=None, search_numar=None, search_an=None,
                 search_text=None, emitent=None, max_pages=12, per_page=10):
    """Parcurge mai multe pagini de rezultate, cu deduplicare.

    Necesitate: API-ul plafonează RezultatePagina la 10 și NU filtrează după
    SearchAn, deci actul căutat poate fi pe paginile următoare. Ne oprim
    devreme dacă am găsit deja un rezultat care trece filtrele (an + emitent).
    """
    seen, collected = set(), []
    for pag in range(1, max_pages + 1):
        page = search(token, search_titlu=search_titlu, search_numar=search_numar,
                      search_an=search_an, search_text=search_text,
                      pagina=pag, rezultate=per_page)
        new = [r for r in page if r.get("LinkHtml") and r["LinkHtml"] not in seen]
        if not new:
            break
        for r in new:
            seen.add(r["LinkHtml"])
        collected.extend(new)

        # Fără criterii de filtrare client-side: o singură pagină e de ajuns.
        if not search_an and not emitent:
            break
        # Oprire timpurie: avem deja un rezultat care trece toate filtrele?
        hit = [r for r in collected
               if (not search_an or _matches_year(r, search_an))
               and (not emitent or _matches_emitent(r, emitent))]
        if hit:
            break
    return collected


def format_results(results, top_n=5):
    if not results:
        return "Nu s-au găsit rezultate."
    lines = []
    for i, r in enumerate(results[:top_n], 1):
        titlu = re.sub(r"\s+", " ", r.get("Titlu", "").replace("\ufeff", "").split("EMITENT")[0].strip())
        lines.append(f"{i}. {r.get('TipAct', '?')} nr. {r.get('Numar', '?')} — {r.get('Emitent', '?')}")
        lines.append(f"   Titlu: {titlu[:200]}")
        lines.append(f"   Link: {r.get('LinkHtml', 'N/A')}")
        lines.append(f"   Data vigoare: {r.get('DataVigoare', 'N/A')}")
        lines.append("")
    return "\n".join(lines)


# ── Descărcare text: delegat la lj_core ─────────────────────────────────────

def diagnostic():
    """Distinge «portalul e picat» de «traseul meu nu poate face HTTPS către portal»."""
    try:
        get_token()
        api = "200"
    except RuntimeError as e:
        api = "EROARE: %s" % e
    try:
        lj_core.fetch_html("/Public/DetaliiDocumentAfis/5729", timeout=30)
        html = "200"
    except lj_core.RouteBlocked as e:
        html = "EROARE: %s" % e
    except LookupError as e:
        html = "EROARE portal: %s" % e
    print("Diagnostic legislatie.just.ro  (python %s, proxy=%s)" % (
        sys.version.split()[0], "da" if os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy") else "nu"))
    print("  API SOAP  (http)  : %s" % api)
    print("  pagini HTML (https): %s" % html)
    api_ok, html_ok = api.startswith("2"), html == "200"
    if html_ok:
        print("VERDICT: acces complet. --fetch / lj_core merg din acest mediu.")
    elif api_ok:
        print("VERDICT: ROUTE_BLOCKED — căutarea merge, textul NU. Treci la ruta următoare din SKILL.md.")
    else:
        print("VERDICT: portalul nu e accesibil deloc de aici (sau e picat). Încearcă altă rută.")
    return 0 if html_ok else 3


def fetch_act_text(link_html, doc_id=None, out_path=None, no_cache=False, forma_baza=False):
    """Compatibilitate v5: (cale_fișier, nr_caractere) pentru forma în vigoare."""
    meta = lj_core.get_in_force(doc_id or link_html, no_cache=no_cache, forma_baza=forma_baza)
    path = meta.get("cache")
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(meta["text"])
        path = out_path
    return path, len(meta["text"])


extract_articol = lj_core.extract_articol

# ── CLI ─────────────────────────────────────────────────────────────────────

def _print_fetch(meta, args, api_label=None):
    print(lj_core.header(meta))
    if api_label:
        print(api_label)
    text = meta["text"]
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print("SALVAT: %s" % args.out)
    if args.articol:
        art = lj_core.extract_articol(text, args.articol)
        if art is None:
            print("[!] Articolul %s nu apare în text." % args.articol, file=sys.stderr)
            return 4
        print("\n--- Articolul %s (%s caractere) ---\n%s" % (
            lj_core._norm_ref(args.articol), format(len(art), ","), art))
    elif args.grep:
        print("\n" + (lj_core.grep(text, args.grep, args.context) or "(nicio potrivire)"))
    elif not args.silent:
        print("\nFolosește --articol <N>, --grep <regex> sau grep pe fișierul de mai sus.")
    return 0


def main():
    lj_core.utf8_console()
    parser = argparse.ArgumentParser(description="Caută/descarcă acte normative pe legislatie.just.ro")
    parser.add_argument("referinta", nargs="?", help='Referință act, ex: "OUG 57/2019"')
    parser.add_argument("--tip", help="Tip act (ex: ORDONANTA DE URGENTA, LEGE, HG)")
    parser.add_argument("--numar", help="Număr act")
    parser.add_argument("--an", help="An act")
    parser.add_argument("--text", help="Căutare text liber")
    parser.add_argument("--emitent", help='Filtru strict de emitent (ex: "Guvernul", "Senatul")')
    parser.add_argument("--pagini", type=int, default=12, help="Pagini API parcurse la filtrare (implicit 12)")
    parser.add_argument("--rezultate", type=int, default=10, help="Număr maxim rezultate afișate")
    parser.add_argument("--json", action="store_true", help="Metadate JSON (fără câmpul Text)")
    parser.add_argument("--id", help="Sari peste căutare: id sau link DetaliiDocument/<id>")
    parser.add_argument("--fetch", action="store_true", help="Descarcă textul ÎN VIGOARE al primului rezultat")
    parser.add_argument("--articol", help="Extrage articolul (ex: 485^1, 12, XLIX, unic); implică --fetch")
    parser.add_argument("--grep", help="Regex căutat în text; implică --fetch")
    parser.add_argument("--context", type=int, default=1, help="Linii de context pentru --grep")
    parser.add_argument("--out", help="Salvează textul și aici")
    parser.add_argument("--silent", "--info", action="store_true", help="Doar antetul (forma, data), fără text")
    parser.add_argument("--no-cache", action="store_true", help="Ignoră cache-ul (TTL 6h)")
    parser.add_argument("--forma-baza", action="store_true", help="Forma publicată inițial, nu cea în vigoare")
    parser.add_argument("--exact", action="store_true", help="Cu --id: exact consolidarea istorică indicată")
    parser.add_argument("--api-text", action="store_true",
                        help="Dacă HTTPS e blocat: text din API (FORMA PUBLICATĂ INIȚIAL, marcată ca atare)")
    parser.add_argument("--diagnostic", action="store_true", help="Testează accesul și spune ce rută merge")
    parser.add_argument("--version", action="store_true")
    args = parser.parse_args()

    if args.version:
        print("legislatie_search 6 / lj_core", lj_core.VERSION)
        return 0
    if args.diagnostic:
        return diagnostic()
    if args.articol or args.grep or args.silent:
        args.fetch = True

    if args.id:
        try:
            meta = lj_core.get_in_force(args.id, no_cache=args.no_cache, forma_baza=args.forma_baza,
                                        exact=args.exact)
        except lj_core.RouteBlocked as e:
            print("ROUTE_BLOCKED: %s" % e, file=sys.stderr)
            return 3
        except LookupError as e:
            print(str(e), file=sys.stderr)
            return 6
        return _print_fetch(meta, args)

    search_params = {}
    if args.referinta:
        parsed = parse_act_reference(args.referinta)
        search_params = parsed if parsed else {"search_text": args.referinta}
    else:
        if args.tip:
            search_params["search_titlu"] = ACT_TYPE_MAP.get(args.tip.strip().upper(), args.tip.strip().upper())
        if args.numar:
            search_params["search_numar"] = args.numar
        if args.an:
            search_params["search_an"] = args.an
        if args.text:
            search_params["search_text"] = args.text
    if not search_params:
        parser.print_help()
        return 1

    token = get_token()
    key_map = {"SearchTitlu": "search_titlu", "SearchNumar": "search_numar", "SearchAn": "search_an",
               "search_titlu": "search_titlu", "search_numar": "search_numar",
               "search_an": "search_an", "search_text": "search_text"}
    kwargs = {key_map[k]: v for k, v in search_params.items() if k in key_map}

    auto_emitent = search_params.get("_auto_emitent")
    if not auto_emitent and args.tip:
        auto_emitent = AUTO_EMITENT.get(args.tip.strip().upper())
    effective_emitent = args.emitent or auto_emitent
    results = search_paged(token, emitent=effective_emitent, max_pages=args.pagini, **kwargs)

    # API-ul NU respectă SearchAn: filtrăm client-side.
    year = kwargs.get("search_an")
    if year:
        filtered = [r for r in results if _matches_year(r, year)]
        if filtered:
            results = filtered
    if effective_emitent:
        filtered = [r for r in results if _matches_emitent(r, effective_emitent)]
        if args.emitent or filtered:  # explicit = strict; automat = doar dacă nu golește lista
            results = filtered

    if not args.fetch:
        if args.json:
            print(json.dumps([{k: v for k, v in r.items() if k != "Text"} for r in results],
                             ensure_ascii=False, indent=2))
        else:
            print(format_results(results, top_n=args.rezultate))
        return 0 if results else 2

    if not results or not results[0].get("LinkHtml"):
        print("Nu s-au găsit rezultate — nimic de descărcat.", file=sys.stderr)
        return 2
    first = results[0]
    titlu = re.sub(r"\s+", " ", first.get("Titlu", "").replace("\ufeff", "").split("EMITENT")[0]).strip()[:160]
    print("REZULTAT: %s nr. %s — %s | %s" % (first.get("TipAct", "?"), first.get("Numar", "?"),
                                          first.get("Emitent", "?"), titlu))
    try:
        meta = lj_core.get_in_force(first["LinkHtml"], no_cache=args.no_cache, forma_baza=args.forma_baza)
    except lj_core.RouteBlocked as e:
        if not (args.api_text and first.get("Text")):
            print("ROUTE_BLOCKED: HTTPS către %s nu merge din acest mediu (%s).\n"
                  "Treci la ruta următoare din SKILL.md; ca ultim resort: --api-text." % (SOAP_HOST, e),
                  file=sys.stderr)
            return 3
        raw = first["Text"]
        text = lj_core.html_to_text(raw) if "<" in raw[:2000] else lj_core.clean_text(raw)
        meta = {"id": lj_core.doc_id_of(first["LinkHtml"]), "url": first["LinkHtml"],
                "forma": "PUBLICATĂ INIȚIAL (din API) — NU include modificările ulterioare",
                "text": text}
        return _print_fetch(meta, args, api_label=(
            "ATENȚIE: HTTPS blocat; text din API = forma publicată inițial. Nu îl cita ca drept în "
            "vigoare decât dacă ai verificat că actul nu a fost modificat."))
    except LookupError as e:
        print(str(e), file=sys.stderr)
        return 6
    return _print_fetch(meta, args)


if __name__ == "__main__":
    sys.exit(main())
