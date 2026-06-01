---
name: compliance-review
title: Purpose
description: Compliance review for auditability, GDPR/PII, retention, financial controls, consent, and regulatory traceability.
author: aydabd
author_url: https://github.com/aydabd/github-bootstrap/tree/main/templates/.github/skills/compliance-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

## Purpose

Compliance review for auditability, GDPR/PII, retention, financial controls, consent, and regulatory traceability.

## Review focus

- PII without purpose
- missing audit trail
- retention mismatch
- GDPR risk
- financial control gap
- insufficient consent

## Method

1. Inspect changed files and diff hunks relevant to this skill.
2. Use repository-native tools when available.
3. Prefer exact evidence from changed code.
4. Emit findings using the shared JSONL finding contract.
5. Avoid style-only comments unless they create maintainability or correctness risk.

## Tooling hints

- Use `grep` or editor search before opening files.
- Use `git`, `grep`, and `gh` CLI. These are universally available and sufficient for all review tasks.
- Do not depend on tools beyond `git`, `grep`, `cat`, `head`, `wc`, and `gh`.
