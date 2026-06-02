---
name: patent-digest
title: Patent Digest Skill
description: 专利文档智能解析与结构化摘要生成。支持提取基本信息、摘要、权利要求、创新点及技术方案，并输出标准化 Markdown 报告。适用于 OpenClaw、OpenCode、Hermes 等通用 Agent 。
author: TaohongMaxwell
author_url: https://github.com/TaohongMaxwell/PatentDigest/tree/main/skills/patent-digest
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: zh
---

# Patent Digest Skill

本 Skill 旨在帮助 Agent 对专利文档进行深度解析，提取关键信息并生成结构化的摘要报告。它完全继承了 Dify 工作流的处理逻辑，并通过**中间文件持久化**和**并行执行指南**优化了上下文效率与执行速度。

## 核心能力

- **多格式支持**：支持 PDF、DOCX、TXT 等常见格式（扫描版需配合 OCR 技能）。
- **结构化提取**：自动识别专利名称、申请号、申请日、摘要、权利要求书、说明书等。
- **深度分析**：提炼技术背景、现有技术不足、本发明解决的问题、有益效果及核心技术方案。
- **上下文优化**：采用“临时文件夹”策略，将中间结果写入本地文件，大幅降低 Token 消耗。
- **标准化输出**：最终生成格式统一的 Markdown 报告。

## 执行模式与并行策略

本 Skill 支持两种执行模式，Agent 可根据自身能力选择：

### 1. 串行模式（默认，适合资源受限环境）
Agent 按顺序执行所有步骤。虽然速度较慢，但对内存和并发要求最低。

### 2. 并行模式（推荐，适合支持子 Agent/多线程的环境）
为了模拟 Dify 的高效并行处理，建议在执行**第二阶段（关键信息提取）**时，同时启动多个子任务或线程：
- **任务 A**：提取基本信息 (`01_basic_info.txt`)
- **任务 B**：提取原始摘要 (`02_abstract_extract.txt`)
- **任务 C**：提取权利要求书 (`04_claims_extract.txt`)
- **任务 D**：提取说明书 (`06_description_extract.txt`)

*注意：Skill 本身无法强制宿主启动子 Agent，但 Agent 若具备并行调度能力，应优先采用此模式以缩短总耗时。任一并行任务失败不影响其他任务继续执行，失败任务的输出文件写入"未提取到相关信息"即可。*

### 3. 多专利对比分析模式
当用户提供多个同一技术领域的专利文件时，请按以下步骤操作：
1. **独立解析**：为每个专利文件创建一个独立的临时文件夹（如 `tmp/patent_A/`, `tmp/patent_B/`），并分别执行上述第一至第四步，生成各自的 `report.md`。
2. **对比分析**：在所有报告生成后，调用一个额外的对比 Prompt（建议由 Agent 动态生成或使用 `prompts/11_comparison.txt` 如果存在），从技术方案、创新点、保护范围等维度进行横向对比。

## 使用方法：基于临时文件的流转

为了节省上下文并提高健壮性，本 Skill 采用**“读取 -> 提取存盘 -> 读盘总结 -> 合并”**的流程。

### 第一步：环境准备与预处理
1. **创建临时目录**：在 workspace 下创建 `tmp/patent_digest_<timestamp>/` 文件夹。
2. **全文转换与 OCR 检查**：
   - 将专利文档转换为纯文本。
   - **重要**：如果转换后的文本长度极短或包含大量乱码，说明可能是扫描版 PDF。此时应提示用户启用 OCR 技能（如 `pdf-document-handler`）或安装相关环境。
   - 将清洗后的全文存入 `tmp/full_text.txt`。

### 第二步：关键信息提取（并行阶段）
调用以下 Prompt，并将结果**写入**临时文件夹对应的 `.md` 或 `.txt` 文件中，而不是直接输出在对话框中：

| 步骤 | Prompt 模板 | 输入变量 | 输出格式 | 输出文件路径 | 对应 Dify 节点 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `01_basic_info.txt` | `{{patent_text}}` (读取 full_text.txt) | json_object | `tmp/basic_info.md` | 基本信息 |
| 2 | `02_abstract_extract.txt` | `{{patent_text}}` (读取 full_text.txt) | 纯文本 | `tmp/raw_abstract.txt` | 摘要提取 |
| 3 | `04_claims_extract.txt` | `{{patent_text}}` (读取 full_text.txt) | 纯文本 | `tmp/raw_claims.txt` | 权利要求提取 |
| 4 | `06_description_extract.txt` | `{{patent_text}}` (读取 full_text.txt) | 纯文本 | `tmp/description.txt` | 说明书提取 |

### 第三步：深度总结（串行/依赖阶段）
从临时文件中读取上一步的结果，进行处理并再次存盘：

| 步骤 | Prompt 模板 | 输入来源 | 输出格式 | 输出文件路径 | 对应 Dify 节点 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 5 | `03_abstract_summary.txt` | `{{raw_abstract}}` (读取 `tmp/raw_abstract.txt`) | 纯文本 | `tmp/abstract_summary.txt` | 摘要总结 |
| 6 | `05_claims_summary.txt` | `{{raw_claims}}` (读取 `tmp/raw_claims.txt`) | 纯文本 | `tmp/claims_summary.txt` | 权利要求总结 |
| 7 | `07_innovation_summary.txt` | `{{description}}` (读取 `tmp/description.txt`) | markdown | `tmp/innovation_summary.md` | 创新点总结 |
| 8 | `08_technical_solution.txt` | `{{description}}` (读取 `tmp/description.txt`) | 纯文本 | `tmp/technical_solution.txt` | 技术方案概括 |
| 9 | `09_keywords.txt` | `{{description}}` (读取 `tmp/description.txt`) | key-value 列表 | `tmp/keywords.txt` | 关键词提取 |

### 第四步：报告合并
调用 `prompts/10_final_merge.txt`。Agent 需从临时文件夹读取对应文件，填入以下占位符：

| 占位符 | 来源文件 |
| :--- | :--- |
| `{{basic_info}}` | `tmp/basic_info.md` |
| `{{abstract_summary}}` | `tmp/abstract_summary.txt` |
| `{{keywords}}` | `tmp/keywords.txt` |
| `{{claims_summary}}` | `tmp/claims_summary.txt` |
| `{{innovation_summary}}` | `tmp/innovation_summary.md` |
| `{{technical_solution}}` | `tmp/technical_solution.txt` |

填入后生成最终的 `report.md`。

## 文件结构

```
skills/patent-digest/
├── SKILL.md              # 本说明文件
└── prompts/
    ├── 01_basic_info.txt
    ├── 02_abstract_extract.txt
    ├── 03_abstract_summary.txt
    ├── 04_claims_extract.txt
    ├── 05_claims_summary.txt
    ├── 06_description_extract.txt
    ├── 07_innovation_summary.txt
    ├── 08_technical_solution.txt
    ├── 09_keywords.txt
    ├── 10_final_merge.txt
└── 11_comparison.txt    # 多专利对比分析模板（可选）
```

## 注意事项与扩展

- **OCR 引导**：若检测到文档为图片型 PDF，请明确告知用户：“检测到该专利可能为扫描版，建议启用 OCR 技能（如 pdf-document-handler）以获得最佳提取效果。”
- **模型建议**：推荐使用 Qwen2.5-7B-Instruct 及以上版本，或 DeepSeek-R1 等逻辑推理较强的模型。建议参数：temperature=0.3，top_p=0.8，max_tokens=4096；提取类任务（01/02/04/06）可设 temperature=0.1 以获得更稳定的输出。
- **容错处理**：若某一步骤提取失败（如找不到申请号），请在对应文件中写入“未提取到相关信息”，确保后续合并步骤不中断。
