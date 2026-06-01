---
name: vendor-agreement-review-zekaisuni
title: Tedarikçi Sözleşmesi İncelemesi
description: 'Reference: review an inbound vendor, services, MSA, or commercial agreement against the Turkish-law adapted commercial playbook. Flags deviations, drafts surgical redlines, and routes approvals without making final legal decisions. Loaded by /commercial-legal:review when a vendor agreement is detected.'
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/commercial-legal/skills/vendor-agreement-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: commercial
language: tr
---

# Tedarikçi Sözleşmesi İncelemesi

Bu skill bir tedarikçi, hizmet, MSA veya benzeri ticari sözleşmeyi `CLAUDE.md` içindeki playbook'a göre inceler. Sonuç, avukat incelemesine tabi taslaktır.

## Matter Context and Destination Check

Use commercial matter workspace rules. Before output, check destination and offer legal-only or sanitized versions if sharing outside the legal/confidential circle.

## Purpose

Read the agreement, compare each material term against the team's playbook, identify deviations, draft precise redlines where appropriate, and route approvals under the escalation matrix.

## Load Playbook

Read:

- `## Playbook` -> side-specific positions,
- `## Escalation`,
- `## Outputs`,
- matter overrides if active.

If playbook is not configured, use provisional mode only with clear warning:

> Playbook eksik. Varsayılan Türk hukuku kontrol listesine göre ön bulgu çıkarabilirim; ancak GREEN veya imza önerisi veremem.

## Workflow

### Step 1 - Orientation

Extract:

- parties and roles,
- agreement type,
- contract value and currency/TL equivalent,
- term and renewal,
- governing law, venue, arbitration,
- signature authority,
- data/KVKK involvement,
- key business context,
- linked matter or UYAP if any.

### Step 2 - Deal-Breaker Check

Check Turkish-practice red flags:

- uncapped liability,
- tek taraflı veya fahiş cezai şart (TBK m.179-185),
- broad indemnity or guarantee,
- IP assignment / FSEK rights transfer,
- KVKK cross-border transfer without approved mechanism,
- broad audit or data access obligations,
- foreign governing law or forum outside playbook,
- unclear arbitration institution/seat/language,
- exclusivity, non-compete, non-solicit,
- indefinite unilateral price increase,
- automatic renewal without practical notice,
- surety, parent guarantee, letter of guarantee,
- public procurement or regulated-sector issue if applicable.
- damga vergisi (488 sayılı DVK) veya vergi/muhasebe incelemesi gerektirebilecek imza, tadil, teminat, kefalet, sulh veya devir yapısı.

### Step 3 - Clause-by-Clause Review

For each issue:

- quote short relevant language,
- state playbook position,
- explain Turkish-law/practice risk,
- propose narrow redline or escalation,
- identify approver if needed.

### Step 4 - Approval Routing

If issue exceeds authority, call escalation logic:

```yaml
escalation:
  issue:
  approver:
  reason:
  deadline:
```

### Step 5 - Renewal Handoff

If renewal or notice dates are found, create `renewal-tracker` handoff.

## Output

```markdown
# Tedarikçi Sözleşmesi İncelemesi: [Counterparty] - [Agreement type]

## Yönetici Özeti
[Bottom line: signable / negotiate / stop / incomplete]

## Kırmızı Çizgi Kontrolü
| Konu | Durum | Not |
|---|---|---|
| Sorumluluk | [pass/flag] | [summary] |

## Önem Derecesine Göre Bulgular

### [Severity] - [Issue] - Madde [X]
> "[short quote]"

**Risk:** [plain Turkish]
**Playbook:** [reference]
**Önerilen revizyon:** "[surgical language]"
**Onay:** [none / approver]

## Lehe Maddeler ve Eksik Hükümler
[favorable terms and missing protective terms]

## KVKK / Rekabet / Yenileme Notları
[as applicable]

## Sonraki Adımlar
[action list]
```

## Redline Rules

Prefer small edits. Do not rewrite the agreement. If a clause needs a full rewrite, state that attorney drafting is needed.

## What this skill does not do

- It does not approve signature.
- It does not send redlines.
- It does not decide business risk where the playbook requires approver judgment.
- It does not provide final foreign-law advice.
- It does not replace specialist DPA, tax, finance, or technical security review.
