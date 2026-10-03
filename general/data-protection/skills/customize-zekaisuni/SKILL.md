---
name: customize-zekaisuni
title: /customize
description: 'Regulatory practice profilinde tek bir şeyi günceller: izlenen kurum, kaynak, önem eşiği, politika kütüphanesi, gap yanıt süreci, görüş takibi veya matter ayarları.'
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/regulatory-legal/skills/customize
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: tr
---

# /customize

## Ne zaman çalışır

Kullanıcı bütün cold-start görüşmesini yeniden yapmak istemeden regulatory profilini değiştirmek ister.

## Akış

1. `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md` dosyasını oku. Yoksa veya placeholder ise önce `/regulatory-legal:cold-start-interview` öner.
2. Mevcut profili kısa harita olarak göster:
   - Şirket / sektör / yargı alanı
   - İzlenen kurumlar: Resmi Gazete, Mevzuat, KVKK, Rekabet, SPK, BDDK, BTK, EPDK, TCMB vb.
   - Kaynak yapılandırması: URL/metot, format, cadence.
   - Önem eşiği: maddi, incelemeye değer, FYI.
   - Politika kütüphanesi ve sahipleri.
   - Gap response: triage, SLA, escalation.
   - Taslak/görüş takip: karar sahibi, son tarih mantığı.
   - Matter workspace ve entegrasyonlar.
3. Kullanıcıdan hangi bölümün değişeceğini al.
4. Mevcut değer -> yeni değer -> downstream etki açıklaması -> onay -> yaz.

## Örnek Etkiler

- Kurum ekleme: bir sonraki kaynak izleme çalışması bu kurumu tarar; policy-diff bu kurum çıktıları için kaynak etiketi kullanır.
- Önem eşiği sıkılaştırma: digest kısalır; FYI kalemleri görünürlüğü azalır.
- Politika ekleme: policy-diff eşleştirme alanı genişler; gap owner routing iyileşir.
- Taslak takip açma: kamuoyu görüşü çağrıları comment tracker'a düşer.

## Guardrails

- Bölüm silme yerine "monitor only" veya "disabled" gibi açık durum kullan.
- Resmi Gazete/Mevzuat doğrulama katmanını kaldırma talebi gelirse riskini belirt.
- Kaynak etiketi, `[verify]` ve gönderim öncesi onay kuralları kaldırılmaz.
- Tek seferde tek değişiklik yap; büyük yeniden kurulum için cold-start'e yönlendir.
