---
name: documents
title: Documents Skill
description: Create and convert DOCX documents — contracts, policies, memoranda, letters, term sheets, opinions, press releases, and more. Also converts markdown ↔ DOCX. Use this skill for any Word-document task. For presentations (PPTX) use the presentations skill; for spreadsheets (XLSX) use the spreadsheets skill.
author: firelex
author_url: https://github.com/firelex/open_teamsuzie/tree/main/packages/skills/templates/documents
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Documents Skill

Everything Word-document-related lives behind one base URL. Three operations: **Draft**, **Markdown → DOCX**, **DOCX → Markdown**.

## Which operation should I use?

You have two ways to produce a new Word document:

1. **Draft it yourself in markdown, then use §2 Markdown → DOCX to convert.** Good for short or simple documents where you're confident in the structure yourself — quick notes, a letter, a one-page summary, an internal update.

2. **Use §1 Draft.** This runs the request through a structured drafting pipeline that's particularly well-suited for **legal and regulatory documents and other complex documents spanning many pages** — contracts, policies, memoranda, engagement letters, term sheets, opinions, press releases, and similar. It produces a properly-templated DOCX in one call.

   **When you use §1 Draft, include an appropriately detailed description in the `instructions` field** — the drafting pipeline works best with rich context (parties, dates, key terms, tone, length, etc.) rather than a one-line prompt.

Use §3 DOCX → Markdown to read or summarize an existing DOCX the user hands you.

## Operation types

- **Async** (Draft) — you get a `job_id` immediately; a webhook fires on completion (30–120s).
- **Sync** (Markdown → DOCX, DOCX → Markdown) — server returns the final response within a single request/response.

Both kinds share the **same download flow**: server returns `{ job_id, download_url, filename }`, you fetch the URL, save to workspace, attach the file. Never paste document contents directly into chat — always download to the workspace and attach as a file.

## Base URL

```
{{DOCX_AGENT_URL}}
```

## Authentication

All requests require this header:
```
X-API-Key: {{AGENT_API_KEY}}
```

---

## 1. Draft a Document (async)

Draft a new DOCX from natural-language instructions. Produces contracts, policies, memoranda, engagement letters, term sheets, opinions, press releases, and similar.

**Include a detailed `instructions` field for optimal results.** A rich prompt (parties, dates, key terms, tone, length, intended audience) produces a much better document than a one-line ask. If you only have a short prompt from the user, either ask a follow-up question to enrich it, or use §2 Markdown → DOCX for a simpler path.

**Method:** POST
**Endpoint:** `/api/documents/draft`
**Content-Type:** `application/json`

```json
{
  "instructions": "Draft a mutual non-disclosure agreement between Company A (disclosing party) and Company B (receiving party). Two-year term, standard carve-outs.",
  "document_type": "agreement"
}
```

| Field           | Required | Description                                                                                 |
| --------------- | -------- | ------------------------------------------------------------------------------------------- |
| `instructions`  | Yes      | Detailed natural-language description. Richer context produces better output.               |
| `document_type` | No       | Optional hint: `agreement`, `engagement_letter`, `memorandum`, `opinion`, `policy`, `press_release`, `term_sheet`, `other`. |

**Response (202 Accepted):**
```json
{
  "job_id": "a1b2c3d4-...",
  "status": "processing"
}
```

**IMPORTANT:** Do NOT wait for the response before replying to the user. Tell them you've submitted the request (quote the job id) and that you'll notify them when it's ready. A webhook system event arrives when the document is done.

Write JSON payloads to a file and pass them to curl with `--data-binary @file` to avoid escaping issues.

---

## 2. Convert Markdown → DOCX (sync)

Convert markdown text to a DOCX file. Useful when you have generated content as markdown and want to deliver it as a Word document.

**Method:** POST
**Endpoint:** `/api/documents/markdown-to-docx`
**Content-Type:** `application/json`

```json
{
  "markdown": "# Heading\n\nSome body text...",
  "filename": "notes"
}
```

Response returns `{ job_id, status: "completed", filename, download_url }`. Proceed directly to the download flow (§4).

---

## 3. Convert DOCX → Markdown (sync)

Convert a DOCX file to markdown text. Useful when the user wants to read or edit a Word document's contents as plain text.

**Method:** POST
**Endpoint:** `/api/documents/docx-to-markdown`
**Content-Type:** `multipart/form-data`

```bash
curl -X POST "{{DOCX_AGENT_URL}}/api/documents/docx-to-markdown" \
  -H "X-API-Key: {{AGENT_API_KEY}}" \
  -F "file=@/path/to/contract.docx"
```

Response returns `{ job_id, status: "completed", filename, download_url }`. Proceed to §4.

---

## 4. Download and deliver

Same flow for every operation above.

**Method:** GET
**Endpoint:** `/api/documents/:id/download`

### Agent procedure

1. **Parse** the `download_url` from the response (sync) or the webhook text (async).
2. **Save** the file into your workspace:
   ```bash
   mkdir -p /tmp/workspace/{{AGENT_SLUG}}
   curl -o /tmp/workspace/{{AGENT_SLUG}}/document.docx <download_url>
   ```
3. **Send** the file to the user via the message tool using `filePath` — never paste contents into chat, never send the download URL as text.

## Context variables

- `{{DOCX_AGENT_URL}}` — base URL of the DOCX service
- `{{AGENT_API_KEY}}` — API key this agent uses to authenticate
- `{{AGENT_SLUG}}` — this agent's slug, for workspace path segmentation
