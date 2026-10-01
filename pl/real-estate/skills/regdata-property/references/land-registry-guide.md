# Polish Land Registry (Ksiega Wieczysta) - Field-by-Field Interpretation Guide

This reference document explains every field you will encounter when reading structured data extracted from the Polish Electronic Land Registry (Elektroniczne Ksiegi Wieczyste, EKW). It is designed for lawyers, investors, and analysts who need to interpret raw registry data.

> **Note**: This guide explains how to read and interpret EKW data. To extract the data in structured form, use the `regdata/ekw-ksiegi-wieczyste-scraper` Apify actor via the `/regdata-property` skill.

---

## Dzial I-O: Property Designation (Oznaczenie nieruchomosci)

This section describes the physical and cadastral identity of the property. Data is sourced from the local land and buildings register (ewidencja gruntow i budynkow).

| Field | Polish Term | Description |
|---|---|---|
| Parcel number | Numer dzialki | Cadastral parcel identifier (e.g., "123/4"). Slash indicates subdivision. |
| Precinct | Obreb ewidencyjny | Cadastral precinct name or number. Together with gmina, uniquely identifies location. |
| Municipality | Gmina | Local administrative unit. |
| Area | Powierzchnia | Total area in hectares (ha). 1 ha = 10,000 m2. For apartments, this is the usable area. |
| Land use type | Sposob korzystania | Cadastral land classification code. See table below. |
| Building type | Typ budynku | If the KW covers a building: residential, commercial, industrial, etc. |
| Number of stories | Liczba kondygnacji | Number of floors in the building. |
| Premises number | Numer lokalu | For apartment KWs - the unit number within the building. |
| Associated land KW | KW gruntowa | For apartment KWs - the parent land registry number. |

### Land Use Classification Codes

| Code | Category | Description |
|---|---|---|
| B | Tereny mieszkaniowe | Residential land |
| Ba | Tereny przemyslowe | Industrial land |
| Bi | Inne tereny zabudowane | Other developed land |
| Bp | Zurbanizowane niezabudowane | Urbanized undeveloped land |
| R | Grunty orne | Arable farmland |
| S | Sady | Orchards |
| Ls | Lasy | Forest land |
| W | Wody | Water bodies |
| dr | Drogi | Roads |
| Tk | Tereny kolejowe | Railway land |
| K | Uzytek kopalniane | Mining land |
| N | Nieuzytki | Wasteland |

---

## Dzial I-Sp: Associated Rights (Spis praw zwiazanych z wlasnoscia)

This section lists rights that are legally tied to ownership of this property. It is especially important for apartments and properties with shared infrastructure.

| Field | Polish Term | Description |
|---|---|---|
| Share in common parts | Udzial w czesciach wspolnych | Fraction (e.g., "1/100") representing the owner's share in shared land and building parts. Critical for apartments. |
| Common property KW | KW wspolna | The KW number of the shared land/building that this unit is part of. |
| Easement in favor | Sluzebnosc na korzysc | An easement that benefits this property - e.g., right of way across a neighbor's land. |
| Perpetual usufruct | Prawo uzytkowania wieczystego | If the land is state/municipal-owned and held under perpetual usufruct. Time-limited (typically 99 years). |

**Key interpretation notes:**
- For apartments (lokal mieszkalny), Dzial I-Sp always contains the share in common parts. No share = potential legal defect.
- The share fraction affects voting rights in the housing community (wspolnota mieszkaniowa) and maintenance cost allocation.

---

## Dzial II: Ownership (Wlasnosc)

The most legally significant section. It establishes who has the right to dispose of the property.

| Field | Polish Term | Description |
|---|---|---|
| Owner name | Wlasciciel | Full name (individuals) or registered company name (legal entities). |
| PESEL | PESEL | 11-digit personal identifier for Polish citizens. |
| KRS number | Numer KRS | National Court Register number for companies. Use this to look up board members and beneficial owners. |
| REGON | REGON | Statistical identification number for legal entities. |
| NIP | NIP | Tax identification number. |
| Ownership share | Udzial | Fraction of ownership (e.g., "1/1" for sole owner, "1/2" for equal co-owners). |
| Type of right | Rodzaj prawa | "Wlasnosc" (full ownership) or "Uzytkowanie wieczyste" (perpetual usufruct). |
| Legal basis | Podstawa wpisu | Document that established the ownership - e.g., umowa sprzedazy (sale contract), postanowienie sadu (court order), akt poswiadczenia dziedziczenia (inheritance certificate). |
| Entry date | Data wpisu | When the ownership was registered. There can be a lag between the transaction date and the registry entry date. |

**Key interpretation notes:**
- If the owner is a company (sp. z o.o., S.A., etc.), cross-reference with KRS Board Members and CRBR Beneficial Owners to identify the humans behind the entity.
- "Wspolnosc ustawowa malzonska" means joint marital property - both spouses must consent to a sale.
- Check that the legal basis is a recognized transaction type. Unusual bases (e.g., "decyzja administracyjna") warrant further investigation.

---

## Dzial III: Rights, Restrictions, Encumbrances (Prawa, roszczenia, ograniczenia)

This section contains entries that limit the owner's rights over the property. It is the primary risk section in due diligence.

| Entry Type | Polish Term | Risk Level | Description |
|---|---|---|---|
| Ground easement | Sluzebnosc gruntowa | Medium | Right of another property's owner to use part of this property (e.g., right of way, drainage). |
| Personal easement | Sluzebnosc osobista | Medium | Right of a specific person to use the property (e.g., lifetime residence right). Cannot be sold. |
| Transmission easement | Sluzebnosc przesylu | Low-Medium | Right of a utility company to maintain infrastructure (pipes, cables, pylons) on the property. |
| Disposal restriction | Ograniczenie w rozporadzaniu | High | Court-ordered ban on selling or encumbering the property. Usually from enforcement proceedings. |
| Enforcement warning | Ostrzezenie o egzekucji | Critical | Notice that enforcement (komornik) proceedings have been initiated against the property. |
| Litigation warning | Ostrzezenie o postepowaniu | High | Notice that a court case affecting the property is pending. Ownership may be challenged. |
| Claim | Roszczenie | Medium-High | A registered claim against the property - e.g., right of first refusal, claim from a preliminary sale agreement. |
| Lease registration | Najem/Dzierzawa | Low-Medium | Registered lease that survives change of ownership. |
| Pre-emption right | Prawo pierwokupu | Medium | Someone has the right to purchase the property before any other buyer. |
| Administrative decision | Decyzja administracyjna | Variable | Entry from a government body - e.g., road planning, environmental protection zone. |

**Key interpretation notes:**
- Entries in Dzial III can block or delay a property transaction. Always review every active entry.
- "Ostrzezenie o wszczeniu egzekucji z nieruchomosci" is the most serious flag - it means a bailiff (komornik) is actively pursuing the property.
- Personal easements (especially "sluzebnosc mieszkania" - lifetime residence right) are difficult to remove and significantly reduce property value.

---

## Dzial IV: Mortgages (Hipoteki)

This section records all mortgage encumbrances. A property can have multiple mortgages from different creditors.

| Field | Polish Term | Description |
|---|---|---|
| Mortgage type | Rodzaj hipoteki | "Umowna" (contractual - from a loan) or "Przymusowa" (compulsory - from a court order or tax authority). |
| Amount | Suma hipoteki | The secured amount with currency (e.g., "500 000,00 PLN"). This is the maximum the creditor can claim from the property, not necessarily the remaining debt. |
| Creditor | Wierzyciel hipoteczny | Name of the mortgage holder - typically a bank, but can be a tax office (Urzad Skarbowy), ZUS, or a private entity. |
| Interest rate | Odsetki | Secured interest rate (if specified). Often "odsetki umowne" (contractual) or "odsetki ustawowe" (statutory). |
| Maturity/conditions | Termin/warunki | Repayment terms or conditions for mortgage release. |
| Basis | Podstawa wpisu | The document creating the mortgage - e.g., "Umowa kredytu z dnia..." (loan agreement dated...) or "Tyytul wykonawczy" (enforcement title). |

**Key interpretation notes:**
- "Hipoteka przymusowa" is a red flag - it means a creditor obtained a court order to secure their claim against the property without the owner's consent.
- Tax authority (Urzad Skarbowy) or social insurance (ZUS) as creditor indicates serious financial problems of the owner.
- The mortgage amount is the secured ceiling, not current debt. A 500,000 PLN mortgage may back a loan with only 200,000 PLN remaining.
- Multiple mortgages are ranked by registration date - the first registered has priority in case of foreclosure.

---

## Entry Status: Wpis vs. Wykreslenie

Every entry in the land registry has a status:

| Status | Polish Term | Meaning |
|---|---|---|
| Active entry | Wpis | Currently in force. Has legal effect. |
| Deleted entry | Wykreslenie | Struck from the register. No longer has legal effect. |
| Pending entry | Wzmianka | A new entry has been submitted but not yet processed by the court. Visible as a flag on the KW. |

**Important**: A "wzmianka" (pending entry) means that something is about to change in the KW. This is a critical signal during a property transaction - it could be a new mortgage, ownership transfer, or restriction being added. Always investigate pending entries before proceeding with a transaction.

---

## Historical vs. Current View

The land registry offers two views:

- **Tresc aktualna (Current content)** - shows only active (non-deleted) entries. This is the snapshot of the current legal state of the property. Use this for a quick status check.

- **Tresc zupelna (Full/historical content)** - shows all entries including deleted ones, with timestamps. This is the complete legal history of the property. Use this to:
  - Trace the chain of ownership over time
  - Understand why a mortgage was deleted (repaid? transferred? foreclosed?)
  - Identify patterns (rapid succession of owners, repeated enforcement entries)
  - Verify that a claimed deletion actually happened

For thorough due diligence, always request the full historical view (tresc zupelna).

---

## Court Department Codes

The first part of a KW number identifies the court department (wydzial ksiag wieczystych) that maintains the register. This tells you the geographic jurisdiction.

| Code Prefix | City / Region |
|---|---|
| WA | Warszawa (multiple districts: WA1M, WA2M, WA3M, WA4M, WA5M, WA6M) |
| WR | Wroclaw (WR1K = Wroclaw I, WR2K = Wroclaw-Krzyki) |
| KR | Krakow (KR1P = Krakow-Podgorze, KR2K = Krakow-Krowodrza) |
| PO | Poznan (PO1P = Poznan-Stare Miasto, PO2P = Poznan-Grunwald) |
| GD | Gdansk (GD1G = Gdansk I) |
| LO | Lodz (LO1M = Lodz-Srodmiescie) |
| KA | Katowice (KA1K = Katowice I) |
| SZ | Szczecin (SZ1S = Szczecin-Prawobrzeze) |
| LU | Lublin (LU1I = Lublin I) |
| BY | Bydgoszcz (BY1B = Bydgoszcz I) |
| OL | Olsztyn (OL1O = Olsztyn I) |
| RZ | Rzeszow (RZ1Z = Rzeszow I) |
| OP | Opole (OP1O = Opole I) |
| KI | Kielce (KI1L = Kielce I) |
| ZG | Zielona Gora (ZG1E = Zielona Gora I) |
| BI | Bialystok (BI1B = Bialystok I) |
| TO | Torun (TO1T = Torun I) |
| RA | Radom (RA1R = Radom I) |
| EL | Elblag (EL1E = Elblag I) |
| NS | Nowy Sacz (NS1S = Nowy Sacz I) |
| LE | Legnica (LE1L = Legnica I) |

The format is always: `PREFIX + DIGIT + LETTER(S)` / `NUMBER` / `CHECK_DIGIT`

Example: `WR1K/00094598/3` - maintained by Wroclaw I District Court (Wydzial Ksiag Wieczystych), entry number 94598, check digit 3.

---

## Common Abbreviations

| Abbreviation | Full Term | English |
|---|---|---|
| KW | Ksiega wieczysta | Land and mortgage register |
| EKW | Elektroniczne Ksiegi Wieczyste | Electronic land registry system |
| dz. | Dzialka | Land parcel |
| pow. | Powierzchnia | Area |
| wl. | Wlasnosc | Ownership |
| uzytk. wiecz. | Uzytkowanie wieczyste | Perpetual usufruct |
| hip. | Hipoteka | Mortgage |
| hip. um. | Hipoteka umowna | Contractual mortgage |
| hip. przym. | Hipoteka przymusowa | Compulsory mortgage |
| sluz. | Sluzebnosc | Easement |
| ostrz. | Ostrzezenie | Warning/caution |
| sp. z o.o. | Spolka z ograniczona odpowiedzialnoscia | Limited liability company |
| S.A. | Spolka akcyjna | Joint-stock company |
| KRS | Krajowy Rejestr Sadowy | National Court Register |
| CRBR | Centralny Rejestr Beneficjentow Rzeczywistych | Central Register of Beneficial Owners |
| PESEL | Powszechny Elektroniczny System Ewidencji Ludnosci | Universal Electronic Population Registry |
| NIP | Numer Identyfikacji Podatkowej | Tax identification number |
| REGON | Rejestr Gospodarki Narodowej | National Business Registry number |
