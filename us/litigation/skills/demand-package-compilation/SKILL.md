---
name: demand-package-compilation
title: Demand Package Compilation
description: Compiles pre-suit and settlement demand packages for U.S. commercial litigation plaintiff matters. Assembles demand letter with chronological facts, liability theories, itemized damages, and indexed exhibits. Use when drafting pre-filing demand packages, settlement demand letters with exhibit bundles, or structured pre-litigation claim presentations.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/demand-package-compilation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Demand Package Compilation

Assembles a litigation-ready demand package — cover letter, demand letter, and indexed exhibits — for settlement negotiation.

## Prerequisites

1. **Case facts** — incident/breach narrative, dates, party names and roles
2. **Damages documentation** — medical bills, invoices, wage records, repair estimates
3. **Evidence inventory** — photos/video, witness statements, expert reports, contracts, correspondence
4. **Legal theories** — duties breached, applicable statutes or common law claims
5. **Demand figure** — client-approved amount with response deadline

## Quick Start

Collect all five prerequisites, then draft the package in order: cover letter, demand letter (with exhibit references woven into the fact narrative), damages table, and exhibit index. Cross-check every exhibit reference before finalizing.

## Package Structure

### 1. Cover Letter

Brief transmittal identifying matter, parties, and purpose.

### 2. Demand Letter

| Section | Content |
|---|---|
| Introduction | Client identity, adverse party, basis for claim |
| Statement of Facts | Chronological narrative with exhibit references (Ex. 1, Ex. 2…) |
| Legal Theories | Duty, breach, causation, damages — one paragraph per theory |
| Damages Summary | Itemized table with total demand figure |
| Liability Analysis | Why liability is clear; preempt key weaknesses |
| Demand & Deadline | Dollar amount; response deadline (typically 30 days) |

### 3. Damages Table

| Category | Subcategory | Amount | Exhibit |
|---|---|---|---|
| Economic | Past medical expenses | $ | Ex. __ |
| Economic | Future medical expenses | $ | Ex. __ |
| Economic | Past lost wages | $ | Ex. __ |
| Economic | Future earning capacity | $ | Ex. __ |
| Economic | Property damage / repairs | $ | Ex. __ |
| Economic | Out-of-pocket expenses | $ | Ex. __ |
| Non-Economic | Pain and suffering | $ | — |
| Non-Economic | Emotional distress | $ | — |
| Non-Economic | Loss of enjoyment of life | $ | — |
| Non-Economic | Loss of consortium | $ | — |
| Punitive | Legal basis + conduct described | $ | Ex. __ |
| **TOTAL DEMAND** | | **$** | |

### 4. Exhibit Index

Number exhibits sequentially mirroring demand letter narrative. Typical groupings:

- Incident documentation (reports, scene photos)
- Medical records and billing
- Employment and wage loss records
- Property damage estimates and invoices
- Photographic / video evidence
- Witness statements and affidavits
- Expert reports
- Contracts and agreements
- Correspondence
- Legal authority (statutes, key cases)

## Pre-Finalization Checklist

- [ ] Every exhibit reference in the letter matches an included, labeled exhibit
- [ ] Every factual assertion backed by an exhibit
- [ ] Damages figures cross-referenced to source documents
- [ ] Dates, names, party designations consistent throughout
- [ ] Total demand and response deadline stated clearly
- [ ] No attorney work product or privileged communications included
- [ ] HIPAA: written patient authorization confirmed before transmitting medical records
- [ ] Sensitive PII redacted where not essential
- [ ] Package paginated, bookmarked (PDF), and exhibit-indexed

## Common Pitfalls

- **Privilege leak** — The package becomes opposing counsel's property upon transmission. Exclude all attorney-client communications and work product.
- **HIPAA violation** — Never include medical records without confirmed written patient authorization.
- **Unsupported punitives** — Include punitive damages only where conduct meets the governing state's legal standard. Verify jurisdiction-specific threshold and pleading requirements.
- **Statute of limitations** — Verify the applicable limitations period and any statutory notice requirements before setting the response deadline.
- **Incomplete package** — The package must be self-contained. The recipient should be able to evaluate the full claim without follow-up.
- **Tone** — Professional and factual. Let evidence carry persuasive weight; avoid inflammatory language.

---

**Key changes made:**

- **Removed `tags`** — not part of the Agent Skills spec frontmatter
- **Trimmed description** — tightened wording while keeping all trigger keywords
- **Added Quick Start** section per best practices structure
- **Consolidated Exhibit Index** — replaced verbose table (with placeholder ranges) with a compact bullet list
- **Renamed "Guidelines" to "Common Pitfalls"** — reframed as actionable failure modes instead of passive guidance
- **Merged jurisdiction/tone/HIPAA/privilege rules** into the pitfalls section to eliminate duplication with the checklist
- **Reduced line count** from 92 to ~82 while preserving all domain-critical content (damages table, demand letter structure, checklist, compliance guardrails)
