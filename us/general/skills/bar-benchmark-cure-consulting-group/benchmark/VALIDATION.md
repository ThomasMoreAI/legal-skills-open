# Bank validation record

Every change to an answer key, and every validation pass, is logged here with its source.

## 2026-09-28 — initial build (Wave 6, T64/T65)

**Authoring.** Four independent authors, one per subject cluster, each writing reference files
and the items that test them. Authors source-checked high-risk NY figures on nysenate.gov and
corrected the brief they were given in eight places (e.g. "nail and mail" is CPLR 308(4), not
308(2); revocation by divorce is EPTL 5-1.4, not 3-4.4; NY RPC 1.10 was amended effective
2025-01-01 to permit screening laterals; NY GOL 5-701(a)(1) reaches lifetime contracts, the
opposite of the multistate rule).

**Blind key verification.** A second, separate agent per cluster answered every item from
`bar_bench.py list` (no key, no references, no web), then adjudicated disagreements against
primary sources, then fact-checked the cluster's reference files.

| Cluster | Sets | Closed-book (verifier) | Wrong keys | Items edited |
|---|---|---|---|---|
| A | mbe-civil-procedure, mbe-evidence, nyle-cluster-a, mee-cluster-a | 57/57 | 0 | 4 (MBE-EV-013 choice reworded; MBE-CP-008 `why`; MEE-CP-001, MEE-CL-001 rubrics) |
| B | mbe-contracts, mbe-real-property, nyle-cluster-b, mee-cluster-b | 54/54 | 0 | 4 (MBE-K-002 stem; MBE-RP-014 choice; NYLE-K-001 `why`; MEE-BA-001 rubric + answer) |
| C | mbe-torts, mbe-criminal-law-procedure, mbe-constitutional-law, nyle-cluster-c, mee-cluster-c | 70/70 | 0 | 3 (MBE-CON-010 stem; MBE-CON-009 `why`; MEE-TORT-001 answer) |
| D | mpre, nyle-cluster-d, mee-cluster-d | 43/43 | 0 | 5 (MPRE-006, MPRE-008 `why`; NYLE-FAM-004 choice; MEE-TE-001 rubric + answer (**wrong law**); MEE-FAM-001 cite) |

**Result:** 224 of 224 MCQ keys confirmed by an independent closed-book pass; 0 key changes.
One essay stated wrong law and was rewritten (MEE-TE-001: UPC 2-606(a)(5) replacement property
covers only real or tangible personal property; stock bought with sale proceeds is not
replacement property). Stems tightened where a second answer was arguable.

**What the 100% means.** Same-family verifiers scoring 100% confirms the keys are consistent
and unambiguous; it also shows the bank is at the ceiling for current frontier models. MCQ
scores therefore work as a regression gate, not as an uplift measure. Uplift is measured on
citation integrity (`scripts/cite_probe.py`), where models still fail.

**Reference-file defects found and fixed (the class this domain exists to prevent):**
- Wrong case years: *People v. Vasquez* (was 2009, is 1996), *People v. Beam* (was 1991, is 1982);
  *Messner Vetere* (was 1998, is 1999).
- Misattributed case: *People v. McFarland* cited as Court of Appeals 2013; the case found is
  4th Dep't 2017. Removed.
- Stale law: removal power after *Trump v. Slaughter* (U.S. June 29, 2026) overruling
  *Humphrey's Executor*.
- Statute details corrected against nysenate.gov: SAPA 202(4-a) (45 days, was 30), CPLR 4519
  accident exception scope, EPTL 4-1.3 (7 months from letters; 24 months in utero **or** 33 born),
  EPTL 5-3.1 set-off, EPTL 3-4.5, DRL 236(B)(5)(d)(7) ("shall consider"), BCL 713 alternative
  approval, BCL 722(c), PL 125.27(1)(b) ("more than eighteen").
- Garbled rules rewritten: UCC 9-323(b) future advances; Rest. 3d Products misuse; MBCA 13.40
  exceptions (4, not 3).

**Open (marked "confirm before use" in the files):** 2026 CSSA/maintenance income caps (secondary
sources only); verbatim NY RPC 1.10(c) text (substance confirmed via NYC Bar Formal Op. 2026-1);
PL 35.15 wording after the 2024 sex-offense amendments; *Settles* standard for exculpatory
penal-interest statements.

## 2026-09-28 — first live measurements

Raw data: `../results/2026-09-28-{claude,codex,cite-claude,cite-codex}.json`.

**MCQ + essays (`run_live.py`, full bank, essays judged cross-family).**

| Candidate | Arm | MBE (140) | NYLE (54) | MPRE (30) | MEE (7) | Cost |
|---|---|---|---|---|---|---|
| Claude Opus 5.5 | bare | 100.0 | 98.1 | 100.0 | 99.3 | \$1.18 |
| Claude Opus 5.5 | doctrine | 100.0 | **100.0** | 100.0 | 98.6 | \$3.86 |
| Codex (default model) | bare | 100.0 | 98.1 | 100.0 | 85.0 | subscription |
| Codex (default model) | doctrine | 100.0 | **100.0** | 100.0 | 85.7 | subscription |

Both bare misses were NY distinctions the doctrine files fixed: Claude missed EPTL 3-2.1(a)(4)
(30-day attestation window); Codex missed NY's rule on employee admissions (NY doesn't follow
FRE 801(d)(2)(D)). The MCQ bank is at the ceiling for both families. It stays as the regression
gate; it can't show more uplift.

**Citation integrity (`cite_probe.py`, 6 NY memo prompts × 2 runs per arm, rescored with the
tokenless CourtListener check).**

| Candidate | Arm | Statute cites (exist) | Case cites (found in CourtListener) | Case cites carrying a status |
|---|---|---|---|---|
| Claude | bare | 52 (52) | 18 (16; 2 unchecked) | 0% |
| Claude | skill | 56 (46; 1 nonexistent, 9 rate-limited) | 2 (2) | 100% |
| Codex | bare | 25 (25) | 31 (21; **8 not found**) | 0% |
| Codex | skill | 21 (21) | 3 (3) | 100% |

Adjudication of the not-found items (web search against nycourts.gov / Justia / CourtListener):
- Codex bare: *Cohen v. Abruzzo* cited as both 225 A.D.3d 723 (**wrong**) and 228 A.D.3d 724
  (right; 2d Dep't 2024, not indexed at that cite); *Prando v. Kelly* cited as 73 Misc. 3d 144,
  really an unreported Appellate Term decision (73 Misc 3d 144(A), 2021 NY Slip Op 51241(U)) —
  real case, incomplete cite; 228 A.D.3d 791 and 164 A.D.3d 758 **could not be confirmed**;
  3 others unresolved.
- Claude skill: EPTL 5-2.1 **does not exist**; the memo's own authorities table flagged it and
  corrected it to 5-1.2 before delivery.

**Reading.** The skills don't make either model know more black-letter law; the bank can't show
that and it isn't the point. They change behavior where the risk is: with the skill, both models
cut unverifiable case citations by ~90% (49 → 5), lean on statutes (every one checked exists except the one the model
flagged itself), and label every case they still cite. Bare Codex produced at least one wrong citation and
two it couldn't back up, all unlabeled: the *Mata v. Avianca* failure mode, measured.

**Caveats.** n = 12 memos per arm; nysenate.gov rate-limited part of the statute checks (counted
as unchecked, never as pass); CourtListener misses some real reporter cites, so not-found is
adjudicated by hand before being called wrong.

## 2026-09-28 — Wave 6.1 practice references

**Authoring and verification.** Six practice references (590 lines) written by three authors
against primary sources, then fact-checked by two independent verifiers (~235 claims).
Verifiers confirmed every headline status claim and caught three author errors:
Education Law §2-d penalty tiers (\$1k / \$5k / \$10k, not "up to \$10k later"); GBL §527-a
cancellation subsections ((1)(d)/(d-1), not (1)(e)); *Epic v. Apple* status (cert granted
2026-06-30, No. 25-1311). Also corrected: Penal Law §222.40 is possession, not sale.
`cite_check.py` over the six files: every reporter-cited case VERIFIED except *Florida Bar v.
TIKD*, 326 So. 3d 1073 (Fla. 2021) — real, not indexed by CourtListener.

**Practice-suite citation probe** (`cite_probe.py --suite practice`, 4 prompts × 2 runs per arm).

| Candidate | Arm | Statute cites (exist) | Case cites (found) | Carry a status |
|---|---|---|---|---|
| Claude | bare | 34 (34) | 19 (16; 1 not found, 2 unchecked) | 0% |
| Claude | skill | 27 (27) | 1 (1) | 100% |
| Codex | bare | 28 (28) | 15 (11; 4 not found) | 0% |
| Codex | skill | 18 (18) | 2 (2) | 100% |

All five not-found cites were adjudicated **real**: *Schultz v. Boy Scouts*, 65 N.Y.2d 189 (1985);
*Matter of People v. Sirius XM Radio*, 243 A.D.3d 424 (1st Dep't 2025); *Ballan v. Sirota*,
163 A.D.3d 516 (2d Dep't 2018). CourtListener's index misses many recent A.D.3d cites, so
NOT-FOUND over-counts fabrication; across every run to date the only confirmed wrong citation
is bare Codex's *Cohen v. Abruzzo*, 225 A.D.3d 723 (the case is 228 A.D.3d 724).

**Disclosures.** (1) The first practice runs were discarded: a race in `run_live.workdir()`
(introduced by the security fix, after the Wave 6 runs) deleted the shared temp dir mid-call and
produced empty memos; fixed with a lock and re-run clean. Wave 6 numbers predate the race.
(2) `cite_probe`'s status pattern now also recognizes `REFERENCE-ONLY`, a label Codex used; the
Codex practice run was rescored after that change (0% → 100% on 2 cites). (3) With the skill,
models also cite cases by name and year without a reporter; those aren't counted as case cites.

**Reading.** Same result as Wave 6, in the regulatory areas the portfolio needs: with the skill,
both models drop from 34 to 3 reporter-cited cases, rely on statutes that all check out, and
label every authority. The reference files also let both models state 2025–2026 changes (NY
auto-renewal amendments, the FAIR Act, SAFE for Kids rules) that bare runs don't mention.
