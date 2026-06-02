---
name: contracts-query-enhancer
title: Contract Query Enhancer
description: Enhance contract search queries with contextual understanding, mapping natural language to contract fields, obligation types, clause categories, and CLM-specific terminology
author: Happy-Technologies-LLC
author_url: https://github.com/Happy-Technologies-LLC/happy-platform-skills/tree/main/skills/legal/contracts-query-enhancer
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [legal, contract, search, query, nlp, clm, natural-language, filtering, discovery]
---

# Contract Query Enhancer

## Overview

This skill transforms natural language contract search queries into precise ServiceNow queries, enabling users to find contracts without knowing table structures or encoded query syntax. It covers:

- Mapping conversational search terms to contract table fields and encoded query operators
- Resolving vendor names, contract types, and status values to their ServiceNow equivalents
- Translating date expressions ("expiring next quarter", "signed last year") to encoded date queries
- Understanding obligation-specific terminology and mapping to CLM obligation types
- Combining multiple search criteria into optimized compound queries
- Suggesting follow-up queries to refine broad result sets

**When to use:**
- When users search for contracts using business language rather than field names
- During contract discovery for audits, renewals, or due diligence projects
- When building contract reports that require specific filtering criteria
- When non-technical stakeholders need to find contracts without ServiceNow expertise
- For automated contract monitoring that triggers on natural language conditions

## Prerequisites

- **Roles:** `contract_reader`, `contract_manager`, `sn_clm.user`, or `admin`
- **Plugins:** `com.snc.contract_management` (Contract Management) or `com.sn_clm` (Contract Lifecycle Management)
- **Access:** Read access to ast_contract, clm_obligation, core_company, sys_choice tables
- **Knowledge:** Basic understanding of contract terminology and your organization's contract taxonomy

## Query Mapping Reference

### Natural Language to Field Mapping

| Natural Language Term | ServiceNow Field | Table | Encoded Query Example |
|----------------------|------------------|-------|----------------------|
| "vendor", "supplier", "provider" | vendor | ast_contract | vendor.nameLIKE[term] |
| "expires", "expiring", "end date" | ends | ast_contract | ends<javascript:gs.daysAgoEnd(-90) |
| "value", "cost", "amount", "price" | total_cost | ast_contract | total_cost>100000 |
| "auto-renew", "automatic renewal" | auto_renew | ast_contract | auto_renew=true |
| "notice period", "opt-out window" | notice_period | ast_contract | notice_period<=60 |
| "governing law", "jurisdiction" | governing_law | ast_contract | governing_lawLIKE[state] |
| "obligation", "commitment" | short_description | clm_obligation | short_descriptionLIKE[term] |
| "type", "category" | contract_type | ast_contract | contract_type=[value] |
| "active", "current", "in force" | state | ast_contract | state=active |
| "department", "business unit" | department | ast_contract | department=[sys_id] |

### Date Expression Translation

| Natural Language | Encoded Query |
|-----------------|---------------|
| "expiring this month" | `endsBETWEENjavascript:gs.beginningOfThisMonth()@javascript:gs.endOfThisMonth()` |
| "expiring next quarter" | `endsBETWEENjavascript:gs.beginningOfNextQuarter()@javascript:gs.endOfNextQuarter()` |
| "expiring in 90 days" | `ends<=javascript:gs.daysAgoEnd(-90)^ends>=javascript:gs.daysAgoEnd(0)` |
| "signed last year" | `startsBETWEENjavascript:gs.beginningOfLastYear()@javascript:gs.endOfLastYear()` |
| "renewed in 2025" | `renewal_dateBETWEEN2025-01-01@2025-12-31` |
| "overdue obligations" | `due_date<javascript:gs.now()^state!=complete` |

## Procedure

### Step 1: Parse the Natural Language Query

Analyze the user's search intent and identify the components:
- **Entity type:** Contract, obligation, clause, or vendor
- **Filter criteria:** Date ranges, values, statuses, parties
- **Sort preference:** By date, value, relevance, or risk
- **Scope:** Single contract, vendor portfolio, or full portfolio

### Step 2: Resolve Field Values

Map user terms to ServiceNow choice values and references.

**Resolve contract type values:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sys_choice
  query: name=ast_contract^element=contract_type
  fields: value,label
  limit: 50
```

**Using REST API:**
```bash
GET /api/now/table/sys_choice?sysparm_query=name=ast_contract^element=contract_type&sysparm_fields=value,label&sysparm_limit=50
```

**Resolve vendor by name:**
```
Tool: SN-Query-Table
Parameters:
  table_name: core_company
  query: nameLIKE[search_term]^vendor=true
  fields: sys_id,name,vendor_type
  limit: 10
```

### Step 3: Build the Enhanced Query

Combine resolved values into an optimized encoded query.

**Example: "Show me all SaaS contracts with Acme expiring in the next 6 months worth over $100K"**

**Step-by-step translation:**
1. "SaaS contracts" -> `contract_type=saas` (resolved from sys_choice)
2. "with Acme" -> `vendor=[acme_sys_id]` (resolved from core_company)
3. "expiring in the next 6 months" -> `ends<=javascript:gs.daysAgoEnd(-180)^ends>=javascript:gs.daysAgoEnd(0)`
4. "worth over $100K" -> `total_cost>100000`

**Combined query:**
```
Tool: SN-Query-Table
Parameters:
  table_name: ast_contract
  query: contract_type=saas^vendor=[acme_sys_id]^ends<=javascript:gs.daysAgoEnd(-180)^ends>=javascript:gs.daysAgoEnd(0)^total_cost>100000^active=true
  fields: sys_id,number,short_description,vendor,contract_type,starts,ends,total_cost,auto_renew,notice_period,state
  limit: 50
  order_by: ends
```

### Step 4: Execute and Validate Results

Run the query and verify results match the user's intent.

**Using REST API:**
```bash
GET /api/now/table/ast_contract?sysparm_query=contract_type=saas^vendor=[acme_sys_id]^ends<=javascript:gs.daysAgoEnd(-180)^ends>=javascript:gs.daysAgoEnd(0)^total_cost>100000^active=true&sysparm_fields=sys_id,number,short_description,vendor,contract_type,starts,ends,total_cost,auto_renew,notice_period&sysparm_limit=50&sysparm_display_value=true
```

**Alternatively, use Natural Language Search for fuzzy matching:**
```
Tool: SN-Natural-Language-Search
Parameters:
  table_name: ast_contract
  query: "SaaS contracts with Acme expiring in the next 6 months worth over 100 thousand dollars"
  limit: 25
```

### Step 5: Search Obligations by Context

Translate obligation-related queries to CLM table searches.

**Example: "Find all vendor data protection obligations due this quarter"**

```
Tool: SN-Query-Table
Parameters:
  table_name: clm_obligation
  query: obligation_type=vendor_obligation^short_descriptionLIKEdata protection^due_dateBETWEENjavascript:gs.beginningOfThisQuarter()@javascript:gs.endOfThisQuarter()^active=true
  fields: sys_id,short_description,contract,obligation_type,responsible_party,due_date,state,compliance_status,clause_reference
  limit: 50
```

### Step 6: Generate Query Suggestions

**Offer follow-up queries to refine results:**
```
Tool: SN-Execute-Background-Script
Parameters:
  script: |
    var suggestions = {
      original_query: 'SaaS contracts with Acme expiring next 6 months over $100K',
      results_found: 0,
      refinement_suggestions: [],
      broadening_suggestions: []
    };

    // Count results
    var ga = new GlideAggregate('ast_contract');
    ga.addQuery('contract_type', 'saas');
    ga.addQuery('active', true);
    ga.addQuery('ends', '<=', gs.daysAgoEnd(-180));
    ga.addQuery('ends', '>=', gs.daysAgoEnd(0));
    ga.addQuery('total_cost', '>', 100000);
    ga.addAggregate('COUNT');
    ga.query();
    if (ga.next()) suggestions.results_found = parseInt(ga.getAggregate('COUNT'));

    if (suggestions.results_found > 20) {
      suggestions.refinement_suggestions = [
        'Add department filter: "...in the Engineering department"',
        'Narrow timeline: "...expiring in the next 30 days"',
        'Add renewal filter: "...with auto-renewal enabled"'
      ];
    } else if (suggestions.results_found == 0) {
      suggestions.broadening_suggestions = [
        'Remove value filter: "SaaS contracts with Acme expiring in 6 months"',
        'Expand vendor: "SaaS contracts expiring in 6 months over $100K"',
        'Expand type: "All contracts with Acme expiring in 6 months"'
      ];
    }

    gs.info('QUERY SUGGESTIONS:\n' + JSON.stringify(suggestions, null, 2));
  description: "CLM: Generate query refinement suggestions based on result count"
```

### Step 7: Build Saved Search Queries

**Save frequently used query patterns for reuse:**
```
Tool: SN-Create-Record
Parameters:
  table_name: sys_filter
  fields:
    title: "Contracts Expiring Next 90 Days - Auto Renew"
    table: ast_contract
    filter: active=true^auto_renew=true^ends<=javascript:gs.daysAgoEnd(-90)^ends>=javascript:gs.daysAgoEnd(0)
```

## Tool Usage

| Operation | MCP Tool | REST Endpoint |
|-----------|----------|---------------|
| Query Contracts | SN-Query-Table | GET /api/now/table/ast_contract |
| Fuzzy Search | SN-Natural-Language-Search | N/A |
| Resolve Choice Values | SN-Query-Table | GET /api/now/table/sys_choice |
| Resolve Vendors | SN-Query-Table | GET /api/now/table/core_company |
| Query Obligations | SN-Query-Table | GET /api/now/table/clm_obligation |
| Aggregate Counts | SN-Execute-Background-Script | POST /api/now/table/sys_trigger |
| Discover Fields | SN-Discover-Table-Schema | GET /api/now/table/sys_dictionary |

## Best Practices

- **Always Resolve References:** Never pass raw text into reference fields; resolve vendor names and department names to sys_ids first
- **Date Safety:** Use JavaScript date functions rather than hardcoded dates so queries remain valid over time
- **Progressive Refinement:** Start with broader queries and offer refinements rather than returning zero results
- **Field Validation:** Check sys_dictionary before querying non-standard fields to avoid "invalid field" errors
- **Display Values:** Always request `sysparm_display_value=true` for user-facing results so reference fields show names
- **Compound Queries:** For OR conditions, use `^OR` or `^NQ` (new query) operators; test complex boolean logic carefully
- **Performance:** Add `sysparm_limit` to all queries; use indexed fields (number, sys_id, state) as primary filters
- **Encoding:** URL-encode special characters in REST query parameters, especially `^`, `=`, and date expressions

## Troubleshooting

### Query Returns No Results When Contracts Exist

**Symptom:** Natural language query translates correctly but returns zero results
**Cause:** Choice value mismatch (e.g., "saas" vs "SaaS" vs "software_as_a_service")
**Solution:** Always resolve choice values from `sys_choice` first:
```
Tool: SN-Query-Table
Parameters:
  table_name: sys_choice
  query: name=ast_contract^element=contract_type^labelLIKESaaS
  fields: value,label
  limit: 5
```

### Date Queries Return Unexpected Results

**Symptom:** "Expiring next quarter" returns contracts from the wrong time period
**Cause:** JavaScript date functions use server timezone; `gs.daysAgoEnd()` counts from today
**Solution:** Verify server timezone with `gs.getProperty('glide.sys.date.format')`. Use `BETWEEN` with explicit quarter boundaries for precision.

### Vendor Name Does Not Resolve

**Symptom:** Vendor lookup returns no results for a known vendor
**Cause:** The vendor name in `core_company` may differ from common usage (e.g., "International Business Machines" vs "IBM")
**Solution:** Use `nameLIKE` with partial match, or search across `name`, `stock_symbol`, and `u_dba_name` fields.

## Examples

### Example 1: Renewal Dashboard Query

**User Query:** "Show me all contracts that auto-renew and need notice within 60 days"

**Enhanced Query:**
```
Tool: SN-Query-Table
Parameters:
  table_name: ast_contract
  query: active=true^auto_renew=true^endsRELATIVELE@dayAgo@-60^endsRELATIVEGE@dayAgo@0
  fields: number,short_description,vendor,ends,notice_period,total_cost,contract_administrator
  limit: 50
  order_by: ends
```

### Example 2: Compliance Audit Query

**User Query:** "Find contracts with European vendors that don't mention GDPR"

**Enhanced Query (two-step):**
```
Tool: SN-Query-Table
Parameters:
  table_name: ast_contract
  query: active=true^vendor.country=Germany^ORvendor.country=France^ORvendor.country=Netherlands^terms_and_conditionsNOT LIKEGDPR
  fields: number,short_description,vendor,governing_law,total_cost,ends
  limit: 50
```

### Example 3: Financial Exposure Query

**User Query:** "What is our total contract spend with technology vendors expiring this year?"

**Enhanced Query:**
```
Tool: SN-Execute-Background-Script
Parameters:
  script: |
    var ga = new GlideAggregate('ast_contract');
    ga.addQuery('active', true);
    ga.addQuery('vendor.vendor_type', 'technology');
    ga.addQuery('ends', 'BETWEEN', gs.beginningOfThisYear() + '@' + gs.endOfThisYear());
    ga.addAggregate('SUM', 'total_cost');
    ga.addAggregate('COUNT');
    ga.query();
    if (ga.next()) {
      gs.info('Total contracts: ' + ga.getAggregate('COUNT'));
      gs.info('Total spend: $' + ga.getAggregate('SUM', 'total_cost'));
    }
  description: "CLM: Calculate total spend for technology vendors with contracts expiring this year"
```

## Related Skills

- `legal/contract-metadata-extraction` - Extract metadata from contract records
- `legal/contract-analysis` - Full contract risk analysis
- `legal/contract-obligation-extraction` - Obligation discovery and tracking
- `legal/legal-request-triage` - Triage contract review requests
- `itsm/natural-language-queries` - General natural language query techniques
