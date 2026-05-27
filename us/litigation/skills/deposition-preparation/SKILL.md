---
name: deposition-preparation
title: 'Deposition Preparation: Strategic Planning and Execution'
description: Produces a comprehensive deposition preparation package for taking or defending depositions in U.S. civil litigation. Use this skill whenever the user mentions deposition prep, depo outlines, witness examination planning, deposition strategy, cross-examination preparation, 30(b)(6) witness prep, expert deposition planning, impeachment materials, or asks for help preparing to take or defend any deposition. Also trigger when the user references FRCP 30, deposition notices, deposition exhibit strategy, witness profiling for depositions, or asks about deposition time allocation. Even if the user just says "I have a depo next week" or "help me prep for questioning this witness," use this skill.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/deposition-preparation
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Deposition Preparation: Strategic Planning and Execution

## Why This Skill Exists

Depositions are one of the highest-leverage moments in U.S. civil litigation. Fewer than one percent of cases reach a jury, making the deposition the functional equivalent of trial. Testimony becomes a permanent evidentiary artifact that drives summary judgment, settlement posture, expert framing, trial examination, and impeachment. When prep is done poorly, the record is incomplete, admissions are missed, privilege is waived, and the client gets locked into avoidable testimony.

This skill produces a deposition preparation package a litigation team can actually use at the table—not just a question list, but a strategic plan tied to elements and defenses, a time allocation, exhibit integration, impeachment scripts, and (when defending) an ethics-safe witness prep agenda.

The primary grounding is FRCP 26 and 30, with supporting guidance from FRE 612, 613, 702, 803, and 901. For detailed legal standards, read `references/legal-standards.md`. For jurisdiction-specific adaptations, read `references/jurisdiction-adaptations.md`.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Deponent identity and witness type** — party, nonparty fact witness, expert, 30(b)(6) corporate representative, or apex executive
2. **Posture** — taking or defending, and which side counsel represents
3. **Top 2–3 ranked objectives** — discovery, summary judgment admissions, trial preservation, impeachment setup, credibility assessment, damages exploration, or expert reliability challenge
4. **Controlling time limit** — whether a court order or stipulation modifies the default (federal default: 7 hours under FRCP 30(d)(1))
5. **Case posture question** — "What is the next major milestone?" (summary judgment, mediation, class cert, Daubert, PI, trial). This tunes the outline: if SJ is next, emphasize element-by-element commit points over open-ended exploration

**If the user doesn't respond**, apply and clearly label these defaults: taking deposition; objectives of discovery and impeachment setup; seven hours; hybrid topical-chronological format.

### Documents to Request

Request these materials—they substantially improve quality:

- Deposition notice (especially topic list for 30(b)(6))
- Operative complaint + answer with affirmative defenses
- Initial disclosures (FRCP 26(a)(1)) and supplementation history
- Key discovery responses (interrogatories, RFPs, RFAs)
- "Hot doc" set — documents the witness authored, received, or that bear on targeted issues
- Prior statements: declarations, affidavits, prior testimony, emails, texts
- Expert reports/disclosures if expert witness (FRCP 26(a)(2))
- Scheduling order and protective order
- Meet-and-confer correspondence on scope disputes

If materials are missing, flag them explicitly. Proceed with labeled assumptions rather than stalling, but list "Open Items / Needed Inputs" for attorney follow-up.

---

## Step 1: Build the Issue Map

Deposition outlines fail when they're topic lists untethered to burdens and elements. Every substantive topic must serve a purpose: establishing a prima facie element, supporting an affirmative defense, or attacking credibility.

Extract or infer claims, defenses, and disputed issues from the pleadings. If pleadings aren't available, create a provisional issue map with `[ASSUMED]` markers.

### Required Deliverable: Issue Mapping Table

| Issue/Element | What We Need to Prove/Disprove | What This Witness Can Establish | Best Documents/Prior Statements | Target Admission/Lock Point |
|---|---|---|---|---|

**Example:** In a negligence case where "notice" is an element, the lock point might be: *"You received the inspection report (Ex. 12) on March 3 and understood it described the hazard."*

Do not invent evidence. Use placeholders and flag them for attorney verification when the record is unknown.

The issue map also supports proportionality under FRCP 26(b)(1)—you can justify time spent by showing its link to claims, defenses, and the importance of the issues.

---

## Step 2: Profile the Witness and Choose Examination Architecture

### Witness Profile

Compile: role and tenure; relationship to key actors; likely motivation or bias; prior statements and testimony; personal knowledge vs. hearsay vs. learned knowledge (critical for 30(b)(6) designees); all documents authored by, received by, or mentioning the witness.

Include an "anticipated demeanor and risk" paragraph:
- **Overconfident witness** → accelerate commit points, use documents to tighten
- **Anxious witness** → slow down, avoid compound questions
- **Evasive witness** → plan for "I don't recall" patterns, prepare FRE 612 memory refreshment sequences

### Architecture Selection

Match structure to witness type and litigation objective:

- **Pure chronological** — best for percipient witnesses who experienced events in sequence and where credibility is central
- **Topical** — best for 30(b)(6) reps (notice topics control scope) and experts (opinions are modular)
- **Hybrid** — frequently best for party witnesses: background/role → short chronology → issue-driven topical modules

For detailed witness-type adaptations (30(b)(6), expert, apex, defending), read `references/witness-types.md`.

---

## Step 3: Draft the Outline as a Record-Building Instrument

The outline must be easy to execute under time pressure and easy for later users (SJ drafter, trial examiner) to mine for usable testimony.

### Required Deliverable: Time Allocation Table

| Topic | Est. Time | Priority (1–5) | Notes |
|---|---|---|---|

Total should approximate the controlling limit. Federal default is 7 hours under FRCP 30(d)(1). Whether breaks count against time varies by stipulation and court order—confirm with the attorney.

### Outline Structure

**Preliminary Section (~15 min)**
- Admonitions: verbal responses required, no head nods, ask for clarification, correct misunderstandings, break rules
- Preparation inquiry: when did the witness learn of the depo, who did they meet with, what documents did they review, any outlines or memoranda used
- When defending: privilege and instruction-not-to-answer reminder per FRCP 30(c)(2)

**Substantive Modules** — for each topic, use the funnel technique:

1. **Open narrative** — "Tell me everything you remember about the June 1 meeting." Gather information before narrowing the witness's room to maneuver.
2. **Investigative follow-up** — "Who sat where? What documents were on the table? Who spoke first?"
3. **Document examination** — authenticate ("Is this an email you received?"), have the witness read the relevant passage, ask for their interpretation at the time, lock in the commitment
4. **"Is That All" exhaustion** — "Besides what you just told me, is there anything else? Are you sure?"
5. **Confirming lock** — "So it's fair to say Mr. Jones never mentioned the budget deficit during that meeting, correct?"

Jumping to the locking-in phase too early is a common and costly mistake. Leading immediately suggests the answer and may prevent discovering a more damaging fact the witness would have volunteered.

**FWD Boxing-In (Critical for SJ Prep)**

This is the most critical tool for summary judgment preparation. Exhaust the witness's memory so they cannot "remember" new facts at trial:

- "Is that the complete list of everyone who was present?"
- "Have you now told me every reason why you terminated the plaintiff?"
- "If we go to trial six months from now, will you have any other reasons to add?"

Failing to ask the catch-all question is one of the most common errors—without it, the witness can appear at trial with a "refreshed memory" and impeachment is significantly weakened.

**Conclusion Section (~15 min)** — completeness check, additional witnesses/documents identification, truthfulness confirmation, reservation of rights if needed.

---

## Step 4: Integrate Exhibits and Impeachment Materials

### Required Deliverable: Exhibit Integration Guide

| Topic | Exhibit | When to Use | Purpose | Foundation Questions | Impeachment Hook |
|---|---|---|---|---|---|

For every major exhibit, prepare a Foundation Script. Example:

> "I'm handing you what's been marked as Exhibit 4. Do you recognize it? It's an email from you to Sarah Smith dated January 10, correct? You wrote this in the ordinary course of your job, right? Looking at the second paragraph, you wrote [quote]. What did you mean by that?"

Include foundation for authentication (FRE 901) and, where applicable, business records exception (FRE 803(6)).

Flag FRE 612 implications when documents refresh recollection—the adverse party may be entitled to production.

Prompt for non-traditional exhibits that often prove decisive: calendars, metadata, system logs, training records, ticketing systems, version histories, collaboration platform records.

### Required Deliverable: Impeachment Materials Table

| Topic | Prior Statement | Source/Citation | Expected Current Testimony | Contradiction | Approach |
|---|---|---|---|---|---|

Use the **Commit → Credit → Confront** method:

1. **Commit** — get the witness to state the inconsistent position clearly: *"You never saw the warning sign, correct?"*
2. **Credit** — build up the contradicting document's reliability: *"You signed this declaration under penalty of perjury two weeks after the accident? Your memory was fresh? You were being truthful?"*
3. **Confront** — present the contradiction: *"Then why does your declaration say, 'I saw the yellow warning sign and walked around it'?"*

If exact citations (page, line, paragraph) aren't available, insert placeholders and mark for attorney verification. Reference FRE 613 requirements for prior inconsistent statements.

---

## Step 5: Produce the Deliverables

Output a two-lane deliverable by default, plus a defending pack when appropriate.

### Lane 1: Full Deposition Prep Package
- Strategy overview tied to the case milestone
- Issue-element map table
- Deposition outline with time allocation
- Exhibit integration guide
- Impeachment materials table
- Follow-up discovery targets

### Lane 2: Condensed At-the-Table One-Pager
- Top objectives
- Three must-get admissions
- Exhibit order
- Time-topic clock with fallback paths if time runs short

The one-pager is not optional—it's the execution instrument. Opposing counsel benefits when the examining attorney can't find the next move.

### Lane 3: Defending Pack (when counsel is defending)
- Anticipated topics and exhibits
- Vulnerabilities and safe themes
- Ethics-safe prep session agenda
- Objection and privilege framework (per FRCP 30(c)(2))
- Rehabilitation topics for re-examination

For defending-specific details, read `references/witness-types.md` (defending section).

### Mandatory Front Matter

At the very top of every output, before any substantive content, include:

1. **Assumptions Used** — posture, time limit, objectives, witness type, key case facts relied on
2. **Open Items / Needed Inputs** — missing pleadings, discovery, exhibits, jurisdictional rule uncertainties

This front matter is a critical anti-hallucination guardrail: it tells the attorney exactly what was assumed and what must be verified.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial package, ask:

1. Does this match the right witness and posture?
2. Which add-on modules should be generated? — condensed one-pager, verbatim question sequences for key admissions, exhibit pack with authentication scripts, impeachment scripts (commit-credit-confront), defending prep agenda, topic deep-dive
3. Are there "red-line topics" to avoid or handle delicately?
4. What are the three must-get admissions (or does the attorney confirm the proposed three)?

If the user doesn't answer, recommend the next best refinement based on stated objectives and proceed if authorized.

---

## Quality Audit

Before finalizing, run through the self-audit checklist in `references/quality-checklist.md`. The critical checks:

- Every objective ranked and tied to claims, defenses, and issues
- Issue mapping table completed
- Time allocations total matches controlling limit
- Funnel technique present in each substantive module
- FWD boxing-in included in each module
- Exhibit integration guide present
- Impeachment table present (even with placeholders)
- Defending materials included if defending
- Assumptions and open items listed prominently
- Every factual assertion traceable to a document, pleading, discovery response, or labeled as assumption
- No invented case citations — see authority guardrails in `references/legal-standards.md`

---

## Reference Files

Read these when you need deeper guidance on specific areas:

- `references/legal-standards.md` — FRCP/FRE rules, ethics of witness preparation, privilege, anti-hallucination guardrails for legal authorities, malpractice risk areas
- `references/witness-types.md` — Detailed adaptations for defending depositions, 30(b)(6) corporate reps, expert witnesses, and apex witnesses
- `references/jurisdiction-adaptations.md` — State-specific variations (CA, TX, NY), time limits, objection practice, expert standards
- `references/quality-checklist.md` — Full self-audit checklist for the final package
