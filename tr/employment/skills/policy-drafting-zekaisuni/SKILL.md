---
name: policy-drafting-zekaisuni
title: /policy-drafting
description: Türk iş hukuku uygulamasına uygun işyeri politikası, personel yönetmeliği bölümü veya prosedür taslağı hazırlar. Disiplin, taciz/mobbing, uzaktan çalışma, fazla çalışma, KVKK/çalışan verisi, e-posta/cihaz, kamera, İSG, masraf, sosyal medya ve yan hak konularında kullanılır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/policy-drafting
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /policy-drafting

## Başlamadan

1. Employment `CLAUDE.md` dosyasını oku.
2. `## İşyeri Politikaları`, `## SGK / İŞKUR / İSG / KVKK Kapıları`, `## Çıktı Kuralları` bölümlerini yükle.
3. Mevcut personel yönetmeliği veya politika varsa stilini oku.

## Politika Kapıları

- İş Kanunu ve ikincil mevzuatla uyum.
- KVKK aydınlatma/açık rıza ayrımı.
- İSG ve işyeri uygulaması etkisi.
- Çalışanlara tebliğ yöntemi.
- Disiplin yaptırımı varsa savunma ve eşit işlem.
- Toplu iş sözleşmesi veya sendika etkisi.
- Uygulanabilirlik: İK ve yöneticiler gerçekten bunu işletebilir mi?

## Çıktı

```markdown
GİZLİ HUKUKİ / İŞ HUKUKU ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

# Politika Taslağı - [Konu]

## Uygulama Notu

- Kapsam:
- Tebliğ yöntemi:
- KVKK/İSG/SGK etkisi:
- Hukukçu kontrolü:

## Politika Metni

[Başlık]

1. Amaç
2. Kapsam
3. Tanımlar
4. Kurallar
5. Sorumluluklar
6. İhlal ve yaptırım
7. Yürürlük

## Açık Noktalar

- [karar gerektiren alan]
```

## Bu Skill Ne Yapmaz

- Politikayı çalışanlara tebliğ etmez.
- TİS veya kurul onayı gerekip gerekmediğini kesinleştirmeden yürürlük önermez.
