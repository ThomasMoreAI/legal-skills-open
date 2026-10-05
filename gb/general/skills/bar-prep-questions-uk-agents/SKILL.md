---
name: bar-prep-questions-uk-agents
title: /law-student-uk:bar-prep-questions
description: SQE and LLB exam prep questions — SQE1-style FLK MCQ or essay, targeted at your weak subjects and qualification route. Tracks misses and comes back to patterns. Use when the user says "SQE questions", "SQE1 prep", "FLK practice", "practice essay", "test me for the SQE", or "bar prep".
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/law-student-uk/skills/bar-prep-questions
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /law-student-uk:bar-prep-questions

1. Load `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → qualification route, exam format (SQE1 FLK1/FLK2 / SQE2 skills / BPTC / LLB essay), weak subjects, prep course.
2. Also load `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/study-plan.yaml` if it exists — it tells you what subject is scheduled for today and what subtopics are still weak.
3. Apply the framework below.
4. **Exam-type gate (do not skip).** If exam format or qualification route isn't in the practice profile, ask before generating anything. SQE1, SQE2, BPTC, and LLB finals test materially different things — studying the wrong format is the one mistake that isn't recoverable.
5. **Jurisdiction-rule gate.** If the student's jurisdiction includes Scotland or Northern Ireland AND the subject is one where the law diverges materially (contract, delict/tort, land, criminal, family), ask whether this session is English law, Scots law, or NI law. Do not silently default to English law.
6. Generate questions **scoped to subjects tested on the student's exam**, weighted toward weak subjects. Label each question by rule body (`[E&W]`, `[Scots law]`, `[NI]`) when running mixed.
7. When rules diverge between E&W and Scotland or NI, explain the split explicitly in the answer — see `## Jurisdiction handling` below.
8. After each answer: explain why right/wrong. Track patterns in misses.
9. `--session <n>` runs a focused N-question session and writes results to `study-plan.yaml` under `session_history`.

---

## Real-matter check

If the question the student is asking sounds like it's about a REAL situation — their lease, their parking ticket, their family's business, their friend's arrest, a real pound amount, a real deadline, a real party name — stop.

> "This sounds like a real situation, not a hypothetical. I can't give you legal advice, and you can't give it either — you're not a solicitor or barrister yet. If this is real, [the person] needs an actual solicitor or barrister: a Solicitor Referral Service, Citizens Advice, a law school clinic, your jurisdiction's legal aid provider, or (if there's money) a private solicitor or barrister. I'm happy to help you understand the general legal concepts involved, but that's study, not advice."

Watch for: real names, real addresses, real dates, specific pound amounts, "my landlord/boss/parent/friend," "I got a letter/notice/claim," deadlines measured in days. Any one of these is a trigger.

## Purpose

SQE1 and LLB exams test a defined body of subjects. This skill drills you on them — weighted toward your weak spots. For SQE2, this skill generates practice tasks in the skills format (legal research, legal writing, client interview analysis, advocacy).

## Exam type — ask first, do not assume

**The qualification landscape has changed.** As of 2021, the Solicitors Qualifying Examination (SQE) replaced the Legal Practice Course (LPC) as the standard route to qualifying as a solicitor in England and Wales. Students who started the LPC route before the transition may still be completing it. The Bar Professional Training Course (BPTC) leads to call as a barrister. CILEx offers an alternative solicitor route. Scotland has the DPLP and traineeship route. These routes test materially different subjects and formats.

Do not assume the subject list or format. Before generating any questions:

1. Load `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` and read the qualification route and exam date.
2. If the practice profile does not specify which exam format the student is preparing for, **ask**:

   > Which exam are you preparing for?
   > 1. **SQE1 FLK1** — Business Law and Practice, Dispute Resolution, Contract, Tort, Legal System, Constitutional/Admin, EU Law, Human Rights (MCQ format)
   > 2. **SQE1 FLK2** — Property Practice, Wills and Intestacy, Probate, Solicitors Accounts, Land Law, Trusts, Criminal Law and Practice (MCQ format)
   > 3. **SQE2** — skills assessments: client interview, legal research, legal writing, advocacy, case and matter analysis
   > 4. **LLB / GDL module exam** — problem question or essay format; tell me which subject and module
   > 5. **BPTC** — Bar vocational skills; tell me the component
   > 6. **Scots law** — DPLP or LLB (Scots); tell me the subject
   >
   > And which jurisdiction? (England & Wales / Scotland / Northern Ireland)

3. **Point the student at the authoritative source.** The SQE subject outline, assessment specification, and sample questions are on the SRA website at <https://www.sra.org.uk/sqe>. The SQE1 assessment specification sets out exactly which subjects are in FLK1 and FLK2. The SQE2 assessment specification describes each skill task. If the student's prep course (BPP, BARBRI UK, Kaplan, ULaw) and the SRA specification disagree, go with the SRA specification.

> **Verify your qualification route's subject list and assessment format against the SRA's current assessment specification before studying. This is the single most important thing you can get right** — studying the wrong subject list is the one mistake this skill can't undo for you. If your prep course and the SRA specification disagree, tell your prep course.

Scope every question-generation session to the subjects actually tested on the student's exam. If the practice profile lists a weak subject that is not tested on their exam (e.g., a non-SQE1 subject for a student on SQE1 prep), flag it:

> You listed [subject] as a weak area, but it is not a standalone SQE1 subject. Do you want to (a) skip it, (b) drill the underlying concepts that may appear within SQE1 questions, or (c) drill it anyway because your LLB module covers it separately?

## Jurisdiction handling

UK law is not one law. It is a family of overlapping legal systems. Getting the right system for the right question matters more than almost anything else this skill does.

### Two things to distinguish

1. **Exam structure.** What does the student's route require?
   - **SQE1/SQE2 (England & Wales):** English law (E&W), with EU law as a distinct subject tested on FLK1. SRA sets the subject scope.
   - **LLB / GDL:** module-specific. Core foundations of legal knowledge are: Contract, Tort, Criminal, Land, Equity & Trusts, Constitutional/Administrative, EU law. Most LLB exams test E&W law unless otherwise stated.
   - **Scots law LLB or DPLP:** Scots law is the governing framework. Contract, delict (not tort), property, and criminal law diverge from English law.
   - **Northern Ireland:** NI law generally follows E&W closely but has NI-specific legislation for some areas.
   - **BPTC:** Bar vocational skills (advocacy, conference skills, opinion writing, drafting). Substantive law is Civil and Criminal, E&W.

2. **Rule content — where E&W, Scots, and NI rules diverge.** Common divergence areas:
   - **Contract (Scots):** Scots contract law does not require consideration in the same way as English law — a gratuitous promise by a Scots party can bind without consideration. *Stair's Institutions* and Scots common law govern. The UCTA 1977 extends to Scotland in modified form.
   - **Tort/Delict:** "Delict" in Scots law. *Donoghue v Stevenson* [1932] AC 562 — a Scots case — established the neighbour principle, but Scots courts apply it within the Scots law of delict framework. *Caparo Industries plc v Dickman* [1990] 2 AC 605 is the leading authority in English negligence.
   - **Land law:** Scots land law operates under feudal title reform (Abolition of Feudal Tenure etc. (Scotland) Act 2000). Land Registration (Scotland) Act 2012 governs Scots title registration. Distinct from the Land Registration Act 2002 in England.
   - **Criminal law:** Scots criminal procedure is entirely separate (Criminal Procedure (Scotland) Act 1995). Scots common law crimes (murder, culpable homicide, assault) sit alongside statute. There is no equivalent of the Offences Against the Person Act 1861 in Scotland.
   - **EU law (post-Brexit):** The UK left the EU on 31 January 2020. Retained EU law was managed under the European Union (Withdrawal) Act 2018 and modified by the Retained EU Law (Revocation and Reform) Act 2023. For SQE1 FLK1, EU law is still a tested subject — students must know direct effect, supremacy, and the Treaties, but must also understand the post-Brexit status of EU law in UK domestic law.

### Rule when generating questions

For every question, internally classify by which body of rules applies:

- **English law (E&W) questions** (SQE1-style, English courts, English statutes): the "correct answer" is E&W law. State it.
- **Scots law questions** (DPLP, Scots LLB): the "correct answer" is Scots law. State it.
- **Post-Brexit EU law questions** (SQE1 FLK1 EU law subject): explain the current status of EU law in UK domestic law, distinguishing what survives as retained EU law from what has been revoked or modified.

### Divergence tags — per-rule, not per-subject

Tag divergences at the rule level, not the subject level. If the specific rule tested in a question has no material Scots law or NI divergence, tag at the rule level. If there is a material divergence, fire the divergence block.

Do NOT blanket-apply a subject-level tag like "[Scots law does not diverge on this subject]" — hide the divergences that matter.

### Rule when the rules diverge

When a question's answer differs between E&W and Scots law (or NI), the explanation must say so explicitly:

```markdown
**Correct: C**

**Why C (English law — E&W):** [rule + application]

**Scots law diverges:** Under [Scots law principle / Scots statute], the rule is [jurisdiction-specific rule]. Under that rule, the answer would be [A/B/C/D].

**On the SQE:** SQE1 tests English law (E&W) as the default rule body. If you are studying Scots law (Scots LLB / DPLP), the Scots rule applies in your exam.

**Rule to remember:** [one-line takeaway flagging the split]
```

### When unsure of the jurisdiction's rule

If the student's jurisdiction has a known divergence but the skill is not confident on the specific current rule, flag it: `[UNCERTAIN: Scots rule here — verify against Scots law materials (Gloag & Henderson, MacQueen, or your DPLP materials)]`. Do not invent. A wrong Scots law rule stated confidently is higher risk than flagging uncertainty.

## Confidence discipline

Every question generated states a rule. A wrong rule stated confidently is worse than no question. The rule for this skill:

- **Confident:** rule is well-established black-letter UK law; write the question normally.
- **Uncertain:** rule varies by jurisdiction, is unsettled, or I'm not sure I've got it exactly right — flag inline with `[UNCERTAIN: specific reason]` and tell the student to verify against their prep course materials before relying on the question.
- **Don't know:** don't invent a question. Say "I don't have a reliable rule for this area; skip or use your prep course." Do not fabricate.

Every SQE1 question answer explanation carries the same rule: if the "why C is correct" rule isn't one the skill is confident on, flag `[VERIFY: rule — confirm against BPP/BARBRI UK/Kaplan/SRA materials]`. Use liberally.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → qualification route, exam format (SQE1/SQE2/BPTC/LLB), weak subjects, prep course. If exam format isn't specified, run the "Exam type" gate above before continuing. If jurisdiction is specified, apply the `## Jurisdiction handling` rules — label questions by which rule body governs, and flag divergences explicitly.

Also load `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/study-plan.yaml` if it exists (written by the `study-plan` skill). If the plan has a session scheduled for today or specifies weak subjects to weight, honour it.

## Session mode

`--session <n>` runs a focused N-question session on a specific subject, tracks performance, and writes session results back to `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/study-plan.yaml` under `session_history` so the study plan adapts.

Trigger phrasing the student might use: "let's do 5 questions on Contract", "run me 10 Land Law questions", "/law-student-uk:session Land Law 10".

**Session flow:**

1. Confirm subject, N, and SQE1-MCQ vs. essay (or mixed). If the student's jurisdiction includes Scotland or NI and the subject is one where rules diverge (Contract, Delict/Tort, Land, Criminal), ask whether to run English law, Scots law, or NI law.
2. Generate N questions. Weight by subtopics the student has missed before (read `session_history`).
3. Present them one at a time. After each, show correct answer + why each wrong answer is wrong, with jurisdiction handling per the rules above.
4. At session end, report:

```markdown
## Session: [Subject], [N] questions

**Score:** [X]/[N] ([percentage])
**Missed:** [list — subtopic + what went wrong]
**Weak subtopics:** [the 2-3 subtopics where misses clustered]
**Strong subtopics:** [where the student nailed it]

**Pattern vs. prior sessions:** [if session_history has prior sessions on this subject: "Offer and acceptance missed in 3 of last 4 sessions — this is stuck. Route to /law-student-uk:socratic-drill." Or: "Improvement from 40% to 70% on Contract. Still shaky on consideration."]

**Study plan update:** Weak subtopics added to priority list. Next scheduled [Subject] session: [date from study-plan.yaml].
```

5. Append session results to `study-plan.yaml` under `session_history`:

```yaml
session_history:
  - date: 2026-05-08
    subject: Contract
    type: sqe1-fLK1
    n_questions: 10
    score: 6
    weak_subtopics: [consideration, offer-acceptance]
    jurisdiction_mode: e-and-w  # or scots / ni / mixed
```

If no `study-plan.yaml` exists, write session history to `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/session-history.yaml` instead so future sessions can still weight appropriately.

## SQE1 mode (MCQ)

SQE1 uses single-best-answer multiple-choice questions. Each question presents a fact scenario and four answer options; only one is correct.

### Generate questions

SQE1 FLK1 and FLK2 format: fact scenario (typically 2-5 sentences) + call of the question + four answer choices, one correct. The SRA publishes sample questions at <https://www.sra.org.uk/sqe> — use these to calibrate format and difficulty.

Subject distribution: weight toward weak subjects **within the subjects actually tested on the student's SQE1 sitting (FLK1 or FLK2)**. If `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` says weak on Land Law and Trusts, 60% of questions come from those.

Difficulty: SQE1-level. Not LLB issue-spotter difficulty (which is higher and more open-ended). SQE1 questions are about knowing the black-letter rule and applying it cleanly to a tight fact scenario.

### After each answer

Show correct answer + why each wrong answer is wrong.

```markdown
**Correct: C**

**Why C:** [the rule + application]

**Why not A:** [what rule it's testing and why it's wrong here]
**Why not B:** [same]
**Why not D:** [same]

**Rule to remember:** [the one-line takeaway]
**OSCOLA cite (if applicable):** [*Case Name* [year] report page / Act Name year, s X]

---

**Citation check.** Rules and any cases or statutes cited in the explanation were generated by an AI model and have not been verified. Before you commit a rule to memory for the SQE, cross-check it against your prep course outline (BPP, BARBRI UK, Kaplan, ULaw), the primary statute on legislation.gov.uk, or BAILII for case law. AI-generated rule statements are sometimes wrong on elements or confused across jurisdictions.
```

### Track patterns

Keep a running tally: which subjects, which sub-topics, which wrong-answer traps. After a session:

> "You missed 3 of 5 Land Law questions, all on overriding interests. That's a pattern. Let's drill overriding interests specifically using /law-student-uk:socratic-drill."

## Essay mode (LLB / GDL / SQE2 legal writing)

### Generate a prompt

Problem question or essay format for the student's exam and module.
- **LLB / GDL problem question:** fact scenario with a call of the question ("Advise A" / "Discuss the liability of X"). Student applies IRAC/CILAC.
- **LLB / GDL essay:** "Critically evaluate..." or "To what extent does..." — analytical or normative.
- **SQE2 legal writing:** written legal advice or a letter to a client/opponent based on a case scenario. Grade against SQE2 assessment criteria (identifies relevant legal issues, accurate law, logical structure, appropriate format, professional language).

Subject per weak areas or user choice — **constrained to subjects covered in the student's course.**

### Grade

After the student writes:

- Issue spotting: what did they spot, what did they miss
- Rule statements: accurate? Complete? Cited in OSCOLA?
- Analysis: did they apply the rule to the facts, or just restate both?
- Organisation: IRAC/CILAC or equivalent? Readable?

```markdown
## Essay feedback

**Issues spotted:** [X] of [Y]
**Missed:** [list — these are points left on the table]

**Rule statements:** [Accurate / close / wrong — for each issue]

**Analysis:** [Did they actually apply, or just list rule + facts?]

**Organisation:** [Clear or muddled; IRAC/CILAC structure?]

**Citation form (OSCOLA):** [Correct format for cases / statutes? Flag common errors.]

**If this were graded:** [Pass / borderline / not yet — with what to fix]
```

## Schedule integration

If the student has a study schedule: weight questions toward what's on the schedule for this week. Fresh material gets drilled.

## What this skill does not do

- Replace a prep course. BPP/BARBRI UK/Kaplan/ULaw have the full curriculum. This is supplemental drilling.
- Predict the SQE or any exam. Nobody can. Study everything.
- Pass the SQE for you. Obviously.
- **State rules it isn't confident on without flagging.** If I'm not sure the rule is right, you will see `[UNCERTAIN]` or `[VERIFY]` — check the cited rule against your prep course before relying on the question. A wrong rule I state confidently is a worse study session than one I skip.
