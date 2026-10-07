# Phase 5: Compliance Review & Iterative Refinement

Discovery-driven refinement loop until CPCC compliance is met.

## Execution

### Step 1: Extract Compliance Issues

```javascript
function extractComplianceIssues(validationResult, deepAnalysis) {
  return {
    // Missing or incomplete sections
    missingSections: validationResult.details
      .filter(d => !d.pass)
      .map(d => ({
        section: d.name,
        severity: 'critical',
        suggestion: `需要补充 ${d.name} 相关内容`
      })),

    // Features with weak descriptions (< 50 chars)
    weakDescriptions: (deepAnalysis.functions?.feature_list || [])
      .filter(f => !f.description || f.description.length < 50)
      .map(f => ({
        feature: f.name,
        current: f.description || '(无描述)',
        severity: 'warning'
      })),

    // Complex algorithms without detailed flowcharts
    complexAlgorithms: (deepAnalysis.algorithms?.algorithms || [])
      .filter(a => (a.complexity || 0) > 10 && (a.steps?.length || 0) < 5)
      .map(a => ({
        algorithm: a.name,
        complexity: a.complexity,
        file: a.file,
        severity: 'warning'
      })),

    // Data relationships without descriptions
    incompleteRelationships: (deepAnalysis.data_structures?.relationships || [])
      .filter(r => !r.description)
      .map(r => ({from: r.from, to: r.to, severity: 'info'})),

    // Diagram validation issues
    diagramIssues: (deepAnalysis.diagrams?.validation || [])
      .filter(d => !d.valid)
      .map(d => ({file: d.file, issues: d.issues, severity: 'critical'}))
  };
}
```

### Step 2: Build Dynamic Questions

```javascript
function buildComplianceQuestions(issues) {
  const questions = [];

  if (issues.missingSections.length > 0) {
    questions.push({
      question: `发现 ${issues.missingSections.length} 个章节内容不完整，需要补充哪些？`,
      header: "章节补充",
      multiSelect: true,
      options: issues.missingSections.slice(0, 4).map(s => ({
        label: s.section,
        description: s.suggestion
      }))
    });
  }

  if (issues.weakDescriptions.length > 0) {
    questions.push({
      question: `以下 ${issues.weakDescriptions.length} 个功能描述过于简短，请选择需要详细说明的：`,
      header: "功能描述",
      multiSelect: true,
      options: issues.weakDescriptions.slice(0, 4).map(f => ({
        label: f.feature,
        description: `当前：${f.current.substring(0, 30)}...`
      }))
    });
  }

  if (issues.complexAlgorithms.length > 0) {
    questions.push({
      question: `发现 ${issues.complexAlgorithms.length} 个复杂算法缺少详细流程图，是否生成？`,
      header: "算法详解",
      multiSelect: false,
      options: [
        {label: "全部生成 (推荐)", description: "为所有复杂算法生成含分支/循环的流程图"},
        {label: "仅最复杂的", description: `仅为 ${issues.complexAlgorithms[0]?.algorithm} 生成`},
        {label: "跳过", description: "保持当前简单流程图"}
      ]
    });
  }

  questions.push({
    question: "如何处理当前文档？",
    header: "操作",
    multiSelect: false,
    options: [
      {label: "应用修改并继续", description: "应用上述选择，继续检查"},
      {label: "完成文档", description: "当前文档满足要求，生成最终版本"},
      {label: "重新分析", description: "使用不同配置重新分析代码"}
    ]
  });

  return questions.slice(0, 4);
}
```

### Step 3: Apply Updates

```javascript
async function applyComplianceUpdates(responses, issues, analyses, outputDir) {
  const updates = [];

  if (responses['章节补充']) {
    for (const section of responses['章节补充']) {
      const sectionAnalysis = await Task({
        subagent_type: "cli-explore-agent",
        prompt: `深入分析 ${section.section} 所需内容...`
      });
      updates.push({type: 'section_supplement', section: section.section, data: sectionAnalysis});
    }
  }

  if (responses['算法详解'] === '全部生成 (推荐)') {
    for (const algo of issues.complexAlgorithms) {
      const detailedSteps = await analyzeAlgorithmInDepth(algo, analyses);
      const flowchart = generateAlgorithmFlowchart({
        name: algo.algorithm,
        inputs: detailedSteps.inputs,
        outputs: detailedSteps.outputs,
        steps: detailedSteps.steps
      });
      Write(`${outputDir}/diagrams/algorithm-${sanitizeId(algo.algorithm)}-detailed.mmd`, flowchart);
      updates.push({type: 'algorithm_flowchart', algorithm: algo.algorithm});
    }
  }

  return updates;
}
```

### Step 4: Iteration Loop

```javascript
async function runComplianceLoop(documentPath, analyses, metadata, outputDir) {
  let iteration = 0;
  const maxIterations = 5;
  
  while (iteration < maxIterations) {
    iteration++;
    
    // Validate current document
    const document = Read(documentPath);
    const validation = validateCPCCCompliance(document, analyses);
    
    // Extract issues
    const issues = extractComplianceIssues(validation, analyses);
    const totalIssues = Object.values(issues).flat().length;
    
    if (totalIssues === 0) {
      console.log("✅ 所有检查通过，文档符合 CPCC 要求");
      break;
    }
    
    // Ask user
    const questions = buildComplianceQuestions(issues);
    const responses = await AskUserQuestion({questions});
    
    if (responses['操作'] === '完成文档') break;
    if (responses['操作'] === '重新分析') return {action: 'restart'};
    
    // Apply updates
    const updates = await applyComplianceUpdates(responses, issues, analyses, outputDir);
    
    // Regenerate document
    const updatedDocument = regenerateDocument(document, updates, analyses);
    Write(documentPath, updatedDocument);
    
    // Archive iteration
    Write(`${outputDir}/iterations/v${iteration}.md`, document);
  }
  
  return {action: 'finalized', iterations: iteration};
}
```

## Output

Final compliant document + iteration history in `iterations/`.
