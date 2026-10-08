---
name: use-case-triage-privacy-legal-zekaisuni
title: /use-case-triage
description: Yeni veri işleme faaliyeti, ürün özelliği, tedarikçi, AI/model eğitimi, çalışan izleme, pazarlama veya aktarım akışını KVKK açısından hızlıca sınıflandırır. PROCEED, VKED REQUIRED, LEGAL REVIEW, STOP karar seçenekleri, eksik bilgi ve handoff üretir.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/privacy-legal/skills/use-case-triage
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: data-protection
language: tr
---

# /use-case-triage

## Amaç

Yeni bir faaliyetin KVKK bakımından hangi kapıdan geçmesi gerektiğini belirler. Yabancı privacy rejimlerine özgü zorunlu etki değerlendirmesi veya tüketici privacy varsayımı yapmaz; Türk KVKK çekirdeğini uygular.

## Başlamadan

1. `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasını oku.
2. Config eksikse kullanıcıyı `/privacy-legal:cold-start-interview` komutuna yönlendir.
3. `references/currency-watch.md` dosyasını kontrol listesi olarak oku.
4. Matter workspace açıksa aktif matter'ı yükle.

## Veri Toplama

Eksikse şu soruları sor:

- Hangi veri kategorileri işleniyor?
- Veri sahipleri kim?
- Amaç nedir?
- Veri kaynağı nedir?
- Sistem/tedarikçi/bulut var mı?
- Türkiye dışına aktarım var mı?
- Otomatik karar, profil çıkarma, AI/model eğitimi veya büyük ölçekli izleme var mı?
- Özel nitelikli veri, çocuk verisi, çalışan verisi, sağlık/biyometri/konum verisi var mı?

## Sınıflandırma

### PROCEED

Yalnızca şu koşullarda:

- KVKK m.5/m.6 işleme şartı açık,
- aydınlatma metni kapsamı karşılıyor,
- yurt dışı aktarım yok veya mekanizma doğrulanmış,
- tedarikçi/DPA gerekmiyor veya mevcut,
- yüksek risk tetiklenmiyor,
- politika/VERBIS/envanter çelişkisi yok.

### VKED REQUIRED

Şunlardan biri varsa:

- özel nitelikli veri,
- çocuk verisi,
- çalışan izleme veya performans/profil analizi,
- konum, biyometri, sağlık, ceza mahkumiyeti verisi,
- AI/model eğitimi veya otomatik karar,
- büyük ölçekli izleme,
- yeni tedarikçi veya yurt dışına aktarım,
- politika veya envanterde yeni amaç/veri kategorisi.

### LEGAL REVIEW

Hukuki sebep, açık rıza, aydınlatma, sektör regülasyonu, Kurul kararı, veri işleyen rolü veya aktarım mekanizması belirsizse.

### STOP

Şunlardan biri varsa:

- işleme amacı belirsiz veya meşru değil,
- KVKK m.5/m.6 şartı yok,
- açık rıza baskılı/battaniye veya aydınlatmadan kopuk,
- yurt dışı aktarım mekanizması yok,
- politika açıkça bu faaliyeti dışlıyor,
- veri minimizasyonu veya güvenlik tedbiri bariz yetersiz.

## Çıktı

```markdown
GİZLİ HUKUKİ / KVKK ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

Reviewer note
- Kaynaklar:
- Okuma kapsamı:
- Doğrulanması gerekenler:
- Aksiyon öncesi:

# KVKK Use-Case Triage - [Faaliyet]

**Sınıflandırma:** PROCEED | VKED REQUIRED | LEGAL REVIEW | STOP
**Kısa gerekçe:** [1-3 cümle]

## KVKK Kapıları

| Kapı | Durum | Not |
|---|---|---|
| Kişisel veri / anonimlik | uygun / belirsiz / risk | |
| Rol | veri sorumlusu / veri işleyen / ortak / belirsiz | |
| KVKK m.5/m.6 işleme şartı | uygun / belirsiz / yok | |
| Aydınlatma | kapsıyor / güncellenmeli / yok | |
| Açık rıza | gerekmiyor / gerekli / sorunlu | |
| Yurt dışı aktarım | yok / mekanizma var / mekanizma yok | |
| Tedarikçi/DPA | yok / mevcut / gerekli | |
| VERBIS/envanter | etkilenmez / güncellenmeli / belirsiz | |

## Devam Koşulları

- [aksiyon]

## Handoff

- [VKED / DPA review / policy monitor / security / legal review]
```

## Bu Skill Ne Yapmaz

- Kurul bildirimi veya veri aktarım bildirimi yapmaz.
- Nihai hukuki uygunluk onayı vermez.
- Teknik güvenlik tedbirlerinin uygulandığını kanıt olmadan varsaymaz.
