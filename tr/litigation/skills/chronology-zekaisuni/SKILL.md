---
name: chronology-zekaisuni
title: /chronology
description: Build or update a Turkish litigation chronology from declared sources and uploads. Extracts dated events, merges duplicates, tags importance under the matter theory, and flags missing evidence, KVKK/privacy concerns, and deadline risks.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/chronology
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: en
---

# /chronology

Belge ve kaynaklardan tarihli olayları çıkararak dava teorisine bağlı bir kronoloji oluşturur. Çıktı delil sadakati gerektirir; kaynaklanmayan olaylar kesin vakıa gibi yazılmaz.

## Instructions

1. Load litigation `CLAUDE.md`.
2. If matter slug or active matter exists, load `matter.md`, theory, known pleadings, and evidence index.
3. Identify sources in this order:
   - user-provided files,
   - active matter folder,
   - configured document sources,
   - UYAP/UETS/KEP records if available and relevant.
4. Extract dated events.
5. Merge duplicates.
6. Tag importance under the theory.
7. Output in requested format.

## Sources

Typical sources:

- dava dilekçesi,
- cevap dilekçesi,
- ihtarname,
- KEP/e-mail correspondence,
- contract and amendments,
- invoices and payments,
- meeting minutes,
- UYAP documents,
- expert reports,
- witness notes,
- official records.

## KVKK and Confidentiality

If personal data, special categories, health data, employee data, or third-party information appears, flag and minimize. Do not include unnecessary personal identifiers in broad outputs.

## Event Record

Each event should have:

```yaml
event:
  date:
  title:
  description:
  source:
  confidence: high | medium | low
  importance: critical | relevant | background
  theory_link:
  deadline_effect:
```

If date is approximate, say so.

## Formats

### Working Chronology

```markdown
# Kronoloji - [Matter]

## Zaman Çizelgesi
| Tarih | Olay | Kaynak | Güven | Önem |
|---|---|---|---|---|
| [date] | [event] | [source] | [high/medium/low] | [critical/relevant/background] |

## Kritik Vakıalar
[short discussion]

## Eksikler
- [missing source/date/fact]

## Deadline Notes
- [limitation, response, mediation, appeal, enforcement]
```

### Facts Format

Use when drafting facts section. Include only sourced, pleading-ready facts.

### Witness Format

Use for witness preparation. Do not invent testimony; list topics, documents to show, and questions to verify.

## Importance Tagging

- `critical`: outcome-changing under case theory.
- `relevant`: useful but not central.
- `background`: context only.

If the theory is missing, ask for it or produce neutral chronological output.

## What this skill does not do

- It does not decide admissibility.
- It does not create testimony.
- It does not file evidence.
- It does not calculate final limitation dates without verified trigger dates.
- It does not read other matters unless cross-matter access is allowed and requested.
