---
name: pia-generation-zekaisuni
title: /pia-generation
description: Yeni veri işleme faaliyeti için Türk KVKK pratiğine uygun VKED/PIA taslağı üretir. Amaç, veri kategorisi, rol, hukuki sebep, aydınlatma, açık rıza, yurt dışı aktarım, tedarikçi, güvenlik, saklama-imha, risk ve aksiyon planı çıkarır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/privacy-legal/skills/pia-generation
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: data-protection
language: tr
---

# /pia-generation

## Amaç

VKED (Veri Koruma Etki Değerlendirmesi) / privacy impact assessment taslağı üretir. Türk hukukunda yabancı rejimlere özgü "her durumda zorunlu etki değerlendirmesi" terminolojisini otomatik varsaymaz; yüksek risk ve Kurul uygulaması kontrolü yapar.

## Girdi

1. Practice profile `CLAUDE.md`.
2. Varsa use-case triage çıktısı.
3. Ürün/iş birimi açıklaması.
4. Veri akışı, sistem mimarisi, tedarikçi, bulut ve aktarım bilgileri.
5. Aydınlatma metni, politika, envanter ve DPA.

## Eksik Bilgi Soruları

- Faaliyet hangi amaçla yapılacak?
- Hangi veri kategorileri var?
- Veri sahipleri kim?
- Veri kaynağı ve veri alıcıları kim?
- Türkiye dışına aktarım var mı?
- Saklama süresi nedir?
- Erişim yetkileri ve güvenlik tedbirleri neler?
- İlgili kişi hakları nasıl karşılanacak?
- Tedarikçi/alt işleyen var mı?

## VKED Bölümleri

```markdown
# VKED / Privacy Impact Assessment - [Faaliyet]

## 1. Faaliyet Özeti
- Amaç:
- İş sahibi:
- Sistemler:
- Veri sahibi grupları:
- Veri kategorileri:

## 2. Rol ve Taraflar
| Taraf | Rol | Not |
|---|---|---|
| [şirket] | veri sorumlusu / veri işleyen / ortak | |
| [tedarikçi] | veri işleyen / alt işleyen / alıcı | |

## 3. Hukuki Sebep
| Veri kategorisi | Amaç | KVKK m.5/m.6 şartı | Aydınlatma | Açık rıza |
|---|---|---|---|---|
| [kategori] | [amaç] | [şart] | [durum] | [gerekli/gereksiz] |

## 4. Aktarım
- Yurt içi alıcılar:
- Yurt dışı aktarım:
- KVKK m.9 mekanizması:
- Standart sözleşme / taahhüt / yeterlilik / istisna:
- Kurum bildirimi gerekliliği:

## 5. Veri Minimizasyonu ve Saklama
- Gereklilik:
- Alternatif / daha az veriyle çözüm:
- Saklama süresi:
- İmha yöntemi:

## 6. Güvenlik Tedbirleri
- Erişim:
- Şifreleme / maskeleme:
- Loglama:
- Yetki gözden geçirme:
- İhlal müdahalesi:

## 7. Risk Değerlendirmesi
| Risk | Olasılık | Etki | Seviye | Azaltım |
|---|---|---|---|---|
| [risk] | düşük/orta/yüksek | düşük/orta/yüksek | yeşil/sarı/turuncu/kırmızı | [tedbir] |

## 8. Karar ve Koşullar
**Sonuç:** ilerleyebilir / koşullu ilerleyebilir / hukuk incelemesi / durdur

**Koşullar:**
- [aksiyon, sahip, tarih]
```

## Özel Eskalasyon

Şunlar varsa hukuk + güvenlik + ilgili iş sahibi onayı iste:

- özel nitelikli veri,
- çocuk verisi,
- çalışan izleme,
- sağlık/biyometri/konum,
- AI/model eğitimi,
- büyük ölçekli izleme,
- yurt dışı aktarım,
- veri ihlali geçmişi,
- Kurul/şikayet/dava riski.

## Bu Skill Ne Yapmaz

- Nihai Kurul uyum görüşü vermez.
- Teknik kontrolleri test etmez.
- Politika veya envanteri otomatik yayımlamaz.
