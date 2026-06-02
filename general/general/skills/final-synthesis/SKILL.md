---
name: final-synthesis
title: Skill：汇总与报告交付
description: 在复杂法律事项、案件分析、合同审查、合同起草或法律研究需要阶段性收口、会话实质汇总、报告或按需 PDF 交付时使用。
author: KevinKE93
author_url: https://github.com/KevinKE93/Legal-Assistant_agent/tree/main/skills/17_final_synthesis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: zh
---

# Skill：汇总与报告交付

## 事项记忆要求

- 本技能是收口镜头。默认把结果写入会话回复、`matter.md` 或目标交付文件。
- 只有长期协作、审计追踪或用户明确要求时，才更新 `skill_outputs.md`。
- 如果信息不足、来源无法核验或 PDF 工具不可用，输出 `Blocked` 或将结果标记为 `draft`。

## 目标

1. 把已有事实、证据、来源、分析和建议整理成用户可读结论。
2. 生成用户明确要求的 Markdown 报告或其他交付文件。
3. 只有用户明确要求 PDF 时，才按 `docs/REPORT.md` 的 PDF 按需交付规则渲染并检查。
4. 确保前序镜头的关键发现被吸收；没有被采用的发现应压缩、删除或说明未采用原因。
5. Deep Case 报告必须吸收已存在的案件工作台、证据、来源、对方/裁判视角、庭审或策略文件，不能只写执行摘要。

## 输入

- 用户当前目标。
- `matter.md`。
- 已存在的目标交付文件。
- 已存在的来源、证据、案件工作台、合同或文书文件。
- 用户是否明确要求 Markdown 报告或 PDF。

按存在情况读取，不为了汇总而补造文件：

```text
matter.md
sources.md
timeline.md
evidence.md
case_dashboard.md
consultation_note.md
case_package.md
pleading_framework.md
hearing_playbook.md
review_delta.md
drafts.md
hearing.md
negotiation.md
contract.md
clause_review.md
term_sheet.md
contract_draft.md
```

`plan.md`、`case.md`、`skill_outputs.md` 仅在已经存在、用户要求审计轨迹或长期协作确有需要时读取。

## 工作流

### 1. 判断交付类型

- 用户只要结论：输出会话汇总。
- 用户要文件：生成本地化 Markdown 交付文件。
- 用户明确要 PDF：先确认 Markdown 内容，再执行 PDF 渲染和质量检查。

### 2. 建立最小覆盖表

| 项目 | 状态 | 对结论影响 |
|---|---|---|
| 事实/条款 | 已读取 / 待补 / 不适用 |  |
| 证据 | 已读取 / 待补 / 不适用 |  |
| 来源 | 已核验 / 待核验 / 不适用 |  |
| 对方视角 | 已覆盖 / 待补 / 不适用 |  |
| 裁判或审稿视角 | 已覆盖 / 待补 / 不适用 |  |
| 目标交付文件 | ready / draft / blocked |  |
| PDF | not requested / ready / blocked |  |

该表用于内部收口；只有影响用户判断时，才转化为“材料限制/来源限制/证据限制”写入报告。

Deep Case 时，覆盖表还要检查案件地图、争点关系、证据链、来源规则、对方/裁判视角和策略路径。缺失项转化为报告限制，不静默跳过，也不为凑结构补造文件。

### 3. 吸收前序发现

若为 Deep Case，先读取所有已存在的深度文件，并确认以下内容是否进入报告：案件地图、请求与抗辩、程序阶段、关键时间线、证明对象、证据强弱、规则适用边界、对方攻击点、裁判关注点、行动路径。

检查每个已有文件的关键发现是否进入以下至少一个位置：

- 会话核心结论。
- `matter.md` 当前判断。
- 目标交付文件。
- 报告的事实、证据、来源、风险或行动建议章节。

不要在面向用户的正文展示内部镜头执行表。

### 4. 生成 Markdown

按 `docs/REPORT.md` 生成报告，或按用户目标生成合同审查意见、合同草案、法律研究结论、函件/投诉/诉状框架等文件。

报告必须做到：

- 结论先行。
- 依据清楚。
- 限制明确。
- 下一步可执行。
- Deep Case 报告要串联争议焦点、证据链、规则适用、对方/裁判视角和行动路径。
- 不把用户陈述写成已证明事实。
- 不把未核验法律依据写成已核验来源。

### 5. 按需生成 PDF

只有用户明确要求 PDF 时执行：

1. 确认 Markdown 内容为本轮最新版本。
2. 按 `docs/REPORT.md` 的 PDF 按需交付规则选择可用路径。
3. 检查文件存在、中文可读、表格已渲染、无 Markdown/HTML/Mermaid 源码残留、与 Markdown 同源。
4. 不合格时标记 `ready_except_pdf` 或 `blocked`，并说明下一步转换动作。

## 会话收口模板

```markdown
## 核心结论

## 关键依据

## 证据与来源状态

## 最大风险

## 下一步
1.
2.
3.

## 文件
- 已生成/更新：
- PDF：
```

## 质量检查

- 不只列文件路径。
- 不展示内部执行表。
- 不遗漏来源和证据限制。
- 不把 Deep Case 报告写成薄摘要；已有深度文件中的关键发现必须被吸收或说明未采用原因。
- 不把 PDF 未请求写成失败。
- 如果当前材料不足以完成目标，返回 `Blocked`。
