---
name: poland-social-insurance-xopoko
title: Poland Social Insurance
description: Social insurance. Use for Polish ZUS or eZUS registration, contributions, coverage records, or cross-border coordination.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-social-insurance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: social-security
language: en
---

# Poland Social Insurance

Use for ZUS/eZUS navigation, payer or insured-person registration routes,
contribution records, certificates, social-insurance coverage, and cross-border
coordination. Tax filing belongs to `poland-tax`; healthcare access and medical
records belong to `poland-healthcare`.

Confirm worker, employer, business, student, family, or other stated coverage
context; relevant country or countries; locality; period; deadline; and whether
the request concerns public guidance or an official-service handoff. Do not
collect PESEL, account data, contribution amounts, health data, credentials, or
personal-record content in plugin tools.

Use current public ZUS and official EU coordination sources. Name unresolved
coverage questions and show the competent institution and evidence categories.
Do not decide coverage or benefit entitlement from incomplete facts.

For requested eZUS help, apply `../../references/automation-playbook.md`. The
user authenticates and performs signatures and attestations. After explicit task
scope, a caller-owned tool may inspect relevant contribution, insurance, or
message records and fill necessary fields. Filing, send, booking, payment
initiation, upload, download, or record correction requires action-time
confirmation; final payment authorization remains with the user.

Route employment rights to `poland-employment-rights`, work permission to
`poland-work-authorization`, healthcare to `poland-healthcare`, and family or
social-assistance benefits to `poland-benefits-support`. Read
`../../references/work-tax-business.md`.
