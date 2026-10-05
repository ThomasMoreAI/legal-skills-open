---
name: case-law-summary-open-legal-products
title: Oikeustapauksen referointi
description: 'Structure and summarize a Finnish court decision (KKO, KHO, courts of appeal, Market Court and others): identifiers, legal question, facts, outcome, ratio decidendi, and precedential value, based strictly on the actual decision text.'
author: open-legal-products
author_url: https://github.com/open-legal-products/mike-workflows/tree/main/assistant-workflows/finnish-law-pack/case-law-summary
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fi
practice: litigation
language: en
---

# Oikeustapauksen referointi

Jäsennä tuomioistuinratkaisun olennainen sisältö niin, että sitä voi käyttää ja arvioida luotettavasti. **Referointi perustuu vain ratkaisun varsinaiseen tekstiin** — ei muistiin eikä otsikkotietoon (headnote) yksin.

Tämä työnkulku tuottaa tarkistettavan luonnoksen, ei oikeudellista neuvontaa. Lopullinen arvio kuuluu ihmisjuristille.

## Ohjeet

**Hae ratkaisun varsinainen teksti ensin.** Jos käytettävissä on suomalaisen oikeuden hakulähde (esimerkiksi Finlex-tietokanta tai oikeudellinen hakutyökalu), hae ratkaisu sieltä; muuten lue käyttäjän toimittama ratkaisuteksti. Älä referoi ratkaisua pelkän tunnuksen tai muistikuvan perusteella — ratkaisuselosteen otsikko ei ole sama kuin perustelut. Jos et saa ratkaisua lähteestä, sano se ja pyydä käyttäjää toimittamaan teksti; älä keksi sisältöä.

Etene vaiheittain:

1. **Tunnistetiedot.** Ratkaisutunnus oikeassa muodossa (KKO:VVVV:NN, KHO:VVVV:NN), antopäivä, tuomioistuin ja kokoonpano (esim. täysistunto, jaosto) sekä mahdollinen äänestys.
2. **Oikeuskysymys.** Mihin oikeudelliseen kysymykseen ratkaisu vastaa? Muotoile täsmällisesti — tämä ohjaa koko referaatin.
3. **Faktat ja prosessihistoria.** Vain ratkaisun kannalta merkitykselliset tosiseikat sekä alempien asteiden ratkaisut pääpiirteittäin (käräjäoikeus → hovioikeus → KKO; tai hallinto-oikeus → KHO).
4. **Lopputulos.** Mitä tuomioistuin päätti (valitus hyväksyttiin/hylättiin, alempi ratkaisu pysytettiin/kumottiin). Erota lopputulos perusteluista.
5. **Perustelujen ydin (ratio decidendi).** Oikeusohje, jonka tuomioistuin asetti ratkaisun perustaksi. Erota ratio ja obiter: kaikki perusteluissa lausuttu ei ole kantava oikeusohje — merkitse, mikä on ydin ja mikä sivuhuomautus. Viittaa numeroituihin perustelukohtiin; erota suora lainaus omasta tiivistyksestä. Äänestysratkaisussa erota enemmistön perustelut ja eri mieltä olleiden kannat.
6. **Merkitys ja soveltuvuus.** Prejudikaattiarvo: mihin oikeusohje yleistyy ja mihin ei. Soveltuvuus käyttäjän tapaukseen: mitkä faktat ovat samanlaiset, mitkä erottavat (distinguishing). Älä ylitulkitse — yhden ratkaisun ohje on sidoksissa sen kysymyksenasetteluun. Tarkista, ettei oikeusohje perustu sittemmin kumottuun tai muutettuun säännökseen; jos ajantasaisuutta ei voi tarkistaa hakulähteestä, merkitse se [tarkistettava].
7. **Koottu referaatti.** Tuota jäsennelty referaatti yllä olevin otsikoin. Merkitse, mikä on suoraa ratkaisutekstiä ja mikä omaa tulkintaa soveltuvuudesta. Kun kokoat useita ratkaisuja, esitä ne samalla rakenteella ja nosta esiin linja sekä poikkeamat.

Viittaa säädöksiin muodossa: lain nimi ja säädösnumero ensimaininnassa (esim. työsopimuslaki (55/2001)), sen jälkeen vakiintunut lyhyt muoto ja tarkka kohta (esim. TSL 7:2). Oikeustapaukset tunnisteella (esim. KKO 2024:15). Merkitse epävarmat viittaukset [tarkistettava].

## Rajaukset

- Ei referointia muistista tai pelkän otsikon perusteella — vain varsinaisesta ratkaisutekstistä.
- Ei ration ja obiterin sekoittamista eikä sivuhuomautuksen esittämistä kantavana oikeusohjeena.
- Ei väitteitä ratkaisun sisällöstä tarkistamatta tekstiä.
- Ei prejudikaattiarvon ylitulkintaa yli ratkaisun kysymyksenasettelun.
