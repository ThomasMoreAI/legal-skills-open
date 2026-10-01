# Changelog — WCC-BiH skill

## [1.0.2] — 2026-07-06

### Fixed
- Shortened the `SKILL.md` frontmatter `description` below the 1024-character limit enforced by Claude Skills (reported by a user during installation). The triggering function is preserved — institutions, flagship cases, founding instruments, and the verification-first rule remain; the exhaustive enumerations live on in the skill body and references.

## [1.0.1] — 2026-06-02

### Fixed
- `references/foundational-texts.md`: noted that **Section I (War Crimes)** was introduced by the **December 2004 amendment** (Registry for Section I established 1 December 2004), not the original 2002 Law — hence operations beginning 9 March 2005. Harmonised the *Mejakić* referral/transfer dates.

## [1.0.0] — initial release

### Added
- `SKILL.md` — entry point, verification-first discipline, institutional architecture (Law on the Court of BiH 3 July 2002, operational January 2003, **WCC officially began operations 9 March 2005**, joint OHR + ICTY initiative, international-to-national composition transition 2005-2012), source hierarchy, citation format, audit mode, sensitive contexts
- `references/foundational-texts.md` — Law on the Court of BiH 2002, Law on the Prosecutor's Office of BiH, Criminal Code of BiH 2003 (with Maktouf qualification), SFRY Criminal Code 1976 (lex mitior), Criminal Procedure Code of BiH 2003, Rules of Procedure of the Court of BiH, National War Crimes Processing Strategy (December 2008), ICTY RPE Rule 11 bis, Constitution of BiH (Dayton Agreement Annex 4)
- `references/authoritative-sources.md` — Tier 1 (sudbih.gov.ba primary source, tuzilastvobih.gov.ba for indictments, IRMCT/ICTY archives for Rule 11 bis documents, legal-tools.org, OHR archives), Tier 2 (OSCE Mission to BiH as Tier 1-in-practice for monitoring, ICTJ Bogdan Ivanišević 2008 principal analytical treatment, UNDP BiH implementation reports, HRW, Hybrid Justice project, BIRN BiH balkaninsight.com daily monitoring), BCS as authoritative procedural language with English official translation
- `references/citation-format.md` — four citation modes (foundational texts, WCC-BiH judgments, ICTY referral documents, ECHR jurisprudence), chamber designations (Section I for War Crimes; Appellate Division Section I), case-number formats (X-KR-XX/XX first-instance, X-KRŽ-XX/XX appellate), document types (Indictment, First-Instance Verdict / Prvostepena presuda, Second-Instance Verdict / Drugostepena presuda, Decision / Rješenje, Order / Naredba), institutional milestones timeline, BCS diacritics discipline
- `references/verification-workflow.md` — fallback ladder (sudbih.gov.ba → tuzilastvobih.gov.ba → IRMCT/ICTY → legal-tools.org → OSCE → OHR → ICTJ → BIRN BiH), **7 WCC-BiH-specific traps**: (1) 2003 vs 1976 Criminal Code temporal application (*Maktouf and Damjanović* ECHR GC 18 July 2013) ; (2) State Court Section I vs entity/cantonal courts (FBiH, RS, Brčko) ; (3) Rule 11 bis cases vs locally-initiated ; (4) Lukić and Lukić referral revoked, case tried at ICTY ; (5) international/national composition transition 2005-2012 ; (6) WCC-BiH has no time limit (still operational as of 2026) ; (7) WCC formal vs informal nomenclature
- `references/jurisprudence-map.md` — 10 sections: Srebrenica genocide (Stupar/Kravica, Trbić), Foča sexual violence (Janković, Samardžić, Stanković), Prijedor camps (Mejakić et al., Rašević and Todović), command/superior responsibility, joint criminal enterprise (Tadić three-tier doctrine), *Maktouf* temporal application as most important doctrinal development, witness protection and support (OSCE report 2010), Rule 11 bis operational record with table of 6 cases including Lukić and Lukić revocation, application of customary international law, limited victim participation in criminal proceedings
- `examples/example-verification.md` — verifying the first Rule 11 bis case (Stanković) with parallel citations to ICTY Referral Bench decision (17 May 2005) and WCC-BiH First-Instance Verdict (14 November 2006), including subsequent escape and recapture
- `examples/example-audit.md` — two audits (pre-2013 Stupar/Kravica judgment without *Maktouf* note — Trap 1; cantonal court conviction attributed to WCC-BiH — Trap 2)

### Skill scope at v1.0.0
- Covers WCC-BiH operations from establishment (9 March 2005) through fully nationalised phase to present (2026)
- Encodes the verification-first methodology with WCC-BiH-specific procedural and substantive complexities
- Specifically equips the user to handle the **Maktouf temporal-application issue** (the most important doctrinal development), the **distinction between state-level and entity-level prosecutions**, the **Rule 11 bis institutional history**, and the **international-to-national composition transition**
- Comprehensive coverage of Rule 11 bis cases (Stanković, Janković, Mejakić et al., Trbić, Rašević and Todović, plus the revoked Lukić and Lukić referral)

### Known limitations
- The WCC-BiH continues to operate as a permanent national institution; the skill will need periodic updates as new jurisprudence emerges
- Post-Maktouf *lex mitior* analysis varies case-by-case; the skill flags the issue but cannot resolve case-specific questions
- Entity-level prosecutions (FBiH cantonal courts, RS district courts, Brčko District) are **flagged as distinct** but not covered by this skill — they would warrant separate skills if/when added
- Constitutional Court of BiH decisions touching WCC-BiH proceedings are referenced but not exhaustively mapped
