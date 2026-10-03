---
name: demand-received-zekaisuni
title: /demand-received
description: Analyze an incoming Turkish ihtarname or demand letter. Extracts parties, claims, deadlines, legal bases, portfolio matches, merits, response options, and next steps, with teblig/KEP/noter proof and attorney-review gates.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/demand-received
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: en
---

# /demand-received

Gelen ihtarnameyi tasnif eder, süre ve riskleri çıkarır, portföy kontrolü yapar, cevap seçenekleri sunar ve gerekiyorsa yeni dosya veya karşı ihtar akışına yönlendirir.

## Instructions

1. Read the provided incoming document.
2. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/matters/_log.yaml` if available for portfolio check.
3. Load `litigation-legal/CLAUDE.md` for risk calibration and style.
4. Extract data, deadlines, allegations, legal bases, and requested action.
5. Save analysis to `~/.claude/plugins/config/claude-for-legal/litigation-legal/inbound/[slug]/analysis.md` if writing is appropriate.
6. Route based on user choice: open matter, draft response, prepare intake, or monitor.

## Workflow

### Step 1 - Read the Notice

Extract:

- sender and recipient,
- representatives,
- date on document,
- tebliğ / delivery / KEP timestamp,
- subject,
- alleged facts,
- legal basis,
- requested action,
- deadline,
- attachments,
- notice method.

If delivery date is missing:

> Tebliğ veya teslim tarihi doğrulanmadan kesin son gün hesaplanamaz.

### Step 2 - Portfolio Check

Search for related:

- same counterparty,
- same contract,
- same IP/brand/product,
- same employment/personnel issue,
- same invoice/payment,
- same court/UYAP file.

### Step 3 - Merits Assessment

Classify:

- strong,
- mixed,
- weak,
- insufficient information.

Explain evidence and legal basis separately. Do not dismiss a claim solely because tone is aggressive.

### Step 4 - Response Options

Options may include:

- substantive response / objection,
- counter-notice,
- cure / payment / performance,
- negotiation / settlement,
- request documents,
- open matter and investigate,
- no response / monitor, only if legally acceptable.

### Step 5 - Deadline Calendar

Record:

```yaml
deadline:
  trigger_date:
  source: noter | kep | posta | e-posta | other | unknown
  response_deadline:
  confidence: high | medium | low
  note:
```

### Step 6 - Write Analysis

```markdown
[AVUKAT ÇALIŞMA ÜRÜNÜ - TASLAK]

# Gelen İhtarname Analizi: [Counterparty]

## İhtarın Özeti
[plain summary]

## Tarih ve Süreler
| Olay | Tarih | Kaynak | Güven |
|---|---|---|---|

## İddia Edilen Vakıalar ve Dayanaklar
[claims]

## Portföy Kontrolü
[matches or none]

## Esas Değerlendirmesi
[strong/mixed/weak/unknown with reasons]

## Cevap Seçenekleri
### Seçenek A - Esaslı Cevap
[pros/cons]
### Seçenek B - Karşı İhtar
[pros/cons]
### Seçenek C - Uzlaşma / Görüşme
[pros/cons]
### Seçenek D - İzleme
[only if safe]

## Önerilen Sonraki Adım
[recommendation]

## Eksik Bilgi
[items]
```

## What this skill does not do

- It does not send a response.
- It does not ignore a deadline because delivery date is unclear.
- It does not make final merits determinations without evidence and attorney review.
- It does not open a new matter without user confirmation.
