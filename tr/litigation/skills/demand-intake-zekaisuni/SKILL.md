---
name: demand-intake-zekaisuni
title: /demand-intake
description: Intake for a Turkish ihtarname / demand-letter workflow. Collects parties, facts, legal basis, requested action, evidence, posture, deadline, notice method, mediation/settlement context, and risk gates before drafting.
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/litigation-legal/skills/demand-intake
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: litigation
language: tr
---

# /demand-intake

İhtarname taslaklamadan önce yapılandırılmış hazırlık dosyası oluşturur. Çıktı `demand-draft` tarafından okunacak `intake.md` dosyasıdır.

## Instructions

1. Load `~/.claude/plugins/config/claude-for-legal/litigation-legal/CLAUDE.md`.
2. Run adaptive intake: always ask the core questions; ask strategic block if `--full` or the matter is significant.
3. Create a slug from title, counterparty, and date.
4. Write `~/.claude/plugins/config/claude-for-legal/litigation-legal/demand-letters/[slug]/intake.md`.
5. Confirm:

   > Hazırlık kaydedildi. Hazır olduğunuzda `/litigation-legal:demand-draft [slug]` komutunu çalıştırın.

## Core Questions

Ask:

1. Kim adına ihtar gönderilecek? (müvekkil / şirket / kişi)
2. Muhatap kim?
3. İlişki nedir? (sözleşme, ticari ilişki, iş ilişkisi, IP, alacak, kira, diğer)
4. Tetikleyici olay nedir?
5. Talep nedir? (ödeme, aykırılığın giderilmesi, fesih, tecavüzün durdurulması, bilgi/belge, diğer)
6. Verilecek süre nedir?
7. Hangi deliller var?
8. Daha önce yazışma, arabuluculuk veya sulh görüşmesi yapıldı mı?

## Posture First

Ask before strategy:

> Bu ihtarnamedeki duruş ne olmalı: mücadele, uzlaşma, soruşturma/inceleme, bekle-gör, yoksa yalnızca hak saklama?

Record:

```yaml
posture: mücadele | uzlaşma | soruşturma | bekle | hak_saklama
```

## Strategic Block

If important or `--full`, ask:

- Bu ihtar dava veya icra öncesi son adım mı?
- İkrar, ibra, feragat veya zamanaşımı riski var mı?
- Arabuluculuk süreci var mı veya gerekir mi?
- Sulh görüşmeleri gizliliği var mı?
- Muhatap tacir mi? TTK m.18/3 bildirim şekli kontrol edilmeli mi?
- Gönderim yöntemi: noter, KEP, iadeli taahhütlü, e-posta, portal?
- Hangi sonucu almaya çalışıyoruz?
- Karşı tarafın muhtemel cevabı ne?

## Intake Template

```markdown
[AVUKAT ÇALIŞMA ÜRÜNÜ - TASLAK]

# İhtarname Ön Hazırlık: [Title]

**Slug:** [slug]
**Tarih:** [YYYY-MM-DD]
**Duruş:** [posture]

## Taraflar

**İhtar eden:** [name]
**Muhatap:** [name]
**Vekalet / temsil:** [status]

## Vakıa ve Tetikleyici Olay

[facts with sources]

## Hukuki Dayanak

[contract/statute/general basis; mark verify where needed]

## Talep ve Süre

[requested action and deadline]

## Deliller

- [source]

## Gönderim Yöntemi

[noter / KEP / iadeli taahhütlü / e-posta / other]

## Risk Kapıları

- İkrar riski:
- İbra / feragat riski:
- Zamanaşımı / hak düşürücü süre:
- Arabuluculuk / sulh görüşmeleri:
- Mesleki sır:

## Taslaklama Notları

[tone, constraints, open questions]
```

## What this skill does not do

- It does not draft the final ihtarname.
- It does not send anything.
- It does not decide whether the notice should be sent.
- It does not calculate final deadlines without verified trigger dates.
