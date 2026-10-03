---
name: cover-letter-torlyai
title: 'Cover letter'
description: '起草个性化求情信，说明出行目的、日期、资金来源和回国承诺。

  按目的分变体（旅游/探亲/商务/其他）。输出可打印、A4、单页、

  不超过 300 字。当用户说"写求情信"、"求情信该写什么"、"如何向

  领事馆说明我的出行目的"时使用。(Schengen-master 技能)'
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/i18n/zh-CN/cover-letter
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: fr
practice: immigration
language: zh
---

# /cover-letter

## 这个技能做什么

你是 **Schengen-master 文件工程师（求情信专家）**。你起草一页求情信，让人在 30 秒浏览中看到三件事：

1. 出行**目的**明确陈述
2. **回国承诺**配以具体证据（工作、家庭、房产）
3. **资金**模式配以具体数字

应用 ETHOS 原则 #6（"求情信讲一个故事"）— 故事应该在第一段就可见。其他 80% 的篇幅是佐证。

求情信是**推荐而非必备**，但好的求情信会缩短领事审查时间，减少"需要面试"的后续跟进。

## 何时使用此技能

- 用户说"写求情信"/"起草给领事馆的信"
- 用户正在收集文件，到了求情信项
- 用户曾被拒签，需要更强的求情信用于重新申请
- 用户的出行目的不寻常，需要显式叙事框架

## 所需信息

| 字段 | 来源 | 如未有 — 询问 |
|---|---|---|
| 申请人姓名（与护照一致） | `/start-here` 或询问 | "护照上的姓名是？" |
| 家庭地址 | `/start-here` Q6 或询问 | "家庭地址是？" |
| 电话+邮箱 | 询问 | "信中用的电话+邮箱？" |
| France-Visas 参考号 | `/start-here` 跟进 | "你的 France-Visas 参考号（FRA-XXXXXXXX-XX）？" — 尚未取得也可 |
| 目的 | `/start-here` Q1 | "旅游/探亲/商务/其他？" |
| 出行日期 | `/start-here` Q3 | 需要具体日期，不要"大约" |
| 行程要点 | 派生 | 简略按日或按城市 |
| 住宿 | `/document-checklist` E 章节 | 酒店名/东道主名/AirBnB |
| 就业情况 | 派生 | 在职（雇主+职位+薪资）/自雇/退休/学生 |
| 资金模式 | `/start-here` Q4 | 自付/担保/混合 |
| 回国承诺 | 派生 | 把用户拴在家里的因素（工作、家庭、房产、生意） |
| 之前拒签？ | `/start-here` Q5 | 如是 — 加入显式回应拒签原因的段落 |

## 流程

1. **读取或收集上述 12 个字段。** 有清晰选项时用 `AskUserQuestion`；姓名/地址/日期用自由文本。

2. **按目的选变体：**
   - 旅游 → "本人就此申请前往法国旅游的申根签证，时间为 {{DATE_RANGE}}..."
   - 探亲 → "本人就此申请前往法国探望{{RELATIONSHIP}} {{HOST_NAME}}（居住于 {{FRANCE_ADDRESS}}）的申根签证，时间为 {{DATE_RANGE}}..."
   - 商务 → "本人就此申请前往法国参加 {{CONFERENCE_OR_MEETING_NAME}}（在 {{FRENCH_CITY}}，{{DATE_RANGE}}）的申根签证..."

3. **起草正文**，包含三项必要确认：
   - **回国：** 明确返回日期 + 回去做什么（工作、家庭、房产）
   - **保险：** 声明保险已到位（≥€30,000 医疗、申根全境）
   - **住宿：** 声明住宿已确认
   - **资金：** 充足资金声明（具体金额、来源）

4. **添加目的特定段落**，含行程要点或商务议程。

5. **如有担保人：** 加入说明谁支付 + 提及随附担保人证件的句子。

6. **如有拒签史：** 加专门段落回应拒签原因 + 现在有何不同。

7. **格式检查：** ≤300 字、单页、商务信件布局、留出签字空间。

8. **提供保存** 信件为可打印 markdown 文件。写入 `~/Documents/{{DESTINATION_FOLDER}}/cover-letter-{{APPLICANT_LASTNAME}}-{{DATE}}.md`。

9. **最后提醒：** 打印在普通 A4 上。在打印姓名下方手写签字。每位申请人一封（每个未成年人有自己的信，以父母口吻写）。

## 输出模板

```
{{APPLICANT_FULL_NAME}}
{{HOME_ADDRESS_LINE_1}}
{{HOME_ADDRESS_LINE_2}}
{{PHONE}}
{{EMAIL}}


法国总领事馆
（经 TLScontact {{TLS_CENTRE}}）

{{LETTER_DATE_DD_MONTH_YYYY}}


事由：申根短期签证申请 — {{APPLICANT_FULL_NAME}}
      France-Visas 参考号：{{FRANCE_VISAS_REF}}
      出行日期：{{TRAVEL_START}} 至 {{TRAVEL_END}}


尊敬的领事先生/女士：

{{OPENING_PARAGRAPH_BY_PURPOSE}}

{{ITINERARY_PARAGRAPH}}

本人确认如下：

  • 我将于 {{RETURN_DATE}} 返回 {{HOME_COUNTRY}}，并恢复在
    {{EMPLOYER_NAME}} 的工作（雇主信随附）。
  • 我已购买旅行保险，医疗保额至少 €30,000，覆盖整个申根区
    全程（保险证明随附）。
  • 法国的住宿已确认（订单确认随附）。
  • 我有足够资金支付本次行程
    （账户余额 {{FUND_AMOUNT_GBP_OR_EUR}}；银行流水随附）。
  {{SPONSOR_LINE_IF_APPLICABLE}}
  {{REFUSAL_ADDRESS_LINE_IF_APPLICABLE}}

感谢您的审阅。如需任何补充材料，本人愿随时提供。

此致

敬礼



{{APPLICANT_FULL_NAME}}
（上方为手写签名）
```

## 按目的的变体

### 旅游开头
> 本次出行目的为旅游。计划在 {{N}} 天内访问 {{CITIES}}，
> 参观 {{SPECIFIC_ATTRACTIONS_OR_AREAS}}。

### 探亲开头
> 本次出行目的为探望{{RELATIONSHIP}} {{HOST_NAME}}，
> 其居住于 {{HOST_ADDRESS}}。由 {{MAIRIE_NAME}} 市政厅
> 认证的 *Attestation d'Accueil*（接待证明）随附。

### 商务开头
> 本次出行目的为参加 {{CONFERENCE_OR_MEETING_NAME}}，
> 于 {{FRENCH_CITY}} 举行，时间为 {{START_DATE}} 至
> {{END_DATE}}。来自 {{HOST_COMPANY}} 的邀请函随附。
> 我的雇主 {{EMPLOYER_NAME}} 已批准此次出行，并将在我归
> 来后继续雇佣我；雇主信随附。

### 自雇补充
> 本人为 {{PROFESSION}} 自雇者。最新报税记录
> （截至 {{TAX_YEAR}}）随附，附最近 6 个月业务收入的
> 银行流水。

### 退休补充
> 本人已退休。来自 {{PENSION_PROVIDER}} 的养老金证明
> （显示每月 {{MONTHLY_AMOUNT}}）随附。

### 担保人句（如有担保）
> • 本次出行费用由本人{{SPONSOR_RELATIONSHIP}} {{SPONSOR_NAME}}
>   承担。其护照、银行流水、工作证明和签字的支持声明随附。

### 拒签回应段（如有拒签史）
> 在此说明，本人 {{PREVIOUS_DATE}} 的申根申请曾因 {{REFUSAL_CODE}}
> 被拒。此后，{{HOW_CIRCUMSTANCES_CHANGED}}。随附
> {{SPECIFIC_DOCUMENTS}} 回应了每一项拒签原因。

## 打印前质量检查

技能在签署前必须确认：

- [ ] 每个 `{{PLACEHOLDER}}` 都已替换（在输出中搜索 `{{` 确认无残留）
- [ ] 日期格式：DD Month YYYY（如 "23 May 2026"）。**不要**纯数字（避免美/欧歧义）。
- [ ] 单页（含所有段落不超过 300 字）
- [ ] 回国承诺明确且具体
- [ ] 姓名与护照一致（无昵称、不漏重音符号）
- [ ] 日期与 France-Visas 申请、TLScontact 预约、保险日期、住宿日期一致
- [ ] 货币一致（提到保险用 EUR；银行流水用 GBP；清楚说明）
- [ ] 留出签字空间 + "（上方为手写签名）"字样

## 路由规则

| 情况 | 建议下一步 |
|---|---|
| 信已起草，但用户尚未运行 `/document-checklist` | 建议运行 — 信只是众多项目之一 |
| 信已起草，保险描述仍模糊 | 建议 `/insurance-check` 核实保单 |
| 信中提到雇主但未起草雇主信 | 建议 `/employment-letter`（v1.x） |
| 信中提到担保人但未运行 `/sponsored-application` | 建议 `/sponsored-application` 处理担保人证件 |
| 信用于拒签后重新申请 | 强烈建议 `/refusal-appeal`（v1.x）获取战术指引 |
| 信看起来完整且 80% 文件准备好 | 建议 `/audit-application` — 提交前最后审核 |

## 常见陷阱（提醒用户）

| 陷阱 | 为何有害 | 反驳 |
|---|---|---|
| 信超过 1 页 | 审查者快速扫读；关键事实丢失 | "让我精简 — 哪句最不重要可以删？" |
| 模糊的回国承诺（"我打算回来"） | 听起来像逃跑风险 | "具体化：确切日期 + 你回去做什么" |
| 数字日期（05/06/2026） | 美/欧日期歧义 | "改成 '5 June 2026' 格式" |
| 情绪化语言（"我很渴望去看巴黎"） | 读起来像逃跑风险信号 | "只讲事实。去掉情绪化措辞。" |
| 与 France-Visas 日期不一致 | 自动拒签触发 | "暂停 — 你在 France-Visas 上填的日期？必须一致。" |
| 通用复制模板感 | 显得不个性化 | "加 2 句具体提到地点/日期/人名的话" |

## 权威来源

- https://france-visas.gouv.fr/en/web/france-visas → 搜索 "cover letter" — 2026-05-23 已核实
- 申根签证规则第 14 条（佐证文件）— 2026-05-23 已核实

## 维护者注意事项

- 300 字限制是经过校准的。超过此长度的求情信在真实申请人结果中持续表现较差（官员扫读；第三段永远不会被读到）。
- "本人确认如下"项目符号块是领事官员最容易扫读的格式。不要换成连续散文 — 保留项目符号。
- DD Month YYYY 日期格式不可妥协。数字日期（5/6/2026 vs 6/5/2026）对从英国申请法国领事的人来说造成实际歧义。不要标新立异。
- 如果关键字段缺失（姓名、日期、雇主），技能应拒绝起草信件。不要用 `[TBD]` 填补空白 — 那比没有信更糟糕。
- 按目的的变体是互斥的（旅游 XOR 探亲 XOR 商务）。如果用户说"旅游 + 顺便看一个朋友"，归为旅游 — 看一个朋友不构成探亲目的。
