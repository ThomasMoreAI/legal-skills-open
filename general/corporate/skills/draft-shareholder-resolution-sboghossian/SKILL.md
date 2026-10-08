---
name: draft-shareholder-resolution-sboghossian
title: Draft — Shareholder Resolution
description: Use when drafting a shareholder resolution — whether an ordinary resolution for routine corporate decisions or a special resolution requiring a higher majority for constitutional changes, share issuances, or M&A approvals. Covers written resolution format and meeting-vote record format for DIFC, ADGM, UAE onshore, KSA, Lebanon, and UK entities. Flags the required voting thresholds, quorum rules, and registration requirements per jurisdiction.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-shareholder-resolution
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Draft — Shareholder Resolution

A shareholder resolution is the formal expression of shareholder will on a specific matter. It may be passed in a general meeting (Annual General Meeting or Extraordinary General Meeting) or, where permitted, by written resolution outside a meeting. The drafting requirements — identification, resolution type, operative language, and execution — are strictly interpreted in most jurisdictions.

## When to use this

- Approving a major transaction (acquisition, disposal, merger) that requires shareholder approval under applicable law or the company's articles / shareholders' agreement
- Amending the articles or bylaws
- Issuing new shares (pre-emptive rights, capital increase)
- Appointing or removing directors
- Approving auditor appointment or financial statements
- Approving a dividend
- Winding up the company voluntarily
- Any matter reserved to shareholders in the SHA or company constitution

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Company (full legal name, registration number, jurisdiction) | Identifies the legal entity and applicable law | Must provide |
| Resolution type (ordinary vs special) | Determines required majority | Must identify correctly |
| Specific resolution language | The operative text of what is being resolved | Must provide; see templates below |
| Passing mechanism | Written consent or general meeting vote | Written consent where law permits; meeting record otherwise |
| Shareholders and their holdings | Required to confirm quorum and voting sufficiency | Must provide (or confirm with company secretary) |
| Date | Date of passing | Must provide |

## Resolution Types and Required Majorities

| Resolution type | Standard majority | Typical use |
|---|---|---|
| Ordinary | Simple majority (>50% of votes cast) | Routine matters: director appointment, approve accounts, declare dividend |
| Special | 75% supermajority of votes cast (English-law standard) | Alter articles, change company name, wind up voluntarily |
| Reserved matter | Threshold set in SHA (often 75%, 80%, or unanimity) | SHA reserved matters list: new share class, change of business, key personnel |
| Unanimous | 100% | Specific matters in some jurisdictions; waiving statutory rights |

Note: in many MENA civil-law jurisdictions (LB, UAE onshore, KSA), the company law sets its own thresholds for specific resolutions which may differ from English-law conventions.

## Written Resolution Format (English-law / DIFC / ADGM)

```
WRITTEN RESOLUTION OF THE SHAREHOLDERS
OF [COMPANY FULL LEGAL NAME]
(Registration Number: [X]) (the "Company")

Date: [Date]

BACKGROUND
The shareholders of the Company, acting pursuant to [Article X of the Articles of
Association / Section X of the Companies Law], hereby pass the following resolution
by written consent without a meeting:

[ORDINARY / SPECIAL] RESOLUTION

RESOLVED THAT:
[Operative text of resolution — precise, in the present tense, with defined terms
cross-referencing any attached documents]

Signed by / on behalf of:

[Shareholder 1 Name]  
[Capacity / Title]  
[Date of signature]

[Shareholder 2 Name]  
[Capacity / Title]  
[Date of signature]
```

### Written Resolution Mechanics
- Circulated to all shareholders simultaneously (English law requirement; mirrors Meeting notice logic)
- Deadline for response specified (typically 28 days under UK Companies Act 2006)
- A written resolution is passed when the required majority has signed and returned it
- Attach all relevant documents (term sheet, share transfer form, amended articles) as exhibits to the resolution

## Meeting Resolution Format

```
MINUTES OF EXTRAORDINARY GENERAL MEETING
OF THE SHAREHOLDERS OF [COMPANY]
Held at: [Location] / Via video conference
Date and time: [Date], [Time]

PRESENT:
[Name], holding [X] shares ([Y]% of issued capital)
[Name], holding [X] shares ([Y]% of issued capital)

QUORUM: A quorum being present, the Chairman declared the meeting duly constituted.

[ORDINARY / SPECIAL] RESOLUTION NO. [X]:

RESOLVED THAT:
[Operative text]

VOTE:
In favor: [X] shares ([Y]%)
Against: [X] shares ([Y]%)
Abstentions: [X] shares ([Y]%)
Result: PASSED [as an ordinary / special resolution]

[Additional resolutions as needed]

CLOSE: There being no further business, the Chairman declared the meeting closed.

Chairman: ___________________  Date: ___________
Secretary: ___________________  Date: ___________
```

## Common Resolution Templates

### New share issuance / capital increase
"RESOLVED THAT the share capital of the Company be increased from [current capital] to [new capital] by the creation of [X] new [ordinary / preferred] shares of [par value] each, and that the directors be authorized to allot such shares to [subscriber] at a price of [X] per share on the terms set out in the [subscription agreement / term sheet] attached as Exhibit A."

### Director appointment
"RESOLVED THAT [Full Name] be and is hereby appointed as [Executive Director / Non-Executive Director / Independent Director] of the Company with effect from [Date], having confirmed their willingness to act."

### Director removal
"RESOLVED THAT [Full Name] be and is hereby removed from the office of director of the Company with effect from [Date], in accordance with [Article X / applicable law]."

### Amendment to articles / bylaws
"RESOLVED THAT the Articles of Association of the Company be amended as set out in the marked version attached as Exhibit B, and that the [Secretary / registered agent] be authorized to file the amended Articles with [the relevant registrar]."

### Approval of transaction
"RESOLVED THAT the Company's entry into the [Agreement Name] dated [Date] with [Counterparty], in the form attached as Exhibit C, is hereby approved and ratified, and that [Director Name] be authorized to execute, deliver, and perform all actions necessary to give effect to such agreement."

### Dividend declaration
"RESOLVED THAT a [final / interim] dividend of [amount per share / total amount] be declared payable on [Date] to shareholders on the register as at [Record Date]."

## Jurisdictional Notes

### DIFC / ADGM
Written resolutions are widely available and routinely used. English-law conventions apply. Resolutions and any associated share transfers must be filed with the DIFC / ADGM Companies Registrar within the prescribed period (typically 15 business days for significant corporate actions).

### UAE Onshore (Federal Companies Law)
The UAE Federal Decree-Law 32/2021 on Commercial Companies governs. LLCs (LLCs are the most common form) require resolutions to be passed by partners at a meeting, or by circular resolution where the articles permit. Special resolutions (e.g., capital increase, amendment of memorandum of association) require a higher majority (often 75% of capital) and notarization of the resolution and the amended MOA before re-filing with the Department of Economic Development (DED).

### KSA
Resolutions of shareholders of a Limited Liability Company (LLC — الشركة ذات المسؤولية المحدودة) or a Joint Stock Company are governed by the Companies Law and its executive regulations. Ordinary resolutions: simple majority of represented shares. Extraordinary general meeting (capital changes, dissolution, M&A): typically 75% of represented shares. Minutes must be signed and may need Notary Public certification.

### Lebanon
Société à responsabilité limitée (SARL / شركة محدودة المسؤولية): resolutions passed by partners holding >50% (ordinary) or >75% (constitutional matters). Joint stock company (SAL / شركة مساهمة): AGM, EGM quorum and majority rules apply per the Code of Commerce. Resolutions affecting the company's articles must be registered with the Commercial Court registry (Le Greffe du Tribunal de Commerce).

### Notarization / Tawqi3i requirement
In UAE onshore, KSA, and LB, resolutions amending the company's constitutional documents (memorandum, articles) must be notarized and then filed with the relevant registry. The resolution itself may need to appear as a notarial instrument or be attached to a notarial certification. This adds time (typically 3–10 business days) and cost.

## Common Mistakes

- **Wrong resolution type** — passing a matter that requires a special resolution as an ordinary resolution renders the resolution void
- **Quorum not confirmed** — meeting minutes that fail to record quorum confirmation may be challenged
- **Operative text ambiguous** — "approved the transaction" without attaching the transaction document creates disputes about what exactly was approved; attach all relevant documents as exhibits
- **No filing follow-through** — passing the resolution is step one; filing with the registrar or notarizing as required is step two; both must be completed
- **Written resolution deadline missed** — if a written resolution is not returned by all required parties within the deadline, it lapses; re-circulate or convene a meeting

## Related skills

- [[draft-shareholders-agreement]]
- [[draft-articles-of-association]]
- [[draft-share-purchase-agreement]]
- [[draft-board-resolution]]
