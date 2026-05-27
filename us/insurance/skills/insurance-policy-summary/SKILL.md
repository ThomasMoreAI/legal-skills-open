---
name: insurance-policy-summary
title: Insurance Policy Summary
description: Produces structured, citation-backed summaries of U.S. insurance policies, endorsements, claims files, and coverage correspondence for coverage analysis and insurance litigation. Use when summarizing policies, declarations, claims files, reservation-of-rights letters, denial letters, or coverage disputes.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/insurance-policy-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: insurance
language: en
---

# Insurance Policy Summary

Deliver a litigation-grade, source-cited summary of policy terms and claim handling that supports coverage strategy. Stay neutral unless instructed otherwise.

## Prerequisites

- All policies, endorsements, declarations pages, and schedules
- Claims file materials and correspondence (notice, ROR, denial)
- Loss facts and timeline (date of loss, claimant, damages)
- Jurisdiction and choice-of-law indicators (policy clause, venue)

## Output Structure

### 1. Executive Summary

2-3 paragraphs covering: policies at issue and coverage posture, triggering event/loss and claim status, primary disputes or ambiguities.

### 2. Policy Inventory

| Insurer | Policy No. | Period | Named Insured | Coverage Types | Limits | Deductible/SIR | Key Endorsements | Source |

### 3. Endorsements and Modifiers

| Endorsement | Effect on Coverage | Date/Version | Source |

### 4. Coverage Analysis

- Insuring agreement(s) relevant to the claim
- Definitions controlling scope of coverage
- Exclusions potentially invoked
- Conditions precedent and compliance issues
- Other insurance / priority (primary vs. excess)
- Allocation across policy periods
- Quote critical policy language verbatim with pinpoint cite

### 5. Claims Chronology

| Date | Event | Actor | Amount | Coverage Position | Source |

### 6. Parties and Roles

| Party | Role | Relationship | Source |

### 7. Financials

| Type | Amount | Date | Notes | Source |

Types: Reserves, Payments, Demand, Estimate, Exposure.

### 8. Coverage Positions

| Position | Basis | Policy Provision | Communicated By | Date | Source |

### 9. Legal Issues and Dispute Drivers

- Ambiguity points and competing interpretations
- Notice, cooperation, and prejudice issues
- Bad faith / extra-contractual exposure indicators
- Choice-of-law implications for interpretation
- Subrogation, contribution, or allocation disputes

### 10. Gaps and Missing Information

Flag: missing endorsements/schedules, unclear policy periods, incomplete claims file segments, unverified loss facts.

### 11. Source Map

Document name + page/paragraph for each quoted or key fact.

## Checks

- Pinpoint cite every key term, exclusion, condition, and coverage position.
- Flag privilege or work-product materials without summarizing content.
- Distinguish primary vs. excess; identify overlap or gaps.
- Apply jurisdiction-specific interpretation only when identified in the documents.
- Mark uncertain authority as `[VERIFY]`.
