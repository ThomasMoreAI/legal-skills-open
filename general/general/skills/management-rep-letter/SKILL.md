---
name: management-rep-letter
title: Management Representation Letter Updater
description: Update management representation letter templates with firm and client details. Use when the user needs to prepare, update, or generate management representation letters for audit engagements.
author: WeiKhjan
author_url: https://github.com/WeiKhjan/worker-k/tree/main/skills/management-rep-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Management Representation Letter Updater

## Purpose

Update a management representation letter (.docx) template by replacing placeholder details with actual firm and client information.

## Dependencies

```bash
pip install python-docx
```

## Usage

```
/management-rep-letter [filepath]
```

The user provides:
1. **A .docx template** — uploaded or specified by path
2. **Firm details** — auditor firm name, AF number, and address
3. **Client details** — client entity name, AF number (if applicable), and address

## Workflow

### Step 1: Read the Template

Use `python-docx` to read the uploaded `.docx` file:

```python
from docx import Document
doc = Document('<filepath>')
for i, para in enumerate(doc.paragraphs):
    print(f'{i}: {para.text}')
```

### Step 2: Identify and Replace Placeholders

Common placeholders to look for and replace:

| Placeholder | Replace With |
|---|---|
| `[ON CLIENT LETTERHEAD]` | Client name and address |
| `[FIRM NAME]` | Auditor firm name (with AF number) |
| `[FIRM ADDRESS]` | Auditor firm address |
| `[Date]` or date placeholders | Keep as-is unless user specifies |
| Entity name throughout | Client entity name |
| Related party names | Updated holding/related company names if provided |

### Step 3: Replace Using Run-Level Text

Preserve formatting by replacing at the run level:

```python
for para in doc.paragraphs:
    for run in para.runs:
        run.text = run.text.replace('<old>', '<new>')
```

### Step 4: Save and Deliver

Save the updated document and provide it to the user.

## Important Notes

- **Always preserve original formatting** — use run-level replacement, not paragraph-level
- **Ask the user** if they want related party names, director names, or financial figures updated
- **Do not modify** financial figures, dates, or ISA references unless explicitly requested
- After replacement, print a summary of all changes made for user verification
