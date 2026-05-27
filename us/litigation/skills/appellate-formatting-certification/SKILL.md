---
name: appellate-formatting-certification
title: Appellate TOC/TOA and Compliance Certificate
description: Generates appellate-brief TOC, TOA, and Certificate of Compliance with defensible word-count methodology. Triggers on TOC/TOA rebuilds, certificate of compliance drafting, FRAP 32(g) compliance, word-count certification, or final brief formatting before filing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/appellate-formatting-certification
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, brief, drafting]
---

# Appellate TOC/TOA and Compliance Certificate

Produce filing-ready Table of Contents, Table of Authorities, and Certificate of Compliance tied to the final paginated brief and governing rules.

## Quick Start

Gather before drafting:

| Input | Required | If missing |
|---|---|---|
| Court and brief type | Yes | Ask before drafting |
| Final paginated PDF | Preferred | Use `[__]` placeholders; label DRAFT |
| Word processor word count | Yes | Insert placeholder; require attorney count |
| Excluded sections list | Yes | Require rule text; never assume |
| Local rules / standing orders | Yes | Request rule text or cite with [VERIFY] |

## Rule Anchors

Verify all cites against current rules before drafting.

| Forum | Core anchors |
|---|---|
| Federal courts of appeals | FRAP 28, 32(a)(5)–(7), 32(f), 32(g) [VERIFY] |
| State appellate courts | State rule text only [VERIFY] |
| U.S. Supreme Court | Sup. Ct. R. 33, 34, 33.1(g), 33.2 [VERIFY] |

## Core Workflow

1. **Confirm rules** — Identify governing rules and any court order modifying limits.
2. **Build heading map** — Extract headings from brief; preserve exact text, capitalization, numbering.
3. **Generate TOC** — Map headings to final page numbers. If unpaginated, use `[__]` and label `DRAFT - PAGE NUMBERS TBD`. Include all forum-required sections (certificates, required statements). Use Roman/Arabic numbering only if the forum does so.
4. **Generate TOA** — Extract all citations from the brief (including footnotes) and sort by category:
   - **Cases** — alphabetical by first party name
   - **Constitutional Provisions** — jurisdiction then provision
   - **Statutes** — code then section
   - **Rules** — rule number
   - **Other Authorities** — alphabetical by author/title
5. **Compute word count** — Document total words, excluded sections (with rule cite), excluded words, and net count.
6. **Draft certificate** — Tie language to confirmed rules. Template:

> Pursuant to [Rule cite] [VERIFY], I certify that this brief complies with the type-volume limitation of [Rule cite] [VERIFY] because it contains [____] words, excluding the parts exempted by [Rule cite] [VERIFY].
>
> This brief complies with the typeface and type-style requirements of [Rule cite] [VERIFY] because it has been prepared in a proportionally spaced typeface using [Software] in [Font Size]-point [Font Name].

7. **Final QC** — Run the checklist below against the final PDF.

## Final QC Checklist

- [ ] TOC headings match brief verbatim
- [ ] TOC page numbers match final PDF
- [ ] TOA entries match brief citations; page references correct
- [ ] Word count matches source document used for PDF
- [ ] Certificate cites correct rule, states actual method and software
- [ ] If within 2% of limit, flag for trimming or motion for leave

## Pitfalls and Checks

- **Never fabricate** page numbers, word counts, or citations.
- **Never certify** compliance without a confirmed count and formatting specs.
- **TOA integrity** — Do not add or fix citations absent from the brief. Flag incomplete citations for attorney review. Avoid "passim" unless forum permits.
- **"Rule 37 certificate" requests** — Ask for the exact order or rule basis; FRAP 37 is substantive amicus interest relief, not a formatting certificate [VERIFY].
- **State / Supreme Court filings** — Require exact rule text or insert [VERIFY] placeholders.
- **Attorney review required** — All counts, citations, and certificates must be independently verified before filing.
- **Confidentiality** — Exclude sealed or sensitive data unless explicitly authorized.
