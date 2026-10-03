---
name: legal-research-malnlda
title: legal-research（法律研究编排技能）
description: 法律研究编排技能（meta-skill）。按"查法规 → 查案例 → 生成备忘录"流水线协同调度 yd-law-search、yd-case-search、cs-china-lawyer-analyst 三个子技能，形成完整的 法律研究工作流。本技能本身不做检索也不做分析，只负责调度与汇总。
author: malnlda
author_url: https://github.com/malnlda/legal-research/tree/main/skills/legal-research
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: general
language: zh
---

# legal-research（法律研究编排技能）

## 定位

编排型 skill。本身不调用任何外部 API，不下结论；只在被显式触发时把
`yd-law-search` → `yd-case-search` → `cs-china-lawyer-analyst` 串成流水线。

三个子技能维持独立可用：
- `yd-law-search`（自有）：法律法规检索
- `yd-case-search`（自有）：案例检索
- `cs-china-lawyer-analyst`（外部，submodule 锁版本）：法律分析与备忘录生成

用户可以继续直接喊单个子技能（如"只用 yd-law-search 查一下"），编排只在被
显式触发时介入。

## 触发场景

显式触发关键词（任一命中即进入流水线）：
- "请使用 legal-research"、"用 legal-research 帮我..."
- "做一份法律研究"、"出法律研究备忘录"、"做法律研究备忘录"
- "帮我做案件法律研究"、"研究这个案件的法律法规和案例"
- "走完整法律研究流程"

不触发的情况（即使关键词模糊也不要进入流水线）：
- 单纯"查法条"、"查案例" → 直接走对应单个子技能
- 没有清晰的「案件事实 / 研究问题」输入 → 先反问用户补充，再决定是否进入流水线
- 用户只想要法律意见结论但拒绝检索环节 → 直接走 cs-china-lawyer-analyst

## 流水线（固定顺序）

```
Step 0  解析输入
        ├─ 从用户给的事实/问题里抽出 2-5 个核心法律研究问题（research questions）
        ├─ 列出涉及的法律领域（合同/侵权/刑事/行政/...）
        └─ 若提取不到，反问用户补充事实，不进 Step 1。

Step 1  调用 yd-law-search（查规范依据）
        ├─ 默认: search（语义）打底，每个 research question 1 次
        ├─ 必要时补 search_keyword（精确术语，如已识别出明确法律术语）
        ├─ 不主动用 search_fg（除非用户要求"列出相关法规"）
        └─ 输出: 相关法条清单（含 id），不在此步拉全文

Step 2  调用 yd-case-search（查案例）
        ├─ 默认: search_al_vector（语义）打底
        ├─ 必要时补 search_al（按案由/法院/时间筛选）
        ├─ authority_only 默认 false；用户强调"权威/典型"时才 true
        └─ 输出: 相关案例清单（含 id 与 type，短摘要）

Step 2.5 按需 detail 下钻（限量）
        ├─ 从 Step 1/2 结果中挑 1-3 条最相关的，分别调:
        │     ft_detail / fg_detail / case_detail
        └─ 硬上限: 单次研究最多 5 次详情调用，避免积分浪费。

Step 3  调用 cs-china-lawyer-analyst（生成备忘录）
        ├─ 输入: 原始问题 + Step 1/2/2.5 的结构化结果
        └─ 输出: 法律研究备忘录（结构由该子技能自行决定）

Step 4  汇总返回给用户
        └─ 末尾附"参考资料"区块: 法条/案例链接 + id，便于核验
```

## 中断与降级

- 用户在任何一步插话调整 → 编排让位，按用户指令走，不要硬撑流水线。
- Step 1 / Step 2 任一返回为空 → **不阻塞**，向 Step 3 传"未检索到相关 X"，
  由 analyst 在备忘录里如实标注"该方向无检索结果"。
- 子技能调用失败（API 错误、网络异常、积分不足）→ 跳过该步并在最终备忘录里
  标记「该部分未检索成功」，**不静默吞错**。
- **严禁在 Step 3 之前自行下结论**；编排技能只搬运、不分析。
- 每个 step 之间可以输出极简进度提示（如"✓ Step 1 完成，找到 6 条法条"），
  但不要把全部检索结果塞回上下文，只保留 id + 标题 + 一行摘要传给 Step 3。

## token 控制原则

编排技能本身不消耗 token，但调度时必须遵守：
1. 子技能默认输出（不带 `--full`）已是精简版，**不要轻易加 --full**。
2. Step 2.5 详情下钻硬上限 5 次。
3. 传给 Step 3 的检索结果用紧凑结构：每条 1-2 行（id + 标题 + 关键摘要），
   而不是把整段文本贴进上下文。

## 使用示例

```
用户: 请使用 legal-research 帮我研究：A 公司向 B 个人出借 100 万，年利率 30%，
      逾期未还。A 起诉 B 要求返还本金及利息，问利率部分能支持多少？

编排执行:
  Step 0 → research questions:
           1) 民间借贷利率的法定上限
           2) 法院对超过上限部分的处理
           3) 借贷主体（公司↔个人）对利率上限是否有特殊影响
  Step 1 → yd-law-search search × 3
  Step 2 → yd-case-search search_al_vector × 2
  Step 2.5 → ft_detail × 2 (民法典/民间借贷司法解释关键条文)
  Step 3 → cs-china-lawyer-analyst（生成备忘录）
  Step 4 → 汇总输出
```

## 与子技能 SKILL.md 的关系

- 子技能 SKILL.md 中已声明本 skill 是它们的"上层编排技能"。
- 不修改 cs-china-lawyer-analyst 的 SKILL.md（它是 git submodule，避免上游冲突）。
