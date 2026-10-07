# labor-compliance migration notes

## 来源

- 旧目录：`src-tauri/plugins/labor-compliance`（本次复核通过 `git ls-tree` / `git show HEAD:...` 读取，未恢复已删除的旧目录）
- 已复核：`plugin.toml`、`workflow.toml`、`prompts/*.md`、`scripts/knowledge/*`
- 新入口：`docs/skills-migration/labor-compliance/SKILL.md`

## 迁移取舍

- 将旧多步 workflow 改写为 standalone、无状态的 SKILL.md 指南；正文不依赖 `plugin.toml`、`workflow.toml`、旧 session state 或系统自动预计算。
- 保留原技能的触发场景、角色定位、核心分析框架、阶段性确认、报告和 PPT 交付要求。
- 旧预计算能力未随包保留为可运行资产；关键判断、指标和匹配口径已转写到 SKILL.md 流程中，避免依赖旧运行时变量或自动注入状态。
- `allowed-tools` 只保留本技能正文真实建议使用的工具；旧状态型保存/记忆工具未在新正文中作为机制保留，阶段信息改为通过当前回复内复述确认。

## 保留资源

- 知识库：`references/knowledge/regulations.json`, `references/knowledge/remediation.json`

## 人工复核点

- 知识库文件与旧 `scripts/knowledge/` 同名文件逐一比对一致。
- 原预计算逻辑仅保留为迁移理解依据，未作为文件随包发布；可复制使用的执行口径已并入 SKILL.md 正文步骤。
- Frontmatter 已按 AIjia SKILL.md 新规范设置：`name` 等于目录名，`context: inline`，`user-invocable: true`，`disable-model-invocation: false`，`version: "1.0"`，`metadata.label` 为中文显示名。
