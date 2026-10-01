---
name: poland-work-authorization-xopoko
title: Poland Work Authorization
description: Work authorization. Use for permission to work in Poland, employer permits, declarations, notifications, or labour-market access.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-work-authorization
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: immigration
language: en
---

# Poland Work Authorization

Use for whether a work-authorization route may be needed, employer-side permits
or declarations, notifications, exemptions, and the interaction between work
access and residence status. Employment contracts and workplace disputes belong
to `poland-employment-rights`.

Confirm citizenship/status group, current stated work-access basis, employer or
worker perspective, broad work type, location, intended start date, and whether
residence depends on the job. Keep unknown branches separate; do not assume that
all foreign workers use one permit or authority.

Use current Office for Foreigners, Gov.pl, Biznes.gov.pl, and public employment
service records. Identify the responsible actor, authority, current channel,
evidence categories, residence dependency, and human filing boundary. Verify
forms, deadlines, and exemptions at action time. Do not conclude that work is
lawful or unlawful from incomplete facts.

Hands-on service assistance follows `../../references/automation-playbook.md`.
The actor who owns the account authenticates, signs, and accepts employer or
applicant declarations. After that actor explicitly scopes the task, a
caller-owned tool may inspect relevant records and fill necessary fields.
Server-side draft creation, upload, download, send, notice filing, or submission
requires a fresh action-time confirmation and receipt check.

Treat praca.gov.pl as the public map and protected filing channel for relevant
employer-side permits, declarations, and notifications, not as the worker's
universal portal. Identify whether the foreigner, employer or other entrusting
entity, or voivode owns each step before planning it. Any authenticated
employer-side action requires authorization from the employer or its authorized
human representative; the foreign worker's authorization alone is insufficient.

For EU Blue Card questions, compose this skill with `poland-stay-residence` and
use `mos-eu-blue-card` plus `udsc-mos-electronic-residence`. Live-verify the
salary threshold and reference period, qualification route, contract conditions,
regulated-profession branch, employer-change or notification rule, and mobility
branch. Keep the foreigner's application, the employer's signed attachment, and
the voivode's decision and in-person follow-up distinct; do not conclude
eligibility or operate either party's portal.

Route stay consequences to `poland-stay-residence`, contract rights to
`poland-employment-rights`, tax to `poland-tax`, and ZUS registration or coverage
to `poland-social-insurance`. Read
`../../references/work-tax-business.md` and the Blue Card actor map in
`../../references/immigration-status-map.md`.
