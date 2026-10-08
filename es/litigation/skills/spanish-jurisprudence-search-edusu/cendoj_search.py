#!/usr/bin/env python3
"""CENDOJ jurisprudence search — reverse-engineered Struts/IDOL API.

The official Spanish jurisprudence database at poderjudicial.es exposes no
public REST API. This module wraps the internal `search.action` endpoint that
the JS frontend uses, handling the wire-format quirks (literal parens,
pipe-wrapped multi-values, trailing pipe in COMUNIDAD, etc.) that broke naive
attempts.

Usage:
    cendoj_search.py "violencia género extinción" --jurisdiccion SOCIAL --comunidad CANARIAS
    cendoj_search.py "ECLI:ES:TS:2024:1234"
    cendoj_search.py "art 41 ET" --comunidad CANARIAS --per-page 20

Output: JSON to stdout with `total` and `items[]` (each: ref, db, fechares, url, text).
"""
from __future__ import annotations

import argparse
import http.cookiejar
import json
import re
import sys
import time
from html.parser import HTMLParser
from urllib import request
from urllib.parse import quote, urlsplit

BASE = "https://www.poderjudicial.es/search"
_u = urlsplit(BASE)
ORIGIN = f"{_u.scheme}://{_u.netloc}"
UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
)

JURISDICCIONES = {"CIVIL", "PENAL", "CONTENCIOSO", "SOCIAL", "MILITAR", "ESPECIAL"}
COMUNIDADES = {
    "CANARIAS", "MADRID", "CATALUÑA", "ANDALUCÍA", "ARAGÓN", "ASTURIAS",
    "BALEARES", "CANTABRIA", "CASTILLA_LA_MANCHA", "CASTILLA_Y_LEÓN",
    "CEUTA", "COMUNIDAD_VALENCIANA", "EXTREMADURA", "GALICIA", "LA_RIOJA",
    "MELILLA", "MURCIA", "NAVARRA", "PAÍS_VASCO",
}


def _enc(s: str) -> str:
    """Wire-format encoder.

    Two non-obvious requirements observed when capturing the real XHR:
    - Parens '(' ')' must stay literal — IDOL parses them as syntax inside
      VALUESCOMUNIDAD; if percent-encoded the search is rejected as invalid.
    - Spaces must be '+' (form-urlencoded), not '%20' (which `urllib.quote`
      emits by default). Same: '%20' triggers "búsqueda no es válida".
    Everything else (including ':' inside `sort`) is encoded normally.
    """
    return quote(s, safe="()").replace("%20", "+")


class CendojSession:
    def __init__(self) -> None:
        cj = http.cookiejar.CookieJar()
        self.opener = request.build_opener(request.HTTPCookieProcessor(cj))
        self.opener.addheaders = [("User-Agent", UA)]
        self._bootstrapped = False

    def bootstrap(self) -> None:
        with self.opener.open(f"{BASE}/indexAN.jsp", timeout=15) as r:
            r.read()
        self._bootstrapped = True

    def search(
        self,
        text: str,
        *,
        jurisdiccion: str | list[str] | None = None,
        comunidad: str | None = None,
        fecha_desde: str | None = None,
        fecha_hasta: str | None = None,
        roj: str | None = None,
        ecli: str | None = None,
        ponente: str | None = None,
        start: int = 1,
        per_page: int = 10,
        sort: str = "IN_FECHARESOLUCION:decreasing",
    ) -> dict:
        if not self._bootstrapped:
            self.bootstrap()

        parts = [
            "action=query",
            f"sort={_enc(sort)}",
            f"recordsPerPage={per_page}",
            "databasematch=AN",
            f"start={start}",
            f"TEXT={_enc(text)}",
        ]
        if jurisdiccion:
            vals = [jurisdiccion] if isinstance(jurisdiccion, str) else list(jurisdiccion)
            for v in vals:
                if v not in JURISDICCIONES:
                    raise ValueError(f"jurisdiccion must be one of {JURISDICCIONES}, got {v!r}")
            parts.append(f"JURISDICCION={_enc('|' + '|'.join(vals) + '|')}")
        if comunidad:
            if comunidad not in COMUNIDADES:
                raise ValueError(f"comunidad must be one of {COMUNIDADES}, got {comunidad!r}")
            # Wire format observed: "CANARIAS(C) | "  (name + "(C)" + space + "|" + trailing space)
            parts.append(f"VALUESCOMUNIDAD={_enc(comunidad + '(C) | ')}")
        for key, value in (
            ("FECHARESOLUCIONDESDE", fecha_desde),
            ("FECHARESOLUCIONHASTA", fecha_hasta),
            ("ROJ", roj),
            ("ECLI", ecli),
            ("PONENTE", ponente),
        ):
            if value:
                parts.append(f"{key}={_enc(value)}")

        body = "&".join(parts).encode("utf-8")

        req = request.Request(
            f"{BASE}/search.action",
            data=body,
            headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With": "XMLHttpRequest",
                "Accept": "text/html, */*; q=0.01",
                "Referer": f"{BASE}/indexAN.jsp",
                "Origin": ORIGIN,
            },
        )
        with self.opener.open(req, timeout=20) as r:
            html = r.read().decode("utf-8", errors="replace")

        return self._parse(html, body=body.decode())

    @staticmethod
    def _parse(html: str, *, body: str = "") -> dict:
        if "búsqueda no es válida" in html:
            return {
                "error": "search_rejected",
                "message": "El servidor rechazó la búsqueda (formato de body inválido o estado de sesión)",
                "sent_body": body,
            }
        if "algo ha salido mal" in html or 'class="errorMessage"' in html:
            return {
                "error": "server_error_or_waf",
                "message": "El servidor devolvió la página genérica de error (probablemente WAF/rate-limit). Espera unos minutos.",
            }

        total_m = re.search(r'data-totalhits="(\d+)"', html)
        total = int(total_m.group(1)) if total_m else 0

        items = []
        for m in _iter_doc_blocks(html):
            attrs = m["attrs"]
            inner = m["inner"]
            link_m = re.search(r'data-link="([^"]+)"', inner)
            url = link_m.group(1) if link_m else None
            text = _strip_html(inner)
            items.append(
                {
                    "ref": attrs.get("data-ref"),
                    "db": attrs.get("data-db"),
                    "fechares": attrs.get("data-fechares"),
                    "url": url,
                    "text": text,
                }
            )

        return {"total": total, "count": len(items), "items": items}


def _iter_doc_blocks(html: str):
    """Yield each `<div class="row searchresult doc" ...>...</div>` block.

    Uses a small state machine over the marker `class="row searchresult doc"`,
    counting nested <div> tags to find the matching close. This is more robust
    than regex on the closing tag because the body may itself contain nested divs.
    """
    pattern = re.compile(r'<div\s+class="row searchresult doc"([^>]*)>')
    for opening in pattern.finditer(html):
        attrs_str = opening.group(1)
        attrs = dict(re.findall(r'(\w[\w-]*)="([^"]*)"', attrs_str))
        i = opening.end()
        depth = 1
        n = len(html)
        while i < n and depth > 0:
            next_open = html.find("<div", i)
            next_close = html.find("</div>", i)
            if next_close == -1:
                break
            if next_open != -1 and next_open < next_close:
                depth += 1
                i = next_open + 4
            else:
                depth -= 1
                if depth == 0:
                    yield {"attrs": attrs, "inner": html[opening.end() : next_close]}
                    break
                i = next_close + 6


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self.parts)).strip()


def _strip_html(html: str) -> str:
    p = _TextExtractor()
    p.feed(html)
    return p.text()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=(
            "Search Spanish jurisprudence at CENDOJ (Poder Judicial). "
            "Returns JSON. Respects rate limits — there's a WAF that blocks "
            "after a few rapid requests from the same IP."
        ),
    )
    p.add_argument("query", help="free-text query")
    p.add_argument(
        "-j",
        "--jurisdiccion",
        choices=sorted(JURISDICCIONES),
        action="append",
        help="filter by jurisdicción (repeatable for multiple)",
    )
    p.add_argument(
        "-c",
        "--comunidad",
        choices=sorted(COMUNIDADES),
        metavar="COMUNIDAD",
        help="autonomous community (e.g. CANARIAS, MADRID, CATALUÑA)",
    )
    p.add_argument("--desde", help="date from (dd/mm/yyyy)")
    p.add_argument("--hasta", help="date to (dd/mm/yyyy)")
    p.add_argument("--roj", help="exact ROJ (e.g. 'STSJ ICAN 287/2026')")
    p.add_argument("--ecli", help="exact ECLI (e.g. 'ECLI:ES:TS:2014:3877')")
    p.add_argument("--ponente", help="ponente name substring")
    p.add_argument("--start", type=int, default=1, help="pagination offset (1, 11, 21...)")
    p.add_argument("--per-page", type=int, default=10, help="results per page")
    p.add_argument(
        "--sort",
        default="IN_FECHARESOLUCION:decreasing",
        help="IDOL sort expression (default: most recent first)",
    )
    p.add_argument("--delay", type=float, default=0.5, help="seconds to wait after bootstrap")
    p.add_argument("--truncate", type=int, default=0, help="truncate `text` field to N chars (0 = no limit)")
    args = p.parse_args(argv)

    s = CendojSession()
    try:
        s.bootstrap()
    except Exception as e:
        print(json.dumps({"error": "bootstrap_failed", "message": str(e)}, ensure_ascii=False))
        return 2
    time.sleep(args.delay)

    try:
        result = s.search(
            args.query,
            jurisdiccion=args.jurisdiccion,
            comunidad=args.comunidad,
            fecha_desde=args.desde,
            fecha_hasta=args.hasta,
            roj=args.roj,
            ecli=args.ecli,
            ponente=args.ponente,
            start=args.start,
            per_page=args.per_page,
            sort=args.sort,
        )
    except Exception as e:
        print(json.dumps({"error": "search_failed", "message": str(e)}, ensure_ascii=False))
        return 2

    if args.truncate and "items" in result:
        for it in result["items"]:
            if it.get("text"):
                it["text"] = it["text"][: args.truncate]

    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0 if "error" not in result else 1


if __name__ == "__main__":
    sys.exit(main())
