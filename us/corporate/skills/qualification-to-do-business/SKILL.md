---
name: qualification-to-do-business
title: State Qualification to Do Business
description: 'Drafts U.S. foreign-corporation qualification filings (Certificate of Authority) for a target state. Use when registering a corporation to transact business outside its home jurisdiction, appointing a registered agent, checking qualification triggers, or assembling a filing-ready package. Trigger terms: certificate of authority, foreign corporation, register to do business, registered agent appointment.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/qualification-to-do-business
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# State Qualification to Do Business

Produces a state-specific Certificate of Authority packet for a foreign corporation seeking authorization to transact business in a U.S. state.

## Quick Start

Gather before beginning:

- Formation documents (articles/certificate, bylaws, officer authorization)
- Exact legal name as filed in home jurisdiction (including punctuation and designator)
- Home-jurisdiction certificate of good standing/existence
- Current officers/directors with titles and addresses
- Target-state filing requirements (form, fee, method, signature/notary rules)
- Name-availability result in target state

## Workflow

### 1. State Compliance Snapshot

Build this table first — all downstream work depends on it.

| Item | Output |
|---|---|
| Target state + filing office | Exact program and office |
| Qualification required? | Yes/No + legal basis or exception |
| Official form | Title, version, or "none available" |
| Filing name | Legal name + assumed-name requirement if any |
| Registered agent | Name, physical address, consent format |
| Notarization/declaration | Required? Text if yes |
| Certificate authentication | Apostille/consular rule if applicable |
| Fee + payment channel | Amount and method |
| Submission channel | Online/mail/in-person + portal ID |

If qualification is **not required**, output a reasoned denial memo instead of a filing package and stop.

### 2. Collect Core Data

| Field | Rule |
|---|---|
| Legal name | Match formation document exactly |
| Formation jurisdiction + date | State/country + incorporation date |
| Duration | Perpetual or fixed term |
| Principal office | Physical address (no PO box if disallowed) |
| Registered office | Physical in target state |
| Registered agent | Full name + address + availability |
| Officers | Names, titles, business addresses |
| Directors | Names + addresses |
| Authorized filer | Title + authority source |

Do not infer missing officer/agent details — request them.

### 3. Draft the Application

1. Build statutory sections: identification, in-state presence, registered office/agent, governance disclosure, certification, signature block.
2. Populate from source records only.
3. Insert signature block with state-specific attestation/declaration.
4. Add registered-agent consent using required language.
5. Append filing checklist: application, good-standing certificate, name reservation docs (if needed), fee payment, required affidavits.
6. Add transacting-business risk note if applicability is uncertain.

### 4. Validate Before Output

- [ ] No placeholders remain
- [ ] Registered-agent consent present and complete
- [ ] Good-standing certificate recency meets target-state tolerance [VERIFY]
- [ ] Officer/director rosters current and sourced
- [ ] Notary/declaration block matches state requirement
- [ ] Fee amount verified from latest state guidance [VERIFY]

## Pitfalls

- **No cross-state assumptions.** Each state has unique forms, fees, and requirements — use target-state authority directly.
- **Preserve exact legal name.** Capitalization, punctuation, and entity designator must match formation documents.
- **Foreign-country incorporation.** Evaluate apostille or authentication chain requirements [VERIFY].
- **Exempt activities.** If activity may be exempt (isolated transaction, interstate-only), flag for legal review [VERIFY].
