---
name: demand-draft-zekaisuni
title: /demand-draft
description: Draft a Turkish ihtarname from a completed demand-intake file. Applies mesleki sır, admission/waiver, settlement confidentiality, deadline, notice-method, and attorney-review gates before producing a draft suitable for lawyer review and later docx generation.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/demand-draft
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: tr
---

# /demand-draft

Tamamlanmış `demand-intake` dosyasından ihtarname taslağı hazırlar. Göndermez; noter, KEP veya başka bir kanalla kullanılmadan önce avukat incelemesi gerekir.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/demand-letters/[slug]/intake.md`.
2. Load litigation `CLAUDE.md` for drafting style and examples.
3. If strategic fields are missing for an important matter, stop and ask for intake completion.
4. Run pre-draft gate unless `--skip-gate` is passed by a lawyer-role user.
5. Draft in chat for review.
6. If approved and tooling is available, create `draft-v[N].docx` in the demand-letter folder.
7. Create a post-send checklist.

## Pre-Draft Gate

Confirm:

- Mesleki sır and audience.
- İkrar risk.
- İbra / feragat risk.
- Zamanaşımı or hak düşürücü süre.
- Arabuluculuk or settlement confidentiality.
- Tone and factual accuracy.
- Notice method and proof of delivery.
- Authority to send.

Do not proceed if the user cannot confirm material facts.

## Turkish Ihtarname Structure

Use:

```markdown
İHTARNAME

İHTAR EDEN:
[name/address]

VEKİLİ:
[lawyer/firm if applicable]

MUHATAP:
[name/address]

KONU:
[one sentence]

AÇIKLAMALAR:
1. [facts]
2. [contract/legal basis]
3. [breach / event]

TALEP:
[specific demand and deadline]

AKSİ HALDE:
[rights reserved; legal remedies]

DELİLLER / EKLER:
[list]

TARİH:
[date]

İMZA:
[signatory]
```

For merchant-to-merchant termination/default notices, check TTK m.18/3 and the contract notice clause.

## Drafting Rules

- Use firm but accurate language.
- Do not overstate facts.
- Do not include unnecessary personal data.
- Preserve rights without making accidental waiver.
- Do not include settlement admissions unless intentionally approved.
- If asking for payment, state amount, currency, basis, account details only if provided.
- If giving a cure period, state exact date or "tebliğden itibaren [N] gün" and mark verification.

## Output

```markdown
[AVUKAT ÇALIŞMA ÜRÜNÜ - TASLAK]

# İhtarname Taslağı - [slug] - v[N]

[draft text]

---

## Taslak Notları
- [risk / verification / open issue]

## Gönderim Sonrası Takip Listesi
- [ ] Gönderim yöntemi doğrulandı.
- [ ] Tebliğ / teslim kaydı alındı.
- [ ] Cevap süresi takvime işlendi.
- [ ] Cevap gelmezse sonraki adım belirlendi.
```

## What this skill does not do

- It does not send the ihtarname.
- It does not notarize, e-sign, or file anything.
- It does not guarantee that the chosen notice method is legally sufficient without lawyer review.
- It does not create facts or claims not in intake.
