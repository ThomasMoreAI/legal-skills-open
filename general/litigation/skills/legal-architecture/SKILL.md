---
name: legal-architecture
title: Legal Diagram Skill
description: 生成专业的法律结构可视化图，输出为自包含 HTML 文件（内嵌 SVG，浅色主题，适合打印和嵌入文档）。适用场景：(1) 用户要求"画结构图""生成可视化""做流程图""法律图示"时；(2) 涉及诉讼推理结构（当事人→证据→事实→法律→判决）；(3) 合同关系图（甲乙方权利义务、履约节点、违约责任）；(4) 法规程序图（申请→审查→决定→救济）；(5) 证据链图、请求权基础分析图、法律体系层级图。Use when the user asks for litigation flow diagrams, contract relationship diagrams, legal reasoning structure diagrams, evidence chain diagrams, or any legal visualization.
author: zh-xx
author_url: https://github.com/zh-xx/legal-assistant-skills/tree/main/legal-architecture
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: zh
---

# Legal Diagram Skill

Create professional legal structure diagrams as self-contained HTML files with inline SVG. Designed for court document analysis, contract review, legal knowledge management, and client presentations. Output is light-themed and print-ready.

## Design System

### Color Palette

Use these semantic colors for legal component types:

| Component Type | Fill (rgba) | Stroke | Use Case |
|---|---|---|---|
| 当事人/主体 (Party) | `rgba(219,234,254,0.9)` | `#2563eb` (blue-600) | 原告、被告、甲方、乙方、第三人 |
| 事实/行为 (Fact) | `rgba(241,245,249,0.9)` | `#475569` (slate-600) | 侵权行为、违约事实、案件经过 |
| 证据 (Evidence) | `rgba(254,243,199,0.9)` | `#b45309` (amber-700) | 书证、物证、证人证言、鉴定意见 |
| 法律规范 (Law) | `rgba(209,250,229,0.9)` | `#047857` (emerald-700) | 法条、司法解释、行政法规 |
| 程序节点 (Procedure) | `rgba(237,233,254,0.9)` | `#6d28d9` (violet-700) | 立案、开庭、举证、质证、裁定 |
| 裁判/结论 (Judgment) | `rgba(254,226,226,0.9)` | `#b91c1c` (red-700) | 判决主文、责任认定、风险结论 |
| 争议焦点 (Issue) | `rgba(255,237,213,0.9)` | `#c2410c` (orange-700) | 争议焦点、待查明事实 |

### Typography

Use Inter for all text — clean, professional, print-friendly:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

Font sizes: 12px for primary labels, 10px for secondary, 9px for annotations, 8px for tiny labels.

### Visual Elements

**Background:** `#f8fafc` with subtle light grid:
```svg
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
  <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#f1f5f9" stroke-width="0.8"/>
</pattern>
```

**Component boxes:** Rounded rectangles (`rx="6"`) with 1.5px stroke.
Always draw an opaque white background rect FIRST to mask arrows behind boxes:
```svg
<rect x="X" y="Y" width="W" height="H" rx="6" fill="white"/>
<rect x="X" y="Y" width="W" height="H" rx="6" fill="rgba(219,234,254,0.9)" stroke="#2563eb" stroke-width="1.5"/>
```

**Arrows — standard flow:**
```svg
<marker id="arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
  <polygon points="0 0, 8 3, 0 6" fill="#94a3b8"/>
</marker>
<line x1="..." y1="..." x2="..." y2="..." stroke="#94a3b8" stroke-width="1.2" marker-end="url(#arr)"/>
```

**Arrows — judgment emphasis (red):**
```svg
<marker id="arr-red" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
  <polygon points="0 0, 8 3, 0 6" fill="#b91c1c"/>
</marker>
```

**Cross-layer or indirect logical connections:** Use dashed lines:
```svg
stroke-dasharray="4,3"
```

**Arrow z-order:** ALWAYS draw all arrows BEFORE component boxes in the SVG. SVG renders in document order, so arrows drawn first appear behind boxes drawn later.

### Layout Patterns

Choose the layout based on content type:

**1. 诉讼流程图 (Litigation Flow)** — top-to-bottom layered with group boxes

For: case analysis, judgment structure, evidence → fact → law → judgment chain.

**PREFERRED PATTERN — dashed group boxes + single vertical arrows:**

Each reasoning stage is enclosed in a dashed group box with a badge label straddling its top-left border. Stages connect via a single purely vertical arrow in the center (x=500 for a 1000-wide viewBox). No node-to-node arrows across stages — this avoids visual clutter and false logical implications.

```
┌─────────────────────────────────┐
│ [当事人]  原告 ●●● 被告          │  ← group box, dashed border
└─────────────────────────────────┘
              ↓  (single arrow at center x)
┌─────────────────────────────────┐
│ [争议焦点] 焦点一  焦点二         │
└─────────────────────────────────┘
              ↓
  ... etc through 证据 → 事实认定 → 法律适用 → 判决结果
```

Group box SVG pattern (badge label straddles top-left border):
```svg
<!-- Group box -->
<rect x="8" y="127" width="984" height="82" rx="8"
      fill="rgba(255,237,213,0.12)" stroke="#fb923c"
      stroke-width="1.2" stroke-dasharray="6,4"/>
<!-- Badge: rect behind text, centered on top border (y = group top - 8) -->
<rect x="14" y="119" width="64" height="16" rx="4"
      fill="rgba(255,237,213,0.95)" stroke="#fb923c" stroke-width="0.8"/>
<text x="46" y="131" fill="#9a3412" font-size="9" font-weight="600"
      text-anchor="middle" font-family="Inter,system-ui">争议焦点</text>
```

Vertical gap between group boxes: 28–32px. Place one arrow per gap:
```svg
<line x1="500" y1="[group_bottom+2]" x2="500" y2="[next_group_top-2]"
      stroke="#64748b" stroke-width="1.5" marker-end="url(#arr)"/>
<!-- Final arrow to judgment box uses red: stroke="#b91c1c" stroke-width="2" marker-end="url(#arr-red)" -->
```

Within each group box, items are arranged horizontally (no intra-group arrows needed — spatial proximity implies relationship). Reserve arrows for cross-group logical flow only.

**2. 合同关系图 (Contract Relationship)** — hub-and-spoke or two-column
For: contract parties, rights/obligations flow, key clause mapping
```
甲方 ←→ 合同核心义务 ←→ 乙方
         ↓
    履约条件/违约责任
```

**3. 法律体系图 (Legal Framework)** — tree or hierarchical
For: legal concepts, regulatory hierarchy, claim basis analysis (请求权基础)
```
上位法 → 下位法 → 实施细则/司法解释
```

### Spacing Rules

**CRITICAL:** Avoid element overlaps:
- Standard component height: 55-60px for single-line, 75-90px for multi-line
- Minimum vertical gap between rows: 38px
- Minimum horizontal gap between same-row items: 15px
- Use equal start/end margins: startX = (viewBoxWidth - totalRowWidth) / 2

**Row width calculation:**
```
totalRowWidth = N * boxWidth + (N-1) * gap
startX = (viewBoxWidth - totalRowWidth) / 2
```

### Legend Placement

Place legend BELOW all diagram content, at least 20px below the lowest element. Use a light rounded-rectangle background. Arrange legend items horizontally.

### Page Structure

1. **Header** — title (with colored status dot), subtitle (case number / date / court)
2. **Diagram card** — white card with border-shadow, contains SVG
3. **Info cards** — 3-column grid with metadata (parties, evidence summary, judgment key points)
4. **Footer** — case number and skill attribution

## Output Format

Always produce a single self-contained `.html` file:
- Embedded CSS only (Google Fonts link allowed)
- Inline SVG (no external images or scripts)
- Light background (`#f8fafc`) — suitable for printing and embedding in Word/PPT
- No JavaScript required

File should open and render correctly in any modern browser, and look professional when printed.
