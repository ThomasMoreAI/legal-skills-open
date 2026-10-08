---
skill: agrarrecht/lwanpg-pruefung
fact_pattern: |
  Mandant ist Alleinerbe eines 1998 aus der LPG „Roter Stern" e.G.
  i.L. ausgeschiedenen Mitglieds (Sachsen). Der Erblasser ist 2022
  verstorben. Die Nachfolgegesellschaft (e.G. i.L.) hat 1999 eine
  Teilzahlung von 3.500 DM geleistet, danach nichts. Keine Über-
  gangsbilanz wurde dem Erblasser je vorgelegt. Letzte Korrespon-
  denz zwischen Erblasser und Liquidator 2015 (Zahlungsbereitschaft
  in Aussicht gestellt, aber nicht eingelöst). Bitte Anspruchs-
  grundlage, Verjährung § 51a LwAnpG, Klagebefugnis Erbe und
  Antragsschrift Landwirtschaftsgericht vorbereiten.

must_cite:
  - "§ 44 LwAnpG"
  - "§ 49 LwAnpG"
  - "§ 51a LwAnpG"
  - "§ 1922 BGB"
  - "LwVG"
  - "FamFG"

must_appear:
  - "Auseinandersetzungsguthaben"
  - "Übergangsbilanz"
  - "Landwirtschaftsgericht"
  - "Stufenklage"
  - "Verjährung"
  - "Auskunftsanspruch"
  - "Nachfolgegesellschaft"

must_flag:
  - "Erbengemeinschaft"
  - "Verschmelzung"
  - "Zivilkammer"
  - "Sachverständigengutachten"
---

# Test — lwanpg-pruefung

Struktureller Smoke-Test. Verjährung § 51a LwAnpG, Stufenklage Auskunft → Zahlung und Zuständigkeit Landwirtschaftsgericht (nicht Zivilkammer) müssen alle adressiert sein. Konkrete Beträge nur unter Verweis auf Übergangsbilanz.

Run: `python ../../../scripts/eval.py --skill agrarrecht/skills/lwanpg-pruefung`
