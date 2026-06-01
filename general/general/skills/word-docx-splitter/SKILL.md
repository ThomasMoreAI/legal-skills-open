---
name: word-docx-splitter
title: Word Document Splitter & Merger
description: Split large Word documents (.docx) into smaller chunks and reassemble them. Use when working with large legal documents, contracts, or agreements that need to be processed in smaller pieces—particularly useful when AI tools struggle with document size limits. Supports splitting by heading style (e.g., "Heading 1") or text pattern (e.g., "ARTICLE"), and merging edited chunks back together.
author: diegosouzapw
author_url: https://github.com/diegosouzapw/awesome-omni-skill/tree/main/skills/tools/word-docx-splitter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Word Document Splitter & Merger

Split large .docx files into smaller documents by article/section, then reassemble after editing.

## Dependencies

```bash
pip install python-docx lxml --break-system-packages
```

## Quick Reference

| Task | Command |
|------|---------|
| List styles | `python scripts/docx_splitter.py doc.docx --list-styles` |
| Split by style | `python scripts/docx_splitter.py doc.docx --split-on "Heading 1"` |
| Split by pattern | `python scripts/docx_splitter.py doc.docx --pattern "ARTICLE"` |
| Merge chunks | `python scripts/docx_merger.py ./chunks/ -o merged.docx` |

## Splitting Documents

### Step 1: Identify Split Points

Always check available styles first:

```bash
python scripts/docx_splitter.py document.docx --list-styles
```

### Step 2: Split

**By heading style** (preferred for well-formatted documents):
```bash
python scripts/docx_splitter.py document.docx --split-on "Heading 1" --output-dir ./chunks
```

**By text pattern** (for inconsistent styling):
```bash
python scripts/docx_splitter.py document.docx --pattern "ARTICLE" --output-dir ./chunks
python scripts/docx_splitter.py document.docx --pattern "^SECTION \d+" --output-dir ./chunks
```

### Split Options

| Option | Description |
|--------|-------------|
| `--split-on`, `-s` | Style name (e.g., "Heading 1", "Heading 2") |
| `--pattern`, `-p` | Regex pattern (e.g., "ARTICLE", "^SECTION \d+") |
| `--output-dir`, `-o` | Output directory (default: `<input>_split/`) |
| `--no-header` | Exclude preamble content from each chunk |

### Output Structure

Files are numbered for proper ordering:
```
document_split/
├── 00_Preamble.docx          # Content before first split point
├── 01_ARTICLE_I.docx
├── 02_ARTICLE_II.docx
└── ...
```

## Merging Documents

Reassemble edited chunks:

```bash
python scripts/docx_merger.py ./chunks/ -o final_document.docx
```

**Merge specific files in order:**
```bash
python scripts/docx_merger.py file1.docx file2.docx file3.docx -o merged.docx
```

### Merge Options

| Option | Description |
|--------|-------------|
| `-o`, `--output` | Output path (required) |
| `--page-breaks` | Add page breaks between sections |
| `--include-duplicates` | Keep duplicate preamble content |

## Typical Workflow

```bash
# 1. Check document structure
python scripts/docx_splitter.py BigContract.docx --list-styles

# 2. Split by articles
python scripts/docx_splitter.py BigContract.docx --split-on "Heading 1" -o ./chunks

# 3. Edit individual chunks (with Harvey, Claude, or manually)

# 4. Reassemble
python scripts/docx_merger.py ./chunks/ -o BigContract_Final.docx
```

## Limitations

- **Cross-references**: Internal references preserved but not auto-updated if sections renumber
- **Tables**: Tables spanning split boundaries may break
- **Numbering**: Automatic numbering restarts per chunk
- **Track changes**: Preserved but may need reconciliation after merge

## Tips for Legal Documents

- Split at ARTICLE level for credit agreements and loan documents
- Use `--pattern` when heading styles are inconsistent (common in opposing counsel docs)
- For very large definition sections, re-split that chunk by "Heading 2"
- Review merged document at section boundaries for formatting issues
