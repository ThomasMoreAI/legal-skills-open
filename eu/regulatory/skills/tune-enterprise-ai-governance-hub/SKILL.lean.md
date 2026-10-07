---
name: "tune-enterprise-ai-governance-hub"
description: "Tune Enterprise AI Governance Hub — risk classification rules, review cadence, policy gates, dashboard metrics, regulation mapping, cost optimization."
---

# Tune Enterprise AI Governance Hub

## Prerequisites

- Deployed governance hub with evaluation results available
- Access to `config/openai.json`, `config/guardrails.json`, `config/agents.json`

## Step 1: Tune Risk Classification

```json
// config/guardrails.json — risk classification settings
{
  "risk_classification": {
    "method": "rules_first_llm_fallback",
    "rule_based_categories": {
      "unacceptable": ["social_scoring", "subliminal_manipulation", "mass_biometric_surveillance"],
      "high": ["biometric_id", "critical_infrastructure", "education_access", "employment", "law_enforcement"],
      "limited": ["chatbot", "emotion_recognition", "deepfake"],
      "minimal": ["spam_filter", "game_ai", "inventory"]
    },
    "llm_classification": {
      "enabled": true,
      "model": "gpt-4o",
      "confidence_threshold": 0.85,
      "human_review_below": 0.70
    },
    "affected_population_boost": {
      "vulnerable": "+1_level",
      "children": "+1_level",
      "employees": "no_change",
      "general_public": "no_change"
    }
  }
}
```

Classification tuning:
| Parameter | Default | Impact |
|-----------|---------|--------|
| `method` | rules_first | LLM-only = more flexible but less predictable |
| `confidence_threshold` | 0.85 | Lower = accept less certain classifications |
| `affected_population_boost` | +1 for vulnerable/children | Ensures higher scrutiny for at-risk groups |

### Risk Level Decision Matrix
| Use Case | General Public | Vulnerable/Children | Decision |
| --- | --- | --- | --- |
| Chatbot | Limited | High | Population matters |
| Spam filter | Minimal | Minimal | Low risk always |
| Employment screening | High | High | Always high |
| Game recommendation | Minimal | Limited | Children = higher |

## Step 2: Tune Review Schedule

```json
// config/agents.json — review settings
{
  "reviews": {
    "schedule_by_risk": {
      "high": {"frequency": "quarterly", "lead_time_days": 14, "review_type": "full"},
      "limited": {"frequency": "annually", "lead_time_days": 30, "review_type": "standard"},
      "minimal": {"frequency": "biannually", "lead_time_days": 30, "review_type": "light"}
    },
    "trigger_ad_hoc_review_on": [
      "major_model_update",
      "data_source_change",
      "incident_severity_high",
      "regulation_change",
      "user_complaint_pattern"
    ],
    "overdue_escalation": {
      "warn_at_days": 7,
      "escalate_at_days": 14,
      "block_at_days": 30
    },
    "auto_generate_review_template": true,
    "review_checklist_by_level": {
      "full": ["risk_assessment", "data_governance", "technical_docs", "human_oversight", "incident_history", "model_performance"],
      "standard": ["risk_assessment", "incident_history", "model_performance"],
      "light": ["incident_history", "status_verification"]
    }
  }
}
```

Review tuning:
| Risk Level | Frequency | Review Type | Checklist Items |
|-----------|-----------|-------------|----------------|
| High | Quarterly | Full (6 checks) | Risk + data + docs + oversight + incidents + performance |
| Limited | Annual | Standard (3 checks) | Risk + incidents + performance |
| Minimal | Biannual | Light (2 checks) | Incidents + status verification |

## Step 3: Tune Policy Enforcement

```json
// config/agents.json — policy settings
{
  "policies": {
    "registration_gate": {
      "enforce_before": "staging",
      "block_unregistered": true,
      "grace_period_days": 0
    },
    "high_risk_gate": {
      "required_before_production": [
        "human_oversight_plan",
        "conformity_assessment",
        "technical_documentation",
        "risk_management_system"
      ],
      "block_if_missing": true
    },
    "deprecation_enforcement": {
      "warn_at_days": 60,
      "block_at_days": 90,
      "migration_plan_required": true
    },
    "incident_reporting": {
      "severity_high_deadline_hours": 72,
      "auto_notify": ["governance_team", "system_owner", "ciso"],
      "regulate_report_to": ["eu_ai_office"]
    },
    "ci_cd_integration": {
      "pre_deployment_webhook": true,
      "block_on_policy_violation": true,
      "allow_override_with_approval": true,
      "approval_role": "ai_governance_admin"
    }
  }
}
```

Policy tuning:
| Policy | Default | Impact |
|--------|---------|--------|
| `registration_gate` | Before staging | Earlier = catch sooner, may slow dev |
| `block_if_missing` (high-risk) | true | false = warn only (not recommended) |
| `deprecation block_at_days` | 90 | Shorter = faster cleanup, more pressure |
| `allow_override_with_approval` | true | false = no exceptions (strictest) |

## Step 4: Tune Regulation Mapping

```json
// config/guardrails.json — regulation settings
{
  "regulations": {
    "eu_ai_act": {
      "enabled": true,
      "effective_date": "2025-08-01",
      "articles": {
        "article_6": "High-risk classification",
        "article_9": "Risk management system",
        "article_10": "Data governance",
        "article_13": "Transparency",
        "article_14": "Human oversight",
        "article_62": "Incident reporting (72h)"
      }
    },
    "gdpr": {
      "enabled": true,
      "requires_dpia": ["high_risk", "sensitive_data"],
      "data_retention_check": true
    },
    "nist_ai_rmf": {
      "enabled": true,
      "functions": ["govern", "map", "measure", "manage"]
    },
    "iso_42001": {
      "enabled": false,
      "note": "Enable when pursuing certification"
    }
  }
}
```

## Step 5: Tune Model Configuration

```json
// config/openai.json
{
  "risk_classification": {
    "model": "gpt-4o",
    "temperature": 0,
    "max_tokens": 200
  },
  "compliance_report": {
    "model": "gpt-4o",
    "temperature": 0.2,
    "max_tokens": 2000
  },
  "review_template": {
    "model": "gpt-4o-mini",
    "temperature": 0.1,
    "max_tokens": 1000
  }
}
```

| Task | Model | Why |
| --- | --- | --- |
| Risk classification | gpt-4o | Critical accuracy — determines regulatory requirements |
| Compliance report | gpt-4o | Board-level quality reporting |
| Review template | gpt-4o-mini | Structured template generation |

## Step 6: Cost Optimization

```python
# Enterprise AI Governance Hub cost per month:
# LLM:
#   - Risk classification (gpt-4o, ~20 new systems/month × $0.02): ~$0.40
#   - Compliance reports (gpt-4o, ~5/month × $0.10): ~$0.50
#   - Review templates (gpt-4o-mini, ~10/month × $0.005): ~$0.05
# Infrastructure:
#   - Container Apps: ~$15/month
#   - Cosmos DB Serverless: ~$10/month
#   - Functions (policy gates): ~$5/month
#   - App Insights: ~$5/month
# Total: ~$36/month (very low — governance is mostly policy + data, not compute-heavy)

# Cost is minimal because:
# 1. Registry is CRUD (no ML serving)
# 2. Risk classification uses rules first (LLM only for ambiguous)
# 3. Policy enforcement is rule-based (Azure Functions)
# 4. Dashboard is aggregation queries (Cosmos DB)
```

| Component | Cost | Note |
| --- | --- | --- |
| LLM | ~$1/month | Minimal — rules handle most classification |
| Infrastructure | ~$35/month | Standard serverless footprint |
| **Total** | **~$36/month** | **Most cost-effective play** |

## Step 7: Verify Tuning Impact

```bash
python evaluation/eval_classification.py --test-data evaluation/data/ai_systems/
python evaluation/eval_policy.py --test-data evaluation/data/policy_tests/
python evaluation/eval_registry.py --test-data evaluation/data/registry/
python evaluation/eval_dashboard.py --test-data evaluation/data/dashboard/

python evaluation/compare_results.py \
  --baseline evaluation/results/baseline/ \
  --current evaluation/results/ \
  --output evaluation/tuning-impact.md
```

Expected improvements:
| Metric | Before | After | Target |
|--------|--------|-------|--------|
| Classification accuracy | baseline | > 90% | > 90% |
| Gate enforcement | baseline | 100% | 100% |
| Registration rate | baseline | > 95% | > 95% |
| Review compliance | baseline | > 90% | > 90% |
| Monthly cost | ~$36 | ~$36 | < $50 |
