---
name: legal-job-search
title: 法律AI求职助手
description: 法律AI求职助手 - 帮助法律人（法务/律师）使用AI辅助求职。支持公司/律所调研、法律风险分析、网页简历生成、针对性材料准备、面试备忘录生成。具备MCP工具级降级能力，无MCP时自动使用Web Search。
author: zh-xx
author_url: https://github.com/zh-xx/legal-assistant-skills/tree/main/legal-job-search
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: zh
---

# 法律AI求职助手

## Overview

本技能帮助法律人（法务、律师）在求职过程中使用AI提升效率和准备质量。

**核心能力**：
- 公司/律所深度调研（支持 Deep Research 降级到 Web Search）
- 法律风险分析（支持 MCP 工具级降级到 Web Search）
- 网页简历生成（完全可配置的样式系统）
- 针对性简历调整
- 面试备忘录生成

**工作路径**：
```
环境检测 → 信息收集 → 材料生成 → 输出确认
```

---

## 工作流

### 阶段 0：环境检测与路径规划

**步骤 0.1：检测可用 MCP 工具**

采用**功能匹配**策略，不限定具体工具名称：

```
for 每个功能需求:
    │
    ├─ 功能1：企业被执行信息
    │   └─ 匹配关键词：executed, execution, enforcement, 被执行, 执行
    │
    ├─ 功能2：企业失信信息
    │   └─ 匹配关键词：dishonest, breach, 失信, 违约
    │
    ├─ 功能3：限制高消费
    │   └─ 匹配关键词：consumption, restriction, 限制高消费, 限消
    │
    ├─ 功能4：终本案件
    │   └─ 匹配关键词：final, closed, 终本
    │
    └─ 功能5：裁判文书
        └─ 匹配关键词：judgment, court, ruling, 裁判文书, 判决

匹配依据：
├─ 工具名称包含关键词
├─ 工具描述包含功能说明
└─ 工具参数包含 entname 或 company_name
```

记录可用工具列表。

详细说明见：`references/mcp-tools/mcp-catalog.md`

**步骤 0.2：询问 Deep Research 工具**

询问用户是否有以下工具：
- 秘塔AI搜索（深度研究模式）
- Perplexity Pro
- 其他 Deep Research 工具

**步骤 0.3：确定岗位类型**

```
岗位类型判断：
│
├─ 法务岗位 → 使用「公司调研框架」
├─ 律所岗位 → 使用「律所调研框架」
└─ 其他法律岗位 → 询问用户使用哪个框架
```

---

### 阶段 1：信息收集

#### 1.1 岗位信息提取

从用户提供的内容中提取：
- 职位名称
- 岗位职责
- 任职要求
- 优先条件

如果用户只提供了公司/律所名称，引导用户提供 JD 信息。

#### 1.2 公司/律所调研

**法务岗位 - 公司调研**

```
优先路径：Deep Research 工具
│
├─ 秘塔AI搜索：开启「深度研究」模式
│   └─ 查询："{公司名} 公司介绍 商业模式 业绩 行业地位"
│
├─ Perplexity Pro：
│   └─ 同样查询
│
└─ 降级路径：Web Search（多轮）
    ├─ 搜索1：{公司名} + "公司介绍" + "商业模式"
    ├─ 搜索2：{公司名} + "行业地位" + "竞争对手"
    ├─ 搜索3：{公司名} + "业绩" + "年报"
    └─ 整合生成简版报告
```

**律所岗位 - 律所调研**

```
公开信息：
├─ 律所官网团队介绍
├─ 律师专业领域公示
├─ 律所业绩展示
└─ 行业排名/奖项

私域信息（用户自行补充）：
├─ 使用 references/frameworks/firm-research-framework.md
└─ 提供问题清单引导用户收集
```

#### 1.3 法律风险分析（功能级降级）

**对每个功能需求独立执行：**

```
功能需求列表：
├─ 企业被执行信息
├─ 企业失信信息
├─ 限制高消费
├─ 终本案件
└─ 裁判文书

for 每个功能需求:
    │
    ├─ 尝试查找功能匹配的 MCP 工具
    │   ├─ 检查工具名称、描述、参数
    │   ├─ 找到匹配工具 → 尝试调用
    │   │   ├─ 调用成功 → 使用 MCP 数据
    │   │   └─ 调用失败 → 继续尝试其他工具
    │   │
    │   └─ 没有找到匹配工具 → 执行降级
    │
    └─ 降级：Web Search（多轮）
        ├─ 使用预设查询模板
        ├─ 多轮搜索获取信息
        └─ 整合结果到报告
```

详细说明见：`references/frameworks/legal-risk-framework.md`
    │
    └─ 降级：Web Search
        └─ 使用 references/mcp-tools/fallback-queries.md
            中的对应查询模板
        └─ 整合搜索结果到报告
```

**输出结构**：
```markdown
## 法律风险分析报告

### 执行信息
- 查询时间：{时间戳}
- 数据来源：{MCP工具名称 / Web Search}

### 风险概览
| 风险类型 | 风险等级 | 核心问题 |
|---------|---------|---------|
|         |         |         |

### 详细信息
#### 被执行信息
...

#### 失信信息
...

（其他类别）
```

---

### 阶段 2：基础材料准备

#### 2.1 用户材料收集引导

**首次用户引导**：

如果用户是首次使用或材料不完整，引导用户参考材料准备清单：

```
请参考「法律人求职材料准备清单」提供你的信息。

清单位置：references/prompts/preparation-checklist.md

你可以：
1. 复制清单中的模板填写
2. 或直接按你自己的方式提供信息
```

**材料检查清单**：

```
必需信息：
├─ 基本信息（姓名、职位、年龄、学历、联系方式）
├─ 教育背景（学校、学历、专业、时间）
├─ 工作经历（公司、职位、时间、主要成就）
├─ 核心技能（专业技能、语言能力）
└─ 资格证书（如有）

推荐信息：
├─ 目标公司/律所名称
├─ 目标岗位 JD
└─ 自我评价

可选信息：
├─ 照片
├─ 项目经验
├─ 发表文章/论文
└─ 其他补充信息
```

#### 2.2 简历信息处理

如果用户已有网页简历：
- 直接加载 HTML 文件
- 提取简历内容用于后续调整

如果用户提供 Word/PDF 简历：
- 使用 docx skill 或 mineru-ocr skill 提取内容
- 整理为结构化信息
  - 教育背景
  - 工作经历
  - 核心技能
  - 资格证书
  - 自我评价

#### 2.2 简历样式选择

```
样式选择：
│
├─ 使用预设样式：
│   ├─ business-elite - 商务精英风（金色+深蓝）
│   ├─ modern-tech - 现代科技风（蓝色+灰白）
│   └─ minimal-clean - 极简清新风（绿色+米白）
│
├─ 或自定义样式：
│   └─ 使用 references/styles/custom-guide.md
│       └─ 用户指定：配色方案、字体、布局
│
└─ 或保持已有简历样式
```

---

### 阶段 3：针对性材料生成

#### 3.1 调整策略制定

分析以下内容：
- JD 中的关键词
- 公司/律所业务特点
- 用户经验与岗位的匹配点

**输出调整策略**：
```markdown
# 简历调整策略

## 关键词匹配
| JD关键词 | 简历对应位置 |
|---------|-------------|
|         |             |

## 经验重构
- 前置：{需要前置的经验}
- 扩充：{需要扩充的经验}
- 合并：{可以合并的经验}

## 技能排序
按与岗位相关性重新排序：
1. {最相关技能}
2. {次相关技能}
...
```

#### 3.2 针对性简历生成

使用 `references/prompts/html-resume-template.md` 中的提示词模板：
- 应用调整策略
- 匹配目标样式
- 生成新的 HTML 简历

#### 3.3 面试备忘录生成

使用 `references/prompts/materials-prompt-template.md` 中的备忘录部分：
- 公司/律所核心信息速览
- 业务/法律接口地图
- 风险与挑战分析
- 岗位价值主张
- 面试谈话要点（洞察 + 可提问题）

**输出格式**：精美 Word 文档（.docx）

使用 `docx` skill 生成固定格式的 Word 文档，样式规范见：
`references/prompts/memo-word-spec.md`

**文档结构**：
- 封面页（公司/律所名称、岗位名称、制备人、日期）
- 目录页
- 正文（五个章节）
- 附录（数据来源说明、使用建议）

**样式特点**：
- A4 页面，专业配色（金色+深蓝）
- 统一字体规范（微软雅黑标题 + 宋体正文）
- 精美表格样式（表头深色背景 + 斑马纹）
- 页眉页脚（章节导航 + 页码）

---

### 阶段 4：输出与确认

#### 4.1 文件输出

```
输出文件：
├── 简历_{姓名}_{目标公司/律所}.html
├── 面试备忘录_{目标公司/律所}.docx  （精美 Word 文档）
└── 法律风险分析报告_{目标公司/律所}.md
```

#### 4.2 (可选) 交互式简历集成

如果用户询问如何添加聊天窗口：
- 引导至 `extensions/interactive-resume/dify-integration.md`

---

## Dependencies

### 必需
- Claude Code（支持 HTML 生成、Web Search）
- 用户简历基础信息

### 可选但推荐
- MCP 工具（企业法律风险类）：
  - `get_executed_entity`
  - `get_dishonest_entity`
  - `get_consumption_restrictions`
  - `get_final_cases`
  - `get_judgments`
- Deep Research 工具：
  - 秘塔AI搜索（深度研究模式）
  - Perplexity Pro

### 可选扩展
- Dify.ai（用于交互式简历）
- Live Server（VS Code 扩展，用于本地测试）

---

## Key Rules

### 1. 工具级降级原则
每个 MCP 工具独立判断可用性，不可用时单独降级到 Web Search。不因单个工具失败而影响整体流程。

### 2. 信息真实性原则
所有生成内容必须基于：
- 用户提供的真实信息
- 公开可查的公司/律所信息
- MCP 或 Web Search 返回的结果

严禁虚构经历、夸大成果或编造公司信息。

### 3. 结构化表达优先
优先使用：
- 表格（比较、分类、风险矩阵）
- ASCII 流程图（业务流程、决策路径）
- 清单（谈话要点、待办事项）
- 时间线（发展阶段、职业轨迹）

### 4. 面试导向原则
所有生成的材料都要能直接支撑面试：
- 备忘录中的每条信息都要能转化为谈话内容
- 简历中的每条经历都要准备展开说明
- 风险分析中的每个点都要有应对思路

### 5. 用户知情原则
明确告知用户：
- 哪些信息来自 MCP（精确度高）
- 哪些信息来自 Web Search（需要验证）
- 哪些信息需要用户自行补充（如律所私域信息）

---

## 快速开始（用户端）

### 场景 1：首次使用，从零开始

```
用户：我想申请腾讯音乐的法务岗位，JD在这里

Claude：
1. 提取 JD 信息
2. 询问：你有秘塔AI搜索或 Perplexity Pro 吗？
3. 开始调研：
   - 公司调研（Deep Research 或 Web Search）
   - 法律风险分析（MCP 或 Web Search）
4. 询问：你的基础简历信息
5. 生成：网页简历 + 面试备忘录
```

### 场景 2：已有简历，调整目标

```
用户：这是我的简历，我想申请红杉律所的资本市场团队

Claude：
1. 加载现有简历
2. 询问：你有关于这个团队的私域信息吗？
3. 使用「律所调研框架」+「团队信息收集清单」
4. 生成：针对性简历 + 面试备忘录
```

### 场景 3：快速调研模式

```
用户：帮我快速调研一下字节跳动的法律风险情况

Claude：
1. 直接执行法律风险分析（工具级降级）
2. 输出：法律风险分析报告
```

---

## 扩展功能

### 交互式简历集成

见 `extensions/interactive-resume/dify-integration.md`

### 自定义简历样式

见 `references/styles/custom-guide.md`

---

## References

### 提示词模板
- `references/prompts/preparation-checklist.md` - 材料准备清单
- `references/prompts/html-resume-template.md` - 简历 HTML 生成提示词
- `references/prompts/materials-prompt-template.md` - 求职材料生成提示词
- `references/prompts/memo-word-spec.md` - 面试备忘录 Word 文档规范
- `references/prompts/firm-research-extension.md` - 律所求职扩展

### 调研框架
- `references/frameworks/company-research-framework.md` - 公司调研框架
- `references/frameworks/firm-research-framework.md` - 律所调研框架
- `references/frameworks/legal-risk-framework.md` - 法律风险分析框架

### MCP 工具
- `references/mcp-tools/mcp-catalog.md` - 支持的 MCP 工具目录（功能匹配）
- `references/mcp-tools/fallback-queries.md` - MCP 降级查询模板

### 简历样式
- `references/styles/business-elite.md` - 商务精英风配置
- `references/styles/modern-tech.md` - 现代科技风配置
- `references/styles/minimal-clean.md` - 极简清新风配置
- `references/styles/custom-guide.md` - 自定义配置指南
