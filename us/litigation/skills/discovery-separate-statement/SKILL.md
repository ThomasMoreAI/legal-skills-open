---
name: discovery-separate-statement
title: California Discovery Separate Statement
description: Drafts a California-compliant discovery Separate Statement for motions to compel under Cal. Rules of Court rule 3.1345. Trigger when the user mentions a California motion to compel, Separate Statement, "sep stat," Rule 3.1345, CCP 2023.030 sanctions, interrogatory/RFP/RFA/deposition disputes, or verbatim request-response formatting for CA Superior Court discovery motions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/discovery-separate-statement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, motion]
---

# California Discovery Separate Statement

Produces a request-by-request Separate Statement that is verbatim-accurate and aligned with the motion package (memorandum, declaration, proposed order). Required under Cal. R. Ct. 3.1345 — omission renders the motion procedurally defective.

## Quick Start

1. Collect verbatim request/response text and meet-and-confer record
2. Build a disputed-item ledger locking sources
3. Draft per-item blocks (request → response → meet-and-confer → reasons → remedy)
4. Run consistency pass against the full motion package
5. Deliver for attorney review

## Pre-Draft Intake

Gather before drafting (apply labeled defaults if user says "use defaults" or "just draft"):

1. **Discovery set** — verbatim propounding text, definitions, latest responses (objections, qualifications, verification status, production references)
2. **Meet-and-confer record** — letters, emails, declarations with dates; concessions or supplements
3. **Case framing** — complaint/answer (claims, defenses tied to each request); protective orders, ESI protocols
4. **Motion posture** — motion type, proposed relief, hearing date, 45-day deadline calculation including service method
5. **Court requirements** — local/department preferences (IDC/JCCP, format, tables vs. sequential text)

**Defaults if user skips:** compel further responses; all disputed requests; sequential text; sanctions under CCP § 2023.030.

> **Hard stop:** If verbatim request/response text is missing, halt and request it before drafting.

## Core Workflow

### 1. Classify Motion

Produce a single-line taxonomy and gap check:

`Taxonomy: Motion to compel further responses to [device/set]: Nos. [range], plus [relief/sanctions].`

- Further-response motion with deficient responses → Separate Statement required (Cal. R. Ct. 3.1345(a)) [VERIFY]
- Pure failure-to-respond → may use alternate CCP tracks [VERIFY]

### 2. Build Disputed-Item Ledger

One row per disputed item — source-lock table preventing drift:

| Item ID | Device | Request Source | Response Source | Service Date | Dispute Type |
|---|---|---|---|---|---|
| RFA-1-8 | RFA | RFA Set One No. 8 | Response 3/01/2026 | 3/01/2026 | Evasive response |

- Copy verbatim including punctuation
- Include cross-referenced responses inline
- Preserve "subject to and without waiving" language
- Flag no-response items for failure-to-respond branching

### 3. Draft Per-Item Blocks

Each disputed item follows this structure:

**REQUEST [ID]:** verbatim request + relevant definitions
**RESPONSE:** verbatim response + objections + qualifications + supplements
**MEET-AND-CONFER:** date, issue, cure requested, outcome
**FACTS AND LEGAL REASONS:** device-specific deficiency + relevance to pleadings + authority + burden/privacy handling
**ORDER SOUGHT:** single, enforceable, narrow, date-certain remedy

Prefer labeled blocks for e-filing stability. Use tables only if court preference supports it.

### 4. Apply Device-Specific Analysis

| Device | Deficiency Focus | Typical Remedy |
|---|---|---|
| Interrogatory (CCP §§ 2030.210–.310) [VERIFY] | Non-verified, incomplete, evasive | Further verified response; inability statement |
| Production (CCP §§ 2031.210–.320) [VERIFY] | "Will comply" only, no search showing, missing privilege log | Production by custodian/date/form; privilege log |
| Admission (CCP §§ 2033.210–.300) [VERIFY] | Boilerplate objections, noncommittal answers | Clear admit/deny; strike unsupported objections |
| Deposition | Refusal, privilege overreach | Further response or appearance order |

- Tie every reasons paragraph to a pleaded issue (liability, damages, causation, impeachment)
- Privacy/trade-secret claims: include narrowing, redaction, protective measures
- Burden objections: require evidentiary support; flag missing declarations

### 5. Draft Remedies and Sanctions

Permissible relief (keep narrow and enforceable):
- Further response without objections
- Document-existence statement
- Production by fixed date
- Privilege log
- Verified inability-to-comply statement

For sanctions under CCP § 2023.030 [VERIFY]: identify conduct item-by-item; align with motion language. Do not introduce requests beyond original discovery.

### 6. Consistency Pass

- Verify quoted text matches exhibits page-accurate
- Cross-check IDs, dates, relief language across memorandum, declaration, and Separate Statement
- Remove moot/fully cured items
- Keep chronology factual; no hyperbole

## Post-Draft Alignment

Ask after delivering initial draft:

1. Correct set of disputed requests — any to add or remove?
2. Meet-and-confer summaries accurate for each item?
3. Per-item relief matches memorandum and proposed order?
4. Court-specific formatting adjustments needed?

If no answer, recommend consistency cross-check against memorandum and proceed if authorized.

## Quality Checklist

- [ ] All requests/responses verbatim — no paraphrasing
- [ ] Motion type consistent throughout
- [ ] Every item has documented meet-and-confer support
- [ ] Deadline + service method verified
- [ ] Citations verified or marked `[VERIFY]`
- [ ] Relief is enforceable and date-certain
- [ ] IDs, dates, party names consistent across motion documents
- [ ] No moot/cured items remaining
- [ ] Device-specific analysis applied correctly
- [ ] Privacy/privilege handling includes narrowing proposals

## Pitfalls

- Never draft from paraphrased memory — use source documents only
- Never omit adverse response portions
- Never include arguments belonging in the memorandum
- Never overstate meet-and-confer efforts
- Flag doubtful citations with `[VERIFY]` — no plausible-sounding unverified law
- Use California terminology; avoid federal substitutions unless user confirms
- Respect CRPC duties: competence (1.1), candor (3.3), confidentiality (1.6), fairness (3.4) [VERIFY]
- **All output is practice-support work product — attorney review required before filing**
