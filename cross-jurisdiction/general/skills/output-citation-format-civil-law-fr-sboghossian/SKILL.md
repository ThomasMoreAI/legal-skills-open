---
name: output-citation-format-civil-law-fr-sboghossian
title: Citation Format — French Civil Law (Dalloz / JurisClasseur)
description: Use when formatting legal citations in the French civil-law style (Dalloz / JurisClasseur convention) for case law, statutes, and doctrine. Applies to outputs destined for francophone MENA jurisdictions (Lebanon, Morocco, Tunisia) as well as France — where citation style follows Cass. com./Civ./soc. conventions rather than Bluebook or OSCOLA.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/output/output-citation-format-civil-law-fr
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: general
language: en
---

# Citation Format — French Civil Law (Dalloz / JurisClasseur)

## When to use this

Apply French civil-law citation style when:
- The output is a memo, brief, or opinion for a French-trained practitioner.
- The jurisdiction is France (FR) or a francophone civil-law jurisdiction where French legal culture is dominant: Lebanon, Morocco, Tunisia.
- The document cites French case law (arrêts) from the Cour de cassation, Conseil d'État, or lower courts.
- The output will appear in a French legal publication (Dalloz, JurisClasseur, Recueil Lebon).

Do **not** apply this format for DIFC/ADGM (use OSCOLA), US (use Bluebook), or purely Arabic-language MENA output (use MENA conventions).

## Case law (arrêts)

### Cour de cassation

The Cour de cassation is divided into chambers. The standard citation format:

```
Cass. com., 7 mars 2018, n° 16-23.000, D. 2018, p. 700.
```

Components:
1. **Court abbreviation**: `Cass.` followed by the chamber abbreviation
2. **Date**: day + month (written out) + year, no comma between
3. **Pourvoi number**: `n°` followed by the case number (format: YY-XX.XXX)
4. **Publication reference**: journal abbreviation, year, page

**Chamber abbreviations**:
| Chamber | Abbreviation |
|---------|-------------|
| Chambre commerciale | Cass. com. |
| Chambre civile (1re) | Cass. 1re civ. |
| Chambre civile (2e) | Cass. 2e civ. |
| Chambre civile (3e) | Cass. 3e civ. |
| Chambre sociale | Cass. soc. |
| Chambre criminelle | Cass. crim. |
| Assemblée plénière | Cass. ass. plén. |

**Publication references**:
| Journal | Abbreviation |
|---------|-------------|
| Recueil Dalloz | D. |
| Bulletin des arrêts de la Cour de cassation | Bull. civ. I (or II, III, etc.) |
| JurisClasseur Périodique (La Semaine Juridique) | JCP G. |
| Revue trimestrielle de droit civil | RTD civ. |
| Actualité juridique de droit administratif | AJDA |

### Conseil d'État

```
CE, 28 sept. 2016, n° 388135, Lebon p. 412.
```

Format: `CE`, date, number, publication in Recueil Lebon.

### Courts of appeal (Cours d'appel)

```
CA Paris, 15 janv. 2020, n° 18/12345.
```

Format: `CA [city]`, date, case number.

### First-instance courts

```
TGI Paris, 3 ch., 12 févr. 2019, n° 17/00123.
```

Format: `TGI [city]`, chamber (if relevant), date, case number.

## Statutes and codes

French statutes are cited by their date of publication in the Journal officiel (JO):

```
Loi n° 2016-1547 du 18 novembre 2016 de modernisation de la justice du XXIe siècle.
```

For codified provisions, cite the code and article:

```
C. civ., art. 1134.        (Code civil)
C. com., art. L. 210-1.   (Code de commerce)
C. trav., art. L. 1234-1. (Code du travail)
```

Note: articles in the new codified codes are numbered with letter prefixes (L. = législatif, R. = réglementaire, D. = décret).

## Doctrine (academic works)

Books:
```
G. Viney, Traité de droit civil. Introduction à la responsabilité, 3e éd., LGDJ, 2008, n° 123.
```

Format: Initials Surname, *Title in italics*, edition, publisher, year, paragraph number (n°) or page.

Articles:
```
P. Dupont, « Le droit des contrats en question », D. 2020, p. 1234.
```

Format: Initials Surname, « Article title in guillemets », journal abbreviation, year, page.

## Lebanon-specific adaptations

Lebanon's legal system follows the French model closely; the citation style is the same with these adaptations:
- Lebanese Cour de cassation: `Cass. lib., ch. civ., [date], n° [...], Rev. jud. lib. [year], p. [...].`
- Lebanese official gazette: `J.O. lib. n° [X], [date].`
- Lebanese laws are cited as: `Loi n° [X] du [date] relative à [subject].`

## Key differences vs common-law citation

| Dimension | French civil-law | Common-law (Bluebook/OSCOLA) |
|-----------|------------------|-----------------------------|
| Case name | Not in citation (cases named by court + date) | Central element (party names) |
| Date format | Day + month written out | Year only (OSCOLA) or in parenthetical (Bluebook) |
| Pin-cite | Page number after journal reference | Page number after reporter |
| Party names | Not cited in French case references | Always cited |

## Caveats and currency

French law is subject to frequent legislative reform. The Code civil was substantially reformed in 2016 (contract law), and commercial and employment codes are regularly updated. Always verify article numbers against the current version of the code on legifrance.gouv.fr before citing in a formal document.

## Related skills

- [[output-citation-format-bluebook]] — for US-trained audiences
- [[output-citation-format-oscola]] — for UK/DIFC common-law audiences
- [[output-citation-mena-conventions]] — for Arabic-language MENA citations
- [[output-creac-structure]] — the analytical structure that uses these citations
