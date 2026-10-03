# Human-in-the-Loop Review (after anonymization)

HITL review is **mandatory** after every `anonymize_file` call (unless `PII_SKIP_REVIEW=true` in extension settings). It runs **100% on the user's machine** via an MCP Apps iframe — PII never leaves their computer and no browser/external server is involved.

## The flow in one paragraph

`anonymize_file` writes a SEALED anonymized file to disk and returns `session_id` + `output_path` + `output_rel_path`. Claude then calls `start_review(session_id)`, which opens an in-chat review panel (MCP Apps iframe) in the conversation UI. The user sees color-coded highlights, clicks any to remove false positives, selects text to add missed entities, then clicks **Approve**. Claude tells the user to send any short message to continue, waits for the next turn, then calls `anonymize_file(path, review_session_id=session_id)` **unconditionally** — the server reports one of three actionable statuses. **No PII ever passes through Claude.**

## Review pipeline

1. `anonymize_file` returned `session_id`, `output_path`, `output_rel_path` (maybe `docx_output_path` + `docx_output_rel_path`). **Do not Read any output file yet.** Files are SEALED.

2. Call `start_review`. **If you have multiple session_ids (2+ documents), pass them ALL in one call:**
   - **Single document:** `start_review(session_id=<sid>)`
   - **Multiple documents:** `start_review(session_ids=[sid_1, sid_2, ...])` — returns a single panel with tabs for all documents. Do NOT call `start_review` separately for each document.
   - The response opens the in-chat review panel automatically (MCP Apps iframe resource `ui://pii-shield/review.html`).

3. Tell the user verbatim: "Review panel opened. Click **Approve** in the panel when done, then send me any short message (e.g. 'done', 'continue') to proceed." Then **STOP and wait for the user's next message.**

   While waiting, you MUST NOT:
   - `Read` / `Bash(cat|head|pandoc)` / any tool that touches `output_path` / `output_rel_path` / `docx_output_path` / `docx_output_rel_path` — all SEALED
   - Call `get_mapping`, `anonymize_text`, or any tool that touches the anonymized content
   - Spawn a sub-agent (see NO SUB-AGENT DELEGATION rule in SKILL.md)
   - Call `AskUserQuestion` — the continue-prompt replaces it
   - Inspect the transcript for `apply_review_overrides` — invisible on some hosts, unreliable signal

   While waiting, you MAY:
   - Read skill reference files (memo style, docx formatting, etc.)
   - Plan the analysis structure in your head

4. **On the user's next message (whatever its content), call `anonymize_file(file_path: "<original_path>", review_session_id: "<sid>")` unconditionally.** The server is the authoritative source of approval state. It returns ONE of these three statuses:

   | Response `status` | Meaning | What to do |
   |---|---|---|
   | `waiting_for_approval` | User hasn't clicked Approve yet. | Reply: "Still waiting for Approve click. Please click Approve in the panel and send any short message." Wait next turn, retry this tool. |
   | `approved_no_changes` | User approved without edits. Response carries the ORIGINAL `output_path` / `docx_output_path` / `output_rel_path` / `docx_output_rel_path`. | Use these. No re-anonymization ran. Proceed. |
   | `success` | User approved WITH edits (removed FPs and/or added entities). Response carries NEW paths (with `_corrected` suffix). | **REPLACE** every path/session_id you were holding with the new values. Old files are stale — never touch. |

5. **Reading the output file**: always via `output_rel_path` joined with the original input file's directory. Example:
   ```
   Read("<input_dir>/<output_rel_path>")
   ```
   This is portable across environments. `output_path` (absolute host path) is a fallback if you have direct host access.

6. If the user explicitly tells you to skip review (e.g. "just proceed"), simply proceed with the original `output_path`. But HITL-skip is the user's call, never Claude's.

## Absolute rules

- **NEVER** Read, `cat`, `head`, `pandoc`, or otherwise access `output_path` / `docx_output_path` / `output_rel_path` / `docx_output_rel_path` before step 4 above has returned `approved_no_changes` or `success`. This is ABSOLUTE BAN #1 in SKILL.md. Violations are PII leaks of the same severity as reading a deanonymized file.
- **NEVER** read, log, or forward the contents of the decisions archive JSON. You do not need to; the server applies it.
- **NEVER** pass `entity_overrides` as an inline parameter — always use `review_session_id` so the server handles overrides internally.
- **NEVER** call `apply_review_overrides` yourself. The iframe calls it when the user clicks Approve. The server stores approval state; your `anonymize_file(review_session_id=sid)` call on the next turn is how you read that state.
- **NEVER** try to find missed PII yourself by reading the source file — that defeats anonymization.
- After HITL, if the status was `success`, you MUST use the NEW `session_id` / `output_path` / `docx_output_path` / `output_rel_path` / `docx_output_rel_path` for every downstream step. The old values are dead.
- Keep the original source `file_path` around — you need it for the re-anonymize call.

## What if the user keeps sending "still not approved"?

If step 4 keeps returning `waiting_for_approval` across multiple user turns:
1. Ask the user to confirm they clicked **Approve** at the top of the review panel.
2. If the panel disappeared or shows an error, ask the user to describe what they see. A host restart or a new `start_review` call restores the panel.
3. If the user insists they approved but the status stays stuck, the iframe → server bridge may be broken on this host. Fall back: tell the user to reply with the literal word "approve" in their next message, and treat that as implicit no-changes approval (proceed with the ORIGINAL `output_path` unchanged). Do this only with their verbal confirmation.

Never, under any circumstances, proceed past HITL by reading the sealed file. If HITL truly can't complete, abort and tell the user.
