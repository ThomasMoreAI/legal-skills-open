---
name: betriebskostenabrechnung-borghei
title: /mietrecht:betriebskostenabrechnung
description: Prüfung und Erstellung der Betriebskostenabrechnung im Wohnraummietrecht – Umlagevereinbarung und Abrechnungspflicht § 556 BGB, Abrechnungsfrist § 556 Abs. 3 S. 2 BGB und Einwendungsfrist § 556 Abs. 3 S. 5 BGB, Umlagemaßstab § 556a BGB, Betriebskostenkatalog der BetrKV, HeizkostenV, Belegeinsicht, Abgrenzung formeller und materieller Fehler, Wirtschaftlichkeitsgebot, CO2KostAufG mit Stufenmodell seit 2023. Use when eine Betriebskostenabrechnung erstellt, geprüft oder eine Nachforderung bzw. ein Guthaben durchgesetzt wird.
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/mietrecht/skills/betriebskostenabrechnung
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: real-estate
language: de
---

# /mietrecht:betriebskostenabrechnung

## Zweck

Die Betriebskostenabrechnung ist die häufigste mietrechtliche Streitursache und die mit den härtesten Ausschlussfristen: Wer die **12-Monats-Abrechnungsfrist** versäumt, verliert die Nachforderung endgültig; wer als Mieter die **12-Monats-Einwendungsfrist** versäumt, kann materielle Fehler nicht mehr rügen. Diese Skill trennt konsequent **formelle** Fehler (die die Abrechnung insgesamt unwirksam machen) von **materiellen** Fehlern (die nur den Saldo korrigieren) und rechnet die Fristen deterministisch nach.

## Eingaben

- **Mietvertrag**: Umlagevereinbarung, vereinbarter Umlagemaßstab, Höhe der Vorauszahlungen
- **Abrechnung** im Wortlaut, Datum des **Zugangs**, Abrechnungszeitraum
- Gesamtkosten je Kostenart, Gesamtumlagemaßstab, Anteil des Mieters, geleistete Vorauszahlungen
- **Heizkostenabrechnung** (Verteilung Verbrauch / Fläche, Ableseprotokolle)
- Angaben zur **Gebäudeenergieeffizienz** (für das CO2-Stufenmodell)
- Leerstand im Abrechnungszeitraum, Nutzerwechsel, gewerbliche Mitnutzung
- Ob **Belegeinsicht** verlangt bzw. gewährt wurde

## Sub-Agent-Architektur

Die Prüfung wird in Prosa von spezialisierten Schritten getragen; einen `agents`-Block trägt diese Skill bewusst nicht (mietrecht-Konvention). Ein **Fristen-Prüfer** stellt zuerst fest, ob Abrechnungs- und Einwendungsfrist gewahrt sind — davon hängt ab, ob eine inhaltliche Prüfung überhaupt noch etwas ändert. Ein **Formal-Prüfer** kontrolliert die Mindestangaben der Abrechnung; ein formeller Fehler macht sie insgesamt unwirksam und die Nachforderung nicht fällig. Ein **Material-Prüfer** untersucht Umlagefähigkeit jeder Kostenart, Umlageschlüssel, Wirtschaftlichkeit und die Heizkostenverteilung. Ein **CO2-Prüfer** bearbeitet gesondert das Stufenmodell des CO2KostAufG. Ein **Beleg-Prüfer** organisiert die Einsichtnahme und das Zurückbehaltungsrecht.

## Ablauf

### 1. Umlagevereinbarung und Abrechnungspflicht ([§ 556 Abs. 1, Abs. 3 S. 1 BGB](https://www.gesetze-im-internet.de/bgb/__556.html))

Betriebskosten sind nur umlagefähig, wenn die Parteien dies **vereinbart** haben; ohne Vereinbarung sind sie mit der Grundmiete abgegolten. Die Bezugnahme auf die **Betriebskostenverordnung** oder auf „Betriebskosten im Sinne des § 556 Abs. 1 BGB" genügt. Über Vorauszahlungen ist **jährlich abzurechnen**; der Abrechnungszeitraum darf zwölf Monate nicht überschreiten. Nicht umlagefähig sind **Verwaltungskosten** und **Instandhaltungs-/Instandsetzungskosten** ([§ 1 Abs. 2 BetrKV](https://www.gesetze-im-internet.de/betrkv/__1.html)).

### 2. Betriebskostenkatalog ([§ 2 BetrKV](https://www.gesetze-im-internet.de/betrkv/__2.html))

Der Katalog des § 2 BetrKV ist **abschließend** für die dort benannten Arten; Nr. 17 („sonstige Betriebskosten") erfasst weitere laufende Kosten nur, wenn sie im Mietvertrag **konkret benannt** sind. Eine pauschale Klausel „und sonstige Betriebskosten" reicht dafür nicht. Prüfe jede Position einzeln: Grundsteuer, Wasser/Entwässerung, Heizung, Warmwasser, Aufzug, Straßenreinigung, Müllbeseitigung, Gebäudereinigung, Gartenpflege, Beleuchtung, Schornsteinreinigung, Sach- und Haftpflichtversicherung, Hauswart, Gemeinschaftsantenne, Wäschepflege.

### 3. Abrechnungsfrist ([§ 556 Abs. 3 S. 2, S. 3 BGB](https://www.gesetze-im-internet.de/bgb/__556.html))

Die Abrechnung ist dem Mieter **spätestens bis zum Ablauf des zwölften Monats nach Ende des Abrechnungszeitraums** mitzuteilen. Nach Ablauf dieser Frist ist die Geltendmachung einer **Nachforderung ausgeschlossen**, es sei denn, der Vermieter hat die verspätete Geltendmachung **nicht zu vertreten** (S. 3). Es handelt sich um eine **materielle Ausschlussfrist** — sie wirkt nur gegen Nachforderungen; ein **Guthaben** bleibt auch bei verspäteter Abrechnung auszukehren, und der Anspruch des Mieters auf Erteilung der Abrechnung besteht fort. Maßgeblich ist der **Zugang** der Abrechnung, nicht die Absendung.

### 4. Formelle Anforderungen — Mindestangaben

Eine formell ordnungsgemäße Abrechnung muss für einen durchschnittlichen Mieter **gedanklich und rechnerisch nachvollziehbar** sein und enthält:

1. Zusammenstellung der **Gesamtkosten** je Kostenart,
2. Angabe und Erläuterung des **Verteilerschlüssels**,
3. **Berechnung des Anteils** des Mieters,
4. Abzug der geleisteten **Vorauszahlungen**,
5. Angabe des **Abrechnungszeitraums**.

Ein **formeller** Fehler macht die Abrechnung **insgesamt unwirksam**; die Nachforderung wird nicht fällig, und nach Ablauf der Abrechnungsfrist ist sie endgültig verloren. Ein **materieller** Fehler (falscher Ansatz, Rechenfehler, nicht umlagefähige Position) lässt die Abrechnung wirksam und führt nur zur Korrektur des Saldos — er kann auch nach Fristablauf zugunsten des Mieters berichtigt werden. Zu den Anforderungen an die Angabe der Gesamtkosten und an Vorwegabzüge: BGH, Urt. v. 20.01.2016 – VIII ZR 93/15, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2016-01-20&Aktenzeichen=VIII%20ZR%2093/15.

### 5. Einwendungsfrist ([§ 556 Abs. 3 S. 5, S. 6 BGB](https://www.gesetze-im-internet.de/bgb/__556.html))

Der Mieter hat Einwendungen gegen die Abrechnung **spätestens bis zum Ablauf des zwölften Monats nach Zugang** der Abrechnung mitzuteilen. Nach Fristablauf kann er Einwendungen nicht mehr geltend machen, es sei denn, er hat die verspätete Geltendmachung nicht zu vertreten. Die Frist läuft **unabhängig** von der Abrechnungsfrist des Vermieters und ist der schärfste Fallstrick auf Mieterseite. Rein **formelle** Mängel und die Frage der Fälligkeit unterfallen der Präklusion nicht.

### 6. Umlagemaßstab ([§ 556a BGB](https://www.gesetze-im-internet.de/bgb/__556a.html))

Ohne abweichende Vereinbarung sind Betriebskosten nach dem **Anteil der Wohnfläche** umzulegen. Kosten, die von einem **erfassten Verbrauch** abhängen, sind nach Verbrauch umzulegen (§ 556a Abs. 1 S. 2 BGB). Der Vermieter kann durch **Erklärung in Textform** auf einen verbrauchsabhängigen Maßstab umstellen; die Umstellung wirkt zum Beginn des folgenden Abrechnungszeitraums (Abs. 2). Für **Heizung und Warmwasser** gilt vorrangig die [HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/): mindestens 50 %, höchstens 70 % nach erfasstem Verbrauch; bei Verstoß Kürzungsrecht des Mieters von **15 %** ([§ 12 HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__12.html)).

### 7. Wirtschaftlichkeitsgebot ([§ 556 Abs. 3 S. 1 Hs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__556.html))

Der Vermieter hat den **Grundsatz der Wirtschaftlichkeit** zu beachten. Er darf nur Kosten ansetzen, die ein vernünftiger Vermieter bei angemessener Berücksichtigung der Mieterinteressen aufgewendet hätte. Der Mieter, der einen Verstoß behauptet, muss konkrete Anhaltspunkte darlegen (etwa deutliche Überschreitung des örtlichen Betriebskostenspiegels); erst dann trifft den Vermieter eine sekundäre Darlegungslast.

### 8. Belegeinsicht und Zurückbehaltungsrecht

Der Mieter kann Einsicht in die **Abrechnungsunterlagen** verlangen; der Anspruch folgt aus § 259 BGB i.V.m. § 242 BGB. Er erstreckt sich auch auf die **Zahlungsbelege** (BGH, Urt. v. 09.12.2020 – VIII ZR 118/19, https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2020-12-09&Aktenzeichen=VIII%20ZR%20118/19). Einsichtsort ist regelmäßig das Büro des Vermieters; Kopien nur gegen Kostenerstattung, außer die Anreise ist unzumutbar. Bis zur Gewährung der Einsicht steht dem Mieter ein **Zurückbehaltungsrecht** nach [§ 273 BGB](https://www.gesetze-im-internet.de/bgb/__273.html) an der Nachzahlung zu.

### 9. CO2-Kostenaufteilung ([CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/), seit 01.01.2023)

Der auf den Brennstoff entfallende **CO2-Preis** nach dem BEHG wird nicht mehr vollständig auf den Mieter umgelegt. Für Wohngebäude gilt ein **Stufenmodell** nach dem spezifischen CO2-Ausstoß des Gebäudes in kg CO2/m² Wohnfläche und Jahr: Je schlechter die energetische Qualität des Gebäudes, desto höher der vom **Vermieter** zu tragende Anteil (bis zu 95 %); bei sehr guter Effizienz trägt der **Mieter** den vollen Anteil. Praktische Anforderungen:

- Der Vermieter muss die **CO2-Kosten in der Abrechnung ausweisen** und die Aufteilung nach dem Stufenmodell **nachvollziehbar darlegen**; die erforderlichen Angaben liefert die Rechnung des Brennstofflieferanten.
- Unterlässt er die Aufteilung, kann der Mieter den auf ihn entfallenden Anteil an den Heizkosten **um 3 %** kürzen.
- Für **Nichtwohngebäude** gilt bis auf Weiteres eine hälftige Teilung.
- Bei rechtlichen Beschränkungen der energetischen Sanierung (Denkmalschutz, Milieuschutz) kann sich der Vermieteranteil ermäßigen.

Die konkreten Stufengrenzen und Prozentsätze sind vor jeder Abrechnung gegen den aktuellen Gesetzestext zu prüfen.

## Deterministische Berechnung

Beide Jahresfristen des § 556 Abs. 3 BGB sind Ereignisfristen nach [§ 187 Abs. 1 BGB](https://www.gesetze-im-internet.de/bgb/__187.html) mit Fristende nach [§ 188 Abs. 2 BGB](https://www.gesetze-im-internet.de/bgb/__188.html); [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html) verschiebt das Ende auf den nächsten Werktag. Der Rechner in [`../../../scripts/legal_calc/`](../../../scripts/legal_calc/) macht **nur die Arithmetik** — das Ende des Abrechnungszeitraums und vor allem der **Zugang** der Abrechnung bleiben juristische Eingaben und sind gesondert nachzuweisen.

```bash
# Abrechnungsfrist § 556 Abs. 3 S. 2 BGB: Abrechnungszeitraum endet 31.12.2025
python -m scripts.legal_calc.cli frist --ereignis 31.12.2025 --menge 12 --einheit monate --land BE

# Einwendungsfrist § 556 Abs. 3 S. 5 BGB: Abrechnung zugegangen am 15.01.2026
python -m scripts.legal_calc.cli frist --ereignis 15.01.2026 --menge 12 --einheit monate --land BE

# Umstellung des Umlagemaßstabs § 556a Abs. 2 BGB: Wirkung zum nächsten Zeitraum
python -m scripts.legal_calc.cli frist --ereignis 31.12.2026 --menge 1 --einheit monate --land BE
```

`--json` liefert die Rechenschritte samt Normzitat. Der Rechner sagt nichts darüber, ob der Vermieter die Verspätung zu vertreten hat (§ 556 Abs. 3 S. 3 BGB) — das bleibt Wertungsfrage.

## Quellen

### Statute

- [§ 556 BGB](https://www.gesetze-im-internet.de/bgb/__556.html), [§ 556a BGB](https://www.gesetze-im-internet.de/bgb/__556a.html), [§ 259 BGB](https://www.gesetze-im-internet.de/bgb/__259.html), [§ 273 BGB](https://www.gesetze-im-internet.de/bgb/__273.html), [§ 242 BGB](https://www.gesetze-im-internet.de/bgb/__242.html)
- [BetrKV](https://www.gesetze-im-internet.de/betrkv/) — [§ 1 BetrKV](https://www.gesetze-im-internet.de/betrkv/__1.html), [§ 2 BetrKV](https://www.gesetze-im-internet.de/betrkv/__2.html)
- [HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/) — [§ 7 HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__7.html), [§ 12 HeizkostenV](https://www.gesetze-im-internet.de/heizkostenv/__12.html)
- [CO2KostAufG](https://www.gesetze-im-internet.de/co2kostaufg/) (Kohlendioxidkostenaufteilungsgesetz, seit 01.01.2023)
- [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html), [§ 188 BGB](https://www.gesetze-im-internet.de/bgb/__188.html), [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html)

### Kommentare

- Langenberg, in: Schmidt-Futterer, Mietrecht, 15. Aufl. 2023, § 556 BGB Rn. 1 ff.
- Zehelein, in: MüKoBGB, 9. Aufl. 2023, § 556 Rn. 1 ff.; § 556a Rn. 1 ff.
- Weidenkaff, in: Grüneberg, BGB, 84. Aufl. 2025, § 556 Rn. 1 ff.
- Wall, Betriebskosten- und Heizkostenabrechnung, aktuelle Auflage (Praxishandbuch)

### Rechtsprechung

- BGH, Urt. v. 20.01.2016 – VIII ZR 93/15 (formelle Anforderungen an die Betriebskostenabrechnung; kein Ausweis der Rechenschritte bei Vorwegabzug) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2016-01-20&Aktenzeichen=VIII%20ZR%2093/15
- BGH, Urt. v. 09.12.2020 – VIII ZR 118/19 (Einsichtsrecht des Mieters in Zahlungsbelege) — verifiziert: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2020-12-09&Aktenzeichen=VIII%20ZR%20118/19
- Zur Reichweite des Wirtschaftlichkeitsgebots und zur Darlegungslast beim Betriebskostenspiegel ist die einschlägige BGH-Rechtsprechung heranzuziehen `[unverifiziert - prüfen]`.

## Formulierungshilfe — Einwendungsschreiben des Mieters

```
Sehr geehrte Damen und Herren,

gegen Ihre Betriebskostenabrechnung für den Zeitraum <…> vom <Datum>,
mir zugegangen am <Datum>, erhebe ich innerhalb der Frist des
§ 556 Abs. 3 S. 5 BGB folgende Einwendungen:

1. Formelle Mängel: Die Abrechnung weist den Verteilerschlüssel für die
   Position <…> nicht aus und ist insoweit nicht nachvollziehbar. Die
   Nachforderung ist daher nicht fällig.
2. Nicht umlagefähige Positionen: Die Position <…> betrifft
   Instandsetzungsaufwand und ist nach § 1 Abs. 2 Nr. 2 BetrKV nicht
   umlagefähig. Die Position "sonstige Betriebskosten" ist im Mietvertrag
   nicht konkret benannt (§ 2 Nr. 17 BetrKV).
3. Heizkosten: Der Verbrauchsanteil beträgt lediglich <…> % und
   unterschreitet die Mindestquote des § 7 HeizkostenV. Ich kürze den
   Heizkostenanteil gemäß § 12 Abs. 1 HeizkostenV um 15 %.
4. CO2-Kosten: Eine Aufteilung nach dem Stufenmodell des CO2KostAufG ist
   nicht ausgewiesen. Ich kürze den Heizkostenanteil um weitere 3 %.
5. Belegeinsicht: Ich beantrage Einsicht in sämtliche Abrechnungsunterlagen
   einschließlich der Zahlungsbelege und schlage den <Datum> vor. Bis zur
   Gewährung mache ich von meinem Zurückbehaltungsrecht nach § 273 BGB
   Gebrauch.

Mit freundlichen Grüßen
```

## Ausgabeformat

```
BETRIEBSKOSTENABRECHNUNG — Prüfung — <Mandat-ID> — <Datum>

I.    Umlagevereinbarung (§ 556 Abs. 1)   [vorhanden / fehlt ❌]
II.   Fristen
      - Abrechnungszeitraum               <von> – <bis>
      - Abrechnungsfrist (12 Monate) Ende <Datum>   [gewahrt / versäumt]
      - Zugang der Abrechnung             <Datum>
      - Einwendungsfrist Ende             <Datum>   [offen / abgelaufen]
III.  Formelle Prüfung                    [✅ / ❌ — Abrechnung insgesamt unwirksam]
      - Gesamtkosten je Kostenart         [✅ / ❌]
      - Verteilerschlüssel angegeben      [✅ / ❌]
      - Anteilsberechnung                 [✅ / ❌]
      - Vorauszahlungen abgezogen         [✅ / ❌]
IV.   Materielle Prüfung je Position      <Tabelle: Position | Betrag | umlagefähig? | Rüge>
      Nicht umlagefähig gesamt            <Betrag>
V.    Umlagemaßstab (§ 556a)              [Fläche / Verbrauch / Einheiten]  [✅ / ⚠️]
VI.   Heizkosten (HeizkostenV)            Verbrauchsanteil <…> %  [50–70 % / Verstoß]
      Kürzung § 12 HeizkostenV            [keine / 15 %]
VII.  CO2KostAufG (Stufenmodell)          Vermieteranteil <…> %  [ausgewiesen / fehlt]
      Kürzung bei fehlender Aufteilung    [keine / 3 %]
VIII. Wirtschaftlichkeitsgebot            [kein Anhalt / Rüge <Position>]
IX.   Belegeinsicht                       [gewährt / verlangt am <Datum>]
      Zurückbehaltungsrecht § 273 BGB     [ja / nein]
X.    Korrigierter Saldo                  Abrechnung: <Betrag>
                                          Korrigiert: <Betrag>  [Nachzahlung / Guthaben]

Ergebnis: <Nachforderung fällig / nicht fällig / ausgeschlossen>
Risiko: [🟢 / 🟡 / 🔴]
```

## Risiken / typische Fehler

- **Abrechnungsfrist versäumt** — die Nachforderung ist nach § 556 Abs. 3 S. 3 BGB endgültig ausgeschlossen; ein Guthaben bleibt gleichwohl auszukehren.
- **Einwendungsfrist versäumt** — der Mieter kann materielle Fehler nicht mehr rügen; formelle Mängel und die Fälligkeitsfrage bleiben davon unberührt.
- **Formelle und materielle Fehler verwechselt** — nur der formelle Fehler macht die Abrechnung insgesamt unwirksam; wer beides gleich behandelt, verschenkt Positionen oder überschätzt die Wirkung einer Rüge.
- **Zugang statt Absendung** — für beide Fristen zählt der Zugang; ohne Zugangsnachweis ist die Frist nicht belegt.
- **Nicht umlagefähige Positionen** — Verwaltungs- und Instandsetzungskosten (§ 1 Abs. 2 BetrKV) sowie nicht konkret benannte „sonstige Betriebskosten" (§ 2 Nr. 17 BetrKV).
- **Heizkostenverteilung unter 50 % Verbrauch** — löst das Kürzungsrecht von 15 % nach § 12 HeizkostenV aus.
- **CO2-Kosten nicht nach dem Stufenmodell aufgeteilt** — Kürzungsrecht des Mieters von 3 %; die Stufengrenzen sind vor jeder Abrechnung am aktuellen CO2KostAufG zu prüfen.
- **Belegeinsicht verweigert** — der Mieter kann die Nachzahlung nach § 273 BGB zurückhalten; die Nachforderung wird faktisch nicht durchsetzbar.
- **Leerstandskosten auf Mieter umgelegt** — der Vermieter trägt den Leerstandsanteil selbst.
