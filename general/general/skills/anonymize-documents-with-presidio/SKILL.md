---
name: anonymize-documents-with-presidio
title: Anonymize Documents
description: anonymize uploaded pdf, powerpoint, and word files with presidio. use when the user provides an uploaded pdf, ppt/pptx, doc/docx, or wants a fully redacted version that removes names, emails, phone numbers, addresses, ids, and company/project names. only use on files uploaded in the current conversation.
author: schneidermichael
author_url: https://github.com/schneidermichael/anonymize-documents-with-presidio
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Anonymize Documents

## Overview

Use this skill to turn an uploaded PDF, PowerPoint, or Word file into a fully redacted version. Detect names, emails, phone numbers, addresses, IDs, and company or project names with Presidio, then replace matched content so the resulting file no longer contains the original sensitive text.

## Workflow

1. Confirm the input is an uploaded file from the current conversation.
2. Identify the file type: PDF, PowerPoint, or Word.
3. Run Presidio detection against all extractable text.
4. Fully redact every match for the approved sensitive entities.
5. Rebuild the document in the same format when possible.
6. Verify that the output contains no original sensitive text in visible content.

## Redaction rules

Use these entity groups for redaction:
- names
- emails
- phone numbers
- addresses
- ids
- company names
- project names

Redact completely rather than substituting placeholders. Prefer visual removal over partial masking.

## File handling guidance

### PDF
- Redact selectable text using Presidio findings.
- Remove the original text from the page content, not just from a copied text layer.
- Keep page count and page order unless the file must be rebuilt to achieve full redaction.
- Verify page text after redaction.

### Word
- Redact body text, tables, headers, footers, footnotes, endnotes, and text inside shapes when accessible.
- Preserve document structure and formatting as much as possible.
- Recheck all text runs after replacement.

### PowerPoint
- Redact slide text, speaker notes when present, and other accessible text fields.
- Preserve the slide order and layout as much as possible.
- Check titles, subtitles, labels, bullets, and table text separately.

## Presidio usage

Use Presidio as the detection layer and redaction engine for text entities. The analyzer finds sensitive spans and the anonymizer applies the redaction operator. Default to a full redaction operator for every target entity.

When needed, extend Presidio with project-specific recognizers for company and project names so they are also removed.

## Quality checks

Before returning the output:
- ensure no original PII remains in visible text
- ensure company and project names are also removed
- ensure the output file opens normally
- ensure the redaction did not expose the sensitive text in comments, notes, metadata, or hidden text when those are accessible

## Limits

Only process files uploaded in the current conversation. Do not use connector files or external sources for this skill.
