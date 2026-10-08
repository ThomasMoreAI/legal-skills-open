# Litigation Mode

Use for practical litigation/arbitration/non-contentious dispute analysis. Facts are not given; they must be reconstructed from pleadings, evidence, and party narratives.

## Core Distinction

Keep these separate:

- party assertion;
- evidence content;
- evidence-supported fact;
- disputed fact;
- fact to be proved;
- legal evaluation;
- model inference.

## Workflow

1. Inventory materials and label source types.
2. Identify parties, roles, relationships, and claim goals.
3. Translate raw demands into legal claims.
4. Identify material professional terms and route them through concept cards or temporary concept cards.
5. Match claim goals to candidate request bases and rule-obligation groups.
6. If no rule-obligation group fits, create a temporary candidate group with trigger facts, paths, defenses, evidence targets, and verification tasks.
7. List candidate causes of action as filing/retrieval/calibration labels, with uncertainty.
8. Use rule-obligation group `entry_mappings` to keep substantive paths, backup paths, and deferred paths separate.
9. For each request basis selected for detailed analysis, apply the lifecycle gates: right arises, not extinguished, exercisable, defenses/counter-defenses.
10. Reverse-engineer element facts and defense facts for each lifecycle gate.
11. Map evidence to facts and facts to elements.
12. Identify denials, defenses, counter-defenses, burden holder, and proof gaps.
13. Build a source register with verification status for material claims.
14. List MCP research tasks for current law and case-law.
15. Provide next-step lawyer worklist.

For real case pilots, also use the real-case-testing reference. Start with a material register and a first-pass map unless the user asks to deep-dive a specific claim.

## Output Skeleton

```markdown
# 请求权基础实务分析

## 1. 材料分层说明

## 2. 主体与法律关系

| 主体 | 可能身份 | 材料依据 | 待核验 |
| --- | --- | --- | --- |

## 3. 诉请/潜在诉请

| 编号 | 原始表述 | 法律表达 | 请求对象 | 请求内容 |
| --- | --- | --- | --- | --- |

## 4. 候选请求权基础与规则义务群

| 请求目标 | 请求权基础 | 规则义务群 | 路径用途 | 不确定性 |
| --- | --- | --- | --- | --- |

## 5. 专业概念触发与概念卡

| 概念 | 触发事实 | 相邻概念 | 请求权影响 | 状态 |
| --- | --- | --- | --- | --- |

## 6. 候选案由

案由用于检索、立案、诉状草拟、类案召回或校准，不作为唯一实体分类。

| 候选案由 | 关联请求目标 | 关联请求权基础 | 用途 | 不确定性 |
| --- | --- | --- | --- | --- |

## 7. 请求权生命周期检视

| 请求权基础 | 产生 | 未消灭 | 可行使 | 抗辩/反抗辩 | 证据/核验缺口 |
| --- | --- | --- | --- | --- | --- |

## 8. 要件事实与证据映射

| 请求权基础 | 要件 | 待证事实 | 举证责任 | 现有证据 | 强度 | 缺口 |
| --- | --- | --- | --- | --- | --- | --- |

## 9. 抗辩与反抗辩

## 10. 来源登记与核验状态

| 对象 | 命题/用途 | 来源类型 | 核验状态 | 定位/检索范围 | 备注 |
| --- | --- | --- | --- | --- | --- |

## 11. 需 MCP 检索的问题

| 问题 | 类型 | 强制性 | 理由 | 预期输出 |
| --- | --- | --- | --- | --- |

## 12. 下一步工作清单

## 13. 测试反馈记录

| 问题类型 | 观察到的问题 | 可能原因 | 建议修复位置 | 是否进入仓库 |
| --- | --- | --- | --- | --- |
```

## Guardrails

- Do not write client assertions as found facts.
- Do not let a single cause of action replace request-basis analysis.
- Do not skip proof gaps.
- Do not say courts usually rule a way without case-law research.
- If evidence is insufficient, output risk rather than a strong conclusion.
- Track source labels for material facts, legal rules, causes of action, request bases, and case-law claims.
- Do not turn real matter facts into permanent examples; only abstract reusable workflow defects into feedback.
