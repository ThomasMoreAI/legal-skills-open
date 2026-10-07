# Regulatory Compliance Rules

## Core Principles

- NEVER report PASS on partial compliance — any open finding is CONDITIONAL or FAIL
- ALWAYS validate against all applicable jurisdictions (GDPR, CCPA, state laws) — not just one
- ALWAYS provide specific remediation steps with owning agent for every finding
- Regulations change frequently — stamp every report with assessment date and regulation version
- Privacy-by-design must be validated at design time, not retrofitted post-deployment
- ADA/WCAG compliance is non-negotiable for public-facing interfaces (active litigation risk)
- DPAs must be specific — vague processing descriptions are regulatory failures

## Severity Classification

| Severity | Action                                              |
| -------- | --------------------------------------------------- |
| CRITICAL | Block deployment; remediate immediately             |
| HIGH     | Remediate before next release                       |
| MEDIUM   | Remediate within 30 days; document in risk register |
| LOW      | Best-practice improvement; track in backlog         |

## Decision Rules

- `PASS`: All applicable checklist items verified, zero open findings
- `CONDITIONAL`: Minor/medium findings with documented remediation plan; deployment allowed
- `FAIL`: Any critical or high finding; deployment blocked until remediated

## Anti-Patterns

- Checking only GDPR and ignoring CCPA, state laws, and multi-jurisdiction exposure
- Treating accessibility as optional when interfaces are public-facing
- Accepting vague DPA language ("process data as needed") without requiring specificity
- One-time audit without establishing continuous monitoring cadence
- Claiming compliance without evidence — always produce a written report with dated findings

## Integration Points

### Agents Using This Skill

- **compliance-checker** (primary): Regulatory compliance assessments
- **security-architect** (supporting): Overlapping security + privacy concerns

### Related Skills

- **compliance-policy-check**: Framework policy compliance (internal rules)
- **security-architect**: Security threat modeling and OWASP analysis
- **audit-context-building**: Deep code review before compliance assessment
- **content-security-scan**: Automated scanning for external content security

### Report Output Location

Reports: `.claude/context/reports/compliance/`
Naming: `{subject}-compliance-{YYYY-MM-DD}.md`

## When to Invoke

```javascript
Skill({ skill: 'regulatory-compliance' });
```

- Before deploying any feature handling personal data
- During architecture review for PII-touching systems
- When validating third-party vendor DPAs
- Before EU/California/multi-jurisdiction product launches
- As part of accessibility audits for public-facing interfaces
