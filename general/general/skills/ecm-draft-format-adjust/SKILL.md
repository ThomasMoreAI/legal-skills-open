---
name: ecm-draft-format-adjust
title: ecm-draft-format-adjust
description: Word 文档格式调整 skill。当用户要求调整 / 优化 / 修正 / 排版 / 套版 / 套格式 / 按律所模板 格式化 / 按证监会要求格式化 Word 文档（包括律师工作报告、法律意见书、法律备忘录、法律意见、 会议文件、信披文件等），具体调整项包括：字体、字号、行距、段前段后、首行缩进、标题层级、 章节编号、自动编号、交叉引用、脚注、尾注、页眉页脚、页码、目录（自动生成 / 更新）、 表格样式、封面页、签字页、Markdown → Word 转换、套用律所样式 / 样式表、批量统一格式、 按 shared/templates 规范套版，或说"把这份文件格式弄一下""按律所模板排版""格式不统一帮我 改下""加个目录""生成页眉页脚""正文统一小四宋体""一级标题用黑体"等场景时触发。 典型输入：待调整的 Markdown / Word / PDF 文件、目标格式规范名（work-report / legal-opinion / legal-memo / meeting-docs / 律所自定义样式），或具体格式要求（字体 / 字号 / 行距等）。 典型输出：格式调整后的 Word 文档 + 格式检查清单 + 样式调整记录。 非触发边界：本 skill 不起草文书内容（归各起草类 skill）、不做内核审查（归 ecm-qc-*）、 不做 PDF 填表（归外部 pdf skill）。即使用户未明确说"排版 / 格式"，只要涉及 Word 的视觉 / 结构调整（标题层级、编号、目录、页眉页脚、交叉引用）也应触发。
author: zeweihan
author_url: https://github.com/zeweihan/A-market-ecm-lawyer-plugin/tree/main/skills/ecm-draft-format-adjust
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: zh
---

# ecm-draft-format-adjust

## 定位与边界

本 skill **负责**：
- **Markdown → Word 套版**：把起草类 skill 输出的 Markdown 初稿按 `shared/templates/` 下的格式规范转为 Word 文档
- **Word 文档的格式统一**：字体 / 字号 / 行距 / 段前段后 / 首行缩进的全文档统一
- **章节编号 / 自动编号**：将硬编码的"第一部分"/"第二部分"转为 Word 自动编号（Heading 样式绑定列表）
- **目录生成 / 更新**：自动插入 / 刷新目录（TOC）
- **交叉引用处理**：将形如 `{{XREF: 第N部分.小节M}}` 的占位符替换为 Word 域代码
- **页眉页脚 / 页码**：按格式规范添加页眉页脚，支持奇偶页不同 / 章节页码重置
- **封面与正文之间的分页**：插入分页符，保证封面独占一页
- **签字页格式**：按格式规范生成签字盖章页
- **表格样式统一**：应用标准表格样式（外框 / 内框 / 表头底色 / 跨页表头重复）
- **律所自定义样式表注入**：若用户提供律所 `.dotx` 模板，按其样式表套版

本 skill **不负责**：
- 文书内容的起草（归各起草类 skill）
- 内核审查修订痕迹（归 ecm-qc-*）
- PDF 的生成（Word → PDF 由用户在 Word 中另存）
- 骑缝章、电子签章的添加（由印章系统或后期处理）
- 超出 Word 的特殊排版（如需要 LaTeX、Adobe InDesign 等工具的排版需求）

## 免责声明

本 skill 做**格式化**工作，不修改文书的内容实质。格式调整后文件需律师复核确认内容未因格式化而失真。完整免责声明见 [DISCLAIMER.md](../../DISCLAIMER.md)。

## 资深律师执行标准

执行本 skill 时，必须同时遵循 [senior-lawyer-execution-standards.md](../../shared/templates/senior-lawyer-execution-standards.md)。本 skill 的任何输出不得突破四条底线：事实可追溯、法源可核验、风险可分级、建议可落地；无法核验时必须显式标注。

## 本 skill 的实务加固点

- **格式不改实体**：格式调整不得改变法律结论、事实描述、金额、日期、主体名称和风险等级。
- **修订痕迹保护**：含 tracked changes / comments 的 Word 文件不得扁平化；无法保留时必须先提示用户。
- **目录与交叉引用**：自动目录、编号、表格编号、附件编号和交叉引用应优先修复，避免申报文件结构错误。
- **失败回退**：无法转换或样式冲突时，应输出问题清单和可手工处理步骤，不得生成看似完成的错误版本。

## 前置依赖

- 外部 `docx` skill（必需）：本 skill 的 Word 操作都委托给 docx skill 执行
- `shared/templates/` 下的格式规范文件（本 skill 的"套版源"）：
  - [`work-report-format.md`](../../shared/templates/work-report-format.md)（律师工作报告 / 尽职调查报告）
  - [`legal-opinion-format.md`](../../shared/templates/legal-opinion-format.md)（法律意见书）
  - [`legal-memo-format.md`](../../shared/templates/legal-memo-format.md)（法律备忘录）
  - [`meeting-docs-format.md`](../../shared/templates/meeting-docs-format.md)（会议文件）

## 核心工作流（七步）

### Step 1：识别目标格式规范

用户可能通过以下方式指定目标格式：

1. **显式指定**：指定 `shared/templates/` 下具体文件（如 `work-report-format.md`）
2. **隐式识别**：按输入文件类型推断：
   - 律师工作报告 / 尽职调查报告 → `work-report-format.md`
   - 法律意见书 → `legal-opinion-format.md`
   - 法律备忘录 / 备忘 / 备注录 / legal memo → `legal-memo-format.md`
   - 会议通知 / 议案 / 决议 / 会议记录 / 签到表 → `meeting-docs-format.md`
3. **律所自定义**：用户提供 `.dotx` / `.docx` 模板 → 本 skill 按该模板样式表套版，但章节结构仍按标准规范
4. **手工指定**：用户直接告诉本 skill 具体参数（字体 / 字号 / 行距等），不使用标准规范

### Step 2：读取输入文件

- Markdown → 结构化解析（用 pypandoc 或标准 Markdown AST）
- Word → 调用 `docx` skill 读取样式、段落、表格、页眉页脚
- PDF → 提示用户提供 Word 源文件（PDF 的格式难以可靠回填）

### Step 3：规范化转换（按格式规范表套版）

对每个 Markdown / Word 元素按格式规范的"Markdown → Word 参数表"查找对应 Word 样式，执行：

- 段落属性（字体、字号、加粗、段前段后、行距、首行缩进、对齐）
- 标题层级映射（Markdown `# ## ###` → Word Heading 1/2/3 + 绑定自动编号样式）
- 表格样式（外框、内框、表头、跨页重复）
- 页面设置（纸张 A4 / 页边距 / 奇偶页不同）

### Step 4：自动编号 / 交叉引用 / 目录

- 将 Markdown 中的汉字编号（"第一部分"）转为 Word Heading 1 绑定的自动编号样式
- 扫描文档中的交叉引用占位符（`{{XREF: 第N部分.小节M}}` / 对应 Markdown 章节名）替换为 Word REF 域代码
- 在"封面后、引言前"插入 TOC 域代码，并触发刷新

### Step 5：页眉页脚 / 页码

- 按格式规范在 Word 中添加页眉页脚
- 奇偶页不同（律师工作报告 / 法律意见书）：奇数页右对齐文件类型、偶数页左对齐律所名
- 页码：封面 / 目录不显示；从引言起算阿拉伯数字；附件部分重新编号（若格式规范如此要求）

### Step 6：特殊段落处理

- **封面页**：按规范的元素顺序和样式生成；封面末尾自动插入分页符
- **签字盖章页**：按规范生成（律所盖章位 + 律所负责人签字行 + 经办律师签字行 + 日期）
- **表格**：应用标准表格样式；表格上方加表号表名（如 "表 5-1  股权结构穿透表"）
- **脚注 / 尾注**：统一为尾注（律师文书惯例），字号小五号

### Step 7：输出 + 格式检查清单

- Word 文档落到原始输入文件同目录（若输入为 Markdown，则落到 `04-文件输出/` 对应类别目录）
- 文件名：`{原文件名}-{YYYYMMDD}-{格式化版本}.docx`
- 生成**格式检查清单**（同目录，`格式检查-{YYYYMMDD}.md`），列明：
  - 格式规范来源（用了哪份 `shared/templates/*.md`）
  - Markdown → Word 元素映射清单（每个样式的应用数量）
  - 自动编号绑定结果（多少个章节、多少级标题使用自动编号）
  - 交叉引用处理结果（成功替换数 / 未找到目标数）
  - 目录生成结果（层级深度、条目数）
  - 页眉页脚 / 页码应用结果
  - 异常项清单（格式规范中有要求但输入文件未提供的元素，如"封面签字栏未找到必需字段"）

## 配置项

### 目标格式规范（Target Format）

- `work-report`（律师工作报告 / 尽职调查报告）
- `legal-opinion`（法律意见书）
- `legal-memo`（法律备忘录）
- `meeting-docs`（会议文件）
- `auto`（默认；按输入文件类型自动识别）
- `custom`（用户提供 `.dotx` 模板或手工指定参数）

### Word 样式绑定方式（Style Binding）

- `direct`（默认）：直接设置段落属性（字体 / 字号 / 行距等）—— 简单但不利于后期批量修改
- `style-based`：使用 Word Style 机制（推荐律所内批量出文档时使用）—— 后期修改样式即可批量应用

### 页面设置（Page Setup）

- `a4-standard`（默认）：A4，上 2.5 / 下 2.5 / 左右 2.5 cm
- `a4-tight`：上 3.5 / 下 2.5 / 左右 2.5 cm（封面用，右侧留骑缝章位）
- `custom`：用户指定

### 交叉引用处理（XRef Handling）

- `auto`（默认）：扫描占位符自动替换为 Word 域代码
- `off`：跳过交叉引用处理（保留占位符）
- `manual`：只报告占位符位置，不自动替换

### 目录（TOC）

- `on`（默认）：生成 2 级目录
- `deep`：生成 3 级目录
- `off`：不生成目录

## 输出格式契约

1. **文件路径**：`{输入目录}/{原文件名}-{YYYYMMDD}.docx`（Word 版本）
2. **格式检查清单**：同目录 Markdown，必出
3. **样式绑定结果**：按配置项 `style-based` 模式时，输出 Word 文件需保留 Style 定义（可通过 Word 文档的"样式"窗格查看）
4. **异常清单**：必出；每条异常有明确位置（章节 / 页码），不含行号（Markdown 的行号与 Word 不对应）

## 与邻近 skill 的边界

- 与 `ecm-draft-report-assembly` / `opinion-letter` / `meeting-docs` / `disclosure-review`：本 skill 是它们的"下游"——起草类 skill 出 Markdown 初稿后，本 skill 做 Word 套版
- 与 `ecm-design-*` 系列：本 skill 对 `ecm-design` 输出的法律备忘录（走 `legal-memo-format.md`）做 Word 套版
- 与 `docx` 外部 skill：本 skill 是"业务层"，`docx` 是"操作层"；本 skill 的 Word 操作都委托给 docx
- 与 `ecm-qc-*` 系列（QC 审查）：QC skill 输出的是带 tracked changes 的 Word 修订稿，**不经过本 skill**；QC 的修订痕迹是在**已套版**的 Word 上直接做

## 参考资料索引

- [references/markdown-to-word-mapping.md](./references/markdown-to-word-mapping.md) —— Markdown 元素 → Word 样式的完整映射表（所有格式规范共用）
- [references/format-check-checklist.md](./references/format-check-checklist.md) —— 格式检查清单的具体条目（每类文档独立 checklist）
- [references/docx-skill-invocation-patterns.md](./references/docx-skill-invocation-patterns.md) —— 调用 docx 外部 skill 的典型模式（对段落属性、表格、页眉页脚、域代码等）

## 常见误用 / FAQ

1. **"能直接调整 PDF 吗？"**：不能。PDF 的格式难以可靠回填；请提供 Word 源文件。
2. **"律所有自己的 .dotx 模板，能用吗？"**：可以。用 `custom` 模式；本 skill 会优先使用律所模板的样式表 + 本仓库格式规范的章节结构（若冲突以律所模板的字体 / 字号为准，章节结构按规范）
3. **"能只改字体不改其他吗？"**：可以。在 Step 1 指定 `custom` 模式并手工传入"仅字体"参数
4. **"目录更新后字体不统一怎么办？"**：本 skill 生成的 TOC 自动继承目录样式；若仍不统一，可能是 Word 在插入 TOC 时按 Normal 样式；建议运行 `style-based` 模式以确保样式绑定
5. **"交叉引用占位符怎么写？"**：在 Markdown 中使用 `{{XREF: 第N部分.小节M}}`（推荐）或 `详见本报告"第N部分"`（后者本 skill 无法自动替换为域代码，但保留文本）
6. **"表格跨页了怎么办？"**：本 skill 对所有表格应用"跨页时自动重复表头行"样式；若仍出问题，可能是单行高度超过一页（一般是超长单元格）；手工拆分内容
7. **"输入 Markdown 的段落里用了 `**加粗**`，转换到 Word 后还加粗吗？"**：保留。本 skill 保留行内样式（加粗 / 斜体 / 下划线 / 代码）

## 变更规则

- 输出契约变动 → MAJOR
- 新增配置项 / 支持新格式规范 → MINOR
- Markdown → Word 映射表的样式参数调整（跟随 shared/templates 下格式规范的 PATCH 更新） → PATCH
