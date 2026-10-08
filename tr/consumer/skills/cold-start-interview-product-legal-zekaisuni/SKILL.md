---
name: cold-start-interview-product-legal-zekaisuni
title: /cold-start-interview
description: 'Product-legal profilini Turk urun hukuku icin kurar: lansman gate''leri, risk kalibrasyonu, reklam iddia politikasi, KVKK/AI/sektor eskalasyonu ve entegrasyonlari toplar.'
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/product-legal/skills/cold-start-interview
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: consumer
language: tr
---

# /cold-start-interview

## Amac

Bu kurulum, product-legal skill'lerinin sirketin gercek risk kalibrasyonuna gore calismasini saglar. Turkiye urun hukuku icin odak: tuketici/e-ticaret, reklam, KVKK, sektor regulasyonu, urun guvenligi, AI ve lansman sureci.

## Konum

Profil su yola yazilir:

```text
~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md
```

Var olan profil doluysa yeniden yazma; kullanici `--redo` istemediyse mevcut profili ozetle ve `customize` oner.

## `--check-integrations`

Yalnizca Jira/Linear/Asana, dokuman depolama ve Slack gibi baglantilari test eder. Bir connector sadece `.mcp.json` icinde gorunuyor diye calisir kabul edilmez; kucuk bir okuma/arama denemesi basarili olmadan `bagli` yazma.

## Hızlı Kurulum Sorulari

Kullanici hizli kurulum isterse yalnizca sunlari sor ve kalan alanlari `[DEFAULT]` olarak isaretle:

1. Rolunuz nedir: hukukcu, PM, pazarlama, kurucu, operasyon?
2. Sirket/urun modeli nedir: B2C, B2B, pazaryeri, abonelik, fintech, saglik, oyun, egitim, diger?
3. Ana pazarlar neresi: Turkiye, AB, ABD, global?
4. En hassas alanlar: KVKK, reklam, fiyat/abonelik, sektor reg, AI, guvenlik, IP?
5. Lansman onayi kimde ve kritik risk kime eskale edilir?

## Tam Kurulum Sorulari

### 1. Sirket ve urun

- Urun ne satiyor ve kime?
- Tuketiciye mi, tacire mi, ikisine birden mi?
- Pazaryeri, abonelik, finansal hizmet, saglik, egitim, oyun, telekom veya kamu ayagi var mi?
- Turkiye disinda hangi pazarlar hedefleniyor?
- Hangi regulatorler veya kurumlar pratikte kritik?

### 2. Lansman sureci

- Lansmanlar nereden gelir: Jira, Linear, Asana, Drive, Slack, manuel?
- Hukuk hangi asamada devreye girer?
- Hangi degisiklikler otomatik hukuk review ister?
- Tipik SLA nedir?
- Gecmiste hangi lansmanlar bloklandi veya sartli ship edildi?

### 3. Risk kalibrasyonu

Asagidaki pattern'ler icin `FYI / bakmak gerekir / bloke` kararini iste:

- yeni veri/cerez/tracking,
- yeni vendor veya veri aktarimi,
- karsilastirmali veya sayisal reklam iddiasi,
- fiyat/indirim/abonelik/otomatik yenileme,
- cocuk/saglik/finans/egitim/telekom gibi sektor,
- AI, otomatik karar, model egitimi,
- app store/platform politikasi,
- customer logo/testimonial/influencer.

### 4. Pazarlama iddialari

- Kim inceler?
- Karsilastirmali reklam politikasi nedir?
- "En iyi / tek / garantili / ucretsiz / sinirsiz / 100%" gibi ifadeler icin ev kurali nedir?
- Indirim ve fiyat gosteriminde hangi kanitlar tutulur?
- Influencer/testimonial ve musteri logosu icin izin/ifsa standardi nedir?

### 5. KVKK, AI ve guvenlik

- KVKK sorumlusu ve privacy review sureci kimde?
- Cerez/CMP, IYS, VERBIS, aydinlatma ve yurt disina aktarim nasil yonetilir?
- AI use-case registry veya AI policy var mi?
- Security review ve vendor review nerede yapilir?

### 6. Cikti ve eskalasyon

- Dahili not formati nedir?
- Ticket'a paylasilabilir kisa yorum nasil olmalidir?
- Kim hangi riskte imza verir?
- Hukukcu olmayan kullanici icin hangi noktada durup avukat onayi istenir?

## Yazilacak Profil

Kokteki `product-legal/CLAUDE.md` sablonunu kullan. `[PLACEHOLDER]` alanlarini kullanicinin yanitlariyla doldur. Bilinmeyen alanlara `[PENDING - kullanici atladı]` yaz; sessiz bosluk birakma.

## Dogrulama

Kullanici belirli bir kanun, tutar, ceza, tarih, regulator karari veya platform politikasi soylerse, yazmadan once dogrulama gerektigini belirt. Guncel resmi kaynak olmadan profile kesin hukuk kuralı yazma; `dogrula` notu koy.

## Kapanis

Kurulum sonunda:

- risk kalibrasyonu tablosunu ozetle,
- ilk denenebilecek komutlari soyle,
- eksik kalan alanlari listele,
- `references/currency-watch.md` dosyasinin guncellik kontrol listesi oldugunu belirt.
