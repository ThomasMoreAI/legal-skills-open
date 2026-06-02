---
name: contract-metadata-extraction
title: Contract Metadata Extraction
description: Extract metadata from contracts including parties, effective dates, value, auto-renewal terms, governing law, key contacts, and obligation summaries for portfolio management
author: Happy-Technologies-LLC
author_url: https://github.com/Happy-Technologies-LLC/happy-platform-skills/tree/main/skills/legal/contract-metadata-extraction
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
tags: [legal, contract, metadata, extraction, clm, renewal, parties, obligations, governing-law]
---

# Contract Metadata Extraction

## Overview

This skill extracts structured metadata from contracts in ServiceNow Contract Lifecycle Management (CLM). It covers:

- Identifying contracting parties, signatories, and key contacts from contract records
- Extracting effective dates, expiration dates, and renewal windows
- Capturing financial terms including total value, payment schedules, and fee escalation
- Parsing auto-renewal clauses with notice period requirements and opt-out windows
- Identifying governing law jurisdiction, dispute resolution, and venue provisions
- Cataloging obligations with responsible parties, deadlines, and compliance requirements
- Populating metadata fields on contract records for portfolio-wide reporting

**When to use:**
- After uploading new contracts that need metadata population
- During contract portfolio audits requiring consistent metadata across all records
- When preparing renewal dashboards and need accurate date/term extraction
- Before M&A due diligence requiring rapid contract inventory
- When migrating contracts into ServiceNow from legacy systems

## Prerequisites

- **Roles:** `contract_manager`, `sn_clm.admin`, `sn_legal_case_manager`, or `admin`
- **Plugins:** `com.sn_clm` (Contract Lifecycle Management), `com.snc.contract_management` (Contract Management)
- **Access:** Read/write access to ast_contract, clm_contract_doc, clm_obligation, sys_attachment tables
- **Knowledge:** Understanding of contract structure, legal terminology, and your organization's contract metadata taxonomy

## Key CLM Tables

| Table | Purpose | Key Fields |
|-------|---------|------------|
| `ast_contract` | Master contract records | number, short_description, vendor, contract_type, starts, ends, renewal_date, payment_amount, total_cost, auto_renew, notice_period, governing_law |
| `clm_contract_doc` | Contract document versions | contract, document_version, status, doc_type, effective_date, content |
| `clm_obligation` | Contractual obligations | contract, short_description, obligation_type, responsible_party, due_date, state, compliance_status, clause_reference |
| `clm_clause` | Contract clause library | name, clause_type, content, category, standard, risk_level |
| `sys_attachment` | Document attachments | table_name, table_sys_id, file_name, content_type, size_bytes |
| `core_company` | Party/vendor records | name, vendor_type, primary_contact, city, state, country |

## Procedure

### Step 1: Retrieve the Contract Record

Get the base contract record with existing metadata.

**Using MCP (Claude Code/Desktop):**
```
Tool: SN-Read-Record
Parameters:
  table_name: ast_contract
  sys_id: [contract_sys_id]
  fields: sys_id,number,short_description,description,contract_type,vendor,starts,ends,renewal_date,payment_amount,total_cost,state,terms_and_conditions,auto_renew,notice_period,assigned_to,department,contract_administrator,parent_contract,governing_law,currency,payment_terms,subcontracting_allowed
```

**Using REST API:**
```bash
GET /api/now/table/ast_contract/[contract_sys_id]?sysparm_fields=sys_id,number,short_description,description,contract_type,vendor,starts,ends,renewal_date,payment_amount,total_cost,state,terms_and_conditions,auto_renew,notice_period,assigned_to,department,contract_administrator,parent_contract,governing_law,currency,payment_terms&sysparm_display_value=true
```

### Step 2: Retrieve Contract Documents

Fetch associated contract documents and attachments for content analysis.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: clm_contract_doc
  query: contract=[contract_sys_id]^ORDERBYDESCdocument_version
  fields: sys_id,document_version,status,doc_type,effective_date,content,file_name
  limit: 10
```

**Using REST API:**
```bash
GET /api/now/table/clm_contract_doc?sysparm_query=contract=[contract_sys_id]^ORDERBYDESCdocument_version&sysparm_fields=sys_id,document_version,status,doc_type,effective_date,content,file_name&sysparm_limit=10
```

**Retrieve attachments:**
```
Tool: SN-Query-Table
Parameters:
  table_name: sys_attachment
  query: table_name=ast_contract^table_sys_id=[contract_sys_id]
  fields: sys_id,file_name,content_type,size_bytes,sys_created_on
  limit: 20
```

### Step 3: Extract Party Information

Identify all contracting parties, signatories, and key contacts.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: core_company
  query: sys_id=[vendor_sys_id]
  fields: sys_id,name,vendor_type,primary_contact,street,city,state,country,phone,website,stock_symbol,parent
  limit: 1
```

**Using REST API:**
```bash
GET /api/now/table/core_company/[vendor_sys_id]?sysparm_fields=sys_id,name,vendor_type,primary_contact,street,city,state,country,phone,website&sysparm_display_value=true
```

### Step 4: Extract and Catalog Obligations

Query existing obligations or create them from contract analysis.

**Using MCP:**
```
Tool: SN-Query-Table
Parameters:
  table_name: clm_obligation
  query: contract=[contract_sys_id]^active=true
  fields: sys_id,short_description,obligation_type,responsible_party,due_date,state,compliance_status,clause_reference,frequency,penalty
  limit: 50
```

**Using REST API:**
```bash
GET /api/now/table/clm_obligation?sysparm_query=contract=[contract_sys_id]^active=true&sysparm_fields=sys_id,short_description,obligation_type,responsible_party,due_date,state,compliance_status,clause_reference,frequency&sysparm_limit=50&sysparm_display_value=true
```

### Step 5: Build Metadata Extraction Report

**Generate a comprehensive metadata extraction:**
```
Tool: SN-Execute-Background-Script
Parameters:
  script: |
    var contractNumber = 'CON0045678'; // Replace with target contract
    var gr = new GlideRecord('ast_contract');
    gr.addQuery('number', contractNumber);
    gr.query();

    if (gr.next()) {
      var metadata = {
        extraction_date: new GlideDateTime().toString(),
        contract_id: gr.number.toString(),
        parties: {
          buyer: {
            name: gs.getProperty('glide.servlet.uri', 'Your Organization'),
            contact: gr.contract_administrator.getDisplayValue()
          },
          vendor: {
            name: gr.vendor.getDisplayValue(),
            contact: ''
          }
        },
        dates: {
          effective_date: gr.starts.toString(),
          expiration_date: gr.ends.toString(),
          renewal_date: gr.renewal_date.toString(),
          execution_date: gr.sys_created_on.toString()
        },
        financials: {
          total_value: gr.total_cost.toString(),
          payment_amount: gr.payment_amount.toString(),
          currency: gr.currency.getDisplayValue() || 'USD',
          payment_terms: gr.payment_terms.getDisplayValue() || 'Not specified'
        },
        renewal: {
          auto_renew: gr.auto_renew.toString() == 'true',
          notice_period_days: gr.notice_period.toString() || 'Not specified',
          notice_deadline: ''
        },
        governing_law: gr.governing_law.getDisplayValue() || 'Not specified',
        contract_type: gr.contract_type.getDisplayValue(),
        state: gr.state.getDisplayValue(),
        obligations: [],
        metadata_completeness: 0
      };

      // Calculate notice deadline
      if (metadata.renewal.auto_renew && gr.ends.toString() && gr.notice_period.toString()) {
        var endDate = new GlideDateTime(gr.ends.toString());
        var noticeDays = parseInt(gr.notice_period.toString()) || 0;
        endDate.addDaysUTC(-noticeDays);
        metadata.renewal.notice_deadline = endDate.toString();
      }

      // Get vendor contact
      var vendor = new GlideRecord('core_company');
      if (vendor.get(gr.vendor.toString())) {
        metadata.parties.vendor.contact = vendor.primary_contact.getDisplayValue();
      }

      // Get obligations
      var obl = new GlideRecord('clm_obligation');
      obl.addQuery('contract', gr.sys_id.toString());
      obl.addQuery('active', true);
      obl.query();
      while (obl.next()) {
        metadata.obligations.push({
          description: obl.short_description.toString(),
          type: obl.obligation_type.getDisplayValue(),
          responsible: obl.responsible_party.getDisplayValue(),
          due_date: obl.due_date.toString(),
          status: obl.compliance_status.getDisplayValue()
        });
      }

      // Metadata completeness score
      var fields = ['total_cost', 'starts', 'ends', 'vendor', 'contract_type', 'governing_law', 'notice_period', 'payment_terms'];
      var filled = 0;
      for (var i = 0; i < fields.length; i++) {
        if (gr.getValue(fields[i])) filled++;
      }
      metadata.metadata_completeness = Math.round((filled / fields.length) * 100);

      gs.info('CONTRACT METADATA EXTRACTION:\n' + JSON.stringify(metadata, null, 2));
    }
  description: "CLM: Extract comprehensive metadata from a contract record"
```

### Step 6: Create Missing Obligations from Analysis

**Create obligation records discovered during extraction:**
```
Tool: SN-Create-Record
Parameters:
  table_name: clm_obligation
  fields:
    contract: [contract_sys_id]
    short_description: "Annual SOC 2 Type II report delivery"
    obligation_type: vendor_obligation
    responsible_party: [vendor_sys_id]
    due_date: 2026-06-30
    frequency: annual
    clause_reference: "Section 9.3 - Audit and Compliance"
    state: active
    compliance_status: pending
```

**Using REST API:**
```bash
POST /api/now/table/clm_obligation
Content-Type: application/json

{
  "contract": "[contract_sys_id]",
  "short_description": "Annual SOC 2 Type II report delivery",
  "obligation_type": "vendor_obligation",
  "responsible_party": "[vendor_sys_id]",
  "due_date": "2026-06-30",
  "frequency": "annual",
  "clause_reference": "Section 9.3",
  "state": "active"
}
```

### Step 7: Update Contract Record with Extracted Metadata

**Populate missing fields on the contract record:**
```
Tool: SN-Update-Record
Parameters:
  table_name: ast_contract
  sys_id: [contract_sys_id]
  data:
    governing_law: "State of Delaware, United States"
    payment_terms: "Net 30"
    notice_period: 90
    work_notes: "Metadata extraction completed. Completeness: 88%. 5 obligations cataloged. Notice deadline: 2026-09-01."
```

## Tool Usage

| Operation | MCP Tool | REST Endpoint |
|-----------|----------|---------------|
| Read Contract | SN-Read-Record | GET /api/now/table/ast_contract/{sys_id} |
| Query Documents | SN-Query-Table | GET /api/now/table/clm_contract_doc |
| Query Obligations | SN-Query-Table | GET /api/now/table/clm_obligation |
| Query Attachments | SN-Query-Table | GET /api/now/table/sys_attachment |
| Create Obligation | SN-Create-Record | POST /api/now/table/clm_obligation |
| Update Contract | SN-Update-Record | PATCH /api/now/table/ast_contract/{sys_id} |
| Batch Extraction | SN-Execute-Background-Script | POST /api/now/table/sys_trigger |

## Best Practices

- **Consistent Taxonomy:** Use standardized obligation types and clause categories to enable portfolio-wide analysis
- **Completeness Scoring:** Track metadata completeness percentage for each contract; target 90%+ for active contracts
- **Renewal Calendar:** Build a centralized renewal calendar from extracted dates; alert 90 days before notice deadlines
- **Party Normalization:** Ensure vendor names are linked to `core_company` records to avoid duplicate vendor entries
- **Version Control:** Always extract metadata from the most recent executed version of the contract document
- **Obligation Ownership:** Assign clear responsible parties (buyer vs. vendor) for each obligation
- **Financial Standardization:** Normalize all financial values to a single currency for portfolio reporting
- **Audit Trail:** Record who performed the extraction and when; note any assumptions or ambiguities

## Troubleshooting

### Contract Document Content Is Empty

**Symptom:** `clm_contract_doc` records exist but the content field is null
**Cause:** Contract content may be stored as attachments rather than inline in the content field
**Solution:** Query `sys_attachment` with `table_name=clm_contract_doc^table_sys_id=[doc_sys_id]` to find the actual document file.

### Governing Law Field Not Available

**Symptom:** The `governing_law` field does not exist on `ast_contract`
**Cause:** This field may be a custom addition or use a different name like `jurisdiction` or `applicable_law`
**Solution:**
```
Tool: SN-Discover-Table-Schema
Parameters:
  table_name: ast_contract
```
Search for fields containing "law", "jurisdiction", or "govern" in the element name or label.

### Obligation Types Do Not Match Expected Values

**Symptom:** Obligation type choices do not include expected categories
**Cause:** Choice values are organization-specific and may differ from defaults
**Solution:** Query `sys_choice` with `name=clm_obligation^element=obligation_type` to see available choices. Add custom choices if needed.

## Examples

### Example 1: New Contract Metadata Population

**Scenario:** Legal assistant uploads a new vendor agreement and needs metadata extracted

```
Tool: SN-Read-Record
Parameters:
  table_name: ast_contract
  sys_id: abc123def456
  fields: sys_id,number,short_description,vendor,starts,ends,total_cost,auto_renew,notice_period,governing_law
```

**Extracted Metadata:**
- **Parties:** Acme Corp (Buyer) / CloudVault Inc. (Vendor)
- **Effective Date:** 2026-04-01 | **Expiration:** 2029-03-31
- **Total Value:** $450,000 ($150,000/year)
- **Auto-Renewal:** Yes, 1-year terms | **Notice Period:** 60 days
- **Notice Deadline:** 2029-01-30
- **Governing Law:** State of California
- **Key Contacts:** Jane Smith (Buyer), Bob Chen (Vendor)
- **Obligations Cataloged:** 7 (4 vendor, 3 buyer)
- **Completeness:** 94%

### Example 2: Portfolio-Wide Metadata Audit

**Scenario:** CLM admin needs to identify contracts with missing metadata

```
Tool: SN-Query-Table
Parameters:
  table_name: ast_contract
  query: active=true^governing_lawISEMPTY^ORnotice_periodISEMPTY^ORtotal_costISEMPTY
  fields: number,short_description,vendor,starts,ends,governing_law,notice_period,total_cost
  limit: 50
```

**Result:** 23 active contracts with incomplete metadata. Priority: 8 contracts expiring within 6 months missing notice period data.

## Related Skills

- `legal/contract-analysis` - Full contract risk analysis
- `legal/contract-obligation-extraction` - Deep obligation extraction and tracking
- `legal/contracts-query-enhancer` - Enhanced contract search capabilities
- `legal/legal-matter-summarization` - Legal matter context for contracts
- `document/document-extraction` - Document content extraction from attachments
