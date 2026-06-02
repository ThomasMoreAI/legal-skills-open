---
name: legal-matter-tracker
title: Legal Matter Tracker
description: 'Scan local workspace folders by client or case name and assemble a chronological timeline of events with key facts. No external integrations required. Triggers: ''matter tracker'', ''case timeline'', ''track [client]'', ''timeline for [case]'', ''client history'', ''matter report'', ''summarize [client] matter'', ''трекер дела'', ''хронология дела'', ''история клиента'', ''что было по [клиент]'', ''отчёт по делу'', ''хронология событий по [клиент/дело]''.'
author: KirKruglov
author_url: https://github.com/KirKruglov/claude-skills-kit/tree/main/skills/legal-matter-tracker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal Matter Tracker

This skill scans a local Cowork workspace for files related to a specified client or legal matter, extracts dated events and key facts, and assembles a structured chronological timeline report — entirely from local files, with no external integrations required.

**Input:** Client or case name (required). Optional: folder path to narrow scan scope.

**Output:** Structured markdown timeline report (inline). Optionally saved to `output/matter-timeline-[client]-YYYY-MM-DD.md` on request.

---

## Language Detection

Detect the user's language from their message:
- If Russian (or contains Cyrillic): respond in Russian
- If English (or other Latin-script language): respond in English
- If ambiguous: default to English

---

## Instructions

### Step 1: Parse Input

1. Extract the client or case name from the user's message.
   - Accepted forms: `"case timeline for Acme Corp"`, `"track Smith matter"`, `"хронология по делу Иванов"`, `"что было по клиенту Ромашка"`.
   - The name may be a company, person, project code, or case identifier.

2. If no name is provided, return:
   - EN: "Please provide a client or case name. Example: 'Case timeline for Acme Corp'"
   - RU: "Укажите имя клиента или название дела. Пример: «хронология по делу Ромашка»"
   Stop — do not generate output.

3. If the user provided a folder path to narrow the scan scope, note it. Otherwise scan the full workspace.

---

### Step 2: Scan Workspace

1. Search for files that match the client/case name using these criteria:
   - **Filename match:** filename contains any word from the name (case-insensitive).
   - **Content match:** file contains the name in a heading (`#`, `##`, `**Name**`) or first 10 lines.
   - Accepted file types: `.md`, `.txt`.
   - Search folders: workspace root + `notes/`, `clients/`, `cases/`, `input/`, `output/`, `context/`.

2. If a folder path was provided: scan only that folder (recursive).

3. Count total files scanned and matching files found.

4. If no matching files found, return:
   - EN: "No files found matching '[name]'. Try a broader term or check that the relevant files are in your workspace."
   - RU: "Файлов по запросу «[name]» не найдено. Попробуйте более широкий запрос или проверьте, что нужные файлы есть в воркспейсе."
   Stop — do not generate output.

---

### Step 3: Extract Events

For each matched file:

1. Extract **dated events**: lines or paragraphs that contain:
   - An explicit date (ISO: `2025-01-15`, written: `January 15, 2025`, `15 января 2025`, `15.01.2025`, `01/15/2025`)
   - A fact, decision, event, action item, or key information associated with that date.

2. Extract **key entities** (if detectable):
   - Party names (people, organisations)
   - Amounts or values (monetary, percentages, quantities)
   - Status indicators (`open`, `closed`, `pending`, `active`, `закрыто`, `открыто`)
   - Action items or open questions

3. For lines with no associated date: collect as **undated entries** — do not discard.

4. If a file yields zero events (file is empty or contains only unstructured text with no extractable facts), note it and skip.

5. If all matched files yield zero events, return:
   - EN: "Found [N] file(s) matching '[name]' but could not extract events. Files may be empty or contain only unstructured text."
   - RU: "Найдено [N] файл(ов) по запросу «[name]», но извлечь события не удалось. Файлы могут быть пустыми или содержать только неструктурированный текст."
   Stop.

---

### Step 4: Assemble Timeline

1. Sort all dated events **chronologically, ascending** (oldest first).

2. Group undated entries separately at the end — ordered by source file.

3. Build the timeline table:
   - Column 1: **Date** (formatted as `YYYY-MM-DD` for ISO dates; preserve written format for ambiguous dates)
   - Column 2: **Event** (concise description, max 120 chars; truncate with `…` if needed)
   - Column 3: **Source** (filename with relative path, in backticks)

4. Build the **Key Facts Summary** using extracted entities:
   - Parties (if found)
   - Matter status (open/closed/unknown)
   - Open items (action items or questions found in files)

5. Build the **Sources** list: each matched file with count of extracted events.

6. Assemble the full report (see Output Format below).

---

### Step 5: Output

1. Display the complete timeline report inline in chat.

2. If the user says "save" or "save to file" (or RU: "сохрани", "сохрани в файл"):
   - Write to `output/matter-timeline-[client-slug]-YYYY-MM-DD.md` where `client-slug` is the client name lowercased with spaces replaced by hyphens.
   - Confirm: "Saved to `output/matter-timeline-[client-slug]-YYYY-MM-DD.md`"

---

## Edge Cases

- **Multiple files match:** Include all matched files; label every event with its source filename. Do not deduplicate events.
- **No explicit dates in matched files:** Include all entries in the Undated Entries section. Add a note at the top: "No dated events found — all entries are undated."
- **User provides folder path to narrow scan:** Scan only that folder (recursive); note scan scope in report header.
- **Conflicting facts across files** (e.g., different amounts for the same event): List both versions in the event table with their respective source references. Do not resolve silently; add a flag `⚠ Conflict` in the Event column.
- **Very long event descriptions (>120 chars):** Truncate with `…` in the table; include the full text as a footnote below the table.
- **Date formats in Russian** (e.g., `15 января 2025`): Parse and normalise to `YYYY-MM-DD` for chronological sorting; display original format in the table.

---

## Negative Cases

- **No client/case name provided:** Return usage message (EN/RU). Stop. No partial output.
- **No matching files found:** Return "No files found" message with search guidance. Stop.
- **Files found but no extractable events:** Return informative message. Stop. Do not generate an empty timeline.

---

## Output Format

```
# Matter Timeline — [Client/Case Name]
**Generated:** YYYY-MM-DD
**Files scanned:** N  |  **Matching files:** M  |  **Events extracted:** K
**Scan scope:** [workspace root / specified folder path]

---

## Chronological Timeline

| Date | Event | Source |
|------|-------|--------|
| 2025-01-15 | Initial consultation. Client presented IP dispute claim. | `notes/acme-notes.md` |
| 2025-02-03 | Contract signed. Engagement fee: $12,000. | `contracts/acme-contract.md` |
| 2025-03-10 | Discovery phase completed. 3 key documents identified. | `notes/acme-notes.md` |

---

## Undated Entries
*(entries without extractable dates — ordered by source file)*

| Entry | Source |
|-------|--------|
| Opposing counsel: Smith & Partners LLP | `notes/acme-notes.md` |

---

## Key Facts Summary
- **Parties:** Acme Corp (client), Smith & Partners LLP (opposing counsel)
- **Matter status:** Open (last activity: 2025-03-10)
- **Open items:**
  - Discovery documents pending review
  - Fee invoice not yet confirmed

---

## Sources
- `notes/acme-notes.md` — 3 events extracted
- `contracts/acme-contract.md` — 1 event extracted
```
