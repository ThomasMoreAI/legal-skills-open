---
name: tprm-issue-summarization
title: TPRM Issue Summarization
description: Summarize Third-Party Risk Management issues including vendor risk exposure, assessment gaps, remediation status, and compliance impact across the TPRM lifecycle
author: Happy-Technologies-LLC
author_url: https://github.com/Happy-Technologies-LLC/happy-platform-skills/tree/main/skills/grc/tprm-issue-summarization
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
tags: [grc, tprm, vendor-risk, third-party, assessment, remediation, compliance, risk-exposure]
---

# TPRM Issue Summarization

## Overview

This skill generates comprehensive summaries of Third-Party Risk Management (TPRM) issues in ServiceNow. It covers:

- Aggregating TPRM issues by vendor, risk tier, and assessment cycle
- Evaluating vendor risk exposure across security, operational, financial, and compliance dimensions
- Identifying assessment gaps where vendors lack current or complete assessments
- Tracking remediation status for open findings and overdue corrective actions
- Measuring compliance impact by mapping vendor issues to regulatory requirements
- Producing executive-ready dashboards for vendor risk committees

**When to use:**
- Preparing for vendor risk committee meetings or board reporting
- During annual or periodic third-party assessment reviews
- When onboarding new vendors and evaluating risk posture
- After a vendor security incident requiring rapid exposure analysis
- For regulatory examinations requiring third-party risk documentation

## Prerequisites

- **Roles:** `sn_tprm.viewer`, `sn_tprm.manager`, `sn_grc.manager`, or `admin`
- **Plugins:** `com.sn_tprm` (Third-Party Risk Management), `com.sn_grc`
- **Access:** Read access to sn_tprm_assessment, sn_tprm_issue, sn_tprm_vendor_assessment, sn_grc_profile, core_company tables
- **Knowledge:** Understanding of vendor risk tiering methodology and organizational third-party risk appetite

## Key TPRM Tables

| Table | Purpose | Key Fields |
|-------|---------|------------|
| `sn_tprm_assessment` | TPRM assessment records | number, short_description, state, assessment_type, vendor, risk_tier, due_date, score |
| `sn_tprm_issue` | Issues found during assessments | number, short_description, state, priority, vendor, assessment, remediation_plan, due_date |
| `sn_tprm_vendor_assessment` | Vendor-level assessment rollups | vendor, assessment_status, overall_risk, last_assessment_date, next_assessment_date |
| `core_company` | Vendor/company master records | name, sys_id, vendor_type, stock_symbol, city, state, country |
| `sn_grc_profile` | GRC profile linked to vendors | number, short_description, profile_type, applies_to |
| `sn_grc_risk` | Risk records associated with vendor profiles | number, risk_score, state, treatment, residual_risk, inherent_risk |

## Procedure

### Step 1: Retrieve Open TPRM Issues

Query all active TPRM issues to establish the current issue landscape.

**Using MCP (Claude Code/Desktop):**
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_tprm_issue
  query: active=true^ORDERBYDESCpriority
  fields: sys_id,number,short_description,description,state,priority,vendor,assessment,remediation_plan,due_date,assigned_to,category,risk_rating,sys_created_on
  limit: 200
```

**Using REST API:**
```bash
GET /api/now/table/sn_tprm_issue?sysparm_query=active=true^ORDERBYDESCpriority&sysparm_fields=sys_id,number,short_description,description,state,priority,vendor,assessment,remediation_plan,due_date,assigned_to,category,risk_rating&sysparm_limit=200&sysparm_display_value=true
```

### Step 2: Gather Vendor Assessment Context

For each vendor with issues, retrieve their assessment history and current risk posture.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sn_tprm_vendor_assessment
  query: vendor=[vendor_sys_id]
  fields: sys_id,vendor,assessment_status,overall_risk,last_assessment_date,next_assessment_date,risk_tier,assessment_score
  limit: 10
```

**Using REST API:**
```bash
GET /api/now/table/sn_tprm_vendor_assessment?sysparm_query=vendor=[vendor_sys_id]&sysparm_fields=sys_id,vendor,assessment_status,overall_risk,last_assessment_date,next_assessment_date,risk_tier,assessment_score&sysparm_limit=10&sysparm_display_value=true
```

### Step 3: Identify Assessment Gaps

Find vendors with overdue or missing assessments to highlight blind spots.

**Using MCP:**
```
Tool: SN-Execute-Background-Script
Parameters:
  script: |
    var gaps = [];
    var va = new GlideRecord('sn_tprm_vendor_assessment');
    va.addQuery('next_assessment_date', '<', new GlideDateTime().toString());
    va.addOrCondition('assessment_status', 'incomplete');
    va.addOrCondition('assessment_status', 'not_started');
    va.query();

    while (va.next()) {
      var vendor = new GlideRecord('core_company');
      vendor.get(va.vendor);
      gaps.push({
        vendor_name: vendor.name.toString(),
        vendor_sys_id: va.vendor.toString(),
        assessment_status: va.assessment_status.getDisplayValue(),
        overall_risk: va.overall_risk.getDisplayValue(),
        risk_tier: va.risk_tier.getDisplayValue(),
        last_assessment: va.last_assessment_date.toString(),
        next_assessment: va.next_assessment_date.toString(),
        days_overdue: gs.dateDiff(va.next_assessment_date.toString(), new GlideDateTime().toString(), true)
      });
    }

    gs.info('ASSESSMENT GAPS (' + gaps.length + ' vendors):\n' + JSON.stringify(gaps, null, 2));
  description: "TPRM: Identify vendors with overdue or incomplete assessments"
```

### Step 4: Generate Vendor Risk Exposure Summary

Produce aggregate metrics across all vendors and risk tiers.

**Using MCP:**
```
Tool: SN-Execute-Background-Script
Parameters:
  script: |
    var summary = {
      generated_date: new GlideDateTime().toString(),
      issue_overview: { total_open: 0, critical: 0, high: 0, medium: 0, low: 0, overdue: 0 },
      by_vendor: {},
      by_category: {},
      remediation_status: { with_plan: 0, without_plan: 0, plan_overdue: 0 },
      assessment_coverage: { total_vendors: 0, assessed_current: 0, assessed_overdue: 0, never_assessed: 0 },
      risk_tier_distribution: {}
    };

    var now = new GlideDateTime();

    // Issue metrics
    var gr = new GlideRecord('sn_tprm_issue');
    gr.addQuery('active', true);
    gr.query();
    while (gr.next()) {
      summary.issue_overview.total_open++;
      var pri = gr.priority.toString();
      if (pri == '1') summary.issue_overview.critical++;
      else if (pri == '2') summary.issue_overview.high++;
      else if (pri == '3') summary.issue_overview.medium++;
      else summary.issue_overview.low++;

      if (gr.due_date.toString() && new GlideDateTime(gr.due_date.toString()).compareTo(now) < 0) {
        summary.issue_overview.overdue++;
      }

      var vendorName = gr.vendor.getDisplayValue() || 'Unknown';
      summary.by_vendor[vendorName] = (summary.by_vendor[vendorName] || 0) + 1;

      var cat = gr.category.getDisplayValue() || 'Uncategorized';
      summary.by_category[cat] = (summary.by_category[cat] || 0) + 1;

      if (gr.remediation_plan.toString()) {
        summary.remediation_status.with_plan++;
        if (gr.due_date.toString() && new GlideDateTime(gr.due_date.toString()).compareTo(now) < 0) {
          summary.remediation_status.plan_overdue++;
        }
      } else {
        summary.remediation_status.without_plan++;
      }
    }

    // Assessment coverage
    var va = new GlideRecord('sn_tprm_vendor_assessment');
    va.query();
    while (va.next()) {
      summary.assessment_coverage.total_vendors++;
      var tier = va.risk_tier.getDisplayValue() || 'Untiered';
      summary.risk_tier_distribution[tier] = (summary.risk_tier_distribution[tier] || 0) + 1;

      if (!va.last_assessment_date.toString()) {
        summary.assessment_coverage.never_assessed++;
      } else if (va.next_assessment_date.toString() && new GlideDateTime(va.next_assessment_date.toString()).compareTo(now) < 0) {
        summary.assessment_coverage.assessed_overdue++;
      } else {
        summary.assessment_coverage.assessed_current++;
      }
    }

    gs.info('TPRM EXECUTIVE SUMMARY:\n' + JSON.stringify(summary, null, 2));
  description: "TPRM: Generate executive risk exposure summary"
```

### Step 5: Analyze Remediation Effectiveness

Evaluate how effectively issues are being remediated across the vendor portfolio.

**Using MCP:**
```
Tool: SN-Execute-Background-Script
Parameters:
  script: |
    var remediation = {
      avg_days_to_close: 0,
      closed_on_time: 0,
      closed_late: 0,
      still_open_on_time: 0,
      still_open_overdue: 0,
      top_overdue_vendors: []
    };

    var now = new GlideDateTime();
    var closedDays = [];

    // Closed issues - resolution time
    var closed = new GlideRecord('sn_tprm_issue');
    closed.addQuery('active', false);
    closed.addQuery('closed_at', '>=', gs.daysAgo(180));
    closed.query();
    while (closed.next()) {
      var created = new GlideDateTime(closed.sys_created_on.toString());
      var closedAt = new GlideDateTime(closed.closed_at.toString());
      var days = gs.dateDiff(created.toString(), closedAt.toString(), true);
      closedDays.push(parseInt(days));

      if (closed.due_date.toString() && closedAt.compareTo(new GlideDateTime(closed.due_date.toString())) <= 0) {
        remediation.closed_on_time++;
      } else {
        remediation.closed_late++;
      }
    }

    if (closedDays.length > 0) {
      var total = 0;
      for (var i = 0; i < closedDays.length; i++) total += closedDays[i];
      remediation.avg_days_to_close = Math.round(total / closedDays.length);
    }

    // Open issues - on-time vs overdue
    var vendorOverdue = {};
    var open = new GlideRecord('sn_tprm_issue');
    open.addQuery('active', true);
    open.query();
    while (open.next()) {
      if (open.due_date.toString() && new GlideDateTime(open.due_date.toString()).compareTo(now) < 0) {
        remediation.still_open_overdue++;
        var v = open.vendor.getDisplayValue() || 'Unknown';
        vendorOverdue[v] = (vendorOverdue[v] || 0) + 1;
      } else {
        remediation.still_open_on_time++;
      }
    }

    // Sort vendors by overdue count
    var sorted = Object.keys(vendorOverdue).sort(function(a, b) { return vendorOverdue[b] - vendorOverdue[a]; });
    for (var j = 0; j < Math.min(5, sorted.length); j++) {
      remediation.top_overdue_vendors.push({ vendor: sorted[j], overdue_count: vendorOverdue[sorted[j]] });
    }

    gs.info('REMEDIATION ANALYSIS:\n' + JSON.stringify(remediation, null, 2));
  description: "TPRM: Analyze remediation effectiveness across vendor portfolio"
```

### Step 6: Generate Compliance Impact Narrative

Search for issues with regulatory or compliance implications.

**Using MCP:**
```
Tool: SN-Natural-Language-Search
Parameters:
  table_name: sn_tprm_issue
  query: "third-party vendor issues related to data privacy, GDPR, SOC 2, regulatory compliance, or security controls"
  limit: 30
```

**Post the summary as work notes:**
```
Tool: SN-Add-Work-Notes
Parameters:
  table_name: sn_tprm_vendor_assessment
  sys_id: [vendor_assessment_sys_id]
  work_notes: |
    === TPRM ISSUE SUMMARY ===
    Vendor: [vendor_name]
    Report Date: [current_date]
    Risk Tier: [tier]

    OPEN ISSUES: [count] ([critical] critical, [high] high)
    OVERDUE ISSUES: [overdue_count]

    ASSESSMENT STATUS:
    - Last Completed: [date]
    - Next Due: [date]
    - Coverage Gaps: [gap_details]

    COMPLIANCE IMPACT:
    - Regulatory Findings: [count]
    - Affected Frameworks: [SOC 2, GDPR, HIPAA, etc.]
    - Remediation Timeline: [estimated_completion]

    RECOMMENDED ACTIONS:
    1. [action_1]
    2. [action_2]
    3. [action_3]
```

## Tool Usage

| Operation | MCP Tool | REST Endpoint |
|-----------|----------|---------------|
| Query TPRM Issues | SN-Query-Table | GET /api/now/table/sn_tprm_issue |
| Search Issues by Theme | SN-Natural-Language-Search | N/A |
| Query Assessments | SN-Query-Table | GET /api/now/table/sn_tprm_assessment |
| Query Vendor Assessments | SN-Query-Table | GET /api/now/table/sn_tprm_vendor_assessment |
| Aggregate Analysis | SN-Execute-Background-Script | POST /api/now/table/sys_trigger |
| Schema Discovery | SN-Discover-Table-Schema | GET /api/now/table/sys_dictionary |
| Post Summary Notes | SN-Add-Work-Notes | PATCH /api/now/table/{table}/{sys_id} |

## Best Practices

- **Risk Tiering:** Always segment vendor analysis by risk tier (critical, high, medium, low) to prioritize attention and resources appropriately
- **Assessment Currency:** Flag any Tier 1 or Tier 2 vendor whose assessment is more than 12 months old as an immediate gap
- **Remediation SLAs:** Define clear remediation timelines by issue severity: Critical (30 days), High (60 days), Medium (90 days), Low (180 days)
- **Trend Analysis:** Include quarter-over-quarter trends to show whether the vendor risk posture is improving or degrading
- **Concentration Risk:** Highlight vendors with disproportionate numbers of open issues, which may indicate systemic risk management failures
- **Fourth-Party Awareness:** Note any vendor issues that stem from their subcontractors or fourth-party dependencies
- **Regulatory Mapping:** Map TPRM issues to specific regulatory requirements (OCC, FFIEC, GDPR) for examination readiness

## Troubleshooting

### Empty Vendor Assessment Records

**Symptom:** sn_tprm_vendor_assessment returns no results for known vendors
**Cause:** Vendor assessments may use a different relationship model or the vendor record is in core_company but not linked to TPRM
**Solution:**
```
Tool: SN-Discover-Table-Schema
Parameters:
  table_name: sn_tprm_vendor_assessment
```
Verify the vendor reference field name. Some configurations use `entity` or `company` instead of `vendor`.

### Assessment Score Fields Return Null

**Symptom:** Assessment scores are empty despite completed assessments
**Cause:** Scoring may be calculated at the questionnaire response level, not stored on the assessment record
**Solution:** Query `sn_tprm_assessment` with the assessment sys_id to check for child questionnaire records or `asmt_metric_result` entries that hold the computed scores.

### Issue-to-Vendor Linkage Missing

**Symptom:** Issues show no vendor association in query results
**Cause:** Issues may be linked via the assessment record rather than directly to the vendor
**Solution:** Join through the assessment reference: query the issue's `assessment` field, then read the assessment record to find its `vendor` field.

## Examples

### Example 1: Quarterly Vendor Risk Committee Report

**Scenario:** VP of Risk needs a portfolio-wide TPRM summary for the quarterly committee meeting.

```
Tool: SN-Natural-Language-Search
Parameters:
  table_name: sn_tprm_issue
  query: "all open third-party risk issues with critical or high priority updated in the last quarter"
  limit: 50
```

**Generated Summary:**
- **Total Open Issues:** 83 across 34 vendors (down from 91 last quarter)
- **Critical/High Priority:** 18 issues requiring immediate attention
- **Overdue Remediation:** 12 issues past due date (14% overdue rate)
- **Top Risk Category:** Data Security (28 issues, 34%)
- **Assessment Coverage:** 92% of Tier 1 vendors current; 3 Tier 1 vendors overdue
- **Average Remediation Time:** 47 days (target: 30 days for critical)
- **Recommendation:** Escalate 3 Tier 1 vendors with overdue critical findings; initiate reassessment for 5 vendors approaching annual review

### Example 2: Vendor-Specific Deep Dive After Incident

**Scenario:** A critical vendor reported a data breach; need immediate risk exposure summary.

```
Tool: SN-Query-Table
Parameters:
  table_name: sn_tprm_issue
  query: vendor=[vendor_sys_id]^active=true
  fields: sys_id,number,short_description,state,priority,category,due_date,remediation_plan
  limit: 50
```

**Generated Detail:**
- **Vendor:** DataCorp International (Tier 1 - Critical)
- **Open Issues:** 7 (2 critical, 3 high, 2 medium)
- **Pre-Existing Security Issues:** 3 issues related to access controls and encryption
- **Last Assessment:** 2025-11-15 (Score: 62/100 - Below Acceptable Threshold)
- **Overdue Remediations:** 2 critical findings past 90-day SLA
- **Compliance Impact:** SOC 2 Type II gaps; GDPR Article 28 processor requirements unmet
- **Recommended Actions:** Invoke contractual audit rights; require 30-day remediation plan; evaluate alternative vendors

## Related Skills

- `grc/issue-summarization` - General GRC issue summarization for broader risk context
- `grc/risk-assessment-summarization` - Deep risk analysis behind vendor risk scores
- `grc/regulatory-alert-analysis` - Monitor regulatory changes affecting third-party requirements
- `grc/control-objective-management` - Manage controls mapped to vendor risk areas
- `security/audit-compliance` - Audit trail and compliance reporting for vendor assessments

## References

- [ServiceNow TPRM Documentation](https://docs.servicenow.com/bundle/utah-governance-risk-compliance/page/product/third-party-risk-management/concept/tprm-overview.html)
- [OCC Third-Party Risk Management Guidance](https://www.occ.gov/topics/supervision-and-examination/third-party-relationships/index-third-party-relationships.html)
- [NIST SP 800-161 Supply Chain Risk Management](https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final)
