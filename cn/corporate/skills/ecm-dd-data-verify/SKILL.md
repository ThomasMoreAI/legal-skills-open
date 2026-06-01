---
name: ecm-dd-data-verify
title: ecm-dd-data-verify
description: ECM 尽职调查工具类 Skill：调用第三方公开数据源（Tushare Pro / 企查查开放平台）与客户 提供的材料做交叉比对，发现数据不一致、未披露变更、过期信息等问题。当用户提到以下场景时 触发：外部数据验证、第三方数据核实、自动比对工商信息 / 股东 / 主要人员 / 知识产权 / 行政处罚、 用 Tushare 查财务数据 / 用企查查查工商、客户提供的营业执照 / 股东名册与外部工商档案是否一致、 API 数据比对、public data verification、cross-check 客户材料、抓取外部公开数据、 核实注册资本、核实法定代表人、核实实控人穿透、查专利 / 商标 / 软著是否真实存在、 查行政处罚记录。 典型输入：公司统一社会信用代码 / 名称 / ts_code、需比对的维度列表、客户提供的对应数据； 典型输出：数据比对报告（Markdown 表格 + 差异分析 + 建议核实清单）。 非触发边界：本 skill 是**工具类**不输出 DD Memo（五段式）；真正的合规判断由各业务 DD skill 去做。不负责文件读取（归 ecm-dd-file-review）、不负责文件搬运（归 ecm-setup-file-organize）、不做实质合规结论（归各业务 DD skill）。 即使用户未明确说"外部数据比对"，只要涉及"用 Tushare / 企查查 查 XXX 并与客户材料对比" 也应触发本 skill。
author: zeweihan
author_url: https://github.com/zeweihan/A-market-ecm-lawyer-plugin/tree/main/skills/ecm-dd-data-verify
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cn
practice: corporate
language: zh
---

# ecm-dd-data-verify

## 定位与边界

本 skill 是 **ECM DD 的工具类 skill**，和 17 个业务性 DD skill（dd-approval / dd-entity / … /
dd-compliance）有明显的职责分工：

- 业务性 DD skill **输出"合规判断"**（核查要点 + 审阅发现 + 风险分级 + 建议措施，五段式）
- 本 skill **输出"数据差异清单"**（客户数据 ↔ 外部公开数据的逐字段比对结果），供业务 DD
  skill 作为输入使用

> **⚠️ 本 skill 不套用 `shared/templates/dd-skill-template.md` 的五段式输出契约。**
> 该模板只约束业务性 DD skill。本 skill 走自己的"数据比对报告"格式。

### 本 skill 负责

- 按需求维度调用 `scripts/tushare_connector.py` / `scripts/qcc_connector.py` 取外部数据
- 将外部数据与客户材料中的对应字段做逐项比对
- 为每条差异打"高 / 中 / 低"级别（仅指**比对差异本身的严重程度**，不等同于业务风险分级）
- 输出差异清单 + 可能原因 + 建议核实措施

### 本 skill 不负责

- 合规结论——差异是否构成发行上市障碍，交由调用它的业务 DD skill 判断
- 文件读取——客户文件的 PDF/Word/Excel 读取归 `ecm-dd-file-review`
- 文件归位——归 `ecm-setup-file-organize`
- 法规解释——归 `ecm-research-reg-search` / `ecm-research-reg-study`

## 免责声明

本 skill 产出的数据比对报告仅为尽调辅助工具底稿，不构成最终法律意见。Tushare 与企查查是
第三方商业数据源，数据口径与更新频率由其运营方决定，存在滞后或偏差的可能。关键事项仍须
以政府主管部门出具的官方文件为准。完整免责声明见 [DISCLAIMER.md](../../DISCLAIMER.md)。

## 资深律师执行标准

执行本 skill 时，必须同时遵循 [senior-lawyer-execution-standards.md](../../shared/templates/senior-lawyer-execution-standards.md)。本 skill 的任何输出不得突破四条底线：事实可追溯、法源可核验、风险可分级、建议可落地；无法核验时必须显式标注。

## 本 skill 的实务加固点

- **数据不替代底稿**：Tushare、企查查等第三方数据仅作交叉验证线索，不得覆盖客户原件和官方登记信息。
- **差异分级**：主体名称、股本、股东、董监高、处罚、诉讼、经营范围等差异需按发行影响分级。
- **原始响应留存**：每次调用必须记录来源、查询关键词、时间戳、接口返回和失败原因，归入数据比对底稿。
- **高风险触发器**：第三方数据出现未披露处罚/诉讼/股权冻结/经营异常，应转对应 DD skill 复核。

## 前置依赖

### 外部依赖

- Python 3.9+（脚本使用 dataclass / `from __future__ import annotations`）
- `pip install -r scripts/requirements.txt`（requests / pandas 等）
- 至少一个以下环境变量组合（缺失时自动进入 fallback）：
  - `TUSHARE_TOKEN`（Tushare Pro 账号 token）
  - `QCC_APPKEY` + `QCC_SECRET`（企查查开放平台凭证）

### 内部依赖

- `ecm-setup-file-organize`：已归位的客户文件，本 skill 据此定位"客户侧数据"
- `ecm-dd-file-review`：如需从 PDF/Word/Excel 中抽取客户侧字段值，先调用它

### 可选数据源

目前已封装的数据源：

| 数据源 | 覆盖维度 | 典型用途 |
|-------|---------|---------|
| Tushare Pro | 上市公司基础、财务指标、前十大股东、利润表 / 资产负债表 | 已上市标的反查、财务口径核验 |
| 企查查 | 工商基础、股东及出资、主要人员、工商变更、知识产权、行政处罚 | 全量非上市标的核验（发行人自身 / 股东 / 子公司 / 关联方） |

## 核心工作流（五步）

### 第 1 步：明确比对维度

和律师确认本次需要比对的维度。ECM DD 场景常见的 6 大维度：

| 维度 | 对应字段 | 数据源优先级 |
|------|---------|-------------|
| 工商基本信息 | 企业名称、统一社会信用代码、注册资本（实缴 / 认缴）、成立日期、注册地址、经营范围、法定代表人、登记机关、企业状态 | 企查查 > Tushare |
| 股东信息 | 股东名称、出资额、持股比例、出资方式、出资日期 | 企查查（穿透）+ Tushare（上市公司前十大） |
| 主要人员 | 法定代表人、董事、监事、高管 | 企查查 + Tushare `stock_company` |
| 知识产权 | 专利号、商标注册号、软著登记号、权利人 | 企查查 |
| 行政处罚 | 处罚机关、处罚日期、处罚事由、处罚结果 | 企查查 |
| 财务数据 | 营业收入、净利润、资产总额、负债总额、股东权益、ROE | Tushare（仅上市公司） |

不在列表里但用户要求的维度，应以"可扩展点"加入 `references/dimensions-registry.md`。

### 第 2 步：凭证预检

使用对应脚本的 `--smoke` 模式检查凭证：

```bash
python scripts/tushare_connector.py --smoke
python scripts/qcc_connector.py --smoke
```

- **两个都没凭证**：直接跳到第 5 步的"fallback 路径"，不要伪造数据
- **只有一个有凭证**：走可用那个的维度，另一个相关维度进 fallback

### 第 3 步：取客户侧数据

对于每个维度，先确定"客户说什么"：

1. 从 `02-尽职调查/02-02-主体资格/` 等目录读取相关文件（由
   [ecm-dd-file-review](../ecm-dd-file-review/SKILL.md) 完成）
2. 从已完成的业务 DD skill 的 Memo 里摘取字段（如已运行 dd-entity，可从其 Memo 抽注册资本）
3. 直接由律师口头告知（适用于快速核对场景）

把客户侧数据整理成结构化表格写入 `references/client-data-staging.md`（工作区临时文件），
明确每个值的来源。

### 第 4 步：调用 API 取外部数据

按维度调用 connector。**推荐脚本方式**（可追溯 + 留日志）：

```bash
# 工商基础 + 股东 + 处罚
python scripts/qcc_connector.py \
    --basic "腾讯科技（深圳）有限公司" \
    > 05-底稿和附件/数据比对/qcc_basic_$(date +%Y%m%d_%H%M%S).json

# 已上市标的：基础 + 财务
python scripts/tushare_connector.py \
    --ts-code 600519.SH --fields full \
    --period 20241231 --financials
```

**库方式**（供编排脚本使用）：

```python
from scripts.qcc_connector import QccClient, MissingCredentialError
c = QccClient()
try:
    basic = c.company_basic("腾讯科技（深圳）有限公司")
    keyno = basic["Result"][0]["KeyNo"]
    shareholders = c.shareholders(keyno)
    penalty = c.penalty(keyno)
except MissingCredentialError:
    # 跳到 fallback
    ...
```

所有原始响应 **留痕**到 `05-底稿和附件/数据比对/` 目录，保留到项目归档。

### 第 5 步：逐字段比对 + 输出报告

按下方"输出格式契约"生成 Markdown 报告。差异分级规则：

| 级别 | 含义 | 典型情形 |
|------|------|---------|
| **高** | 核心字段存在实质差异，**可能触发业务级高风险** | 注册资本客户说 5000 万、API 显示 3000 万；法定代表人客户写张三、API 显示李四；实控人穿透链断裂 |
| **中** | 次要字段差异或信息滞后 | 经营范围表述不同但实质相近；最近一次变更未同步到 API（<30 天） |
| **低** | 格式 / 笔误 / 翻译差异 | 名称全角 / 半角括号差异；地址后缀"号""栋"差异；单位万元 / 元 |

**差异 ≠ 业务风险**。差异的业务意义由调用本 skill 的上层业务 DD skill 判断。

### fallback 路径（凭证 / 数据完全不可用时）

无法取到外部数据时，**绝不伪造**。改为输出"人工核对清单"：

```markdown
# 数据比对报告（fallback 模式）

> 本次比对因 [外部 API 凭证缺失 / API 返回错误 / 数据源暂时不可用]，
> 已自动降级为"人工核对清单"。以下字段需要项目组律师**手工登录相应平台**核对，
> 核对完成后把结果补充到本报告。

## 建议的人工核对渠道

- 企查查官网 https://www.qcc.com/
- 天眼查 https://www.tianyancha.com/
- 国家企业信用信息公示系统 https://www.gsxt.gov.cn/
- 裁判文书网 https://wenshu.court.gov.cn/
- 证监会行政处罚库 http://www.csrc.gov.cn/pub/zjhpublic/ (搜索"行政处罚决定书")

## 待人工核对字段清单

| 维度 | 字段 | 客户侧数据 | 官方口径（待核对） | 核对结果 |
|------|------|-----------|-------------------|---------|
| 工商 | 注册资本 | 5000 万元 | （待核对） | |
| 工商 | 法定代表人 | 张三 | （待核对） | |
| ... | ... | ... | ... | |
```

## 输出格式契约

```markdown
# 数据比对报告：{客户简称}

> 项目：{客户简称} | 编制日期：YYYY-MM-DD | 编制人：{律师姓名}
> 数据源：{Tushare Pro / 企查查 / 二者}
> 凭证状态：{均可用 / 仅 Tushare / 仅企查查 / 均不可用（fallback 模式）}

## 一、比对维度与数据源

| 维度 | 数据源 | 抓取时间 | 原始响应存档 |
|------|-------|---------|-------------|
| 工商基本信息 | 企查查 | 2026-04-24 10:30 | 05-底稿和附件/数据比对/qcc_basic_20260424_103000.json |
| 股东信息 | 企查查 | 2026-04-24 10:31 | ... |
| 财务数据 | Tushare Pro | 2026-04-24 10:32 | ... |

## 二、比对结果汇总

| 序号 | 维度 | 字段 | 客户侧数据 | 外部数据 | 差异 | 级别 | 备注 |
|-----:|------|------|-----------|---------|------|------|------|
| 1 | 工商 | 注册资本 | 5000 万元 | 5000 万元 | 无 | - | 一致 |
| 2 | 工商 | 法定代表人 | 张三 | 李四 | 人名不同 | 高 | 建议核实最近变更 |
| 3 | 股东 | 股东 A 持股比例 | 30% | 28% | -2 个百分点 | 高 | 疑有未披露股权转让 |

## 三、差异分析

### 差异 2：法定代表人不一致
- 客户侧来源：02-02-主体资格/营业执照-20250312.pdf
- API 侧数据：企查查 2026-04-23 抓取
- 可能原因：
  1. 客户营业执照为旧版，未及时更换
  2. 外部数据源未同步最近变更
  3. 存在未披露的治理层变更
- 建议核实：向客户索取最新营业执照 + 变更登记通知书；同时查工商局在线档案

### 差异 3：股东持股比例不一致
...

## 四、建议核实事项

- **高风险项（立即核实）**：
  1. 法定代表人差异——要求客户提供最近一次变更登记完整档案
  2. 股东 A 持股比例差异——要求客户提供近两年历次股权变更协议
- **中风险项（次轮核实）**：
  - ...
- **低风险项（可一并处理）**：
  - ...

## 五、数据源局限与注意事项

- 企查查数据有 T+{N} 天滞后，本次抓取时间：2026-04-24
- Tushare 财务数据以公司披露的定期报告为准，定期报告披露前可能暂无最新季度数据
- 行政处罚维度仅覆盖公开发布的处罚决定书，部门内部处理、未公开的警示谈话等不在覆盖范围
- 关键事项仍以政府主管部门出具的官方文件为准

## 六、附件

- 05-底稿和附件/数据比对/qcc_basic_YYYYMMDD_HHMMSS.json
- 05-底稿和附件/数据比对/qcc_shareholders_YYYYMMDD_HHMMSS.json
- 05-底稿和附件/数据比对/tushare_fina_YYYYMMDD_HHMMSS.csv
- （下级业务 DD skill 可直接引用上述原始响应）
```

**契约硬性要求**：

1. 一级标题必须是"数据比对报告：{客户简称}"——供上层 Skill 识别
2. 必有"比对维度与数据源 / 比对结果汇总 / 差异分析 / 建议核实事项 / 数据源局限与注意事项"
   五个二级标题
3. 汇总表的"级别"列取值必须是"高 / 中 / 低 / -"（"-" 表示一致）
4. 输出文件放到 `05-底稿和附件/数据比对/数据比对报告-{YYYYMMDD}.md`
   （如该目录尚未建立，先按 `shared/templates/project-folder-structure.md` 创建）
5. 所有 API 原始响应必须**留痕存档**到 `05-底稿和附件/数据比对/`，不得仅贴到报告里

## 如何被其他 DD skill 调用

业务 DD skill 可以在自己的"核心工作流"里插入本 skill 作为可选前置步骤。约定：

- **调用方式**：在业务 DD skill 的 SKILL.md 里写"可选：调用 `ecm-dd-data-verify` 对 {具体字段}
  做外部数据核验"
- **传递的输入**：公司名称 / 统一社会信用代码 / ts_code、需比对的字段清单、客户侧字段值
- **接收的输出**：本 skill 生成的 Markdown 报告 + 原始响应 JSON
- **后续处理**：业务 DD skill 将"高"级差异写进自己的"审阅发现"段，"中 / 低"级差异
  作为补充材料注明

典型链路：

```
ecm-dd-entity（主体资格）
    └─ 可选调用 ecm-dd-data-verify（工商基本信息维度）
            └─ 调用 scripts/qcc_connector.py --basic
```

## 常见误用 / FAQ

- **Q：可以让本 skill 直接生成 DD Memo 吗？**
  A：不可以。本 skill 是工具，产出的是"数据差异"。业务合规判断必须由对应业务 DD skill 完成。

- **Q：API 数据和客户数据都对不上怎么办？**
  A：记为"高"级差异，写进报告的"差异分析"，并建议人工登录政府主管部门官网核对 —— 以官方
  档案为最终仲裁。

- **Q：可以把 TUSHARE_TOKEN 写到仓库的某个文件里吗？**
  A：不可以。任何形式落盘都违反本 skill 的安全约束。见 [docs/data-connectors.md](../../docs/data-connectors.md#安全约束)。

- **Q：我只想手动对一下，不想跑脚本？**
  A：可以。走 fallback 模式：不调用 API，仅输出"人工核对清单"+"建议核对渠道"。

## 参考资料索引

- [references/dimensions-registry.md](./references/dimensions-registry.md) — 6 大比对维度 + 字段级映射
- [references/report-template.md](./references/report-template.md) — 数据比对报告完整模板（含 fallback 版）
- [../../docs/data-connectors.md](../../docs/data-connectors.md) — 连接器安装、环境变量、异常分层、故障排查
- [../../scripts/tushare_connector.py](../../scripts/tushare_connector.py) — Tushare 封装
- [../../scripts/qcc_connector.py](../../scripts/qcc_connector.py) — 企查查封装

## 变更规则

- 输出契约变动（报告结构）→ **MAJOR**，同步更新所有引用本 skill 的业务 DD skill
- 新增数据源 / 新增比对维度 → **MINOR**，更新 `references/dimensions-registry.md` 和
  `docs/data-connectors.md`
- connector 脚本 API 兼容性不变的修复 → **PATCH**
