---
name: ai-act-compliance-open-legal-products
title: Tekoälyasetuksen vaatimustenmukaisuus — määräajat, sakot, GPAI, FRIA
description: 'Support EU AI Act (Regulation (EU) 2024/1689) compliance timing and risk assessment: phased application deadlines, maximum administrative fines under Article 99, the GPAI systemic-risk threshold, and the fundamental rights impact assessment (FRIA, Article 27).'
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/assistant-workflows/finnish-law-pack/ai-act-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# Tekoälyasetuksen vaatimustenmukaisuus — määräajat, sakot, GPAI, FRIA

## Ohjeet

Tue vaatimustenmukaisuuden ajoitusta ja riskien arviointia EU:n tekoälyasetuksen (asetus (EU) 2024/1689) mukaan. Tämä työnkulku tuottaa tarkistettavan ensiarvion, ei oikeudellista neuvontaa — sakkojen ja luokittelun lopullinen arvio kuuluu ihmisasiantuntijalle.

Määräajat ja luvut ovat kiinteitä, eivät arvioita: soveltamisen siirtymäajat ja seuraamusten enimmäismäärät tulevat asetuksesta. Jos käytettävissä on tekoälyasetuksen hakulähde (esimerkiksi EUR-Lex tai muu oikeudellinen hakutyökalu), hae päivämäärät, sakkojen enimmäismäärät ja kynnysarvot aina ajantasaisesta lähteestä ennen lopullista vastausta — asetuksen soveltaminen on vaiheittaista (2025–2027) ja tilanne muuttuu. Jos hakulähdettä ei ole käytettävissä, älä esitä lukuja tai päivämääriä varmistettuina: merkitse ne muotoon [tarkistettava] ja pyydä käyttäjää toimittamaan ajantasainen asetusteksti.

### Tehtävä 1: Määräajat ja siirtymäajat

Selvitä käyttäjän tilanteeseen osuvat soveltamisen virstanpylväät ja seuraava määräpäivä lähteestä. Jos jokin muutos (esim. EU-tason keventämisehdotus) on vasta ehdotus eikä voimassa olevaa lakia, sano se selvästi: voimassa olevat päivät ovat ratkaisevia neuvonnassa, kunnes muutos on hyväksytty ja julkaistu EU:n virallisessa lehdessä.

### Tehtävä 2: Seuraamukset (99 art)

Selvitä rikkomustyyppi, liikevaihto ja pk-status. Esitä 99 artiklan mukainen enimmäissakko lähteestä ja pk-yritysten ja startupien kevennys (99(6) art) vertailuna. Korosta, että kyseessä on enimmäismäärä, ei ennuste viranomaisen tosiasiassa määräämästä seuraamuksesta.

### Tehtävä 3: Yleiskäyttöisen mallin (GPAI) systeeminen riski

Arvioi lähteen avulla, ylittääkö malli systeemisen riskin kynnyksen (asetuksessa laskentamääräkynnys 10^25 FLOPs — vahvista lähteestä). Raportoi seuraukset: 53 artiklan perustason velvoitteet, 55 artiklan systeemisen riskin lisävelvoitteet ja 52 artiklan ilmoitusvelvollisuus komissiolle.

### Tehtävä 4: FRIA — perusoikeusvaikutusten arviointi (27 art)

Selvitä, onko käyttöönottaja FRIA-velvollinen. Laukaisijoita ovat mm. Annex III(5)(b) (luottokelpoisuuden arviointi ja luottoluokitus) ja Annex III(5)(c) (henki- ja sairausvakuutuksen riskinarviointi ja hinnoittelu); Annex III(2) (kriittinen infrastruktuuri) on vapautettu. Jos FRIA tarvitaan, ohjaa sen sisältöön: käyttöprosessin kuvaus, vaikutukset perusoikeuksiin, riskit ja lieventävät toimet. FRIA ja GDPR:n vaikutustenarviointi (DPIA, 35 art) limittyvät — muistuta rinnakkaisesta tietosuoja-arviosta.

### Tehtävä 5: Raportoi

Tuota selkeä yhteenveto haetuista luvuista ja päivistä lähdemerkinnöin (EUR-Lex), ja merkitse tulkinnanvaraiset kohdat [varmista — asiantuntijan arvioitava]. Muistuta kansallisen kerroksen tarkistuksesta: Suomen toimivaltaiset viranomaiset ja täytäntöönpanon yksityiskohdat ovat muotoutumassa — merkitse [varmista — kansallinen sääntely muotoutumassa].

## Rajaukset

- Ei tee lopullista vaatimustenmukaisuus- tai luokittelupäätöstä — sitova arvio kuuluu asiantuntijalle.
- Ei esitä määräpäiviä eikä sakkoja muistista — aina lähteestä tai [tarkistettava].
- Ei ennusta todellista seuraamusta — 99 artiklan luvut ovat enimmäismääriä.
- Ei kohtele ehdotuksia voimassa olevana lakina — muutos on suuntaa-antava, kunnes se on hyväksytty ja julkaistu virallisessa lehdessä.
- Ei vahvista kansallisia viranomaisnimeämisiä eikä täytäntöönpanon yksityiskohtia.
- Ei kirjoita FRIA- tai DPIA-asiakirjaa valmiiksi — tunnistaa velvollisuuden ja ohjaa rakenteeseen; varsinainen arviointi jää organisaatiolle.
