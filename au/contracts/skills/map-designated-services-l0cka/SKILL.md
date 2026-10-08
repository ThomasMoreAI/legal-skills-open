---
name: map-designated-services-l0cka
title: Map Designated Services
description: Map whether services described by an Australian legal practice are designated services under table 6 of subsection 6(5B) of the Anti-Money Laundering and Counter-Terrorism Financing Act 2006 (Cth), applying AUSTRAC's sufficiently-linked principles, the customer definition, standing exemptions and the incidental trust-money exemption, with every item verified against official sources. Use when a practice needs to know if a service line, engagement type or proposed offering may trigger AML/CTF obligations. Do not use for other tranche 2 sectors, for tranche 1 services, to decide enrolment or to give final legal advice — an unmapped service fails closed to human review.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-aml-ctf/skills/map-designated-services
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: contracts
language: en
---

# Map Designated Services

Map described legal services to the designated services in table 6 of the
amended AML/CTF Act. Separate designated, not designated and cannot be
determined — never guess and never clear a service the registry does not
cover.

Read the [source and control method](../../references/aml-ctf-source-and-control-method.md),
use an approved profile per the
[practice profile schema](../../references/aml-ctf-practice-profile-schema.md)
and work from the
[designated services registry](references/designated-services-registry.json).

## Workflow

1. Fix the services and time.
   - Record each service to be mapped: what the practice actually does, for
     whom, the client-facing outcome and whether it is current or proposed.
     Record the date of assessment.
   - Require an approved, current practice profile; record any gap.
2. Map each service against the registry.
   - Test the described activity against each table 6 item in the registry,
     applying the recorded scope notes: the sufficiently-linked principles
     (assistance must directly advance the transaction, creation or
     restructure — merely influencing, general advice or ancillary services
     is not enough), the in-the-course-of-carrying-on-a-business element,
     the external-customer requirement and, for items 1–2, the
     court-or-tribunal-order carve-out.
   - Verify the item text and any decisive element against the Act through
     `$check-commonwealth-legislation` at the assessment date; record the
     AUSTRAC guidance section relied on with its last-updated date.
3. Test exemptions as claims, not conclusions.
   - Where the profile claims a standing exemption (legal aid commission,
     community legal centre, barrister acting for Australian government
     bodies) or the incidental trust-money position under subsection 6(5C),
     record the claimed basis and its decisive facts. Note that the
     trust-money exemption operates at the level of the whole practice, so
     any designated service elsewhere in the practice defeats it.
4. Assemble the map.
   - For each service: `designated` (item number, why each element is met),
     `not designated` (which element fails and why) or
     `cannot be determined` (what fact or verification is missing). Note the
     geographical-link element as a separate check for cross-border
     services.
   - Flag consequences for human decision only — enrolment timing and
     obligations are stated as verified propositions with sources, never as
     directions.
5. Set the human decision gate.
   - Name the reviewer who must confirm the mapping, resolve every
     `cannot be determined` entry and decide any next step.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Services assessed: <service; current or proposed; assessment date>
Profile: <approved identifier and version>
Mapping: <service → designated (item, elements met) | not designated
  (failing element) | cannot be determined (missing fact)>
Exemption claims: <claimed basis; decisive facts; evidence state>
Verified: <provision or guidance; source URL; evidence state; checked date>
Out of scope flags: <non-legal sector services, tranche 1 services, IFTI>
Human decision gate: <reviewer; unresolved entries; decisions required>
Limitations: <mapping is issue-spotting, not advice; no enrolment action>
```

## Fail closed

Return `NOT READY` when a decisive fact about the service, the customer or
the profile cannot be established, and mark any service the registry does
not cover `cannot be determined` — never `not designated`. Never map
services of other tranche 2 sectors or tranche 1 entities, never conclude an
exemption applies, and never treat AUSTRAC guidance as the statute it
interprets.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`.
  Verifies the AML/CTF Act, Rules and amending instruments against the Federal
  Register of Legislation.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
