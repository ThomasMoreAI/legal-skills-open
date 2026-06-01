---
name: conduct-gxp-audit-2
title: 行 GxP 稽核
description: Conduct a GxP audit of computerized systems and processes. Covers audit planning, opening meetings, evidence collection, finding classification (critical/major/minor), CAPA generation, closing meetings, report writing, and follow-up verification. Use for scheduled internal audits, supplier qualification audits, pre-inspection readiness assessments, for-cause audits triggered by deviations or data integrity concerns, or periodic compliance posture reviews of validated systems.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/wenyan-lite/skills/conduct-gxp-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: zh
---

# 行 GxP 稽核

規劃並行電腦化系統、數據完整性實踐、或受規流程之 GxP 稽核。

## 適用時機

- 受驗電腦化系統之定期內部稽核
- GxP 相關軟體之供應商資格稽核
- 法規稽核前之備查評估
- 偏差、投訴、數據完整性疑慮觸發之因由稽核
- 受驗系統之合規姿態之定期審

## 輸入

- **必要**：稽核範圍（受稽之系統、流程、或場址）
- **必要**：適用法規（21 CFR Part 11、EU Annex 11、GMP、GLP、GCP）
- **必要**：先前稽核報告與未結 CAPA 項
- **選擇性**：系統驗證文件（URS、VP、IQ/OQ/PQ、可追蹤矩陣）
- **選擇性**：SOP、訓練記錄、變更控制日誌
- **選擇性**：觸發稽核之具體風險或疑慮

## 步驟

### 步驟一：擬稽核計畫

```markdown
# Audit Plan
## Document ID: AP-[SYS]-[YYYY]-[NNN]

### 1. Objective
[State the purpose: scheduled, for-cause, supplier qualification, pre-inspection]

### 2. Scope
- **System/Process**: [Name and version]
- **Regulations**: [21 CFR Part 11, EU Annex 11, ICH Q7, etc.]
- **Period**: [Date range of records under review]
- **Exclusions**: [Any areas explicitly out of scope]

### 3. Audit Criteria
| Area | Regulatory Reference | Key Requirements |
|------|---------------------|------------------|
| Electronic records | 21 CFR 11.10 | Controls for closed systems |
| Audit trail | 21 CFR 11.10(e) | Secure, computer-generated, time-stamped |
| Electronic signatures | 21 CFR 11.50 | Manifestation, legally binding |
| Access controls | EU Annex 11, §12 | Role-based, documented |
| Data integrity | MHRA guidance | ALCOA+ principles |
| Change control | ICH Q10 | Documented, assessed, approved |

### 4. Schedule
| Date | Time | Activity | Participants |
|------|------|----------|-------------|
| Day 1 AM | 09:00 | Opening meeting | All |
| Day 1 AM | 10:00 | Document review | Auditor + QA |
| Day 1 PM | 13:00 | System walkthrough | Auditor + IT + System Owner |
| Day 2 AM | 09:00 | Interviews + evidence collection | Auditor + Users |
| Day 2 PM | 14:00 | Finding consolidation | Auditor |
| Day 2 PM | 16:00 | Closing meeting | All |

### 5. Audit Team
| Role | Name | Responsibility |
|------|------|---------------|
| Lead Auditor | [Name] | Plan, execute, report |
| Subject Matter Expert | [Name] | Technical assessment |
| Auditee Representative | [Name] | Facilitate access and information |
```

**預期：** 稽核計畫經品管准並於稽核至少兩週前告受稽方。
**失敗時：** 若受稽方不能供所需文件或人員，重排。

### 步驟二：行開場會

議程：
1. 介紹稽核團隊與角色
2. 確範圍、排程、後勤
3. 解發現分類制（critical/major/minor）
4. 確保密協議
5. 識受稽方陪同與文件保管者
6. 答疑

**預期：** 開場會附出席記錄而記。
**失敗時：** 若關鍵人員無法到場，重排所受影響之稽核活動。

### 步驟三：集並審證

依稽核標準審文件與記錄：

#### 3a. 驗證文件審
- [ ] URS 存且已核
- [ ] 驗證計畫合系統類別與風險
- [ ] IQ/OQ/PQ 協議已執行且結果有記
- [ ] 可追蹤矩陣連需求與測試結果
- [ ] 偏差已記且已解
- [ ] 驗證總結報已核

#### 3b. 運作控制審
- [ ] SOP 現行且已核
- [ ] 訓練記錄顯所有用戶之勝任
- [ ] 變更控制記錄完整（申請、評估、核、驗）
- [ ] 事件/偏差報依 SOP 處
- [ ] 定期審依排程進行

#### 3c. 數據完整性評估
- [ ] 稽核軌跡已啟且用戶不可改
- [ ] 電子簽章合法規要件
- [ ] 備份與復原程序有記且已測
- [ ] 存取控制執行角色權限
- [ ] 資料可歸屬、可讀、同時、原始、準確（ALCOA+）

#### 3d. 系統組態審
- [ ] 生產組態合受驗態
- [ ] 用戶帳已審——無共用、無效者已停
- [ ] 系統時鐘同步且準
- [ ] 安全修補依已核變更控制而施

**預期：** 證以螢幕截圖、文件副本、附時戳之面談筆記收集。
**失敗時：** 記「不能驗」為觀察並註其因。

### 步驟四：分類發現

按嚴重性分類每發現：

| Classification | Definition | Response Required |
|---------------|------------|-------------------|
| **Critical** | Direct impact on product quality, patient safety, or data integrity. Systematic failure of a key control. | Immediate containment + CAPA within 15 business days |
| **Major** | Significant departure from GxP requirements. Potential to impact data integrity if uncorrected. | CAPA within 30 business days |
| **Minor** | Isolated deviation from procedure. No direct impact on data integrity or product quality. | Correction within 60 business days |
| **Observation** | Opportunity for improvement. Not a regulatory requirement. | Optional — tracked for trend analysis |

每發現記：

```markdown
## Finding F-[NNN]
**Classification:** [Critical / Major / Minor / Observation]
**Area:** [Audit trail / Access control / Change control / etc.]
**Reference:** [Regulatory clause, e.g., 21 CFR 11.10(e)]

**Observation:**
[Objective description of what was found]

**Evidence:**
[Document ID, screenshot reference, interview notes]

**Regulatory Expectation:**
[What the regulation requires]

**Risk:**
[Impact on data integrity, product quality, or patient safety]
```

**預期：** 每發現有分類、證、法規引。
**失敗時：** 若分類有爭，升呈稽核計畫經理裁決。

### 步驟五：行閉場會

議程：
1. 報發現總（不宜生新發現）
2. 審發現分類
3. 商初步 CAPA 期待與時限
4. 確後續步驟與報告時限
5. 謝受稽方之配合

**預期：** 閉場會附出席而記。受稽方認發現（認≠同意）。
**失敗時：** 若受稽方爭某發現，記其歧異並依 SOP 升呈。

### 步驟六：寫稽核報告

```markdown
# Audit Report
## Document ID: AR-[SYS]-[YYYY]-[NNN]

### 1. Executive Summary
An audit of [System/Process] was conducted on [dates] against [regulations].
[N] findings were identified: [n] critical, [n] major, [n] minor, [n] observations.

### 2. Scope and Methodology
[Summarize audit plan scope, criteria, and methods used]

### 3. Findings Summary
| Finding ID | Classification | Area | Brief Description |
|-----------|---------------|------|-------------------|
| F-001 | Major | Audit trail | Audit trail disabled for batch record module |
| F-002 | Minor | Training | Two users missing annual GxP training |
| F-003 | Observation | Documentation | SOP formatting inconsistencies |

### 4. Detailed Findings
[Include full finding details from Step 4 for each finding]

### 5. Positive Observations
[Document areas of good practice observed during the audit]

### 6. Conclusion
The overall compliance status is assessed as [Satisfactory / Needs Improvement / Unsatisfactory].

### 7. Distribution
| Recipient | Role |
|-----------|------|
| [Name] | System Owner |
| [Name] | QA Director |
| [Name] | IT Manager |

### Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Lead Auditor | | | |
| QA Director | | | |
```

**預期：** 報告於閉場會後 15 工作日內發。
**失敗時：** 若延超 15 日，告關係人並記其因。

### 步驟七：追 CAPA 並驗其效

每需 CAPA 之發現：

```markdown
## CAPA Tracking
| Finding ID | CAPA ID | Root Cause | Corrective Action | Due Date | Status | Effectiveness Check |
|-----------|---------|------------|-------------------|----------|--------|-------------------|
| F-001 | CAPA-2025-042 | Configuration oversight during upgrade | Enable audit trail, verify all modules | 2025-04-15 | Open | Scheduled 2025-07-15 |
| F-002 | CAPA-2025-043 | Training matrix not updated | Complete training, update tracking | 2025-05-01 | Open | Scheduled 2025-08-01 |
```

**預期：** CAPA 已指派、追蹤、於定時限內驗效。
**失敗時：** 未結之 CAPA 升呈 QA 管理並於次稽核週期標記。

## 驗證

- [ ] 稽核計畫於稽核前已核且已告
- [ ] 開場與閉場會附出席而記
- [ ] 證附時戳與來源引而集
- [ ] 每發現有分類、證、法規引
- [ ] 稽核報於 15 工作日內發
- [ ] 所有 critical 與 major 發現之 CAPA 已指派含到期日
- [ ] 前稽核之 CAPA 已驗其結效

## 常見陷阱

- **範圍蔓延**：稽核中擴範圍而無正式協議致涵蓋不全且生爭
- **意見性發現**：發現須引具體法規要件，非個人偏好
- **對抗語調**：稽核乃協作品質改進，非審訊
- **忽正面**：僅報發現而不認良實損信
- **無效性檢**：未驗修確有效即結 CAPA，乃屢現之法規引

## 相關技能

- `perform-csv-assessment` — 完整 CSV 生命週期評估（URS 至驗證總結）
- `setup-gxp-r-project` — 受驗 R 環境之項目結構
- `implement-audit-trail` — 電子記錄之稽核軌跡實現
- `write-validation-documentation` — IQ/OQ/PQ 協議與報告撰寫
- `security-audit-codebase` — 安全聚焦之代碼稽核（互補視角）
