#!/usr/bin/env python3
"""Suchwrapper fuer die RIS-OGD-API v2.6 (Endpoint /Judikatur).

Liefert Metadaten + Direkt-Link pro Treffer. Volltext-Download ist
ausserhalb des Scopes dieses Skills.

Quelle: https://data.bka.gv.at/ris/api/v2.6/
Nur Standardbibliothek, keine Pip-Installation noetig.

Beispiele:
  ris_search.py --applikation Justiz --suchworte "Mietzinsminderung"
  ris_search.py --applikation Vfgh   --geschaeftszahl "G 12/2020"
  ris_search.py --applikation Vwgh   --norm "ABGB §1319a" \\
                --von 2020-01-01 --bis 2024-12-31 --pro-seite 50
  ris_search.py --applikation Justiz --suchworte "Datenschutz" --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

BASE_URL = "https://data.bka.gv.at/ris/api/v2.6/Judikatur"

ATTRIBUTION_TEXT = (
    "Quelle: RIS, Bundeskanzleramt — CC BY 4.0 "
    "(https://creativecommons.org/licenses/by/4.0/deed.de). "
    "Recherchehilfe, keine authentische Rechtsquelle — verbindlich ist "
    "ausschliesslich der Wortlaut im Bundes-/Landesgesetzblatt."
)

APPLIKATIONEN = [
    "Justiz", "Vfgh", "Vwgh", "Bvwg", "Lvwg",
    "Dsk", "AsylGH", "Normenliste", "Pvak", "Gbk", "Dok",
]

PRO_SEITE_VALUES = ["Ten", "Twenty", "Fifty", "OneHundred"]

IM_RIS_SEIT_VALUES = [
    "Undefined", "EinerWoche", "EinemMonat",
    "DreiMonaten", "SechsMonaten", "EinemJahr",
]

# Prefix-Konvention: J{Court}{T|R} — J=Judikatur,
# Court ∈ {J=Justiz, W=Vwgh, F=Vfgh}, T=Text, R=Rechtssatz.
# Reihenfolge muss "längster Prefix zuerst" einhalten — wir
# erzwingen das beim Modul-Load (siehe unten).
DOCNUMBER_PREFIX_TO_PATH = [
    ("BVWG",   "Bvwg"),
    ("LVWG",   "Lvwg"),
    ("ASYLGH", "AsylGH"),
    ("PVAK",   "Pvak"),
    ("GBK",    "Gbk"),
    ("DSB",    "Dsk"),
    ("JJT",    "Justiz"),
    ("JJR",    "Justiz"),
    ("JWT",    "Vwgh"),
    ("JWR",    "Vwgh"),
    ("JFT",    "Vfgh"),
    ("JFR",    "Vfgh"),
]
DOCNUMBER_PREFIX_TO_PATH.sort(key=lambda kv: -len(kv[0]))

DOCNUMBER_RE = re.compile(r"^[A-Z][A-Z0-9_]+$")

# 3-Zeichen-Prefixe der Konvention J{Court}{T|R}, getrennt nach Doktyp.
# Andere Applikationen (BVWG, LVWG, Dsk, …) folgen der Konvention nicht
# und bleiben unklassifiziert.
RECHTSSATZ_PREFIXES = {"JJR", "JFR", "JWR"}
VOLLTEXT_PREFIXES = {"JJT", "JFT", "JWT"}


def docnumber_to_html_url(docnr: str) -> str | None:
    if not (5 <= len(docnr) <= 50 and DOCNUMBER_RE.match(docnr)):
        return None
    for prefix, path in DOCNUMBER_PREFIX_TO_PATH:
        if docnr.startswith(prefix):
            return f"https://ris.bka.gv.at/Dokumente/{path}/{docnr}/{docnr}.html"
    return None


def classify_docnr(docnr: str | None) -> str | None:
    """Liefert "Rechtssatz", "Volltext" oder None."""
    if not docnr or len(docnr) < 3:
        return None
    head = docnr[:3]
    if head in RECHTSSATZ_PREFIXES:
        return "Rechtssatz"
    if head in VOLLTEXT_PREFIXES:
        return "Volltext"
    return None


def derive_volltext_docnr(docnr: str | None) -> str | None:
    """Heuristik: aus einer Rechtssatz-Dokumentennummer die
    wahrscheinliche Volltext-Dokumentennummer ableiten.

    Konvention bei OGH/VfGH/VwGH: J{Court}R_…_NNN ↔ J{Court}T_…_000.
    Trifft nicht in 100 % der Fälle zu — bei seltenen Sonderfällen
    (z. B. berichtigte Entscheidungen) liefert der abgeleitete Link 404.
    """
    if classify_docnr(docnr) != "Rechtssatz":
        return None
    parts = docnr.split("_")
    if len(parts) < 2:
        return None
    parts[0] = parts[0][:2] + "T"  # JJR → JJT, JFR → JFT, JWR → JWT
    parts[-1] = "000"
    return "_".join(parts)


def normalize_norm(value: str | None) -> tuple[str | None, str | None]:
    """Repariert Norm-Eingaben ohne §-Zeichen.

    Der RIS-Norm-Index ist auf die kanonische Form ``{Kürzel} §{Paragraph}``
    angewiesen; ohne § fällt der Index praktisch komplett weg. Auf der
    Mobile-Tastatur ist § umständlich, deshalb fügt das Skript ihn ein,
    wenn die Eingabe das offensichtliche Muster ``{Kürzel} {Zahl}`` hat.

    Returns (normalisierter_wert, original_falls_geaendert_sonst_None).
    """
    if not value:
        return value, None
    stripped = value.strip()
    parts = stripped.split(None, 1)
    if len(parts) != 2 or "§" in stripped:
        return stripped, None
    kuerzel, rest = parts
    if rest and rest[0].isdigit():
        return f"{kuerzel} §{rest}", value
    return stripped, None


def build_url(args: argparse.Namespace, page: int | None = None) -> str:
    """Bau die Anfrage-URL.

    Sortierung-Default: Wird weder ``--sortierung`` noch
    ``--sort-direction`` gesetzt, sortieren wir nach
    ``Datum`` / ``Descending``. Im Chat-Kontext ("aktuelle Judikatur
    zu …") ist das fast immer die gewollte Reihenfolge; wer den
    API-Default ``Relevanz`` zurueckwill, kann ``--sortierung Relevanz``
    setzen.
    """
    sortierung = args.sortierung
    sort_direction = args.sort_direction
    if not sortierung and not sort_direction:
        sortierung = "Datum"
        sort_direction = "Descending"

    params: list[tuple[str, str]] = [
        ("Applikation", args.applikation),
        ("DokumenteProSeite", args.pro_seite),
        ("Seitennummer", str(page if page is not None else args.seite)),
    ]
    # SucheNachRechtssatz / SucheNachText sind nur bei Volltext-Suche
    # (Suchworte) sinnvoll. Bei Geschaeftszahl/Norm/Rechtssatznummer-
    # Abfragen würden sie Treffer unnötig filtern, also nur senden, wenn
    # explizit gesetzt.
    if args.suchworte:
        params.append(
            ("SucheNachRechtssatz", "False" if args.no_rechtssatz else "True"),
        )
        params.append(("SucheNachText", "False" if args.no_text else "True"))
    optional = [
        (args.suchworte, "Suchworte"),
        (args.geschaeftszahl, "Geschaeftszahl"),
        (args.norm, "Norm"),
        (args.rechtssatznummer, "Rechtssatznummer"),
        (args.schlagworte, "Schlagworte"),
        (args.von, "EntscheidungsdatumVon"),
        (args.bis, "EntscheidungsdatumBis"),
        (args.im_ris_seit, "ImRisSeit"),
        (sortierung, "Sortierung"),
        (sort_direction, "SortDirection"),
    ]
    for value, key in optional:
        if value:
            params.append((key, value))
    return f"{BASE_URL}?{urllib.parse.urlencode(params)}"


def http_get_json(url: str, timeout: float) -> dict[str, Any]:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "ris-rechtsprechung-skill/1.0 (+claude-code)",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


_RETRYABLE = (
    urllib.error.URLError,
    urllib.error.HTTPError,
    TimeoutError,
    json.JSONDecodeError,
)


def _read_error_body(err: urllib.error.HTTPError, max_chars: int = 500) -> str:
    """Liefert ein Body-Snippet aus dem HTTPError, kompakt fuer stderr."""
    try:
        body = err.read().decode("utf-8", errors="replace").strip()
    except Exception:
        return ""
    body = " ".join(body.split())
    return body[:max_chars] + ("…" if len(body) > max_chars else "")


def fetch_with_retries(url: str, args: argparse.Namespace) -> dict[str, Any] | None:
    """Hole JSON von der RIS-API mit linearem Backoff. None = Aufgabe.

    HTTP 4xx (Client-Fehler — z. B. 400 bei fehlenden Pflichtparametern,
    404 bei nicht existenter Ressource) werden NICHT retried, da sich die
    Antwort durch erneutes Senden derselben Anfrage nicht aendert. Wir
    geben stattdessen sofort eine sprechende Fehlermeldung aus —
    insbesondere fuer 400 erklaeren wir die typische Ursache.
    """
    for attempt in range(1 + args.retries):
        try:
            return http_get_json(url, timeout=args.timeout)
        except urllib.error.HTTPError as e:
            if 400 <= e.code < 500:
                body = _read_error_body(e)
                if e.code == 400:
                    sys.stderr.write(
                        "RIS-API HTTP 400 — Anfrage abgewiesen.\n"
                        "Typische Ursachen: kein Suchparameter angegeben, "
                        "Datumsformat falsch (erwartet YYYY-MM-DD), oder "
                        "ungueltige Kombination.\n"
                    )
                else:
                    sys.stderr.write(f"RIS-API HTTP {e.code} — {e.reason}.\n")
                if body:
                    sys.stderr.write(f"Antwort: {body}\n")
                sys.stderr.write(f"URL: {url}\n")
                return None
            if attempt < args.retries:
                time.sleep(args.retry_sleep * (attempt + 1))
                continue
            sys.stderr.write(
                f"RIS-API HTTP {e.code} nach {args.retries} Wiederholungen: "
                f"{e.reason}\nURL: {url}\n"
            )
            return None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
            if attempt < args.retries:
                time.sleep(args.retry_sleep * (attempt + 1))
                continue
            sys.stderr.write(f"RIS-Anfrage fehlgeschlagen: {e}\nURL: {url}\n")
            return None
    return None


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]


def first_text(value: Any) -> str | None:
    """Extrahiere String aus Werten, die String, Dict ({'item': ...}, {'#text': ...}) oder Liste sein koennen."""
    if value is None:
        return None
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        for v in value:
            t = first_text(v)
            if t:
                return t
        return None
    if isinstance(value, dict):
        for key in ("item", "#text"):
            if key in value:
                return first_text(value[key])
    return None


def all_texts(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        out: list[str] = []
        for v in value:
            out.extend(all_texts(v))
        return out
    if isinstance(value, dict):
        for key in ("item", "#text"):
            if key in value:
                return all_texts(value[key])
    return []


def format_date_de(iso_date: str | None) -> str | None:
    """ISO YYYY-MM-DD → DD.MM.YYYY. Bei unerwartetem Format Original."""
    if not iso_date:
        return None
    try:
        y, m, d = iso_date.split("-", 2)
        if len(y) == 4 and y.isdigit() and m.isdigit() and d.isdigit():
            return f"{d}.{m}.{y}"
    except ValueError:
        pass
    return iso_date


def normalize(raw: dict[str, Any]) -> dict[str, Any]:
    result = (raw.get("OgdSearchResult") or {}).get("OgdDocumentResults") or {}
    hits = result.get("Hits") or {}
    if isinstance(hits, dict):
        total = int(hits.get("#text", 0) or 0)
        page = int(hits.get("@pageNumber", 1) or 1)
        size = int(hits.get("@pageSize", 0) or 0)
    else:
        total, page, size = int(hits or 0), 1, 0

    docs: list[dict[str, Any]] = []
    for ref in as_list(result.get("OgdDocumentReference")):
        data = (ref or {}).get("Data") or {}
        meta = data.get("Metadaten") or {}
        tech = meta.get("Technisch") or {}
        allgemein = meta.get("Allgemein") or {}
        jud = meta.get("Judikatur") or {}

        docnr = tech.get("ID")
        gz = first_text(jud.get("Geschaeftszahl"))
        gz_alle = all_texts(jud.get("Geschaeftszahl"))
        ent_datum = first_text(jud.get("Entscheidungsdatum"))

        # Gericht zuverlässig aus Technisch.Organ. Fallback auf Justiz.Gericht.
        gericht = tech.get("Organ") or first_text(jud.get("Gericht"))

        # API liefert die Felder im Plural: Normen / Rechtssatznummern.
        # Vorher hatten wir die Singular-Form geprüft — daher blieben sie
        # leer, obwohl die API sie liefert.
        normen = all_texts(jud.get("Normen"))

        leitsatz: Any = None
        fachgebiete: list[str] = []
        rechtssatznummer: str | None = None
        entscheidungstexte: list[Any] = []
        for app_key in APPLIKATIONEN:
            block = jud.get(app_key) or {}
            if not isinstance(block, dict):
                continue
            if leitsatz is None and block.get("Leitsatz"):
                leitsatz = first_text(block["Leitsatz"]) or block["Leitsatz"]
            if not gericht and block.get("Gericht"):
                gericht = first_text(block.get("Gericht"))
            if not fachgebiete and block.get("Fachgebiete"):
                fachgebiete = all_texts(block.get("Fachgebiete"))
            if not rechtssatznummer and block.get("Rechtssatznummern"):
                rechtssatznummer = first_text(block.get("Rechtssatznummern"))
            if not entscheidungstexte and block.get("Entscheidungstexte"):
                entscheidungstexte = as_list(
                    (block.get("Entscheidungstexte") or {}).get("item")
                )

        # Bei Rechtssatz-Dokumenten ist die "Geschaeftszahl" oben eine
        # verkettete Liste aller zitierenden Geschäftszahlen, und das
        # "Entscheidungsdatum" das letzte Update-Datum — nicht das
        # Entscheidungsdatum der Stamm-Entscheidung. Letztere steht
        # sauber in Entscheidungstexte.item[0]. Wenn vorhanden, nehmen
        # wir die als Quelle für GZ + Datum + Volltext-URL.
        stamm_volltext_url: str | None = None
        if entscheidungstexte and isinstance(entscheidungstexte[0], dict):
            stamm = entscheidungstexte[0]
            if stamm.get("Geschaeftszahl"):
                gz = stamm.get("Geschaeftszahl")
            if stamm.get("Entscheidungsdatum"):
                ent_datum = stamm.get("Entscheidungsdatum")
            stamm_volltext_url = stamm.get("DokumentUrl")

        urls: dict[str, str] = {}
        cref = (data.get("Dokumentliste") or {}).get("ContentReference")
        for c in as_list(cref):
            for u in as_list((c or {}).get("Urls", {}).get("ContentUrl")):
                dt, link = (u or {}).get("DataType"), (u or {}).get("Url")
                if dt and link:
                    urls[dt.lower()] = link

        link = (
            allgemein.get("DokumentUrl")
            or urls.get("html")
            or (docnumber_to_html_url(docnr) if docnr else None)
        )

        doc_type = classify_docnr(docnr)
        # Volltext-URL: bevorzugt aus Entscheidungstexte (echt von der API),
        # sonst Heuristik aus der Dokumentennummer.
        volltext_url = stamm_volltext_url
        if doc_type == "Rechtssatz" and not volltext_url:
            derived = derive_volltext_docnr(docnr)
            if derived:
                volltext_url = docnumber_to_html_url(derived)

        docs.append({
            "dokumentnummer": docnr,
            "applikation": tech.get("Applikation"),
            "gericht": gericht,
            "doc_type": doc_type,
            "rechtssatznummer": rechtssatznummer,
            "geschaeftszahl": gz,
            "geschaeftszahlen": gz_alle,
            "entscheidungsdatum": ent_datum,
            "leitsatz": leitsatz,
            "normen": normen,
            "fachgebiete": fachgebiete,
            "entscheidungstexte_count": len(entscheidungstexte),
            "link": link,
            "volltext_url": volltext_url,
            "content_urls": urls,
        })

    return {
        "total_hits": total,
        "page": page,
        "page_size": size,
        "documents": docs,
        "attribution": ATTRIBUTION_TEXT,
    }


def render_markdown(result: dict[str, Any]) -> str:
    pages_fetched = result.get("pages_fetched") or 1
    if pages_fetched > 1:
        rendered = len(result.get("documents") or [])
        header = (
            f"**Treffer:** {result['total_hits']} "
            f"(Seiten {result['page']}–{result['page'] + pages_fetched - 1} "
            f"geholt, {rendered} Dokumente gerendert)"
        )
    else:
        header = (
            f"**Treffer:** {result['total_hits']} "
            f"(Seite {result['page']}, {result['page_size']} pro Seite)"
        )
    lines = [header, ""]
    for i, d in enumerate(result["documents"], start=1):
        gz = d["geschaeftszahl"] or "(ohne Geschäftszahl)"
        datum = format_date_de(d["entscheidungsdatum"]) or "?"
        court = d.get("gericht") or d.get("applikation") or ""
        type_label = ""
        if d.get("doc_type"):
            if d.get("rechtssatznummer"):
                type_label = f" [{d['doc_type']} {d['rechtssatznummer']}]"
            else:
                type_label = f" [{d['doc_type']}]"
        lines.append(f"### {i}. {court} {gz} vom {datum}{type_label}")
        if d["leitsatz"]:
            ls = " ".join(d["leitsatz"].split())
            if len(ls) > 400:
                ls = ls[:397] + "..."
            lines.append(f"_Leitsatz:_ {ls}")
        if d.get("normen"):
            lines.append(f"**Norm:** {', '.join(d['normen'])}")
        if d.get("fachgebiete"):
            lines.append(f"**Fachgebiet:** {', '.join(d['fachgebiete'])}")
        if d.get("volltext_url"):
            if d["link"]:
                lines.append(f"- [Rechtssatz im RIS]({d['link']})")
            label = ("Volltext der Stammentscheidung"
                     if d.get("doc_type") == "Rechtssatz"
                     else "Volltext im RIS")
            lines.append(f"- [{label}]({d['volltext_url']})")
        elif d["link"]:
            lines.append(f"- [Zur Entscheidung im RIS]({d['link']})")
        n_zitate = d.get("entscheidungstexte_count") or 0
        if n_zitate > 1:
            lines.append(
                f"_Auch zitiert in {n_zitate - 1} weiteren Entscheidungen._"
            )
        lines.append("")
    attribution = result.get("attribution") or ATTRIBUTION_TEXT
    lines.append(f"---\n_{attribution}_")
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="RIS-Judikatur-Suche (data.bka.gv.at v2.6) — Metadaten + Link.",
    )
    p.add_argument("--applikation", required=True, choices=APPLIKATIONEN)
    p.add_argument("--suchworte")
    p.add_argument("--geschaeftszahl")
    p.add_argument("--norm",
                   help='Format "{Gesetzeskuerzel} §{Paragraph}", z.B. "ABGB §1319a"')
    p.add_argument("--rechtssatznummer")
    p.add_argument("--schlagworte",
                   help="kontrolliertes Schlagwort (RIS-Vokabular)")
    p.add_argument("--von", metavar="YYYY-MM-DD",
                   help="EntscheidungsdatumVon")
    p.add_argument("--bis", metavar="YYYY-MM-DD",
                   help="EntscheidungsdatumBis")
    p.add_argument("--im-ris-seit", choices=IM_RIS_SEIT_VALUES,
                   dest="im_ris_seit")
    p.add_argument("--pro-seite", choices=PRO_SEITE_VALUES, default="Twenty")
    p.add_argument("--seite", type=int, default=1,
                   help="Startseite (1-basiert). Bei --alle-seiten der Einstiegspunkt.")
    p.add_argument("--alle-seiten", action="store_true", dest="alle_seiten",
                   help="Mehrere Seiten automatisch holen, bis Treffer erschoepft "
                        "oder --max-seiten erreicht (mit RIS-konformer Pause).")
    p.add_argument("--max-seiten", type=int, default=5, dest="max_seiten",
                   help="Cap fuer --alle-seiten (Default 5).")
    p.add_argument("--pause-pagination", type=float, default=1.5,
                   dest="pause_pagination",
                   help="Pause in Sekunden zwischen Seiten (RIS empfiehlt 1-2 s).")
    p.add_argument("--sortierung",
                   help="Default: Datum (im Chat-Kontext meist gewollt). "
                        "Andere Werte: Relevanz, Geschaeftszahl.")
    p.add_argument("--sort-direction", choices=["Ascending", "Descending"],
                   dest="sort_direction",
                   help="Default: Descending (zusammen mit Sortierung-Default).")
    p.add_argument("--no-rechtssatz", action="store_true")
    p.add_argument("--no-text", action="store_true")
    p.add_argument("--json", action="store_true",
                   help="Strukturiertes JSON statt Markdown ausgeben")
    p.add_argument("--raw", action="store_true",
                   help="Roh-JSON der RIS-API ausgeben")
    p.add_argument("--timeout", type=float, default=30.0)
    p.add_argument("--retries", type=int, default=2,
                   help="Wiederholungsversuche bei HTTP-/Netzfehlern")
    p.add_argument("--retry-sleep", type=float, default=2.0)
    return p.parse_args(argv)


SUCHWORTE_NULL_HINT_TEMPLATE = (
    "> **Hinweis: 0 Treffer im OGD-Volltext-Index.**\n"
    "> Bei alten Entscheidungen (vor ca. 1990) ist der Index lückenhaft — "
    "der Volltext kann existieren und das Suchwort enthalten, ohne dass "
    "die API ihn findet.\n"
    ">\n"
    "> **Empfohlener Fallback:** Google `site:`-Suche im RIS-Web-Korpus, "
    "der Google-indexiert ist:\n"
    "> ```\n"
    "> {query}\n"
    "> ```\n"
    "> In Claude.ai-Kontext kann diese Query direkt an `web_search` "
    "weitergegeben werden. Manuell unter "
    "<https://www.google.com/search?q={query_url}> oder ein Stück "
    "präziser unter <https://www.ris.bka.gv.at/Judikatur/>."
)


def build_websearch_query(args: argparse.Namespace) -> str:
    """Erzeugt eine Google `site:`-Such-Query als Fallback, wenn die API
    nichts findet. Google indexiert das RIS-Web-Frontend deutlich
    breiter als der OGD-API-Volltext-Index — insbesondere bei alten
    Entscheidungen.
    """
    parts: list[str] = ["site:ris.bka.gv.at", args.applikation]
    if args.suchworte:
        parts.append(args.suchworte)
    if args.norm:
        parts.append(args.norm)
    if args.geschaeftszahl:
        parts.append(f'"{args.geschaeftszahl}"')
    if args.schlagworte:
        parts.append(args.schlagworte)
    if args.rechtssatznummer:
        parts.append(args.rechtssatznummer)
    query = " ".join(parts)
    if args.von:
        query += f" after:{args.von.split('-')[0]}"
    if args.bis:
        query += f" before:{args.bis.split('-')[0]}"
    return query


def fetch_pages_normalized(args: argparse.Namespace) -> dict[str, Any] | None:
    """Holt eine oder mehrere Seiten und liefert ein zusammengefuehrtes
    normalisiertes Resultat. Ohne ``--alle-seiten`` ist das Verhalten
    identisch zum Single-Page-Aufruf.
    """
    raw = fetch_with_retries(build_url(args, page=args.seite), args)
    if raw is None:
        return None
    norm = normalize(raw)

    if not args.alle_seiten:
        return norm

    norm["pages_fetched"] = 1
    page_size = norm.get("page_size") or 0
    total = norm.get("total_hits") or 0
    fetched = len(norm["documents"])
    cap = max(1, args.max_seiten)

    next_page = args.seite + 1
    while (
        norm["pages_fetched"] < cap
        and (page_size == 0 or fetched < total)
        and len(norm["documents"]) > 0
    ):
        time.sleep(args.pause_pagination)
        raw_n = fetch_with_retries(build_url(args, page=next_page), args)
        if raw_n is None:
            break
        page_norm = normalize(raw_n)
        if not page_norm["documents"]:
            break
        norm["documents"].extend(page_norm["documents"])
        norm["pages_fetched"] += 1
        fetched = len(norm["documents"])
        next_page += 1

    return norm


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv if argv is not None else sys.argv[1:])

    if not any([args.suchworte, args.geschaeftszahl, args.norm,
                args.rechtssatznummer, args.schlagworte]):
        sys.stderr.write(
            "Fehler: mindestens --suchworte, --geschaeftszahl, --norm, "
            "--rechtssatznummer oder --schlagworte angeben.\n"
        )
        return 2

    if args.raw and args.alle_seiten:
        sys.stderr.write(
            "Fehler: --raw und --alle-seiten sind nicht kombinierbar "
            "(Roh-JSON ist immer Single-Page-Output der API).\n"
        )
        return 2

    norm_original = None
    if args.norm:
        args.norm, norm_original = normalize_norm(args.norm)

    if args.raw:
        url = build_url(args)
        raw = fetch_with_retries(url, args)
        if raw is None:
            return 1
        json.dump(raw, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
        return 0

    norm = fetch_pages_normalized(args)
    if norm is None:
        return 1

    if norm_original is not None:
        norm["norm_normalized"] = {"from": norm_original, "to": args.norm}

    websearch_query: str | None = None
    if args.suchworte and norm["total_hits"] == 0:
        websearch_query = build_websearch_query(args)
        norm["websearch_query"] = websearch_query
        norm["hint"] = SUCHWORTE_NULL_HINT_TEMPLATE.format(
            query=websearch_query,
            query_url=urllib.parse.quote_plus(websearch_query),
        )

    if args.json:
        json.dump(norm, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write("\n")
    else:
        if norm_original is not None:
            sys.stdout.write(
                f"_Hinweis: Norm-Eingabe automatisch ergänzt — "
                f"`{norm_original}` → `{args.norm}`._\n\n"
            )
        sys.stdout.write(render_markdown(norm))
        if websearch_query is not None:
            sys.stdout.write("\n" + norm["hint"] + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
