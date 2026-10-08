---
skill: gewerberecht/gewerbeanzeige-reisegewerbe
fact_pattern: |
  Mandant vertreibt Matratzen. Er unterhält ein angemietetes Ladenlokal,
  in dem er auf Terminvereinbarung berät, sucht daneben aber auch ohne
  vorherige Anmeldung Seniorenheime und Privathaushalte auf und
  verkauft dort direkt. Auf einem behördlich festgesetzten Jahrmarkt
  betreibt er zusätzlich einen Stand. Angemeldet ist bei der Gemeinde
  nur "Einzelhandel mit Möbeln"; eine 2024 eröffnete unselbständige
  Zweigstelle in der Nachbarstadt wurde nie angezeigt. Seit Kurzem
  vermittelt er auf Provisionsbasis auch Finanzierungen für den
  Matratzenkauf. Die Behörde hat am 04.05.2026 unter Berufung auf § 35
  GewO die Fortsetzung "sämtlicher Tätigkeiten" untersagt, weil eine
  Reisegewerbekarte und eine Erlaubnis für die Finanzierungsvermittlung
  fehlen.

must_cite:
  - "§ 4 GewO"
  - "§ 6 GewO"
  - "§ 14 GewO"
  - "§ 15 GewO"
  - "§ 34c GewO"
  - "§ 35 GewO"
  - "§ 55 GewO"
  - "§ 69 GewO"
  - "§ 145 GewO"
  - "§ 40 VwVfG"

must_appear:
  - "vorhergehende Bestellung"
  - "gewerbliche Niederlassung"
  - "Reisegewerbekarte"
  - "unselbständige Zweigstelle"
  - "Gegenstandswechsel"
  - "Marktprivileg"
  - "drei Tage"
  - "Ermessen"
  - "mildere"
  - "legal_calc"

must_flag:
  - "§ 15 Abs. 2 GewO und § 35 GewO verwechselt"
  - "Reisegewerbe allein nach dem Ort bestimmt"
  - "Anzeigepflicht bei Gegenstandswechsel oder Verlegung vergessen"
  - "Unselbständige Zweigstellen nicht angemeldet"
  - "Marktprivileg unterstellt"
  - "Ermessensausfall bei § 15 Abs. 2 GewO nicht gerügt"
---

# Test — gewerbeanzeige-reisegewerbe

Struktureller Smoke-Test. Die Ausgabe muss die Beratung im Ladenlokal auf Terminvereinbarung als stehendes Gewerbe, das Aufsuchen von Seniorenheimen ohne Bestellung als Reisegewerbe nach § 55 Abs. 1 GewO und den Jahrmarktstand über das Marktprivileg der §§ 69, 69a GewO einordnen. Die fehlende Anzeige der unselbständigen Zweigstelle und der Gegenstandswechsel durch die Finanzierungsvermittlung sind § 14 Abs. 1 GewO zuzuordnen, die Finanzierungsvermittlung § 34c Abs. 1 S. 1 Nr. 2 GewO. Die auf § 35 GewO gestützte Verfügung ist als auf die falsche Rechtsgrundlage gestützt zu beanstanden; richtig wäre § 15 Abs. 2 GewO mit Ermessensausübung und der Fristsetzung zur Nachholung als milderem Mittel.

Run: `python ../../../scripts/eval.py --skill gewerberecht/skills/gewerbeanzeige-reisegewerbe`
