# us-state-privacy-navigator

A Claude skill for cross-jurisdictional analysis of the US state consumer privacy law patchwork — applicability triage, gap analysis, deliverable generation, and DSAR routing across all 20 comprehensive state privacy laws (CA/CO/CT/VA/UT/TX/OR/MT/IA/IN/TN/DE/NJ/NH/NE/KY/MD/MN/RI/FL).

## What it does

1. **Applicability triage.** Given a business profile, returns a per-state applicability verdict with the threshold reasoning shown.
2. **Gap analysis.** Compares current practice to each applicable law's controller obligations and consumer rights, produces a severity-scored issue log, and prioritizes remediation.
3. **Deliverables.** Generates a memo (Markdown) and a formal client-ready DOCX, including an applicability matrix, gap log, and remediation roadmap. Drafts state-compliant notice clauses on request.
4. **DSAR / consumer-rights orchestration.** Routes a consumer rights request to the correct response procedure based on residency, the right invoked, and controller status.

## Why it exists

Most privacy compliance work product available today — vendor checklists, generic memos, AI summaries — gets the basic distinctions wrong: conflating CCPA and CPRA, treating "sensitive data" as one concept across states, missing UOOM mandates, missing CA's coverage of employee and B2B data, missing Maryland's flat bans. This skill is built around eight operating principles enforced throughout the analysis:

1. Statutes over recollection.
2. Applicability first.
3. Status before duties.
4. Personal information ≠ consumer (sectoral and B2B/HR carve-outs differ by state).
5. Distinguish sale from sharing from targeted advertising from profiling.
6. Cite as you go.
7. No legal advice posture.
8. AD/BC dating in formal deliverables.

The goal is defensible legal work product, not vendor-style compliance theater.

## Structure

```
us-state-privacy-navigator/
├── SKILL.md                          The orchestrator.
├── references/
│   ├── applicability-matrix.md       Master threshold matrix.
│   ├── rights-comparison.md          Consumer rights side-by-side.
│   ├── controller-duties.md          Controller obligations side-by-side.
│   ├── sensitive-data.md             Definitions, opt-in vs opt-out structures.
│   ├── universal-opt-out.md          GPC / UOOM implementation reference.
│   ├── kids-and-teens.md             COPPA + state minor overlay.
│   ├── federal-overlays.md           Federal sectoral overlays (HIPAA/GLBA/COPPA/FERPA/FCRA/DPPA × state).
│   ├── enforcement.md                AGs, penalties, cure periods.
│   ├── enforcement_actions.json      Structured precedent corpus (82 actions, 48-tag taxonomy).
│   ├── ag-priorities.md              Per-state AG enforcement priorities & risk weighting.
│   ├── defense-arguments.md          Litigation defenses with strength ratings & doctrinal basis.
│   ├── states/                       20 state-specific files (ca.md, va.md, etc.).
│   └── workflows/
│       ├── intake-questionnaire.md   Structured intake.
│       ├── gap-analysis-method.md    Severity scoring & prioritization.
│       ├── status-determination.md   Controller/processor/third-party decision tree (per data flow).
│       └── dsar-routing.md           Rights-request orchestration.
├── assets/
│   ├── memo-template.md              MD memo skeleton.
│   ├── applicability-questions.json  Machine-readable intake schema.
│   └── notice-clauses/
│       ├── notice-at-collection.md
│       ├── opt-out-disclosures.md
│       ├── sensitive-data-notice.md
│       └── financial-incentive.md
└── scripts/
    ├── applicability_check.py        Deterministic threshold engine.
    ├── precedent_match.py            Gap-to-precedent matcher (tag-based & free-text).
    ├── conflict_resolver.py          Multi-state compliance ceiling synthesizer.
    ├── citation_audit.py             Pre-publication citation discipline auditor.
    └── generate_docx_memo.js         DOCX deliverable generator (docx-js).
```

## Using the scripts

### Applicability check

```bash
python scripts/applicability_check.py --input intake.json --output verdict.json
```

The `intake.json` file should conform to `assets/applicability-questions.json`. The script returns per-state verdicts (Applies / Likely Applies / Does Not Apply / Insufficient Info) with reasoning. It does not invoke an LLM, does not infer missing inputs, and does not soften close calls.

### Precedent matching

```bash
# Match a specific gap to analogous prior enforcement actions
python scripts/precedent_match.py --tag gpc_not_honored --tag no_donotsell_link --state CA --top 3

# Free-text search across the corpus
python scripts/precedent_match.py --query "session replay wiretap pixel"

# Bulk match for an array of gaps
python scripts/precedent_match.py --gaps gaps.json --output precedents.json
```

The corpus is `references/enforcement_actions.json`. Each action carries violation-theory tags, factual pattern, monetary amount, remediation imposed, citation, and operational lessons. The ranker scores by tag overlap (100 pts/tag), state proximity (35 pts), recency (max 20 pts), and severity (max 25 pts).

### Conflict-of-laws synthesis

```bash
python scripts/conflict_resolver.py --states CA,CO,CT,MD,VA
python scripts/conflict_resolver.py --states-from verdict.json --format json --output ceiling.json
```

For each of ~13 compliance dimensions (notice content, sensitive-data treatment, sale of sensitive data, minor treatment, response time, appeal right, UOOM recognition, processor contract terms, DPA requirements, etc.), the synthesizer returns the strictest applicable rule, the controlling state, the citation, and other states' positions. Maryland's flat bans on sensitive-data sale and minor-data sale/targeted-advertising surface as the binding constraint where MD is in scope.

### Citation audit

```bash
python scripts/citation_audit.py --input memo.md
python scripts/citation_audit.py --input memo.md --strict --output audit.json
```

Mechanical enforcement of citation discipline. Detects substantive claims lacking inline citations, citations failing canonical formats for state privacy statutes, implausible section numbers (e.g., `Cal. Civ. Code § 1798.X` outside the CCPA range), unresolved `[citation needed]` markers, and naming inconsistencies (CPRA reified outside parentheticals). Exits 1 on errors; exits 1 on warnings under `--strict`.

### DOCX deliverable

```bash
npm install -g docx
node scripts/generate_docx_memo.js --input memo.json --output deliverable.docx
```

Produces a US Letter document with cover, TOC, applicability matrix, gap log table, and remediation roadmap. Conforms to the `docx` skill conventions (dual-width tables, ShadingType.CLEAR, LevelFormat.BULLET, etc.).

## v2.0 — sophistication upgrades

Six modules added in v2.0 to push beyond a navigator into legal-reasoning territory:

1. **Structured precedent corpus** (`references/enforcement_actions.json` + `scripts/precedent_match.py`) — enables every gap to be paired with the closest analogous prior matter, including operational lessons from each.
2. **Conflict-of-laws engine** (`scripts/conflict_resolver.py`) — synthesizes the binding multi-state constraint instead of stacking parallel state analyses.
3. **Defense-side framing** (`references/defense-arguments.md`) — what controllers can argue when challenged, with strength ratings and counter-arguments grounded in CCPA/CPPA enforcement record (Sephora, DoorDash, Honda) and adjacent doctrine (CIPA, BIPA, FTC § 5).
4. **Status determination as dedicated workflow** (`references/workflows/status-determination.md`) — replaces the single-table treatment with a decision tree, dual-status patterns for the most common SaaS / adtech / analytics / payments / AI scenarios, and edge cases.
5. **Citation discipline auditor** (`scripts/citation_audit.py`) — mechanical pre-delivery QA that enforces the operating principles (every substantive claim cited; canonical formats; section numbers plausible; no orphaned [citation needed] markers).
6. **AG enforcement priorities** (`references/ag-priorities.md`) — per-state stated and observed priorities, risk-tier classification, and gap-scoring adjustments so risk weighting reflects actual enforcement posture rather than statutory penalty caps.

## v2.5 — federal overlay reference and scope discipline (2026)

Two changes this version, both about scope discipline rather than scope expansion:

1. **New file: `references/federal-overlays.md`.** A dedicated reference for where federal sectoral regimes intersect with state privacy law. Covers HIPAA, GLBA, COPPA, FERPA, FCRA, and DPPA. The single most important section is the **entity-level vs. data-level exemption diagnostic** — getting this wrong is the most common error in multi-state compliance work for federally-regulated entities. Includes:
   - Per-state HIPAA exemption matrix (all 20 states), with citations to each state's exemption clause
   - Per-state GLBA exemption matrix, same format
   - COPPA preemption framework with the express preemption clause analysis (15 U.S.C. § 6502(d)) and state teen-overlay integration (CA AB 1949, CT/CO teen provisions, MD MODPA flat ban on minor targeted advertising)
   - FERPA non-preemption analysis with SOPIPA-style state student-privacy law interaction (Department of Education's January 2025 *Dear Colleague* AI guidance noted)
   - FCRA partial preemption doctrine (15 U.S.C. § 1681t) and the circuit split on § 1681t(b)(1)(F) furnisher-conduct preemption (Ross v. FDIC, Galper v. JP Morgan, evolving 9th Circuit doctrine)
   - DPPA brief treatment for telematics and connected-vehicle context
   - Cross-references to 12+ existing corpus entries throughout (HIPAA OCR, CFPB, FTC sectoral, multistate AG anchors)
   - Explicit "what this is NOT for" section to prevent scope creep

   Maryland's data-level approach to HIPAA/GLBA combined with MODPA flat bans is flagged repeatedly as the multi-state binding constraint where MD is in scope.

2. **Scope-disclaimer language in SKILL.md.** The description's "Do NOT use" clause now explicitly identifies HIPAA / GLBA / COPPA / FERPA / FCRA standalone analysis as out of scope and points to `references/federal-overlays.md` as the bridge for overlay questions. The Limitations section now includes a structured "What this skill is *not* for — explicit scope and referrals" subsection enumerating both federal sectoral regimes (out of scope standalone, in scope as overlay) and other adjacent regimes (out of scope entirely — GDPR, state biometric laws standalone, state consumer-health-data laws standalone, state AI laws, state social-media/minor-platform laws). The route table in SKILL.md adds a row for `references/federal-overlays.md`.

No changes to the enforcement corpus, taxonomy (still 48 tags), existing reference files, scripts, or tests. All 58 tests continue to pass.

The narrowness is the point. This skill is a state privacy patchwork navigator. Federal sectoral regimes and other adjacent regimes warrant their own skills with their own depth.

## v2.4 — fact-check pass (2026)

Pre-PR fact-check pass against authoritative sources for high-priority entries. Twelve corrections applied:

1. **ca-cppa-todd-snyder-2025**: fine $345,000 → $345,178 (per Stipulated Final Order, Case No. ENF23-M-TO-26)
2. **ny-allstate-root-2025**: split into ny-james-root-2025 (settled $975k March 20, 2025) + ny-james-allstate-pending-2025 (litigation pending; ~165,000 NYers exposed)
3. **wa-mhmda-amazon-flo-2024-2025 → wa-mhmda-maxwell-amazon-2025**: corrected mischaracterization. Maxwell v. Amazon, No. 2:25-cv-00261 (W.D. Wash. Feb. 10, 2025) is a *private class action* under MHMDA's private right of action, not a state AG enforcement action. First federal MHMDA lawsuit.
4. **ny-james-amerimedical-2024 → ny-james-aent-2024**: corrected respondent name (Albany ENT & Allergy Services, P.C., not "Capital Region Healthcare Provider"); clarified that $2.25M is mandated security investment, not cash penalty (cash = $500k + $500k suspended); fixed affected count (213,935 NYers, not 4,700).
5. **il-bipa-cothron-amendment-2024**: added April 1, 2026 7th Circuit ruling (Clay/Willis/Gregg consolidated appeal) holding SB 2979 applies *retroactively* to pending cases — material change reducing pre-amendment damages exposure.
6. **cfpb-block-cashapp-2025**: corrected URL to current CFPB press release path.
7. **multistate-23andme-2025 → mdl-23andme-bankruptcy-2025**: recharacterized. The $50M (revised, October 2025) figure is an MDL class action settlement (In re 23andMe, MDL 3098, N.D. Cal., Judge Chen), not a multistate AG settlement. The multistate AG dimension is the June 2025 bankruptcy intervention by 28+ states (led by Oregon AG) objecting to genetic-data sale without consumer consent.
8. **ny-james-genericgear-2025 → ny-james-wojeski-2025**: ID rename from v2.1 placeholder.
9. **ca-cipa-flo-meta-jury-2025**: caption corrected from `In re Flo Health Privacy Litigation` to `Frasco v. Flo Health, Inc., No. 3:21-cv-00757 (N.D. Cal., filed Jan. 29, 2021; verdict Aug. 1, 2025)`. The "In re" caption was a media-style reference; the actual MDL caption is Frasco v. Flo Health.
10. **ftc-ngl-labs-2024**: regulator corrected from "California Attorney General" to "Los Angeles County District Attorney." The July 9, 2024 joint action was FTC + LA DA's Office, not the state AG. Some secondary coverage (e.g., Inside Privacy blog) misidentified the partner agency; the FTC press release and primary sources confirm LA DA.
11. **ca-blackbaud-2024 → multistate-blackbaud-2023**: ID prefix and year corrected. California was NOT in the multistate (49 states + DC, excluding California). The multistate AG settlement was October 5, 2023; the parallel FTC action was announced February 1, 2024 (no monetary penalty), finalized May 2024. Removed "(revised entry)" leftover from case_name.
12. **hipaa-inmediata-2024 split into two entries**: hipaa-inmediata-ocr-2024 ($250k HHS OCR settlement, December 10, 2024) and hipaa-inmediata-multistate-2023 ($1.4M 32-state AG + Puerto Rico settlement, October 17, 2023, led by Indiana AG Rokita). Previous combined entry blurred two distinct enforcement actions; splitting properly distinguishes the two regulatory channels.

The fact-check pass also confirmed the following anchor entries as accurate without changes: Honda ($632,500), Healthline ($1.55M), Tractor Supply ($1.35M, third 2025 CPPA settlement, Placerville complaint trigger), Mobilewalla/Gravy (RTB first), GEICO/Travelers ($11.3M joint NY OAG+NYDFS), BNSF/Rogers ($228M verdict → $75M settlement), Texas Allstate-Arity (first state AG TDPSA enforcement, Jan 13 2025), Connecticut TicketNetwork ($85k), Marriott ($52M state AG, Oct 9 2024), Disney COPPA ($10M, Dec 31 2025), GoodRx ($1.5M, Feb 1 2023), Rytr (with Dec 22 2025 vacatur).

Total actions: 82 (up from 80: ny-james-root / ny-james-allstate-pending split during initial pass; hipaa-inmediata further split into OCR-only and multistate-only entries during deeper pass). All 58 tests still pass. Test suite caught one taxonomy violation introduced during corrections (`third_party_vendor_management` was not in the canonical 47-tag taxonomy; replaced with `processor_contract_inadequate`).

## v2.3 — test suite (2026)

Stdlib-only test directory at `tests/` covering every script, the corpus, and every shipped reference doc. 58 tests, ~1.6s runtime, zero external dependencies. Five test files:

- `test_corpus_integrity.py` (12 tests) — JSON well-formedness, taxonomy adherence, anchor presence, field-shape validation.
- `test_precedent_match.py` (8 tests) — scoring and ranking against canonical queries, batch mode, output structure.
- `test_conflict_resolver.py` (7 tests) — multi-state synthesis, MD flat-ban controlling rule, dimension filtering, edge cases.
- `test_citation_audit.py` (9 tests) — fixture-based positive/negative cases plus reference-doc sweep that caught and surfaced 13 real citation gaps now fixed.
- `test_applicability_check.py` (22 tests) — three fixture scenarios (sub-threshold, CA-only, national multistate) plus output structure invariants and the "refuse to guess" principle.

Run: `python3 tests/run_all.py` (or `python3 -m unittest discover tests`).

The reference-doc audit-test layer caught and forced fixes to citation gaps in `rights-comparison.md`, `sensitive-data.md`, `universal-opt-out.md`, and `kids-and-teens.md` that v2.2 corpus expansion had not surfaced — exactly the failure mode the citation auditor was designed to prevent. Dogfooding works.

## v2.2 — production-grade corpus depth (2026)
Enforcement corpus expanded from 53 to 80 actions. New coverage adds:

- **CIPA wiretap class-action depth**: Kaiser Permanente $46M settlement (largest healthcare-pixel CIPA settlement to date, 13.4M class members); Flo/Meta jury verdict establishing SDK liability and rejecting the 'no physical device' defense; Torres v. Prudential summary judgment narrowing session-replay theory; Thomas v. Papa John's (9th Cir.) foreclosing direct-party CIPA theory; pen register rulings (Palacios, Aviles, Khamooshi, Popa) narrowing § 638.51 claims; chatbot-CIPA litigation pattern.
- **Recent FTC AI/algorithm enforcement**: Rytr (with critical December 2025 reversal flagged); DoNotPay $193k; NGL Labs $5M (joint FTC + Cal. AG, first permanent under-18 ban); Evolv (school-safety AI); IntelliVision (facial recognition bias claims); Texas AG v. Pieces Technologies (first state-AG AI-healthcare action).
- **GLBA / financial sector**: Block/Cash App CFPB $175M consent order; Salinas v. Block class settlement $15M (cumulative Block exposure $295M+); NYDFS PayPal $2M Part 500 action; SEC R.R. Donnelley $2.125M cybersecurity disclosure; FTC Safeguards Rule expanded scope summary; NYDFS Part 500 enforcement pattern.
- **HIPAA business-associate enforcement**: AHA v. Becerra (N.D. Tex. 2024) vacating OCR pixel guidance — narrowed but did not eliminate exposure; Warby Parker $1.5M CMP; Inmediata Health Group ($250k OCR Dec 2024 + $1.4M 32-state AG + Puerto Rico Oct 2023, $1.65M combined); Children's Hospital Colorado $548k CMP with continuing-violation calculation; healthcare-pixel class-action pattern (Advocate Aurora, Novant, UCSF/Dignity, WakeMed totaling $30M+); Third Circuit CMIA pixel dismissal.
- **Disney COPPA**: $10M civil penalty + 10-year audience-designation program (Dec 2025).
- **CFPB Equifax**: $15M FCRA dispute-handling action (Jan 2025).
- **Advisory entry**: explicit treatment of 14 comprehensive-privacy-law states with no published enforcement (VA, UT, IA, IN, TN, DE, NJ, NH, NE, KY, RI, MD, MN, MT) — by design, to prevent the corpus from being read as implying these states pose no enforcement risk.

The Rytr entry deserves attention: the original 2024 settlement was vacated by the FTC's new majority on December 22, 2025, which signals a narrowed FTC AI-enforcement posture (deception theories with concrete consumer harm preferred over unfairness theories about AI products' misuse potential). The entry expressly flags this status to prevent stale citation.

Tag taxonomy coverage: 38 of 47 tags now have at least one published action. The remaining 9 empty tags reflect reality, not gaps to fill — most are violation modes that have not yet produced standalone published enforcement (e.g., MD's flat ban on sensitive-data sale has no published action because MODPA is too new; financial-incentive value-calculation challenges have not been published; appeal-right denials are folded into broader actions rather than appearing as standalone matters).

## v2.1 — corpus expansion (2026)

Enforcement corpus expanded from 21 to 53 actions. New coverage includes:

- **2025 CPPA enforcement**: Honda (corrected to March 2025, $632.5k), Todd Snyder ($345k), Tractor Supply ($1.35M — first published action on HR/applicant data), Background Alert ($50k), data-broker sweep across KMA/ROR Partners/Datamasters/S&P Global ($270k aggregate)
- **2025 California AG**: Healthline ($1.55M — largest CCPA settlement to date; first regulatory privacy action fining inferred sensitive PI rather than explicit health data)
- **2025 Texas AG**: Allstate/Arity (first comprehensive-state-privacy-law lawsuit by any state AG); GM/OnStar (TX); 100+ cure letters across the TDPSA initiative
- **2025 Connecticut AG**: TicketNetwork ($85k — first CTDPA monetary settlement)
- **2025 Oregon DOJ**: 21+ cure-letter actions; first-year enforcement report; 2026 cure-period sunset
- **2024 FTC location-data line**: X-Mode/Outlogic, Mobilewalla, Gravy/Venntel, Kochava, InMarket — coherent doctrinal framework state AGs are importing
- **2024 FTC health-data line**: Cerebral ($7.1M), Monument; expansion of GoodRx/BetterHelp framework
- **2026 FTC GM/OnStar**: First connected-vehicle order with 5-year sale ban + 20-year affirmative-consent requirement
- **VPPA appellate development**: Solomon v. Flipps Media (2d Cir. 2025) shutting the door on Pixel-based VPPA claims under the ordinary-person standard; circuit split with Sixth Circuit's Salazar v. Paramount
- **BIPA**: Rogers v. BNSF $75M verdict; SB 2979 / Public Act 103-0769 amendment narrowing per-scan damages going forward
- **Multistate**: Marriott/Starwood ($52M FTC + 49 AGs); 23andMe (post-bankruptcy genetic-data protections)
- **NY OAG**: GEICO/Travelers ($11.3M); Allstate and Root Insurance pending; Wojeski accounting firm ($60k); Capital Region healthcare provider ($2.25M)
- **WA MHMDA**: Amazon (WA AG suit Feb 2025); Flo Health, Hims & Hers private actions
- **Defense-arguments updates**: Solomon v. Flipps and three additional VPPA defense subsections added

The defense-arguments reference and AG-priorities reference were updated to reflect the new caselaw and enforcement posture. The Honda CPPA settlement date was corrected (it occurred March 12, 2025, not 2024 — this was a draft-stage error that the new entries surfaced).


## Limitations

- **Reflects law as of the version date in the SKILL.md frontmatter.** State privacy law moves fast. New states pass laws; existing laws are amended. When a question turns on a development that may post-date the references, the skill flags it and recommends verification against a current source.
- **Federal sectoral regimes are in scope only as overlay, never standalone.** HIPAA, GLBA, COPPA, FERPA, and FCRA each have a dedicated treatment in `references/federal-overlays.md` — but only as an *overlay* on state privacy analysis. For standalone HIPAA / GLBA / COPPA / FERPA / FCRA questions (Privacy Rule mechanics, VPC implementation, dispute-resolution timing, etc.), this skill is the wrong tool; use a sectoral resource. The narrowness is intentional.
- **Other adjacent regimes are out of scope entirely**: GDPR / UK GDPR / non-US laws; state biometric laws standalone (BIPA, CUBI, WA biometric — though enforcement actions appear in the corpus); state AI laws (CO AI Act, NYC LL 144, UT AI Disclosure); state consumer-health-data laws standalone (WA MHMDA, CT amendments, NV — though MHMDA private right of action filings appear in the corpus); state social media / minor-platform laws (CA SB 976, NY SAFE for Kids, FL HB 3, TX SCOPE).
- **Produces analysis and drafts**, not legal advice. A licensed attorney must review.

## License

MIT.
