---
name: compliance-check-josstei
title: Maestro Compliance Check
description: Run a Maestro-style regulatory compliance review for GDPR/CCPA, cookie consent, data handling, and licensing
author: josstei
author_url: https://github.com/josstei/maestro-orchestrate/tree/main/claude/skills/compliance-check
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# Maestro Compliance Check

Call `get_skill_content` with resources: ["architecture"].

## Protocol

Before delegating, call `get_skill_content` with resources: ["delegation"] and follow the returned methodology.

## Workflow

1. Identify applicable regulations and define audit scope
2. Review data handling patterns, user disclosures, consent flows, retention policies, and third-party integrations
3. Audit regulatory compliance: GDPR/CCPA, cookie consent, data residency, licensing, and open-source obligations
4. Present findings with regulatory reference, severity, compliance risk, and recommended actions
5. Distinguish legal-risk observations from code-level bugs

## Constraints

- Present findings before proposing remediation
- Do not modify code without explicit user approval
