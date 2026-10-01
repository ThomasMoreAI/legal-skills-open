---
skill: ki-vo-compliance/verbotene-ki-praktiken
fact_pattern: |
  Eine Behörde plant ein System, das Bürgerinnen und Bürger anhand ihres
  Sozialverhaltens (Zahlungsmoral, Verkehrsdelikte, Aktivität in sozialen
  Netzwerken) bewertet und daraus einen allgemeinen Vertrauenswert für den
  Zugang zu öffentlichen Leistungen ableitet. Zusätzlich soll an belebten
  Plätzen eine biometrische Echtzeit-Erkennung zur Fahndung eingesetzt werden.
  Ist das nach der KI-VO zulässig?
must_cite:
  - "Art. 5 KI-VO"
  - "Art. 99 KI-VO"
  - "Art. 6 KI-VO"
  - "Anhang III"
must_appear:
  - "Social Scoring"
  - "biometrische Echtzeit-Fernidentifizierung"
  - "Ausnahme"
  - "Tatbestandsmerkmale"
  - "Bußgeldrisiko"
  - "02.12.2026"
  - "NCII"
  - "CSAM"
  - "Bundesnetzagentur"
must_flag:
  - "Manipulation"
  - "Social Scoring"
  - "Scheinausnahme"
  - "Bußgeldrisiko"
  - "Neue Verbote NCII und CSAM übersehen"
  - "Nationale Zuständigkeit falsch adressiert"
---

# Test — verbotene-ki-praktiken

**Rechtsstand.** Die acht Verbotstatbestände des Art. 5 KI-VO gelten seit dem **02.02.2025** unverändert. Der Digital Omnibus on AI (EP 16.06.2026, Rat 29.06.2026) hat den Katalog um **NCII** und **CSAM** ergänzt; diese gelten **ab 02.12.2026**. Die Prüfung muss beide Zeitschichten unterscheiden.

**Zuständigkeit.** Deutsche Marktüberwachungsbehörde ist die **Bundesnetzagentur** (Auffangzuständigkeit, KI-MIG), für Biometrie in der Strafverfolgung die **UKIM** — **nicht** die Datenschutzaufsicht. Diese Assertion wurde ergänzt, weil die verbreitete Zuordnung zur Datenschutzaufsicht unzutreffend ist. Für das KI-MIG darf keine BGBl.-Fundstelle zitiert werden (zum 21.07.2026 nicht verkündet).

Run: `python3 scripts/eval.py --skill ki-vo-compliance/skills/verbotene-ki-praktiken`
