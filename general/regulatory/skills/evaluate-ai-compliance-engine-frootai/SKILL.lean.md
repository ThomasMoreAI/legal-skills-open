---
name: evaluate-ai-compliance-engine
description: "Evaluate AI Compliance Engine — measure check accuracy, evidence quality, framework coverage, risk scoring calibration, false positive/negative rate. Use when: evaluate, audit compliance."
---

# Evaluate AI Compliance Engine

## When to Use
- Validate compliance check accuracy against known test scenarios
- Measure evidence collection completeness
- Assess framework coverage (are all requirements checked?)
- Calibrate risk scoring against expert assessments
- Gate compliance engine deployment with quality thresholds

## Compliance Engine Metrics & Targets

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Check accuracy | ≥ 90% | LLM assessment matches expert review |
| Evidence completeness | ≥ 95% | All required evidence sources connected |
| Framework coverage | 100% | All regulation requirements have checks |
| Risk score calibration | Within ±1 of expert | Compare LLM risk vs human auditor risk |
| False positive rate | < 10% | Compliant items flagged as non-compliant |
| False negative rate | < 5% | Non-compliant items marked as pass |
| Report quality | ≥ 4.0/5.0 | Auditor rating of generated reports |
| Check execution time | < 30 min per framework | Full framework scan duration |

## Step 1: Prepare Compliance Test Scenarios
```json
{"system": "test-rag-app", "framework": "GDPR", "check": "data-retention-policy",
 "known_status": "fail", "reason": "No retention policy documented"}
{"system": "test-rag-app", "framework": "GDPR", "check": "encryption-at-rest",
 "known_status": "pass", "evidence": "Azure Storage CMK enabled"}
{"system": "test-voice-app", "framework": "HIPAA", "check": "phi-access-control",
 "known_status": "partial", "reason": "RBAC configured but not audited"}
```
Minimum: 50 test scenarios with known pass/fail/partial status per framework.

## Step 2: Validate Check Accuracy
```bash
python evaluation/eval.py --test-set evaluation/compliance-tests.jsonl --metrics check_accuracy
```
- Compare LLM compliance assessment vs known ground truth
- Per-framework accuracy (GDPR, HIPAA, EU AI Act, SOC 2)
- Identify check types where LLM consistently wrong

## Step 3: Validate Evidence Quality
- For each check: is the evidence sufficient for an auditor?
- Does evidence link to specific resources (not generic)?
- Is evidence timestamped and verifiable?
- Can an auditor reproduce the finding from the evidence?

## Step 4: Calibrate Risk Scoring
| Test Scenario | Expert Risk | LLM Risk | Delta |
| --- | --- | --- | --- |
| No encryption at rest | 9 (Critical) | Measure | Target ±1 |
| Missing audit logs | 7 (High) | Measure | Target ±1 |
| Documentation gap | 3 (Low) | Measure | Target ±1 |

## Step 5: Test False Negative Detection
- Deploy test system with known violations
- Run compliance engine → verify all violations detected
- False negative (missed violation) = most dangerous outcome
- Target: < 5% false negative rate

## Step 6: Generate Report
```bash
python evaluation/eval.py --all --output evaluation/compliance-report.json --ci-gate
```

### Quality Gate Decision
| Result | Action |
| --- | --- |
| All PASS | Deploy compliance engine for audit use |
| Check accuracy < 85% | Improve evidence grounding in LLM prompts |
| False negative > 10% | BLOCKER — add missing checks before use |
| Risk miscalibration > ±2 | Retrain risk scoring with expert labels |
| Evidence gaps | Connect missing data sources |

## Evaluation Cadence
- **Pre-deployment**: Full test scenario suite per framework
- **Quarterly**: Re-calibrate risk scoring with auditor review
- **On regulation update**: Add new requirements, re-evaluate coverage
- **Annual**: Full external audit comparison (LLM vs human auditor)

## Common Failure Patterns

| Symptom | Root Cause | Fix |
| --- | --- | --- |
| All checks pass (suspicious) | Evidence source not connected | Verify data source connectivity |
| Inconsistent risk scores | No grounding in evidence | Add "base assessment on evidence only" to prompt |
| GDPR check misses consent | Consent management not exposed | Connect consent API as evidence source |
| Report rejected by auditor | Missing evidence references | Include resource IDs and timestamps in evidence |
| EU AI Act risk wrong | Wrong risk category assigned | Add risk classification decision tree to prompt |
| Check takes >1 hour | Full scan on every run | Enable incremental checks (delta since last run) |

## CI/CD Quality Gates
```yaml
- name: Compliance Check Accuracy
  run: python evaluation/eval.py --metrics check_accuracy --ci-gate --threshold 0.90
- name: False Negative Gate
  run: python evaluation/eval.py --metrics false_negative --ci-gate --max-rate 0.05
- name: Framework Coverage
  run: python evaluation/eval.py --metrics coverage --ci-gate --threshold 1.0
```
