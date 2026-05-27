---
name: bulk-document-extraction-review
title: Bulk Document Extraction & Review
description: 'Extracts structured data from large sets of legal documents into tabular format for review, analysis, and reporting. Processes contracts, agreements, correspondence, filings, and other legal documents in bulk — extracting key terms, dates, parties, obligations, risks, and custom fields into organized tables. Use when conducting due diligence document review, bulk contract extraction, compliance audits across document sets, lease portfolio analysis, employment agreement review, regulatory filing review, or any task requiring structured extraction from multiple documents. Trigger keywords: tabular review, bulk extraction, document review table, data room review, batch document analysis, contract extraction, portfolio review, structured extraction, document comparison table.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/bulk-document-extraction-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [transactional, corporate, litigation, summary, report, analysis, research]
---

# Bulk Document Extraction & Review

Extracts structured data from sets of legal documents into tabular format. Each document becomes a row; user-defined questions become columns. Produces reviewable tables with source citations, then supports analysis across the extracted dataset.

## Prerequisites

1. **Document set** — the files to analyze (contracts, agreements, correspondence, filings, etc.)
2. **Extraction questions** — what to extract from each document (see Column Design below)
3. **Document type** — the nature of the documents (e.g., all NDAs, mixed data room, email set)
4. **Review purpose** — what the table will be used for (DD report, compliance check, portfolio analysis, case chronology)
5. **Output preferences** — format (table, CSV, report narrative), language, level of detail

If extraction questions are not provided, propose a standard column set based on the document type.

## Workflow

### Phase 1: Column Design

Define extraction columns. Each column is a question asked of every document. Column types:

| Type | Description | Example |
|---|---|---|
| **Verbatim** | Extract exact language from the document | "What is the governing law clause?" |
| **Free response** | Summarize or interpret | "Summarize the key obligations of the Seller" |
| **Classification** | Yes/No or category | "Does this agreement contain a change-of-control provision?" |
| **Date** | Extract specific dates | "What is the effective date?" |
| **Numeric** | Extract amounts, percentages | "What is the liability cap amount?" |
| **List** | Multiple items from same document | "List all defined terms" |

**Standard column sets by document type:**

**Contracts / Agreements:**
- Document name and type
- Parties (with roles)
- Effective date and term
- Governing law and jurisdiction
- Key financial terms (price, payment, caps)
- Termination provisions (convenience, cause, notice period)
- Assignment / change of control
- Indemnification scope
- Limitation of liability
- Confidentiality term
- Unusual or non-standard provisions
- Red flags or concerns

**Correspondence / Emails:**
- Date and time
- Sender and recipient(s)
- Subject
- Key facts or events described
- Commitments or action items
- Attachments referenced
- Privilege indicators

**Court Filings / Pleadings:**
- Filing date
- Document type (motion, brief, order, etc.)
- Filing party
- Relief sought or ruling issued
- Key arguments or findings
- Deadlines or next dates
- Cited authorities

### Phase 2: Document Processing

For each document in the set:

1. **Identify** — document name, type, date, page count
2. **Extract** — answer each column question with:
   - The extracted value
   - Source citation (page number, section, paragraph)
   - Confidence indicator when the answer requires interpretation
3. **Flag** — note any documents that:
   - Cannot be processed (corrupted, illegible, wrong format)
   - Contain ambiguous answers for a given column
   - Have notable omissions (expected provision absent)

### Phase 3: Table Assembly

Compile results into a structured table:

| Doc # | Document Name | [Column 1] | [Column 2] | ... | [Column N] | Flags |
|---|---|---|---|---|---|---|

**Table conventions:**
- One row per document
- Empty cells marked "Not found" or "N/A" (distinguish between absent and inapplicable)
- Multi-value cells use semicolons as delimiters
- Source citations in parentheses after each value: (§3.2, p.7)
- Flags column captures anomalies, concerns, or items requiring attorney review

### Phase 4: Cross-Document Analysis

After extraction, analyze the dataset:

#### 4a. Summary Statistics
- Total documents processed / skipped / flagged
- Distribution of key values (e.g., "65% have mutual indemnification, 35% one-sided")
- Date ranges (earliest and latest effective dates, expirations)
- Outliers (documents with unusual terms relative to the set)

#### 4b. Risk and Anomaly Report
- **Inconsistencies** — documents with conflicting terms (different governing law, conflicting definitions)
- **Missing provisions** — documents lacking standard clauses present in majority of set
- **Outlier terms** — values significantly different from the norm (unusually high caps, short cure periods)
- **Red flags** — provisions requiring immediate attorney attention

#### 4c. Comparative Analysis
- Side-by-side comparison of key terms across selected documents
- Deviation from standard or template language
- Trend analysis (if documents span time periods)

### Phase 5: Report Generation

Based on the extracted table and analysis, produce:

1. **Executive summary** — key findings, overall risk assessment, critical items requiring action
2. **Detailed table** — full extraction results (Phase 3 output)
3. **Analysis narrative** — written summary of cross-document patterns, risks, and recommendations
4. **Follow-up list** — documents or issues requiring further review, with specific questions

## Use Case Templates

### M&A Due Diligence Data Room
**Columns:** Parties, Date, Contract type, Term, Renewal, Change of control, Assignment consent, Material financial terms, Restrictive covenants, IP provisions, Termination triggers, Red flags
**Analysis focus:** Change-of-control provisions that could block closing, material contracts requiring consent, unusual termination rights, aggregate financial exposure

### Lease Portfolio Review
**Columns:** Property, Landlord, Tenant, Commencement, Expiration, Renewal options, Monthly rent, Escalation, CAM/NNN, Assignment/subletting, Termination rights, Restoration obligations
**Analysis focus:** Upcoming expirations, below/above-market rents, assignment restrictions affecting transactions, aggregate lease obligations

### Employment Agreement Audit
**Columns:** Employee, Title, Start date, Term, Base compensation, Bonus/equity, Non-compete scope and duration, Non-solicit, IP assignment, Severance triggers, Change-of-control provisions, Governing law
**Analysis focus:** Non-compete enforceability by jurisdiction, aggregate severance exposure, key person dependencies, inconsistencies across similar roles

### Regulatory Filing Review
**Columns:** Filing type, Filing date, Filer, Jurisdiction, Status, Key disclosures, Material changes from prior filing, Deficiencies noted, Response deadline
**Analysis focus:** Compliance gaps, missed deadlines, material disclosure changes, cross-filing consistency

## Guidelines

- Every extracted value must include a source citation (section, page, or paragraph reference)
- Distinguish between "Not found" (searched but absent) and "N/A" (not applicable to this document type)
- Do not infer or extrapolate values — extract only what the document explicitly states
- When a provision is ambiguous, extract the verbatim language and flag for attorney review rather than interpreting
- Process documents in consistent order (alphabetical, chronological, or as provided)
- For large sets, process in batches and maintain consistent column definitions across batches
- Flag any document that appears to be a duplicate or superseded version
- Note document language — if documents are in multiple languages, indicate the source language and whether extraction was from the original or a translation
- Mark [VERIFY] on any extracted value where confidence is low due to poor document quality, ambiguous language, or complex cross-references
- Maintain a processing log: document name, status (processed/skipped/flagged), notes
