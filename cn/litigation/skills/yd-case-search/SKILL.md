---
name: yd-case-search
title: 元典案例检索技能（yd-case-search）
description: '元典案例检索技能（开放平台版 https://open.chineselaw.com）。

  用于中国案例、类案、典型案例、权威案例的关键词检索与语义检索，以及案例详情拉取。

  不负责最终法律结论；如需基于案例做论证，应继续调用 cs-china-lawyer-analyst；

  若是"做法律研究备忘录"类完整流程，应交由 legal-research 编排技能调度。'
author: malnlda
author_url: https://github.com/malnlda/legal-research/tree/main/skills/yd-case-search
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: litigation
language: zh
---

# 元典案例检索技能（yd-case-search）

## 定位

案例检索型 skill，负责把相关案例和类案快速捞出来。

- 它负责：案例关键词检索、类案语义检索、按法院/地区/案由/时间筛选、案例详情
- 它不负责：直接替代完整法律分析
- 与现有 skill 的关系：
  - `yd-case-search`：找案例（本 skill）
  - `yd-law-search`：找法条和规范依据
  - `cs-china-lawyer-analyst`：把案例和法条整合成法律意见
  - `legal-research`：上层编排技能，按"查法规→查案例→出备忘录"调度上述三者

## API Key 配置

与 `yd-law-search` 相同，按以下顺序读取：
1. `YD_OPEN_API_KEY`
2. `~/.yd_open_api_key`
3. `YD_API_KEY`
4. `~/.yd_api_key`
5. 脚本目录 `.api_key`

申请入口：<https://open.chineselaw.com/>

## 工作流（重要）

- 默认搜索只返回元数据 + 高亮/要旨片段，不返回全文。
- 当需要某案例的全文时，使用 `case_detail` 配合 id 与 `type`（ptal/qwal）拉取。
- 不要在搜索后立即对全部命中调用详情接口；先筛 1-3 条最相关的再下钻。
- `--full` 开关用于调试或用户明确要求全文展示时使用。

## 子命令

### 1. `search_al` — 案例关键词/筛选检索
适合：已有关键词、案由、法院、案号、标题，要做筛选式案例研究。

路由：
- `authority_only=true` → 走 `/open/rh_qwal_search`（权威/典型案例）
- 否则 → 走 `/open/rh_ptal_search`（普通案例）
- **不主动同时打两边**（避免 2× 积分）。如需两边都看，请显式分两次调用。

### 2. `search_al_vector` — 案例语义检索
适合：用自然语言描述争议焦点、做类案语义检索。

### 3. `case_detail` — 案例详情
按 id 拉单个案例全文。**必须传 `type`：`ptal`（普通）或 `qwal`（权威）**。

## 调用方式

```bash
# 1. 关键词检索（普通案例）
echo '{"ay":["买卖合同纠纷"],"xzqh_p":["北京"],"qw":"违约金 逾期","top_k":5}' | \
  python3 ~/.claude/skills/yd-case-search/scripts/yd_case_search.py search_al --stdin

# 2. 关键词检索（权威案例）
echo '{"qw":"人工智能","authority_only":true}' | \
  python3 ~/.claude/skills/yd-case-search/scripts/yd_case_search.py search_al --stdin

# 3. 案例语义检索（带筛选）
echo '{"query":"正当防卫的限度","wenshu_filter":{"ja_start":"2020-01-01","ja_end":"2025-12-31"}}' | \
  python3 ~/.claude/skills/yd-case-search/scripts/yd_case_search.py search_al_vector --stdin

# 4. 案例详情（按 id）
echo '{"id":"183fe9bf6e95f51fab804e383854a51f","type":"ptal"}' | \
  python3 ~/.claude/skills/yd-case-search/scripts/yd_case_search.py case_detail --stdin
```

通用 flag：
- `--stdin` / `--full` / `--raw`（同 yd-law-search）

## 使用规则

- 「查有没有相关案例」→ 优先 `search_al_vector`
- 「精确筛选、限定字段」→ 优先 `search_al`
- 用户明确要求"只看权威/典型案例" → `authority_only=true`
- 默认 `top_k = 8`；展示时至少保留：标题、案号、案件类别、经办法院、裁判日期、id（含 type）、链接
- 如需从案例中抽取裁判规则并论证适用，再交给 `cs-china-lawyer-analyst`

## 输出建议

1. 最相关案例列表（≤8 条）
2. 每个案例的基本信息 + id (含 type)
3. 与当前问题的关联点（短）
4. 提示是否需要拉全文（case_detail）或继续法条检索
