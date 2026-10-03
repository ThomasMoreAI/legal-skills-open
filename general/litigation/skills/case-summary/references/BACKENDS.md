# Backends — Implementations of the Workflow

This file lists concrete implementations of the phases described in `WORKFLOW.md`. The core skill is backend-agnostic; a backend is any toolchain that can satisfy the following contract:

**Backend contract:**
1. **Ingest + enumerate** — load a folder/zip of files; return a stable object ID and filename for each.
2. **OCR (or equivalent text extraction)** — produce a text layer on non-searchable PDFs and image-only documents.
3. **Search** — run a content-based query against the corpus and return ranked passages with source object + page metadata.
4. **Retrieve** — return the full content (or at least a bounded page range) of any object on demand.
5. **Cite** — every returned passage carries enough metadata to build a memo citation (object name + page or chunk ID, at minimum).

Any backend that satisfies the contract can power the skill. A backend that doesn't satisfy the contract should be wrapped (e.g., by adding a lightweight OCR pre-step) before use.

---

## Backend: case.dev (primary today)

Encrypted vaults with auto-OCR, semantic + hybrid + entity + graph search, chunk retrieval, and object download. Sub-skills under `skills/casedev/` are the authoritative reference for the CLI surface:

- `skills/casedev/setup` — install and authenticate the CLI.
- `skills/casedev/vaults` — create vaults, upload folders, list objects, get job status.
- `skills/casedev/search` — run content queries across modes (hybrid, vector, fast, global, entity, graph, local).
- `skills/casedev/ocr` — OCR a specific object and fetch word-level positional results.

Recipe cards:

### Ingest

```bash
casedev vault create --name "<Matter Caption — YYYY-MM-DD>" --description "Case-summary corpus"
casedev vault upload /path/to/matter-files --vault <vault-id>
```

Check ingestion:

```bash
casedev vault get <vault-id>
casedev jobs list --scope vault --vault <vault-id>
```

### OCR (only when needed)

```bash
casedev --json vault object list <vault-id> \
  | jq '.objects[] | select(.contentType == "application/pdf")'
casedev ocr process --document-id <object-id> --engine default
casedev ocr watch <ocr-job-id>
```

### Inventory

```bash
casedev vault object list <vault-id> --wide
casedev --json vault object list <vault-id> \
  | jq '[.objects[].contentType] | group_by(.) | map({type: .[0], count: length})'
casedev --json vault object list <vault-id> \
  | jq -r '.objects[].name' | sort
```

### Search

```bash
casedev search vault "<query>" --vault <vault-id> --limit 10
casedev search vault "<query>" --vault <vault-id> --method entity --limit 5
casedev --json search vault "<query>" --vault <vault-id> --limit 10 \
  | jq '.results[] | {object: .fileName, page: .pageNumber, text: .text}'
```

### Method mapping

| `WORKFLOW.md` mode | case.dev `--method` |
|---|---|
| Hybrid (default) | `hybrid` |
| Semantic only | `vector` |
| Keyword / quick coverage | `fast` |
| Global overview | `global` |
| Entity-focused | `entity` |
| Graph / relational | `graph` |
| Local neighborhood | `local` |

See `skills/casedev/search/SKILL.md` for the authoritative flag list; do not treat the table above as canonical if it drifts.

### Retrieve

```bash
casedev vault download --vault <vault-id> --object <object-id> --out ./work
```

---

## Backend: small-corpus direct read (<20 files)

Under 20 files the indexing setup is overkill. Read the files directly:

- PDF: extract text with a PDF library; OCR image-only pages before extraction.
- DOCX / XLSX: read with a structured parser.
- EML / MSG: parse headers + body + attachments.

Cite by filename + page or by filename + cell/row as appropriate. Skip the **Map** search phase; walk the documents once end-to-end and build the memo directly.

---

## Backend contract — adding a new backend

To add a new backend (generic RAG index, third-party vector store, on-prem installation), document it here with:

1. What it is in one paragraph.
2. How it satisfies each point of the **Backend contract** above.
3. Recipe cards for ingest, OCR, inventory, search, retrieve (bash, Python, or whatever the backend expects).
4. Mode mapping from `WORKFLOW.md` modes to the backend's own query vocabulary.
5. Known limitations (e.g., no OCR — must be paired with a separate OCR step).

A backend that can't produce a filename-and-page citation for every search hit is not acceptable for this skill. Citation fidelity is non-negotiable.
