---
name: customize-privacy-legal-zekaisuni
title: /customize
description: Privacy/KVKK practice profilini kısmi olarak günceller. Risk iştahı, eskalasyon kişileri, veri sorumlusu/veri işleyen playbook'u, yurt dışına aktarım pozisyonu, aydınlatma/politika taahhütleri, VKED tetikleri, ilgili kişi başvurusu süreci, veri ihlali süreci veya matter workspace ayarlarını tüm cold-start mülakatını tekrar etmeden değiştirir.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/privacy-legal/skills/customize
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: data-protection
language: tr
---

# /customize

## Ne Zaman Kullanılır

Kullanıcı profilin bir bölümünü değiştirmek ister: örneğin "alt işleyen bildirim süresini 14 gün yap", "ilgili kişi başvurusu sahibi değişti", "yurt dışı aktarımda daha konservatif ol", "VKED tetiklerine çalışan izlemeyi ekle".

## Akış

1. `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasını oku.
2. Profil yoksa veya placeholder ağırlıklıysa şunu söyle:

   > Önce `/privacy-legal:cold-start-interview` çalışmalı. `customize`, kurulmuş profilde tekil değişiklik yapmak içindir.

3. Değiştirilebilir haritayı göster:

   - **Kurum Profili**: şirket, sektör, rol, veri sahibi grupları, regülatör ayak izi.
   - **Kullanıcı Rolü**: hukukçu / non-lawyer, eskalasyon ve human-in-the-loop.
   - **KVKK Çekirdek Kontrolleri**: m.5/m.6, aydınlatma, açık rıza, VERBIS/envanter.
   - **Yurt Dışına Aktarım**: m.9 mekanizmaları, standart sözleşme, bildirim, bulut/grup şirketi akışları.
   - **Veri İşleyen / DPA Playbook**: alt işleyen, güvenlik, ihlal, silme-iade, audit, sorumluluk.
   - **Aydınlatma / Politika Taahhütleri**: gizlilik politikası, aydınlatma, açık rıza, çerez, İYS.
   - **VKED / PIA**: tetikler, risk skoru, onay sahipleri.
   - **İlgili Kişi Başvurusu**: kanallar, kimlik doğrulama, sistem listesi, 30 gün takibi.
   - **Veri İhlali**: incident owner, Kurul/ilgili kişi bildirimi, forensic kaynakları.
   - **Matter Workspaces**: aktif matter, cross-matter, arşiv.

4. Tek değişiklik seçtir; mevcut değeri göster.
5. Yeni değeri al, aşağı akış etkisini açıkla.
6. Yazmadan önce onay al.
7. Değişikliği profile işle ve hangi skill'leri etkilediğini söyle.

## Aşağı Akış Etkisi Örnekleri

- Alt işleyen bildirim süresi değişirse `dpa-review` yeni eşiği sapma olarak kullanır.
- VKED tetiklerine yeni kategori eklenirse `use-case-triage` daha fazla faaliyeti `VKED REQUIRED` sınıfına alır.
- İlgili kişi başvuru sistemi listesi değişirse `dsar-response` arama tablosunu buna göre üretir.
- Politika taahhüdü değişirse `policy-monitor` yeni metni esas alır.
- Yurt dışı aktarım risk iştahı değişirse `dpa-review` ve `pia-generation` daha sık hukuk incelemesi ister.

## Guardrails

- Bölüm silme; kapsam dışı kalan bir rejimi "şu an kapsam dışı" diye işaretle.
- KVKK m.5/m.6, m.10 aydınlatma, m.11/m.13 başvuru, m.12 güvenlik, m.9 aktarım ve ihlal guardrail'lerini kaldırma.
- Açık rıza ile aydınlatmayı tek metne birleştirme.
- 30 günlük ilgili kişi yanıt süresini daha uzun bir "iç hedef" olarak ayarlama.
- Standart sözleşme veya Kurul bildirimi gibi resmi süreçleri "gerekmez" yapmadan önce hukuki gerekçe iste.
- Bir seferde tek değişiklik yap; tüm profil mülakatını tekrar başlatma.

## Çıktı

```markdown
# Privacy/KVKK Profil Güncellemesi

**Değişen bölüm:** [bölüm]
**Eski değer:** [özet]
**Yeni değer:** [özet]

## Etkilenen Skill'ler

- [skill]: [etki]

## Kontrol

- [ ] Çelişki yok
- [ ] İnsan onayı alındı
- [ ] Sonraki çıktı yeni değeri kullanacak
```

## Bu Skill Ne Yapmaz

- İlk kurulumu yapmaz.
- Hukuki guardrail'leri sessizce gevşetmez.
- Kullanıcı onayı olmadan config yazmaz.
