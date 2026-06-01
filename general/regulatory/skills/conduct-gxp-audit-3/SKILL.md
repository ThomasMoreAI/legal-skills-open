---
name: conduct-gxp-audit-3
title: 行 GxP 之審
description: Conduct a GxP audit of computerized systems and processes. Covers audit planning, opening meetings, evidence collection, finding classification (critical/major/minor), CAPA generation, closing meetings, report writing, and follow-up verification. Use for scheduled internal audits, supplier qualification audits, pre-inspection readiness assessments, for-cause audits triggered by deviations or data integrity concerns, or periodic compliance posture reviews of validated systems.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/wenyan/skills/conduct-gxp-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: zh
---

# 行 GxP 之審

謀與行 GxP 之審於算系、資整之行、或規程。

## 用時

- 排之內審於已驗之算系
- 供者資之審於 GxP 關軟
- 察前備評於規審前
- 因之審由偏、訴、或資整之疑而發
- 已驗系之規態週察

## 入

- **必**：審之範（系、程、或地）
- **必**：適之規（21 CFR Part 11、EU Annex 11、GMP、GLP、GCP）
- **必**：前審報與開之 CAPA
- **可選**：系驗之書（URS、VP、IQ/OQ/PQ、追溯矩）
- **可選**：SOP、訓錄、變控誌
- **可選**：發審之特險處或疑

## 法

### 第一步：建審之謀

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

**得：** 審謀已得質管之准且於審前二週通於被審者。
**敗則：** 若被審者不能供所需書或人，改期。

### 第二步：行開會

序：
1. 引審團與職
2. 確範、程、物流
3. 明得分之系（危/重/微）
4. 確密約
5. 識被審之陪與書之守
6. 答問

**得：** 開會有書附到錄。
**敗則：** 若要員不得，改受影之活。

### 第三步：收察證

察書與錄對審之準：

#### 3a. 驗書察
- [ ] URS 存且已准
- [ ] 驗謀合系類與險
- [ ] IQ/OQ/PQ 已行且果已書
- [ ] 追溯矩連求於測果
- [ ] 偏已書且解
- [ ] 驗總報已准

#### 3b. 行控察
- [ ] SOP 現且已准
- [ ] 訓錄示諸用者之能
- [ ] 變控錄全（請、評、准、驗）
- [ ] 事/偏之報依 SOP 治
- [ ] 週察依期行

#### 3c. 資整評
- [ ] 審跡啟且用者不可改
- [ ] 電簽合規
- [ ] 備與復之序已書且試
- [ ] 訪控執職之權
- [ ] 資可歸、可讀、當時、原、準（ALCOA+）

#### 3d. 系設察
- [ ] 產設合已驗之態
- [ ] 用戶察——無共戶，閒戶禁
- [ ] 系鐘同且準
- [ ] 安補依已准之變控施

**得：** 證收為截圖、書副、訪記附時戳。
**敗則：** 錄「不可驗」為察而注由。

### 第四步：分所得

依重分每得：

| Classification | Definition | Response Required |
|---------------|------------|-------------------|
| **Critical** | Direct impact on product quality, patient safety, or data integrity. Systematic failure of a key control. | Immediate containment + CAPA within 15 business days |
| **Major** | Significant departure from GxP requirements. Potential to impact data integrity if uncorrected. | CAPA within 30 business days |
| **Minor** | Isolated deviation from procedure. No direct impact on data integrity or product quality. | Correction within 60 business days |
| **Observation** | Opportunity for improvement. Not a regulatory requirement. | Optional — tracked for trend analysis |

每得書：

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

**得：** 每得有分、證、規引。
**敗則：** 若分有爭，升於審程之管以裁。

### 第五步：行閉會

序：
1. 示所得之摘（不應新得於此升）
2. 察得之分
3. 議初 CAPA 之期望與期
4. 確後步與報期
5. 謝被審之合

**得：** 閉會書附到。被審者認之（認 ≠ 同）。
**敗則：** 若被審爭得，書異而依 SOP 升。

### 第六步：書審報

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

**得：** 報於閉會後十五工日內發。
**敗則：** 若遲逾十五日，告相關而書由。

### 第七步：追 CAPA 而驗效

每需 CAPA 之得：

```markdown
## CAPA Tracking
| Finding ID | CAPA ID | Root Cause | Corrective Action | Due Date | Status | Effectiveness Check |
|-----------|---------|------------|-------------------|----------|--------|-------------------|
| F-001 | CAPA-2025-042 | Configuration oversight during upgrade | Enable audit trail, verify all modules | 2025-04-15 | Open | Scheduled 2025-07-15 |
| F-002 | CAPA-2025-043 | Training matrix not updated | Complete training, update tracking | 2025-05-01 | Open | Scheduled 2025-08-01 |
```

**得：** CAPA 已分、追、依期驗效。
**敗則：** 未解 CAPA 升於 QA 管且標於下審周。

## 驗

- [ ] 審謀已准且於審前通
- [ ] 開閉會書附到
- [ ] 證附時戳與源引
- [ ] 每得有分、證、規引
- [ ] 審報於十五工日內發
- [ ] 諸危重得有期之 CAPA
- [ ] 前審之 CAPA 已驗閉效

## 陷

- **範蔓**：審中擴範無正約，生不全之涵與爭。
- **意之得**：得必引特規，非私好。
- **敵語**：審乃共質改之事，非訊。
- **忽善**：只報得而不認善實損信。
- **無效察**：閉 CAPA 而不驗修真行乃常規之引。

## 參

- `perform-csv-assessment` — 全 CSV 生命之評（URS 至驗總）
- `setup-gxp-r-project` — 驗之 R 境之項目構
- `implement-audit-trail` — 電錄之審跡之實
- `write-validation-documentation` — IQ/OQ/PQ 之儀與報之書
- `security-audit-codebase` — 安專之碼審（補之觀）
