# Integrity Checks — `--integrity` (data-honesty layer)

Adds 4 cross-cutting integrity checks that run on top of the standard sections. Designed to surface **discrepancies, fabrications, and scam patterns** that single-section analysis misses.

These checks are **additive to** `shared/anti-hallucination.md`, not a replacement. Anti-hallucination prevents fabrication in our output; integrity checks scrutinize the *seller's* claims.

## When to run

- **Always** for foreign-buyer purchases (more vulnerable to scams)
- **Always** for off-plan / new build (developer claims need verification)
- **Always** for auction (no reps & warranties)
- **Recommended** for any property with €> normal-market premium
- **Optional** for low-value purchases where due-diligence cost > risk

Combine with: `/property-deep-dive <addr> --all --integrity`

## The 4 checks

| Check | What it does | Confidence boost |
|---|---|---|
| 1. **Dispute resolver** | When 2+ sources disagree, structured "both + gap explained" output | HIGH |
| 2. **Listing photo OCR** | Analyze listing pictures for hidden defects, missing rooms, suspicious cropping | MEDIUM |
| 3. **Listing-vs-cadastre cross-check** | Verify m², bedrooms, year, plot vs official cadastre | HIGH |
| 4. **Red-flag scanner** | Match property/listing/seller against known scam patterns | MEDIUM-HIGH |

---

## Check 1 — Dispute Resolver

**Trigger**: when sources disagree on a numeric or categorical claim.

### Common disputes

| Dispute | Source A | Source B | Resolution heuristic |
|---|---|---|---|
| Year built | Listing 1985 | Cadastre 1971 | **Trust cadastre** unless renovation date plausible |
| Surface m² | Listing 130 m² | Cadastre 112 m² | **Trust cadastre** unless extension permit on file |
| Bedrooms | Listing 4 | Cadastre 3 | **Investigate** — basement/attic conversion may be illegal |
| Plot size | Listing 1,200 m² | Cadastre 947 m² | **Trust cadastre** + check for adverse possession claims |
| Heating type | Listing "fioul" | Diagnostic "gaz + bois" | **Trust diagnostic** (DPE/EPC) — listing often outdated |
| Property class | Listing "DPE C" | Diagnostic register "DPE E" | **Trust register** — sellers often quote pre-renovation |
| Mains drains | Listing "raccordée" | Mairie / sewer plan | **Trust authority** — sellers self-declare |
| Property tax (annual) | Listing "€1,500" | Tax assessment | **Trust assessment** + check for partial year |
| Outstanding mortgage | Listing "free of debt" | KW / Tinglysning encumbrance | **Trust register** — listings exclude pending discharges |

### Output template

```markdown
### Dispute: <claim>

**Listing claims**: <X> (date: <date>, source: <listing URL>)
**Authority shows**: <Y> (date: <date>, source: <cadastre/registry URL>)
**Gap**: <difference + impact>
**Most likely truth**: <which to trust + why>
**Verification path**: <call mairie / order survey / request specific document>
**Impact on valuation**: €<X> if buyer accepts seller's claim
```

### Resolution rules

- **Government source > regulated registry > listing > forum**
- **Newer source > older source** (unless newer is from less authoritative source)
- **Specific source > general source** (cadastre > "around")
- **Independent source > seller-controlled source**
- **Multiple corroborating sources > single source**

When unresolvable: surface both, let buyer verify in person.

---

## Check 2 — Listing Photo OCR

**Trigger**: any listing with photos. Analyze visually + extract metadata.

### What to flag

#### Suspicious cropping

- **Always same angle** — no wide shots from different perspectives → hiding adjacent issue
- **Crop right at boundary** of feature → may hide damaged neighbor / unsightly element
- **No exterior wide shot** → may hide poor curb / bad neighbor
- **No bathroom photo** → may hide aged plumbing / leaks
- **No kitchen photo** → may hide poor appliances / hood
- **No roof photo from outside** → may hide aged tiles, sagging
- **No basement photo** (if mentioned) → may hide damp / water staining

#### Visual red flags

| Sign | What it suggests |
|---|---|
| Yellow stains on ceiling | Water leaks (current or past) |
| Crack patterns (>3mm wide, vertical or stair-step) | Structural movement |
| Mismatched paint sections | Recently patched issues |
| Wallpaper bubbling | Damp behind walls |
| Mold/black spots in corners | Ventilation / damp issue |
| Single-pane windows | Energy retrofit needed |
| Exposed pipes (with visible corrosion) | Plumbing replacement needed |
| Old fuse box / cloth wiring visible | Electrical re-wire needed |
| Missing radiators / unusual heating | Heating system issue |
| Damp creep on lower walls | Rising damp / no DPC |
| Concrete block walls visible | Pyrite/mica zones (IE Mayo/Donegal) |

#### EXIF / metadata

- **Photo date**: if older than 12 months and listing claims "recently renovated" → suspect
- **GPS coordinates**: if don't match listed address → red flag
- **Camera type**: agency stock photos (suspiciously perfect) vs phone photos (usually authentic)

#### Watermarks suggesting stale photos

- Old furniture style / decor
- Old TV (CRT visible) → photo > 20 years old
- Old appliance brand (e.g., 1990s-style refrigerator)
- VHS/DVD case
- Computer monitor (CRT) → 1990s-2000s photo

### Output template

```markdown
### Photo Analysis

**Photos analyzed**: <N>
**EXIF date range**: <oldest> to <newest>

#### Anomalies detected

1. **No exterior wide shot** — agency provided 12 interior photos, 0 exterior wide shots → request from agent
2. **Bathroom missing** — kitchen + 4 bedrooms shown; no bathroom or WC → likely dated/poor
3. **Yellow ceiling stain in living room photo (img 7)** → past or current water leak
4. **Crack visible in stair-step pattern (img 11)** → structural movement, request engineer's report
5. **Stale photos**: oldest EXIF July 2018 → may not reflect current condition

#### Verdict
- 🟢 **Clean** — no anomalies, photos comprehensive
- 🟡 **Probe** — 1-2 missing rooms / dated photos
- 🟠 **Concern** — multiple anomalies + visible defects
- 🔴 **Red flag** — significant defects visible OR significant rooms missing
```

---

## Check 3 — Listing-vs-Cadastre Cross-Check

**Trigger**: when both listing and cadastre records are accessible.

### Fields to verify

| Field | Listing source | Cadastre source | Tolerance |
|---|---|---|---|
| Surface m² | Listing | Cadastre / Land Registry | ±5% |
| Year built | Listing | Cadastre / building register | ±2 years |
| Plot m² | Listing | Cadastre | ±2% |
| Bedrooms | Listing | Building permit | exact |
| Building permit | (often missing) | Cadastre / commune | match |
| Property type | Listing | Cadastre | match |
| Building height / floors | Listing | Cadastre | exact |
| Outbuildings (garage, shed, pool) | Listing | Cadastre | match |
| Heritage / listed status | Often missing | National register | match |
| Easements (servitudes) | Often missing | Cadastre | match |
| Encumbrances (mortgage, lien) | Almost never | Land Register | should match (free of liens at completion) |

### Per-country cadastre URL templates

| Country | Cadastre lookup |
|---|---|
| 🇫🇷 | `https://www.cadastre.gouv.fr/scpc/accueil.do` (free, address lookup) |
| 🇮🇹 | `https://www.agenziaentrate.gov.it/` Visure catastali (paid) |
| 🇩🇪 | BORIS-D (Bodenrichtwerte) + ALKIS (per Bundesland, paid) |
| 🇪🇸 | `https://www.sedecatastro.gob.es/` (free) |
| 🇵🇹 | `https://www.portaldasfinancas.gov.pt/` Caderneta predial (free) |
| 🇨🇭 | `https://map.geo.admin.ch/` (free) |
| 🇸🇪 | `https://www.lantmateriet.se/` Min fastighet (BankID) |
| 🇫🇮 | `https://www.maanmittauslaitos.fi/en/e-services` |
| 🇳🇴 | `https://eiendomsregisteret.kartverket.no/` (free) |
| 🇩🇰 | `https://www.tinglysning.dk/` (free) |
| 🇮🇸 | `https://www.hms.is/` (free) |
| 🇸🇮 | `https://ipi.eprostor.gov.si/jv/` (free) |
| 🇮🇪 | `https://tailte.ie/` Land Registry / Registry of Deeds |
| 🇬🇧 | `https://search-property-information.service.gov.uk/` |
| 🇳🇱 | `https://www.kadaster.nl/` (€2.95 per inzage) |
| 🇧🇪 | `https://finances.belgium.be/fr/particuliers/habitation/cadastre` |
| 🇨🇿 | `https://nahlizenidokn.cuzk.cz/` (free) |
| 🇸🇰 | `https://www.katasterportal.sk/` (free) |
| 🇦🇹 | Grundbuch via `https://www.justiz.gv.at/home/service/grundbuch~36.de.html` (paid) |
| 🇬🇷 | `https://www.ktimatologio.gov.gr/` |
| 🇵🇱 | `https://ekw.ms.gov.pl/` (KW number; paid certified) |

### Output template

```markdown
### Listing vs Cadastre Cross-Check

**Listing source**: <URL>
**Cadastre source**: <URL>
**Reference date**: <date>

| Field | Listing | Cadastre | Match? | Impact |
|---|---|---|---|---|
| Surface m² | 130 | 112 | ❌ -14% | -€<X> at €/m² rate |
| Year built | 1985 | 1971 | ❌ -14yrs | DPE class likely worse |
| Bedrooms | 4 | 3 | ❌ +1 | "Bedroom" likely converted attic — may be illegal |
| Plot m² | 1,200 | 947 | ❌ -21% | Verify boundary in person + bornage |
| Heritage status | Not listed | "Bâtiment d'intérêt patrimonial" | ❌ | Restoration constraints apply |

#### Material discrepancies

1. **Surface inflation**: 130 vs 112 m² → if priced at €1,500/m², seller is over by €27,000
2. **Possible illegal extension**: 4 vs 3 bedrooms → request building permit ("permis de construire") for 4th
3. **Plot boundary**: -21% → request cadastral survey + pre-emption check

#### Verdict
- 🟢 **Aligned** — listing matches cadastre within tolerance
- 🟡 **Minor variance** — 1 field off, easily explained (recent extension, etc.)
- 🟠 **Material variance** — 2-3 fields off, affecting valuation by 5-10%
- 🔴 **Significant fraud risk** — multiple major discrepancies suggest deliberate misrepresentation
```

---

## Check 4 — Red-Flag Scanner

**Trigger**: every property analysis with `--integrity`.

### Pattern library

#### Fiscal red flags

- **Untaxed property** — no LPT/IBI/IMU/Grundsteuer paid in last 3 years → seller may have legal issues
- **Unregistered short-let** — property advertised on Airbnb but no AMA/CIN/AL registration → liability for buyer + future demolition / regularization risk
- **Cadastre value notably below market** — may indicate undeclared improvements (untaxed)
- **Seller paid notary in cash** → AML red flag
- **Discount for "quick sale" + "no questions"** → AML red flag
- **Foreign-currency listed price** → laundering vehicle

#### Title red flags

- **Different name on deed vs seller** — deceased + no probate? Power of attorney? Verify
- **Co-ownership not disclosed** (FR indivision, IT comunione) → all heirs must consent
- **Restrictions / easements not disclosed** — pre-emption right, right of way, servitude
- **Recent transfer** (within 2 years) — flipping at premium → investigate why
- **Multiple prior transfers** in short window → potentially flipping for laundering
- **Mortgage exceeding declared value** → seller underwater
- **Liens / litigation** on property → resolve at notary or walk
- **Heritage listing not disclosed** — seller may not know

#### Regulatory red flags

- **Building permit not on file** for visible additions → illegal construction (authairesia GR, izgradnja brez gradbenega dovoljenja SI)
- **Asbestos / lead / PCB diagnostic missing** for pre-1996/97 property → mandatory, seller liable
- **Septic compliance certificate missing** for rural → mandatory, expensive to remediate
- **DPE/EPC class missing** → mandatory, fine to seller
- **Pre-emption rights not addressed** — mairie / SAFER / kommune in some regimes can buy ahead

#### Behavioral red flags (seller / agent)

- **Pressure to sign without independent legal review**
- **Refuses to allow inspection by independent surveyor**
- **Refuses access to documents you've requested**
- **Multiple price reductions in short period** → may be desperate or property has issue
- **"Cash only" / "no mortgage"** → AML
- **Foreign agency operating without local license**
- **Pressure for off-record payments** ("for the seller, not on contract")
- **Delays / excuses about diagnostic reports**
- **Listing changes price upward suddenly** → fishing for naive foreign buyer

#### Off-plan / new build red flags

- **Developer has no completed projects** → first-timer risk
- **Developer recently incorporated** → shell company, may walk
- **Insurance / guarantee body absent** (FR garantie d'achèvement, DE Bauträgerinsolvenzversicherung)
- **Off-plan with non-refundable deposit > 5%** → red flag
- **Promised features not in sales contract** → not enforceable
- **Site progress not matching milestone payment**
- **Subcontractor disputes / liens visible at site**

### Output template

```markdown
### Red-Flag Scan

**Patterns checked**: 45 across fiscal / title / regulatory / behavioral / off-plan
**Red flags detected**: <N>
**Severity**: <🟢 / 🟡 / 🟠 / 🔴>

#### Detected flags

1. 🔴 **Untaxed property** — no LPT registered for 2024
   - Verification: contact Revenue.ie / municipal tax office
   - Risk: seller may have inheritance issue or unresolved transfer
   - Action: do not proceed without proof of paid LPT to date

2. 🟠 **Cadastre m² lower than listing** — 14% gap
   - Cross-reference with Check 3
   - Risk: paying for square meters not legally part of building
   - Action: request building permit for any extensions; deduct from offer

3. 🟡 **Listing price 8% below commune avg + DPE class A**
   - Listed €380k for 130m² in commune averaging €450k
   - DPE A is unusual for 1985 build — verify with DPE register
   - Risk: stale DPE / agent error / undisclosed issue
   - Action: verify DPE in national register; explain why below market

#### Recommended next steps

- Pull cadastre extract (free / paid)
- Pull tax assessment / arrears check (mairie / Schatzamt)
- Pull title certificate (KW outprint / Folio / Tinglysning)
- Independent surveyor visit
- Independent legal review (do NOT use seller's notary alone)

#### Verdict
- 🟢 **Clean** — no red flags
- 🟡 **Probe** — 1-2 minor flags, addressable via verification
- 🟠 **Multiple concerns** — 3+ flags, valuation impact + buyer-side legal review essential
- 🔴 **Stop & reassess** — fraud / structural issue / regulatory risk that may make property unbuyable
```

---

## How to invoke

```
/property-deep-dive <addr> --all --integrity
/property-deep-dive <addr> --integrity   # integrity-only run, fast
/property-deep-dive <addr> --integrity=cross-check,red-flags  # specific checks
```

## Output structure

When `--integrity` is requested, output adds an "## Integrity Audit" section at the top with all 4 checks summarized, plus inline annotations in relevant sections.

## Confidence labels

- **HIGH**: Cadastre + diagnostic register + listing all accessible; cross-checks complete
- **MEDIUM**: Listing only / cadastre only / one source missing
- **LOW**: Cannot verify (closed jurisdiction, pre-cadastre area)

## Forbidden hallucinations

- Never invent a discrepancy if data not accessed
- Never accuse seller of fraud — say "discrepancy" + "verify"
- Never claim "X is illegal" without citing law
- Always provide verification path — actionable next step
- Surface uncertainty: "potentially illegal extension" not "illegal extension"

## Legal disclaimer (mandatory in output)

```
⚠️ This integrity check surfaces patterns and discrepancies. It is not legal advice. 
Engage a local notary/solicitor for binding analysis. 
Allegations of fraud require formal investigation by competent authorities.
```
