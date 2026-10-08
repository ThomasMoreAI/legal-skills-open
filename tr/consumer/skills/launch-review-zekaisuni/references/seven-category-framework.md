# Turkish Product Launch Review Framework

Bu varsayilan cerceve, ekipte ozel bir framework yoksa kullanilir. Kategoriler sabittir; sonuc ve agirlik sirket profilindeki risk kalibrasyonuna, hedef pazarlara ve sektor duzenlemelerine gore belirlenir.

## 1. Sozlesme ve Kullanici Taahhutleri

**Soru:** Lansman mevcut kullanim sartlari, SLA, abonelik, garanti, mesafeli satis, iade/cayma veya musteri sozlesmeleriyle celisiyor mu?

**Kontrol:** ToS, gizlilik/cerez politikasi, SLA, kampanya sartlari, abonelik sozlesmesi, mesafeli sozlesme, on bilgilendirme, enterprise MSA, public docs.

**Auto-skip:** Kullaniciya gorunmeyen, taahhut degistirmeyen saf ic altyapi degisikligi.

## 2. KVKK ve Veri

**Soru:** Yeni veri, yeni amac, yeni paylasim, yeni tedarikci, cerez/profil veya yurt disina aktarim var mi?

**Kontrol:** Veri kategorileri, ilgili kisi gruplari, KVKK m.5/m.6 isleme sarti, aydinlatma, acik riza, saklama, imha, aktarim, VERBIS/envanter, cerez/CMP, IYS.

**Auto-skip:** Gercekten veri akisi degismiyor ve yeni logging/analytics yok.

## 3. Reklam ve Haksiz Ticari Uygulamalar

**Soru:** Metin, gorsel, UX veya kampanya tuketiciyi yaniltabilecek iddia, karsilastirma, indirim, ortulu reklam veya eksik bilgi iceriyor mu?

**Kontrol:** Ticari Reklam ve Haksiz Ticari Uygulamalar Yonetmeligi, Reklam Kurulu duyurulari, fiyat/indirim kilavuzlari, sosyal medya etkileyici kilavuzu, sektor reklam yasaklari.

**Auto-skip:** Dis pazarlama, urun ici iddia, fiyat/indirim, influencer veya kampanya yok.

## 4. E-ticaret, Checkout ve Abonelik

**Soru:** Online satis, siparis, abonelik, otomatik yenileme, ucretsiz deneme, iptal, iade veya ticari elektronik ileti akisi degisiyor mu?

**Kontrol:** 6502, 6563, mesafeli sozlesme, abonelik yonetmeligi, on bilgilendirme, cayma istisnasi, siparis ozeti, ETBIS/IYS, ETHS/ETAHS rolleri.

**Auto-skip:** Para, siparis, abonelik, ticari ileti veya checkout akisi yok.

## 5. Urun Guvenligi, Erisilebilirlik ve Sektor

**Soru:** Urun regule bir sektor, guvenlik standardi, teknik mevzuat, erisilebilirlik veya kamu/yerel izin etkisi doguruyor mu?

**Kontrol:** BTK, BDDK/TCMB, SPK, TİTCK, EPDK, Rekabet, Ticaret Bakanligi urun guvenligi, ilgili teknik duzenlemeler, app store/marketplace kurallari.

**Auto-skip:** Ayni kullanici, ayni sektor, ayni pazar ve ayni teknik yuzey.

## 6. Fikri Haklar ve Icerik

**Soru:** Yeni ucuncu taraf icerik, marka, lisans, acik kaynak, veri seti, kullanici icerigi veya AI output'u var mi?

**Kontrol:** FSEK/SMK etkisi, lisans kosullari, marka kullanimi, customer logosu, stock/gorsel/font, UGC moderasyon, takedown, egitim verisi haklari.

**Auto-skip:** Yeni icerik, dependency, logo, veri seti veya output yok.

## 7. Guvenlik ve Ucuncu Taraflar

**Soru:** Yeni vendor, entegrasyon, API, bulut servisi, kimlik dogrulama veya veri erisim paterni var mi?

**Kontrol:** Vendor sozlesmesi, DPA/VK sozlesmesi, alt isleyen, guvenlik review, SLA, incident notice, veri lokasyonu, erisim yetkileri.

**Auto-skip:** Yeni ucuncu taraf veya teknik saldiri yuzeyi yok.

## 8. AI / Otomasyon

**Soru:** AI, otomatik karar, scoring, recommendation, generative content, model egitimi veya AI vendor kullanimi var mi?

**Kontrol:** AI use-case kaydi, insan denetimi, veri haklari, model egitimi, sentetik icerik ifsasi, KVKK profil/otomatik karar etkisi, vendor AI sartlari, sektor kurallari.

**Auto-skip:** AI veya otomasyon bileseni yok.
