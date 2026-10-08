---
skill: kapitalmarktrecht/prospektpflicht-pruefung
fact_pattern: |
  Mandantin (deutsche AG, Familienunternehmen, geprüfte Konzernabschlüsse
  für die letzten drei Geschäftsjahre vorliegend) plant erstmaligen
  Börsengang mit Zulassung der Aktien zum regulierten Markt (Prime
  Standard FWB). Volumen ca. 120 Mio. EUR, davon 80 % Kapitalerhöhung,
  20 % Verkauf bestehender Aktien durch Altgesellschafter. Mindeststücke-
  lung 1 Aktie, Anlegerkreis Privatanleger und Institutionelle. Bitte
  prüfen, ob Prospektpflicht besteht, welche Ausnahmen einschlägig sein
  könnten, BaFin-Billigungsverfahren und Prospekthaftungs-Risiken
  einschließlich Verantwortlichkeitserklärung nach Art. 11 Prospekt-VO.

must_cite:
  - "Art. 3 Prospekt-VO"
  - "Art. 1 IV Prospekt-VO"
  - "Art. 7 Prospekt-VO"
  - "Art. 11 Prospekt-VO"
  - "Art. 20 Prospekt-VO"
  - "Art. 23 Prospekt-VO"
  - "§ 3 WpPG"
  - "§ 9 WpPG"
  - "§ 11 WpPG"

must_appear:
  - "öffentliches Angebot"
  - "regulierter Markt"
  - "qualifizierte Anleger"
  - "Wertpapier-Informationsblatt"
  - "Risikofaktoren"
  - "Zusammenfassung"
  - "BaFin-Billigung"
  - "20 Werktage"
  - "Nachtrag"
  - "Verjährung"

must_flag:
  - "Risikofaktoren generisch"
  - "Nachtragspflicht"
  - "12-Monats-Zeitraum"
  - "Verantwortlichkeitserklärung"
---

# Test — prospektpflicht-pruefung

Struktureller Smoke-Test. Trigger Art. 3 und Ausnahmenkatalog Art. 1 IV müssen sauber abgearbeitet werden; BaFin-Fristen (10/20/30 WT) müssen genannt sein; Prospekthaftung §§ 9–11 WpPG mit Verjährung 1/3 Jahre adressiert.

Run: `python ../../../scripts/eval.py --skill kapitalmarktrecht/skills/prospektpflicht-pruefung`
