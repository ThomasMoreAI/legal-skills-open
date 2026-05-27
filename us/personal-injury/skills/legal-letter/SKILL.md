---
name: legal-letter
title: Legal Letter Drafting
description: Drafts professional legal letters for personal injury litigation including settlement demands, cease-and-desist, notice letters, and response correspondence. Tailors tone by recipient type. Use when drafting demand letters, pre-suit correspondence, insurance claim letters, cease-and-desist notices, or litigation response letters.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/legal-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
---

# Legal Letter Drafting

Drafts litigation correspondence that advances settlement positioning, preserves rights, and builds a clean evidentiary record for personal injury cases.

## Quick Start

Gather before drafting:

- **Case identifiers** — case name, docket number, matter number, claim number
- **Recipient** — name, title, firm/organization, delivery method
- **Strategy** — purpose, desired outcome, deadlines
- **Supporting docs** — prior correspondence, medical records, incident reports
- **Damages** (demand letters) — medical bills, lost wages, future costs

## Header Template

```
[DATE]
Via [Delivery Method]: [address]

[RECIPIENT NAME]
[TITLE]
[FIRM/ORGANIZATION]
[ADDRESS]
[CITY, STATE ZIP]

Re: [Case Name]
    [Court Name] Case No. [Number] (if filed)
    Our Client: [Client Name]
    Matter No.: [Internal number]
    Claim No.: [If applicable]
    [Brief subject description]

Dear [RECIPIENT NAME],
```

## Body Structure

Draft in this order:

1. **Opening** — Identify client, state purpose, reference prior correspondence or deadlines
2. **Factual foundation** — Chronological key facts with dates, amounts, parties; cite supporting docs
3. **Legal basis** — Cite statutes, regulations, case law; connect to client's position
4. **Damages** (if applicable) — Itemized monetary damages with calculations, non-economic damages, ongoing costs
5. **Demand & deadline** — Specific demand or action requested, response deadline with consequences, payment instructions
6. **Closing** — Invite communication, list enclosures, provide contact info

When litigation is anticipated, include preservation language:

> Please preserve all documents, electronically stored information, and physical evidence related to this matter as litigation may be reasonably anticipated.

## Tone by Recipient

| Recipient | Tone | Strategy |
|-----------|------|----------|
| Opposing counsel | Professional, firm, respectful | Position client favorably; negotiate or preserve rights |
| Insurance company | Business-like, documentation-focused | Present clear liability and damages for coverage decision |

## Letter-Type Variations

| Type | Key Requirements |
|------|-----------------|
| **Settlement demand** | Lead with strongest liability facts; itemize damages; set firm deadline; leave negotiation room |
| **Cease and desist** | Specify prohibited conduct; cite legal basis; state consequences; document prior violations |
| **Statutory notice** | Meet statutory notice requirements exactly; use required delivery method; preserve proof of delivery |
| **Response letter** | Address opposing points selectively; correct facts diplomatically; preserve position for future proceedings |

## Signature Block

```
Sincerely,

[Signature]
[Typed Name]

cc: [Client name]
Enclosures: [List attachments]
```

## Checks

- Extract all available information from provided files before requesting user input; use placeholders for missing details
- Verify all names, dates, case numbers, and amounts against the file
- Base demands on documented losses; include interest and costs where appropriate
- Set realistic deadlines — allow reasonable response time while creating urgency
- Never disclose privileged or confidential information
- Include all referenced attachments in enclosures list
- Maintain firm but professional tone — no overtly aggressive language
- Flag in output that client must review and approve before sending
- FRE 408 considerations apply to all settlement communications
- For Illinois product liability: 735 ILCS 5/2-621 governs strict liability for defective products [VERIFY current statute]
