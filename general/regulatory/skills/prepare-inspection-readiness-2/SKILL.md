---
name: prepare-inspection-readiness-2
title: 備檢查就緒
description: 備組織受監管檢查：對機構特定焦點區（FDA, EMA, MHRA）評備度。含警告信 與 483 主題析、模擬檢查協、文件包備、檢查事務、應對模板。 監管檢查已宣或預期、定期自評、上檢後已施新系、或重大審計發現或致監管注時用之。
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/wenyan/skills/prepare-inspection-readiness
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: zh
---

# 備檢查就緒

評並進組織受監管檢查之備度，含文件、人員備、事務、應對謀。

## 用時

- 監管檢查已宣或預期
- 定期檢查就緒自評
- 上檢以來已施新系或新程
- 業界趨（警告信、483）示新焦點區
- 重大審計發現或致監管注

## 入

- **必要**：檢查機構（FDA、EMA、MHRA、或他）
- **必要**：預期檢查範（數據完整、CSV、GMP、GLP、GCP）
- **必要**：合規架構與系庫
- **可選**：往檢報與觀察
- **可選**：近業界警告信與 483 主題
- **可選**：開放 CAPA 與審計發現

## 法

### 第一步：析機構特定焦點區

研檢查機構當前優先：

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

得：附險評之檢查焦點區析，限於檢機構。
敗則：若近 483/警告信數不可得，諮 FDA 警告信庫、EMA 檢報、業界刊以得最近趨。

### 第二步：行就緒自評

對各焦點區評廠：

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

得：量化之就緒評，附分優之補救動。
敗則：若總就緒於 70% 下，考請延檢（若許）並施緊急補救。

### 第三步：備文件包

理文件為檢查就緒之包：

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

得：諸包皆備、索、可於檢者請後 30 分內取。
敗則：若文缺或不全，立缺列、分優補救、記謀。檢者察雜亂。

### 第四步：設模擬檢查協

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

得：模擬檢查於實檢前揭問題。
敗則：若模擬檢揭關鍵缺，當實檢觀察之急視之。

### 第五步：謀檢查事務

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

得：事務謀確專業、有序之檢查應對。
敗則：若關鍵人於檢日不可得，識並簡介替代。

### 第六步：立應對模板

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

得：應對模板使對檢查觀察之速、結構化回。
敗則：若應對模板通用而不對特定觀察，依特定證與時程定制各應對。

## 驗

- [ ] 機構特定焦點區已析附險評
- [ ] 就緒自評已完附量化分
- [ ] 諸缺有補救謀附主與期
- [ ] 諸範系之文件包已備並索
- [ ] 模擬檢查已行附記發現與隨訪
- [ ] 檢查事務謀定室、角、通信協
- [ ] 常見觀察型之應對模板已備
- [ ] 諸關鍵補救項於檢日前已閉

## 陷

- **末刻備**：檢查就緒為續程，非臨時抱佛腳。倉促之組產雜亂、不全之應。
- **匿問題**：檢者經驗豐能察隱。透明附明補救謀勝匿。
- **過自願訊**：答所問。供未求之訊或開新查線。
- **未訓人員**：未練應檢者問之專家表現劣。模擬檢為要練。
- **忽後室**：後室（文件取回與策協）與前室同要。劣文件取造雜亂之印。

## 參

- `design-compliance-architecture` — 檢者欲見之基文
- `conduct-gxp-audit` — 內審當仿檢方法
- `monitor-data-integrity` — 數據完整為 FDA 檢之首焦
- `investigate-capa-root-cause` — CAPA 必檢前徹查
- `qualify-vendor` — 廠商資質檢時常請
