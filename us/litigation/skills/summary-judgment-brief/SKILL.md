---
name: summary-judgment-brief
title: Summary Judgment Motion Brief
description: Drafts FRCP 56 summary judgment motion briefs for U.S. commercial litigation. Synthesizes discovery evidence with controlling authority to show no genuine dispute of material fact. Use when drafting MSJ briefs, dispositive motions, or partial summary judgment papers post-discovery.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/summary-judgment-brief
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [brief, drafting]
---

# Summary Judgment Motion Brief

Draft a dispositive motion demonstrating entitlement to judgment as a matter of law under FRCP 56 or state equivalent.

## Prerequisites

Before drafting, confirm:

1. **Discovery record** — depositions, interrogatory answers, RFAs, document productions
2. **Claims/defenses targeted** — which counts or affirmative defenses the motion addresses
3. **Controlling authority** — binding precedent on substantive elements and SJ standard
4. **Local rules** — page limits, separate statement requirements, combined vs. separate motion/brief
5. **Party role** — plaintiff (proving all elements undisputed) or defendant (negating an element)

## Brief Structure

### 1. Caption

Include court (with division), full case title, case number, and document title per local rule formatting. Check whether jurisdiction requires separate notice of motion.

### 2. Introduction (2–3 paragraphs)

- Identify moving party and claims/defenses at issue
- Preview key undisputed facts material to disposition
- State why judgment as a matter of law follows
- Frame: no reasonable jury could find for non-movant on this record

### 3. Statement of Undisputed Material Facts

Number each fact separately with record citations:

```
1. [Objective fact — no argument or conclusions].
   (Ex. A, Smith Dep. 45:12–46:3; Ex. B, Invoice dated 3/15/2024.)

2. [Next fact...]
   (Jones Decl. ¶ 7; RFA No. 12, admitted.)
```

Rules:
- Every fact cited to admissible evidence (deposition page:line, declaration ¶, exhibit, RFA)
- Only material facts — no background filler
- Objective language only
- Organize chronologically or by element

### 4. Legal Standard

Cover these components:

| Component | Content |
|-----------|---------|
| Rule | FRCP 56(a) or state equivalent |
| Movant's burden | Demonstrate absence of genuine dispute — *Celotex Corp. v. Catrett*, 477 U.S. 317 (1986) |
| Burden shift | Non-movant must show specific facts creating genuine issue — *Anderson v. Liberty Lobby*, 477 U.S. 242 (1986) |
| Viewing standard | Light most favorable to non-movant — *Matsushita Elec. v. Zenith Radio*, 475 U.S. 574 (1986) |

Add substantive standards for the specific claims/defenses at issue.

### 5. Argument

Structure by claim, defense, or element:

```
I. [CLAIM/DEFENSE] FAILS BECAUSE [ELEMENT] IS UNDISPUTED

   A. Legal Rule — controlling statute + binding case law on elements
   B. Application — map numbered facts to each element
   C. Preemptive Rebuttal — anticipate opposition, distinguish unfavorable cases
```

- Each element: rule → fact application → conclusion
- Binding precedent first; persuasive authority supplemental
- Distinguish (don't ignore) unfavorable cases
- Tone: measured, confident — "reasonable minds could not differ"
- Cross-reference numbered undisputed facts throughout

### 6. Conclusion

Synthesize key points in 1–2 paragraphs. No new arguments or facts.

### 7. Prayer for Relief

- Specify scope: all claims or identified counts only
- Dismissal with prejudice where applicable
- Costs/fees if authorized by statute, contract, or rule
- Include catch-all: "such other relief as the Court deems just"

### 8. Signature Block & Certificate of Service

- Attorney name, bar number, firm, contact, designation per local rule
- Certificate: method (ECF/email/mail), date, all served parties/counsel

## Pitfalls

- **Unsupported assertions** — every factual statement needs a record cite; every legal proposition needs authority
- **Orphan facts** — facts section, argument, and prayer must align; no facts without argument use
- **Citation format** — Bluebook unless local rules specify otherwise
- **Partial SJ scope** — if fewer than all claims, delineate scope in intro, argument, and prayer
- **Page/word limits** — confirm and comply with local rules before finalizing
- **Exhibit consistency** — reference by letter/number uniformly; confirm all cited evidence is in the record
- **Strategic framing** — defendant: target weakest plaintiff element; plaintiff: lead with strongest undisputed evidence
