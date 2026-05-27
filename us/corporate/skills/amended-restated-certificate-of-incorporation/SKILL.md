---
name: amended-restated-certificate-of-incorporation
title: Amended and Restated Certificate of Incorporation (Delaware)
description: Drafts filing-ready Delaware Amended and Restated Certificates of Incorporation for venture-financing rounds. Converts term-sheet economics and governance terms into a defensible charter document under DGCL 242/245. Trigger when user needs to reauthorize capital structure, designate preferred stock series, set investor protections, or prepare a charter filing for closing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/amended-restated-certificate-of-incorporation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Amended and Restated Certificate of Incorporation (Delaware)

Drafts a Delaware A&R COI aligned to term sheet, SPA, and governance documents, ready for filing.

## Prerequisites

Collect before drafting. Stop and request any missing item.

1. Exact legal name, Delaware formation date, current charter text
2. Board resolution and stockholder approval route (DGCL 242 vs. 245)
3. Term sheet + definitive docs (SPA, investors' rights, voting agreement, ROFR/co-sale)
4. Cap table: outstanding shares, option pool, convertibles, warrants, financing amounts
5. Per-series economics: OIP, liquidation multiple, conversion mechanics, anti-dilution method, voting/protective rights
6. Delaware registered agent name, physical office address with county
7. Board composition rights and series-specific carve-outs
8. Authorized signer with corporate authorization evidence

## Quick Start

1. Gather all prerequisites above
2. Walk through the six-step workflow sequentially
3. Halt at any step where required data is missing—request it before continuing
4. Output complete certificate text or redline-ready draft with assumptions log

## Workflow

| Step | Gate | Output |
|---|---|---|
| 1. Deal parsing | Transaction math and term consistency confirmed | Validated term summary |
| 2. Entity compliance | Jurisdiction, registered details, adoption path verified | Entity confirmation |
| 3. Capital math | Authorized share tables with rounding/cushion checks | Share authorization schedule |
| 4. Preferred architecture | Series provisions, voting, protections, conversion, anti-dilution drafted | Preferred stock articles |
| 5. Governance layer | 102(b)(7), indemnification, forum/consent mechanics added | Governance articles |
| 6. Filing hardening | Witness/signature block, signatory authority confirmed | Execution-ready document |

## Required Inputs

| Item | Source | Validation |
|---|---|---|
| Legal name | Formation docs | Exact match across all transaction docs |
| Registered office + agent | Corporate records | Physical address with county |
| Series designations | Term sheet | Unique identifiers, share counts |
| OIP / Conversion price | Cap table + pricing | Convertible math tested |
| Liquidation waterfall | Term sheet / SPA | Participating vs. non-participating explicit |
| Anti-dilution | Term sheet | Full formula with carve-outs |
| Protective provisions | Term sheet + voting agreement | Series-specific treatment resolved |
| Officer execution | Corporate records | Authorized signer identified |

## Drafting Structure

### Preface / Recitals
- Heading: "Amended and Restated Certificate of Incorporation of [Exact Legal Name]"
- DGCL 242/245 basis, supersession clause, full textual restatement statement

### Articles I–III: Identity
- **Name**: exact legal name, Delaware naming compliance
- **Registered office/agent**: physical address, county, consent posture
- **Purpose**: broad Delaware-purpose clause unless deal terms narrow it

### Article IV: Capitalization
- Common authorized shares / par value
- Preferred authorized shares / par value, per-series designation and count
- Blank-check preferred if negotiated
- **Math checks**: common authorized ≥ outstanding + option pool + convertibles + cushion; preferred includes anti-dilution reserve buffer

### Article V: Preferred Stock Rights
- **Dividends**: cumulative/non-cumulative, rate, priority
- **Liquidation**: preference multiple (1x default), waterfall, participation/election logic
- **Conversion**: optional + mandatory mechanics, fractional handling, timing
- **Anti-dilution**: broad-based weighted average default; full ratchet only if explicitly instructed
- **Protective provisions**: veto rights thresholds, affected actions, exceptions
- **Voting**: as-converted framework, class/series voting where required

### Article VI: Directors / Governance
- 102(b)(7) exculpation with DGCL-compliance fallback
- Indemnification only if negotiated in rights docs
- Optional: forum selection, board action mechanics

### Execution
- "IN WITNESS WHEREOF" block, officer signature/date lines
- Signatory authority backed by corporate action record

## Templates

Series designation summary format:

Series [X] Preferred Stock
- Designated Shares: [__]
- OIP: [$__] / Conversion Price: [$__]
- Liquidation: [__]x non-participating
- Conversion: Optional [yes/no], Mandatory: [trigger list]
- Anti-dilution: [broad-based weighted avg / other]
- Voting: [as-converted rights text]
- Protective actions: [list with vote threshold]

## Pitfalls and Checks

- **Term consistency**: align all charter economics with SPA, investor rights, and voting agreement—resolve conflicts before drafting
- **Defined terms**: define once, reference consistently; never introduce synonyms
- **Statutory anchoring**: confirm DGCL references against current statute text; mark unverified references with `[VERIFY]`
- **Scope discipline**: exclude investor-specific terms outside preferred stock mechanics (repurchase discounts, drag thresholds) unless charter language is required
- **Missing-data gates**: enforce checkpoints for adoption path (242 vs. 245), min/max authorized totals, series-specific protective voting splits, anti-dilution carve-outs
- **Delaware-only**: include county and physical registered office only; no non-Delaware filing forms
- **Waterfall testing**: reconcile liquidation outputs under ≥3 exit-value scenarios and ≥2 dilution scenarios before finalizing
- **Flexibility vs. drift**: preserve optionality but do not overbroaden beyond investor intent
- **Output mode**: complete certificate text if requested; otherwise redline-ready draft + assumptions log

---

**Key changes made:**

- **Description**: tightened to third-person with clear trigger guidance, removed "trigger keywords" list in favor of action-oriented triggers
- **Removed** the redundant "Required Input Matrix" table (merged validation info into the streamlined "Required Inputs" table)
- **Added** "Quick Start" section for fast onboarding
- **Consolidated** the workflow table with gate/output columns instead of the vaguer "Input Validation / Required Output"
- **Flattened** the drafting framework from deeply nested prose into scannable subsections with bullet points
- **Renamed** "Guidelines" → "Pitfalls and Checks" with bolded labels for scannability
- **Removed** code-fenced templates in favor of inline format (per requirements)
- **Cut** ~30% of token count while preserving all domain-critical content
