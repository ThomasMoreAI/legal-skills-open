---
name: stakeholder-summary-zekaisuni
title: İş Birimi Özet Raporu
description: Convert a legal review into a short, sanitized, business-readable summary for Turkish commercial practice. Use when the user asks to explain a contract review to procurement, sales, finance, product, management, or another non-legal stakeholder.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/stakeholder-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: commercial
language: tr
---

# İş Birimi Özet Raporu

Bu skill tamamlanmış bir incelemeyi hukukçu olmayan paydaşın okuyacağı kısa bir aksiyon özetine çevirir. Hukuki mütalaa üretmez; ne yapılması gerektiğini sadeleştirir.

## Matter Context

If matter workspaces are enabled, load active matter and write output there.

## Destination Check

Ask where the summary will go if destination is not obvious:

- legal only,
- procurement / sales / finance / product,
- management,
- counterparty,
- broad internal channel.

If outside legal/confidential circle, prepare a sanitized version. Do not include privileged strategy, internal legal debate, or unnecessary personal data.

## Purpose

Answer:

- Can we sign?
- What are the top risks?
- What needs business input?
- Who needs to approve?
- What is the deadline?

## Audience Calibration

Calibrate language:

- Procurement: price, renewal, vendor leverage, operational obligations.
- Sales: deal blockers, customer-facing asks, fallback language.
- Finance: TL value, payment, FX, price escalation, budget risk.
- Product/IT: data, security, SLA, integration, exit.
- Management: decision, risk ownership, approval path.

## Format

Keep it short. Default max: one page.

```markdown
# İş Birimi Özeti: [Counterparty] - [Agreement]

## Karar Cümlesi
[İmzalanabilir / şu değişikliklerle imzalanabilir / hukuk onayı olmadan ilerlemeyin]

## Bilmeniz Gereken 3 Konu
1. **[Issue]** - [why it matters to business]
2. **[Issue]** - [why it matters]
3. **[Issue]** - [why it matters]

## Sizden Beklenen Karar
| Konu | Seçenek | Öneri | Son tarih |
|---|---|---|---|
| [issue] | [options] | [recommendation] | [date] |

## Hukuk Ekibinin Aksiyonu
[redline/escalation/approval]

## Paylaşım Notu
[legal-only or sanitized]
```

## Sanitization Rules

Remove or soften:

- litigation strategy,
- legal merits debate,
- attorney mental impressions,
- confidential settlement posture,
- unnecessary personal data,
- counterparty-sensitive internal thresholds.

Keep:

- decision,
- risk owner,
- deadline,
- required approval,
- business action.

## What this skill does not do

- It does not replace the full legal review.
- It does not create a counterparty-facing position unless explicitly requested and attorney-reviewed.
- It does not hide material legal risk to make the summary easier to read.
- It does not approve the agreement.
