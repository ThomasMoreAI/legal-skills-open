"""
Texas Secretary of State / Comptroller entity search script.

Purpose: Search Texas business registries for entities matching a name.
         Uses the TX Comptroller franchise tax search (public) and
         links to TX SOS for incorporation details.
Author:  Reinaldo Chaves <reichaves@gmail.com>
Date:    2026-04-30
Dependencies: requests, click, beautifulsoup4
Usage:   python texas_comptroller.py --variations identity-variations.json [--output findings/tx.json]
         python texas_comptroller.py --name "Ferreira Global Energy"
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

import click
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("texas_comptroller")

TX_COA_SEARCH_URL = "https://mycpa.cpa.state.tx.us/coa/searchGeneral.do"
TX_SOS_BASE = "https://www.sos.state.tx.us/corp/sosda/index.shtml"
RATE_LIMIT_SECONDS = 2.5
MAX_RETRIES = 3
BACKOFF_FACTOR = 2.0

USER_AGENTS = [
    (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    (
        "Mozilla/5.0 (X11; Linux x86_64) "
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


def _search_tx_coa(session: requests.Session, name: str) -> list[dict[str, Any]]:
    """Search TX Comptroller franchise tax database by entity name."""
    logger.info("Searching TX Comptroller for: %s", name)
    session.headers["User-Agent"] = _next_user_agent()
    params = {
        "name": name,
        "btnSearch": "Search",
        "search": "name",
    }
    time.sleep(RATE_LIMIT_SECONDS)
    try:
        response = session.get(TX_COA_SEARCH_URL, params=params, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        logger.error("TX Comptroller search failed for '%s': %s", name, exc)
        return []

    return _parse_tx_results(response.text)


def _parse_tx_results(html: str) -> list[dict[str, Any]]:
    """Parse TX Comptroller search results HTML."""
    soup = BeautifulSoup(html, "html.parser")
    results: list[dict[str, Any]] = []

    # TX COA results are in a table with class "table"
    table = soup.find("table", class_="table")
    if not table:
        return results

    headers_row = table.find("tr")
    if not headers_row:
        return results
    headers = [th.get_text(strip=True).lower() for th in headers_row.find_all(["th", "td"])]

    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        if not cells:
            continue

        record: dict[str, Any] = {}
        for idx, cell in enumerate(cells):
            if idx < len(headers):
                record[headers[idx]] = cell.get_text(strip=True)

        # Extract taxpayer number if available as link
        first_link = cells[0].find("a") if cells else None
        if first_link:
            href = first_link.get("href", "")
            # TX COA uses ?taxpayer=XXXXXXXXXX in detail links
            if "taxpayer=" in href:
                taxpayer_num = href.split("taxpayer=")[-1].split("&")[0]
                record["taxpayer_number"] = taxpayer_num

        if record:
            results.append(record)

    return results


def _normalize_hit(raw: dict[str, Any], variation: str) -> dict[str, Any]:
    """Normalize a TX Comptroller result into findings schema format."""
    taxpayer_num = raw.get("taxpayer_number", raw.get("taxpayer number", ""))
    entity_name = raw.get("taxpayer name", raw.get("name", ""))
    return {
        "variation_matched": variation,
        "match_type": "fuzzy",
        "source_id": taxpayer_num,
        "source_url": f"https://mycpa.cpa.state.tx.us/coa/searchGeneral.do?name={variation}",
        "confidence": "indicio",
        "raw_record": {**raw, "_state": "TX", "_registry": "TX-Comptroller"},
        "normalized": {
            "entity_name": entity_name,
            "entity_type": raw.get("entity type", ""),
            "state": "TX",
            "state_registry": "TX",
        },
    }


def run_search(variations: list[str]) -> dict[str, Any]:
    """Run TX Comptroller search for all name variations."""
    session = _build_session()
    hits: list[dict[str, Any]] = []
    no_hits: list[str] = []
    queries_executed = 0
    status = "ok"
    error_message = None

    for variation in variations:
        found_something = False
        try:
            raw_results = _search_tx_coa(session, variation)
            queries_executed += 1
            for r in raw_results:
                hits.append(_normalize_hit(r, variation))
                found_something = True
        except Exception as exc:  # noqa: BLE001
            logger.error("Unexpected error for '%s': %s", variation, exc)
            status = "partial"
            error_message = str(exc)

        if not found_something:
            no_hits.append(variation)

    return {
        "base": "TX-COMPTROLLER",
        "consulted_at": datetime.now(tz=timezone.utc).isoformat(),
        "queries_executed": queries_executed,
        "status": status,
        "error_message": error_message,
        "hits": hits,
        "no_hits": no_hits,
        "legal_context": [
            (
                "Texas exige registro de franchise tax para empresas que operam no estado. "
                "O Comptroller divulga nome, status de franchise tax e endereço postal. "
                "Officers de LLCs não são divulgados — apenas incorporadoras tipo Corporation "
                "listam officers no Texas SOS."
            ),
            (
                "Para investigações de petróleo e gás em TX, consultar separadamente a "
                "Railroad Commission of Texas (rrc.texas.gov) que registra operadores de poço."
            ),
        ],
        "next_frontiers": [
            "Para empresas Corp (não LLC): buscar officers no TX SOS (sos.state.tx.us)",
            "Para petróleo e gás: verificar Railroad Commission TX (rrc.texas.gov)",
            "Empresas 'Forfeited' (franchise tax não pago) podem indicar abandono ou reestruturação",
            "Cruzar nome da empresa TX com Sunbiz FL para verificar presença em múltiplos estados",
        ],
        "methodology_note": (
            "Busca realizada via TX Comptroller franchise tax search (mycpa.cpa.state.tx.us). "
            "Campo pesquisado: nome da entidade. TX não oferece busca pública por officer de LLC. "
            "Para incorporações, o TX SOS (sos.state.tx.us) tem dados adicionais mas "
            "requer acesso via SOSDirect (USD 1/consulta)."
        ),
    }


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
    help="Entity name to search in Texas (alternative to --variations)",
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
    """Search Texas Comptroller for entity names related to a Brazilian person."""
    if not variations_path and not single_name:
        raise click.UsageError("Provide --variations or --name")

    if variations_path:
        data = json.loads(variations_path.read_text(encoding="utf-8"))
        variations: list[str] = [v["name_string"] for v in data.get("variations", [])]
    else:
        variations = [single_name]  # type: ignore[list-item]

    logger.info("Starting TX Comptroller search for %d variations", len(variations))
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
