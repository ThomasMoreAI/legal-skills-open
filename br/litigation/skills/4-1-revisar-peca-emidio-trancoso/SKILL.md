---
name: 4-1-revisar-peca-emidio-trancoso
title: Revisar peça — auditoria adversarial
description: Revisa qualquer peça já redigida linha por linha via auditoria adversarial — confere prova documental e testemunhal contra os documentos do caso, valida toda base jurídica com as skills de pesquisa, audita a honestidade dos argumentos e aponta as fragilidades que o adversário exploraria. Produz um relatório de revisão acionável.
author: emidio-trancoso
author_url: https://github.com/emidio-trancoso/advocacia-aberta/tree/main/.agents/skills/4.1-revisar-peca
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Revisar peça — auditoria adversarial

Esta skill é o seu procedimento de revisão escrito em português. Ela lê uma peça já redigida — petição, contestação, recurso, parecer, contrato, notificação, alegações finais, qualquer uma — linha por linha e citação por citação. Confere se cada afirmação de fato está sustentada pelos documentos do caso, se cada citação de lei e de jurisprudência é precisa e existe de fato, se os argumentos são honestos e bem enquadrados, e se há fragilidades que o adversário ou a contraparte exploraria. No final, entrega um relatório claro com os achados priorizados por gravidade e a ação recomendada para cada um.

> Quem redige olha para o argumento que quer defender. Quem revisa olha para a prova e para a fonte. Esta skill executa o segundo papel. Presuma que pode haver erro, confirme tudo por leitura direta da fonte e registre o que está certo com a mesma disciplina com que registra o que está errado.

---

## Como começar

Considere `<arquivo-da-peca>` o caminho relativo do arquivo `.md` informado pelo
usuário. Exemplo: `casos/joao-silva/pecas/contestacao-v1.md`.

Se o caminho não tiver sido informado, peça-o ao usuário. Sem o arquivo, não há o que
revisar.

A pasta do caso é tudo até `/pecas/` no caminho (no exemplo acima, `casos/joao-silva`). Daqui em diante, `<caso>` se refere a essa pasta.

### Dois modos de trabalho

- **Modo repositório** — a peça e as fontes estão em `casos/<caso>/`, nos caminhos do Passo 1.
- **Modo conversa** — a peça a revisar e as fontes foram anexadas na conversa (ou geradas
  nela). Confira contra os anexos e **entregue o relatório de revisão como arquivo** ao final.

Ao validar a base jurídica, a skill `buscar-fontes` (que usa o acervo, inclusive via MCP)
confere lei, súmulas, temas e teses. A skill `buscar-tjpr` depende de ferramenta local e
**não roda no ChatGPT Web hospedado**; sem ela, valide com a `buscar-fontes` e confira os
links oficiais de cada citação, registrando o que ficar pendente de confirmação em tribunal.

---

## Passo 1 — Conferir os arquivos disponíveis

Verifique quais arquivos existem na pasta do caso. Eles são as fontes contra as quais a peça será conferida. A peça em si é obrigatória; os demais podem não existir em todo caso, mas quanto menos houver, mais cega fica a revisão — registre o que falta.

| Arquivo | Caminho | Para que serve na revisão |
|---|---|---|
| Peça a revisar | `<arquivo-da-peca>` | Obrigatório — é o objeto da revisão |
| Resumo do caso | `<caso>/analise/SUMARIO.md` | Identificar partes, peças e o que cada documento contém |
| Diagnóstico de fragilidades | `<caso>/analise/DIAGNOSTICO.md` | Saber quais pontos próprios são vulneráveis |
| Legislação do caso | `<caso>/fundamentacao/LEGISLACAO.md` | Conferir texto de lei e súmulas já levantados |
| Jurisprudência do caso | `<caso>/fundamentacao/JURISPRUDENCIA.md` | Conferir acórdãos, temas e súmulas já levantados |
| Documentos dos autos | `<caso>/autos/` | Conferir cada afirmação de fato contra a prova |
| Transcrições de audiência | `<caso>/analise/` ou `<caso>/autos/` | Conferir cada citação de depoimento |

Se a peça (`<arquivo-da-peca>`) não existir, pare e avise o usuário. Para os demais,
liste os que faltam e siga em frente com os disponíveis.

---

## Passo 2 — Ler a peça inteira e inventariar as referências

Leia **todo** o arquivo `<arquivo-da-peca>`, sem pular seções. Enquanto lê, monte três
listas:

### 2a. Inventário documental
Toda afirmação de fato que aponta para um documento — uma página de PDF, um anexo, um contrato, uma nota fiscal, um print de mensagem. Para cada uma, anote: qual documento, em que ponto, e **qual fato** a peça diz que aquele documento prova.

### 2b. Inventário de depoimentos
Toda citação de fala de audiência. Para cada uma, anote: o texto entre aspas, o momento (timestamp, se houver), quem falou e em que qualidade (parte, testemunha compromissada, informante sem compromisso).

### 2c. Inventário jurídico
Toda citação de lei e de jurisprudência — artigos, súmulas, temas repetitivos, acórdãos, cláusulas contratuais legais. Para cada uma, anote: a identificação completa, o texto entre aspas (se houver) e **qual argumento ou conclusão** da peça aquela citação sustenta.

Ao terminar, informe ao usuário os totais: *"Encontrei N referências a documentos, M citações de depoimento e K citações jurídicas. Vou conferir cada uma."*

---

## Passo 3 — Conferir a prova documental

Para **cada** item do inventário 2a, abra o documento correspondente em `<caso>/autos/` e verifique:

| Verificação | Pergunta |
|---|---|
| **Existe** | O documento e a página realmente existem? |
| **É literal** | Se a peça usa aspas, o texto entre aspas está idêntico ao documento? |
| **É fiel ao contexto** | O fato atribuído ao documento é o que ele de fato demonstra, no contexto em que aparece? |
| **Atribuição correta** | Em mensagens, e-mails e conversas, quem a peça diz que enviou é mesmo quem enviou? Data e hora conferem? |
| **Juntado pelo lado certo** | Quando a peça diz "a própria parte contrária juntou", o documento foi mesmo juntado por ela? |

Classifique cada item:
- **Confere** — registrar para a tabela final.
- **Impreciso** — existe, mas com página errada, paráfrase apresentada como aspas, ou ênfase fora do contexto. Indicar a correção.
- **Não localizado** — não está onde a peça diz. Grave. Indicar a correção.
- **Descontextualizado** — existe literalmente, mas o documento prova coisa diferente (ou o oposto) do que a peça atribui. Grave.

> Atenção especial a prints de mensagem e documentos não assinados: confira quem
> enviou, quem juntou, datas e contexto. Se o caso já passou pela skill `diagnosticar`,
> use o DIAGNOSTICO.md como guia desses pontos sensíveis.

---

## Passo 4 — Conferir os depoimentos

Para **cada** item do inventário 2b, abra a transcrição correspondente (em `<caso>/analise/` ou `<caso>/autos/`) e verifique:

| Verificação | Pergunta |
|---|---|
| **Texto literal** | As aspas são idênticas à transcrição? Paráfrase disfarçada de citação literal é erro grave. |
| **Momento correto** | O timestamp citado bate com a posição real do trecho na gravação? |
| **Quem falou** | Quem disse a frase é mesmo quem a peça nomeia? Cruzar com a ata da audiência no SUMARIO. |
| **Qualidade do depoente** | Parte, testemunha compromissada e informante sem compromisso têm pesos diferentes. Trocar parte por testemunha é erro grave. |
| **Quem perguntou** | Resposta dada ao advogado contrário pesa mais que resposta dada ao próprio advogado. Se a peça atribui peso de contraditório a uma fala ensaiada, sinalizar. |
| **Contexto preservado** | A citação não foi cortada num ponto que muda o sentido (por exemplo, omitir o "mas" seguinte que retrata a afirmação). |
| **Trecho incerto** | Se a transcrição marca o trecho como incerto ou duvidoso, a peça não pode citá-lo como fato firme. |

Use as mesmas quatro classificações do Passo 3 (Confere / Impreciso / Não localizado / Descontextualizado).

---

## Passo 5 — Conferir a base jurídica contra a fundamentação do caso

Para **cada** item do inventário 2c, confronte com `<caso>/fundamentacao/LEGISLACAO.md` (texto de lei) ou `<caso>/fundamentacao/JURISPRUDENCIA.md` (súmulas, temas, acórdãos), conforme o tipo da citação:

| Verificação | Pergunta |
|---|---|
| **Está na fundamentação?** | A citação consta de LEGISLACAO.md ou de JURISPRUDENCIA.md? Se não consta, o risco de erro ou invenção é maior — marcar para busca externa obrigatória no Passo 6. |
| **Texto literal** | Ementas, trechos centrais e artigos reproduzem exatamente o que está na fundamentação? Paráfrase apresentada como citação literal é erro grave. |
| **Identificação completa** | Acórdãos: número do processo, relator, data e órgão julgador. Súmulas e temas: número, tribunal e situação (ativa, cancelada, superada). |
| **Vigência** | A súmula não foi cancelada? A tese não foi superada por decisão posterior? O artigo está com a redação atual? |
| **Rito compatível** | Precedente de um rito (por exemplo, procedimento comum) usado em outro (por exemplo, Juizado Especial) sem ressalva é bandeira amarela. |
| **Enquadramento honesto** | O ponto efetivamente decidido no precedente é **o mesmo** que a peça precisa, ou só parece análogo? |

Classifique cada item: Confere / Impreciso / Ausente ou inventado / Existe mas não sustenta o argumento.

Toda citação que não seja "Confere" entra obrigatoriamente no Passo 6. As que conferem também passam pelo Passo 6 — confirmar a base jurídica por fonte externa é regra geral, não exceção.

---

## Passo 6 — Validar toda a base jurídica pelas skills de pesquisa

> Este passo é obrigatório e completo. **Toda** citação jurídica passa por validação externa. O objetivo não é marcar "confere" rápido — é testar se o argumento se sustenta de verdade ou se é forçação. Quando for forçação, procure o trecho ou o precedente que realmente encaixa. Quando nada encaixar, registre isso como achado e sinalize o argumento como vulnerável.

### 6a. Agrupar por argumento
Identifique cada argumento, cláusula ou conclusão central da peça. Liste todas as fontes jurídicas que a peça usa para sustentar cada um.

### 6b. Buscar externamente
Para cada argumento, rode em sequência:

1. **Skill `buscar-fontes` com os termos do argumento** — súmulas, temas repetitivos
   e leis. Use 3 a 5 termos centrais. Anote a força de cada resultado (vinculante,
   persuasivo, orientativo).
2. **Skill `buscar-tjpr` com os termos do argumento** — acórdãos do tribunal
   competente. Use 3 a 5 termos; se a busca zerar, fragmente os termos em vez de
   empilhar sinônimos.

Para um acórdão limítrofe — a ementa sugere apoio mas não confirma —, leia o inteiro teor antes de validar. Ementa engana; só a leitura do ponto decidido evita citar um precedente que na verdade não serve.

### 6c. Classificar o resultado de cada fonte

| Status | Significado | Ação |
|---|---|---|
| **Confirmada** | A fonte é real, vigente e sustenta o argumento. | Manter. |
| **Substituível** | A fonte existe, mas há precedente ou súmula **mais forte ou mais direto** disponível. | Registrar a substituição sugerida com identificação, trecho literal e link. |
| **Forçada** | A fonte existe, mas o ponto decidido **não é** o que a peça precisa. O adversário sustentaria a distinção. | Procurar alternativa real. Se houver, substituir. Se não, rebaixar o argumento ou apresentá-lo sem o precedente. |
| **Inexistente ou superada** | Não encontrada, cancelada ou superada por decisão posterior. | Remover e procurar substituto. |
| **Sem precedente direto** | Não há súmula ou acórdão diretamente sobre o ponto. | Registrar o achado. Sinalizar que o argumento depende de lei ou de construção doutrinária, não de precedente. |

### 6d. Argumentos sem fonte na fundamentação do caso
Para os que saíram do Passo 5 sem amparo em LEGISLACAO.md nem JURISPRUDENCIA.md, a busca externa é a única validação possível. Se nada retornar, o argumento está desancorado — achado grave.

### 6e. Honestidade sobre achados negativos
Se um argumento não tem precedente direto, diga isso ao usuário. Precedente forçado é pior que nenhum: o adversário o distingue e expõe a fragilidade. "Não foi encontrado precedente direto sobre X" é um achado legítimo, não uma falha da revisão.

---

## Passo 7 — Auditar os argumentos e a lógica

Com a prova e a base jurídica já conferidas, olhe a arquitetura dos argumentos.

- **Conclusão sustentada** — cada argumento ou pedido da peça decorre de fato provado + norma aplicável? Há salto de raciocínio em algum ponto?
- **Apoio suficiente** — cada argumento se apoia em ao menos dois elementos (documento + depoimento, ou dois documentos convergentes), ou pende de um único elemento frágil?
- **Resposta ao adversário** — se há peça da parte contrária no caso, cada argumento principal dela foi enfrentado em algum ponto da peça? Liste os argumentos do adversário **não** rebatidos: são flancos abertos.
- **Pontos fracos próprios** — os pontos vulneráveis listados no DIAGNOSTICO.md estão neutralizados ou contextualizados na peça? Os que ficaram de fora são flancos abertos.
- **Coerência interna** — a peça afirma uma coisa numa seção e a contraria em outra? Data, valor ou documento citado de forma divergente entre seções? Sinalizar cada incoerência.
- **Honestidade do enquadramento** — algum fato está apresentado de forma que sugere mais do que a prova mostra? Alguma omissão convenientemente deixa de fora um detalhe que enfraquece o argumento? O adversário veria isso.

---

## Passo 8 — Conferir a forma e o estilo

Varredura rápida — não precisa listar todos os casos, basta amostrar e apontar o padrão:

- [ ] Cada parágrafo abre afirmando uma **posição**, não anunciando um tema ("Quanto a...", "Cumpre analisar...").
- [ ] **Voz ativa** predomina ("a clínica realizou", não "foi realizado").
- [ ] Sem arcaísmos desnecessários ("outrossim", "destarte", "hodiernamente").
- [ ] Uma ideia por parágrafo; parágrafos curtos.
- [ ] O nome da parte cliente aparece no corpo, não só "o autor" ou "a ré".
- [ ] Toda citação tem contexto antes e conclusão depois.
- [ ] Toda afirmação de fato relevante traz a referência ao documento que a prova.

---

## Passo 9 — Escrever o relatório de revisão

Salve em `<caso>/pecas/revisao-<arquivo>.md`, onde `<arquivo>` é o nome da peça revisada (por exemplo, `contestacao-v1.md` gera `revisao-contestacao-v1.md`). Se o arquivo já existir, acrescente um sufixo para não sobrescrever.

Estrutura do relatório:

```markdown
---
peca_revisada: [caminho relativo da peça]
caso: [identificação do caso]
data: [AAAA-MM-DD]
totais: [N documentos · M depoimentos · K citações jurídicas]
---

# Revisão — [nome do arquivo]

## Resumo

- Achados graves: [n] — exigem correção antes de protocolar
- Ajustes: [n] — melhoram a peça, não a impedem
- Confirmados: [n] — verificados e corretos

Veredicto: [Pronta · Ajustes recomendados · Refazer]

Os 3 pontos mais críticos:
1. ...
2. ...
3. ...

---

## 1. Prova documental
| Referência na peça | Status | Observação | Correção |
|---|---|---|---|

## 2. Depoimentos
| Citação | Momento na peça | Momento real | Quem a peça diz | Quem de fato | Status | Correção |
|---|---|---|---|---|---|---|

## 3. Base jurídica
| Citação na peça | Está na fundamentação? | Literal? | Status externo | Substituição sugerida |
|---|---|---|---|---|

Para cada argumento, registrar a busca executada (`buscar-fontes` e `buscar-tjpr`),
o resultado, a substituição sugerida com trecho literal e link, e os achados negativos.

## 4. Argumentos e lógica
- Conclusões sustentadas: ...
- Argumentos do adversário não rebatidos: ...
- Pontos fracos próprios não neutralizados: ...
- Incoerências internas: ...

## 5. Forma e estilo
- Padrões a corrigir (2 a 3 exemplos): ...

## 6. Plano de correção
Lista numerada por prioridade, do mais grave ao ajuste fino, com a localização de cada item na peça.

## 7. Próximo passo
- [ ] Refazer a peça aplicando o plano de correção
- [ ] Revisar de novo após a nova versão
```

---

## Passo 10 — Apresentar ao usuário

Depois de salvar, mostre ao usuário:
1. O caminho do relatório gerado.
2. O veredicto (Pronta / Ajustes recomendados / Refazer).
3. Os 3 achados mais graves, com a localização de cada um na peça.
4. As substituições jurídicas mais importantes encontradas no Passo 6.
5. O próximo passo: após corrigir os achados, o ciclo é **`redigir-peca`** (nova
   versão) → **`revisar-peca`** de novo → **`diagramar-peca`**.

---

## Princípios do revisor

| Princípio | Como aplicar |
|---|---|
| Presumir que pode haver erro | Nunca marcar "confere" por suposição — sempre abrir o documento, a transcrição ou a fundamentação. |
| A aspa é literal | Citação entre aspas tem que bater palavra por palavra com a fonte. Paráfrase entre aspas é achado grave. |
| Precedente forçado é pior que nenhum | Quando o precedente não decide o ponto, procure alternativa. Se não houver, remova e avise o usuário. |
| Achado negativo tem valor | "Não há precedente direto sobre X" sinaliza um argumento vulnerável antes que o adversário o faça. |
| Rito antes do mérito | Precedente de um rito usado em outro precisa de ressalva ou substituição. |
| Ementa engana | Para acórdão limítrofe, leia o inteiro teor antes de validar. |
| O revisor não reescreve | Esta skill produz diagnóstico e plano de correção. Reescrever é tarefa da skill `redigir-peca` na próxima volta. |
