---
name: contract-analysis-happy-technologies-llc
title: Contract Analysis
description: Analyze contracts for key terms, obligations, risks, renewal dates, and compliance requirements with metadata extraction and clause flagging
author: Happy-Technologies-LLC
author_url: https://github.com/Happy-Technologies-LLC/happy-platform-skills/tree/main/skills/legal/contract-analysis
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [legal, contract, analysis, risk, compliance, terms, renewal, legal-service-delivery]
---

# Contract Analysis

## Overview

This skill provides a structured approach to analyzing contracts within ServiceNow Legal Service Delivery and Contract Lifecycle Management. It helps you:

- Retrieve contract records from `ast_contract` and associated legal cases from `sn_legal_case`
- Extract and catalog key terms including payment, liability, indemnification, and termination provisions
- Identify obligations and deadlines for both parties across the contract lifecycle
- Flag high-risk clauses such as unlimited liability, automatic renewal, broad IP assignment, or non-standard terms
- Track renewal dates, expiration windows, and notice period requirements
- Assess compliance requirements including regulatory, data privacy, and industry-specific mandates
- Generate structured analysis reports for legal review and business stakeholder consumption

**When to use:** When a new contract needs legal review, during contract renewal assessments, for portfolio-wide risk audits, or when business stakeholders need a plain-language summary of contractual obligations.

**Plugin required:** `com.sn_legal_service_delivery`

## Prerequisites

- **Roles:** `sn_legal_case_user`, `sn_legal_case_manager`, `contract_manager`, or `sn_legal_admin`
- **Access:** Read access to `ast_contract`, `sn_legal_case`, `sn_legal_task`, and `sys_attachment` tables
- **Knowledge:** Understanding of contract law fundamentals, your organization's standard contract terms, and risk tolerance thresholds
- **Plugin:** Legal Service Delivery (`com.sn_legal_service_delivery`) must be activated. Optional: Contract Lifecycle Management for enhanced contract metadata.

## Procedure

### Step 1: Retrieve the Contract Record

Query the contract to obtain its core metadata and current status.

**Using MCP (Claude Code/Desktop):**
```
Tool: SN-Get-Record
Parameters:
  table_name: ast_contract
  sys_id: [contract_sys_id]
  fields: sys_id,number,short_description,contract_type,vendor,starts,ends,renewal_date,payment_amount,total_cost,state,terms_and_conditions,auto_renew,notice_period,assigned_to,department,contract_administrator,parent_contract
```

**Using REST API:**
```bash
GET /api/now/table/ast_contract/[contract_sys_id]?sysparm_fields=sys_id,number,short_description,contract_type,vendor,starts,ends,renewal_date,payment_amount,total_cost,state,terms_and_conditions,auto_renew,notice_period,assigned_to,department,contract_administrator,parent_contract&sysparm_display_value=true
```

### Step 2: Retrieve the Contract Document

Fetch attachments to access the actual contract text for analysis.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sys_attachment
  query: table_name=ast_contract^table_sys_id=[contract_sys_id]
  fields: sys_id,file_name,content_type,size_bytes,sys_created_on,sys_created_by
  limit: 20
  order_by: sys_created_on
```

**Using REST API:**
```bash
GET /api/now/table/sys_attachment?sysparm_query=table_name=ast_contract^table_sys_id=[contract_sys_id]^ORDERBYDESCsys_created_on&sysparm_fields=sys_id,file_name,content_type,size_bytes,sys_created_on,sys_created_by&sysparm_limit=20
```

To download the attachment content:
```bash
GET /api/now/attachment/[attachment_sys_id]/file
```

### Step 3: Extract Key Contract Terms

Analyze the contract for the following term categories:

| Term Category | Key Fields to Extract | Risk Indicators |
|--------------|----------------------|-----------------|
| **Payment Terms** | Amount, frequency, net days, late fees, escalation | Net 15 or shorter; annual escalation > 5% |
| **Liability** | Cap amount, exclusions, consequential damages | Unlimited liability; no mutual cap |
| **Indemnification** | Scope, carve-outs, defense obligations | Broad indemnity without IP carve-out |
| **Termination** | For cause triggers, convenience period, wind-down | No termination for convenience; > 12-month lock-in |
| **Renewal** | Auto-renew, notice period, price adjustment | Auto-renew with < 60-day notice window |
| **Confidentiality** | Duration, scope, permitted disclosures | Perpetual confidentiality; no carve-outs |
| **IP Rights** | Ownership, license grants, work product | Broad IP assignment to vendor; no license-back |
| **Data Privacy** | Data handling, breach notification, DPA | No DPA; breach notification > 72 hours |
| **SLA/Performance** | Uptime, response times, credits, remedies | No SLA credits; no termination for chronic failure |
| **Governing Law** | Jurisdiction, dispute resolution, venue | Foreign jurisdiction; mandatory arbitration |

### Step 4: Assess Risk Level

Score each term category and compute an overall contract risk level:

**Risk scoring framework:**
- **Low (1):** Term aligns with organizational standards, no deviation
- **Medium (2):** Minor deviation from standard; acceptable with documentation
- **High (3):** Significant deviation; requires senior counsel approval
- **Critical (4):** Unacceptable term; must be renegotiated before execution

**Overall risk calculation:**
- Any single Critical (4) score = Overall Critical
- Average score >= 3.0 = Overall High
- Average score >= 2.0 = Overall Medium
- Average score < 2.0 = Overall Low

### Step 5: Check for Related Legal Cases and Matters

Query for any existing legal activity related to this contract or vendor.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_legal_case
  query: short_descriptionLIKE[vendor_name]^ORdescriptionLIKE[contract_number]
  fields: sys_id,number,short_description,state,case_type,priority,assigned_to,resolution_notes
  limit: 10
```

**Using REST API:**
```bash
GET /api/now/table/sn_legal_case?sysparm_query=short_descriptionLIKE[vendor_name]^ORdescriptionLIKE[contract_number]&sysparm_fields=sys_id,number,short_description,state,case_type,priority,assigned_to,resolution_notes&sysparm_limit=10&sysparm_display_value=true
```

### Step 6: Flag Concerning Clauses

Create legal tasks for each clause that requires attention or renegotiation.

**Using MCP:**
```
Tool: SN-Create-Record
Parameters:
  table_name: sn_legal_task
  fields:
    short_description: "Review unlimited liability clause - Section 8.2"
    description: "Contract [contract_number] contains an unlimited liability provision in Section 8.2. Organization standard requires liability cap at 12 months of fees. Recommend renegotiation to add mutual liability cap."
    legal_case: [case_sys_id]
    priority: 2
    task_type: contract_review
    assigned_to: [counsel_sys_id]
    due_date: [review_deadline]
    state: 1
```

**Using REST API:**
```bash
POST /api/now/table/sn_legal_task
Content-Type: application/json

{
  "short_description": "Review unlimited liability clause - Section 8.2",
  "description": "Contract contains unlimited liability. Standard requires cap at 12 months of fees.",
  "legal_case": "[case_sys_id]",
  "priority": "2",
  "task_type": "contract_review",
  "assigned_to": "[counsel_sys_id]",
  "due_date": "[review_deadline]",
  "state": "1"
}
```

### Step 7: Generate the Contract Analysis Report

Document the complete analysis as work notes on the legal case.

**Using MCP:**
```
Tool: SN-Add-Work-Notes
Parameters:
  table_name: sn_legal_case
  sys_id: [case_sys_id]
  work_notes: |
    === CONTRACT ANALYSIS REPORT ===
    Contract: [contract_number] - [short_description]
    Vendor: [vendor_name]
    Analyst: AI Contract Analyst
    Date: [current_date]

    CONTRACT OVERVIEW:
    - Type: [contract_type]
    - Effective: [start_date] to [end_date]
    - Total Value: $[total_cost]
    - Auto-Renewal: [Yes/No] | Notice Period: [notice_period] days
    - Governing Law: [jurisdiction]

    KEY TERMS SUMMARY:
    1. Payment: [payment_summary]
    2. Liability Cap: [liability_summary]
    3. Indemnification: [indemnity_summary]
    4. Termination: [termination_summary]
    5. Data Privacy: [privacy_summary]
    6. IP Rights: [ip_summary]
    7. SLA/Performance: [sla_summary]

    RISK ASSESSMENT:
    - Overall Risk Level: [HIGH/MEDIUM/LOW]
    - Critical Issues: [count]
    - High-Risk Items: [count]

    FLAGGED CLAUSES:
    1. [CRITICAL] Section 8.2 - Unlimited liability (standard: 12-month cap)
    2. [HIGH] Section 12.1 - Auto-renew with 30-day notice (standard: 90 days)
    3. [HIGH] Section 15.3 - No DPA attached (required for data processing)
    4. [MEDIUM] Section 6.4 - IP assignment broader than industry standard

    COMPLIANCE REQUIREMENTS:
    - GDPR: [compliant/non-compliant] - [details]
    - SOC 2: [compliant/non-compliant] - [details]
    - Industry-specific: [details]

    RECOMMENDED ACTIONS:
    1. Renegotiate liability cap to 12 months of annual fees
    2. Extend auto-renewal notice period to 90 days
    3. Execute Data Processing Agreement before contract signing
    4. Narrow IP assignment clause to deliverables only

    RENEWAL CALENDAR:
    - Contract Expires: [end_date]
    - Renewal Decision Deadline: [notice_date]
    - Days Until Notice Required: [days_remaining]
```

### Step 8: Update Contract Metadata

Record analysis results back to the contract record for portfolio tracking.

**Using MCP:**
```
Tool: SN-Update-Record
Parameters:
  table_name: ast_contract
  sys_id: [contract_sys_id]
  data:
    risk_level: high
    review_date: [current_date]
    short_description: "[original_description] [REVIEWED]"
    work_notes: "Legal analysis completed. Risk level: HIGH. 4 flagged clauses require renegotiation. See legal case [case_number] for full analysis."
```

**Using REST API:**
```bash
PATCH /api/now/table/ast_contract/[contract_sys_id]
Content-Type: application/json

{
  "risk_level": "high",
  "review_date": "[current_date]",
  "work_notes": "Legal analysis completed. Risk level: HIGH. 4 flagged clauses."
}
```

## Tool Usage

### MCP Tools Reference

| Tool | When to Use |
|------|-------------|
| `SN-Natural-Language-Search` | Find contracts by vendor name, type, or description |
| `SN-Query-Table` | Structured queries for contracts, cases, tasks, attachments |
| `SN-Get-Record` | Retrieve a single contract or case by sys_id |
| `SN-Create-Record` | Create legal tasks for flagged clauses |
| `SN-Update-Record` | Update contract risk level and review metadata |
| `SN-Add-Work-Notes` | Post the analysis report to the legal case |

### REST API Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/now/table/ast_contract` | GET | Query contracts |
| `/api/now/table/ast_contract/{sys_id}` | GET/PATCH | Read or update a contract |
| `/api/now/table/sn_legal_case` | GET/POST | Query or create legal cases |
| `/api/now/table/sn_legal_task` | POST | Create review tasks for flagged clauses |
| `/api/now/table/sys_attachment` | GET | Retrieve contract document attachments |
| `/api/now/attachment/{sys_id}/file` | GET | Download attachment content |

## Best Practices

- **Use playbooks:** Maintain standard analysis templates for each contract type (SaaS, professional services, NDA, license) to ensure consistency
- **Compare to standards:** Always compare terms against your organization's approved contract templates and fallback positions
- **Track deviations:** Document every deviation from standard terms, even if accepted, for portfolio-wide risk visibility
- **Set renewal alerts:** Create calendar reminders at least 90 days before auto-renewal notice deadlines
- **Cross-reference vendors:** Check for other active contracts with the same vendor to identify aggregate exposure
- **Privilege protection:** Mark all analysis work notes as Attorney-Client Privileged; do not share raw analysis with non-legal staff
- **Regulatory awareness:** Always check for jurisdiction-specific requirements (GDPR for EU vendors, CCPA for California, etc.)
- **Version tracking:** Note which version of the contract was analyzed; flag if amendments or side letters exist

## Troubleshooting

### "Contract record not found in ast_contract"

**Cause:** The contract may be stored in a different table depending on your CLM configuration
**Solution:** Check `clm_contract_document`, `sn_sm_contract`, or custom contract tables. Query `sys_db_object` with `nameLIKEcontract` to find all contract-related tables.

### "Cannot access contract attachment"

**Cause:** Attachment ACLs restrict access, or the document is stored externally
**Solution:** Verify you have the `itil` or `contract_manager` role. Check if the contract references an external URL field for document storage.

### "Risk level field not available on ast_contract"

**Cause:** The field may be a custom addition or part of an optional plugin
**Solution:** Query `sys_dictionary` with `name=ast_contract^elementLIKErisk` to find available risk-related fields. Create a custom field if needed.

### "Renewal date calculation seems incorrect"

**Cause:** Auto-renewal logic may depend on custom business rules or the `notice_period` field format
**Solution:** Verify the `notice_period` field stores days (not months). Check business rules on `ast_contract` that compute renewal dates: `sys_script` with `collection=ast_contract^scriptLIKErenewal`.

## Examples

### Example 1: SaaS Vendor Agreement Review

**Input:** Contract CON0045678 - "Enterprise SaaS Platform - 3-year agreement with DataCorp"

**Analysis:**
- Total value: $1.2M over 3 years
- Auto-renew: Yes, 30-day notice (flagged: below 90-day standard)
- Liability: Capped at 12 months fees (acceptable)
- SLA: 99.9% uptime with credits (acceptable)
- Data privacy: No DPA included (critical: required for GDPR)
- Overall risk: HIGH (missing DPA)

**Action:** Create legal task to draft and execute DPA before contract signing.

### Example 2: NDA Review

**Input:** Contract CON0045679 - "Mutual NDA with AcquiCo for M&A due diligence"

**Analysis:**
- Duration: 3 years with 2-year survival after termination
- Scope: Appropriately limited to transaction evaluation
- Residual knowledge clause: Present (medium risk)
- Non-solicitation: 18-month rider attached (needs review)
- Overall risk: MEDIUM

**Action:**
```
Tool: SN-Update-Record
Parameters:
  table_name: ast_contract
  sys_id: def456abc...
  data:
    risk_level: medium
    review_date: 2026-03-19
    work_notes: "NDA reviewed. Medium risk. Residual knowledge clause and non-solicitation rider flagged for counsel review."
```

### Example 3: Contract Portfolio Risk Audit

**Input:** "Analyze all contracts expiring in the next 90 days"

**Query:**
```
Tool: SN-Query-Table
Parameters:
  table_name: ast_contract
  query: active=true^endsBETWEENjavascript:gs.beginningOfToday()@javascript:gs.daysAgoEnd(-90)
  fields: sys_id,number,short_description,vendor,ends,auto_renew,notice_period,total_cost,risk_level
  limit: 50
  order_by: ends
```

**Result:** 12 contracts expiring, 4 with auto-renew requiring notice within 30 days, 2 with no documented risk assessment. Prioritize these 6 for immediate review.

## Related Skills

- `legal/legal-request-triage` - Triage incoming contract review requests
- `legal/contract-obligation-extraction` - Extract specific obligations from contracts
- `legal/legal-matter-summarization` - Summarize legal matters linked to contracts
- `document/document-extraction` - Extract structured data from contract documents
- `document/smart-documents` - Manage contract templates and generation
