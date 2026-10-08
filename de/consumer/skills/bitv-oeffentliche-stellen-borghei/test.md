---
skill: barrierefreiheit-bfsg/bitv-oeffentliche-stellen
fact_pattern: |
  Eine Bundesoberbehörde betreibt ein Serviceportal, ein Intranet und ein
  neu beschafftes Fachverfahren zur elektronischen Aktenführung. Die
  Erklärung zur Barrierefreiheit auf dem Portal benennt zwar einzelne
  nicht barrierefreie PDF-Formulare, enthält aber weder einen
  Kontaktweg für Rückmeldungen noch einen Hinweis auf die
  Schlichtungsstelle. Erläuterungen in Deutscher Gebärdensprache und in
  Leichter Sprache fehlen vollständig. Das Fachverfahren wurde im
  Vergabeverfahren ohne Barrierefreiheitsanforderungen ausgeschrieben;
  seine grafische Oberfläche ist nicht tastaturbedienbar. Am 03.04.2026
  ist eine Mitteilung einer Nutzerin über Barrieren eingegangen, die
  bislang unbeantwortet ist. Die Behörde fragt zusätzlich, ob ihr ein
  Bußgeld nach dem BFSG droht.

must_cite:
  - "§ 12a BGG"
  - "§ 12b BGG"
  - "§ 15 BGG"
  - "§ 16 BGG"
  - "§ 3 BITV"
  - "§ 4 BITV"
  - "§ 7 BITV"
  - "§ 8 BITV"

must_appear:
  - "Deutscher Gebärdensprache"
  - "Leichter Sprache"
  - "Erklärung zur Barrierefreiheit"
  - "Feedback"
  - "Schlichtung"
  - "eines Monats"
  - "Intranet"
  - "Ausschreibung und Beschaffung"
  - "Überwachungsstelle"
  - "legal_calc"

must_flag:
  - "Bundes- und Landesrecht vermengt"
  - "BFSG-Maßstab auf eine Behörde angewandt"
  - "§ 4 BITV 2.0 übersehen"
  - "Intranet und Fachverfahren ausgeklammert"
  - "Erklärung ohne Feedback-Mechanismus"
  - "Bußgeld angedroht"
---

# Test — bitv-oeffentliche-stellen

Struktureller Smoke-Test. Die Ausgabe muss zuerst das Bundesregime (§§ 12a ff. BGG, BITV 2.0) festlegen, die fehlenden Erläuterungen in Gebärdensprache und Leichter Sprache an § 4 BITV 2.0 messen, die Erklärung wegen der fehlenden Bestandteile des § 12b Abs. 2 Nr. 2 und Nr. 3 BGG beanstanden, Intranet und Fachverfahren über § 12a Abs. 1 BGG einbeziehen, die unterlassene Berücksichtigung in der Beschaffung an § 12a Abs. 3 BGG messen, die Monatsfrist des § 12b Abs. 4 BGG ab 03.04.2026 berechnen und klarstellen, dass das BGG keinen Bußgeldtatbestand kennt.

Run: `python ../../../scripts/eval.py --skill barrierefreiheit-bfsg/skills/bitv-oeffentliche-stellen`
