---
name: forma-cn
title: FormaCN — 中文公文格式化工貝
description: Chinese legal document formatter. Formats .docx contracts, agreements, and official documents per GB/T 9704—2012 (Chinese government document standard). Use this skill whenever the user asks to format, typeset, or standardize Chinese Word documents (.docx) — contracts, privacy policies, service agreements, EULAs, attachments, or any legal/official doc — especially when they mention 公文格式, 排版, 标准格式, or GB/T 9704. Also use when the user has raw .docx legal files that look unstyled or inconsistently formatted and need a professional, standardized layout.
author: ethanl-dev
author_url: https://github.com/ethanl-dev/forma-cn
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: zh
---

# FormaCN — 中文公文格式化工貝

Applies GB/T 9704—2012 formatting to `.docx` files. Preserves all tracked
changes (修订), comments (批注), and text content — only the visual formatting
changes.

## Quick start

```bash
cd ~/.claude/skills/forma-cn
pip install python-docx
python -m forma_cn.cli 文件1.docx 文件2.docx
```

Or as a Python API:

```python
from forma_cn.formatter import FormatEngine

engine = FormatEngine("文件.docx")
engine.run()
engine.save("文件_格式化.docx")
```

## Formatting applied

| Element | Standard |
|---------|----------|
| Paper | A4 (210×297 mm) |
| Margins | Top 3.7 / Bottom 3.5 / Left 2.8 / Right 2.6 cm |
| Title | 方正小标宋简体 22pt (二号), centered |
| Section headings | 黑体 16pt (三号), bold, left-aligned |
| Body text | 仿宋 16pt (三号), first-line indent 2 chars |
| Line spacing | Fixed 28pt |
| Bullet items | Hanging indent (no first-line indent) |
| Latin text | Times New Roman |

## Bundled resources

- `forma_cn/` — Python package (pure, no deps beyond `python-docx`)

## Notes

- Input files must be `.docx` (Word OpenXML format).
- Output is saved as `{原名}_格式化.docx` alongside the original.
- The script modifies formatting at both the paragraph level (indent, spacing,
  alignment) and run level (font face, size). It works at the lxml layer so
  tracked changes and comments are never touched.
