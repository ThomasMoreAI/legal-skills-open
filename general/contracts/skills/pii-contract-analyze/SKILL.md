---
name: pii-contract-analyze
title: PII Shield — Universal Legal Document Processor
description: 'Universal legal document processor with PII anonymization. Anonymize → Work → Deanonymize. Modes: MEMO (legal analysis), REDLINE (tracked changes in contract), SUMMARY (brief overview), COMPARISON (diff two docs), BULK (up to 5 files). Supports .docx and .pdf input. Trigger for: contract review, risk analysis, compliance check, GDPR review, clause analysis, tracked changes, redline, ''anonymize'', ''pii shield''. If user uploads contract/NDA/DSAR/HR doc — USE THIS SKILL. If user says ''skip pii'' or ''don''t anonymize'' — skip anonymization and work directly.'
author: gregmos
author_url: https://github.com/gregmos/PII-Shield/tree/main/nodejs-v2/plugin/skills/pii-contract-analyze
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

## ⚡ YOUR FIRST ACTION

When the user invokes `/pii-contract-analyze <anything>`, you respond in TWO turns.

### Turn 1 — acknowledge and wait

Do NOT call any tool. Do NOT read files. Do NOT run Bash. Reply with one short line and stop:

> Ready to start. Type **go** or **continue** to proceed.

Wait for the user's next turn. The MCP deferred-tools registry is often not populated yet on turn 1; it lazy-loads between turns.

### Turn 2 — discover and proceed

When the user replies with any continue signal (`go`, `continue`, `yes`, `ok`, `proceed`, or equivalents in their language), silently run this discovery sequence:

1. `ToolSearch(query: "select:mcp__PII_Shield_v2__list_entities", max_results: 1)`
2. If that returns "No matching deferred tools found": `ToolSearch(query: "select:mcp__pii-shield__list_entities", max_results: 1)`
3. If that also fails: `ToolSearch(query: "select:mcp__plugin_pii-shield_pii-shield__list_entities", max_results: 1)`

If any of them loads a schema → immediately call `list_entities` and continue with the Startup procedure, mode detection, and pipeline below. Do NOT surface these attempts to the user.

If all three fail → show the user:

> PII Shield MCP tools are installed on your host (Claude Desktop) but this session can't reach them. Known Anthropic bridging bug on Windows. Fixes: (1) restart Claude Desktop and start a fresh session, or (2) install `pii-shield-v2.0.1-plugin.zip` directly into this Cowork session. Meanwhile I can proceed without PII anonymization — OK?

### Rules

- Never call ToolSearch on turn 1. The prompt "type go" is the whole turn-1 response.
- Never fuzzy-search with bare keywords (`"list_entities"`, `"pii-shield"`) — underscore names don't match as substrings on Cowork CLI.
- Never declare the plugin missing before turn-2's full three-attempt `select:` chain has run.
- Never spawn sub-agents, grep the codebase, or probe filesystem paths / localhost ports / beacon files hunting for the server. If MCP tool discovery fails, the three `select:` attempts above are the whole fallback chain; anything beyond them is off-limits.

---

# PII Shield — Universal Legal Document Processor

Anonymize → Work → Deanonymize → Deliver. Claude NEVER sees raw PII at any stage.

## CRITICAL: PII never flows through Claude

**File handling**: The user must connect a folder (not attach the file directly to the message). When a file is attached to a chat message, its content is rendered and sent to the API as part of the prompt — Claude sees the raw data before PII Shield can process it. When a folder is connected, Claude only sees the file path and calls `anonymize_file(path)` — the MCP server reads and anonymizes the file locally. PII never enters Claude's context.

**If the user attaches a file directly**: Warn them politely: "For full PII protection, please connect the folder containing your document instead of attaching it directly. When a file is attached to a message, its content is included in the API request before PII Shield can anonymize it. I can still process it, but the privacy guarantee is stronger when you connect the folder."

- `anonymize_file` reads the file locally, anonymizes it, writes the result to disk, returns only `output_path` + `session_id` to Claude. **After HITL is approved, and only then, Claude reads the anonymized text from the output file — never before.**
- `deanonymize_*` tools write results to LOCAL FILES and return only the file path
- `get_mapping` returns only placeholder keys and types — no real values
- **ABSOLUTE BAN #1 — HITL GATE**: Claude must NEVER read, open, `cat`, `head`, `pandoc`, use the `Read` tool, `python`, `bash`, or in any way access the anonymized output file (`output_path`, `docx_output_path`) BEFORE the review panel reports that the user has clicked **Approve** (see "Human-in-the-Loop Review" below for how that signal arrives). Not to "preview entity quality", not to "verify placeholders", not to "check formatting", not to "plan the memo" — NEVER. The anonymized file is considered **SEALED** between `anonymize_file` and HITL approval. The HITL reviewer is the human, not Claude.
- **ABSOLUTE BAN #2 — DEANONYMIZED FILES**: Claude must NEVER read, open, cat, head, pandoc, or in any way access the content of deanonymized/restored files. Not to "verify", not to "check formatting", not to "validate" — NEVER. These files contain real PII. Just give the user the file path and STOP. Any "verification" of deanonymized output is a PII leak.
- Claude must NEVER read the source file (via Read tool, pandoc, python, bash, etc.) BEFORE or INSTEAD OF anonymization — always use `anonymize_file(path)` first
- If an anonymize tool times out or fails with a NON-"tool not found" error — retry once. If it still fails, tell the user PII Shield is unavailable and ask whether to proceed without anonymization or abort. NEVER fall back to reading the raw file.
- **NEVER** use `anonymize_text` or `scan_text` — these take raw text as input which means PII passes through the API. The ONLY exception is if the user explicitly pastes text into the chat (PII is already in the conversation).

## Startup

PII Shield is a pure-Node.js MCP server — no Python dependency, instant startup. On first run, the NER model (~665 MB fp32 ONNX GLiNER) and its runtime deps (`onnxruntime-node`, `@xenova/transformers`, `gliner`) download into `${CLAUDE_PLUGIN_DATA}/models` and `${CLAUDE_PLUGIN_DATA}/deps`. This takes 2–5 minutes once per plugin install and is cached for the full life of the plugin (survives host restarts, only wiped by `/plugin remove`).

### ⛔ ABSOLUTE RULE — NO SUB-AGENT DELEGATION

**NEVER delegate PII Shield tool calls to a sub-agent.** Not to a general-purpose agent, not to a Task agent, not to an Explore agent — NEVER. Sub-agents do not stream text to the user; they return one final message only when they exit. If PII Shield is initializing, a sub-agent will poll silently for minutes while the user sees nothing. This is the single worst UX failure mode. All PII Shield tool calls (`list_entities`, `anonymize_file`, `start_review`, etc.) MUST happen in the MAIN conversation.

If you cannot call a PII Shield tool because it shows "No such tool available" — the fix is the turn-1 / turn-2 pattern above (prompt for `go`, discover silently on turn 2), NOT a sub-agent.

### Startup procedure

1. **Call `list_entities`** — this happens on **turn 2** after the user sends a continue signal. See the YOUR FIRST ACTION block at the top of this skill for the exact two-turn flow. You MUST have `list_entities` responding before proceeding.
2. Identify the file(s) to process and determine the mode (MEMO, REDLINE, etc.)
3. Read the `list_entities` response to check NER status
   - If `"ner_ready": true` — proceed to `anonymize_file`
   - If `"ner_ready": false` — NER is still initializing. The response includes `phase` (`installing_deps` / `downloading_model` / `loading_model`), `progress_pct`, a human `message`, and a pre-formatted `user_message` field. **If the response ALSO contains a `first_run_notice` field (only present on the very first loading response per server process), print `first_run_notice` VERBATIM to the user as a plain chat message BEFORE anything else.** It explains where the ~700 MB NER cache will live and why the next session will be instant — the user needs to see this once, up front. Subsequent polls will NOT contain `first_run_notice`. **On every poll (including the first), print the `user_message` field VERBATIM to the user as a plain chat message BEFORE calling `list_entities` again.** This is the ONLY thing the user sees during the wait — do not paraphrase, do not summarize, do not skip it, do not batch it silently. **Wait and retry**: the server enforces a ~20 second throttle by holding the `list_entities` response for 20 s internally while `phase` is `installing_deps` / `downloading_model` / `loading_model`. First run may take 2–5 minutes. Between polls (inside the 20 s window) you MAY do useful prep work in the MAIN conversation only — read skill references, plan the analysis. Do NOT delegate any of this to a sub-agent (see the ABSOLUTE RULE above). **Do NOT call `anonymize_file` until `ner_ready: true`** — without NER, only regex patterns work, missing PERSON/ORGANIZATION/LOCATION entities.
   - If `"ner_error"` field present — show it to the user. If `"ner_error_suggestions"` array is also present (platform-specific recovery steps like "install VC++ Redistributable", "switch to Node 22 LTS"), print each entry verbatim as a bulleted list — these are the concrete actions the user should try next. If `"ner_error_diagnostic"` object is present, its `likely_cause` field is a one-word root-cause tag useful to include in any bug report the user may file.

### Long document handling (chunked processing)

For documents >15K characters, `anonymize_file` returns `"status": "chunked"`. **Chunked processing flow:**
1. `anonymize_file(path)` returns `session_id`, `total_chunks`, `processed_chunks: 1`
2. Loop: call `anonymize_next_chunk(session_id)` until `status` is `"complete"` — show "Anonymizing... [chunk X/Y]"
3. Call `get_full_anonymized_text(session_id)` to finalize — returns `output_path`, `session_id`, `output_dir`
4. Continue with the normal pipeline using the returned values

For short documents (<15K chars), `anonymize_file` processes everything in one call.

### File path resolution

Call `anonymize_file(file_path: "<path or filename>")` directly — no ceremony. The server auto-resolves:
1. The path as-given (if it's a valid absolute host path it just works)
2. `$PII_WORK_DIR/<basename>` if that env is set
3. BFS (depth 4) of `~/Downloads`, `~/Documents`, `~/Desktop`, `$PII_WORK_DIR` for an unambiguous match

If the response is `status: "error"` with a "file not found" or "ambiguous filename" hint — the file is in a non-standard location. Fall back to:

```
# create a marker next to the target file
touch "/path/visible/to/you/.pii_marker_abc"
# then:
resolve_path(filename: "<basename>", marker: ".pii_marker_abc")
# take host_path from the response and retry:
anonymize_file(file_path: "<host_path>")
```

The marker+resolve_path tools stay available as a reliability net — the auto-BFS handles ~95% of cases, marker covers the rest.

## Available MCP tools

| Tool name (suffix) | Parameters | Returns to Claude |
|---|---|---|
| `anonymize_file` | file_path, language, prefix, **session_id**, **review_session_id** | output_path (.txt) + session_id + doc_id + pool_size + documents_in_session + output_dir + docx_output_path (.docx, for .docx input only). For long docs: returns `status: "chunked"` with session_id and total_chunks. |
| `anonymize_next_chunk` | session_id | Progress: processed_chunks, total_chunks, progress_pct, entities_so_far |
| `get_full_anonymized_text` | session_id | output_path, session_id, output_dir, docx_output_path (same as anonymize_file) |
| `resolve_path` | filename, marker | absolute path + parent dir (fallback when auto-BFS in `anonymize_file` can't find the file — user-drops-marker-next-to-file ritual) |
| `deanonymize_text` | text, session_id, output_path | **File path only** (takes anonymized text, writes deanonymized file) |
| `deanonymize_docx` | file_path, session_id? | **File path only**. If `session_id` is omitted, server reads `pii_shield.session_id` from the input .docx's `docProps/custom.xml` — works across chats/sessions without needing to pass session_id manually. |
| `get_mapping` | session_id | Placeholder keys + types only |
| `list_entities` | — | Server status and config |
| `find_file` | filename | Full host path(s) — searches configured work_dir only (fallback) |
| `start_review` | session_id | Opens the review panel in the chat (MCP Apps iframe). No URL, no browser. |
| `apply_review_overrides` | session_id, overrides | Called automatically by the review panel when the user clicks Approve. Claude does NOT call this directly. |
| `apply_tracked_changes` | file_path, changes (JSON), author | Output .docx with Word-native w:del/w:ins revision marks |
| `export_session` | session_id, passphrase, output_path | `{archive_path, archive_size_bytes}` — encrypted `.pii-session` archive for team handoff. |
| `import_session` | archive_path, passphrase, overwrite? | `{session_id, overwritten, document_count, had_review}` — restores a session's mapping locally after receiving an archive from a colleague. |

**DO NOT USE these tools** (they exist on the server but must not be called for file workflows):
- `anonymize_text` — sends raw text through the API. Only acceptable if user pasted text into chat.
- `scan_text` — sends raw text through the API.
- `anonymize_docx` — use `anonymize_file` instead (handles .docx automatically).

**`prefix` parameter**: Optional per-doc label WITHIN a shared session. Example: `prefix="D1"` prepends to placeholders as `<D1_ORG_1>`. Use it only when the user explicitly wants to visually distinguish placeholders from different documents inside the SAME matter (power-user case: "party A track" vs "party B track"). The default behaviour — no prefix — is recommended; identical entities across files in one session will coalesce into the same placeholder automatically.

**`session_id` parameter (multi-file workflow)**: Pass the `session_id` from a previous `anonymize_file` call to ADD the new document to the same session. Identical entities across files in the session share the **same placeholder** (e.g. `Acme Corp.` becomes `<ORG_1>` in every file). The response includes the same `session_id`, a fresh `doc_id`, and `pool_size` (running count of unique entities). **This is the default in ALL modes (MEMO, REDLINE, SUMMARY, COMPARISON, BULK, ANONYMIZE-ONLY) when the user uploads N≥2 files and confirms they're part of one matter** — see `references/bulk-mode.md` "One matter" pipeline for the full step list. For unrelated files across separate matters, omit this parameter and use `prefix="D{i}"` instead.

**`review_session_id` parameter**: Pass the `session_id` from a previous `anonymize_file` call after HITL review. The server fetches the user's overrides internally and re-anonymizes. PII never passes through Claude.

**Preferred approach**: Always use `anonymize_file(file_path)` — only the file path (not content) passes through the API. The server auto-resolves paths via BFS of common user dirs, so passing a filename or the absolute path the user mentioned is fine. Fall back to `resolve_path(filename, marker)` or `find_file(filename)` only if the auto-resolve returns a `not_found` / `ambiguous` error.

## Skip mode

If user says "skip pii shield", "don't anonymize", "work directly" — skip anonymization, work with the file directly.

---

## Continuing in a later session (cross-chat deanonymize)

PII Shield v2.1+ embeds `pii_shield.session_id` into the `docProps/custom.xml` of every emitted `_anonymized.docx`. This makes the file **self-describing**: the server can recover the session_id without Claude holding it in context. If the session has multiple documents (a "one matter" multi-file session), EVERY file in the session carries the SAME session_id in custom.xml, and the shared mapping covers all of them — `deanonymize_docx` on any one file restores every placeholder in it from that matter's pool.

**When the user returns in a new chat with an anonymized document and asks to restore PII** (e.g. "deanonymize this", "give me the PII version", "restore my memo"):

1. Ask for (or accept) the file: `.docx` files carry their session_id internally. `.txt`/`.pdf` files don't — for those, the user must either pass the session_id or show you a parent anonymized `.docx`.
2. Call `deanonymize_docx(file_path: "<path>")` — **no `session_id` argument needed** for .docx with embedded metadata.
3. Server reads `docProps/custom.xml` → finds session_id → loads mapping from `~/.pii-shield/mappings/` → returns `restored_path`.
4. If response contains `"session_id_source": "custom_xml"` — tell the user the file was self-identifying (bonus clarity).
5. If response is an error like `Mapping not found for session 'X'`, the mapping was cleaned up (TTL, or it was created on another machine). Ask the user if they have a `.pii-session` archive to import (team-handoff case).
6. ABSOLUTE BAN #2 still applies: NEVER read the restored file.

For `.txt` / `.pdf` and for files where the user overwrote `custom.xml`: ask the user to pass `session_id` explicitly via `AskUserQuestion`, or show `list_entities` (which lists recent sessions) and let them pick.

---

## Team handoff (export / import encrypted session)

When one lawyer anonymized a document and a colleague needs to restore PII on their machine, the mapping itself must cross the trust boundary. PII Shield v2.1 ships this via an **AES-256-GCM + scrypt** encrypted archive — no network, no cloud.

### Exporter side — "передай коллеге" / "export for X"

When the user asks to export a session for a colleague:

1. Make sure you know the `session_id` to export. If it's the current session, use it; otherwise call `list_entities` to see recent sessions and confirm with the user.
2. Ask the user for a passphrase via `AskUserQuestion` (or let them paste one). Minimum 4 characters; in practice 16+ with words is safer. Do **not** suggest a passphrase yourself.
3. Pick an `output_path`: by default `<source_dir>/<matter-label>.pii-session`. Absolute paths work best.
4. Call `export_session(session_id, passphrase, output_path)`.
5. Show the user the archive path AND tell them verbatim:
   > "Send the colleague TWO things **via different channels**:
   > (1) the `.pii-session` archive (any file channel — email, Signal, SharePoint),
   > (2) the passphrase (a separate channel — phone call, password manager share).
   >
   > Never send both in the same message. The archive is authenticated-encrypted; a wrong passphrase fails the decrypt loudly.
   >
   > Also send the anonymized documents the colleague needs to restore — those are separate from the archive."
6. **Do NOT echo the passphrase in your reply.** If the user already typed it in chat that's their choice; you don't repeat it.

### Importer side — "восстанови от коллеги" / "import from X"

When the user receives an archive and asks to use it:

1. Confirm you have both: the `.pii-session` archive path and the passphrase.
2. Call `import_session(archive_path, passphrase)`. If the response is `error: Session 'X' already exists locally`, the same session_id already sits in the user's mapping store — ask the user whether to `overwrite` (true will replace the local copy with the imported one).
3. On success you get `session_id`. Now `deanonymize_docx(<colleague's anonymized file path>)` works — the file's `custom.xml` already names the session_id and the mapping is local.
4. If the user provides a wrong passphrase, the response `error` message says so literally — show it to the user, ask for the correct passphrase, retry.

---

## Reference files — read BEFORE starting the mode

Load the appropriate reference file(s) based on the detected mode. Reference files are in the `references/` directory next to this SKILL.md.

| Mode / Phase | Read BEFORE starting work |
|---|---|
| All modes | `references/hitl-review.md` (at the HITL Review step) |
| Path issues | `references/path-resolution.md` (for host path resolution details) |
| MEMO | `references/memo-writing-style.md` + `references/docx-formatting.md` |
| REDLINE | `references/redline-tracked-changes.md` |
| SUMMARY | `references/docx-formatting.md` |
| COMPARISON | `references/comparison-mode.md` + `references/docx-formatting.md` |
| BULK | `references/bulk-mode.md` + reference file(s) for the wrapped mode |
| ANONYMIZE-ONLY | No reference files needed |

**You MUST read the listed reference file(s) BEFORE starting analysis, not after.**

---

## Human-in-the-Loop Review (mandatory)

HITL review is **mandatory** after every `anonymize_file` call, unless the user has set `skip_review: true` in extension settings (Settings → Extensions → PII Shield). Check the `PII_SKIP_REVIEW` environment variable — if it equals `"true"`, skip the review step entirely.

**When review is active** (default), first explain what will happen, then call `start_review(session_id)`. The response opens an **in-chat review panel** (an MCP Apps iframe) with color-coded PII highlights. The panel runs entirely on the user's machine — no browser, no external server, no PII over the network.

Tell the user BEFORE calling `start_review`:

> "I've anonymized N entities in your document. I'm opening a review panel right here in the chat. You'll see color-coded highlights: click any to remove false positives, select text to add missed entities. Click **Approve** in the panel when done, then send me any short message (e.g. 'done', 'continue') to proceed."

### How approval reaches Claude — unconditional re-anonymize pattern

**Do NOT** use `AskUserQuestion` after `start_review`. **Do NOT** inspect the transcript for `apply_review_overrides` — that tool call is invisible to Claude on some hosts (known limitation). The server is the authoritative source of approval state.

Flow:

1. After `start_review(session_id)`, reply with the "send any short message" prompt above, then STOP and wait for the user's next turn.
2. On the user's next message (whatever it is), call `anonymize_file(file_path: "<original_path>", review_session_id: session_id)` **unconditionally**. The server returns one of three statuses:

| Response status | What it means | Action |
|---|---|---|
| `waiting_for_approval` | User hasn't clicked Approve yet. | Reply: "Still waiting for Approve click. Please click it in the panel and send any short message." Wait for next turn, retry this tool. |
| `approved_no_changes` | User approved without edits. Response includes original `output_path` / `docx_output_path` / `output_rel_path` / `docx_output_rel_path`. | Use these paths (same as originals). Proceed with pipeline. |
| `success` | User approved with edits (removed false positives and/or added missed entities). Response includes NEW `output_path` / `docx_output_path` / `output_rel_path` / `docx_output_rel_path` (with `_corrected` suffix). | **REPLACE** `session_id`, `output_path`, `output_rel_path`, `docx_output_path`, `docx_output_rel_path` with the new values. Old files are stale — never read them. |

This single unconditional call covers all three outcomes, skipping the ceremony of AskUserQuestion + transcript-inspection entirely.

**Reading output files**: always use `output_rel_path` (relative to the original input file's directory) joined with the input directory you passed — e.g. `Read("<input_dir>/<output_rel_path>")`. This works regardless of whether the caller's environment can access the absolute host path directly.

---

## MODE DETECTION

Detect the mode from the user's request. If ambiguous, ask.

| User says | Mode |
|---|---|
| "review contract", "risk analysis", "legal analysis", "write a memo", "compliance check" | **MEMO** |
| "tracked changes", "redline", "mark up", "make client-friendly", "edit the contract" | **REDLINE** |
| "summarize", "overview", "brief summary", "what's in the contract" | **SUMMARY** |
| "compare documents", "diff", "what changed", "differences" | **COMPARISON** |
| Multiple files uploaded + any of the above | **BULK** (wraps any mode above) |
| "just anonymize", "anonymize only", "only anonymization" | **ANONYMIZE-ONLY** |

### Multi-file clarification (triggered by FILE COUNT ≥ 2, not content)

Whenever the user uploads **2 or more files** for ANY mode (MEMO, REDLINE, SUMMARY, COMPARISON, BULK, ANONYMIZE-ONLY), BEFORE calling the first `anonymize_file` ask ONE `AskUserQuestion`:

> I see N files. Are they part of **one matter** (e.g. MSA + Amendment + SOW, same parties across files) or **separate matters** (e.g. unrelated NDAs from different clients)?

- **One matter (Recommended)** → chain `session_id` across all files. Identical entities share placeholders. One review panel with N tabs. One deanonymize call. See `references/bulk-mode.md` "One matter" pipeline.
- **Separate matters** → each file gets its own session with `prefix="D{i}"`. Placeholders don't coalesce across files. See `references/bulk-mode.md` "Separate matters" pipeline.

The question is based strictly on file count, never on peeking at file contents (ABSOLUTE BAN #1). If the user has already stated intent in the conversation ("compare these two unrelated NDAs", "merge these three amendments"), skip the question and pick the matching pipeline.

For N = 1 file this question does not apply — go straight into the mode's single-file pipeline.

---

## MODE: MEMO (Legal Analysis)

Full legal memorandum with risk assessment. The default mode. Read `references/memo-writing-style.md` + `references/docx-formatting.md` before starting.

### Pipeline

1. Warm-up (if not already done in YOUR FIRST ACTION): `list_entities()` → verify `ner_ready: true`. If `ner_ready: false`, follow the Startup procedure loop above (poll `list_entities` every ~20 s, print each `user_message` verbatim) before proceeding.
2. Call `anonymize_file(file_path: "<path or filename>")`. Remember `session_id`, `output_path`, `output_rel_path`, `output_dir`. **DO NOT Read any output file yet. Files are SEALED until HITL approves.** If response is `status: "error"` with "file not found" hint, fall back to `resolve_path` + marker per "File path resolution" above, then retry.
3. Call `start_review(session_id)` — opens the in-chat review panel. Tell the user verbatim: "Review panel opened. Click Approve in the panel when done, then send me any short message (e.g. 'done') to continue." Then STOP and wait for user's next message.
4. On the user's next message, call `anonymize_file(file_path: "<same path>", review_session_id: session_id)` **unconditionally** (no AskUserQuestion, no transcript inspection — the server is authoritative). Handle the response:
   - `status: "waiting_for_approval"` → reply: "Still waiting for Approve click. Please click Approve in the panel and send any short message." Wait and retry on the next turn.
   - `status: "approved_no_changes"` → use `output_path` / `output_rel_path` from the response (equals the originals). Proceed.
   - `status: "success"` → REPLACE `session_id`, `output_path`, `output_rel_path` with the NEW values from the response. Old paths are stale.
5. **Only now** Read the anonymized text: use `output_rel_path` joined with the original input file's directory (e.g. `Read("<input_dir>/<output_rel_path>")`). This works regardless of environment. `output_path` (absolute host path) is a fallback if you happen to have direct host access.
6. Analyze anonymized text → structured memo with `<ORG_1>` etc.
7. Create formatted .docx via docx-js (see `references/docx-formatting.md`)
8. `deanonymize_docx(formatted.docx, session_id)` → final.docx
9. Present the link to the user. **DO NOT read/verify deanonymized file.**

---

## MODE: REDLINE (Tracked Changes)

Apply tracked changes to make the contract more favorable. Output: .docx with Word-native revision marks. Read `references/redline-tracked-changes.md` before starting.

### Pipeline

1. Warm-up (if not already done in YOUR FIRST ACTION): `list_entities()` → verify `ner_ready: true`. If `ner_ready: false`, follow the Startup procedure loop above before proceeding.
2. Call `anonymize_file(file_path: "<path or filename>")`. Remember `session_id`, `output_path`, `output_rel_path`, `docx_output_path`, `docx_output_rel_path`, `output_dir`. **DO NOT Read any output file yet. All files are SEALED until HITL approves.** If response is `status: "error"` with "file not found", use `resolve_path` + marker fallback.
3. Call `start_review(session_id)` — opens the in-chat review panel. Tell the user verbatim: "Review panel opened. Click Approve in the panel when done, then send me any short message (e.g. 'done') to continue." Then STOP and wait for user's next message.
4. On user's next message, call `anonymize_file(file_path: "<same path>", review_session_id: session_id)` **unconditionally**. Handle:
   - `status: "waiting_for_approval"` → ask user to click Approve, wait, retry next turn.
   - `status: "approved_no_changes"` → use original `output_path` / `docx_output_path` / rel_paths from response. Proceed.
   - `status: "success"` → REPLACE `session_id`, `output_path`, `output_rel_path`, `docx_output_path`, `docx_output_rel_path` with the NEW values.
5. **Only now** Read the anonymized text via `<input_dir>/<output_rel_path>`.
6. Analyze: identify clauses to change, draft new wording (all in placeholders).
7. Apply tracked changes to the anonymized .docx (use `<input_dir>/<docx_output_rel_path>`) via OOXML (see `references/redline-tracked-changes.md`). Save in `output_dir`.
8. `deanonymize_docx(tracked_changes.docx, session_id)` → final.docx
9. Present the link to the user. **DO NOT read/verify deanonymized file.**

---

## MODE: SUMMARY (Brief Overview)

Concise document summary. Read `references/docx-formatting.md` before creating .docx.

### Pipeline

1. Warm-up (if not already done in YOUR FIRST ACTION): `list_entities()` → verify `ner_ready: true`. If `ner_ready: false`, follow the Startup procedure loop above before proceeding.
2. Call `anonymize_file(file_path: "<path or filename>")`. Remember `session_id`, `output_path`, `output_rel_path`, `output_dir`. **DO NOT Read any output file yet. SEALED until HITL approves.** If "file not found" → fall back to `resolve_path` + marker.
3. Call `start_review(session_id)`. Tell user: "Review panel opened. Click Approve, then send me any short message (e.g. 'done') to continue." Stop and wait for next message.
4. On user's next message, call `anonymize_file(file_path: "<same path>", review_session_id: session_id)` unconditionally. Handle the 3 statuses (`waiting_for_approval` → ask user to click Approve and retry; `approved_no_changes` → use originals; `success` → REPLACE all values).
5. **Only now** Read the anonymized text via `<input_dir>/<output_rel_path>`.
6. Write summary (1–2 pages max) with placeholders.
7. Create formatted .docx via docx-js.
8. `deanonymize_docx(summary.docx, session_id)` → final.docx
9. Present the link to the user. **DO NOT read/verify deanonymized file.**

### Summary structure

1. **Header**: Document type + parties (`Purchase Order between <ORG_1> and <ORG_2>`)
2. **Key terms table**: Party A, Party B, Subject, Term, Total value, Payment terms, Governing law
3. **Notable provisions**: 3–5 bullet points on unusual or important clauses
4. **Risk flags**: Brief list of potential issues (if any)

---

## MODE: COMPARISON (Diff Two Documents)

Read `references/comparison-mode.md` + `references/docx-formatting.md` before starting. Full pipeline is in the reference file. **HITL gate (ABSOLUTE BAN #1) applies to every `anonymize_file` call in this mode — never Read any `output_path` before its `session_id` is approved.**

---

## MODE: BULK (Multiple Files)

Read `references/bulk-mode.md` + reference file(s) for the wrapped mode before starting. Full pipeline is in the reference file. **HITL gate (ABSOLUTE BAN #1) applies to every `anonymize_file` call in this mode.** Each file gets its own `session_id` and its own review panel. Wait for **every** session to receive `apply_review_overrides` before reading any output file.

---

## MODE: ANONYMIZE-ONLY

Just anonymize and return the anonymized file(s). No analysis. No reference files needed.

### Pipeline (single file)

1. Warm-up (if not already done in YOUR FIRST ACTION): `list_entities()` → verify `ner_ready: true`.
2. Call `anonymize_file(file_path: "<path or filename>")`. Remember `session_id`, `output_path`, `output_rel_path`, `output_dir`. **DO NOT Read the output.** In ANONYMIZE-ONLY mode, Claude NEVER reads the file — user is the only one who sees anonymized content. If "file not found" → fall back to `resolve_path` + marker.
3. Call `start_review(session_id)`. Tell user: "Review panel opened. Click Approve, then send me any short message (e.g. 'done') to continue." Stop and wait.
4. On user's next message, call `anonymize_file(file_path: "<same path>", review_session_id: session_id)` unconditionally. Handle the 3 statuses (`waiting_for_approval` → ask user to click Approve and retry; `approved_no_changes` → use originals; `success` → REPLACE all values). Still DO NOT Read the output.
5. Present the anonymized file link (`output_path` and/or `<input_dir>/<output_rel_path>`) to the user and tell them the `session_id` in case they need deanonymization later. Tell them the anonymized `.docx` carries `session_id` in its metadata — they can return in a new chat with just the file and you'll be able to restore PII.

### Pipeline (multiple files → one shared session)

When the user uploads multiple files and says "just anonymize them" (no analysis requested), group them into **one session** so identical entities across files share placeholders. This is the v2.1 way; don't fall back to the legacy D1/D2 prefix pattern for this case.

1. Warm-up: `list_entities()` → verify `ner_ready: true`.
2. First file: `anonymize_file(file_path: "<path_1>")` — note the returned `session_id` (call it `S`).
3. Remaining files: for each file i in 2..N call `anonymize_file(file_path: "<path_i>", session_id: S)`. Each response returns the same `session_id`, a new `doc_id`, and a growing `pool_size`. All N emitted `.docx` carry `session_id=S` in their `docProps/custom.xml`.
4. Call `start_review(session_id: S)` once. The panel shows all entities across all N docs (they're a single session now). Tell the user: "Review panel opened. Click Approve, then send any short message to continue."
5. On user's next message, call `anonymize_file(file_path: "<path_i>", review_session_id: S)` for each path i in 1..N, unconditionally, and handle the 3 statuses per file (same logic as single-file step 4). If ANY returned `waiting_for_approval`, ask user to approve and retry those paths next turn.
6. Present all N anonymized file links to the user. State the `session_id` ONCE and explain: "Одинаковые стороны во всех файлах помечены одинаково. Когда понадобится расшифровать — верните любой из этих файлов (или ваш memo на их основе) в новом чате и вызовите `deanonymize_docx` — сессия определится автоматически по метаданным docx."

The same pattern (chain `session_id`) is also the default in BULK-wrapped modes (MEMO, REDLINE, SUMMARY, COMPARISON when N≥2 files). See `references/bulk-mode.md` for the full pipeline and for the N≥2 clarifying question (one matter vs separate matters) that the skill must ask before the first `anonymize_file` call.
