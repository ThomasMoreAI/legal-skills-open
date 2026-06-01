---
name: box-legal-workflows
title: Shared Legal Concepts
description: Legal concepts for Box-based legal workflows — risk rating frameworks, human-in-the-loop requirements, confidentiality principles, Box AI governance, collaboration roles, metadata strategy, and common workflow patterns. Referenced by box-legal-workflows-ma, box-legal-workflows-intake, and box-legal-workflows-contract skills.
author: box
author_url: https://github.com/box/box-for-ai/tree/main/skills/box-legal-workflows
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Shared Legal Concepts

> **PREREQUISITE:** Read `box:box` for Box MCP authentication, tool selection, and base workflows. If missing, run: `npx skills add https://github.com/box/box-for-ai --skill box`

Common legal principles, risk frameworks, and Box workflow patterns used by legal skills (M&A, Intake, Contract Review).

---

## Risk Rating Framework

**[CONFIRM WITH USER: What risk rating criteria does your firm use?]**

### High Risk
- Matters > firm's value threshold (e.g., $500K+)
- Politically exposed persons (PEP)
- Cross-border with sanctioned jurisdictions
- Conflicts of interest identified
- Missing critical contract protections
- 3+ material variances from standard templates
- Reputational risk to firm
- Criminal matters with media exposure

### Medium Risk
- Complex corporate matters
- Litigation or regulatory exposure
- Unclear source of funds
- Minor conflicts requiring analysis
- 1-2 material variances from templates
- Incomplete documentation (can be supplemented)
- Matter value in mid-range (e.g., $50K-$500K)

### Low Risk
- Individual clients, standard matters
- No litigation history
- All required documents complete and valid
- No conflicts of interest
- No material variances from templates
- Matter value below threshold (e.g., < $50K)

**[CONFIRM: Customize thresholds for your firm's practice areas]**

---

## Human-in-the-Loop Requirements

### ALWAYS Confirm Before:
1. Granting external access (outside your organization)
2. Creating shared links (especially Open/Company-wide)
3. Auto-approving any client or contract
4. Assigning risk ratings
5. Routing to specific attorneys
6. Generating legal documents (engagement letters, contracts)
7. Sharing legal documents with clients/third parties
8. Copying files to externally-accessible folders (if file was NOT already externally accessible)
9. Creating initial folder structures (default vs. custom for deal rooms, matter folders)

### CONFIRM If Uncertain:
10. Writing or modifying metadata (if extracted values are unclear or contradictory)
11. Copying or reorganizing files (if categorization is ambiguous)
12. Making decisions based on AI analysis (if confidence is low or edge case)

### Proceed Autonomously When Confident:
- Writing metadata when extraction is clear and unambiguous
- Copying/organizing files between folders with same access level (internal-only to internal-only, or external to external)
- Extracting standard information (dates, parties, amounts) with high confidence
- Creating summary reports and analysis documents
- Categorizing documents by obvious type

### NEVER Auto-Approve Without Authorization:
- High-risk matters
- External access grants (Editor/Co-Owner roles)
- Engagement letters or contract generation
- Matters in sensitive practice areas (criminal, sanctions)
- Clients/contracts above value thresholds
- Actions that bypass firm policies

---

## Confidentiality & Data Protection

### Access Control Principles
- **Need-to-know**: Grant minimum permissions required
- **Least privilege**: Default to Viewer over Editor
- **Folder-level**: Prefer specific folders over root access
- **Time-limited**: Set expiration dates on external collaborations
- **Audit trail**: Track access grants with `list_item_collaborations`

### Sensitive Information Categories
- Client intake forms (ID scans, financial records)
- Contract terms (pricing, IP rights, liability caps)
- M&A deal documents (financials, strategy, due diligence)
- Attorney work product and strategy memos

**Never expose to:**
- External parties beyond need-to-know
- Internal staff outside matter team
- Open shared links
- AI training (follow Box AI governance)

### Box Collaboration Roles

**[CONFIRM: What permission level is appropriate?]**

| Role | View | Upload | Edit | Delete | Invite | Use Case |
|------|------|--------|------|--------|--------|----------|
| Viewer | ✅ | ❌ | ❌ | ❌ | ❌ | Clients, read-only stakeholders |
| Uploader | ❌ | ✅ | ❌ | ❌ | ❌ | External counsel submissions |
| Previewer | ✅* | ❌ | ❌ | ❌ | ❌ | High-confidentiality (no download) |
| Editor | ✅ | ✅ | ✅ | ✅ | ❌ | Internal team members |
| Co-Owner | ✅ | ✅ | ✅ | ✅ | ✅ | Deal leads, matter owners |

*Preview only, no download

---

## Box AI Governance

### When to Use Box AI
- Document completeness checks
- Risk factor identification (flag for human review)
- Metadata extraction (dates, parties, terms)
- Contract comparison (identify variances)
- Due diligence Q&A (with citation verification)

### When NOT to Use Box AI
- Final legal advice/decisions (human attorney only)
- Access control decisions (human approves permissions)
- Client conflict checks (use firm's conflict system)
- Privilege determinations (attorney judgment)
- Settlement negotiations or strategy

### Best Practices
- **Pace calls**: 1-2 seconds apart (rate limits)
- **Verify citations**: Surface source documents
- **Provide context**: "Assessing risk for law firm. Identify..."
- **Limit scope**: Search specific folders, not entire account
- **Human verification**: AI informs, human decides

---

## Common Legal Workflows

### Document Review Pattern
1. Authenticate (`who_am_i`)
2. Locate folder (`list_folder_content_by_folder_id` or `search_folders_by_name`)
3. Inventory documents (`list_folder_content_by_folder_id`)
4. **[CONFIRM: What documents are required?]**
5. Assess completeness (`ai_qa_multi_file`)
6. Extract metadata (`ai_extract_structured_from_metadata_template`)
7. Write metadata (`set_file_metadata`)
8. Route for review (`create_file_comment` + `create_collaboration`)

### Permission Audit Pattern
1. **[CONFIRM: What folder to audit?]**
2. List current permissions (`list_item_collaborations`)
3. Categorize: internal vs. external, roles, expirations
4. Present audit report
5. **[CONFIRM: Should permissions be modified?]**
6. Make approved changes
7. Re-audit to verify (`list_item_collaborations`)

### Temporal Monitoring Pattern
1. **[CONFIRM: Date range? (e.g., next 60 days)]**
2. Search by metadata date field (`search_files_metadata`)
3. Identify owner, calculate days to deadline
4. **[CONFIRM: Who to notify?]**
5. Create reminder (`create_file_comment`)
6. Update metadata (`set_file_metadata` with notification tracking)

---

## Metadata Strategy

**[CONFIRM: Do you have existing Box metadata templates?]**

### Common Legal Metadata Fields

**Matter information:**
- matter_id, matter_name, practice_area, matter_owner

**Parties:**
- client_name, counterparty_name, contracting_entities

**Dates:**
- execution_date, effective_date, expiration_date, review_date

**Status:**
- active, expired, under_negotiation, pending_approval

**Risk:**
- risk_rating (high/medium/low), risk_factors, review_required

**Contract terms:**
- contract_value, payment_terms, notice_period, auto_renewal

**Review tracking:**
- reviewed_by, review_date, next_review_date

### Template Setup (If None Exists)
1. **[CONFIRM: Create metadata template?]**
2. Define fields based on firm needs
3. Use `create_metadata_template`
4. Apply to files with `set_file_metadata`

---

## Decision Transparency

For every automated decision, document:
- **WHAT**: Approved, rejected, routed, risk rating
- **WHY**: Supporting evidence, risk factors, variances
- **WHEN**: Timestamp
- **WHO**: Human or "Automated Review Agent"
- **SOURCES**: Which documents, sections, pages
- **TRACEABILITY**: Write summary to Box, add to metadata

---

## Compliance & Audit Trail

### Maintain Records Of:
- Permission grants (who, what, when, why, expiration)
- Risk assessments (criteria, factors identified)
- Routing decisions (who assigned, why)
- Client approvals/rejections (basis)
- Contract reviews (variances, ratings)

### Verification Steps:
1. `list_item_collaborations` before and after permission changes
2. Record returned IDs (folder, file, collaboration IDs)
3. Timestamp all actions
4. Write decision summaries to Box
5. Update metadata to reflect current state

---

## Legal Tool Selection

| Legal Task | Primary Tool | Notes |
|------------|--------------|-------|
| Create folders | `create_folder` | Batch for efficiency |
| Upload documents | `upload_file` | New files |
| Copy documents | `copy_file` | Organize existing |
| Grant internal access | `create_collaboration` | Viewer/Editor/Co-Owner |
| Grant external access | **CONFIRM**, then `create_collaboration` | Always confirm |
| Create shared links | **CONFIRM**, then `add_folder_shared_link` | Confirm Open/Company/Collaborators |
| Audit permissions | `list_item_collaborations` | Before/after changes |
| Search by keyword | `search_files_keyword` | General search |
| Search by metadata | `search_files_metadata` | Structured queries |
| Review documents | `ai_qa_multi_file` | Completeness, risk, comparison |
| Extract metadata (template) | `ai_extract_structured_from_metadata_template` | If template exists |
| Extract metadata (custom) | `ai_extract_structured_from_fields_enhanced` | Define fields at runtime |
| Write metadata | `set_file_metadata` | Persist data |
| Tag for review | `create_file_comment` | Notify attorney |
| Due diligence Q&A | `ai_qa_multi_file` | Cross-document analysis |

---

## Common Confirmation Patterns

### Risk Rating
"Based on [factors], I would rate this as [High/Medium/Low] risk. Does this match your firm's criteria for [type]?"

### Permissions
"I'll grant [person] [role] access to [folder/file]. They can [permissions]. Proceed?"

### Routing
"Based on [practice area/risk/type], I recommend routing to [attorney]. Correct, or assign to someone else?"

### Document Completeness
"Firm requires: [list]. Found: [list]. Missing: [list]. Proceed with assessment?"

### Auto-Approval
"This [client/contract] is low-risk and complete. Does your firm allow auto-approval, or should attorney review first?"

### Metadata Template
"Do you have Box metadata template for [type]? If yes, scope and template key?"

### Thresholds
"What is your firm's threshold for [matter value/expiration alert/risk escalation]?"

### External Sharing
"Before sharing with [external party], confirm: (1) Permission level? (2) Folders? (3) Expiration? (4) Link or collaboration?"
