# Research Sources — generuj-smlouvu

## 2026-07-14 — vznik skillu (research fáze legal vertikály)
Kompletní research: `skills/legal/research/` (01-zahranicni-landscape, 02-document-automation, 03-cz-patterns, 00-SYNTEZA, 04-analyza-vzoru).

Klíčové zdroje (reálně otevřené):
- https://docxtpl.readthedocs.io/en/latest/ — docxtpl engine, {%p %} tagy, run-splitting
- https://github.com/elapouya/python-docx-template — docxtpl repo
- https://automationlogs.com/legal/contract-drafting-101-automation-basics/ — datový model před šablonou, AI=extrakce ne drafting
- https://help.hotdocs.com/author/current/Conditional_Region_Overview.htm — conditional regions pattern
- https://www.thomsonreuters.com/en-us/help/contract-express/getting-started/key-concepts.html — Contract Express markup
- https://help.gavel.io/articles/basic-variables — Gavel {{ }} syntax
- https://learningcenter.xpressdox.com/conditional-if-else/ — When() pluralizace/rod
- https://github.com/anthropics/knowledge-work-plugins/tree/main/legal — Anthropic legal plugin (playbook pattern, disclaimer)
- https://github.com/anthropics/claude-for-legal — practice profile, cold-start interview, [verify] tagging
- https://www.cak.cz/advokatni-uschovy — pravidla úschov (EKÚ, Garanční fond, zákaz hotovosti)
- https://blog.xa0.de/post/Filling-a-docx-template-with-Python-while-preserving-style/ — run-preserving replace

Vstupní vzory: 4 reálné smlouvy AK Sládek (KS ×2, RS, SÚ) — `_podklady/vzory-sladek/` (gitignored, PII).
