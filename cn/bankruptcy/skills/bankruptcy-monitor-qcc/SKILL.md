---
name: bankruptcy-monitor-qcc
title: 企业破产预警与破产重整监控 · 企查查 MCP V2.0 增强版
description: '企业破产预警与破产重整监控 SKILL · 企查查 MCP V2.0 增强版。 对重要客户、债务人、担保方进行破产风险的持续监控工具，同时覆盖"破产预警"（事前识别）与"破产重整预警"（事中跟踪）两种子场景。通过 qcc-history 历史数据 + qcc-executive 核心人员画像 + qcc-risk 当前司法信号三层融合，在破产重整申请提交、清算公告发布等关键节点实时推送预警，帮助债权人在债权申报窗口期内及时采取保全措施。

  核心能力： - 破产先行指标识别：法代被执行、股权冻结扩散、终本案件累积、失信连年新增等 7 大先行指标 - 破产重整 / 清算状态跟踪：`get_bankruptcy_reorganization` / `get_liquidation_info` 实时监控正式破产程序 - 核心人员跑路信号：实控人限制出境、法代更替、核心高管离任等 qcc-executive 穿透 - 重整可行性预判：基于财务底盘 × 司法泥潭 × 实控人现状三元组合，区分"值得重整 vs 必然清算" - 债权申报窗口期推算：按破产法规定的 30 / 60 / 90 日窗口，动态计算最晚申报日

  适用场景：银行不良贷款管理 / 供应链应收账款管理 / 商票与保理业务贷后 / 公司债券债权人管理 / 保险公司保费追索。

  使用方式：/bankruptcy-monitor 企业名称 [--scenario warning|restructuring|both] [--claim-amount 债权金额] [--format md|docx|pptx]'
author: duhu2000
author_url: https://github.com/duhu2000/vibe-lawyering-qcc/tree/main/skills/bankruptcy-monitor-qcc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: bankruptcy
language: zh
---

## 📖 QCC MCP 术语对照表（强制工具映射）

> **使用约定**：本表列出 SKILL 内业务简写与企查查 MCP 工具的精确映射。AI 执行本 SKILL 时遇到下表"业务简写"列的词汇，**必须调用对应"MCP 工具"列**，禁止使用 web search 或自由文本推测替代。完整规范见 [QCC-MCP-TERMINOLOGY.md](../../QCC-MCP-TERMINOLOGY.md)。

| 业务简写 | 规范全名 | 企查查 MCP 工具 |
| --- | --- | --- |
| 失信 | 失信被执行人 | `mcp__qcc-risk__get_dishonest_info` |
| 被执行 | 被执行人 / 判决债务人 | `mcp__qcc-risk__get_judgment_debtor_info` |
| 限高 | 限制高消费 | `mcp__qcc-risk__get_high_consumption_restriction` |
| 限出境 / 限境 | 限制出境 | `mcp__qcc-risk__get_exit_restriction` |
| 终本 | 终结本次执行案件 | `mcp__qcc-risk__get_terminated_cases` |
| 破产 / 重整 | 破产重整 | `mcp__qcc-risk__get_bankruptcy_reorganization` |
| 经营异常 | 经营异常 | `mcp__qcc-risk__get_business_exception` |
| 严重违法 | 严重违法失信 | `mcp__qcc-risk__get_serious_violation` |
| 行政处罚 / 重大处罚 | 行政处罚 | `mcp__qcc-risk__get_administrative_penalty` |
| 股权冻结 | 股权冻结 | `mcp__qcc-risk__get_equity_freeze` |
| 股权出质 | 股权出质 | `mcp__qcc-risk__get_equity_pledge_info` |
| 欠税 | 欠税公告 | `mcp__qcc-risk__get_tax_arrears_notice` |
| 税务异常 / 税务违法 | 税务异常 / 税收违法 | `mcp__qcc-risk__get_tax_abnormal` / `mcp__qcc-risk__get_tax_violation` |
| 受益所有人 / UBO | 受益所有人 | `mcp__qcc-company__get_beneficial_owners` |
| 实控人 / 实际控制人 | 实际控制人 | `mcp__qcc-company__get_actual_controller` |
| 主要人员 / 董监高 | 主要人员 | `mcp__qcc-company__get_key_personnel` |
| 抽查检查 / 双随机 | 双随机抽查 | `mcp__qcc-operation__get_random_check` |
| 吊销 | （登记状态字段判断）| 调 `mcp__qcc-company__get_company_registration_info` 取"登记状态" |
| 资不抵债 | （资产负债率字段判断）| 调 `mcp__qcc-company__get_financial_data` 判断负债率 > 100% |

---

# 企业破产预警与破产重整监控 · 企查查 MCP V2.0 增强版

## SKILL 定位

本 SKILL 服务于债权人对重要客户 / 债务人 / 担保方的破产风险持续监控需求，覆盖两个紧密关联的子场景：

- **子场景一：破产预警**（pre-bankruptcy）—— 企业尚未进入正式破产程序，SKILL 通过 7 大先行指标识别破产概率，为债权人抢跑"加速回收 / 资产保全 / 诉讼抢先"提供预警时间窗
- **子场景二：破产重整预警**（restructuring-alert）—— 企业已进入或即将进入破产重整 / 破产清算，SKILL 跟踪程序节点并推算债权申报窗口期

V2.0 相对 V1.0 的最大升级在于新增"核心人员画像"维度——实控人限制出境、法代更替等个人层信号常常**早于**企业层正式的破产申请出现，成为破产识别的"先行指标中的先行指标"。V1.0 仅依赖企业层 `get_bankruptcy_reorganization` 和 `get_liquidation_info` 两个工具，这两者只能识别"已经进入正式破产程序"的企业——对债权人而言已经丧失先机。

## MCP 依赖与配置

必选：
- `qcc-company`（企业基座）—— 工商登记 × `get_financial_data` × 对外投资
- `qcc-risk`（风控大脑）—— `get_bankruptcy_reorganization` + `get_liquidation_info` + 失信 / 被执行 / 限高 / 终本 / 股权冻结

强烈建议：
- `qcc-history`（历史存档）—— 识别"历史修复过但近期再次出险"的重复型破产风险
- `qcc-executive`（人员画像）—— **核心破产先行指标**：法代个人被执行 / 实控人限制出境 / 核心高管批量离任

## 通用执行原则

**第一，破产先行指标权重高于破产程序本身。** 当企业已经出现在 `get_bankruptcy_reorganization` 的查询结果里时，对债权人来说往往已经错过最佳保全时机。SKILL 的核心价值是在正式破产程序前 6-24 个月通过先行指标发出预警。

**第二，法代与实控人是分离判断的。** 法代已更替但实控人仍在位 vs 实控人已被追责但法代仍在位，风险含义完全不同。前者可能是"职业清算人接手、企业转入被动清算模式"，后者可能是"实控人急流勇退、企业被动继续经营"。两者触发的推荐 Action 差异显著。

**第三，重整 vs 清算的分叉点必须识别清楚。** 破产重整（Chapter 11 式）意味着企业有重生可能，普通债权的清偿率可能达到 20-40%；破产清算（Chapter 7 式）意味着企业将被肢解变卖，普通债权清偿率通常 5-15%。SKILL 通过财务底盘 × 司法泥潭 × 实控人现状三元组合预判分叉路径。

**第四，债权申报窗口期不容错过。** 根据中国《企业破产法》，债权申报期不少于 30 日不超过 3 个月，由人民法院指定。错过申报期的债权虽可补充申报但优先级降低。SKILL 必须根据 MCP 返回的破产受理公告日期动态计算最晚申报日。

**第五，担保债权 vs 普通债权的区分。** 有财产担保的债权享有优先清偿权，SKILL 对持有担保权益的债权人和普通债权人需给出不同的 Action 建议。

## 工作流

### 维度一：破产先行指标扫描（V2.0 核心新能力）

**7 大先行指标**：

| 序号 | 指标 | 工具 | 警戒阈值 | 致命阈值 |
|------|------|------|---------|---------|
| 1 | 失信被执行人累计 | `mcp__qcc-risk__get_dishonest_info` | > 50 条 | > 200 条 |
| 2 | 终本案件未履行金额 | `mcp__qcc-risk__get_terminated_cases` | > 1 亿元 | > 10 亿元 |
| 3 | 股权冻结扩散 | `mcp__qcc-risk__get_equity_freeze` | > 10 条 | > 50 条 |
| 4 | 法代个人被执行 | `mcp__qcc-executive__get_personnel_judgment_debtor` | > 0 条（任何命中）| — |
| 5 | 实控人限制出境 | `mcp__qcc-executive__get_personnel_exit_restriction` | > 0 条（任何命中）| — |
| 6 | 连年失信模式 | `mcp__qcc-history__get_historical_dishonest` | 近 3 年每年新增 | 近 5 年每年新增 |
| 7 | 资产负债率 | `mcp__qcc-company__get_financial_data` | > 100% | > 150% |

**破产概率分级**：
- 命中 0-1 个警戒阈值：低破产风险（破产概率 < 10%）
- 命中 2-3 个警戒阈值：中破产风险（破产概率 10-30%）
- 命中 ≥ 4 个警戒阈值 或 任一致命阈值：**高破产风险（破产概率 > 50%）**
- 命中 ≥ 2 个致命阈值：**极高破产风险（破产概率 > 80%）**

### 维度二：正式破产程序识别

工具链：
- `mcp__qcc-risk__get_bankruptcy_reorganization` — 破产重整申请 / 受理 / 裁定
- `mcp__qcc-risk__get_liquidation_info` — 清算信息（包括清算组成员）
- `mcp__qcc-risk__get_cancellation_record_info` — 注销备案（清算后注销）
- `mcp__qcc-risk__get_simple_cancellation_info` — 简易注销

**识别内容**：
- 破产程序状态：是否已受理、是否已宣告、是否已终结
- 程序类型：破产重整 / 破产和解 / 破产清算 / 自愿清算
- 关键节点日期：申请日、受理日、宣告日、第一次债权人会议、重整计划表决日、重整期限等

### 维度三：核心人员跑路信号

工具链：
- `mcp__qcc-executive__get_personnel_exit_restriction` — 实控人 / 法代被限制出境（跑路风险最强信号）
- `mcp__qcc-executive__get_personnel_dishonest` + `get_personnel_judgment_debtor` — 个人失信被执行
- `mcp__qcc-executive__get_personnel_high_consumption_ban` — 个人限高
- `mcp__qcc-history__get_historical_legal_rep` — 法代更替时间线

**判定标准**：
- 实控人限制出境 → **已跑路或已准备跑路，破产概率极高**
- 法代 6 个月内连续更替 → **正在切割责任链，破产已进入倒计时**
- 法代更替后新任者为"职业清算人型"（MCP 零负面 + 接手时间短）→ **企业已进入被动清算模式**
- 核心高管 3 个月内 ≥ 3 人离任 → **内部已知情，正在提前撤离**

### 维度四：重整 vs 清算分叉预判

基于以下三元组合预判企业将走向重整还是清算：

| 组合 | 特征 | 预判 |
|------|------|------|
| 财务负债率 < 200% + 主营业务仍有经营价值 + 实控人未被追责 | "重生希望" | **重整**（清偿率 25-45%）|
| 财务负债率 > 200% + 主营业务已萎缩 + 实控人已被追责 / 出走 | "无人接手" | **清算**（清偿率 5-15%）|
| 财务负债率 100-200% + 业务尚可 + 实控人在位但财务压力大 | "被动重整" | **重整但可能失败**（清偿率 10-30%）|

### 维度五：债权申报窗口期计算

一旦 MCP 返回"破产受理"信号，立即根据受理公告日推算：

```
债权申报窗口 = 破产受理公告日 + 法院指定期限
                其中法院指定期限 = 30 日（最短） ~ 3 个月（最长）

典型 Action 时限：
- T+3 日内：提交债权申报材料初稿
- T+7 日内：正式向清算组 / 管理人提交债权申报
- T+30 日内：跟进第一次债权人会议
```

**重要提示**：如 SKILL 检测到"破产受理"事件发生在 30 日前且本机构尚未申报，立即升级为 S 级预警。

## 预警分级 × 推荐 Action

| 预警级别 | 触发条件 | 推荐 Action |
|---------|---------|------------|
| **L0（无风险）** | 先行指标全绿 + 无正式破产程序 | 标准贷后周期监测 |
| **L1（警戒）** | 命中 2-3 个警戒阈值 | T+7 内召集风控会议，评估是否提前介入加速回收 |
| **L2（高风险）** | 命中 ≥ 4 警戒 或 任一致命 | T+3 内立即启动诉前保全 + 上报分行风险管理部 |
| **L3（极高风险）** | 命中 ≥ 2 致命 或 法代 / 实控人出险 | **T+24h 内**紧急三方会议 + 重分类为"可疑类"贷款 + 准备债权申报材料 |
| **L4（已破产）** | `get_bankruptcy_reorganization` 返回 > 0 或 `get_liquidation_info` 返回 > 0 | **T+0 立即**提交债权申报 + 根据受理日推算窗口期 |

## 输出模板

- 章节 1：**执行摘要 · 破产预警 Decision Pack**（预警级别 + 破产概率 + 重整/清算预判 + T+0/T+3/T+7 Action）
- 章节 2：数据来源与互证方法
- 章节 3：被监控主体基本信息
- 章节 4：**7 大破产先行指标扫描结果**
- 章节 5：正式破产程序状态（如已进入）
- 章节 6：核心人员跑路信号分析
- 章节 7：重整 vs 清算分叉预判
- 章节 8：债权申报窗口期计算（如已受理）
- 章节 9：预警分级结论 × 推荐 Action 清单
- 章节 10：数据来源、采集时间戳、下次监控日建议

## 参数

- `--scenario <warning|restructuring|both>`：监控场景模式（默认 both——同时输出预警 + 重整两个子场景分析）
- `--claim-amount <金额>`：本机构持有的债权金额（用于债权申报金额测算）
- `--claim-type <secured|unsecured>`：债权类型（有担保 / 无担保，影响清偿率预测）
- `--format md|docx|pptx`：输出格式，默认 md

## 边界与免责

破产先行指标基于统计规律，命中警戒阈值不等于企业一定破产——部分主体可能通过资产重组、第三方收购、债务重组等方式成功修复。SKILL 输出的破产概率为"基于历史类似特征主体的统计推断"，不构成对特定主体破产行为的确定性预测。

重整可行性预判是方向性判断，最终是否启动重整由法院和主要债权人决定。SKILL 的预判仅为决策支持，不可替代专业法律顾问的意见。

债权申报的法律时效和程序要求以 MCP 返回的实时公告日期为准，但 MCP 更新可能有 T+1 至 T+3 的延迟。**正式法律操作应以人民法院公告原文为准**，不得仅依赖 MCP 日期。

---

**SKILL 版本**：v2.0（MCP V2.0 升级版 · 整合 #15 破产预警 + #26 破产重整预警）
**适配 MCP 版本**：146 工具 / 6 Server 全量版
**所需 Server**：qcc-company（必选）、qcc-risk（必选）、qcc-history（强烈建议）、qcc-executive（强烈建议）
