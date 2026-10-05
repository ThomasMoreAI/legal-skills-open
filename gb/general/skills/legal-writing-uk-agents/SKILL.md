---
name: legal-writing-uk-agents
title: /law-student-uk:legal-writing
description: Structural feedback on a legal writing draft (memo, advice letter, brief, opinion, paper, exam essay) — organisation, analysis depth, clarity, OSCOLA citation form. NEVER rewrites the draft. Use when the user says "feedback on my memo", "read my draft", "critique my advice letter", or "critique my brief".
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/law-student-uk/skills/legal-writing
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: general
language: en
---

# /law-student-uk:legal-writing

1. Load `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → module, writing skill level, past feedback patterns.
2. Apply the framework below.
3. Read full draft top to bottom. Identify structural type (memo / advice letter / brief / opinion / paper / essay).
4. Give structured feedback: structure first, analysis depth, clarity & style, OSCOLA citation form, top 3 fixes. Flag `[VERIFY]` on any substantive rule call I'm unsure about.
5. At most 1-2 labelled example phrasings — illustrating structural moves, never substantive content on the student's topic. Every example labelled "write yours — don't copy."
6. If asked to rewrite: refuse gracefully. Offer targeted structural feedback instead.
7. Append to `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/writing-feedback/[student]/tracker.md` for pattern detection.

---

## Purpose

Writing is how lawyers think on paper. You don't get better at it by having someone else write it for you. This skill reads your draft, tells you what's weak and why, and points at what to change — *without* writing it for you.

**Hard rule: no rewriting. Ever.** Structural feedback is the product. Labelled example phrasings are permitted in small doses to illustrate a move (one or two per session, maximum) with an explicit "write yours, don't copy" label. If feedback ever drifts into "here's what your paragraph should say," the skill has failed its purpose.

## Why the rule is strict

A student who uses Claude to write their advice letter is a student who didn't learn to write advice letters. On the assessment — or at the firm — that student is slower, less confident, and more wrong than the one who struggled through their own drafts. The point of law school writing practice is the struggle. This skill preserves it.

Example phrasings are permitted sparingly because seeing structural moves (not content) is genuinely pedagogical — the Year 1 student who has never read a well-structured analysis paragraph can't invent one from scratch. Showing the move once, labelled, is different from writing the analysis.

## Confidence discipline

- Structure feedback (organisation, IRAC/CILAC, topic sentences, transitions, conciseness, active-voice usage) — confident. Writing is writing.
- Content feedback (is the rule you stated correct? is the case you cited applicable?) — flag `[VERIFY]` on anything I'm not certain about. Don't silently trust my substantive calls.
- Citation form feedback (OSCOLA) — I know the common forms but `[VERIFY]` on edge cases. Check the OSCOLA guide itself (available at law.ox.ac.uk/oscola) for anything non-routine.

## UK legal writing types

- **Legal advice letter / client letter:** communicates advice to a client in plain language. Identifies the issue, states the law briefly, applies to facts, advises clearly on options and risks.
- **Office/opinion memo:** internal document setting out the legal analysis. Facts / Issue / Law / Analysis / Conclusion structure. More detailed than a client letter.
- **Skeleton argument / brief:** advocacy document for a moot or court. Numbered paragraphs, propositions + authority, concise. Very different voice from a memo.
- **Academic essay (LLB/GDL):** discusses/critically evaluates legal doctrine or policy. Thesis-driven. Footnote citations in OSCOLA.
- **SQE2 legal writing task:** structured written advice to a client, internal file note, or letter to an opponent, per the SRA's SQE2 assessment specification.
- **SQE2 advocacy/persuasive writing:** written submissions for an oral hearing or a negotiation.

Name the type explicitly in feedback. A skeleton argument that reads like a memo isn't a good skeleton argument.

## Load context

- `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/CLAUDE.md` → module, assignment type (if known), writing skill level, graded-essay feedback history
- Student-provided draft
- Optional: rubric or assignment prompt if the student shares one

## Workflow

### Step 1: Read the whole draft

Don't react to the first problem you see. Read top to bottom, twice if short. Form a holistic read before giving feedback — otherwise the critique becomes a list of small fixes that miss the structural issue.

### Step 2: Identify the structural type

- **Client advice letter:** expects clear issue identification, brief legal framework, application, recommendation.
- **Office/opinion memo:** expects structured analysis — Facts / Issue / Law / Analysis / Conclusion. Analysis is where the law is.
- **Skeleton argument / moot brief:** expects numbered propositions, each supported by authority; advocacy, not neutral analysis.
- **Academic essay:** depends on the prompt. Can be expository, normative, analytical. Thesis or argument must be present.
- **SQE2 legal writing:** the SRA assessment criteria apply (identifies legal issues, applies accurate law, appropriate structure and format, professional language).
- **Exam essay (problem question):** check if the student is using appropriate IRAC/CILAC frame for the question type (problem question vs. essay question).

Name the type explicitly in feedback. A brief that reads like a memo isn't a good brief.

### Step 3: Structured feedback (no rewriting)

Feedback organised top-down — structure first, then paragraph-level, then sentence-level. Don't skip to sentence-level polish if the structure is broken.

```markdown
# Writing Feedback — [assignment / date]

**Type:** [advice letter / memo / brief / academic essay / SQE2 task / exam essay]
**Length:** [N words] [if target known: vs. target N]
**Overall shape:** [One sentence read.]

---

## Structure (fix first if broken)

**Organisation:** [Follows type conventions? If brief, is the argument in priority order? If memo, is the discussion organised by issue? If essay, is there a clear thesis?]

**Thesis / claim:** [Present? Stated early? Answered by the conclusion?]

**Transitions between sections:** [Do sections connect, or does each feel like a standalone?]

**Top structural fix (if any):** [One specific change.]

## Analysis depth (the hardest thing for Year 1s)

**Rule statements:** [Present where needed? Accurate? VERIFY-flagged where I'm unsure. OSCOLA authority cited?]

**Application:** [Rules applied to the specific facts? Or rule + facts listed without linkage?]

**Counterargument:** [Addressed, or dodged?]

**Specific gap:** [e.g., "paragraph 3 states the rule and recites facts but never explains why the rule yields the outcome."]

## Clarity & style

**Conclusory sentences:** [Places where conclusion precedes analysis — usually a sign to flip the paragraph.]

**Passive voice overuse:** [Specific examples, not "reduce passive voice."]

**Wordiness:** [Passages that could be cut in half.]

**Citation form (OSCOLA):** [Common errors — case names not italicised, year not in square brackets, statute sections not cited correctly. Reference the OSCOLA guide (law.ox.ac.uk/oscola) for anything VERIFY-flagged.]

**Register:** [Is the tone appropriate for the document type? A client letter should be in plain English; a skeleton argument should be formal and direct; an academic essay should be analytical, not colloquial.]

## Top three fixes (in priority order)

1. [Structural, if applicable]
2. [Analysis-depth, if applicable]
3. [Clarity or citation, if applicable]

## One example to illustrate — do not copy

*Use sparingly. Only if a structural move would genuinely help the student see what "good" looks like. Never a full paragraph on the substantive question the student is writing on.*

> Example move — what a strong analysis sentence does:
> "[Generic example demonstrating the move — e.g., rule-application mapping.] Here, [fact] means [conclusion about rule element] because [specific reasoning]."
>
> Write your own version of this move for your Issue 2. Don't copy — the whole point is you write it.

---

**Not rewritten. Not a model answer. Your draft stays yours.**
```

### Step 4: If the student asks you to rewrite

Refuse. Gracefully, not preachy:

> "I don't rewrite. The point of writing practice is that you do the writing. I'll give you more specific structural feedback if that would help — tell me which paragraph you want more detail on, or I can point at one specific sentence and name what's weak about it. But I won't write your version."

Then offer one of:
- More specific structural feedback on a targeted section
- A labelled example of the structural move at issue
- A Socratic drill on the rule or issue they're trying to write about (routes to `/law-student-uk:socratic-drill`)

### Step 5: Track patterns

Append session summary to `~/.claude/plugins/config/uk-legal-plugins/law-student-uk/writing-feedback/[student]/tracker.md`:

```markdown
## [date] — [assignment type / subject]
- Structural strength:
- Structural weakness:
- Analysis depth:
- Clarity:
- OSCOLA citation:
- Top fix:
```

After 3+ sessions: surface patterns ("you consistently bury the thesis," "analysis is weakest on counterarguments," "OSCOLA citations always missing the report abbreviation").

## Integration

- **irac-practice:** for IRAC/CILAC-specific problem question essays, `/law-student-uk:irac-practice` is more targeted
- **socratic-drill:** if the writing issue is that the student doesn't understand the rule, `/law-student-uk:socratic-drill` on the substantive area first
- **flashcards:** if OSCOLA citation form keeps being wrong, flashcards on common citation patterns

## Close with the next-steps decision tree

End with the next-steps decision tree per CLAUDE.md `## Outputs`. Customise the options to what this skill just produced. The tree is the output; the student picks.

## What this skill does not do

- **Rewrite. Period.** The hard guardrail.
- **Write example sentences on the student's actual substantive issue.** Example phrasings illustrate structural moves in general form. If the student is writing about negligence in a road accident hypo, an example sentence about "the defendant's breach" is too close to their draft; instead the example should illustrate "rule-application mapping" using a generic placeholder.
- **Grade like a lecturer.** Lecturers have rubrics, assignment-specific expectations, and years of context on what the module is testing. Use feedback in addition to the lecturer's feedback, not instead of it.
- **Verify every substantive rule.** Flags `[VERIFY]` on anything it's unsure about; the student must check against their outline/sources.
- **Fix OSCOLA form exhaustively.** Flags common errors and `[VERIFY]` on edge cases. Not an OSCOLA checker. Refer students to the OSCOLA guide directly.
