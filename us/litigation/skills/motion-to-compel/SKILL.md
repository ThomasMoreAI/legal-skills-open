---
name: motion-to-compel
title: Motion to Compel Discovery
description: Drafts filing-ready motions to compel discovery in civil litigation with deficiency matrix, declaration, memorandum, and proposed order. Covers interrogatories, RFPs, RFAs, depositions, and ESI disputes under federal FRCP and state analogs. Includes Rule 37(a)(5) sanctions strategy and meet-and-confer certification. Use when drafting a motion to compel, addressing boilerplate objections, seeking discovery sanctions, or preparing discovery dispute briefing.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/motion-to-compel
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, drafting, motion]
---

# Motion to Compel Discovery

Draft a filing-ready motion to compel with deficiency matrix, good-faith declaration, memorandum, and proposed order. Defaults to federal FRCP; swap to state analogs when state court specified.

## Prerequisites

1. **Court + jurisdiction** — federal district or state/county; local rule requirements (separate statement, page limits, pre-motion conference, joint letter)
2. **Discovery at issue** — interrogatories (Rule 33), RFPs (Rule 34), RFAs (Rule 36), depositions (Rules 30/31), subpoenas (Rule 45)
3. **Verbatim text** — requests served and responses/objections received, quoted exactly
4. **Chronology** — service dates, response deadlines, extensions, court orders, discovery cutoff
5. **Meet-and-confer record** — dates, methods, participants, concessions, remaining disputes
6. **Targeted relief** — specific items to compel, ESI format, privilege log demands, fees/sanctions sought
7. **Prejudice** — specific harm from the discovery failure

## Quick Start

1. Collect prerequisites above.
2. Map discovery type to rule authority (Phase 1 table).
3. Build deficiency matrix quoting requests and responses verbatim.
4. Draft motion package: Notice → Memorandum → Declaration → Proposed Order.
5. Run filing-readiness checks before submission.

Default posture: opposing party served boilerplate objections and/or incomplete answers; one written meet-and-confer plus live conference attempted; relief = complete verified responses within 14 days + fees under FRCP 37(a)(5).

## Phase 1: Rule Mapping & Deadlines

### Motion type selector

| Issue | Federal Authority | Traps |
|-------|-------------------|-------|
| No responses to interrogatories/RFPs | FRCP 33(b), 34(b), 37(a) | Some courts require first moving to deem objections waived |
| Boilerplate objections / incomplete answers | FRCP 26(b)(1), 33, 34, 37(a) | Must address proportionality |
| Privilege without adequate log | FRCP 26(b)(5) + local rule | Courts often require conferral + proposed log format |
| RFAs improperly denied | FRCP 36(a)(6) | Different standard from Rule 37(a) |
| Deposition nonappearance | FRCP 30, 37(a)(3)(B), 37(d) | 37(d) (no prior order needed) vs. 37(a) (refusal to answer) |
| ESI format dispute | FRCP 34(b)(1)(C), 34(b)(2)(E) | Specify custodians, date ranges, search terms, metadata, native vs. TIFF |

### Rule reference

| Topic | Rule |
|-------|------|
| Scope / Proportionality | FRCP 26(b)(1) |
| Interrogatories | FRCP 33 |
| Requests for Production | FRCP 34 |
| Requests for Admission | FRCP 36 |
| Motion to Compel | FRCP 37(a) |
| Expenses on Motion | FRCP 37(a)(5) |
| Failure to Attend / Serve | FRCP 37(d) |
| Privilege Log | FRCP 26(b)(5) |
| ESI Format | FRCP 34(b)(1)(C), 34(b)(2)(E) |

### Deadline checklist

- [ ] Response due dates per discovery set (including extensions)
- [ ] Motion-to-compel filing deadline (state rules may impose strict windows, e.g., CA: 45 days)
- [ ] Scheduling order discovery-motion deadlines
- [ ] Local rules: pre-motion conference/IDC, joint statement, separate statement, page limits, e-filing
- [ ] Judge's standing orders and chambers rules
- [ ] Discovery cutoff — confirm hearing can occur before cutoff

## Phase 2: Deficiency Analysis & Meet-and-Confer

### Deficiency matrix (core deliverable)

Quote all requests and responses **verbatim** — courts disfavor paraphrasing.

| No. | Request (Verbatim) | Response/Objection (Verbatim) | Deficiency | M&C Position / Compromise | Relief Requested |
|----:|---------------------|-------------------------------|-----------|---------------------------|-----------------|
| 1 | [Full text] | [Full text] | [Rule violated] | [Narrowing offered] | [Precise order sought] |

Group related requests by legal issue. For each deficiency, cite rule violated and quantify proportionality (importance to claims, amount in controversy, relative access, resources, burden vs. benefit).

### Meet-and-confer log

| Date | Method | Participants | Issues Raised | Opposing Position | Result |
|------|--------|-------------|---------------|-------------------|--------|

## Phase 3: Draft Motion Package

### 3A — Notice of Motion

Structure: court caption → title identifying discovery type → relief paragraphs (compel responses, production format, deem RFAs admitted, compel deposition, award expenses under FRCP 37(a)(5)) → reference to memorandum and declaration → date/signature block.

### 3B — Memorandum of Points and Authorities

Include only sections relevant to the discovery types at issue:

**I. Introduction** — One paragraph: what was served, what is deficient, why it matters.

**II. Procedural History** — From timeline and M&C log.

**III. Legal Standard**
- Scope: FRCP 26(b)(1) — relevant and proportional to needs of the case
- Compel: FRCP 37(a) — motion lies on failure to answer or evasive/incomplete response
- Burden: resisting party must show irrelevance or disproportionality
- Evasive/incomplete = failure to respond: FRCP 37(a)(4)

**IV. Argument** — Use applicable modules:

| Module | Key Points |
|--------|-----------|
| Interrogatories (Rule 33) | Answer separately, fully, under oath. "See documents" valid only under 33(d) if burden substantially same and records specified. Unverified = no response. |
| RFPs (Rule 34) | State compliance or objection with specificity per 34(b)(2)(B). State whether materials withheld per 34(b)(2)(C). "Subject to and without waiving" condemned as ambiguous. |
| RFAs (Rule 36(a)(6)) | Denial must fairly respond to substance. Court may deem admitted or order amended answer. |
| Depositions (Rules 30/37) | Nonappearance: sanctions mandatory under 37(d). Instructions not to answer proper only to preserve privilege, enforce court limitation, or present 30(d)(3) motion. |

**V. Expenses — Rule 37(a)(5) sanctions decision tree:**

| Condition | Result |
|-----------|--------|
| Motion granted or disclosure made after filing | Fees presumptively awarded — 37(a)(5)(A) |
| Movant failed M&C? | Exception (i) — fees denied |
| Opposing position substantially justified? | Exception (ii) — fees denied |
| Other circumstances make award unjust? | Exception (iii) — fees denied |
| Prior violations by same party? | Strengthens sanctions; cite pattern |
| Willful/bad-faith conduct? | Consider Rule 37(b)/(c) if prior order violated |

**VI. Conclusion** — Summarize specific relief; request entry of proposed order.

### 3C — Good-Faith Declaration

Structure: declarant identification and personal knowledge → discovery served (Exhibit A) → responses received with deficiencies (Exhibits B–C) → chronological M&C efforts with dates, methods, compromises offered (Exhibits D–E) → remaining impasse by request number → good-faith certification → penalty-of-perjury attestation → signature with bar number.

Some courts require certification in the motion body or specific statutory language. [VERIFY] for jurisdiction.

### 3D — Proposed Order

Structure: title (granting in whole or part) → numbered paragraphs: supplemental responses deadline, document production deadline with search methodology, privilege log deadline, RFA deemed-admitted or amended-response deadline, deposition reconvened with hour/topic limits, fee award with 37(a)(5)(A) cite and briefing schedule → signature line for judge.

### 3E — Exhibit checklist

- [ ] **A**: Discovery requests as served
- [ ] **B**: Responses and objections received
- [ ] **C**: Deficiency matrix
- [ ] **D**: Meet-and-confer letter(s)
- [ ] **E**: Follow-up correspondence confirming impasse
- [ ] **F**: Stipulations/extensions
- [ ] **G**: Deposition transcript excerpts (if obstruction)
- [ ] **H**: ESI correspondence/protocol (if ESI dispute)
- [ ] **I**: Relevant scheduling order portions

## Phase 4: Filing Readiness

### Local rules compliance

- [ ] Pre-motion conference / IDC completed if required
- [ ] Joint statement / joint letter prepared if required
- [ ] Separate statement in jurisdiction-required format (request → response → reasons → relief)
- [ ] Page limits, formatting, exhibit labeling verified
- [ ] Judge's individual practices reviewed
- [ ] Notice period and calendaring rules confirmed
- [ ] E-filing requirements confirmed; proposed order uploaded separately
- [ ] Certificate of service prepared

### Hearing preparation

- [ ] 1–2 page disputes summary (top 3–5 contested requests, one-sentence argument each)
- [ ] Proportionality talking points (importance, amount in controversy, relative access, resources, burden vs. benefit)
- [ ] Narrowed compromise position ready (phased production, reduced custodians, date-range limits, sampling)
- [ ] Fee documentation with Rule 37(a)(5) exceptions addressed preemptively
- [ ] Responses to anticipated opposition (proportionality, privilege, burden, work product)

## Output Modes

| Mode | Contents |
|------|----------|
| **Full Package** (default) | Notice + Memorandum + Declaration + Deficiency Matrix + Proposed Order + Exhibit Checklist |
| **Matrix + Templates** | Deficiency Matrix + Declaration + Proposed Order + Timeline Table |
| **Compliance Checklist** | Deadline + M&C + Local Rules + Hearing Prep checklists (no drafted text) |

## Refinement Options

| Option | Description |
|--------|-------------|
| **State conversion** | Provide state/court; all FRCP cites replaced with state analogs and special requirements incorporated |
| **Separate statement** | Standalone separate statement in jurisdiction-required format |
| **Aggressive tone** | Sanctions-focused tone emphasizing obstructionist conduct and noncompliance pattern |
| **ESI relief** | Detailed ESI sections: custodians, data sources, search terms/TAR, metadata, native format, clawback |
| **RFA variant** | Focused motion under Rule 36(a)(6) to determine sufficiency or deem admitted |
| **Deposition variant** | Focused motion under Rule 37(d) for nonappearance |
| **Joint letter** | 3–5 page joint discovery letter format for magistrate judges |

## Guidelines

- Quote all discovery requests and responses **verbatim** — courts disfavor paraphrasing
- Burden assignment: resisting party must justify objections with specific facts
- Relief must be precise: specific request numbers, deadlines, format, verification, privilege log deadline
- Address Rule 37(a)(5) exceptions preemptively (substantial justification, good faith, unjust circumstances)
- Verify all rule citations are current; confirm local rule numbers for the specific court
- For state courts, map all FRCP references to state equivalents (e.g., CA separate statement, CA 45-day filing deadline)
- No placeholder text in filed documents; redact confidential information per court rules

---

Key changes from the original:

- **Description**: Tightened from 3 dense lines to a focused paragraph with clear trigger guidance
- **Added Quick Start**: 5-step entry point so the agent can orient fast
- **Removed verbatim templates**: The Notice of Motion, Good-Faith Declaration, and Proposed Order were full boilerplate templates (~60 lines of code blocks). Replaced with structural outlines that convey the same sequencing and required elements in ~3 lines each. The agent generates the actual text; it doesn't need a fill-in-the-blank template.
- **Removed Defaults table**: Inlined as a single sentence in Quick Start since it's just 4 values
- **Preserved all legal-critical content**: Rule mapping table, rule reference table, sanctions decision tree, argument modules, deficiency matrix schema, deadline checklist, exhibit checklist, filing readiness checklists — all retained verbatim
- **Added `[VERIFY]` tag** on the declaration jurisdiction note, consistent with other legal skills in the repo
- **Net reduction**: ~285 lines → ~175 lines (~39% smaller) with no loss of procedural accuracy
