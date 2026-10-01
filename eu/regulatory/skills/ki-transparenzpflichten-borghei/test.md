---
skill: ki-vo-compliance/ki-transparenzpflichten
fact_pattern: |
  Ein Medienunternehmen betreibt auf seiner Website einen KI-Chatbot für den
  Kundendialog und produziert mit einem Bildgenerator fotorealistische
  Werbevideos, in denen eine reale Person täuschend echt nachgebildet wird
  (Deepfake). Eine Kennzeichnung der KI oder der generierten Inhalte erfolgt
  bisher nicht. Welche Pflichten bestehen nach der KI-VO?
must_cite:
  - "Art. 50 KI-VO"
  - "Art. 99 KI-VO"
  - "Art. 3 KI-VO"
must_appear:
  - "KI-Interaktion"
  - "synthetische"
  - "Deepfake"
  - "maschinenlesbar"
  - "Bußgeldrisiko"
  - "02.08.2026"
  - "nicht verschoben"
  - "Bundesnetzagentur"
must_flag:
  - "Kennzeichnung vergessen"
  - "Deepfake nicht offengelegt"
  - "Chatbot ohne Hinweis"
  - "Bußgeldrisiko"
  - "Verschiebung der Hochrisiko-Pflichten als Entwarnung für Art. 50 missverstanden"
  - "Art. 50 an die Hochrisiko-Einstufung gekoppelt"
  - "Nationale Zuständigkeit falsch adressiert"
---

# Test — ki-transparenzpflichten

**Rechtsstand.** Art. 50 KI-VO gilt **ab 02.08.2026** und wurde vom Digital Omnibus on AI **ausdrücklich von der Verschiebung ausgenommen**. Verschoben sind allein die Hochrisiko-Pflichten (Anhang III → 02.12.2027, Anhang I → 02.08.2028). Die Prüfung darf daraus **keine** Entwarnung für Art. 50 ableiten; die Assertion `nicht verschoben` sichert diese Abgrenzung ab.

Deutsche Marktüberwachungsbehörde ist die **Bundesnetzagentur** (Auffangzuständigkeit, KI-MIG), nicht die Datenschutzaufsicht; für das KI-MIG darf keine BGBl.-Fundstelle zitiert werden (zum 21.07.2026 nicht verkündet).

Run: `python3 scripts/eval.py --skill ki-vo-compliance/skills/ki-transparenzpflichten`
