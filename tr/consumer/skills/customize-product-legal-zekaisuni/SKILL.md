---
name: customize-product-legal-zekaisuni
title: /customize
description: 'Product-legal profilinde tek bir bolumu degistirir: risk kalibrasyonu, lansman framework''u, reklam iddia politikasi, eskalasyon, entegrasyon veya matter workspace ayarlari.'
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/product-legal/skills/customize
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: consumer
language: tr
---

# /customize

## Ne zaman kullanilir

Kullanici tum cold-start'i yeniden yapmak istemeden product-legal profilini ayarlamak ister.

## Akis

1. `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` dosyasini oku. Yoksa veya placeholder doluysa once `/product-legal:cold-start-interview` iste.
2. Degistirilebilir haritayi goster:
   - Sirket/urun modeli ve hedef pazarlar,
   - lansman sureci ve SLA,
   - Turk launch review kategorileri,
   - risk kalibrasyonu,
   - pazarlama iddialari ve kanit standardi,
   - KVKK/AI/guvenlik eskalasyonlari,
   - entegrasyonlar,
   - matter workspace.
3. Kullanici hangi bolumu degistirmek istedigini soyledikten sonra mevcut degeri goster.
4. Yeni degeri al; downstream etkisini acikla.
5. Kullanici onaylayinca profilde yalnizca ilgili satir/bolumu degistir.

## Guardrail

- `[dogrula]`, kaynak etiketi, reviewer note ve hukukcu incelemesi guardrail'leri kaldirilamaz.
- Risk kalibrasyonu gevsetiliyorsa etkisini acikca yaz: hangi komutlar artik daha az flag atacak?
- Yeni sektor veya pazar eklenirse `references/currency-watch.md` uyarisi ve ilgili resmi kaynak ihtiyaci eklenir.
- Ortadan kaldirilmak istenen kategori silinmez; `out of scope / route to [plugin/team]` olarak isaretlenir.

## Kapanis

Degisiklikten sonra kisa ozet ver:

```text
Guncellendi: [bolum]
Etkisi: [launch-review / is-this-a-problem / marketing-claims-review uzerindeki etki]
Eksik dogrulama: [varsa]
```
