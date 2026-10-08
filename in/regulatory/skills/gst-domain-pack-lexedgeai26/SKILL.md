---
name: gst-domain-pack-lexedgeai26
title: GST Domain Pack
description: Indian GST domain knowledge pack for classification, limitation awareness, drafting, compliance checks, and citation discipline across GST notices, demands, appeals, and returns.
author: Lexedgeai26
author_url: https://github.com/Lexedgeai26/legal-hermes/tree/main/skills/legal-india/gst-domain-pack
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: in
practice: regulatory
language: en
---

# GST Domain Pack

## When to Use

Use this whenever a matter involves Indian GST: scrutiny notices, pre-SCN intimations, show-cause notices, demand orders, appeals, returns, ITC disputes, e-invoicing, e-way bills, penalty, interest, or compliance review.

This is a knowledge pack for other legal skills. Pair it with `intake-triage`, `gst-notice-reply`, `legal-research`, `citation-check`, `compliance-check`, `risk-analysis`, and drafting/review skills.

## Procedure

1. Identify the GST document or workflow type. Common forms include:
   - ASMT-10: scrutiny notice.
   - DRC-01A: pre-SCN intimation.
   - DRC-01: show-cause notice.
   - DRC-06: reply to SCN.
   - DRC-07: summary of order.
   - APL-01: appeal to Appellate Authority.
2. Identify the statutory track and issue family:
   - CGST/SGST/IGST Acts, 2017 and CGST Rules, 2017.
   - Section 73: non-fraud demand track for periods up to FY 2023-24.
   - Section 74: fraud, suppression, or wilful-misstatement demand track for periods up to FY 2023-24.
   - Section 74A: merged demand regime from FY 2024-25, subject to advocate confirmation.
   - Section 50: interest.
   - Section 122: penalty.
   - Section 107: appeal to Appellate Authority.
   - Section 112: appeal to Tribunal.
3. Treat limitation as deterministic, not model-computed. Use the firm's GST rules, connected GST MCP/source, or advocate-confirmed computation for:
   - Section 73 order and SCN windows.
   - Section 74 order and SCN windows.
   - Section 74A order window from SCN and any extension.
   - Section 107 appeal window and condonable delay.
4. For GST replies, structure work as: notice recital, issue-wise demand heads, facts and annexures, limitation/jurisdiction objections, merits response, authorities, relief sought, and filing checklist.
5. For GST appeals, structure work as: facts, grounds of appeal, limitation/condonation position, issue-wise arguments, pre-deposit status, prayer, and annexures.
6. For compliance checks, assess at least: GSTR-1, GSTR-3B, GSTR-9/9C, e-invoicing, e-way bill compliance, ITC reconciliation against GSTR-2B/books, payment, interest, and penalty exposure.
7. Cite only authorities returned by a trusted GST source or supplied by the advocate. If no trusted source is connected, produce a non-citation draft and mark every authority gap.

## Pitfalls

- Do not guess limitation dates from memory. Surface the applicable track and ask for deterministic computation or advocate confirmation.
- Do not cite judgments, circulars, notifications, or statutory extracts unless they are provided or retrieved from a trusted source.
- Do not file on the GST portal, upload documents, send emails, or dispatch notices from this skill.
- Do not assume Section 74A applies without checking the financial year and effective regime.
- Mark unverified factual inputs as `[CONFIRM: ...]`.

## Verification

- GST form/document type and statutory track are identified.
- The limitation issue is either computed by a trusted deterministic source or explicitly marked for confirmation.
- Every cited authority traces to a provided or retrieved source.
- Output remains a draft/checklist for advocate review; nothing is filed, served, uploaded, or sent.
