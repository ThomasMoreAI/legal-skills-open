---
name: patent-search-zimoliao
title: patent-search — USPTO 专利搜索
description: Use when the user wants USPTO patent discovery, patent metadata lookup, application lookup, or downloadable patent candidates before ingest.
author: ZimoLiao
author_url: https://github.com/ZimoLiao/scholaraio/tree/main/.claude/skills/patent-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: zh
---

# patent-search — USPTO 专利搜索

通过 USPTO Patent Public Search (PPUBS) 搜索美国专利，**无需 API Key，无需注册账号**。

同时保留 USPTO Open Data Portal (ODP) API 作为可选后端（需要 API Key），用于更结构化的申请号查询。

**注意：本命令仅用于搜索发现，不会直接入库。** 如需将专利纳入知识库，请后续通过 `patent-fetch` 或 `--fetch` 下载 PDF 后放入 configured patent inbox（fresh 默认 `data/spool/inbox-patent/`），再执行 `scholaraio pipeline ingest` 走正常的专利入库流程（含公开号去重）。

## 用法

### 关键词搜索（默认 PPUBS，无需 API Key）

```bash
# 基本搜索
scholaraio patent-search "artificial intelligence"

# 指定结果数量
scholaraio patent-search "neural network" --count 20

# 分页
scholaraio patent-search "semiconductor" --count 10 --offset 10
```

### 搜索并自动下载 PDF

```bash
# 搜索并自动下载所有结果中的专利 PDF 到 configured patent inbox
scholaraio patent-search "quantum computing" --count 5 --fetch
```

### 高级查询语法（PPUBS）

PPUBS 支持字段限定检索，基本语法为 `("term").field.`：

```bash
# 标题检索
scholaraio patent-search '("artificial intelligence").title.'

# 发明人检索
scholaraio patent-search '("Smith").inventor.'

# 公开号检索
scholaraio patent-search '("US20230123456A1").publ.'

# 布尔组合
scholaraio patent-search '("artificial intelligence").title. AND ("neural network").title.'
```

### 使用 ODP API（需要 API Key）

若已配置 ODP API Key，可通过 `--source odp` 切换到 ODP 后端：

```bash
# ODP 关键词搜索
scholaraio patent-search "artificial intelligence" --source odp

# 按申请号查询详情（ODP 支持更完整的结构化元数据）
scholaraio patent-search --application 17123456 --source odp
```

**ODP API Key 配置方式：**
- `config.local.yaml`：
  ```yaml
  patent:
    uspto_odp_api_key: "your-api-key"
  ```
- 环境变量：
  ```bash
  export USPTO_ODP_API_KEY="your-api-key"
  ```

## 输出示例

```
找到 3 / 1542 条 USPTO 专利结果

[1] SYSTEMS AND METHODS FOR MACHINE LEARNING BASED IMAGE PROCESSING
    Publication: US20230123456A1
    Inventors: John Doe, Jane Smith
    Filing: 2021-05-15
    Published: 2023-04-20
    Type: US-PGPUB
    下载: scholaraio patent-fetch US20230123456A1

[2] NEURAL NETWORK ACCELERATOR WITH DYNAMIC SPARSITY
    Publication: US11678901B2
    Inventors: Alice Wong
    Assignees: Example Corp
    Filing: 2020-03-10
    Published: 2023-06-13
    Type: USPAT
    下载: scholaraio patent-fetch US11678901B2
```

## 推荐工作流

### 方式一：搜索后手动下载
```bash
# 1. 搜索发现目标专利
scholaraio patent-search "quantum computing" --count 10

# 2. 根据输出提示，手动下载感兴趣的专利
scholaraio patent-fetch US20230123456A1
```

### 方式二：搜索并自动下载
```bash
# 1. 搜索并自动下载前 5 条结果的 PDF
scholaraio patent-search "quantum computing" --count 5 --fetch

# 2. 走正常 pipeline 入库
scholaraio pipeline ingest

# 3. 本地检索
scholaraio search "quantum computing"
```

## 故障排除

**缺少 API Key（仅影响 `--source odp`）**
```
搜索失败: 缺少 USPTO ODP API Key。请在 config.local.yaml 中配置...
```
解决方案：
1. 如果不需 ODP 的额外功能，直接使用默认 PPUBS（不加 `--source odp`）
2. 如需 ODP，访问 https://data.uspto.gov/apis/getting-started 注册账号
3. 完成视频验证后获取 API Key
4. 配置到 `config.local.yaml` 或环境变量

**未找到专利**
```
未找到与 '...' 相关的专利
```
- 尝试简化关键词
- 检查 PPUBS 字段语法是否正确（引号、括号、点号）
- 对精确申请号查询，使用 `--source odp --application <号码>`

**PPUBS 会话过期/403**
- 客户端会自动刷新会话并重试，通常无需手动处理
- 若频繁失败，可能是网络波动，稍后再试

**patent-fetch 下载失败**
- 美国专利会优先尝试 USPTO PPUBS 官方导出；若失败再回退 Google Patents
- 该专利可能尚未提供可导出的 PDF（如非常新的 WO 专利）
- 尝试在浏览器中打开专利页面确认
- 部分专利需要换源（如 EPO）

## 相关功能

- `scholaraio patent-fetch` — 下载指定专利 PDF 到 configured patent inbox（fresh 默认 `data/spool/inbox-patent/`）
- `scholaraio arxiv` — arXiv 论文搜索与下载
- `scholaraio websearch` — 实时网页搜索
- `scholaraio pipeline ingest` — 将 inbox-patent 中的 PDF 入库
- `scholaraio search` / `scholaraio vsearch` — 本地知识库检索
