---
name: distill-protocol
title: Distill Protocol
description: 蒸馏协议：为个人数字资料生成人类可读条款与机器可读 manifest；戏称「牛马保护法」仅为传播梗，非法律意见。
author: agenmod
author_url: https://github.com/agenmod/distill-protocol-skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: zh
---

## 复制给 AI

- **本 Skill 唯一入口**：当前文件 `SKILL.md`。
- **生成脚本**：

```bash
python3 kit/protocol_gen.py --owner "你的名字" --tier human_only --output ./my-protocol
```

`--tier`：`human_only` | `no_commercial_distill` | `research_ok`。

# Distill Protocol

## 语言

根据用户**第一条消息**的语言，全程使用同一语言。

## 何时激活

- 用户要为资料包附加 **使用范围**、生成 `LICENSE-DISTILL.md` + `manifest.json`。
- 用户提及 **「牛马保护法」**：视为本协议的中文梗名，正文仍使用正式免责声明。

## 重要声明

- 本文档 **不构成法律意见**；效力因法域与合同而异。
- **「牛马保护法」** 仅为自嘲式传播用语，**勿暗示**具有真实法律效力。

## 操作顺序

### Phase 0：选择档位

| 档位 | 含义（摘要） |
|------|----------------|
| `human_only` | 仅供人类阅读，禁止用于模型训练与自动化蒸馏 |
| `no_commercial_distill` | 允许个人学习，禁止商用蒸馏产物 |
| `research_ok` | 允许研究用途，禁止商用 |
| `custom` | 用户自定义条款（需人工审阅） |

### Phase 1：填写变量

- 资料所有者名称 / 代号
- 覆盖的文件范围（路径或描述）
- 生效与更新日期

### Phase 2-3：生成

```bash
python3 kit/protocol_gen.py --tier human_only --owner "张三" --output ./my-protocol
```

检查生成的 `LICENSE-DISTILL.md` 与 `manifest.json`。

### Phase 4：（可选）站点片段

若用户有个人网站，可复制 `templates/robots-snippet.txt` 思路，拒绝特定 AI 爬虫。

### Phase 5：附署

建议将协议与资料包放在**同一目录**，并在 README 中链接。

### Phase 6：搭配防蒸馏

建议同时使用 [防蒸馏](https://github.com/agenmod/distill-shield-skill) 进行技术加固，协议负责权利表达，Shield 负责技术标记。

## 不做的事

- 不保证对第三方产生约束力；**合同/授权场景请咨询律师**。
