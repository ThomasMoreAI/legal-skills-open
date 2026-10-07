# Phase 1: Metadata Collection

Collect software metadata for document header and context.

## Execution

### Step 1: Software Name & Version

```javascript
AskUserQuestion({
  questions: [{
    question: "请输入软件名称（将显示在文档页眉）：",
    header: "软件名称",
    multiSelect: false,
    options: [
      {label: "自动检测", description: "从 package.json 或项目配置读取"},
      {label: "手动输入", description: "输入自定义名称"}
    ]
  }]
})
```

### Step 2: Software Category

```javascript
AskUserQuestion({
  questions: [{
    question: "软件属于哪种类型？",
    header: "软件类型",
    multiSelect: false,
    options: [
      {label: "命令行工具 (CLI)", description: "重点描述命令、参数"},
      {label: "后端服务/API", description: "重点描述端点、协议"},
      {label: "SDK/库", description: "重点描述接口、集成"},
      {label: "数据处理系统", description: "重点描述数据流、转换"},
      {label: "自动化脚本", description: "重点描述工作流、触发器"}
    ]
  }]
})
```

### Step 3: Scope Definition

```javascript
AskUserQuestion({
  questions: [{
    question: "分析范围是什么？",
    header: "分析范围",
    multiSelect: false,
    options: [
      {label: "整个项目", description: "分析全部源代码"},
      {label: "指定目录", description: "仅分析 src/ 或其他目录"},
      {label: "自定义路径", description: "手动指定路径"}
    ]
  }]
})
```

## Output

Save metadata to `project-metadata.json`:

```json
{
  "software_name": "智能数据分析系统",
  "version": "V1.0.0",
  "category": "后端服务/API",
  "scope_path": "src/",
  "tech_stack": {
    "language": "TypeScript",
    "runtime": "Node.js 18+",
    "framework": "Express.js",
    "dependencies": ["mongoose", "redis", "bull"]
  },
  "entry_points": ["src/index.ts", "src/cli.ts"],
  "main_modules": ["auth", "data", "api", "worker"]
}
```
