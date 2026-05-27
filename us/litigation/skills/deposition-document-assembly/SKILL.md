---
name: deposition-document-assembly
title: Deposition Document Assembly
description: Assembles and organizes documents for deposition preparation, producing a document inventory, exhibit list, impeachment index, and gap analysis. Use before building a deposition outline for any deponent type (fact witness, party, corporate rep/30(b)(6), expert) in US federal or state litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-document-assembly
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Deposition Document Assembly

Identifies, categorizes, and inventories documents tied to a deponent, then produces an exhibit candidate list, gap analysis, impeachment index, and preparation checklist.

## Prerequisites

Collect before starting:

1. **Deponent identity** — name, role, party/non-party status
2. **Topics** — subject matter; 30(b)(6) notice topics if applicable
3. **Case materials** — produced documents, pleadings, prior testimony
4. **Deponent type** — fact witness, party, corporate rep, or expert

Prompt for any missing items before proceeding.

## Workflow

### 1. Identify Documents

Search by three axes:

**Connection to deponent:** authored, received, CC'd/BCC'd, mentioned by name, custodial (from deponent's files/email).

**Topic:** key events deponent will testify about, decisions they participated in, relevant communications, applicable policies, business records they maintained.

**Prior statements:** depositions in this or other cases, affidavits/declarations, interrogatory answers, RFA responses identifying the deponent, written or recorded statements.

### 2. Build Document Inventory

Create a table with columns: Doc ID, Description, Date, Bates, Connection, Category, Key Pages, Notes.

Connection types: Authored / Received / CC'd / Mentioned / Custodial / Topic-related

Categories: Authentication / Impeachment / Key Fact / Background / Pleading-Discovery

### 3. Generate Exhibit Candidate List

Create a table with columns: Exhibit #, Document, Bates/ID, Topic, Purpose, Priority (Essential / Likely / Backup).

Choose an organization scheme: chronological (narrative depositions), topical (issue-focused), or strategic (examination sequence).

### 4. Run Gap Analysis

Check for missing documents by deponent type:

| Deponent Type | Verify Presence Of |
|---|---|
| Any | Resume/CV, org chart, job description, prior testimony in this case |
| Party | Complaint/Answer, interrogatory responses, RFA responses, produced docs |
| Employee | Personnel file (if relevant), training/disciplinary records, email samples |
| 30(b)(6) rep | Corporate org docs, policies/procedures per notice topic, prior 30(b)(6) testimony |
| Expert | Expert report, CV, publications, fee agreement, prior testimony list, materials considered |

For each gap, document: what is missing, why it matters, potential source, and action required.

### 5. Build Impeachment Index

For each potential inconsistency, record: document, Bates/ID, exact quote from document, expected testimony, nature of inconsistency, and planned approach.

For each entry include: (1) exact page/paragraph citation, (2) commitment questions before confrontation, (3) follow-up after introduction.

### 6. Produce Final Package

Output a summary containing:

- Deponent name, role, deposition date
- Document counts by category (authentication, impeachment, key fact, background, pleadings/discovery)
- Gaps identified with required actions
- Preparation checklist:
  - Obtain missing documents per gap analysis
  - Prepare clean exhibit copies
  - Number/tab exhibits; prepare sets for witness, opposing counsel, reporter
  - For remote depositions: load documents in presentation software, test screen sharing
  - Review impeachment documents; integrate into deposition outline

## Pitfalls and Rules

- **Impeachment exhibits:** Do not pre-disclose if jurisdiction permits surprise; keep separate from main exhibit binder
- **30(b)(6) scope:** Exhibits must align with designated notice topics — flag any documents outside scope
- **Authentication planning:** Note which deponent can authenticate each exhibit for trial (FRE 901-902); plan method per exhibit (witness testimony, self-authentication, stipulation)
- **FRCP 30(f):** Original exhibits must be annexed to the deposition record unless parties stipulate otherwise — verify local rules
- **FRE 408:** Label settlement-adjacent communications if used for a non-settlement purpose

## Related Skills

- `deposition-preparation` — outline building
- `deposition-questioning-techniques` — document use during examination
- `deposition-30b6-corporate-rep` — corporate representative specifics

---

**Key changes made:**

- **Removed `tags`** — not part of the Agent Skills spec
- **Tightened description** — shorter, third-person, with clear trigger guidance (from 394 to 230 chars)
- **Eliminated empty template tables** — described column schemas inline instead; Claude knows how to produce tables
- **Removed the code-fenced final output template** — replaced with a concise bullet list of what to include
- **Condensed Phase 1's three sub-tables** into compact inline lists — same information, ~60% fewer tokens
- **Collapsed "Guidelines" into "Pitfalls and Rules"** — tighter section name, same legal substance
- **Renamed "Output Structure / Process" to "Workflow"** with numbered steps — matches best-practice pattern
- **Reduced from 149 lines to ~85 lines** — well under the 500-line ceiling
