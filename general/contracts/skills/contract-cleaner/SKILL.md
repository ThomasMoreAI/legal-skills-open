---
name: contract-cleaner
title: Contract Cleaner
description: 清洗合同、整理合同格式、统一合同术语、规范合同条款。当用户需要 整理、格式化、统一术语、清洗合同文本时使用。 触发词：清洗合同、整理合同、合同格式化、合同术语、合同规范化、 合同文本清洗、修复合同。
author: MarvinLann
author_url: https://github.com/MarvinLann/contract-cleaner
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: zh
---

# Contract Cleaner

将混乱的合同文本变成干净、规范、符合法律语言体系的 Markdown。

##  CRITICAL：完整流程必须全部执行

本工具的清洗流程包含 Python 步骤和 AI 步骤，**必须按顺序全部执行**，不能只跑 Python 命令就结束。缺少任何一步都会导致输出未经清洗。

完整流程：

```
1. Python preprocess   → 生成会话目录 + 编号规范化输入文件
2. AI 编号规范化       → 读取 numbering.md，只改编号不改内容，写入 02 文件
3. Python preprocess-continue → 加载 02 文件，分块
4. AI 五遍清洗         → 逐块执行：义务句式 → 结构重组 → 格式清理 → 质量验证 → 最终润色
5. Python finalize     → 拼接 + 自检 + 导出 docx
```

**禁止跳过步骤 2 和步骤 4**。步骤 2 是编号规范化的核心，步骤 4 包含义务句式、结构重组、格式清理、质量验证、最终润色共 5 个 pass，跳过任何 pass 都会导致输出质量不达标。

---

## 执行流程

### 第 1 步：预处理

```bash
python scripts/auto_cleaner.py --stage preprocess -i <合同文件>
```

此命令会完成文档转换、格式清洗、规则引擎，输出到 `清洗会话_<合同名>_<时间戳>/` 目录。

关键输出文件：
- `_原始轻量.md` — 原合同轻量清理版（仅清理 docx 转换噪音，用于 pandiff 对比基线）
- `00_规则引擎输出.md` — 规则引擎处理后的文本
- `01_编号规范化输入.md` — 待编号规范化的文本

### 第 2 步：AI 编号规范化（CRITICAL，不可跳过）

**此步骤由你（Agent）直接执行，不需要调用任何外部 API。**

1. 读取 `references/prompts/numbering.md` 获取编号规范化规则
2. 读取会话目录中的 `01_编号规范化输入.md`
3. 按规则处理文本，统一编号为标准层级：
   - 一级：**第一条**、**第二条**……（加粗）
   - 二级：1.1、1.2……
   - 三级：（1）、（2）……
4. **只改编号，不改任何文字内容**
5. 将结果写入会话目录中的 `02_编号规范化输出.md`

> 💡 `_原始轻量.md` 在 preprocess 阶段已自动生成，不需要你处理。finalize 阶段会优先用它作为 pandiff 的"原合同"对比基线。

### 第 3 步：预处理继续

```bash
python scripts/auto_cleaner.py --stage preprocess-continue --session <会话目录名>
```

此命令会加载 `02_编号规范化输出.md`，执行分块，输出 chunks 目录和 `manifest.json`。

### 第 4 步：AI 五遍清洗（CRITICAL，不可跳过）

**此步骤由你（Agent）直接执行，不需要调用任何外部 API。**

读取 `manifest.json`，对 `needs_ai: true` 的每个 chunk，按顺序执行 5 个 pass：

**Pass 1 — 义务句式**：
1. 读取 `references/prompts/obligation.md`
2. 读取 chunk 文件内容
3. 按 obligation.md 的要求处理文本（为义务性条款添加"应当"等）
4. 将结果写回原 chunk 文件

**Pass 2 — 结构重组**：
1. 读取 `references/prompts/structure.md`
2. 读取 chunk 文件内容
3. 按 structure.md 的要求处理文本（删除非标小标题、确认层级等）
4. 将结果写回原 chunk 文件

**Pass 3 — 格式清理**：
1. 读取 `references/prompts/format.md`
2. 读取 chunk 文件内容
3. 按 format.md 的要求处理文本（清理残留标记、统一格式等）
4. 将结果写回原 chunk 文件

**Pass 4 — 质量验证（不可跳过）**：
1. 读取 `references/prompts/verification.md`
2. 读取 chunk 文件内容
3. 按 verification.md 的语义检查清单逐条检查
4. 如果发现问题，根据 suggestions 直接修正后写回；如果无问题，原样写回
5. **禁止只输出 JSON 而不修改文件**——发现问题必须直接修正，无问题则原样保留

**Pass 5 — 最终润色（不可跳过）**：
1. 读取 `references/prompts/polish.md`
2. 读取 chunk 文件内容
3. 按 polish.md 的润色规则修正语法错误、句法错误、低级错误和怪异表达
4. 将结果写回原 chunk 文件
5. **禁止跳过**——即使看起来"没问题"也要执行，润色规则会捕获人眼易漏的低级错误

**规则**：
- `needs_ai: false` 的 chunk（首部、签署区）保持原样，不处理
- 如果某个 chunk 内容简短，可以一次合并处理多个 pass，但每个 pass 的结果都要体现
- 每个 pass 处理完立即写回文件

### 第 5 步：收尾

```bash
python scripts/auto_cleaner.py --stage finalize --session <会话目录名>
```

此命令会拼接所有 chunk、自检验证、导出文件。输出到输入文件同目录：
- `合同名-原合同（预处理后）.md` — 原合同轻量清理后的 Markdown
- `合同名-新合同（预处理后）.md` — AI 清洗后的 Markdown
- `合同名-清洁版.docx` — 清洗后的美观 Word 文档
- `合同名-对比版.docx` — 新旧对比修订痕迹版（pandiff 生成）

---

## 清洗规范

### 第 1 步已执行的确定性规则（AI 不需要重复处理）

| 规则 | 示例 |
|------|------|
| 术语替换 | 缴纳→支付、罚款→违约金、权力→权利 |
| 金额格式 | ¥123,456→人民币123456.00元 |
| 日期格式 | 2026-2-23→2026年2月23日 |
| 全角→半角 | 有多条 |
| 近义术语标记 | 终止/解除同时出现→【近义术语待统一】 |
| 首部/签署区保护 | 不进入条款编号体系 |

### 第 2 步已执行的编号规范化（AI 不需要重复处理）

| 规则 | 示例 |
|------|------|
| 条款编号标准化 | "一、""1.""（一）"→ **第X条** |
| 二级编号统一 | 子项统一为 X.X 格式 |
| 三级编号统一 | 子子项统一为（X）格式 |
| 层级递进修复 | 一级→三级跳级修复为自然段落 |

详细规范见 `references/global_text_processing.md`。

---

## 文件结构

```
contract-cleaner/
├── SKILL.md
├── scripts/
│   ├── auto_cleaner.py            # 主入口（支持 --stage preprocess/preprocess-continue/finalize）
│   ├── rule_engine.py             # 规则引擎
│   ├── industrial_cleaner.py      # AI 清洗引擎（自动模式用）
│   ├── format_cleaner.py          # 格式清洗
│   ├── document_converter.py      # 文档转换
│   ├── self_verifier.py           # 自检验证
│   └── docx_exporter.py           # Word 导出
└── references/
    ├── global_text_processing.md  # 完整清洗规范
    ├── troubleshooting.md          # 故障排查
    └── prompts/                    # AI 清洗 prompt
        ├── numbering.md            # 第2步：编号规范化（只改编号不改内容）
        ├── obligation.md           # Pass 1：义务句式
        ├── structure.md            # Pass 2：结构重组
        ├── format.md               # Pass 3：格式清理
        ├── verification.md         # Pass 4：质量验证（不可跳过）
        └── polish.md               # Pass 5：最终润色（不可跳过）
```

---

## 自动模式（有 API Key 的高级用户）

如已配置 API Key，可一条命令跑完：

```bash
python scripts/auto_cleaner.py -i 合同.docx
```

效果等价于手动执行上述全部 5 步，但 AI 清洗由 Python 脚本直接调用 API 完成。

首次配置：
```bash
python scripts/auto_cleaner.py --config
```
或设置环境变量：
```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

---

## 常见问题

| 现象 | 原因 | 解决方案 |
|------|------|---------|
| 输出与输入几乎相同 | 跳过了第2步或第4步的 AI 清洗 | 确保完整执行全部5步 |
| 没有"第一条"编号 | 跳过了第2步编号规范化 | 执行编号规范化后重新 preprocess-continue |
| `manifest.json 不存在` | 未运行第1步或第3步 | 先执行 preprocess，再执行编号规范化+preprocess-continue |
| chunk 数量太多 | 长合同条款多 | 正常现象，每个 needs_ai=true 的 chunk 都需要单独清洗 |
| docx 未生成 | pandoc 未安装 | 执行 `brew install pandoc`，不影响 MD 输出 |
