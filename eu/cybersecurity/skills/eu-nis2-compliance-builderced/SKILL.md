---
name: eu-nis2-compliance-builderced
title: EU NIS2 Compliance
description: Implement NIS2 Directive (2022/2555) cybersecurity obligations for essential and important entities — risk management, incident reporting, supply chain security.
author: BuilderCed
author_url: https://github.com/BuilderCed/agent-skills/tree/main/skills/compliance/eu-nis2-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: cybersecurity
language: en
---

# EU NIS2 Compliance

> **DISCLAIMER**: This skill provides guidance only. It does not constitute legal or cybersecurity advice. Always verify with qualified professionals.

## When to Use

- Determining if your organization falls under NIS2 scope
- Implementing cybersecurity risk management measures
- Setting up incident reporting procedures
- Auditing supply chain security
- Preparing for national authority inspections

## Step 1: Scope — Am I Affected?

NIS2 applies to entities in these sectors meeting size thresholds:

### Essential Entities (stricter obligations)
| Sector | Examples |
|--------|---------|
| Energy | Electricity, oil, gas, hydrogen, district heating |
| Transport | Air, rail, water, road |
| Banking | Credit institutions |
| Financial market | Trading venues, CCPs |
| Health | Hospitals, laboratories, pharma, medical devices |
| Drinking water | Supply and distribution |
| Waste water | Treatment |
| Digital infrastructure | DNS, TLD, cloud, data centers, CDNs, trust services |
| ICT service management (B2B) | Managed service providers, managed security providers |
| Public administration | Central government (excluding judiciary, parliament, central banks) |
| Space | Ground-based infrastructure operators |

### Important Entities (lighter obligations)
| Sector | Examples |
|--------|---------|
| Postal & courier | Services |
| Waste management | Collection, treatment |
| Chemicals | Manufacturing, production, distribution |
| Food | Production, processing, distribution |
| Manufacturing | Medical devices, computers, electronics, machinery, motor vehicles |
| Digital providers | Online marketplaces, search engines, social networks |
| Research | Research organizations |

### Size Thresholds
- **Medium**: 50-249 employees OR turnover EUR 10-50M
- **Large**: 250+ employees OR turnover > EUR 50M
- Some entities included regardless of size (DNS, TLD, qualified trust services)

## Step 2: Risk Management Measures (Article 21)

Implement at minimum:

1. **Risk analysis and information system security policies**
2. **Incident handling** — detection, response, recovery
3. **Business continuity and crisis management** — backups, disaster recovery
4. **Supply chain security** — assess security of direct suppliers
5. **Security in network and information system acquisition, development, and maintenance** — vulnerability handling, disclosure
6. **Policies and procedures to assess effectiveness** — testing, auditing
7. **Basic cyber hygiene and cybersecurity training**
8. **Cryptography and encryption policies**
9. **Human resources security, access control, and asset management**
10. **Multi-factor authentication or continuous authentication** — where appropriate

## Step 3: Incident Reporting (Article 23)

### Timeline
| Deadline | Report | Content |
|----------|--------|---------|
| 24 hours | Early warning | Is it suspected malicious? Could it have cross-border impact? |
| 72 hours | Incident notification | Initial assessment, severity, impact, indicators of compromise |
| 1 month | Final report | Root cause, mitigation, cross-border impact if any |

### Significant Incident Criteria
An incident is significant if it:
- Caused or can cause severe operational disruption or financial loss
- Has affected or can affect other natural or legal persons by causing material or non-material damage

### Reporting Authority
Report to the national CSIRT or competent authority. In France: ANSSI (Agence nationale de la securite des systemes d'information).

## Step 4: Supply Chain Security

For each critical supplier:
1. Assess their cybersecurity maturity
2. Include security requirements in contracts
3. Monitor their security posture continuously
4. Have contingency plans for supplier failure or compromise

## Step 5: Governance (Article 20)

- **Management body** must approve cybersecurity risk management measures
- **Management body** must oversee implementation
- **Management body members** must receive cybersecurity training
- **Personal liability** possible for management body members in case of non-compliance

## Penalties

| Entity Type | Max Fine |
|-------------|----------|
| Essential | EUR 10M or 2% of worldwide annual turnover (whichever is higher) |
| Important | EUR 7M or 1.4% of worldwide annual turnover (whichever is higher) |

## Key Dates

- **17 October 2024**: Transposition deadline (member states must transpose into national law)
- **17 April 2025**: List of essential and important entities established
- **17 October 2027**: Commission review of the Directive

## What This Skill Does NOT Do

- Does not perform penetration testing
- Does not configure security tools (firewalls, SIEM, etc.)
- Does not manage incident response execution
- Does not replace ANSSI or national authority guidance
