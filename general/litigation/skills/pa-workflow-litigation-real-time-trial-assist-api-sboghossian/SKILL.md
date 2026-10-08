---
name: pa-workflow-litigation-real-time-trial-assist-api-sboghossian
title: Real-Time Trial Assist API
description: Use during an active trial or arbitration hearing to provide live support to counsel at the counsel table. Detects witness contradictions against prior depositions and statements in real time, surfaces suggested cross-examination follow-up questions, fact-checks opposing counsel's legal propositions, and retrieves relevant documents within a 1–3 second latency budget. Designed for DIFC, ADGM, international arbitration, UK, and US trial settings.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-litigation-real-time-trial-assist-api
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Real-Time Trial Assist API

## Purpose

Trial hearings are real-time, high-stakes environments where facts surface unexpectedly. This API-layer workflow provides a live decision-support layer for counsel at the counsel table: streaming witness testimony triggers instant contradiction alerts, document retrieval is sub-3-second, and suggested follow-up questions are surfaced in a minimal UI without disrupting courtroom proceedings.

**Latency budget: ≤ 3 seconds for contradiction alerts and document retrieval; ≤ 5 seconds for suggested questions.**

## What It Does

| Function | Description | Latency target |
|---|---|---|
| Live contradiction detection | Compare incoming witness statement against indexed prior depositions, statements, and documents | ≤ 3 sec |
| Cross-examination follow-up suggestions | Generate contextually appropriate next questions based on testimony just given | ≤ 5 sec |
| Opposing counsel cite-check | Verify legal propositions and case citations as they are stated in argument | ≤ 5 sec |
| Document retrieval | Surface any exhibit, deposition excerpt, or case authority from the trial database | ≤ 2 sec |
| Timeline consistency check | Identify if a witness's stated timeline contradicts known dates in the record | ≤ 3 sec |

## Setup and Data Model

Before trial begins, the trial database must be loaded and indexed:

### Required pre-trial indexing

1. **All prior depositions** — full transcripts, indexed by witness and topic
2. **All witness statements** (if jurisdiction uses pre-filed statements)
3. **All trial exhibits** — OCR'd, tagged by exhibit number, witness, and topic
4. **Public statements** — press releases, LinkedIn posts, news coverage attributed to key witnesses
5. **Documents authored or received by each witness** — extracted from the discovery corpus
6. **Case authorities** — all legal citations in briefs, referenced by party and proposition

### Technical requirements

- Streaming transcript feed: human-typed (paralegal types testimony in real time) or automated court reporter feed (where available)
- Vector-indexed document store for sub-second semantic search
- Alert interface: minimal sidebar or tablet display at counsel table
- Keyboard shortcut triggers: e.g., `Ctrl+Q` for "generate follow-up question," `Ctrl+D` for "retrieve document"

## Functions — Detailed Behavior

### Contradiction Detection

**Trigger**: every 2–3 sentences of live testimony, run a semantic similarity pass against the prior testimony and statements index for the active witness.

**Output format:**
```
CONTRADICTION ALERT
Witness: Ahmed Al-Sayed
Current statement: "I never reviewed the contract before it was signed."
Prior statement: Deposition 2023-03-14, p. 47, line 12 — "I personally reviewed and approved every vendor contract over $50,000."
Exhibit: Ex. 22 — Contract approval form bearing witness's signature, dated 2022-09-01.
SEVERITY: HIGH — direct factual contradiction on material issue
```

Do not alert on every minor variation — reserve HIGH alerts for direct factual contradictions on material issues. Mark LOW for tone or timing inconsistencies.

### Cross-Examination Follow-Up Suggestions

**Trigger**: counsel presses `Ctrl+Q` after a witness answer.

**Input**: the last 3–5 witness answers in context + the contradiction alerts fired so far in this session.

**Output**: 3 prioritized follow-up questions, each with:
- The question text
- The goal (lock down the admission, confront with document, or establish foundation)
- The exhibit or prior-statement reference to use if the witness retreats

Example:
```
Suggested questions (post-testimony: "I had no authority over that account"):
1. Q: "Earlier in your deposition you testified you approved all wire transfers — did you give that testimony?" [Goal: establish perjury foundation] [Exhibit: Depo p. 47]
2. Q: "This is Exhibit 23 — the wire approval log — is that your signature?" [Goal: confront with document]
3. Q: "Who in your organization had authority over this account during Q3 2022, if not you?" [Goal: foreclose alternative explanations]
```

### Opposing Counsel Cite-Check

**Trigger**: paralegal types an opposing counsel citation as heard.

**Input**: case name + year + jurisdiction.

**Output within 5 seconds**:
- Does the case exist? (from pre-loaded authorities database)
- Is the cited proposition accurate? (matches indexed holding)
- Has the case been overruled or distinguished? (pre-loaded subsequent treatment)
- Alert if the citation appears to mischaracterize the holding

### Document Retrieval

**Trigger**: counsel types exhibit number, witness name, or keyword.

**Returns**: the indexed exhibit or transcript excerpt, highlighted at the relevant passage, ready to display on counsel's screen or the court's display system.

## Permissions and Safety

- The system is an assist tool; all trial decisions are made by counsel, not the system.
- The system must not send communications to the court or opposing counsel.
- Alerts appear only on counsel's device; the system has no courtroom display integration by default.
- All data ingested into the trial database must be court-filed or pre-approved material; no external internet lookups during trial (risk of inadvertent judicial notice issues).
- The contradiction detection output is attorney work product; it is protected from disclosure.

## Jurisdictional Notes

- **US (federal / state)**: Counsel may use laptops and tablets at counsel table freely in most federal courts. Check local rules for technology order requirements.
- **UK / DIFC / ADGM**: Courts routinely permit electronic hearing bundles and laptop use. Streaming court reporter feeds may not be available; paralegal typing is the standard input method.
- **International Arbitration (ICC, LCIA, DIAC)**: Hearing rooms typically permit electronic devices. Arbitral tribunals do not have the same constraints as courts. Technology orders should be addressed in procedural orders.
- **UAE onshore / KSA**: Court hearings are shorter and more document-focused. Sessions before a single judge with limited oral cross-examination reduce the value of a full real-time assist setup. A document-retrieval-only mode is more practical in these forums.

## Failure Modes

- **Streaming lag**: if testimony input falls more than 30 seconds behind actual testimony, contradiction alerts are no longer useful. Test input speed before trial.
- **OCR errors in prior transcripts**: poor-quality OCR on deposition transcripts creates false negatives (missed contradictions). Pre-trial OCR quality check is mandatory.
- **Over-alerting**: if sensitivity is set too high, counsel is flooded with LOW-severity alerts during routine testimony. Calibrate to HIGH only for first day; adjust based on volume.
- **Database completeness**: any material not indexed before trial will not surface in retrieval or contradiction detection. Run a completeness audit the evening before each hearing day.

## Related Skills

- [[pa-workflow-litigation-witness-contradiction-finder]]
- [[pa-workflow-litigation-transcript-search-q-and-a-indexing]]
- [[pa-workflow-litigation-deposition-binder-builder]]
- [[pa-workflow-litigation-expert-witness-prep-memo]]
- [[pa-workflow-litigation-brief-cite-checker]]
