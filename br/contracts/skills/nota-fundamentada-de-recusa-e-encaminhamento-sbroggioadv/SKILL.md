---
name: nota-fundamentada-de-recusa-e-encaminhamento-sbroggioadv
title: Nota fundamentada de recusa e encaminhamento
description: Produz o entregável probatório da qualificação negativa com dispositivo legal, razão concreta e caminho de correção ou encaminhamento, respeitando a forma e o rito da UF sem inventar nota devolutiva federal. Esta skill deve ser usada quando o pedido mencionar redigir nota de exigências, fundamentar recusa, responder reclamação de recusa sem motivo, indicar diligência corretiva, encaminhar ao juízo ou MP, dúvida notarial ou documentar decisão do titular.
author: sbroggioadv
author_url: https://github.com/sbroggioadv/tabelionato-os-marketplace/tree/main/tabelionato-os/skills/nota-fundamentada-de-recusa-e-encaminhamento
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Nota fundamentada de recusa e encaminhamento

> Camada C3. Constituir prova da qualificação. Não existe nota devolutiva federal geral para o tabelião de notas.

## Anexos e skills obrigatórios

- `context/sequencia-do-ato.md` — posição do fluxo negativo;
- `context/travas-defasagem.md` — três elementos e proibições de generalidade;
- `context/uf-matriz-27.md` — categoria estadual do rito;
- `travas-do-ato-cinco-categorias` — classificação anterior;
- `recusa-e-nota-de-exigencias-por-uf` — forma, verbo e exigência superveniente;
- `duvida-notarial-por-uf` — destino do inconformismo.

## Pré-condições

Fixar UF, ato, modalidade, fato, documento analisado, dispositivo e categoria A/B/C/D/E. Não redigir nota antes de excluir hipótese consignável ou devolutiva.

Sem UF, produzir apenas relatório interno de qualificação e declarar que sua conversão em nota depende do regime estadual. Não chamar esse relatório de nota federal.

## Os três elementos

Redigir cada exigência com:

1. **Dispositivo legal:** norma, artigo e estado de vigência aplicável ao ato e à UF.
2. **Razão concreta:** fato individualizado que não satisfaz a norma, sem fórmula genérica.
3. **Caminho de correção:** providência possível, responsável e forma de reapresentação; quando não houver saneamento, nomear a via adequada.

Repetir a tríade por exigência. Não agrupar fundamentos distintos numa frase vaga.

## Fluxo por categoria

- **A — absoluta:** não oferecer correção impossível; explicar a vedação e a via alternativa.
- **B — condicional:** identificar o ato externo, a autoridade responsável e a prova que libera nova análise.
- **C — sanável:** emitir nota no regime da UF e indicar a diligência exata.
- **D — consignável:** não emitir recusa; converter o resultado em advertência/consignação no ato e comunicação quando cabível.
- **E — devolutiva:** preparar ofício, suscitação, remessa ou orientação, sem decidir o mérito de outro órgão.

## Forma estadual

Aplicar escrita obrigatória, escrita a requerimento, escrita se solicitada ou ausência de exigência formal conforme a UF. Cumprir conteúdo taxativo do RN, vedação de nota genérica em MA/BA/PE e regime de exigência superveniente. Não apresentar prudência probatória como comando.

Antes de indicar dúvida, classificar A1/A2/A3/B/C. Não prometer rito geral em A3, B ou C.

## Estrutura da entrega

```text
QUALIFICAÇÃO NEGATIVA — natureza e categoria
1. Ato, UF, modalidade e data de corte
2. Fato verificado
3. Dispositivo aplicável e vigência
4. Razão concreta
5. Providência corretiva ou obstáculo externo
6. Prazo e marco, somente se a UF fixar
7. Destino do inconformismo
8. Responsável pela análise e prova de entrega, quando exigidos
```

Não inserir dados pessoais reais no modelo. Gerar campos sem marcadores genéricos proibidos e solicitar os dados necessários durante o caso.

## Valor probatório e limite

Tratar a nota como prova constituída de que o titular qualificou e motivou a conduta, útil diante de representação por recusa desmotivada. Não afirmar que esse valor probatório transforma a nota em obrigação federal ou elimina responsabilidade.

## Reprovação automática

- emitir exigência sem dispositivo, razão ou caminho;
- usar apenas “legalidade”, “segurança jurídica” ou fórmula equivalente;
- chamar nota de exigência de instrumento federal geral;
- recusar categoria D;
- oferecer saneamento para categoria A;
- decidir matéria da categoria E;
- omitir forma, prazo ou conteúdo obrigatório da UF;
- prometer dúvida sem categoria estadual;
- inserir fato, documento ou artigo não verificado.
