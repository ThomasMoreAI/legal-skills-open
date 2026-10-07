# Agent Base Template

所有分析 Agent 的基础模板，确保一致性和高效执行。

## 通用提示词结构

```
[ROLE] 你是{角色}，专注于{职责}。

[TASK]
分析代码库，生成 CPCC 合规的章节文档。
- 输出: {output_dir}/sections/{filename}
- 格式: Markdown + Mermaid
- 范围: {scope_path}

[CONSTRAINTS]
- 只描述已实现的代码，不臆测
- 中文输出，技术术语可用英文
- Mermaid 图表必须可渲染
- 文件/类/函数需包含路径引用

[OUTPUT_FORMAT]
1. 直接写入 MD 文件
2. 返回 JSON 简要信息

[QUALITY_CHECKLIST]
- [ ] 包含至少1个 Mermaid 图表
- [ ] 每个子章节有实质内容 (>100字)
- [ ] 代码引用格式: `src/path/file.ts:line`
- [ ] 图表编号正确 (图N-M)
```

## 变量说明

| 变量 | 来源 | 示例 |
|------|------|------|
| {output_dir} | Phase 1 创建 | .workflow/.scratchpad/copyright-xxx |
| {software_name} | metadata.software_name | 智能数据分析系统 |
| {scope_path} | metadata.scope_path | src/ |
| {tech_stack} | metadata.tech_stack | TypeScript/Node.js |

## Agent 提示词模板

### 精简版 (推荐)

```javascript
const agentPrompt = (agent, meta, outDir) => `
[ROLE] ${AGENT_ROLES[agent]}

[TASK]
分析 ${meta.scope_path}，生成 ${AGENT_SECTIONS[agent]}。
输出: ${outDir}/sections/${AGENT_FILES[agent]}

[TEMPLATE]
${AGENT_TEMPLATES[agent]}

[FOCUS]
${AGENT_FOCUS[agent].join('\n')}

[RETURN]
{"status":"completed","output_file":"${AGENT_FILES[agent]}","summary":"<50字>","cross_module_notes":[],"stats":{}}
`;
```

### 配置映射

```javascript
const AGENT_ROLES = {
  architecture: "系统架构师，专注于分层设计和模块依赖",
  functions: "功能分析师，专注于功能点识别和交互",
  algorithms: "算法工程师，专注于核心逻辑和复杂度",
  data_structures: "数据建模师，专注于实体关系和类型",
  interfaces: "API设计师，专注于接口契约和协议",
  exceptions: "可靠性工程师，专注于异常处理和恢复"
};

const AGENT_SECTIONS = {
  architecture: "Section 2: 系统架构图",
  functions: "Section 3: 功能模块设计",
  algorithms: "Section 4: 核心算法与流程",
  data_structures: "Section 5: 数据结构设计",
  interfaces: "Section 6: 接口设计",
  exceptions: "Section 7: 异常处理设计"
};

const AGENT_FILES = {
  architecture: "section-2-architecture.md",
  functions: "section-3-functions.md",
  algorithms: "section-4-algorithms.md",
  data_structures: "section-5-data-structures.md",
  interfaces: "section-6-interfaces.md",
  exceptions: "section-7-exceptions.md"
};

const AGENT_FOCUS = {
  architecture: [
    "1. 分层: 识别代码层次 (Controller/Service/Repository)",
    "2. 模块: 核心模块及职责边界",
    "3. 依赖: 模块间依赖方向",
    "4. 数据流: 请求/数据的流动路径"
  ],
  functions: [
    "1. 功能点: 枚举所有用户可见功能",
    "2. 模块分组: 按业务域分组",
    "3. 入口: 每个功能的代码入口",
    "4. 交互: 功能间的调用关系"
  ],
  algorithms: [
    "1. 核心算法: 业务逻辑的关键算法",
    "2. 流程步骤: 分支/循环/条件",
    "3. 复杂度: 时间/空间复杂度",
    "4. 输入输出: 参数和返回值"
  ],
  data_structures: [
    "1. 实体: class/interface/type 定义",
    "2. 属性: 字段类型和可见性",
    "3. 关系: 继承/组合/关联",
    "4. 枚举: 枚举类型及其值"
  ],
  interfaces: [
    "1. API端点: 路径/方法/说明",
    "2. 参数: 请求参数类型和校验",
    "3. 响应: 响应格式和状态码",
    "4. 时序: 典型调用流程"
  ],
  exceptions: [
    "1. 异常类型: 自定义异常类",
    "2. 错误码: 错误码定义和含义",
    "3. 处理模式: try-catch/中间件",
    "4. 恢复策略: 重试/降级/告警"
  ]
};
```

## 效率优化

### 1. 减少冗余

**Before (冗余)**:
```
你是一个专业的系统架构师，具有丰富的软件设计经验。
你需要分析代码库，识别系统的分层结构...
```

**After (精简)**:
```
[ROLE] 系统架构师，专注于分层设计和模块依赖。
[TASK] 分析 src/，生成系统架构图章节。
```

### 2. 模板驱动

**Before (描述性)**:
```
请按照以下格式输出:
首先写一个二级标题...
然后添加一个Mermaid图...
```

**After (模板)**:
```
[TEMPLATE]
## 2. 系统架构图
{intro}
\`\`\`mermaid
{diagram}
\`\`\`
**图2-1 系统架构图**
### 2.1 {subsection}
{content}
```

### 3. 焦点明确

**Before (模糊)**:
```
分析项目的各个方面，包括架构、模块、依赖等
```

**After (具体)**:
```
[FOCUS]
1. 分层: Controller/Service/Repository
2. 模块: 职责边界
3. 依赖: 方向性
4. 数据流: 路径
```

### 4. 返回简洁

**Before (冗长)**:
```
请返回详细的分析结果，包括所有发现的问题...
```

**After (结构化)**:
```
[RETURN]
{"status":"completed","output_file":"xxx.md","summary":"<50字>","cross_module_notes":[],"stats":{}}
```
