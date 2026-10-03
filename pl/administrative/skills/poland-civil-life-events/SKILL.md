---
name: poland-civil-life-events
title: Poland Civil Life Events
description: 'Civil status and life events: route birth, marriage, name, death, funeral, and succession administration in Poland. Excludes residence status and personalized inheritance advice.'
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-civil-life-events
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: administrative
language: en
---

# Poland Civil Life Events

Use for civil-status records and the administrative consequences of birth,
parentage, marriage, a name change, death, burial, or succession. Route the
event across the civil registry office, gmina, court, notary, consulate, or
another competent owner without assuming that one office handles every step.

Establish the event category, whether it occurred in Poland or abroad, the
relevant locality, the date, the person's broad citizenship/residence category,
and the requested result. Do not request record numbers or personal documents
in bundled CLI/MCP inputs. Separate registration, obtaining a copy, recognizing
a foreign record, family-law effects, funeral administration, and succession;
they are not interchangeable procedures.

For succession, use `civil-succession-route` and keep civil title, debts,
court/notary ownership, tax reporting, and cross-border questions separate.
Use the e-Justice factsheet and authority atlas plus `justice-court-finder` only
to identify candidate routes. A cross-border element, minor, dispute, debt,
applicable-law question, or unclear venue requires legal escalation. Never
select heirs or shares, acceptance or rejection, court or notary as an
individualized legal conclusion.

Use the matching scenario and source IDs in `data/scenarios.json` and
`data/sources.json`. Show which steps are online, local, consular, notarial, or
court-owned; mark original-document, witness, signature, and personal-appearance
requirements for live verification. Read
`../../references/life-events-and-services.md` for the maintained service map
and `../../references/documents-and-language.md` for foreign records,
translation, apostille, and legalization.

For an authorized portal task, apply
`../../references/automation-playbook.md`: the user authenticates and controls
signatures and attestations; the agent may inspect the minimum authorized record
and prepare fields; submit, send, book, upload, download, or record change needs
fresh action-time confirmation. Never infer parentage, marital status, heirs,
ownership, or entitlement from incomplete facts.

Route status acquisition to `poland-stay-residence` or
`poland-citizenship-long-term`, family disputes to
`poland-justice-legal-aid`, and immediate bereavement or safety needs to the
appropriate human service.
