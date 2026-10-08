---
skill: beamten-disziplinarrecht/konkurrentenstreit
fact_pattern: |
  Mandantin ist Landesbeamtin (A 13) und hat sich auf ein
  Beförderungsamt A 14 beworben. Am 06.07.2026 ging ihr die
  Konkurrentenmitteilung zu; die Behörde will nach Ablauf von zwei
  Wochen ernennen. Die Auswahl stützt sich auf Anlassbeurteilungen;
  Mandantin und ausgewählter Mitbewerber haben dieselbe Gesamtnote,
  die Mandantin jedoch im höheren Statusamt. Der Auswahlvermerk
  besteht aus zwei Sätzen und verweist auf die "größere
  Verwendungsbreite" des Mitbewerbers. Akteneinsicht wurde bislang
  nicht gewährt.

must_cite:
  - "Art. 33 Abs. 2 GG"
  - "Art. 19 Abs. 4 GG"
  - "§ 9 BBG"
  - "§ 9 BeamtStG"
  - "§ 123 VwGO"
  - "§ 21 BBG"

must_appear:
  - "Anwendbares Recht"
  - "Bewerbungsverfahrensanspruch"
  - "Anforderungsprofil"
  - "Auswahlvermerk"
  - "Konkurrentenmitteilung"
  - "Wartefrist"
  - "Anordnungsanspruch"
  - "Anordnungsgrund"
  - "Ämterstabilität"
  - "Ausschöpfung"
  - "Antrag nach § 123 VwGO"

must_flag:
  - "Wartefrist verstreichen lassen"
  - "Nur die Gesamtnote verglichen"
  - "Kausalität nicht dargelegt"
  - "Akteneinsicht nicht beantragt"
  - "Eilrechtsschutz versäumt"
---

# Test — konkurrentenstreit

Struktureller Smoke-Test. Schritt 1 muss die Bestimmung des anwendbaren Rechts sein (Art. 33 Abs. 2 GG für alle, § 9 BBG nur im Bund). Der Bewerbungsverfahrensanspruch muss als subjektives Recht ohne Anspruch auf das Amt beschrieben sein. Anordnungsanspruch und Anordnungsgrund müssen im Antragsgerüst getrennt geführt werden, der Antrag auf Freihaltung der Stelle gerichtet sein. Die Ämterstabilität und ihre Durchbrechung bei Rechtsschutzvereitelung müssen erscheinen.

Run: `python ../../../scripts/eval.py --skill beamten-disziplinarrecht/skills/konkurrentenstreit`
