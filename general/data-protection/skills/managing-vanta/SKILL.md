---
name: managing-vanta
title: Vanta Management Skill
description: 'Use when working with Vanta — vanta compliance automation platform for SOC 2,

  ISO 27001, HIPAA, PCI DSS, and GDPR compliance monitoring. Covers test

  monitoring, evidence collection, vulnerability tracking, personnel compliance,

  and vendor risk management. Use when reviewing compliance test results,

  tracking failing tests, managing personnel security requirements, or preparing

  for compliance audits.'
author: cloudthinker-ai
author_url: https://github.com/cloudthinker-ai/CloudSkills/tree/main/skills/connections/managing-vanta
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Vanta Management Skill

Manage and analyze Vanta compliance tests, evidence, vulnerabilities, and personnel compliance.

## API Conventions

### Authentication
All API calls use `Authorization: Bearer $VANTA_API_TOKEN` -- injected automatically. Never hardcode tokens.

### Base URL
`https://api.vanta.com/v1`

### Core Helper Function

```bash
#!/bin/bash

vanta_api() {
    local method="$1"
    local endpoint="$2"
    local data="${3:-}"

    if [ -n "$data" ]; then
        curl -s -X "$method" \
            -H "Authorization: Bearer $VANTA_API_TOKEN" \
            -H "Content-Type: application/json" \
            "https://api.vanta.com/v1${endpoint}" \
            -d "$data"
    else
        curl -s -X "$method" \
            -H "Authorization: Bearer $VANTA_API_TOKEN" \
            -H "Content-Type: application/json" \
            "https://api.vanta.com/v1${endpoint}"
    fi
}
```

## Output Rules
- **TOKEN EFFICIENCY**: Extract only needed fields with `jq`
- Target <=50 lines per script output
- Never dump full API responses

## Discovery Phase

```bash
#!/bin/bash
echo "=== Test Summary ==="
vanta_api GET "/tests?pageSize=1" \
    | jq '"Total tests: \(.pageInfo.totalCount // "N/A")"' -r

echo ""
echo "=== Integrations ==="
vanta_api GET "/integrations" \
    | jq -r '.data[] | "\(.name)\t\(.status)\t\(.lastSyncedAt[0:16] // "Never")"' | column -t | head -10

echo ""
echo "=== Frameworks ==="
vanta_api GET "/frameworks" \
    | jq -r '.data[] | "\(.name)\t\(.status)"' | column -t
```

## Analysis Phase

### Test Results Overview

```bash
#!/bin/bash
echo "=== Tests by Status ==="
TESTS=$(vanta_api GET "/tests?pageSize=500")
echo "$TESTS" | jq '{
    total: (.data | length),
    passing: ([.data[] | select(.status == "PASSING")] | length),
    failing: ([.data[] | select(.status == "FAILING")] | length),
    disabled: ([.data[] | select(.status == "DISABLED")] | length)
}'

echo ""
echo "=== Failing Tests ==="
echo "$TESTS" | jq -r '.data[] | select(.status == "FAILING") | "\(.status)\t\(.name[0:50])\t\(.framework // "N/A")"' \
    | column -t | head -20

echo ""
echo "=== Tests by Category ==="
echo "$TESTS" | jq -r '[.data[].category] | group_by(.) | map({category: .[0], count: length}) | sort_by(.count) | reverse | .[:10][] | "\(.count)\t\(.category)"' | column -t
```

### Vulnerability Tracking

```bash
#!/bin/bash
echo "=== Open Vulnerabilities ==="
vanta_api GET "/vulnerabilities?status=open&pageSize=20" \
    | jq -r '.data[] | "\(.severity)\t\(.cveId // "N/A")\t\(.packageName[0:25])\t\(.affectedAsset[0:25])\t\(.status)"' \
    | column -t | head -20

echo ""
echo "=== Vulnerability Counts by Severity ==="
vanta_api GET "/vulnerabilities?status=open&pageSize=500" \
    | jq -r '[.data[].severity] | group_by(.) | map({severity: .[0], count: length}) | sort_by(.count) | reverse | .[] | "\(.severity): \(.count)"'
```

### Personnel Compliance

```bash
#!/bin/bash
echo "=== Personnel Overview ==="
vanta_api GET "/people?pageSize=200" \
    | jq '{
        total: (.data | length),
        compliant: ([.data[] | select(.complianceStatus == "COMPLIANT")] | length),
        non_compliant: ([.data[] | select(.complianceStatus == "NON_COMPLIANT")] | length),
        pending: ([.data[] | select(.complianceStatus == "PENDING")] | length)
    }'

echo ""
echo "=== Non-Compliant Personnel ==="
vanta_api GET "/people?pageSize=50&complianceStatus=NON_COMPLIANT" \
    | jq -r '.data[] | "\(.displayName)\t\(.email[0:30])\t\(.complianceStatus)\ttasks:\(.outstandingTaskCount // 0)"' \
    | column -t | head -15
```

### Vendor Risk

```bash
#!/bin/bash
echo "=== Vendors by Risk Level ==="
vanta_api GET "/vendors?pageSize=100" \
    | jq -r '[.data[].riskLevel] | group_by(.) | map({risk: .[0], count: length}) | sort_by(.count) | reverse | .[] | "\(.risk): \(.count)"'

echo ""
echo "=== High Risk Vendors ==="
vanta_api GET "/vendors?pageSize=50&riskLevel=HIGH" \
    | jq -r '.data[] | "\(.name[0:30])\t\(.riskLevel)\treviewStatus:\(.reviewStatus)\tlastReview:\(.lastReviewDate[0:10] // "Never")"' \
    | column -t | head -10
```

## Output Format

Present results as a structured report:
```
Managing Vanta Report
═════════════════════
Resources discovered: [count]

Resource       Status    Key Metric    Issues
──────────────────────────────────────────────
[name]         [ok/warn] [value]       [findings]

Summary: [total] resources | [ok] healthy | [warn] warnings | [crit] critical
Action Items: [list of prioritized findings]
```

Target ≤50 lines of output. Use tables for multi-resource comparisons.

## Anti-Hallucination Rules

1. **NEVER assume resource names** — always discover via CLI/API in Phase 1 before referencing in Phase 2.
2. **NEVER fabricate metric names or dimensions** — verify against the service documentation or `--help` output.
3. **NEVER mix CLI commands between service versions** — confirm which version/API you are targeting.
4. **ALWAYS use the discovery → verify → analyze chain** — every resource referenced must have been discovered first.
5. **ALWAYS handle empty results gracefully** — an empty response is valid data, not an error to retry.

## Counter-Rationalizations

| Shortcut | Counter | Why |
|----------|---------|-----|
| "I'll skip discovery and check known resources" | Always run Phase 1 discovery first | Resource names change, new resources appear — assumed names cause errors |
| "The user only asked for a quick check" | Follow the full discovery → analysis flow | Quick checks miss critical issues; structured analysis catches silent failures |
| "Default configuration is probably fine" | Audit configuration explicitly | Defaults often leave logging, security, and optimization features disabled |
| "Metrics aren't needed for this" | Always check relevant metrics when available | API/CLI responses show current state; metrics reveal trends and intermittent issues |
| "I don't have access to that" | Try the command and report the actual error | Assumed permission failures prevent useful investigation; actual errors are informative |

## Common Pitfalls

- **Pagination**: Use `pageSize` and cursor-based pagination via `pageInfo.endCursor`
- **Rate limits**: 60 requests/minute -- implement backoff
- **Test vs control**: Vanta uses "tests" (automated checks) rather than "controls"
- **Integration sync**: Test results depend on integration connections -- check sync status
- **Framework mapping**: Tests map to multiple frameworks -- filter by framework name
