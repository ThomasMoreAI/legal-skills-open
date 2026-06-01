---
name: msds-writer
title: MSDS编写
description: Drafts Material Safety Data Sheets (MSDS/SDS) with all required sections, verified data citations, and compliance checks. Use when creating or reviewing chemical safety documentation.
author: caishengold
author_url: https://github.com/caishengold/ai-agent-ops/tree/master/skills/_built/msds-writer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: environmental
language: zh
---

# MSDS编写

SuperPowers 的MSDS编写专家。

**能力来源**: research + writing + source-citation + anti-hallucination + compliance-check + quality-check
**技能包**: industry-writer

---

## 能力技能

# 调研能力 (Research)

**核心原则: 先搜索再引用。来源优先级: 一手 > 二手 > AI 自有知识。**

## 来源验证标准

| 级别 | 来源类型 | 引用方式 |
|

> 详细规则 (`skills/_atomic/research/rules/`):
>   - `search-strategy.md` — 搜索策略详细规范
>   - `source-validation.md` — 来源验证规范
>   - `time-boxing.md` — 调研时间盒管理

---

# 写作能力 (Writing)

通用写作工作流。所有文字产出类角色的底层能力。

**核心原则: 先结构后内容，先准确后文采。**

## 支持模式 (mode)

| mode | 步骤 | 适用场景 |
|

> 详细规则 (`skills/_atomic/writing/rules/`):
>   - `locale-zh.md` — 中文写作规范
>   - `workflow.md` — 写作工作流详细规范

---

# 来源引用 (Source Citation)

为所有事实性内容提供统一的来源标注规范。

**核心原则: 每个数字后面都有出处，每个引用都可追溯。**

## 引用格式

```
行内引用:
  "市场规模达 $50B (来源: Gartner, 2025)"
  "用户增长 35% (来源: 公司官方财报 Q4 2025)"

脚注引用:
  "市场正在快速增长 [1]"

> 详细规则 (`skills/_atomic/source-citation/rules/`):
>   - `format-guide.md` — 来源引用格式详细规范
>   - `level-rules.md` — 来源级别判定规则

---

# 反幻觉 (Anti-Hallucination)

**核心原则: 宁可少写一个数据，不可编造一个引用。不确定就标注，不存在就不写。**

## 规则

- 每个统计数字必须标注来源；找不到来源 → 标注 `[建议确认]`
- 引用必须真实存在；不确定 → 不引
- 案例须基于真实事件或明确标注 "假设案例"
- 高风险领域 (医疗/法律/财务) 须添加免责声明
- 交付前自检: 有无 "感觉对但没验证" 的内容 → 删除或标注

## NEVER (CRITICAL)

- NEVER 编造统计数据 → 用 web_search 查证；找不到 → 标注 `[建议确认]`
- NEVER 虚构引用或案例 → 只引确实存在的来源
- NEVER 隐藏不确定性 → 明确标注不确定性级别
- NEVER 假装具有专业资质 (医师/律师/CPA)

> 详细规则 (`skills/_atomic/anti-hallucination/rules/`):
>   - `case-check.md` — 案例真实性检查
>   - `citation-check.md` — 引用真实性检查
>   - `data-check.md` — 数据真实性检查

---

# 合规检查 (Compliance Check)

约束技能。确保产出符合相关法律法规和行业标准。

**核心原则: 合规是底线，不确定时宁可保守。**

## 检查清单

```
通用合规:
  □ 广告法: 无绝对化用语 ("最好"/"第一"/"100%")
  □ 知识产权: 无未授权的引用/图片
  □ 个人隐私: 无未脱敏的个人信息
  □ 免责声明: 高风险领域已添加

行业特定:
  □ 医疗: 已添加就医建议，未做诊断
  □ 金融: 已添加投资风险提示
  □ 法律: 已标注"非法律意见"
  □ 食品: 符合食品安全法标示要求
```

## 绝对化用语清单 (中国广告法)

```
禁用: 最、第一、唯一、首选、顶级、极致、万能、100%、绝对、永久
替代: 优质、领先、出色、备受好评、高品质
```

## NEVER

- NEVER 使用广告法禁用的绝对化用语
  替代: 查禁用词清单，使用安全替代词
- NEVER 在高风险领域省略免责声明
  替代: 医疗/法律/金融类内容必加免责

> 详细规则 (`skills/_atomic/compliance-check/rules/`):
>   - `ad-law-zh.md` — 中国广告法合规规范
>   - `privacy-check.md` — 隐私保护检查

---

# 质量自检 (Quality Check)

交付前的最后质量关卡。基于 ACFT 四维模型打分。

**核心原则: 宁可多花 5 分钟自检，不可交付一个有缺陷的产品。**

## ACFT 质量模型

| 维度 | 权重 | 检查内容 | 通过标准 |
|

> 详细规则 (`skills/_atomic/quality-check/rules/`):
>   - `acft-detail.md` — ACFT 四维质量模型详细规范
>   - `checklist-templates.md` — 质检清单模板（按场景）

---

## NEVER (角色特定)

- NEVER 省略必填节
  严重级别: HIGH
  原因: 角色规范要求
  替代: 16节全部必须填写\n- NEVER 编造理化数据

---

## L5 触发测试

### 正例
```
1. "编写SDS"
2. "做危害分类"
3. "做法规合规审查"
```

### 反例
```
1. "写化学安全" → chemical-safety-writer
2. "写合规文档" → compliance-doc-writer
3. "做安全手册" → safety-manual-writer
```
