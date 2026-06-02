---
name: yd-law-search
title: 元典法条/法规检索技能（yd-law-search）
description: '元典法律法规检索技能（开放平台版 https://open.chineselaw.com）。

  用于中国法律、行政法规、司法解释、部门规章、地方性法规等规范性文件的检索。

  适合：法条语义检索、法条关键词检索、法规级别检索、法条/法规详情查询。

  不负责最终法律结论；如需基于检索结果做法律分析，应继续调用 cs-china-lawyer-analyst；

  若是"做法律研究备忘录"类完整流程，应交由 legal-research 编排技能调度。'
author: malnlda
author_url: https://github.com/malnlda/legal-research/tree/main/skills/yd-law-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: general
language: zh
---

# 元典法条/法规检索技能（yd-law-search）

## 定位

检索型 skill，把规范依据稳定、结构化地检索出来。

- 它负责：查法条、查法规、查司法解释、查具体条文全文
- 它不负责：直接替代法律分析、出完整法律意见
- 与现有 skill 的关系：
  - `yd-law-search`：检索规范依据（本 skill）
  - `yd-case-search`：检索案例与类案
  - `cs-china-lawyer-analyst`：基于检索结果做法律分析
  - `legal-research`：上层编排技能，按"查法规→查案例→出备忘录"调度上述三者

## API Key 配置

脚本按以下顺序读取 API Key：
1. 环境变量 `YD_OPEN_API_KEY`
2. `~/.yd_open_api_key`
3. 环境变量 `YD_API_KEY`
4. `~/.yd_api_key`
5. 脚本目录下 `.api_key`

申请入口：<https://open.chineselaw.com/>

## 工作流（重要）

- 默认搜索只返回元数据 + 高亮/要旨片段，不返回全文。
- 当需要某条法条或法规的全文时，使用 `ft_detail` / `fg_detail` 配合 id 拉取。
- 不要在搜索后立即对全部命中条目调用详情接口；先由模型/用户筛选 1-3 条最相关的，再单独拉详情。
- `--full` 开关用于调试或用户明确要求全文展示时使用。

## 子命令决策树（严格遵守，不要自由发挥）

默认路由（用于 99% 的"查法律/查规定"提问）：
1. **自然语言问题、想要规范依据原文** → `search`（语义法条）
2. **多关键词、术语精确、要做条件过滤** → `search_keyword`（关键词法条）
3. **已知法规名 + 条号** → `ft_detail`（法条详情）

仅在出现以下显式信号时才走「法规级别」接口：
- 用户问"有哪些法规/规章/规定"、"列出相关法规"
- 用户问"某机关发过什么文件"、"做法规盘点"
- 用户已明确给出法规名要拉法规全文 → `fg_detail`

明确禁止：
- **不要用 `search_fg` 来回答"某规则是什么"**——那是 `search` / `search_keyword` 的活。
- `search_fg` 只回法规清单（标题、发布部门、发布日期），不返回具体条文。

## 调用方式

```bash
# 1. 语义检索（自然语言）
echo '{"query":"民间借贷利率上限"}' | \
  python3 ~/.claude/skills/yd-law-search/scripts/yd_law_search.py search --stdin

# 2. 关键词检索（精确）
echo '{"keyword":"个人信息 处罚","search_mode":"AND","sxx":"现行有效"}' | \
  python3 ~/.claude/skills/yd-law-search/scripts/yd_law_search.py search_keyword --stdin

# 3. 法条详情（需法规名 + 中文条号）
echo '{"fgmc":"中华人民共和国刑法","ftnum":"第一百条"}' | \
  python3 ~/.claude/skills/yd-law-search/scripts/yd_law_search.py ft_detail --stdin

# 4. 法规级别检索（仅在用户要"列法规清单"时）
echo '{"keyword":"行政处罚","sxx":"现行有效","top_k":8}' | \
  python3 ~/.claude/skills/yd-law-search/scripts/yd_law_search.py search_fg --stdin

# 5. 法规详情（按 id 或 fgmc）
echo '{"fgmc":"中华人民共和国民法典"}' | \
  python3 ~/.claude/skills/yd-law-search/scripts/yd_law_search.py fg_detail --stdin

# 旧子命令 search_ft_info 仍兼容（自动映射 query→fgmc, ft_name→ftnum）
echo '{"query":"民法典","ft_name":"第六百八十条"}' | \
  python3 ~/.claude/skills/yd-law-search/scripts/yd_law_search.py search_ft_info --stdin
```

通用 flag：
- `--stdin`：从 stdin 读 JSON
- `--full`：打印全文（默认只打 ≤120 字摘要）
- `--raw`：直接打印 API 原始 JSON

## 使用规则

- 默认 `top_k = 8`；用户明确要更多时再调大。
- 时效性默认 `现行有效`；查历史版本用 `refer_date`（仅 ft_detail / fg_detail 支持）。
- 展示结果时至少保留：法规名、条号、时效性、内容片段、链接、id（便于下钻详情）。
- 引用法条原文时不擅自改写。
- 若需要论证法条如何适用，转入 `cs-china-lawyer-analyst`。

## 输出建议

1. 最相关法条 / 法规清单（≤8 条）
2. 关键条文摘要 + id
3. 链接
4. 提示是否需要拉全文（ft_detail/fg_detail）或继续案例检索
