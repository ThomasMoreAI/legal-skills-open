---
name: monitor-data-integrity
title: 監測資料完整性
description: Design and operate a data integrity monitoring programme based on ALCOA+ principles. Covers detective controls, audit trail review schedules, anomaly detection patterns (off-hours activity, sequential modifications, bulk changes), metrics dashboards, investigation triggers, and escalation matrix definition. Use when establishing a data integrity monitoring programme for GxP systems, preparing for inspections where data integrity is a focus area, after a data integrity incident requiring enhanced monitoring, or when implementing MHRA, WHO, or PIC/S guidance.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/wenyan-lite/skills/monitor-data-integrity
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: zh
---

# 監測資料完整性

依 ALCOA+ 原則與異常偵測，設計並運行貫穿經驗證系統之資料完整性持續監測計劃。

## 適用時機

- 為 GxP 系統建立資料完整性監測計劃
- 法規檢查在即，而資料完整性為其重點
- 資料完整性事件之後，須加強監測
- 既有資料完整性管制之定期檢視
- 實施 MHRA、WHO 或 PIC/S 之資料完整性指引

## 輸入

- **必要**：在範圍內之系統及其 ALCOA+ 風險概況
- **必要**：適用之指引（MHRA Data Integrity、WHO TRS 996、PIC/S PI 041）
- **必要**：每系統當前之審計追蹤能力
- **選擇性**：先前之資料完整性發現或法規觀察
- **選擇性**：既有監測程序或指標
- **選擇性**：用戶存取矩陣與角色定義

## 步驟

### 步驟一：評估當前 ALCOA+ 態勢

對每系統依 ALCOA+ 各原則評之：

```markdown
# Data Integrity Assessment
## Document ID: DIA-[SITE]-[YYYY]-[NNN]

### ALCOA+ Assessment Matrix

| Principle | Definition | Assessment Questions | System 1 | System 2 |
|-----------|-----------|---------------------|----------|----------|
| **Attributable** | Who performed the action and when? | Are all entries linked to unique user IDs? Is the timestamp system-generated? | G/A/R | G/A/R |
| **Legible** | Can data be read and understood? | Are records readable throughout retention period? Are formats controlled? | G/A/R | G/A/R |
| **Contemporaneous** | Was data recorded at the time of the activity? | Are timestamps real-time? Are backdated entries detectable? | G/A/R | G/A/R |
| **Original** | Is this the first-captured data? | Are original records preserved? Is there a clear original vs copy distinction? | G/A/R | G/A/R |
| **Accurate** | Is the data correct and truthful? | Are calculations verified? Are transcription errors detectable? | G/A/R | G/A/R |
| **Complete** | Is all data present? | Are deletions detectable? Are all expected records present? | G/A/R | G/A/R |
| **Consistent** | Are data elements consistent across records? | Do timestamps follow logical sequence? Are versions consistent? | G/A/R | G/A/R |
| **Enduring** | Will data survive for the required retention period? | Is the storage medium reliable? Are backups verified? | G/A/R | G/A/R |
| **Available** | Can data be accessed when needed? | Are retrieval procedures documented? Are access controls appropriate? | G/A/R | G/A/R |

Rating: G = Good (controls adequate), A = Adequate (minor improvements needed), R = Remediation required
```

**預期：** 每系統皆有評級之 ALCOA+ 評估，且各原則皆有具體發現。
**失敗時：** 若某系統不可評估（如無審計追蹤能力），標之為關鍵缺口，需即刻補正。

### 步驟二：設計偵測性管制

定義偵測資料完整性違規之監測活動：

```markdown
# Detective Controls Design
## Document ID: DCD-[SITE]-[YYYY]-[NNN]

### Audit Trail Review Schedule
| System | Review Type | Frequency | Reviewer | Scope |
|--------|-----------|-----------|----------|-------|
| LIMS | Comprehensive | Monthly | QA | All data modifications, deletions, and access events |
| ERP | Targeted | Weekly | QA | Batch record modifications and approvals |
| R/Shiny | Comprehensive | Per analysis | Statistician | All input/output/parameter changes |

### Review Checklist
For each audit trail review cycle:
- [ ] All data modifications have documented justification
- [ ] No unexplained deletions or void entries
- [ ] Timestamps are sequential and consistent with business operations
- [ ] No off-hours activity without documented justification
- [ ] No shared account usage detected
- [ ] Failed login attempts are within normal thresholds
- [ ] No privilege escalation events outside change control
```

**預期：** 偵測性管制有排程、有指派，並有明確檢視標準之記錄。
**失敗時：** 若審計追蹤檢視未按時執行，記錄缺口並上呈 QA 管理層。錯過之檢視累積風險。

### 步驟三：定義異常偵測模式

建立可觸發調查之具體模式：

```markdown
# Anomaly Detection Patterns

### Pattern 1: Off-Hours Activity
**Trigger:** Data creation, modification, or deletion outside business hours (defined as [06:00-20:00 local time, Monday-Friday])
**Threshold:** Any GxP-critical data modification outside defined hours
**Response:** Verify with user and supervisor within 2 business days
**Exceptions:** Documented shift work, approved overtime, automated processes

### Pattern 2: Sequential Modifications
**Trigger:** Multiple modifications to the same record within a short timeframe
**Threshold:** >3 modifications to the same record within 60 minutes
**Response:** Review modification reasons; verify each change has documented justification
**Exceptions:** Initial data entry corrections within [grace period, e.g., 30 minutes]

### Pattern 3: Bulk Changes
**Trigger:** Unusually high volume of data modifications by a single user
**Threshold:** >50 modifications per user per day (baseline: [calculate from normal usage])
**Response:** Verify business justification for bulk activity
**Exceptions:** Documented batch operations, data migration activities under change control

### Pattern 4: Delete/Void Spikes
**Trigger:** Unusual number of record deletions or voidings
**Threshold:** >5 delete/void events per user per week
**Response:** Immediate QA review of deleted/voided records
**Exceptions:** None — all delete/void events require documented justification

### Pattern 5: Privilege Escalation
**Trigger:** User access changes granting administrative or elevated privileges
**Threshold:** Any privilege change outside the user access management SOP
**Response:** Verify with IT security and system owner within 24 hours
**Exceptions:** Emergency access per documented emergency access procedure

### Pattern 6: Audit Trail Gaps
**Trigger:** Missing or interrupted audit trail entries
**Threshold:** Any gap > 0 entries (audit trail should be continuous)
**Response:** Immediate investigation — potential system malfunction or tampering
**Exceptions:** None — audit trail gaps are always critical
```

**預期：** 模式具體、可量、可行，並有所定之閾值與回應程序。
**失敗時：** 若閾值過低（誤報過多），依基線資料調整。若過高（漏失真實問題），於首監測週期後縮緊。

### 步驟四：建立指標儀表板

```markdown
# Data Integrity Metrics Dashboard
## Document ID: DIMD-[SITE]-[YYYY]-[NNN]

### Key Performance Indicators

| KPI | Metric | Target | Yellow Threshold | Red Threshold | Source |
|-----|--------|--------|-----------------|---------------|--------|
| DI-01 | Audit trail review completion rate | 100% | <95% | <90% | Review log |
| DI-02 | Anomalies detected per month | Trending down | >10% increase MoM | >25% increase MoM | Anomaly log |
| DI-03 | Anomaly investigation closure rate | <15 business days | >15 days | >30 days | Investigation log |
| DI-04 | Open data integrity CAPAs | 0 overdue | 1-2 overdue | >2 overdue | CAPA tracker |
| DI-05 | Shared account instances detected | 0 | 1-2 | >2 | Access review |
| DI-06 | Unauthorised access attempts | <5/month | 5-10/month | >10/month | System logs |
| DI-07 | Audit trail gap events | 0 | N/A | >0 (always red) | System monitoring |

### Reporting Cadence
| Report | Frequency | Audience | Owner |
|--------|-----------|----------|-------|
| DI Metrics Summary | Monthly | QA Director, System Owners | QA Analyst |
| DI Trend Report | Quarterly | Quality Council | QA Manager |
| DI Annual Review | Annual | Site Director | QA Director |
```

**預期：** 儀表板提供一目了然之合規狀態，附明確之上呈觸發。
**失敗時：** 若資料來源不能支持自動化指標，先行人工蒐集，並記錄自動化計劃。

### 步驟五：建立調查觸發與上呈

```markdown
# Investigation and Escalation Matrix

### Investigation Triggers
| Trigger | Severity | Response Time | Investigator |
|---------|----------|---------------|-------------|
| Audit trail gap detected | Critical | Immediate (within 4 hours) | IT + QA |
| Confirmed data falsification | Critical | Immediate (within 4 hours) | QA Director |
| Anomaly pattern confirmed after review | Major | Within 5 business days | QA Analyst |
| Repeated anomalies from same user | Major | Within 5 business days | QA + HR |
| Overdue audit trail review | Minor | Within 10 business days | QA Manager |

### Escalation Path
| Level | Escalated To | When |
|-------|-------------|------|
| 1 | System Owner | Any confirmed anomaly |
| 2 | QA Director | Major or critical finding |
| 3 | Site Director | Critical finding or potential regulatory impact |
| 4 | Regulatory Affairs | Confirmed data integrity failure requiring regulatory notification |
```

**預期：** 每樁調查皆有定之嚴重度、時程與上呈路徑。
**失敗時：** 若調查未於所定時程內完成，上呈下一層級。

### 步驟六：彙編監測計劃

將諸組件合為主資料完整性監測計劃：

```markdown
# Data Integrity Monitoring Plan
## Document ID: DI-MONITORING-PLAN-[SITE]-[YYYY]-[NNN]

### 1. Purpose and Scope
[From assessment scope]

### 2. ALCOA+ Assessment Summary
[From Step 1]

### 3. Detective Controls
[From Step 2]

### 4. Anomaly Detection Rules
[From Step 3]

### 5. Metrics and Reporting
[From Step 4]

### 6. Investigation and Escalation
[From Step 5]

### 7. Periodic Review
- Monitoring plan review: Annual
- Anomaly thresholds: Adjust after each quarterly review
- ALCOA+ re-assessment: When systems change or new systems are added

### 8. Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|
| QA Director | | | |
| IT Director | | | |
| Site Director | | | |
```

**預期：** 一份單一、已核准之文件，定義完整之資料完整性監測計劃。
**失敗時：** 若計劃過大，難容於單一文件，建立主計劃並引用各系統特定之監測程序。

## 驗證

- [ ] 對所有在範圍內之系統完成 ALCOA+ 評估
- [ ] 審計追蹤檢視排程已定，含頻率、範圍與責任檢視者
- [ ] 至少定義五種異常偵測模式，附具體閾值
- [ ] 指標儀表板有 KPI，附綠/黃/紅閾值
- [ ] 調查觸發已定，附嚴重度與回應時程
- [ ] 上呈矩陣於關鍵發現時可達法規事務
- [ ] 監測計劃經 QA 與 IT 領導層核准
- [ ] 已建立定期檢視之排程

## 常見陷阱

- **監測而不行動**：蒐集指標而從不調查異常，徒生虛假之安全感，較無監測更糟（反生「忽視發現」之證據）。
- **固定閾值**：基於猜測而非基線資料之閾值，產生過多誤報，導致告警疲勞。
- **審計追蹤檢視流於形式**：檢視審計追蹤而不知所求，無效。當訓練檢視者熟悉異常偵測模式。
- **忽略系統限制**：某些系統審計追蹤能力差。記錄限制並施以補償性管制，勿佯裝限制不存。
- **無趨勢分析**：個別異常或顯輕，然跨時或跨用戶之模式可揭系統性問題。資料完整性指標恆當趨勢化。

## 相關技能

- `design-compliance-architecture` — 識別需資料完整性監測之系統
- `implement-audit-trail` — 監測所賴之技術基礎
- `investigate-capa-root-cause` — 監測偵得需正式調查之問題時
- `conduct-gxp-audit` — 稽核評估監測計劃之有效性
- `prepare-inspection-readiness` — 資料完整性為法規檢查之主要焦點領域
