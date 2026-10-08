# CENDOJ URL Patterns (Reverse-Engineered)

Documented from observation of the CENDOJ public web interface at
<https://www.poderjudicial.es/search/indexAN.jsp>.

## Search results listing

The search form at `/search/indexAN.jsp` is JavaScript-driven. Plain HTTP POST does not reliably
reproduce the search state — use Playwright (or similar) to fill the form and click "Buscar".

After search, results are paginated (10 per page by default). Each result links to an `openDocument`
URL.

## openDocument URL

Pattern observed:

```
https://www.poderjudicial.es/search/AN/openDocument/{REFERENCE}/{OPTIMIZE}
```

Where:

- `{REFERENCE}` = hex hash, 16 chars (pre-2018 sentences) or 32 chars (post-2018)
- `{OPTIMIZE}` = YYYYMMDD — date the document was inserted or last optimized in CENDOJ's database
  (NOT the resolution date)

This URL serves an HTML page with embedded PDF viewer + an "aquí" link to the direct PDF endpoint.

## Direct PDF download URL

Pattern observed:

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

All parameters constant except `{REFERENCE}` and `{OPTIMIZE}` (same values as in the openDocument
URL).

### Constant parameters

| Parameter         | Value         | Notes                                           |
| ----------------- | ------------- | ----------------------------------------------- |
| `action`          | `accessToPDF` | Action selector                                 |
| `publicinterface` | `true`        | Public access (no auth)                         |
| `tab`             | `AN`          | Covers all jurisdictions (TS, AN, TSJ, AP, JSO) |
| `encode`          | `true`        | Required (decoder hint)                         |
| `databasematch`   | `AN`          | Same as `tab`                                   |

## Required HTTP headers

CENDOJ filters requests with generic User-Agent strings (curl/python/wget). Use a browser-like
User-Agent:

```
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
Accept: application/pdf,*/*
Referer: https://www.poderjudicial.es/search/indexAN.jsp
```

A cooperative UA (`cendoj-toolkit/0.1.0 (+url)`) was NOT tested by us; it may or may not work. The
skill defaults to the browser UA but offers `--user-agent cooperative`.

## Filtering side panel results

CENDOJ pages embed sidebars showing "Resoluciones más consultadas", "Sentencias por tema", and
"Últimas sentencias del Tribunal Supremo". These also contain `openDocument` links that ARE NOT
search results.

To filter: results have titles matching the regex `^[A-Z]+\s` followed by date (e.g.
`"STSJ Galicia, a 06 de febrero de 2026"`), and contain `ROJ:` in their title. Sidebar items have
short titles like `"STS 1898/2026"` without dates or ROJ.

The Playwright extractor in this toolkit filters by title format.

## ECLI codes

ECLI = European Case Law Identifier. Format:

```
ECLI:ES:{COURT_CODE}:{YEAR}:{NUMBER}[{LETTER}]
```

Where `{COURT_CODE}` examples observed:

| Code    | Court                       |
| ------- | --------------------------- |
| TS      | Tribunal Supremo            |
| AN      | Audiencia Nacional          |
| APM     | Audiencia Provincial Madrid |
| TSJGAL  | TSJ Galicia                 |
| TSJCV   | TSJ Comunidad Valenciana    |
| TSJM    | TSJ Madrid                  |
| TSJBAL  | TSJ Baleares                |
| TSJICAN | TSJ Canarias                |
| TSJCL   | TSJ Castilla y León         |
| TSJCLM  | TSJ Castilla-La Mancha      |
| TSJAS   | TSJ Asturias                |
| TSJCANT | TSJ Cantabria               |
| JSO     | Juzgado de lo Social        |

Letter suffix indicates "Auto" (`A`) vs sentencia (no suffix), and occasionally "Sentencia del
Tribunal Supremo en aclaración" or similar.

ECLI codes are STABLE — they survive CENDOJ database optimizations. Reference hashes may rotate
occasionally; ECLI is the canonical identifier.

## ROJ codes

ROJ = Repertorio Oficial de Jurisprudencia. Format:

```
ROJ: {COURT_PREFIX} {COURT_CODE} {NUMBER}/{YEAR}
```

Examples:

- `ROJ: STSJ GAL 1040/2026`
- `ROJ: STS 3291/2025`
- `ROJ: SAN 138/2025`
- `ROJ: SJSO 3460/2025` (Juzgado de lo Social — Sentencia)
- `ROJ: AAP M 6968/2024` (Auto de Audiencia Provincial Madrid)
- `ROJ: ATS 14560/2024` (Auto del Tribunal Supremo)

The `S` prefix indicates Sentencia; `A` prefix indicates Auto.

## Bottom-of-page indicators (legal limits)

The CENDOJ legal notice modal (which appears on first page load and must be closed to interact with
the search form) states:

- Use particular permitted
- Commercial use forbidden
- Bulk downloads forbidden
- Reuse for commercial DB requires CGPJ procedure

The robots.txt sets `Crawl-delay: 5` for `User-agent: *`.

This toolkit enforces 5s delay as hard minimum and caps downloads per execution.
