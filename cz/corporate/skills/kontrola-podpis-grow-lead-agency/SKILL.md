---
name: kontrola-podpis-grow-lead-agency
title: /kontrola-podpis -- Kontrola a směrování elektronického podpisu
description: Připravte a nasměrujte dokument k elektronickému podpisu — ověřte oprávnění signatáře v obchodním rejstříku přes DirectCase, projděte kontrolní seznam před podpisem, nastavte pořadí podepisování a odešlete k podpisu. Použijte, když je smlouva finalizována a připravena k podpisu, při ověřování názvů subjektů, příloh a podpisových bloků před odesláním nebo při sestavování obálky se sekvenčními či paralelními signatáři.
author: grow-lead-agency
author_url: https://github.com/grow-lead-agency/ak-sladek/tree/master/skills/kontrola-podpis
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cz
practice: corporate
language: cs
---

# /kontrola-podpis -- Kontrola a směrování elektronického podpisu

> Pokud narazíte na neznámé zástupné symboly nebo si potřebujete ověřit, které nástroje jsou propojeny, viz [CONNECTORS.md](../../CONNECTORS.md).

Připravte dokument k elektronickému podpisu — ověřte úplnost dokumentu, oprávnění signatáře protistrany a nasměrujte k podpisu.

**Důležité**: Tento skill pomáhá s právními workflow, ale neposkytuje právní poradenství ve smyslu zákona č. 85/1996 Sb. o advokacii. Před odesláním k podpisu ověřte, že je dokument ve finální podobě.

## Jak používat (pro uživatele)

Vyvolej skill `/kontrola-podpis` a přilož dokument k podpisu (PDF, DOCX, URL nebo textovou referenci na již známý dokument). AI provede:

1. **Ověření oprávnění signatáře protistrany** v obchodním rejstříku přes DirectCase (statutární orgán, způsob jednání, prokura, plná moc).
2. **Kontrolní seznam před podpisem** — finální verze dokumentu, kompletní přílohy, správné názvy subjektů, podpisové bloky, interní schválení.
3. **Konfiguraci podepisování** — signatáři (jména, e-maily, role), pořadí (sekvenční × paralelní), interní schvalovatelé, příjemci v kopii.
4. **Nasměrování k podpisu** — pokud je připojený konektor pro elektronický podpis (Signi, DocuSign), vytvoří podpisovou obálku a odešle; jinak vygeneruje pokyny k manuálnímu podpisu.
5. **Strukturovaný výstup** — detaily smlouvy, výsledek checklistu, konfigurace podepisování, stav, další kroky.

> ⚙ Sekce s technickými detaily (názvy nástrojů, integrace) jsou ve zbytku skillu označené poznámkou „Pro AI agenta". Při čtení skillu jako uživatel je můžete přeskočit.

## Krok 0 — startovací kontrola DirectCase konektoru

Před zahájením přípravy podpisu ověř, zda je dostupný **DirectCase konektor** pro vyhledávání v obchodním rejstříku, a zeptej se uživatele, zda ho má v procesu použít.

**Postup:**

1. Zjisti stav DirectCase konektoru. Pokud konektor není připojený nebo je v této konverzaci vypnutý, zobraz uživateli kartu pro jeho povolení.
2. Polož uživateli otázku: *„Před přípravou podpisu — chcete, abych přes DirectCase ověřil oprávnění signatáře protistrany v obchodním rejstříku?"*
3. Postupuj podle odpovědi:
   - **Ano + konektor aktivní** → DirectCase aktivně použij v sekci „Ověření oprávnění k podpisu přes DirectCase" níže.
   - **Ano + konektor není aktivní** → počkej, dokud uživatel konektor nepovolí nebo nenapíše „pokračuj".
   - **Ne** → pokračuj bez něj a v závěru jasně uveď, že údaje z OR nebyly nezávisle ověřeny.

Tento krok přeskoč pouze tehdy, byl-li už proveden v této konverzaci.

> ⚙ **Pro AI agenta:** Stav konektoru zjisti přes `mcp__mcp-registry__search_mcp_registry` s klíčovými slovy `["directcase", "obchodní rejstřík"]` a najdi záznam „DirectCase CZ". Pokud `connected: true` + `enabledInChat: false`, zavolej `mcp__mcp-registry__suggest_connectors` s `directoryUuid` z výsledku. Otázku uživateli pokládej přes `AskUserQuestion`. Pro spolehlivé ověření, že DirectCase je skutečně dostupný a jaký má tier, lze přímo zavolat nástroj `get_entitlements` — je vždy dostupný a nezávisí na stavu registru konektorů. Plné znění technického postupu viz [SKILL.md → Krok 0](SKILL.md).

## Použití

```
/kontrola-podpis $ARGUMENTS
```

Připravit k podpisu: @$1

## Ověření oprávnění k podpisu přes DirectCase

Pokud je v Kroku 0 potvrzeno použití DirectCase, ověř oprávnění signatáře protistrany **před odesláním dokumentu k podpisu**. Jde o nejčastější příčinu sporů o platnost smlouvy — podpis osoby bez oprávnění může způsobit, že smlouva není platně uzavřena.

Z výpisu z obchodního rejstříku přes DirectCase MCP zjisti:

- **Statutární orgán** protistrany (jednatel, představenstvo, ředitel) a den vzniku funkce.
- **Způsob jednání za společnost** — typické varianty:
  - „Jednatel jedná za společnost samostatně" → každý jednatel může podepsat sám.
  - „Společnost zastupují vždy dva jednatelé společně" → jeden podpis nestačí.
  - „Společnost zastupuje jednatel společně s prokuristou" / „dva členové představenstva" → vyžaduje kombinaci podpisů.
- **Prokura** — zda existuje, kdo je prokuristou a jaký je její rozsah. Prokura nezahrnuje zcizení a zatížení nemovitostí, není-li v zápisu výslovně uvedeno jinak (§ 453 OZ).
- **Sbírka listin** — zápis o volbě členů statutárního orgánu (kdy byli jmenováni, zda je funkce stále platná) a případná plná moc, je-li v rejstříku zapsaná.

Porovnej zjištěné údaje s podpisovým blokem ve smlouvě:

- **Pokud podepisuje jednatel uvedený v OR a způsob jednání to umožňuje** → OK, zaznamenej do kontroly.
- **Pokud podepisuje někdo jiný než statutární orgán** → ke smlouvě musí být přiložena **písemná plná moc** dle § 441 OZ, nebo na ni musí být v textu smlouvy odkázáno. Plná moc musí obsahovat výslovné oprávnění k podpisu této konkrétní smlouvy nebo k danému typu jednání. **Pokud plná moc chybí, signalizuj problém před odesláním a požádej o její doložení.**
- **Pokud podepisuje prokurista** → ověř rozsah prokury podle zápisu v OR.
- **Pokud nelze oprávnění z OR ověřit** (např. nový jednatel ještě není zapsaný) → doporuč před podpisem vyžádat aktuální výpis z OR nebo plnou moc přímo od protistrany.

> ⚙ **Pro AI agenta — konkrétní nástroje DirectCase:** `search_company` (statutární orgán, způsob jednání, prokura), `search_identifier` (přesné hledání podle IČO), `search_company_documents` (sbírka listin — zápisy o volbě, plné moci), `convert_file_to_markdown` (přečtení konkrétního dokumentu ze sbírky listin — funguje jen pro důvěryhodné právní domény; **PDF mimo tyto domény převáděj lokálně**, ne přes DirectCase).

## Pracovní postup

### Krok 1: Přijetí dokumentu

Přijmi dokument v libovolném formátu:

- **Nahraný soubor**: PDF, DOCX
- **URL**: odkaz na dokument v ~~cloudovém úložišti nebo ~~CLM
- **Reference**: „Rámcová smlouva s Acme Corp, kterou jsme včera finalizovali"

### Krok 2: Kontrolní seznam před podpisem

Před odesláním k podpisu ověř:

```markdown
## Kontrolní seznam před podpisem

- [ ] Dokument je ve finální, odsouhlasené podobě (žádné otevřené redline úpravy)
- [ ] Všechny přílohy a dodatky jsou připojeny
- [ ] Správné názvy právních subjektů v podpisových blocích (ověřeno proti OR)
- [ ] Data jsou správná nebo ponechána prázdná pro datum podpisu
- [ ] Podpisové bloky odpovídají oprávněným osobám (ověřeno přes DirectCase v sekci výše)
- [ ] Byla získána všechna požadovaná interní schválení
- [ ] Dokument byl zkontrolován příslušným právníkem
```

### Krok 3: Konfigurace podepisování

Shromáždi podrobnosti o podepisování:

- **Signatáři**: kdo musí podepsat? (jména, e-maily, funkce)
- **Pořadí podepisování**: sekvenční, nebo paralelní?
- **Interní schválení**: musí někdo z vaší strany schválit dokument předtím, než ho podepíše protistrana?
- **Příjemci v kopii (CC)**: kdo má obdržet kopii podepsaného dokumentu?

Pokud OR vyžaduje **dva jednatele společně**, upozorni uživatele, že jeden podpis nestačí — musí se přidat druhý signatář.

### Krok 4: Nasměrování k podpisu

**Pokud je ~~elektronický podpis propojen:**

- Vytvoř podpisovou obálku/žádost.
- Nastav podpisová pole a pořadí.
- Přidej případné požadované pole pro parafy nebo datum.
- Odešli k podpisu.

**Pokud není propojen:**

- Vygeneruj pokyny k podepsání.
- Poskytni dokument naformátovaný pro vlastnoruční podpis nebo manuální elektronický podpis.
- Uveď seznam všech signatářů s kontaktními údaji.

> **Poznámka k formě podpisu v ČR:** Podle zákona č. 297/2016 Sb. o službách vytvářejících důvěru pro elektronické transakce a nařízení eIDAS (EU) č. 910/2014 je **kvalifikovaný elektronický podpis (KEP)** nejvyšším standardem a je právně rovnocenný vlastnoručnímu podpisu. U úkonů vůči veřejné správě, některých katastrálních podání a u zvláštních forem podle § 560 a násl. OZ je KEP vyžadován. U běžných obchodních smluv stačí prostý nebo zaručený elektronický podpis (např. Signi, DocuSign).
>
> **AI nerozhoduje o požadované formě podpisu.** Posouzení, zda pro konkrétní právní úkon postačí prostý / zaručený / kvalifikovaný elektronický podpis, je **právní otázka, kterou musí posoudit kvalifikovaný advokát nebo právník**. Skill může uvést obecný rámec a upozornit na rizikové oblasti (úkony vůči katastru nemovitostí, datové schránky orgánů veřejné moci, právní úkony se zvláštní formou podle § 560+ OZ), ale konečné rozhodnutí o vhodné formě podpisu pro daný úkon ponech na uživateli a jeho právním poradci.

## Výstup

```markdown
## Žádost o podpis: [Název dokumentu]

### Podrobnosti dokumentu
- **Typ**: [rámcová smlouva / smlouva o mlčenlivosti / dílčí smlouva o dílo / dodatek atd.]
- **Smluvní strany**: [Strana A] a [Strana B]
- **Počet stran**: [X]

### Ověření oprávnění (DirectCase OR)
- **Strana A (vaše)**: [jméno signatáře + statutární orgán + způsob jednání: OK]
- **Strana B (protistrana)**: [jméno signatáře + statutární orgán + způsob jednání: OK / vyžaduje plnou moc / vyžaduje druhý podpis]

### Kontrola před podpisem: [V POŘÁDKU / ZJIŠTĚNY PROBLÉMY]
[Uveď případné problémy, které je třeba vyřešit před odesláním.]

### Konfigurace podepisování
| Pořadí | Signatář | E-mail | Role |
|-------|--------|-------|------|
| 1 | [jméno] | [e-mail] | [oprávněná osoba Strany A] |
| 2 | [jméno] | [e-mail] | [oprávněná osoba Strany B] |

### Příjemci v kopii (CC)
- [jméno] — [e-mail]

### Stav
[Odesláno k podpisu / Připraveno k odeslání / Je třeba nejprve vyřešit problémy]

### Další kroky
- [Co lze očekávat po odeslání]
- [Očekávaná doba vyřízení]
- [Následný krok, pokud nebude podepsáno do X dnů]
```

## Tipy

1. **Pečlivě zkontroluj názvy subjektů** — Nejčastější chybou při podepisování jsou nesprávné názvy právních subjektů. Vždy ověř název, IČO a sídlo proti aktuálnímu výpisu z OR.
2. **Ověř oprávnění** — Ujisti se, že každý signatář je oprávněn zavazovat svou organizaci (statutární orgán nebo osoba s plnou mocí). KYC v OR je rychlejší a levnější než pozdější spor o platnost smlouvy kvůli neoprávněnému podpisu.
3. **Uchovej kopii** — Podepsané kopie ihned po podpisu ulož v ~~cloudovém úložišti nebo ~~CLM.

<!-- Origin: DirectCase pravo-skills v1.1.0 (MIT, LICENSE-directcase-pravo-skills) | Import: 2026-07-14 do ak-sladek pluginu, review bez adaptaci (Cowork-native reference OK) | Inspiration: https://www.directcase.ai/cz/cs/news/claude-legal-plugin-cs -->
