---
name: legal-impressum-eu
description: EU-wide Impressum requirements under eCommerce Directive 2000/31/EC. Country-by-country compliance matrix.
version: 1.0.0
triggers:
  - impressum eu
  - ecommerce directive
  - eu legal notice
  - european union imprint
---

# EU Impressum Requirements

> **Jurisdiction:** European Union (27 Member States)
> 
> **Related Skills:**
> - [SKILL.md](./SKILL.md) - Austrian requirements (main skill)
> - [SKILL-GERMANY.md](./SKILL-GERMANY.md) - German requirements
> - [SKILL-WORLD.md](./SKILL-WORLD.md) - International requirements

This skill covers EU-wide legal notice requirements based on the eCommerce Directive.

---

## 1. Legal Framework

### Primary EU Legislation

| Directive/Regulation | Article | Scope |
|---------------------|---------|-------|
| **eCommerce Directive 2000/31/EC** | Art. 5 | Information requirements |
| **Digital Services Act (DSA)** | Various | Platform transparency |
| **GDPR** | Art. 13-14 | Privacy notices |
| **Consumer Rights Directive 2011/83/EU** | Art. 6 | B2C online sales |
| **ODR Regulation 524/2013** (repealed by Reg. (EU) 2024/3228) | Art. 14 | Link obligation ended 2025-07-20 — remove legacy ODR links |
| **Services Directive 2006/123/EC** | Art. 22 | Service provider info |

### eCommerce Directive Art. 5 Requirements

All EU member states must ensure service providers make available:

| Field | Description |
|-------|-------------|
| Name | Full name or business name |
| Address | Geographic address (establishment) |
| Email | Electronic contact details |
| Trade register | Registration number if applicable |
| Regulatory authority | If subject to authorization |
| VAT ID | If VAT registered |
| Professional body | For regulated professions |
| Professional title | And member state where granted |
| Professional rules | Reference and means of access |
| Prices | Clear indication including taxes |

---

## 2. Country-by-Country Requirements

### Comparison Matrix

| Country | National Law | Key Differences |
|---------|--------------|-----------------|
| **Austria** | § 5 ECG | + MedienG Offenlegung for media |
| **Germany** | § 5 DDG | + MStV for journalistic content |
| **France** | LCEN Art. 6-III | + Publication director (directeur) |
| **Italy** | D.Lgs. 70/2003 Art. 7 | + Chamber of commerce registration |
| **Spain** | LSSI Art. 10 | + Geographic coordinates optional |
| **Netherlands** | Art. 3:15d BW | + Chamber of commerce number |
| **Belgium** | Art. XII.6 WER | + Enterprise number (BCE) |
| **Poland** | Art. 18 UŚUDE | + NIP and REGON numbers |
| **Sweden** | Lag 2002:562 | Relatively minimal requirements |
| **Ireland** | SI 68/2003 | + Company registration office |

### Detailed Country Notes

#### France (LCEN)

Additional requirements:
- **Directeur de publication** (publication director) - mandatory
- **Hébergeur** (hosting provider) contact details
- **Capital social** for companies

```
Mentions légales

Éditeur:
Exemple SARL
123 Rue de l'Exemple
75001 Paris

Directeur de la publication:
Jean Dupont

Hébergeur:
OVH SAS
2 rue Kellermann
59100 Roubaix
```

#### Italy

Additional requirements:
- **Codice fiscale** (tax code)
- **Partita IVA** (VAT number)
- **REA** number (chamber of commerce)
- **Capitale sociale** (share capital) + "i.v." or "n.i.v."

#### Netherlands

Additional requirements:
- **KvK-nummer** (Chamber of Commerce number)
- **BTW-nummer** (VAT number)

#### Belgium

Additional requirements:
- **Ondernemingsnummer/Numéro d'entreprise** (BCE/KBO number)
- **BTW/TVA nummer**

---

## 3. VAT Requirements

### When VAT ID is Required

| Scenario | VAT ID Required |
|----------|-----------------|
| Registered for VAT | Yes |
| Intra-EU B2B sales | Yes |
| B2C cross-border sales | Yes (if VAT registered) |
| Below VAT threshold, domestic only | Optional |

### One-Stop Shop (OSS)

For B2C cross-border digital services:
- Registration in one EU country
- Report and pay VAT for all EU sales
- Display VAT ID on website

---

## 4. ODR (Online Dispute Resolution) — Discontinued

### Status

The EU ODR platform was **discontinued on 2025-07-20**: Regulation (EU) 2024/3228 repealed Regulation (EU) 524/2013. The Art. 14 link obligation **no longer exists**.

### Required Action

1. **Remove** any legacy ODR link (https://ec.europa.eu/consumers/odr/) from Impressum, legal notice, and AGB/terms pages
2. Keeping the dead link is itself an Abmahnung (cease-and-desist) risk
3. Remove the former ODR template text from email footers and order confirmations

### Still Required (ADR)

The national alternative-dispute-resolution information duties under the ADR Directive 2013/11/EU remain in force (e.g. VSBG in Germany, AStG in Austria): B2C traders must still state whether they are willing or obliged to participate in dispute resolution proceedings before a consumer arbitration board.

---

## 5. Cross-Border Compliance

### Country of Origin Principle

Under eCommerce Directive Art. 3:
- Comply primarily with **your establishment country's** laws
- Target country can impose additional requirements in specific areas

### Multi-Country Strategy

For websites serving multiple EU countries:

1. **Minimum**: Comply with establishment country
2. **Recommended**: Cover strictest requirements (DE/AT)
3. **Best practice**: Country-specific legal notices

### Language Requirements

| Approach | Description |
|----------|-------------|
| Local language | Required in some countries (France, Spain) |
| English fallback | Acceptable for B2B, risky for B2C |
| Multi-language | Best for consumer-facing sites |

---

## 6. Sector-Specific Requirements

### Financial Services

- **MiFID II** disclosure requirements
- **PSD2** payment service provider info
- **IDD** insurance distribution info

### Healthcare

- Pharmacy registration
- Medical device CE marking
- Health professional registration

### Legal/Accounting

- Professional body membership
- Insurance details (often required)
- Jurisdiction of qualification

---

## 7. EU Template (Comprehensive)

```
LEGAL NOTICE / IMPRESSUM

Company Information:
[Company Name] [Legal Form]
[Street Address]
[Postal Code] [City]
[Country]

Contact:
Phone: [+XX XXX XXX XXX]
Email: [email@example.com]

Registration:
Commercial Register: [Court/Authority]
Registration Number: [Number]
VAT ID: [XXXXXXXXXXXX]

Representatives:
Managing Director(s): [Name(s)]

[For regulated professions:]
Professional Body: [Chamber/Association]
Professional Title: [Title, Member State of grant]
Professional Regulations: [Reference, access link]

[For media content:]
Responsible for Content: [Name, Address]
Editorial Direction: [Statement]

[For B2C — ADR information duty:]
Dispute Resolution:
We are [not] willing/obliged to participate in dispute resolution proceedings
before a consumer arbitration board. [Name/address of board if obliged]
(Do NOT include a link to the former EU ODR platform — it was discontinued on 2025-07-20.)

Privacy:
See our Privacy Policy: [Link]
```

---

## 8. Brexit Impact (UK)

Since January 2021:
- UK no longer under eCommerce Directive
- EU websites need separate UK compliance
- See [SKILL-WORLD.md](./SKILL-WORLD.md) for UK requirements

---

## 9. Compliance Checklist (EU-Wide)

### Minimum (Art. 5 eCommerce Directive)

- [ ] Business/owner name
- [ ] Geographic address
- [ ] Email address
- [ ] Trade/commercial register (if applicable)
- [ ] VAT ID (if applicable)
- [ ] Regulatory authority (if applicable)
- [ ] Professional body + rules (if regulated)

### B2C Online Sales (Additional)

- [ ] No legacy ODR platform link (platform discontinued 2025-07-20 — remove if present)
- [ ] ADR information (willingness/obligation to participate in consumer arbitration)
- [ ] Clear pricing including VAT
- [ ] Consumer rights information (withdrawal, etc.)

### GDPR (All)

- [ ] Privacy notice link
- [ ] Cookie consent mechanism

---

## 10. Resources

- **EUR-Lex (EU law)**: https://eur-lex.europa.eu/
- **Your Europe Business**: https://europa.eu/youreurope/business/
- **ECC-Net (Consumer disputes)**: https://ec.europa.eu/info/ecc-net

---

## Credits & Attribution

This skill is part of the webconsulting.at skills collection.

Sources: EUR-Lex, European Commission, national implementations
