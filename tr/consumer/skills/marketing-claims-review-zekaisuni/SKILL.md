---
name: marketing-claims-review-zekaisuni
title: /marketing-claims-review
description: Reklam, landing page, e-posta, sosyal medya, app store metni, indirim ve kampanya iddialarini Turk reklam hukuku ve Reklam Kurulu pratigi acisindan inceler. "Can we say this", "bu reklam olur mu", "check these claims" gibi isteklerde kullan.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/product-legal/skills/marketing-claims-review
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: consumer
language: tr
---

# /marketing-claims-review

## Amac

Pazarlama metnindeki olculebilir, karsilastirmali, mutlak, ima edilen veya hassas sektor iddialarini bul; kanit gereksinimini ve duzeltme onerilerini ver. Reklam Kurulu/Ticaret Bakanligi, 6502 ve ilgili sektor kurallari guncel kaynak kontrolu gerektirebilir.

## Akis

1. Product profile `## Pazarlama Iddialari` bolumunu oku.
2. Asset'i oku: metin, gorsel ima, fiyat/indirim, influencer/testimonial, mecra ve hedef kitle.
3. Her iddiayi ayikla; saf subjektif ifade disinda kalanlari tabloya al.
4. Iddia tipini belirle: olgusal, karsilastirmali, ima edilen, mutlak, fiyat/indirim, influencer/testimonial, sektor hassas.
5. Kanit dosyasi, metodoloji, tarih, kapsam ve disclaimers kontrolu yap.
6. Kisa asset'lerde duzeltilmis metni dogrudan yaz; uzun asset'lerde degisiklik listesini ver.

## Turk Reklam Kontrol Kapilari

- Reklam dogru, durust, kamu duzeni/genel ahlak ve kisilik haklarina uygun mu?
- Tuketici deneyim/bilgi eksikligi istismar ediliyor mu?
- Ortulu reklam veya ifsasiz influencer/testimonial var mi?
- Karsilastirmali reklamda rakip marka/logo/unvan kullaniliyor mu; karsilastirma objektif, olculebilir, dogrulanabilir mi?
- Indirimde onceki fiyat, baslangic/bitis tarihi ve stok/miktar siniri acik mi?
- "Ucretsiz", "garantili", "sinirsiz", "en iyi", "tek", "100%", "risksiz" gibi mutlak ifadeler kanitlanabilir mi?
- Saglik, gida, takviye edici gida, kozmetik, finans, cocuk, oyun veya regule sektor iddiasi var mi?
- Platform politikasi veya mecra kurali canli dogrulama gerektiriyor mu?

## Iddia Tablolama

```markdown
**Iddia:** "[tam alinti]"
**Tip:** [Olgusal | Karsilastirmali | Ima edilen | Mutlak | Fiyat/indirim | Influencer/testimonial | Sektor hassas]
**Kanit dosyasi:** [Var - kaynak | Yok | Bilinmiyor]
**Cagri:** [Temiz | Kanit gerekir | Yeniden yaz | Kes]
**Onerilen metin:** "[alternatif]"
**Neden:** [tek cumle]
**Dogrulama:** [Ticaret Bakanligi/Reklam Kurulu/KVKK/platform/kullanici sagladi/dogrula]
```

## Cikti

```markdown
[GIZLI HUKUKI / URUN HUKUKU CALISMA TASLAGI - HUKUKCU INCELEMESINE TABIDIR]

Reviewer note
- Kaynaklar:
- Okuma kapsami:
- Dogrulanmasi gerekenler:
- Aksiyon oncesi:

# Reklam Iddia Incelemesi: [Asset]

## Ozet

[N] iddia incelendi. [N] temiz, [N] kanit/duzeltme, [N] kes.

**Yayin durumu:** [Yayinlanabilir | Degisiklikle yayinlanabilir | Yayinlanmamali]

## Iddia Bazli Inceleme

[Kirmizi once, sonra sari, sonra temiz]

## Onerilen Revizyon

[Kisa metinlerde final revize metin; uzun metinlerde degisiklik listesi]

## Yayin Oncesi Gereken Kanitlar

| Iddia | Gereken kanit | Sahip |
|---|---|---|
```

Non-lawyer kullanici icin "Yayinlanabilir" ifadesi hukukcu incelemesi sonrasi kullanilir; aksi halde "hukukcuya goturulecek taslak cagri" olarak yaz.

## Handoff

- KVKK/cerez/hedefleme varsa `/privacy-legal:use-case-triage`.
- AI iddiasi varsa `/ai-governance-legal:use-case-triage`.
- Sektor iddiasi varsa ilgili uzman/hukukcu onayi.
