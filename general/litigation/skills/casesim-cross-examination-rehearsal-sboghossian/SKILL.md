---
name: casesim-cross-examination-rehearsal-sboghossian
title: Cross-Examination Rehearsal — Build, Practice, and Score Your Cross
description: Use when an attorney needs to build and rehearse a cross-examination of a witness — identifying prior inconsistent statements, generating leading-question sequences, mapping impeachment opportunities, and preparing for non-cooperative witnesses. Louis plays the witness in cooperative, hostile, or evasive modes with realistic memory failures and lawyer-coached cleanups. Produces a cross outline, impeachment files, and a scoring rubric. Applies across DIFC, ADGM, UAE civil, Lebanese, KSA, and international arbitration forums.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/casesim/casesim-cross-examination-rehearsal
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Cross-Examination Rehearsal — Build, Practice, and Score Your Cross

## When to use this

Invoke when:
- An attorney is preparing to cross-examine a fact witness in trial or arbitration
- An attorney needs to identify and organize prior inconsistent statements for impeachment
- A litigation team wants to rehearse a cross before a hearing
- A junior litigator is learning cross-examination technique (see also [[academy-litigation-game-coach]])
- An advocate needs to plan a cross in a forum with constrained cross-examination rights (e.g., KSA, Lebanese civil courts)

## Inputs

| Input | Required | Notes |
|---|---|---|
| Witness identity and role | Yes | Fact witness, expert witness, party witness |
| Prior statements | Yes | Deposition transcripts, affidavits, witness statements, social media posts |
| Case theory | Yes | The point the cross is meant to advance or establish |
| Trial / hearing context | Yes | Forum, scheduled time allocation for cross |
| Expert report (if expert) | Recommended | Full report; opposing expert's report if available |
| Witness profile | Optional | Known demeanor, prior testimony in other matters, counsel who prepared them |

## Process

### Step 1: Identify Prior Inconsistent Statements

Louis reviews all available prior statements and identifies:
- Factual inconsistencies between the witness's current statement and prior testimony
- Omissions in the current statement of facts the witness previously confirmed
- Internal inconsistencies within the same statement
- Inconsistencies with documentary evidence (emails, contracts, records)
- Social media posts or public statements that contradict the formal position

Output: an **inconsistency matrix** — two columns (prior statement vs. current position) with source references and severity rating.

### Step 2: Generate the Cross Outline

Cross-examination design follows a disciplined structure:
- **Credit attacks first** (establish witness credibility issues early, before substance)
- **Document-control sequences** (get witness to confirm a document is authentic and what it says before using it)
- **Closed loops** (leading questions that lock the witness into a position before the impeachment lands)
- **Impasse questions** (questions where either answer helps the cross-examiner)
- **Final commitment** (confirm the central concession before moving on)

Louis generates a sequenced cross outline in this format:
```
Topic: [Subject area]
Goal: [What we want the jury/tribunal to understand after this topic]
Q1: [Leading question — establishes foundation]
Q2: [Leading question — advances position]
Q3: [Leading question — locks in commitment]
[DOCUMENT: Exhibit X] "Let me show you Exhibit X. You wrote this email on [date], correct?"
Q4: [Leading question — confronts with document]
Q5: [Closing the loop — gets the concession]
```

### Step 3: Prepare Contingencies for Non-Cooperative Witnesses

Some witnesses will not give clean answers. Louis maps the main evasion tactics and prepares responses:

| Witness tactic | Attorney counter |
|---|---|
| "I don't recall" on a documented fact | "But you wrote this email, correct? Would you like me to show it to you?" |
| Explaining instead of answering | "My question was simply yes or no: did you [do X]?" |
| Introducing new facts | "I'll address that in a moment — my question was [repeat]" |
| Attacking the question | "If the question is unclear, tell me — would you like me to rephrase?" |
| Lawyer-coached cleanup on re-direct | Prepared follow-up questions that lock in the cross concessions before redirect can undo them |

### Step 4: Time Budget

Each witness cross is time-allocated. Louis divides the outline into timed segments:
- Credibility / background (typically 10–15% of time)
- Core fact disputes (60–70%)
- Concession/damages/remedies topics (15–20%)
- Reserve for unexpected developments (buffer)

Louis flags if the outline has more material than the allocated time and recommends cuts.

### Step 5: Rehearsal — Louis Plays the Witness

Three witness modes:

**Cooperative mode:** The witness is honest and responsive but has been well-prepared. They give technically accurate answers that are as favorable to their side as possible. Tests whether the cross outline extracts concessions from a fully prepped witness.

**Hostile mode:** The witness is actively resistant. They argue with questions, give long non-responsive answers, and try to rehabilitate themselves at every opportunity. Tests whether the attorney can maintain control.

**Evasive mode:** The witness uses plausible-deniability language throughout: "to the best of my recollection," "I may have," "I believe." Tests whether the attorney can pin down evasive witnesses on documented facts.

Realistic memory failures are built in: the witness may not remember the date of a meeting but remembers the substance; they may remember signing a document but not what was discussed. These mirror real deposition and trial experience.

## Scoring rubric

After each rehearsal session:

| Criterion | Weight | What it measures |
|---|---|---|
| Control maintenance | 30% | Did the attorney keep the witness to the question? Were long answers cut off appropriately? |
| Concession extraction | 25% | How many of the planned concessions were secured? |
| Impeachment technique | 20% | Were inconsistencies confronted effectively? Was the document-control sequence used correctly? |
| Loop construction | 15% | Were closed loops properly constructed so the witness could not escape? |
| Time discipline | 10% | Did the attorney stay within time allocation and prioritize high-value topics? |

## Output

1. **Cross outline** (full question sequence organized by topic with goals and notes)
2. **Inconsistency matrix** (prior statement vs. current position, with sources)
3. **Impeachment files** (one per inconsistency: prior statement excerpt, current statement excerpt, recommended question sequence)
4. **Scoring rubric** (post-rehearsal performance assessment)

## Jurisdictional notes

| Forum | Cross-examination approach |
|---|---|
| US Federal / State Court | Wide latitude; leading questions standard; impeachment with prior inconsistent statements by reference to transcript |
| DIFC / ADGM Courts | English commercial court style; witness statement primary; cross at oral hearing more focused; tribunal may limit scope |
| ICC / DIAC / LCIA Arbitration | Witness statement primary; cross constrained by IBA Rules on Evidence where adopted; time limits strict |
| Lebanese Civil Court | Judge-centric; parties examine through the judge; direct adversarial cross is limited; preparation focuses on written submissions and interrogatories |
| KSA Commercial Court | Written evidence primary; oral testimony limited; cross in the Western sense rarely occurs |

Adapt technique to the forum: a comprehensive leading-question cross outline designed for a US trial will not work in a KSA commercial court setting.

## Related skills

- [[casesim-client-q-and-a-prep]]
- [[casesim-judge-bench-perspective]]
- [[casesim-opposing-counsel-simulator]]
- [[casesim-fact-pattern-builder]]
- [[academy-litigation-game-coach]]
