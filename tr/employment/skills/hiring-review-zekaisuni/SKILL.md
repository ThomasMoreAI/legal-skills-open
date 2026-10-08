---
name: hiring-review-zekaisuni
title: /hiring-review
description: İş teklifi, iş sözleşmesi, uzaktan çalışma eki, belirli süreli sözleşme, deneme süresi, rekabet yasağı, gizlilik, fikri haklar, eğitim masrafı, cezai şart, SGK işe giriş, yabancı çalışma izni ve aday/çalışan KVKK süreçlerini Türk iş hukuku uygulamasına göre inceler.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/hiring-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /hiring-review

## Başlamadan

1. Employment `CLAUDE.md` dosyasını oku.
2. `## İşe Alım ve Sözleşme Playbook`, `## Ücret ve Çalışma Süresi`, `## SGK / İŞKUR / İSG / KVKK Kapıları`, `## Çıktı Kuralları` bölümlerini yükle.
3. `references/currency-watch.md` içinden güncel değişkenleri kontrol et.

## Kontrol Kapıları

| Kapı | Sorular |
|---|---|
| Sözleşme türü | Belirsiz/belirli süreli gerekçesi, kısmi süre, uzaktan çalışma, deneme süresi uygun mu? |
| İş tanımı | Görev, lokasyon, raporlama, yan görev ve değişiklik yetkisi dengeli mi? |
| Ücret ve yan hak | Brüt/net ayrımı, ödeme günü, prim/bonus, masraf, yan haklar net mi? |
| Çalışma süresi | Fazla çalışma onayı, vardiya, denkleştirme, hafta tatili ve UBGT dili var mı? |
| SGK | İşe giriş bildirgesi, işyeri sicili, meslek kodu ve bordro hazırlığı işaretlendi mi? |
| KVKK | Aday/çalışan aydınlatması, özlük dosyası, background check, sağlık verisi ayrı mı? |
| Rekabet/gizlilik | TBK rekabet yasağı sınırları, gizlilik, fikri haklar, eğitim masrafı, cezai şart makul mü? |
| Yabancı çalışan | Çalışma izni, oturma/ikamet, bordro ve SGK istisnası kontrol edildi mi? |
| Politika ekleri | Personel yönetmeliği, disiplin, uzaktan çalışma, KVKK ve İSG ekleri tebliğ ediliyor mu? |

## Kırmızı Bayraklar

- Belirli süreli sözleşmede objektif neden yok.
- Deneme süresi veya rekabet yasağı ölçüsüz.
- Ücret/prim yapısı belirsiz.
- Fazla çalışma onayı yok veya iş sözleşmesine gömülü ve yenilenmeyen formatta.
- Sağlık/ceza kaydı/background check için KVKK dayanağı belirsiz.
- Yabancı çalışanda çalışma izni süreci yok.
- Alt işveren/geçici iş ilişkisi gerçekte işçi temini gibi duruyor.

## Çıktı

```markdown
GİZLİ HUKUKİ / İŞ HUKUKU ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

Reviewer note
- Kaynaklar:
- Okuma kapsamı:
- Doğrulanması gerekenler:
- Aksiyon öncesi:

# İşe Alım / İş Sözleşmesi İncelemesi - [Aday/Rol]

**Rol:** [pozisyon]
**Lokasyon/çalışma modeli:** [şehir/uzaktan/hibrit]
**Sözleşme türü:** [belirsiz/belirli/kısmi/uzaktan]

## Kısa Sonuç

[Gönderilebilir mi? Hangi maddeler değişmeli?]

## Bulgular

| Seviye | Konu | Sorun | Öneri |
|---|---|---|---|
| kırmızı/turuncu/sarı | | | |

## Revizyon Önerileri

- [madde ve önerilen metin]

## İşe Başlatma Checklist

- [ ] SGK işe giriş
- [ ] KVKK aydınlatma/özlük dosyası
- [ ] Politika ve eklerin tebliği
- [ ] Fazla çalışma onayı
- [ ] İSG eğitimi/sağlık gözetimi gerekiyorsa plan
```

## Bu Skill Ne Yapmaz

- Sözleşmeyi imzalamaz veya göndermez.
- Çalışma izni/SGK bildirimi yapmaz.
- Nihai rekabet yasağı veya cezai şart uygulanabilirliği görüşü vermez.
