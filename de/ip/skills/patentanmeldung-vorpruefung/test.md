---
skill: patentrecht/patentanmeldung-vorpruefung
fact_pattern: |
  Mittelständisches Maschinenbauunternehmen hat ein KI-gestütztes
  Verfahren zur Vorhersage von Werkzeugverschleiß und automatischer
  Anpassung der Schnittparameter einer CNC-Fräsmaschine entwickelt.
  Vor 3 Monaten haben zwei beteiligte Ingenieure die Methode auf
  einer Fachkonferenz vorgestellt (Folien online verfügbar). Das
  Unternehmen will jetzt anmelden: DPMA, EPA, PCT? Zugleich besteht
  Unsicherheit, ob das Verfahren überhaupt patentierbar ist
  (Software-/KI-Anteil) und ob ein Gebrauchsmuster sinnvoll wäre.
  Die Ingenieure sind angestellt (ArbnErfG-Bezug).

must_cite:
  - "§ 1 PatG"
  - "§ 3 PatG"
  - "§ 4 PatG"
  - "Art. 52 EPÜ"
  - "Art. 54 EPÜ"
  - "Art. 56 EPÜ"
  - "§ 1 GebrMG"
  - "§ 3 GebrMG"
  - "§ 6 ArbnErfG"
  - "§ 9 ArbnErfG"

must_appear:
  - "technischer Charakter"
  - "Aufgabe-Lösungs-Ansatz"
  - "Neuheitsschonfrist"
  - "Eigenvorveröffentlichung"
  - "computerimplementierten Erfindungen"
  - "Prioritätsrecht"
  - "Einheitspatent"
  - "Inanspruchnahme"

must_flag:
  - "Konferenzbeiträge"
  - "EPÜ kennt keine Schonfrist"
  - "Verfahren sind nicht gebrauchsmusterfähig"
---

# Test — patentanmeldung-vorpruefung

Struktureller Smoke-Test. Alle vier Schutzvoraussetzungen (technischer Charakter, Neuheit, erfinderische Tätigkeit, gewerbliche Anwendbarkeit) müssen sauber durchgeprüft werden; Aufgabe-Lösungs-Ansatz muss explizit erscheinen; Eigenvorveröffentlichung und Neuheitsschonfrist § 3 V PatG / Art. 55 EPÜ müssen adressiert sein; Anmeldeweg-Strategie (DPMA / EPA / PCT) und Gebrauchsmuster-Alternative müssen genannt werden; ArbnErfG-Bezug (Meldung, Inanspruchnahme, Vergütung) muss berücksichtigt sein.

Run: `python ../../../scripts/eval.py --skill patentrecht/skills/patentanmeldung-vorpruefung`
