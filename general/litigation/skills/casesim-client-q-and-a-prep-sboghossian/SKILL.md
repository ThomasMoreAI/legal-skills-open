---
name: casesim-client-q-and-a-prep-sboghossian
title: Client Q&A Prep — Deposition, Witness Statement, and Mediation Coaching
description: Use when an attorney needs to prepare a client for a deposition, witness statement, mediation session, or court testimony. Coaches the attorney through building a question bank from the case file, scoring question difficulty, running roleplay rehearsal (with Louis playing opposing counsel), critiquing answer quality, and running a final stress-test under interruption and time pressure. Covers privilege boundaries, conflicting evidence, and personal weak points. Produces a question bank, answer-coaching notes, and rehearsal log.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/casesim/casesim-client-q-and-a-prep
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Client Q&A Prep — Deposition, Witness Statement, and Mediation Coaching

## When to use this

Invoke when:
- An attorney is preparing a client for a deposition
- A client is submitting a witness statement and needs to be ready for follow-up questioning
- A party is attending a mediation where they will be questioned by the mediator or opposing counsel
- A client is testifying in court or before a tribunal (civil or commercial)
- An attorney wants to rehearse a client's narrative before a settlement negotiation

**Jurisdictional applicability:** deposition procedures vary significantly by forum. The US adversarial deposition model differs from Lebanese civil procedure (where pre-trial witness examination is limited), DIFC arbitration (where witness statements are primary and cross-examination at hearing is more constrained), and KSA Commercial Court practice. Calibrate the coaching intensity and procedure to the actual forum.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Case summary / key facts | Yes | Who are the parties, what is the dispute, what happened? |
| Client's role | Yes | Fact witness, party witness, expert witness |
| Forum | Yes | Deposition (US), DIFC arbitration, Lebanese court, mediation, etc. |
| Key documents | Recommended | Contracts, emails, prior statements, relevant records |
| Privilege scope | Recommended | Attorney-client and work-product boundaries for this client |
| Known weak points | Optional | Prior testimony, social media, conflicts of interest, prior inconsistencies |
| Opposing counsel profile | Optional | Firm, known style, prior cross-examination patterns |

## Process

### Step 1: Build the Question Bank

From the case file, Louis constructs a question bank organized by topic:

**Opening narrative questions** (always appear; shape how the client frames themselves):
- "Tell me about yourself and your role at [company]."
- "Walk me through your involvement in [key event]."
- "How long have you worked there, and who did you report to?"

**Key fact questions** (derived from the specific facts):
- What the client directly observed vs. was told vs. inferred
- Source of knowledge for each material fact ("how do you know that?")
- Documents the client authored, received, forwarded, or was copied on

**Conflicting evidence questions** (where the record shows inconsistency):
- Prior emails that seem to contradict the client's current position
- Statements made in earlier depositions or declarations
- Social media posts or external communications relevant to the matter

**Documents under attack** (specific documents likely to be put to the client):
- For each: who drafted it, what does it mean, what was the client's state of mind

**Privilege boundary questions**:
- Questions designed to pierce attorney-client privilege (indirect approaches)
- Questions designed to discover work product
- The client must know how to respond without inadvertently waiving privilege (redirect to counsel, do not explain privileged communications)

**Personal weak points**:
- Prior testimony in other proceedings
- Social media activity during the relevant period
- Conflicts of interest or financial interests relevant to the case
- Credibility vulnerabilities (prior conviction, prior inconsistent statement on an unrelated matter)

### Step 2: Score Question Difficulty

Each question is scored 1–5:
- **1 (Routine):** Uncontroversial facts the client knows well
- **2 (Attention required):** Facts requiring precise language; small errors matter
- **3 (Significant):** Documents or events where the record could be read multiple ways
- **4 (High-risk):** Questions designed to create or exploit inconsistency; privilege boundary proximity
- **5 (Critical):** Questions that go directly to the heart of liability or credibility; a bad answer here is case-changing

Focus rehearsal time on Level 3–5 questions.

### Step 3: Roleplay Rehearsal

Louis plays opposing counsel. Behavioral modes:
- **Baseline:** professional, methodical questioning as a competent but not aggressive counsel
- **Pressure mode:** interrupts frequently, asks compound questions, uses silence as a tool
- **Aggressive mode:** raised stakes, leading questions, attempts to get the client to commit to damaging positions

The attorney directs which mode to use and when to escalate.

**Coaching focus areas** during rehearsal:
- **Rambling:** client gives too much information; answers go beyond what was asked
- **Speculation:** client answers what they think must have happened rather than what they know
- **Volunteering:** client introduces new information that was not asked for
- **Imprecision:** client uses approximations ("around," "maybe," "I think") on facts that are documentable
- **Hedging when clarity is needed:** over-qualified answers on simple documented facts look evasive

### Step 4: Critique and Refine

After each answer, Louis provides structured feedback:
- What was strong (accurate, concise, appropriately limited to knowledge)
- What needs adjustment (and why: volunteered, speculative, over-explained, inconsistent with document X)
- Suggested rephrase (if the answer structure, not the fact, is the problem)

The attorney and client iterate until the answer set is stable.

### Step 5: Stress Test

Final rehearsal run:
- Full simulated session at speed with time pressure (limited minutes per question set)
- Random interruption ("wait — you said earlier… [invented inconsistency]") to test whether the client handles pressure calmly
- Back-to-back difficult questions without breaks

The attorney reviews the stress-test log and decides whether more prep is needed.

## Output

At the end of each session Louis produces:
1. **Question bank** (full list, scored by difficulty, with notes)
2. **Answer coaching notes** (per question: what to say, what to avoid, how to respond to follow-ups)
3. **Rehearsal log** (timestamped record of questions asked, answers given, coaching notes applied)

## Hard limits

Louis will not:
- Coach a client to fabricate facts or give knowingly false testimony
- Help a client conceal documents that are subject to disclosure obligations
- Draft scripts that instruct the client to misrepresent their knowledge or memory
- Advise a client to hide or destroy evidence

If a user request crosses these lines, Louis declines and explains why.

## Jurisdictional notes

| Forum | Key preparation differences |
|---|---|
| US Deposition | Broad scope; counsel can object but client must answer unless privilege; video-recorded; transcript binding |
| DIFC / LCIA Arbitration | Witness statement primary; oral examination at hearing is more constrained; tribunal controls the process |
| Lebanese Civil Court | Oral examination by judge rather than by parties; preparation focuses on judge's likely questions rather than counsel's |
| KSA Commercial Court | Written evidence primary; oral testimony limited; preparation focuses on written statement accuracy |
| Mediation | Non-compulsory; client should be prepared for the mediator's probing questions and for informal dialogue with the opposing party |

## Related skills

- [[casesim-cross-examination-rehearsal]]
- [[casesim-judge-bench-perspective]]
- [[casesim-opposing-counsel-simulator]]
- [[casesim-fact-pattern-builder]]
- [[academy-litigation-game-coach]]
