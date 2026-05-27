---
name: discovery-response-summary
title: Discovery Response Summary
description: Synthesizes interrogatories, RFPs, RFAs, deposition transcripts, and privilege logs into a thematic, issue-based analytical memorandum with gap analysis and deficiency tracking. Trigger when the user asks to summarize discovery responses, review discovery, analyze privilege logs, plan follow-up discovery, prepare for summary judgment or trial from discovery materials, or cross-reference voluminous discovery across multiple methods.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/discovery-response-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [analysis, summarization]
---

# Discovery Response Summary

Reorganizes discovery responses from request-number order into legal-issue order, mapping what is established, disputed, or missing across all discovery methods — directly supporting motions to compel, summary judgment, settlement, and trial prep.

## Quick Start

1. Gather intake inputs (Checkpoint A)
2. Produce executive summary
3. Build thematic cross-reference table (primary deliverable)
4. Organize responses by discovery type
5. Analyze privilege log
6. Build deficiency tracker
7. Produce gap analysis and next steps
8. Validate with post-draft alignment (Checkpoint B)

## Checkpoint A: Pre-Draft Intake

Ask unless the user says "use defaults" or "just draft":

1. **Discovery requests** — interrogatories, RFPs, RFAs with request numbers and service dates
2. **Responses and objections** — all written responses including supplementals
3. **Production logs** — Bates ranges, privilege logs, withholding notices
4. **Deposition transcripts** — with page/line citations if available
5. **Operative pleadings** — complaint and answer (anchors thematic organization)
6. **Case posture** — next milestone (SJ, mediation, trial, class cert)

Defaults if no response: organize by claims/defenses from pleadings; include all discovery types provided; federal court; neutral tone.

> If operative pleadings are missing, organize by discovery categories and flag issue-mapping as provisional.

## Step 1: Executive Summary

- Scope of discovery (methods, parties, date range)
- Top 3–5 favorable findings
- Top 3–5 critical gaps or adverse admissions
- Recommended immediate next steps

## Step 2: Thematic Cross-Reference Table

Group all responses by legal issue, not request number:

| Issue/Element | Interrogatory | RFP | RFA | Deposition | Assessment |
|---|---|---|---|---|---|
| Liability – [element] | No. X: [summary] | No. X: [summary] | No. X: Admitted/Denied | [Witness], [page:line] | Established / Disputed / Gap |
| Damages | ... | ... | ... | ... | ... |
| Affirmative defenses | ... | ... | ... | ... | ... |

This is the primary deliverable.

## Step 3: Discovery by Type

**Interrogatories** — for each:
- **No. [X]**: [Request paraphrase]
  - *Objections*: [List] · *Answer*: [Summary] · *Flag*: Admission / Evasive / New witness / Bates ref

**RFPs** — for each:
- **No. [X]**: [Category]
  - *Produced*: [Bates range] · *Withheld*: [Privilege/ground] · *Deficiency*: [Yes/No — describe]

**RFAs** — for each:
- **No. [X]**: [Statement]
  - *Response*: Admitted / Denied / Objected / Insufficient denial · *Note*: [SJ/trial impact]

**Depositions** — for each witness:
- **[Name]** ([date])
  - Key admissions: [topic] — [page:line]
  - Contradictions with written discovery: [describe]
  - Documents identified: [Bates or description]

## Step 4: Privilege Log Analysis

| Entry | Privilege Claimed | Basis Adequate? | Challenge Viable? |
|---|---|---|---|
| [Doc/date] | AC / WP | Yes / No | Yes / No — reason |

Flag: over-designation, missing privilege elements, subject-matter waiver arguments.

## Step 5: Deficiency Tracker

| Request | Deficiency | MTC Basis | Priority |
|---|---|---|---|
| Rog No. X | Boilerplate objection, no substance | FRCP 33(b)(3) [VERIFY] | High |
| RFP No. X | Partial production, no withholding log | FRCP 34(b)(2)(C) [VERIFY] | Medium |

## Step 6: Gap Analysis and Next Steps

- **Additional interrogatories**: [Topic — reason gap exists]
- **Additional RFPs**: [Category — what's missing and why]
- **Depositions to take**: [Witness — identified in response No. X, not yet deposed]
- **MTC candidates**: [Deficient response — proposed remedy]

## Checkpoint B: Post-Draft Alignment

Ask after delivering the initial summary:

1. Does the thematic organization match your case theory?
2. Are the established/disputed/gap assessments calibrated to your posture?
3. Which follow-up actions to prioritize first?
4. Generate standalone deficiency tracker or MTC analysis from flagged items?

Default if no response: prioritize gap analysis and deficiency tracker for nearest deadline.

## Quality Checks

- Every finding cites a specific request number, Bates number, or deposition page:line
- Thematic table covers all claims, defenses, and disputed elements
- No discovery type omitted from cross-reference
- Favorable and adverse findings separately labeled
- Privilege log summaries do not reveal protected content
- Deficiency tracker includes rule basis and priority
- Interrogatory/deposition inconsistencies flagged for impeachment
- All rule citations verified or marked `[VERIFY]`
- Neutral analytical tone throughout

## Rules

- Mark jurisdiction-specific rules `[VERIFY]` if not confirmed U.S. federal
- For state court, confirm applicable rules before citing deadlines or limits
- **Anti-hallucination**: all citations must be verified or left as explicit placeholders
- **Attorney review required**: all output is practice-support work product requiring supervising counsel review before use in filings or client communications

---

**Key changes**: Tightened the description to focus on trigger guidance. Removed the "Why This Skill Exists" prose section and folded the core idea into a one-line overview. Added a Quick Start outline. Consolidated the per-type discovery formats into a denser inline style. Merged the Quality Audit and Guidelines sections into compact "Quality Checks" and "Rules" sections, eliminating duplicated guidance (e.g., citation requirements appeared in both). Removed horizontal rules between steps and the `summary` tag (redundant with `summarization`). Could you grant write permission so I can save this to the file?
