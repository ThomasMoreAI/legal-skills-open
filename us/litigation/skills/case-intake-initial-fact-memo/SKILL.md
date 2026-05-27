---
name: case-intake-initial-fact-memo
title: Case Intake & Initial Fact Memo
description: Generates a structured attorney work product memorandum from an initial client consultation for commercial litigation. Extracts verifiable facts from uploaded documents, builds a chronological narrative, identifies parties and contracts, flags preliminary legal claims and defenses, and produces a prioritized action plan. Triggers at matter intake when a business client needs a foundational case evaluation document for a pre-filing commercial dispute.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/case-intake-initial-fact-memo
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, drafting, memo]
---

# Case Intake & Initial Fact Memo

Produces an attorney work product memorandum capturing the initial consultation for a commercial litigation matter. Serves as the foundational document for case evaluation and strategy.

## Quick Start

1. Collect client intake info, key contracts, correspondence, financial records, and conflicts check results
2. Generate the memo using the section structure below
3. Mark every page **ATTORNEY WORK PRODUCT – CONFIDENTIAL**
4. Use assigned case number or `Intake-[YYYY-MM-DD]` as identifier

## Prerequisites

- **Client intake** — full legal entity name, formation state, principal contacts
- **Key contracts** — executed agreements central to the dispute, with amendments
- **Correspondence** — demand letters, emails, notices (chronological)
- **Financial records** — invoices, payment records, damages calculations (if available)
- **Conflicts check** — clearance confirmation and any waivers

## Memo Sections

### 1. Header

Include: Matter/Case No., Date Prepared, Prepared By, Supervising Attorney, Client (full legal entity name), Subject line as `Initial Fact Memo: [Client] – [Dispute Type] – [Brief Description]`.

### 2. Client & Business Profile

- Legal entity: name, type, formation state, principal place of business, registered agent
- Key contacts: name, title, phone, email
- Business context: industry, size, corporate structure
- Referral source, prior representations, conflicts status

### 3. Case Overview

3–5 paragraph narrative covering:
- Dispute type and party relationship
- Legal objectives (recovery, injunction, declaratory relief) vs. business objectives (relationship preservation, reputation, deterrence)
- Precipitating event and urgency drivers
- Amount in controversy with source citation
- Posture: claimant, defendant, or both

*No liability conclusions — frame as facts and preliminary observations only.*

### 4. Chronology of Key Facts

| Date | Event | Parties Involved | Source / Citation |
|------|-------|-----------------|-------------------|

- Use **direct quotations** when contract/correspondence language may be dispositive
- Label every fact: `[Client Statement]`, `[Doc: filename, p. X]`, or `[Unverified]`
- Flag timeline gaps, inconsistencies, and missing referenced materials

### 5. Key Parties

| Party | Full Legal Name | Jurisdiction | Role | Status |
|-------|----------------|--------------|------|--------|

Include client, adverse parties, and third-party witnesses.

### 6. Contractual Framework

For each material agreement, document:
- Contract type, execution date, parties
- Key obligations (cite § and quote verbatim)
- Payment terms, notice/cure requirements, termination provisions
- Dispute resolution clause (**quote verbatim** — arbitration or litigation)
- Choice of law and forum selection (**quote verbatim** — mandatory or permissive)
- Liquidated damages, liability caps, consequential damages exclusions (cite §)
- Amendments and side letters (date and effect)

### 7. Preliminary Legal Issues & Claims

**Potential claims (client as claimant):**

| Claim | Elements | Supporting Facts (cite) | Apparent Strength | Likely Defenses |
|-------|----------|------------------------|-------------------|-----------------|

**Potential counterclaims / client exposure:**

| Claim | Factual Basis | Preliminary Defenses |
|-------|--------------|---------------------|

**Threshold issues checklist:**
- [ ] Statute of limitations: accrual date, governing period, expiration
- [ ] Arbitration clause: mandatory? scope? waivable?
- [ ] Forum selection: mandatory or permissive?
- [ ] Choice of law conflicts with forum state?
- [ ] Pre-suit notice/demand requirement (cite contract §)
- [ ] Administrative exhaustion required?
- [ ] Heightened pleading standard (e.g., fraud/particularity)?
- [ ] Novel or unsettled legal questions requiring research

### 8. Damages & Relief

**Monetary:** Direct damages, consequential/lost profits (methodology + assumptions), incidental, statutory/punitive (cite statute), attorneys' fees (contract/statute §).

**Contractual modifiers:** Liquidated damages, liability caps, consequential exclusions — cite § for each.

**Non-monetary:** Specific performance, injunction, declaratory judgment, rescission, accounting — state basis for inadequacy of legal remedies.

**Business objectives beyond recovery:** Relationship preservation, confidentiality, precedent, competitive protection.

### 9. Procedural Posture & Deadlines

| Item | Date / Status | Notes |
|------|--------------|-------|

Track: demand letters, litigation filings, arbitration demands, administrative proceedings, SOL deadlines, contractual notice deadlines, response deadlines, litigation hold status.

### 10. Document Inventory & Evidence Assessment

| # | Document | Date | Author / Recipients | Relevance | Evidentiary Issues |
|---|----------|------|--------------------|-----------|--------------------|

- Extract critical quoted language verbatim with citations
- List missing documents referenced but not produced
- Flag privilege issues (attorney-client, work product)
- Note metadata/forensic concerns (version history, track changes, send times)

### 11. Preliminary Strategic Assessment

- **Strengths/weaknesses**: factual and legal, including gaps and credibility concerns
- **Witness assessment**: availability, reliability, impeachment vulnerability
- **Opposing party profile**: financial capacity, likely strategy, known counsel
- **Leverage points**: business dependencies, reputational exposure, regulatory risk
- **ADR viability**: negotiation/mediation/arbitration timing and client receptiveness
- **Settlement posture**: client objectives and risk tolerance

### 12. Recommendations & Immediate Action Items

| Priority | Action | Responsible | Deadline | Consequence of Delay |
|----------|--------|-------------|----------|---------------------|

Always include:
1. Litigation hold notice (immediate — spoliation risk)
2. File/respond deadline (SOL/waiver risk)
3. Additional document requests
4. Legal research on specific issues
5. Expert consultation needs

Note **client decisions needed** (file vs. negotiate, preliminary injunction, fee arrangement) and **additional information needed** (documents, witnesses, factual clarifications).

### 13. Attachments

Every document cited in the memo must appear in an attachment index or its absence explained. Organize by category: contracts, correspondence, financial records, corporate/organizational docs, administrative.

## Guidelines

- **Source every fact**: `[Client Statement]`, `[Doc: name, p. X]`, or `[Unverified]`
- **Quote, don't paraphrase** notice, arbitration, forum selection, and choice-of-law clauses — these control procedure
- **No liability conclusions** in §§ 3–4; reserve legal assessment for § 7 with qualifiers (`preliminary analysis suggests`, `subject to further research`)
- **Flag `[VERIFY]`** on any legal citation whose current validity is uncertain
- **Work product designation** on every page
- **US commercial litigation** scope — note state-specific procedural rules; flag choice-of-law conflicts

## Troubleshooting

- **Missing contracts**: Flag in § 10 and add to § 12 action items as priority document request
- **Conflicting client statements vs. documents**: Note discrepancy in § 4 chronology with both versions; flag for follow-up
- **No case number assigned**: Use `Intake-[YYYY-MM-DD]` format throughout; update on assignment
- **Uncertain legal citations**: Always append `[VERIFY]` — never present unconfirmed authority as settled law
