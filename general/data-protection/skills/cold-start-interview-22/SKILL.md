---
name: cold-start-interview-22
title: /cold-start-interview
description: 'Türkiye regulatory setup görüşmesi: izlenen kurumları, kaynakları, önem eşiğini, politika kütüphanesini, gap response ve taslak/görüş takip ayarlarını kurar.'
author: ZekaiSuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/regulatory-legal/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: tr
---

# /cold-start-interview

## Amaç

Her kurum çok şey yayımlar; kullanıcının ihtiyacı olan şey kendi sektörüne ve politika kütüphanesine göre anlamlı olanları yakalamaktır. Bu görüşme regulatory-legal profilini kurar.

## İlk Kontrol

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md`:

- Yoksa görüşmeye başla.
- `SETUP PAUSED` varsa kaldığı yerden devam etmeyi öner.
- Placeholder varsa tamamlanmamış setup olarak ele al.
- Doluysa `--redo` olmadan yeniden sorma.
- `--check-integrations` varsa sadece entegrasyon durumunu test et; test edilmeyen konnektörü bağlı sayma.

## Kısa Preamble

> `regulatory-legal`, Türkiye'de düzenleyici gelişmeleri izlemek, politika gap'i çıkarmak ve taslak/görüş sürelerini takip etmek içindir.
>
> Kısa kurulum: rol, sektör, izlenecek ana kurumlar. Tam kurulum: kaynaklar, önem eşiği, politika kütüphanesi, gap sahipleri ve görüş takip akışı.
>
> Kısa mı, tam mı?

## Part 0 - Kullanıcı ve Entegrasyonlar

Sor:

- Günlük kullanıcı kim: avukat/hukuk profesyoneli, avukat erişimi olan non-lawyer, avukat erişimi olmayan non-lawyer?
- Çalışma bağlamı: in-house, hukuk bürosu, danışmanlık, kamu/clinic, başka?
- Bağlı araçlar: Slack/Teams, Google Drive/SharePoint, araştırma/veri tabanı, e-posta.

Non-lawyer ise çıktıların araştırma/avukat incelemesi çerçevesinde verileceğini ve kurumlara sunum, gap kapatma, uyum sertifikasyonu gibi adımlarda avukat kontrolü sorulacağını kaydet.

## Part 1 - İzleme Listesi

Kullanıcıda mevcut watchlist/spreadsheet/memo varsa önce onu iste. Yoksa sor:

- Şirket/klient ne yapıyor, hangi sektörde?
- Hangi Türkiye kurumları izlenmeli?
  - Genel: Resmi Gazete, Mevzuat.
  - Veri: KVKK.
  - Rekabet: Rekabet Kurumu.
  - Finans: TCMB, BDDK, SPK, MASAK.
  - Telekom/internet: BTK.
  - Enerji: EPDK.
  - Tüketici/e-ticaret/reklam: Ticaret Bakanlığı, Reklam Kurulu.
  - Sağlık: TİTCK, Sağlık Bakanlığı.
- Her kurum neden izleniyor?
- Bilerek izlenmeyecek ama yakın komşu kurum var mı?

## Part 2 - Önem Eşiği

Örneklerle kalibre et:

- Resmi Gazete'de yayımlanmış bağlayıcı değişiklik.
- Kurul kararı veya idari yaptırım.
- Sektördeki rakibe yaptırım.
- Taslak düzenleme / kamuoyu görüşü çağrısı.
- Rehber / ilke kararı.
- Basın açıklaması veya konuşma.
- İkincil kaynak bülteni.

Çıktı:

```markdown
## Materiality threshold

**Maddi / hemen bak:**
- [kurum/konu örnekleri]

**İncelemeye değer / digest:**
- [örnekler]

**FYI / atla:**
- [örnekler]
```

## Part 3 - Politika Kütüphanesi

Önce mevcut indeks iste. Yoksa:

- Politikalar nerede: Drive, SharePoint, yerel klasör, Confluence/Notion?
- İsimlendirme ve versiyon bilgisi var mı?
- Her politikanın sahibi kim?
- Hangi prosedürler regülasyon değişikliğinde genelde etkileniyor?

## Part 4 - Kaynaklar

Başlangıç olarak Resmi Gazete ve Mevzuat öner. Her kurum için kaynak/metot belirle:

| Kurum | Kaynak/metot | Format | Not |
|---|---|---|---|
| KVKK | kvkk.gov.tr karar/duyuru sayfaları | HTML | kurul kararları, rehberler |
| SPK | spk.gov.tr + SPK Bülteni | HTML/PDF | bülten/yaptırım |

RSS/API yoksa "HTML izleme" veya "manuel giriş" olarak kaydet. İkincil kaynaklar sadece lead olarak yazılır.

## Part 5 - Gap ve Görüş Süreci

- Gap triage sahibi kim?
- Kritik gap SLA'sı nedir?
- Politika sahibi bulunamazsa kime gider?
- Taslak/görüş karar sahibi kim?
- Görüş verilecekse iç inceleme son tarihi nasıl hesaplanır?

## Yazılacak Profil Blokları

`CLAUDE.md` içine:

- Who's using this
- Watched institutions
- Available integrations
- Policy library
- Materiality threshold
- Feed configuration
- Gap response process
- Consultation / draft tracking
- Matter workspaces
- Outputs

Eksik cevapları sessiz placeholder yapma; yazmadan önce kullanıcıya "bunlar açık kaldı" diye göster.

## Kapanış

Kurulumdan sonra öner:

- İlk kaynak izleme testi: `/regulatory-legal:reg-feed-watcher --since YYYY-MM-DD`
- Politika kütüphanesi gap testi: `/regulatory-legal:policy-diff`
- Açık gap görünümü: `/regulatory-legal:gaps`
- Taslak/görüş görünümü: `/regulatory-legal:comments`

## Yapmadıkları

- Kişisel hafızadan veya önceki konuşmalardan izin almadan profil doldurmaz.
- Test edilmeyen entegrasyonu bağlı göstermez.
- Türkiye dışı kaynakları varsayılan ana akış yapmaz; gerekirse ek katman olarak tutar.
