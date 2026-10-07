# CPCC Compliance Requirements

China Copyright Protection Center (CPCC) requirements for software design specification.

## When to Use

| Phase | Usage | Section |
|-------|-------|---------|
| Phase 4 | Check document structure before assembly | Document Requirements, Mandatory Sections |
| Phase 4 | Apply correct figure numbering | Figure Numbering Convention |
| Phase 5 | Validate before each iteration | Validation Function |
| Phase 5 | Handle failures during refinement | Error Handling |

---

## Document Requirements

### Format
- [ ] 页眉包含软件名称和版本号
- [ ] 页码位于右上角说明
- [ ] 每页不少于30行文字（图表页除外）
- [ ] A4纵向排版，文字从左至右

### Mandatory Sections (7 章节)
- [ ] 1. 软件概述
- [ ] 2. 系统架构图
- [ ] 3. 功能模块设计
- [ ] 4. 核心算法与流程
- [ ] 5. 数据结构设计
- [ ] 6. 接口设计
- [ ] 7. 异常处理设计

### Content Requirements
- [ ] 所有内容基于代码分析
- [ ] 无臆测或未来计划
- [ ] 无原始指令性文字
- [ ] Mermaid 语法正确
- [ ] 图表编号和说明完整

## Validation Function

```javascript
function validateCPCCCompliance(document, analyses) {
  const checks = [
    {name: "软件概述完整性", pass: document.includes("## 1. 软件概述")},
    {name: "系统架构图存在", pass: document.includes("图2-1 系统架构图")},
    {name: "功能模块设计完整", pass: document.includes("## 3. 功能模块设计")},
    {name: "核心算法描述", pass: document.includes("## 4. 核心算法与流程")},
    {name: "数据结构设计", pass: document.includes("## 5. 数据结构设计")},
    {name: "接口设计说明", pass: document.includes("## 6. 接口设计")},
    {name: "异常处理设计", pass: document.includes("## 7. 异常处理设计")},
    {name: "Mermaid图表语法", pass: !document.includes("mermaid error")},
    {name: "页眉信息", pass: document.includes("页眉")},
    {name: "页码说明", pass: document.includes("页码")}
  ];

  return {
    passed: checks.filter(c => c.pass).length,
    total: checks.length,
    details: checks
  };
}
```

## Software Categories

| Category | Document Focus |
|----------|----------------|
| 命令行工具 (CLI) | 命令、参数、使用流程 |
| 后端服务/API | 端点、协议、数据流 |
| SDK/库 | 接口、集成、使用示例 |
| 数据处理系统 | 数据流、转换、ETL |
| 自动化脚本 | 工作流、触发器、调度 |

## Figure Numbering Convention

| Section | Figure | Title |
|---------|--------|-------|
| 2 | 图2-1 | 系统架构图 |
| 3 | 图3-1 | 功能模块结构图 |
| 4 | 图4-N | {算法名称}流程图 |
| 5 | 图5-1 | 数据结构类图 |
| 6 | 图6-N | {接口名称}时序图 |
| 7 | 图7-1 | 异常处理流程图 |

## Error Handling

| Error | Recovery |
|-------|----------|
| Analysis timeout | Reduce scope, retry |
| Missing section data | Re-run targeted agent |
| Diagram validation fails | Regenerate with fixes |
| User abandons iteration | Save progress, allow resume |

---

## Integration with Phases

**Phase 4 - Document Assembly**:
```javascript
// Before assembling document
const docChecks = [
  {check: "页眉格式", value: `<!-- 页眉：${metadata.software_name} - 版本号：${metadata.version} -->`},
  {check: "页码说明", value: `<!-- 注：最终文档页码位于每页右上角 -->`}
];

// Apply figure numbering from convention table
const figureNumbers = getFigureNumbers(sectionIndex);
```

**Phase 5 - Compliance Refinement**:
```javascript
// In 05-compliance-refinement.md
const validation = validateCPCCCompliance(document, analyses);

if (validation.passed < validation.total) {
  // Failed checks become discovery questions
  const failedChecks = validation.details.filter(d => !d.pass);
  discoveries.complianceIssues = failedChecks;
}
```
