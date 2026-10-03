# 数据比对维度登记表

> 本表是 `ecm-dd:dd-data-verify` 的**可扩展字段字典**，登记所有已支持的比对维度与字段。
> 新增维度时在此登记，并更新 SKILL.md 中的维度表。

## 维度 1：工商基本信息

| 字段 | 中文 | 企查查字段 | Tushare 字段 | 核查要点 |
|------|------|-----------|-------------|---------|
| `name` | 企业名称 | `Name` | `stock_company.company` | 字符完全一致；注意全 / 半角括号 |
| `credit_no` | 统一社会信用代码 | `CreditNo` | - | 18 位必须完全一致 |
| `registered_capital` | 注册资本 | `RegistCapi` | `stock_company.reg_capital` | 单位（万元 / 亿元 / 元）；实缴 vs 认缴 |
| `paid_capital` | 实缴资本 | `RealCapi` | - | 2014 注册资本改革后实缴非强制，但发行人要求说明 |
| `establish_date` | 成立日期 | `StartDate` | `stock_company.setup_date` | YYYY-MM-DD，比对完全一致 |
| `legal_rep` | 法定代表人 | `OperName` | `stock_company.chairman` | **高敏感字段**，不一致必须立刻核实 |
| `reg_address` | 注册地址 | `Address` | `stock_company.reg_location` | 表述微差（如"号"/"栋"）可归低级；跨区变化归高级 |
| `business_scope` | 经营范围 | `Scope` | `stock_company.business_scope` | 允许表述差异；但"新增 xx 业务"未披露属中级 |
| `industry` | 所属行业 | `Industry` | `stock_company.industry` | 证监会行业分类 vs 国标 GB/T 4754 |
| `state` | 企业状态 | `Status` | `stock_company.status` | "存续"/"注销"/"吊销" 必须一致 |
| `reg_authority` | 登记机关 | `BelongOrg` | - | 核实是否属于声称管辖区域 |

## 维度 2：股东信息

| 字段 | 中文 | 企查查字段 | Tushare 字段 | 核查要点 |
|------|------|-----------|-------------|---------|
| `partner_name` | 股东名称 | `StockName` | `top10_holders.holder_name` | 同名不同主体（重名 / 同名关联公司） |
| `stock_percent` | 持股比例 | `StockPercent` | `top10_holders.hold_ratio` | 百分比 vs 千分比单位；Tushare 常以流通股计算 |
| `should_capi` | 认缴出资额 | `ShouldCapi` | - | 与注册资本 × 持股比例的乘积应一致 |
| `real_capi` | 实缴出资额 | `RealCapi` | - | 实缴 < 认缴属正常，0 实缴须提醒 |
| `capital_type` | 出资方式 | `CapitalType` | - | 货币 / 实物 / 知识产权 / 土地使用权等 |
| `capital_date` | 出资（认缴）期限 | `CapiDate` | - | 新《公司法》5 年认缴期（2024-07-01 起）衔接 |

> **跨源对比注意**：Tushare 只覆盖**上市公司前十大股东**（含流通 / 非流通两张表），
> 未上市公司股权结构必须走企查查。

## 维度 3：主要人员

| 字段 | 中文 | 企查查字段 | Tushare 字段 | 核查要点 |
|------|------|-----------|-------------|---------|
| `name` | 姓名 | `Name` | `stock_company.chairman` 等 | 多岗位兼任须一致 |
| `job_title` | 职务 | `Job` | - | 董事 / 监事 / 董秘 / 总经理 / 副总经理 / 财务负责人 |
| `sex` | 性别 | - | - | 偶尔作辅助校验 |
| `from_date` | 任职日期 | - | - | 企查查通常不提供；需查决议 |

## 维度 4：知识产权

| 字段 | 中文 | 企查查字段 | 核查要点 |
|------|------|-----------|---------|
| `patent_no` | 专利号 | `PatentNo` | 国家知识产权局官网二次核验 |
| `patent_type` | 专利类型 | `PatentType` | 发明 / 实用新型 / 外观设计 |
| `patent_status` | 专利状态 | `Status` | "有效" / "失效" / "审中" |
| `trademark_no` | 商标注册号 | `TrademarkNo` | 商标局官网二次核验 |
| `soft_no` | 软著登记号 | `SoftNo` | 中国版权保护中心 |

## 维度 5：行政处罚

| 字段 | 中文 | 企查查字段 | 核查要点 |
|------|------|-----------|---------|
| `punish_no` | 处罚文书号 | `PunishNumber` | 用于去重 |
| `punish_authority` | 处罚机关 | `PunishOrganization` | 用于判断处罚级别（部 / 省 / 市 / 县） |
| `punish_content` | 处罚内容 | `Content` | 是否属于"重大违法违规"的判断 |
| `punish_amount` | 罚款金额 | `PunishMoney` | 关注是否触发注册办法第 10 条消极条件 |
| `punish_date` | 处罚决定日期 | `PunishDate` | 36 个月 / 12 个月窗口判断 |
| `publish_date` | 公示日期 | `PublishDate` | 用于判断时效性 |

## 维度 6：财务数据（仅上市公司）

| 字段 | 中文 | Tushare 字段 | 核查要点 |
|------|------|-------------|---------|
| `revenue` | 营业收入 | `income.total_revenue` | 单位：元；报告期一致 |
| `net_profit` | 净利润 | `income.n_income` | 归母 vs 全部 |
| `total_assets` | 资产总额 | `balancesheet.total_assets` | 期末口径 |
| `total_liab` | 负债总额 | `balancesheet.total_liab` | 期末口径 |
| `equity` | 股东权益 | `balancesheet.total_hldr_eqy_inc_min_int` | 含少数股东权益 |
| `roe` | 加权平均 ROE | `fina_indicator.roe` | 发行条件触发（创业板 / 主板 / 科创板各有口径） |
| `eps` | 每股收益 | `fina_indicator.eps` | 基本 vs 稀释 |

## 如何新增维度

1. 在本文件新增一张表（表头按现有格式）
2. 登记字段映射（客户中文 → 数据源字段）
3. 备注"核查要点"——字段的业务意义
4. 回到 SKILL.md 的"第 1 步：明确比对维度"表格加一行
5. 若涉及新数据源，先完成 `scripts/<source>_connector.py` 封装

## 版本

| 日期 | 变更 |
|------|------|
| 2026-04-24 | 初版，登记 6 大维度的核心字段 |
