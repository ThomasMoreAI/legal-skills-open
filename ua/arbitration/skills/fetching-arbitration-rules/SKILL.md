---
name: fetching-arbitration-rules
title: fetching-arbitration-rules
description: Use when retrieving arbitration institutional rules (ICC, LCIA, SCC, SIAC, HKIAC, VIAC, МКАС/МАК при ТПП України, UNCITRAL) — fetching current version, verifying redaction applicable to the date of arbitration agreement, constructing URLs for official rule texts
author: crankshift
author_url: https://github.com/crankshift/lawpowers/tree/main/skills/ua/law-ua-fetching-arbitration-rules
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: ua
practice: arbitration
language: uk
---

# fetching-arbitration-rules

Регламенти арбітражних інституцій періодично переглядаються (ICC — 2012/2017/2021; LCIA — 1998/2014/2020; SCC — 2017/2023; SIAC — 2013/2016/2025; HKIAC — 2013/2018/2024). Різні редакції по-різному регулюють консолідацію, emergency arbitrator, expedited procedure, early dismissal, third-party funding — тому цитата без указання року редакції не має доказової цінності. Для українського арбітражу релевантні МКАС і МАК при ТПП України, а серед провідних іноземних — ICC, LCIA, SCC, SIAC, HKIAC, VIAC; для ad hoc арбітражу — UNCITRAL Arbitration Rules.

## URL patterns (звірено 2026-04-20)

| Інституція | Чинний регламент | URL | Дата редакції |
|---|---|---|---|
| МКАС при ТПП України (ICAC) | Регламент МКАС | `https://icac.org.ua/arbitrazh/reglament/` (копія на zakon.rada: `https://zakon.rada.gov.ua/go/v0025571-17`) | Чинну редакцію звіряти на сайті МКАС |
| МАК при ТПП України | Регламент МАК | `https://icac.org.ua/` (окремий розділ Морської арбітражної комісії) | Чинну редакцію звіряти на сайті |
| ICC | 2021 ICC Rules of Arbitration | `https://iccwbo.org/dispute-resolution/dispute-resolution-services/arbitration/rules-procedure/2021-arbitration-rules/` | 01.01.2021 |
| LCIA | 2020 LCIA Arbitration Rules | `https://www.lcia.org/Dispute_Resolution_Services/lcia-arbitration-rules-2020.aspx` | 01.10.2020 |
| SCC Arbitration Institute | 2023 SCC Arbitration Rules | `https://sccarbitrationinstitute.se/en/scc-arbitration-rules-english-2023/` | 01.01.2023 |
| SIAC | SIAC Rules 2025 (7th edition) | `https://siac.org.sg/siac-rules-2025` | 01.01.2025 |
| HKIAC | 2024 HKIAC Administered Arbitration Rules | `https://hkiac.org/arbitration/rules-and-practice-notes/2024-administered-arbitration-rules/` | 01.06.2024 |
| VIAC | Vienna Rules 2021 (чинна редакція з 01.01.2025) | `https://www.viac.eu/en/arbitration-basics/arbitration-rules/` | 01.07.2021 (оригінал); чинна — 01.01.2025 |
| UNCITRAL | UNCITRAL Arbitration Rules (1976 / 2010 / 2013 / 2021 Expedited) | `https://uncitral.un.org/en/texts/arbitration/contractualtexts/arbitration` | 2013 (основний); 2021 (Expedited) |

## Workflow

1. **Визначити інституцію.** Джерело — арбітражне застереження в договорі, Request for Arbitration, Answer, terms of reference або процесуальний наказ. Якщо застереження двозначне (наприклад, «Arbitration Institute of the Stockholm Chamber of Commerce» — стара назва SCC) — звірити, яка саме організація є адміністратором спору сьогодні.
2. **Визначити дату старту арбітражу.** За більшістю регламентів (ICC Art. 6(1), LCIA Art. 1, SIAC Rule 3, HKIAC Art. 4) чинною для процедури є редакція, що діяла на дату подання Request for Arbitration / Notice of Arbitration, якщо сторони не домовилися інакше. Саме ця дата, а не дата арбітражного застереження, визначає застосовну редакцію.
3. **Звірити перехідні положення застереження.** Окремі застереження фіксують конкретну редакцію («as in force on the date of this Agreement» або «as may be amended from time to time»); зафіксована редакція має пріоритет над замовчуванням.
4. **Фетч офіційної сторінки** через WebFetch за URL з таблиці. Перевірити у шапці сторінки або preamble регламенту: дату набрання чинності, номер редакції, чи не з'явилося оголошення про нову редакцію, що готується.
5. **Завантажити PDF регламенту** за посиланням «Download» / «Rules (PDF)» на офіційній сторінці — PDF є authoritative text, HTML-версія часто скорочена.
6. **Знайти точну статтю/правило** — за номером (Article/Rule/Стаття) і частиною/підпунктом. У SIAC та HKIAC нумерація — «Rule», в ICC/LCIA/SCC/VIAC — «Article», в МКАС — «§».
7. **Цитувати** з обов'язковим зазначенням року редакції та, за потреби, дати звірки.

## Пошук історичних редакцій

- **ICC.** Архів минулих редакцій (1998, 2012, 2017) публікується на iccwbo.org у розділі «Previous versions of the Arbitration Rules». За відсутності на сайті — через `https://web.archive.org/web/*/iccwbo.org/*arbitration-rules*`.
- **LCIA.** 2014 LCIA Rules і 1998 LCIA Rules доступні з розділу «Historic LCIA Arbitration Rules» на lcia.org; PDF зазвичай збережено як окремі документи.
- **SCC.** Редакції 2010 і 2017 — на sccarbitrationinstitute.se у розділі попередніх версій.
- **SIAC.** Редакції 2013 і 2016 — на siac.org.sg у розділі Previous Rules; 6th edition (2016) залишалася чинною до 31.12.2024.
- **HKIAC.** 2013 і 2018 HKIAC Administered Arbitration Rules — на hkiac.org у розділі попередніх редакцій.
- **VIAC.** Vienna Rules 2013, 2018, 2021 — на viac.eu; архівні редакції PDF.
- **МКАС при ТПП України.** Попередні редакції — на сайті icac.org.ua або в архівах ТПП України. Для станів до 2017 р. — через `https://web.archive.org/web/*/icac.org.ua/*` та zakon.rada (постанови ТПП мають власні ID). Перед використанням — звірити дату набуття чинності саме тієї редакції.
- **UNCITRAL.** Офіційні редакції: 1976 (original), 2010 (revised), 2013 (з urbanisation для Transparency Rules), 2021 (Expedited Rules як доповнення). Усі доступні на `uncitral.un.org` у розділі Arbitration.
- **Web Archive.** Для будь-якої інституції перевіряти дату кешу (timestamp у URL archive.org) — проміжна редакція може виглядати як фінальна, якщо зняти скрін у перехідний період.

## Формат цитування

Базовий шаблон:

`<Стаття/Article/Rule/§> <номер>(<частина>) of the <рік> <назва регламенту> (URL, звірено <дата>)`

Приклади:

- § 19 Регламенту МКАС при ТПП України (в редакції від 27.07.2017), `https://icac.org.ua/arbitrazh/reglament/` (звірено 2026-04-20).
- § 4 Регламенту МАК при ТПП України (чинна редакція).
- Art. 4(3) of the 2021 ICC Rules of Arbitration, `https://iccwbo.org/.../2021-arbitration-rules/`.
- Article 28 of the 2020 LCIA Arbitration Rules, `https://www.lcia.org/.../lcia-arbitration-rules-2020.aspx`.
- Article 8 of the 2023 SCC Arbitration Rules, `https://sccarbitrationinstitute.se/en/scc-arbitration-rules-english-2023/`.
- Rule 5 of the SIAC Rules 2025 (7th edition), `https://siac.org.sg/siac-rules-2025`.
- Article 28 of the 2024 HKIAC Administered Arbitration Rules, `https://hkiac.org/.../2024-administered-arbitration-rules/`.
- Article 45 of the Vienna Rules 2021 (as amended with effect from 01.01.2025), `https://www.viac.eu/en/arbitration-basics/arbitration-rules/`.
- Article 17 of the UNCITRAL Arbitration Rules (as revised in 2013), `https://uncitral.un.org/en/texts/arbitration/contractualtexts/arbitration`.

Для документів українською мовою — кирилицею «§» / «ст.» / «пункт»; для англомовних меморандумів — «Article» / «Rule» / «§». Назва регламенту — мовою документа.

## Common mistakes

- **Цитата без року редакції.** 2012 ICC Rules ≠ 2021 ICC Rules — різні правила emergency arbitrator (з'явився у 2012), консолідації (оновлено у 2021, Art. 10), expedited procedure (введено у 2017, Art. 30 та Appendix VI), joinder of additional parties. Без року редакції цитата не має процесуальної цінності.
- **Покладання на таблицю без свіжої перевірки.** Таблиця в цьому скілі — стартова точка; регламенти оновлюються без попередження (SIAC перейшов з 6th на 7th edition з 01.01.2025; SCC оновив правила у 2023; HKIAC — у 2024). Перед фінальним документом — обов'язковий WebFetch офіційного сайту.
- **Плутання UNCITRAL Rules з UNCITRAL Model Law on International Commercial Arbitration.** UNCITRAL Arbitration Rules — процесуальний регламент для ad hoc арбітражу, застосовується за згодою сторін. UNCITRAL Model Law — зразок національного законодавства, імплементований у ЗУ «Про міжнародний комерційний арбітраж» (1994). Посилатися в процесуальному меморандумі на Model Law як на Rules — груба помилка.
- **Застосування поточного регламенту до старого спору.** Якщо Request for Arbitration поданий у 2018 р., для ICC застосовуються 2017 Rules, а не 2021; для LCIA — 2014 Rules, а не 2020; для HKIAC — 2013 Rules, а не 2018 (якщо RfA до 01.11.2018). Перехід на нову редакцію без згоди сторін — підстава для оспорювання рішення.
- **Web Archive без перевірки дати кешу.** Timestamp у URL (`/web/20190315.../...`) показує дату кешування, а не дату редакції документа. Читати дату набрання чинності внизу сторінки або в preamble PDF, щоб не прийняти проміжну редакцію (наприклад, 2017 ICC Rules в архіві 2019 р.) за редакцію, чинну на момент спору.
- **Використання застарілого URL МКАС (arbiter.ua).** Домен arbiter.ua не є офіційним. Правильний сайт МКАС при ТПП України — `icac.org.ua`. Перевіряти саме цей домен; копія регламенту на zakon.rada (`v0025571-17`) — допоміжне джерело для української редакції.
- **Плутання SCC з іншими «SCC».** SCC Arbitration Institute у Стокгольмі (раніше — Arbitration Institute of the Stockholm Chamber of Commerce) — не плутати з Swiss Chambers' Arbitration Institution (SCAI, тепер Swiss Arbitration Centre) і не з China's CIETAC. Власний сайт — `sccarbitrationinstitute.se`.
- **Ігнорування транзитних положень у самому регламенті.** Нові редакції зазвичай містять окрему статтю про застосування в часі (наприклад, ICC 2021 Art. 6(1), SIAC 2025 Rule 1.3). Читати її окремо — там прописано, коли застосовується стара редакція.
