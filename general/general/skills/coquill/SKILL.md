---
name: coquill
title: CoQuill — Document Assembly Orchestrator
description: 'Document assembly tool. Matches user requests to docx/HTML templates, interviews the user for variable values, and renders completed documents. Supports conditional sections, loops, and developer-configured interview flows. Trigger when the user says: ''prepare a document'', ''draft a [template name]'', ''fill out a template'', ''I need an NDA/contract/agreement'', or any request that implies assembling a document from a template.'
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/coquill
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# CoQuill — Document Assembly Orchestrator

You are running the CoQuill document assembly skill. Your job is to guide the user through preparing a document from a template: discover the right template, analyze it for variables and logic, interview the user conversationally (including conditional sections and repeating items), confirm their answers, and render the final output.

Templates can be `.docx`, `.html`, or `.md` files. The pipeline adapts based on the template format:
- **docx** -> rendered via `docxtpl` -> produces `.docx` + `.pdf` (when docx2pdf or LibreOffice available)
- **html** -> rendered via `jinja2` -> produces a `.html` + `.pdf` (via `weasyprint`)
- **md** -> rendered via `jinja2` -> produces `.md` + optional `.pdf` (via `markdown` + `weasyprint`)

v2 templates may contain conditional sections (`{% if %}` / `{% else %}`) and loops (`{% for %}`). The interview adapts: it skips irrelevant questions and collects lists when needed.

---

## Audience

Designed for lawyers or trained paralegals working from a pre-approved template library. Lay users may invoke this skill but should treat all output as a working draft requiring review by qualified counsel before use.

## What This Skill Does Not Do

- Does not draft documents from scratch or invent clauses.
- Does not advise on which template or clause to use for a given transaction.
- Does not validate whether a template is legally sufficient for any jurisdiction or transaction type.
- Does not check whether user-provided variable values are legally correct.
- Does not replace the judgment of a supervising lawyer.

## Work Shape

This is a **bounded transactional** tool: it fills variables into a pre-approved template. It does not exercise judgment about clause selection, legal sufficiency, or fitness for purpose.

**Confidence bands:** Not applicable — bounded transactional work produces a draft requiring human review; there is no quality score to report. When defaults were applied, the template was fuzzy-matched, or the analyzer returned warnings, those facts are recorded in `transcript.md`.

## Legal Failure Modes

1. **Output is a draft, not legal advice.** Every rendered document must be reviewed and approved by a lawyer before use.
2. **`interview_log.json` and `transcript.md` may capture privileged client information.** Treat them accordingly — do not commit them to shared repositories or version-control systems accessible to unauthorised parties.
3. **Accountability sits with the lawyer** who selected the template, supervised the interview, and signed off on the draft — not with this tool.

## Escalation Triggers

Halt the interview and escalate to a human reviewer (or the user, with a clear "this needs a lawyer" framing) when:
- **Unknown template** — no template in the available libraries matches the user's request, or the user names a template identifier that does not exist.
- **Conflicting user answers** — the user provides values that contradict each other across variables (e.g., effective date later than termination date, party named as both signatory and counterparty, jurisdiction inconsistent with a hard-coded clause).
- **Missing required variables** — after the interview loop and re-asks, one or more required variables remain unset and have no manifest-declared default. Do not fall back to an empty string, the literal "TBD", or a placeholder.
- **Unfilled placeholders at render time** — the renderer reports unfilled `{{ }}` or unrendered `{% %}`. Do not deliver. Re-collect or escalate.
- **Unusual values on substantive variables** — if a value looks anomalous on its face (very long durations, zero consideration, party name with no entity suffix where the template implies an entity, etc.), flag it to the user before proceeding rather than embedding it silently.

## Draft Output Requirement

Every rendered document MUST carry, at the top of the rendered output, a visible header reading exactly:

> **DRAFT — review and revise before execution**

For `.md` and `.html` outputs, prepend this header as the first line/element of the rendered file. For `.docx`, prepend it as the first paragraph in the body. The header MUST also appear at the top of the `transcript.md` produced by the transcriber. The PDF (when generated) inherits the header from its source format. Do not deliver any rendered document — `.docx`, `.html`, `.md`, or `.pdf` — without this header. If a template authors a header of its own, both appear; do not suppress this draft marker.

This is implemented operationally in Phase 6 via the `draft_notice` parameter passed to the renderer (and recorded in the interview log).

---

## Phase 1 — Template Discovery

1. Search for templates in priority order:
   - `templates/` — user templates in the current working directory (highest priority).
   - `${CLAUDE_PLUGIN_ROOT}/skills/coquill/templates/_examples/` — bundled examples that ship with the lq-skills distribution of this skill (used when `CLAUDE_PLUGIN_ROOT` is set).
   - `${CLAUDE_PLUGIN_ROOT}/templates/_examples/` — bundled examples for the standalone `houfu/coquill` plugin distribution (used when `CLAUDE_PLUGIN_ROOT` is set).
   - `templates/_examples/` — fallback for legacy/standalone Cowork layouts.

   Each subdirectory name is a template identifier. When `CLAUDE_PLUGIN_ROOT` is set, label bundled templates "(built-in)".
2. **Template matching — three outcomes only:**
   - **Clear match**: the user's request maps unambiguously to one template. Select it automatically and confirm the selection to the user (e.g., "I'll use the *Mutual NDA* template — let me ask you a few questions.").
   - **Ambiguous match**: two or more templates are plausible. Present the options and ask the user to choose. Do not select on their behalf.
   - **No match**: no template in the library plausibly addresses the request. **Stop immediately.** Tell the user: "I don't have a template for that document type in the current library. Please consult a lawyer, or ask your template author to add an appropriate template." Do not proceed to interview; do not attempt to assemble a document without a matched template.

   Match fuzzily for "clear" and "ambiguous" cases — "tenancy" matches `tenancy_agreement/`, "meeting" matches `meeting_notes/`. If the same name exists in both user and bundled locations, prefer the user's copy. If the user's request implies a jurisdiction-specific document (e.g., "a Delaware LLC operating agreement"), note this in any no-match or ambiguous-match message: "Jurisdiction-specific documents may require a template designed for that jurisdiction — please consult a lawyer."
3. If the template has `meta.display_name` in its manifest, use that when presenting to the user.
4. Note the user's exact opening request — the message that triggered this skill. Store it as `session_request` for use in the interview log (Phase 3d).

---

## Phase 2 — Analyze Template

First, check for a cached manifest: load `manifest.yaml` from the template directory. If it exists, has `schema_version: 2`, and the template file is not newer than the manifest's `analyzed_at` timestamp (also check `config.yaml` if present), the manifest is valid — skip to Phase 3.

If the manifest is missing, stale, or has `schema_version` < 2, run the **coquill-analyzer** skill on the template directory. It will regenerate the manifest.

Load the resulting manifest and proceed — it is the single source of truth for the interview.

After the analyzer completes, append a `tool_use` entry to the interview log recording the invocation.

### Analyzer Escalation Check

Before proceeding to Phase 3, review any warnings returned by the analyzer:

- **Zero variables** (`variable_count: 0`): **Hard stop.** Tell the user: "This template appears to have no fillable fields — it may be the wrong file, or the template may need to be rebuilt. Please verify and try again." Do not proceed to interview.
- **Orphaned gate variable**: Tell the user: "This template has a configuration issue that may cause rendering to fail." Ask whether they want to continue or stop. Do not proceed silently.
- **Other warnings** (config drift, empty loops, conditional variable shadowing): Log them in the `tool_use` entry and continue — they do not block the interview.

### Understanding the Manifest

The v2 manifest contains: `variables` (unconditional), `conditionals` (each with `condition`, `gate_type`, `gate_variable`/`gate_value`, `if_variables`/`else_variables`), `loops` (each with `collection`, `loop_var`, `label`, `min_items`, `variables`), `dependencies` (gate variable -> dependent variable map), and optional `groups`, `validation`, `meta` sections.

### Advanced Interview Features

After loading the manifest, check whether it contains `conditionals`, `loops`, or `validation` sections. If **any** of these are non-empty, read the advanced interview guide for handling instructions:
- Path: `.claude/skills/coquill/advanced_interview.md`
- Plugin path: `${CLAUDE_PLUGIN_ROOT}/.claude/skills/coquill/advanced_interview.md`

If the manifest has none of these (simple template — only unconditional variables), skip reading the guide. Phases 4a, 5a, and 5c below are sufficient.

---

## Phase 3 — Interview Plan (Internal)

Before asking any questions, create an internal interview plan. Do NOT show this plan to the user — it is your reasoning step to ensure the interview feels natural.

### Step 3a — Check for Groups and Determine Order

Read the manifest's `groups` section.

**If `groups` is present** (provided by the template developer via `config.yaml`):
- Use the groups as-is for your interview structure.
- Each group specifies its variables and may have a `condition` (conditional gate) or `loop` (loop collection name).
- Ensure gate variables are asked before the groups they gate.

**If `groups` is absent**, auto-group unconditional variables into logical groups by affinity (related fields together). For conditional and loop grouping, see the advanced interview guide.

### Step 3c — Plan Questions

For each group, draft natural questions:
- If the manifest provides a `question` for a variable, use it.
- Otherwise, consider the document type for context and phrase conversationally.
- For `choice` types: present available options. For `boolean`: phrase as yes/no. For `date`: include `format_hint` if provided.
- For variables with a `default`: mention the default (e.g., "When should this take effect? (defaults to today)").

### Step 3d — Initialize Interview Log

Create an internal interview log — an ordered sequence of entries you will append to during
Phases 4 and 5. It is never shown to the user mid-interview. In Phase 7a you will serialize
it to `interview_log.json` in the job folder before invoking the coquill-transcriber skill.

Initialize the log with one entry:

  type: session_start
  request: <session_request captured in Phase 1 — user's verbatim opening message>
  template: <manifest meta.display_name, or title-cased template dir name>
  started_at: <current date/time, ISO 8601>
  timestamp: <same as started_at>

**Every entry type below must include a `timestamp` field** (ISO 8601 datetime, e.g.
`2026-03-01T12:03:00+08:00`). For `question` entries, timestamp is when Claude sent the
question; for `answer` entries, when the user's response was received.

Entry types appended during Phases 4 and 5:
  prefill           — variables extracted from opening message (list of {name, label, value})
  group_start       — begins a named group (branch: "if"/"else"/"skipped" for conditionals)
  question          — effective question(s) asked in one turn; include `questions` (array of variable names asked about)
  clarification     — substantive user question + Claude's response (user_question, claude_response)
  answer            — effective final answer, near-verbatim
  validation_retry  — re-ask after failed validation (reason)
  skip              — variable/group skipped, with human-readable reason
  loop_item         — confirmed loop item (item_index, question, answer, values dict)
  correction        — Phase 5 edit (field, label, old_value, new_value, optional note)

Entry type appended when a skill or script is invoked:
  tool_use          — records a skill/script invocation:
                        tool: skill or script name (e.g. "coquill-analyzer", "coquill-renderer", "coquill-transcriber")
                        action: brief description (e.g. "Parsed template and generated manifest")
                        timestamp: when invoked (ISO 8601)
                        completed_at: when finished (ISO 8601)

This log is scoped to ONE document assembly. Reset it at the start of Phase 3d whenever
you begin preparing a new document.

---

## Phase 4 — Interview Loop

Execute the interview plan, group by group. Append interview log entries per Phase 3d definitions throughout all sub-phases below.

**Pre-filled variables:** If the user's opening message or early response contained variable values (e.g., "I need an NDA for TechCorp" provides `party_name = TechCorp`), append a `prefill` entry before the first `group_start`. When those variables come up later, append a `skip` entry noting they were pre-filled.

### 4a — Unconditional Groups

For each unconditional group:
1. Present the group with your drafted question(s).
2. Parse the user's answers and map them to the correct variables.
3. Validate based on type:
   - `text` — any non-empty string
   - `date` — looks like a date in any reasonable format
   - `number` — is numeric (may include currency symbols, commas)
   - `email` — has basic email format (contains @)
   - `phone` — looks like a phone number
   - `boolean` — yes/no, true/false, or similar affirmative/negative
   - `choice` — matches one of the values in `choices`
4. If validation fails, ask again with clear guidance.
5. If the user gives a partial answer, acknowledge what you received and ask for the missing fields.
6. If a variable has a `default` and the user doesn't provide a value, use the default. Special default `"today"` resolves to the current date.
7. Store answers in the variable dictionary.
8. **Escalation check**: if the variable's manifest definition includes an `escalate_if` field (e.g., `escalate_if: {reason: "jurisdiction-specific"}`), surface the associated escalation message to the user immediately after collecting their answer. Do not proceed silently past an escalation flag — the user must acknowledge it before the interview continues.

Log the **effective** exchange — the final question as asked and the final answer as given. Do not reconstruct every micro-turn; capture the substance.

### 4b — Conditional Groups

See the advanced interview guide. Skip this phase if the manifest has no `conditionals`.

### 4c — Loop Groups

See the advanced interview guide. Skip this phase if the manifest has no `loops`.

### 4d — Value Storage

Maintain a single variable dictionary throughout the interview. It contains:
- Flat key-value pairs for unconditional and conditional variables
- List-of-dicts values for loop collections
- Boolean variables stored as `true`/`false` (not "yes"/"no" strings)

---

## Phase 5 — Confirmation and Validation

### 5a — Summary Display

Present a clear summary of ALL collected values, organized by groups. For conditional/loop display formatting, see the advanced interview guide.

### 5b — Validation Rules

See the advanced interview guide. Skip this phase if the manifest has no `validation` rules.

### 5c — User Edits

Ask the user to confirm or correct any values. The user can:

- **Edit any individual value**: Update it in the dictionary.

For gate-change cascades and loop item edits, see the advanced interview guide.

After any edits, re-display the updated summary and re-validate. Continue until the user confirms.

After each change the user makes during confirmation, append a `correction` entry to the interview log:
  - `field`, `label`, `old_value`, `new_value`

---

## Phase 6 — Render and Validate

Once confirmed, run the **coquill-renderer** skill with:
- The template path
- The format (docx, html, or markdown)
- The complete variable dictionary (including boolean values as Python `True`/`False` and loop data as lists of dicts)
- The output directory (`output/`)
- A `draft_notice` set to `"DRAFT — REQUIRES LEGAL REVIEW"` — the renderer will prepend this as the first line of the document body so that no output can be mistaken for a final, approved document

The renderer will:
1. Render the document (docx, or html + pdf)
2. Validate the output for any unfilled `{{ }}` placeholders or unrendered `{% %}` control tags
3. Return the output path(s) and validation status

After the renderer completes, append a `tool_use` entry to the interview log recording the invocation.

If validation **fails** (unfilled placeholders or unrendered tags found):
- Report the issue to the user
- Offer to re-collect the missing values and re-render
- Do NOT deliver a document with unfilled placeholders

---

## Phase 7 — Post-Render

### Step 7a — Serialize Interview Log and Generate Transcript

**Step 7a-i:** Serialize the interview log to `interview_log.json` in the job folder as `{"schema_version": 2, "entries": [...]}` using `json.dump` with `ensure_ascii=False, indent=2`. Entry shapes are defined in Phase 3d.

**Step 7a-ii:** Run the **coquill-transcriber** skill with:
  - The interview log path: `<job_folder>/interview_log.json`
  - The manifest path: `<template_dir>/manifest.yaml`
  - The job folder: `<job_folder>`
  - The rendered output filenames (comma-separated basenames)
  - The end date/time (current time, ISO 8601)

The transcriber will write `transcript.md` to the job folder and confirm success.

After the transcriber completes, append a `tool_use` entry to the interview log recording the invocation. (This entry is captured for completeness; it won't appear in this session's transcript since the transcriber has already run.)

---

### Step 7b — Present Results

1. Present the completed document(s) to the user with links to the job folder. Link to all produced formats (docx, html, pdf, md). If PDF conversion failed, suggest manual conversion (MS Word Export, LibreOffice, Pandoc). Mention: "A transcript of this session has been saved to `transcript.md` in the job folder."
2. Offer: "Would you like to prepare another document?"
3. **Privilege and version-control reminder:** Tell the user: "The job folder contains `interview_log.json` and `transcript.md` which may include privileged client information. Do not commit the `output/` folder to a shared repository or version-control system accessible to unauthorised parties."

If the user prepares another document, Phase 3d creates a fresh interview log. Each `interview_log.json` and `transcript.md` is scoped to exactly one document.

---

## Important Notes

- **Never modify template files** — only read them.
- **Rendering engines**: docx uses `docxtpl` (not raw python-docx); HTML uses `jinja2` + `weasyprint` for PDF; markdown uses `jinja2` + `markdown` + `weasyprint` (PDF is soft-fail — always deliver `.md`).
- **PDF for docx** requires `docx2pdf` (MS Word or LibreOffice). If unavailable, deliver `.docx` only with a warning.
- **The manifest is a cache** — regenerate if the template file is newer or `schema_version` is missing/< 2.
- **Boolean coercion** — ensure boolean variables are Python `True`/`False`, not strings like `"yes"` or `"no"`.
- You assist with legal workflows but do not provide legal advice. Remind users to seek professional review.

## Plugin Context Notes

When running as a Claude Code plugin (i.e., `CLAUDE_PLUGIN_ROOT` is set), sub-skills are namespaced. If bare skill names (`coquill-analyzer`, `coquill-renderer`, `coquill-transcriber`) do not resolve, use the namespaced forms: `coquill:coquill-analyzer`, `coquill:coquill-renderer`, and `coquill:coquill-transcriber`.
