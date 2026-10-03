# Workflow — The Work, Not the Tool

This file describes the *work* the agent must do at each phase of the case-summary loop. It is backend-agnostic — it doesn't prescribe a CLI, a vector store, or a specific indexing tool. For how a specific backend implements each phase (today: case.dev; others can be added), see `BACKENDS.md`.

The phases map 1:1 to the loop in `SKILL.md`.

---

## 1. Ingest — make the corpus addressable and searchable

Every subsequent phase assumes the agent can (a) enumerate the files in the corpus, (b) retrieve the full content of any file by ID or filename, and (c) run content-based queries that return ranked passages with source + page metadata.

**Done looks like:**
- Every file in the source folder has an object ID and filename.
- Every non-image file is text-searchable (text layer present or extracted).
- A metadata listing (filename, content-type, size) is available.
- Any index-building / chunking the backend performs is complete or knowingly queued.

**Stop conditions:**
- Ingestion fails on a subset — note which files and continue.
- The corpus has no folder structure — work from filenames only.
- The user supplied a single ZIP — expand before ingesting.

---

## 2. OCR — when PDFs aren't already searchable

Most modern PDFs have a text layer and ingest correctly. Scans, screenshots-as-PDF, and fax-generated files do not. If **Inventory** finds PDFs with zero extractable text, OCR them before searching.

**Done looks like:**
- Every non-searchable PDF has been through OCR.
- Word-level positional data is available if the backend supports it (useful for page-and-word citations).
- The OCR job log is captured so the memo can note any files that failed.

**Stop conditions:**
- OCR fails on a file — note it in the memo's evidence inventory and proceed.
- A file is image-only with no meaningful text (a blank form, for example) — note and skip.

---

## 3. Inventory — build a mental model before querying

Before any targeted queries, the agent pulls the full filename list and a content-type breakdown, and skims for signals:

- Practice-area signals in filenames (e.g., `demand.pdf`, `MRI-L4-L5.pdf`, `claim-chart.xlsx`, `consent-decree.pdf`).
- Document-type clusters (depositions, medical records, discovery responses, lien correspondence) that should be routed to sibling skills per `ROUTING.md`.
- Gaps (a suit but no answer; a complaint but no contract attached) that should be flagged in the memo.

**Done looks like:**
- Filename list sorted and reviewed.
- Content-type counts tallied (e.g., 42 PDFs, 7 XLSXs, 3 DOCXs).
- Practice-area hypothesis with 1–3 candidate playbooks.

**Stop conditions:**
- Filename list is opaque (random hashes) — rely on content-type counts and global-overview queries instead.

---

## 4. Diagnose practice area — load playbook module(s)

Using the inventory and a single **global-overview** query ("what is this case about?"), the agent picks one or more playbook modules from the `PLAYBOOK-*.md` files. Each playbook has `triggers.filenames` and `triggers.content_signals` in its frontmatter — match filenames and global-overview content against them.

**Done looks like:**
- The chosen playbook(s) are recorded in the memo header.
- If two playbooks fit (e.g., a commercial contract dispute with an IP carve-out), both are loaded and their sections merged in the output.
- If no playbook fits, the agent proceeds with **core-only** behavior and labels the memo accordingly.

**Stop conditions:**
- Ambiguous — choose the best single fit, proceed, and note the ambiguity in `VIII. Strengths / Weaknesses / Red Flags`.
- Corpus is multi-matter (multiple unrelated cases) — surface this to the user before proceeding.

---

## 5. Map — iterative search per dimension

For each of the eight dimensions in `CORE-DIMENSIONS.md`:

1. Issue the base queries from `SEARCH-PLAYBOOK.md` for that dimension.
2. Issue the module queries from each loaded playbook for that dimension.
3. Read the top 3–10 chunks per query.
4. Decide: (a) record the hit in the working memo with citation, (b) re-query to narrow, or (c) delegate the cluster to a sibling skill per `ROUTING.md` if the document type warrants it.

**Query mode selection** — use hybrid as the default, semantic for paraphrase-tolerant questions, keyword for proper names and dates, entity for canonical mentions, global-overview for one-shot framing, graph/relational for cross-document relationships. See `SEARCH-PLAYBOOK.md`.

**Citation discipline** — every chunk the agent relies on is cited (object name + page or chunk ID). An uncited claim is either cut or labeled an assumption.

**Done looks like:**
- All eight dimensions covered.
- For each dimension, either a set of cited hits or an explicit "no evidence found" note.
- Sibling-skill deliverables (if any were routed) are present as consumable artifacts ready to slot into the memo.

**Stop conditions:**
- Queries saturate on a dimension — move on.
- Queries reveal a new practice area signal not in the loaded playbook — re-enter phase 4 to load the additional playbook.
- Corpus too large to cover with 100+ queries in the allotted time — narrow scope with user, prioritize the dimensions that matter for the user's stated objective.

---

## 6. Retrieve — pull the full object when a chunk is load-bearing

When a search hit is about to become a load-bearing citation in the memo (damages number, key admission, dispositive provision), retrieve the full source document and verify the surrounding context. A chunk is an index entry — the document is the evidence. Every load-bearing citation should be grounded in a reading of at least the page the chunk came from.

**Done looks like:**
- No load-bearing citation rests solely on a search snippet.
- Surrounding context either confirms the hit or disqualifies it.
- Downloaded files kept in a working directory for the attorney's later review.

---

## 7. Reduce — synthesize into the memo

Assemble the memo using the core skeleton in `OUTPUT-TEMPLATE.md`, plus the output sections contributed by each loaded playbook. Walk the quality checklist (core items + playbook-specific items). Flag any items that can't be satisfied.

**Done looks like:**
- Every core section populated (or "N/A — <reason>" noted).
- Every playbook insert populated.
- Quality checklist walked, with unsatisfied items explicitly flagged.
- Disclaimer present.
- Memo ready for attorney review.

---

## 8. Honesty rules (apply across phases)

- A claim in the memo without a citation is either cut or labeled an assumption.
- A citation without verification (legal citation marked `[VERIFY]`) is flagged.
- A dimension with no hits is labeled "no evidence found" — not omitted.
- A file the agent couldn't search (failed OCR, corrupt, password-protected) is listed in the memo as out-of-scope, not silently skipped.
- A scratch log of queries issued + what came back is kept so the attorney can audit the path the memo took.
