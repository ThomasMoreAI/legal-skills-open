"""
Delaware Division of Corporations entity search script.

Purpose: Search Delaware's corporate registry for entities matching a name.
         NOTE: Delaware deliberately limits public disclosure — this script
         returns entity existence and basic metadata only, NOT officers or owners.
Author:  Reinaldo Chaves <reichaves@gmail.com>
Date:    2026-04-30
Dependencies: requests, click, beautifulsoup4
Usage:   python delaware_corp.py --variations identity-variations.json [--output findings/de.json]
         python delaware_corp.py --name "Ferreira Global Energy"
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import click
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("delaware_corp")

DE_SEARCH_URL = "https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx"
RATE_LIMIT_SECONDS = 3.0  # Delaware server is slow — be extra cautious
MAX_RETRIES = 3
BACKOFF_FACTOR = 2.0

USER_AGENTS = [
    (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
]
_ua_index = 0


def _next_user_agent() -> str:
    global _ua_index  # noqa: PLW0603
    ua = USER_AGENTS[_ua_index % len(USER_AGENTS)]
    _ua_index += 1
    return ua


def _build_session() -> requests.Session:
    session = requests.Session()
    retry_strategy = Retry(
        total=MAX_RETRIES,
        backoff_factor=BACKOFF_FACTOR,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST"],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def _get_viewstate(session: requests.Session) -> tuple[str, str, str]:
    """Fetch the Delaware search page to extract ASP.NET ViewState tokens."""
    session.headers["User-Agent"] = _next_user_agent()
    time.sleep(RATE_LIMIT_SECONDS)
    try:
        response = session.get(DE_SEARCH_URL, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        logger.error("Failed to load Delaware search page: %s", exc)
        return ("", "", "")

    soup = BeautifulSoup(response.text, "html.parser")
    viewstate = soup.find("input", {"id": "__VIEWSTATE"})
    viewstate_gen = soup.find("input", {"id": "__VIEWSTATEGENERATOR"})
    event_validation = soup.find("input", {"id": "__EVENTVALIDATION"})

    return (
        viewstate["value"] if viewstate else "",
        viewstate_gen["value"] if viewstate_gen else "",
        event_validation["value"] if event_validation else "",
    )


def _search_entity(
    session: requests.Session,
    name: str,
    viewstate: str,
    viewstate_gen: str,
    event_validation: str,
) -> list[dict[str, Any]]:
    """POST search form to Delaware corporate search."""
    logger.info("Searching Delaware corps for: %s", name)
    session.headers["User-Agent"] = _next_user_agent()
    session.headers["Referer"] = DE_SEARCH_URL
    time.sleep(RATE_LIMIT_SECONDS)

    form_data = {
        "__VIEWSTATE": viewstate,
        "__VIEWSTATEGENERATOR": viewstate_gen,
        "__EVENTVALIDATION": event_validation,
        "ctl00$ContentPlaceHolder1$txtEntityName": name,
        "ctl00$ContentPlaceHolder1$btnSubmit": "Search",
    }

    try:
        response = session.post(DE_SEARCH_URL, data=form_data, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        logger.error("Delaware search POST failed for '%s': %s", name, exc)
        return []

    return _parse_de_results(response.text)


def _parse_de_results(html: str) -> list[dict[str, Any]]:
    """Parse Delaware search results HTML."""
    soup = BeautifulSoup(html, "html.parser")
    results: list[dict[str, Any]] = []

    # Delaware results are in a GridView table
    table = soup.find("table", {"id": "ctl00_ContentPlaceHolder1_SearchResults_gvSearchResults"})
    if not table:
        # Check for "no results" message
        no_result = soup.find("span", {"id": "ctl00_ContentPlaceHolder1_SearchResults_lblNoResults"})
        if no_result:
            logger.info("Delaware returned no results")
        return results

    rows = table.find_all("tr")[1:]  # skip header
    for row in rows:
        cells = row.find_all("td")
        if len(cells) < 3:
            continue

        entity_link = cells[0].find("a")
        entity_name = entity_link.get_text(strip=True) if entity_link else cells[0].get_text(strip=True)
        file_number = cells[1].get_text(strip=True)
        entity_type = cells[2].get_text(strip=True)

        results.append({
            "entity_name": entity_name,
            "file_number": file_number,
            "entity_type": entity_type,
        })

    return results


def _normalize_hit(raw: dict[str, Any], variation: str) -> dict[str, Any]:
    """Normalize a Delaware result into findings schema format."""
    file_num = raw.get("file_number", "")
    return {
        "variation_matched": variation,
        "match_type": "fuzzy",  # DE search is by entity name, not officer
        "source_id": file_num,
        "source_url": f"https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx",
        "confidence": "indicio",  # DE officer data is not public
        "raw_record": {**raw, "_state": "DE", "_registry": "DE-DoC"},
        "normalized": {
            "entity_name": raw.get("entity_name", ""),
            "entity_type": raw.get("entity_type", ""),
            "state": "DE",
            "state_registry": "DE",
        },
    }


def run_search(variations: list[str]) -> dict[str, Any]:
    """Run Delaware search for all name variations."""
    session = _build_session()
    hits: list[dict[str, Any]] = []
    no_hits: list[str] = []
    queries_executed = 0
    status = "ok"
    error_message = None

    # NOTE: For Delaware, variations should include COMPANY names, not just person names.
    # Person names are searched as entity names (company may be named after person).
    viewstate, viewstate_gen, event_validation = _get_viewstate(session)
    if not viewstate:
        return {
            "base": "DE-CORPS",
            "consulted_at": datetime.now(tz=timezone.utc).isoformat(),
            "queries_executed": 0,
            "status": "error",
            "error_message": "Failed to load Delaware search page (could not get ViewState)",
            "hits": [],
            "no_hits": variations,
            "legal_context": [DE_LEGAL_CONTEXT],
            "next_frontiers": DE_NEXT_FRONTIERS,
            "methodology_note": DE_METHODOLOGY_NOTE,
        }

    for variation in variations:
        found_something = False
        try:
            raw_results = _search_entity(
                session, variation, viewstate, viewstate_gen, event_validation
            )
            queries_executed += 1
            for r in raw_results:
                hits.append(_normalize_hit(r, variation))
                found_something = True

            # Refresh viewstate for next search
            viewstate, viewstate_gen, event_validation = _get_viewstate(session)

        except Exception as exc:  # noqa: BLE001
            logger.error("Unexpected error for '%s': %s", variation, exc)
            status = "partial"
            error_message = str(exc)

        if not found_something:
            no_hits.append(variation)

    return {
        "base": "DE-CORPS",
        "consulted_at": datetime.now(tz=timezone.utc).isoformat(),
        "queries_executed": queries_executed,
        "status": status,
        "error_message": error_message,
        "hits": hits,
        "no_hits": no_hits,
        "legal_context": [DE_LEGAL_CONTEXT],
        "next_frontiers": DE_NEXT_FRONTIERS,
        "methodology_note": DE_METHODOLOGY_NOTE,
    }


DE_LEGAL_CONTEXT = (
    "Delaware NÃO divulga officers, diretores ou beneficial owners publicamente. "
    "Registro de existência de empresa confirma apenas que a entidade existe em DE. "
    "Para vincular pessoa a empresa DE, cruzar com: Sunbiz (FL) para foreign corps, "
    "FARA/LDA se lobbyou, ou SEC EDGAR se emitiu securities. "
    "FinCEN BOI (pós-2024) é confidencial e não acessível ao público."
)

DE_NEXT_FRONTIERS = [
    "Buscar a empresa encontrada em FL Sunbiz como 'Foreign Profit Corporation'",
    "Verificar SEC EDGAR (sec.gov/cgi-bin/browse-edgar) se a empresa emitiu securities",
    "Verificar OpenCorporates para cross-reference com outras jurisdições",
    "Para beneficial owner pós-2024: solicitar via FOIA ou aguardar divulgação judicial",
]

DE_METHODOLOGY_NOTE = (
    "Busca realizada via formulário Delaware Division of Corporations Entity Search "
    "(icis.corp.delaware.gov). Campo pesquisado: EntityName. "
    "Delaware não oferece busca por officer — resultados são EMPRESAS com nome similar, "
    "não pessoas. Usar para descobrir se existe empresa com nome do alvo constituída em DE."
)


@click.command()
@click.option(
    "--variations",
    "variations_path",
    type=click.Path(exists=True, path_type=Path),
    default=None,
    help="Path to identity-variations.json",
)
@click.option(
    "--name",
    "single_name",
    default=None,
    help="Entity name to search in Delaware (alternative to --variations)",
)
@click.option(
    "--output",
    "output_path",
    type=click.Path(path_type=Path),
    default=None,
    help="Output path for findings JSON (default: stdout)",
)
def main(
    variations_path: Path | None,
    single_name: str | None,
    output_path: Path | None,
) -> None:
    """Search Delaware Division of Corporations for entity names."""
    if not variations_path and not single_name:
        raise click.UsageError("Provide --variations or --name")

    if variations_path:
        data = json.loads(variations_path.read_text(encoding="utf-8"))
        variations: list[str] = [v["name_string"] for v in data.get("variations", [])]
    else:
        variations = [single_name]  # type: ignore[list-item]

    logger.info("Starting Delaware search for %d name variations", len(variations))
    findings = run_search(variations)

    output_json = json.dumps(findings, ensure_ascii=False, indent=2)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output_json, encoding="utf-8")
        logger.info("Findings written to %s", output_path)
    else:
        click.echo(output_json)


if __name__ == "__main__":
    main()
