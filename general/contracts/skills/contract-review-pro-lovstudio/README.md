# 合同批注专家 · Contract Reviewer

![Version](https://img.shields.io/badge/version-0.2.0-CC785C)

Professional-grade contract review skill. Adds comment-based issue annotations without modifying the original text. Enforces a four-layer review methodology and produces a full review deliverable.

专业级合同审阅 skill。只加批注、不改原文；四层方法论审查，并生成完整的审核交付物。

## What you get / 产出

- **Annotated contract (.docx)** — inline comments anchored to specific clauses
- **Contract summary (.docx)** — key terms, amounts, parties at a glance
- **Consolidated review opinion (.docx)** — prioritized issue list with recommendations
- **Business flowchart** — Mermaid source + rendered image

- **批注版合同（.docx）** — 精准锚定条款的批注
- **合同摘要（.docx）** — 关键条款 / 金额 / 主体一览
- **综合审核意见（.docx）** — 按优先级排序的问题清单与建议
- **业务流程图** — Mermaid 源码 + 渲染图

## Four-layer methodology / 四层方法论

0. **Entity verification** — 主体核验：确认签约方资质
1. **Basic review** — 基础审查：标题、日期、条款编号、引用一致性
2. **Business review** — 业务审查：商业条款合理性与内部一致性
3. **Legal review** — 法务审查：风险条款、责任分配、争议解决

## Language

Output language follows the contract's dominant language (detected automatically). All comments, summary, opinion, and flowchart labels are generated in the detected language.

输出语言跟随合同主导语言自动适配。

## Install

```bash
npx skills add lovstudio/contract-review-pro-skill --all -g
```

## See also

- [`review-doc`](https://github.com/lovstudio/review-doc-skill) — lightweight daily version for general document review
- [`review-doc`](https://github.com/lovstudio/review-doc-skill) — 日常轻量版，适用于普通文档审阅

## License

MIT — content adapted from jicheng's contract-review methodology.
