---
name: cendoj-toolkit-joserprieto
title: CENDOJ Toolkit
description: Use when the user needs to search and download court decisions from CENDOJ (Centro de Documentación Judicial del Consejo General del Poder Judicial), the Spanish official judicial database. Also when user says "buscar sentencias", "descargar sentencia CENDOJ", "jurisprudencia CENDOJ", "ECLI", or provides a poderjudicial.es URL. STRICTLY for personal/individual use (uso particular). Bulk downloads or commercial use are explicitly forbidden by CENDOJ legal notice and require formal authorization from CGPJ.
author: joserprieto
author_url: https://github.com/joserprieto/ai-skills/tree/main/skills/cendoj-toolkit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: es
practice: litigation
language: es
sources:
- title: Cendoj Legal Notice
  path: references/cendoj-legal-notice.md
- title: Compliance Checklist
  path: references/compliance-checklist.md
- title: Url Patterns
  path: references/url-patterns.md
---

# CENDOJ Toolkit

Search and download Spanish court decisions from CENDOJ (Centro de Documentación Judicial del
Consejo General del Poder Judicial) for personal use only.

## ⚠️ LEGAL NOTICE — READ BEFORE USING

CENDOJ's official legal notice (verbatim from their portal):

> Las resoluciones que componen esta base de datos se difunden a efectos de conocimiento y consulta
> de los criterios de decisión de los Tribunales, en cumplimiento de la competencia otorgada al
> Consejo General del Poder Judicial por el art. 560.1.10º de la Ley Orgánica del Poder Judicial.
>
> El usuario de la base de datos podrá consultar los documentos siempre que lo haga **para su uso
> particular**.
>
> **No está permitida la utilización de la base de datos para usos comerciales, ni la descarga
> masiva de información.** La reutilización de esta información para la elaboración de bases de
> datos o con fines comerciales debe seguir el procedimiento y las condiciones establecidas por el
> CGPJ a través de su Centro de Documentación Judicial.

**Permitted use cases** (uso particular):

- Defending your own legal case (employee/citizen looking up case law for your dispute)
- Academic research on jurisprudence (with citation, non-commercial)
- Personal legal study or preparation
- Lawyer preparing defense for a specific client case

**Forbidden use cases**:

- Building commercial legal databases
- Aggregating CENDOJ content for resale or commercial AI training
- Indiscriminate bulk downloading
- Republishing CENDOJ content as a competing service

If you intend a commercial use, you must request formal authorization from CGPJ (see
<https://www.poderjudicial.es/cgpj/es/Servicios/Centro-de-Documentacion-Judicial>).

## Robots.txt compliance

CENDOJ `robots.txt` (<https://www.poderjudicial.es/robots.txt>) sets:

```
User-agent: *
Crawl-delay: 5
```

**This skill enforces `Crawl-delay: 5` (5 seconds between requests)** as the non-negotiable minimum.
Do not lower this without explicit CGPJ authorization.

## Prerequisites

| Tool                        | Min Version | Purpose                            | Install                                                 |
| --------------------------- | ----------- | ---------------------------------- | ------------------------------------------------------- |
| Python                      | >= 3.10     | Run scripts                        | `brew install python` or `mise install python`          |
| `playwright`                | latest      | Form-based search (CENDOJ uses JS) | `pip install playwright && playwright install chromium` |
| `requests`                  | latest      | PDF download                       | `pip install requests`                                  |
| `pdfminer.six` or `docling` | latest      | PDF → text/markdown conversion     | `pip install pdfminer.six` or `pip install docling`     |

Install all dependencies:

```bash
pip install playwright requests pdfminer.six
playwright install chromium
```

## Capabilities

This skill provides three composable scripts:

### 1. `cendoj_search.py` — Search by free text

Performs a free-text search on CENDOJ via Playwright (the search form is JS-driven, plain HTTP POST
doesn't work reliably). Returns a JSON inventory of all results with ECLI codes + reference IDs
needed for PDF download.

```bash
python scripts/cendoj_search.py --query "Avincis" --output results.json
```

Output JSON schema (one entry per result):

```json
[
  {
    "title": "STSJ Galicia, a 06 de febrero de 2026 - ROJ: STSJ GAL 1040/2026",
    "ecli": "ECLI:ES:TSJGAL:2026:1040",
    "tribunal": "TSJ Galicia",
    "city": "Coruña (A)",
    "date_iso": "2026-02-06",
    "resolution_number": "572/2026",
    "appeal_number": "3429/2025",
    "ponente": "EVA MARIA DOVAL LORENTE",
    "summary": "DESPIDO DISCIPLINARIO",
    "reference": "a73e3b3c0538644fa0a8778d75e36f0d",
    "optimize": "20260316",
    "open_document_url": "https://www.poderjudicial.es/search/AN/openDocument/a73e3b3c0538644fa0a8778d75e36f0d/20260316",
    "pdf_url": "https://www.poderjudicial.es/search/contenidos.action?action=accessToPDF&publicinterface=true&tab=AN&reference=a73e3b3c0538644fa0a8778d75e36f0d&encode=true&optimize=20260316&databasematch=AN"
  }
]
```

### 2. `cendoj_download.py` — Download PDFs from inventory

Takes the JSON inventory produced by `cendoj_search.py` and downloads each PDF respecting
`Crawl-delay: 5` enforced minimum. Calculates SHA-256 for each downloaded file. Generates an
`INVENTARIO.md` summary table.

```bash
python scripts/cendoj_download.py \
  --input results.json \
  --output-dir ./pdfs/ \
  --max-downloads 50 \
  --delay 5
```

Safety limits:

- `--max-downloads` defaults to 50 (hard maximum 200, configurable but printed warning)
- `--delay` defaults to 5 seconds (hard minimum 5, cannot be lowered)
- Existing files are skipped (idempotent re-runs)
- Each PDF is validated post-download (must be PDF magic bytes)

### 3. `cendoj_pdf_to_md.py` — Convert downloaded PDFs to markdown

Converts each PDF in a directory to markdown using `pdfminer.six` (default) or `docling` (with
`--engine docling`). Preserves structure best-effort.

```bash
python scripts/cendoj_pdf_to_md.py \
  --input-dir ./pdfs/ \
  --output-dir ./markdown/ \
  --engine pdfminer
```

## Full pipeline (recommended workflow)

```bash
# 1. Search
python scripts/cendoj_search.py --query "Avincis" --output results.json

# 2. Review results.json manually — confirm "uso particular" applies to your case

# 3. Download PDFs (respects 5s crawl-delay automatically)
python scripts/cendoj_download.py --input results.json --output-dir ./pdfs/

# 4. Convert to markdown
python scripts/cendoj_pdf_to_md.py --input-dir ./pdfs/ --output-dir ./markdown/
```

## Verification of compliance

Every script execution:

1. Prints the CENDOJ legal notice as the first output
2. Asks explicit user confirmation before downloading (if `--max-downloads > 10`)
3. Logs all requests with timestamps for audit trail
4. Refuses to lower `--delay` below 5 seconds

## URL patterns documented

For developers extending this skill or doing manual URL construction:

### Search results format (from openDocument links in HTML)

```
https://www.poderjudicial.es/search/AN/openDocument/{REFERENCE}/{OPTIMIZE}
```

Where:

- `{REFERENCE}` = hex hash (16 or 32 chars depending on era of insertion)
- `{OPTIMIZE}` = YYYYMMDD (date inserted/last optimized in CENDOJ DB)

### PDF direct download URL

```
https://www.poderjudicial.es/search/contenidos.action
  ?action=accessToPDF
  &publicinterface=true
  &tab=AN
  &reference={REFERENCE}
  &encode=true
  &optimize={OPTIMIZE}
  &databasematch=AN
```

Required HTTP headers (CENDOJ filters generic curl):

```
User-Agent: Mozilla/5.0 (...) [browser-like UA required]
Accept: application/pdf,*/*
Referer: https://www.poderjudicial.es/search/indexAN.jsp
```

## Limitations

- The search form is JS-driven; cannot use plain HTTP POST (need Playwright)
- The `databasematch=AN` parameter covers all jurisdictions (TS, AN, TSJ, AP, JSO). No separate
  parameter set needed by jurisdiction
- Pre-2015 sentences have shorter 16-char references; same URL pattern applies
- ECLI codes are stable across CENDOJ updates; references may rotate (rare but documented)

## References

- `references/cendoj-legal-notice.md` — full CENDOJ legal notice verbatim (ES)
- `references/url-patterns.md` — detailed URL pattern documentation
- `references/compliance-checklist.md` — pre-execution compliance checklist

## License

MIT for the toolkit code. The downloaded CENDOJ content remains property of CENDOJ and is subject to
their terms of use (uso particular only).
