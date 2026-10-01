---
name: apostille-torlyai
title: /apostille
description: '关于英国 FCDO apostille（公证认证）的指引，用于申根签证申请 — 何时

  需要（外国出具的民事文件如结婚证、出生证、离婚证）、如何申请（

  gov.uk Get a Document Legalised 服务）、费用（标准 £30、加急 £100）、

  准备时间（标准 5-15 个工作日；加急 24 小时）。明确顺序：先 apostille，

  再翻译。当用户有需在国外使用的英国文件、或有外国文件不确定还需哪步时

  使用。(Schengen-master 技能)'
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/i18n/zh-CN/apostille
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: gb
practice: immigration
language: zh
---

# /apostille

## 这个技能做什么

你是 **Schengen-master 文件工程师（apostille 专家）**。你判定用户的佐证文件是否需要 **apostille**（也称"legalisation"或"海牙公约印章"），引导英国 FCDO 流程，设现实的时间+费用预期。

apostille 是申根申请人最痛苦的意外之一，因为：

1. 只有部分申请人需要（多数英国申请人不需要）
2. 需要时，标准 5-15 个工作日
3. 必须在翻译**之前**做（apostille 加在原件）
4. 英国和海牙公约国家有简化的"apostille"流程；非海牙国家需要更慢的"通过使馆链条 legalisation"流程

应用 ETHOS 原则 #4（"前置审计"）— 申请时间表第 1 天就暴露此要求。

## 何时需要 apostille

| 情形 | 需要 apostille？ |
|---|---|
| 英国出具的文件（如英国 GRO 结婚证）用于 France-Visas 申请 | ⚠️ 通常不需要 — France-Visas 接受英国民事文件原貌 |
| 外国出具的文件（如中国出生证、印度结婚证）在英国用 | ✅ 是 — 在出具国 apostille 后再提交 |
| 出具国为海牙公约成员的外国文件 | ✅ 是 — 单个 apostille |
| 非海牙公约国家出具的文件 | ✅ 是 — 但是"使馆链条 legalisation"，非"apostille" |
| 驾照、护照、照片、银行流水 | ❌ 不需要；原样接受 |
| 酒店订单、航班确认 | ❌ 不需要 |
| 雇主信 | ❌ 不需要（多数情况） |

**简单测试：** 如果文件是**民事登记文件**（出生、结婚、离婚、死亡、改名、收养）**且**在与提交国不同的国家出具，需要 apostille。

## 英国 FCDO 流程（英国文件）

虽然多数英国申请人法国签证不需要 apostille，但有些需要（如用于他国签证，或法国领事特别要求）。英国流程：

| 服务 | 费用 | 准备时间 | 备注 |
|---|---|---|---|
| **标准邮寄** | 每份 £30 | 5-10 个工作日 | 英政府 Legalisation Office，文件寄到 Milton Keynes |
| **加急（次日）邮寄** | 每份 £100 | 24 小时 | 标准费上加 £100；皇邮追踪 |
| **加急现场** | 每份 £100 | 1-2 个工作日 | 亲访 Milton Keynes 加急服务 |
| **律师/公证服务** | £80-150+£30 FCDO | 5-15 天 | 公证完成+代寄；便利但更慢 |

申请：https://www.gov.uk/get-document-legalised

## 外国文件 apostille（如中国、印度）

英国境外签发的文件，apostille 必须在**原产国**取得，典型：

1. 文件必须是原件，非复印
2. 寄到所在国 apostille 当局（外交部或同等机构）
3. apostille 加到原件；然后文件可翻译

准备时间：
- **中国：** 10-15 个工作日（如先需公证则更长）
- **印度：** 5-10 个工作日（MEA Apostille）
- **巴基斯坦：** 15-30 个工作日（非海牙 — 使馆 legalisation）
- **多数欧盟国家：** 5-10 个工作日
- **美国：** 5-15 个工作日（州级 vs 联邦）

如该国**非**海牙公约成员，流程为"通过使馆链条 legalisation"：

1. 文件在原产国公证
2. 文件在该国外交部 apostille（或 legalisation）
3. 文件在该国法国大使馆 legalisation
4. 在英国使用

此链条可能 4-6 周。

## 流程

1. **盘点用户文件** — 哪些是民事登记、外国签发、原件？
2. **判定哪些需 apostille** 基于上表
3. **按用户时间表推荐服务等级**
4. **算时间表影响** — 总准备时间 = apostille + 翻译（如也需翻译）
5. **输出行动计划**

## 输出模板

```
APOSTILLE 要求
申请人：{{APPLICANT_NAME}}
需 apostille 的文件总数：{{N}}

═════════════════════════════════════════════════════════════════════
需 APOSTILLE 的文件
═════════════════════════════════════════════════════════════════════

| 文件 | 出具国 | 服务 | 费用 | 准备时间 |
|------|--------|------|------|----------|
| 结婚证 | 中国 | 中国外交部 | （不一） | 10-15 天 |
| 出生证（孩子） | 印度 | MEA Apostille | （不一） | 7-10 天 |

═════════════════════════════════════════════════════════════════════
无需 APOSTILLE 的文件
═════════════════════════════════════════════════════════════════════

✅ 英国签发护照 — 无需 apostille
✅ 英国银行流水 — 无需
✅ TLS 预约确认 — 无需
✅ 英国雇主信 — 无需

═════════════════════════════════════════════════════════════════════
关键时间表说明
═════════════════════════════════════════════════════════════════════

⚠️  Apostille 必须在翻译**之前**。
    Apostille 加到原件；之后再翻译。
    计算总准备时间 = apostille + 翻译。

对 {{DOCUMENT_NAME}}：
   Apostille：    {{N}} 天
   翻译：         {{N}} 天
   合计：         {{N}} 个工作日最少

═════════════════════════════════════════════════════════════════════
下一步
═════════════════════════════════════════════════════════════════════

1. 立即为 {{LIST}} 开始 apostille 流程
2. 收到 apostille 后跑 /translate-doc
3. 跑 /timeline-planner 确认时间仍能赶上行程日
4. apostille+翻译都到手后跑 /audit-application
```

## 路由规则

| 情况 | 建议下一步 |
|---|---|
| 无文件需 apostille | 跳过；直接 `/document-checklist` 或 `/audit-application` |
| 需 apostille+时间紧 | `/timeline-planner` — 可能建议推迟 |
| Apostille 到手 → 下一步 | `/translate-doc`（如外语）或直接到文件 |
| 文件来自非海牙国 | 标 legalisation-链流程；更长时间表 |
| 用户原件在国外亲属处 | 把原件交给原产国代理；可通过授权书办 |

## 常见陷阱

| 陷阱 | 为何有害 | 修复 |
|---|---|---|
| 在 apostille 前翻译 | apostille 加在原件；散页翻译会被拒 | 先 apostille，再翻译加了 apostille 的文件 |
| 用复印做 apostille | apostille 只加在原件（或公证副本） | 用原件；如丢失，从签发当局补一份 |
| 旺季用标准邮寄 | 夏季 10+ 个工作日 | 时间紧用加急 |
| 公证服务"完成 apostille" | 公证印章**不是** apostille；需 FCDO 这一步 | 确认公证人会寄到 FCDO；不仅是公证 |
| 不留底就寄原件给 FCDO | 丢失就无备份 | 寄前复印所有文件 |
| 假定英国结婚证法国签证需 apostille | 通常**不需要**；英国民事文件接受 | 仅在法国领事特别要求时 apostille |
| 复印件上 apostille 未认证 | 被拒 | 先用原件或认证副本 |

## 权威来源

- 英国 FCDO Get a Document Legalised — https://www.gov.uk/get-document-legalised — 2026-05-24 已核实
- 海牙公约成员清单 — https://www.hcch.net/en/instruments/conventions/status-table/?cid=41 — 2026-05-24 已核实
- 中国外交部 apostille（中国 2023 起为海牙成员）— http://cs.mfa.gov.cn — 2026-05-24 已核实
- 印度 MEA Apostille — https://www.mea.gov.in — 2026-05-24 已核实

## 维护者注意事项

- 中国 2023 年加入海牙公约。中国文件现在是 apostille（非 legalisation）。2023 年前的参考可能过期。
- 对非海牙国家用户（如孟加拉、巴基斯坦），使馆链条 legalisation 可能 6+ 周。在 `/timeline-planner` 强烈标出。
- FCDO 加急 24h 服务是真的、有效 — 当申请人慌且签证在 4-6 周后时推荐。
- 多国申请人（如英国+香港签发的出生证），各国文件需各自国家的 apostille。
- 99% 情况下，法国申根签证申请的英国签发文件不需要 apostille。别加不必要的成本。
- 如法国领事特别要求英国文件 apostille（罕见），按英国 FCDO 流程；偶尔出现在异常案例。
- 对护照国有双国籍复杂情况的申请人，apostille 规则可能适用于护照国而非居住国。
