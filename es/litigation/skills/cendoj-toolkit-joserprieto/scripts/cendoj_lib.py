"""
cendoj_lib — pure functions shared by the CLI scripts.

Anything testable without IO or browser automation lives here:

- URL construction
- Result text parsing (ECLI, ROJ, dates, ponente, ...)
- Filename sanitization
- PDF validation (magic bytes)
- SHA-256 hashing
- Constants (rate limits, caps)

The CLI scripts (`cendoj_search.py`, `cendoj_download.py`,
`cendoj_pdf_to_md.py`) import from here so the same logic stays
single-sourced and unit-testable.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

CENDOJ_BASE = "https://www.poderjudicial.es"
SEARCH_URL = f"{CENDOJ_BASE}/search/indexAN.jsp"

# Rate limit and download caps (CENDOJ robots.txt + skill safety policy).
MIN_DELAY_SECONDS = 5.0
DEFAULT_MAX_DOWNLOADS = 50
HARD_CAP_MAX_DOWNLOADS = 200

# User agents
BROWSER_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)
COOPERATIVE_UA = "cendoj-toolkit/0.1.0 (+https://github.com/joserprieto/ai-skills)"

LEGAL_NOTICE = """
============================================================
CENDOJ — Legal Notice (uso particular only)
============================================================
Las resoluciones se difunden a efectos de conocimiento y consulta
para uso particular del usuario.

NO se permite uso comercial ni descarga masiva.

Reutilización comercial requiere autorización formal del CGPJ.

Robots.txt: Crawl-delay: 5s (enforced as hard minimum).
============================================================
"""

_MONTHS_ES = {
    "enero": "01", "febrero": "02", "marzo": "03", "abril": "04",
    "mayo": "05", "junio": "06", "julio": "07", "agosto": "08",
    "septiembre": "09", "octubre": "10", "noviembre": "11",
    "diciembre": "12",
}


# ---------------------------------------------------------------------------
# URL construction
# ---------------------------------------------------------------------------

def build_pdf_url(reference: str, optimize: str) -> str:
    """Build the CENDOJ direct-PDF download URL.

    Args:
        reference: hex hash from the openDocument URL (16 or 32 chars)
        optimize: YYYYMMDD date stamp from the openDocument URL

    Returns:
        Full URL to the public PDF endpoint.
    """
    if not reference or not optimize:
        raise ValueError("reference and optimize must be non-empty")
    return (
        f"{CENDOJ_BASE}/search/contenidos.action"
        f"?action=accessToPDF"
        f"&publicinterface=true"
        f"&tab=AN"
        f"&reference={reference}"
        f"&encode=true"
        f"&optimize={optimize}"
        f"&databasematch=AN"
    )


def parse_open_document_url(url: str) -> tuple[str, str] | None:
    """Extract (reference, optimize) from an openDocument URL.

    Returns None if the URL doesn't match the expected pattern.
    """
    m = re.search(r"openDocument/([a-f0-9]+)/(\d{8})", url)
    if not m:
        return None
    return m.group(1), m.group(2)


# ---------------------------------------------------------------------------
# Result metadata parsing
# ---------------------------------------------------------------------------

def parse_result_text(text: str) -> dict[str, str | None]:
    """Extract structured metadata from a result block's text content."""
    out: dict[str, str | None] = {}

    ecli_match = re.search(r"ECLI:ES:[A-Z]+:\d{4}:\d+[A-Z]?", text)
    out["ecli"] = ecli_match.group(0) if ecli_match else None

    res_num = re.search(r"N[ºo]\s*de\s*Resoluci[oó]n:\s*([0-9/]+)", text)
    out["resolution_number"] = res_num.group(1).strip() if res_num else None

    appeal = re.search(r"N[ºo]\s*Recurso:\s*([0-9/]+)", text)
    out["appeal_number"] = appeal.group(1).strip() if appeal else None

    municipio = re.search(r"Municipio:\s*([^\-\n]+?)(?:\s*-|\n|$)", text)
    out["city"] = municipio.group(1).strip() if municipio else None

    ponente = re.search(r"Ponente:\s*([^\-\n]+?)(?:\s*-|\n|$)", text)
    out["ponente"] = ponente.group(1).strip() if ponente else None

    resumen = re.search(r"RESUMEN:\s*([^\n]+)", text)
    if not resumen:
        resumen = re.search(r"Resumen Autom[áa]tico:\s*([^\n]+)", text)
    out["summary"] = resumen.group(1)[:300].strip() if resumen else None

    return out


def parse_title(title: str) -> dict[str, str | None]:
    """Parse a CENDOJ result title.

    Example title:
        ``STSJ Galicia, a 06 de febrero de 2026 - ROJ: STSJ GAL 1040/2026``

    Returns a dict with keys: raw_title, roj, tribunal, date_iso.
    """
    out: dict[str, str | None] = {"raw_title": title}

    roj_match = re.search(r"ROJ:\s*([A-Z]+\s+[A-Z]+\s+\d+/\d{4})", title)
    out["roj"] = roj_match.group(1).strip() if roj_match else None

    tribunal_match = re.match(r"^([A-Z]+(?:\s+[A-Za-zñáéíóú]+)?)", title)
    out["tribunal"] = tribunal_match.group(1).strip() if tribunal_match else None

    date_match = re.search(
        r"a\s+(\d{1,2})\s+de\s+([a-zñáéíóú]+)\s+de\s+(\d{4})",
        title,
        flags=re.IGNORECASE,
    )
    if date_match:
        day, month_es, year = date_match.groups()
        month_num = _MONTHS_ES.get(month_es.lower())
        out["date_iso"] = f"{year}-{month_num}-{int(day):02d}" if month_num else None
    else:
        out["date_iso"] = None

    return out


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------

def safe_filename(entry: dict[str, Any], index: int) -> str:
    """Generate a safe `.pdf` filename for an entry.

    Preference order: ROJ → ECLI → ``sentencia-{index}``.

    Always prefixed with a 2-digit zero-padded index for stable ordering.
    """
    roj = entry.get("roj") or ""
    ecli = entry.get("ecli") or ""
    base = roj or ecli or f"sentencia-{index:03d}"
    base = re.sub(r"[^A-Za-z0-9]+", "-", base).strip("-")
    return f"{index:02d}-{base}.pdf"


def is_pdf(path: Path) -> bool:
    """Validate that a file starts with the PDF magic bytes ``%PDF-``."""
    try:
        with path.open("rb") as f:
            head = f.read(5)
        return head == b"%PDF-"
    except (OSError, IOError):
        return False


def sha256_file(path: Path) -> str:
    """Compute SHA-256 hex digest of a file in 64 KiB chunks."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()
