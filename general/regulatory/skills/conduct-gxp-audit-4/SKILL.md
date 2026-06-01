---
name: conduct-gxp-audit-4
title: 行 GxP 稽核
description: Conduct a GxP audit of computerized systems and processes. Covers audit planning, opening meetings, evidence collection, finding classification (critical/major/minor), CAPA generation, closing meetings, report writing, and follow-up verification. Use for scheduled internal audits, supplier qualification audits, pre-inspection readiness assessments, for-cause audits triggered by deviations or data integrity concerns, or periodic compliance posture reviews of validated systems.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/wenyan-ultra/skills/conduct-gxp-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: zh
---

# 行 GxP 稽核

謀與行 GxP 稽核於計算系統、數據完整踐、監管過程。

## 用

- 排定之內稽於驗證過之計算系統
- 供應/廠商資格稽於 GxP 相關軟體
- 監管稽前之備狀察
- 偏差、投訴、數據完整疑觸之因稽
- 驗證系統合規狀之期察

## 入

- **必**：稽範（所稽之系、程、場）
- **必**：適用法（21 CFR Part 11、EU Annex 11、GMP、GLP、GCP）
- **必**：前稽報與未閉 CAPA
- **可**：系統驗證文（URS、VP、IQ/OQ/PQ、追蹤矩陣）
- **可**：SOPs、訓練錄、變更控錄
- **可**：觸稽之特險域或憂

## 行

### 一：建稽計畫

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

**得：** 稽計畫由質管准、稽前至少 2 週告受稽方。

**敗：** 受稽方不能供所需文或人→改期。

### 二：行開會

議程：
1. 介稽組與角
2. 確範、程、物流
3. 釋發現分級（critical/major/minor）
4. 確保密協議
5. 識受稽方陪與文守者
6. 答問

**得：** 開會記含出席。

**敗：** 要員不在→改稽活動。

### 三：集與審證

對稽準察文與錄：

#### 3a. 驗證文審
- [ ] URS 在且已准
- [ ] 驗證計畫合系類與險
- [ ] IQ/OQ/PQ 協已行、果已記
- [ ] 追蹤矩鏈求於測果
- [ ] 偏差已記且解
- [ ] 驗證總結報已准

#### 3b. 操作控審
- [ ] SOPs 現且准
- [ ] 訓練錄示諸用之能
- [ ] 變更控錄全（求、評、准、驗）
- [ ] 事故/偏差報按 SOP 處
- [ ] 期察按程行

#### 3c. 數據完整評
- [ ] 稽軌啟且用者不可改
- [ ] 電簽合監管求
- [ ] 備復程已記且測
- [ ] 存取控執角色權
- [ ] 數據可歸、可讀、當時、原、準（ALCOA+）

#### 3d. 系配察
- [ ] 生產配合驗證態
- [ ] 用戶已察——無共帳、停活帳
- [ ] 系鐘同步且準
- [ ] 安補丁按已准變更控施

**得：** 證以截圖、文副、面談注加時戳集。

**敗：** 記「不可驗」為觀察且注因。

### 四：分發現

各發現按嚴分：

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

**得：** 每發現有級、證、監管引。

**敗：** 分級爭→升至稽程經理裁。

### 五：行閉會

議程：
1. 呈發現總結（勿生新發現）
2. 察發現分級
3. 議初 CAPA 期望與程
4. 確下一步與報程
5. 謝受稽方合

**得：** 閉會記含出席。受稽方承發現（承≠同）。

**敗：** 受稽方爭發現→記異且按 SOP 升。

### 六：寫稽報

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

**得：** 報於閉會後 15 工日內發。

**敗：** 逾 15 日→告干係人且記因。

### 七：追 CAPA 且驗效

每須 CAPA 之發現：

```markdown
## CAPA Tracking
| Finding ID | CAPA ID | Root Cause | Corrective Action | Due Date | Status | Effectiveness Check |
|-----------|---------|------------|-------------------|----------|--------|-------------------|
| F-001 | CAPA-2025-042 | Configuration oversight during upgrade | Enable audit trail, verify all modules | 2025-04-15 | Open | Scheduled 2025-07-15 |
| F-002 | CAPA-2025-043 | Training matrix not updated | Complete training, update tracking | 2025-05-01 | Open | Scheduled 2025-08-01 |
```

**得：** CAPAs 派、追、效按定程驗。

**敗：** 未解 CAPAs 升至 QA 管且於下稽周期標。

## 驗

- [ ] 稽計畫於稽前已准且告
- [ ] 開閉會記含出席
- [ ] 證含時戳與源引
- [ ] 每發現有級、證、監管引
- [ ] 稽報於 15 工日內發
- [ ] Critical 與 Major 發現有 CAPAs 含期
- [ ] 前稽 CAPAs 已驗閉效

## 忌

- **範蔓延**：行中無正式協增範→覆不全與爭。
- **憑見之發現**：發現須引具體監管求，非個好。
- **敵音**：稽為協質改，非訊問。
- **忽正**：只報發現而不承良踐→損信。
- **無效驗**：閉 CAPA 而不驗實效→常返監管引。

## 參

- `perform-csv-assessment` — 全 CSV 生命評（URS 至驗證總結）
- `setup-gxp-r-project` — 驗證 R 境之項目結構
- `implement-audit-trail` — 電錄之稽軌施
- `write-validation-documentation` — IQ/OQ/PQ 協與報寫
- `security-audit-codebase` — 安為重碼稽（補視角）
