---
name: policy-reader
title: policy_reader（app / Policy）
description: 合规示例：读取 policy references（skill_ref_read）。
author: okwinds
author_url: https://github.com/okwinds/skills-runtime-sdk/tree/main/examples/apps/policy_compliance_redactor_pro/skills/policy_reader
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: zh
---

# policy_reader（app / Policy）

## 目标

- 使用 `skill_ref_read` 读取 `references/policy.md`
- 提取“必须脱敏/禁止明文”的规则要点（供后续补丁执行）

## 必须使用的工具

- `skill_ref_read`
