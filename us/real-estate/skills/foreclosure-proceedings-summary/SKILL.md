---
name: foreclosure-proceedings-summary
title: Foreclosure Proceedings Summary
description: Generates structured chronological summaries of U.S. foreclosure proceedings from case documents. Extracts parties, property, loan info, procedural timeline, judicial decisions, deadlines, and current status. Flags bankruptcy stays, loss mitigation holds, standing challenges, RESPA/TILA issues, and procedural irregularities. Distinguishes judicial vs. non-judicial procedures. Use when summarizing foreclosure case posture for lender representation, borrower defense, or real estate transactions affected by pending foreclosure.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/foreclosure-proceedings-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Foreclosure Proceedings Summary

Produces a structured case summary from foreclosure documents for rapid attorney review of procedural posture, deadlines, and next steps.

## Required Inputs

1. **Court filings** — complaint/petition, summons, proof of service, answer, motions, orders
2. **Notices** — notice of default, notice of sale, notice to occupants/junior lienholders
3. **Loan documents** — promissory note, mortgage/deed of trust, payment history
4. **Orders and judgments** — scheduling orders, judgment of foreclosure, sale confirmation
5. **Bankruptcy filings** or loss mitigation correspondence, if applicable

## Quick Start

1. Identify foreclosure type (judicial vs. non-judicial) and applicable state
2. Extract case overview fields into the Case Overview table
3. Build chronological procedural timeline from filings
4. Catalog all judicial decisions with reasoning and impact
5. Compile critical deadlines with current status
6. Assess current posture, immediate actions, and projected timeline
7. Run the Flags & Issues checklist

## Output Structure

### 1. Case Overview

| Field | Detail |
|---|---|
| Court & Case No. | |
| Plaintiff/Lender | |
| Defendant/Borrower | |
| Property Owner (if different) | |
| Property Description | Legal description + address |
| Original Loan Amount & Date | |
| Amount in Default | |
| Foreclosure Type | Judicial / Non-Judicial |

### 2. Procedural Timeline

Chronological table of all significant events:

| Date | Event | Legal Significance |
|---|---|---|
| | Initial default | |
| | Notice of default issued | |
| | Complaint filed / Trustee's sale recorded | |
| | Service of process completed | |
| | Answer / responsive pleadings | |
| | Motions (MTD, MSJ, etc.) | |
| | Hearings / conferences | |
| | Mediation / settlement | |
| | Judgment of foreclosure | |
| | Sale scheduled / conducted | |

### 3. Key Judicial Decisions

For each order or ruling: date, ruling, court's reasoning, and practical impact.

### 4. Critical Dates & Deadlines

| Date | Deadline / Event | Status |
|---|---|---|
| | Redemption period expiration | |
| | Foreclosure sale date | |
| | Response deadline (pending motions) | |
| | Trial / hearing dates | |
| | Jurisdiction-specific statutory deadlines | |

### 5. Current Status & Next Steps

- **Current procedural posture** — where the matter stands in the foreclosure process
- **Immediate actions required** — by which party, by when
- **Projected timeline** to resolution or sale

### 6. Flags & Issues

Check all that apply and note specifics:

- [ ] **Bankruptcy filing** — automatic stay in effect? Relief from stay sought/granted?
- [ ] **Loss mitigation** — application pending, foreclosure paused?
- [ ] **Standing challenge** — note transfers, MERS issues, securitization chain
- [ ] **TILA / RESPA** — compliance issues raised
- [ ] **Notice defects** — proper notice to junior lienholders, occupants, co-borrowers?
- [ ] **Procedural irregularities** — missed statutory deadlines, defective service
- [ ] **Deficiency judgment** — permitted under applicable state law?
- [ ] **Right of redemption** — statutory period and expiration

## Pitfalls & Checks

- **Judicial vs. non-judicial**: Always identify the mechanism — procedures, timelines, and defenses differ materially by state
- **Jurisdiction**: U.S. only; flag the state and note whether it is a judicial-foreclosure state [VERIFY applicable state statute]
- **Monetary figures**: State amounts exactly as in source documents; never round or estimate
- **Citations**: Reference specific document names and page numbers for key facts and dates
- **Objectivity**: Use neutral language suitable for plaintiff or defense counsel
- **Federal overlays**: Note RESPA (12 U.S.C. § 2605), TILA (15 U.S.C. § 1601), and CFPB loss mitigation rules (12 C.F.R. § 1024.41) where implicated [VERIFY current regulations]
