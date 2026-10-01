# Registrierkassenpflicht and the RKSV signature chain

Basis: § 131b BAO, § 132a Abs 8 BAO, § 131 Abs 4 BAO, Registrierkassensicherheitsverordnung (RKSV, BGBl. II Nr. 410/2015, last amended by BGBl. II Nr. 134/2026), Barumsatzverordnung 2015 (BarUV 2015, BGBl. II Nr. 247/2015, last amended by BGBl. II Nr. 321/2025). All consolidated versions as at 2026-08-05 (RIS). Status as at 2026-08-05.

This construction has no German or Swiss equivalent. A German TSE under the KassenSichV is not a substitute: the Austrian device is a qualified signature or seal creation unit under eIDAS, the chain format is JSON Web Signature, and the device must be registered in FinanzOnline.

## When the obligation bites

> "Die Verpflichtung zur Verwendung eines elektronischen Aufzeichnungssystems … besteht ab einem **Jahresumsatz von 15 000 Euro je Betrieb**, sofern die **Barumsätze dieses Betriebes 7 500 Euro** im Jahr überschreiten." — § 131b Abs 1 Z 2 BAO

Both thresholds must be met, and they are measured **per Betrieb**, not per legal entity.

**Barumsatz is wider than cash** (§ 131b Abs 1 Z 3 BAO): payment by Bankomat- or Kreditkarte, other comparable electronic payment forms, Barschecks, and vouchers, bons or gift tokens issued by the Unternehmer and accepted by them in lieu of money all count. A card-only counter is inside the regime.

**Start and end** (§ 131b Abs 3 BAO):

- the duty starts with the beginning of the **fourth month following** the end of the Voranmeldungszeitraum in which the thresholds were first exceeded
- it falls away from the beginning of the next calendar year if the thresholds are not exceeded in a following year **and** particular circumstances make it foreseeable that they will not be exceeded in future

Credit institutions under § 1 Abs 1 BWG and branches of CRR credit institutions under § 9 BWG are outside §§ 131b and 132a entirely (§ 132b BAO).

## Exemptions

Under § 131 Abs 4 BAO the BMF may grant relief, and the BarUV 2015 does so. § 1 Abs 4 BarUV: where simplified turnover determination under §§ 2 to 4 is permitted, **neither the Registrierkassenpflicht under § 131b BAO nor the Belegerteilungspflicht under § 132a BAO applies**.

| Exemption | Limit | Basis |
|---|---|---|
| "Kalte-Hände-Regelung" — supplies door to door, or on public ways, streets, squares or other public places, but not in or in connection with firmly enclosed premises | **45 000 € per calendar year and taxpayer** | § 131 Abs 4 Z 1 lit a BAO, version BGBl. I Nr. 97/2025, **in force since 2026-01-01** (§ 323 Abs 87 BAO). The earlier figure of 30 000 € is obsolete |
| Supplies in immediate connection with Hütten (Alm-, Berg-, Schi-, Schutzhütten) | same 45 000 € | § 131 Abs 4 Z 1 lit b BAO |
| Buschenschank open no more than 14 days per calendar year | same 45 000 € | § 131 Abs 4 Z 1 lit c BAO |
| Canteen run by a non-profit association, operated no more than 52 days per calendar year ("kleine Kantine") | same 45 000 € | § 131 Abs 4 Z 1 lit d BAO |
| Wirtschaftliche Geschäftsbetriebe of tax-privileged bodies under § 45 Abs 1, 1a and 2 BAO | — | § 131 Abs 4 Z 2 BAO, § 3 BarUV |
| Vending and service machines put into operation after 2015-12-31 where the consideration per single transaction does not exceed **20 €** | 20 € per transaction | § 4 BarUV. For machines in operation before 2016-01-01 this takes effect on **2027-01-01** (§ 9 Abs 2 BarUV) |
| Ticket machines for passenger transport put into operation after 2015-12-31, where complete capture of the tickets is assured | — | § 5 BarUV |
| **Online shops** — turnover where no cash is paid directly to the supplier and the agreement was concluded through an online platform | — | § 6 BarUV. Note: exempt from § 131b only; the § 132a Beleg duty is expressly unaffected by § 131 Abs 4 Z 4 BAO |
| Supplies made **away from the business premises** | — | § 7 BarUV: entry in the Registrierkasse may wait until return to the premises, **but a § 132a Abs 3 Beleg must be handed over at the time of cash payment** and a duplicate kept. Does not apply to taxi and Mietwagen passenger transport (§ 7 Abs 2) |

If the threshold in a lit a or lit b case is exceeded, the duties start with the beginning of the fourth month following the end of the Voranmeldungszeitraum in which the limit was first exceeded (§ 2 Abs 2 BarUV).

## What the system must be

Requirements on the Registrierkasse, § 5 RKSV:

- a **Datenerfassungsprotokoll** (DEP) and a printer or a facility for electronic transmission of payment receipts (Abs 1)
- a suitable interface to a **Signatur- bzw. Siegelerstellungseinheit**; one unit may serve several Registrierkassen (Abs 2)
- **AES-256** available for the encryptions required by the machine-readable code (Abs 3)
- a **Kassenidentifikationsnummer** unique within the undertaking (Abs 4)
- no facility permitting the security device to be bypassed (Abs 5)
- shared use by several Unternehmer only where each uses their own certificate and the machine keeps a **separate DEP per Unternehmer** (Abs 6)

## The signature chain

§ 131b Abs 2 BAO requires unalterability through cryptographic signature or seal of **each** Barumsatz, and verifiability through the signature being carried on the individual receipt. § 4 RKSV: the security device consists of the **chaining of Barumsätze** — elements of the previously issued, DEP-stored signature enter the signature currently being created. For the first Barumsatz the **Kassenidentifikationsnummer** takes the place of the previous signature.

Data entering the signature, § 9 Abs 2 RKSV, in this order:

1. Kassenidentifikationsnummer
2. sequential number of the Barumsatz
3. date and time of receipt issue
4. amount paid, **split by the § 10 UStG rates**
5. state of the Umsatzzähler, encrypted with AES-256 (Anlage Z 8 and Z 9)
6. serial number of the signature/seal certificate
7. signature/seal value of the previous Barumsatz in the DEP (Verkettungswert, Anlage Z 4)

Signature algorithms and keys must correspond to qualified signature or seal creation units under the eIDAS Regulation.

**Everything is signed**, not just sales: each individual Barumsatz plus the Monats-, Jahres- and Schlussbeleg, plus every Trainings- and Stornobuchung (§ 9 Abs 1 RKSV).

### The JSON payload — RKSV Anlage Z 4

Field names, exactly as the Anlage defines them:

| Field | Content | JSON type |
|---|---|---|
| `Kassen-ID` | § 9 Abs 2 Z 1 | string, UTF-8 |
| `Belegnummer` | § 9 Abs 2 Z 2 | string, UTF-8 |
| `Beleg-Datum-Uhrzeit` | ISO 8601 **without time zone**, `JJJJ-MM-TT'T'hh:mm:ss`, e.g. `2015-07-21T14:23:34`; Austrian local time is always assumed | string, UTF-8 |
| `Betrag-Satz-Normal` | 20 % bucket, `0,00` if none | number, 2 decimals |
| `Betrag-Satz-Ermaessigt-1` | reduced bucket 1, `0,00` if none | number, 2 decimals |
| `Betrag-Satz-Ermaessigt-2` | reduced bucket 2, `0,00` if none | number, 2 decimals |
| `Betrag-Satz-Null` | zero-rated bucket, `0,00` if none | number, 2 decimals |
| `Betrag-Satz-Besonders` | labelled **"(19 %, 4,9 %)"** in the Anlage as amended by BGBl. II Nr. 134/2026, in force 2026-07-01 | number, 2 decimals |
| `Stand-Umsatz-Zaehler-AES256-ICM` | BASE64 of the AES-256-ICM encrypted turnover counter | string |
| `Zertifikat-Seriennummer` | certificate serial | string, UTF-8 |
| `Sig-Voriger-Beleg` | BASE64 of N bytes taken from the hash of the previous receipt's JWS result; for the first Barumsatz the hash input is the `Kassen-ID` | string |

The signing payload (Anlage Z 5) is those fields **in § 9 Abs 2 Z 1 to Z 7 order, UTF-8 encoded, joined with `_`**, prefixed with `_RKA_` where `RKA` is the Registrierkassenalgorithmuskennzeichen:

```text
_R1-AT1_Wert(Kassen-ID)_Wert(Belegnummer)_Wert(Beleg-Datum-Uhrzeit)_Wert(Betrag-Satz-Normal)_Wert(Betrag-Satz-Ermaessigt-1)_Wert(Betrag-Satz-Ermaessigt-2)_Wert(Betrag-Satz-Null)_Wert(Betrag-Satz-Besonders)_Wert(Stand-Umsatz-Zaehler-AES256-ICM)_Wert(Zertifikat-Seriennummer)_Wert(Sig-Voriger-Beleg)
```

The Registrierkassenalgorithmuskennzeichen has the form `RN-CM` (Anlage Z 2): fixed prefix `R`, algorithm-suite index `N`, separator `-`, country code `C` of the trust service provider, provider index `M`. For `R1-CM`: signature/hash algorithm **ES256** per the JWA standard; chaining hash **SHA-256** with **N = 8** extracted bytes; a closed system under § 20 RKSV must state `AT0` as the provider.

The signing result (Anlage Z 6) is the **JWS compact serialisation**: three BASE64-URL elements joined by `.` — protected header, payload, signature value.

### Failure of the signature unit

§ 17 Abs 4 RKSV and Anlage Z 6: if no signature can be created, the third JWS element is replaced by the UTF-8 string `Sicherheitseinrichtung ausgefallen`, BASE64-URL encoded. The note `Sicherheitseinrichtung ausgefallen` must additionally appear **visibly on the receipt**. After the unit is back, a signed **Sammelbeleg with amount zero** covering the affected receipts must be created and stored in the DEP. Any non-temporary failure or decommissioning must be reported through FinanzOnline without unnecessary delay, with the affected component, the reason, and the start (§ 17 Abs 1 and 2); the end of the failure is likewise reported (§ 17 Abs 6).

If the Registrierkasse itself fails, Barumsätze go to another Registrierkasse; failing that they are recorded manually with duplicates kept, and re-entered afterwards (§ 17 Abs 5).

## The machine-readable code on the receipt

§ 10 Abs 2 RKSV — the code contains the same items 1 to 7 as the signature, **plus** item 8, the signature/seal value of the Barumsatz itself. Training and cancellation bookings additionally carry the words `Trainingsbuchung` or `Stornobuchung` in the code (§ 10 Abs 3).

Preparation, Anlage Z 12: the string is the **signed receipt data** (the JWS payload, extractable from the compact representation) and the **signature value in standard BASE64** — note the re-encoding step: the JWS compact form is BASE64-**URL**, which contains `_`, and `_` is the field separator, so it must be decoded and re-encoded as standard BASE64 — joined with `_`, UTF-8 encoded.

§ 11 Abs 1 RKSV — the receipt shows, **in addition to** the § 132a Abs 3 BAO data: Kassenidentifikationsnummer, date and time of issue, amount split by rate, and the content of the machine-readable code. § 11 Abs 3: training and cancellation receipts must be expressly labelled as such.

§ 11 Abs 2 RKSV — where a QR code cannot be printed, the data are instead made available as a **link dependent on the signature value, in machine-readable form as barcode or OCR**, or printed per the **OCR encoding of Anlage Z 14**. The OCR variant re-encodes `Signatur- bzw. Siegelwert`, `Sig-Voriger-Beleg` and `Stand-Umsatz-Zaehler-AES256-ICM` from BASE64 to **BASE32** and prints them in the **OCR-A** font.

## DEP, Umsatzzähler, and the periodic receipts

**Datenerfassungsprotokoll**, § 7 RKSV:

- every individual Barumsatz is captured and stored, with at least the § 132a Abs 3 BAO receipt data (Abs 1)
- **Trainings- and Stornobuchungen are recorded like Barumsätze** (Abs 2)
- the DEP data must be backed up **at least quarterly to external electronic media, unalterably**, and that backup is retained under § 132 BAO (Abs 3)
- the contents of the machine-readable code are stored in the DEP together with the corresponding Barumsatz (Abs 4)
- the DEP must be **exportable at any time to an external data carrier in the export format of Anlage Z 3** (Abs 5)

**Export format**, Anlage Z 3 — a JSON structure with a `Belege-Gruppe` array, one element per signing certificate, each containing the BASE64/DER certificate, the certificate-authority chain, and `Belege-kompakt`, an array of the signed receipts in **JWS compact form, in DEP storage order**, with the chaining from position *x* to *x+1* guaranteed.

**Umsatzzähler**, § 8 RKSV:

- Barumsätze captured in the Registrierkasse are continuously summed. **Trainingsbuchungen must not affect the counter** (Abs 1)
- at each month end the intermediate counter state is determined and stored in the DEP as a **Monatsbeleg** — a Barumsatz with amount zero, signed (Abs 2)
- at the end of each calendar year the Monatsbeleg carrying the year-end counter state is the **Jahresbeleg**; it must be **printed, checked, and retained under § 132 BAO** (Abs 3), with § 6 Abs 4 applying analogously to the check

The Jahresbeleg is the December Monatsbeleg. Practice deadline: create it by 31 December, and complete the check or transmission to the BMF **by 15 February of the following year** (WKO, "Prüfung Jahresbeleg Registrierkasse").

**Startbeleg**, § 6 RKSV: putting the security device into operation consists of setting up the DEP and storing the Kassenidentifikationsnummer as part of the data to be signed for the **first Barumsatz with amount zero** — the Startbeleg. Registration under § 16 must follow **within one week** of putting the device into operation (Abs 3). Immediately after registration the creation of the signature and the encryption of the Umsatzzähler must be **verified using the Startbeleg**; if either does not meet § 9, the Registrierkasse is immediately treated as one with a failed signature unit under § 17 Abs 4. **The result of the check is protocolled and retained with the Startbeleg** under § 132 BAO (Abs 4).

**Schlussbeleg**, § 17 Abs 8 RKSV: on planned decommissioning of the Registrierkasse a Schlussbeleg with amount zero is created, printed and retained under § 132 BAO.

## Procurement and registration

**Procurement**, § 15 RKSV: the signature/seal creation units are bought from a trust service provider (VDA) established in the EU/EEA or Switzerland, or recognised under Art 14 eIDAS, offering qualified certificates. The Unternehmer must have an **Ordnungsbegriff known to the tax authority** entered in the certificate together with the OID value "Österreichische Finanzverwaltung Registrierkasseninhaber". That OID is **`1.2.40.0.10.1.11.1`** (Anlage Z 16). Costs are borne by the Unternehmer.

**Registration**, § 16 RKSV — through **FinanzOnline**, reporting per signature/seal creation unit:

- the **serial number of the signature/seal certificate**
- the **type** of the unit
- the **Kassenidentifikationsnummern** of the Registrierkassen to be connected to it
- the freely chosen **Benutzerschlüssel** (AES-256 key, BASE64-encoded per Anlage Z 8) for decrypting the encrypted data in the machine-readable code

Only after FinanzOnline has verified that the VDA appears in the public trust list and the certificate exists in the VDA directory are the data passed to the BMF database of security devices (§ 16 Abs 2, § 18 RKSV).

## Verification — Belegcheck

The BMF publishes a **Belegcheck** app (bundle identifier `at.gv.bmf.belegcheck`, listed under bmf.gv.at/services/apps.html) that scans the QR code on a receipt and verifies it against FinanzOnline. It is used for the mandatory check of the **Startbeleg** and of the **Jahresbeleg**. An **Authentifizierungscode** obtained from FinanzOnline after registering the Registrierkasse and the signature unit is required. Automated submission through the cash register web service is the alternative to the manual app check.

## Checkpoints

- [ ] Both thresholds implemented per Betrieb: 15 000 € annual turnover **and** 7 500 € Barumsätze
- [ ] Card, contactless and vendor vouchers counted as Barumsatz
- [ ] Obligation start computed as the fourth month after the Voranmeldungszeitraum of first breach
- [ ] Exemption evaluation uses **45 000 €**, not 30 000 €, for the § 131 Abs 4 Z 1 cases
- [ ] Unique Kassenidentifikationsnummer per Registrierkasse within the undertaking
- [ ] Separate DEP and separate certificate per Unternehmer in shared-terminal setups
- [ ] Signature payload assembled in § 9 Abs 2 Z 1–7 order, joined with `_`, prefixed `_RKA_`
- [ ] All five amount buckets present, including `Betrag-Satz-Besonders` for 19 % and 4,9 %
- [ ] `Beleg-Datum-Uhrzeit` written as ISO 8601 without time zone, Austrian local time
- [ ] Chaining value derived from the previous receipt's JWS result; Kassen-ID used for the first
- [ ] Concurrency control guarantees correct chaining under parallel receipt creation (Anlage Z 4 and Z 11 require this explicitly)
- [ ] Trainingsbuchungen excluded from the Umsatzzähler; Storno- and Trainingsbelege signed and labelled
- [ ] Machine-readable code carries items 1–8 including the receipt's own signature value
- [ ] Signature value re-encoded from BASE64-URL to standard BASE64 before assembling the QR string
- [ ] OCR fallback uses BASE32 and the OCR-A font where a QR code cannot be printed
- [ ] Startbeleg created, registered within one week, verified, and the check result protocolled and retained
- [ ] Monatsbeleg generated at every month end as a signed zero-amount Barumsatz
- [ ] Jahresbeleg printed, checked and retained; check completed by 15 February of the following year
- [ ] Schlussbeleg produced on planned decommissioning
- [ ] DEP backed up at least quarterly to external media, unalterably, and retained
- [ ] DEP export to Anlage Z 3 JSON works on demand and preserves storage order and chaining
- [ ] Signature-unit failure path writes `Sicherheitseinrichtung ausgefallen` into the JWS third element **and** onto the receipt, and produces the Sammelbeleg on recovery
- [ ] FinanzOnline registration data complete: certificate serial, unit type, Kassen-IDs, AES Benutzerschlüssel
- [ ] Certificate carries the Ordnungsbegriff and OID `1.2.40.0.10.1.11.1`
