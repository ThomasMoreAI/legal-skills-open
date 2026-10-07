"""
Florida Sunbiz (Division of Corporations) search script.

Purpose: Search Sunbiz for a person appearing as officer/director/registered
         agent in Florida corporations, LLCs, and other entities.
Author:  Reinaldo Chaves <reichaves@gmail.com>
Date:    2026-04-30
Dependencies: requests, click, beautifulsoup4
Usage:   python florida_sunbiz.py --variations identity-variations.json [--output findings/fl.json]
         python florida_sunbiz.py --name "Carlos Ferreira"
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

import click
import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("florida_sunbiz")

SUNBIZ_BASE = "https://search.sunbiz.org"
OFFICER_SEARCH_URL = f"{SUNBIZ_BASE}/Inquiry/CorporationSearch/SearchResults"
RATE_LIMIT_SECONDS = 2.0
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
    (
        "Mozilla/5.0 (X11; Linux x86_64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
]
_ua_index = 0


def _next_user_agent() -> str:
    """Rotate through user agents."""
    global _ua_index  # noqa: PLW0603
    ua = USER_AGENTS[_ua_index % len(USER_AGENTS)]
    _ua_index += 1
    return ua


def _build_session() -> requests.Session:
    """Build a requests Session with retry and backoff."""
    session = requests.Session()
    retry_strategy = Retry(
        total=MAX_RETRIES,
        backoff_factor=BACKOFF_FACTOR,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"],
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def _search_officers(session: requests.Session, name: str) -> list[dict[str, Any]]:
    """Search Sunbiz for a person as officer/director/registered agent."""
    logger.info("Searching Sunbiz officers for: %s", name)
    params = {
        "inquiryType": "OfficerDirector",
        "inquiryDirectionType": "ForwardList",
        "searchNameOrder": name.upper(),
        "activeOnly": "false",
    }
    session.headers["User-Agent"] = _next_user_agent()
    time.sleep(RATE_LIMIT_SECONDS)
    try:
        response = session.get(OFFICER_SEARCH_URL, params=params, timeout=30)
        response.raise_for_status()
    except requests.exceptions.RequestException as exc:
        logger.error("Sunbiz officer search failed for '%s': %s", name, exc)
        return []

    return _parse_officer_results(response.text, name)


def _parse_officer_results(html: str, query_name: str) -> list[dict[str, Any]]:
    """Parse Sunbiz HTML search results for officer/director search."""
    soup = BeautifulSoup(html, "html.parser")
    results: list[dict[str, Any]] = []

    # Sunbiz results table has class "dataTable"
    table = soup.find("table", class_="dataTable")
    if not table:
        return results

    rows = table.find_all("tr")[1:]  # skip header
    for row in rows:
        cells = row.find_all("td")
        if len(cells) < 4:
            continue

        entity_link = cells[0].find("a")
        entity_name = entity_link.get_text(strip=True) if entity_link else cells[0].get_text(strip=True)
        entity_href = entity_link.get("href", "") if entity_link else ""
        entity_url = f"{SUNBIZ_BASE}{entity_href}" if entity_href else ""
        document_number = cells[1].get_text(strip=True)
        status = cells[2].get_text(strip=True)
        officer_name = cells[3].get_text(strip=True) if len(cells) > 3 else ""

        # Extract entity type from document number prefix
        entity_type_map = {
            "P": "Profit Corporation",
            "N": "Non-Profit Corporation",
            "L": "Limited Liability Company",
            "A": "Foreign Corporation",
            "B": "LP / LLP",
        }
        prefix = document_number[0] if document_number else ""
        entity_type = entity_type_map.get(prefix, "Unknown")

        # Determine match type: exact if officer name contains all words of query
        query_words = set(query_name.upper().split())
        officer_words = set(officer_name.upper().split())
        match_type = "exact" if query_words.issubset(officer_words) else "fuzzy"

        results.append({
            "entity_name": entity_name,
            "document_number": document_number,
            "entity_type": entity_type,
            "status": status,
            "officer_name": officer_name,
            "entity_url": entity_url,
            "match_type": match_type,
        })

    return results


def _normalize_hit(raw: dict[str, Any], variation: str) -> dict[str, Any]:
    """Normalize a raw Sunbiz result into findings schema format."""
    doc_num = raw.get("document_number", "")
    return {
        "variation_matched": variation,
        "match_type": raw.get("match_type", "fuzzy"),
        "source_id": doc_num,
        "source_url": raw.get("entity_url", f"https://search.sunbiz.org/Inquiry/CorporationSearch/SearchResultDetail?inquiryType=EntityName&inquiryDirectionType=ForwardList&searchNameOrder={quote(raw.get('entity_name', ''))}&aggregateId={doc_num}"),
        "confidence": "confirmado" if raw.get("match_type") == "exact" else "indicio",
        "raw_record": {**raw, "_state": "FL", "_registry": "Sunbiz"},
        "normalized": {
            "full_name": raw.get("officer_name", ""),
            "entity_name": raw.get("entity_name", ""),
            "entity_type": raw.get("entity_type", ""),
            "role": "officer/director",
            "state": "FL",
            "state_registry": "FL",
        },
    }


def run_search(variations: list[str]) -> dict[str, Any]:
    """Run Sunbiz officer search for all name variations."""
    session = _build_session()
    hits: list[dict[str, Any]] = []
    no_hits: list[str] = []
    queries_executed = 0
    status = "ok"
    error_message = None

    for variation in variations:
        found_something = False
        try:
            raw_results = _search_officers(session, variation)
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
        "base": "FL-SUNBIZ",
        "consulted_at": datetime.now(tz=timezone.utc).isoformat(),
        "queries_executed": queries_executed,
        "status": status,
        "error_message": error_message,
        "hits": hits,
        "no_hits": no_hits,
        "legal_context": [
            (
                "Florida exige que officers e diretores de empresas sejam listados "
                "nos Annual Reports. Dados são públicos via Sunbiz (Division of Corporations)."
            ),
        ],
        "next_frontiers": [
            "Para cada empresa ativa encontrada: verificar Annual Reports para timeline de officers",
            "Verificar registered agent — pode ser escritório jurídico que indica outros vínculos",
            "Empresas com status 'Inactive' podem indicar encerramento ou mudança de estrutura",
        ],
        "methodology_note": (
            "Busca realizada via Sunbiz officer/director search (search.sunbiz.org). "
            "Campo pesquisado: OfficerDirector (nome de officer, director ou registered agent). "
            "Inclui entidades ativas e inativas. Case-insensitive. "
            "Sunbiz usa busca por prefixo — nomes incompletos retornam mais resultados."
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
    help="Single name to search (alternative to --variations)",
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
    """Search Florida Sunbiz for a person as officer/director."""
    if not variations_path and not single_name:
        raise click.UsageError("Provide --variations or --name")

    if variations_path:
        data = json.loads(variations_path.read_text(encoding="utf-8"))
        variations: list[str] = [v["name_string"] for v in data.get("variations", [])]
    else:
        variations = [single_name]  # type: ignore[list-item]

    logger.info("Starting Sunbiz search for %d variations", len(variations))
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
