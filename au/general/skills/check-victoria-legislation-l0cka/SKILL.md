---
name: check-victoria-legislation-l0cka
title: Check Victoria Legislation
description: Verify the identity, status, point-in-time version, commencement and currency of Victorian Acts and statutory rules using the official Victorian legislation publisher. Use when a user asks whether Victorian legislation is in force or repealed, which version applied on a date, or whether a citation or supplied provision matches the official text, for current or historical Victorian legislative text and provision checks. Do not use for Commonwealth or other State or Territory legislation, Bills, case law, court deadlines, interpretation, application or final legal advice.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-legal-research/skills/check-victoria-legislation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: general
language: en
---

# Check Victoria Legislation

Use `legislation.vic.gov.au` as the controlling source. Produce a provenance
record, not a bare assertion that legislation is "current".

Read [the shared point-in-time method](../../references/point-in-time-method.md)
before performing a check. It defines the official-source rules, identity
resolution, point-in-time selection and fail-closed boundary shared by every
State and Territory checker in this plugin.

## Workflow

1. Fix the scope.
   - Accept Victorian Acts and statutory rules.
   - Record the exact title, provision and requested date. If no date is
     given, use today's `Australia/Melbourne` date and state it explicitly.
   - Return `OUTSIDE SCOPE` for Bills, another jurisdiction, case treatment or
     a request for legal advice.
2. Resolve identity.
   - Search `legislation.vic.gov.au` and identify one official title and
     legislation type. Treat multiple plausible titles as ambiguous.
3. Select the point-in-time version.
   - Select the official authorised version covering the requested date.
   - Record its version number or effective date range, the title's present
     status and the exact URL.
   - Keep the title's present status separate from whether the selected
     version operated on the requested date.
4. Check commencement and currency.
   - Inspect the displayed commencement, amendment, version-history and
     currency information relevant to the provision.
   - Do not infer operation from an as-made document or a URL date alone.
5. Report using the required result contract.

## Result contract

Lead with one status:

- `VERIFIED` — one official title and applicable version were identified with
  no unresolved qualification relevant to the request.
- `VERIFIED WITH QUALIFICATIONS` — identity and version were established, but
  an identified commencement, currency or authorisation limitation matters.
- `NOT VERIFIED` — official evidence is missing, inconsistent or insufficient.
- `OUTSIDE SCOPE` — the request is outside this Victorian metadata and text
  check.

Then provide:

```text
Requested check: <legislation and provision, if any>
Jurisdiction: Victoria, Australia
As at: <YYYY-MM-DD>
Official title: <title>
Type: <Act / statutory rule>
Current title status: <In force / Repealed / other official status>
Applicable version: <authorised version number and effective date range>
Commencement evidence: <official commencement material inspected, or not established>
Currency flags: <none or itemised flags>
Official sources: <exact official pages actually inspected>
Checked: <date and Australian timezone>
Limitations and review: <what remains unverified and the human-review point>
```

Cite the exact official page supporting each field. Never describe the result
as legal advice or as proof of interpretation, application or legal effect.

## Fail closed

Return `NOT VERIFIED` instead of guessing when the title or type is ambiguous,
the requested date cannot be tied to a displayed authorised version, the
official publisher is unavailable, or a relevant commencement, amendment or
currency issue cannot be resolved. Case law is outside scope.
