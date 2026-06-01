---
name: contract-draft
title: Contract Draft
description: 用户用自然语言描述合同需求，需要生成合同草稿、同步合同台账或导出 Word 时，优先匹配 contract-draft；/起草合同 或 /contract-draft 仅作为强制入口。
author: Clukay-Fun
author_url: https://github.com/Clukay-Fun/feishu-opencode-bridge/tree/main/.opencode/skills/contract-draft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: zh
---

# Contract Draft

当用户要起草一份通用合同，例如服务合同、采购合同、保密协议、合作协议时，优先走 bridge 已实现的合同起草链路。

本 skill 属于 `contract` 合同工作域下的“起草新合同”专项能力。

当前运行时支持 `Skill Intent Router + Material Context`：

- 用户可以直接用自然语言描述起草需求，不必先输入 `/起草合同`。
- `/起草合同` / `/contract-draft` 保留为强制入口，用于跳过意图识别或纠偏。
- 自然语言触发和 slash command 触发必须进入同一套卡片生命周期：合同起草进行中、完成或失败。
- 如果用户只是讨论条款思路、审查已有合同或要求劳动争议材料工作台，不应自动触发本 skill。

运行时 prompt 覆盖文件：

- `references/prompt.txt`

## 使用方式

自然语言可直接触发，例如：

```text
起草一份软件开发服务合同，甲方杭州某科技公司，乙方张三工作室，金额20万元，周期6个月
帮我写一份保密协议，甲方为上海某公司，乙方为李某
```

强制入口：

```bash
/起草合同 <合同类型与关键参数>
/contract-draft <合同类型与关键参数>
```

## 规则

- 这是通用合同起草专项 skill，不等于 labor-skill。
- 如果用户是在劳动争议场景里要起草劳动合同、竞业协议、离职协议、offer，可以由 labor-skill 转调本能力。
- 比赛演示或高质量文书起草场景中，可按配置优先使用 Alpha GPT 作为起草模型；skill 只描述模型策略，不在 prompt 中硬编码密钥或 provider 细节。
- 若用户只是让你讨论条款思路，不一定要立刻执行；但只要目标是“生成合同初稿”，优先匹配本 skill。
