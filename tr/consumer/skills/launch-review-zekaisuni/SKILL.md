---
name: launch-review-zekaisuni
title: /launch-review
description: Turk urun hukuku cercevesinde PRD, ticket veya lansman dokumanini kategori kategori inceler. Kullanici "review this launch", "legal review", "can we ship", "lansman incelemesi" veya PRD/ticket verdiginde kullan.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/product-legal/skills/launch-review
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: consumer
language: tr
sources:
- title: Seven Category Framework
  path: references/seven-category-framework.md
---

# /launch-review

## Akis

1. `~/.claude/plugins/config/claude-for-legal/product-legal/CLAUDE.md` profilini oku; placeholder varsa cold-start iste.
2. PRD, ticket, tasarim, checkout akisi, reklam/plans, policy ve hedef pazar bilgisini topla.
3. `references/seven-category-framework.md` icindeki Turk product launch framework'unu veya profilin kendi framework'unu uygula.
4. Bulgulari profil risk kalibrasyonuna gore `Dusuk / Orta / Yuksek / Bloke` olarak sinifla.
5. KVKK varsa `/privacy-legal:use-case-triage`; AI varsa `/ai-governance-legal:use-case-triage`; reklam iddiasi varsa `/product-legal:marketing-claims-review` handoff'u yap.
6. Ic hukuk notu ve paylasilabilir ticket yorumu olarak iki ayri cikti uret.

## Girdi Kontrolu

- Urun/ozellik ne yapiyor?
- Kim kullaniyor: tuketici, tacir, calisan, cocuk, hasta, finansal tuketici, kamu?
- Hedef pazar: Turkiye, AB, ABD veya diger?
- Yeni veri, yeni amac, yeni vendor, yeni fiyat/abonelik, yeni reklam iddiasi, yeni sektor veya yeni AI bileseni var mi?
- Lansman tarihi ve geri alma imkani nedir?

## Kategori Ciktisi

Her kategori icin su format kullanilir:

```markdown
### [Kategori]

**Kontrol edilen:** [PRD/ticket/policy/metin/ekran]
**Sonuc:** [Temiz | Is gerekiyor | Yuksek risk | Bloke | Uygulanmaz]
**Neden:** [somut bulgu, genel ders degil]
**Kaynak / dogrulama:** [resmi kaynak / kullanici sagladi / dogrula]
**Kalibrasyon:** [profildeki pattern veya "yeni pattern"]
**Aksiyon:** [ne yapilacak, kim, ne zamana kadar]
```

Uygulanmayan kategori tek cumleyle aciklanir; bos kontrol listesi doldurulmaz.

## Varsayilan Kategoriler

1. Sozlesme ve kullanici taahhutleri.
2. KVKK ve veri.
3. Reklam ve haksiz ticari uygulamalar.
4. E-ticaret, checkout ve abonelik.
5. Urun guvenligi, erisilebilirlik ve sektor.
6. Fikri haklar ve icerik.
7. Guvenlik ve ucuncu taraflar.
8. AI / otomasyon.

## Sektor Overlay

Su isaretler varsa kategoriye ek overlay ekle ve guncel resmi kaynak dogrula:

| Isaret | Overlay |
|---|---|
| Cocuk/ogrenci | KVKK cocuk verisi, reklamda cocuk istismari yasagi, egitim sektoru, platform yas derecelendirmesi |
| Saglik/gida/kozmetik/takviye | TİTCK, ilgili Bakanlik mevzuati, saglik beyanlari, Reklam Kurulu |
| Finans/odeme/kripto/yatirim | BDDK, TCMB, SPK, MASAK, finansal tuketici, yatirim tavsiyesi |
| Telekom/iletisim | BTK, elektronik haberlesme, ticari ileti |
| Oyun/sans/bahis/loot box | Sans/bahis mevzuati, tuketici, platform yas sinifi, odeme/iade |
| Kamu/ihale | Kamu ihale/sozlesme, veri lokasyonu, guvenlik, sektor izinleri |
| Pazaryeri | ETHS/ETAHS, mesafeli sozlesme rolleri, satici bilgisi, urun guvenligi |

## Cikti

```markdown
[GIZLI HUKUKI / URUN HUKUKU CALISMA TASLAGI - HUKUKCU INCELEMESINE TABIDIR]

Reviewer note
- Kaynaklar:
- Okuma kapsami:
- Dogrulanmasi gerekenler:
- Aksiyon oncesi:

# Lansman Incelemesi: [Ozellik]

**Tarih:** [YYYY-MM-DD]
**Lansman tarihi:** [varsa]
**PRD/Ticket:** [link/path]

## Kisa sonuc

**Cagri:** [Ship edilebilir | Sartli ship | Hukuk/uyum onayi gerekli | Bloke]

[Bir paragraf: ne ship oluyor, ana risk, ship icin hangi sartlar gerekir.]

## Bulgular

[Kategori bloklari]

## Aksiyonlar

| # | Aksiyon | Sahip | Son tarih | Bloke mi? |
|---|---|---|---|---|

## Eskalasyonlar

[Gerekirse]

## Sonraki kalibrasyon notu

[Bu pattern profil kalibrasyonuna eklenmeli mi?]

---

## SAFE TO POST TO TRACKER

**Launch status:** [green / yellow / red]

**Conditions:**
- [ ] [PM/eng/legal aksiyonu] - Owner: [ ] - Due: [ ]
```

Tracker yorumu hukuki gerekce, kaynak, gizli analiz veya regulasyon tartismasi icermez; sadece yapilacaklari soyler.

## Yapmadiklari

- Lansmani onaylamaz.
- Resmi kaynak kontrolu yapilmadan guncel tutar, ceza, esik veya platform politikasi kesinlestirmez.
- Teknik guvenlik veya urun performansini belge olmadan dogru varsaymaz.
