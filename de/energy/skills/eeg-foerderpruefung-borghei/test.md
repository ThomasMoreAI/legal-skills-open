---
skill: energierecht/eeg-foerderpruefung
fact_pattern: |
  Mandantin (Windpark-Betreiberin, 6 WEA á 4,2 MW) hat im
  Ausschreibungsverfahren der BNetzA einen Zuschlag erhalten. IBN soll
  am 31.12. erfolgen. Die 110-kV-Trafostation ist noch nicht installiert,
  die Anlagen sind aber über einen provisorischen 30-kV-Anschluss
  einspeisefähig und werden tatsächlich einspeisen. MaStR-Eintragung
  ist eingeplant. Streit um IBN-Begriff und Folgen für den
  anzulegenden Wert nach §§ 36 ff. EEG.

must_cite:
  - "§ 3 EEG"
  - "§ 6 EEG"
  - "§ 19 EEG"
  - "§ 22 EEG"
  - "§ 25 EEG"
  - "§§ 36 ff. EEG"
  - "§ 51 EEG"
  - "§ 52 EEG"
  - "§ 8 MaStRV"

must_appear:
  - "Inbetriebnahme"
  - "technische Betriebsbereitschaft"
  - "Marktstammdatenregister"
  - "anzulegender Wert"
  - "Direktvermarktung"
  - "Negativstunden"
  - "Förderzeitraum"

must_flag:
  - "IBN-Datum"
  - "MaStR-Meldung"
  - "BImSchG"
---

# Test — eeg-foerderpruefung

Struktureller Smoke-Test. IBN-Datum und MaStR-Meldung müssen als Vorfragen vor jeder Förderhöhen-Prüfung adressiert werden; BImSchG-Genehmigungsstatus muss als Vorfrage benannt werden; der anzulegende Wert muss korrekt aus dem Ausschreibungs-Zuschlag (§§ 22, 36 ff. EEG) statt aus dem Festwert (§§ 49 ff.) abgeleitet werden.

Run: `python ../../../scripts/eval.py --skill energierecht/skills/eeg-foerderpruefung`
