---
name: legal-impressum-germany
description: German Impressum requirements under DDG and MStV. All Rechtsformen including GmbH, AG, UG, GbR, OHG, KG.
version: 1.0.0
triggers:
  - impressum germany
  - impressum deutschland
  - DDG
  - TMG
  - telemediengesetz
  - medienstaatsvertrag
---

# German Impressum Requirements

> **Jurisdiction:** Germany (Deutschland)
> 
> **Related Skills:**
> - [SKILL.md](./SKILL.md) - Austrian requirements (main skill)
> - [SKILL-EU.md](./SKILL-EU.md) - EU-wide requirements
> - [SKILL-WORLD.md](./SKILL-WORLD.md) - International requirements

This skill covers German Impressum (Anbieterkennzeichnung) requirements for websites and telemedien.

---

## 1. Legal Framework

| Law | Full Name | Scope | Effective |
|-----|-----------|-------|-----------|
| § 5 DDG | Digitale-Dienste-Gesetz | All commercial websites | May 2024 (replaced TMG) |
| § 18 MStV | Medienstaatsvertrag | Journalistic content | Nov 2020 |
| § 2 DL-InfoV | Dienstleistungs-Informationspflichten-VO | Service providers | 2010 |
| Art. 13-14 DSGVO | Datenschutz-Grundverordnung | Privacy notice | 2018 |
| § 5a UWG | Gesetz gegen unlauteren Wettbewerb | Fair competition | Various |

### Note: TMG Replaced by DDG

On 14 May 2024, the **Telemediengesetz (TMG)** was largely replaced by the **Digitale-Dienste-Gesetz (DDG)**; only the EU Digital Services Act (DSA) already applied from 17 February 2024. Impressum requirements are now in **§ 5 DDG**, which is nearly identical to the former § 5 TMG.

---

## 2. Required Fields (§ 5 DDG)

### 2.1 Mandatory for All Commercial Websites

| Field | German | Required |
|-------|--------|----------|
| Name | Vollständiger Name/Firma | ✓ |
| Legal form | Rechtsform | ✓ |
| Address | Ladungsfähige Anschrift | ✓ |
| Email | E-Mail-Adresse | ✓ |
| Phone or contact form | Telefon oder Kontaktformular | ✓ |
| Trade register | Handelsregister + HRB/HRA-Nr | ✓ if registered |
| VAT ID | Umsatzsteuer-ID (USt-IdNr.) | ✓ if applicable |
| Economic ID | Wirtschafts-ID | When introduced |
| Supervisory authority | Zuständige Aufsichtsbehörde | ✓ if regulated |
| Professional regulations | Berufsrechtliche Regelungen | ✓ if regulated profession |
| Share capital | Stammkapital/Grundkapital | ✓ for GmbH/AG |
| Liquidation status | "in Liquidation/Abwicklung" | ✓ if applicable |

### 2.2 Journalistic Content (§ 18 MStV)

Additional requirement for websites with journalistic-editorial content:

| Field | Description |
|-------|-------------|
| **Verantwortlicher** | Name and address of person responsible for journalistic content |

---

## 3. All German Rechtsformen

### 3.1 Quick Reference

| Company Type | Register | Capital Requirement | Special Notes |
|--------------|----------|---------------------|---------------|
| Einzelunternehmen | Optional (HR) | None | Owner name required |
| GbR | None | None | All partners listed |
| OHG | HR | None | All partners listed |
| KG | HR | None | Komplementäre listed |
| PartG / PartG mbB | PR | None | Professionals only |
| GmbH | HR | €25,000 | Stammkapital required |
| UG (haftungsbeschränkt) | HR | €1+ | Stammkapital required |
| GmbH & Co. KG | HR | Varies | Both entities listed |
| AG | HR | €50,000 | Grundkapital, Vorstand |
| SE | HR | €120,000 | European company |
| KGaA | HR | €50,000 | Hybrid form |
| eG (Genossenschaft) | GR | None | Vorstand listed |
| e.V. (Verein) | VR | None | Vorstand listed |

**Register abbreviations:**
- HR = Handelsregister (commercial register)
- PR = Partnerschaftsregister
- GR = Genossenschaftsregister
- VR = Vereinsregister

---

## 4. Templates by Rechtsform

### 4.1 Einzelunternehmen (Sole Proprietor)

```
IMPRESSUM

Angaben gemäß § 5 DDG

Max Mustermann
Musterstraße 1
10115 Berlin

Kontakt:
Telefon: +49 30 123456
E-Mail: info@mustermann.de

Umsatzsteuer-ID:
Umsatzsteuer-Identifikationsnummer gemäß § 27a UStG: DE123456789

Berufsbezeichnung und berufsrechtliche Regelungen:
[Falls zutreffend: Kammer, Berufsordnung, etc.]
```

### 4.2 GbR (Gesellschaft bürgerlichen Rechts)

```
IMPRESSUM

Angaben gemäß § 5 DDG

Mustermann & Partner GbR
Musterstraße 1
10115 Berlin

Vertreten durch die Gesellschafter:
Max Mustermann
Maria Musterfrau

Kontakt:
Telefon: +49 30 123456
E-Mail: info@mustermann-partner.de

Umsatzsteuer-ID:
DE123456789
```

### 4.3 GmbH

```
IMPRESSUM

Angaben gemäß § 5 DDG

Muster GmbH
Musterstraße 1
10115 Berlin

Vertreten durch die Geschäftsführung:
Max Mustermann

Kontakt:
Telefon: +49 30 123456
E-Mail: info@muster-gmbh.de

Registereintrag:
Eingetragen im Handelsregister
Registergericht: Amtsgericht Berlin-Charlottenburg
Registernummer: HRB 123456

Stammkapital: 25.000 EUR

Umsatzsteuer-ID:
DE123456789
```

### 4.4 UG (haftungsbeschränkt)

```
IMPRESSUM

Angaben gemäß § 5 DDG

Muster UG (haftungsbeschränkt)
Musterstraße 1
10115 Berlin

Vertreten durch die Geschäftsführung:
Max Mustermann

Kontakt:
Telefon: +49 30 123456
E-Mail: info@muster-ug.de

Registereintrag:
Eingetragen im Handelsregister
Registergericht: Amtsgericht Berlin-Charlottenburg
Registernummer: HRB 123456

Stammkapital: 1.000 EUR

Umsatzsteuer-ID:
DE123456789
```

### 4.5 GmbH & Co. KG

```
IMPRESSUM

Angaben gemäß § 5 DDG

Muster GmbH & Co. KG
Musterstraße 1
10115 Berlin

Persönlich haftende Gesellschafterin:
Muster Verwaltungs GmbH
Registergericht: Amtsgericht Berlin-Charlottenburg
Registernummer: HRB 654321
Geschäftsführer: Max Mustermann

Kommanditgesellschaft:
Registergericht: Amtsgericht Berlin-Charlottenburg
Registernummer: HRA 123456

Kontakt:
Telefon: +49 30 123456
E-Mail: info@muster-kg.de

Umsatzsteuer-ID:
DE123456789
```

### 4.6 AG (Aktiengesellschaft)

```
IMPRESSUM

Angaben gemäß § 5 DDG

Muster AG
Musterstraße 1
10115 Berlin

Vorstand:
Dr. Max Mustermann (Vorsitzender)
Maria Musterfrau

Aufsichtsratsvorsitzender:
Prof. Dr. Klaus Beispiel

Kontakt:
Telefon: +49 30 123456
E-Mail: info@muster-ag.de

Registereintrag:
Eingetragen im Handelsregister
Registergericht: Amtsgericht Berlin-Charlottenburg
Registernummer: HRB 123456

Grundkapital: 50.000 EUR

Umsatzsteuer-ID:
DE123456789
```

### 4.7 OHG (Offene Handelsgesellschaft)

```
IMPRESSUM

Angaben gemäß § 5 DDG

Mustermann OHG
Musterstraße 1
10115 Berlin

Gesellschafter:
Max Mustermann
Maria Musterfrau

Registereintrag:
Eingetragen im Handelsregister
Registergericht: Amtsgericht Berlin-Charlottenburg
Registernummer: HRA 123456

Kontakt:
Telefon: +49 30 123456
E-Mail: info@mustermann-ohg.de

Umsatzsteuer-ID:
DE123456789
```

### 4.8 KG (Kommanditgesellschaft)

```
IMPRESSUM

Angaben gemäß § 5 DDG

Mustermann KG
Musterstraße 1
10115 Berlin

Persönlich haftende Gesellschafter (Komplementäre):
Max Mustermann

Registereintrag:
Eingetragen im Handelsregister
Registergericht: Amtsgericht Berlin-Charlottenburg
Registernummer: HRA 123456

Kontakt:
Telefon: +49 30 123456
E-Mail: info@mustermann-kg.de

Umsatzsteuer-ID:
DE123456789
```

### 4.9 PartG mbB (Partnerschaftsgesellschaft)

```
IMPRESSUM

Angaben gemäß § 5 DDG

Mustermann & Partner Rechtsanwälte PartG mbB
Musterstraße 1
10115 Berlin

Partner:
RA Max Mustermann
RAin Maria Musterfrau

Registereintrag:
Eingetragen im Partnerschaftsregister
Registergericht: Amtsgericht Berlin-Charlottenburg
Registernummer: PR 123456

Berufsrechtliche Angaben:
Berufsbezeichnung: Rechtsanwalt/Rechtsanwältin
Zuständige Kammer: Rechtsanwaltskammer Berlin
Berufsrechtliche Regelungen: BRAO, BORA, FAO, RVG
(einsehbar unter: www.brak.de)

Berufshaftpflichtversicherung:
[Versicherungsname], [Geltungsbereich]

Kontakt:
Telefon: +49 30 123456
E-Mail: info@mustermann-partner.de

Umsatzsteuer-ID:
DE123456789
```

### 4.10 e.V. (Eingetragener Verein)

```
IMPRESSUM

Angaben gemäß § 5 DDG

Musterverein e.V.
Musterstraße 1
10115 Berlin

Vertreten durch den Vorstand:
Max Mustermann (1. Vorsitzender)
Maria Musterfrau (2. Vorsitzende)
Klaus Beispiel (Schatzmeister)

Registereintrag:
Eingetragen im Vereinsregister
Registergericht: Amtsgericht Berlin-Charlottenburg
Registernummer: VR 123456

Kontakt:
Telefon: +49 30 123456
E-Mail: info@musterverein.de
```

---

## 5. Journalistic Content (§ 18 MStV)

### When Required

Websites with journalistic-editorial content must name a **Verantwortlicher** (responsible person):

- News sites
- Blogs with opinion/commentary
- Online magazines
- Corporate blogs with editorial content

### Template Addition

```
Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV:
Max Mustermann
Musterstraße 1
10115 Berlin
```

---

## 6. Austria vs Germany Comparison

| Aspect | Austria | Germany |
|--------|---------|---------|
| Primary law | § 5 ECG | § 5 DDG |
| Commercial register | Firmenbuch | Handelsregister |
| Mini-GmbH | N/A | UG (haftungsbeschränkt) |
| Media disclosure | § 25 MedienG | § 18 MStV |
| Editorial direction | "Grundlegende Richtung" | "Verantwortlicher" |
| Regulated professions | Berufsrecht link | Berufsrechtliche Regelungen |

---

## 7. Penalties

| Violation | Penalty |
|-----------|---------|
| Missing/false Impressum | Up to €50,000 (Ordnungswidrigkeit) |
| Unfair competition (§ 5a UWG) | Abmahnung + damages |
| DSGVO violations | Up to €20M or 4% of turnover |

---

## 8. Compliance Checklist

- [ ] Full company/owner name
- [ ] Legal form (Rechtsform)
- [ ] Physical address (no P.O. Box)
- [ ] Email address
- [ ] Phone number or contact form
- [ ] Register + registration number (if applicable)
- [ ] VAT ID (USt-IdNr.) if applicable
- [ ] Share capital (GmbH, UG, AG)
- [ ] Representatives (Geschäftsführer, Vorstand)
- [ ] Supervisory authority (if regulated)
- [ ] Professional regulations (if regulated profession)
- [ ] Verantwortlicher (if journalistic content)
- [ ] Privacy notice link
- [ ] Cookie consent

---

## 9. Resources

- **IHK Impressum-Check**: Various regional IHK websites
- **BMJ Legal texts**: https://www.gesetze-im-internet.de/
- **DIHK Information**: https://www.dihk.de/

---

## Credits & Attribution

This skill is part of the webconsulting.at skills collection.

Sources: German Federal Ministry of Justice, IHK, official legal texts
