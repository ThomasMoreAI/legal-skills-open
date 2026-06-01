---
name: mit-licensing
title: MIT License Compatibility Audit
description: Audit dependency licenses for MIT compatibility. Use when the user wants to check if their project's dependencies are compatible with MIT license, find problematic licenses (GPL, AGPL, etc.), or generate a license audit report. Supports Node.js (npm/pnpm) and Rust (Cargo) projects.
author: joe-re
author_url: https://github.com/joe-re/eyes-on-claude-code/tree/main/.claude/skills/mit-licensing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# MIT License Compatibility Audit

Check project dependencies for licenses incompatible with MIT.

## Workflow

### 1. Collect License Data

**Node.js (pnpm):**
```bash
pnpm licenses list --json
```

**Node.js (npm):**
```bash
npx license-checker --json
```

**Rust:**
```bash
cargo metadata --format-version 1
```

### 2. Identify Problematic Licenses

**Incompatible with MIT** (block release):
- GPL, GPLv2, GPLv3
- AGPL, AGPLv3
- SSPL, BUSL, CPAL, EUPL

**Requires investigation:**
- LGPL (may be acceptable depending on linking)
- `UNKNOWN`, `UNLICENSED`, `SEE LICENSE IN LICENSE`
- CC-BY-* (requires attribution)

**Generally compatible:**
- MIT, ISC, BSD-2-Clause, BSD-3-Clause
- Apache-2.0 (include NOTICE if present)
- MPL-2.0 (disclose modifications to MPL files)
- Unlicense, CC0-1.0, WTFPL

**Rust dual-licensing:**
- `MIT OR Apache-2.0` → Choose MIT, compatible
- `GPL OR MIT` → Choose MIT, compatible

### 3. Generate Report

Report format:

```markdown
# License Audit Report

## Summary
- Total packages: [count]
- Compatible: [count]
- Requires attention: [count]
- Incompatible: [count]

## Incompatible Licenses
| Package | License | Action Required |
|---------|---------|-----------------|
| [name]  | GPL-3.0 | Remove or find alternative |

## Requires Attention
| Package | License | Notes |
|---------|---------|-------|
| [name]  | UNKNOWN | Verify license manually |
| [name]  | CC-BY-4.0 | Add attribution |

## Compatible Licenses
[List of packages grouped by license type]
```
