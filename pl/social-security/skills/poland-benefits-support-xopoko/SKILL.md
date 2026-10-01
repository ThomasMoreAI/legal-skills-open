---
name: poland-benefits-support-xopoko
title: Poland Benefits and Public Support
description: Benefits support. Use for Polish family benefits, social assistance, disability support, or Empatia routes.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-benefits-support
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: social-security
language: en
---

# Poland Benefits and Public Support

Use for family-benefit, social-assistance, disability-support, and Empatia or
municipality-owned public-support navigation. School, childcare, and university
administration belong to `poland-family-education`.

Confirm the benefit or support category, relevant person's citizenship/status
group, household category without names or financial values, locality, benefit
period, deadline, and whether an official decision already exists. Do not infer
entitlement or request account, income, health, or identity records in plugin
tools.

Use current Gov.pl, ministry, Empatia, and competent municipal or disability
support sources returned by the registry. Identify the responsible authority,
current period and public channel, evidence categories, locality variation, and
official landing-page handoff. Verify amounts, thresholds, dates, and forms from
public official pages at action time. Do not infer entitlement or promise an
award.

For requested hands-on help, follow `../../references/automation-playbook.md`.
After user-only authentication and explicit task scope, a caller-owned tool may
inspect the relevant case record and fill necessary fields. Submission, appeal,
upload, download, or other external effect requires action-time confirmation;
signatures, attestations, and final payment authorization remain with the user.

Route school or childcare administration to `poland-family-education`, social
insurance to `poland-social-insurance`, residence dependencies to
`poland-stay-residence`, and adverse decisions to `poland-appeals-review`. Read
`../../references/daily-life-map.md`.
