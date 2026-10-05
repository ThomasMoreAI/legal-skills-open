---
name: check-australian-privacy-principles-l0cka
title: Check Australian Privacy Principles
description: Verify the Australian Privacy Principles and their application framework from current official sources; distinguish APP text, coverage and exemptions, regulations and registered codes, known future amendments and versioned OAIC guidance; detect change across a decision horizon; and return fail-closed statuses for downstream privacy, breach and AI assessments. Use whenever an Australian workflow relies on an APP or reuses an earlier APP analysis. Do not treat schema-valid user JSON as verified law or use case law.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-privacy-cybersecurity/skills/check-australian-privacy-principles
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: data-protection
language: en
sources:
- title: App Verification Method
  path: references/app-verification-method.md
---

# Check Australian Privacy Principles

Verify every fact-triggered APP framework layer before applying an APP. Never
assume that the text, application perimeter, instruments, codes, future changes
or guidance remains unchanged.

Read [references/app-verification-method.md](references/app-verification-method.md)
before starting.

## Workflow

1. Fix dates and facts.
   - Record the legal as-at date and decision horizon, including deployment,
     contract, retention and review dates actually known.
   - Identify the relevant entity, conduct, location, information, exemption,
     code and instrument facts. Do not invent a future horizon.
2. Establish official versions.
   - Invoke `$check-commonwealth-legislation` for the Privacy Act, Schedule 1
     and every material application provision at the as-at date.
   - Invoke `$trace-commonwealth-legislative-change` through the horizon when a
     version boundary, amendment or commencement may intervene.
   - Check current Privacy Regulations and the OAIC registered-code inventory.
     Treat OAIC APP text and Guidelines as regulator material, not legislation.
3. Build provenance-bound inventories.
   - Inspect complete Schedule 1 boundaries and enumerate every displayed APP
     without a hard-coded count or list.
   - Capture the official canonical and final URL, effective period, retrieval
     timestamp, raw document SHA-256 and the complete text needed for
     fingerprinting. Do not reproduce full statutory text in the work product.
   - Fingerprint the application perimeter, applicable regulations and codes,
     and versioned guidance as separate layers using the reference schema.
4. Compare deterministically.

   ```bash
   python3 <skill-root>/scripts/compare_app_inventory.py validate <inventory.json>
   python3 <skill-root>/scripts/compare_app_inventory.py compare \
     <earlier.json> <later.json> --horizon <YYYY-MM-DD>
   ```

   `validate` returns only `INVENTORY SCHEMA VALID`. The script cannot prove
   that supplied content is official and never independently returns `APP
   FRAMEWORK VERIFIED`. The helper is optional, read-only and offline. Without
   command execution, perform the same comparison manually and record that the
   scripted check was not run.
5. Apply fail-closed statuses.
   - Use `APP FRAMEWORK VERIFIED` only after legislation checks establish the
     official source, applicable period, complete Schedule and every
     fact-triggered layer.
   - Use `APP FRAMEWORK CHANGE DETECTED – LEGAL CONTENT REVIEW REQUIRED` for an
     APP text, application-perimeter, regulation or applicable-code change.
   - Use `APP TEXT UNCHANGED – APPLICATION LAW REVIEW REQUIRED` for a mapped
     future change or unresolved application layer.
   - Use `GUIDANCE REFRESH REQUIRED` for a guidance-only change, separately
     from statutory status.
   - Use `APP FRAMEWORK NOT VERIFIED – DO NOT RELY` whenever any required
     source, version, Schedule boundary, layer or comparison is unresolved.

## Result contract

Lead with the overall fail-closed status, then provide:

```text
As at and decision horizon: <dates and Australia/Sydney timezone>
APP text status: <source, compilation, effective period and comparison>
Application perimeter status: <definitions, coverage, exemptions and provisions>
Codes and instruments status: <Privacy Regulations and applicable registered code>
Known future amendments: <mapped change and horizon effect>
Guidance status: <page versions and refresh result>
Inventory: <identifier, heading, clause range and SHA-256 for every APP>
Official sources: <links actually inspected>
Downstream effect: <proceed, refresh or do not rely>
Limitations and lawyer review: <unresolved legal or factual issues>
```

Case law is outside scope. Framework verification does not prove entity
coverage, compliance, interpretation or application to the facts.

<!-- generated:plugin-dependencies -->
## Other plugins

This skill names skills from other Legal Skills plugins. Install a required
plugin alongside this one; install a hand-off plugin when the matter needs
that depth.

- `australian-legal-research` (required): `check-commonwealth-legislation`,
  `trace-commonwealth-legislative-change`. Verifies the Commonwealth, state
  and territory legislation the privacy, breach and cyber workflows rely on.

If a named skill is not available in this session, say so and name the plugin
to install. Treat the step it would have performed as not done: record the
affected proposition as not verified, or the hand-off as not made. Never
perform that step from memory or substitute a different skill.
<!-- end:plugin-dependencies -->
