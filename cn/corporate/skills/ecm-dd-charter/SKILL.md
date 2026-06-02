---
name: ecm-dd-charter
title: ecm-dd-charter
description: 资本市场尽职调查 Skill：公司章程及组织机构（三会运作）核查（对应《编报规则第 12 号》第 11 章）。 当用户提到以下场景时触发：公司章程合规性、三会议事规则、股东大会议事规则、董事会议事规则、 监事会议事规则、独立董事制度、董事会专门委员会（审计、战略、提名、薪酬）、关联交易决策制度、 对外担保决策制度、对外投资决策制度、信息披露管理制度、内控制度、三会召开程序、表决程序、 会议通知、会议记录、决议有效性、公司治理结构、corporate governance、charter DD 等。 典型输入：现行公司章程及历次修订版、三会议事规则、独立董事工作制度、董事会专门委员会 实施细则、内控制度文件、近 3 年股东会 / 董事会 / 监事会的通知 / 议案 / 决议 / 会议记录 / 签到表。 非触发边界：设立时的章程归 ecm-dd-establishment；历次章程修订伴随的股本变动归 ecm-dd-history； 董监高任职资格归 ecm-dd-directors；股东身份核查归 ecm-dd-shareholders；本次发行的批准 决议归 ecm-dd-approval。 即使用户只说"帮我看下这家公司治理规范不规范"，也应触发本 skill。
author: zeweihan
author_url: https://github.com/zeweihan/A-market-ecm-lawyer-plugin/tree/main/skills/ecm-dd-charter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: corporate
language: zh
---

# ecm-dd-charter

## 定位与边界

本 skill **负责**：
- 现行公司章程（及报告期内历次修订版本）的合法合规核查
- 股东大会 / 董事会 / 监事会议事规则的完整性与合规性
- 近 3 年（报告期内）三会召开程序、表决程序、会议记录的规范性
- 独立董事制度、董事会专门委员会的运行情况
- 关联交易 / 对外担保 / 对外投资 / 募集资金管理等内控制度
- 公司治理整体评价

本 skill **不负责**：
- 设立时章程（归 `ecm-dd-establishment`）
- 历次章程修订所对应的股本变动决议（归 `ecm-dd-history`）
- 本次发行所涉决议（归 `ecm-dd-approval`）
- 董监高任职资格、兼职、变化（归 `ecm-dd-directors`）
- 股东身份 / 实控人认定（归 `ecm-dd-shareholders`）

## 免责声明

见 [DISCLAIMER.md](../../DISCLAIMER.md)。

## 资深律师执行标准

执行本 skill 时，必须同时遵循 [senior-lawyer-execution-standards.md](../../shared/templates/senior-lawyer-execution-standards.md)。本 skill 的任何输出不得突破四条底线：事实可追溯、法源可核验、风险可分级、建议可落地；无法核验时必须显式标注。

## 本 skill 的实务加固点

- **现行章程锁定**：必须确认使用经有效审议并完成备案/披露的最新版章程，不得混用历史版本。
- **公司法衔接**：重点核查股东会、董事会、审计委员会/监事会、法定代表人、出资期限和利润分配条款。
- **上市规则衔接**：拟上市或上市公司需核对章程指引、股东会规则、交易所规范运作和独董/专委会要求。
- **高风险触发器**：章程与法律强制规定冲突、反收购/特殊表决权安排未披露、三会议事规则缺失，应列高风险。

## 前置依赖

- 上游：`ecm-setup-file-organize`
- 对应目录：`02-尽职调查/02-10-公司治理/`
- 对应标签：`charter`

## 核心工作流（四步）

1. **生成核查要点清单**
2. **文件审阅与标注**：重点核查章程与《公司法》《上市公司章程指引》《上市公司股东会规则》的
   差异；三会近 3 年召开是否符合章程和议事规则
3. **风险分级**
4. **结论与建议**

## 统一风险分级口径

| 级别 | 定义 | 本 skill 场景的典型例子 |
|------|------|------------------------|
| **高（红）** | 实质性障碍 | 章程条款与《公司法》强制性规定冲突（如限制股东法定权利）、报告期内重大决议程序违法（如应经股东大会未经股东大会）、近 3 年全部未召开股东大会 |
| **中（黄）** | 瑕疵但可补正 | 议事规则部分条款缺失、独立董事未按期述职、董事会专门委员会未按期开会、内控制度文件未及时更新、会议记录要素不全 |
| **低（蓝）** | 形式瑕疵 | 章程个别表述与最新监管指引不完全一致、会议文件归档顺序混乱、签到表复印件盖章轻微模糊 |

## 输出格式契约（强制）

严格遵循 [shared/templates/dd-skill-template.md](../../shared/templates/dd-skill-template.md)。
落地：`02-尽职调查/02-10-公司治理/DD-Memo-公司治理-{YYYYMMDD}.md`

## 参考资料索引

- [references/checklist.md](./references/checklist.md)
- [references/regulations-index.md](./references/regulations-index.md)

## 变更规则

- 输出契约变动 → MAJOR
- checklist 条目增删 → MINOR
- 法规版本更新 → PATCH
