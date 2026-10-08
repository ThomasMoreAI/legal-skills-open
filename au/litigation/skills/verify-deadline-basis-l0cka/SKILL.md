---
name: verify-deadline-basis-l0cka
title: Verify Deadline Basis
description: Verify the computation-rule tables and holiday tables that the Australian litigation-deadlines workflows rely on against the official publishers — legislation sites for Interpretation Acts, court rules and tribunal Acts, and government publications for public holidays — recording source URL, version identifier, checked date and a table fingerprint, and detecting changes since the last verification. This is the only path that moves a table entry to the verified state that activates computation. Use before first computed reliance in a matter, on the profile's verification posture, or when a rule amendment is suspected. Do not use to compute dates, to verify Acts that the Australian Legal Research checkers cover, or to bypass a publisher's bot protections.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-litigation-deadlines/skills/verify-deadline-basis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: litigation
language: en
---

# Verify Deadline Basis

Verify the tables computation depends on, entry by entry, against the
official publishers, and record the evidence. An entry stays
`pending-verification` — and the script keeps refusing to compute from it —
until this workflow confirms it.

Read the [source and control method](../../references/litigation-deadlines-source-and-control-method.md)
and verify the [computation-rule tables](../../references/computation-rules/)
and [holiday tables](../../references/holidays/).

## Workflow

1. Fix the verification scope.
   - Record which tables and entries the matter relies on, the assessment
     date and the previous fingerprint if one exists.
2. Verify each entry against its publisher.
   - For Acts (Interpretation Acts, Limitation Acts, tribunal Acts), route
     to the Australian Legal Research checkers
     (`$check-commonwealth-legislation`, `$check-nsw-legislation`,
     `$check-victoria-legislation` or the applicable sibling) and record
     the result.
   - For court rules and procedural instruments, check the official
     legislation publisher for the jurisdiction directly: confirm the
     provision exists, its current text supports the table's summary and
     period, and record the version identifier and checked date. Never
     bypass a publisher's bot protections; an unreachable source leaves the
     entry `pending-verification`.
   - For holiday tables, check the official government publication, confirm
     the dates and uncertain windows, and record the page's last-updated
     signal.
3. Record the outcome.
   - For each entry: `VERIFIED`, `VERIFIED WITH QUALIFICATIONS` or
     `NOT VERIFIED`, with source URL, version identifier and checked date.
     Compute a fingerprint over the verified table content and compare with
     the previous fingerprint; report every change as a change, never
     silently.
   - Present table updates as drafts for the practice to apply and store —
     the workflow itself marks nothing verified without the human applying
     the update.
4. Set the human decision gate.
   - Name who applies the table updates and who decides reliance where an
     entry stays `NOT VERIFIED`.

## Result contract

Lead with `READY FOR HUMAN REVIEW`, `READY WITH QUALIFICATIONS`, `NOT READY`
or `OUTSIDE SCOPE`.

```text
Scope: <tables and entries; assessment date; previous fingerprint>
Verification: <per entry: state; source URL; version; checked date>
Changes: <differences from previous fingerprint; affected period rules>
Draft updates: <table edits proposed for human application>
Human decision gate: <who applies updates; reliance decisions required>
Limitations: <verification is point-in-time; recheck per the profile's
  posture; no computation performed here; every date elsewhere remains
  provisional until confirmed>
```

## Fail closed

Return `NOT READY` when a publisher is unreachable or a provision cannot be
found — the entry stays `pending-verification` and computation stays off.
Never mark an entry verified from commentary, memory or a non-official
mirror, never bypass bot protections, and report every fingerprint change
rather than reconciling it silently.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`,
  `check-nsw-legislation`, `check-victoria-legislation`. Verifies the
  Commonwealth and state legislation behind limitation periods and deadline
  rules.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
