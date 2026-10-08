---
name: share-deal-spa-borghei
title: /m-a-transaktionsrecht:share-deal-spa
description: Gestaltung und Prüfung des Anteilskaufvertrags über GmbH-Geschäftsanteile (Share Deal / SPA) – notarielle Form der Abtretung § 15 Abs. 3 GmbHG und der Verpflichtung § 15 Abs. 4 GmbHG mit Heilung durch den Abtretungsvertrag, Bestimmtheit des Kaufgegenstands, Kaufpreismechanik (Locked Box, Closing Accounts, Earn-out), aufschiebende Bedingungen und Signing/Closing-Struktur, Gesellschafterliste § 40 GmbHG, Legitimationswirkung § 16 Abs. 1 GmbHG, gutgläubiger Erwerb § 16 Abs. 3 GmbHG und Vinkulierung § 15 Abs. 5 GmbHG. Use when ein GmbH-Anteilskaufvertrag entworfen, verhandelt, auf Formwirksamkeit geprüft oder eine Closing-Checkliste erstellt werden soll.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/m-a-transaktionsrecht/skills/share-deal-spa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: corporate
language: de
---

# /m-a-transaktionsrecht:share-deal-spa

## Zweck

Der Share Deal überträgt das Unternehmen mittelbar durch Übertragung der Geschäftsanteile — der Rechtsträger bleibt identisch, sämtliche Verträge, Genehmigungen und Verbindlichkeiten laufen unverändert weiter. Das ist die Stärke der Struktur und zugleich ihr Risiko: Der Käufer erwirbt jede Altlast mit. Dieser Skill baut den **Anteilskaufvertrag (Share Purchase Agreement, SPA)** auf, sichert die **notarielle Form** und strukturiert **Signing und Closing**.

## Eingaben

- Zielgesellschaft: Rechtsform, Registergericht und HRB-Nummer, Stammkapital, aktuelle Gesellschafterliste
- Verkäuferstruktur: ein oder mehrere Verkäufer, gesamtschuldnerisch oder pro rata haftend, Familienstand und güterrechtliche Zustimmung (§ 1365 BGB)
- Kaufgegenstand: laufende Nummern der Geschäftsanteile nach der im Handelsregister aufgenommenen Liste, Nennbeträge, Gewinnbezugsrecht ab welchem Stichtag
- Kaufpreismechanik: Locked Box (mit Locked-Box-Datum) oder Closing Accounts, Earn-out-Parameter, Escrow
- Gesellschaftsvertrag: Vinkulierung, Vorerwerbsrechte, Andienungspflichten, Nachfolgeklauseln
- Aufschiebende Bedingungen: Fusionskontrolle, Investitionsprüfung (AWV), Gremienzustimmungen, Change-of-Control-Konsente
- Fristen: Long-Stop-Date, Closing-Termin, Wiedervorlage für Rücktrittsrechte

## Sub-Agent-Architektur

1. **Researcher** ([`../../agents/researcher.md`](../../agents/researcher.md)) liefert §§ 15, 16, 40 GmbHG, die Formrechtsprechung zum Gesamtbeurkundungsgrundsatz und Kommentarstellen zur Vinkulierung.
2. **Drafter** ([`../../agents/drafter.md`](../../agents/drafter.md)) entwirft Kaufgegenstand, Kaufpreisklausel, Closing-Conditions und Closing Actions und formuliert die Vollzugsbestätigung.
3. **Reviewer** ([`../../agents/reviewer.md`](../../agents/reviewer.md)) prüft Formwirksamkeit, Vollständigkeit der Anlagen, Gesellschafterlisten-Kette und ob jede Closing Condition einen Verantwortlichen und ein Datum hat.

## Ablauf

### 1. Formprüfung ([§ 15 Abs. 3 und Abs. 4 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__15.html))

Die klassische Falle liegt in der Doppelung: **beide** Rechtsgeschäfte sind formbedürftig.

- **§ 15 Abs. 3 GmbHG** — die dingliche **Abtretung** des Geschäftsanteils bedarf eines in notarieller Form geschlossenen Vertrags.
- **§ 15 Abs. 4 S. 1 GmbHG** — der notariellen Form bedarf **auch** die schuldrechtliche **Verpflichtung** zur Abtretung. Ein privatschriftliches SPA ist nach § 125 BGB nichtig.
- **§ 15 Abs. 4 S. 2 GmbHG — Heilung:** Eine ohne Form getroffene Vereinbarung wird durch den formgerecht geschlossenen Abtretungsvertrag gültig. Die Heilung wirkt **ex nunc** und erfasst nur den Anteil, der tatsächlich abgetreten wird; sie rettet weder eine bereits gescheiterte Transaktion noch Nebenabreden, die vor der Abtretung erfüllt sein sollten.
- **Gesamtbeurkundungsgrundsatz:** Alle Abreden, die nach dem Willen der Parteien Teil des Vertrags sein sollen, müssen mitbeurkundet werden — auch Nebenabreden in separaten Dokumenten (Wettbewerbsverbot, Beraterverträge, Gesellschaftervereinbarung, Darlehensablösungen). Anlagen werden entweder verlesen oder nach § 14 BeurkG als **Bezugsurkunde** beigefügt. Wird eine Abrede bewusst aus der Urkunde herausgehalten, droht Gesamtnichtigkeit `[unverifiziert - prüfen]`.
- **Auslandsbeurkundung** (typisch Schweiz, Basel/Zürich): in der Praxis verbreitet, in der Wirksamkeit umstritten und seit der Digitalisierung der Gesellschafterlisten praktisch riskant — im Zweifel im Inland beurkunden.

### 2. Kaufgegenstand — Bestimmtheit

Der Anteil ist so zu bezeichnen, dass er zweifelsfrei identifizierbar ist: **laufende Nummer** nach der zuletzt im Handelsregister aufgenommenen Gesellschafterliste, Nennbetrag, Gesellschaft mit HRB-Nummer und Registergericht.

> „Der Verkäufer verkauft und tritt hiermit an den dies annehmenden Käufer den Geschäftsanteil mit der laufenden Nummer [N] im Nennbetrag von EUR [Betrag] an der [Firma] mit Sitz in [Ort], eingetragen im Handelsregister des Amtsgerichts [Ort] unter HRB [Nummer], ab — einschließlich des Gewinnbezugsrechts für das Geschäftsjahr [Jahr] und für alle nachfolgenden Geschäftsjahre sowie sämtlicher Gewinnvorträge und noch nicht ausgeschütteter Gewinne früherer Geschäftsjahre."

**Prüfpunkte:** Sind alle Anteile erfasst (auch nach Kapitalerhöhung entstandene)? Sind Nebenrechte (Nießbrauch, Pfandrecht, Treuhand, Unterbeteiligung) offengelegt und freigegeben? Stimmt die Summe der Nennbeträge mit dem Stammkapital überein?

### 3. Kaufpreismechanik

| Mechanik | Funktionsweise | Risikoverteilung |
|---|---|---|
| **Locked Box** | Fester Preis auf Basis eines vergangenen Stichtagsabschlusses; wirtschaftlicher Übergang bereits zum Locked-Box-Datum; Schutz durch **No-Leakage-Zusage** mit Euro-für-Euro-Erstattung | Käufer trägt das Geschäftsrisiko ab Locked-Box-Datum; Preissicherheit für beide Seiten |
| **Closing Accounts** | Vorläufiger Preis bei Closing, Anpassung anhand eines Stichtagsabschlusses (Net Debt, Working Capital, ggf. Cash-free/Debt-free) | Verkäufer trägt das Risiko bis Closing; Streitpotenzial in der Abschlusserstellung — Schiedsgutachter nach § 317 BGB vorsehen |
| **Earn-out** | Teil des Preises abhängig von künftigen Kennzahlen (EBIT, Umsatz, Meilenstein) | Verlagert Bewertungsrisiko; braucht zwingend Schutzklauseln zur Geschäftsführung in der Earn-out-Periode |

**Leakage** ist abschließend zu definieren (Ausschüttungen, Gesellschafterdarlehen, Boni, Beraterhonorare, Verzichte) und von **Permitted Leakage** (im Vorfeld vereinbart und beziffert) abzugrenzen. Beim Earn-out gehören in den Vertrag: die Berechnungsformel mit Rechenbeispiel als Anlage, die anzuwendenden Bilanzierungsregeln, ein Verwässerungsschutz gegen konzerninterne Umlagen und ein Streitentscheidungsmechanismus.

### 4. Signing und Closing — aufschiebende Bedingungen

Fallen Signing und Closing auseinander, wird die Abtretung **aufschiebend bedingt** (§ 158 Abs. 1 BGB) auf den Eintritt der Closing Conditions und die vollständige Kaufpreiszahlung erklärt. Typische Bedingungen:

1. **Fusionskontrollfreigabe** — Vollzugsverbot § 41 GWB / Art. 7 FKVO; siehe `/kartellrecht:gwb-zusammenschluss-anmeldung`
2. **Investitionsprüfung** nach AWG/AWV bei ausländischem Erwerber
3. **Gesellschafterbeschlüsse** und Zustimmung nach Vinkulierungsklausel
4. **Change-of-Control-Konsente** wesentlicher Vertragspartner und Kreditgeber
5. **Ablösung der Finanzierung**, Freigabe von Sicherheiten, Rückführung von Gesellschafterdarlehen
6. **MAC-Klausel** (Material Adverse Change) — nur mit objektiv messbarem Schwellenwert brauchbar

**Long-Stop-Date** mit beidseitigem Rücktrittsrecht setzen. Die Frist rechnet der Fristenrechner:

```bash
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 1 --einheit monate --land BY
```

Der Rechner leistet ausschließlich die Arithmetik der §§ 187–193 BGB. **Fristbeginn und Zugang bleiben rechtliche Eingaben** — ob eine Freigabe zugegangen ist und wann die Bedingung eingetreten ist, entscheidet der Bearbeiter, nicht das Werkzeug.

### 5. Closing Actions und Gesellschafterliste ([§ 40 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__40.html))

Am Closing werden in festgelegter Reihenfolge abgearbeitet: Bedingungseintritt bestätigen → Kaufpreis zahlen → Abtretung wirksam → Geschäftsführerwechsel beschließen und anmelden → Bankvollmachten ändern → Vollzugsprotokoll unterzeichnen.

Nach § 40 Abs. 2 GmbHG reicht der **mitwirkende Notar** die geänderte Gesellschafterliste unverzüglich zum Handelsregister ein und versieht sie mit der Notarbescheinigung. Die Verletzung der Einreichungspflicht löst nach § 40 Abs. 3 GmbHG eine gesamtschuldnerische Haftung der Geschäftsführer gegenüber Betroffenen und Gläubigern aus.

### 6. Legitimations- und Gutglaubenswirkung ([§ 16 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__16.html))

- **§ 16 Abs. 1 S. 1 GmbHG — Legitimationswirkung:** Im Verhältnis zur Gesellschaft gilt als Inhaber **nur**, wer in der im Handelsregister aufgenommenen Liste eingetragen ist. Vor Aufnahme der Liste kann der Erwerber weder Stimmrechte ausüben noch Gewinn beanspruchen. § 16 Abs. 1 S. 2 GmbHG heilt rückwirkend, wenn die Liste **unverzüglich** nach der Rechtshandlung aufgenommen wird — deshalb keine Gesellschafterbeschlüsse des Erwerbers vor Listenaufnahme ohne diese Rückwirkungsoption.
- **§ 16 Abs. 2 GmbHG:** Der Erwerber haftet neben dem Veräußerer für rückständige Einlageverpflichtungen. Die Volleinzahlung ist in der Due Diligence zu belegen und im Garantiekatalog abzusichern.
- **§ 16 Abs. 3 GmbHG — gutgläubiger Erwerb:** möglich, wenn der Veräußerer in der aufgenommenen Liste eingetragen ist. **Ausgeschlossen**, wenn die Liste hinsichtlich des Anteils weniger als **drei Jahre** unrichtig und die Unrichtigkeit dem Berechtigten nicht zuzurechnen ist, wenn dem Erwerber die fehlende Berechtigung bekannt oder grob fahrlässig unbekannt ist oder wenn der Liste ein **Widerspruch** zugeordnet ist. Der gutgläubige Erwerb ersetzt daher **keine** Prüfung der Anteilskette — er ist Auffangnetz, nicht Prüfungsverzicht.

### 7. Vinkulierung und flankierende Regelungen

**Vinkulierung (§ 15 Abs. 5 GmbHG):** Der Gesellschaftsvertrag kann die Abtretung an weitere Voraussetzungen knüpfen, insbesondere an die Genehmigung der Gesellschaft. Fehlt die Zustimmung, ist die Abtretung schwebend unwirksam. Der Zustimmungsbeschluss ist **vor** oder **im** Closing zu fassen und der Urkunde beizufügen. Ebenso zu prüfen: Vorerwerbs- und Andienungsrechte, Mitverkaufsrechte (Tag-along) und Mitverkaufspflichten (Drag-along).

Flankierend gehören in das SPA: Wettbewerbs- und Abwerbeverbot (zeitlich, räumlich und gegenständlich begrenzt — kartellrechtliche Grenzen beachten), Rangrücktritt oder Ablösung von Gesellschafterdarlehen (`/gesellschaftsrecht:kapitalerhaltung`), Freistellung ausscheidender Geschäftsführer, Steuerklauseln (`/steuerrecht:aussenpruefung-betriebspruefung`), Vertraulichkeit, Rechtswahl und Gerichtsstand oder Schiedsklausel.

## Quellen

### Statute

- [§ 15 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__15.html) (Abs. 3 Abtretung, Abs. 4 Verpflichtung und Heilung, Abs. 5 Vinkulierung)
- [§ 16 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__16.html) (Abs. 1 Legitimation, Abs. 2 Einlagenhaftung, Abs. 3 gutgläubiger Erwerb)
- [§ 40 GmbHG](https://www.gesetze-im-internet.de/gmbhg/__40.html) (Gesellschafterliste, Notarbescheinigung, Haftung)
- [§ 125 BGB](https://www.gesetze-im-internet.de/bgb/__125.html), [§ 158 BGB](https://www.gesetze-im-internet.de/bgb/__158.html), [§ 317 BGB](https://www.gesetze-im-internet.de/bgb/__317.html), [§ 1365 BGB](https://www.gesetze-im-internet.de/bgb/__1365.html)
- [§ 41 GWB](https://www.gesetze-im-internet.de/gwb/__41.html) (Vollzugsverbot)

### Kommentare

- Löbbe, in: Ulmer/Habersack/Löbbe, GmbHG, 3. Aufl. 2021, § 15 Rn. 1 ff. (Form, Gesamtbeurkundung) `[unverifiziert - Auflagenstand prüfen]`
- Seibt, in: Scholz, GmbHG, 13. Aufl. 2022, § 15 Rn. 60 ff.; § 16 Rn. 1 ff. `[unverifiziert - Auflagenstand prüfen]`
- Altmeppen, GmbHG, 11. Aufl. 2023, § 16 Rn. 1 ff. (Legitimation, gutgläubiger Erwerb)

### Rechtsprechung

- BGH, Urt. v. 20.09.2011 – II ZR 234/09 (Gesellschafterliste und § 16 GmbHG) `[unverifiziert - prüfen]`
- BGH, Urt. v. 17.12.2013 – II ZR 21/12 (Widerspruch zur Gesellschafterliste) `[unverifiziert - prüfen]`

> Beide Aktenzeichen vor Verwendung in juris / Beck-Online prüfen. Die tragenden Aussagen dieses Skills folgen unmittelbar aus dem Gesetzeswortlaut der §§ 15, 16, 40 GmbHG.

## Ausgabeformat

```
SHARE DEAL / SPA — <Zielgesellschaft> — <Datum>

I.    Transaktionsstruktur          [Share Deal — Verkäufer: <…> / Käufer: <…>]
II.   Form § 15 Abs. 3, 4 GmbHG     [Beurkundung geplant am <…> / Heilung § 15 IV 2 erforderlich?]
        Gesamtbeurkundung:          [alle Nebenabreden erfasst ✅ / 🔴 Lücke: <…>]
III.  Kaufgegenstand                [lfd. Nr. <…>, Nennbetrag EUR <…>, Gewinnbezug ab <…>]
        Belastungen:                [frei / Pfandrecht / Nießbrauch / Treuhand]
IV.   Kaufpreis                     [Locked Box zum <…> / Closing Accounts / Earn-out]
        Leakage-Schutz:             [✅ / ❌]  Escrow: [<Betrag>, Laufzeit <…>]
V.    Closing Conditions            1. <…> [Verantwortlich / Zieldatum]
                                    2. <…>
        Long-Stop-Date:             <TT.MM.JJJJ>  Rücktritt: [beidseitig / einseitig]
VI.   Closing Actions               <nummerierte Reihenfolge>
VII.  Gesellschafterliste § 40      [Notar reicht ein — Aufnahme erwartet am <…>]
VIII. § 16 GmbHG                    Legitimation: [ab Listenaufnahme]
                                    Gutglaubensschutz Abs. 3: [tragfähig / 🔴 Kette prüfen]
IX.   Vinkulierung § 15 Abs. 5      [keine / Zustimmung erforderlich — Beschluss vom <…>]
X.    Nebenabreden                  [Wettbewerbsverbot / Gesellschafterdarlehen / Steuerklausel]

Gesamtbefund: [🟢 / 🟡 / 🔴]
Offene Punkte: <Liste>
```

## Risiken / typische Fehler

- **Nur die Abtretung beurkundet, die Verpflichtung nicht** — oder umgekehrt eine privatschriftliche Vorvereinbarung, die bereits bindet. § 15 Abs. 4 S. 2 GmbHG heilt erst mit der Abtretung und nur ex nunc; bis dahin ist das SPA nichtig.
- **Nebenabreden aus der Urkunde herausgehalten** — Verstoß gegen den Gesamtbeurkundungsgrundsatz mit dem Risiko der Gesamtnichtigkeit; Anlagen als Bezugsurkunde nach § 14 BeurkG beifügen.
- **Vinkulierung im Gesellschaftsvertrag übersehen** — die Abtretung bleibt schwebend unwirksam, obwohl der Kaufpreis geflossen ist.
- **Gesellschafterliste nicht als Anspruchsvoraussetzung behandelt** — vor Aufnahme der Liste kann der Erwerber nach § 16 Abs. 1 GmbHG weder abstimmen noch Gewinn verlangen; Beschlüsse sind fehlerhaft.
- **Auf § 16 Abs. 3 GmbHG als Ersatz für die Anteilskettenprüfung vertraut** — der Gutglaubensschutz greift bei Widerspruch, Kenntnis, grober Fahrlässigkeit und innerhalb der Dreijahresfrist gerade nicht.
- **Vollzug vor der Fusionskontrollfreigabe** — Verstoß gegen das Vollzugsverbot des § 41 GWB mit Bußgeld- und Unwirksamkeitsfolge.
- **Earn-out ohne Schutz der Geschäftsführung** — der Käufer kann die Bemessungsgrundlage nach Closing steuern; ohne Verwässerungsschutz und Streitmechanismus ist der Anspruch wertlos.
- **Rückständige Einlagen nicht geprüft** — der Erwerber haftet nach § 16 Abs. 2 GmbHG neben dem Veräußerer.
