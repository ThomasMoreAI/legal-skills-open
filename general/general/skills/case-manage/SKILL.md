---
name: case-manage
title: Case Manage
description: 用户用自然语言提供一个或多个案件的基本信息，需要新增案件记录、更新案件字段、查询待办或管理提醒时，优先匹配 case-manage；/案件录入、/case-manage、/案件更新 或 /case-update 仅作为强制入口。
author: Clukay-Fun
author_url: https://github.com/Clukay-Fun/feishu-opencode-bridge/tree/main/.opencode/skills/case-manage
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: zh
---

# Case Manage

当用户要把一个或多个案件信息写入或更新到飞书多维表时，优先走这条专项 skill。

当前运行时支持 `Skill Intent Router + Material Context`：

- 新增案件可以直接用自然语言说明案件信息，不必先输入 `/案件录入`。
- 单个案件直接进入单条案件整理链路；多个案件应先拆分为案件清单，再逐条复用同一套解析、写表和结果卡片。
- `/案件录入` / `/case-manage` 保留为强制新增入口。
- `/案件更新` / `/case-update` 保留为强制更新入口。
- 自然语言触发和 slash command 触发必须进入同一套卡片生命周期：案件整理进行中、完成或失败。
- 查询待办和提醒仍建议使用明确入口，避免把普通案件讨论误判为写表动作。

运行时 prompt 覆盖文件：

- `references/create-prompt.txt`
- `references/update-prompt.txt`

## 使用方式

新增案件自然语言可直接触发，例如：

```text
新增一个案件：张三和北京XX科技劳动争议，仲裁阶段，承办律师刘达律师
录入案件，委托人李四，对方杭州XX公司，案由服务合同纠纷，一审阶段
把下面三起案件都录入案件管理表：……
把这个表格里的案件逐条建到工作台
```

强制入口：

```bash
/案件录入 民事案件 原告XX公司 标的50万 北京朝阳法院
/case-manage 民事案件 原告XX公司 标的50万 北京朝阳法院
```

## 规则

- 制作或更新 skill 时，以真实飞书表结构为准。
- 如果用户明确要“录入案件管理”或“更新案件阶段”，优先匹配本 skill；slash command 只作为强制入口。
- 用户说“这个案件 / 新增一个案件”时按单案处理；用户说“这些案件 / 多个案件 / 这批案件 / 表格里的案件”时按批量处理。
- 批量案件录入必须逐条拆分、逐条校验、逐条写表；部分失败应汇总展示，不能因为某一条失败中断或吞掉其他案件结果。
- 批量案件应基于委托人、对方当事人、案由、案号、受理机构做重复疑似检查，避免重复建案。
- 如果用户明确要查询案件待办或案件提醒，优先引导到 `/案件待办`、`/case-todos`、`/案件提醒`、`/case-reminders`。
- 结果信息要尽量完整，缺失项必须提醒。
