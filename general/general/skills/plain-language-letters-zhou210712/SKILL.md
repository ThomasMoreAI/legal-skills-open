---
name: plain-language-letters-zhou210712
title: '[已弃用] 通俗语言信函 → 参见 `/client-letter` 和 `/status client`'
description: 参考：已弃用——常规信函请使用 `/client-letter`，实质性更新请使用 `/status client`。在 v2 重构中拆分为两个更聚焦的技能。保留为重定向以支持迁移。
author: zhou210712
author_url: https://github.com/zhou210712/claude-for-legal-ZH/tree/main/legal-clinic/skills/plain-language-letters
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: zh
---

# [已弃用] 通俗语言信函 → 参见 `/client-letter` 和 `/status client`

本技能在 v2 重构中已拆分：

- **常规信函**（预约确认、文件索取、简要"已提交"更新） → `skills/client-letter/` — 使用 `/client-letter [类型]`

- **实质性当事人状态更新** → `skills/status/` 当事人面向模式 — 使用 `/status client`

两者均适用 CLAUDE.md 中的通俗语言标准（阅读水平、无法律术语）。

完整工作流见各 SKILL.md 文件。
