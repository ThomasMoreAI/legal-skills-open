---
name: employment-law-dashboard
title: US Employment Law Dashboard
description: Build a single-file HTML dashboard for any area of US employment law, modeled after the AI Employment Laws Dashboard. Use this skill any time the user wants to create, build, generate, or update a dashboard, tracker, comparison page, or visual brief covering an employment-law topic across US jurisdictions. Triggers include phrases like "make a dashboard for [topic]", "build a tracker for [employment topic]", "state-by-state comparison page for [topic]", "visualize the legal landscape for [topic]", "create a dashboard like the AI one but for [topic]". The dashboard always includes a masthead, TL;DR, multi-state trackers, recent articles, a state comparison table with multi-select jurisdiction filter, and one or more deep-dive tabs (the skill explicitly asks the user which states they want a deep-dive page for). ALWAYS run the employment-law-research skill first if research notes don't already exist for the topic. Outputs a single self-contained HTML file the user can open in
  a browser.
author: bstevescherer
author_url: https://github.com/bstevescherer/heycounsel-community/tree/main/skills/employment-law-dashboard
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: contracts
language: en
sources:
- title: Content structure
  path: references/content-structure.md
- title: Source policies
  path: references/source-policies.md
- title: Visual language
  path: references/visual-language.md
---

# US Employment Law Dashboard

Builds a single-file HTML dashboard for any area of US employment law. The dashboard follows a fixed visual language and content structure based on the AI Employment Laws Dashboard so practitioners can read across topics with a consistent mental model.

The skill assumes you have research notes already. If you don't, use the `employment-law-research` skill first.

## When to use

Trigger this skill any time the user wants:
- A dashboard, tracker, comparison page, or visual brief on a US employment law topic.
- A "state-by-state" view of an employment-law topic.
- An update to an existing dashboard built with this skill.

Examples:
- "Make a dashboard for the laws regulating non-compete agreements."
- "Build a tracker for paid family leave laws across the US."
- "Create a state-by-state comparison dashboard for pregnancy accommodation."
- "Update the AI dashboard to reflect the new Texas law." (use this skill on the existing file)

## Workflow

### 1. Verify research is done

Before building anything, check that you have research notes for the topic. Look for a markdown file in the user's workspace folder, or ask the user where they keep their research.

If no research exists, **stop**. Tell the user you need to research first, point them to the `employment-law-research` skill, and offer to run it. Don't try to build a dashboard without research — you'll guess at statutes, miss jurisdictions, and end up citing law firm summaries for compliance claims.

If research is incomplete (e.g., they have one state but want a 5-state dashboard), use the research skill to fill the gaps before building.

### 2. Read the references

Read these in order before touching any HTML:

1. `references/source-policies.md` — the load-bearing rule. Every cell in the comparison table needs a primary-source citation. Don't cite law firm alerts in compliance cells, ever.
2. `references/visual-language.md` — the design system. Don't modify it; learn it.
3. `references/content-structure.md` — section-by-section content guidance.

### 3. Read the template

Read `assets/dashboard-template.html`. This is the working AI Employment Laws Dashboard, in full. Use it as the structural reference: every CSS class, every JS handler, every section pattern is what you should reproduce. The CSS and JS are tuned and tested — do not change them.

### 4. Ask the user which jurisdictions they want a deep-dive tab for

Before sketching content, ask the user explicitly: "Which states or cities do you want a deep-dive page for?" The dashboard supports one or more deep-dive top-tabs (one per jurisdiction). Suggest a sensible default based on the research (typically the jurisdiction with the most stringent or most-litigated regime), but let the user override or add others.

Examples:
- "I'd suggest Illinois for the deep dive since it has the most prescriptive notice rules. Want to keep it at just Illinois, or add others like California or Colorado?"
- "Two of these regimes (CA full ban, MA garden-leave) are structurally distinct enough to warrant their own deep-dive pages. Want both, or just one?"

Capture the answer before moving on. The number of deep-dive tabs determines how many top-level tabs the dashboard will have (US Overview + N deep-dives).

### 5. Plan the content before writing HTML

Sketch the content for each section based on the research notes:

- **Masthead:** title, subtitle, updated date, 3-6 meta stats. Stats should be substantive — for a non-compete dashboard, "States banning all non-competes" matters more than "States with a non-compete law".
- **TL;DR:** 3-4 collapsible items. What are the headline observations? Aim for genuinely surprising claims, not background filler.
- **Multi-state trackers:** 2-4 reputable trackers from the research notes.
- **Recent articles:** 2-3 enacted-law articles (left column) + 1-2 pending-bills articles (right column).
- **Comparison table:** decide on 3-5 tab categories. For an AI dashboard the tabs are AI definition / Notice / Disparate impact / Enforcement. For pay transparency they might be Coverage / Required disclosures / Recordkeeping / Enforcement. Pick categories that segment the actual obligations cleanly.
- **Deep dives:** for each jurisdiction the user picked in step 4, plan the field rows and compliance subsections.

### 6. Build the dashboard

Copy the template to the output filename and edit it section-by-section. Preserve all CSS, JS, classes, and structural HTML — only swap the substantive content. Concretely:

1. **Copy** `dashboard-template.html` to `[Topic]-Dashboard.html` in the user's workspace folder.
2. **Edit the masthead**: title, subtitle, updated date, meta stats. Keep the eyebrow as "The Brief On" unless the user wants a different framing.
3. **Edit the TL;DR items**: keep the `<details>`/`<summary>` structure with `class="tldr__item"`, `class="tldr__toggle"`, `class="tldr__body"`. Just swap text.
4. **Edit the multi-state trackers**: keep the `<article class="article">` pattern with `article__meta` / `article__title` / `article__desc`.
5. **Edit the recent articles section**: same pattern, two columns.
6. **Edit the comparison table tabs**: rename tab buttons to match topic categories; ensure each tab panel has a `<table class="cat-table">` with the same structure (Jurisdiction, Law, then category-specific columns). Each row needs `data-state="..."` for the filter to work. Each statement cell needs a `<span class="cell-cite">` pinning the claim.
7. **Edit the state filter pills**: update the `data-state` codes and labels in the dropdown to match the jurisdictions in your tables.
8. **Update the top-level tabs to match the deep-dive jurisdictions the user picked.** The template ships with two top-tabs: "U.S. Overview" and "Illinois". For each deep-dive jurisdiction the user chose, you need one top-tab button and one matching `<div class="top-panel">` with an `<div class="il-card">` inside. The `il-card` CSS class is generic and stays — you only change the panel's `id` (e.g., `id="california-panel"`) and the `data-target` on the corresponding tab button. To add a third or fourth deep-dive: duplicate the existing Illinois panel block, change the panel id, change the tab button label and `data-target`, then fill in that jurisdiction's content.
9. **Edit each deep-dive card**: title, citations, lede, field rows, compliance subsections. Repeat for every jurisdiction the user picked.
10. **Edit the footer**: footnotes (if any) plus the "For practitioner use only, not legal advice." closer.

### 7. Apply the source policy

Walk through every cell in the comparison table and every claim in the deep-dive card. For each, check the citation. Is it a primary source? If not, fix it. Common patterns:

- ✓ Statute (`leg.colorado.gov/bills/sb24-205`)
- ✓ Regulation (`rules.cityofnewyork.us/...`)
- ✓ Official agency guidance (`dhr.illinois.gov/...`)
- ✗ Law firm alert (`klgates.com/insight/...`)
- ✗ Tracker org (`multistate.ai/...`) — fine for footnote citations on counts, but not for compliance claims

If the user added secondary-source citations to compliance cells, remove them quietly or ask first.

### 8. Final passes

Before handing off, do these passes:

- **Tag balance check** — run a quick HTML validator (basic stack-based check) to make sure no unclosed tags. The template starts balanced; edits can introduce drift.
- **Acronym check** — every acronym (AEDT, IDHR, CRD, FEHA, etc.) should be expanded on first use within each cell. Don't assume the reader knows them.
- **Em dash check** — replace any `—` with periods, semicolons, colons, parens, or hyphens. The dashboard's editorial voice doesn't use em dashes.
- **State filter check** — verify that the dropdown options match the `data-state` attributes on the table rows. If you added Massachusetts, the dropdown needs an option for it AND every row needs `data-state="ma"`.
- **JS check** — make sure the three handlers still work: top-tab switching, inner-tab switching, multi-select dropdown filter, collapsible TL;DR.

### 9. Save and present

Save the file to the user's workspace folder (not the temporary outputs directory). Provide the user with a `computer://` link to view it. Brief summary of what you built, but don't recap section-by-section — the user can open the file.

## Updating an existing dashboard

If the user asks you to update a dashboard that was built with this skill (e.g., "the new Texas law just passed, update the AI dashboard"):

1. Read the existing dashboard file. Don't start from the template.
2. Confirm the change with the user first if it's substantive (new jurisdiction, restructured tabs).
3. For factual updates: research the new development first (`employment-law-research` skill), then make targeted edits.
4. Re-apply the source policy after the edit. New citations must be primary.
5. Update the "Updated [date]" line in the masthead.

## What this skill won't do

- It won't write a dashboard from your raw research without you reading the source policy first. Skipping that step produces dashboards with mixed primary / secondary citations in compliance cells, which is a credibility problem for a practitioner tool.
- It won't change the visual design. The cream + slate-blue palette, hairline rules, and editorial typography are the design. If the user wants a different look (dark mode, branded colors, different fonts), say so and offer to do it as a separate styling pass after the content is right.
- It won't generate dashboards for non-US employment law. The template's vocabulary (states, cities, federal preemption, IHRA, FEHA, etc.) is US-specific. For other jurisdictions, the structure could be adapted but you'd need a different template.
