# Phase 2: Deep Code Analysis

6 个并行 Agent，各自直接写入 MD 章节文件。

> **模板参考**: [../templates/agent-base.md](../templates/agent-base.md)
> **规范参考**: [../specs/cpcc-requirements.md](../specs/cpcc-requirements.md)

## Exploration → Agent 自动分配

根据 Phase 1.5 生成的 exploration 文件名自动分配对应的 analysis agent。

### 映射规则

```javascript
// Exploration 角度 → Agent 映射（基于文件名识别，不读取内容）
const EXPLORATION_TO_AGENT = {
  'architecture': 'architecture',
  'commands': 'functions',      // CLI 命令 → 功能模块
  'endpoints': 'interfaces',    // API 端点 → 接口设计
  'algorithms': 'algorithms',
  'data-structures': 'data_structures',
  'dataflow': 'data_structures', // 数据流 → 数据结构
  'interfaces': 'interfaces',
  'exceptions': 'exceptions'
};

// 从文件名提取角度
function extractAngle(filename) {
  // exploration-architecture.json → architecture
  const match = filename.match(/exploration-(.+)\.json$/);
  return match ? match[1] : null;
}

// 分配 agent
function assignAgent(explorationFile) {
  const angle = extractAngle(path.basename(explorationFile));
  return EXPLORATION_TO_AGENT[angle] || null;
}

// Agent 配置（用于 buildAgentPrompt）
const AGENT_CONFIGS = {
  architecture: {
    role: '系统架构师，专注于分层设计和模块依赖',
    section: '2',
    output: 'section-2-architecture.md',
    focus: '分层结构、模块依赖、数据流向'
  },
  functions: {
    role: '功能分析师，专注于功能点识别和交互',
    section: '3',
    output: 'section-3-functions.md',
    focus: '功能点枚举、模块分组、入口文件、功能交互'
  },
  algorithms: {
    role: '算法工程师，专注于核心逻辑和复杂度分析',
    section: '4',
    output: 'section-4-algorithms.md',
    focus: '核心算法、流程步骤、复杂度、输入输出'
  },
  data_structures: {
    role: '数据建模师，专注于实体关系和类型定义',
    section: '5',
    output: 'section-5-data-structures.md',
    focus: '实体定义、属性类型、关系映射、枚举'
  },
  interfaces: {
    role: 'API设计师，专注于接口契约和协议',
    section: '6',
    output: 'section-6-interfaces.md',
    focus: 'API端点、参数校验、响应格式、时序'
  },
  exceptions: {
    role: '可靠性工程师，专注于异常处理和恢复策略',
    section: '7',
    output: 'section-7-exceptions.md',
    focus: '异常类型、错误码、处理模式、恢复策略'
  }
};
```

### 自动发现与分配流程

```javascript
// 1. 发现所有 exploration 文件（仅看文件名）
const explorationFiles = bash(`find ${sessionFolder} -name "exploration-*.json" -type f`)
  .split('\n')
  .filter(f => f.trim());

// 2. 按文件名自动分配 agent
const agentAssignments = explorationFiles.map(file => {
  const angle = extractAngle(path.basename(file));
  const agentName = EXPLORATION_TO_AGENT[angle];
  return {
    exploration_file: file,
    angle: angle,
    agent: agentName,
    output_file: AGENT_CONFIGS[agentName]?.output
  };
}).filter(a => a.agent);

// 3. 补充未被 exploration 覆盖的必需 agent（分配相关 exploration）
const coveredAgents = new Set(agentAssignments.map(a => a.agent));
const requiredAgents = ['architecture', 'functions', 'algorithms', 'data_structures', 'interfaces', 'exceptions'];
const missingAgents = requiredAgents.filter(a => !coveredAgents.has(a));

// 相关性映射：为缺失 agent 分配最相关的 exploration
const RELATED_EXPLORATIONS = {
  architecture: ['architecture', 'dataflow', 'interfaces'],
  functions: ['commands', 'endpoints', 'architecture'],
  algorithms: ['algorithms', 'dataflow', 'architecture'],
  data_structures: ['data-structures', 'dataflow', 'architecture'],
  interfaces: ['interfaces', 'endpoints', 'architecture'],
  exceptions: ['exceptions', 'algorithms', 'architecture']
};

function findRelatedExploration(agent, availableFiles) {
  const preferences = RELATED_EXPLORATIONS[agent] || ['architecture'];
  for (const pref of preferences) {
    const match = availableFiles.find(f => f.includes(`exploration-${pref}.json`));
    if (match) return { file: match, angle: pref, isRelated: true };
  }
  // 最后兜底：任意 exploration 都比没有强
  return availableFiles.length > 0
    ? { file: availableFiles[0], angle: extractAngle(path.basename(availableFiles[0])), isRelated: true }
    : { file: null, angle: null, isRelated: false };
}

missingAgents.forEach(agent => {
  const related = findRelatedExploration(agent, explorationFiles);
  agentAssignments.push({
    exploration_file: related.file,
    angle: related.angle,
    agent: agent,
    output_file: AGENT_CONFIGS[agent].output,
    is_related: related.isRelated  // 标记为相关而非直接匹配
  });
});

console.log(`
## Agent Auto-Assignment

Found ${explorationFiles.length} exploration files:
${agentAssignments.map(a => {
  if (!a.exploration_file) return `- ${a.agent} agent (no exploration)`;
  if (a.is_related) return `- ${a.agent} agent ← ${a.angle} (related)`;
  return `- ${a.agent} agent ← ${a.angle} (direct)`;
}).join('\n')}
`);
```

---

## Agent 执行前置条件

**每个 Agent 接收 exploration 文件路径，自行读取内容**：

```javascript
// Agent prompt 中包含文件路径
// Agent 启动后的操作顺序：
// 1. Read exploration 文件（如有）
// 2. Read CPCC 规范文件
// 3. 执行分析任务
```

规范文件路径（相对于 skill 根目录）：
- `specs/cpcc-requirements.md` - CPCC 软著申请规范要求

---

## Agent 配置

| Agent | 输出文件 | 章节 |
|-------|----------|------|
| architecture | section-2-architecture.md | 系统架构图 |
| functions | section-3-functions.md | 功能模块设计 |
| algorithms | section-4-algorithms.md | 核心算法与流程 |
| data_structures | section-5-data-structures.md | 数据结构设计 |
| interfaces | section-6-interfaces.md | 接口设计 |
| exceptions | section-7-exceptions.md | 异常处理设计 |

## CPCC 规范要点 (所有 Agent 共用)

```
[CPCC_SPEC]
1. 内容基于代码分析，无臆测或未来计划
2. 图表编号格式: 图N-M (如图2-1, 图3-1)
3. 每个子章节内容不少于100字
4. Mermaid 语法必须正确可渲染
5. 包含具体文件路径引用
6. 中文输出，技术术语可用英文
```

## 执行流程

```javascript
// 1. 发现 exploration 文件并自动分配 agent
const explorationFiles = bash(`find ${sessionFolder} -name "exploration-*.json" -type f`)
  .split('\n')
  .filter(f => f.trim());

const agentAssignments = explorationFiles.map(file => {
  const angle = extractAngle(path.basename(file));
  const agentName = EXPLORATION_TO_AGENT[angle];
  return { exploration_file: file, angle, agent: agentName };
}).filter(a => a.agent);

// 补充必需 agent
const coveredAgents = new Set(agentAssignments.map(a => a.agent));
const requiredAgents = ['architecture', 'functions', 'algorithms', 'data_structures', 'interfaces', 'exceptions'];
requiredAgents.filter(a => !coveredAgents.has(a)).forEach(agent => {
  agentAssignments.push({ exploration_file: null, angle: null, agent });
});

// 2. 准备目录
Bash(`mkdir -p ${outputDir}/sections`);

// 3. 并行启动所有 Agent（传递 exploration 文件路径）
const results = await Promise.all(
  agentAssignments.map(assignment =>
    Task({
      subagent_type: "cli-explore-agent",
      run_in_background: false,
      description: `Analyze: ${assignment.agent}`,
      prompt: buildAgentPrompt(assignment, metadata, outputDir)
    })
  )
);

// 4. 收集返回信息
const summaries = results.map(r => JSON.parse(r));

// 5. 传递给 Phase 2.5
return { summaries, cross_notes: summaries.flatMap(s => s.cross_module_notes) };
```

### Agent Prompt 构建

```javascript
function buildAgentPrompt(assignment, metadata, outputDir) {
  const config = AGENT_CONFIGS[assignment.agent];
  let contextSection = '';

  if (assignment.exploration_file) {
    const matchType = assignment.is_related ? '相关' : '直接匹配';
    contextSection = `[CONTEXT]
**Exploration 文件**: ${assignment.exploration_file}
**匹配类型**: ${matchType}
首先读取此文件获取 ${assignment.angle} 探索结果作为分析上下文。
${assignment.is_related ? `注意：这是相关探索结果（非直接匹配），请提取与 ${config.focus} 相关的信息。` : ''}
`;
  }

  return `
${contextSection}
[SPEC]
读取规范文件：
- Read: ${skillRoot}/specs/cpcc-requirements.md

[ROLE] ${config.role}

[TASK]
分析 ${metadata.scope_path}，生成 Section ${config.section}。
输出: ${outputDir}/sections/${config.output}

[CPCC_SPEC]
- 内容基于代码分析，无臆测
- 图表编号: 图${config.section}-1, 图${config.section}-2...
- 每个子章节 ≥100字
- 包含文件路径引用

[FOCUS]
${config.focus}

[RETURN JSON]
{"status":"completed","output_file":"${config.output}","summary":"<50字>","cross_module_notes":[],"stats":{}}
`;
}
```

---

## Agent 提示词

### Architecture

```javascript
Task({
  subagent_type: "cli-explore-agent",
  run_in_background: false,
  prompt: `
[SPEC]
首先读取规范文件：
- Read: ${skillRoot}/specs/cpcc-requirements.md
严格遵循 CPCC 软著申请规范要求。

[ROLE] 系统架构师，专注于分层设计和模块依赖。

[TASK]
分析 ${meta.scope_path}，生成 Section 2: 系统架构图。
输出: ${outDir}/sections/section-2-architecture.md

[CPCC_SPEC]
- 内容基于代码分析，无臆测
- 图表编号: 图2-1, 图2-2...
- 每个子章节 ≥100字
- 包含文件路径引用

[TEMPLATE]
## 2. 系统架构图

本章节展示${meta.software_name}的系统架构设计。

\`\`\`mermaid
graph TD
    subgraph Layer1["层名"]
        Comp1[组件1]
    end
    Comp1 --> Comp2
\`\`\`

**图2-1 系统架构图**

### 2.1 分层说明
| 层级 | 组件 | 职责 |
|------|------|------|

### 2.2 模块依赖
| 模块 | 依赖 | 说明 |
|------|------|------|

[FOCUS]
1. 分层: 识别代码层次 (Controller/Service/Repository 或其他)
2. 模块: 核心模块及职责边界
3. 依赖: 模块间依赖方向
4. 数据流: 请求/数据的流动路径

[RETURN JSON]
{"status":"completed","output_file":"section-2-architecture.md","summary":"<50字摘要>","cross_module_notes":["跨模块发现"],"stats":{"diagrams":1,"subsections":2}}
`
})
```

### Functions

```javascript
Task({
  subagent_type: "cli-explore-agent",
  run_in_background: false,
  prompt: `
[SPEC]
首先读取规范文件：
- Read: ${skillRoot}/specs/cpcc-requirements.md
严格遵循 CPCC 软著申请规范要求。

[ROLE] 功能分析师，专注于功能点识别和交互。

[TASK]
分析 ${meta.scope_path}，生成 Section 3: 功能模块设计。
输出: ${outDir}/sections/section-3-functions.md

[CPCC_SPEC]
- 内容基于代码分析，无臆测
- 图表编号: 图3-1, 图3-2...
- 每个子章节 ≥100字
- 包含文件路径引用

[TEMPLATE]
## 3. 功能模块设计

本章节展示${meta.software_name}的功能模块结构。

\`\`\`mermaid
flowchart TD
    ROOT["${meta.software_name}"]
    subgraph Group1["模块组1"]
        F1["功能1"]
    end
    ROOT --> Group1
\`\`\`

**图3-1 功能模块结构图**

### 3.1 功能清单
| ID | 功能名称 | 模块 | 入口文件 | 说明 |
|----|----------|------|----------|------|

### 3.2 功能交互
| 调用方 | 被调用方 | 触发条件 |
|--------|----------|----------|

[FOCUS]
1. 功能点: 枚举所有用户可见功能
2. 模块分组: 按业务域分组
3. 入口: 每个功能的代码入口 \`src/path/file.ts\`
4. 交互: 功能间的调用关系

[RETURN JSON]
{"status":"completed","output_file":"section-3-functions.md","summary":"<50字>","cross_module_notes":[],"stats":{}}
`
})
```

### Algorithms

```javascript
Task({
  subagent_type: "cli-explore-agent",
  run_in_background: false,
  prompt: `
[SPEC]
首先读取规范文件：
- Read: ${skillRoot}/specs/cpcc-requirements.md
严格遵循 CPCC 软著申请规范要求。

[ROLE] 算法工程师，专注于核心逻辑和复杂度分析。

[TASK]
分析 ${meta.scope_path}，生成 Section 4: 核心算法与流程。
输出: ${outDir}/sections/section-4-algorithms.md

[CPCC_SPEC]
- 内容基于代码分析，无臆测
- 图表编号: 图4-1, 图4-2... (每个算法一个流程图)
- 每个算法说明 ≥100字
- 包含文件路径和行号引用

[TEMPLATE]
## 4. 核心算法与流程

本章节展示${meta.software_name}的核心算法设计。

### 4.1 {算法名称}

**说明**: {描述，≥100字}
**位置**: \`src/path/file.ts:line\`

**输入**: param1 (type) - 说明
**输出**: result (type) - 说明

\`\`\`mermaid
flowchart TD
    Start([开始]) --> Input[/输入/]
    Input --> Check{判断}
    Check -->|是| P1[步骤1]
    Check -->|否| P2[步骤2]
    P1 --> End([结束])
    P2 --> End
\`\`\`

**图4-1 {算法名称}流程图**

### 4.N 复杂度分析
| 算法 | 时间 | 空间 | 文件 |
|------|------|------|------|

[FOCUS]
1. 核心算法: 业务逻辑的关键算法 (>10行或含分支循环)
2. 流程步骤: 分支/循环/条件逻辑
3. 复杂度: 时间/空间复杂度估算
4. 输入输出: 参数类型和返回值

[RETURN JSON]
{"status":"completed","output_file":"section-4-algorithms.md","summary":"<50字>","cross_module_notes":[],"stats":{}}
`
})
```

### Data Structures

```javascript
Task({
  subagent_type: "cli-explore-agent",
  run_in_background: false,
  prompt: `
[SPEC]
首先读取规范文件：
- Read: ${skillRoot}/specs/cpcc-requirements.md
严格遵循 CPCC 软著申请规范要求。

[ROLE] 数据建模师，专注于实体关系和类型定义。

[TASK]
分析 ${meta.scope_path}，生成 Section 5: 数据结构设计。
输出: ${outDir}/sections/section-5-data-structures.md

[CPCC_SPEC]
- 内容基于代码分析，无臆测
- 图表编号: 图5-1 (数据结构类图)
- 每个子章节 ≥100字
- 包含文件路径引用

[TEMPLATE]
## 5. 数据结构设计

本章节展示${meta.software_name}的核心数据结构。

\`\`\`mermaid
classDiagram
    class Entity1 {
        +type field1
        +method1()
    }
    Entity1 "1" --> "*" Entity2 : 关系
\`\`\`

**图5-1 数据结构类图**

### 5.1 实体说明
| 实体 | 类型 | 文件 | 说明 |
|------|------|------|------|

### 5.2 关系说明
| 源 | 目标 | 类型 | 基数 |
|----|------|------|------|

[FOCUS]
1. 实体: class/interface/type 定义
2. 属性: 字段类型和可见性 (+public/-private/#protected)
3. 关系: 继承(--|>)/组合(*--)/关联(-->)
4. 枚举: enum 类型及其值

[RETURN JSON]
{"status":"completed","output_file":"section-5-data-structures.md","summary":"<50字>","cross_module_notes":[],"stats":{}}
`
})
```

### Interfaces

```javascript
Task({
  subagent_type: "cli-explore-agent",
  run_in_background: false,
  prompt: `
[SPEC]
首先读取规范文件：
- Read: ${skillRoot}/specs/cpcc-requirements.md
严格遵循 CPCC 软著申请规范要求。

[ROLE] API设计师，专注于接口契约和协议。

[TASK]
分析 ${meta.scope_path}，生成 Section 6: 接口设计。
输出: ${outDir}/sections/section-6-interfaces.md

[CPCC_SPEC]
- 内容基于代码分析，无臆测
- 图表编号: 图6-1, 图6-2... (每个核心接口一个时序图)
- 每个接口详情 ≥100字
- 包含文件路径引用

[TEMPLATE]
## 6. 接口设计

本章节展示${meta.software_name}的接口设计。

\`\`\`mermaid
sequenceDiagram
    participant C as Client
    participant A as API
    participant S as Service
    C->>A: POST /api/xxx
    A->>S: method()
    S-->>A: result
    A-->>C: 200 OK
\`\`\`

**图6-1 {接口名}时序图**

### 6.1 接口清单
| 接口 | 方法 | 路径 | 说明 |
|------|------|------|------|

### 6.2 接口详情

#### METHOD /path
**请求**:
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|

**响应**:
| 字段 | 类型 | 说明 |
|------|------|------|

[FOCUS]
1. API端点: 路径/方法/说明
2. 参数: 请求参数类型和校验规则
3. 响应: 响应格式、状态码、错误码
4. 时序: 典型调用流程 (选2-3个核心接口)

[RETURN JSON]
{"status":"completed","output_file":"section-6-interfaces.md","summary":"<50字>","cross_module_notes":[],"stats":{}}
`
})
```

### Exceptions

```javascript
Task({
  subagent_type: "cli-explore-agent",
  run_in_background: false,
  prompt: `
[SPEC]
首先读取规范文件：
- Read: ${skillRoot}/specs/cpcc-requirements.md
严格遵循 CPCC 软著申请规范要求。

[ROLE] 可靠性工程师，专注于异常处理和恢复策略。

[TASK]
分析 ${meta.scope_path}，生成 Section 7: 异常处理设计。
输出: ${outDir}/sections/section-7-exceptions.md

[CPCC_SPEC]
- 内容基于代码分析，无臆测
- 图表编号: 图7-1 (异常处理流程图)
- 每个子章节 ≥100字
- 包含文件路径引用

[TEMPLATE]
## 7. 异常处理设计

本章节展示${meta.software_name}的异常处理机制。

\`\`\`mermaid
flowchart TD
    Req[请求] --> Try{Try-Catch}
    Try -->|正常| Process[处理]
    Try -->|异常| ErrType{类型}
    ErrType -->|E1| H1[处理1]
    ErrType -->|E2| H2[处理2]
    H1 --> Log[日志]
    H2 --> Log
    Process --> Resp[响应]
\`\`\`

**图7-1 异常处理流程图**

### 7.1 异常类型
| 异常类 | 错误码 | HTTP状态 | 说明 |
|--------|--------|----------|------|

### 7.2 恢复策略
| 场景 | 策略 | 说明 |
|------|------|------|

[FOCUS]
1. 异常类型: 自定义异常类及继承关系
2. 错误码: 错误码定义和分类
3. 处理模式: try-catch/中间件/装饰器
4. 恢复策略: 重试/降级/熔断/告警

[RETURN JSON]
{"status":"completed","output_file":"section-7-exceptions.md","summary":"<50字>","cross_module_notes":[],"stats":{}}
`
})
```

---

## Output

各 Agent 写入 `sections/section-N-xxx.md`，返回简要 JSON 供 Phase 2.5 汇总。
