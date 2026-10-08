---
name: guia-cartorio-andrevictor23-tech
title: Guia de Estudos — Concurso de Cartório
description: Produz o guia semanal de estudos para concurso de cartório com as novidades notariais e registrais dos últimos 7 dias. Use ao pedir "guia da semana", "novidades do cartório" ou "boletim registral", ou quando a rotina agendada disparar.
author: andrevictor23-tech
author_url: https://github.com/andrevictor23-tech/claude-skills/tree/main/guia-cartorio
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Guia de Estudos — Concurso de Cartório

Produz uma edição do guia com o que foi publicado nos **últimos 7 dias** nas fontes abaixo.

Contexto do usuário: candidato ao **concurso de outorga de delegações de MT (Edital TJMT 48/2025, Cebraspe)** — objetiva em 05/09/2026, escrita e prática em 31/10/2026, oral em 25/04/2027. O material de base está em `E:\Users\<usuário>\Documents\ESTUDO\CARTORIO-MT\`.

## 1. Varredura das fontes

Percorra **todas** as sete fontes públicas. Elas são independentes: falha em uma não interrompe as demais.

| # | Fonte | Endereço | Como colher |
|---|---|---|---|
| 1 | Migalhas Notariais e Registrais | `migalhas.com.br/coluna/migalhas-notariais-e-registrais` | WebFetch na coluna; pegue os textos dos últimos 7 dias |
| 2 | IBDFAM — Artigos | `ibdfam.org.br/artigos` | WebFetch; filtre por data e por pertinência registral/notarial |
| 3 | CNJ — Notícias | `cnj.jus.br` | WebSearch com `allowed_domains: ["cnj.jus.br"]` para "cartório", "registro", "notarial", "extrajudicial" |
| 4 | Anoreg/BR | `anoreg.org.br/site/` | WebFetch na home de notícias + WebSearch no domínio |
| 5 | Colégio Notarial do Brasil | `notariado.org.br` | WebFetch; publicações recentes |
| 6 | STJ — Jurisprudência | — | WebSearch por decisões recentes em usucapião extrajudicial, ata notarial, registro de imóveis, RCPN, RTD, protesto, alienação fiduciária |
| 7 | Boletim KollGEN do IRIB | `irib.org.br/kollgen/` | WebFetch |

**Sempre** cheque também os **atos novos da Corregedoria Nacional** em `atos.cnj.jus.br` — é a fonte primária dos provimentos que alteram o Código Nacional de Normas (Prov. 149/2023), e tem precedência sobre qualquer notícia sobre eles.

### Kollemata (fonte 8, condicional)

O Kollemata (`kollemata.com.br`) exige login com reCAPTCHA e a sessão dura **~2 horas**, então a rotina automática **não consegue acessá-lo sozinha**.

- Se houver cookie válido em `E:\Users\<usuário>\Documents\ESTUDO\CARTORIO-MT\.kollemata-sessao` (linha única no formato `__kid=...; ci_session=...`), use-o.
- Testar validade: baixe `https://www.kollemata.com.br/` com o cookie; se o HTML contiver `>Sair<`, a sessão vive; se vier cabeçalho `Refresh:` para `/login/`, expirou.
- Busca (GET na raiz): `pagina`, `rows`, `gera-csv=nao`, `conector` (`&` todas / `|` qualquer / `f` frase), `q`, `campo[]` (`chave` verbetação, `ementa`, `integra`), `orgao[]`, `relator`, `data_de`, `data_ate`, `legislacao`, `legislacao_art`.
- **Órgãos úteis por id:** `316` CGJMT, `272` CSMSP, `283` CGJSP, `296` CNJ, `299` CGJMG, `300` CGJRS, `282` CGJSC, `313` CGJPA, `311` ONR, `295` IRIB, `288` Arisp.
- Para a rotina, priorize `orgao[]=316` (CGJMT) e `orgao[]=272` (CSMSP) com `data_de` = 7 dias atrás.
- Ementas marcadas **"IA-KollGEN"** são resumos gerados automaticamente pelo próprio sistema, **não são ementas oficiais** — sinalize sempre que usar uma.

Se não houver cookie válido, **diga isso explicitamente na edição**, siga com as sete fontes públicas e **peça o cookie ao usuário ao final**, com as instruções de coleta (F12 → Application → Cookies → `__kid` e `ci_session`).

**Pendência técnica em aberto:** construir um servidor MCP com navegador persistente (Playwright, perfil salvo) que dispense essa cobrança manual — o usuário resolveria o reCAPTCHA uma vez e a sessão seria reaproveitada. O usuário optou por adiar em 02/08/2026 e pediu que a rotina cobrasse o cookie a cada edição. Se ele perguntar sobre automatizar o Kollemata, retome daqui.

## 2. Critérios de relevância

Ordene os destaques por esta prioridade:

1. **Alterações legislativas ou normativas** — provimentos do CNJ, leis novas, decretos, provimentos de corregedorias estaduais
2. **Decisões judiciais paradigmáticas** — STJ, STF, CSMSP e CGJSP
3. **Temas de alta incidência em prova** — registro de imóveis, RCPN, tabelionato de notas, protesto, RTD
4. **Artigos doutrinários** com análise crítica de temas controversos
5. **Mudanças procedimentais** em serventias extrajudiciais

Priorize o que tem alta probabilidade de cobrança em concursos de cartório — **especialmente TJ-MT, que é o certame do usuário**, e também TJ-SP, TJ-MG, TJ-PR e TJ-RS.

## 3. Estrutura da edição

Escreva em `E:\Users\<usuário>\Documents\ESTUDO\CARTORIO-MT\guias\guia-AAAA-MM-DD.md`:

> **Atenção ao destino.** Use sempre o drive **E:**. Este material já foi perdido uma vez no perfil do usuário em `C:` — aquele drive opera com pouco espaço livre e houve remoção por processo externo à sessão. Nunca grave esta frente em C:.

### Cabeçalho
Período coberto, data de geração, contagem de itens por fonte, e — se aplicável — aviso de fonte inacessível.

### Destaques da semana
Para cada item relevante (tipicamente 5 a 12):

- **Título** e classificação (normativo / jurisprudencial / doutrinário / procedimental)
- **Fonte e data**, com link
- **O que mudou**, em 2 a 5 parágrafos de análise técnica — não resumo de manchete
- **Fundamentação legal precisa**: número do artigo, lei, provimento
- **Por que importa para a prova**: conexão com o conteúdo programático do edital do MT e com as teses já consolidadas no material de base

### Questões de fixação
**Cinco** questões objetivas, estilo CESPE/Cebraspe e VUNESP, **baseadas exclusivamente nos temas encontrados naquela semana**:

- Enunciado
- Quatro alternativas (A, B, C, D)
- **Gabarito comentado** com fundamentação — explique por que a correta está correta *e* por que cada distratora está errada

### Mapa de estudo dirigido
Tabela por matéria do edital, com:

| Matéria | Tema da semana | Prioridade | Leitura complementar |
|---|---|---|---|

Prioridade **Alta / Média / Baixa** para aquela semana. Leitura complementar = artigos de lei e doutrina específicos.

## 4. Entrega

1. Grave o markdown em `guias/guia-AAAA-MM-DD.md`.
2. Gere o EPUB da edição com `python E:\Users\<usuário>\Documents\ESTUDO\CARTORIO-MT\gerar_guia_epub.py guias/guia-AAAA-MM-DD.md` — sai um `.epub` ao lado, pronto para o Send to Kindle.
3. Apresente no chat um resumo curto: quantos destaques, quais os 3 mais importantes, e o que ficou de fora por indisponibilidade de fonte.

## 5. Regras de qualidade — inegociáveis

- **NUNCA invente** artigos, decisões, provimentos ou publicações. Se uma fonte não trouxe nada relevante na semana, **diga isso explicitamente** na edição, nominalmente, fonte por fonte.
- **Cite sempre a fundamentação precisa**: número do artigo, da lei, do provimento, do processo.
- Não confunda **notícia sobre** um ato com o **ato**. Ao noticiar provimento novo, abra o texto em `atos.cnj.jus.br` (ou no diário da corregedoria estadual) e cite o dispositivo.
- Ementas geradas por IA (KollGEN e similares) **não são fonte oficial** — marque e, se for citar tese, confira o inteiro teor.
- Semana fraca em publicações? **Reduza o número de destaques e mantenha a qualidade.** Não encha linguiça.
- Linguagem técnico-jurídica, sem simplificações excessivas.
- Onde houver divergência jurisprudencial ou dúvida sobre vigência, marque **[VERIFICAR]** e diga o que precisa ser conferido.

## 6. Continuidade entre edições

Antes de escrever, leia o índice `guias/INDICE.md` (crie se não existir) e as duas edições anteriores. **Não repita destaque já publicado**, salvo se houver desdobramento novo — nesse caso, diga que é desdobramento e remeta à edição anterior.

Ao terminar, acrescente uma linha ao `INDICE.md`:

```
- [AAAA-MM-DD](guia-AAAA-MM-DD.md) — N destaques — <os dois temas principais>
```
