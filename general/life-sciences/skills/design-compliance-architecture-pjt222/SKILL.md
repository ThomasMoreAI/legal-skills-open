---
name: design-compliance-architecture-pjt222
title: 設合規架構
description: Design a compliance architecture that maps applicable regulations to computerized systems. Covers system inventory, criticality classification (GxP-critical, GxP-supporting, non-GxP), GAMP 5 category assignment, regulatory requirements traceability, and governance structure definition. Use when establishing a new regulated facility, formalising compliance across multiple systems, addressing a regulatory gap analysis, harmonising compliance after mergers or reorganisations, or preparing a site master file that references computerized systems.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/wenyan/skills/design-compliance-architecture
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: life-sciences
language: zh
---

# 設合規架構

立頂層合規框，映法規至系統、分要度、定受管境之治理。

## 用時

- 新受管之設施、部門或項目立
- 既有組織需跨諸系正其合規態
- 合規差析揭系統分類或驗策之缺
- 併購或重組需跨實體統合規
- 備場主文件或質手冊引諸計算系統

## 入

- **必要**：在範計算系統之單（名、用、供/自造）
- **必要**：適法規框（21 CFR Part 11、EU Annex 11、GMP、GLP、GCP、ICH Q7、ICH Q10）
- **必要**：組境（部、場、品類）
- **可選**：既有之驗主計或質手冊
- **可選**：前審發或法規察
- **可選**：附質與 IT 報告線之組圖

## 法

### 第一步：建系統清冊

建全面之計算系統清冊：

```markdown
# System Inventory
## Document ID: SI-[SITE]-[YYYY]-[NNN]

| ID | System Name | Version | Vendor | Purpose | Department | Data Types | Users |
|----|-------------|---------|--------|---------|------------|------------|-------|
| SYS-001 | LabWare LIMS | 8.1 | LabWare Inc. | Sample management and testing | QC | Test results, COA | 45 |
| SYS-002 | SAP ERP | S/4HANA | SAP SE | Batch release and inventory | Production | Batch records, BOM | 120 |
| SYS-003 | Custom R/Shiny | 2.1.0 | Internal | Statistical analysis | Biostatistics | Clinical data | 8 |
| SYS-004 | Windows Server | 2022 | Microsoft | File server | IT | Documents | 200 |
```

**得：** 建、改、存、取、傳 GxP 相關數據之諸系統皆列。
**敗則：** 若系統主不能供全資，錄缺而排發現會。缺系統為關鍵合規險。

### 第二步：分系統要度

各系統賦要度層：

```markdown
# System Criticality Classification
## Document ID: SCC-[SITE]-[YYYY]-[NNN]

### Classification Criteria

| Tier | Definition | Validation Required | Examples |
|------|-----------|-------------------|----------|
| **GxP-Critical** | Directly impacts product quality, patient safety, or data integrity. Generates or processes GxP records. | Full CSV per GAMP 5 | LIMS, ERP (batch), CDMS, MES |
| **GxP-Supporting** | Supports GxP processes but does not directly generate GxP records. Failure has indirect impact. | Risk-based qualification | Email, document management, scheduling |
| **Non-GxP** | No impact on product quality, safety, or data integrity. | IT standard controls only | HR systems, cafeteria, general web |

### System Classification Matrix

| System ID | System | Tier | Rationale |
|-----------|--------|------|-----------|
| SYS-001 | LabWare LIMS | GxP-Critical | Generates test results used for batch release |
| SYS-002 | SAP ERP | GxP-Critical | Manages batch records and material traceability |
| SYS-003 | R/Shiny App | GxP-Critical | Performs statistical analysis for regulatory submissions |
| SYS-004 | Windows Server | GxP-Supporting | Stores controlled documents but does not generate GxP data |
```

**得：** 各系統有層賦並記由。
**敗則：** 若系統要度有爭，升至質委。疑則分高一層，正險析後重評。

### 第三步：賦 GAMP 5 軟類

為各 GxP-Critical 與 GxP-Supporting 系統賦 GAMP 5 類：

```markdown
# GAMP 5 Category Assignment

| System ID | System | GAMP Category | Rationale | Validation Effort |
|-----------|--------|---------------|-----------|-------------------|
| SYS-001 | LabWare LIMS | 4 — Configured Product | COTS with extensive workflow configuration | Medium-High |
| SYS-002 | SAP ERP | 4 — Configured Product | COTS with custom transactions | Medium-High |
| SYS-003 | R/Shiny App | 5 — Custom Application | Internally developed | High — Full lifecycle |
| SYS-004 | Windows Server | 1 — Infrastructure | Operating system, no custom configuration | Low — Verify installation |
```

類參：
- **Category 1**：基礎設施（OS、固件）——驗裝
- **Category 3**：未配 COTS——驗功能如是
- **Category 4**：已配產品——驗諸配
- **Category 5**：自造應用——全生命驗

**得：** 類賦合系統實用，非唯其性。
**敗則：** 若系統跨類（如 COTS 附自加），自加部分類為 Category 5，基為 Category 4。

### 第四步：映法規至系統

建法規可溯矩陣：

```markdown
# Regulatory Requirements Traceability Matrix
## Document ID: RRTM-[SITE]-[YYYY]-[NNN]

| Regulation | Clause | Requirement | Applicable Systems | Control Type |
|-----------|--------|-------------|-------------------|--------------|
| 21 CFR 11 | 11.10(a) | Validation | SYS-001, SYS-002, SYS-003 | Procedural + Technical |
| 21 CFR 11 | 11.10(d) | Access controls | SYS-001, SYS-002, SYS-003, SYS-004 | Technical |
| 21 CFR 11 | 11.10(e) | Audit trail | SYS-001, SYS-002, SYS-003 | Technical |
| 21 CFR 11 | 11.50 | Signature manifestation | SYS-001, SYS-002 | Technical |
| EU Annex 11 | §4 | Validation | SYS-001, SYS-002, SYS-003 | Procedural + Technical |
| EU Annex 11 | §7 | Data storage and backup | All | Technical |
| EU Annex 11 | §9 | Audit trail | SYS-001, SYS-002, SYS-003 | Technical |
| EU Annex 11 | §12 | Security and access | All | Technical |
| ICH Q10 | §3.2 | Change management | All GxP-Critical | Procedural |
| ICH Q10 | §1.8 | Knowledge management | SYS-001, SYS-003 | Procedural |
```

**得：** 諸適法規款映至少一系統，諸 GxP-Critical 系統映相關款。
**敗則：** 未映款為合規缺。為各缺建修計附時限。

### 第五步：定各系統驗策

依要度、類、法規映：

```markdown
# Validation Strategy Summary

| System | Category | Criticality | Validation Approach | Key Deliverables |
|--------|----------|------------|--------------------|--------------------|
| LabWare LIMS | 4 | Critical | Prospective CSV | URS, RA, VP, IQ, OQ, PQ, TM, VSR |
| SAP ERP | 4 | Critical | Prospective CSV | URS, RA, VP, IQ, OQ, TM, VSR |
| R/Shiny App | 5 | Critical | Prospective CSV + code review | URS, RA, VP, IQ, OQ, PQ, TM, VSR, code audit |
| Windows Server | 1 | Supporting | Installation qualification | IQ checklist |
```

簡：URS（用者要求）、RA（險評）、VP（驗計）、IQ/OQ/PQ（裝/運/性能合格）、TM（可溯矩陣）、VSR（驗總結報）。

**得：** 驗力比險——Category 5 GxP-Critical 系統全生命；Category 1 基礎設施簡 IQ。
**敗則：** 若關者欲減關鍵系統之驗，以 QA 簽錄險受。

### 第六步：設治理結構

定持續合規之組框：

```markdown
# Compliance Governance Structure

## Roles and Responsibilities
| Role | Responsibility | Authority |
|------|---------------|-----------|
| Quality Director | Overall compliance accountability | Approve validation strategies, accept risks |
| System Owner | Day-to-day system compliance | Approve changes, ensure validated state |
| Validation Lead | Plan and coordinate validation activities | Define validation scope and approach |
| IT Operations | Technical infrastructure and security | Implement technical controls |
| QA Reviewer | Independent review of validation deliverables | Accept or reject validation evidence |

## Governance Committees
| Committee | Frequency | Purpose | Members |
|-----------|-----------|---------|---------|
| Change Control Board | Weekly | Review and approve system changes | System owners, QA, IT, validation |
| Periodic Review Committee | Quarterly | Review system compliance status | Quality director, system owners, QA |
| Audit Programme Committee | Annual | Plan internal audit schedule | Quality director, lead auditor, QA |

## Escalation Matrix
| Issue | First Escalation | Second Escalation | Timeline |
|-------|-----------------|-------------------|----------|
| Critical audit finding | System Owner → QA Director | QA Director → Site Director | 24 hours |
| Validated state breach | Validation Lead → System Owner | System Owner → Quality Director | 48 hours |
| Data integrity incident | System Owner → QA Director | QA Director → Regulatory Affairs | 24 hours |
```

**得：** 諸合規活有清責無孤責。
**敗則：** 若責疊或未賦，集 RACI 會以解。責歧為常法規引。

### 第七步：匯合規架構文件

合諸件為主文件：

```markdown
# Compliance Architecture
## Document ID: CA-[SITE]-[YYYY]-[NNN]
## Version: 1.0

### 1. Purpose and Scope
[Organisation, site, product scope, regulatory scope]

### 2. System Inventory
[From Step 1]

### 3. Criticality Classification
[From Step 2]

### 4. GAMP 5 Category Assignments
[From Step 3]

### 5. Regulatory Requirements Traceability
[From Step 4]

### 6. Validation Strategy
[From Step 5]

### 7. Governance Structure
[From Step 6]

### 8. Periodic Review Schedule
- System inventory refresh: Annual
- Criticality re-assessment: When new systems added or regulations change
- Regulatory mapping update: When new guidance issued
- Governance review: Annual or after organisational change

### 9. Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Quality Director | | | |
| IT Director | | | |
| Regulatory Affairs | | | |
```

**得：** 單一文為全受管境之合規藍圖。
**敗則：** 若文超實用大小，建主文件附按系或域之從屬文件。

## 驗

- [ ] 系統清冊含諸理 GxP 數據之系
- [ ] 各系統有要度層並記由
- [ ] GAMP 5 類賦諸 GxP-Critical 與 GxP-Supporting 系
- [ ] 法規可溯矩陣覆諸適款
- [ ] 諸 GxP-Critical 系統有定驗策
- [ ] 治理結構定責、委、升階線
- [ ] 諸文有唯一 ID 與版控
- [ ] 合規架構文經質與 IT 領導准

## 陷

- **清冊不全**：缺系統於合規為隱。用網掃、軟資產理具、部問——非唯問 IT。
- **二元思**：系統非唯「GxP」或「非 GxP」。三層模（關鍵、支持、非 GxP）避過驗與欠驗。
- **類惑**：GAMP 5 類述軟件是何，然驗力宜反如何用。用於批放之 Category 4 需測多於用於排程之 Category 4。
- **靜架構**：合規架構為活文件。新系、法規變、審發皆需更。
- **治理無牙**：紙上委從不集則合規無值。定會頻與定足。

## Related Skills

- `perform-csv-assessment` — 為個系統執此所定之驗策
- `manage-change-control` — 運治理中定之變控程
- `implement-electronic-signatures` — 實法規矩陣映之電簽控
- `prepare-inspection-readiness` — 以此架構為察備基
- `conduct-gxp-audit` — 以合規架構為基線審
