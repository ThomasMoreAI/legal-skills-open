---
name: cold-start-interview-employment-legal-zekaisuni
title: /cold-start-interview
description: Türk iş hukuku practice profilini kurar veya yeniler. İşveren/işyeri yapısı, çalışan grupları, SGK/İŞKUR/İSG, sendika/TİS, işe alım, ücret/çalışma süresi, izin, fesih, arabuluculuk, iç soruşturma, KVKK ve eskalasyon ayarlarını toplar. İlk kurulum, redo veya entegrasyon kontrolü için kullanılır.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/employment-legal/skills/cold-start-interview
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: tr
practice: employment
language: tr
---

# /cold-start-interview

## Amaç

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` dosyasını Türk iş hukuku uygulamasına göre oluşturur veya günceller.

## Akış

1. Mevcut config'i oku.
2. Placeholder ağırlıklıysa mülakatı başlat.
3. `--redo` yoksa dolu profili ezmeden önce onay iste.
4. `--check-integrations` varsa yalnızca erişilebilen entegrasyonları test et; bağlı olmayan kaynağı bağlı gösterme.
5. Yazmadan önce kurulum özetini göster.

## Açılış

Şunu söyle:

> `employment-legal` Türkiye iş hukuku işleri içindir: işe alım, iş sözleşmesi, ücret ve çalışma süresi, izin/rapor, fesih, arabuluculuk, iç soruşturma, işyeri politikası, SGK/İŞKUR/İSG ve çalışan verisi.
>
> Kısa kurulum temel işveren profili, çalışan grupları, fesih/izin ve eskalasyonları kurar. Tam kurulum SGK/İŞKUR/İSG, sendika/TİS, politika, örnek belgeler ve house style çıkarır.
>
> Kısa mı, tam mı ilerleyelim?

Yanıtı bekle.

## Mülakat Bölümleri

### 1. İşveren ve İşyeri

- İşveren/müvekkil kim?
- Sektör ve faaliyet nedir?
- İşyeri lokasyonları, SGK işyeri sicilleri ve çalışan sayıları?
- Çalışan grupları: beyaz yaka, mavi yaka, uzaktan, hibrit, saha, part-time, stajyer, yabancı çalışan?
- Alt işveren, taşeron, hizmet alımı, geçici iş ilişkisi veya EOR/payroll provider var mı?

### 2. Regülatör ve Sistemler

- SGK, İŞKUR, İSG, KVKK, sendika/TİS, belediye/ruhsat veya sektör düzenleyici etkisi var mı?
- HRIS, bordro, izin takip, SGK/e-Bildirge, arabuluculuk/dava dosyaları nerede tutuluyor?
- Kim hangi sistemi yönetiyor?

### 3. İşe Alım

- Standart iş sözleşmesi/teklif mektubu var mı?
- Belirsiz/belirli süreli, deneme süreli, uzaktan çalışma ve yabancı çalışma izni süreçleri?
- Rekabet yasağı, gizlilik, fikri haklar, eğitim masrafı, cezai şart standardı?
- Aday/çalışan KVKK aydınlatmaları ve background check pratiği?

### 4. Ücret ve Çalışma Süresi

- Ücret yapısı: aylık, saatlik, prim, bonus, komisyon, yan hak.
- Fazla çalışma onayı ve ödeme/serbest zaman pratiği.
- Vardiya, gece çalışması, denkleştirme, hafta tatili, UBGT, uzaktan çalışma masrafı.
- Bordro, puantaj ve imzalı kayıt standardı.

### 5. İzin ve Devamsızlık

- Yıllık izin sistemi ve bakiye yönetimi.
- Rapor/iş göremezlik, doğum, süt izni, ücretsiz izin, mazeret izinleri.
- Devamsızlık ihtarı ve haklı fesih süreci.
- Sağlık verisi ve raporların KVKK saklama düzeni.

### 6. Fesih ve Arabuluculuk

- Standart fesih incelemesini kim başlatır?
- Savunma alma, uyarı/disiplin, performans yönetimi ve PIP süreçleri.
- SGK çıkış kodunu kim belirler?
- Kıdem/ihbar/yıllık izin/işçilik alacağı hesaplamasını kim yapar?
- İbraname, ikale ve arabuluculuk dosyası standardı?
- Toplu işçi çıkarma veya yeniden yapılanma süreci var mı?

### 7. İç Soruşturma

- Tipik konular: taciz, mobbing, ayrımcılık, hırsızlık, veri ihlali, çıkar çatışması, İSG.
- Soruşturmayı kim açar ve kim yürütür?
- Görüşme notları, deliller, kamera/e-posta kayıtları nerede saklanır?
- Hukuki gizlilik ve KVKK minimizasyonu nasıl sağlanır?

### 8. Politika ve Personel Yönetmeliği

- Personel yönetmeliği, disiplin prosedürü, uzaktan çalışma, fazla çalışma, KVKK, İSG, sosyal medya, cihaz/e-posta, kamera/CCTV politikaları var mı?
- Çalışanlara tebliğ/duyuru yöntemi nedir?

### 9. Eskalasyon

- Hukuk, İK, finans/bordro, İSG, KVKK, dış avukat ve yönetim onay zinciri.
- Kırmızı bayraklar: hamilelik/izin/sağlık/sendika/şikayet sonrası fesih, toplu işçi çıkarma, iş kazası, taciz/mobbing, yüksek tutarlı alacak, üst düzey çalışan, regülatör/dava.

## Yazmadan Önce

```markdown
## İş Hukuku Kurulum Özeti
- İşveren / işyerleri:
- Çalışan grupları:
- SGK/İŞKUR/İSG:
- Sendika/TİS:
- İşe alım playbook:
- Ücret/çalışma süresi:
- İzin/rapor:
- Fesih/arabuluculuk:
- İç soruşturma:
- Açık kalan sorular:
```

Sonra sor:

> Bunları employment profiline yazayım mı? Açık alanları `[PLACEHOLDER]` bırakabilirim.

## Yazılacak Yer

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`

Template olarak plugin içindeki `employment-legal/CLAUDE.md` kullanılır.

## Bu Skill Ne Yapmaz

- Hukuki görüş vermez.
- SGK/İŞKUR/UYAP/arabuluculuk sistemi işlemi yapmaz.
- Eksik cevapları uydurmaz.
- Kullanıcı onayı olmadan mevcut profili ezmez.
