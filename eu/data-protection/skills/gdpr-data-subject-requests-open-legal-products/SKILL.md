---
name: gdpr-data-subject-requests-open-legal-products
title: GDPR Data Subject Requests
description: 'Handle a data subject rights request under GDPR Articles 12 and 15-22: identify the right invoked (access, rectification, erasure, restriction, portability, objection, automated decisions), verify identity, track the one-month deadline and the two-month extension, check exemptions and refusal grounds, and draft the response plus a request register entry. Use when a subject access request, erasure request, objection, or portability request arrives and the deadline and legal gates must be worked through. The workflow drafts; a human decides, performs the erasure or export, and sends the response.'
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/assistant-workflows/eu-gdpr-pack/gdpr-data-subject-requests
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
---

# GDPR Data Subject Requests

A rights request is a clock plus a legal assessment, not an automation. The workflow classifies the request, tracks the deadline, and produces a draft; the fulfil-or-refuse decision and the act of sending belong to the controller. Erasure and export are irreversible or outward acts, so they always stay with a human.

## Step 0 - Identity and deadline

- Identity verification (Article 12(6)): where reasonable doubt exists, request further information. This does not pause the clock unconditionally. Per EDPB Guidelines 01/2022, the deadline may be suspended only where the additional information is necessary to confirm identity and the controller asked for it without undue delay. Always preserve the original receipt date in the register - a late or disproportionate identity request does not extend the deadline, and verification must not be used to obstruct the request.
- Deadline: one month from receipt (Article 12(3)), extendable by up to two further months for complexity or number of requests - the data subject must be informed of the extension and its reasons within the first month. Compute the exact deadline dates and state them in the draft and register. Month arithmetic has traps: under Regulation (EEC) No 1182/71, a request received on 31 January runs to the last day of February.
- Free of charge by default (Article 12(5)). A fee or refusal is allowed only where the request is manifestly unfounded or excessive, and the burden of proof is on the controller.

## Step 1 - Classify the right

| Article | Right | Key points |
|---|---|---|
| 15 | Access and copy | scope of information, copy of the data, third-party rights |
| 16 | Rectification | inaccurate or incomplete data |
| 17 | Erasure ("right to be forgotten") | grounds in 17(1) against the exemptions in 17(3): legal obligation, legal claims, freedom of expression |
| 18 | Restriction | a freeze instead of erasure |
| 20 | Portability | consent or contract basis plus automated processing only; structured, machine-readable format |
| 21 | Objection | legitimate interest or direct marketing - the marketing objection is absolute |
| 22 | Automated decisions | the primary right is not to be subject to a solely automated decision producing legal or similarly significant effects; exceptions in 22(2) (contract, authorising law, explicit consent) trigger safeguards - at minimum human intervention, expressing one's view, and contesting the decision (22(3)) |

A request can be informal - interpret its substance, not its heading.

## Step 2 - Gates and refusal grounds

Check the exemptions specific to the right invoked (especially Article 17(3) and national restrictions). Every refusal must be legally justified and must inform the data subject of the right to lodge a complaint with the supervisory authority and to seek a judicial remedy (Article 12(4)).

## Step 3 - Draft the response and the register entry

Draft the response in clear and plain language (Article 12(1)), tailored to the right invoked. For an Article 15 request that means a copy of the personal data undergoing processing, retrieved from the operational systems that actually hold it, plus any available information on the data's source (Article 15(1)(g)). The records of processing supply only the general processing information - purposes, categories, recipients, retention - not the person's data or necessarily its sources; a response drafted from the RoPA alone is incomplete. Close with a register entry recording receipt date, request type, deadline, and outcome.

## Governance boundary

The workflow classifies, computes deadlines, drafts, and maintains the register. A human verifies identity, decides whether to fulfil or refuse, performs the erasure or export, and sends the response. Irreversible and outward acts are never automatic.
