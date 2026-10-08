---
name: meeting-briefing-wenzhuoxu
title: /meeting-briefing — Counterparty / Authority Meeting Prep
description: Prepare a negotiation / meeting briefing for a legal interaction with a counterparty or authority. Use when preparing for a term-sheet call, M&A negotiation, vendor SOW review, regulator inspection or LOI response meeting, customer kickoff, or a multi-party closing dry-run.
author: WenzhuoXu
author_url: https://github.com/WenzhuoXu/lawgent/tree/main/legal_helper/skills/meeting-briefing
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# /meeting-briefing — Counterparty / Authority Meeting Prep

Produce the analysis behind a briefing memo: counterparty profile,
governing law, open issues, positions, and procedural plan.

**Not legal advice.** This is internal work product; counsel validates
positions before any commitment.

## Output Contract (binding)

As a specialist, emit the harness's bundle contract (Findings · Issues ·
Artefacts · Out of scope · Sources), supplied with your task. As the author of
a final answer, follow the author contract instead and put these artefacts in
the answer where they help the reader.

Artefacts this skill produces: the issue list (issue · our position · counterparty's likely position · ask · fallback).

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
- Sanity checks: general playbook §3; finding labels: the bundle contract.
- When the **aviation** pack is active, also apply
  `/domains/aviation/overlays/meeting-briefing.md`.
