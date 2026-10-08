---
name: international-expansion-zekaisuni
title: /international-expansion
description: Türkiye merkezli işverenin yeni ülke/şehir/çalışma modelinde istihdam planını veya yabancı işverenin Türkiye'de çalışan istihdamını ön değerlendirmeye alır. Payroll, SGK, işyeri/şube, çalışma izni, EOR, uzaktan çalışma, vergi, KVKK aktarımı ve yerel hukuk danışmanı gereksinimini çıkarır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/international-expansion
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /international-expansion

## Amaç

Yeni bir yerde çalışan istihdamı, sadece offer göndermek değildir. Türkiye bakımından SGK, vergi, bordro, iş sözleşmesi, çalışma izni, KVKK, İSG ve yerel hukuk zorunlulukları birlikte değerlendirilir. Türkiye dışı istihdamda nihai yerel hukuk görüşü gerekir.

## Intake

- Hangi ülke/şehir?
- Çalışan sayısı ve roller?
- Çalışma modeli: remote, şube, yerel şirket, EOR, danışman, alt işveren?
- Türkiye'de mi çalışacak, Türkiye dışından mı?
- Bordro ve ödeme kimde?
- Çalışan verisi Türkiye dışına aktarılıyor mu?
- Yabancı çalışan/çalışma izni var mı?
- İSG ve ekipman sorumluluğu kime ait?

## Türkiye Kapıları

| Kapı | Kontrol |
|---|---|
| İstihdam modeli | Yerel iş sözleşmesi, danışman, EOR, alt işveren, geçici iş ilişkisi |
| SGK/vergi | İşveren kaydı, bordro, prim, işyeri sicili |
| Çalışma izni | Yabancı çalışan, Türkiye'de fiili çalışma |
| KVKK | Çalışan verisi aktarımı, HRIS, grup şirketi erişimi |
| İSG | Uzaktan/saha çalışması, ekipman, risk değerlendirmesi |
| Politika | Personel yönetmeliği, disiplin, izin, çalışma saatleri |
| Yerel danışman | Türkiye dışı ülke için zorunlu eskalasyon |

## Çıktı

```markdown
GİZLİ HUKUKİ / İŞ HUKUKU ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

# İstihdam Genişleme Ön Değerlendirmesi - [Ülke/Model]

**Model:** [remote / local payroll / EOR / danışman / şube]
**Risk:** yeşil / sarı / turuncu / kırmızı

## Kısa Sonuç

[İlerlenebilir mi? Önce hangi yerel görüş/kayıt gerekir?]

## Kapı Analizi

| Kapı | Durum | Aksiyon |
|---|---|---|
| SGK/vergi | | |
| İş sözleşmesi | | |
| KVKK | | |
| İSG | | |
| Yerel hukuk | | |

## Aksiyon Planı

- [ ] Yerel hukuk danışmanı
- [ ] Payroll/SGK/vergi kurulumu
- [ ] Sözleşme/politika
- [ ] KVKK aktarım kontrolü
```

## Bu Skill Ne Yapmaz

- Türkiye dışı ülke hukukunu nihai olarak yorumlamaz.
- Yerel şirket, payroll veya vize/çalışma izni başvurusu yapmaz.
