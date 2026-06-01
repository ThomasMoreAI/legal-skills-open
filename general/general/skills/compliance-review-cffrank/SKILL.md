---
name: compliance-review-cffrank
title: Compliance Review
description: Audit agent behavior against company policies. Use when running periodic compliance checks, investigating policy violations, or producing compliance sections for board reports. Checks budget adherence, task freshness, escalation chain compliance, and approval gate enforcement.
author: cffrank
author_url: https://github.com/cffrank/paperclip-governance/tree/master/skills/compliance-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Compliance Review

Verify agents are following company policies. Run on the cadence defined in governance context.

## Before Starting

Read company-governance-context for:
- Compliance requirements
- Stale task threshold
- Blocked task escalation threshold
- Any specific policies to enforce

## Review Procedure

### 1. Budget Compliance

Check that all agents are operating within their budget:
- `GET /api/companies/{companyId}/costs/by-agent`
- Any agent spending above allocation without approval → violation
- Any agent auto-paused for budget exhaustion → note (may be intentional)

### 2. Task Freshness

Check for stale work:
- `GET /api/companies/{companyId}/issues?status=in_progress`
- Any task in_progress beyond stale threshold → violation
- Any task blocked beyond escalation threshold without escalation comment → violation

### 3. Escalation Chain Compliance

Check that escalations are being honored:
- `GET /api/companies/{companyId}/activity`
- Look for blocked tasks: was the chain of command notified?
- Look for approval requests: were they responded to in reasonable time?

### 4. Approval Gate Compliance

Check that governed actions went through approval:
- Agent hires: was approval requested and granted?
- Budget changes: was proper authority exercised?
- Strategic decisions: was the human board consulted per governance context?

### 5. Record Findings

For each violation or concern:
1. Use decision-protocol to record the finding
2. Severity: info (process improvement) / warning (needs attention) / violation (requires remediation)
3. For violations: create remediation issue, assign to the responsible agent's manager

## Output

Post compliance review as issue comment or document. Include:
- Review period
- Checks performed
- Findings (with evidence)
- Remediation actions created

For the full audit checklist, read `references/audit-checklist.md`.

## Related Skills

- company-governance-context defines policies to enforce
- decision-protocol records compliance findings
- escalation-protocol if systemic violations found
- governance-reporting consumes compliance review for board reports
