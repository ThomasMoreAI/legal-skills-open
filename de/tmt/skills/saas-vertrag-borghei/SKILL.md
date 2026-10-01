---
name: saas-vertrag-borghei
title: /it-recht:saas-vertrag
description: 'Prüfung von Software-as-a-Service-Verträgen: vertragstypologische Einordnung als Mietvertrag (§ 535 BGB, BGH zu ASP), Mängelrechte des Mietrechts (§ 536 BGB), Service Level Agreement/Verfügbarkeit, Datenexport und AGB-Inhaltskontrolle (§§ 305, 307, 310 BGB). Use when ein SaaS- oder Cloud-Nutzungsvertrag bewertet, verhandelt oder gestaltet wird.'
author: borghei
author_url: https://github.com/borghei/AI-Skills-German-Law/tree/main/it-recht/skills/saas-vertrag
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: tmt
language: de
---

# /it-recht:saas-vertrag

## Zweck

Beim Software-as-a-Service überlässt der Anbieter dem Kunden Software zur zeitlich begrenzten Nutzung über das Netz; die Software verbleibt auf den Servern des Anbieters. Dieser Skill ordnet den Vertrag rechtlich ein, prüft die Verfügbarkeits- und Mängelregelungen am Maßstab des Mietrechts und unterzieht die typischen Klauseln der AGB-Inhaltskontrolle. Ziel ist eine belastbare Risikoeinschätzung für Anbieter wie Kunden.

## Eingaben

- Vertragsrolle (Anbieter / Kunde)
- Vertragsdokument oder Klauselauszüge (Verfügbarkeit, Haftung, Beendigung)
- Größenklasse (B2B / B2C)
- Vereinbarte Verfügbarkeitsquote und etwaige Service-Level-Anlage
- Regelung zu Datenexport und Datenlöschung bei Vertragsende

## Sub-Agent-Architektur

Die Prüfung wird gedanklich auf drei Rollen verteilt, die nacheinander arbeiten. Ein **Einordnungs-Agent** bestimmt zunächst den Vertragstyp und das anwendbare Gewährleistungsregime, weil davon Mängelrechte und Verjährung abhängen. Ein **AGB-Agent** prüft sodann jede vorformulierte Klausel isoliert gegen §§ 305 ff. BGB und markiert Verstöße gegen das Klauselverbot. Ein **Risiko- und Verhandlungs-Agent** bündelt schließlich Verfügbarkeit, Haftung und Beendigung zu einer Empfehlung. Die Rollen tauschen nur strukturierte Zwischenergebnisse aus; Quelle bleibt stets der konkrete Vertragstext, nicht eine Vermutung über die Branchenüblichkeit.

## Ablauf

### 1. Vertragstypologische Einordnung

Der BGH ordnet die entgeltliche Überlassung von Software auf Zeit (ASP/SaaS) dem Mietrecht zu, weil der Schwerpunkt in der Gebrauchsüberlassung liegt (BGH, Urt. v. 15.11.2006 – XII ZR 120/04, NJW 2007, 2394 — ASP-Vertrag ist Mietvertrag, [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2006-11-15&Aktenzeichen=XII%20ZR%20120/04)). Maßgeblich ist damit § 535 BGB: Der Anbieter schuldet die fortlaufende Gewährung des vertragsgemäßen Gebrauchs während der gesamten Laufzeit, nicht nur eine einmalige Bereitstellung. Implementierungs-, Customizing- oder Schulungsanteile können zu einem typengemischten Vertrag mit werkvertraglichen Elementen führen und sind gesondert auszuweisen.

### 2. Mängelrechte und Verfügbarkeit

Aus der mietrechtlichen Einordnung folgt das Gewährleistungsregime des § 536 BGB: Bei einem Mangel, der die Tauglichkeit zum vertragsgemäßen Gebrauch aufhebt oder mindert, ist die Vergütung kraft Gesetzes gemindert. Die vereinbarte **Verfügbarkeit** (z. B. 99,5 % im Monatsmittel) konkretisiert den geschuldeten Gebrauch; ihre Unterschreitung ist ein Mangel im Sinne des § 536 BGB. Zu prüfen sind Berechnungsmethodik, Wartungsfenster (geplant/ungeplant) und ob ein formularmäßiger Ausschluss der gesetzlichen Minderung vorliegt — ein solcher ist in AGB unwirksam.

### 3. Service Level Agreement

Das **Service Level Agreement** sollte die Verfügbarkeit, Reaktions- und Wiederherstellungszeiten, Messpunkte sowie Sanktionen (Gutschriften, Sonderkündigungsrecht) klar definieren. Pauschale Service-Gutschriften dürfen die gesetzlichen Mängelrechte nicht abschneiden, sondern nur ergänzen.

### 4. Datenexport und Beendigung

Zentral ist die Regelung zum **Datenexport**: Herausgabe der Kundendaten in einem strukturierten, gängigen, maschinenlesbaren Format, ohne Zusatzentgelt, mit angemessenem Übergangszeitraum und anschließendem Löschnachweis. Fehlt sie, droht eine faktische Bindung an den Anbieter.

### 5. AGB-Inhaltskontrolle (§§ 305, 307, 310 BGB)

Anbietervorlagen sind AGB. Über § 310 Abs. 1 BGB gelten § 305c und § 307 BGB auch im B2B-Verkehr. Typische Bruchstellen:

- formularmäßiger Ausschluss der Minderung nach § 536 BGB → § 307 BGB, unwirksam;
- Haftungsausschluss für Kardinalpflichten bei einfacher Fahrlässigkeit → § 307 BGB;
- einseitiges Leistungsänderungsrecht ohne Anlass und Zumutbarkeitsgrenze → § 308 Nr. 4 BGB;
- intransparente Verfügbarkeitsdefinition → Transparenzgebot § 307 Abs. 1 S. 2 BGB.

## Risiken

- **Verfügbarkeit** ohne Messmethodik oder mit verstecktem Ausschluss der Minderung nach § 536 BGB — der Mangelbegriff läuft leer.
- **Datenexport** fehlt oder ist kostenpflichtig — Vendor Lock-in und Verlust der Verhandlungsmacht bei Vertragsende.
- **Haftungsbegrenzung** zu weit (Kardinalpflichten, grobe Fahrlässigkeit, Leib/Leben erfasst) — unwirksam nach § 307, § 309 Nr. 7 BGB.
- **Vendor Lock-in** durch proprietäre Formate ohne Exportschnittstelle und ohne Mitwirkungspflicht im Übergang.
- Vertragstyp ungeprüft als „Dienstvertrag" deklariert, obwohl Gebrauchsüberlassung überwiegt — falsches Mängel- und Verjährungsregime.

## Ausgabeformat

```
SaaS-VERTRAGSPRÜFUNG — <Vertragsbezeichnung> — <Datum>

I.   Vertragstypologische Einordnung   [Miete § 535 BGB / typengemischt]
     Begründung / Rechtsprechung:       <ASP = Miete, XII ZR 120/04>
II.  Mängelrechte & Verfügbarkeit       [§ 536 BGB — Minderung erhalten? ✓/❌]
     Verfügbarkeitsquote / Methodik:    <…>
III. Service Level Agreement            [vollständig / lückenhaft]
     Sanktionen:                        <…>
IV.  Datenexport / Beendigung           [✓ / 🔴 fehlt]
     Löschnachweis:                     [✓ / 🔴]
V.   AGB-Kontrolle (§§ 305, 307, 310)   [✓ / ⚠️ / ❌]
     Problemklauseln:                   <…>
VI.  Haftung                            [Cap / Ausnahmen vollständig?]

Verhandlungsempfehlung:                 <…>
```

## Quellen

- [§ 535 BGB](https://www.gesetze-im-internet.de/bgb/__535.html), [§ 536 BGB](https://www.gesetze-im-internet.de/bgb/__536.html)
- [§ 305 BGB](https://www.gesetze-im-internet.de/bgb/__305.html), [§ 307 BGB](https://www.gesetze-im-internet.de/bgb/__307.html), [§ 310 BGB](https://www.gesetze-im-internet.de/bgb/__310.html)
- BGH, Urt. v. 15.11.2006 – XII ZR 120/04, NJW 2007, 2394 = MMR 2007, 243 (ASP-Vertrag = Mietvertrag), [dejure.org](https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=2006-11-15&Aktenzeichen=XII%20ZR%20120/04)
