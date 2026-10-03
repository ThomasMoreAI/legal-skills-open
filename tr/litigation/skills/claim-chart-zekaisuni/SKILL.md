---
name: claim-chart-zekaisuni
title: /claim-chart
description: Build or review an element chart. In patent matters, maps patent claim elements to accused products, invalidity references, or evidence. In Turkish civil litigation, maps legal elements of a claim or defense to evidence and proof gaps. Primary output is an evidence/proof-gap table.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/claim-chart
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: en
sources:
- title: Element templates
  path: references/element-templates.md
---

# /claim-chart

Türk hukukuna uyarlanmış unsur tablosu oluşturur. Patent modunda teknik istem unsurları; hukuk modunda dava veya savunma unsurları delillerle eşleştirilir.

## Instructions

1. Load `litigation-legal/CLAUDE.md`.
2. Load active matter if available.
3. Determine mode:
   - `--patent`: patent istem tablosu.
   - `--law`: hukuk davası unsur tablosu.
   - no flag: ask which mode.
4. Use sources provided by the user or matter file.
5. Build table with evidence, gaps, and confidence.
6. Mark every conclusion as draft, not final opinion.

## Safety Banner

Include:

> Bu tablo bir çalışma taslağıdır. Nihai hukuki kanaat, bilirkişi görüşü, teknik görüş veya mahkemeye sunulacak beyan değildir. Avukat ve gerekiyorsa teknik uzman incelemesine tabidir.

## Mode 1 - Patent Claim Chart

For each claim element:

- claim number,
- element text,
- accused product / method mapping or prior art mapping,
- evidence source,
- missing proof,
- technical uncertainty,
- legal note.

```markdown
| İstem | Unsur | Karşılık / Delil | Güven | Eksik |
|---|---|---|---|---|
| [n] | [element] | [source] | high/medium/low | [gap] |
```

Do not provide final infringement, invalidity, or FTO opinion.

## Mode 2 - Civil Litigation Element Chart

Map legal elements to evidence. Common templates:

- sözleşmeye aykırılık,
- haksız fiil,
- sebepsiz zenginleşme,
- ticari alacak,
- işçilik alacağı,
- marka/telif/haksız rekabet,
- ihtiyati tedbir,
- ihtiyati haciz.

For each element:

```markdown
| Unsur | Dayanak | Delil | İspat durumu | Karşı taraf savunması | Eksik |
|---|---|---|---|---|---|
| [element] | [law/case] | [source] | güçlü/orta/zayıf | [defense] | [gap] |
```

If element templates are configured in `references/element-templates.md`, use them. If not, ask the attorney to confirm elements before relying on the chart.

## CSV / Excel Safety

When exporting table data, neutralize formula injection in cells beginning with `=`, `+`, `-`, or `@`.

## Output

```markdown
# Unsur Tablosu - [Matter / Claim]

## Kısa Sonuç
[proof gaps and strongest evidence]

## Tablo
[table]

## İspat Boşlukları
- [gap]

## Doğrulama
- [legal authority or technical point to verify]
```

## What this skill does not do

- It does not give final infringement, invalidity, or merits opinions.
- It does not replace expert review.
- It does not invent legal elements, evidence, or claim constructions.
- It does not file the table.
