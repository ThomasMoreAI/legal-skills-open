# Michigan Law — Programmatic Data Access

> **NOT LEGAL ADVICE.** Access notes for agents. Endpoints and schemes
> change; verify the live response before relying on parsed output.

Agent-facing index of the structured / fetchable sources behind
Michigan primary law. For human-facing URLs see `online-sources.md`.

---

## Michigan Compiled Laws — legislature.mi.gov objectName scheme

The Michigan Legislature site addresses each MCL section by an
**objectName** of the form `mcl-<chapter>-<section>` (the dot in the
citation becomes a hyphen). This makes section text directly fetchable:

- **Section page**:
  `https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-600-5701`
- **Document (printable) endpoint**:
  `https://www.legislature.mi.gov/Home/Document?objectName=mcl-600-5701`

Examples of the objectName transform:

| Citation | objectName |
|---|---|
| MCL 600.5701 | `mcl-600-5701` |
| MCL 600.5807 | `mcl-600-5807` |
| MCL 600.2116 *(illustrative form)* | `mcl-600-2116` |
| MCL 445.901 | `mcl-445-901` |

This is the scheme the `mi-statutes-debt` puller targets. To enumerate
a chapter, walk the chapter's section list from the act page and build
the objectName for each section.

---

## Court rules, evidence rules, and forms — courts.michigan.gov

- The **MCR**, **MRE**, administrative orders, and **SCAO forms** are
  published as web pages and **PDFs** on `courts.michigan.gov`. There is
  no public REST API; the `court-rules` puller fetches the posted rule
  documents (HTML/PDF) and converts them.
- The **MiFILE** e-filing platform (Tyler/Odyssey) is an authenticated
  filing system, not a content API.

---

## Case law — CourtListener (Free Law Project)

CourtListener exposes Michigan appellate opinions through its REST API
and bulk data, and is the recommended programmatic source for Michigan
case law.

- **Michigan Supreme Court** — CourtListener court id: **`mich`**
- **Michigan Court of Appeals** — CourtListener court id: **`michctapp`**
- **REST API** (opinions / clusters / dockets):
  `https://www.courtlistener.com/api/rest/` — filter by `court=mich` or
  `court=michctapp`.
- Use CourtListener to pull full opinion text, parallel citations, and
  precedential status (published vs. unpublished) before quoting an
  authority from `key-cases.md`.

### CourtListener MCP

A **CourtListener MCP server** is connected in this environment
(surfaced as a deferred tool). When case-law lookup or citation
verification is needed, prefer the CourtListener MCP tools (search,
fetch opinion, resolve citation) over scraping — they return structured
opinion metadata and text. Load the tool schemas via tool search before
calling.

---

## Verification workflow for the agent

1. **Statute** → fetch the `legislature.mi.gov` objectName document and
   read the current text; do not rely on a cached amount or day count.
2. **Rule (MCR/MRE)** → fetch the current posting on
   `courts.michigan.gov`; confirm post-2024-restyling MRE text.
3. **Case** → resolve and fetch via the CourtListener MCP (or REST,
   `court=mich` / `court=michctapp`); confirm published/unpublished
   status and that the opinion is still good law.

---

## Cross-references

- `online-sources.md` — the human-facing equivalents
- `citation-format.md` — Michigan Appellate Opinion Manual citation form
- `key-cases.md` — the authorities to verify through these channels
