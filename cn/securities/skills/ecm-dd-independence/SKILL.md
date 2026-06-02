---
name: ecm-dd-independence
title: ecm-dd-independence
description: 资本市场尽职调查 Skill：发行人独立性核查（对应《编报规则第 12 号》第 4 章）。 当用户提到以下场景时触发：独立性、五独立、资产独立、业务独立、人员独立、财务独立、 机构独立、资产完整、业务完整、完整的业务体系、直接面向市场独立持续经营、 控股股东依赖、实控人依赖、关联方依赖、高管兼职、一套人马两块牌子、 财务核算独立、独立银行账户、独立纳税、独立财务制度、独立机构设置、 独立董事会 / 监事会 / 股东会、与控股股东资金混同、与关联方业务混同、 非独立性问题、独立性瑕疵、整改承诺、独立性意见、 independence DD、five-independence check、substantive independence 等。 典型输入：资产权属证明（土地 / 房产 / 知识产权 / 主要设备）、董监高及财务人员兼职情况说明、 财务管理制度、独立的银行账户证明、独立纳税证明、组织机构图、内部部门设置文件、 关联交易协议（关联方依赖评估输入）、同业竞争说明、历史期对控股股东资金拆借清理证明、 独立性整改承诺函。 非触发边界：具体的关联交易和同业竞争问题归 ecm-dd-related-party（本 skill 依赖其产出 做重大依赖判断）；股东 / 实控人本身的身份穿透归 ecm-dd-shareholders；董监高的任职资格 归 ecm-dd-directors（本 skill 只关注高管兼职对独立性的影响）；业务资质和合法合规归 ecm-dd-business；资产权属本身归 ecm-dd-assets；财务核算会计准则问题由会计师主导； 五独立审查的主责主体是法律 + 会计联合完成，本 skill 承担法律视角的独立性核查。 即使用户只说"帮我看一下这家公司和大股东的独立性""能不能过五独立"，也应触发本 skill。
author: zeweihan
author_url: https://github.com/zeweihan/A-market-ecm-lawyer-plugin/tree/main/skills/ecm-dd-independence
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: securities
language: zh
---

# ecm-dd-independence

## 定位与边界

本 skill **负责**：
- 综合评价发行人是否具备"**完整的业务体系**"和"**直接面向市场独立持续经营的能力**"
- 按五独立维度（资产完整、业务独立、人员独立、财务独立、机构独立）逐一核查
- 评价发行人对控股股东 / 实控人 / 关联方是否存在**实质依赖**
- 识别历史期独立性瑕疵（资金混同、人员混同、资产混同）并核查整改情况
- 出具编报规则第 4 章、《注册办法》第 12 条对应的 DD Memo
- 作为**横向 skill**，综合其他 DD skill 的输出形成最终独立性结论

本 skill **不负责**：
- 关联交易 / 同业竞争本身（归 `ecm-dd-related-party`；本 skill 依赖其输出评价重大依赖）
- 股东 / 实控人本身的身份和股权结构（归 `ecm-dd-shareholders`）
- 董监高本人的任职资格（归 `ecm-dd-directors`；本 skill 关注兼职对独立性的影响）
- 业务资质和合法合规（归 `ecm-dd-business`；本 skill 关注业务对关联方的依赖）
- 资产权属本身（归 `ecm-dd-assets`；本 skill 关注资产是否完整、独立配置）
- 会计核算 / 财务报表层面的财务独立性（由会计师主导；本 skill 关注法律意义上的财务独立制度）
- 文件读取 / 搬运（归 `ecm-dd-file-review` / `ecm-setup-file-organize`）

## 免责声明

本 skill 产出的 DD Memo 为工作底稿，不构成最终法律意见。完整免责声明见
[DISCLAIMER.md](../../DISCLAIMER.md)。

## 资深律师执行标准

执行本 skill 时，必须同时遵循 [senior-lawyer-execution-standards.md](../../shared/templates/senior-lawyer-execution-standards.md)。本 skill 的任何输出不得突破四条底线：事实可追溯、法源可核验、风险可分级、建议可落地；无法核验时必须显式标注。

## 本 skill 的实务加固点

- **五独立逐项判断**：资产、人员、财务、机构、业务独立必须分别引用底稿和其他 DD Memo，不得合并笼统结论。
- **资金与账户核查**：重点核查资金占用、共用账户、代收代付、关联方垫款和财务人员兼职。
- **业务依赖识别**：关联采购销售、共用渠道、共用品牌技术、客户供应商重合需判断是否削弱独立经营能力。
- **高风险触发器**：重大资金占用未解决、核心资产归属关联方、人员/财务混同、独立获客能力不足，应列高风险。

## 前置依赖

- 上游 skill（建议先完成）：
  - `ecm-dd-related-party`（关联交易、同业竞争数据）
  - `ecm-dd-directors`（董监高兼职情况）
  - `ecm-dd-assets`（资产完整性证据）
  - `ecm-dd-business`（业务完整性 / 业务依赖度）
  - `ecm-dd-debt`（资金拆借 / 对外担保证据）
- 上游：`ecm-setup-file-organize` 已完成，`文件索引表.md` 可用
- 对应目录：`02-尽职调查/02-04-独立性/`
- 对应标签：`independence`（见
  [shared/terminology/classification-labels.md](../../shared/terminology/classification-labels.md)）

## 核心工作流（五步）

1. **汇总上游 DD 输出**：从 related-party / directors / assets / business / debt 五个 skill
   的 Memo 中提取独立性相关事实，形成**五独立事实清单**
2. **生成核查要点清单**：照 [references/checklist.md](./references/checklist.md) 输出本项目清单
3. **五维度独立性评估**：按资产 / 业务 / 人员 / 财务 / 机构五个维度对照评估——是否**完整 /
   独立 / 可持续**
4. **风险分级**：按下方口径给每个问题打高 / 中 / 低，注意**复合依赖**（单项不构成高风险但
   多项叠加可能构成）
5. **结论与建议**：汇总独立性结论，对存在的依赖提出化解方案（剥离 / 采购替代 / 签署承诺 /
   规范协议 / 补决议 / 调整治理等）

## 统一风险分级口径

| 级别 | 定义 | 本 skill 场景的典型例子 |
|------|------|------------------------|
| **高（红）** | 足以构成发行 / 交易的实质性障碍 | 业务严重依赖控股股东（如主要生产 / 销售 / 采购通过控股股东进行）；核心资产仍在控股股东名下未划转；存在"一套人马两块牌子"、高管大量兼职控股股东单位；与控股股东存在重大资金混同（集中收付 / 长期拆借）未清理；财务核算体系依赖控股股东财务共享；申报时仍有非经营性资金占用 / 违规担保未清理 |
| **中（黄）** | 程序或文件存在瑕疵但可补正 | 少量关联交易未履行决策程序但可补决议；部分资产仍在关联方名下但可短期内完成划转；少数高管兼职控股股东单位的非核心职务；历史期存在资金拆借但已规范清理并出具承诺 |
| **低（蓝）** | 不影响实质的形式瑕疵 | 历史期共用办公场地但已规范租赁；历史期共用网络 / 门禁系统但已独立；少量关联采购但金额小且可替代；披露口径表述不严谨 |

## 输出格式契约（强制）

严格遵循 [shared/templates/dd-skill-template.md](../../shared/templates/dd-skill-template.md) 的
"输出格式契约"五段式结构：

1. 一级标题：`# DD Memo：发行人的独立性`
2. 二级标题：`一、核查要点清单` / `二、审阅发现` / `三、风险分级汇总` / `四、结论与建议` / `五、参考资料`
3. 风险等级列取值限"高 / 中 / 低"
4. 输出落地：`02-尽职调查/02-04-独立性/DD-Memo-独立性-{YYYYMMDD}.md`

**额外要求**（本 skill 专属）：

1. Memo 中必须附**五独立对照评估表**，按"资产完整 / 业务独立 / 人员独立 / 财务独立 /
   机构独立"五行，每行列：核查结论（完整 / 独立 / 存在瑕疵）/ 关键事实依据 / 上游 DD skill
   来源 / 整改情况
2. Memo 中必须附**独立性重大依赖汇总表**：依赖类型（业务 / 资产 / 人员 / 财务 / 机构）/
   依赖对象（控股股东 / 实控人 / 关联方具体名称）/ 依赖内容 / 金额或占比 / 合理性说明 /
   化解方案

## 与邻近 DD skill 的边界

| 场景 | 归属 skill | 分工说明 |
|------|-----------|---------|
| 五独立综合评价 | **本 skill** | 本 skill 的核心 |
| 关联交易 / 同业竞争本身 | `ecm-dd-related-party` | 本 skill 引用其数据做重大依赖判断 |
| 董监高兼职 | `ecm-dd-directors` | 本 skill 引用兼职事实做人员独立性判断 |
| 资产权属 | `ecm-dd-assets` | 本 skill 引用权属结果做资产完整判断 |
| 业务资质、主营业务合规 | `ecm-dd-business` | 本 skill 引用业务事实做业务完整判断 |
| 资金拆借 / 担保 | `ecm-dd-debt` | 本 skill 引用拆借事实做财务独立判断 |
| 会计核算 / 财务报表层面的独立性 | 会计师主导 | 本 skill 只关注法律层面的财务制度 |

## 参考资料索引

- [references/checklist.md](./references/checklist.md)——核查要点详细清单
- [references/regulations-index.md](./references/regulations-index.md)——本 skill 引用的法规条文索引

## 变更规则

- 输出契约变动 → MAJOR（同步改 `shared/templates/dd-skill-template.md` 和 `ecm-draft:report-assembly`）
- checklist 条目增删 → MINOR
- 法规版本更新 → PATCH（仅改 `shared/regulations/`）
