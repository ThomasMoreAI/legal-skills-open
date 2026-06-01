---
name: box-legal-workflows-contract
title: Contract Review Agent
description: Automate contract review and monitoring with Box MCP — identify new contracts added since last review period using metadata or keyword search, compare contracts against standard firm templates to flag material variances (indemnification, liability caps, termination rights, governing law, IP ownership), extract and write structured metadata (parties, dates, contract value, key clauses, risk ratings, expiration dates) to Box for searchability, create variance analysis reports with citations, proactively monitor for expiring contracts to trigger renegotiation reminders with calculated notice deadlines, and batch process multiple contracts with rate-limit-aware pacing. Use this skill when the user mentions contract review, contract monitoring, NDA review, MSA comparison, contract expiration, contract metadata, variance analysis, or needs recurring contract analysis workflows.
author: box
author_url: https://github.com/box/box-for-ai/tree/main/skills/box-legal-workflows-contract
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Review Agent

> **PREREQUISITES:**
> - Read `box:box` for Box MCP auth, tool selection, base workflows. If missing, run: `npx skills add https://github.com/box/box-for-ai --skill box`
> - Read `box-legal-workflows` for risk frameworks, confidentiality, human-in-the-loop requirements, Box AI governance, metadata strategy. If missing, ensure it's installed from the same skill package.

Legal contract management involves regular review of executed agreements to ensure compliance, track dates (renewals, expirations), identify risks, and maintain structured metadata. This skill automates recurring reviews, variance analysis, metadata extraction, and proactive expiration monitoring.

**Core principles:** Recurring cadence, template-based comparison, structured metadata, proactive monitoring, human oversight for risk.

---

## Risk Assessment Framework

### Variance Analysis

**[CONFIRM: Material clauses for your firm/practice area?]**

**Material variances (High Risk):**
- Liability caps or limitations changes
- Indemnification modifications
- Termination rights or notice period alterations
- Governing law or dispute resolution changes
- Confidentiality obligation modifications
- IP ownership changes
- Non-standard payment terms or penalties

**Minor variances (Low Risk):**
- Address or entity name updates
- Minor formatting differences
- Clarifying language (no substance change)
- Standard exhibits or schedules

**Practice-specific material:**
- **Employment**: Non-compete, termination, benefits
- **Commercial**: Payment, warranties, liability
- **IP Licensing**: Usage rights, royalties, ownership
- **Real Estate**: Title, zoning, environmental
- **NDAs**: Confidential info definition, term, exceptions

### Risk Rating

**See box-legal-workflows for:** General risk framework.

**Contract-specific:**

**High Risk:**
- 3+ material variances from template
- Changes to indemnification, liability caps, termination, governing law
- Missing key protections from standard
- Unfavorable terms (unlimited liability, one-sided, auto-renewal without notice)
- Regulatory concerns (non-compliance, missing required clauses)

**Medium Risk:**
- 1-2 material variances
- Minor unfavorable terms (longer notice, restricted termination)
- Unclear/ambiguous clauses
- Missing exhibits (referenced but not attached)

**Low Risk:**
- No material variances OR minor clarifying changes only
- Favorable terms (stronger protections than standard)
- All key protections present

**[CONFIRM: Contract types ALWAYS flagged regardless of variance?]**
Examples: High-value (> $[threshold]), specific counterparties, certain jurisdictions, contracts > [X] years.

---

## Metadata Extraction Strategy

**[CONFIRM: Fields to extract?]**

**Core metadata:**
- Contract title/description
- Contracting parties (your entity + counterparty)
- Counterparty name (normalized)
- Contract type (NDA, MSA, SOW, License)
- Execution, effective, expiration dates
- Term length (months/years)
- Auto-renewal (yes/no, renewal term)
- Notice period for termination (days)
- Contract value, payment terms
- Governing law / jurisdiction

**Risk & review:**
- Risk rating (High/Medium/Low)
- Material variances (list)
- Review date, reviewed by
- Next review date
- Expiration alert date (e.g., 60 days before)
- Status (active/expired/terminated/under negotiation)

**Practice-specific:**
- **Employment**: Non-compete duration, benefits eligibility
- **IP**: License scope, royalty rate, territory
- **Real Estate**: Property address, zoning, environmental liens
- **Vendor**: SLA terms, data security requirements

**[CONFIRM: Box metadata templates for contracts exist?]**
If yes: scope and template key. If no: can create with `create_metadata_template`.

---

## Tool Selection

| Task | Primary Tool | Notes |
|------|--------------|-------|
| Find new contracts (date) | `search_files_metadata` | Query execution_date if exists |
| Find expiring | `search_files_metadata` | Query expiration_date within 30/60/90 days |
| Compare to template | `ai_qa_multi_file` | Multi-file Q&A (contract + template) |
| Extract metadata (template) | `ai_extract_structured_from_metadata_template` | If template exists |
| Extract metadata (custom) | `ai_extract_structured_from_fields_enhanced` | Define fields at runtime |
| Write metadata | `set_file_metadata` | Persist extracted fields |
| Identify variances | `ai_qa_multi_file` | Compare and highlight differences |
| Create variance report | `upload_file` | Write summary doc |
| Tag owner | `create_file_comment` | Notify attorney (expiring/review) |
| Batch process | Iterate with delays | 1-2 sec pauses for rate limits |

---

## Temporal Search Patterns

**Metadata search for date-based queries:**

### Find contracts executed in last 30 days
**[CONFIRM: Review cadence? Monthly? Quarterly?]**
```
search_files_metadata: "execution_date >= 'YYYY-MM-DD' AND execution_date <= 'YYYY-MM-DD'"
```

### Find contracts expiring in next 60 days
**[CONFIRM: Alert timing? 30/60/90 days before expiration?]**
```
search_files_metadata: "expiration_date >= 'YYYY-MM-DD' AND expiration_date <= 'YYYY-MM-DD' AND status = 'active'"
```

### Find by counterparty or risk
```
search_files_metadata: "counterparty_name = 'Acme Corp'"
search_files_metadata: "risk_rating = 'High'"
```

**Note:** Metadata search only works if contracts have metadata. Otherwise use `search_files_keyword` with date filters.

**[CONFIRM: How to identify new contracts? Execution date metadata? File upload date? Naming convention?]**

---

## Implementation Workflow

### Phase 1: Identify New Contracts (Recurring)
1. **Authenticate**: `who_am_i`
2. **[CONFIRM: Date range? Contracts folder ID?]**
3. **Search**: `search_files_metadata` (if metadata) or `search_files_keyword`
4. **[CONFIRM: These contracts to review?]**

### Phase 2: Compare vs. Template
5. **[CONFIRM: Standard template file ID for contract type?]**
6. **Compare**: `ai_qa_multi_file` (ask for material differences)
7. **[CONFIRM: Material clauses?]**
8. **Assess risk**: Apply criteria. **[CONFIRM: Match firm's criteria?]**

### Phase 3: Extract & Store Metadata
9. **Extract**: **[CONFIRM: Template scope/key?]** → `ai_extract_structured_from_metadata_template` or `ai_extract_structured_from_fields_enhanced`
10. **Write**: **[CONFIRM: Write all or only certain fields?]** → `set_file_metadata`
11. **Report**: `upload_file` (contract name, risk, variances, recommendations, citations)

### Phase 4: Route for Review (If Needed)
12. **Determine need**:
    - **HIGH RISK**: ALWAYS route
    - **MEDIUM RISK**: **[CONFIRM: Auto-approve or review?]**
    - **LOW RISK**: **[CONFIRM: Log only or review?]**
13. **Tag owner**: **[CONFIRM: Responsible attorney?]** → `create_file_comment`
14. **Grant access**: **[CONFIRM: Attorney has access?]** → `create_collaboration`

### Phase 5: Monitor Expiring (Proactive)
15. **Search expiring**: **[CONFIRM: Alert timing (30/60/90)?]** → `search_files_metadata`
16. **Create reminders**: **[CONFIRM: Who to notify?]** → `create_file_comment`
17. **Update metadata**: `set_file_metadata` (expiration_alert_sent: yes)

---

## Guardrails

**See box-legal-workflows for:** Human-in-the-loop requirements, confidentiality, Box AI governance.

**Contract-specific:**

**ALWAYS confirm before:**
1. Assigning risk ratings (validate criteria)
2. Routing to attorneys (confirm correct person)
3. Sending expiration alerts (confirm timing & recipient)
4. Copying files to externally-accessible folders (if file was NOT already externally accessible)

**CONFIRM if uncertain:**
5. Identifying material variances (if ambiguous or edge case)
6. Writing metadata (if extracted values are unclear or contradictory)

**Proceed autonomously when confident:**
- Writing metadata when extraction is clear and unambiguous
- Copying/organizing files between folders (internal-only to internal-only, or external to external)
- Creating variance reports
- Extracting dates, parties, and standard terms with high confidence
- Batch processing any size (pace appropriately)

**NEVER auto-approve without authorization:**
- High-risk contracts (3+ variances)
- Unfavorable indemnification or liability
- Contracts missing key protections
- Above value threshold
- High-stakes practice areas (litigation, IP)

**Batch processing:**
- Process one at a time (rate limits)
- Pace 1-2 seconds apart
- Report progress: "Processed 10/50..."

**Decision transparency:**
- Document WHAT compared (contract vs. template)
- Document WHICH variances (specific clauses)
- Document WHY rating assigned (link to report)
- Cite sections (page numbers, clauses)
- Timestamp review

**Box AI usage:**
- Context: "Reviewing contracts for law firm. Identify material variances creating legal risk..."
- Request citations: "For each variance, cite section and page"
- Pace appropriately (1-2 secs)
- Limit 2-3 files at a time (contract + template + max 1 prior version)

---

## Example Workflows

### Example 1: Monthly NDA Review
**Request:** "Review NDAs from last 30 days, compare to standard."

**Flow:**
1. **[CONFIRM]**: "NDAs folder ID? Metadata 'execution_date' or upload date?"
2. `search_files_metadata` (date range)
3. **[CONFIRM]**: "Found 5 NDAs. Standard template ID?"
4. For each (1-2 sec pauses):
   a. `ai_qa_multi_file` (compare, focus material clauses)
   b. **[CONFIRM]**: "Company X: 2 variances (broader definition, 5yr vs. 3yr). Medium risk?"
   c. `ai_extract_structured_from_metadata_template`
   d. `set_file_metadata`
   e. Create report, upload
5. Report: "Reviewed 5. Risk: 1 High, 2 Medium, 2 Low. High (Company Y): unlimited liability, no mutual."
6. **[CONFIRM]**: "Who reviews high-risk?"
7. `create_file_comment`, `create_collaboration`
8. Report: "Review complete. High routed to David."

### Example 2: Expiring Contracts
**Request:** "Find contracts expiring in next 60 days, alert owners."

**Flow:**
1. **[CONFIRM]**: "Folder ID? Metadata 'expiration_date' and 'status'?"
2. `search_files_metadata` (60 days, status=active)
3. **[CONFIRM]**: "Found 8. Owner from metadata 'contract_owner' or collaborations?"
4. For each:
   a. `get_file_details` (owner, dates, risk, notice period)
   b. Calculate days to expiration and notice deadline
   c. **[CONFIRM]**: "[Counterparty] expires [date] in [X] days. Notice [Y] days, act by [deadline]. Tag [attorney]?"
   d. `create_file_comment`
   e. `set_file_metadata` (alert_sent: yes)
5. Report: "Alerts sent for 8. 3 high (renegotiate), 4 medium (review), 1 low (consider expire)."

### Example 3: Extract Metadata (Unstructured)
**Request:** "20 vendor contracts, no metadata. Extract key terms."

**Flow:**
1. **[CONFIRM]**: "Folder ID?"
2. `list_folder_content_by_folder_id` (20)
3. **[CONFIRM]**: "Template exists? If no, extract: vendor, type, dates, value, payment, SLA, notice, renewal, law. Add/remove?"
4. **[CONFIRM]**: "Process 20 with 1-2 sec delays (~30-40 sec)?"
5. For each:
   a. `ai_extract_structured_from_fields_enhanced`
   b. **[IF UNCLEAR]**: **[CONFIRM]**: "Expiration '[date]'. Contract says '[text]'. Correct?"
   c. `set_file_metadata`
   d. Progress: "Processed 10/20..."
6. Report: "Extraction complete. 20 now searchable."
7. **[CONFIRM]**: "Create template for future?"

### Example 4: Compare Versions
**Request:** "Compare initial and final MSA with Acme, what changed?"

**Flow:**
1. **[CONFIRM]**: "File IDs for initial and final?"
2. `get_file_details` (both, verify)
3. **[CONFIRM]**: "Most important clauses? (Payment, Warranties, Indemnification, Liability, Termination, IP, Data)"
4. `ai_qa_multi_file` (compare, focus clauses)
5. Present: initial vs. final, favorable or unfavorable
6. **[CONFIRM]**: "Create report, route to attorney?"
7. `upload_file`, `create_file_comment`, `create_collaboration`
8. Report: "Comparison complete. Report routed to [attorney]."
