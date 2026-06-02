---
name: document-summarization
title: Document Summarization Skill
description: Summarize an uploaded document (DOCX, PDF, contract, filing, memo, opinion, etc.) by reading it structurally rather than linearly. Use whenever the user asks to summarize, recap, brief, give the gist of, pull key terms from, or "tell me what this is about" for an attached document. NOT for summarizing a chat conversation or vector-search results — only for a binary the user uploaded.
author: firelex
author_url: https://github.com/firelex/suzielaw/tree/main/apps/suzielaw/skills/document-summarization
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Document Summarization Skill

Lawyers don't read contracts cover-to-cover when they need a brief — they scan the table of contents, dive into the clauses that matter, and check defined terms when something looks unusual. This skill prescribes the same workflow using the document tools you already have.

## When to use

Trigger when the user has attached a binary (DOCX, PDF, etc.) AND is asking for one of:
- A summary, brief, recap, executive summary, abstract
- Key terms, key points, key dates, parties, obligations
- "What is this about?", "what does this say?", "give me the gist"
- A risk summary or red-flag review

If multiple binaries are attached, treat each one separately unless the user explicitly asks to compare/synthesize.

If no binary is attached but a document is already in the chat (paste, vector-search hit), skip §1 and start at §2 with whatever doc_id is in scope.

## Workflow

### 1. Convert the binary to a navigable document

For each attached binary the user wants summarized:

```
convert_to_markdown(file_id=<id from [Attachments]>)
```

Returns a `doc_id`. If conversion fails (scanned PDF with no extractable text, corrupt file), tell the user plainly — don't fabricate a summary from the filename.

### 2. Get the structure

```
get_outline(doc_id=<doc_id>)
```

Read the outline before reading any section. The outline tells you:
- **Document type** (contract, memo, filing, opinion, policy) — infer from headings
- **Length and depth** — a 4-section memo and a 60-section credit agreement need different treatment
- **Where the load-bearing content is** — definitions, recitals, operative covenants, schedules

### 3. Decide what to read

Pick sections to read in full based on the outline. Heuristics by document type:

- **Contracts / agreements** — definitions, term/termination, payment, IP, liability/indemnity, governing law, any section with an unusual or non-boilerplate heading. Skip standard boilerplate (notices, severability, counterparts) on the first pass.
- **Memos / opinions** — issue, short answer/conclusion, analysis. Read those three; skip lengthy facts unless the user asked about facts.
- **Filings (briefs, motions)** — introduction, statement of facts, argument headings, conclusion. Read the argument headings to see what's being argued; read the conclusion.
- **Policies / regulations** — scope, definitions, the operative requirements, penalties/enforcement.
- **Unknown structure** — read the first section, the last section, and any section whose heading is unusually specific.

For each chosen section:

```
read_section(doc_id=<doc_id>, path=<heading path from outline>)
```

Reference the heading path verbatim from the outline (e.g. `§3.2`, `Article IV`, `Section 7(a)`). Don't paraphrase paths.

### 4. Targeted lookups (optional)

If during reading you find a defined term, cross-reference, or unusual phrase you need to verify:

```
search_document(doc_id=<doc_id>, query=<term>)
```

Use this for: defined terms used before they're defined, references like "see Section X", numbers/dates that need confirming, names of parties, governing-law clauses hidden in catch-all sections.

Don't use `search_document` as a replacement for `get_outline` — it's a follow-up tool, not a discovery tool.

### 5. Write the summary

Choose the categories and structure that fit *this* document. A purchase agreement, a motion to dismiss, a regulatory rule, and an internal memo all warrant different breakdowns — pick what a partner reviewing the document would want to see at a glance, and let unrelated documents look unrelated.

Register: **legal and formal**. Write in the voice of a practicing lawyer briefing a colleague. No casual phrasing, no first-person editorializing, no exclamation points. Defined terms get capitalized as they appear in the document. Headings use the document's own terminology where it has any (e.g. "Indemnification" not "who pays for problems").

Always cite the heading path (`§2.1`, `Article IV.B`) inline so the user can verify. Never invent a clause. If you didn't read a section, don't summarize it — say "I didn't open §X; let me know if you want me to."

### 6. Length

- **Default:** ~10–20 lines for a typical contract or memo. Long enough to be useful, short enough that the user reads it.
- **One-pager request:** longer prose, more headings, fuller treatment of the substantive provisions.
- **One-line request ("just the gist"):** 1–2 sentences, no headings.

### 7. If the user asks for a DOCX

Switch to the drafting tools — `create_document`, `set_outline`, `write_section`, `export_to_docx` — using the summary content you just produced. This is the standard drafting flow; nothing summarization-specific about the export step.

## Edge cases

- **Multiple files** — summarize each separately, then offer a comparison if relevant. Don't merge unprompted.
- **Very long documents (>50 sections)** — read the outline, pick ~10–15 priority sections, name what you're skipping. Quality > coverage.
- **Very short documents (<5 sections)** — `read_section` everything; `get_outline` is still useful for headings to cite.
- **Image-only PDF / scanned doc** — `convert_to_markdown` will return little or no text. Tell the user the file appears to be scanned and you can't read it; don't bluff a summary.
- **Document already in scope** — if the user is asking a follow-up about a doc you've already navigated, reuse the existing `doc_id` and skip §1.
- **User asks "what changed?" between two versions** — out of scope for this skill; it's a diff task, not a summary task. Read both outlines, but flag that you're describing differences rather than summarizing.

## What this skill does NOT do

- Doesn't replace `vector_search` for knowledge-base questions.
- Doesn't apply to summarizing a chat conversation.
- Doesn't draft new content — for that, use drafting tools directly.
