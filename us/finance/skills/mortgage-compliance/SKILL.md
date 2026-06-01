---
name: mortgage-compliance
title: Mortgage Compliance Validation Skill
description: Validates mortgage advisor responses against three hardcoded compliance rules and returns structured JSON.
author: heyparth1
author_url: https://github.com/heyparth1/openclaw_2-Agent-workflow/tree/main/openclaw/skills/mortgage-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: finance
language: en
---

# Mortgage Compliance Validation Skill

This skill validates a mortgage advisor's response against three compliance rules:

1. **Credit Score Threshold** — Ensures correct FHA/conventional guidance based on credit score.
2. **APR Disclosure** — Ensures rate-related responses include required disclaimers.
3. **No Guarantee Language** — Ensures no definitive approval promises are made.

## Usage

This skill is invoked by the compliance-validator agent when it receives an advisor
response to evaluate. The validator outputs structured JSON following the ValidationResult schema.

## Workflow

1. Receive the borrower query and advisor response from the borrower-advisor agent.
2. Evaluate the response against all 3 rules.
3. Output a structured JSON result with per-rule verdicts, risk level, and recommended action.
