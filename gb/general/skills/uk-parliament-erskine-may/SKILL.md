---
name: uk-parliament-erskine-may
title: Erskine May API
description: Search and retrieve Erskine May — *A Treatise on the Law, Privileges, Proceedings and Usage of Parliament*, the authoritative reference work on UK parliamentary procedure. Browse by Part, Chapter, Section, paragraph reference (e.g. "20.5") or index term, or full-text search across the whole work. Use when the question is about parliamentary procedure, precedent, the rules governing debate, motions, divisions, privilege, or anything else covered in Erskine May.
author: danbri
author_url: https://github.com/danbri/forgetmenot/tree/main/skills/erskine-may
license: CC0-1.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# Erskine May API

Base URL: `https://erskinemay-api.parliament.uk/api`

OpenAPI 3 spec: `https://erskinemay-api.parliament.uk/swagger/v1/swagger.json`
(cached at `_specs/erskinemay.json`).

## What it covers

The full, current 25th edition of *Erskine May* (Parliament's
authoritative procedure manual) as a structured tree:

- **Parts** — the top-level divisions (e.g. "Privilege").
- **Chapters** — numbered chapters within each part.
- **Sections** — sub-chapter sections; each section has step navigation.
- **Paragraphs** — individual numbered paragraphs (the smallest cited
  unit, e.g. "20.5").
- **Index terms** — the back-of-book index, browseable A–Z and
  searchable.

## Common entry points

| Use case | Endpoint |
|---|---|
| List all Parts | `GET /Part` |
| One Part | `GET /Part/{partNumber}` |
| One Chapter | `GET /Chapter/{chapterNumber}` |
| One Section | `GET /Section/{sectionId}` |
| Section navigation step | `GET /Section/{sectionId},{step}` (e.g. `/Section/12345,next`) |
| Paragraph by reference | `GET /Search/Paragraph/{reference}` (e.g. `20.5`) |
| Full-text search of paragraphs | `GET /Search/ParagraphSearchResults/{searchTerm}` |
| Full-text search of sections | `GET /Search/SectionSearchResults/{searchTerm}` |
| Browse index A–Z | `GET /IndexTerm/browse?startLetter=A` |
| One index term | `GET /IndexTerm/{indexTermId}` |
| Full-text search of index | `GET /Search/IndexTermSearchResults/{searchTerm}` |

## Worked example

```sh
# Find paragraphs about "casting vote"
curl -s 'https://erskinemay-api.parliament.uk/api/Search/ParagraphSearchResults/casting%20vote' \
  | jq '.searchResults[] | {ref: .reference, text: (.contentTextHtml | gsub("<[^>]+>"; "") | .[0:160])}'

# Or pull a paragraph directly by its reference
curl -s 'https://erskinemay-api.parliament.uk/api/Search/Paragraph/20.5'
```

## Notes

- References (e.g. `20.5`) are stable across reprints within an edition
  but may change between editions.
- HTML in paragraph text contains semantic markup (`<em>`,
  `<a>`-style cross-references); strip tags for plain text or render
  as HTML.
- Erskine May is © House of Commons / House of Lords; the API is
  available under the Open Parliament Licence for reuse.

<!-- parl-cli-start -->

## Using the CLI

This skill ships with a Node CLI alongside the documentation. From the
repo root:

```sh
node bin/parl.mjs em --help
```

Or after `npm link` (one-time install):

```sh
parl em --help
```

Wraps the Erskine May API (parliamentary procedure manual).

### Examples

```sh
parl em parts
```
List Parts.

```sh
parl em paragraph 20.5
```
Pull paragraph 20.5 by reference.

```sh
parl em search "casting vote"
```
Search paragraphs.

```sh
parl em search-sections "privilege"
```
Search sections.

```sh
parl em index --start-letter A
```
Browse the index from A.


### Library use (Node + browser)

Same surface as a JS module:

```js
import * as fac from '../../lib/facilities/erskine-may.mjs';

// Each function is async and returns parsed JSON (or bytes for
// download endpoints). See the .mjs source for the full export list.
```

The library uses only `fetch` / `URL` / `AbortController`, so the
same source runs in Node 18+ and in modern browsers.

<!-- parl-cli-end -->
