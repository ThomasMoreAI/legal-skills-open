---
name: abstract-of-judgment
title: Abstract of Judgment
description: Drafts a recordable Abstract of Judgment to create a judgment lien on a debtor's real property. Extracts party names, monetary components, and judgment details from case documents, then applies jurisdiction-specific formatting and certification requirements. Use post-judgment in commercial litigation when enforcing monetary awards, perfecting judgment liens, or preparing lien filings with the county recorder.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/abstract-of-judgment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, summary]
---

# Abstract of Judgment

Produces a recordable Abstract of Judgment that perfects a judgment lien against the debtor's real property.

## Prerequisites

1. **Judgment order** — final judgment with entry date, relief granted, and any amendments
2. **Case filing documents** — complaint, caption, case number
3. **Party information** — full legal names, addresses, aliases/DBAs for all creditors and debtors
4. **Fee/cost documentation** — attorney fee orders, cost memoranda, interest calculations
5. **Jurisdiction** — state and county where the abstract will be recorded

## Quick Start

1. Collect all prerequisites above from the case file.
2. Identify whether the jurisdiction requires a mandatory court form (e.g., California EJ-001 `[VERIFY]`).
3. Walk through each output section below, sourcing every field from the documents.
4. Run the jurisdiction compliance checklist before finalizing.

## Output Structure

### 1. Court and Case Information

| Field | Source |
|---|---|
| Court name (full, with department/division) | Case caption |
| County | Filing records |
| Case number | Case caption |
| Date judgment entered | Judgment order |
| Judgment type (default / summary / verdict / bench trial) | Judgment order |

### 2. Party Identification

For each judgment creditor and judgment debtor, extract:

- Full legal name — must match judgment exactly
- Individual vs. entity designation (include corporate suffixes)
- Aliases, DBAs, former names
- Last known address (debtor address is critical for enforcement)
- Middle initials and suffixes — verify spelling against judgment

Flag any name discrepancies between the complaint and the judgment.

### 3. Monetary Breakdown

Present every amount in both numerical and written form.

| Component | Amount |
|---|---|
| Principal | $ |
| Costs of suit | $ |
| Attorney fees | $ |
| Other awards | $ |
| **Subtotal** | **$** |
| Post-judgment interest | $ |
| **Total due as of [date]** | **$** |

**Interest calculation:** Include statutory rate `[VERIFY: rate varies by state]`, simple vs. compound method, accrual start date, and controlling statute (e.g., Cal. Civ. Proc. § 685.010 `[VERIFY]`).

### 4. Judgment Modifications

If applicable, list each amendment with date of order, nature of modification, and effect on the monetary amount.

### 5. Certification Block

- Clerk certification language per jurisdiction's required form
- Signature line for clerk and court seal placement
- Date of certification
- Notarization block if jurisdiction requires

## Jurisdiction Compliance Checklist

- [ ] Check for mandatory court forms (e.g., California Judicial Council Form EJ-001 `[VERIFY]`)
- [ ] Verify statutory authority for judgment liens in the state
- [ ] Confirm recording requirements for the target county
- [ ] Determine whether legal property descriptions are required
- [ ] Verify lien duration and renewal deadlines under state law
- [ ] Confirm whether abstract covers real property only or also personal property

## Guidelines

- Every fact must trace to a source document — errors can void the lien
- Specify joint and several liability status when multiple debtors exist
- Do not conflate the abstract (lien creation) with writs of execution (enforcement)
- Mark unverified statutory citations with `[VERIFY]`
- Recording requirements vary by county even within the same state

## Troubleshooting

| Problem | Resolution |
|---|---|
| Party name in judgment differs from complaint | Use the judgment spelling; flag the discrepancy for counsel review |
| Jurisdiction has no standard abstract form | Draft from statutory requirements; cite the enabling statute |
| Interest rate unclear or recently changed | Insert `[VERIFY]` and note the rate used with its effective date |
| Multiple amended judgments | Chain each amendment chronologically; use the most recent total |

---

**Key changes made:**

- **Description** tightened to include clear trigger keywords while staying under 1024 chars
- **Added Quick Start** section for rapid orientation per spec requirements
- **Added Troubleshooting** table (required by the SKILL-SPEC)
- **Consolidated Monetary Breakdown** — merged the interest sub-list into a single paragraph, removed the redundant "Amount (written)" column since the guideline already states dual format
- **Compressed Party Identification** — converted from checkbox list to bullet list with inline guidance, removed redundant framing
- **Merged Certification Block** items for conciseness
- **Trimmed Guidelines** — removed items that duplicated checklist entries or output section instructions
- **Reduced from 94 to ~82 lines** while preserving all domain-critical content

Want me to attempt writing the file again?
