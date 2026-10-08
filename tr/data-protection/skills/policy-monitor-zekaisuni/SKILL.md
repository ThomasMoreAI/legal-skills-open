---
name: policy-monitor-zekaisuni
title: /policy-monitor
description: Gizlilik politikası, aydınlatma metinleri, açık rıza metinleri, çerez/CMP, İYS/ticari ileti, VERBIS/envanter ve sektör bildirimlerinin fiili uygulamayla uyumunu izler. VKED, DPA review, use-case triage ve ilgili kişi başvurusu çıktılarından politika drift'i bulur veya yeni bir veri işleme faaliyeti için "mevcut metinler bunu kapsıyor mu" kontrolü yapar.
author: zekaisuni
author_url: https://github.com/ZekaiSuni/claude-for-legal-turkish/tree/main/privacy-legal/skills/policy-monitor
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: tr
practice: data-protection
language: tr
---

# /policy-monitor

## Modlar

**Sweep modu:** Argüman yoksa veya `--sweep` geldiyse kayıtlı çıktıları tarar.

**Doğrudan sorgu modu:** Kullanıcı yeni bir faaliyet anlatırsa mevcut metinlerle karşılaştırır.

## Başlamadan

1. `~/.claude/plugins/config/claude-for-legal/privacy-legal/CLAUDE.md` dosyasını oku.
2. `## Aydınlatma / Politika Taahhütleri`, `## KVKK Çekirdek Kontrolleri`, `## Yurt Dışına Aktarım`, `## Çıktı Kuralları` bölümlerini yükle.
3. Gerçek gizlilik politikası, aydınlatma, açık rıza, çerez, İYS, VERBIS/envanter ve saklama-imha dokümanlarının yolunu kontrol et.
4. Profilde belge yolu yoksa doğrudan sorgu yapılabilir; sweep için kurulum eksikliği bulgu olarak yazılır.

## Amaç

KVKK uyumunda sorun çoğu zaman yeni ürünün hukuki analizi değil, eski metinlerin yeni uygulamayı artık doğru anlatmamasıdır. Bu skill, "metin ne söylüyor" ile "iş gerçekten ne yapıyor" arasındaki farkı yakalar.

## İzlenecek Yüzeyler

| Yüzey | Kontrol |
|---|---|
| Gizlilik politikası | Veri kategorisi, amaç, alıcı grubu, haklar, saklama, aktarım |
| Aydınlatma metni | KVKK m.10 kapsamı, sade/açık dil, hukuki sebep, alıcı, yöntem |
| Açık rıza metni | Aydınlatmadan ayrı mı, belirli konuya özgü mü, serbest irade var mı? |
| Çerez/CMP | Çerez kategorileri, amaç, zorunlu/analitik/pazarlama ayrımı, rıza yönetimi |
| İYS/ticari ileti | Ticari elektronik ileti izni ve ret/iptal mekanizması |
| VERBIS/envanter | Faaliyet, veri kategorisi, alıcı, saklama, aktarım kaydı |
| Saklama-imha | Yeni veri kategorisinin imha süresi ve yöntemi |
| Sektör metinleri | BDDK/SPK/BTK/TİTCK/sağlık/e-ticaret gibi özel bildirimler |
| App store / platform etiketleri | Mobil uygulama veri güvenliği beyanları ve mağaza etiketleri |

## Sweep Modu

1. Son sweep tarihinden sonraki çıktıları tara; tarih yoksa ilk sweep olarak tümünü tara.
2. Şu çıktılardan fiili uygulama çıkar:
   - `use-case-triage`: onaylanan faaliyet, koşullar, veri kategorileri,
   - `pia-generation`: VKED riskleri, alıcılar, aktarım, saklama,
   - `dpa-review`: tedarikçi/alt işleyen, veri lokasyonu, güvenlik, aktarım,
   - `dsar-response`: sistem listesine yeni giren veri kategorileri,
   - `reg-gap-analysis`: yeni doküman güncelleme yükümlülükleri.
3. Her çıktıyı yukarıdaki yüzeylerle karşılaştır.
4. Sweep tamamlanınca son sweep tarihini güncellemek için kullanıcı onayı iste.

## Doğrudan Sorgu Modu

Yeni faaliyet açıklamasından şunları çıkar:

- hangi veri kategorileri,
- hangi amaç,
- veri sahipleri,
- alıcı/tedarikçi/alt işleyen,
- yurt dışına aktarım,
- saklama süresi,
- açık rıza veya aydınlatma etkisi,
- çerez/İYS/app store/platform etkisi.

Belirsizse tek netleştirme sorusu sor.

## Gap Sınıfları

| Sınıf | Anlam |
|---|---|
| REQUIRED | Metin yanlış, eksik veya fiili işleme başlamadan güncellenmeli |
| ADVISABLE | Metin hukuken tolere edilebilir ama uygulama daha açık anlatılmalı |
| CONFLICT | Mevcut metin açıkça tersini söylüyor; faaliyet veya metin değişmeden ilerlenmemeli |
| NO ACTION | Mevcut metin ve envanter yeterli görünüyor |

## Çıktı

```markdown
GİZLİ HUKUKİ / KVKK ÇALIŞMA TASLAĞI - HUKUKÇU İNCELEMESİNE TABİDİR

Reviewer note
- Kaynaklar:
- Okuma kapsamı:
- Doğrulanması gerekenler:
- Aksiyon öncesi:

# Politika / Aydınlatma Uyum Kontrolü - [Sweep veya faaliyet]

**Mod:** sweep / doğrudan sorgu
**Tarih:** [YYYY-MM-DD]
**Taranan çıktılar:** [N]
**Bulgular:** [N] REQUIRED | [N] ADVISABLE | [N] CONFLICT

## REQUIRED / CONFLICT

### [Bulgu]

**Kaynak:** [çıktı veya faaliyet]
**Fiili uygulama:** [özet]
**Mevcut metin:** [alıntı veya "kapsamıyor"]
**Gap:** [eksik/çelişki]
**Önerilen aksiyon:** [doküman/süreç/sözleşme]
**Taslak metin:**
> [mevcut stile uygun kısa öneri]

## ADVISABLE

- [bulgu ve öneri]

## Uyumlu Alanlar

- [kontrol edildi, aksiyon yok]

## Sonraki Adımlar

- [ ] Politika/aydınlatma güncellemesini hukukçuya gönder
- [ ] VERBIS/envanter etkisini kontrol et
- [ ] DPA veya VKED gerekiyorsa ilgili skill'i çalıştır
- [ ] Canlıya çıkış öncesi onay al
```

## Yazım Standardı

- Gerçek dokümanın üslubunu oku; sadece profil özetine bakarak politika dili yazma.
- Çok geniş vaat verme: "asla paylaşmayız" gibi mimariyle kanıtlanamayan ifadelerden kaçın.
- Aydınlatma ve açık rıza metinlerini ayrı tut.
- Veri kategorisi, amaç, hukuki sebep ve alıcıyı sade ve açık yaz.

## Bu Skill Ne Yapmaz

- Politikayı kendiliğinden yayımlamaz.
- Regülasyon değişikliği takibi yapmaz; bunun için `reg-gap-analysis` kullanılır.
- E-posta/Slack gibi kayıt dışı kararları taramaz; yapılandırılmış çıktılara dayanır.
