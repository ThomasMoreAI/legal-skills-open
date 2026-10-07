---
name: poland-healthcare
title: Poland Healthcare
description: Healthcare. Use when NFZ or IKP matters.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-healthcare
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: pl
practice: administrative
language: en
---

# Poland Healthcare

Use for NFZ coverage navigation, IKP/mojeIKP, primary care, referrals,
prescriptions, insurance confirmation, cross-border documents, and finding the
right public service. Do not diagnose, interpret symptoms, or delay urgent care.

First determine whether the need is an emergency. If immediate danger is possible,
surface 112 and human action through `poland-emergency-rights`; do not continue a
routine portal workflow. Otherwise confirm only broad coverage basis, locality,
`eu_eea_swiss` or `third_country` cross-border context, and whether the request
concerns public access guidance or a medical decision.

Use public NFZ and Pacjent.gov.pl sources. Identify evidence categories and the
competent branch, and state what a medical professional or insurer must confirm.
Do not diagnose from portal data.

For requested IKP/mojeIKP help, apply
`../../references/automation-playbook.md`. The user authenticates and explicitly
authorizes the minimum health-record scope. A caller-owned tool may then inspect
the relevant record and fill necessary administrative fields; booking, provider
declaration, send, upload, or download requires fresh action-time confirmation.
Signatures, medical consent, and treatment decisions remain user-controlled.
Avoid screenshots and durable copies of health data.

For insurance registration or contributions route to
`poland-social-insurance`; for EU coordination also use
`poland-eu-mobility`. Read
`../../references/daily-life-map.md` and the emergency boundary in
`../../references/emergency-and-escalation.md`.
