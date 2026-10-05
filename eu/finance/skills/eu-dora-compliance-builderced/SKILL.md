---
name: eu-dora-compliance-builderced
title: EU DORA Compliance (Digital Operational Resilience Act)
description: Implement DORA Regulation (2022/2554) digital operational resilience for financial entities — ICT risk management, incident reporting, resilience testing, third-party risk.
author: BuilderCed
author_url: https://github.com/BuilderCed/agent-skills/tree/main/skills/compliance/eu-dora-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: finance
language: en
---

# EU DORA Compliance (Digital Operational Resilience Act)

> **DISCLAIMER**: This skill provides guidance only. It does not constitute legal or financial advice. Always verify with qualified professionals.

## When to Use

- Building software for financial institutions in the EU
- Assessing ICT risk management for fintech
- Setting up ICT incident reporting for financial entities
- Designing resilience testing programs
- Managing third-party ICT service provider relationships

## Scope — Who Is Affected?

DORA applies to virtually all EU financial entities:

| Category | Entities |
|----------|---------|
| Banking | Credit institutions, payment institutions, e-money institutions |
| Investment | Investment firms, trading venues, central securities depositories |
| Insurance | Insurance/reinsurance undertakings, intermediaries |
| Pension | IORPs (Institutions for Occupational Retirement Provision) |
| Crypto | Crypto-asset service providers (MiCA-regulated) |
| Infrastructure | CCPs, trade repositories, securitization repositories |
| Other | Credit rating agencies, crowdfunding providers, data reporting services |
| ICT providers | Third-party ICT service providers to the above (critical designation) |

## 5 Pillars of DORA

### Pillar 1: ICT Risk Management (Articles 5-16)

Establish an ICT risk management framework:
- **Identify** all ICT assets, risks, dependencies
- **Protect** through security policies, access controls, encryption
- **Detect** anomalies and incidents via continuous monitoring
- **Respond** with incident response and crisis communication plans
- **Recover** with backup policies, restoration procedures, lessons learned

### Pillar 2: ICT Incident Reporting (Articles 17-23)

Classify and report major ICT-related incidents:

| Criterion | Threshold for Major |
|-----------|-------------------|
| Clients affected | > 10% of clients or significant clients |
| Duration | > 2 hours for critical services |
| Geographic spread | > 2 member states |
| Data loss | Integrity, confidentiality, or availability compromised |
| Economic impact | Material financial loss |
| Criticality of services | Core banking, payment processing, trading |

**Reporting timeline**:
- Initial notification: within 4 hours of classification as major
- Intermediate report: within 72 hours
- Final report: within 1 month

### Pillar 3: Digital Operational Resilience Testing (Articles 24-27)

| Test Type | Frequency | Who |
|-----------|-----------|-----|
| Vulnerability assessments | At least annually | All entities |
| Network security testing | At least annually | All entities |
| Scenario-based testing | At least annually | All entities |
| Threat-Led Penetration Testing (TLPT) | At least every 3 years | Significant entities only |

TLPT must be conducted by qualified external testers following the TIBER-EU framework.

### Pillar 4: Third-Party ICT Risk (Articles 28-44)

For all ICT third-party service providers:
- Maintain a register of all ICT service agreements
- Conduct pre-contract due diligence
- Include mandatory contractual clauses (audit rights, exit strategies, data location)
- Monitor ongoing compliance
- Have exit plans for critical providers

**Critical ICT third-party providers** (designated by ESAs) face direct EU oversight.

### Pillar 5: Information Sharing (Article 45)

Financial entities may participate in voluntary information-sharing arrangements on:
- Cyber threat intelligence
- Indicators of compromise
- Tactics, techniques, and procedures (TTPs)
- Security alerts and configuration tools

## Key Date

- **17 January 2025**: DORA fully applicable

## What This Skill Does NOT Do

- Does not conduct penetration testing or TLPT
- Does not configure ICT security tools
- Does not manage third-party provider contracts
- Does not replace compliance officer or legal counsel
