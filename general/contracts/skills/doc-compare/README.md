# /doc-compare

Semantic comparison between two document versions with risk analysis.

## What It Does

- Compares two versions of a document (contracts, policies, specs, etc.)
- Goes beyond text diff — explains what changed and why it matters
- Aligns sections even when headings or structure changed between versions
- Flags high-risk changes automatically (liability, payment terms, termination clauses)
- Generates a structured comparison report with risk ratings

## Install

```bash
claude install doculent/community/skills/doc-compare
```

### Dependencies

- `poppler-utils` — for PDF processing
- `tesseract` — for scanned document OCR (optional)

```bash
# macOS
brew install poppler tesseract

# Ubuntu/Debian
apt install poppler-utils tesseract-ocr
```

## Usage

**Compare two contract versions:**
```
/doc-compare ./contract-v1.pdf ./contract-v2.pdf
```

**Focus on specific sections:**
```
/doc-compare ./policy-old.pdf ./policy-new.pdf --focus "payment terms, liability"
```

**Output as JSON:**
```
/doc-compare ./spec-v1.md ./spec-v2.md --format json
```

## Example Output

```markdown
# Document Comparison Report

**Document A:** contract-v1.pdf (12 pages, dated 2025-08-15)
**Document B:** contract-v2.pdf (14 pages, dated 2026-03-20)

## Summary

- 4 sections modified, 1 section added, 1 section removed
- 2 high-risk changes identified

## High-Risk Changes

### Section 9 — Liability Cap
- **Change:** Removed entirely (was $500,000 cap in v1)
- **Risk:** HIGH — unlimited liability exposure

### Section 5.4 — Intellectual Property (NEW)
- **Change:** New source code escrow requirement added
- **Risk:** HIGH — new obligation with third-party dependency

## All Changes

### Section 3.2 — Payment Terms (Modified)
| Aspect | Before | After |
|--------|--------|-------|
| Payment window | Net-30 | Net-60 |
| Late fee | 1.5% | 2.5% |
| Early payment discount | 2% / 10 days | Removed |
```

## Risk Detection

The skill automatically flags these change patterns:

| Pattern | Risk Level |
|---------|-----------|
| Liability cap removed or increased | High |
| Termination clause modified | High |
| Indemnification expanded | High |
| Non-compete added or expanded | High |
| Payment terms extended | Medium |
| Auto-renewal added | Medium |
| Governing law changed | Medium |
| New obligations added | Medium |

## License

MIT — see [LICENSE](../../LICENSE).
