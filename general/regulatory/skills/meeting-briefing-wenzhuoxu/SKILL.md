---
name: meeting-briefing-wenzhuoxu
title: /meeting-briefing — Counterparty / Authority Meeting Prep
description: Prepare a negotiation / meeting briefing for a legal interaction with a counterparty or authority. Use when preparing for a term-sheet call, M&A negotiation, vendor SOW review, regulator inspection or LOI response meeting, customer kickoff, or a multi-party closing dry-run.
author: WenzhuoXu
author_url: https://github.com/WenzhuoXu/lawgent/tree/main/legal_helper/skills/meeting-briefing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# /meeting-briefing — Counterparty / Authority Meeting Prep

Produce the analytical bundle the orchestrator turns into a briefing
memo: counterparty profile, governing law, open issues, positions, and
procedural plan.

**Not legal advice.** The bundle is internal work product; counsel
validates positions before any commitment.

## Output Contract (binding)

Same as `/playbook/general_playbook.md` §4 and §5:

````
## Findings
- [self-contained claim, ONE sentence, ≤60 English words, inline pinpoint `[Source, art./§/p.]`] (label: treaty | regulation | case | guidance | local-law | best-practice | risk | drafting)
- ...

## Out of scope
- ...

## Sources
- [source name] — [URL or local path] — supports findings #X[, online-checked: yes/no, pinpoint: confirmed/unavailable]
````

Hard ceiling **≤ 2000 characters**.

## Inputs

- **Counterparty / authority** (name, role, jurisdiction).
- **Meeting purpose** (term sheet, SOW, dispute, inspection, closing).
- **Prior documents** (existing draft, term sheet, MOU, prior
  correspondence).
- **Time / venue / mode** (in-person, video, written).
- **Internal team** + reporting line.

## Workflow

1. **Counterparty profile** — entity status, jurisdiction, sanctions /
   denied-party screen, prior dealings (if known), known positions.
2. **Governing law / forum** — applicable law for the deal / dispute;
   procedural rules for any regulator meeting.
3. **Issue list** — one Findings bullet per material issue with the
   position, the fallback, and the walk-away.
4. **Procedural plan** — sequence, who speaks to what, privilege posture,
   document exchange protocol.
5. **Risk + escalation hooks** — flag any issue that triggers escalation
   (see `legal-risk-assessment` matrix).

## Counterparty types (generic)

Commercial counterparties: customer, supplier, distributor, joint-venture
partner, M&A target / acquirer, licensee / licensor, investor.

Authorities: regulator (sector-specific), tax authority, data-protection
authority, court / arbitral tribunal, customs / immigration / police.

## Pointers

- Authority hierarchy + citation: `/playbook/general_playbook.md` §0 + §2.
- Sanity-check + label set: general playbook §3 + §4.
- When the **aviation** pack is active, also apply
  `/domains/aviation/overlays/meeting-briefing.md`.
