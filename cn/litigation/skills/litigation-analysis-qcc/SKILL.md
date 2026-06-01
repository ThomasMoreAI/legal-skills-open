---
name: litigation-analysis-qcc
title: 诉讼风险评估 · 企查查 MCP V2.0 增强版
description: '诉讼风险评估 SKILL · 企查查 MCP V2.0 增强版。 对目标企业执行"企业现状 + 企业历史 + 核心人员"三层诉讼全景扫描，输出可直接用于立案决策、授信决策、投资决策的司法风险评估报告。

  核心能力： - 三层诉讼全景：企业现状（17 个 qcc-risk 工具） + 企业历史（14 个 qcc-history 工具） + 核心人员（18 个 qcc-executive 工具） - 时间序列趋势：基于历史裁判文书 / 立案 / 开庭公告做近 5-10 年真实趋势分析 - 执行能力诊断：被执行 / 失信 / 限高 / 终本 × 现状 × 历史双层，识别"修复型主体"与"连年失信型主体" - 核心人员诉讼档案：法代 + 实控人 + 董事长 + 总经理的个人涉诉全景 - 风险敞口精算：未结案件潜在赔付、执行案件待履行金额、占注册资本比例

  适用场景：立案前对手方核查 / 授信尽调 / 投资尽调 / 供应商准入 / 客户信用评估 / 破产预警。

  使用方式：/litigation-analysis-qcc 企业名称 [--period 近N年] [--type 合同纠纷|劳动争议|知识产权|...] [--person-scan 是否对核心人员做诉讼档案]'
author: duhu2000
author_url: https://github.com/duhu2000/financial-services-qcc/tree/main/skills/litigation-analysis-qcc
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: litigation
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

# 诉讼风险评估 · 企查查 MCP V2.0 增强版

## SKILL 定位

本 SKILL 服务于立案前对手方核查、授信尽调、投资尽调、供应商准入、客户信用评估、破产预警等场景的涉诉深度分析需求。输入目标企业全称或统一社会信用代码后，SKILL 自动执行"企业现状 × 企业历史 × 核心人员"三层扫描，识别活跃诉讼、历史诉讼、执行风险、关键人员个人涉诉，最终输出综合诉讼风险评级与决策建议。

V2.0 相对旧版的最大变化是引入"历史"与"核心人员"两个独立维度。旧版受限于 MCP 只能拉到当前数据，只能以发布日期做粗糙的年份切分做趋势近似；V2.0 可以直接调取历史数据接口，形成真实的时间序列，并对关键人员做个人诉讼档案，真正实现"企业层面看不到的风险信号，从人员和历史两个侧面把它揪出来"。

## MCP 依赖与配置

SKILL 运行前必须确保以下 MCP Server 已配置：

必选：
- `qcc-risk`（风控大脑，34 工具）—— 当前司法记录全量
- `qcc-history`（历史存档，34 工具）—— 本 SKILL 核心数据源之一，提供 5-10 年真实诉讼时间序列

强烈建议开通：
- `qcc-executive`（人员画像，42 工具）—— 核心人员诉讼档案维度，缺少此 Server 时 SKILL 仍可运行但输出不包含维度六
- `qcc-company`（企业基座）—— 获取注册资本、实控人、主要人员名单，用于敞口计算与人员锁定

详细配置方法参见 `docs/MCP_CONFIGURATION.md`。

## 通用执行原则

**第一，不止于统计数量。** 诉讼分析的核心不是"多少件案子"，而是"案件的性质、金额、角色、结果"。一家企业 100 件小额劳动争议（作为被告）与 10 件证券虚假陈述集体诉讼（作为被告）的风险等级不在一个量级。SKILL 输出必须拆分到案件性质层面，不得仅呈现汇总数字。

**第二，涉诉金额与注册资本比必算。** 涉案总金额占注册资本的比例是诉讼是否"致命"的最直接衡量指标。30% 以下属于可承受区间，30-50% 是警戒区间，50% 以上属于可能触发资本重组的水位。SKILL 必须在摘要位置呈现这一指标。

**第三，历史数据必须入表。** 仅看当前数据的诉讼分析会低估累积风险。V2.0 MCP 的 qcc-history 工具链允许直接查询近 10 年的历史裁判文书 / 立案 / 开庭 / 终本 / 失信，这些数据与现状数据合并计算才构成真实的诉讼密度。

**第四，未结案件的风险敞口必须量化。** 每一件被告方未结案件都是潜在赔付敞口。SKILL 必须对"最可能判赔金额"做合理估算（可按起诉金额的 30-70% 估算，具体比率依案件性质调整），形成"未结敞口 + 执行敞口 + 合计敞口"三项报表数据。

**第五，核心人员涉诉不可缺失。** 企业诉讼数据可能因主体变更、注销、子公司隔离而"被漂白"，但核心人员的个人涉诉是跟人走的、难以漂白。以核心人员为主体做独立诉讼档案是识别"僵尸企业表面清洁、实控人跑路"类隐性风险的关键手段。

**第六，数据时效必须明示。** 所有输出项均须标注 MCP 采集时间戳，尤其是开庭公告、立案信息等具有明确日期属性的数据项。

## 工作流

### 维度一：涉诉全景 × 历史累积

**目标**：全量盘点目标企业从成立至今的涉诉情况，形成"当前 + 历史"双层数据。

工具链：

企业现状（qcc-risk）：
- `mcp__qcc-risk__get_judicial_documents` — 裁判文书
- `mcp__qcc-risk__get_case_filing_info` — 立案信息
- `mcp__qcc-risk__get_hearing_notice` — 开庭公告
- `mcp__qcc-risk__get_court_notice` — 法院公告
- `mcp__qcc-risk__get_service_notice` — 送达公告
- `mcp__qcc-risk__get_pre_litigation_mediation` — 诉前调解

企业历史（qcc-history）：
- `mcp__qcc-history__get_historical_judicial_docs` — 历史裁判文书
- `mcp__qcc-history__get_historical_case_filing` — 历史立案
- `mcp__qcc-history__get_historical_hearing_notice` — 历史开庭公告
- `mcp__qcc-history__get_historical_court_notice` — 历史法院公告
- `mcp__qcc-history__get_historical_service_notice` — 历史送达公告
- `mcp__qcc-history__get_historical_pre_litigation_mediation` — 历史诉前调解

产出：一张"涉诉全景总表"，按"作为原告 / 作为被告 / 作为第三人"三角色、按案件性质（合同 / 劳动 / 知产 / 股权 / 债务 / 侵权 / 行政 / 其他）交叉分布，同时区分"已结 / 未结 / 执行中"三种状态；另附"案件密度"指标（年均案件数、每 N 个月一起的诉讼频率）。

### 维度二：案件性质深度分类

**目标**：按案件性质（案由）做风险特征解读，不同案由对应不同的业务风险模型。

分析要点：

合同纠纷高发 —— 反映履约能力不足 / 客户质量偏差 / 合同管理混乱，是经营类风险的直接信号。如果作为被告的合同纠纷占比超过 50%，需要把"履约能力"列为独立质疑项。

劳动争议集中 —— 反映用工合规瑕疵（未缴社保 / 未签合同 / 加班费争议等）。劳动争议单案金额不高但批量发生时对企业品牌和招聘端的隐性冲击大。作为被告的劳动仲裁 + 诉讼超过 20 件 / 年，原则上触发劳动合规专项审查。

知识产权纠纷 —— 需细分角色：作为原告通常意味着企业具备 IP 防御能力，属中性甚至正面信号；作为被告（被指侵权）则直接威胁产品上市与营收，单案赔付可能达到数百万至上亿元级别，须立即评估胜诉概率与赔付敞口。

股权 / 公司纠纷 —— 内部治理不稳定的直接信号。如果股权纠纷发生在实控人 / 大股东之间，可能直接导致控制权变动，对长期合作与投资为严重负面信号。

债务纠纷 —— 现金流紧张的前哨信号。结合被执行记录一起看，债务纠纷从几起上升到几十起意味着企业已进入债务危机阶段。

侵权 / 行政 / 环保类 —— 合规风险信号，结合是否上市、是否拟 IPO 综合判断，在 IPO 审核周期内这类纠纷可能致命。

### 维度三：执行风险双层扫描

**目标**：拆分"当前执行风险"与"历史执行痕迹"两层，区分活跃风险与修复型风险。

工具链：

当前执行风险（qcc-risk）：
- `mcp__qcc-risk__get_judgment_debtor_info` — 当前被执行人
- `mcp__qcc-risk__get_dishonest_info` — 当前失信被执行人
- `mcp__qcc-risk__get_high_consumption_restriction` — 当前限制高消费
- `mcp__qcc-risk__get_terminated_cases` — 当前终本案件
- `mcp__qcc-risk__get_exit_restriction` — 当前限制出境（关联人员）
- `mcp__qcc-risk__get_equity_freeze` — 股权冻结

历史执行痕迹（qcc-history）：
- `mcp__qcc-history__get_historical_dishonest` — 历史失信被执行人
- `mcp__qcc-history__get_historical_judgment_debtor` — 历史被执行人
- `mcp__qcc-history__get_historical_high_consumption_ban` — 历史限高
- `mcp__qcc-history__get_historical_terminated_cases` — 历史终本案件
- `mcp__qcc-history__get_historical_equity_freeze` — 历史股权冻结

**分析要点**：

当前执行层以三色信号呈现。任何一项当前失信未履行、限高生效、股权冻结未解除均直接触发 C 级或更低评级。

历史执行层的解读更为微妙。历史失信已全部履行可以视为"信用修复"的正面信号——尤其是对于创业期经历过困境但度过危机的企业。但历史失信次数 ≥ 3 次即便全部已履行，也反映企业长期存在"判决后不主动履行"的行为模式，是信用评估的加重因素。

"终本案件"的信号价值往往被低估。终本指"法院无可供执行财产、暂时结束执行程序"，并非"结案"，债务仍然存在并可申请恢复执行。历史终本 + 当前无被执行的组合通常意味着企业过了债务危机 peak 但未真正脱险，须在报告中单独说明。

### 维度四：诉讼趋势与时间序列分析

**目标**：基于历史数据做真实的 5-10 年时间序列分析，判断诉讼是否在扩大、收敛还是集中爆发。

分析要点：

按年分桶统计历史裁判文书数量、立案数量、涉案金额，形成年度 / 季度时序表。V2.0 MCP 提供的历史数据让这一统计从"基于发布日期的粗糙近似"升级为"按真实立案时间的精准分桶"。

诉讼演化形态识别：
- **平稳型**：年度诉讼数量变化在 ±20% 内，属于正常经营波动
- **收敛型**：近 2-3 年明显下降，通常对应合规改善或业务收缩，需要结合经营数据判断是"主动改善"还是"业务萎缩"
- **扩张型**：连续 2 年以上上升，尤其涉案金额增速快于案件数增速，通常预示现金流恶化或大客户违约
- **集中爆发型**：某一年突然出现历史 3 倍以上的诉讼量，常见于实控人出事、重大违约、板块塌陷事件

趋势判断须结合案件性质变化一起看。如果总数稳定但"债务纠纷 + 劳动争议 + 失信被执行"占比持续上升，即便总数没变也是恶化信号。

### 维度五：重点案件深度解析

**目标**：对涉及核心业务 / 大额标的 / 影响治理结构的重要案件做个案深度分析。

重点案件识别标准：
- 涉案金额 > 注册资本 10%
- 作为被告的未结案件
- 涉及核心资产 / 核心业务 / 核心品牌的案件
- 群体性诉讼 / 系列案件（超过 5 件同一类型 / 同一对手方）
- 与实控人 / 法定代表人直接相关的案件
- 诉讼结果可能直接影响企业上市 / 退市 / 重整的案件

对每一件重点案件输出"案由 / 角色 / 涉案金额 / 案件状态 / 判决结果（如已结） / 影响评估 / 风险提示"六项分析，并在最后形成"潜在风险敞口"汇总表：未结案件潜在赔付金额、执行案件待履行金额、合计敞口、占注册资本比例。

### 维度六：核心人员诉讼档案（V2.0 新增）

**目标**：对目标企业的法定代表人、实际控制人、董事长、总经理 4 人分别做个人涉诉档案，识别"企业表面清洁、个人已出事"类的隐性风险。

工具链（以 qcc-executive 为核心，每人调用 12-15 个工具）：

- `mcp__qcc-executive__get_personnel_judicial_docs` / `_historical_judicial_docs` — 个人裁判文书现状 × 历史
- `mcp__qcc-executive__get_personnel_case_filing` / `_historical_case_filing` — 个人立案
- `mcp__qcc-executive__get_personnel_hearing_notice` / `_historical_hearing_notice` — 个人开庭
- `mcp__qcc-executive__get_personnel_court_notice` / `_historical_court_notice` — 个人法院公告
- `mcp__qcc-executive__get_personnel_service_notice` / `_historical_service_notice` — 个人送达
- `mcp__qcc-executive__get_personnel_pre_litigation_mediation` / `_historical_pre_litigation_mediation` — 个人诉前调解
- `mcp__qcc-executive__get_personnel_judgment_debtor` / `_historical_judgment_debtor` — 个人被执行（现状 + 历史）
- `mcp__qcc-executive__get_personnel_dishonest` / `_historical_dishonest` — 个人失信（现状 + 历史）
- `mcp__qcc-executive__get_personnel_high_consumption_ban` / `_historical_high_consumption_ban` — 个人限高
- `mcp__qcc-executive__get_personnel_exit_restriction` — 个人限制出境
- `mcp__qcc-executive__get_personnel_terminated_cases` / `_historical_terminated_cases` — 个人终本
- `mcp__qcc-executive__get_personnel_property_reward_notice` — 个人财产悬赏

**分析要点**：

每人输出独立一节，包括个人诉讼时间轴、案由分布、角色比例（原告 / 被告）、是否存在硬性失信、历史已修复事件、与目标企业诉讼的重叠度（例如法代在本企业被起诉同时又在其他企业被起诉）。

核心人员个人涉诉比企业涉诉更能反映"跑路风险"。实控人或法代被限制出境 + 被执行 + 关联企业注销的组合，即便本企业看起来清洁也应立即视为 D 级。

本维度可通过 `--person-scan false` 参数关闭，但在高风险尽调项目中强烈建议开启。

## 综合评级

本 SKILL 按下列 ABCD（+F）五级输出最终诉讼风险评级。

- **A 级（可正常合作）**：无当前被执行人 / 失信；历史诉讼密度低（年均 < 2 件）；无未结重大诉讼；核心人员无个人涉诉硬性失信。
- **B 级（可合作，加强监测）**：历史被执行但已全部履行；年均诉讼 2-5 件；或有未结但标的较小的诉讼；核心人员无当前失信。
- **C 级（谨慎合作，要求担保）**：当前有被执行人或 5 年内历史失信；或年均诉讼 > 5 件；或有未结重大诉讼（金额 > 注册资本 10%）；核心人员历史上有已解除的执行事件。
- **D 级（强烈建议避免）**：当前失信被执行人；或涉诉金额 > 注册资本 50%；或存在群体性诉讼；或核心人员当前失信 / 限高 / 限出境。
- **F 级（绝对禁合作）**：诉讼泥潭级（文书数 > 5,000 份或涉案金额 > 10 亿元）；或实控人出走 / 刑事被告；或企业已注销 / 进入破产清算；任何合作关系都会带来诉讼牵连风险。

评级采用"同时触发多项以取最低"的原则，不取平均值。

## 输出模板

报告统一采用以下章节结构：

- 章节 1：**执行摘要 · Decision Pack** —— 一句话结论 + 关键判断表 + 推荐 Action（按 T+0 / T+3 / T+7 / T+14 / T+30 紧迫度排序） + 抗辩清单（预判质疑点）
- 章节 2：**数据来源与互证方法** —— 列明 qcc-risk / qcc-history / qcc-executive 各 Server 采集时间、年报 / 招股书等外部源、互证命中一览
- 章节 3：**重大风险预警**（仅在评级为 D 或 F 时出现）
- 章节 4：**诉讼全景双源对标** —— MCP 数据 vs 年报披露做双源印证，识别披露差异
- 章节 5：**涉诉案件分类与趋势**
  - 5.1 按角色分布（原告 / 被告 / 第三人）
  - 5.2 按案由分布
  - 5.3 时间序列趋势（近 10 年分年分桶）
- 章节 6：**执行风险双层扫描** —— 当前层 + 历史层
- 章节 7：**重点案件深度解析** —— Top 5-10 案件个案分析 + 潜在风险敞口汇总
- 章节 8：**核心人员诉讼档案**（每人独立成节）
  - 8.X 人员姓名（角色）
    - 个人诉讼时间轴
    - 个人硬性失信检查
    - 与企业诉讼的重叠度
    - 人员风险评级
- 章节 9：**综合评级与合作建议**
- 章节 10：**数据来源、采集时间戳、免责声明**

每个章节末尾附"深度推演"段，以业务化中文叙述阐释数据背后的判断逻辑。

## 参数

- `--period <N年>`：历史事件追溯年限，默认 10 年
- `--type <案由>`：仅分析指定案由的案件（合同纠纷 / 劳动争议 / 知识产权 / 股权争议 / 债务纠纷等），默认全量
- `--person-scan <true|false>`：是否对核心人员做诉讼档案（维度六），默认 true
- `--format md|docx|pptx`：输出格式，默认 Markdown；docx 为法务审查档案格式；pptx 为一页投委会摘要

## 边界与免责

本 SKILL 基于企查查 MCP 公开司法数据生成。数据源包括裁判文书网、立案信息、开庭公告、失信被执行人名单、终本案件等。未公开判决的涉密案件、调解协议、仲裁案件（未走司法确认）不在覆盖范围。

涉案金额估算基于起诉金额与判决结果，对"调解和解"类案件可能存在系统性高估。SKILL 报告中的"风险敞口"数据属于保守估算，正式法律尽调应由专业律师结合卷宗实质审查完成。

诉讼信息动态变化，本 SKILL 输出具有强时效性，须标注采集时间戳。合作签约、投资决策、授信审批前建议复核当期最新数据。

---

**SKILL 版本**：v2.0（MCP V2.0 升级版）
**适配 MCP 版本**：146 工具 / 6 Server 全量版（2026-04-23 发布）
**所需 Server**：qcc-risk（必选）、qcc-history（必选）、qcc-executive（强烈建议）、qcc-company（建议）
