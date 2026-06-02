---
name: contract
title: Contract
description: 合同工作域总入口。用户用自然语言提出合同起草、录入、审查、修改、查询、更新、删除或作废等需求时，先由 contract 判断意图，再转交明确的专项 skill；slash command 仅作为纠偏和强制入口。
author: Clukay-Fun
author_url: https://github.com/Clukay-Fun/feishu-opencode-bridge/tree/main/.opencode/skills/contract
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: zh
---

# Contract

合同相关能力采用“入口整合，能力拆分”的结构。用户侧可以直接说自然语言；工程侧必须把高风险写操作、文档解析、审查、修改和台账操作拆到专项 skill。

## 子能力

```text
contract
  -> contract-draft      从需求生成新合同草稿、Word、台账同步
  -> contract-extract    从已有合同提取字段并写入合同台账
  -> contract-review     审查已有合同，输出风险、缺失条款和修改建议
  -> contract-revise     基于已有合同或工作台状态修改、删改、补充、导出合同
  -> contract-query      查询合同台账，待实现
  -> contract-update     更新合同台账字段、付款节点、状态，待实现
  -> contract-delete     删除、作废或归档合同记录，高风险，待实现且必须确认
```

## 路由原则

- 用户要“新写一份合同”“生成初稿”“导出 Word”：优先 `contract-draft`。
- 用户给的是已有合同，并要求“录入台账”“提取字段”“写入合同表”：优先 `contract-extract`。
- 用户给的是已有合同，并要求“审查一下”“看看风险”“有没有问题”：优先 `contract-review`。
- 用户给的是已有合同或正在工作台中，并要求“改一下”“删掉某条”“补一条”“重新导出”：优先 `contract-revise`。
- 用户要查台账、更新台账字段、删除或作废记录时，必须区分 `query / update / delete`，不要混入合同文本修改。
- 如果用户只是讨论合同条款思路，不一定触发写操作；可以普通对话或引导用户确认是否进入专项 skill。

## 材料上下文

- 用户可以先上传文件，再用自然语言决定处理方式。
- 用户可以在同一句中提供本地绝对路径。
- 文件上传本身只建立材料上下文，不等于自动执行写表、审查或修改。
- 自然语言触发后，应进入对应专项 skill 的卡片生命周期，不能静默用普通文本替代。

## 安全边界

- 合同录入、台账更新、删除、作废属于写操作，低置信或字段缺失时必须确认或拒绝。
- 合同审查默认不修改原文，也不写台账；除非用户明确要求生成修改稿或同步台账。
- 合同修改默认不写回台账；导出 Word 或更新台账需要单独确认。
- 删除、作废、覆盖合同记录必须是独立高风险入口，不能由模糊自然语言直接执行。

## Prompt References

- `references/router-policy.txt`
