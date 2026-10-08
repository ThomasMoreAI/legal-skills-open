---
skill: medizinrecht/mbo-aerzte-pruefung
fact_pattern: |
  Mandant ist Facharzt für Plastische und Ästhetische Chirurgie mit
  Praxis in Bayern. Auf seiner Website bewirbt er Brustvergrößerungen
  mit dem Slogan „100 % Patientenzufriedenheit – Premium-Ergebnisse
  garantiert" und veröffentlicht Vorher-Nachher-Fotos ohne explizite
  Einwilligung der gezeigten Patientinnen. Außerdem hat er auf einem
  Arztbewertungsportal eine bezahlte Top-Platzierung gekauft, ohne
  dass dies als Werbung gekennzeichnet ist. Die Bayerische
  Landesärztekammer hat ein berufsrechtliches Verfahren eingeleitet
  und ein Schreiben mit Anhörung versandt. Außerdem droht die
  Approbationsbehörde mit der Prüfung der Berufsunwürdigkeit.

must_cite:
  - "MBO-Ä"
  - "§ 27 MBO-Ä"
  - "§ 9 MBO-Ä"
  - "§ 203 StGB"
  - "HWG"
  - "§ 5 BÄO"
  - "Art. 12 GG"
  - "§ 630f BGB"

must_appear:
  - "Landesberufsordnung"
  - "Bayerische"
  - "Heilberufe-Kammergesetz"
  - "sachangemessene Information"
  - "anpreisende Werbung"
  - "irreführende Werbung"
  - "Heilsversprechen"
  - "Bewertungsportal"
  - "Premium-Platzierung"
  - "Approbation"
  - "Berufsunwürdigkeit"

must_flag:
  - "MBO-Ä nur Muster"
  - "Approbationsentzug"
  - "Schweigepflicht"
  - "Vorher-Nachher-Fotos"
---

# Test — mbo-aerzte-pruefung

Struktureller Smoke-Test. Erwartet wird (i) ausdrückliche Identifikation der bayerischen Berufsordnung (nicht nur MBO-Ä), (ii) Prüfung der drei Werbe-Verbotskategorien (anpreisend / irreführend / vergleichend), (iii) Abgrenzung berufsrechtliche Sanktion ↔ § 203 StGB ↔ § 5 BÄO-Approbationsfolge, (iv) Hinweis auf Patienteneinwilligung für Vorher-Nachher-Fotos.

Run: `python ../../../scripts/eval.py --skill medizinrecht/skills/mbo-aerzte-pruefung`
