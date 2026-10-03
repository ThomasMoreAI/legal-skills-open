# 公司调研框架

> 适用场景：法务岗位求职 - 目标公司调研
> 输出：结构化的公司分析报告

---

## 调研维度

### 一、公司基础信息

```markdown
## 公司基础信息

| 项目 | 内容 |
|------|------|
| 公司名称 | {COMPANY_NAME} |
| 成立时间 | {FOUNDED_DATE} |
| 注册资本 | {REGISTERED_CAPITAL} |
| 企业类型 | {COMPANY_TYPE} |
| 法定代表人 | {LEGAL_REPRESENTATIVE} |
| 注册地址 | {REGISTERED_ADDRESS} |
| 办公地址 | {OFFICE_ADDRESS} |
| 员工规模 | {EMPLOYEE_COUNT} |
| 上市情况 | {LISTING_STATUS} |
| 股票代码 | {STOCK_CODE} |
```

---

### 二、公司定位与业务模式

```markdown
## 公司定位与业务模式

### 公司定位
{ONE_LINE_SUMMARY}

### 核心业务
| 业务板块 | 占比/重要性 | 商业模式 |
|---------|------------|---------|
| {BUSINESS_1} | {PERCENTAGE_1} | {MODEL_1} |
| {BUSINESS_2} | {PERCENTAGE_2} | {MODEL_2} |

### 客户结构
| 客户类型 | 占比 | 代表客户 |
|---------|------|---------|
| {CUSTOMER_TYPE_1} | {PERCENTAGE} | {EXAMPLES} |

### 收入结构
| 收入来源 | 占比 | 趋势 |
|---------|------|------|
| {REVENUE_SOURCE_1} | {PERCENTAGE} | {TREND} |
```

---

### 三、行业地位与竞争格局

```markdown
## 行业地位与竞争格局

### 市场地位
- **市场份额**：{MARKET_SHARE}
- **行业排名**：{RANKING}
- **核心优势**：{ADVANTAGES}

### 主要竞争对手
| 竞争对手 | 优势 | 劣势（对比目标公司） |
|---------|------|---------------------|
| {COMPETITOR_1} | {STRENGTH} | {WEAKNESS} |
| {COMPETITOR_2} | {STRENGTH} | {WEAKNESS} |

### 行业趋势
- {TREND_1}
- {TREND_2}
- {TREND_3}
```

---

### 四、财务与经营状况

```markdown
## 财务与经营状况

### 核心财务数据（近三年）
| 指标 | {YEAR_1} | {YEAR_2} | {YEAR_3} | 趋势 |
|------|---------|---------|---------|------|
| 营业收入 | | | | |
| 净利润 | | | | |
| 毛利率 | | | | |
| 净利率 | | | | |

### 经营亮点
- {HIGHLIGHT_1}
- {HIGHLIGHT_2}

### 经营风险
- {RISK_1}
- {RISK_2}
```

---

### 五、组织架构与团队

```markdown
## 组织架构与团队

### 组织架构
```
[ASCII 或 Mermaid 组织架构图]
```

### 核心管理层
| 职位 | 姓名 | 背景 |
|------|------|------|
| {POSITION} | {NAME} | {BACKGROUND} |

### 法务团队（如可知）
- **团队规模**：{LEGAL_TEAM_SIZE}
- **汇报关系**：{REPORTING_LINE}
- **团队结构**：{TEAM_STRUCTURE}
```

---

## Deep Research 提示词模板

### 模板1：秘塔AI搜索

```
请对 {COMPANY_NAME} 进行深度研究，包括：

1. 公司基础信息（成立时间、注册资本、企业类型、上市情况）
2. 公司定位与核心业务
3. 商业模式与客户结构
4. 行业地位与主要竞争对手
5. 近三年财务状况与经营趋势
6. 组织架构与核心管理层
7. 法务团队情况（如可知）

请生成结构化的研究报告。
```

### 模板2：Perplexity Pro

```
Research {COMPANY_NAME} and provide:

1. Company overview (founding date, registration capital, company type, listing status)
2. Business model and core business segments
3. Customer structure and revenue sources
4. Market position and key competitors
5. Financial performance (last 3 years)
6. Organization structure and key management
7. Legal team information (if available)

Please provide a structured research report.
```

---

## Web Search 降级策略

### 搜索轮次

```
轮次1：公司基础信息
├─ 搜索："{公司名}" + "公司介绍" + "官网"
├─ 搜索："{公司名}" + "基本信息" + "成立时间"
└─ 整合：成立时间、注册资本、企业类型、上市情况

轮次2：业务与商业模式
├─ 搜索："{公司名}" + "商业模式" + "主营业务"
├─ 搜索："{公司名}" + "客户结构" + "收入来源"
└─ 整合：核心业务、商业模式、客户结构

轮次3：行业地位
├─ 搜索："{公司名}" + "行业地位" + "市场份额"
├─ 搜索："{公司名}" + "竞争对手" + "排名"
└─ 整合：市场地位、竞争对手、行业排名

轮次4：财务状况
├─ 搜索："{公司名}" + "年报" + "财务数据"
├─ 搜索："{公司名}" + "营收" + "净利润"
└─ 整合：近三年财务数据、经营趋势

轮次5：组织与管理
├─ 搜索："{公司名}" + "组织架构" + "管理层"
├─ 搜索："{公司名}" + "高管" + "团队"
└─ 整合：组织架构、核心管理层
```

---

## 输出模板

```markdown
# {COMPANY_NAME} 公司调研报告

> 生成时间：{TIMESTAMP}
> 数据来源：{SOURCE}

---

## 一、公司基础信息

{CONTENT}

## 二、公司定位与业务模式

{CONTENT}

## 三、行业地位与竞争格局

{CONTENT}

## 四、财务与经营状况

{CONTENT}

## 五、组织架构与团队

{CONTENT}

## 六、法务相关分析

### 业务-法律接口地图
| 业务板块 | 法律关注点 | 相关法规 |
|---------|-----------|---------|
| | | |

### 合规重点领域
- {COMPLIANCE_AREA_1}
- {COMPLIANCE_AREA_2}

---

*报告结束*
```
