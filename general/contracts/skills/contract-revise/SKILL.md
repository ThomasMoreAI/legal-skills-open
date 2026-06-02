---
name: contract-revise
title: Contract Revise
description: 用户上传已有合同、提供合同本地路径，或处于合同工作台会话中，需要修改、删减、补充、重写条款或导出修改稿时，优先匹配 contract-revise；该 skill 复用合同工作台连续编辑链路。
author: Clukay-Fun
author_url: https://github.com/Clukay-Fun/feishu-opencode-bridge/tree/main/.opencode/skills/contract-revise
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: zh
---

# Contract Revise

当用户要对已有合同进行修改、删条款、补条款、重写局部内容、查看当前版本或导出修改稿时，优先走这条专项 skill。

当前运行时底层复用 `contract-assistant` 合同工作台：

- `/合同起草开始` 进入连续编辑会话。
- 上传已有合同或发送文字需求初始化合同结构。
- 在会话中用自然语言连续查看、修改、删除、补充和导出。

## 触发

自然语言可直接触发，例如：

```text
把刚才合同里的争议解决改成深圳法院管辖
删除风险收费那一段
补一条保密义务，然后重新导出 Word
```

强制入口建议：

```bash
/合同修改
/contract-revise
/合同起草开始
```

## 卡片生命周期

- 进入合同工作会话。
- 等待上传合同或文字起点。
- 合同初始化中。
- 合同已载入工作会话。
- 合同处理中。
- 合同已处理或导出完成。

## 边界

- 修改合同文本不等于更新合同台账。
- 只改用户明确要求的部分，其余条款必须保留。
- 用户要求整体重写时，也要保留版本历史和修改摘要。
- 用户要求审查但不要求改写时，应转入 `contract-review`。
- 用户要求从合同抽字段入表时，应转入 `contract-extract`。

## Prompt References

- `references/revise-policy.txt`
