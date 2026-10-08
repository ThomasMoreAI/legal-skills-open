---
name: analise-letradalei
title: Análise Processual e Minuta
description: Diagnostica a fase de um processo cível ou trabalhista e redige a peça cabível (réplica, recursos, cumprimento de sentença, embargos, ações autônomas etc.), fundamentada. Use para "o que faço agora?", "perdi a sentença, como recorro?", "cabe [peça/recurso]?". Não use para petição inicial, contestação ou fundamentação judicial, há skills próprias.
author: letradalei
author_url: https://github.com/letradalei/skills/tree/main/plugins/letradalei/skills/analise
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: employment
language: pt
sources:
- title: Acoes Autonomas
  path: references/acoes-autonomas.md
- title: Cumprimento E Execucao
  path: references/cumprimento-e-execucao.md
- title: Irdr
  path: references/irdr.md
- title: Recursos Extraordinarios
  path: references/recursos-extraordinarios.md
- title: Recursos Ordinarios
  path: references/recursos-ordinarios.md
- title: Replica E Tutelas
  path: references/replica-e-tutelas.md
---

# Análise Processual e Minuta

O advogado sabe o que aconteceu; nem sempre sabe qual é a próxima peça, ou como estruturá-la com rigor. Esta skill lê o que está nos autos (ou o que o usuário descreveu), identifica o momento processual, propõe a peça mais adequada e redige o rascunho com fundamentação verificada lei por lei.

O que a separa das demais:
1. **Diagnostica antes de redigir.** Nenhuma linha de peça sai sem que a fase processual esteja identificada e confirmada pelo usuário.
2. **Cobre a fase pós-postulação** no rito comum e trabalhista: réplica, recursos (apelação, recurso ordinário, agravo, embargos), cumprimento de sentença e execução.
3. **Não adivinha intenção.** Se o usuário quer recorrer mas a sentença foi favorável, a skill pergunta antes de produzir.

O rascunho **não é peça pronta**, é andaime revisável. Quem assina, ajusta tom e decide estratégia é a pessoa habilitada na OAB.

## Contratos compartilhados (leia antes de redigir)

- **`letradalei:pesquisa`** — como buscar e verificar lei e jurisprudência no MCP. Nenhuma citação vem de memória.
- **`../_shared/intake.md`** — disciplina de entrevista (em blocos de até 4 perguntas/rodada), protocolo "Informar manualmente" e fallback não-interativo.
- **`../_shared/citacao-e-formato.md`** — como uma fonte verificada entra na peça e como o bloco de citação é formatado no `.docx` (vale para lei e jurisprudência).
- **`../_shared/saida.md`** — arquivos de saída, montagem do `.docx`, marcadores em vermelho e bloco de notas.

Regras desta peça, além da `pesquisa`: citação sem `citacao` + `source_url` → `[CITAÇÃO PENDENTE]`; `situacao` ≠ `vigente` → `[VERIFICAR VIGÊNCIA, situação: <X>]`; norma estadual/municipal/infralegal → `[FORA DO CORPUS]`; busca vazia/contraditória → registre via `acervo · reclame_aqui` antes de seguir.

**Fontes específicas desta skill (além de lei e jurisprudência):**
- **Autos do processo.** Quando o usuário enviar o processo ou documentos dos autos, a skill pode extrair e citar conteúdo das peças já produzidas — sobretudo petições anteriores da parte que o usuário representa (revelam as teses sustentadas e o que foi prequestionado). O **acórdão recorrido** e outras decisões dos autos **não são jurisprudência**: são objeto do recurso e podem ser citados literalmente para demonstrar o cabimento ou o erro. Sinalize a fonte: `Fonte: [nome do documento nos autos], [data/ID], autos nº [...]`. Nunca atribua à parte contrária argumento que não conste dos autos.
- **Recurso Extraordinário (RE ao STF).** Jurisprudência do STF é estruturalmente necessária: use `jurisprudencia-federal · buscar_precedentes` com `autoridade: "STF"` para localizar o Tema de Repercussão Geral aplicável. Sem resultado pertinente → `[JURISPRUDÊNCIA, confirmar Tema e tese antes do protocolo]`.

## Passo 1, Guardrail: sem fase, sem peça

**Não produza nenhuma peça antes de diagnosticar a fase.** Esta skill serve a múltiplos momentos processuais; uma peça feita sem diagnóstico é, em regra, inútil ou danosa. Colete primeiro (siga `../_shared/intake.md`):

**Rodada 1, Fase e documentos:**
- **O que acabou de acontecer no processo?** (Ex.: "recebi a contestação", "a sentença saiu e perdi", "ganhei e quero cobrar".) Se houver documento dessa fase, peça o arquivo ou o texto.
- **Qual é o rito?** comum, JEC, trabalhista, Fazenda Pública, outro?
- **Qual parte o usuário representa?** autor(a), réu(é), ambos?
- **Há prazo correndo?** Data de publicação/intimação e data-limite que o usuário conhece.

Se o usuário não fornecer **nenhuma** descrição da fase **e** **nenhum** documento, responda com clareza e firmeza:

> "Para redigir a peça certa, preciso saber em que ponto o processo está. Sem isso, qualquer minuta seria genérica e possivelmente inadequada. Me conta: (a) o que acabou de acontecer? (b) qual é o documento mais recente — contestação, sentença, decisão, algo do tribunal? (c) você representa o(a) autor(a) ou o(a) réu(é)?"

Se o usuário insistir ("monta uma apelação genérica", "faz um modelo de réplica"), **mantenha a recusa.** Uma apelação sem a sentença que ataca é pura forma vazia. Explique de forma direta, sem moralismo. Não ceda nas duas insistências.

## Passo 2, Diagnóstico da fase e mapa de peça cabível

Após receber os documentos ou a descrição da fase, diagnostique e mapeie:

| Fase identificada | Peça cabível | Base legal |
|---|---|---|
| Autor recebeu contestação, réu arguiu matérias do art. 337 ou fatos extintivos/modificativos/impeditivos | Réplica **obrigatória** | CPC arts. 350-351 |
| Autor recebeu contestação, réu não arguiu matérias novas | Réplica **facultativa** (estratégica) | CPC art. 350 |
| Parte precisa de medida urgente antes de ajuizar a ação principal, urgência que antecipa o próprio bem da vida pretendido | Tutela antecipada antecedente | CPC art. 303 |
| Parte precisa de medida urgente para **assegurar** o resultado da ação principal, não antecipa o bem da vida, mas garante a utilidade do processo futuro | Tutela cautelar antecedente | CPC arts. 305-310 |
| Parte perdeu sentença, rito comum ou especial (não JEC, não trabalhista) | Apelação | CPC arts. 1.009-1.014 |
| Parte recebeu decisão interlocutória que consta no rol do art. 1.015 do CPC | Agravo de instrumento | CPC arts. 1.015-1.020 |
| Parte recebeu sentença/decisão com omissão, contradição, obscuridade ou erro material | Embargos de declaração | CPC arts. 1.022-1.026 |
| Parte ganhou sentença de pagar quantia, quer cobrar | Cumprimento de sentença (quantia) | CPC arts. 523-527 |
| Parte ganhou sentença de obrigação de fazer/não fazer, quer cobrar | Cumprimento de sentença (obrigação) | CPC art. 536 |
| Parte ganhou sentença de entregar coisa, quer cobrar | Cumprimento de sentença (entrega) | CPC art. 538 |
| Executado quer se defender em cumprimento de sentença de quantia certa, transcorridos os 15 dias do art. 523 sem pagamento | Impugnação ao cumprimento de sentença | CPC art. 525 |
| Executado quer se defender em execução de **título extrajudicial** (cheque, nota promissória, contrato, CDA etc.) | Embargos à execução | CPC arts. 914-917 |
| Executado quer arguir matéria de **ordem pública** (prescrição, nulidade do título, ilegitimidade) **sem penhora prévia e sem dilação probatória**, em qualquer execução | Exceção de pré-executividade | Construção pretoriana, STJ Súmula 393; âncora normativa: CPC art. 803, par. único |
| **Terceiro que não é parte** no processo sofre penhora, arresto ou constrição sobre bem seu | Embargos de terceiro | CPC arts. 674-681 |
| Parte perdeu sentença da Vara do Trabalho | Recurso ordinário trabalhista | CLT art. 895, I |
| Parte perdeu sentença de juizado especial cível (JEC) | Recurso inominado | Lei 9.099 art. 41 |
| Parte perdeu acórdão de TRF, TJ ou TST e quer levar questão constitucional ao STF, após esgotadas as vias ordinárias (inclusive embargos de declaração para prequestionamento) | Recurso Extraordinário | CF art. 102, III, "a" + CPC arts. 1.029-1.035 |
| Parte perdeu acórdão de TRF ou TJ e quer levar questão de direito federal infraconstitucional ao STJ | Recurso Especial (REsp) | CF art. 105, III + CPC arts. 1.029-1.032 |
| ⚠️ Acórdão de TRF ou TJ viola **simultaneamente** lei federal infraconstitucional **e** a Constituição Federal | **RE + REsp interpostos simultaneamente** em petições separadas ao mesmo Presidente/VP do tribunal de origem | CF arts. 102 III "a" e 105 III + CPC art. 1.031, a não interposição de um implica preclusão da matéria correspondente |
| Presidente/VP do tribunal de origem negou seguimento ao RE/REsp por inadmissibilidade geral (art. 1.030, V, CPC), motivo não é conformidade com repetitivo/RG | Agravo em RE ou Agravo em REsp (ARE/AREsp) ao tribunal superior | CPC art. 1.042 |
| Acórdão de turma do STJ ou STF em RE/REsp **diverge de outro acórdão do mesmo tribunal** sobre a mesma questão | Embargos de divergência | CPC arts. 1.043-1.044 |
| Presidente/VP do tribunal de origem negou seguimento ao RE ou REsp **com fundamento em conformidade com entendimento de casos repetitivos ou RG** (art. 1.030, I ou III, CPC) | Agravo Interno ao próprio tribunal de origem | CPC arts. 1.021 + 1.030, §2º |
| Relator do tribunal (qualquer instância) proferiu decisão monocrática e a parte quer submeter ao colegiado | Agravo Interno | CPC art. 1.021 |
| Tribunal **denegou** HC/MS/HD/MI em **competência originária** (única instância) e a parte vencida quer recorrer | Recurso Ordinário Constitucional | CF art. 102, II (ao STF) ou 105, II (ao STJ) + CPC arts. 1.027-1.028 |
| Ato/decisão usurpou competência de tribunal, descumpriu decisão dele, ou contrariou súmula vinculante, decisão do STF em controle concentrado, IRDR ou IAC, **antes** do trânsito em julgado | Reclamação constitucional | CPC arts. 988-993 |
| Decisão **de mérito transitada em julgado** padece de um dos vícios do art. 966 (incompetência absoluta, violação manifesta de norma, prova falsa, prova nova, erro de fato etc.) | Ação Rescisória | CPC arts. 966-975 |
| Terceiro (que não é parte na ação) pretende a coisa ou o direito disputado entre autor e réu, sentença ainda não proferida | Oposição | CPC arts. 682-686 |
| **Poder Público** quer suspender liminar/sentença concessiva de MS ou tutela de urgência que cause grave lesão à ordem, saúde, segurança ou economia públicas | Suspensão de segurança | Lei 12.016/2009 art. 15 (MS) / Lei 8.437/1992 art. 4 [FORA DO CORPUS] (outras ações) |
| Há **múltiplos processos** com mesma questão unicamente de direito e risco de decisões divergentes, parte, MP ou Defensoria quer fixar tese vinculante no tribunal | Suscitação de IRDR | CPC arts. 976-987 |
| ⚠️ Situação não coberta por nenhum módulo acima | **Módulo subsidiário** (Passo 3.6): diagnostica a fase e orienta o próximo passo, informando que não há minuta específica | — |

**Antes de prosseguir, devolva o diagnóstico ao usuário para confirmação:**

> "Com base no(s) documento(s) fornecido(s), a fase que identifico é: [fase]. A peça mais adequada é: [peça], com fundamento no(s) art(s). [X] do [diploma]. Confirmo o entendimento antes de redigir, está correto?"

Só redija após a confirmação. Se o usuário discordar, pergunte o que está errado e ajuste.

## Passo 3, Intake específico e roteamento por módulo

> **Distinção estrutural, recursos × ações autônomas de impugnação (ler antes de qualquer módulo).**
> A natureza da peça molda o intake e a estrutura:
> - **Recursos** (apelação, agravo de instrumento, embargos de declaração, recurso ordinário trabalhista, recurso inominado, RE, REsp, ARE/AREsp, agravo interno, recurso ordinário constitucional): impugnam decisão **dentro do mesmo processo** e têm **prazo de interposição**. A peça abre por uma seção de **tempestividade**.
> - **Ações autônomas de impugnação** (reclamação, ação rescisória): **não são recursos**, instauram **processo novo**. O intake e a estrutura aproximam-se de uma **petição inicial** (qualificação completa, causa de pedir, pedido, valor da causa, requisitos do art. 319 e ss.). **Não há "tempestividade recursal"**, há cabimento de ação e, conforme o caso, prazo decadencial ou limite negativo (rescisória: 2 anos decadenciais com termo variável, art. 966/975; reclamação: inadmissível após o trânsito em julgado, art. 988, §5º, I).
>
> Tratar uma ação autônoma como recurso (ou vice-versa) é erro estrutural. Confirme a natureza antes de escolher o esqueleto.

### Como usar os módulos

Cada família de peça está em um arquivo de `references/`. **Depois de confirmar o diagnóstico (Passo 2), abra apenas o arquivo da peça identificada e siga o módulo** — não carregue os outros. Cada arquivo é autossuficiente quanto ao intake e à estrutura; os contratos compartilhados e os Passos 4–6 abaixo valem para todos.

| Peça diagnosticada | Arquivo de referência |
|---|---|
| Réplica; tutela antecipada/cautelar antecedente | `references/replica-e-tutelas.md` |
| Apelação, agravo de instrumento, embargos de declaração, recurso ordinário trabalhista, recurso inominado (JEC), recurso ordinário constitucional, agravo interno | `references/recursos-ordinarios.md` |
| Recurso extraordinário, recurso especial, agravo em RE/REsp, embargos de divergência | `references/recursos-extraordinarios.md` |
| Cumprimento de sentença (quantia/obrigação), impugnação ao cumprimento, embargos à execução, exceção de pré-executividade | `references/cumprimento-e-execucao.md` |
| Reclamação, ação rescisória, oposição, embargos de terceiro, suspensão de segurança | `references/acoes-autonomas.md` |
| Suscitação de IRDR | `references/irdr.md` |

### 3.6, Módulo subsidiário (situação sem módulo específico)

Quando o Passo 2 identificar a fase mas não houver módulo correspondente, a skill não recusa o trabalho:
1. **Descreve a fase e a peça cabível** com o fundamento legal (buscar via MCP o que for possível).
2. **Informa** que não há módulo dedicado ainda.
3. **Oferece produzir uma estrutura básica** com intake mínimo, usando os princípios gerais (dispositivos via MCP, sem jurisprudência sem marcador, marcadores nos pontos incertos).
4. **Registra o gap** para o usuário saber que a peça é menos estruturada que as de módulo dedicado.

> "Identifiquei que a fase é [fase] e a peça cabível seria [peça], com fundamento no(s) art(s). [X] do [diploma]. Esta skill ainda não tem módulo dedicado para esse tipo. Posso produzir uma minuta estrutural básica, menos detalhada, ou apenas orientar os próximos passos sem redigir. Como prefere?"

## Passo 4, Pesquisa legal

Para cada dispositivo identificado no diagnóstico e na estrutura, siga `letradalei:pesquisa`: identifique a norma (CPC, CLT, CC, lei especial), busque, verifique `situacao` e registre o bloco no formato de `../_shared/citacao-e-formato.md`. Norma fora do corpus → `[FORA DO CORPUS]`. **Sem suplementação silenciosa:** MCP retornou pouco/nada → pergunte ao usuário antes de buscar fora.

**Prioridades de busca por tipo de peça:**

| Peça | Dispositivos essenciais | norma (sigla/slug) |
|---|---|---|
| Réplica | arts. 350, 351, 435 | Lei-13105-2015 |
| Tutela antecipada antecedente | arts. 303 (caput e §§1º-6º), 304 (estabilização) | Lei-13105-2015 |
| Tutela cautelar antecedente | arts. 305, 306, 307, 308, 309, 310 | Lei-13105-2015 |
| Apelação | arts. 1.009, 1.010, 1.012, 1.003 §5º, 85 §11 | Lei-13105-2015 |
| Agravo de instrumento | art. 1.015 (inciso específico), 1.016-1.020 | Lei-13105-2015 |
| Embargos de declaração | arts. 1.022, 1.023, 1.024 | Lei-13105-2015 |
| Cumprimento (quantia) | arts. 523, 523 §1º, 835 | Lei-13105-2015 |
| Cumprimento (obrigação) | arts. 536, 537 | Lei-13105-2015 |
| Impugnação ao cumprimento de sentença | arts. 525 (caput e §§1º, 4º, 5º, 6º, 12-14) | Lei-13105-2015 |
| Embargos à execução | arts. 914 (caput e §§1º-2º), 915 (caput e §§1º-3º), 917 (caput e §§1º-7º), 919 (caput e §§1º-5º) | Lei-13105-2015 |
| Exceção de pré-executividade | art. 803 (caput e par. único, base normativa mais próxima), art. 924 (extinção da execução); dispositivo de prescrição/decadência aplicável à obrigação via MCP; cabimento é pretoriano, marcador obrigatório | Lei-13105-2015 + lei especial da obrigação |
| Embargos de terceiro | arts. 674 (caput e §§1º-2º), 675 (caput e par. único), 676, 677 (caput e §§1º-4º), 678 (caput e par. único), 679, 681; art. 792 se fraude à execução | Lei-13105-2015 |
| Recurso ordinário trabalhista | CLT arts. 895, 899 | DL-5452-1943 |
| Recurso inominado JEC | Lei 9.099 arts. 41, 42 | [verificar norma, provável Lei-9099-1995] |
| Recurso Extraordinário | CF art. 102 III "a"; CPC arts. 1.029, 1.003 §5º, 1.035, 1.037; dispositivos constitucionais violados; art. 1.031 se simultâneo com REsp | CF-1988 + Lei-13105-2015 |
| Recurso Especial | CF art. 105 III; CPC arts. 1.029, 1.003 §5º, 1.032, 85 §11; dispositivos de lei federal violados; art. 1.031 se simultâneo com RE | CF-1988 + Lei-13105-2015 |
| Agravo em RE / Agravo em REsp | CPC arts. 1.042, 1.030 V, 1.003 §5º | Lei-13105-2015 |
| Embargos de divergência | CPC arts. 1.043 (caput e §§1º-5º), 1.044 (caput e §§1º-2º); dispositivo legal/constitucional da questão de fundo via MCP; acórdão paradigma com `[JURISPRUDÊNCIA NÃO VERIFICADA VIA MCP]` | Lei-13105-2015 |
| Agravo Interno | CPC arts. 1.021, 1.021 §2º; se hipótese 2: também art. 1.030 §2º | Lei-13105-2015 |
| Recurso Ordinário Constitucional | CF art. 102 II ou 105 II; CPC arts. 1.027, 1.028; prazo: 15 dias úteis (art. 1.003 §5º) na regra geral, inclusive HC ao STF (102 II "a"); 5 dias (Lei 8.038 art. 30, `[VERIFICAR/FORA DO CORPUS]`) só no HC ao STJ (105 II "a"); dispositivo legal violado | CF-1988 + Lei-13105-2015 |
| Reclamação constitucional | CPC arts. 988 (caput, inciso e §§4º/5º), 989, 992 | Lei-13105-2015 |
| Ação Rescisória | CPC arts. 966 (inciso e §§1º/5º/6º), 967, 968 (I, II, §§1º/2º), 969, 970, 975 (caput e §§1º/2º/3º) | Lei-13105-2015 |
| Oposição | CPC arts. 682, 683 (caput e par. único), 684, 685 (caput e par. único), 686 | Lei-13105-2015 |
| Suspensão de segurança | Lei 12.016/2009 art. 15 (caput e §§1º-5º) no corpus; Lei 8.437/1992 art. 4 [FORA DO CORPUS, transcrever manualmente] | Lei-12016-2009 |
| Suscitação de IRDR | CPC arts. 976 (caput e §§1º-5º), 977 (caput e par. único), 978, 980 (caput e par. único), 982 (caput e §§1º-5º), 985 (caput e §§1º-2º), 987 (caput e §§1º-2º); dispositivo legal controvertido via MCP | Lei-13105-2015 |

## Passo 5, Conferências antes da entrega

1. **Diagnóstico confirmado** pelo usuário antes de redigir?
2. **Prazo buscado via MCP** (texto literal da lei, não de memória), registrado nas notas?
3. **Cabimento verificado.** Agravo: o inciso do art. 1.015 está explícito? Recurso ordinário trabalhista: prazo de 8 dias?
4. **Auditoria de citação** (segue `../_shared/citacao-e-formato.md`): todo dispositivo tem `citacao` + `source_url`? Sem isso = de memória = inválida; remover ou converter em `[CITAÇÃO PENDENTE]`.
5. **Auditoria de jurisprudência.** Há súmula/acórdão/REsp/RE/OJ na peça?
   - **Peças ordinárias:** remova e substitua por `[JURISPRUDÊNCIA, a ser inserida pelo(a) advogado(a)]`.
   - **Recurso Extraordinário:** toda jurisprudência deve estar marcada `[JURISPRUDÊNCIA NÃO VERIFICADA VIA MCP, confirmar número, data e texto exato do julgado antes do protocolo]`. Tema de Repercussão Geral sem marcador = falha grave.
6. **Marcadores remanescentes** listados no `NOTAS.md`.
7. **Depósito recursal (trabalhista).** Se empregador recorrente, mencionado e marcado `[FORA DO CORPUS]`?

## Passo 6, Saída

Siga `../_shared/saida.md` (dois arquivos, `montar_docx.py`, `colorir_marcadores.py`, aviso de itens em vermelho). `<tipo>` é o prefixo da peça diagnosticada:

`replica`, `tutela-antecipada-antecedente`, `tutela-cautelar-antecedente`, `apelacao`, `agravo-instrumento`, `embargos-declaracao`, `cumprimento-sentenca`, `impugnacao-cumprimento`, `embargos-execucao`, `excecao-pre-executividade`, `embargos-terceiro`, `recurso-ordinario-trt`, `recurso-inominado-jec`, `recurso-extraordinario`, `recurso-especial`, `agravo-are`, `agravo-aresp`, `agravo-interno`, `recurso-ordinario-constitucional`, `embargos-divergencia`, `reclamacao`, `acao-rescisoria`, `oposicao`, `suspensao-seguranca`, `suscitacao-irdr`.

No bloco de notas, inclua o prazo (legal + data de publicação + data-limite estimada como `[VERIFICAR, confirmar no sistema do tribunal, feriados forenses fora do corpus]`). Marcador extra desta skill: `[JURISPRUDÊNCIA NÃO VERIFICADA VIA MCP, ...]` (RE/reclamação/rescisória).

## O que esta skill NÃO faz

- **Não protocola.** Nunca. Ato privativo de advogado(a) habilitado(a).
- **Não calcula prazo final.** Devolve o texto legal do prazo (via MCP) e os marcos; a contagem no PJe/eSAJ, com feriados forenses, recesso (CPC art. 220) e suspensões, é do(a) advogado(a).
- **Não confirma cabimento de agravo sem consultar o art. 1.015 via MCP.** O rol é taxativo; a skill verifica o inciso antes de afirmar que cabe agravo.
- **Não insere jurisprudência sem marcador.** Em peças ordinárias é vedada e sai como `[JURISPRUDÊNCIA, a ser inserida pelo(a) advogado(a)]`. No RE, precedentes do STF podem entrar, mas sempre marcados `[JURISPRUDÊNCIA NÃO VERIFICADA VIA MCP, ...]`. Nenhum precedente entra limpo, sem marcador, em nenhuma peça.
- **Não cobre normas estaduais ou tabelamentos do tribunal.** Custas, depósito recursal, tabela de honorários periciais → `[FORA DO CORPUS]`.
- **Não decide estratégia.** "Apelar ou embargar primeiro?" é decisão profissional; a skill produz a peça escolhida.
- **Não substitui o(a) advogado(a).** Produz rascunho; assinatura, responsabilidade e estratégia são da pessoa habilitada na OAB.
