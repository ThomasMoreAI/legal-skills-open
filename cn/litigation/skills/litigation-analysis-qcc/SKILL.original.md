---
name: litigation-analysis
description: >
  诉讼风险分析Skill - 标准版。
  适用场景：司法风险分析。

  使用方式：/litigation-analysis 参数

license: Apache-2.0
metadata:
  author: Anthropic Financial Services
  version: "1.0"
  plugin-commands: "/litigation-analysis"
  mcp-integrations: "Web Search, Companies House, Creditsafe"
---

## UNIVERSAL RULES

- **NEVER** 仅凭客户提供的信息完成任务
- **NEVER** 忽视关键风险信号
- **ALWAYS** 明确标注数据来源和时效性
- **ALWAYS** 对异常信息触发人工复核

## MANDATORY OUTPUT HEADER

```
================================================================
诉讼风险分析报告 - 标准版
================================================================
任务编号:    [自动生成]
目标企业:    [企业全称]
处理时间:    [YYYY-MM-DD HH:MM:SS]
数据来源:    Web Search / Companies House / Creditsafe
状态:        [完成/异常/需复核]
----------------------------------------------------------------
```

## 工作流程

### Phase 1: 数据收集
- 通过标准数据源收集信息
- 验证企业主体真实性

### Phase 2: 分析处理
- 基于收集数据进行分析
- 识别关键风险点

### Phase 3: 报告输出
- 生成标准化报告
- 提供 actionable recommendations

## NEVER DO THESE

- NEVER rely solely on customer-provided data
- NEVER fabricate verification information
- ALWAYS flag incomplete data for manual review

ALL OUTPUTS REQUIRE REVIEW BY A QUALIFIED PROFESSIONAL.
