---
skill: wettbewerbsrecht/irrefuehrende-werbung-pruefung
fact_pattern: |
  Mandant (SaaS-Anbieter B2B) bewirbt sein Produkt auf der Landing-
  Page mit "Schneller als Marktführer X — bis zu 3× kürzere
  Ladezeiten*". Sternchen-Auflösung im Footer (8 pt grau auf weiß):
  "*basierend auf interner Messung August 2024, Konfiguration A".
  Marktführer X ist namentlich genannt. Bitte präventive Prüfung
  der Werbeaussage: Irreführung § 5 UWG, vergleichende Werbung § 6
  UWG, Vorenthalten wesentlicher Informationen § 5a UWG.

must_cite:
  - "§ 3 UWG"
  - "§ 5 UWG"
  - "§ 5a UWG"
  - "§ 6 UWG"
  - "UGP-RL"

must_appear:
  - "geschäftliche Handlung"
  - "Durchschnittsverbraucher"
  - "Verkehrsauffassung"
  - "vergleichende Werbung"
  - "Schwarze Liste"
  - "Anhang"

must_flag:
  - "Sternchen"
  - "nachprüfbarer"
  - "objektiv"
  - "Herabsetzung"
---

# Test — irrefuehrende-werbung-pruefung

Struktureller Smoke-Test. Erwartete Prüfschritte (geschäftliche Handlung → Schwarze Liste → § 5 → § 5a → § 5b → § 6 → Rechtsfolge) müssen alle im Output erscheinen. Bei vergleichender Werbung muss § 6 II Nr. 1–6 UWG vollständig geprüft sein.

Run: `python ../../../scripts/eval.py --skill wettbewerbsrecht/skills/irrefuehrende-werbung-pruefung`
