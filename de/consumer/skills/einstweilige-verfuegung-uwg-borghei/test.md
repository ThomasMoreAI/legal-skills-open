---
skill: wettbewerbsrecht/einstweilige-verfuegung-uwg
fact_pattern: |
  Mandantin (Mitbewerberin, GmbH) hat am 15.04.2026 erstmals
  Kenntnis von einer rechtswidrigen Werbeaussage der
  Antragsgegnerin auf deren Webseite genommen (eidesstattliche
  Versicherung des Geschäftsführers vorhanden). Mandantin hat am
  17.04.2026 abgemahnt, Frist bis 24.04.2026. Antragsgegnerin lehnt
  modifizierte UE am 23.04.2026 ab. Heute ist der 28.04.2026.
  Mandantin will einstweilige Verfügung beantragen, sofern
  Dringlichkeit gegeben. Zuständig wäre das LG München.

must_cite:
  - "§ 8 UWG"
  - "§ 12 UWG"
  - "§ 14 UWG"
  - "§ 935 ZPO"
  - "§ 929 ZPO"
  - "§ 937 ZPO"
  - "§ 945 ZPO"

must_appear:
  - "Verfügungsanspruch"
  - "Verfügungsgrund"
  - "Dringlichkeitsvermutung"
  - "Selbstwiderlegung"
  - "Vollziehungsfrist"
  - "Glaubhaftmachung"
  - "Schutzschrift"

must_flag:
  - "Erstkenntnis"
  - "Monatsfrist"
  - "Antragstenor"
  - "Kerntheorie"
---

# Test — einstweilige-verfuegung-uwg

Struktureller Smoke-Test. Erwartete Prüfschritte (Verfügungsanspruch → Aktivlegitimation → Verfügungsgrund § 12 I → Selbstwiderlegung → Vollziehung § 929 II ZPO → § 945 ZPO-Risiko) müssen alle im Output erscheinen. Antragstenor muss als zitierfähiger Block formatiert sein.

Run: `python ../../../scripts/eval.py --skill wettbewerbsrecht/skills/einstweilige-verfuegung-uwg`
