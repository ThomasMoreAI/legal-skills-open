# 法律风险分析框架

> 适用场景：法务岗位求职 - 目标公司法律风险分析
> 支持：MCP 工具级降级到 Web Search

---

## 风险类别与数据源

### 一、企业执行信息

**功能需求**：查询企业被执行人信息、案件数量、执行标的等

**MCP 功能匹配**：
- 任何提供 `entname` 或 `company_name` 参数，能返回被执行信息的 MCP 工具
- 工具名称可能包含：`executed`、`execution`、`enforcement`、`被执行` 等关键词

**降级查询**：`"{公司名}" 被执行人信息`

```markdown
## 被执行信息

| 项目 | 内容 |
|------|------|
| 查询时间 | {TIMESTAMP} |
| 数据来源 | {MCP_TOOL / WEB_SEARCH} |
| 被执行案件数 | {COUNT} |
| 执行标的总额 | {TOTAL_AMOUNT} |
| 最新案件日期 | {LATEST_DATE} |

### 案件列表
| 立案时间 | 案号 | 执行标的 | 执行法院 | 状态 |
|---------|------|---------|---------|------|
| {DATE} | {CASE_NO} | {AMOUNT} | {COURT} | {STATUS} |

### 风险评估
- **风险等级**：{HIGH / MEDIUM / LOW}
- **核心问题**：{KEY_ISSUES}
- **应对思路**：{RESPONSE_STRATEGY}
```

---

### 二、失信信息

**功能需求**：查询企业失信被执行人名单、失信行为等

**MCP 功能匹配**：
- 任何提供 `entname` 或 `company_name` 参数，能返回失信信息的 MCP 工具
- 工具名称可能包含：`dishonest`、`breach`、`失信`、`违约` 等关键词

**降级查询**：`"{公司名}" 失信被执行人名单`

```markdown
## 失信被执行人信息

| 项目 | 内容 |
|------|------|
| 查询时间 | {TIMESTAMP} |
| 数据来源 | {MCP_TOOL / WEB_SEARCH} |
| 失信案件数 | {COUNT} |

### 失信案件列表
| 发布日期 | 案号 | 失信行为 | 履行情况 |
|---------|------|---------|---------|
| {DATE} | {CASE_NO} | {BEHAVIOR} | {STATUS} |

### 风险评估
- **风险等级**：{HIGH / MEDIUM / LOW / NONE}
- **核心问题**：{KEY_ISSUES}
- **应对思路**：{RESPONSE_STRATEGY}
```

---

### 三、限制高消费

**功能需求**：查询企业限制高消费令、限消记录等

**MCP 功能匹配**：
- 任何提供 `entname` 或 `company_name` 参数，能返回限消信息的 MCP 工具
- 工具名称可能包含：`consumption`、`restriction`、`限制高消费`、`限消` 等关键词

**降级查询**：`"{公司名}" 限制高消费令`

```markdown
## 限制高消费信息

| 项目 | 内容 |
|------|------|
| 查询时间 | {TIMESTAMP} |
| 数据来源 | {MCP_TOOL / WEB_SEARCH} |
| 限消令数量 | {COUNT} |

### 限消令列表
| 发布日期 | 案号 | 限制内容 | 关联人员 |
|---------|------|---------|---------|
| {DATE} | {CASE_NO} | {RESTRICTION} | {PERSON} |

### 风险评估
- **风险等级**：{HIGH / MEDIUM / LOW / NONE}
- **核心问题**：{KEY_ISSUES}
- **应对思路**：{RESPONSE_STRATEGY}
```

---

### 四、终本案件

**功能需求**：查询企业终本案件（无财产可供执行）

**MCP 功能匹配**：
- 任何提供 `entname` 或 `company_name` 参数，能返回终本案件信息的 MCP 工具
- 工具名称可能包含：`final`、`closed`、`终本` 等关键词

**降级查询**：`"{公司名}" 终本案件`

```markdown
## 终本案件信息

| 项目 | 内容 |
|------|------|
| 查询时间 | {TIMESTAMP} |
| 数据来源 | {MCP_TOOL / WEB_SEARCH} |
| 终本案件数 | {COUNT} |
| 未执行标的总额 | {TOTAL_AMOUNT} |

### 终本案件列表
| 立案时间 | 案号 | 执行标的 | 终本原因 |
|---------|------|---------|---------|
| {DATE} | {CASE_NO} | {AMOUNT} | {REASON} |

### 风险评估
- **风险等级**：{HIGH / MEDIUM / LOW / NONE}
- **核心问题**：{KEY_ISSUES}
- **应对思路**：{RESPONSE_STRATEGY}
```

---

### 五、裁判文书

**功能需求**：查询企业裁判文书、案件数量、案件类型等

**MCP 功能匹配**：
- 任何提供 `entname` 或 `company_name` 参数，能返回裁判文书信息的 MCP 工具
- 工具名称可能包含：`judgment`、`court`、`ruling`、`裁判文书`、`判决` 等关键词

**降级查询**：`"{公司名}" 裁判文书`

```markdown
## 裁判文书信息

| 项目 | 内容 |
|------|------|
| 查询时间 | {TIMESTAMP} |
| 数据来源 | {MCP_TOOL / WEB_SEARCH} |
| 文书总数 | {TOTAL_COUNT} |

### 案件类型分布
| 案件类型 | 作为原告 | 作为被告 | 第三人 |
|---------|---------|---------|-------|
| 民商事 | {COUNT} | {COUNT} | {COUNT} |
| 知识产权 | {COUNT} | {COUNT} | {COUNT} |
| 劳动争议 | {COUNT} | {COUNT} | {COUNT} |
| 行政 | {COUNT} | {COUNT} | {COUNT} |

### 诉讼数量时间分布
| 年份 | 诉讼数量 | 主要类型 |
|------|---------|---------|
| {YEAR} | {COUNT} | {MAIN_TYPES} |
| {YEAR} | {COUNT} | {MAIN_TYPES} |
| {YEAR} | {COUNT} | {MAIN_TYPES} |

### 诉讼趋势分析
```
[ASCII 时间线或趋势图]
```
- **总体趋势**：{INCREASING / STABLE / DECREASING}
- **高发年份**：{PEAK_YEARS}
- **近期变化**：{RECENT_TREND}

### 典型案件
| 案号 | 案由 | 诉讼地位 | 裁判结果 | 争议焦点 |
|------|------|---------|---------|---------|
| {CASE_NO} | {CAUSE} | {POSITION} | {RESULT} | {ISSUE} |

### 风险评估
- **作为原告分析**：{PLAINTIFF_ANALYSIS}
- **作为被告分析**：{DEFENDANT_ANALYSIS}
- **核心争议领域**：{KEY_DISPUTES}
- **应对思路**：{RESPONSE_STRATEGY}
```

---

## MCP 工具功能匹配策略

### 匹配原则

```
1. 功能优先，名称次要
   ├─ 不限定具体的 MCP 工具名称
   ├─ 根据工具描述和参数进行功能匹配
   └─ 支持任何提供相同功能的 MCP 工具

2. 参数匹配
   ├─ 接受 `entname` 参数的企业信息类 MCP
   ├─ 接受 `company_name` 参数的企业信息类 MCP
   └─ 其他合理的企业名称参数

3. 关键词匹配
   └─ 工具名称或描述中包含相关关键词即可使用
       ├─ 被执行: executed, execution, enforcement, 执行
       ├─ 失信: dishonest, breach, 失信, 违约
       ├─ 限消: consumption, restriction, 限制高消费, 限消
       ├─ 终本: final, closed, 终本
       └─ 裁判: judgment, court, ruling, 裁判文书, 判决
```

### 工具检测流程

```python
# 伪代码：功能匹配的 MCP 检测

def find_mcp_by_function(required_function, available_mcps):
    """
    根据功能需求查找匹配的 MCP 工具

    参数:
        required_function: 需要的功能描述
        available_mcps: 当前可用的所有 MCP 工具

    返回:
        匹配的 MCP 工具列表（可能多个）
    """
    # 功能到关键词的映射
    function_keywords = {
        "executed_entity": ["executed", "execution", "enforcement", "被执行", "执行"],
        "dishonest_entity": ["dishonest", "breach", "失信", "违约"],
        "consumption_restrictions": ["consumption", "restriction", "限制高消费", "限消"],
        "final_cases": ["final", "closed", "终本"],
        "judgments": ["judgment", "court", "ruling", "裁判文书", "判决"],
    }

    keywords = function_keywords.get(required_function, [])
    matched_tools = []

    for mcp_name, mcp_info in available_mcps.items():
        # 检查工具名称
        if any(keyword in mcp_name.lower() for keyword in keywords):
            matched_tools.append(mcp_name)
            continue

        # 检查工具描述
        description = mcp_info.get("description", "").lower()
        if any(keyword in description for keyword in keywords):
            matched_tools.append(mcp_name)
            continue

        # 检查参数
        params = mcp_info.get("parameters", {})
        if "entname" in params or "company_name" in params:
            # 参数匹配，可能是同类工具
            matched_tools.append(mcp_name)

    return matched_tools
```

### 降级策略

```
对于每个功能需求：
│
├─ 尝试查找功能匹配的 MCP 工具
│   ├─ 找到匹配工具 → 尝试调用
│   │   ├─ 调用成功 → 使用 MCP 数据
│   │   └─ 调用失败 → 继续尝试其他匹配工具
│   │
│   └─ 没有找到匹配工具 → 降级到 Web Search
│
└─ Web Search 降级
    ├─ 使用预设的查询模板
    ├─ 多轮搜索获取信息
    └─ 整合结果输出
```

---

## 工具级降级流程

```python
# 伪代码：工具级降级流程

def analyze_legal_risks(company_name, available_mcps):
    report = LegalRiskReport(company_name)
    report.timestamp = now()

    # 定义所有风险类别
    risk_categories = [
        {
            "name": "被执行信息",
            "mcp_tool": "get_executed_entity",
            "fallback_query": f'"{company_name}" 被执行人信息',
            "template": "executed_entity_template"
        },
        {
            "name": "失信信息",
            "mcp_tool": "get_dishonest_entity",
            "fallback_query": f'"{company_name}" 失信被执行人名单',
            "template": "dishonest_entity_template"
        },
        {
            "name": "限制高消费",
            "mcp_tool": "get_consumption_restrictions",
            "fallback_query": f'"{company_name}" 限制高消费令',
            "template": "consumption_restrictions_template"
        },
        {
            "name": "终本案件",
            "mcp_tool": "get_final_cases",
            "fallback_query": f'"{company_name}" 终本案件',
            "template": "final_cases_template"
        },
        {
            "name": "裁判文书",
            "mcp_tool": "get_judgments",
            "fallback_query": f'"{company_name}" 裁判文书',
            "template": "judgments_template"
        }
    ]

    # 对每个类别独立执行
    for category in risk_categories:
        result = None
        source = None

        # 尝试 MCP
        if category["mcp_tool"] in available_mcps:
            try:
                result = call_mcp(category["mcp_tool"], company_name)
                source = category["mcp_tool"]
            except Exception as e:
                # MCP 失败，降级到 Web Search
                pass

        # 降级到 Web Search
        if result is None:
            result = web_search(category["fallback_query"])
            source = "Web Search"

        # 添加到报告
        report.add_section(
            category["name"],
            format_by_template(category["template"], result),
            source=source
        )

    # 生成风险矩阵
    report.generate_risk_matrix()

    return report
```

---

## 风险矩阵模板

```markdown
## 法律风险矩阵

| 风险领域 | 风险等级 | 数据来源 | 核心问题 | 应对思路 |
|---------|---------|---------|---------|---------|
| 被执行信息 | {LEVEL} | {SOURCE} | {ISSUE} | {STRATEGY} |
| 失信信息 | {LEVEL} | {SOURCE} | {ISSUE} | {STRATEGY} |
| 限制高消费 | {LEVEL} | {SOURCE} | {ISSUE} | {STRATEGY} |
| 终本案件 | {LEVEL} | {SOURCE} | {ISSUE} | {STRATEGY} |
| 裁判文书 | {LEVEL} | {SOURCE} | {ISSUE} | {STRATEGY} |

### 诉讼活动综合分析
| 维度 | 数据 | 分析 |
|------|------|------|
| 总诉讼数量 | {TOTAL_COUNT} | {COUNT_ANALYSIS} |
| 高发年份 | {PEAK_YEARS} | {PEAK_ANALYSIS} |
| 主要类型 | {MAIN_TYPES} | {TYPE_ANALYSIS} |
| 诉讼趋势 | {TREND} | {TREND_ANALYSIS} |

### 风险等级说明
- **高风险**：存在严重法律风险，可能影响公司经营或声誉
- **中风险**：存在一定法律风险，需要关注和应对
- **低风险**：法律风险较小，在可接受范围内
- **无风险**：未发现相关风险信息
```

---

## 可扩展 MCP 工具

如果用户配置了以下 MCP，也可以集成到分析中：

| MCP 类型 | 功能 | 降级查询 |
|---------|------|----------|
| 行政处罚 | 企业行政处罚记录 | `"{公司名}" 行政处罚` |
| 股权追溯 | 股权结构、股东信息 | `"{公司名}" 股权结构` |
| 知识产权 | 专利、商标信息 | `"{公司名}" 专利` `"{公司名}" 商标` |
| 工伤检索 | 工伤事故记录 | `"{公司名}" 工伤事故` |
| 环保处罚 | 环保处罚记录 | `"{公司名}" 环保处罚` |
| 税务处罚 | 税务处罚记录 | `"{公司名}" 税务处罚` |

---

## 输出模板

```markdown
# {COMPANY_NAME} 法律风险分析报告

> 生成时间：{TIMESTAMP}
> 查询方式：{METHOD}

---

## 风险概览

### 风险矩阵
| 风险领域 | 风险等级 | 核心问题 |
|---------|---------|---------|
| | | |

### 诉讼活动综合分析
| 维度 | 数据 | 分析 |
|------|------|------|
| 总诉讼数量 | {TOTAL_COUNT} | {COUNT_ANALYSIS} |
| 高发年份 | {PEAK_YEARS} | {PEAK_ANALYSIS} |
| 主要类型 | {MAIN_TYPES} | {TYPE_ANALYSIS} |
| 诉讼趋势 | {TREND} | {TREND_ANALYSIS} |

### 总体评估
{OVERALL_ASSESSMENT}

---

## 详细分析

### 一、被执行信息
{DETAILS}

### 二、失信信息
{DETAILS}

### 三、限制高消费
{DETAILS}

### 四、终本案件
{DETAILS}

### 五、裁判文书与诉讼趋势
{DETAILS}

#### 5.1 诉讼数量时间分布
```
[时间线图表]
```

#### 5.2 诉讼类型分布分析
| 诉讼类型 | 占比 | 趋势 | 分析 |
|---------|------|------|------|
| | | | |

#### 5.3 诉讼地位分析
| 诉讼地位 | 案件数 | 占比 | 分析 |
|---------|-------|------|------|
| 原告 | | | |
| 被告 | | | |
| 第三人 | | | |

---

## 面试谈话要点

### 可展示的洞察
- [ ] {INSIGHT_1}
- [ ] {INSIGHT_2}

### 可提出的问题
- {QUESTION_1}
- {QUESTION_2}

---

*数据来源说明：本报告基于公开信息查询，建议在面试前再次核实最新情况*
```
