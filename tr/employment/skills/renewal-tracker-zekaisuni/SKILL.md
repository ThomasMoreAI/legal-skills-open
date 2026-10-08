---
name: renewal-tracker-zekaisuni
title: /renewal-tracker
description: Show contracts with non-renewal or termination-notice deadlines coming up and warn before notice windows close, using a maintained renewal register adapted for Turkish notice practice. Use when the user asks what's renewing soon, whether a cancellation window was missed, or when review skills hand off renewal data.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/renewal-tracker
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: en
---

# /renewal-tracker

Sözleşmelerin otomatik yenileme, dönem sonu ve fesih ihbar tarihlerini izler. Yenilemeye veya feshe karar vermez; karar verilmesi gereken tarihi ve güvenli gönderim penceresini görünür kılar.

## Instructions

1. Read `~/.claude/plugins/config/claude-for-legal/commercial-legal/renewal-register.yaml`.
2. Default mode: show the next 90 days, grouped by urgency using `send_by_effective`.
3. `--days N`: change the window.
4. `--missed`: show deadlines that passed without recorded cancellation.
5. If register is empty and CLM/archive is connected, offer a scan and bulk-load.
6. Recommended actions must include business owner, legal owner if configured, notice method, and pricing risk.

## Register Schema

Each entry should use Turkish-notice fields:

```yaml
- counterparty: "Acme Yazılım A.Ş."
  agreement: "Platform Abonelik Sözleşmesi"
  signed_date: 2025-06-15
  initial_term_end: 2026-06-15
  current_term_end: 2026-06-15
  renewal_mechanism: "otomatik yıllık yenileme"
  notice_period_days: 60
  notice_method: "kep"               # noter | kep | iadeli_taahhutlu_posta | e-posta | portal | per contract
  transit_buffer_days: 0
  cancel_by_calendar: 2026-04-16
  cancel_by_effective: 2026-04-16
  send_by_effective: 2026-04-16
  cancel_by_roll_note: ""
  cancel_by_provenance: "[model calculation - verify against notice clause]"
  price_on_renewal: "TÜFE/ÜFE or then-current list"
  annual_value: 48000
  currency: "TL"
  business_owner: "owner@example.com"
  clm_id:
  uyap_no: ""                         # only if litigation/enforcement linked
  status: "active"                    # active | cancelled | renewed | lapsed
  notes:
```

## Turkish Notice Method Check

For merchants, notices of default, termination, or withdrawal may require the forms listed in TTK m.18/3: noter, registered mail, telegram, or secure e-signature through KEP. Always read the contract's notice clause as well.

Do not assume ordinary email is sufficient unless the contract and risk posture support it. If email is used, flag proof and receipt risk.

## Date Calculation

Track three dates:

- `cancel_by_calendar`: raw arithmetic date.
- `cancel_by_effective`: last date notice must be effective, adjusted for contract wording and business-day risk.
- `send_by_effective`: date by which the notice should be sent, after transit buffer.

Use `send_by_effective` for urgency alerts. If Turkish holiday/weekend adjustment is uncertain, mark the calculation as provisional.

Important nuance: TBK m.93 may move a contractual performance deadline to the next business day when the last day is a holiday, unless otherwise agreed. For non-renewal notices, this tracker is intentionally risk-reducing: it should warn earlier rather than rely on a later interpretation. Explain the difference:

> Hukuki son gün hesabı ile risk azaltıcı gönderim tarihi farklı olabilir. Sözleşmedeki bildirim maddesi ve uygulanacak hukuk kontrol edilmeden kesin son tarih olarak kullanılmamalıdır.

## Modes

### Mode 1 - Ingest Renewal

When a review skill finds a renewal clause, append or update a register entry. If the counterparty already has an entry, ask whether this is a replacement, amendment, or additional agreement.

### Mode 2 - Upcoming Renewals

Urgency bands use days until `send_by_effective`:

- KIRMIZI: 0-13 days
- TURUNCU: 14-44 days
- SARI: 45-89 days

Each deadline belongs to one band only.

```markdown
## Yenileme ve Fesih İhbar Takvimi - Önümüzdeki [N] Gün

### KIRMIZI - 0-13 Gün
| Karşı taraf | En geç gönderim | Dönem sonu | Yıllık değer | Sahibi | Bildirim | Not |
|---|---|---|---|---|---|---|
| [name] | **[date]** | [date] | [TL] | [owner] | [method] | [notes] |

### TURUNCU - 14-44 Gün
[same table]

### SARI - 45-89 Gün
[same table]

## Önerilen Aksiyonlar
- [ ] [Counterparty] - [business owner]'a sor: devam etmek istiyor muyuz?
- [ ] [Counterparty] - fiyat artışı sınırsız; pazarlık için pencere kapanmadan alternatif teklif al.
```

### Mode 3 - Scan CLM / Archive

If connected, search active agreements for renewal, auto-renew, subscription, term, notice, fesih, ihbar, süreli, müddetli, yenileme. Add draft records and mark uncertain entries for manual review.

### Mode 4 - Missed Windows

Show agreements where `send_by_effective` or `cancel_by_effective` passed and no cancellation is recorded.

```markdown
## Kaçırılmış Fesih / Yenilememe Pencereleri

| Karşı taraf | Son gönderim tarihi | Dönem sonu | Durum |
|---|---|---|---|
| [name] | [date] | [date] | Otomatik yenilenmiş olabilir |

## Seçenekler
- Geç fesih veya karşılıklı sonlandırma pazarlığı.
- Yenilemeyi kabul edip sonraki dönemin tarihlerini şimdiden kaydetmek.
- Sözleşmede başka fesih hakları olup olmadığını incelemek.
```

## Gate: Acting on Renewal

Tracking is research. Sending a non-renewal notice, allowing renewal, or countersigning a renewal has legal consequences. If the user is non-lawyer, ask:

> Bu işlem sözleşmeyi sona erdirebilir veya şirketi yeni bir dönem için borç altına sokabilir. Şirket avukatı veya yetkili hukukçu ile görüştünüz mü?

Do not draft/send a notice as if authorized unless explicitly confirmed and within role.

## What this skill does not do

- It does not cancel contracts.
- It does not decide whether to renew.
- It does not send notices.
- It does not produce a final legal deadline without reviewing the notice clause.
- It does not calculate tax, accounting, or budget effects beyond surfacing the issue.
