---
name: travas-do-ato-cinco-categorias-sbroggioadv
title: Travas do ato — cinco categorias
description: 'Organiza obstáculos do ato em cinco categorias juridicamente distintas, após o gate estadual de IA: impeditiva absoluta, impeditiva condicional, sanável, consignável e devolutiva. Esta skill deve ser usada quando o pedido mencionar trava, impedimento, documento faltante, recusa, exigência, PLD, certidão fiscal, procuração vencida, testemunha por deficiência, gratuidade, dúvida ou encaminhamento ao juízo ou MP.'
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/travas-do-ato-cinco-categorias
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Travas do ato — cinco categorias

> Camada C3. Aplicar cinco estados, nunca dois. **Consignável não é sanável.**

## Anexos e skills obrigatórios

- `context/sequencia-do-ato.md` — régua A/B/C/D/E;
- `context/travas-defasagem.md` — exemplos ancorados e exceções;
- `context/precedentes-notariais.md` — certidão fiscal e procuração sem validade genérica;
- `context/res-cnj-35-2007-com-571-2024.md` — gates e devoluções;
- `context/prov-cnj-197-2025-conta-notarial.md` — recusa obrigatória e divergência;
- `regime-de-ia-da-uf`, `qualificacao-notarial-transversal` e a skill do ato correspondente.

## Entradas

Fixar UF, ato, modalidade, fato concreto, documento disponível, pessoa/órgão capaz de remover o obstáculo e dispositivo aplicável. Não classificar apenas pelo nome “pendência” ou “irregularidade”.

## Gate estadual de IA — antes da classificação

Executar primeiro `regime-de-ia-da-uf` para a função de enquadramento pretendida. Se a norma da UF proibir qualificação, interpretação, enquadramento ou influência sobre decisão jurídica, não atribuir categoria A-E nem prescrever a conduta: exibir os dispositivos e fatos relevantes e devolver o enquadramento ao titular.

No **MT**, o Provimento 1/2026-GAB-CGJ, art. 4º, II e III, alcança qualificação ou enquadramento legal e decisão jurídica produzida como apoio, sugestão ou influência, **ainda que sob revisão humana**. Nesse regime, esta skill organiza a régua federal e as fontes, mas o titular realiza a classificação e decide a conduta.

## Régua obrigatória

### A — Impeditiva absoluta

**Não lavrar; não há saneamento por esta via.** Fechar a porta extrajudicial e nomear o caminho admissível.

Exemplos: objeto ilícito ou impossível; testamento por procuração ou conjuntivo; bens no exterior em inventário extrajudicial; reconhecimento de filho no testamento que acompanha inventário extrajudicial; ato eletrônico fora da competência absoluta; assinatura remota fora do e-Notariado; ato eletrônico sem selo exigido; recusa obrigatória da conta notarial.

### B — Impeditiva condicional

**Não lavrar até cair um obstáculo externo.** Identificar quem destrava e qual prova deve voltar.

Exemplos: tributo não recolhido quando exigido antes da lavratura; ausência de advogado/defensor; falta de decisão judicial prévia sobre filho menor; inventário com testamento sem sentença transitada; nascituro; falta de outorga conjugal ou suprimento; procuração sem poder especial para alienar.

Não reduzir ato externo a “documento faltante”.

### C — Sanável

**Emitir nota de exigências conforme a UF; reanalisar após cumprimento.** Indicar dispositivo, razão concreta e caminho de correção.

Exemplos: documento do rol legal ausente; CCIR faltante em imóvel rural; qualificação incompleta; conteúdo obrigatório incompleto. Destacar: sanável não significa dispensável; lavrar imóvel rural sem CCIR pode gerar nulidade legal.

### D — Consignável

**Exibir a norma que manda lavrar, advertir ou consignar e devolver a decisão ao titular.** No regime federal de PLD, o CNN art. 179 torna infracional a recusa fundada somente na falta de informação ou documento exigido exclusivamente por esse capítulo; o art. 165-A, §3º manda consignar a resistência da parte. Não emitir nota para “sanar” condição que a norma proíbe transformar em impedimento e não converter a explicação normativa em ordem da ferramenta.

Aplicar especialmente:

- falta de dado obtido exclusivamente por deveres de PLD: o CNN manda consignar a resistência e comunicar à UIF quando cabível, sem transformar a falta em recusa;
- CND/CPEN ou certidão fiscal como condição genérica: o PCA do CNJ trata a certidão como informação, não bloqueio;
- procuração pública considerada “vencida” apenas pelo tempo: o PCA do CNJ afasta prazo genérico e exige verificação de atualidade;
- testemunha exigida apenas por deficiência: a Lei 8.935/1994 afasta a exigência, ressalvada a regra específica do testamento da pessoa cega;
- gratuidade legal: a norma impede negativa ou adiamento por incapacidade de pagamento;
- situação em que a norma manda advertir ou consignar, como indisponibilidade sem efeito impeditivo local.

Não achatar consignável em sanável. Não pedir correção de uma conduta que a lei protege.

### E — Devolutiva

**Não decidir mérito alheio; remeter ao juízo/MP ou orientar a via competente.** Produzir encaminhamento, não veredito.

Exemplos: dúvida sobre cabimento de inventário; manifestação do MP como gate de eficácia; impugnação que deve ir ao juízo; adjudicação inviável que exige orientação; divergência em conta notarial que gera ata e suspensão; matéria reservada ao registro imobiliário.

## Teste anti-achatamento

Responder antes de concluir:

1. O ato nunca pode ser praticado por esta via?
2. Um evento externo pode remover o bloqueio?
3. A própria parte pode suprir documento/requisito por nota?
4. A norma manda lavrar apesar do fato e constituir prova por consignação?
5. A decisão pertence a outro órgão?

Se as respostas 3 e 4 forem confundidas, interromper e reclassificar.

## Saída

| Campo | Resultado |
|---|---|
| fato e fonte | |
| categoria | A, B, C, D ou E; ou “enquadramento reservado ao titular” quando o gate estadual vedar |
| conduta imediata | |
| quem destrava/decide | |
| documento ou consignação | |
| comunicação | |
| reanálise/encaminhamento | |
| proibições | |

## Reprovação automática

- reduzir a régua a impeditiva/sanável;
- recusar hipótese consignável;
- emitir nota de exigências para PLD, certidão fiscal, prazo genérico de procuração, deficiência ou gratuidade;
- tratar obstáculo externo como simples juntada;
- decidir matéria do juízo, MP, registro ou autoridade tributária;
- omitir a consequência de nulidade de impedimento absoluto;
- classificar sem UF quando a conduta depender do estado.
- classificar o ato depois de `regime-de-ia-da-uf` apontar vedação de enquadramento, especialmente no MT.
