---
name: legal-matter-summarization
title: Legal Matter Summarization
description: Summarize legal matters with case timeline, key documents, parties involved, financial exposure, and recommended actions for legal leadership reporting
author: Happy-Technologies-LLC
author_url: https://github.com/Happy-Technologies-LLC/happy-platform-skills/tree/main/skills/legal/legal-matter-summarization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [legal, matter, summarization, case-timeline, reporting, legal-service-delivery]
---

# Legal Matter Summarization

## Overview

This skill provides a structured approach to summarizing legal matters in ServiceNow Legal Service Delivery. It helps you:

- Retrieve and consolidate all information about a legal matter from `sn_legal_matter` and related tables
- Build a chronological timeline of case events from tasks, work notes, and state transitions
- Identify key documents, attachments, and correspondence linked to the matter
- Catalog all parties involved including internal stakeholders, opposing counsel, and external entities
- Calculate financial exposure including potential liability, settlement ranges, and legal spend
- Generate executive-ready status reports for legal leadership and the General Counsel

**When to use:** When legal leadership needs a comprehensive briefing on a matter, when preparing for board reports, during case reviews, or when onboarding new counsel to an existing matter.

**Plugin required:** `com.sn_legal_service_delivery`

## Prerequisites

- **Roles:** `sn_legal_case_user`, `sn_legal_case_manager`, or `sn_legal_admin`
- **Access:** Read access to `sn_legal_matter`, `sn_legal_case`, `sn_legal_task`, `sn_legal_hold`, and `sys_attachment` tables
- **Knowledge:** Familiarity with your organization's legal matter taxonomy, matter lifecycle states, and reporting requirements
- **Plugin:** Legal Service Delivery (`com.sn_legal_service_delivery`) must be activated

## Procedure

### Step 1: Retrieve the Legal Matter Record

Query the legal matter to obtain its core details, including current state, assigned counsel, and matter type.

**Using MCP (Claude Code/Desktop):**
```
Tool: SN-Read-Record
Parameters:
  table_name: sn_legal_matter
  sys_id: [matter_sys_id]
  fields: sys_id,number,short_description,description,state,priority,matter_type,practice_area,assigned_to,assignment_group,opened_at,closed_at,financial_exposure,settlement_amount,outside_counsel,business_unit,risk_level
```

**Using REST API:**
```bash
GET /api/now/table/sn_legal_matter/[matter_sys_id]?sysparm_fields=sys_id,number,short_description,description,state,priority,matter_type,practice_area,assigned_to,assignment_group,opened_at,closed_at,financial_exposure,settlement_amount,outside_counsel,business_unit,risk_level&sysparm_display_value=true
```

### Step 2: Gather Associated Legal Cases

Retrieve all cases linked to this matter to understand the scope and status of each case.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_legal_case
  query: legal_matter=[matter_sys_id]
  fields: sys_id,number,short_description,state,priority,case_type,assigned_to,opened_at,closed_at,resolution_code,resolution_notes
  limit: 50
  order_by: opened_at
```

**Using REST API:**
```bash
GET /api/now/table/sn_legal_case?sysparm_query=legal_matter=[matter_sys_id]^ORDERBYopened_at&sysparm_fields=sys_id,number,short_description,state,priority,case_type,assigned_to,opened_at,closed_at,resolution_code,resolution_notes&sysparm_limit=50&sysparm_display_value=true
```

### Step 3: Build the Case Timeline

Collect legal tasks and activity entries to construct a chronological timeline.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_legal_task
  query: legal_matter=[matter_sys_id]^ORlegal_case.legal_matter=[matter_sys_id]
  fields: sys_id,number,short_description,state,assigned_to,opened_at,closed_at,due_date,task_type,priority,work_notes
  limit: 100
  order_by: opened_at
```

**Using REST API:**
```bash
GET /api/now/table/sn_legal_task?sysparm_query=legal_matter=[matter_sys_id]^ORlegal_case.legal_matter=[matter_sys_id]^ORDERBYopened_at&sysparm_fields=sys_id,number,short_description,state,assigned_to,opened_at,closed_at,due_date,task_type,priority,work_notes&sysparm_limit=100&sysparm_display_value=true
```

Construct the timeline by sorting all events chronologically:

| Date | Event Type | Description | Actor |
|------|-----------|-------------|-------|
| 2025-01-15 | Matter Opened | New litigation matter created for patent dispute | Legal Ops |
| 2025-01-20 | Case Created | Initial assessment case LC0004521 opened | Senior Counsel |
| 2025-02-01 | Task Completed | Document preservation notice sent | Paralegal |
| 2025-02-15 | Hold Initiated | Legal hold LH0001234 placed on relevant custodians | Legal Ops |
| 2025-03-01 | Task Created | Discovery response due in 30 days | Outside Counsel |

### Step 4: Identify Key Documents and Attachments

Query attachments linked to the matter and its associated cases.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sys_attachment
  query: table_name=sn_legal_matter^table_sys_id=[matter_sys_id]^ORtable_name=sn_legal_case^table_sys_idIN[case_sys_ids_comma_separated]
  fields: sys_id,file_name,content_type,size_bytes,sys_created_on,sys_created_by,table_name
  limit: 50
  order_by: sys_created_on
```

**Using REST API:**
```bash
GET /api/now/table/sys_attachment?sysparm_query=table_name=sn_legal_matter^table_sys_id=[matter_sys_id]^ORtable_name=sn_legal_case^table_sys_idIN[case_sys_ids]^ORDERBYsys_created_on&sysparm_fields=sys_id,file_name,content_type,size_bytes,sys_created_on,sys_created_by,table_name&sysparm_limit=50
```

Categorize documents by type:

- **Pleadings:** Complaints, answers, motions, briefs
- **Contracts:** Agreements, amendments, SOWs under review
- **Correspondence:** Letters, emails, demand notices
- **Discovery:** Interrogatories, document requests, depositions
- **Internal:** Memos, analysis, privilege logs

### Step 5: Catalog Parties Involved

Identify all internal and external parties connected to the matter.

**Internal stakeholders** (from assignment fields and case records):
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_legal_case
  query: legal_matter=[matter_sys_id]
  fields: assigned_to,assignment_group,opened_by,watch_list
  limit: 50
```

**Legal holds** (affected custodians):
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_legal_hold
  query: legal_matter=[matter_sys_id]
  fields: sys_id,number,short_description,state,custodian,hold_type,initiated_date,released_date,hold_notice_sent
  limit: 25
```

**Using REST API:**
```bash
GET /api/now/table/sn_legal_hold?sysparm_query=legal_matter=[matter_sys_id]&sysparm_fields=sys_id,number,short_description,state,custodian,hold_type,initiated_date,released_date,hold_notice_sent&sysparm_limit=25&sysparm_display_value=true
```

### Step 6: Assess Financial Exposure

Compile financial data from the matter and related records:

- **Potential liability:** Value from `sn_legal_matter.financial_exposure`
- **Settlement range:** Low and high estimates from matter record
- **Legal spend:** Aggregate outside counsel fees from legal tasks
- **Reserves:** Amounts set aside for potential outcomes

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_legal_task
  query: legal_matter=[matter_sys_id]^task_type=outside_counsel_invoice
  fields: sys_id,short_description,actual_cost,estimated_cost,vendor,invoice_date
  limit: 100
```

**Using REST API:**
```bash
GET /api/now/table/sn_legal_task?sysparm_query=legal_matter=[matter_sys_id]^task_type=outside_counsel_invoice&sysparm_fields=sys_id,short_description,actual_cost,estimated_cost,vendor,invoice_date&sysparm_limit=100
```

### Step 7: Generate the Executive Summary

Compile all gathered information into a structured summary report.

**Using MCP:**
```
Tool: SN-Add-Work-Notes
Parameters:
  table_name: sn_legal_matter
  sys_id: [matter_sys_id]
  work_notes: |
    === LEGAL MATTER EXECUTIVE SUMMARY ===
    Report Date: [current_date]
    Prepared By: AI Legal Assistant

    MATTER: [matter_number] - [short_description]
    Status: [state] | Priority: [priority] | Risk Level: [risk_level]
    Practice Area: [practice_area] | Matter Type: [matter_type]
    Lead Counsel: [assigned_to]
    Outside Counsel: [outside_counsel]
    Business Unit: [business_unit]

    TIMELINE SUMMARY:
    - Opened: [opened_at]
    - Key Milestones: [milestone_count] completed, [pending_count] pending
    - Next Deadline: [next_due_date] - [next_task_description]

    FINANCIAL EXPOSURE:
    - Potential Liability: $[financial_exposure]
    - Settlement Range: $[low_estimate] - $[high_estimate]
    - Legal Spend to Date: $[total_spend]
    - Outstanding Invoices: $[pending_invoices]

    PARTIES:
    - Internal Stakeholders: [stakeholder_count]
    - Legal Hold Custodians: [custodian_count]
    - Active Holds: [active_hold_count]

    DOCUMENTS: [doc_count] attachments across [case_count] cases

    RECOMMENDED ACTIONS:
    1. [action_1]
    2. [action_2]
    3. [action_3]

    RISK ASSESSMENT:
    [risk_narrative based on financial exposure, timeline pressure, and complexity]
```

### Step 8: Update Matter with Summary Metadata

Record that a summary has been generated and tag the matter for leadership review.

**Using MCP:**
```
Tool: SN-Update-Record
Parameters:
  table_name: sn_legal_matter
  sys_id: [matter_sys_id]
  data:
    last_reviewed: [current_date]
    review_notes: "Executive summary generated. Matter reviewed for leadership briefing."
```

**Using REST API:**
```bash
PATCH /api/now/table/sn_legal_matter/[matter_sys_id]
Content-Type: application/json

{
  "last_reviewed": "[current_date]",
  "review_notes": "Executive summary generated. Matter reviewed for leadership briefing."
}
```

## Tool Usage

### MCP Tools Reference

| Tool | When to Use |
|------|-------------|
| `SN-NL-Search` | Find matters by natural language description |
| `SN-Query-Table` | Structured queries for cases, tasks, holds, attachments |
| `SN-Read-Record` | Retrieve a single matter record by sys_id |
| `SN-Update-Record` | Update matter review date and notes |
| `SN-Add-Work-Notes` | Post the executive summary to the matter record |

### REST API Reference

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/now/table/sn_legal_matter` | GET | Query legal matters |
| `/api/now/table/sn_legal_matter/{sys_id}` | GET/PATCH | Read or update a matter |
| `/api/now/table/sn_legal_case` | GET | Retrieve associated cases |
| `/api/now/table/sn_legal_task` | GET | Retrieve tasks and timeline events |
| `/api/now/table/sn_legal_hold` | GET | Retrieve legal holds and custodians |
| `/api/now/table/sys_attachment` | GET | Retrieve document attachments |

## Best Practices

- **Privilege protection:** Never include attorney-client privileged analysis in fields visible to non-legal users; use work notes or internal-only fields
- **Consistent format:** Use the same summary template across all matters to enable comparison and portfolio-level reporting
- **Financial accuracy:** Always verify financial exposure figures with the finance team before including in board-level reports
- **Timeliness:** Generate summaries at least 48 hours before scheduled leadership briefings to allow counsel review
- **Completeness check:** Verify that all active legal holds are accounted for; missing holds create significant litigation risk
- **Version control:** Include the report date in every summary so readers know the currency of information
- **Confidentiality markings:** Tag all summaries as Attorney-Client Privileged and Work Product where applicable

## Troubleshooting

### "Legal matter record not found"

**Cause:** The matter sys_id is incorrect or the matter has been archived
**Solution:** Search by matter number using `sn_legal_matter` with `number=[MATTER_NUMBER]`. Archived matters may require `active=false` in the query.

### "No cases associated with this matter"

**Cause:** Cases were created without linking to the parent matter, or the matter is new
**Solution:** Search `sn_legal_case` by short description keywords or date range to find orphaned cases. Update their `legal_matter` reference field.

### "Financial exposure fields are empty"

**Cause:** Financial data has not been entered or is maintained in a separate finance system
**Solution:** Check if your organization uses custom fields for financial tracking. Query `sn_legal_task` for outside counsel invoices to estimate spend.

### "Attachment query returns no results"

**Cause:** Documents may be stored in a linked document management system rather than as ServiceNow attachments
**Solution:** Check for URL reference fields on the matter or case records pointing to external document repositories (SharePoint, iManage, NetDocuments).

## Examples

### Example 1: Litigation Matter Summary

**Input:** Legal Matter LM0002345 - "Patent infringement claim - Widget Technology"

**Summary generated:**
- Status: Active | Priority: P2 - High | Risk: High
- 3 active cases, 12 completed tasks, 4 pending tasks
- Financial exposure: $2.5M potential liability
- Legal spend to date: $180,000 (outside counsel)
- 8 custodians under legal hold
- Next deadline: Expert report due in 21 days
- Recommended: Engage additional expert witness for damages analysis

### Example 2: Multi-Case Regulatory Matter

**Input:** Legal Matter LM0003456 - "GDPR compliance investigation - EU Data Protection Authority"

**Summary generated:**
- Status: Under Investigation | Priority: P1 - Critical
- 5 cases spanning 3 jurisdictions (DE, FR, UK)
- Financial exposure: EUR 4.2M (potential fine up to 4% of annual turnover)
- 23 documents collected, 15 custodians under hold
- Outside counsel engaged in each jurisdiction
- Recommended: Prepare voluntary remediation plan to mitigate penalty

### Example 3: Contract Dispute Matter

**Input:** Legal Matter LM0001234 - "Vendor breach of SLA - Cloud Services Agreement"

**Analysis steps:**
```
Tool: SN-Read-Record
Parameters:
  table_name: sn_legal_matter
  sys_id: abc789def...
  fields: number,short_description,state,financial_exposure,settlement_amount,assigned_to,matter_type
```

**Summary generated:**
- Status: Negotiation | Priority: P3 - Medium
- 1 case, contract review and demand letter drafted
- Financial exposure: $350,000 (SLA credits owed)
- Settlement range: $200,000 - $300,000
- No legal hold required (commercial dispute)
- Recommended: Proceed with mediation; prepare fallback litigation strategy

## Related Skills

- `legal/legal-request-triage` - Triage and route incoming legal requests
- `legal/contract-analysis` - Analyze contracts for key terms and risks
- `legal/contract-obligation-extraction` - Extract obligations from contracts
- `security/incident-response` - Security incidents with legal implications
- `grc/issue-action-plan` - Compliance and regulatory action plans
