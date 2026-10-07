# Redline Emailer — Intake Questions

Minimal intake. Most information comes from the document itself or
is obvious from context. Ask only what you cannot determine.
Target: 60 seconds or less.

---

## Q1: Input Mode (auto-detect)

Do NOT ask this question — determine it from what the user provides:

| User provides | Mode |
|--------------|------|
| A single `.docx` file | Check for tracked changes. If found → **Mode A**. If none → ask: "This document doesn't have tracked changes. Can you describe what was changed, or do you have a redlined PDF?" |
| A `.pdf` file | **Mode B** (redlined PDF) |
| No file, describes changes verbally | **Mode C** (verbal description) |
| Ambiguous (multiple files, unclear) | Ask: "Which file has the redlines — the .docx or the PDF?" |

→ `input_mode`: "docx_tracked" | "pdf_redline" | "verbal"

---

## Q2: Recipient Type (always ask unless stated)

> "Is this email going to your client or to opposing counsel?"

- **Own client** → plain-English summary mode
- **Opposing counsel** → professional legal cover mode

→ `recipient`: "client" | "counsel"

If the attorney already stated the recipient (e.g., "write this up for the client"),
do NOT re-ask. Confirm and proceed.

---

## Q3: Contract Identity (extract from doc if possible)

If a document was provided, attempt to extract:
- Contract title (from first heading, header, or title page)
- Party names (scan for defined terms: "Company", "Client", "Licensor", "Provider", etc.)
- Effective date if visible

If not extractable or no document provided:

> "What contract are these changes to? (title and parties)"

→ `contract_title`, `parties`

---

## Q4: Special Instructions (optional — skip if straightforward)

Only ask if the attorney's request suggests complexity or nuance. Skip for
simple "write the redline email" requests.

> "Anything you want me to emphasize, downplay, or flag in the email?"

Examples of when to ask:
- Attorney mentions a contentious issue
- Multiple rounds of negotiation referenced
- Specific items the attorney wants called out

→ `special_instructions`: string | null
