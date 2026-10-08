---
skill: urheber-medienrecht/lizenzvertrag-urhg
fact_pattern: |
  Mandant (freischaffender Drehbuchautor) hat einen Total-Buy-Out-
  Vertrag einer Filmproduktionsgesellschaft (GmbH) erhalten:
  Einmalpauschale 8.000 EUR, sämtliche Nutzungsrechte räumlich
  unbeschränkt, zeitlich unbeschränkt (Schutzdauer-konform), für alle
  bekannten und unbekannten Nutzungsarten, einschließlich Streaming,
  Merchandising und Remake-Rechten. Auskunftspflicht ist in einem
  AGB-Anhang ausgeschlossen. Anpassungsklausel ist nicht enthalten.
  Bitte prüfen: Wirksamkeit, Zweckübertragung, angemessene Vergütung,
  Bestseller-Klausel, § 32d Auskunftspflicht, § 31a Schriftform für
  unbekannte Nutzungsarten.

must_cite:
  - "§ 31 UrhG"
  - "§ 31 V UrhG"
  - "§ 31a UrhG"
  - "§ 32 UrhG"
  - "§ 32a UrhG"
  - "§ 32d UrhG"
  - "§§ 88"
  - "§ 89 UrhG"
  - "§ 307 BGB"

must_appear:
  - "Zweckübertragung"
  - "angemessene Vergütung"
  - "Bestseller-Klausel"
  - "auffälliges Missverhältnis"
  - "AGB-Kontrolle"
  - "Auskunftspflicht"
  - "unbekannte Nutzungsarten"
  - "Schriftform"
  - "Widerrufsrecht"
  - "Filmhersteller"

must_flag:
  - "§ 32a-Klausel als Verzicht"
  - "§ 32d-Auskunftspflicht"
  - "AGB-Unwirksamkeit § 307 BGB"
  - "§ 90 UrhG-Sperre der Rückrufrechte"
  - "§ 31a UrhG-Schriftform und Widerruf"
---

# Test — lizenzvertrag-urhg

Struktureller Smoke-Test. Drei Pflicht-Prüfsteine müssen alle adressiert sein: § 31 V Zweckübertragung, § 32 angemessene Vergütung, § 32a Bestseller-Klausel. § 32d Auskunftspflicht muss als zwingend gekennzeichnet sein, ihr Ausschluss als unwirksam markiert. Filmrechtliche Besonderheiten (§§ 88, 89, 90 UrhG) müssen erkannt werden.

Run: `python ../../../scripts/eval.py --skill urheber-medienrecht/skills/lizenzvertrag-urhg`
