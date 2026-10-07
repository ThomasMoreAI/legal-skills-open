# Erskine May API — full endpoint reference

Cached spec: [`_specs/erskinemay.json`](../../_specs/erskinemay.json)
Endpoint table: [`_specs/endpoint-tables/erskinemay.txt`](../../_specs/endpoint-tables/erskinemay.txt)

Base URL: `https://erskinemay-api.parliament.uk/api`

## Endpoints

### Structural navigation
- `GET /Part` — list of Parts.
- `GET /Part/{partNumber}` — one Part with its chapters.
- `GET /Chapter/{chapterNumber}` — one Chapter with its sections.
- `GET /Section/{sectionId}` — section content.
- `GET /Section/{sectionId},{step}` — next/previous neighbour;
  `step` is `next` or `previous`.

### Paragraphs and search
- `GET /Search/Paragraph/{reference}` — fetch by reference like
  `20.5`. Returns the paragraph text plus its parent section.
- `GET /Search/ParagraphSearchResults/{searchTerm}` — paragraph search.
- `GET /Search/SectionSearchResults/{searchTerm}` — section search.

### Index
- `GET /IndexTerm/browse?startLetter=A` — A–Z browse.
- `GET /IndexTerm/{indexTermId}` — one index entry with cross-references.
- `GET /Search/IndexTermSearchResults/{searchTerm}` — search the index.

## Notes

- The hierarchical IDs are: `partNumber` (1..n), `chapterNumber`
  (within a part), `sectionId` (a guid), `paragraphReference` (a
  human-readable dotted code).
- Paragraph results carry `contentTextHtml` (rendered) and
  `contentText` (plain) — pick the one your downstream needs.
- The current edition is the 25th (2019) plus online updates; the
  API tracks the online version.
