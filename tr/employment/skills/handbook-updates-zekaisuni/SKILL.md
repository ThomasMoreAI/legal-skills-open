---
name: handbook-updates-zekaisuni
title: /handbook-updates
description: Personel yönetmeliği veya işyeri politikası değişikliklerini mevcut metinle karşılaştırır. Türk iş hukuku, KVKK, İSG, disiplin, fazla çalışma, izin, uzaktan çalışma, tebliğ ve çalışan aleyhine esaslı değişiklik risklerini işaretler.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/handbook-updates
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /handbook-updates

## Akış

1. Mevcut yönetmelik/politika metnini ve önerilen değişikliği oku.
2. Employment `CLAUDE.md` içindeki `## İşyeri Politikaları` bölümünü yükle.
3. Değişikliği sınıflandır: açıklayıcı, prosedürel, çalışan aleyhine esaslı değişiklik, KVKK/İSG etkili, disiplin etkili.
4. Tebliğ, onay, açık rıza/aydınlatma, TİS/sendika ve yürürlük tarihi gerekliliklerini işaretle.

## Çıktı

```markdown
GİZLİ HUKUKİ / İŞ HUKUKU ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

# Personel Yönetmeliği Değişiklik İncelemesi - [Konu]

**Değişiklik türü:** açıklayıcı / prosedürel / esaslı / KVKK / İSG / disiplin
**Risk:** yeşil / sarı / turuncu / kırmızı

## Farklar

| Mevcut | Yeni | Etki | Aksiyon |
|---|---|---|---|
| | | | |

## Tebliğ ve Yürürlük

- [çalışanlara duyuru/onay/aydınlatma ihtiyacı]

## Revizyon Önerisi

- [metin]
```

## Bu Skill Ne Yapmaz

- Yönetmeliği yayımlamaz.
- Çalışan onayı veya tebliği yapmaz.
