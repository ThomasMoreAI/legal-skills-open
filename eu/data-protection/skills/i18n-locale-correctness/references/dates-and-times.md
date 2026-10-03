# Dates, times and time zones

Authoritative basis: ISO 8601; RFC 3339; the IANA time zone database, current release **2026c (2026-07-08)** (`iana.org/time-zones`); Unicode CLDR 48.2 for locale data; ECMA-402 (`Intl`); the TC39 Temporal proposal, **Stage 4** (`github.com/tc39/proposal-temporal`). Status as at 2026-08-05. All behaviour below was executed on Node 22.19.0 / ICU 77.1.

## Storage

Three different things get called "a date". They need three different columns.

| What it is | Store as | Example |
|---|---|---|
| An **instant** (when something happened) | UTC timestamp, `timestamptz` / RFC 3339 with `Z` | `2026-08-05T13:12:56Z` |
| A **calendar date** (birthday, invoice date, contract start) | `date` / `YYYY-MM-DD`, no time, no zone | `1984-02-29` |
| A **future local event** (appointment, business hours, recurring meeting) | local date-time **plus the IANA zone id** | `2026-10-25T02:30` + `Europe/Vienna` |

The third row is the one that gets built wrong. Converting a future appointment to UTC at write time bakes in today's DST rules; when a government moves a transition date — and the tz database ships several such changes a year, 2026c alone moving Alberta to permanent −06 and Morocco to permanent +00 — every stored appointment silently shifts by an hour.

**An offset is not a zone.** `+01:00` describes one instant in one place. `Europe/Vienna` describes the rules that generate offsets. Store the zone id.

## The two DST failures

Verified for `Europe/Vienna` in 2026:

```
2026-03-29T00:59:00Z  →  29/03/2026, 01:59 GMT+01:00
2026-03-29T01:00:00Z  →  29/03/2026, 03:00 GMT+02:00     ← 02:00–02:59 never happens
2026-10-25T00:30:00Z  →  25/10/2026, 02:30 GMT+02:00
2026-10-25T01:30:00Z  →  25/10/2026, 02:30 GMT+01:00     ← 02:30 happens twice
```

Consequences you must handle explicitly:

- A user scheduling `02:30` on 2026-03-29 in Vienna has chosen a time that does not exist. Silently shifting it is a defect; ask, or document the rule you applied.
- A cron running "at 02:30 local" runs twice on 2026-10-25 or zero times on 2026-03-29. Idempotency keys, not hope.
- A duration computed as `end - start` across a transition is not the wall-clock duration the user saw. "Two hours from 01:30" is 01:30→03:30 in wall-clock terms and 60 minutes in elapsed terms — decide which one your feature means.

## Temporal

Stage 4; the proposal states it "will be merged into the ECMA-262 and ECMA-402 standards". Shipping status as at 2026-08-05 (`github.com/tc39/proposal-temporal`): **Firefox 139** (2025-05-27), **Chrome 144** (2026-01-13), **Node.js 26** (2026-05-05). Safari is still in development, and MDN states the feature "is not Baseline because it does not work in some of the most widely-used browsers". Node 22 does not expose it (verified: `typeof globalThis.Temporal === 'undefined'`).

So: use Temporal on the server if you are on Node 26+, and behind a polyfill (`temporal-polyfill` or `@js-temporal/polyfill`) in the browser until Safari ships. Do not assume it is there.

What it buys you is exactly the DST problem above, made explicit rather than silent:

```js
// Temporal.ZonedDateTime forces a decision about ambiguous and non-existent times.
const zdt = Temporal.PlainDateTime.from('2026-10-25T02:30')
  .toZonedDateTime('Europe/Vienna', { disambiguation: 'reject' });
// throws RangeError — the local time is ambiguous, so the caller must choose

// disambiguation: 'compatible' (default, matches legacy Date), 'earlier', 'later', 'reject'
// offset:         'use', 'ignore', 'prefer', 'reject'  — for round-tripping a stored offset
```

The classes: `Temporal.Instant`, `Temporal.ZonedDateTime`, `Temporal.PlainDate`, `Temporal.PlainTime`, `Temporal.PlainDateTime`, `Temporal.PlainYearMonth`, `Temporal.PlainMonthDay`, `Temporal.Duration`, `Temporal.Now`. The mapping to the storage table above is direct: `Instant` for row 1, `PlainDate` for row 2, `ZonedDateTime` for row 3.

Without Temporal, use a library that models zones properly (`date-fns-tz`, Luxon) and never `Date` arithmetic across a transition.

## `Date` parsing traps

```js
new Date('2026-03-05')          // 2026-03-05T00:00:00.000Z   — UTC
new Date('2026-03-05T00:00')    // 2026-03-04T23:00:00.000Z   — LOCAL (Europe/Vienna)
```

Verified. A date-only string is parsed as UTC; a date-time string without an offset is parsed as local. So `new Date(user.birthday).getDate()` returns the previous day for every user west of UTC. Never round-trip a calendar date through `Date`.

Anything not in the ISO format is implementation-defined. `new Date('03/05/2026')` is a coin toss across engines and locales. Parse with an explicit parser or not at all.

## Week numbering and first day of the week

ISO 8601 weeks start on Monday and week 1 is the week containing the first Thursday (equivalently, containing 4 January). The common US scheme starts weeks on Sunday and week 1 contains 1 January. They disagree about which week a date falls in for most of January.

CLDR carries both parameters and `Intl.Locale.prototype.weekInfo` exposes them (`firstDay` uses ISO-8601 day numbering, Monday = 1 … Sunday = 7). Verified:

| Locale | `firstDay` | `weekend` | `minimalDays` |
|---|---|---|---|
| `en-US` | 7 (Sun) | 6, 7 | 1 |
| `de-AT`, `de-DE`, `en-GB`, `fr-FR`, `es-ES` | 1 (Mon) | 6, 7 | 4 |
| `pt-PT` | 7 (Sun) | 6, 7 | 4 |
| `pt-BR`, `ja-JP`, `ko-KR`, `en-CA` | 7 (Sun) | 6, 7 | 1 |
| `zh-CN` | 1 (Mon) | 6, 7 | 1 |
| `ar-SA`, `he-IL` | 7 (Sun) | **5, 6** | 1 |
| `en-IN` | 7 (Sun) | **7 only** | 1 |
| `dv-MV` | **5 (Fri)** | 6, 7 | 1 |
| `fa-IR` | **6 (Sat)** | **5 only** | 1 |

```js
const { firstDay, weekend, minimalDays } = new Intl.Locale('de-AT').weekInfo;
// { firstDay: 1, weekend: [6, 7], minimalDays: 4 }
```

Note it is a **getter property**, not `getWeekInfo()`. If a calendar widget hard-codes Sunday-first or Monday-first, it is wrong in half your markets, and the weekend shading is wrong in the Gulf and in Israel.

## 12- versus 24-hour clocks

```js
new Intl.DateTimeFormat(loc, { hour: 'numeric' }).resolvedOptions().hourCycle
```

Verified: `h12` for `en-US` and `en-CA`; `h23` for `en-GB`, `de-AT`, `fr-FR`, `ja-JP`, `es-ES`, `pt-BR`. `en-CA` renders `1:05 p.m.` — lower case with periods, not `PM`. Never hard-code the marker; use `formatToParts` if you need to style it.

CLDR hour cycles: `h11` (0–11), `h12` (1–12), `h23` (0–23), `h24` (1–24). Pass `hourCycle` explicitly only when the user has chosen it in a setting; otherwise take the locale default.

## Month names inflect

Slavic and Baltic languages inflect month names by grammatical case. CLDR models this as **format** context (the month appears with a day number) versus **stand-alone** context (the month appears alone), and `Intl.DateTimeFormat` picks the right one from the options you pass. Verified:

| Locale | With a day (`day` + `month`) | Alone (`month` only) |
|---|---|---|
| `ru` | `15 января` | `январь` |
| `cs` | `15. ledna` | `leden` |
| `pl` | `15 stycznia` | `styczeń` |
| `uk` | `15 січня` | `січень` |
| `hr` | `15. siječnja` | `siječanj` |

A month-name lookup array built from `{ month: 'long' }` and then concatenated with a day number produces `15 январь`, which is wrong in a way a Russian reader notices immediately. Always format the whole date in one `Intl.DateTimeFormat` call.

Austrian German has a lexical difference, not a grammatical one: `de-AT` renders January as **`Jänner`**, `de-DE` and `de-CH` as `Januar`. Verified. February is `Februar` in all three.

## Non-Gregorian calendars

`Intl.supportedValuesOf('calendar')` on ICU 77 returns: `buddhist`, `chinese`, `coptic`, `dangi`, `ethioaa`, `ethiopic`, `gregory`, `hebrew`, `indian`, `islamic`, `islamic-civil`, `islamic-rgsa`, `islamic-tbla`, `islamic-umalqura`, `iso8601`, `japanese`, `persian`, `roc`.

Two locales default to a non-Gregorian calendar (verified via `resolvedOptions().calendar`): **`th-TH` defaults to `buddhist`** and **`fa-IR` defaults to `persian`**. Saudi Arabia's `ar-SA` defaults to `gregory` in ICU 77 despite the Hijri calendar's civil role.

```js
new Intl.DateTimeFormat('th-TH', { dateStyle: 'long' }).format(d)  // '15 มกราคม 2569'
new Intl.DateTimeFormat('ja-JP-u-ca-japanese', { dateStyle: 'long' }).format(d) // '令和8年1月15日'
```

Consequence: a Thai user reading `2569` where your database says `2026` is correct, and a form that parses the year back as an integer will be off by 543. Never round-trip a formatted date through a parser.

## Time zone identifiers

- Use IANA identifiers (`Europe/Vienna`, `America/New_York`, `Asia/Kolkata`). ICU 77 knows 418 of them (`Intl.supportedValuesOf('timeZone')`).
- **`Etc/GMT+1` is UTC−01:00.** Verified: at `2026-07-01T12:00Z`, `Etc/GMT+1` renders `11:00 GMT-01:00` and `Etc/GMT-1` renders `13:00 GMT+01:00`. The tz database keeps the POSIX sign convention, which is inverted relative to ISO 8601. Never expose `Etc/GMT±n` in a picker.
- Abbreviations are ambiguous and must never be stored. `CST` is US Central, China Standard and Cuba Standard.
- Offsets are not whole hours: `Asia/Kolkata` is +05:30, `Asia/Kathmandu` is +05:45, `Australia/Lord_Howe` is +10:30 (and its DST shift is 30 minutes), `Pacific/Chatham` is +12:45. Verified. Any code assuming integer-hour offsets is wrong for roughly a fifth of the world's population.
- Zone identifiers get renamed and merged upstream. Keep tzdata updated on every runtime — Node, the browser, the database and the OS can each hold a different vintage, and a booking made in one and read in another will disagree.

## Formatting for display

```js
new Intl.DateTimeFormat(locale, { dateStyle: 'long', timeZone: userZone }).format(instant);
new Intl.DateTimeFormat(locale, { dateStyle: 'short', timeStyle: 'short', timeZone: userZone })
  .format(instant);
```

`dateStyle`/`timeStyle` cannot be combined with individual component options — mixing them throws `TypeError: Invalid option`. Use one style or the other, never both vocabularies.

For ranges use `formatRange`, which collapses shared components (`5–8 August 2026` rather than `5 August 2026 – 8 August 2026`). For "3 days ago" use `Intl.RelativeTimeFormat`; verified `new Intl.RelativeTimeFormat('de', {numeric:'auto'}).format(-1, 'day')` gives `gestern`, not `vor 1 Tag`.

Never write a date format string by hand. `DD/MM/YYYY` and `MM/DD/YYYY` are indistinguishable for the first twelve days of every month, and the failure is silent.

## Checkpoints

- [ ] Instants, calendar dates and future local events are in three different column types
- [ ] Every scheduled future event stores an IANA zone id, not an offset
- [ ] Non-existent and ambiguous local times are handled explicitly, with a documented rule
- [ ] Recurring jobs are idempotent across both DST transitions
- [ ] No `new Date(string)` on anything but a full ISO instant with an offset
- [ ] Calendar dates never round-trip through `Date`
- [ ] First day of week and weekend days come from `Intl.Locale#weekInfo`, not hard-coded
- [ ] Week numbering scheme (ISO vs US) chosen deliberately and stated in the UI
- [ ] `hourCycle` comes from the locale unless the user has set a preference
- [ ] Dates formatted in a single `Intl.DateTimeFormat` call, never assembled from parts
- [ ] `de-AT` renders `Jänner`; no shared German month-name array
- [ ] `Etc/GMT±n` absent from any time zone picker
- [ ] Half-hour and quarter-hour offsets tested (`Asia/Kolkata`, `Asia/Kathmandu`, `Pacific/Chatham`)
- [ ] tzdata version recorded per runtime and on an update schedule (current: 2026c)
- [ ] Temporal usage gated on runtime support, with a polyfill in the browser
