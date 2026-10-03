# IP Infringement Playbook

---
practice_area: ip-infringement
triggers:
  filenames: [patent, trademark, copyright, prior-art, IDS, IPR, PGR, Markman, claim-chart, claim-construction, accused-product, prosecution-history, file-wrapper, specimen, TTAB, USPTO, cease-and-desist, DMCA, royalty-report, license-agreement]
  content_signals: [patent infringement, trademark infringement, copyright infringement, claim construction, prior art, reasonable royalty, lost profits, willful infringement, likelihood of confusion, substantial similarity, fair use, doctrine of equivalents]
defers_to:
  - deposition-summary: when inventor, technical, or expert depositions appear
  - discovery-summary: when infringement contentions or invalidity contentions appear as discovery responses
  - patent-infringement-analysis: when a deep per-claim infringement analysis is the deliverable
  - patent-infringement-summary: when a high-level patent-centered summary is the deliverable
  - ip-infringement-analysis: when a trademark or copyright infringement deep-dive is the deliverable
---

## Dimension extensions

### Parties & posture
Identify the rights-holder (assignee on the patent face, TM registrant on the certificate, copyright registrant), any exclusive licensees with standing, the accused party/parties, and any indemnitors. Capture pending USPTO/TTAB/Copyright Office proceedings (IPR, PGR, TTAB opposition/cancellation).

### Timeline
Subdivide into: rights acquisition (filing, issuance, registration), accused conduct (first sale / first use / first publication), notice to accused (marking, C&D, actual knowledge), willfulness-triggering events, damages period (6 years patent pre-suit, varies by jurisdiction for TM/copyright).

### Evidence inventory
**Patent:** file history, IDS submissions, prior-art references, accused-product specs / source code / schematics, sales data, license agreements, marking evidence, inventor notebooks.
**Trademark:** registration certificate / file wrapper, specimens of use, consumer-survey data, evidence of actual confusion, marketing materials, channels of trade overlap.
**Copyright:** registration certificate, deposit copies, access evidence, accused work, substantial-similarity analysis (expert or analytical), DMCA notices.

### Claims & legal theories
**Patent:** direct infringement (35 U.S.C. § 271(a)), induced (§ 271(b)), contributory (§ 271(c)), willfulness (post-*Halo*). Doctrine of equivalents where literal infringement gaps exist. Per-claim analysis, not per-patent.
**Trademark:** Lanham Act § 32 / 43(a), likelihood-of-confusion (circuit-specific factors: *Polaroid*, *Sleekcraft*, *DuPont*). Dilution for famous marks.
**Copyright:** ownership + access + substantial similarity; plus registration for damages availability (17 U.S.C. § 411). Fair-use affirmative defense analyzed as four-factor test.

### Exposure / remedies
**Patent:** reasonable royalty (minimum statutory floor, 35 U.S.C. § 284), lost profits (*Panduit* factors), enhanced damages for willfulness (up to 3x), injunction (*eBay* four-factor), fees in exceptional cases (§ 285).
**Trademark:** defendant's profits, plaintiff's damages, injunction, corrective advertising, treble damages for counterfeiting, fees in exceptional cases (§ 1117(a)).
**Copyright:** actual damages + disgorgement, or statutory damages ($750–$30,000 per work; up to $150,000 for willful) — elected at judgment; injunction; fees in court's discretion (§ 505).

### Defenses
**Patent:** non-infringement (per-element), invalidity (§§ 102, 103, 112), inequitable conduct, exhaustion, implied license, laches (rarely since *SCA Hygiene*), prosecution-history estoppel.
**Trademark:** fair use (classic / nominative), parody, priority by the defendant, abandonment, genericide, unclean hands, functionality.
**Copyright:** independent creation, fair use (four-factor), DMCA safe harbor, license, abandonment.

### Red flags & open threads
Gaps in inventor assignments / chain-of-title, missed maintenance fees, non-marking (§ 287 damages limitation), abandoned applications cited as prior art by accused infringer, defendant's non-infringement position strong on a single limitation, prior art the client didn't disclose during prosecution.

## Queries

### Parties & posture
- `"patent owner assignee licensee exclusive"`
- `"trademark registrant owner use in commerce"`
- `"copyright registration author work for hire"`
- `"IPR PGR TTAB opposition cancellation"`

### Timeline
- `"patent filing priority date issuance"`
- `"first sale first offer accused product launch"`
- `"cease and desist notice letter"`
- `"trademark first use in commerce specimen"`
- `"copyright registration deposit"`

### Evidence inventory — patent
- `"claim construction Markman hearing"`
- `"prosecution history file wrapper amendment"`
- `"prior art reference publication"`
- `"accused product specification schematic source code"`
- `"inventor notebook conception reduction to practice"`
- `"patent marking 287 notice"`

### Evidence inventory — trademark
- `"likelihood of confusion consumer survey"`
- `"channels of trade marketing overlap"`
- `"actual confusion evidence consumer"`
- `"specimen of use in commerce"`
- `"secondary meaning acquired distinctiveness"`

### Evidence inventory — copyright
- `"access copying probative substantial similarity"`
- `"registration certificate deposit copy"`
- `"DMCA takedown notice counter-notice"`
- `"fair use purpose character nature amount effect"`

### Claims & legal theories
- `"direct infringement 271 a every element"`
- `"induced contributory infringement 271 b c"`
- `"doctrine of equivalents function way result"`
- `"willful infringement Halo egregious"`
- `"Polaroid Sleekcraft DuPont likelihood factor"`
- `"substantial similarity ordinary observer"`

### Exposure / remedies
- `"reasonable royalty Georgia-Pacific hypothetical negotiation"`
- `"lost profits Panduit acceptable non-infringing substitute"`
- `"enhanced damages willful treble"`
- `"eBay injunction four factor"`
- `"statutory damages election 150,000"`
- `"exceptional case fees 285 1117 505"`

### Defenses
- `"invalidity anticipation obviousness"`
- `"prior art 102 103 printed publication"`
- `"indefiniteness 112 means plus function"`
- `"inequitable conduct intent materiality"`
- `"prosecution history estoppel amendment"`
- `"fair use four factor market effect"`
- `"functionality aesthetic utilitarian"`
- `"abandonment non-use three years"`

### Red flags
- `"chain of title assignment recordation"`
- `"maintenance fee lapse"`
- `"unmarked product 287 notice"`
- `"non-disclosed prior art IDS"`

## Output sections

### Asserted Rights — slots into IV Claims & legal theories

| Right | Number | Filing / Priority | Status | Owner | Exclusive licensee |
|---|---|---|---|---|---|

For patents, also list the asserted claims. For trademarks, the registration number(s) and classes. For copyright, the registered works.

### Accused Conduct — slots into V Evidence inventory

| Accused item | Description | First accused date | Evidence cited |
|---|---|---|---|

### Infringement Analysis — slots into IV Claims & legal theories

**Patent (per asserted claim):**

| Claim element | Accused feature | Evidence | Literal / DOE |
|---|---|---|---|

**Trademark (per factor):**

| Factor (circuit-specific) | Evidence favoring confusion | Evidence against | Weight |
|---|---|---|---|

**Copyright:**

- Ownership: [Registration cite]
- Access: [Evidence]
- Substantial similarity: [Protected elements copied; cite analytical or expert approach]

### Remedies — slots into VI Exposure/remedies

**Reasonable royalty** (patent) — hypothetical-negotiation framework; show royalty base × royalty rate with supporting comparables.
**Lost profits** (patent / TM / copyright) — show Panduit or analog factors satisfied.
**Enhanced / treble damages** — willfulness evidence cited.
**Injunction** — eBay factors where applicable; irreparable harm showing.
**Statutory damages** (copyright) — per-work election analysis; willfulness uplift.
**Fees** — exceptional-case showing where asserted.

## Quality checklist additions

- [ ] Every asserted patent claim has an element-by-element infringement chart
- [ ] Every accused product/feature mapped to the asserted right
- [ ] Prior-art references flagged with anticipation / obviousness positions
- [ ] Chain-of-title traced to current owner with recordation evidence
- [ ] Marking / § 287 notice analyzed for the patent pre-suit damages period
- [ ] Fair-use factors (copyright) analyzed if defendant has raised or can raise
- [ ] Willfulness evidence (pre-suit knowledge + egregiousness) explicitly addressed
- [ ] Royalty base and royalty rate each supported by record evidence or expert opinion

## Remedies / exposure methodology

**Patent damages** (35 U.S.C. § 284) are the amount adequate to compensate, in no event less than a reasonable royalty. The playbook produces reasonable-royalty exposure using a Georgia-Pacific hypothetical-negotiation framework: royalty base (accused-product revenue or apportioned base) × royalty rate (drawn from comparable licenses or expert opinion). Lost profits are considered when the patentee and infringer compete and Panduit factors are met (demand, no non-infringing substitutes, manufacturing/marketing capacity, profit margin). Willfulness uplift (up to 3x) requires evidence of egregious conduct post-*Halo*.

**Trademark damages** (§ 1117) permit defendant's profits (plaintiff bears only the burden of proving sales; defendant must apportion), plaintiff's actual damages (often corrective advertising), and injunction. Counterfeiting triggers mandatory treble and fee-shifting.

**Copyright damages** (§ 504) are either (a) actual damages + disgorgement of defendant's profits attributable to the infringement, or (b) statutory damages ($750–$30,000 per work; up to $150,000 for willful). Registration before infringement (or within three months of publication) is a prerequisite for statutory damages and fees under § 412.

For every remedy category, the playbook shows the computation (or range) and cites the record evidence supporting it. Valuation ranges without evidentiary backing are explicitly flagged as attorney-judgment.
