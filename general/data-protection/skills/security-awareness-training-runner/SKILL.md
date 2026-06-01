---
name: security-awareness-training-runner
title: security-awareness-training-runner
description: This skill designs and runs the security awareness training programme for all employees. Use when asked to create security training, run phishing simulations, or track training completion rates. Also consider when SOC 2 requires evidence of security awareness training. Suggest when the user onboards employees without security training.
author: mittuled
author_url: https://github.com/mittuled/skill-os/tree/main/agents/legal/security-compliance-programme-manager/security-awareness-training-runner
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# security-awareness-training-runner

## Agent: Security & Compliance Programme Manager

L2 security and compliance programme manager (1x) responsible for SOC 2, security awareness training, disaster recovery, GDPR/CCPA compliance, and penetration test programme management.

Department ethos: [ideal-legal.md](../../../../departments/legal/ideal-legal.md)

## Skill Description

Designs, deploys, and manages the security awareness training programme including onboarding training, annual refreshers, phishing simulations, and role-based security education for all employees and contractors.

## When to Use

- When the company needs to establish or refresh its security awareness training programme to meet SOC 2, GDPR, or customer contractual requirements.
- When onboarding new employees or contractors who must complete security training before accessing company systems and data.
- When a security incident or phishing campaign reveals gaps in employee security awareness that require targeted remediation training.

## Workflow

1. **Training Needs Assessment**: Identify regulatory requirements (SOC 2 CC1.4, GDPR Article 39, HIPAA), contractual obligations, and organizational risk areas that training must address. Segment the audience by role (engineering, sales, executives, contractors) to identify role-specific training needs. Deliverable: training needs matrix with regulatory sources, audience segments, and topic priorities.
2. **Curriculum Design**: Design the training curriculum covering core topics (phishing recognition, password hygiene, social engineering, data classification, incident reporting, acceptable use, physical security) and role-specific modules (secure coding for engineers, data handling for customer-facing roles, wire fraud awareness for finance). Deliverable: training curriculum with module descriptions, learning objectives, and assessment criteria.
3. **Training Deployment**: Deploy training through the selected platform (LMS or third-party security training provider). Schedule onboarding training for new hires, annual refresher for all employees, and targeted modules triggered by incidents or role changes. Deliverable: training deployment schedule with enrollment confirmations.
4. **Phishing Simulation Programme**: Design and execute regular phishing simulations (monthly or quarterly) with escalating sophistication. Track click rates, report rates, and credential submission rates. Provide immediate educational feedback to employees who fail simulations. Deliverable: phishing simulation results report with trend analysis.
5. **Compliance Tracking and Reporting**: Track training completion rates, overdue assignments, and assessment scores. Generate compliance reports for SOC 2 auditors, management, and regulatory submissions. Escalate non-completion to managers with defined consequences. Deliverable: training compliance dashboard and quarterly completion report.

## Anti-Patterns

- **Annual checkbox training only**: Running a single annual training module with no reinforcement, simulations, or follow-up throughout the year. *Why*: security awareness degrades without reinforcement; a single annual session produces compliance evidence but not actual behavior change.
- **One-size-fits-all content**: Delivering the same generic training to all roles regardless of their specific risk exposure and access levels. *Why*: an engineer needs secure coding training, not wire fraud awareness; a CFO needs BEC (business email compromise) training, not API security; role relevance drives engagement and effectiveness.
- **Punitive-only failure response**: Disciplining employees who fail phishing simulations without providing additional education. *Why*: punitive approaches suppress incident reporting; employees who fear punishment will not report actual phishing attempts, increasing organizational risk.

## Output

**On success**: Produces the security awareness training programme containing the curriculum, deployment schedule, phishing simulation results, completion tracking dashboard, and quarterly compliance report. Delivered to security leadership, HR, and SOC 2 auditors.

**On failure**: Report which training modules could not be deployed (e.g., LMS integration issues, content not approved), what completion gaps exist, and what remediation steps are planned with revised timelines.

## Related Skills

- [`soc2-programme-manager`](../soc2-programme-manager/SKILL.md) -- SOC 2 requires evidence of security awareness training; completion reports are a key audit artifact.
- [`gdpr-ccpa-compliance-manager`](../gdpr-ccpa-compliance-manager/SKILL.md) -- GDPR requires data protection awareness training; privacy-specific modules should be coordinated with the broader training programme.
