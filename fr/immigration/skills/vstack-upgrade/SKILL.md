---
name: vstack-upgrade
title: 'Vstack upgrade'
description: 自更新 Schengen-master 技能工具集到最新版。检查当前安装版本 vs GitHub 最新可用版、显示变更内容、跑 `git pull` 更新。幂等 — 重复跑 安全。当用户想拉入新技能、被其他技能提示有未安装的 v0.x+ 技能、或 作为定期维护时使用。(Schengen-master 技能)
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/i18n/zh-CN/vstack-upgrade
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: immigration
language: zh
---

# /vstack-upgrade

## 这个技能做什么

你是 **Schengen-master 元工具（自更新）**。你查用户当前已装 vstack 版本 vs GitHub 最新、显示变更、提议更新。

**重复跑安全** — 幂等。安装为通过 git sparse-checkout，更新影响小。

应用 ETHOS 原则 #5（"更新由用户发起"）— 永不自动更新；用户总确认。

## 何时使用此技能

- 定期查（每月或发布后）
- 另一技能引用了用户没装的 `/skill-name`（可能是 v0.x+ 新增）
- 用户想看"新增什么"
- 用户看过的 CHANGELOG 条目之后
- 故障排除 — 报问题前核实用户在最新版

## 流程

1. **读用户当前版本** 从 `~/.claude/skills/schengen-master/VERSION`

2. **从 GitHub 取最新版本** 通过命中原始文件：
   ```
   curl -s https://raw.githubusercontent.com/torlyai/Schengen-master/main/skills/VERSION
   ```

3. **比版本：**
   - 如同：报"你在最新"
   - 如用户落后：列变更（读 CHANGELOG.md）

4. **如更新，问用户许可**，然后跑：
   ```
   cd ~/.claude/skills/schengen-master && git pull
   ```

5. **确认更新** 并显示新增内容。

## 输出模板（已最新）

```
工具集更新检查
═════════════════════════════════════════════════════════════════════

你的已装版本：{{VERSION}}
最新可用：    {{VERSION}}

✅ 你在最新版本。无需做事。

═════════════════════════════════════════════════════════════════════
```

## 输出模板（有更新）

```
工具集更新可用
═════════════════════════════════════════════════════════════════════

你的已装版本：{{CURRENT_VERSION}}
最新可用：    {{LATEST_VERSION}}

新增内容
═════════════════════════════════════════════════════════════════════

{{中间版本 CHANGELOG.md 摘录}}

═════════════════════════════════════════════════════════════════════
更新？
═════════════════════════════════════════════════════════════════════

跑：cd ~/.claude/skills/schengen-master && git pull

[Y/N]
```

## 路由规则

| 情况 | 行动 |
|---|---|
| 用户在最新 | 无行动；确认 |
| 用户落后 | 提议更新；解释新增 |
| 用户更新成功 | 确认+如相关建议重跑最后技能 |
| 用户更新失败（网络） | 建议手动修；提供 URL |
| 用户在开发版/分叉 | 提示在非标准安装；别盲拉 |

## 常见陷阱

| 陷阱 | 为何有害 | 修复 |
|---|---|---|
| 未经许可自动更新 | 让用户会话中间意外 | 总确认 |
| 申请中间更新 | 可能改技能行为 | 等到会话末 |
| 网络中断时试更新 | 静默失败 | 把抓取错误显给用户 |
| 用户有本地编辑 | `git pull` 可能冲突 | 更新前建议备份 |
| 更新带破坏性变更 | 用户流程坏 | 读 CHANGELOG 迁移说明 |

## 权威来源

- GitHub Releases — https://github.com/torlyai/Schengen-master/releases — 2026-05-24 已核实
- CHANGELOG.md — 见技能根目录

## 维护者注意事项

- 版本比较是简单字符串比较；1.0.0 → 1.0.1 行。对 1.x → 2.x，双重检查 semver。
- 对用户报"技能 X 不存在"，先用此技能查版本。
- `git pull` 操作在离线/防火墙环境可能失败；优雅降级告诉用户手动更新。
- 对自定义安装位置用户（`SCHENGEN_SKILLS_DEST=~/foo`），git 路径是 `~/foo` 而非 `~/.claude/skills/schengen-master` — 核实。
- 拉前总显示 CHANGELOG 差异让用户知道拿到什么。
- 对分叉用户，建议 `git fetch upstream && git diff upstream/main` 而非盲拉。
