---
name: poland-pensions-seniors-xopoko
title: Poland Pensions and Senior Services
description: 'Pensions and senior services: route retirement, survivor benefits, cross-border contribution histories, care, and local senior support. Excludes benefit calculation or eligibility decisions.'
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-pensions-seniors
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: social-security
language: en
---

# Poland Pensions and Senior Services

Use for retirement and survivor-pension orientation, contribution-history
questions, cross-border social-security coordination, senior care, caregiver
support, and local services for older people. Do not calculate a pension,
declare entitlement, or recommend a financial product.

Capture the target benefit or service, broad insurance system and employment
history categories, countries involved, locality, known decision stage, and
deadline. Keep account identifiers, health records, and contribution statements
out of bundled CLI/MCP inputs.

Identify the responsible institution and separate national insurance, EU or
bilateral coordination, local social assistance, healthcare, and private
financial matters. Show current official sources, online versus in-person
channels, document categories, and any personal-appearance or life-certificate
requirement that must be verified. Read
`../../references/life-events-and-services.md` and the social-insurance and care
routes in `../../references/daily-life-map.md`.

For eZUS or another protected account, apply
`../../references/automation-playbook.md`. The user performs authentication,
signatures, attestations, and final payment authorization. An authorized agent
may inspect only the relevant record and prepare reviewable fields; filing,
sending, booking, uploading, downloading, or changing a record needs fresh
action-time confirmation.

Route contribution corrections and ordinary benefits to
`poland-social-insurance`, health access to `poland-healthcare`, disability
support to `poland-disability-accessibility`, tax to `poland-tax`, and a refusal
or appeal deadline to `poland-appeals-review`.
