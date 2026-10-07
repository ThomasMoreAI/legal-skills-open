# 更新日志 (Changelog)

## [2026-04-10] 威科先行 API 集成

### 新增功能

#### 1. 威科先行 API 自动化流程

在 SKILL.md 中新增"威科先行 API 确认与配置（自动化）"章节（W.1~W.5），实现：

- **W.1** AI 主动询问用户是否拥有威科先行 API
- **W.2** 用户回答"有"后，AI 依次询问 API 四项信息（端点、Key、Secret、认证方式）
- **W.3** AI 自动将配置写入 `config.json`
- **W.4** AI 用已确认的检索关键词自动调用威科 API
- **W.4** 关键词自动提取规则（从事实总结中提取核心争议关键词）
- **W.5** 配置失败处理（不影响主流程）

**影响范围**：SKILL.md 原文 1424 行 → 1528 行（净增约 104 行）

#### 2. 新增文件

| 文件 | 用途 |
|---|---|
| `wolters_auto.py` | 懒人检索接口（自动读取 config.json，skill 实际调用） |
| `wolters_wrapper.py` | 自动调用包装器（skill 流程自动触发入口） |
| `config.json.example` | 配置文件模板 |
| `wolters_API_GUIDE.md` | 威科集成指南（模块说明 + 用户指南合并文档） |

#### 3. 重构旧文件

| 操作 | 文件 |
|---|---|
| **删除** | `wolters_INTEGRATION_GUIDE.md`（旧版指南，内容已合并） |
| **删除** | `wolterskluwer_searcher_README.md`（旧版模块说明，内容已合并） |
| **新增** | `wolters_API_GUIDE.md`（合并后的完整指南） |

#### 4. Bug 修复

- `auto_search()` 函数逻辑错误：原逻辑先调用 API 再检查配置，现已修复为先检查 `is_configured()` 再调用 API

### 变更说明

- 所有修改**仅涉及插入和新增**，未删除 SKILL.md 原有内容
- 删除了一个重复的"第三阶段：系统性检索"标题（修正常见问题）
- 用户无需修改任何代码，配置 `config.json` 即可使用威科先行 API

### 用户操作变化

**之前**：用户需手动创建 config.json 并填入 API 凭证，skill 被动检测

**现在**：用户只需回答"有/没有 API"，AI 自动完成配置、关键词提取、调用全流程

### 文件清单

```
legal-issue-research/
├── SKILL.md                  ← 主 skill（已整合威科自动化流程）
├── config.json.example       ← 配置模板
├── wolters_API_GUIDE.md      ← 合并后的完整指南
├── wolters_auto.py           ← 懒人接口
├── wolters_wrapper.py        ← 自动调用包装器
├── wolterskluwer_searcher.py ← 完整功能（参考，可选上传）
└── examples/                  ← 示例目录
```
