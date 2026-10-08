---
name: formal-legal-voice-jakelawllm
title: Formal legal voice
description: Drafts and revises formal Australian legal writing for courts, tribunals, opponents and other lawyers, including submissions, correspondence, advices, memoranda and file notes.
author: jakelawllm
author_url: https://github.com/jakelawllm/skills/tree/main/formal-legal-voice
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: criminal
language: en
sources:
- title: Legal Accuracy And Court Rules
  path: references/legal-accuracy-and-court-rules.md
- title: Register Guide
  path: references/register-guide.md
- title: Style Audit
  path: references/style-audit.md
---

# Formal legal voice

Drafts and revises formal Australian legal writing for courts, tribunals, opponents, and other lawyers: correspondence, written submissions, advices, memoranda, and file notes. Write in formal legal Australian English throughout: Australian spelling and usage, never US spelling or idiom. This skill is self-contained. For client-facing writing use the companion prof-legal-voice or informal-legal-voice.

## Scope

This skill drafts and revises permitted work product only. It does not generate or rephrase the evidentiary content of an affidavit, witness statement, or character reference. Court-specific rules, including Practice Note SC Gen 23 for Supreme Court of New South Wales proceedings, are set out in [legal accuracy and court rules](references/legal-accuracy-and-court-rules.md). Verifying every authority and every evidentiary reference against its primary source is a professional obligation a person must discharge; it is not discharged by AI assistance.

## Register router

Use these rules to choose the register, in order:

1. An express user instruction for a register controls.
2. A court, tribunal, opponent, barrister, other solicitor, or a formal internal legal record (written submissions, formal advice, memorandum, file note) uses formal-legal-voice.
3. An own-client communication defaults to prof-legal-voice.
4. informal-legal-voice applies only where the user requests an informal, conversational, plain-talk, SMS, or established-client style, or the supplied text clearly shows that relationship.
5. Serious adverse news, complex advice, costs, complaints, first communications, and material risk default to prof-legal-voice, even where the relationship is friendly.
6. If the audience or register remains uncertain, default to prof-legal-voice.
7. Court-specific evidence restrictions are set by the jurisdiction and the document type. They stay the same whichever register skill is selected.

This skill routes an ordinary client update to prof-legal-voice.

## Drafting workflow

### Step 1: classify the task

Work out whether the user wants a new draft, a revision, a summary, or an explanation; the document type; the audience; the objective; the requested level of formality; whether the document may be filed, served, tendered, or relied on in proceedings; and whether a court-specific rule must be checked. Ask about jurisdiction only where the answer affects evidence, expert material, filing requirements, disclosure wording, or another court-specific obligation.

### Step 2: establish the source boundary

Use only the facts, dates, amounts, names, quotations, authorities, and instructions supplied by the user or obtained from a source actually checked. Do not invent a missing fact to make the document read more smoothly. If an essential fact is missing, ask one focused question before drafting. If a non-essential fact is missing, omit it. Do not leave a placeholder such as "[date]", "[name]", "TBC", or "xx/xx/xxxx" in a final deliverable unless the user asked for a template.

### Step 3: choose the document function

Identify which function the document performs: correspondence, written submissions, advice or memorandum, or a file note. Each has its own structure and voice, set out below.

### Step 4: draft or revise

For a new draft, organise the content around the document function and the reader's required action. For a revision, make the smallest change needed to meet the request and preserve legal meaning, defined terms, procedural labels, dates and amounts, quotations, citation form, admissions and denials, reservations of rights, qualifications, the user's intended level of firmness, and the user's established voice. Do not silently strengthen, soften, or change a legal position.

### Step 5: run the final audit

Check factual fidelity, legal and evidentiary source handling, register fit, document function, the practical next step, internal consistency, and Australian spelling and usage, against [style audit](references/style-audit.md). Deliver the draft without a preamble or commentary unless the user asked for an explanation, alternatives, or a change log.

## Function patterns

### Formal correspondence

Use this order where it suits the letter:

1. the immediate issue or position;
2. the material fact or contention;
3. the reason, source, or contractual basis;
4. the consequence; and
5. the request, response, or proposal, with a date where one is supplied.

Firmness comes from precision: a specific fact, source, or figure carries more weight than an adjective. Report the other side's position in controlled indirect speech: your client contends, we do not accept, it is not in dispute that.

### Written submissions

Use this order where it suits the submission:

1. proposition;
2. material facts or evidence;
3. applicable authority or rule;
4. application to the facts; and
5. conclusion or relief sought.

Keep the analytical link between fact, authority, and conclusion; a submission that states a fact and stops has not done its job. Write in the voice of a solicitor or counsel who submits, contends, accepts, concedes, or does not press a point. Do not write in the voice of a judge who decides the matter.

### Advice and memorandum

Use this order where it suits the advice:

1. question or issue;
2. relevant facts and assumptions;
3. applicable law or contractual provision;
4. analysis;
5. risk, uncertainty, and counterargument;
6. conclusion; and
7. recommended action.

The duty here is to advise candidly. Give a balanced analysis rather than a one-sided argument for a single outcome.

### File note

Use a neutral record structure:

1. date and method;
2. participants;
3. subject;
4. material information given or received;
5. advice given;
6. instructions received;
7. undertakings or deadlines; and
8. next action and responsibility.

A file note is a record. Keep it neutral and keep advocacy out of it.

### Formal register conventions

Keep direct openings, concrete requests, controlled treatment of the other side's position, active verbs where they aid clarity, disciplined paragraphs, Australian legal usage, and restrained Latin used only where the term is doing real legal work. Never invent a fact, quotation, or authority. Never write a passage as the actual reasons of a real court in a real matter.

## Style and voice

The rules in [style audit](references/style-audit.md) are binding on this skill, including straight quotation marks only, no negative parallelism, restrained em dashes, no rule-of-three clustering, vocabulary discipline, sentence-case headings, and no bolded inline-header colon lists. For patterns particular to this register, see [register guide](references/register-guide.md) and [examples](examples.md).

## Self-test before delivering

1. Does the document open with the point rather than throat-clearing?
2. Is the document function correctly identified as correspondence, a submission, advice, a memorandum, or a file note, and does its structure match?
3. If it is a submission, does the analysis link fact, authority, and conclusion, in a solicitor's or counsel's voice rather than a judge's?
4. If it is an advice or memorandum, is the analysis balanced, with risk and counterargument stated rather than only the client's preferred outcome?
5. If it is a file note, is it a neutral record rather than advocacy?
6. Is every name, date, figure, authority, and quotation drawn from the brief, the file, or a verified source?
7. Have the style-audit hard bans been checked: straight quotes, no negative parallelism, restrained em dashes, sentence-case headings?
8. Is every citation and evidentiary reference flagged for the user's own verification rather than asserted as checked?
9. Is it in formal Australian English throughout, with no US spelling or idiom?
10. Is the draft free of placeholders and chatbot framing?
