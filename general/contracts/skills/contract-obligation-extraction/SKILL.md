---
name: contract-obligation-extraction
title: Contract Obligation Extraction
description: Extract obligations from contract documents including deadlines, deliverables, payment terms, SLA commitments, and termination conditions with compliance tracking
author: Happy-Technologies-LLC
author_url: https://github.com/Happy-Technologies-LLC/happy-platform-skills/tree/main/skills/legal/contract-obligation-extraction
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [legal, contract, obligation, extraction, compliance, tracking, deadlines, legal-service-delivery]
---

# Contract Obligation Extraction

## Overview

This skill provides a structured approach to extracting and tracking contractual obligations in ServiceNow Legal Service Delivery. It helps you:

- Parse contract documents from `ast_contract` and linked `sys_attachment` records to identify all binding obligations
- Categorize obligations by type: deliverables, payment terms, SLA commitments, reporting requirements, termination conditions, and compliance mandates
- Extract specific deadlines, milestones, and recurring obligation schedules
- Create trackable legal tasks in `sn_legal_task` for each obligation with due dates and owners
- Build an obligation register for portfolio-wide compliance monitoring
- Monitor obligation compliance status and generate variance reports

**When to use:** After contract execution to set up obligation tracking, during contract audits to verify compliance, when onboarding a new vendor relationship, or when preparing for contract renewal negotiations.

**Plugin required:** `com.sn_legal_service_delivery`

## Prerequisites

- **Roles:** `sn_legal_case_user`, `sn_legal_case_manager`, `contract_manager`, or `sn_legal_admin`
- **Access:** Read/write access to `ast_contract`, `sn_legal_task`, `sn_legal_case`, and `sys_attachment` tables
- **Knowledge:** Understanding of contract structures, obligation types, and your organization's compliance tracking requirements
- **Plugin:** Legal Service Delivery (`com.sn_legal_service_delivery`) must be activated

## Procedure

### Step 1: Retrieve the Contract Record and Documents

Fetch the contract metadata and associated document attachments.

**Using MCP (Claude Code/Desktop):**
```
Tool: SN-Read-Record
Parameters:
  table_name: ast_contract
  sys_id: [contract_sys_id]
  fields: sys_id,number,short_description,contract_type,vendor,starts,ends,renewal_date,payment_amount,payment_terms,total_cost,state,terms_and_conditions,auto_renew,notice_period,assigned_to,department
```

Retrieve attachments:
```
Tool: SN-Query-Table
Parameters:
  table_name: sys_attachment
  query: table_name=ast_contract^table_sys_id=[contract_sys_id]
  fields: sys_id,file_name,content_type,size_bytes,sys_created_on
  limit: 20
  order_by: sys_created_on
```

**Using REST API:**
```bash
# Get contract record
GET /api/now/table/ast_contract/[contract_sys_id]?sysparm_fields=sys_id,number,short_description,contract_type,vendor,starts,ends,renewal_date,payment_amount,payment_terms,total_cost,state,terms_and_conditions,auto_renew,notice_period,assigned_to,department&sysparm_display_value=true

# Get attachments
GET /api/now/table/sys_attachment?sysparm_query=table_name=ast_contract^table_sys_id=[contract_sys_id]&sysparm_fields=sys_id,file_name,content_type,size_bytes,sys_created_on&sysparm_limit=20

# Download contract document
GET /api/now/attachment/[attachment_sys_id]/file
```

### Step 2: Retrieve Existing Terms and Conditions

If Contract Lifecycle Management is active, query linked terms.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: clm_m2m_contract_and_terms
  query: contract=[contract_sys_id]
  fields: sys_id,contract,terms_and_conditions,state
  limit: 50
```

Then retrieve the term details:
```
Tool: SN-Query-Table
Parameters:
  table_name: clm_terms_and_conditions
  query: sys_idIN[terms_sys_ids]
  fields: sys_id,name,description,category,obligation_type,obligation_owner,due_date,frequency,status
  limit: 50
```

**Using REST API:**
```bash
GET /api/now/table/clm_m2m_contract_and_terms?sysparm_query=contract=[contract_sys_id]&sysparm_fields=sys_id,contract,terms_and_conditions,state&sysparm_limit=50

GET /api/now/table/clm_terms_and_conditions?sysparm_query=sys_idIN[terms_sys_ids]&sysparm_fields=sys_id,name,description,category,obligation_type,obligation_owner,due_date,frequency,status&sysparm_limit=50&sysparm_display_value=true
```

### Step 3: Extract Obligations by Category

Parse the contract text and categorize each obligation:

#### 3a. Payment Obligations

| Field | What to Extract | Example |
|-------|----------------|---------|
| Amount | Dollar value per payment | $25,000/month |
| Frequency | Payment schedule | Monthly, quarterly, annual |
| Net Terms | Days until payment due | Net 30, Net 45, Net 60 |
| Late Fees | Penalty for late payment | 1.5% per month on overdue |
| Escalation | Annual price increase | 3% annual escalation |
| True-up | Usage reconciliation | Quarterly true-up for overages |
| Milestone Payments | Deliverable-triggered | 30% at kickoff, 40% at UAT, 30% at go-live |

#### 3b. Deliverable Obligations

| Field | What to Extract | Example |
|-------|----------------|---------|
| Deliverable | What must be provided | Monthly security audit report |
| Owner | Party responsible | Vendor / Client |
| Due Date | When due | 15th of each month |
| Acceptance Criteria | How measured | Per Exhibit B specifications |
| Cure Period | Time to fix deficiencies | 10 business days |

#### 3c. SLA Commitments

| Field | What to Extract | Example |
|-------|----------------|---------|
| Metric | SLA measurement | System uptime |
| Target | Required level | 99.95% monthly |
| Measurement Period | Window | Calendar month |
| Credit | Remedy for miss | 5% credit per 0.1% below target |
| Exclusions | What is excluded | Scheduled maintenance windows |
| Chronic Failure | Repeated misses | 3 consecutive misses = termination right |

#### 3d. Compliance and Reporting

| Field | What to Extract | Example |
|-------|----------------|---------|
| Report | Required reporting | SOC 2 Type II audit report |
| Frequency | How often | Annually |
| Deadline | When due | Within 90 days of audit period end |
| Certification | Required certs | ISO 27001, SOC 2, HITRUST |
| Data Handling | Privacy requirements | GDPR DPA, data residency in EU |
| Breach Notification | Incident reporting | Within 72 hours of discovery |

#### 3e. Termination Conditions

| Field | What to Extract | Example |
|-------|----------------|---------|
| For Cause | Triggers | Material breach uncured after 30 days |
| For Convenience | Notice required | 90 days written notice |
| Wind-down | Transition period | 6-month transition assistance |
| Data Return | Post-termination | Return all data within 30 days |
| Survival | Surviving clauses | Sections 7, 8, 12, 15 survive |

### Step 4: Create an Obligation Register

Build a consolidated obligation register by creating legal tasks for each extracted obligation.

**Using MCP:**
```
Tool: SN-Create-Record
Parameters:
  table_name: sn_legal_task
  fields:
    short_description: "Payment obligation - Monthly license fee $25,000"
    description: |
      Contract: [contract_number]
      Vendor: [vendor_name]
      Obligation Type: Payment
      Amount: $25,000
      Frequency: Monthly
      Due: 1st of each month
      Net Terms: Net 30
      Late Fee: 1.5% per month
      Contract Reference: Section 4.1
    legal_case: [case_sys_id]
    priority: 3
    task_type: obligation_tracking
    assigned_to: [finance_contact_sys_id]
    due_date: [next_payment_date]
    state: 1
```

Repeat for each obligation category. Example for SLA tracking:
```
Tool: SN-Create-Record
Parameters:
  table_name: sn_legal_task
  fields:
    short_description: "SLA monitoring - 99.95% uptime commitment"
    description: |
      Contract: [contract_number]
      Vendor: [vendor_name]
      Obligation Type: SLA
      Metric: System uptime
      Target: 99.95% monthly
      Credit: 5% per 0.1% below target
      Chronic Failure: 3 consecutive misses triggers termination right
      Contract Reference: Exhibit C, Section 2.1
    legal_case: [case_sys_id]
    priority: 2
    task_type: obligation_tracking
    assigned_to: [service_manager_sys_id]
    due_date: [month_end_date]
    state: 1
```

**Using REST API:**
```bash
POST /api/now/table/sn_legal_task
Content-Type: application/json

{
  "short_description": "Payment obligation - Monthly license fee $25,000",
  "description": "Contract: CON0045678\nObligation Type: Payment\nAmount: $25,000\nFrequency: Monthly\nDue: 1st of each month\nNet Terms: Net 30",
  "legal_case": "[case_sys_id]",
  "priority": "3",
  "task_type": "obligation_tracking",
  "assigned_to": "[finance_contact_sys_id]",
  "due_date": "[next_payment_date]",
  "state": "1"
}
```

### Step 5: Set Up Obligation Compliance Monitoring

Query existing obligation tasks to track compliance status.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_legal_task
  query: legal_case.legal_matter=[matter_sys_id]^task_type=obligation_tracking
  fields: sys_id,number,short_description,state,due_date,assigned_to,priority,work_notes
  limit: 100
  order_by: due_date
```

**Using REST API:**
```bash
GET /api/now/table/sn_legal_task?sysparm_query=legal_case.legal_matter=[matter_sys_id]^task_type=obligation_tracking^ORDERBYdue_date&sysparm_fields=sys_id,number,short_description,state,due_date,assigned_to,priority,work_notes&sysparm_limit=100&sysparm_display_value=true
```

Monitor overdue obligations:
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_legal_task
  query: task_type=obligation_tracking^due_date<javascript:gs.beginningOfToday()^state!=3^state!=7
  fields: sys_id,number,short_description,due_date,assigned_to,legal_case,priority
  limit: 50
  order_by: due_date
```

### Step 6: Generate Obligation Compliance Report

Document the full obligation register and compliance status.

**Using MCP:**
```
Tool: SN-Add-Work-Notes
Parameters:
  table_name: sn_legal_case
  sys_id: [case_sys_id]
  work_notes: |
    === OBLIGATION EXTRACTION REPORT ===
    Contract: [contract_number] - [short_description]
    Vendor: [vendor_name]
    Effective: [start_date] to [end_date]
    Analyst: AI Obligation Analyst
    Date: [current_date]

    OBLIGATION SUMMARY:
    Total Obligations Extracted: [total_count]
    - Payment: [payment_count]
    - Deliverables: [deliverable_count]
    - SLA Commitments: [sla_count]
    - Compliance/Reporting: [compliance_count]
    - Termination Conditions: [termination_count]

    PAYMENT OBLIGATIONS:
    1. Monthly license fee: $25,000 due 1st of month (Net 30)
    2. Annual support fee: $50,000 due January 15
    3. Quarterly true-up: Variable, due 15th after quarter end
    Total Annual Financial Commitment: $350,000 + overages

    DELIVERABLE OBLIGATIONS:
    1. Monthly security report: Due 15th of each month (Vendor)
    2. Quarterly business review: Due within 30 days of quarter end (Mutual)
    3. Annual SOC 2 report: Due within 90 days of audit period (Vendor)

    SLA COMMITMENTS:
    1. System uptime: 99.95% monthly (5% credit per 0.1% miss)
    2. Support response: P1 within 1 hour, P2 within 4 hours
    3. Data backup: Daily with 4-hour RPO

    KEY DEADLINES:
    | Date | Obligation | Owner | Task # |
    |------|-----------|-------|--------|
    | Monthly 1st | License payment | Client | LT0012345 |
    | Monthly 15th | Security report | Vendor | LT0012346 |
    | Quarterly | Business review | Mutual | LT0012347 |
    | 2026-12-01 | Renewal notice deadline | Client | LT0012348 |

    COMPLIANCE STATUS:
    - On Track: [on_track_count] obligations
    - At Risk: [at_risk_count] obligations
    - Overdue: [overdue_count] obligations

    RECOMMENDED ACTIONS:
    1. Configure automated reminders for payment due dates
    2. Assign SLA monitoring to service delivery team
    3. Calendar renewal notice deadline 90 days before expiration
    4. Schedule quarterly obligation compliance review
```

### Step 7: Update Contract with Obligation Metadata

Record obligation extraction results on the contract record.

**Using MCP:**
```
Tool: SN-Update-Record
Parameters:
  table_name: ast_contract
  sys_id: [contract_sys_id]
  data:
    work_notes: "Obligation extraction completed. [total_count] obligations identified and tracked. See legal case [case_number] for full register. Next review: [next_review_date]."
```

**Using REST API:**
```bash
PATCH /api/now/table/ast_contract/[contract_sys_id]
Content-Type: application/json

{
  "work_notes": "Obligation extraction completed. 14 obligations identified and tracked across 5 categories."
}
```

## Tool Usage

### MCP Tools Reference

| Tool | When to Use |
|------|-------------|
| `SN-NL-Search` | Find contracts by vendor, type, or obligation keywords |
| `SN-Query-Table` | Query contracts, tasks, terms, and attachments |
| `SN-Read-Record` | Retrieve a specific contract record |
| `SN-Create-Record` | Create obligation tracking tasks |
| `SN-Update-Record` | Update contract metadata and task status |
| `SN-Add-Work-Notes` | Document the obligation register and compliance reports |

### REST API Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/now/table/ast_contract` | GET | Query contract records |
| `/api/now/table/ast_contract/{sys_id}` | GET/PATCH | Read or update a contract |
| `/api/now/table/sn_legal_task` | GET/POST | Query or create obligation tasks |
| `/api/now/table/sn_legal_case` | GET | Query associated legal cases |
| `/api/now/table/sys_attachment` | GET | Retrieve contract attachments |
| `/api/now/attachment/{sys_id}/file` | GET | Download contract documents |
| `/api/now/table/clm_terms_and_conditions` | GET | Query CLM terms records |

## Best Practices

- **Be exhaustive:** Extract every obligation, not just the obvious ones; minor reporting obligations often cause compliance failures
- **Assign owners:** Every obligation must have a named responsible party, not just a department
- **Lead time:** Set task due dates with sufficient lead time before the actual contractual deadline (e.g., 5 business days before)
- **Recurring obligations:** For monthly or quarterly obligations, create a master task and use ServiceNow scheduled jobs to generate recurring child tasks
- **Two-way obligations:** Track obligations that bind your organization separately from those that bind the vendor
- **Version awareness:** Re-extract obligations whenever a contract amendment or change order is executed
- **Link to source:** Always reference the specific contract section number in the obligation description for traceability
- **Financial impact:** Tag each obligation with its financial impact to support budgeting and accruals

## Troubleshooting

### "Cannot find obligation-related fields on ast_contract"

**Cause:** Standard `ast_contract` may not have obligation-specific fields; these may be in CLM extension tables
**Solution:** Check `clm_terms_and_conditions` and `clm_m2m_contract_and_terms` for structured obligation data. Query `sys_dictionary` with `nameLIKEclm^elementLIKEobligation` to find relevant fields.

### "Duplicate obligations detected"

**Cause:** The same obligation may appear in multiple contract sections or amendments
**Solution:** Before creating a new obligation task, query existing tasks: `sn_legal_task` with `legal_case=[case_sys_id]^short_descriptionLIKE[obligation_keyword]` to check for duplicates.

### "Recurring obligation tasks not generating"

**Cause:** Scheduled job for recurring task creation is not configured
**Solution:** Create a scheduled script execution on `sn_legal_task` that clones recurring obligation tasks based on frequency field. Check `sysauto_script` for existing obligation-related jobs.

### "Unable to parse contract attachment"

**Cause:** Contract document is in a scanned PDF or image format without OCR
**Solution:** Use ServiceNow Document Intelligence (`com.sn_doc_intelligence`) to perform OCR extraction. See the `document/document-extraction` skill for configuration steps.

## Examples

### Example 1: SaaS Agreement Obligation Extraction

**Input:** Contract CON0045678 - "Enterprise CRM Platform - CloudCo"

**Obligations extracted:**
1. Payment: $150,000 annual license, due January 1, Net 45
2. Payment: Overage at $2/user/month above 500 users, quarterly true-up
3. SLA: 99.9% uptime, measured monthly, 10% credit per 0.5% miss
4. Deliverable: Monthly usage report by 10th of month
5. Compliance: SOC 2 Type II report annually within 90 days of audit
6. Data: Breach notification within 48 hours
7. Termination: 90 days written notice for convenience; 30 days cure for cause
8. Data return: All data exported within 30 days of termination

**Tasks created:** 8 obligation tracking tasks in `sn_legal_task`

### Example 2: Professional Services Contract

**Input:** Contract CON0046789 - "IT Consulting Services - TechPartners Inc"

**Obligations extracted:**
```
Tool: SN-Create-Record
Parameters:
  table_name: sn_legal_task
  fields:
    short_description: "Milestone payment - Phase 1 completion $75,000"
    description: |
      Contract: CON0046789
      Obligation Type: Milestone Payment
      Amount: $75,000
      Trigger: Phase 1 UAT sign-off
      Net Terms: Net 30 from acceptance
      Contract Reference: Exhibit A, Milestone 2
    legal_case: [case_sys_id]
    priority: 2
    task_type: obligation_tracking
    assigned_to: [project_manager_sys_id]
    due_date: 2026-06-30
    state: 1
```

### Example 3: Obligation Compliance Audit

**Input:** "Show all overdue obligations across active contracts"

**Query:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_legal_task
  query: task_type=obligation_tracking^active=true^due_date<javascript:gs.beginningOfToday()^stateNOT IN3,4,7
  fields: sys_id,number,short_description,due_date,assigned_to,legal_case.short_description,priority,state
  limit: 50
  order_by: due_date
```

**Result:** 6 overdue obligations found:
- 2 vendor reporting obligations (SOC 2 report 15 days late)
- 1 payment obligation (quarterly true-up 5 days past due)
- 3 internal deliverables (business review meeting scheduling)

**Action:** Escalate vendor obligations; update internal task owners; document compliance gaps.

## Related Skills

- `legal/contract-analysis` - Analyze contracts for key terms and risk assessment
- `legal/legal-request-triage` - Triage incoming contract review requests
- `legal/legal-matter-summarization` - Summarize legal matters linked to contracts
- `document/document-extraction` - Extract structured data from contract documents using OCR
- `catalog/approval-workflows` - Configure approval workflows for obligation sign-offs
