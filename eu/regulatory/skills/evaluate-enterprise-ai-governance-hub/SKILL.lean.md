---
name: "evaluate-enterprise-ai-governance-hub"
description: "Evaluate Enterprise AI Governance Hub — risk classification accuracy, policy enforcement, review compliance, registry completeness, dashboard accuracy."
---

# Evaluate Enterprise AI Governance Hub

## Prerequisites

- Deployed governance hub (run `deploy-enterprise-ai-governance-hub` skill first)
- Test AI systems with known risk classifications
- Python 3.11+ with `azure-ai-evaluation`

## Step 1: Evaluate Risk Classification

```bash
python evaluation/eval_classification.py \
  --test-data evaluation/data/ai_systems/ \
  --output evaluation/results/classification.json
```

Classification metrics:
| Metric | Description | Target |
|--------|-------------|--------|
| **Classification Accuracy** | Matches expert risk assessment | > 90% |
| **Unacceptable Detection** | Banned systems correctly identified | 100% |
| **High-Risk Detection** | High-risk systems correctly flagged | > 95% |
| **Over-Classification Rate** | Minimal incorrectly classified as high | < 10% |
| **Requirement Mapping** | Correct requirements assigned per level | > 95% |

## Step 2: Evaluate Policy Enforcement

```bash
python evaluation/eval_policy.py \
  --test-data evaluation/data/policy_tests/ \
  --output evaluation/results/policy.json
```

Policy metrics:
| Metric | Description | Target |
|--------|-------------|--------|
| **Gate Enforcement** | Non-compliant deployments blocked | 100% |
| **False Block Rate** | Compliant systems wrongly blocked | < 2% |
| **Incident Reporting** | Incidents reported within 72 hours | 100% |
| **Review Scheduling** | Reviews scheduled per risk level | 100% |
| **Deprecation Enforcement** | Overdue deprecated models flagged | 100% |

## Step 3: Evaluate Registry Completeness

```bash
python evaluation/eval_registry.py \
  --test-data evaluation/data/registry/ \
  --output evaluation/results/registry.json
```

Registry metrics:
| Metric | Description | Target |
|--------|-------------|--------|
| **Registration Rate** | % AI systems registered vs inventory | > 95% |
| **Schema Completeness** | All required fields populated | > 90% |
| **Status Accuracy** | Status reflects actual deployment state | > 95% |
| **Owner Assigned** | Every system has responsible person | 100% |
| **Shadow AI Detection** | Unregistered systems found | Trend decreasing |

## Step 4: Evaluate Dashboard Accuracy

```bash
python evaluation/eval_dashboard.py \
  --test-data evaluation/data/dashboard/ \
  --output evaluation/results/dashboard.json
```

Dashboard metrics:
| Metric | Description | Target |
|--------|-------------|--------|
| **Compliance Rate Accuracy** | Matches manual calculation | Within ±2% |
| **Overdue Review Count** | Correct count of overdue reviews | 100% |
| **Risk Distribution** | Matches registry aggregation | 100% |
| **Incident Trend Accuracy** | Matches actual incident records | 100% |

## Step 5: Generate Report

```bash
python evaluation/generate_report.py \
  --results-dir evaluation/results/ \
  --output evaluation/report.md
```

Report includes:
- Risk classification confusion matrix
- Policy enforcement effectiveness timeline
- Registry coverage growth trend
- Compliance rate by department
- Overdue review aging analysis

## Threshold Reference

| Metric | Threshold | Source |
| --- | --- | --- |
| Classification accuracy | > 90% | config/guardrails.json |
| Unacceptable detection | 100% | EU AI Act mandatory |
| Gate enforcement | 100% | config/guardrails.json |
| Registration rate | > 95% | config/guardrails.json |
| Incident reporting | 100% within 72h | EU AI Act Article 62 |
