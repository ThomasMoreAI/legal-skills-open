# MODE: BULK (Multiple Files)

Process up to 5 files. Wraps any of the modes above (MEMO / REDLINE / COMPARISON / SUMMARY).

## Session semantics (v2.1.4)

When the user uploads multiple files, ALL of them go into **one shared session** (one `session_id`, one `mapping.json`, one consistent pool of placeholders) **if they belong to the same legal matter** — e.g. MSA + Amendment + SOW. Identical parties across files get the SAME placeholder (`Acme Corp` = `<ORG_1>` in every file).

If the files are **unrelated matters** that happen to be uploaded together (e.g. two NDAs from different clients), each file gets its OWN session — separate pools, no entity mixing.

**Which case applies is decided by the user**, not by Claude reading file contents. The skill asks a single `AskUserQuestion` before the first `anonymize_file`:

> I see N files. Are they part of **one matter** (e.g. MSA + Amendment + SOW, shared parties) or **separate matters** (e.g. unrelated NDAs)?

- **One matter (Recommended)** → chain session_id (this pipeline).
- **Separate matters** → per-file sessions (legacy behaviour described at the end of this file).

The question is based purely on FILE COUNT ≥ 2. It is NOT based on peeking at content (ABSOLUTE BAN #1 — Claude does not read source files before anonymization). If the user already stated their intent in the conversation ("compare these two unrelated NDAs"), skip the question.

## Pipeline — "One matter" (unified session, default)

```
1. Warm-up: list_entities() → confirm ner_ready: true.

2. First file:
     anonymize_file(file_path: "<file_1>")
     → Remember: session_id=S (the response's session_id),
                 doc_id_1, output_path_1, docx_output_path_1, output_rel_path_1

3. Remaining files (i = 2..N):
     anonymize_file(file_path: "<file_i>", session_id: S)
     → Same session_id S returned; new doc_id_i; pool_size grows as new entities
       are discovered; identical entities across files share placeholders.
     DO NOT read any output file yet (HITL absolute ban).
     If "file not found" → resolve_path + marker fallback per SKILL.md.

4. HITL review — ONE call covers all N docs:
     start_review(session_id: S)
     → The iframe renders N tabs (one per doc) because the session now holds
       N PerDocReview entries. Per-doc entities, per-doc Approve, per-doc
       overrides. Do NOT pass `session_ids=[...]` — that is the legacy
       multi-session form.

5. Tell the user verbatim: "Review panel opened with N tabs (one per document).
   Click Approve on each tab when done, then send me any short message
   (e.g. 'done', 'continue') to proceed." STOP and wait for user's next message.

6. On user's next message, for EACH file i in 1..N call:
     anonymize_file(file_path: "<file_i>", review_session_id: S)
   The server locates the per-doc review by source_file_path and returns ONE of:
     - "waiting_for_approval"  → that specific doc still unapproved (other
        tabs may or may not be done). Ask user to click Approve on the named
        doc, retry on next turn.
     - "approved_no_changes"   → use the doc's original output_path/rel_path
        from the response (they equal the paths from step 2/3).
     - "success"               → REPLACE the held values for THIS doc with
        the new `_corrected` ones from the response. Other docs untouched.
   If any response is waiting_for_approval, wait and retry only the unapproved
   doc(s) — the already-settled docs stay settled.

7. After all N docs settled, read each anonymized text:
     Read("<input_dir_i>/<output_rel_path_i>")
   (Per-file path — each doc lives in its own pii_shield_<session>/ outdir
   with its own `<stem>_anonymized.txt` / `_anonymized.docx`.)

8. Apply the requested mode (MEMO / SUMMARY / COMPARISON) ACROSS all anonymized
   texts. Because the pool is shared, cross-document references by placeholder
   are unambiguous: `<ORG_1>` is the same party everywhere.

9. Create the output .docx (memo / redline / comparison / summary) with
   placeholders from the shared pool. Because the skill wrote the file through
   docx-js, embed session_id in its custom.xml is handled automatically by the
   deanonymize path below — no extra step needed on the skill side.

10. Deanonymize the final output:
      deanonymize_docx(file_path: "<final.docx>")
    No session_id arg required — the server reads `pii_shield.session_id`
    from the final.docx's `docProps/custom.xml` (if present) or from the
    anonymized parent used to build it. The shared mapping covers every
    placeholder in the final memo in a single restore pass.

11. Present the link to the user. **DO NOT read/verify the deanonymized file.**
```

### Why chaining is the right default

- **One Acme = one `<ORG_1>`.** Claude's analysis across documents treats the party consistently; no risk of "doc 1 says `<ORG_1>` won, doc 2 says `<ORG_1>` lost" confusion when they're the same entity named twice.
- **One deanonymize call.** The user doesn't have to remember which session belongs to which doc — `deanonymize_docx(final.docx)` just works via `docProps/custom.xml`.
- **Persistence across chats.** Coming back two weeks later with any of the session's anonymized files → server resolves the session from custom.xml → entire matter's mapping restored.

### `prefix` parameter — optional per-doc label within a shared session

If the user explicitly wants to DISTINGUISH placeholders originating from different docs **inside the same matter** (rare: e.g. "party A track" vs "party B track"), pass `prefix="D1"` on file 1 and `prefix="D2"` on file 2. The pool stays shared (identical entities still coalesce by exact-text match), but per-doc prefix appears in the placeholder (`<D1_ORG_1>` vs `<D2_ORG_1>`). This is a POWER-USER override; default behaviour (no prefix) is recommended.

## Pipeline — "Separate matters" (legacy per-file sessions)

Only used when the user explicitly says the files are unrelated (e.g. "compare these two unrelated NDAs from different clients"). Each file gets its own session; the final output typically references each doc by a legend (D1/D2/…) rather than merging their entities.

```
1. Warm-up: list_entities().
2. For each file i (1..N):
     anonymize_file(file_path: "<file_i>", prefix: "D{i}")
     → session_id_i, output_path_i (distinct sessions, independent mappings)
3. HITL: start_review(session_ids=[sid_1, sid_2, ..., sid_N])
   (Legacy array form — one tab per session, each session has one doc.)
4. Tell user: "Review panel opened with N tabs, click Approve on each…" STOP.
5. On user's next message, call anonymize_file(file_path_i, review_session_id=sid_i)
   for EVERY document. Handle the 3 statuses as in step 6 above.
6. Read each anonymized text.
7. Apply the requested mode across all anonymized texts.
8. Create output .docx. Placeholders from different sessions don't collide
   because of the prefix (`<D1_ORG_1>` vs `<D2_ORG_1>`).
9. Deanonymize: use the primary document's session_id_1 via deanonymize_docx
   for that doc's placeholders; for cross-doc placeholders in a consolidated
   memo, either call deanonymize_text per snippet OR leave them unrestored
   with an appended legend table mapping `D1` → <filename_1>, etc.
10. Present the link. DO NOT read/verify.
```

## Important

- **Default is chained session** (one matter). Ask the user ONCE before step 2; trust their answer.
- **HITL gate (ABSOLUTE BAN #1) applies to every `anonymize_file` call in either path.** Never read any `output_path` before its doc is approved.
- **Never poll, never inspect transcript, never AskUserQuestion after start_review.** The server is authoritative — `anonymize_file(review_session_id=sid)` on the user's next message tells you everything via its 3-status response.
