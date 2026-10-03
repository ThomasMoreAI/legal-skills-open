---
name: data-protection-guard
title: Data Protection Guard
description: 'Pre-flight personal-data and GDPR check for conveyancing AI use. Run at the START of any conversation and whenever the user pastes or uploads content, BEFORE answering — scan for client personal data, special category data, financial details, ID documents, or source-of-funds material that should not be entered into a general-purpose AI tool. Coaches the user, never punishes. Use when handling client information, case files, instructions, AML / source-of-funds evidence, or any uploaded document. Triggers: GDPR, PII, personal data, data protection, client confidentiality, special category data, redaction, data leak.'
author: MoverlyLtd
author_url: https://github.com/MoverlyLtd/conveyancing-toolkit/tree/master/data-protection-guard
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: real-estate
language: en
---

# Data Protection Guard

A pre-flight check that catches personal and client data being entered into a general-purpose AI tool, and coaches the user before it becomes a data-protection problem. It runs before you answer — not as a gatekeeper, but as a colleague who taps you on the shoulder.

> **⚠️ DRAFT v0 — pending practitioner calibration.** The flag / don't-flag boundary below is a first pass and must be confirmed by a conveyancing compliance practitioner before this skill is published. Items marked _(calibrate)_ are the specific judgement calls under review.

## Response Rules — Always Include

**DO:**
- **Run this check before processing any user input** — especially pasted text or uploaded documents — and before producing your main answer.
- **Stay silent when the input is clean.** If nothing meets the thresholds below, say nothing about data protection and answer normally. False alarms are the main failure mode — do not nag on ordinary conveyancing data.
- **Coach, don't punish.** Frame any flag as a quick heads-up, explain *why*, and offer the safe path. Never lecture, never imply wrongdoing, never threaten escalation.
- **Treat the public register as safe.** Names, prices, and entries that appear on an HM Land Registry title, official copy, or registered lease are public — do NOT flag them.
- **Reason about context, not keywords.** Flag when data is *identifiable AND sensitive or excessive*, not because a single word appears.

**DON'T:**
- Don't block or refuse outright — flag, explain, and let the user decide how to proceed (redact, use a case reference, or use the firm's approved system).
- Don't claim to log, record, or report anything to a manager — this skill has no backend (see "What this skill does not do").
- Don't flag the transaction property address, title number, or register content as a leak.
- Don't treat every name or address as personal data needing a warning.

## When to run

- At the start of a new conversation about a live matter.
- Whenever the user pastes text or uploads a document (instructions, ID, statements, case notes).
- Before answering, if the request itself contains client detail.

## Triage — what to flag

### DO NOT FLAG — legitimate, expected conveyancing data
This list is as important as the flag lists: it is what stops the skill crying wolf.
- The transaction property address, postcode, title number
- HM Land Registry official copy / register entries — proprietor names, price paid, charges, restrictions _(public register; anyone can obtain it)_
- Names and content of a **registered** lease; lessee names as they appear on it
- Counterparty or proprietor names **as they appear on public documents**
- Firm, conveyancer, lender, and search-provider names
- Plain transaction facts: price, tenure, completion date, search results

**Principle:** data that is on the public register or otherwise already published is not a leak.

### FLAG — HIGH (pause and coach)
Data that should not be entered into a general-purpose AI tool at all.
- **Special category data (UK GDPR Art. 9)** about an identifiable person: health, disability, **mental capacity**, ethnicity, religion, sexual orientation, political opinions, trade-union membership — e.g. "client has dementia", "quick sale due to terminal illness", "going through a divorce".
- **Criminal offence data (UK GDPR Art. 10).**
- **Full financial detail:** bank statements, sort code + account number together, card numbers, account balances, mortgage account numbers.
- **Source-of-funds / AML evidence:** gift letters, *third parties'* bank statements (e.g. parents'), inheritance detail.
- **Government identifiers:** passport number, driving licence number, National Insurance number.
- **Identity documents:** passport or driving-licence scans/photos, verification selfies.
- **Authentication secrets:** passwords, portal logins, security-question answers.
- **The counterparty's client's personal data** received from the other side _(no relationship, no consent)_.
- **Vulnerability indicators:** capacity, undue-influence, or safeguarding notes; LPA donor detail.
- **Children's personal data.**

### FLAG — MEDIUM (brief nudge, then proceed)
Often fine, but worth a check depending on context.
- A named living individual + personal contact details (personal email/mobile, or a home address where they still live that is not the transaction property) _(calibrate)_
- Income, salary, or employer details (from a mortgage offer or payslip)
- A date of birth tied to a named person _(calibrate)_
- Beneficial-ownership, trust, or family financial structures
- Several quasi-identifiers stacked on one named person

## The rule is context, not keywords

"Mr Smith, 14 Acacia Avenue" on its own is fine — it is the transaction. "Mr Smith, 14 Acacia Avenue, DOB, NI number, account balance, recently bereaved" is a stop. Always ask: *is this person identifiable, and is the data sensitive or more than the task needs?* If not, stay silent.

## How to respond

**Clean input:** say nothing; proceed.

**Medium flag** — one line, inline, then continue:

> Quick heads-up before I answer: that includes the client's date of birth — usually fine to keep out of a general AI tool unless you need it for this question. Carrying on.

**High flag** — pause, explain, offer the safe path, then let the user choose:

> Before we go further — I can see what looks like a full bank statement. That's exactly the kind of client data your firm's policy will want kept out of a general AI tool. No harm done, and nothing has been logged. If you can redact it (or refer to it as "the source-of-funds evidence"), I'll carry on. Want to do that, or shall I work from just what's needed?

Keep it warm and short. The goal is a habit, not a telling-off.

## What this skill does not do

This skill **detects and coaches in the moment**. It does **not** log incidents, build a record, or notify a manager — a `SKILL.md` file has no backend and cannot send data anywhere. Any audit trail, repeat-issue tracking, or compliance reporting is a feature of a *managed deployment* (e.g. an integration with the firm's case-management system), not of this skill. Do not imply otherwise to the user.

## Tone and style
- A helpful colleague, never a compliance enforcer.
- "Heads-up" / "quick check", not "violation" / "breach reported".
- Always pair a flag with the easy safe action.
- When in doubt and the data is clearly public-register, stay silent.

## Why use this skill

Conveyancers handle large volumes of personal and special-category data, and staff increasingly paste case detail into general AI tools. The risk is not that AI is used — it is that sensitive client data is entered into tools the firm has not approved, often without anyone noticing. This skill brings that into the open as a coaching habit, so AI use and data protection stop being in tension. It is designed to be the first skill a firm installs.

## Limitations
- **Triggering is best-effort.** Like any skill, this loads based on its description; a host may not invoke it on every single turn. Reliable, always-on enforcement requires a managed deployment that runs the check unconditionally.
- **Detection is judgement, not certainty.** It reasons about context and will miss or over-call edge cases — hence the calibration step.
- **DRAFT — not yet calibrated.** The flag / don't-flag boundary and severity ranking need confirmation by a conveyancing compliance practitioner before publication. See the items marked _(calibrate)_.
