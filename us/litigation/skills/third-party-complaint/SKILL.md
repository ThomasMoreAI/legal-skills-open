---
name: third-party-complaint
title: Third-Party Complaint (Impleader)
description: Drafts a Third-Party Complaint (impleader) under FRCP 14 or state equivalents. Use when a defendant needs to implead a party for indemnification, contribution, subrogation, or breach of warranty during the pleadings phase.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/third-party-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Third-Party Complaint (Impleader)

Produces an FRCP 14 / state-equivalent third-party complaint asserting derivative liability against an impleaded party.

## Prerequisites

1. **Original complaint** — full copy for Exhibit A and incorporation by reference
2. **Derivative-liability basis** — indemnification contracts, insurance policies, warranties, or common-law indemnity/contribution facts
3. **Third-party defendant identity** — legal name, registered agent, service address
4. **Jurisdictional facts** — party citizenship (diversity), personal-jurisdiction contacts, venue basis
5. **Timing status** — within 14 days of original answer (as of right) or leave required

## Workflow

### 1. Caption & Introduction

- Full court name, division, original case number
- Party designations: Plaintiff; Defendant **and Third-Party Plaintiff**; Third-Party Defendant
- Title: "THIRD-PARTY COMPLAINT"
- Opening paragraph citing FRCP 14(a) / state rule and purpose of liability shifting

### 2. Procedural Posture

- Summarize original complaint: claims, theories, relief sought
- State: "The Complaint is attached as Exhibit A and incorporated by reference"
- Note answer date and timeliness of third-party filing

### 3. Jurisdiction & Venue

| Type | Basis |
|---|---|
| Subject matter | Federal question, diversity (complete + amount), or supplemental under § 1367 |
| Personal jurisdiction | Contacts, consent, or long-arm statute |
| Venue | § 1391 or applicable state rule |

### 4. Factual Allegations

Present chronologically. Must establish:

- Relationship between Defendant/TPP and Third-Party Defendant
- Specific agreements creating indemnification/defense/warranty obligations — quote key language verbatim
- Third-Party Defendant's acts or omissions contributing to Plaintiff's alleged harm
- Notice to Third-Party Defendant (dates, method, demands, response)
- Causal chain: TPD conduct → Defendant's exposure → Plaintiff's claims

### 5. Counts

Structure each as a separate numbered count from applicable theories:

| Theory | Key Elements |
|---|---|
| Contractual Indemnification | Quote provision; claims fall within scope; conditions precedent met |
| Common-Law Indemnification | Defendant's liability purely passive/vicarious; TPD is actual wrongdoer |
| Contribution | Both at fault; apportion per comparative-fault principles |
| Breach of Contract/Warranty | Obligation, breach, causation to Defendant's exposure |
| Subrogation | Defendant already paid; TPD bears ultimate responsibility |

Per count: incorporate factual paragraphs by reference, state elements, identify governing law, conclude with entitlement to judgment.

### 6. Prayer for Relief

Request: (a) judgment for all sums adjudged against Defendant including settlements; (b) full indemnification or contribution; (c) defense costs and attorney's fees (cite contractual or statutory basis); (d) declaratory relief on duty to defend/indemnify; (e) pre- and post-judgment interest; (f) costs of third-party action; (g) further just relief.

### 7. Signature Block

Standard attorney signature with Rule 11 / state-equivalent certification.

## Critical Checks

- **Timing**: Within 14 days of serving original answer → as of right (FRCP 14(a)(1)). After → motion for leave required.
- **Derivative liability only**: FRCP 14 requires claims derivative of the original action. Independent claims need separate counterclaim/crossclaim or independent jurisdiction.
- **Service**: Must serve TPD with the third-party complaint AND original complaint plus all prior pleadings.
- **Contract language**: Quote indemnification provisions verbatim — never paraphrase trigger language or scope limitations.
- **Supplemental jurisdiction**: § 1367 typically covers third-party claims, but confirm no statutory exception applies.
- **State variations**: Check local timing rules, leave requirements, and contribution statutes (UCFA vs. joint-and-several jurisdictions).
- **Party consistency**: "Defendant and Third-Party Plaintiff" on first reference, then "Defendant/TPP" throughout.
- **Rule 11**: Every factual allegation must have evidentiary support or be likely to after reasonable investigation.
