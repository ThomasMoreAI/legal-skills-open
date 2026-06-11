---
name: write-validation-documentation
title: 書驗文
description: Write IQ/OQ/PQ validation documentation for computerized systems in regulated environments. Covers protocols, reports, test scripts, deviation handling, and approval workflows. Use when validating R or other software for regulated use, preparing for a regulatory audit, documenting qualification of computing environments, or creating and updating validation protocols and reports for new or re-qualified systems.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/wenyan-ultra/skills/write-validation-documentation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: life-sciences
language: zh
---

# 書驗文

立計算系之全 IQ/OQ/PQ 驗文。

## 用

- 為管用驗 R 或他軟→用
- 備管審→用
- 錄計境之資→用
- 新或重資系建更驗綱與報→用

## 入

- **必**：欲驗系/軟（名、版、用）
- **必**：定範與策之驗計
- **必**：用要規
- **可**：現 SOP 模
- **可**：前驗文（重資）

## 行

### 一：書 IQ 綱

```markdown
# Installation Qualification Protocol
**System**: R Statistical Computing Environment
**Version**: 4.5.0
**Document ID**: IQ-PROJ-001
**Prepared by**: [Name] | **Date**: [Date]
**Reviewed by**: [Name] | **Date**: [Date]
**Approved by**: [Name] | **Date**: [Date]

## 1. Objective
Verify that R and required packages are correctly installed per specifications.

## 2. Prerequisites
- [ ] Server/workstation meets hardware requirements
- [ ] Operating system qualified
- [ ] Network access available (for package downloads)

## 3. Test Cases

### IQ-001: R Installation
| Field | Value |
|-------|-------|
| Requirement | R version 4.5.0 correctly installed |
| Procedure | Open R console, execute `R.version.string` |
| Expected Result | "R version 4.5.0 (2025-04-11)" |
| Actual Result | ______________________ |
| Pass/Fail | [ ] |
| Executed by | ____________ Date: ________ |

### IQ-002: Package Inventory
| Package | Required Version | Installed Version | Pass/Fail |
|---------|-----------------|-------------------|-----------|
| dplyr | 1.1.4 | | [ ] |
| ggplot2 | 3.5.0 | | [ ] |
| survival | 3.7-0 | | [ ] |

## 4. Deviations
[Document any deviations from expected results and their resolution]

## 5. Conclusion
[ ] All IQ tests PASSED - system installation verified
[ ] IQ tests FAILED - see deviation section
```

得：`validation/iq/iq_protocol.md` 完含獨文 ID、意、前置察清、R 裝與每須包之試例、偏節、批欄。

敗：機構要異式→改模合現 SOP。關欄（要、程、期果、實果、過/敗）必保。

### 二：書 OQ 綱

```markdown
# Operational Qualification Protocol
**Document ID**: OQ-PROJ-001

## 1. Objective
Verify that the system operates correctly under normal conditions.

## 2. Test Cases

### OQ-001: Data Import Functionality
| Field | Value |
|-------|-------|
| Requirement | System correctly imports CSV files |
| Test Data | validation/test_data/import_test.csv (MD5: abc123) |
| Procedure | Execute `read.csv("import_test.csv")` |
| Expected | Data frame with 100 rows, 5 columns |
| Actual Result | ______________________ |
| Evidence | Screenshot/log file reference |

### OQ-002: Statistical Calculations
| Field | Value |
|-------|-------|
| Requirement | t-test produces correct results |
| Test Data | Known dataset: x = c(2.1, 2.5, 2.3), y = c(3.1, 3.5, 3.3) |
| Procedure | Execute `t.test(x, y)` |
| Expected | t = -5.000, df = 4, p = 0.00753 |
| Actual Result | ______________________ |
| Tolerance | ±0.001 |

### OQ-003: Error Handling
| Field | Value |
|-------|-------|
| Requirement | System handles invalid input gracefully |
| Procedure | Execute `analysis_function(invalid_input)` |
| Expected | Informative error message, no crash |
| Actual Result | ______________________ |
```

得：`validation/oq/oq_protocol.md` 含數入、統算、誤處之試例，各附特試數、期果（應時附容差）、證要。

敗：試數未備→建合性試數附已知性。錄數生法以使果可獨驗。

### 三：書 PQ 綱

```markdown
# Performance Qualification Protocol
**Document ID**: PQ-PROJ-001

## 1. Objective
Verify the system performs as intended with real-world data and workflows.

## 2. Test Cases

### PQ-001: End-to-End Primary Analysis
| Field | Value |
|-------|-------|
| Requirement | Primary endpoint analysis matches reference |
| Test Data | Blinded test dataset (hash: sha256:abc...) |
| Reference | Independent SAS calculation (report ref: SAS-001) |
| Procedure | Execute full analysis pipeline |
| Expected | Estimate within ±0.001 of reference |
| Actual Result | ______________________ |

### PQ-002: Report Generation
| Field | Value |
|-------|-------|
| Requirement | Generated report contains all required sections |
| Procedure | Execute report generation script |
| Checklist | |
| | [ ] Title page with study information |
| | [ ] Table of contents |
| | [ ] Demographic summary table |
| | [ ] Primary analysis results |
| | [ ] Appendix with session info |
```

得：`validation/pq/pq_protocol.md` 含端到端試例用實（或代）數，果對獨參算（如 SAS 出）較。容差明定。

敗：獨參果未備→錄隙、用雙編（二獨 R 實）為替驗法。標 PQ 為暫至獨驗畢。

### 四：書資報

行綱後，錄果：

```markdown
# Installation Qualification Report
**Document ID**: IQ-RPT-001
**Protocol Reference**: IQ-PROJ-001

## 1. Summary
All IQ test cases were executed on [date] by [name].

## 2. Results Summary
| Test ID | Description | Result |
|---------|-------------|--------|
| IQ-001 | R Installation | PASS |
| IQ-002 | Package Inventory | PASS |

## 3. Deviations
None observed.

## 4. Conclusion
The installation of R 4.5.0 and associated packages has been verified
and meets all specified requirements.

## 5. Approvals
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Executor | | | |
| Reviewer | | | |
| Approver | | | |
```

得：資報（IQ、OQ、PQ）完附諸試果填、偏錄（或「無」）、結述、批簽欄待簽。

敗：行中試敗→各敗錄為偏附根因析與解。觀敗時偏節勿空。

### 五：可處自動

建生證之自動試本：

```r
# validation/scripts/run_iq.R
sink("validation/iq/iq_evidence.txt")
cat("IQ Execution Date:", format(Sys.time()), "\n\n")

cat("IQ-001: R Version\n")
cat("Result:", R.version.string, "\n")
cat("Status:", ifelse(R.version$major == "4" && R.version$minor == "5.0",
                      "PASS", "FAIL"), "\n\n")

cat("IQ-002: Package Versions\n")
required <- renv::dependencies()
installed <- installed.packages()
# ... comparison logic
sink()
```

得：`validation/scripts/` 中自動本生證檔（如 `iq_evidence.txt`）附時戳果於每試例，減手入確可重。

敗：自動本因境異敗→手行並以 `sink()` 捕出。資報中錄自動與手行間異。

## 驗

- [ ] 諸綱有獨文 ID
- [ ] 綱參驗計
- [ ] 試例有清過/敗標
- [ ] 報含諸行試果
- [ ] 偏錄附解
- [ ] 批簽得
- [ ] 文從機構 SOP 模

## 忌

- **受標含混**：「系為正」非可試。明特期值
- **缺證**：每試果須支證（截、日、出檔）
- **偏處不全**：諸敗須錄、究、解
- **文無版控**：驗文如碼須變控
- **略重資**：系更（R 版、包更）須重資評

## 參

- `setup-gxp-r-project` - 驗境之案構
- `implement-audit-trail` - 電記跡
- `validate-statistical-output` - 出驗法
