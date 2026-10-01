---
name: fria-assessment-fdu-ins
title: Fundamental Rights Impact Assessment (FRIA)
description: Conduct Fundamental Rights Impact Assessments (FRIA) for high-risk AI systems as required by EU AI Act Article 27. Use when (1) deployers of high-risk AI systems (Annex III) need to assess fundamental rights impacts before first use, (2) public bodies or private entities providing public services are deploying AI systems, (3) credit scoring or insurance risk assessment AI systems are being deployed (Annex III 5b, 5c), (4) evaluating impact on natural persons' fundamental rights (dignity, liberty, privacy, data protection, non-discrimination, children's rights, etc.), or (5) creating EU AI Act Article 27 compliance documentation with market surveillance notification.
author: FDU-INS
author_url: https://github.com/FDU-INS/Insurance-Skills/tree/main/Skills/fria-assessment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# Fundamental Rights Impact Assessment (FRIA)

## Overview

A Fundamental Rights Impact Assessment (FRIA) is a mandatory evaluation required by EU AI Act Article 27 for certain deployers of high-risk AI systems. It identifies risks to fundamental rights of individuals or groups and establishes mitigation measures.

## Legal Basis: Article 27

```text
┌─────────────────────────────────────────────────────────────────┐
│                    FRIA REQUIREMENT FLOW                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  High-Risk AI System (Annex III)                                │
│           │                                                      │
│           ▼                                                      │
│  ┌─────────────────────────────────────────────┐                │
│  │ Is deployer one of the following?           │                │
│  │ • Body governed by public law               │                │
│  │ • Private entity providing public services  │                │
│  │ • Credit/insurance deployer (Art 5(b),(c))  │                │
│  └─────────────────────────────────────────────┘                │
│           │                                                      │
│      YES  │  NO ──► FRIA not mandatory                          │
│           ▼                                                      │
│  ┌─────────────────────────────────────────────┐                │
│  │ CONDUCT FRIA BEFORE FIRST USE               │                │
│  │ • Identify affected persons/groups          │                │
│  │ • Identify specific risks to rights         │                │
│  │ • Determine mitigation measures             │                │
│  │ • Notify market surveillance authority      │                │
│  └─────────────────────────────────────────────┘                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## FRIA Applicability

### Deployers Required to Conduct FRIA

| Deployer Type | Description | FRIA Required |
|---------------|-------------|---------------|
| **Public Bodies** | Bodies governed by public law | ✅ Yes |
| **Public Service Providers** | Private entities providing public services (education, healthcare, social services, housing, justice) | ✅ Yes |
| **Credit Scoring Deployers** | Using AI to evaluate creditworthiness (except fraud detection) - Annex III 5(b) | ✅ Yes |
| **Insurance Risk Assessment** | Using AI for life/health insurance risk assessment and pricing - Annex III 5(c) | ✅ Yes |
| **Other Deployers** | Not in above categories | ❌ Optional |

### High-Risk AI Categories (Annex III)

| Category | Ref. | Description |
|----------|------|-------------|
| **Biometrics** | 1(a) | Remote biometric identification systems |
| **Biometrics** | 1(b) | Biometric categorisation by sensitive attributes |
| **Biometrics** | 1(c) | Emotion recognition systems |
| **Education** | 3(a) | Access/admission to educational institutions |
| **Education** | 3(b) | Evaluation of learning outcomes |
| **Education** | 3(c) | Assessing appropriate education level |
| **Education** | 3(d) | Monitoring prohibited student behaviour during tests |
| **Employment** | 4(a) | Recruitment, job advertisements, filtering applications |
| **Employment** | 4(b) | Decisions on work terms, promotion, termination, task allocation |
| **Essential Services** | 5(a) | Eligibility for public assistance benefits |
| **Essential Services** | 5(b) | Creditworthiness and credit scoring |
| **Essential Services** | 5(c) | Life and health insurance risk assessment |
| **Essential Services** | 5(d) | Emergency call classification and dispatch |
| **Law Enforcement** | 6(a) | Assessing risk of becoming victim of crime |
| **Law Enforcement** | 6(b) | Polygraphs and similar tools |
| **Law Enforcement** | 6(c) | Evaluating reliability of evidence |
| **Law Enforcement** | 6(d) | Assessing offending/re-offending risk |
| **Law Enforcement** | 6(e) | Profiling during criminal investigation |
| **Migration/Asylum** | 7(a) | Polygraphs by public authorities |
| **Migration/Asylum** | 7(b) | Risk assessment for migration/security/health |
| **Migration/Asylum** | 7(c) | Examining asylum/visa/residence applications |
| **Migration/Asylum** | 7(d) | Identifying natural persons in migration context |
| **Justice/Democracy** | 8(a) | Assisting judicial authorities |
| **Justice/Democracy** | 8(b) | Influencing elections or voting behaviour |

## Fundamental Rights to Assess

### EU Charter of Fundamental Rights

| Right | Charter Article | Assessment Focus |
|-------|-----------------|------------------|
| **Human Dignity** | Art. 1 | Respect for inherent worth, no degrading treatment |
| **Right to Liberty and Security** | Art. 6 | Freedom from arbitrary detention/restriction |
| **Respect for Private and Family Life** | Art. 7 | Privacy in home, family, communications |
| **Protection of Personal Data** | Art. 8 | Data processing lawfulness, purpose limitation, accuracy |
| **Freedom of Expression and Information** | Art. 11 | Receive/impart information without interference |
| **Non-discrimination** | Art. 21 | No discrimination based on protected characteristics |
| **Rights of the Child** | Art. 24 | Best interests of child, protection, wellbeing |
| **Rights of the Elderly** | Art. 25 | Dignity, independence, participation |
| **Integration of Persons with Disabilities** | Art. 26 | Independence, integration, participation |
| **Workers' Rights** | Arts. 27-32 | Working conditions, fair treatment, collective rights |
| **Right to an Effective Remedy** | Art. 47 | Access to justice, fair trial |

## Risk Assessment Methodology

### Likelihood x Severity Matrix

```text
                    SEVERITY
                    Low    Medium    High
              ┌─────────┬─────────┬─────────┐
         High │ MEDIUM  │  HIGH   │CRITICAL │
              ├─────────┼─────────┼─────────┤
LIKELIHOOD Med│  LOW    │ MEDIUM  │  HIGH   │
              ├─────────┼─────────┼─────────┤
         Low  │MINIMAL  │  LOW    │ MEDIUM  │
              └─────────┴─────────┴─────────┘
```

### Likelihood Assessment Criteria

| Level | Description | Indicators |
|-------|-------------|------------|
| **High** | Very likely to occur | History of similar issues, inherent system design risk, vulnerable population |
| **Medium** | Possible under certain conditions | Conditional triggers, partial safeguards |
| **Low** | Unlikely but possible | Strong safeguards, low exposure |

### Severity Assessment Criteria

| Level | Description | Indicators |
|-------|-------------|------------|
| **High** | Significant harm | Major discrimination, denial of essential services, irreversible impact |
| **Medium** | Moderate harm | Partial rights restriction, recoverable harm, limited scope |
| **Low** | Minor harm | Inconvenience, easily remedied, small impact |

## FRIA Assessment Template

```markdown
# Fundamental Rights Impact Assessment

## 1. Deployer Information

| Field | Information |
|-------|-------------|
| Organization Name | [Name] |
| Organization Type | ☐ Public Body ☐ Public Service Provider ☐ Credit/Insurance ☐ Other |
| Contact Person | [Name, Title, Email] |
| Assessment Date | [Date] |
| Next Review Date | [Date] |

## 2. AI System Information

| Field | Information |
|-------|-------------|
| AI System Name | [Name] |
| Provider | [Provider Name] |
| Annex III Category | [e.g., 4(a) - Recruitment] |
| Intended Purpose | [Description] |
| Deployment Context | [Where and how used] |
| Period of Use | [Start date, frequency] |

## 3. Affected Persons and Groups

### 3.1 Categories of Natural Persons
| Category | Number Affected | Vulnerability Level |
|----------|-----------------|---------------------|
| [e.g., Job applicants] | [Estimate] | ☐ High ☐ Medium ☐ Low |
| [e.g., Employees] | [Estimate] | ☐ High ☐ Medium ☐ Low |

### 3.2 Vulnerable Groups Identification
- [ ] Children
- [ ] Elderly persons
- [ ] Persons with disabilities
- [ ] Economically disadvantaged
- [ ] Minorities
- [ ] Other: [Specify]

## 4. Fundamental Rights Risk Assessment

### 4.1 Human Dignity
| Question | Response |
|----------|----------|
| Does the system treat individuals with inherent worth? | ☐ Yes ☐ No ☐ Partial |
| Risk of degrading or humiliating treatment? | ☐ High ☐ Medium ☐ Low ☐ None |
| Assessment Notes | [Notes] |

### 4.2 Right to Liberty and Security
| Question | Response |
|----------|----------|
| Could the system restrict freedom of movement? | ☐ Yes ☐ No ☐ Partial |
| Risk of arbitrary restrictions? | ☐ High ☐ Medium ☐ Low ☐ None |
| Assessment Notes | [Notes] |

### 4.3 Respect for Private and Family Life
| Question | Response |
|----------|----------|
| Does the system process private information? | ☐ Yes ☐ No ☐ Partial |
| Risk of privacy intrusion? | ☐ High ☐ Medium ☐ Low ☐ None |
| Assessment Notes | [Notes] |

### 4.4 Protection of Personal Data
| Question | Response |
|----------|----------|
| Is there a lawful basis for data processing? | ☐ Yes ☐ No ☐ TBD |
| DPIA conducted? | ☐ Yes ☐ No ☐ In Progress |
| Risk of unlawful processing? | ☐ High ☐ Medium ☐ Low ☐ None |
| Assessment Notes | [Notes] |

### 4.5 Freedom of Expression and Information
| Question | Response |
|----------|----------|
| Could the system chill free expression? | ☐ Yes ☐ No ☐ Partial |
| Risk of information restriction? | ☐ High ☐ Medium ☐ Low ☐ None |
| Assessment Notes | [Notes] |

### 4.6 Non-discrimination
| Question | Response |
|----------|----------|
| Has bias testing been conducted? | ☐ Yes ☐ No ☐ In Progress |
| Protected characteristics affected? | [List] |
| Risk of discriminatory outcomes? | ☐ High ☐ Medium ☐ Low ☐ None |
| Assessment Notes | [Notes] |

## 5. Risk Summary

| Fundamental Right | Likelihood | Severity | Risk Level | Priority |
|-------------------|------------|----------|------------|----------|
| Human Dignity | [H/M/L] | [H/M/L] | [Risk] | [1-5] |
| Liberty and Security | [H/M/L] | [H/M/L] | [Risk] | [1-5] |
| Private/Family Life | [H/M/L] | [H/M/L] | [Risk] | [1-5] |
| Personal Data | [H/M/L] | [H/M/L] | [Risk] | [1-5] |
| Expression/Information | [H/M/L] | [H/M/L] | [Risk] | [1-5] |
| Non-discrimination | [H/M/L] | [H/M/L] | [Risk] | [1-5] |

## 6. Mitigation Measures

### 6.1 Technical Measures
| Risk Addressed | Measure | Implementation Status | Owner |
|----------------|---------|----------------------|-------|
| [Risk] | [Measure] | ☐ Planned ☐ In Progress ☐ Complete | [Name] |

### 6.2 Organizational Measures
| Risk Addressed | Measure | Implementation Status | Owner |
|----------------|---------|----------------------|-------|
| [Risk] | [Measure] | ☐ Planned ☐ In Progress ☐ Complete | [Name] |

### 6.3 Human Oversight Arrangements
- [ ] Human review before AI decision
- [ ] Human override capability
- [ ] Designated oversight personnel
- [ ] Training provided
- [ ] Other: [Specify]

### 6.4 Complaint Handling and Redress
- [ ] Complaint mechanism established
- [ ] Contact point designated
- [ ] Response timeline defined: [X] days
- [ ] Escalation procedure documented
- [ ] Remediation process defined

## 7. Documentation and Monitoring

### 7.1 Update Triggers
FRIA must be updated when:
- [ ] Significant changes to AI system
- [ ] Changes to deployment context
- [ ] New affected groups identified
- [ ] New risks identified
- [ ] Regulatory changes

### 7.2 Review Schedule
| Review Type | Frequency | Next Review Date |
|-------------|-----------|------------------|
| Regular Review | [Annual/Semi-annual] | [Date] |
| Triggered Review | As needed | N/A |

## 8. Sign-off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| FRIA Lead | | | |
| DPO | | | |
| Legal/Compliance | | | |
| Authorized Signatory | | | |

## 9. Market Surveillance Notification

- [ ] Notification sent to market surveillance authority
- [ ] Date sent: [Date]
- [ ] Authority: [Name]
- [ ] Reference number: [Number]
```

## FRIA Validation Checklist

### Pre-Deployment
- [ ] Deployer type determined (public body/public service/credit/insurance)
- [ ] Annex III category identified
- [ ] FRIA required assessment completed
- [ ] All affected persons/groups identified
- [ ] All applicable fundamental rights assessed
- [ ] Risk levels assigned (likelihood x severity)

### Risk Assessment
- [ ] Human dignity impact assessed
- [ ] Liberty and security impact assessed
- [ ] Privacy impact assessed
- [ ] Data protection impact assessed (DPIA linkage)
- [ ] Freedom of expression impact assessed
- [ ] Non-discrimination impact assessed
- [ ] Vulnerable groups specifically considered

### Mitigation
- [ ] Technical measures documented
- [ ] Organizational measures documented
- [ ] Human oversight arrangements defined
- [ ] Complaint handling procedure established
- [ ] Redress mechanism in place

### Governance
- [ ] FRIA documented
- [ ] Required sign-offs obtained
- [ ] Market surveillance authority notified
- [ ] Update triggers defined
- [ ] Review schedule established

## DPIA Integration (Article 27(4))

The FRIA may complement an existing Data Protection Impact Assessment (DPIA) under:
- GDPR Article 35
- LED Article 27 (Directive 2016/680)

If a DPIA has been conducted, the FRIA should:
1. Reference the DPIA
2. Build on DPIA findings
3. Focus on fundamental rights beyond data protection
4. Address AI-specific risks

## Integration Points

**Inputs from**:
- `ai-risk-classification` skill → Annex III category determination
- `data-classification` skill → Data processing context
- Provider's instructions for use → System capabilities and limitations
- DPIA → Data protection risk assessment

**Outputs to**:
- Market surveillance authority → Notification
- Internal governance → Compliance documentation
- `hitl-design` skill → Human oversight requirements
- Incident response → Risk monitoring

---

**Last Updated:** 2026-01-10
**EU AI Act Reference:** Article 27, Annex III
**Source:** FRIA_questionnaire.xlsx
