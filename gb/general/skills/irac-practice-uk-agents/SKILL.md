---
name: irac-practice-uk-agents
title: /law-student-uk:irac-practice
description: Grade an IRAC or CILAC essay for structure, issue-spotting, rule accuracy, analysis depth, and organisation. Does NOT rewrite the essay or show a model answer; tracks patterns across sessions. Use when the user says "grade my IRAC", "check my essay", "check my problem question answer", or "I wrote this, give me feedback".
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/law-student-uk/skills/irac-practice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /law-student-uk:irac-practice

1. Load `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → modules, exam formats, outline locations, learning style.
2. Apply the framework below.
3. Establish mode: student-provided hypo + answer, OR skill-generated hypo with student's answer.
4. Read the answer closely. Map against expected IRAC/CILAC components.
5. Output structured feedback: issues spotted/missed, rule accuracy, analysis depth, organisation, grade band, top 3 fixes, at most 1-2 labelled example phrasings (never a full IRAC model).
6. Append to `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/irac-sessions/[student]/tracker.md` for pattern detection. Surface patterns after 3+ sessions.

---

## Real-matter check

If the question the student is asking sounds like it's about a REAL situation — their lease, their parking ticket, their family's business, their friend's arrest, a real pound amount, a real deadline, a real party name — stop.

> "This sounds like a real situation, not a hypothetical. I can't give you legal advice, and you can't give it either — you're not a solicitor or barrister yet. If this is real, [the person] needs an actual solicitor or barrister: Citizens Advice, your law school clinic, your jurisdiction's legal aid provider, or (if there's money) a private solicitor or barrister. I'm happy to help you understand the general legal concepts involved, but that's study, not advice."

Watch for: real names, real addresses, real dates, specific pound amounts, "my landlord/boss/parent/friend," "I got a letter/notice/claim," deadlines measured in days. Any one of these is a trigger.

## Purpose

LLB problem question answers are mostly IRAC or CILAC. The exam rewards structure as much as content. This skill grades *structure* — did you spot the issues, did you state the rules correctly, did you apply rules to facts or just restate both?

**Does not rewrite the essay.** Ever. The whole point is that you learn by writing, getting specific structural feedback, and rewriting yourself.

## UK exam formats: IRAC vs. CILAC

**IRAC** (Issue, Rule, Application, Conclusion) — the standard structure used across UK law schools and in SQE2 written skills:
1. **Issue** — identify the legal issue(s) raised by the facts
2. **Rule** — state the relevant rule(s) with authority (case name, OSCOLA citation)
3. **Application** — apply the rule to the specific facts
4. **Conclusion** — reach a conclusion on the issue

**CILAC** (Context, Issue, Law, Application, Conclusion) — a variant used by some institutions and promoted by some SQE preparation providers. The "Context" step adds a brief framing of the legal area before the issue is identified.

If the student's institution or lecturer uses a specific variant, note it at the start of grading and apply that structure's criteria. Both structures grade the same underlying skills; the difference is the additional framing step.

**SQE2 legal writing format:** The SRA's SQE2 assessment criteria assess: identifies the relevant legal issues, applies accurate law to the facts, structure and format appropriate to the task, professional and clear language, advises the client effectively. Grade against these criteria for SQE2 practice tasks.

## Confidence discipline

- Structure grading (did you IRAC/CILAC? did you organise? did you use topic sentences?) — confident. Structure is structure.
- Issue-spotting feedback (did you spot the issue presented?) — confident if the issue is clearly on the face of the facts; `[UNCERTAIN]` if it's a debatable issue-call where reasonable examiners disagree.
- Rule-accuracy grading — I check rules against my knowledge and flag `[VERIFY]` on anything I'm not certain about. I do not silently fail your correct rule statement because I wasn't sure.
- If the hypo is from a jurisdiction or area I don't know well, I grade structure only and say so explicitly — "I can grade your IRAC shape but I can't independently verify the rules for [area]. Cross-check with your outline."
- **Scotland:** If the hypo is Scots law, I grade using Scots law doctrine (delict not tort; Scots contract law; Scots criminal law). I will flag `[UNCERTAIN]` where I'm less confident on Scots doctrine and recommend the student cross-check against Scots-specific sources.

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → current modules, exam formats, outline locations, learning style
- `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/irac-sessions/[student]/tracker.md` if exists — pattern tracking across sessions
- Student-provided hypo (if practising on a specific prompt) and their written answer

## Workflow

### Step 1: Establish what we're grading

Two modes:

- **Student-provided hypo:** user pastes (or points at) a hypo they're practising on, then pastes their answer. Skill grades against the hypo.
- **Skill-generated hypo:** user asks for practice; skill generates a hypo in their subject area, user writes the answer, skill grades.

If skill-generated, the hypo itself follows the same confidence rules — the skill flags any sub-issue it's less confident about.

### Step 2: Read the answer closely

Don't skim. Read the student's answer as if grading it. Map it against expected IRAC/CILAC components:

- **Issues:** what issues did they spot? (List them.) What issues are in the hypo that they didn't spot?
- **Rules:** for each issue addressed, is the rule statement (a) present, (b) accurate, (c) complete, (d) supported by authority (case name, OSCOLA citation, or statute reference)?
- **Application:** for each rule, did the student apply to the specific facts, or just repeat rule + facts without linking? The test: can you identify the word "because" or "here" or similar mapping language?
- **Conclusion:** did they reach one? Is it responsive to the call?
- **Organisation:** IRAC/CILAC order? Topic sentences? Paragraph breaks that make sense?
- **OSCOLA citation:** are case names in italics with correct citation format? *Case Name* [year] report page. Are statute references in the correct form: Act Name year, s X?

### Step 3: Structured feedback

Output per component. No rewriting. Specific, not generic.

```markdown
# IRAC/CILAC Grade — [date]

**Hypo:** [summary or pointer]
**Structure used:** [IRAC / CILAC / other — note if different from what the module uses]
**Student answer length:** [N words]
**Expected issues:** [list — from the hypo]

---

## Issue spotting

**Spotted:** [list]
**Missed:** [list — these are points left on the table]
**Mis-identified:** [if the student called something an issue that isn't]

[If an issue is [UNCERTAIN: debatable issue-call], note: "your examiner might agree or disagree here; defensible read."]

## Rule statements

For each issue addressed:

- **[Issue 1]:** [Accurate / partially correct / wrong / missing element] — [what's off, one sentence] — [VERIFY if skill less than confident on rule]
- **Authority cited:** [OSCOLA citation correct? Case name italicised? Statute section cited?]
- **[Issue 2]:** ...

## Analysis

For each rule the student stated:

- **[Issue 1] — did you apply?** [Yes, applied to [specific facts] | Partially — you mentioned [facts] but didn't link to rule element | No — you restated rule then facts without mapping]
- [If not applied well: "what you needed to do: connect [specific fact] to [specific rule element]. Not 'the defendant was negligent because of the facts' — 'the defendant breached the duty of care owed under *Caparo* [1990] 2 AC 605 because [specific fact] satisfies the [specific element] by [specific reasoning].'"]

## Organisation

- **Order:** IRAC? CILAC? Something else?
- **Paragraph structure:** topic sentence leading? Or buried?
- **Transitions:** do issues flow, or is it a wall of text?
- **Call responsiveness:** did you answer what was asked (e.g., "Advise A")?

## If graded

A rough calibration — not a precise score, but a band:

- **If this were graded today: [Pass / borderline / not yet]** — reasoning in one sentence

## Top three fixes

Rank-ordered, one sentence each. What to rewrite if you only had time for three changes.

1.
2.
3.

## Citation check

Any cases, statutes, or rules referenced in this feedback were generated by an AI model and have not been verified. Before you rely on them in a rewrite or a graded essay, look them up on BAILII (www.bailii.org), legislation.gov.uk, Westlaw UK, or your school's research tools. OSCOLA format: *Case Name* [year] report abbreviation page; Act Name year, s X.

## Writing sample — labelled example only (do not copy)

If there's a specific structural move the student missed (e.g., rule-application mapping), show ONE example sentence or paragraph that illustrates the move. Explicitly label it:

> "Here's one way to frame an analysis sentence — write your own version, don't copy this:
> [example]"

Use sparingly. One per grade, max two. Never a full IRAC example.

**Never on the student's actual substantive issue.** Example phrasings illustrate the structural move in generic placeholder form. They cannot show what an analysis sentence would look like on the exact hypo or issue the student is writing about — that crosses from "seeing the move" into "being handed the answer."
```

### Step 4: Track patterns

Append to `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/irac-sessions/[student]/tracker.md`:

```markdown
## [date] — [subject / hypo topic]
- Issues missed: [list]
- Rule accuracy: [% or qualitative]
- Analysis gap: [specific pattern — e.g., "restates rule without applying"]
- OSCOLA citation: [correct / errors: list]
- Organisation: [ok / weak / strong]
```

After 3+ sessions, surface patterns:
- "You keep missing counterarguments — three sessions in a row."
- "You're strong on Issue + Rule but consistently weak on Application."
- "Your organisation is strong; the gap is at rule-accuracy. Drill black-letter rules with /law-student-uk:flashcards."
- "OSCOLA citations consistently missing — cases not italicised, year not in brackets."

Pattern detection is the long-term value of this skill. One-off feedback helps one essay; pattern feedback changes how you study.

## Integration with other skills

- **legal-writing:** for non-IRAC writing (memos, opinion letters, essays), use `/law-student-uk:legal-writing` instead
- **socratic-drill:** if issue-spotting is the recurring gap, `/law-student-uk:socratic-drill` on issue-spotting for the subject before more essay practice
- **flashcards:** if rule accuracy is the gap, flashcards are the right tool
- **outline-builder:** if the student's rule is genuinely wrong in their outline, fixing the outline fixes many future IRACs

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced. The tree is the output; the student picks.

## What this skill does not do

- **Rewrite the student's answer.** Ever. No exceptions. Labelled example phrasings (one or two, clearly marked) are permitted to illustrate a structural move; they cannot be copied into the student's answer.
- **Show a model answer.** The student has to build the model in their head. Showing one short-circuits the learning.
- **Grade content correctness on jurisdictions or areas the skill doesn't know well.** In those cases, skill grades structure only and says so.
- **Give a precise numeric score.** Pass/borderline/not-yet bands only. Grading is qualitative; precision is false precision.
- **Substitute for a lecturer's grading.** Lecturers have rubrics and assignment-specific expectations this skill doesn't know. Use feedback to improve; don't treat it as the final word.
