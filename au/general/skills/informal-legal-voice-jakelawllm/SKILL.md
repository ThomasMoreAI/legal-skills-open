---
name: informal-legal-voice-jakelawllm
title: Informal legal voice
description: Drafts and revises short, plain Australian client messages for an established relationship and routine updates when an informal or conversational register is requested.
author: jakelawllm
author_url: https://github.com/jakelawllm/skills/tree/main/informal-legal-voice
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

# Informal legal voice

Drafts and revises short, plain Australian client messages for an established relationship and routine updates, where an informal or conversational register has been requested or is clearly shown by the relationship. Write in informal Australian English throughout: Australian spelling and usage, never US spelling or idiom. This skill is self-contained and narrower than the companion prof-legal-voice, which remains the default for serious or ambiguous client work. For court, tribunal, or other-lawyer work use formal-legal-voice.

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

This skill routes serious or ambiguous client work to prof-legal-voice, and all court, tribunal, opponent, and other-lawyer work to formal-legal-voice.

## Drafting workflow

### Step 1: classify the task

Work out whether the user wants a new draft, a revision, a summary, or an explanation; the document type; the audience; the objective; the requested level of formality; whether the document may be filed, served, tendered, or relied on in proceedings; and whether a court-specific rule must be checked. Most informal messages need no jurisdiction question at all; ask one only where the answer affects evidence, expert material, filing requirements, disclosure wording, or another court-specific obligation.

### Step 2: establish the source boundary

Use only the facts, dates, amounts, names, quotations, authorities, and instructions supplied by the user or obtained from a source actually checked. Do not invent a missing fact to make the message read more smoothly. If an essential fact is missing, ask one focused question before drafting. If a non-essential fact is missing, omit it. Do not leave a placeholder such as "[date]", "[name]", "TBC", or "xx/xx/xxxx" in a final deliverable unless the user asked for a template.

### Step 3: choose the document function

Confirm the register genuinely fits before drafting. See when this register applies, below. If it does not fit, route to prof-legal-voice or formal-legal-voice under the register router.

### Step 4: draft or revise

For a new draft, organise the content around the reader's required action. For a revision, make the smallest change needed to meet the request and preserve legal meaning, defined terms, procedural labels, dates and amounts, quotations, the user's intended level of firmness, and the user's established voice. Do not silently strengthen, soften, or change a legal position.

### Step 5: run the final audit

Check factual fidelity, legal and evidentiary source handling, register fit, the practical next step, internal consistency, and Australian spelling and usage, against [style audit](references/style-audit.md). Deliver the draft without a preamble or commentary unless the user asked for an explanation, alternatives, or a change log.

## Function patterns

### When this register applies

Use this register for a routine update, a short request for documents or instructions, a plain explanation to an established client, an SMS, chat, or short-email style the user has requested, and low-stakes communication where the legal consequence is still stated accurately.

### When it does not apply

Do not use this register as the default for serious adverse news, a first communication, formal advice, a costs dispute, a complaint, an allegation of misconduct, a settlement recommendation involving material risk, or a case where the relationship is uncertain. Route these to prof-legal-voice under the register router.

### Keeping it plain without trivialising

Use contractions and short paragraphs where they sound natural. Do not invent familiarity, humour, empathy, or slang that the user has not shown. Do not trivialise a legal consequence: avoid "small hiccup" and avoid "nothing to worry about" unless that is literally true. Do not use "knocked the application back" as the model for an adverse result; prefer a plain, accurate statement such as "The Tribunal refused the application." Use no emoji unless the user uses them, requests them, or the channel and relationship clearly support them, and never on serious news.

## Style and voice

The rules in [style audit](references/style-audit.md) are binding on this skill, including straight quotation marks only, no negative parallelism, restrained em dashes, no rule-of-three clustering, vocabulary discipline, sentence-case headings, and no bolded inline-header colon lists. For patterns particular to this register, see [register guide](references/register-guide.md) and [examples](examples.md).

## Self-test before delivering

1. Does this register genuinely fit, or does the matter belong in prof-legal-voice or formal-legal-voice under the register router?
2. Could the client comfortably hear this read aloud, in these words?
3. Is any warmth genuine and specific rather than invented familiarity?
4. Is a serious outcome stated plainly and accurately, with no trivialising phrase such as "small hiccup" or "knocked back"?
5. Does the message still say what the development means and what happens next?
6. Is every name, date, figure, and instruction drawn from the brief, the file, or a verified source?
7. Have the style-audit hard bans been checked: straight quotes, no negative parallelism, restrained em dashes, sentence-case headings?
8. Is it in informal Australian English throughout, with no US spelling or idiom?
9. Is the draft free of placeholders and unrequested emoji?
