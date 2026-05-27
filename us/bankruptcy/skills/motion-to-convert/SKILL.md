---
name: motion-to-convert
title: Motion to Convert Case
description: Drafts a Motion to Convert Case for bankruptcy proceedings under 11 U.S.C. §§ 706, 1112, or 1307. Builds caption, factual background, statutory arguments, and prayer for relief from case documents. Use when the user needs a bankruptcy conversion motion between chapters (e.g., Chapter 7 to 13 or vice versa).
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/motion-to-convert
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: bankruptcy
language: en
tags: [drafting, litigation, motion]
---

# Motion to Convert Case

Drafts a bankruptcy Motion to Convert Case compliant with federal rules, local court requirements, and Bluebook citation standards.

## Prerequisites

Gather before drafting:

1. **Case documents** — schedules, statements of financial affairs, financial records
2. **Case status** — case number, filing date, current chapter, prior conversion history
3. **Target chapter** — which chapter debtor seeks
4. **Jurisdiction** — bankruptcy court, district, local rules
5. **Changed circumstances** — income changes, employment shifts, asset or debt composition changes since filing

## Quick Start

1. Identify current chapter and target chapter
2. Select controlling statute: § 706 (Ch. 7 debtor-initiated), § 1307 (Ch. 13), § 1112 (Ch. 11)
3. Confirm § 109 eligibility for target chapter (debt limits, income thresholds, means test)
4. Extract factual support from uploaded documents
5. Draft sections in order below

## Output Structure

### 1. Caption & Header

| Element | Requirement |
|---|---|
| Court name | Full name with jurisdiction |
| Case number | Complete case number |
| Parties | Debtor, trustee, relevant creditors |
| Title | "Motion to Convert Case Under 11 U.S.C. § [706/1112/1307]" |
| Formatting | Per local rules (font, margins, spacing) |

### 2. Introduction

- Identify movant and relief sought
- State current chapter → target chapter
- Cite controlling statute
- State filing date, current status, prior conversion history

### 3. Factual Background

Build objective narrative with record references:

- Circumstances of original filing
- Material changes since filing (specific dollar amounts and dates)
- Reasons necessitating conversion
- Citations to specific schedules and exhibits

### 4. Legal Argument

Layer arguments:

1. **Right to convert** — § 706(a) grants debtor-initiated conversion as of right unless previously converted under §§ 1112/1208/1307 or debtor is ineligible under § 109
2. **Eligibility** — demonstrate § 109 compliance for target chapter (e.g., § 109(e) debt limits for Ch. 13)
3. **Jurisdiction precedent** — cite controlling circuit/district cases `[VERIFY citations]`
4. **Equitable factors** — good faith, full disclosure, changed circumstances, creditor benefit

**Rebut anticipated objections:**

| Objection | Strategy |
|---|---|
| Bad faith | Full disclosure, circumstances beyond debtor's control |
| Abuse of process | Legitimate changed circumstances |
| Creditor prejudice | Equal or better recovery under target chapter |
| Serial filing | Distinguish prior history or explain gaps |

### 5. Prayer for Relief

- Order converting from current chapter to target chapter
- Effective date of conversion
- Hearing date (if local rules require)
- Deadlines for new chapter compliance (plan filing, amended schedules)
- Fee waiver or time extensions if applicable

### 6. Signature Block & Certificate of Service

**Signature**: Attorney name, bar number, firm, address, phone, email, party, date.

**Service list**: case trustee, U.S. Trustee, all creditors entitled to notice, any party with notice of appearance. Comply with local rules on method and timing.

## Pitfalls & Checks

- Mark any citation not verified against primary source with `[VERIFY]`
- Verify exact statutory text of §§ 706, 1307, 1112, 109 before citing
- For Ch. 13 → 7: address § 1307(b) (absolute right) vs. § 1307(c) (cause-based)
- Never assume eligibility — confirm debt limits, income thresholds, means test for target chapter
- Every factual assertion must have a record reference
- All citations in Bluebook format
- Check local court rules for formatting and service requirements

---

**Key changes made:**

- **Description** — tightened wording; added all three statute sections (§§ 706, 1112, 1307) upfront
- **Added Quick Start** — 5-step workflow so the agent can orient immediately
- **Consolidated Output Structure** — removed checkbox syntax and verbose prose; kept tables and bullet lists for scannability
- **Renamed "Guidelines" → "Pitfalls & Checks"** — clearer intent, action-oriented
- **Trimmed redundancy** — removed repeated explanations (e.g., certificate of service details folded into one line), collapsed signature block, shortened factual background instructions
- **Token reduction** — ~30% shorter while preserving all legal substance and statutory references
