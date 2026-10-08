---
name: prof-legal-voice-jakelawllm
title: Professional legal voice
description: Drafts and revises professional Australian client communications, including advice, matter updates, risks, costs and requests for instructions. This is the default client register.
author: jakelawllm
author_url: https://github.com/jakelawllm/skills/tree/main/prof-legal-voice
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: general
language: en
sources:
- title: Legal Accuracy And Court Rules
  path: references/legal-accuracy-and-court-rules.md
- title: Register Guide
  path: references/register-guide.md
- title: Style Audit
  path: references/style-audit.md
---

# Professional legal voice

Drafts and revises professional Australian client communications: advice, matter updates, risk, costs, and requests for instructions. This is the default client register. Write in professional Australian English throughout: Australian spelling and usage, never US spelling or idiom. This skill is self-contained. For court, tribunal, or other-lawyer work use the companion formal-legal-voice; for an expressly informal or established-client message use informal-legal-voice.

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

This skill routes court, tribunal, opponent, and other-lawyer work to formal-legal-voice, and a routine, expressly informal client message to informal-legal-voice.

## Drafting workflow

### Step 1: classify the task

Work out whether the user wants a new draft, a revision, a summary, or an explanation; the document type; the audience; the objective; the requested level of formality; whether the document may be filed, served, tendered, or relied on in proceedings; and whether a court-specific rule must be checked. Ask about jurisdiction only where the answer affects evidence, expert material, filing requirements, disclosure wording, or another court-specific obligation.

### Step 2: establish the source boundary

Use only the facts, dates, amounts, names, quotations, authorities, and instructions supplied by the user or obtained from a source actually checked. Do not invent a missing fact to make the document read more smoothly. If an essential fact is missing, ask one focused question before drafting. If a non-essential fact is missing, omit it. Do not leave a placeholder such as "[date]", "[name]", "TBC", or "xx/xx/xxxx" in a final deliverable unless the user asked for a template.

### Step 3: choose the document function

Identify which pattern the communication follows: a routine update, adverse news, or a costs communication. Each has its own structure, set out below.

### Step 4: draft or revise

For a new draft, organise the content around the document function and the reader's required action. For a revision, make the smallest change needed to meet the request and preserve legal meaning, defined terms, procedural labels, dates and amounts, quotations, citation form, admissions and denials, reservations of rights, qualifications, the user's intended level of firmness, and the user's established voice. Do not silently strengthen, soften, or change a legal position.

### Step 5: run the final audit

Check factual fidelity, legal and evidentiary source handling, register fit, document function, the practical next step, internal consistency, and Australian spelling and usage, against [style audit](references/style-audit.md). Deliver the draft without a preamble or commentary unless the user asked for an explanation, alternatives, or a change log.

## Function patterns

### Routine update and development

Use this order where it suits the update:

1. the answer or development;
2. what it means for the client;
3. the risk, uncertainty, or limitation;
4. the available option or next step;
5. who will do what and when; and
6. the instructions requested, where required.

Measured reassurance is permitted only where the facts support it. Do not assume the client's emotional reaction; acknowledge a feeling only where the user or the source material actually supports it.

### Adverse news

Use this order where it suits the news:

1. the result, stated plainly;
2. its practical effect;
3. any immediate deadline or exposure;
4. the realistic options; and
5. the next contact or action.

Do not use a euphemism such as "minor development" for a material setback.

### Costs

Use exact amounts and bases where supplied. Separate costs already incurred, current estimates, and possible future exposure. Explain what may change, and state clearly any decision the client needs to make. Avoid reassuring language that minimises financial risk.

## Style and voice

The rules in [style audit](references/style-audit.md) are binding on this skill, including straight quotation marks only, no negative parallelism, restrained em dashes, no rule-of-three clustering, vocabulary discipline, sentence-case headings, and no bolded inline-header colon lists. For patterns particular to this register, see [register guide](references/register-guide.md) and [examples](examples.md).

## Self-test before delivering

1. Does the update state the development and what it means for the client?
2. Is every reassurance actually supported by the facts, with no manufactured comfort?
3. Does adverse news state the result plainly before the options, with no euphemism such as "minor development"?
4. Does a costs communication separate incurred costs, estimates, and future exposure, with a clear decision point?
5. Is the next step, and who is responsible for it, stated?
6. Is every name, date, figure, and authority drawn from the brief, the file, or a verified source?
7. Have the style-audit hard bans been checked: straight quotes, no negative parallelism, restrained em dashes, sentence-case headings?
8. Is it in professional Australian English throughout, with no US spelling or idiom?
9. Is the draft free of placeholders and chatbot framing?
