---
name: tune-ai-compliance-engine
description: "Tune AI Compliance Engine — optimize check frequency, reduce false positives, calibrate risk scoring, configure evidence retention, framework-specific tuning. Use when: tune, optimize compliance."
---

# Tune AI Compliance Engine

## When to Use
- Optimize check execution frequency per risk level
- Reduce false positive rate (compliant items flagged incorrectly)
- Calibrate risk scoring weights per framework
- Configure evidence retention and archival policies
- Tune LLM compliance analysis prompts for accuracy

## Tuning Dimensions

### Dimension 1: Check Frequency Optimization

| Risk Level | Default Frequency | High Sensitivity | Low Sensitivity |
| --- | --- | --- | --- |
| Critical | Daily | Hourly | Daily |
| High | Weekly | Daily | Weekly |
| Medium | Monthly | Weekly | Quarterly |
| Low | Quarterly | Monthly | Annually |
| N/A | Annually | Annually | Annually |

**Rule**: Critical checks run daily minimum. Never reduce below regulation requirement.

### Dimension 2: False Positive Reduction

| Strategy | FP Reduction | Trade-off |
| --- | --- | --- |
| Add evidence context to LLM prompt | 30% | More tokens per check |
| Include previous check history | 25% | Context window usage |
| Require high confidence (>0.85) for fail | 40% | May miss edge cases |
| Two-stage: LLM assess then expert verify | 60% | Slower for flagged items |
| Whitelist known-compliant patterns | 35% | Maintenance of whitelist |

### Dimension 3: Risk Scoring Weights

| Factor | Default Weight | Regulated Industry | Internal Use |
| --- | --- | --- | --- |
| Regulation severity | 0.3 | 0.4 | 0.2 |
| Data sensitivity (PII/PHI) | 0.25 | 0.3 | 0.2 |
| User impact | 0.2 | 0.15 | 0.3 |
| Remediability | 0.15 | 0.1 | 0.2 |
| Time since last check | 0.1 | 0.05 | 0.1 |

### Dimension 4: Evidence Retention Policy

| Evidence Type | Retention | Storage Tier | Cost/GB/mo |
| --- | --- | --- | --- |
| Check results | 7 years | Archive | $0.002 |
| Configuration snapshots | 3 years | Hot → Archive after 90d | $0.02 → $0.002 |
| Remediation records | 7 years | Archive | $0.002 |
| Audit reports | 10 years | Archive (immutable) | $0.002 |
| Raw evidence data | 1 year | Hot → Delete | $0.02 |

### Dimension 5: Framework-Specific Tuning

| Framework | Key Tuning | Optimization |
| --- | --- | --- |
| GDPR | Consent checks, data subject rights | Automate DSR handling verification |
| HIPAA | PHI access, encryption, breach detection | Focus on access control automation |
| EU AI Act | Risk classification, transparency, testing | Automate risk category assessment |
| SOC 2 | Control effectiveness, change management | Continuous monitoring vs point-in-time |

## Production Readiness Checklist
- [ ] All frameworks configured with complete check sets
- [ ] Check accuracy ≥ 90% on test scenarios
- [ ] False positive rate < 10%
- [ ] False negative rate < 5%
- [ ] Risk scoring calibrated (±1 of expert)
- [ ] Evidence collection from all required sources
- [ ] Audit trail immutable and tamper-evident
- [ ] Reports generating in regulation-required format
- [ ] Retention policies configured per evidence type
- [ ] Check frequency matched to risk level

## Output: Tuning Report
After tuning, compare:
- Check accuracy improvement
- False positive rate reduction
- Risk score calibration delta
- Evidence completeness improvement
- Compliance posture score change per framework

## Tuning Playbook
1. **Baseline**: Run all frameworks on test system, record accuracy + FP/FN rate
2. **Accuracy**: Improve evidence grounding in LLM prompts
3. **False positives**: Add whitelist for known-compliant patterns
4. **Risk scores**: Calibrate weights with auditor review on 20 checks
5. **Frequency**: Match check schedule to regulation requirements
6. **Evidence**: Verify all sources connected, data fresh
7. **Reports**: Get auditor feedback on report format + evidence quality
8. **Retention**: Configure per evidence type (check=7y, raw=1y)
9. **Re-test**: Same test system, compare before/after

## Regulatory Update Handling
| Event | Action | Urgency |
| --- | --- | --- |
| GDPR amendment | Update affected checks, re-evaluate | 30 days |
| New EU AI Act guidance | Add new checks, classify risk categories | 60 days |
| HIPAA rule change | Update PHI checks, re-audit access controls | 30 days |
| SOC 2 criteria update | Refresh control mappings | 90 days |
