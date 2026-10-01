---
name: "deploy-enterprise-ai-governance-hub"
description: "Deploy Enterprise AI Governance Hub — AI system registry, EU AI Act risk classification, model lifecycle management, policy enforcement, compliance dashboard."
---

# Deploy Enterprise AI Governance Hub

## Prerequisites

- Azure CLI authenticated (`az account show`)
- Contributor + User Access Administrator on target subscription
- Organization AI system inventory (existing models, data sources)
- Python 3.11+ with `azure-openai`, `azure-identity`

## Step 1: Deploy Infrastructure

```bash
az deployment group create \
  --resource-group rg-frootai-ai-governance \
  --template-file infra/main.bicep \
  --parameters infra/parameters.json \
  --parameters environment=dev
```

Infrastructure components:
| Resource | Purpose | SKU |
|----------|---------|-----|
| Azure OpenAI | Risk classification + compliance report generation | S0 |
| Cosmos DB | AI system registry, assessments, policies, audit log | Serverless |
| Azure AD / Entra ID | RBAC for governance roles (admin, assessor, viewer) | Included |
| Azure Functions | Policy enforcement gates + scheduled reviews | Consumption |
| Container Apps | Governance dashboard API | Consumption |
| Azure Key Vault | Secrets + governance config | Standard |
| App Insights | Governance telemetry + audit trail | Pay-as-you-go |

## Step 2: Deploy AI System Registry

```python
# AI System registration schema
AI_SYSTEM_SCHEMA = {
    "id": str,
    "name": str,
    "description": str,
    "owner": {"team": str, "responsible_person": str, "email": str},
    "risk_level": str,  # Auto-classified: "unacceptable", "high", "limited", "minimal"
    "status": str,      # "development", "staging", "production", "deprecated", "retired"
    "model_info": {
        "model_name": str,
        "version": str,
        "provider": str,  # "azure_openai", "custom", "third_party"
        "model_type": str  # "generative", "classification", "regression", "vision"
    },
    "data_sources": [str],
    "use_case": str,
    "affected_population": str,
    "compliance": {
        "eu_ai_act": {"status": str, "assessment_date": str},
        "gdpr": {"status": str, "dpia_completed": bool},
        "nist_ai_rmf": {"status": str},
        "iso_42001": {"status": str}
    },
    "oversight": {
        "human_in_the_loop": bool,
        "override_mechanism": bool,
        "monitoring_active": bool,
        "escalation_path": str
    },
    "last_assessment": str,
    "next_review": str,
    "incidents": [{"date": str, "severity": str, "description": str}]
}
```

## Step 3: Deploy EU AI Act Risk Classification

```python
EU_AI_ACT_RISK_LEVELS = {
    "unacceptable": {
        "description": "Banned AI applications",
        "examples": ["social_scoring", "real_time_biometric_mass_surveillance", "subliminal_manipulation"],
        "action": "block_registration",
        "allowed_exceptions": ["law_enforcement_with_judicial_authorization"]
    },
    "high": {
        "description": "AI systems with significant impact on health, safety, fundamental rights",
        "categories": [
            "biometric_identification", "critical_infrastructure", "education_access",
            "employment_decisions", "essential_services_access", "law_enforcement",
            "migration_border", "justice_democratic"
        ],
        "requirements": [
            "risk_management_system", "data_governance", "technical_documentation",
            "record_keeping", "transparency_to_users", "human_oversight",
            "accuracy_robustness_cybersecurity", "conformity_assessment"
        ],
        "review_frequency": "quarterly"
    },
    "limited": {
        "description": "AI with transparency obligations",
        "examples": ["chatbots", "emotion_recognition", "deepfake_generation"],
        "requirements": ["transparency_notice", "user_informed_ai_interaction"],
        "review_frequency": "annually"
    },
    "minimal": {
        "description": "Low-risk AI with no specific obligations",
        "examples": ["spam_filters", "game_ai", "inventory_optimization"],
        "requirements": ["voluntary_code_of_conduct"],
        "review_frequency": "biannually"
    }
}

async def classify_risk(system: AISystem) -> str:
    """Auto-classify EU AI Act risk level based on use case and affected population."""
    # Rule-based classification first
    for category in EU_AI_ACT_RISK_LEVELS["unacceptable"]["examples"]:
        if category in system.use_case.lower():
            return "unacceptable"

    for category in EU_AI_ACT_RISK_LEVELS["high"]["categories"]:
        if category in system.use_case.lower() or system.affected_population in ["vulnerable", "children"]:
            return "high"

    # LLM-assisted for ambiguous cases
    if not clear_classification:
        result = await openai.chat.completions.create(
            model="gpt-4o", temperature=0,
            messages=[{"role": "system", "content": f"""Classify this AI system's risk level under EU AI Act.
System: {system.description}
Use case: {system.use_case}
Affected population: {system.affected_population}
Respond with: unacceptable, high, limited, or minimal."""}]
        )
        return parse_risk_level(result)

    return "minimal"
```

## Step 4: Deploy Policy Enforcement Gates

```python
GOVERNANCE_POLICIES = {
    "registration_required": {
        "rule": "All AI systems must be registered before staging/production",
        "enforcement": "block_deployment_if_unregistered",
        "exceptions": None
    },
    "high_risk_oversight": {
        "rule": "High-risk AI must have human oversight plan",
        "enforcement": "block_if_no_oversight_plan",
        "required_fields": ["human_in_the_loop", "override_mechanism", "escalation_path"]
    },
    "review_compliance": {
        "rule": "Systems must be reviewed per schedule",
        "enforcement": "alert_owner_if_overdue",
        "escalation": "block_after_30_days_overdue"
    },
    "incident_reporting": {
        "rule": "Serious incidents must be reported within 72 hours",
        "enforcement": "auto_create_incident_report",
        "notify": ["governance_team", "system_owner", "ciso"]
    },
    "model_deprecation": {
        "rule": "Deprecated models must be retired within 90 days",
        "enforcement": "warn_at_60_days_block_at_90",
        "migration_plan_required": True
    }
}

async def enforce_policy(system: AISystem, action: str) -> PolicyResult:
    """Check if an action (deploy, update, deprecate) is allowed by policies."""
    violations = []
    for policy_name, policy in GOVERNANCE_POLICIES.items():
        if not check_policy_compliance(system, policy, action):
            violations.append(PolicyViolation(policy=policy_name, rule=policy["rule"]))

    if violations:
        return PolicyResult(allowed=False, violations=violations,
            recommended_actions=[v.remediation for v in violations])
    return PolicyResult(allowed=True)
```

## Step 5: Deploy Compliance Dashboard

```python
DASHBOARD_METRICS = {
    "organization_overview": {
        "total_ai_systems": "count(registry)",
        "by_risk_level": "group_by(risk_level).count()",
        "by_status": "group_by(status).count()",
        "compliance_rate": "compliant_systems / total_systems * 100",
        "overdue_reviews": "count(next_review < today)"
    },
    "risk_heatmap": {
        "dimensions": ["department", "risk_level"],
        "values": "system_count",
        "highlight": "overdue_or_non_compliant"
    },
    "incident_tracker": {
        "metrics": ["incident_count_30d", "severity_distribution", "mean_time_to_resolve"],
        "trend": "month_over_month"
    },
    "regulation_coverage": {
        "regulations": ["eu_ai_act", "gdpr", "nist_ai_rmf", "iso_42001"],
        "per_system": "compliance_status_per_regulation"
    }
}
```

## Step 6: Deploy Scheduled Review Engine

```bash
# Azure Functions timer trigger for scheduled reviews
# High-risk: quarterly
# Limited: annually
# Minimal: biannually

# Reviews check: model drift, data quality, incident history, policy changes
# Auto-generate review report with current compliance status
```

## Step 7: Smoke Test

```bash
# Register an AI system
curl -s https://api-governance.azurewebsites.net/api/register \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"name": "Customer Support Bot", "use_case": "chatbot", "affected_population": "general_public"}' | jq '.risk_level, .next_review'

# Check policy for deployment
curl -s https://api-governance.azurewebsites.net/api/policy-check \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"system_id": "sys-001", "action": "deploy_to_production"}' | jq '.allowed, .violations'

# Get compliance dashboard
curl -s https://api-governance.azurewebsites.net/api/dashboard \
  -H "Authorization: Bearer $TOKEN" | jq '.compliance_rate, .overdue_reviews'
```

## Troubleshooting

| Symptom | Cause | Fix |
| --- | --- | --- |
| Risk classification too conservative | LLM classifies everything as high | Add rule-based fast path for common minimal-risk cases |
| Shadow AI not captured | Teams deploy without registering | Integrate with CI/CD gates to enforce registration |
| Reviews always overdue | Review schedule too aggressive | Adjust: minimal → biannual, limited → annual |
| Policy violations not enforced | Gates not integrated with deployment | Add pre-deployment webhook to CI/CD pipeline |
| Dashboard data stale | Registry not updated | Require status update on every model version change |
