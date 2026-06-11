---
name: prepare-inspection-readiness-pjt222
title: 備檢準備度
description: Prepare an organisation for regulatory inspection by assessing readiness against agency-specific focus areas (FDA, EMA, MHRA). Covers warning letter and 483 theme analysis, mock inspection protocols, document bundle preparation, inspection logistics, and response template creation. Use when a regulatory inspection has been announced or is anticipated, when a periodic self-assessment is due, when new systems have been implemented since the last inspection, or after a significant audit finding that may attract regulatory attention.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/wenyan-lite/skills/prepare-inspection-readiness
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: life-sciences
language: zh
---

# 備檢準備度

評估並提升組織迎檢之準備度，含文件、人員、行政與回應規劃。

## 適用時機

- 法規檢查已通報或可預見
- 屆定期之自我評估
- 自上次檢查以來實施了新系統或新流程
- 業界趨勢（警告函、483）顯示新焦點區
- 重大稽核發現後，恐引法規關注

## 輸入

- **必要**：執行檢查之機關（FDA、EMA、MHRA 或他）
- **必要**：預期檢查範圍（資料完整性、CSV、GMP、GLP、GCP）
- **必要**：合規架構與系統清冊
- **選擇性**：先前檢查報告與觀察項
- **選擇性**：近期業界警告函與 483 主題
- **選擇性**：未結 CAPA 與稽核發現

## 步驟

### 步驟一：分析機關特定之焦點區

研究檢查機關當前之優先順序：

```markdown
# Inspection Focus Area Analysis
## Document ID: IFA-[SITE]-[YYYY]-[NNN]

### FDA Current Focus Areas
| Focus Area | Regulatory Basis | Recent 483 Trends | Risk to This Site |
|-----------|-----------------|-------------------|-------------------|
| Data integrity | 21 CFR Part 11, CGMP | #1 cited observation in drug 483s since 2016 | [H/M/L] |
| Audit trail | 21 CFR 11.10(e) | Disabled/incomplete audit trails | [H/M/L] |
| Electronic signatures | 21 CFR 11.50-11.300 | Missing manifestation, shared accounts | [H/M/L] |
| Computer system validation | GAMP 5, FDA guidance | Inadequate validation of Category 4/5 systems | [H/M/L] |
| Change control | ICH Q10 | Undocumented or retrospective changes | [H/M/L] |
| Laboratory controls | 21 CFR 211.160-211.176 | OOS investigation, test repetition | [H/M/L] |

### EMA/MHRA-Specific Considerations
| Area | EU Annex 11 Reference | Focus | Risk to This Site |
|------|----------------------|-------|-------------------|
| Computerized system validation | §4, §5 | Risk-based validation, supplier assessment | [H/M/L] |
| Operational phase | §6-§13 | Security, audit trail, backup, business continuity | [H/M/L] |
| Cloud and outsourced systems | §3.4 | Service level agreements, data sovereignty | [H/M/L] |
| Data governance | MHRA DI guidance | ALCOA+, culture of integrity | [H/M/L] |
```

**預期：** 一份依機關之檢查焦點區之風險評等分析。
**失敗時：** 若無近期 483／警告函資料，查 FDA 警告函資料庫、EMA 檢查報告或業界刊物以取最新趨勢。

### 步驟二：執行準備度自評

依各焦點區評估場域：

```markdown
# Inspection Readiness Assessment
## Document ID: IRA-[SITE]-[YYYY]-[NNN]

### Readiness Scoring
| Focus Area | Weight | Current State | Score (1-5) | Gap | Remediation Priority |
|-----------|--------|--------------|-------------|-----|---------------------|
| Data integrity controls | High | [Description of current state] | [1-5] | [Gap description] | [Critical/High/Medium/Low] |
| Validation documentation | High | [Description] | [1-5] | [Gap] | [Priority] |
| Audit trail compliance | High | [Description] | [1-5] | [Gap] | [Priority] |
| Electronic signatures | Medium | [Description] | [1-5] | [Gap] | [Priority] |
| Change control | Medium | [Description] | [1-5] | [Gap] | [Priority] |
| Training records | Medium | [Description] | [1-5] | [Gap] | [Priority] |
| SOPs (current, approved) | Medium | [Description] | [1-5] | [Gap] | [Priority] |
| CAPA management | Medium | [Description] | [1-5] | [Gap] | [Priority] |
| Vendor qualification | Low | [Description] | [1-5] | [Gap] | [Priority] |
| Periodic review | Low | [Description] | [1-5] | [Gap] | [Priority] |

Score: 1 = Critical gaps, 5 = Fully compliant
Overall readiness score: [Sum / Max] = [X]%

### Remediation Plan
| Gap ID | Description | Owner | Action | Deadline | Status |
|--------|------------|-------|--------|----------|--------|
| GAP-001 | [Gap] | [Name] | [Remediation action] | [Date] | [Open/In Progress/Closed] |
```

**預期：** 一份量化之準備度評估，附排序之修補行動。
**失敗時：** 若整體準備度低於 70%，考慮申請延期（若准許）並施緊急修補。

### 步驟三：備齊文件包

將文件組為迎檢可用之套：

```markdown
# Inspection Document Bundles

### Bundle 1: Validation Pack (per system)
- [ ] Current validation status summary (one-page per system)
- [ ] User Requirements Specification (URS)
- [ ] Risk Assessment
- [ ] Validation Plan
- [ ] IQ Protocol and Report
- [ ] OQ Protocol and Report
- [ ] PQ Protocol and Report (if applicable)
- [ ] Traceability Matrix
- [ ] Validation Summary Report
- [ ] Periodic review records
- [ ] Change control history since last validation

### Bundle 2: Data Integrity Evidence
- [ ] Data integrity policy and programme
- [ ] ALCOA+ assessment results
- [ ] Audit trail review records (last 12 months)
- [ ] Data integrity monitoring metrics and trends
- [ ] Data integrity training records

### Bundle 3: Operational Evidence
- [ ] Current SOPs (master list with effective dates)
- [ ] Training matrix (all GxP personnel)
- [ ] Change control log (last 24 months)
- [ ] Deviation/incident log (last 24 months)
- [ ] CAPA log with closure status
- [ ] Internal audit reports and CAPA follow-up

### Bundle 4: System Configuration Evidence
- [ ] User access list (current active users with roles)
- [ ] System configuration documentation
- [ ] Backup and recovery test records
- [ ] Security patch log
- [ ] Business continuity/disaster recovery plan
```

**預期：** 各包皆已組裝、編索引，並可於檢查官請求之 30 分鐘內取得。
**失敗時：** 若文件缺漏不齊，作缺項清單、排序修補並記錄計畫。檢查官會察覺凌亂。

### 步驟四：設計模擬檢查方案

```markdown
# Mock Inspection Protocol
## Document ID: MIP-[SITE]-[YYYY]-[NNN]

### Scope
- **Focus areas:** [Top 3-5 risk areas from readiness assessment]
- **Systems in scope:** [Systems likely to be inspected]
- **Duration:** [1-2 days]

### Participants
| Role | Name | Mock Inspection Role |
|------|------|---------------------|
| Mock inspector | [Experienced QA or external consultant] | Ask questions, request documents |
| System owner(s) | [Names] | Respond to questions, demonstrate systems |
| QA | [Name] | Observe, note findings |
| Back room coordinator | [Name] | Locate and provide documents |

### Mock Inspection Scenarios
| Scenario | Focus | Inspector Might Ask |
|----------|-------|-------------------|
| 1: Show me the audit trail | Data integrity | "Show me the audit trail for batch record BR-2025-1234" |
| 2: Walk me through a change | Change control | "Show me the change control for the last system upgrade" |
| 3: Show training records | Training | "Show me the training records for user [Name] on system [X]" |
| 4: Explain your validation | CSV | "Walk me through how you validated this system" |
| 5: Show a deviation | CAPA | "Show me your last critical deviation and its CAPA" |
| 6: User access review | Access control | "Show me how you manage user access when people leave" |

### Post-Mock Assessment
| Scenario | Outcome | Findings | Actions |
|----------|---------|----------|---------|
| [#] | [Satisfactory/Needs Work] | [Description] | [Remediation if needed] |
```

**預期：** 模擬檢查在實檢之前先揭出問題。
**失敗時：** 若模擬檢查揭出關鍵缺失，以實檢觀察項之同等急迫性處理。

### 步驟五：規劃檢查行政事務

```markdown
# Inspection Logistics Plan

### Room Setup
| Room | Purpose | Equipment | Assigned To |
|------|---------|-----------|-------------|
| Front room | Inspector workspace | Table, chairs, network access, printer | Facility manager |
| Back room | Document retrieval and strategy | Copier, network access, phone | QA team |
| Demo room | System demonstrations | Workstation with system access | IT support |

### Roles During Inspection
| Role | Person | Responsibilities |
|------|--------|-----------------|
| Inspection coordinator | [Name] | Single point of contact with inspector, schedule management |
| Subject matter experts | [Names] | Answer technical questions in their domain |
| Back room lead | [Name] | Coordinate document retrieval, track requests |
| Scribe | [Name] | Document all questions, requests, and responses |
| Executive sponsor | [Name] | Available for escalation, opening/closing meetings |

### Communication Protocol
- All document requests flow through the back room lead
- No documents provided without QA review
- Questions requiring research get a "we will get back to you" response (track and follow up)
- Daily debrief with inspection team after each day
```

**預期：** 行政計畫確保對檢查之專業、有序回應。
**失敗時：** 若關鍵人員於檢查日不在，辨明並簡報替補者。

### 步驟六：建立回應模板

```markdown
# Inspection Response Templates

### Template 1: 483 Observation Response
[Date]
[FDA District Office Address]

Re: FDA Form 483 Observations — [Inspection Dates] — [Facility Name]

Dear [Inspector Name],

We appreciate the opportunity to address the observations identified during the inspection of [facility] on [dates].

**Observation [N]:** [Quote the exact observation text]

**Response:**
- **Root Cause:** [Brief root cause description]
- **Immediate Corrective Action:** [What was done immediately]
  - Completed: [Date]
- **Long-term Corrective Action:** [Systemic fix]
  - Target completion: [Date]
- **Preventive Action:** [How recurrence will be prevented]
  - Target completion: [Date]
- **Effectiveness Verification:** [How effectiveness will be measured]
  - Target verification date: [Date]

### Template 2: Immediate Correction During Inspection
When an inspector identifies an issue that can be corrected immediately:
1. Acknowledge the observation
2. Implement the correction (if feasible)
3. Document the correction with before/after evidence
4. Inform the inspector that the correction has been made
5. Include in the formal response as "corrected during inspection"
```

**預期：** 回應模板使對檢查觀察項之答覆迅速且有結構。
**失敗時：** 若模板過於通用而未對應具體觀察項，依各觀察項以具體證據與時程客製化。

## 驗證

- [ ] 已分析機關特定焦點區並評風險
- [ ] 已完成自評並量化分數
- [ ] 已對所有缺口建修補計畫，附負責人與期限
- [ ] 已為所有範圍內系統組裝並索引文件包
- [ ] 已執行模擬檢查並記錄發現與後續
- [ ] 行政計畫已界定房間、角色與溝通協定
- [ ] 已為常見觀察類型備回應模板
- [ ] 所有關鍵修補項已於檢查日前結案

## 常見陷阱

- **臨時抱佛腳**：迎檢之準備為持續性方案，非考前衝刺。倉促組織產出之回應雜亂不全。
- **隱瞞問題**：檢查官為老練專業，能察隱瞞。透明加清晰修補計畫，永優於試圖隱瞞。
- **多嘴**：只答所問。未經請求而提供之資訊可能開新詢問線。
- **未訓練人員**：未練過回答檢查官之 SME 表現不佳。模擬檢查為必要之練習。
- **忽視後台**：後台（文件取得與策略協調）與前台同等重要。文件取得不力會給人雜亂之印象。

## 相關技能

- `design-compliance-architecture` —— 檢查官想看之基礎文件
- `conduct-gxp-audit` —— 內稽應仿檢查方法
- `monitor-data-integrity` —— 資料完整性為 FDA 檢查首要焦點
- `investigate-capa-root-cause` —— CAPA 須於受檢前徹底調查
- `qualify-vendor` —— 受檢時常被要求提供供應商資格
