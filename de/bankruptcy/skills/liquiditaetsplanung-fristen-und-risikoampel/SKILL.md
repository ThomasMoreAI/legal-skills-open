---
name: liquiditaetsplanung-fristen-und-risikoampel
title: Fristen- und Risikoampel Liquiditätsplanung
description: 'Für Fristen- und Risikoampel Liquiditätsplanung: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel.'
author: Klotzkette
author_url: https://github.com/Klotzkette/claude-fuer-deutsches-recht/tree/main/liquiditaetsplanung/skills/fristen-und-risikoampel
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: bankruptcy
language: de
---

# Fristen- und Risikoampel Liquiditätsplanung

## Arbeitsauftrag

Erzeuge aus einer Liquiditätsakte eine rote/gelbe/grüne Fristenliste. Entscheidend sind nicht nur Prozessfristen, sondern Zahlungstage und Krisenschwellen: Löhne, SV, Lohnsteuer/USt, Mieten, Leasing, Kreditraten, Covenants, Lieferantenstopps.

## Normenanker

- InsO §§ 17-19, § 15a.
- StaRUG § 1.
- SGB IV § 28e, StGB § 266a für Arbeitnehmeranteile.
- AO §§ 34, 69, 370 bei Steuer-/Erklärungspflichten.
- GmbHG § 43, AktG § 93 sowie ggf. § 64 GmbHG a.F. für Altfälle.

## Ausgabe

Ampel mit Datum, Betrag, Gläubiger, Rechtsrisiko, Beleg, Entscheidung und Verantwortlichem. Zahlungen an verbundene Unternehmen, Gesellschafter und nahestehende Personen gesondert markieren.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->
