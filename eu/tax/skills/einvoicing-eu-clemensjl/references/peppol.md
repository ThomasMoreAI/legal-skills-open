# Peppol

The network that most European e-invoicing rides on. Status as at 2026-08-05. Several load-bearing things changed in the last twelve months — read the migration section before writing any lookup code.

## What Peppol is and is not

Peppol is **a network plus a set of specifications plus a governance framework**. It is not a file format. "Peppol BIS Billing 3.0" is a CIUS of EN 16931; the network is separate from it and carries other document types too.

Four corners: **C1** the business sender → **C2** the sender's Access Point → **C3** the receiver's Access Point → **C4** the business receiver. C2 and C3 speak AS4 to each other; C1 and C4 speak whatever their provider offers. As a developer you build C1 or C4 and integrate a provider for C2 or C3.

## Current specification versions

Source: docs.peppol.eu/edelivery/ and peppol.org.

| Specification | Version | Note |
|---|---|---|
| Peppol BIS Billing 3.0 | **3.0.20** (November 2025 release), hotfix 2026-01-27, mandatory from 2026-02-23 | 3.0.21 mandatory **2026-08-17** |
| AS4 profile | **2.0.3**, valid from 2024-04-22 | |
| SMP specification | **1.4.0**, valid from 2025-11-01 | |
| SML specification | **1.3.0**, valid from 2025-11-01 | |
| Business Message Envelope (SBDH) | **2.0.2**, valid from 2026-07-02 | New parameters `MLS_TO`, `MLS_TYPE` |
| Policy for use of Identifiers (PFUOI) | **4.4.0**, valid from 2025-11-01 | Changed the DNS zone name algorithm |
| Peppol Network Policy | **1.0.0**, 2026-07-02 | New document; makes MLS mandatory |
| MLS (Message Level Status) | **1.1.0**, 2026-07-02 | |
| eDEC Code Lists | **v9.7**, 2026-07-02 | |
| PINT (base) | **1.1.2**, mandatory 2026-03-09; 1.1.3 mandatory 2026-09-07 | |

The release cadence is twice a year with a **mandatory-use date** a few months after publication. Pin the version, diary the mandatory date, and treat a bump as a code change with its own test run.

## Identifiers — the exact literal strings

Scheme identifiers (from the reference implementation `PeppolIdentifierHelper.java`, phax/peppol-commons):

```
iso6523-actorid-upis        participant identifier scheme
busdox-docid-qns            document type identifier scheme (exact match)
peppol-doctype-wildcard     document type identifier scheme (wildcard, since PFUOI 4.2.0)
cenbii-procid-ubl           process identifier scheme
```

Participant identifier: `<EAS code>:<value>`, e.g. `0088:7300010000001`. At transport level it is serialised as `iso6523-actorid-upis::0088:7300010000001`. Inside the invoice XML the EAS code goes in `schemeID` and the value in the element text (`identifiers.md`).

**Peppol BIS Billing 3.0 document type identifiers**, verbatim:

```
busdox-docid-qns::urn:oasis:names:specification:ubl:schema:xsd:Invoice-2::Invoice##urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0::2.1

busdox-docid-qns::urn:oasis:names:specification:ubl:schema:xsd:CreditNote-2::CreditNote##urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0::2.1
```

Structure: `<UBL namespace>::<root element>##<CustomizationID>::<UBL version>`.

**Process identifier** for both:

```
cenbii-procid-ubl::urn:fdc:peppol.eu:2017:poacc:billing:01:1.0
```

**Inside the invoice:**

```xml
<cbc:CustomizationID>urn:cen.eu:en16931:2017#compliant#urn:fdc:peppol.eu:2017:poacc:billing:3.0</cbc:CustomizationID>
<cbc:ProfileID>urn:fdc:peppol.eu:2017:poacc:billing:01:1.0</cbc:ProfileID>
```

**Transport profile identifier**: `peppol-transport-as4-v2_0`. It is the **only active** profile. `busdox-transport-start`, `busdox-transport-as2-ver1p0`, `busdox-transport-as2-ver2p0` and `peppol-transport-as4-v1_0` all carry `removal-date="2023-09-06"` in code list v9.7. AS2 is dead.

## SML/SMP lookup — the algorithm changed and the old one is gone

**Do not implement the MD5/CNAME algorithm.** The migration is complete.

Authoritative document: *Peppol CNAME to NAPTR Migration Process* v1.0.0, 2025-04-17.

```
LEGACY (dead):  "B-" + hexstring(md5(lowercase(ID-VALUE))) + "." + ID-SCHEME + "." + SML-ZONE
CURRENT:        strip-trailing(base32(sha256(lowercase(ID-VALUE))), "=") + "." + ID-SCHEME + "." + SML-ZONE
```

- Hash: **SHA-256**. Encoding: **Base32, RFC 4648 alphabet, `=` padding stripped, lowercased**.
- Only the **value** is hashed, never `scheme::value`. The value is lowercased first; the scheme is lowercased and appended as its own label.
- **No `B-` prefix** on the current form.
- U-NAPTR service name: **`Meta:SMP`**.
- Milestones: CNAME lookup **forbidden since 2025-11-01**; SMPs must be **https-only since 2026-02-01**. Legacy CNAME records now return NXDOMAIN, so an old client is broken, not merely non-compliant.

**The SML DNS zone moved.** OpenPeppol is insourcing the SML from the European Commission.

| Network | DNS zone |
|---|---|
| Production | `participant.sml.prod.tech.peppol.org.` |
| Test | `participant.sml.test.tech.peppol.org.` |
| Legacy production (deprecated) | `edelivery.tech.ec.europa.eu.` |
| Legacy test (deprecated) | `acc.edelivery.tech.ec.europa.eu.` |

As at 2026-08-05 the production OpenPeppol name is still a DNAME alias to the EC zone, so both resolve identically; the test zone is already fully insourced with its own SOA. **Access points must have switched the lookup domain by 2026-08-31**, with the production transfer in early September 2026. Use `participant.sml.prod.tech.peppol.org` now.

**SMP REST URLs.** Serialise the identifier as `scheme + "::" + value`, then percent-encode — `:` becomes `%3A`, `#` becomes `%23`.

```
{smpHost}/{participantId}
{smpHost}/{participantId}/services/{docTypeId}
```

**Worked example, verified live on the test network:**

```
participant   9915:test
DNS name      eh5boavaktmbgzyh2a63dz4qov33fvp5nsdvqklucfraayoodw6a
              .iso6523-actorid-upis.participant.sml.test.tech.peppol.org
NAPTR         100 10 U Meta:SMP !.*!https://test.erechnung.gv.at/smp! .
SMP           GET https://test.erechnung.gv.at/smp/iso6523-actorid-upis%3A%3A9915%3Atest
service       GET https://test.erechnung.gv.at/smp/iso6523-actorid-upis%3A%3A9915%3Atest
              /services/busdox-docid-qns%3A%3Aurn%3Aoasis%3Anames%3Aspecification%3Aubl
              %3Aschema%3Axsd%3AInvoice-2%3A%3AInvoice%23%23urn%3Acen.eu%3Aen16931%3A2017
              %23compliant%23urn%3Afdc%3Apeppol.eu%3A2017%3Apoacc%3Abilling%3A3.0%3A%3A2.1
result        transportProfile="peppol-transport-as4-v2_0"
              Address=https://test.erechnung.gv.at/as4
```

The `SignedServiceMetadata` response contains `ParticipantIdentifier`, `DocumentIdentifier`, `ProcessList/Process/ProcessIdentifier`, and per endpoint: `EndpointReference/Address`, `RequireBusinessLevelSignature`, `MinimumAuthenticationLevel`, `ServiceActivationDate`, `ServiceExpirationDate`, `Certificate` (base64 X.509 of the receiving access point), `ServiceDescription`, `TechnicalContactUrl`, `TechnicalInformationUrl`, plus an enveloped `ds:Signature`.

## Peppol Directory — discovery, not reachability

- Production `https://directory.peppol.eu`, test `https://test-directory.peppol.eu`
- `GET /search/1.0/{xml|json}` with `participant` (exact, scheme-qualified), `q`, `name`, `country`, `doctype`, `identifierScheme`, `identifierValue`, `resultPageIndex`, `resultPageCount`. Percent-encode `:` and `#`.
- **Rate limit 2 queries per second**; HTTP 429 above that. Maximum 1000 results.

Example: `GET https://directory.peppol.eu/search/1.0/json?participant=iso6523-actorid-upis%3A%3A9914%3Aatu72291619` returns `total-result-count`, and per match a `participantID`, a `docTypes` array and `entities` with name, country and registration date.

**Directory presence does not prove reachability.** The Directory is an opt-in business-card index and goes stale — participants listed there can return NXDOMAIN in the SML. For a real reachability check do the SML NAPTR lookup plus the SMP call. Use the Directory for search UX only.

## PINT, and the absence of a European migration date

**PINT is a template, not a usable invoice specification.** It is described as "a template for creating globally interoperable invoice specifications". The base PINT specification is `abstract="true"` and its placeholder CustomizationID `urn:peppol:pint:billing-1@specialization` is never a valid value in a document.

CustomizationID pattern: `urn:peppol:pint:{billing|selfbilling|nontaxinvoice}-1@{jurisdiction}-1`, e.g. `urn:peppol:pint:billing-1@jp-1`, `…@aunz-1`, `…@eu-1`, `…@sg-1`, `…@my-1`, `…@ae-1`, `…@om-1`, `…@ng-1`.

**A trap that breaks SMP code:** all active PINT document types use `scheme="peppol-doctype-wildcard"`, not `busdox-docid-qns`. The `busdox-docid-qns` PINT rows are `state="removed"`.

**There is no published migration date from BIS Billing 3.0 to PINT EU, and no "BIS Billing 4.0" exists in the identifier registry.** BIS Billing 3.0 carries no deprecation release and no removal date in code list v9.7; BIS 3.0.21 and EU PINT 1.1.1 both have future mandatory dates and are listed side by side. Build on BIS Billing 3.0 for Europe today and watch the code list.

## Peppol CTC and the five-corner model

Two OpenPeppol documents exist — a **Peppol CTC Reference Document** (first edition September 2021, addendum September 2023) and a **Peppol CTC Syntax Specification** defining *Document Cleared*, *Document Cleared Response*, *Document Reported* and *Document Reported Response*.

**The generic CTC syntax was never deployed.** Code list v9.7 registers no `Cleared` or `Reported` document types. What actually went live is per-jurisdiction **Tax Data Documents**:

```
urn:peppol:schema:taxdata:1.0::TaxData##urn:peppol:taxdata:ae-1::1.0        UAE
urn:peppol:schema:om-taxdata:1.0::TaxData##urn:peppol:taxdata:om-1::1.0     Oman
urn:peppol:schema:sk-taxdata:1.0::TaxData##urn:peppol:taxdata:sk-1::1.0     Slovakia
```

Who actually runs five corners: **Slovakia** (the clearest EU case, mandate 2027-01-01), **UAE**, **Oman**. Singapore is five-corner in substance but reports to IRAS outside a Peppol TDD. Malaysia allows Peppol as one option for the reporting leg. **Japan, Belgium and France are four-corner on Peppol** — France's e-reporting is a national construct. **Poland's KSeF is outside Peppol entirely.** At EU level the *Peppol ViDA Pilot* is a pilot, not a specification.

## Peppol Authorities

OpenPeppol, as Peppol Coordinating Authority, may delegate authority over implementation and use within a defined jurisdiction to a **Peppol Authority**. A PA issues **PASR** (Peppol Authority Specific Requirements) and **accredits Service Providers** in its jurisdiction. It does not control the SML, the PKI or the Interoperability Framework.

26 authorities as at 2026-08-05: Australia (ATO), Belgium (BOSA), Denmark (ERST), England (NHS SCCL), Finland (Valtiokonttori), France (DGFiP), Germany (KoSIT), Greece (GSIS), Iceland (FJS), Ireland (OGP), Italy (AgID), Japan (Digital Agency), Luxembourg (MDL), Malaysia (MDEC), Netherlands (NPa), New Zealand (MBIE), Nigeria (NRS), Norway (DFØ), Oman (Oman Tax Authority), Poland (MRiT), Portugal (eSPap), Singapore (IMDA), Slovakia (FR SR), Sweden (NAPP), Taiwan (MoDA), UAE (Ministry of Finance).

**Austria, Spain and Switzerland have no Peppol Authority** — OpenPeppol acts as PA there.

## How a developer actually connects

**You cannot send onto the network without a certified Peppol Service Provider.** OpenPeppol states it plainly: to send and receive through the network you need a service provider, not a membership. The gate is the closed PKI — the AS4 profile requires that certificates be verified on fetch from the SMP and that certificates not issued by OpenPeppol must not be used.

Terminology: the *agreement* was renamed to the **Peppol Service Provider Agreement**, but **"Access Point" is still current normative terminology** — membership categories are literally "Service Providers – Access Point and SMP", "Access Point only", "SMP only". Correct usage: **Peppol Service Provider** = the accredited legal entity; **Access Point** = the AS4 component at C2 or C3.

Accreditation path: OpenPeppol membership → sign the **Peppol Service Provider Agreement v4.0.2** (mandatory since 2025-05-28) with your Peppol Authority → verification → test certificates → pass the **Testbed** accreditation suite (testbed.peppol.org) → production certificate, valid 2 years.

Indicative cost for a small shop becoming an Access-Point-only Service Provider (OpenPeppol fee schedule, size band 1–10 people): roughly **1 050 EUR sign-up + 1 500 EUR certification + 1 850 EUR per year**. `[[UNVERIFIED: VAT treatment is not stated on the fee page]]`

Self-hosting the AS4 stack does not avoid any of this. **phase4** (Apache-2.0) and **Oxalis / Oxalis-NG** (LGPL-3.0) are on OpenPeppol's open-source list and save the AS4 and SBDH engineering — they do not supply a certificate.

**Providers a developer would realistically integrate:**

| Provider | Plain REST API | Positioning |
|---|---|---|
| Storecove | Yes — `api.storecove.com/api/v2/`, bearer token, `POST /document_submissions` | Self-serve, developer-first; Peppol plus DBNAlliance |
| Recommand | Yes — `POST /api/v1/{companyId}/send`, `/inbox`, `/verify` | Certified access point **and** SMP; low entry price |
| Qvalia | Yes — API or SFTP | Mid-market, fast onboarding |
| Avalara | Yes — one REST API plus ERP connectors | Enterprise multinational tax compliance |
| Tickstar | Advertised, spec not public | White-label AS4/SMP infrastructure for other service providers |
| Basware | Developer portal exists | Enterprise AP automation |
| ecosio | Not verified | EDI-as-a-service with ERP integration |
| B2Brouter | Not verified | SMB, self-serve |

Pagero now redirects into Thomson Reuters. Tradeshift is absent from OpenPeppol's software directory. Verify a provider's current status before committing.

## Diary these

- **2026-08-17** — Peppol BIS Billing 3.0.21 becomes mandatory
- **2026-08-31** — access points must have switched the SML lookup domain
- early **September 2026** — production SML transfer to OpenPeppol (short downtime expected)
- **2026-09-07** — PINT 1.1.3 and EU PINT 1.1.1 become mandatory
- Already past and worth checking you complied: **MLS became mandatory 2026-07-02** (every Service Provider must support sending and receiving Message Level Status; the default when `MLS_TYPE` is absent from the SBDH is `FAILURE_ONLY`); **all G2 PKI certificates were revoked on 2026-04-01** in the DigiCert ONE / PKI G3 migration; **all six XRechnung 2.0 document types were retired on 2026-08-01**; EAS **`0193` (UBL.BE)** has removal date **2026-07-07**, replaced by `0208`; `9954` (NL:OIN) was removed 2026-03-31.
- Other PFUOI 4.4.0 changes: participant and party identifier maximum length raised from 50 to 130 characters; SMPs must be https on port 443 only; the SMP root-path restriction was lifted.

## Checkpoints

- [ ] Lookup uses SHA-256 + Base32 NAPTR, not MD5 + CNAME
- [ ] SML zone is `participant.sml.prod.tech.peppol.org`, not the EC zone
- [ ] Identifiers serialised as `scheme::value` and percent-encoded in SMP URLs
- [ ] `busdox-docid-qns` used for BIS Billing, `peppol-doctype-wildcard` where PINT is involved
- [ ] Transport profile checked for `peppol-transport-as4-v2_0`; no AS2 code paths remain
- [ ] `cbc:CustomizationID` and `cbc:ProfileID` copied verbatim from the specification
- [ ] Reachability checked via SML + SMP, not via the Peppol Directory
- [ ] Directory queries rate-limited to 2/second
- [ ] Mandatory-use dates of the current BIS release diarised
- [ ] MLS supported if you operate as a Service Provider
- [ ] PKI G3 certificates in use
- [ ] Service provider contract in place, and the national Peppol Authority's PASR checked — noting that Austria, Spain and Switzerland have none
