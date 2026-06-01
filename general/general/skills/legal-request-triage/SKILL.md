---
name: legal-request-triage
title: Legal Request Triage
description: Triage incoming legal requests by classifying type, assigning priority based on urgency and business impact, and routing to the appropriate legal team
author: Happy-Technologies-LLC
author_url: https://github.com/Happy-Technologies-LLC/happy-platform-skills/tree/main/skills/legal/legal-request-triage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [legal, triage, request, routing, priority, legal-service-delivery]
---

# Legal Request Triage

## Overview

This skill provides a structured approach to triaging incoming legal service requests in ServiceNow Legal Service Delivery. It helps you:

- Identify and review new or unassigned legal requests from the `sn_legal_request` table
- Classify requests by type: contract review, compliance inquiry, intellectual property, employment law, litigation, or regulatory
- Assign priority based on urgency indicators and business impact assessment
- Route requests to the appropriate legal team or specialist
- Document triage decisions with work notes for audit trail

**When to use:** When legal requests are submitted through the Legal Service Delivery portal and need to be reviewed, categorized, prioritized, and routed to the correct legal team for action.

**Plugin required:** `com.sn_legal_service_delivery`

## Prerequisites

- **Roles:** `sn_legal_case_user`, `sn_legal_case_manager`, or `sn_legal_admin`
- **Access:** Read/write access to `sn_legal_request`, `sn_legal_case`, and `sn_legal_task` tables
- **Knowledge:** Understanding of your organization's legal team structure, request categories, and routing rules
- **Plugin:** Legal Service Delivery (`com.sn_legal_service_delivery`) must be activated

## Procedure

### Step 1: Identify Requests Requiring Triage

Query for active legal requests that are in a new or unassigned state.

**Using MCP (Claude Code/Desktop):**
```
Tool: SN-NL-Search
Parameters:
  table_name: sn_legal_request
  query: "new legal requests that are not yet assigned or triaged"
  fields: number,short_description,description,state,priority,request_type,requested_by,opened_at,assignment_group,assigned_to
  limit: 25
```

**Using REST API:**
```bash
GET /api/now/table/sn_legal_request?sysparm_query=active=true^assigned_toISEMPTY^ORstate=1&sysparm_fields=sys_id,number,short_description,description,state,priority,request_type,requested_by,opened_at,assignment_group,assigned_to,urgency,impact,business_unit&sysparm_limit=25&sysparm_display_value=true
```

### Step 2: Classify Each Request by Type

For each request, analyze the short description and description fields to determine the legal request type:

1. **Contract Review** - Keywords: "contract", "agreement", "NDA", "MSA", "SOW", "amendment", "renewal", "terms"
2. **Compliance Inquiry** - Keywords: "compliance", "regulation", "GDPR", "HIPAA", "SOX", "policy", "audit", "reporting requirement"
3. **Intellectual Property** - Keywords: "patent", "trademark", "copyright", "IP", "trade secret", "licensing", "infringement"
4. **Employment Law** - Keywords: "employment", "termination", "harassment", "discrimination", "workers comp", "FMLA", "ADA", "severance"
5. **Litigation** - Keywords: "lawsuit", "litigation", "claim", "dispute", "subpoena", "court order", "discovery", "deposition"
6. **Regulatory** - Keywords: "regulatory", "filing", "government", "agency", "investigation", "consent decree", "enforcement"

**Using MCP to retrieve request details:**
```
Tool: SN-Read-Record
Parameters:
  table_name: sn_legal_request
  sys_id: [request_sys_id]
  fields: number,short_description,description,state,priority,request_type,requested_by,business_unit,urgency,impact,opened_at
```

### Step 3: Assess Priority

Evaluate priority using a combination of urgency and business impact:

| Impact / Urgency | Critical (1) | High (2) | Medium (3) | Low (4) |
|-------------------|-------------|----------|------------|---------|
| Enterprise-wide (1) | P1 - Critical | P1 - Critical | P2 - High | P3 - Medium |
| Business Unit (2) | P1 - Critical | P2 - High | P3 - Medium | P4 - Low |
| Department (3) | P2 - High | P3 - Medium | P4 - Low | P4 - Low |
| Individual (4) | P3 - Medium | P4 - Low | P4 - Low | P5 - Planning |

**Urgency escalation indicators:**
- Regulatory filing deadline within 30 days
- Active litigation with court-imposed deadline
- Contract expiration within 14 days
- Executive or board-level request
- Potential financial exposure exceeding $100K
- Data breach or security incident with legal implications
- Government investigation or subpoena

### Step 4: Route to the Appropriate Legal Team

Map request types to legal teams (customize for your organization):

| Request Type | Assignment Group | Escalation Path |
|-------------|-----------------|-----------------|
| Contract Review | Contracts & Commercial | Senior Contracts Counsel |
| Compliance Inquiry | Compliance & Ethics | Chief Compliance Officer |
| Intellectual Property | IP & Technology | IP Counsel |
| Employment Law | Employment & Labor | Employment Counsel |
| Litigation | Litigation & Disputes | General Counsel |
| Regulatory | Regulatory Affairs | Regulatory Counsel |
| Unknown/Mixed | Legal Operations | Legal Triage Manager |

**Find the assignment group sys_id:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sys_user_group
  query: nameLIKEContracts
  fields: sys_id,name,manager,description
  limit: 5
```

**Using REST API:**
```bash
GET /api/now/table/sys_user_group?sysparm_query=nameLIKEContracts&sysparm_fields=sys_id,name,manager,description&sysparm_limit=5&sysparm_display_value=true
```

### Step 5: Update the Legal Request

Apply the triage classification, priority, and assignment.

**Using MCP:**
```
Tool: SN-Update-Record
Parameters:
  table_name: sn_legal_request
  sys_id: [request_sys_id]
  data:
    request_type: contract_review
    priority: 2
    urgency: 2
    impact: 2
    assignment_group: [group_sys_id]
    state: 2
```

**Using REST API:**
```bash
PATCH /api/now/table/sn_legal_request/{sys_id}
Content-Type: application/json

{
  "request_type": "contract_review",
  "priority": "2",
  "urgency": "2",
  "impact": "2",
  "assignment_group": "[group_sys_id]",
  "state": "2"
}
```

### Step 6: Create a Legal Case if Warranted

For requests that require formal legal engagement, create a legal case record.

**Using MCP:**
```
Tool: SN-Update-Record
Parameters:
  table_name: sn_legal_case
  sys_id: new
  data:
    short_description: "Contract Review - Vendor MSA Renewal for Acme Corp"
    description: "[Details from the legal request]"
    legal_request: [request_sys_id]
    priority: 2
    assignment_group: [group_sys_id]
    case_type: contract_review
    state: 1
```

**Using REST API:**
```bash
POST /api/now/table/sn_legal_case
Content-Type: application/json

{
  "short_description": "Contract Review - Vendor MSA Renewal for Acme Corp",
  "description": "[Details from the legal request]",
  "legal_request": "[request_sys_id]",
  "priority": "2",
  "assignment_group": "[group_sys_id]",
  "case_type": "contract_review",
  "state": "1"
}
```

### Step 7: Document the Triage Decision

Add work notes to the legal request documenting the triage rationale.

```
Tool: SN-Add-Work-Notes
Parameters:
  table_name: sn_legal_request
  sys_id: [request_sys_id]
  work_notes: |
    === LEGAL REQUEST TRIAGE ===
    Analyst: AI Legal Triage
    Timestamp: [current_timestamp]

    Classification: Contract Review
    Keywords detected: "MSA", "renewal", "vendor agreement"
    Business Unit: Procurement

    Priority Assessment:
    - Urgency: 2 (High) - Contract expires in 21 days
    - Impact: 2 (Business Unit) - Procurement operations affected
    - Calculated Priority: P2 - High

    Routing: Contracts & Commercial Team
    Rationale: Vendor MSA renewals are handled by the Contracts team per legal routing policy

    Legal Case Created: LC0004521
    Next Steps: Contracts team to review renewal terms and redlines within 5 business days
```

## Tool Usage

### MCP Tools Reference

| Tool | When to Use |
|------|-------------|
| `SN-NL-Search` | Natural language queries for legal requests |
| `SN-Query-Table` | Structured queries for requests, groups, users |
| `SN-Read-Record` | Retrieve a single legal request by sys_id |
| `SN-Update-Record` | Update request type, priority, assignment, state |
| `SN-Add-Work-Notes` | Document triage decisions and rationale |

### REST API Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/now/table/sn_legal_request` | GET | Query legal requests |
| `/api/now/table/sn_legal_request/{sys_id}` | PATCH | Update legal request |
| `/api/now/table/sn_legal_case` | POST | Create a legal case |
| `/api/now/table/sn_legal_task` | POST | Create legal tasks |
| `/api/now/table/sys_user_group` | GET | Find legal assignment groups |

## Best Practices

- **Respond promptly:** Legal requests with regulatory deadlines or litigation holds should be triaged within 4 hours
- **Classify accurately:** Misclassification causes delays; when uncertain, route to Legal Operations for manual review
- **Document thoroughly:** All triage decisions must include rationale for audit and compliance purposes
- **Check for duplicates:** Before creating a new case, query `sn_legal_case` for existing matters involving the same parties or subject
- **Escalate P1 immediately:** Critical requests (active litigation deadlines, regulatory enforcement) require immediate notification to the General Counsel
- **Protect privilege:** Never include privileged legal analysis in work notes visible to non-legal staff; use internal-only fields
- **Track SLAs:** Legal request SLAs vary by type; contract reviews typically have 5-day SLA, litigation matters require same-day response

## Troubleshooting

### "Legal request table not found"

**Cause:** Legal Service Delivery plugin is not activated
**Solution:** Verify that `com.sn_legal_service_delivery` plugin is active. Navigate to System Definition > Plugins and search for "Legal Service Delivery."

### "Cannot assign to legal group"

**Cause:** Assignment group does not have the legal type or is inactive
**Solution:** Query `sys_user_group` with `type=legal^active=true` to find valid legal groups. Verify group membership includes active attorneys.

### "Request type field not available"

**Cause:** The request_type choice list may not include your classification
**Solution:** Check `sys_choice` table: `name=sn_legal_request^element=request_type` to see available values. Add new choices through the dictionary if needed.

### "Insufficient permissions to create legal case"

**Cause:** Missing `sn_legal_case_user` or `sn_legal_case_manager` role
**Solution:** Verify user roles via `sys_user_has_role` table. The `sn_legal_admin` role includes all legal permissions.

## Examples

### Example 1: Contract Review Request Triage

**Input:** Legal Request LR0001234 - "Need legal review of new cloud services vendor agreement before signing"

**Analysis:**
- Keywords: "legal review", "vendor agreement", "signing" - Contract Review
- Urgency: Medium (no stated deadline)
- Impact: Department level (single procurement)
- Priority: P3

**Action:**
```
Tool: SN-Update-Record
Parameters:
  table_name: sn_legal_request
  sys_id: abc123...
  data:
    request_type: contract_review
    priority: 3
    assignment_group: [contracts_group_sys_id]
    state: 2
```

### Example 2: Urgent Regulatory Compliance Request

**Input:** Legal Request LR0001235 - "SEC filing deadline in 10 days - need review of 10-K disclosures for new acquisition"

**Analysis:**
- Keywords: "SEC filing", "deadline", "10-K", "disclosures" - Regulatory + Compliance
- Urgency: Critical (regulatory deadline in 10 days)
- Impact: Enterprise-wide (SEC filing affects entire company)
- Priority: P1

**Action:**
1. Set priority to P1 - Critical
2. Assign to Regulatory Affairs team
3. Notify General Counsel immediately
4. Create a legal case with deadline tracking

### Example 3: Employment Law Inquiry

**Input:** Legal Request LR0001236 - "HR needs guidance on employee termination process for underperformance in California office"

**Analysis:**
- Keywords: "termination", "employee", "California" - Employment Law
- Urgency: Medium (no immediate deadline stated)
- Impact: Individual level
- Priority: P4

**Action:**
```
Tool: SN-Update-Record
Parameters:
  table_name: sn_legal_request
  sys_id: def456...
  data:
    request_type: employment
    priority: 4
    assignment_group: [employment_group_sys_id]
    state: 2
```

## Related Skills

- `legal/legal-matter-summarization` - Summarize legal matters and case timelines
- `legal/contract-analysis` - Analyze contracts for key terms and risks
- `legal/contract-obligation-extraction` - Extract obligations from contracts
- `security/incident-response` - Security incidents with legal implications
- `grc/control-objective-management` - Compliance and regulatory controls
