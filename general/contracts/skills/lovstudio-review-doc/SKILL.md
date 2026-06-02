---
name: lovstudio-review-doc
title: review-doc — Review & Annotate Documents / 批阅文档与合同
description: 'Review and annotate documents/contracts — output annotated docx with comments or tracked changes. Core: contract review (risk clauses, rights imbalance, vague wording, missing clauses); also general document review (grammar, logic, formatting). 批阅文档/合同 — 审阅任意文档并以批注或修订模式输出带标注的 docx。 核心场景：合同/协议审查（风险条款、权利义务、模糊表述、缺失条款）， 也支持通用文档审阅（语法、逻辑、格式）。 Trigger when: user asks to "审阅", "批阅", "批注", "review", "审查合同", "review contract", "review agreement", "annotate document", "check contract", "合同审查", "文档批注", or provides a document (.docx) for review.'
author: lovstudio
author_url: https://github.com/lovstudio/skills/tree/main/skills/review-doc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: zh
---

# review-doc — Review & Annotate Documents / 批阅文档与合同

AI-powered document and contract review. Outputs annotated docx with comments
and/or tracked changes.

审阅文档或合同，AI 进行审查分析，将审查意见以批注（comment）或修订模式
（track changes）写回文档，输出带批注的 docx。

## When to Use

- User provides a document for review, annotation, or audit
  用户提供文档要求审阅、审查、批注、批阅
- Contract/agreement review: risk clauses, rights imbalance, vague wording, missing clauses
  合同/协议审查：识别风险条款、权利义务失衡、模糊表述、缺失条款
- General document review: grammar, logic, formatting, completeness
  通用文档审阅：语法、逻辑、格式、内容完整性
- Supports .docx input / 当前支持 .docx 格式输入

## Workflow

### Step 1: Extract text

Extract paragraph text and indices / 用脚本提取段落文本和索引：

    python3 lovstudio-review-doc/scripts/annotate_docx.py extract --input <path.docx>

Outputs JSON array, each item has `index` (paragraph number) and `text`.
Includes text inside tracked changes (`<w:ins>`) — e.g. counterparty revisions
visible in Track Changes mode.
输出 JSON 数组，每项含 `index`（段落序号）和 `text`（含修订追踪内容）。

**Important:** If the document has tracked changes (e.g. Schedule A added via
Track Changes), these paragraphs are now included in extraction. Always review
the full extracted output before generating annotations.
如果文档包含修订追踪内容（如对方以 Track Changes 添加的附件），这些段落
现已包含在提取结果中。

### Step 2: Ask the user

**IMPORTANT: Use `AskUserQuestion` BEFORE generating annotations.**

    Review mode / 审阅模式确认

    ━━━ Review type / 审阅类型 ━━━
    a) Contract review — risk clauses, rights, vague wording, missing clauses
       合同/协议审查 — 风险条款、权利义务、模糊表述、缺失条款
    b) General document review — grammar, logic, formatting, completeness
       通用文档审阅 — 语法、逻辑、格式、内容完整性

    ━━━ Annotation mode / 批注方式 ━━━
    a) Comments only (default) — add comments alongside text, no changes
       批注模式（默认） — 在原文旁加 comment，不改原文
    b) Track changes — directly modify text, recipient can accept/reject
       修订模式 — 用 track changes 直接改原文，对方可逐条接受/拒绝
    c) Comments + track changes — comments for analysis, revisions for suggestions
       批注 + 修订 — 批注写分析意见，修订写建议改法

    ━━━ Author name / 批注者署名 ━━━
    Default "手工川", customizable

### Step 3: AI Review

Review the extracted text. For contract review, focus on:

根据提取的文本进行审查。对于合同审查，重点关注：

1. **Risk clauses / 风险条款** — one-sided rights, disclaimers, force majeure abuse
2. **Rights imbalance / 权利义务失衡** — disproportionate obligations, inadequate consideration
3. **Vague wording / 模糊表述** — "reasonable", "appropriate" without objective criteria
4. **Missing clauses / 缺失条款** — dispute resolution, post-termination obligations, IP ownership
5. **Terms & amounts / 期限与金额** — unreasonable durations or amounts
6. **Legal compliance / 法律合规** — governing law, arbitration clauses

生成 annotations JSON，格式：

    {
      "comments": [
        {
          "paragraph": 18,
          "text": "【风险】Sourced Deal 认定...",
          "author": "手工川"
        }
      ],
      "revisions": [
        {
          "paragraph": 12,
          "old": "terminates automatically",
          "new": "terminates automatically, provided that...",
          "author": "手工川"
        }
      ]
    }

Annotation text format / 批注文本格式规范：
- Lead with tag / 以标签开头：`【风险/Risk】`、`【建议/Suggestion】`、`【缺失/Missing】`、`【模糊/Vague】`、`【注意/Note】`
- Concise, 1-3 sentences per annotation / 简明扼要，每条批注控制在 1-3 句话
- Provide concrete revision direction when suggesting changes / 有建议时给出具体修改方向
- Match the document language — Chinese docs get Chinese annotations, English docs get English, mixed docs get bilingual / 批注语言跟随文档语言

### Step 4: Apply annotations

将 JSON 写入临时文件，调用脚本：

    python3 lovstudio-review-doc/scripts/annotate_docx.py annotate \
      --input <原文.docx> \
      --annotations <annotations.json> \
      --output <输出路径.docx>

### Step 5: Output naming

输出文件名规范：`手工川-{原文件名}-审阅-{YYYY-MM-DD}-v0.1.docx`

放在原文件同目录下。

## CLI Reference

    python3 annotate_docx.py extract --input <path.docx>
    python3 annotate_docx.py annotate --input <path.docx> --annotations <json> --output <path.docx>

| Subcommand | Argument | Description |
|------------|----------|-------------|
| `extract` | `--input` | 输入 docx 路径 |
| `annotate` | `--input` | 输入 docx 路径 |
| `annotate` | `--annotations` | JSON 批注文件路径 |
| `annotate` | `--output` | 输出 docx 路径 |

## Comment JSON Fields

| Field | Required | Description |
|-------|----------|-------------|
| `paragraph` | Yes | 0-based 段落索引 |
| `text` | Yes | 批注内容 |
| `author` | No | 批注者署名（默认 "Reviewer"） |
| `start` | No | 字符偏移起始位置（精确高亮） |
| `end` | No | 字符偏移结束位置 |

## Revision JSON Fields

| Field | Required | Description |
|-------|----------|-------------|
| `paragraph` | Yes | 0-based 段落索引 |
| `old` | Yes | 要替换的原文 |
| `new` | Yes | 修改后的文本 |
| `author` | No | 修订者署名 |

## Caveats

- **Revisions match per-run**: `old` text in revisions must match a single
  `<w:r>` (run) in the paragraph. If the target text is split across multiple
  runs (common with smart quotes, spell-check, or mixed formatting), the
  revision will be skipped. Workaround: match a substring within one run, or
  use a comment instead.
  修订的 `old` 文本必须完整匹配段落中的单个 run。如果目标文本跨 run，修订会
  被跳过。可改用批注替代。
- **Pre-existing comments**: the script auto-detects max existing comment ID
  and starts new IDs after it. No manual ID management needed.
  脚本自动检测已有批注的最大 ID，新批注从其后开始编号。

## Dependencies

    pip install python-docx --break-system-packages
