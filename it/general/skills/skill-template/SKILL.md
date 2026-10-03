---
name: skill-template
title: Template skill — diritto italiano
description: Template per creare nuovi skill giuridici italiani nel marketplace. Usare quando si aggiunge uno skill o si apre una PR. Riferimento per contributor; user-invocable false consigliato per copia.
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/diritto-italiano-hub/skills/skill-template
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: en
---

# Template skill — diritto italiano

Copia questa cartella in `skills/<nome-skill>/` del plugin appropriato.

## Frontmatter

```yaml
---
name: nome-skill
description: Cosa fa lo skill, quando attivarlo, materia/rito. Max 1024 caratteri. Includere "Nessuna consulenza legale".
argument-hint: "[parametri opzionali]"
---
```

## Corpo minimo

### Obbligatorio

Box iniziale (stesso testo in tutti gli skill):

> **Bozza — non consulenza legale.** Verificare norme, giurisprudenza e vigore.

### Sezioni consigliate

1. **Quando usare** — trigger e limiti
2. **Input richiesti** — documenti, date, rito
3. **Workflow** — passi numerati
4. **Output** — formato bozza
5. **Citazioni** — rimando a `/diritto-italiano-hub:citazione-italiana`
6. **Divieti** — no parere definitivo; no dati cliente reali in esempi pubblici

## Qualità (checklist)

- [ ] Rito e tipo atto indicati se processuale
- [ ] Metodo IT, non common law
- [ ] Esempi solo fittizi o da `testatti/`
- [ ] Description sotto 1024 caratteri

Vedi `/diritto-italiano-hub:skills-qa` prima di aprire PR.
