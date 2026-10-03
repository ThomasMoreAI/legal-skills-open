# Visual language for the employment-law dashboard

The dashboard uses a quiet, editorial design. Think Bloomberg / Reuters / FT briefing — calm cream surface, slate-blue accent, hairline rules, typographic restraint. The template asset (`assets/dashboard-template.html`) already encodes all of this in CSS; do not modify the design system. This reference exists so you understand what's in the template and can avoid breaking it when you customize content.

## Palette

CSS variables defined in the template:

- `--bg: #FAFAF8` — page background (cream)
- `--bg-inset: #F5F2EA` — table headers, slightly deeper cream
- `--bg-row-alt: #F6F4EE` — alternating table rows
- `--ink: #1B1A17` — primary text
- `--ink-2: #3A3833`, `--ink-3: #6B675F`, `--ink-4: #94908A` — three lighter inks
- `--rule: #E6E2D8`, `--rule-strong: #D7D1C2` — hairline borders
- `--accent: #3B5266`, `--accent-ink: #1E3A5F`, `--accent-tint: #ECEEF1` — slate blue
- Traffic-light statuses: `--tl-green`, `--tl-yellow`, `--tl-red`, `--tl-grey` (use `class="yes"`, `class="partial"`, `class="no"` in cells)

Don't introduce new colors. The whole point of the design is restraint.

## Typography

- Sans: Plus Jakarta Sans (loaded from Google Fonts)
- Mono: JetBrains Mono (loaded from Google Fonts)
- Body: 14px / 1.5 / sans
- Page title (masthead): 28px / sans / weight 600
- Section titles: 20px / sans / weight 600
- Eyebrows, dates, table headers, citation pins: mono / 11px / uppercase / letter-spacing 0.04-0.06em

The mono is doing real visual work — it signals "metadata / citation" vs "prose / claim". Keep it consistent: use mono for eyebrows, dates, table column headers, citation rows under the law name, and inline citation pins.

## Hairline rules, not boxes

The design uses 1px hairlines (`var(--rule)`) to separate sections, not heavy cards. The two heavy borders that exist are intentional:
- Left rail on the TL;DR card (2px slate-blue accent stripe).
- Outer 1px border on tables.

Don't add box shadows, gradients, drop caps, or rounded corners (other than the existing 2px radius on tables and the TL;DR card).

## Editorial conventions

- "Updated [date]" lives in the masthead in mono, no period at the end.
- Subtitles are short and start with a preposition or article: "On laws regulating use of AI tools in the workplace." not "A dashboard tracking..."
- TL;DR items are collapsible (`<details>` / `<summary>`) — heading visible by default, body expands on click with a `+`/`-` indicator.
- Citation pins under each table cell use the `cell-cite` class and are small monospace section references. They point to primary sources (statute / reg / official agency guidance).
- Editorial links use a dotted underline (`border-bottom: 1px dotted`) instead of the default underline. The template handles this automatically.

## Tables

The comparison table uses the `cat-table` class. Conventions:
- First two columns are static across all tabs: **Jurisdiction** (state/city name only) and **Law** (with citation row underneath).
- Subsequent columns vary by tab.
- Each statement cell ends with a `<span class="cell-cite">` pinning the claim to a primary source.
- Status colors: green (`yes`), yellow (`partial`), red (`no`).

## Responsive

The page is fixed at `max-width: 960px` and breaks responsively below 900px (tabs and meta strip wrap, two-column splits stack). Don't change the max-width.
