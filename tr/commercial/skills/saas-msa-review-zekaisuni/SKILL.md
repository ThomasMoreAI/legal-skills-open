---
name: saas-msa-review-zekaisuni
title: SaaS / Abonelik Sözleşmesi İncelemesi
description: 'Reference: review SaaS and subscription agreements with a Turkish-law layer for auto-renewal, price escalation, exit/data portability, SLA, KVKK, subprocessors, AI/data-use rights, and renewal-tracker handoff. Loaded by /commercial-legal:review when SaaS or subscription terms are detected.'
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/saas-msa-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: commercial
language: tr
---

# SaaS / Abonelik Sözleşmesi İncelemesi

SaaS ve abonelik sözleşmeleri maliyet, yenileme, veri, çıkış ve hizmet sürekliliği risklerini biriktirir. Bu skill genel commercial playbook'u uygular ve üzerine SaaS'a özgü Türk hukuk/pratik kontrollerini ekler.

## Matter Context

Use commercial matter workspace rules. If active matter exists, load it and write outputs there.

## Purpose

Review SaaS terms under the team's playbook and Turkish practice. Focus on:

- automatic renewal and notice,
- price escalation and FX,
- data portability / exit,
- SLA / uptime,
- KVKK and subprocessors,
- AI or machine-learning rights,
- liability, indemnity, IP, security, audit, and termination.

## Governing Law Assumption

Apply the profile's governing-law posture. If the contract selects foreign law or foreign courts/arbitration, flag that Turkish-law analysis may not transfer and route to attorney review if outside playbook.

## Load Playbook

Read `commercial-legal/CLAUDE.md`:

- general purchasing-side or sales-side playbook,
- SaaS positions,
- KVKK posture,
- renewal preferences,
- escalation matrix.

If SaaS positions are missing, ask and record position before issuing a clean result.

## SaaS-Specific Review Layer

### 1. Automatic Renewal

Extract:

- initial term,
- current term,
- renewal mechanism,
- notice period,
- notice method,
- renewal price,
- non-renewal consequences.

If a date can be tracked, create a `renewal-tracker` handoff:

```yaml
renewal_handoff:
  counterparty:
  agreement:
  current_term_end:
  notice_period_days:
  notice_method:
  price_on_renewal:
  annual_value:
  currency: TL
  notes:
```

### 2. Price Escalation

Check unilateral price change, then-current list price, CPI/PPI/TÜFE/ÜFE, FX indexation, caps, notice, and termination right if price increases.

### 3. Data Portability and Exit

Check:

- export format,
- assistance period,
- deletion certificate,
- transition support,
- fees for export,
- API or backup access,
- vendor lock-in.

### 4. SLA and Service Credits

Check uptime percentage, exclusions, maintenance, remedy exclusivity, service credits, termination rights after repeated outages, and audit/log access.

### 5. KVKK and Subprocessors

Determine roles:

```yaml
kvkk:
  role: veri_sorumlusu | veri_isleyen | ortak_sorumluluk | belirsiz
  personal_data: true | false | belirsiz
  special_category_data: true | false | belirsiz
  sub_processors: listed | approval_required | notice_only | belirsiz
  cross_border_transfer: true | false | belirsiz
  transfer_mechanism: yeterlilik | uygun_guvence | standart_sozlesme | bcr | taahhutname | arizi_istisna | acik_riza | belirsiz
```

### 6. AI / ML Rights

Flag if vendor may use customer data, usage data, prompts, outputs, documents, logs, or metadata for training, analytics, benchmarking, or product improvement. If unclear, classify at least YELLOW.

### 7. Security and Breach

Check incident notice timing, audit rights, security standards, subcontracting, logs, access controls, data location, and deletion.

## Output

Prepend work-product header.

```markdown
# SaaS / Abonelik Sözleşmesi İncelemesi: [Counterparty]

## Sonuç
[GREEN / YELLOW / RED or equivalent playbook status]

## En Önemli Riskler
1. [risk]

## SaaS Kontrol Katmanı
| Konu | Durum | Not |
|---|---|---|
| Yenileme | [pass/flag] | [notice date/handoff] |
| Fiyat artışı | [pass/flag] | [cap/uncapped] |
| KVKK | [pass/flag] | [role/transfer] |
| SLA | [pass/flag] | [uptime/remedy] |
| Exit | [pass/flag] | [data export] |

## Önerilen Revizyonlar
[smallest workable edits]

## Renewal Handoff
[if applicable]

## Sonraki Adımlar
[legal / business owner / renewal tracker]
```

## What this skill does not do

- It does not operate the SaaS system or verify technical claims.
- It does not complete a full cybersecurity audit.
- It does not replace a KVKK DPA review where personal data processing is material.
- It does not decide whether to renew or cancel; it hands dates to `renewal-tracker`.
