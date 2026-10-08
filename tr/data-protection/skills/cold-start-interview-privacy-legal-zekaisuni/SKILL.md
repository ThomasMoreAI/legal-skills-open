---
name: cold-start-interview-privacy-legal-zekaisuni
title: /cold-start-interview
description: Legal Turkish privacy/KVKK kurulum mülakatını çalıştırır. KVKK rolü, veri sorumlusu/veri işleyen pozisyonu, VERBIS, aydınlatma, açık rıza, yurt dışına aktarım, veri ihlali, ilgili kişi başvurusu, DPA/veri işleyen playbook'u ve VKED/PIA tetiklerini kurar. İlk kurulum, redo veya entegrasyon kontrolü için kullanılır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/privacy-legal/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: data-protection
language: tr
---

# /cold-start-interview

Bu skill `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasını Türk KVKK pratiğine göre oluşturur veya günceller.

## Akış

1. Mevcut config'i oku.
2. Eksik veya placeholder ağırlıklı ise mülakatı başlat.
3. `--redo` yoksa dolu profili ezmeden önce onay iste.
4. `--check-integrations` varsa yalnızca erişilebilen entegrasyonları test et; bağlı olmayan kaynağı bağlı gösterme.
5. Yazmadan önce kurulum özetini göster.

## Açılış

Şunu söyle:

> `privacy-legal` KVKK işleri içindir: yeni veri işleme faaliyeti triyajı, VKED/PIA, veri işleyen sözleşmesi, ilgili kişi başvurusu, politika drift takibi, yurt dışına aktarım ve veri ihlali ilk değerlendirmesi.
>
> Kısa kurulum temel rol, veri kategorileri, VERBIS, politika ve eskalasyonları kurar. Tam kurulum DPA playbook, yurt dışı aktarım, ihlal süreci, saklama-imha ve örnek belgelerden house style çıkarır.
>
> Kısa mı, tam mı ilerleyelim?

Yanıtı bekle.

## Mülakat Bölümleri

### 1. Kurum ve Rol

- Şirket/müvekkil kim?
- Sektör ve faaliyet nedir?
- Ana rol: veri sorumlusu, veri işleyen, ortak veri sorumlusu veya değişken mi?
- Veri sahibi grupları kimler: müşteri, çalışan, aday, tedarikçi, ziyaretçi, çocuk, hasta, diğer?
- Türkiye dışı veri konusu, müşteri veya operasyon var mı?
- KVKK ekibi, hukukçu, güvenlik ve eskalasyon sorumluları kim?

### 2. Regülatör Ayak İzi

Sor:

- KVKK/Kurul ve VERBIS kapsamı?
- BDDK, SPK, TCMB, BTK, TİTCK, Rekabet, sağlık, finans, telekom, e-ticaret veya kamu sektörü etkisi var mı?
- AB/AEA, Birleşik Krallık, ABD veya başka ülke privacy rejimi gerçekten uygulanıyor mu?
- Açık Kurul incelemesi, veri ihlali, şikayet veya dava var mı?

### 3. Veri Envanteri ve Politika

İste:

- Kişisel veri işleme envanteri veya VERBIS kaydı.
- Aydınlatma metinleri ve gizlilik politikası.
- Açık rıza metinleri.
- Çerez/CMP, İYS/ticari ileti, çalışan aydınlatması, kamera/CCTV metinleri.
- Saklama ve imha politikası.

### 4. DPA / Veri İşleyen Playbook

Sor:

- Şirket çoğunlukla veri sorumlusu mu veri işleyen mi?
- Alt işleyen onay/bildirim standardı.
- İhlal bildirim süresi ve güvenlik ekibi.
- Silme/iade, denetim, sertifikasyon, audit raporu, log ve teknik tedbir yaklaşımı.
- Yurt dışı aktarım: bulut, destek, analitik, grup şirketi, model/AI eğitimi.
- Asla kabul edilmeyecek maddeler.

### 5. VKED / PIA Tetikleri

Sor:

- Hangi faaliyetler VKED gerektirsin?
- Özel nitelikli veri, çocuk verisi, çalışan izleme, konum, biyometri, sağlık, profil çıkarma, otomatik karar, AI/model eğitimi, büyük ölçekli izleme, yurt dışı aktarım için default yaklaşım.
- Kim onaylar?

### 6. İlgili Kişi Başvurusu

Sor:

- Başvuru kanalları.
- Kimlik doğrulama yöntemi.
- Kontrol edilecek sistemler.
- 30 günlük yanıt takibi kimde?
- Red/istisna kararını kim verir?

### 7. Veri İhlali

Sor:

- İlk haber alma kanalı.
- Security/legal incident commander.
- Kurul ve ilgili kişi bildirimi sahibi.
- Forensic/log kaynakları.
- 72 saat veya başka süre varsayımı kullanılacaksa güncel Kurul kaynağıyla doğrulama gerekeceğini belirt.

### 8. Seed Belgeler

İste:

- Gizlilik politikası / aydınlatma metni,
- DPA/veri işleyen sözleşmesi,
- VKED/PIA örneği,
- VERBIS/envanter,
- İlgili kişi başvurusu örneği,
- İhlal prosedürü.

## Yazmadan Önce

Şu özeti göster:

```markdown
## KVKK Kurulum Özeti
- Rol:
- Veri sahibi grupları:
- Regülatör ayak izi:
- DPA playbook:
- VKED tetikleri:
- İlgili kişi başvurusu:
- İhlal süreci:
- Açık kalan sorular:
```

Sonra sor:

> Bunları privacy profiline yazayım mı? Açık alanları `[PLACEHOLDER]` bırakabilirim.

## Yazılacak Yer

`~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md`

Template olarak plugin içindeki `privacy-legal/CLAUDE.md` kullanılır.

## Bu Skill Ne Yapmaz

- Hukuki görüş vermez.
- Kurul/VERBIS/İYS bildirimi yapmaz.
- Eksik cevapları uydurmaz.
- Kullanıcı onayı olmadan mevcut profili ezmez.
