# Phase 4: Document Assembly

生成索引式文档，通过 markdown 链接引用章节文件。

> **规范参考**: [../specs/cpcc-requirements.md](../specs/cpcc-requirements.md)

## 设计原则

1. **引用而非嵌入**：主文档通过链接引用章节，不复制内容
2. **索引 + 综述**：主文档提供导航和软件概述
3. **CPCC 合规**：保持章节编号符合软著申请要求
4. **独立可读**：各章节文件可单独阅读

## 输入

```typescript
interface AssemblyInput {
  output_dir: string;
  metadata: ProjectMetadata;
  consolidation: {
    synthesis: string;           // 跨章节综合分析
    section_summaries: Array<{
      file: string;
      title: string;
      summary: string;
    }>;
    issues: { errors: Issue[], warnings: Issue[], info: Issue[] };
    stats: { total_sections: number, total_diagrams: number };
  };
}
```

## 执行流程

```javascript
// 1. 检查是否有阻塞性问题
if (consolidation.issues.errors.length > 0) {
  const response = await AskUserQuestion({
    questions: [{
      question: `发现 ${consolidation.issues.errors.length} 个严重问题，如何处理？`,
      header: "阻塞问题",
      multiSelect: false,
      options: [
        {label: "查看并修复", description: "显示问题列表，手动修复后重试"},
        {label: "忽略继续", description: "跳过问题检查，继续装配"},
        {label: "终止", description: "停止文档生成"}
      ]
    }]
  });

  if (response === "查看并修复") {
    return { action: "fix_required", errors: consolidation.issues.errors };
  }
  if (response === "终止") {
    return { action: "abort" };
  }
}

// 2. 生成索引式文档（不读取章节内容）
const doc = generateIndexDocument(metadata, consolidation);

// 3. 写入最终文件
Write(`${outputDir}/${metadata.software_name}-软件设计说明书.md`, doc);
```

## 文档模板

```markdown
<!-- 页眉：{软件名称} - 版本号：{版本号} -->

# {软件名称} 软件设计说明书

## 文档信息

| 项目 | 内容 |
|------|------|
| 软件名称 | {software_name} |
| 版本号 | {version} |
| 生成日期 | {date} |

---

## 1. 软件概述

### 1.1 软件背景与用途

[从 metadata 生成的软件背景描述]

### 1.2 开发目标与特点

[从 metadata 生成的目标和特点]

### 1.3 运行环境与技术架构

[从 metadata.tech_stack 生成]

---

## 文档导航

{consolidation.synthesis - 软件整体设计思路综述}

| 章节 | 说明 | 详情 |
|------|------|------|
| 2. 系统架构设计 | {summary} | [查看](./sections/section-2-architecture.md) |
| 3. 功能模块设计 | {summary} | [查看](./sections/section-3-functions.md) |
| 4. 核心算法与流程 | {summary} | [查看](./sections/section-4-algorithms.md) |
| 5. 数据结构设计 | {summary} | [查看](./sections/section-5-data-structures.md) |
| 6. 接口设计 | {summary} | [查看](./sections/section-6-interfaces.md) |
| 7. 异常处理设计 | {summary} | [查看](./sections/section-7-exceptions.md) |

---

## 附录

- [跨模块分析报告](./cross-module-summary.md)
- [章节文件目录](./sections/)

---

<!-- 页脚：生成时间 {timestamp} -->
```

## 生成函数

```javascript
function generateIndexDocument(metadata, consolidation) {
  const date = new Date().toLocaleDateString('zh-CN');

  // 章节导航表格
  const sectionTable = consolidation.section_summaries
    .map(s => `| ${s.title} | ${s.summary} | [查看](./sections/${s.file}) |`)
    .join('\n');

  return `<!-- 页眉：${metadata.software_name} - 版本号：${metadata.version} -->

# ${metadata.software_name} 软件设计说明书

## 文档信息

| 项目 | 内容 |
|------|------|
| 软件名称 | ${metadata.software_name} |
| 版本号 | ${metadata.version} |
| 生成日期 | ${date} |

---

## 1. 软件概述

### 1.1 软件背景与用途

${generateBackground(metadata)}

### 1.2 开发目标与特点

${generateObjectives(metadata)}

### 1.3 运行环境与技术架构

${generateTechStack(metadata)}

---

## 设计综述

${consolidation.synthesis}

---

## 文档导航

| 章节 | 说明 | 详情 |
|------|------|------|
${sectionTable}

---

## 附录

- [跨模块分析报告](./cross-module-summary.md)
- [章节文件目录](./sections/)

---

<!-- 页脚：生成时间 ${new Date().toISOString()} -->
`;
}

function generateBackground(metadata) {
  const categoryDescriptions = {
    "命令行工具 (CLI)": "提供命令行界面，用户通过终端命令与系统交互",
    "后端服务/API": "提供 RESTful/GraphQL API 接口，支持前端或其他服务调用",
    "SDK/库": "提供可复用的代码库，供其他项目集成使用",
    "数据处理系统": "处理数据导入、转换、分析和导出",
    "自动化脚本": "自动执行重复性任务，提高工作效率"
  };

  return `${metadata.software_name}是一款${metadata.category}软件。${categoryDescriptions[metadata.category] || ''}

本软件基于${metadata.tech_stack.language}语言开发，运行于${metadata.tech_stack.runtime}环境，采用${metadata.tech_stack.framework || '原生'}框架实现核心功能。`;
}

function generateObjectives(metadata) {
  return `本软件旨在${metadata.purpose || '解决特定领域的技术问题'}。

主要技术特点包括${metadata.tech_stack.framework ? `采用 ${metadata.tech_stack.framework} 框架` : '模块化设计'}，具备良好的可扩展性和可维护性。`;
}

function generateTechStack(metadata) {
  return `**运行环境**

- 操作系统：${metadata.os || 'Windows/Linux/macOS'}
- 运行时：${metadata.tech_stack.runtime}
- 依赖环境：${metadata.tech_stack.dependencies?.join(', ') || '无特殊依赖'}

**技术架构**

- 架构模式：${metadata.architecture_pattern || '分层架构'}
- 核心框架：${metadata.tech_stack.framework || '原生实现'}
- 主要模块：详见第2章系统架构设计`;
}
```

## 输出结构

```
.workflow/.scratchpad/copyright-{timestamp}/
├── sections/                           # 独立章节（Phase 2 产出）
│   ├── section-2-architecture.md
│   ├── section-3-functions.md
│   └── ...
├── cross-module-summary.md             # 跨模块报告（Phase 2.5 产出）
└── {软件名称}-软件设计说明书.md         # 索引文档（本阶段产出）
```

## 与 Phase 2.5 的协作

Phase 2.5 consolidation agent 需要提供：

```typescript
interface ConsolidationOutput {
  synthesis: string;           // 设计思路综述（2-3 段落）
  section_summaries: Array<{
    file: string;              // 文件名
    title: string;             // 章节标题（如"2. 系统架构设计"）
    summary: string;           // 一句话说明
  }>;
  issues: {...};
  stats: {...};
}
```

## 关键变更

| 原设计 | 新设计 |
|--------|--------|
| 读取章节内容并拼接 | 链接引用，不读取内容 |
| 嵌入完整章节 | 仅提供导航索引 |
| 重复生成统计 | 引用 cross-module-summary.md |
| 大文件 | 精简索引文档 |
