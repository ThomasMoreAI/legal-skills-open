# MODE: COMPARISON (Diff Two Documents)

Compare two versions of a document or two related documents. Show what changed.

## Pipeline

```
1. Warm-up: list_entities() → confirm ner_ready: true
2. anonymize_file(file_path: "<doc1 path or filename>", prefix="D1")
   → session_id_1, output_path_1, output_rel_path_1 (+ docx_output_rel_path_1 for .docx)
   DO NOT read any output file yet! (HITL absolute ban)
   If "file not found" — fall back to resolve_path + marker per SKILL.md "File path resolution".
3. anonymize_file(file_path: "<doc2 path or filename>", prefix="D2")
   → session_id_2, output_path_2, output_rel_path_2
   DO NOT read any output file yet.
4. HITL Review (BOTH documents in a single panel):
   start_review(session_ids=[session_id_1, session_id_2])
   → Opens the in-chat review panel (MCP Apps iframe) with tabs for both documents.
   Do NOT call start_review separately for each document.
5. Tell the user verbatim: "Review panel opened with both documents as tabs. Click Approve
   on each tab when done, then send me any short message (e.g. 'done', 'continue') to proceed."
   STOP and wait for user's next message.
6. On user's next message, call BOTH:
   anonymize_file(file_path_1, review_session_id=session_id_1)
   anonymize_file(file_path_2, review_session_id=session_id_2)
   (in parallel or sequentially) — each returns one of three statuses:
   - "waiting_for_approval"  → that document still unapproved
   - "approved_no_changes"   → use originals (output_path, output_rel_path in response)
   - "success"               → REPLACE session_id/output_path/output_rel_path for this doc
   If ANY response is waiting_for_approval, ask user to click Approve on the unapproved tab
   and send any message; wait next turn and retry just that doc.
7. After both docs are settled (approved_no_changes or success), read the anonymized text
   via "<input_dir_X>/<output_rel_path_X>" for each document.
8. Compare: structural diff (added/removed/changed clauses) in placeholder space
9. Create comparison report .docx via docx-js
   — Use session_id_1 for deanonymization (primary document)
   — D2 placeholders remain as-is OR use deanonymize_text for D2 references
10. deanonymize_docx(comparison.docx, session_id_1) → final.docx
11. Copy to the agreed output folder, present link to user.
    **DO NOT read, verify, or pandoc the deanonymized file — it contains real PII. Just give the path.**
```

**Important**: Do NOT call `start_review` separately for each document. Use `session_ids` array to open a single tabbed panel covering both.

**Important**: Never poll any tool, never inspect the transcript, never AskUserQuestion. The server is authoritative — `anonymize_file(review_session_id=sid)` on the user's next message tells you everything you need via its 3-status response.

**Note**: With prefix support, `<D1_ORG_1>` and `<D2_ORG_1>` won't collide even if both files mention the same entity.
