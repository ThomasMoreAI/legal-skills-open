---
name: poland-tax-xopoko
title: Poland Tax
description: Poland tax. Use for PIT, tax-residence orientation, tax identifiers, e-Tax Office, or official filing routes.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-tax
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: tax
language: en
---

# Poland Tax

Use for PIT and other official tax-process orientation, tax-year routing, NIP
questions, e-Tax Office, filing channels, tax-office appointments, and source
verification. Social-insurance contributions and eZUS belong to
`poland-social-insurance`.

Confirm tax year, income or activity categories without amounts, employment or
business context, cross-border countries, stated deadline, and whether the user
needs public guidance, a generic placeholder draft, or an official landing-page
handoff.
Do not collect identifiers, account data, tax records, or credentials in plugin
tools.

Use current Ministry of Finance, podatki.gov.pl, and National Revenue
Administration records. State the period, competent office or service, known
assumptions, missing facts, freshness, and human action boundary. Do not decide
tax residence, choose deductions, optimize tax, calculate liability from an
incomplete case, or accept a tax declaration's truth for the user.

For requested e-Tax Office or filing assistance, apply
`../../references/automation-playbook.md`. The user authenticates, signs or
attests, and completes final payment authorization. Explicit task scope permits
minimum relevant record inspection and form filling; booking, correction,
server-side draft creation, payment initiation, upload, download, or submission
requires fresh action-time confirmation. Recheck calculated values and current
official rules before the checkpoint.

Route business formation to `poland-business`, ZUS to
`poland-social-insurance`, cross-border free movement to `poland-eu-mobility`,
and adverse decisions to `poland-appeals-review`. Read
`../../references/work-tax-business.md`.
