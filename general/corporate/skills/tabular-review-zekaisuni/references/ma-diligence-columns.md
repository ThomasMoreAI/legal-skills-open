# M&A Due Diligence - Türkiye Standart Kolon Seti

Alıcı taraf hedef şirket sözleşme incelemesi için başlangıç şemasıdır. Bu bir kontrol listesi değil, tablo iskeletidir; nihai kolonları işlem belgeleri, veri odası talep listesi, SPA/APA beyanları ve hedef sektör belirler.

Yapısal veri standardı: `id` alanları ASCII `english_snake_case` kalır. Kullanıcıya görünen `label` ve `prompt` alanları Türkçe yazılır.

```yaml
schema:
  name: "M&A Due Diligence - Türkiye Standart"
  columns:
    - id: counterparty
      label: "Karşı Taraf"
      type: verbatim
      prompt: "Hedef şirket dışındaki sözleşme tarafının unvanını belgede geçtiği şekliyle yaz."

    - id: agreement_type
      label: "Sözleşme Türü"
      type: classify
      options: [msa, purchase_order, license_in, license_out, lease, services, supply, distribution, nda, joint_venture, loan, guarantee, employment, public_procurement, regulated_service, other]
      prompt: "Bu sözleşme hangi türde?"

    - id: effective_date
      label: "Yürürlük Tarihi"
      type: date
      prompt: "Sözleşme hangi tarihte yürürlüğe girmiş?"

    - id: term
      label: "Süre"
      type: duration
      prompt: "İlk sözleşme süresi nedir?"

    - id: auto_renewal
      label: "Otomatik Yenileme"
      type: classify
      options: [none, annual, fixed_period, indefinite, evergreen, unclear]
      prompt: "Sözleşme kendiliğinden yenileniyor mu? Hangi döngüyle?"

    - id: termination_for_convenience
      label: "Sebepsiz Fesih Hakkı"
      type: classify
      options: [none, either_party, target_only, counterparty_only, unclear]
      prompt: "Taraflardan biri haklı sebep olmadan feshedebilir mi?"

    - id: termination_notice
      label: "Fesih Bildirim Süresi ve Şekli"
      type: verbatim
      prompt: "Fesih bildirimi için süre ve yöntem nedir? KEP/noter/iade taahhüt/e-posta gibi şekil şartı var mı?"

    - id: change_of_control
      label: "Kontrol Değişikliği"
      type: classify
      options: [silent, consent_required, notice_only, termination_right, automatic_termination, unclear]
      prompt: "Hedef şirkette kontrol değişikliği halinde onay, bildirim, fesih veya otomatik sona erme düzenlenmiş mi?"

    - id: assignment
      label: "Devir / Temlik"
      type: classify
      options: [silent, consent_required, freely_assignable, group_company_allowed, non_assignable, unclear]
      prompt: "Sözleşmenin devri veya alacağın temliki sınırlanmış mı? TBK m.205 sözleşme devri kontrolü gerekli mi?"

    - id: exclusivity
      label: "Münhasırlık / Rekabet Kısıtı"
      type: classify
      options: [none, exclusive_supplier, exclusive_customer, non_compete, non_solicit, territory_restriction, most_favored_nation, unclear]
      prompt: "Taraflardan birinin rakiplerle, müşterilerle veya belirli bölgelerde çalışması kısıtlanıyor mu?"

    - id: liability_cap
      label: "Sorumluluk Sınırı"
      type: currency
      prompt: "Sorumluluk sınırı var mı? Tutar, çarpan veya istisnalar nelerdir?"

    - id: penalty_clause
      label: "Cezai Şart"
      type: currency
      prompt: "Cezai şart var mı? Tutar/formül ve TBK m.179-185 bakımından fahişlik veya birlikte talep riski var mı?"

    - id: indemnification
      label: "Tazmin / Garanti"
      type: classify
      options: [none, mutual, target_indemnifies, counterparty_indemnifies, ip_only, third_party_claims_only, guarantee_or_surety, unclear]
      prompt: "Kim kimi hangi zararlar için tazmin ediyor? Kefalet, garanti veya teminat niteliği doğuyor mu?"

    - id: stamp_tax
      label: "Damga Vergisi / Vergi Notu"
      type: classify
      options: [not_apparent, review_needed, paid_evidence_seen, exempt_claimed, unclear]
      prompt: "Damga vergisi (DVK/488), KDV/stopaj veya vergi-muhasebe incelemesi gerektiren yapı var mı?"

    - id: governing_law
      label: "Uygulanacak Hukuk"
      type: verbatim
      prompt: "Sözleşmeye hangi hukuk uygulanıyor?"

    - id: dispute_resolution
      label: "Uyuşmazlık Çözümü"
      type: classify
      options: [turkish_courts, enforcement_offices, istac, icc, other_arbitration, mediation_first, foreign_courts, silent, unclear]
      prompt: "Mahkeme, icra dairesi, tahkim, arabuluculuk veya yabancı forum düzenlemesi nedir?"

    - id: mandatory_mediation
      label: "Arabuluculuk Dava Şartı Notu"
      type: classify
      options: [likely_required, likely_not_required, contract_mediation_only, unclear]
      prompt: "Uyuşmazlık ticari/iş/tüketici/kira gibi dava şartı arabuluculuk alanına girebilir mi?"

    - id: minimum_commitments
      label: "Asgari Alım / Hacim Taahhüdü"
      type: currency
      prompt: "Asgari alım, hacim, ciro, kullanım veya harcama taahhüdü var mı?"

    - id: ip_ownership
      label: "Fikri Mülkiyet / FSEK"
      type: classify
      options: [each_owns_own, target_owns_outputs, counterparty_owns_outputs, joint, license_only, assignment, silent, unclear]
      prompt: "Sözleşme kapsamında doğan veya kullanılan fikri haklar kime ait? FSEK/SMK devri veya lisansı var mı?"

    - id: confidentiality_survival
      label: "Gizlilik ve Bakiye Hükümler"
      type: duration
      prompt: "Gizlilik ve diğer sona erme sonrası yükümlülükler ne kadar devam ediyor?"

    - id: personal_data
      label: "KVKK / Kişisel Veri"
      type: classify
      options: [none_apparent, controller_processor, joint_controller, cross_border_transfer, sensitive_data, dpa_needed, unclear]
      prompt: "Kişisel veri işleme, veri işleyen/veri sorumlusu rolü, yurt dışına aktarım veya özel nitelikli veri var mı?"

    - id: competition_sensitive_info
      label: "Rekabet Hassas Bilgi"
      type: classify
      options: [none_apparent, pricing, customer, cost, capacity, strategy, competitor_contact, unclear]
      prompt: "Rakipler arası veya rekabete hassas bilgi paylaşımı riski var mı?"

    - id: regulatory_approval
      label: "Regülatör / İzin"
      type: classify
      options: [none_apparent, rekabet, spk, bddk, tcmb, btk, epdk, titck, kik, ministry, municipality, other, unclear]
      prompt: "Sözleşme veya işlem için Rekabet Kurumu, SPK, BDDK, TCMB, BTK, EPDK, TİTCK, KİK veya başka izin/bildirim tetikleniyor mu?"

    - id: public_procurement
      label: "Kamu İhale / Kamu Sözleşmesi"
      type: classify
      options: [none_apparent, kik_contract, assignment_restricted, tender_document_needed, public_entity_counterparty, unclear]
      prompt: "Kamu ihalesi veya kamu kurumu sözleşmesi var mı? Devir yasağı, onay veya ihale dokümanı kontrolü gerekli mi?"

    - id: notices
      label: "Bildirim Adresi ve Yöntemi"
      type: verbatim
      prompt: "Hedef şirket için bildirim adresi, KEP, noter, iadeli taahhüt, portal veya e-posta yöntemi nedir?"

    - id: vdr_reference
      label: "VDR / Kaynak Referansı"
      type: verbatim
      prompt: "Belge veri odasında veya kaynak klasörde nerede?"
```

## İşlem türüne göre sık eklenen kolonlar

- **Teknoloji / IP yoğun hedefler:** kaynak kod emanet, açık kaynak kısıtları, veri kullanım hakkı, model eğitimi hakkı, API erişimi, FSEK/SMK devri.
- **Sağlık / ilaç / medikal:** TİTCK izinleri, klinik araştırma yükümlülükleri, ürün güvenliği, farmakovijilans, hasta verisi/KVKK.
- **Kamu ihalesi / kamu sözleşmeleri:** KİK ve 4735 sayılı Kamu İhale Sözleşmeleri Kanunu kontrolü, devir yasağı/onay, teminat mektubu, yasaklılık riski.
- **Gayrimenkul / kira:** kira süresi, uzama, tahliye, depozito, tapu/şerh, alt kira/devir, kira artış ve uyarlama.
- **Finansal / regüle hizmetler:** SPK, BDDK, TCMB, MASAK, MKK/KAP bildirimleri, sermaye/öz kaynak koşulları, müşteri varlığı ve gizlilik.
- **Telekom / enerji / altyapı:** BTK, EPDK, lisans/ruhsat, abonelik/dağıtım yükümlülükleri, kamu hizmeti sürekliliği.
- **Rekabet hassas işlemler:** Rekabet Kurumu izin/bildirim, clean team, hassas bilgi paylaşımı, münhasırlık ve rekabet etmeme.

## Hızlı ilk geçiş

Zaman baskısı varsa ilk 8 kolon çoğu erken M&A sorusunu cevaplar: `counterparty`, `agreement_type`, `effective_date`, `term`, `change_of_control`, `assignment`, `termination_for_convenience`, `regulatory_approval`. İşlem ekibi önceliklendirdikten sonra şemayı genişlet.
