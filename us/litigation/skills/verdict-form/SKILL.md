---
name: verdict-form
title: Verdict Form
description: Drafts civil trial verdict forms with sequentially numbered jury questions covering liability, affirmative defenses, damages, comparative fault, and special interrogatories. Enforces plain-language phrasing, logical conditional flow, and jurisdiction-appropriate formatting. Use when preparing verdict forms, special verdict forms, jury interrogatories, or general verdict forms with interrogatories.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/verdict-form
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Verdict Form

Drafts a trial-ready verdict form guiding jury deliberations through structured questions on liability, defenses, and damages for each cause of action.

## Prerequisites

Gather before drafting:

- **Operative pleading** — all causes of action and elements
- **Answer / affirmative defenses** — complete defense list including comparative fault
- **Jury instructions** — draft or final, for terminology alignment
- **Damages evidence summary** — categories supported by evidence
- **Local rules** — jurisdiction-specific form requirements (signatures, special verdict mandates)

## Quick Start

1. Mirror the caption from operative pleadings exactly
2. Add introductory jury statement
3. Draft sequentially numbered liability questions per cause of action
4. Insert conditional affirmative defense questions
5. Add damages questions conditioned on liability findings
6. Include comparative fault allocation if at issue
7. Add any court-required special interrogatories
8. Close with jurisdiction-appropriate signature block

## Core Sections

### Caption

Copy verbatim from operative pleadings. Include court name, division, parties, case number, and title "VERDICT FORM."

### Introductory Statement

Standard language: "We, the jury, duly empaneled and sworn in the above-entitled action, hereby return the following verdict:"

### Liability Questions

One sequentially numbered question per cause of action:

- **Plain language** — "breached the contract," not "material breach of the subject agreement"
- **State burden** — "proven by a preponderance of the evidence"
- **Answer format** — Yes ___ / No ___ with adequate white space
- **Order** — foundational claims first, then dependent claims

### Affirmative Defense Questions

For each complete-bar defense, insert a conditional question:

- Gate on the relevant liability "Yes" answer
- Ask whether defendant proved the defense applies
- If "Yes," direct jury to skip to Signature
- If "No," direct to next question

### Damages

Condition all damages questions on liability "Yes" + defense "No" findings. Otherwise direct jury to skip to Signature.

Draft separate dollar-amount lines per category:

| Category | Include When |
|----------|-------------|
| Compensatory (general) | Always if liability found |
| Compensatory (special) | Lost profits, medical expenses, property damage — itemize separately |
| Consequential | Pled and supported by evidence |
| Punitive | Only after predicate finding (malice/fraud/oppression per applicable state law) |

For punitive damages, require a separate predicate question before the amount question.

### Comparative Fault

If at issue, add percentage allocation question requiring all parties to total 100%.

### Special Interrogatories

Numbered questions for court-required factual findings: good faith, notice compliance, conditions precedent, timeliness / statute of limitations.

### Signature Block

Standard closing: "We, the jury, certify that this is our verdict." Include date line, foreperson signature and printed name. Check local rules — some jurisdictions require all jurors to sign.

## Pitfalls and Checks

- **Sequential numbering** — number continuously across all sections; never restart per section
- **Terminology alignment** — every question must mirror jury instruction language exactly
- **Explicit skip instructions** — every conditional must state where to go ("If No, skip to Question [N]")
- **Completeness** — cover every claim + every complete-bar defense so the court can enter judgment from answers alone
- **No contradictions** — structure conditionals to prevent logically inconsistent answers
- **Jurisdiction adaptation** — verify local requirements for punitive damages predicates, signature rules, and form mandates
