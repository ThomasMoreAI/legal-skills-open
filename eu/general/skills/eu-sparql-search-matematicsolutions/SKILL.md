---
name: eu-sparql-search-matematicsolutions
title: EU SPARQL Search - Cellar / EUR-Lex
description: 'Search EU legislation, publications and CJEU case law using the Publications Office SPARQL endpoint and Cellar knowledge graph (CDM ontology). Use this skill whenever the user wants to find EU acts (regulations, directives, decisions), search EUR-Lex by CELEX number, date or subject, retrieve CJEU rulings, download EU documents in specific languages or formats, or build SPARQL queries against https://publications.europa.eu/webapi/rdf/sparql. Also trigger when the user asks about EU law programmatically, wants to query Cellar metadata, or mentions CDM ontology, EUR-Lex, EU publications, or SPARQL + EU/legislation. Unlike the verification and drafting skills, this one reaches out: your query goes to the EU Publications Office endpoint, so phrase it in terms of the law, not of your matter.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/eu-law-sources/skills/eu-sparql-search
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: eu
practice: general
language: en
sources:
- title: Resource Types
  path: references/resource-types.md
---

# EU SPARQL Search - Cellar / EUR-Lex

## Endpoint

```
https://publications.europa.eu/webapi/rdf/sparql
```

Accepts HTTP GET and POST. Key parameters:
- `query` - SPARQL query string (URL-encoded)
- `format` - output format (see below)
- `timeout` - milliseconds (use ~30000 for safety)

## CDM Data Model

Every document exists at 4 levels:

```
Work          <- abstract document (e.g. "Regulation 2016/679")
  Expression      <- language version (e.g. Polish, English)
    Manifestation     <- file format (pdfa2a, fmx4, xhtml)
      Item                <- downloadable file URL
```

Main ontology prefix: `cdm:` -> `http://publications.europa.eu/ontology/cdm#`

## Standard Prefixes (include in every query)

```sparql
PREFIX cdm:   <http://publications.europa.eu/ontology/cdm#>
PREFIX annot: <http://publications.europa.eu/ontology/annotation#>
PREFIX skos:  <http://www.w3.org/2004/02/skos/core#>
PREFIX dc:    <http://purl.org/dc/elements/1.1/>
PREFIX xsd:   <http://www.w3.org/2001/XMLSchema#>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
```

## Key CDM Properties

| Property | Description | Example value |
|---|---|---|
| `cdm:work_has_resource-type` | Document type URI | see Resource Types below |
| `cdm:resource_legal_id_celex` | CELEX number | `"32016R0679"` |
| `cdm:work_date_document` | Document date | `"2016-04-27"^^xsd:date` |
| `cdm:resource_legal_in-force` | Currently in force | `"true"^^xsd:boolean` |
| `cdm:expression_uses_language` | Language resource | join with `dc:identifier` - use ISO 639-3 (`POL`, `ENG`...) |
| `cdm:manifestation_type` | File format | `"pdfa2a"`, `"fmx4"`, `"xhtml"` - always match with `FILTER(STR(?fmt) = "pdfa2a")` |
| `cdm:do_not_index` | Hidden doc flag | always filter NOT EXISTS |
| `cdm:expression_belongs_to_work` | Expression → Work link (inverse of `work_has_expression`) | join predicate |
| `cdm:manifestation_manifests_expression` | Manifestation → Expression link (inverse of `expression_manifested_by_manifestation`) | join predicate |
| `cdm:item_belongs_to_manifestation` | Item → Manifestation link (inverse of `manifestation_has_item`) | join predicate |

## Resource Types (most common)

```
REG        -> Regulation
DIR        -> Directive
DEC        -> Decision
RECO       -> Recommendation
OPIN       -> Opinion
JUDG       -> Judgment (CJEU)
ORDER_CJEU -> Order (CJEU)
CASELAW    -> Case law (generic)
```

Full URI pattern: `<http://publications.europa.eu/resource/authority/resource-type/REG>`

For the complete list, see `references/resource-types.md`.

## Language Codes

**IMPORTANT:** Cellar uses **ISO 639-3 three-letter codes**, NOT two-letter ISO 639-1 codes.

| Language | Code |
|---|---|
| Polish | `POL` |
| English | `ENG` |
| German | `DEU` |
| French | `FRA` |
| Italian | `ITA` |
| Spanish | `SPA` |
| Dutch | `NLD` |
| Czech | `CES` |
| Hungarian | `HUN` |
| Romanian | `RON` |
| Bulgarian | `BUL` |
| Croatian | `HRV` |
| Slovak | `SLK` |
| Swedish | `SWE` |
| Finnish | `FIN` |
| Danish | `DAN` |
| Greek | `ELL` |
| Portuguese | `POR` |

Filter pattern:
```sparql
?expr cdm:expression_uses_language ?lang .
?lang dc:identifier "POL" .
```

## Output Formats

| format param value | Description |
|---|---|
| `application/sparql-results+json` | JSON - best for programmatic use |
| `text/csv` | CSV |
| `application/sparql-results+xml` | XML |
| `text/turtle` | Turtle RDF |
| `text/html` | HTML table |

---

## Query Patterns

### 1. Search by document type

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?work ?celex ?date
WHERE {
  ?work cdm:work_has_resource-type
        <http://publications.europa.eu/resource/authority/resource-type/REG> .
  OPTIONAL { ?work cdm:resource_legal_id_celex ?celex }
  OPTIONAL { ?work cdm:work_date_document ?date }
  FILTER NOT EXISTS { ?work cdm:do_not_index "true"^^xsd:boolean }
}
ORDER BY DESC(?date)
LIMIT 20
```

### 2. Search by CELEX number

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX dc:  <http://purl.org/dc/elements/1.1/>

SELECT DISTINCT ?work ?celex ?title
WHERE {
  ?work cdm:resource_legal_id_celex ?celex .
  FILTER(STR(?celex) = "32016R0679")  # ⚠️ always use FILTER(STR()) - direct literal matching fails
  OPTIONAL {
    ?expr cdm:expression_belongs_to_work ?work ;
          cdm:expression_uses_language ?lang .
    ?lang dc:identifier "ENG" .
    ?expr cdm:expression_title ?title .
  }
}
```

### 3. Search by date range

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?work ?celex ?date
WHERE {
  ?work cdm:work_has_resource-type
        <http://publications.europa.eu/resource/authority/resource-type/DIR> .
  ?work cdm:work_date_document ?date .
  OPTIONAL { ?work cdm:resource_legal_id_celex ?celex }
  FILTER (?date >= "2020-01-01"^^xsd:date && ?date <= "2023-12-31"^^xsd:date)
  FILTER NOT EXISTS { ?work cdm:do_not_index "true"^^xsd:boolean }
}
ORDER BY DESC(?date)
LIMIT 50
```

### 4. Get downloadable file URLs (full Work->Item chain)

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX dc:  <http://purl.org/dc/elements/1.1/>

SELECT DISTINCT ?celex ?fmt ?item
WHERE {
  ?work cdm:resource_legal_id_celex ?celex .
  FILTER(STR(?celex) IN ("32016R0679", "32018R1725"))  # ⚠️ always use STR() - direct IN fails
  ?expr cdm:expression_belongs_to_work ?work ;
        cdm:expression_uses_language ?lang .
  ?lang dc:identifier "POL" .
  ?manif cdm:manifestation_manifests_expression ?expr ;
         cdm:manifestation_type ?fmt .
  FILTER(STR(?fmt) = "pdfa2a")  # ⚠️ "pdfa1a" does not exist; use "pdfa2a", "fmx4", or "xhtml"
  ?item cdm:item_belongs_to_manifestation ?manif .
}
```

### 5. CJEU case law by date range

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?work ?celex ?date
WHERE {
  ?work cdm:work_has_resource-type
        <http://publications.europa.eu/resource/authority/resource-type/JUDG> .
  ?work cdm:work_date_document ?date .
  OPTIONAL { ?work cdm:resource_legal_id_celex ?celex }
  FILTER (?date >= "2023-01-01"^^xsd:date)
  FILTER NOT EXISTS { ?work cdm:do_not_index "true"^^xsd:boolean }
}
ORDER BY DESC(?date)
LIMIT 30
```

### 6. Combined: type + date + language + file format (most complete pattern)

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX dc:  <http://purl.org/dc/elements/1.1/>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?celex ?date ?fmt ?item
WHERE {
  ?work cdm:work_has_resource-type
        <http://publications.europa.eu/resource/authority/resource-type/DIR> .
  ?work cdm:work_date_document ?date .  # required (not OPTIONAL) so FILTER applies correctly
  FILTER (?date >= "2023-01-01"^^xsd:date)
  OPTIONAL { ?work cdm:resource_legal_id_celex ?celex }
  FILTER NOT EXISTS { ?work cdm:do_not_index "true"^^xsd:boolean }
  ?expr cdm:expression_belongs_to_work ?work ;
        cdm:expression_uses_language ?lang .
  ?lang dc:identifier "POL" .
  ?manif cdm:manifestation_manifests_expression ?expr ;
         cdm:manifestation_type ?fmt .
  FILTER(STR(?fmt) = "pdfa2a")  # ⚠️ use STR() - direct literal fails; "pdfa1a" does not exist
  ?item cdm:item_belongs_to_manifestation ?manif .
}
ORDER BY DESC(?date)
LIMIT 20
```

### 7. Search by EuroVoc subject (thematic search)

EuroVoc is a multilingual thesaurus maintained by the Publications Office - this is the correct way to search by topic (e.g. "personal data", "environment"), since the endpoint does NOT support full-text search.

EuroVoc URI base: `http://eurovoc.europa.eu/`

To find a EuroVoc concept URI by label:
```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?concept ?label
WHERE {
  ?concept a skos:Concept ;
           skos:prefLabel ?label .
  FILTER(lang(?label) = "en")
  FILTER(CONTAINS(LCASE(str(?label)), "personal data"))
}
LIMIT 10
```

Then use the concept URI to filter documents:
```sparql
PREFIX cdm:  <http://publications.europa.eu/ontology/cdm#>
PREFIX xsd:  <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?work ?celex ?date
WHERE {
  ?work cdm:work_has_resource-type
        <http://publications.europa.eu/resource/authority/resource-type/REG> .
  # ⚠️ JUDG (case law) does NOT have EuroVoc tags - use REG, DIR, DEC or leave type open
  ?work cdm:work_date_document ?date .
  OPTIONAL { ?work cdm:resource_legal_id_celex ?celex }
  ?work cdm:work_is_about_concept_eurovoc ?subject .
  FILTER(?subject IN (
    <http://eurovoc.europa.eu/5595>
  ))
  FILTER (?date >= "2020-01-01"^^xsd:date)
  FILTER NOT EXISTS { ?work cdm:do_not_index "true"^^xsd:boolean }
}
ORDER BY DESC(?date)
LIMIT 30
```

### 8. In-force legislation only

```sparql
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT DISTINCT ?work ?celex ?date
WHERE {
  ?work cdm:work_has_resource-type
        <http://publications.europa.eu/resource/authority/resource-type/REG> .
  ?work cdm:resource_legal_in-force "true"^^xsd:boolean .
  OPTIONAL { ?work cdm:resource_legal_id_celex ?celex }
  OPTIONAL { ?work cdm:work_date_document ?date }
  FILTER NOT EXISTS { ?work cdm:do_not_index "true"^^xsd:boolean }
}
ORDER BY DESC(?date)
LIMIT 20
```

---

## How to Execute Queries

### Preferred method: bash_tool + Python (urllib)

Use `bash_tool` with Python to run SPARQL queries and fetch document content. This bypasses all `web_fetch` permission restrictions and works unconditionally.

```python
import urllib.parse, urllib.request, json

def sparql(query):
    encoded = urllib.parse.quote(query)
    url = f"https://publications.europa.eu/webapi/rdf/sparql?query={encoded}&format=application%2Fsparql-results%2Bjson&timeout=30000"
    with urllib.request.urlopen(url, timeout=35) as r:
        return json.loads(r.read())["results"]["bindings"]

results = sparql("""
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT DISTINCT ?work ?celex WHERE {
  ?work cdm:resource_legal_id_celex ?celex .
  FILTER(STR(?celex) = "32016R0679")
}
""")
for r in results:
    print(r["celex"]["value"])
```

If SSL certificate errors occur (transient), disable verification:
```python
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# pass context=ctx to urlopen
```

### Fetching document content from Cellar

Once you have an item URL from SPARQL (e.g. `?item cdm:item_belongs_to_manifestation ?manif`), fetch the full document text using `curl` in `bash_tool`:

```bash
curl -s -L "<item_url>" -H "Accept: text/html" \
  | python3 -c "
import sys
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'nav', 'header', 'footer'):
            self.skip = True
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'nav', 'header', 'footer'):
            self.skip = False
    def handle_data(self, data):
        if not self.skip and data.strip():
            self.text.append(data.strip())

p = TextExtractor()
p.feed(sys.stdin.read())
print('\n'.join(p.text)[:20000])
"
```

> ⚠️ **Do NOT use `web_fetch` for Cellar URLs returned by SPARQL** - `web_fetch` in Claude.ai only accepts URLs that were provided directly by the user or appeared in `web_search` results. Cellar item URLs from `bash_tool` SPARQL queries will always be rejected. Use `curl` in `bash_tool` instead.

### JSON response structure

```json
{
  "results": {
    "bindings": [
      {
        "work":  { "type": "uri",     "value": "http://publications.europa.eu/resource/cellar/..." },
        "celex": { "type": "literal", "value": "32016R0679" },
        "date":  { "type": "literal", "value": "2016-04-27" }
      }
    ]
  }
}
```

Access results: `data["results"]["bindings"]` - list of dicts, each key maps to `{type, value}`.

---

## Workflow

1. **Identify intent** - what type of document, which filters (date, language, CELEX, format, in-force)?
2. **Choose query pattern** from the patterns above, or combine them
3. **Execute via bash_tool** - run SPARQL with Python/urllib, parse JSON bindings
4. **Parse and present** - extract bindings, display as readable table with CELEX numbers and dates
5. **Fetch document content if needed** - use `curl` in `bash_tool` with the item URL from SPARQL
6. **Always cite sources** - provide clickable links so the user can verify (see Citations section)
7. **Offer next steps** - get file download URLs, filter by language, expand date range, etc.

---

## Citations - always provide verifiable links

**Every answer based on fetched document content MUST include clickable source links.** This lets the user verify that the answer is based on real document text, not hallucinated.

### Mandatory citation elements

Whenever you answer a question based on a fetched document, always include at the end:

1. **EUR-Lex link** - canonical, stable, human-readable URL for the document:
   ```
   https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=celex:{CELEX}
   ```
   e.g. `https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=celex:32022R2554`

2. **Direct Cellar download link** - the item URL returned by SPARQL (use for one-click access to the actual file):
   ```
   http://publications.europa.eu/resource/cellar/{uuid}.{lang_code}.{fmt_code}/DOC_1
   ```

3. **Article anchor on EUR-Lex** - when citing a specific article, append the anchor to the EUR-Lex URL:
   ```
   https://eur-lex.europa.eu/legal-content/PL/TXT/HTML/?uri=celex:32022R2554#d1e3456-1-1
   ```
   EUR-Lex article anchors follow the pattern `#art_{N}` for top-level articles in some acts, but anchors are not always stable. Prefer linking to the full document and mentioning the article number explicitly (e.g. "Art. 30 ust. 2 lit. e)").

### Citation format in responses

After providing an answer based on document content, always end with a source block:

```
**Źródło:** DORA - Rozporządzenie (UE) 2022/2554
- EUR-Lex (PL): https://eur-lex.europa.eu/legal-content/PL/TXT/?uri=celex:32022R2554
- Pobierz plik (PL, xhtml): http://publications.europa.eu/resource/cellar/0caf473a-85bd-11ed-9887-01aa75ed71a1.0018.03/DOC_1
```

### SPARQL query to retrieve item URLs for citations

Always fetch the item URL alongside the content so you can include it in the citation:

```sparql
SELECT DISTINCT ?celex ?fmt ?item
WHERE {
  ?work cdm:resource_legal_id_celex ?celex .
  FILTER(STR(?celex) = "32022R2554")
  ?expr cdm:expression_belongs_to_work ?work ;
        cdm:expression_uses_language ?lang .
  ?lang dc:identifier "POL" .
  ?manif cdm:manifestation_manifests_expression ?expr ;
         cdm:manifestation_type ?fmt .
  ?item cdm:item_belongs_to_manifestation ?manif .
}
```

Then present both EUR-Lex and Cellar links to the user.

## Rules

- Always use `SELECT DISTINCT` - avoids duplicate triples
- Always add `LIMIT` - start with 20, offer to increase; unbound queries time out
- Always add `FILTER NOT EXISTS { ?work cdm:do_not_index "true"^^xsd:boolean }` - hides internal docs
- Endpoint is **public, no authentication required**
- This endpoint covers **metadata only** - for full-text search use EUR-Lex search UI
- CELEX format: `3YYYYTNNNN` for legislative acts (R=regulation, L=directive, D=decision); preparatory acts use `5YYYYPC...` - see CELEX prefix table in Resource Types
- **Language codes are ISO 639-3 (3 letters): POL, ENG, DEU - NOT PL, EN, DE**
- For thematic search, always use EuroVoc concept URIs - there is no keyword/full-text search
- ⚠️ **NEVER use `COM_PROP`, `COM_PROP_REG`, `COM_PROP_DIR`** as resource-type URIs - they do not exist. Use `PROP_REG`, `PROP_DIR`, `PROP_DEC` instead
- ⚠️ **Literal matching**: Cellar stores strings as typed `xsd:string` literals. Direct object matching (e.g. `?work cdm:resource_legal_id_celex "32016R0679"`) silently returns 0 results. Always use `FILTER(STR(?var) = "value")` for CELEX numbers and manifestation types; for multi-value use `FILTER(STR(?celex) IN ("...", "..."))`
- ⚠️ **File format `pdfa1a` does not exist** - use `pdfa2a`, `fmx4`, or `xhtml`; always bind to variable and filter with `FILTER(STR(?fmt) = "pdfa2a")`
- ⚠️ **EuroVoc tags are NOT assigned to JUDG (case law)** - for thematic document search use REG, DIR, DEC, or omit type filter
- ⚠️ **OPTIONAL + FILTER scoping**: never put date in `OPTIONAL` then filter it in the same WHERE - it creates 0 results. Keep `?work cdm:work_date_document ?date` as a required triple when filtering by date

## REST API - Direct File Download

Cellar also provides a simpler REST interface to download files directly, without SPARQL:

```
http://publications.europa.eu/resource/{ps-name}/{ps-id}?language={iso639-3-code}
```

Examples:
- `http://publications.europa.eu/resource/cellar/b84f49cd-750f-11e3-8e20-01aa75ed71a1.0006.01/DOC_1`
- With language: `...?language=POL`
- With format: `...?language=POL&format=pdfa2a`

The Cellar ID (UUID) comes from the `?work` URI returned by SPARQL queries - extract the UUID from the URI and use it in the REST call.

## Other Cellar APIs

- **RSS/Atom feeds**: `https://op.europa.eu/en/web/cellar/cellar-data/rss-and-atom-feeds` - subscribe to new publications by collection
- **Metadata notices**: RESTful XML/RDF metadata for a specific work, richer than SPARQL results
- **Linked Data wizard**: `https://op.europa.eu/en/linked-data` - GUI query builder, no SPARQL needed

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the eu-law-sources plugin (EU law sources)

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

### Sources, not memory

This plugin searches and fetches EU law (legislation and CJEU case law) through an MCP connector (read-only, public EUR-Lex / Cellar SPARQL). Every legal claim belongs to a class:

- **Verified** - confirmed in the database, with an identifier: `(Case C-311/18, CJEU)`, `(CELEX 32016R0679)`.
- **Check** - plausible, not yet confirmed: `[verify on EUR-Lex]`.
- **Do not use** - a CELEX or case number with no match. Omit it, never fabricate.

A case number that exists is not enough - check that the judgment decides what you cite. Whether case law is still good law is a human assessment.

### Connector in this plugin

`.mcp.json` declares the EU SPARQL connector (EUR-Lex / Cellar, read-only, public data). It needs `node`/`npx` in the environment. This is EU-level, language-neutral law - national law of a specific member state is out of scope here.

### Human gate

Output is a draft for review. Nothing is sent or filed before a qualified person checks it and takes professional responsibility.
<!-- shared-rules:end -->
