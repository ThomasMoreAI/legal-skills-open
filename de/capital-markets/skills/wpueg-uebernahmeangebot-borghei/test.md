---
skill: kapitalmarktrecht/wpueg-uebernahmeangebot
fact_pattern: |
  Strategischer Investor (Bieter) hat ohne öffentliches Angebot 28 %
  der Stimmrechte an einer im regulierten Markt (Prime Standard FWB)
  notierten Ziel-AG erworben. Daneben hat er mit einem weiteren
  Aktionär (5 % Stimmrechte) eine schriftliche Stimmbindungsverein-
  barung geschlossen, die u. a. die Abberufung des amtierenden CEO und
  einen Strategiewechsel zum Inhalt hat. Vorerwerbe in den letzten
  6 Monaten erfolgten zu 28,50 EUR pro Aktie; der 3-Monats-Durchschnitts-
  kurs liegt bei 25,80 EUR. Bitte prüfen, ob ein Pflichtangebot nach
  § 35 iVm § 29 WpÜG ausgelöst ist (insb. Acting in concert § 30 II),
  Höhe des Mindestpreises und Frist-Kalender.

must_cite:
  - "§ 29 II WpÜG"
  - "§ 30 WpÜG"
  - "§ 31 WpÜG"
  - "§ 35 WpÜG"
  - "§ 14 II WpÜG"
  - "§ 16 WpÜG"
  - "§ 33 WpÜG"
  - "§ 37 WpÜG"
  - "WpÜG-AngVO"

must_appear:
  - "Kontrolle"
  - "30 %"
  - "Acting in concert"
  - "Zurechnung"
  - "Mindestpreis"
  - "Vorerwerbe"
  - "3-Monats-Durchschnittskurs"
  - "Annahmefrist"
  - "Zaunkönig"
  - "Stellungnahme"
  - "Verteidigungsmaßnahmen"

must_flag:
  - "Pflichtangebot-Umgehung"
  - "Acting in concert"
  - "Mindestpreis"
  - "Stimmrechtsverlust"
---

# Test — wpueg-uebernahmeangebot

Struktureller Smoke-Test. Acting-in-concert-Zurechnung (Stimmbindung + Strategiewechsel) muss sauber subsumiert werden; Mindestpreis muss höchsten Vorerwerbspreis erfassen (nicht den niedrigeren Durchschnittskurs); BaFin-Prüfung 10 WT und Annahmefrist 4–10 Wo + 2 Wo Zaunkönig im Fristkalender.

Run: `python ../../../scripts/eval.py --skill kapitalmarktrecht/skills/wpueg-uebernahmeangebot`
