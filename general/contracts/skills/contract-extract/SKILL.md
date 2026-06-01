---
name: contract-extract
title: Contract Extract
description: 用户上传合同文件或提供合同本地路径，并用自然语言要求提取字段、录入合同台账或写入合同表时，优先匹配 contract-extract；/合同录入 或 /contract-extract 仅作为强制入口。
author: Clukay-Fun
author_url: https://github.com/Clukay-Fun/feishu-opencode-bridge/tree/main/.opencode/skills/contract-extract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: zh
---

# Contract Extract

当用户要把现有合同文件结构化录入合同台账时，优先走这条专项 skill。

本 skill 属于 `contract` 合同工作域下的“已有合同字段提取并写台账”专项能力。

当前运行时支持 `Skill Intent Router + Material Context`：

- 用户可以先上传合同，再用自然语言说明“录入台账 / 提取字段 / 写入合同表”。
- 用户也可以在同一句里给出本地文件路径并说明处理目标。
- `/合同录入` / `/contract-extract` 保留为强制入口，可带本地路径，也可进入等待上传状态。
- 自然语言触发和 slash command 触发必须进入同一套卡片生命周期：等待上传、合同录入进行中、完成或失败。
- 如果用户只是要求总结合同内容，不应自动写入合同台账。

运行时 prompt 覆盖文件：

- `references/prompt.txt`

## 使用方式

自然语言可直接触发，例如：

```text
把刚才这个合同录入台账
提取这份合同字段并写入合同表
把 /Users/me/contracts/demo.pdf 录入合同台账
```

强制入口：

```bash
/合同录入
/contract-extract
/合同录入 /absolute/path/to/contract.pdf
```

## 规则

- 这是“合同信息提取”能力，不负责起草。
- 如果用户只是想总结合同内容，不一定要录入台账。
- 如果用户明确说“录入台账”“入合同表”“结构化提取合同字段”，优先匹配本 skill；slash command 只作为强制入口。
- 不要伪造合同编号、金额、日期或付款节点。
