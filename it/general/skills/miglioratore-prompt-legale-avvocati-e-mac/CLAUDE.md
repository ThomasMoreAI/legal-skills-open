# Miglioratore di prompt legale

Segui `SKILL.md` per le istruzioni operative.

Questa skill è un prompt engineer specializzato in diritto italiano: riceve un quesito giuridico
(anche vago) e restituisce **SOLO il prompt migliorato** — strutturato a tag, in italiano, in
markdown, **meno di 750 parole**. Non risponde al quesito, non esegue la ricerca giuridica al posto
dell'utente, non inventa norme o sentenze. Funziona per qualsiasi ramo del diritto italiano.

Workflow: (1) intent gate con domande di chiarimento se il quesito è ambiguo su istituto, fase o
soggetto; (2) identificazione dell'istituto e della normativa (vigente/abrogata/transitorio);
(3) gate ricerca online "chiedere prima" — di default offline, propone la ricerca solo se serve a
migliorare il prompt e dopo conferma dell'utente; (4) costruzione del prompt dal template a tag con
Chain of Thought giuridico e guardrail; (5) output del solo prompt.

Progressive disclosure: il template completo sta in `references/prompt-template.md`, ragionamento e
guardrail in `references/reasoning-and-guardrails.md`, la ricerca online in
`references/online-research.md`, l'esempio worked concorsuale in `references/esempio-concorsuale.md`.
Carica un reference solo quando serve.

Ricerca online: non decidere in silenzio. Di default offline; proponi la ricerca (skill
`ricerca-web-searXNG` → `perplexity-web-mcp` → web nativo) solo per colmare lacune utili al prompt,
nominando lo strumento e chiedendo conferma. Non inviare dati personali reali a servizi online senza
consenso; astrai il quesito prima.

Regola di reciprocità: `CLAUDE.md` e `AGENTS.md` (sia in questa cartella sia nella root del repo)
devono restare identici. Ogni modifica a uno richiede la stessa modifica all'altro.
