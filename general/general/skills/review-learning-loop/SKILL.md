---
name: review-learning-loop
title: Skill：复盘、事项记忆与迭代学习
description: 在新证据、新陈述、新合同版本、新程序节点、新报价或用户目标变化出现后，需要延续同一事项记忆并更新报告时使用。
author: KevinKE93
author_url: https://github.com/KevinKE93/Legal-Assistant_agent/tree/main/skills/14_review_learning_loop
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: zh
---

# Skill：复盘、事项记忆与迭代学习

## 事项记忆要求

- 本技能是复盘镜头。默认更新 `matter.md`、会话回复或受影响的目标文件。
- 只有长期协作、审计追踪或用户明确要求时，才更新 `skill_outputs.md`。
- 不从头重做；只更新受新信息影响的部分。

## 适用场景

出现新聊天记录、新证据、新合同版本、对方新说法、法院/仲裁员反馈、调解结果、庭审进展、和解报价、投诉反馈或用户目标变化后使用。

## 目标

1. 判断新信息是否属于同一事项。
2. 找出受影响的事实、条款、争议焦点、证明责任、证据强度、来源状态和策略。
3. 更新 `matter.md` 和受影响文件。
4. 必要时生成或更新 `review_delta.md`。
5. 用户已要求报告或 PDF 时，同步更新对应交付物。

## 输入

- 事项文件夹或当前 `matter.md`。
- 新增事实、证据、合同版本、对方表态、程序进展或用户目标变化。
- 已存在的交付文件。

## 工作流

### 1. 定位事项

优先复用已有事项文件夹。没有事项文件夹但需要持续记忆时，创建：

```text
work/<date>_<本地化事项名>/
```

并初始化 `matter.md`。不要为了复盘初始化 `plan.md`、`case.md` 或 `skill_outputs.md`。

### 2. 新旧对比

| 领域 | 旧判断 | 新信息 | 是否改变结论 | 下一步 |
|---|---|---|---|---|

重点检查：

- 原假设是否被证实或推翻。
- 风险是否升高。
- 证据缺口是否被补上或新增。
- 法律来源是否需要复核。
- 交付文件是否需要更新。

### 3. 更新最小文件

默认更新：

- `matter.md`：新增信息、变化判断、风险变化、下一步。

按需更新：

- `sources.md`：新信息影响法律依据、案例、期限或政策。
- `timeline.md` / `evidence.md`：新证据改变时间线或证明力。
- `contract.md` / `clause_review.md` / `contract_draft.md`：合同版本变化。
- `review_delta.md`：Deep Case、长期事项或报告更新需要说明新旧差异。
- 目标交付文件：用户已要求报告、文书、合同意见或 PDF。

## 输出格式

```markdown
## 复盘结论

## 新旧变化
| 领域 | 原判断 | 新信息 | 更新后判断 | 风险变化 |
|---|---|---|---|---|

## 受影响文件
- 已更新：
- 不需要更新：
- 待用户确认：

## 下一步
1.
2.
3.
```

## 质量检查

- 不保留已被推翻的假设。
- 不忽略新信息对风险和策略的影响。
- 不把聊天记录当作唯一记忆；需要持续时更新 `matter.md`。
- 若本轮变化影响用户可读结论，更新对应交付文件。
- 若用户已明确要求 PDF，Markdown 更新后必须重新渲染 PDF；不能沿用旧 PDF。
