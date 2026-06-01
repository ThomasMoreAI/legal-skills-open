---
name: compliance-policy-auditor
title: Compliance Policy Auditor
description: Audit corporate policies or data-handling descriptions against regulatory  frameworks (GDPR, SOC2, HIPAA). Use when users need to identify compliance  gaps or risk levels in technical procedures.
author: CreativeActtech
author_url: https://github.com/CreativeActtech/llm-skills/tree/main/skills/example-skill/compliance-policy-analyzer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
tags: [legal, compliance, audit, security, risk]
---

# Compliance Policy Auditor
Systematically reviews technical or procedural documentation to identify 
alignment or deviations from major regulatory frameworks.

## 🎯 When to Use
- User provides a "Privacy Policy" or "Data Retention Plan" for review.
- User asks: "Is this process SOC2 compliant?" or "What GDPR risks exist here?"
- **Do NOT use** for providing binding legal advice or drafting contracts.
- **Do NOT use** for auditing physical security (cams, locks) unless documented.

## 🧠 Core Workflow
**Step 1 — Scope & Framework Selection**
IF user specifies a framework (GDPR/SOC2/HIPAA/ISO27001), prioritize its rules; 
ELSE, apply General Data Protection principles.

**Step 2 — Data Mapping**
Identify PII (Personally Identifiable Information), PHI (Protected Health 
Information), or PCI data mentioned in the text.

**Step 3 — Gap Analysis**
1. **Data Minimization** — Check if only necessary data is collected.
2. **Access Control** — Audit description of "Who has access" (RBAC).
3. **Security Measures** — Identify encryption, hashing, and log requirements.

**Step 4 — Risk Scoring**
Assign Severity (Critical/Major/Minor) to gaps based on regulatory fine potential.

**Step 5 — Return Output**
Provide a structured JSON audit report.

## 📋 Output Format
```json
{
  "frameworks_evaluated": ["GDPR", "SOC2"],
  "pii_detected": ["email", "IP address"],
  "findings": [
    {
      "severity": "critical",
      "category": "Data Retention",
      "issue": "Policy states data is kept indefinitely.",
      "remediation": "Define a 7-year purge cycle per Article 5(1)(e)."
    }
  ],
  "risk_summary": "1 Critical Gap detected. High risk of non-compliance."
}
```

## ⚠️ Fallback Behavior
IF the input text is too vague to audit:

ASK for specific details regarding data storage, user consent, or encryption
