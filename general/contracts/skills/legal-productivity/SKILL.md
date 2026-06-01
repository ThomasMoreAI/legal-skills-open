---
name: legal-productivity
title: Legal Productivity
description: 'Legal productivity workflows for Copilot CLI: contract review, NDA triage, redline-risk, xref, evidence packs, response drafting, briefings, vendor checks, and style learning over existing legal documents.'
author: dvelton
author_url: https://github.com/dvelton/copilot-legal-productivity-pack/tree/main/skills/legal-productivity
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Legal Productivity

Use this skill when a legal team wants structured legal workflows in Copilot without moving its documents into GitHub. The user's sources may be local Word files, PDFs, exported emails, SharePoint/OneDrive-synced folders, CLM exports, URLs, or matter folders.

This skill is assistive. It does not provide legal advice. Outputs must be reviewed by qualified counsel before use.

## Activation

When the user asks for contract review, NDA triage, redline analysis, legal response drafting, legal briefing, vendor context, xref navigation, or source-backed legal analysis, say that the Legal Productivity skill is active and identify the workflow you will run.

Do not assume the customer's documents live in GitHub. Use local files, folders, URLs, and connected document systems the user provides.

## Tool

The CLI is:

```bash
copilot-legal
```

If it is not installed, from this repository run:

```bash
npm install
npm link
copilot-legal setup-check
```

For global install from GitHub:

```bash
npm install -g github:dvelton/copilot-legal-productivity-pack
```

## Workflows

### Contract review

Use when the user asks to review an MSA, DPA, order form, terms, vendor agreement, customer agreement, or similar contract.

```bash
copilot-legal review-contract "<source>" --we-are "<party>" --playbook "<playbook.yml>"
```

If no playbook is supplied, use the default commercial playbook. Ask which party the user represents if the answer is not clear.

Return:

- overall posture
- red/yellow/green issues
- priority issues
- source excerpts
- fallback positions
- items requiring counsel review

### NDA triage

Use when the user asks whether an NDA is standard or needs review.

```bash
copilot-legal triage-nda "<source>"
```

Return green, yellow, or red, with the specific provisions that drive the classification.

### Redline risk

Use when the user provides a Word document with tracked changes.

```bash
copilot-legal redline-risk "<source.docx>" --we-are "<party>" --format html
```

Ask which party the user represents before running this workflow. Directional assessment depends on party perspective.

### Xref viewer

Use when the user wants to navigate a long agreement, resolve defined terms, or check references.

```bash
copilot-legal xref "<source>"
```

Return the generated HTML file path and a short document-health summary.

### Evidence pack

Use when the user wants source-backed output.

```bash
copilot-legal evidence-pack "<source>" --we-are "<party>"
```

This package produces an HTML evidence report. If the separate Eyeball skill is installed, prefer Eyeball for Word documents with rendered source screenshots.

### Response drafting

Use when the user asks to answer a customer, business stakeholder, security questionnaire, procurement question, or internal legal request.

```bash
copilot-legal respond "<question or question-file>" --sources "<approved-source-folder>" "<policy-folder>"
```

Do not send messages externally. Draft only, cite source basis, and flag counsel-review triggers.

### Briefing

Use when the user asks for a meeting brief, matter brief, topic brief, or summary of a folder.

```bash
copilot-legal brief "<matter-folder>" --topic "<topic>"
```

### Vendor check

Use when the user asks what is known about a vendor.

```bash
copilot-legal vendor-check "<vendor name>" --sources "<matter-folder>" "<approved-responses-folder>"
```

### Style learning

Use when the user provides an AI draft and attorney-edited final version.

```bash
copilot-legal learn-style "<original-draft>" "<final-version>" --profile "~/Copilot Legal/style/style-profile.md"
```

Read the style profile before drafting future legal work product for that user or team.

## Default workspace

Initialize a local workspace:

```bash
copilot-legal init
```

This creates:

```text
~/Copilot Legal/
  playbooks/
  templates/
  approved-responses/
  policies/
  matters/
  outputs/
  style/
```

The workspace is a convenience. The user can point commands at any file or folder.

## Guardrails

- Do not claim final legal conclusions without human review.
- Do not send emails, messages, calendar invites, or external communications without explicit approval.
- Do not invent source support. If the source does not support a statement, say so.
- Preserve privilege and confidentiality. Do not mix unrelated matters unless the user selects those sources.
- If the document is scanned or text extraction fails, ask for a text-layer PDF or Word version.
