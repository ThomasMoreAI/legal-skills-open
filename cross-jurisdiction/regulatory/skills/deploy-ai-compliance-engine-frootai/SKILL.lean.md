---
name: deploy-ai-compliance-engine
description: "Deploy AI Compliance Engine — configure regulatory check framework (GDPR, HIPAA, EU AI Act, SOC 2), automated audit trail, risk scoring, evidence collection. Use when: deploy, configure compliance."
---

# Deploy AI Compliance Engine

## When to Use
- Deploy automated compliance checking for AI systems
- Configure regulatory framework checks (GDPR, HIPAA, EU AI Act)
- Set up automated audit trail with evidence collection
- Implement risk scoring for AI system assessments
- Generate compliance reports for regulatory submissions

## Prerequisites
1. Azure CLI authenticated: `az account show`
2. Azure OpenAI (gpt-4o for compliance analysis)
3. Cosmos DB (compliance evidence store)
4. Azure Storage (audit trail, report storage)
5. Regulatory framework definitions prepared

## Step 1: Deploy Infrastructure
```bash
az bicep lint -f infra/main.bicep
az deployment group create -g $RG -f infra/main.bicep -p infra/parameters.json
```

## Step 2: Configure Regulatory Frameworks
| Framework | Key Requirements | Check Count |
| --- | --- | --- |
| GDPR | Data subject rights, consent, DPO, breach notification | 45 checks |
| HIPAA | PHI protection, access controls, audit logs, encryption | 38 checks |
| EU AI Act | Risk classification, transparency, human oversight, testing | 52 checks |
| SOC 2 | Security, availability, processing integrity, confidentiality | 64 checks |
| ISO 27001 | ISMS, risk management, controls, continuous improvement | 114 checks |

## Step 3: Configure Compliance Check Pipeline
```python
# Check execution pipeline
async def run_compliance_check(system_id, framework):
    checks = load_framework_checks(framework)
    results = []
    for check in checks:
        evidence = await collect_evidence(system_id, check)
        assessment = await assess_compliance(check, evidence, model="gpt-4o")
        results.append({
            "check_id": check.id,
            "status": assessment.status,  # pass, fail, partial, na
            "evidence": evidence,
            "risk_score": assessment.risk_score,
            "remediation": assessment.remediation if assessment.status != "pass" else None
        })
    return generate_report(results)
```

## Step 4: Configure Risk Scoring
| Risk Level | Score | Criteria | Action |
| --- | --- | --- | --- |
| Critical | 9-10 | Regulatory violation likely | Immediate remediation |
| High | 7-8 | Major gap, significant exposure | Remediation within 30 days |
| Medium | 4-6 | Minor gap, moderate exposure | Remediation within 90 days |
| Low | 1-3 | Observation, best practice gap | Track, address in next cycle |
| None | 0 | Fully compliant | No action needed |

## Step 5: Configure Evidence Collection
| Evidence Type | Source | Automation |
| --- | --- | --- |
| Configuration audit | Azure Resource Graph | Fully automated |
| Access control review | Azure AD / Entra ID | Fully automated |
| Data encryption status | Key Vault + Storage | Fully automated |
| Logging completeness | Log Analytics | Fully automated |
| Policy documentation | SharePoint / Git | LLM-assisted review |
| Training records | HR system | Manual + LLM verification |

## Step 6: Configure Audit Trail
- Immutable log: who ran what check, when, what result
- Evidence snapshots: system state at time of check
- Version tracking: which framework version was used
- Retention: 7 years (regulatory requirement)
- Tamper detection: hash chain for audit integrity

## Step 7: Post-Deployment Verification
- [ ] Framework checks loading correctly per regulation
- [ ] Evidence collection from all configured sources
- [ ] Risk scoring producing consistent assessments
- [ ] Audit trail recording all compliance activities
- [ ] Reports generating in required format
- [ ] LLM compliance analysis providing actionable remediation
- [ ] Dashboard showing compliance posture per framework

## Troubleshooting

| Issue | Cause | Fix |
| --- | --- | --- |
| Check returns N/A incorrectly | Evidence source not connected | Verify data source connectivity |
| Risk score inconsistent | LLM hallucinating assessment | Add evidence-grounding in prompt |
| Audit trail incomplete | Missing event source | Add all check executions to log |
| Report format wrong | Template mismatch | Update report template per regulation |
| Stale evidence | Check schedule too infrequent | Increase frequency for critical checks |
| False compliance (pass when should fail) | Missing check for requirement | Audit framework coverage |
