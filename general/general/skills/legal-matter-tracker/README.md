> [Версия на русском языке](README.ru.md)

# Legal Matter Tracker

Scan your workspace files by client or case name and get a complete chronological timeline of events — no integrations, no setup, just your local notes.

---

## Overview

Legal Matter Tracker scans your Cowork workspace for files related to a specific client or legal matter, extracts dated events and key facts, and assembles them into a structured chronological timeline. Give it a client name or case identifier, and it searches your notes, contracts, and documents to build a complete history — sorted by date, with source references for every entry.

No CRM, no case management software, no API keys. It works entirely with `.md` and `.txt` files you already have in your workspace. Useful before a client meeting, when preparing a status update, during due diligence, or any time you need to reconstruct the history of an engagement from scattered notes.

---

## Requirements

- Workspace files related to the client or matter (`.md` or `.txt`)
- The files should include the client/case name in the filename or in headings/first lines
- No external tools or integrations required

**Note:** The skill works best when notes are named after clients or cases (e.g., `acme-notes.md`, `smith-matter.md`). It also searches file content, so unnamed files are included if they mention the client name in headings.

---

## How to Use

1. **Invoke the skill** with a client or case name
   - Say: "Case timeline for Acme Corp" or "Matter report — Smith IP dispute"
   - The skill searches your workspace automatically

2. **Review the timeline**
   - Dated events sorted chronologically with source file references
   - Undated entries grouped at the end
   - Key facts summary: parties, status, open items

3. **Save if needed**
   - Say "save" to write the report to `output/matter-timeline-[client]-YYYY-MM-DD.md`

4. **Narrow the scope** (optional)
   - Add a folder path to limit the search: "Case timeline for Acme Corp in `clients/acme/`"

---

## Examples

### Example 1: Standard matter timeline

**Trigger:** "Case timeline for Acme Corp"

**Output:**
```
# Matter Timeline — Acme Corp
**Generated:** 2026-04-29
**Files scanned:** 12  |  **Matching files:** 3  |  **Events extracted:** 7

---

## Chronological Timeline

| Date | Event | Source |
|------|-------|--------|
| 2025-01-15 | Initial consultation. Client presented IP dispute claim. | `notes/acme-notes.md` |
| 2025-02-03 | Contract signed. Engagement fee: $12,000. | `contracts/acme-contract.md` |
| 2025-03-10 | Discovery phase completed. 3 key documents identified. | `notes/acme-notes.md` |

---

## Key Facts Summary
- **Parties:** Acme Corp (client), Smith & Partners LLP (opposing counsel)
- **Matter status:** Open (last activity: 2025-03-10)
- **Open items:** Discovery documents pending review
```

---

### Example 2: Folder-scoped search

**Trigger:** "Matter report for Project Alpha in `cases/`"

The skill scans only the `cases/` folder for files matching "Project Alpha" and returns a scoped timeline.

---

## Triggers

Use any of these phrases to trigger the skill:

| English | Russian |
|---------|---------|
| case timeline for [name] | хронология дела [название] |
| matter tracker | трекер дела |
| track [client name] | что было по клиенту [имя] |
| client history for [name] | история клиента [имя] |
| matter report | отчёт по делу |
| summarize [client] matter | хронология событий по [клиент] |

---

**Version:** 1.0.0
**Last updated:** 2026-04-29
