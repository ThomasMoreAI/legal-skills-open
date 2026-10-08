---
name: jurisprudencia-miner-ma-serra
title: Jurisprudencia Miner — Pesquisa e Validacao de Precedentes Brasileiros
description: 'Usar quando o usuario precisar pesquisar, validar ou analisar jurisprudencia dos tribunais brasileiros (STF, STJ, TJs, TRFs, TST). Usar para encontrar precedentes, sumulas, teses vinculantes, recursos repetitivos ou repercussao geral aplicaveis a um caso. Triggers: "jurisprudencia", "precedente", "sumula", "tese STJ", "repercussao geral", "repetitivo", "acordao", "julgado", "pesquisa jurisprudencial".'
author: ma-serra
author_url: https://github.com/ma-serra/lex-intelligentia-skills/tree/main/skills/core/jurisprudencia-miner
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: litigation
language: pt
---

# Jurisprudencia Miner — Pesquisa e Validacao de Precedentes Brasileiros

## Overview

Skill para pesquisa estruturada e validacao de jurisprudencia brasileira com protocolo anti-alucinacao rigoroso. Nao e um banco de dados de Sumulas — e uma **metodologia de pesquisa** que ensina a encontrar, validar e citar precedentes de forma segura.

## When to Use

- Fundamentar tese com jurisprudencia do STJ/STF
- Identificar divergencia jurisprudencial sobre um tema
- Rastrear evolucao de teses ao longo do tempo
- Validar citacoes de acordaos antes de usar em pecas
- Construir argumentacao jurisprudencial para sentenca ou peticao
- Pesquisar por tema, artigo de lei ou numero de Sumula

**When NOT to Use:**
- Redigir a sentenca (usar `sentenca-judicial-br`)
- Analisar pecas processuais (usar `peticao-analyzer`)
- Validar solidez de uma tese juridica (usar `tese-juridica-validator`)

---

## Protocolo Anti-Alucinacao (OBRIGATORIO)

Citacoes juridicas inventadas destroem credibilidade profissional. Esta skill adota **verificacao obrigatoria** antes de qualquer citacao:

```
REGRA DE OURO: Nunca inventar numero de processo, data de julgamento,
turma ou relator. Se nao tiver certeza, INDICAR que e necessaria
verificacao nas fontes oficiais antes de uso profissional.
```

### Niveis de Confianca

| Nivel | Quando usar | Formato de citacao |
|-------|-------------|-------------------|
| CONFIRMADO | Sumula com numero certo, tese amplamente consolidada | Citar + "[CONFIRMAR no tribunal]" |
| PROVAVEL | Tendencia jurisprudencial consistente | "Ha jurisprudencia no sentido de..." + "[VERIFICAR]" |
| INCERTO | Sem informacao segura da posicao atual | Declarar incerteza + fornecer links de busca |

### Fontes Primarias para Verificacao

| Tribunal | URL de busca |
|----------|-------------|
| STF — Jurisprudencia | https://portal.stf.jus.br/jurisprudencia/ |
| STF — Sumulas Vinculantes | https://portal.stf.jus.br/textos/verTexto.asp?servico=jurisprudenciaSumulaVinculante |
| STJ — Pesquisa | https://scon.stj.jus.br/SCON/ |
| STJ — Teses Repetitivas | https://processo.stj.jus.br/repetitivos/ |
| STJ — Sumulas | https://www.stj.jus.br/sites/portalp/Jurisprudencia/Sumulas |
| TJ-ES — ESIS | https://sistemas.tjes.jus.br/esis/ |
| TRFs — CJF | https://www.cjf.jus.br/juris/ |
| TST | https://jurisprudencia.tst.jus.br/ |

---

## Hierarquia dos Precedentes Brasileiros (art. 927, CPC)

```
[VINCULANTES]
|-- Sumulas Vinculantes do STF
|-- Decisoes em Controle Concentrado (ADI, ADC, ADPF, ADO)
|-- Acordaos em RE com Repercussao Geral
|-- Acordaos em REsp/AREsp Repetitivos
|-- IAC — Incidente de Assuncao de Competencia

[PERSUASIVOS]
|-- Sumulas do STJ e STF (nao vinculantes)
|-- Precedentes das Secoes e Cortes Especiais
|-- Jurisprudencia dos Tribunais de Justica e TRFs
|-- Enunciados do FPPC (Processualistas Civis)
```

---

## Referencia de Sumulas por Area

**ATENCAO:** As sinteses abaixo sao orientativas. SEMPRE verificar o enunciado completo no site do tribunal antes de usar em pecas ou decisoes. Sumulas podem ser revogadas, superadas ou ter redacao diferente da sintese aqui apresentada.

### Direito Bancario

| Referencia | Sintese orientativa | Status |
|-----------|--------------------|---------|
| Sumula 297/STJ | CDC aplica-se as instituicoes financeiras | [VERIFICAR enunciado completo] |
| Sumula 382/STJ | Juros remuneratorios acima de 12% a.a. nao indicam, por si so, abusividade | [VERIFICAR enunciado completo] |
| Sumula 539/STJ | Capitalizacao sub-anual de juros permitida no SFN pos-31/03/2000 (MP 2.170-36) | [VERIFICAR enunciado completo] |
| Sumula 541/STJ | Taxa anual superior a 12x taxa mensal = capitalizacao efetiva comprovada | [VERIFICAR enunciado completo] |
| Sumula 566/STJ | Tarifa de cadastro em contratos bancarios pos-Resolucao CMN 3.518/2007 | [VERIFICAR enunciado completo] |

### Direito do Consumidor

| Referencia | Sintese orientativa | Status |
|-----------|--------------------|---------|
| Sumula 297/STJ | CDC aplica-se as instituicoes financeiras | [VERIFICAR enunciado completo] |
| Sumula 469/STJ | CDC aplica-se aos contratos de planos de saude | [VERIFICAR enunciado completo] |
| Sumula 563/STJ | CDC e entidades abertas de previdencia complementar | [VERIFICAR enunciado completo] |

### Responsabilidade Civil

| Referencia | Sintese orientativa | Status |
|-----------|--------------------|---------|
| Sumula 37/STJ | Cumulacao de danos morais e materiais | [VERIFICAR enunciado completo] |
| Sumula 227/STJ | Pessoa juridica pode sofrer dano moral | [VERIFICAR enunciado completo] |
| Sumula 403/STJ | Uso nao autorizado de imagem e dano moral | [VERIFICAR enunciado completo] |

### Processo Civil

| Referencia | Sintese orientativa | Status |
|-----------|--------------------|---------|
| Art. 927, CPC | Hierarquia de precedentes vinculantes | Lei — nao precisa verificar |
| Art. 489, §1, CPC | Requisitos de fundamentacao analitica | Lei — nao precisa verificar |
| Art. 926, CPC | Dever de uniformizacao e coerencia | Lei — nao precisa verificar |

### Direito Imobiliario

| Referencia | Sintese orientativa | Status |
|-----------|---------------------|---------|
| Sumula 76/STJ | Compromisso de compra e venda sem registro nao dispensa interpelacao para constituicao em mora | [VERIFICAR enunciado completo] |
| Sumula 84/STJ | Embargos de terceiro admissiveis com compromisso de compra e venda sem registro | [VERIFICAR enunciado completo] |
| Sumula 239/STJ | Adjudicacao compulsoria nao exige registro do compromisso de compra e venda | [VERIFICAR enunciado completo] |
| Sumula 308/STJ | Hipoteca entre construtora e agente financeiro nao vincula adquirentes das unidades | [VERIFICAR enunciado completo] |
| Sumula 543/STJ | Na resolucao de promessa de compra e venda sujeita ao CDC, restituicao imediata dos valores pagos | [VERIFICAR enunciado completo] |
| Sumula 602/STJ | CDC aplicavel a empreendimentos de cooperativas habitacionais | [VERIFICAR enunciado completo] |

### Condominio

| Referencia | Sintese orientativa | Status |
|-----------|---------------------|---------|
| Sumula 260/STJ | Convencao de condominio aprovada mas nao registrada tem eficacia entre condominos | [VERIFICAR enunciado completo] |
| Sumula 449/STJ | Vaga de garagem com matricula propria nao e bem de familia | [VERIFICAR enunciado completo] |
| Sumula 478/STJ | Credito condominial tem preferencia sobre o credito hipotecario | [VERIFICAR enunciado completo] |

### Locacao

| Referencia | Sintese orientativa | Status |
|-----------|---------------------|---------|
| Sumula 214/STJ | Fiador na locacao nao responde por obrigacoes decorrentes de aditamento ao qual nao anuiu | [VERIFICAR enunciado completo] |
| Sumula 268/STJ | Fiador que nao integrou a acao de despejo nao responde pela execucao do julgado | [VERIFICAR enunciado completo] |
| Sumula 332/STJ | Fianca prestada sem autorizacao de um dos conjuges: ineficacia total (nao apenas da meacao) | [VERIFICAR enunciado completo] |
| Sumula 335/STJ | Valida a clausula de renuncia a indenizacao por benfeitorias e ao direito de retencao | [VERIFICAR enunciado completo] |
| Sumula 549/STJ | Valida a penhora de bem de familia do fiador em contrato de locacao | [VERIFICAR enunciado completo] |

### Usucapiao

| Referencia | Sintese orientativa | Status |
|-----------|---------------------|---------|
| Sumula 11/STJ | Presenca da Uniao como interessada nao afasta competencia do foro de situacao do imovel para usucapiao | [VERIFICAR enunciado completo] |

**Nota:** Foram removidas referencias com descricao incorreta da versao anterior desta skill. Ao pesquisar Sumulas em areas como Familia, Posse, Execucao — sempre consultar diretamente no site do STJ.

---

## Temas Repetitivos do STJ (art. 1.036, CPC)

**IMPORTANCIA:** Temas Repetitivos vinculam todos os tribunais e juizos inferiores (art. 927, III, CPC). Sao hoje os precedentes de MAIOR impacto pratico no Judiciario brasileiro.

**ATENCAO:** Os numeros e sinteses abaixo sao orientativos. SEMPRE verificar a tese firmada completa em https://processo.stj.jus.br/repetitivos/ antes de usar em pecas ou decisoes.

### Direito Bancario

| Tema | Sintese orientativa | Status |
|------|---------------------|--------|
| Temas 618/619 | Tarifas bancarias: cadastro (licita pos-30/4/2008), avaliacao do bem (licita se efetivamente prestada) | [VERIFICAR tese completa] |
| Tema 24 | Capitalizacao mensal de juros: admitida quando pactuada | [VERIFICAR tese completa] |
| Tema 27 | Comissao de permanencia: nao pode ser cumulada com outros encargos | [VERIFICAR tese completa] |
| Tema 972 | Venda casada de seguro em financiamento: ilicita se consumidor nao pode escolher seguradora (REsp 1.639.259/SP, Min. Sanseverino, 12/12/2018) | [VERIFICAR tese completa] |
| Tema 1.368 | **SELIC como indice UNICO para dividas civis** — substitui 1%+IPCA-E. Vedada cumulacao SELIC+IPCA-E (REsp 2.199.164/PR e 2.070.882/RS, Min. Villas Boas Cueva, Corte Especial, 15/10/2025) | [VERIFICAR tese completa] |

### Direito do Consumidor

| Tema | Sintese orientativa | Status |
|------|---------------------|--------|
| Tema 622 | Negativacao indevida e dano moral: parametros de fixacao | [VERIFICAR tese completa] |
| Tema 952 | Plano de saude: rol da ANS como referencia | [VERIFICAR tese completa] |

### Responsabilidade Civil

| Tema | Sintese orientativa | Status |
|------|---------------------|--------|
| Tema 983 | Termo inicial dos juros moratorios em indenizacao por dano moral | [VERIFICAR tese completa] |
| Tema 1.368 | SELIC unica para dividas civis — dano moral: SELIC desde evento danoso (convergencia S.54+S.362). Endosso STF: RE 1.558.191/SP | [VERIFICAR tese completa] |

### Processo Civil

| Tema | Sintese orientativa | Status |
|------|---------------------|--------|
| Tema 1.076 | Honorarios advocaticios: limites e fases (art. 85, CPC/2015) | [VERIFICAR tese completa] |

### Direito Imobiliario

| Tema | Sintese orientativa | Status |
|------|---------------------|--------|
| Tema 938 | Comissao de corretagem e taxa SATI em compra de imovel na planta — prescricao trienal, transferencia valida se consumidor informado do preco total (REsp 1.551.956/SP) | [VERIFICAR tese completa] |
| Tema 970 | Clausula penal moratoria por atraso na entrega de imovel tem natureza propria e nao compensa lucros cessantes (REsp 1.635.428/SC) | [VERIFICAR tese completa] |
| Tema 971 | Inversao da clausula penal moratoria em desfavor da construtora/incorporadora inadimplente (REsp 1.614.721/DF) | [VERIFICAR tese completa] |
| Tema 996 | Atraso na entrega de imovel: tolerancia de 180 dias valida, alugueis mensais como indenizacao, vedacao de juros de obra apos prazo (REsp 1.631.485/DF) | [VERIFICAR tese completa] |
| Tema 1.002 | Juros de mora na resolucao de compra e venda por iniciativa do comprador — incidencia a partir do transito em julgado (REsp 1.740.911/DF) | [VERIFICAR tese completa] |
| Tema 1.095 | Alienacao fiduciaria de imovel com registro: Lei 9.514/97 prevalece sobre CDC para procedimento de execucao extrajudicial (REsp 1.891.498/SP) | [VERIFICAR tese completa] |
| Tema 1.113 | Base de calculo do ITBI — valor de mercado na data do fato gerador, nao vinculado ao valor venal do IPTU (REsp 1.937.821/SP) | [VERIFICAR tese completa] |
| Tema 1.288 | Purgacao da mora apos consolidacao da propriedade em alienacao fiduciaria — limites pre e pos Lei 13.465/2017 | [VERIFICAR tese completa] |

### Condominio

| Tema | Sintese orientativa | Status |
|------|---------------------|--------|
| Tema 882 | Taxas de associacao de moradores/condominio de fato: nao vinculam proprietarios nao associados (RE 695.911/SP — STF com RG) | [VERIFICAR tese completa] |
| Tema 886 | Legitimidade para cobranca de cotas condominiais: posse com ciencia do condominio basta (EM REVISAO — acompanhar) | [VERIFICAR tese completa] |
| Tema 949 | Prescricao de cotas condominiais: 5 anos, art. 206, §5, I, CC — prestacao periodica (REsp 1.483.930/DF) | [VERIFICAR tese completa] |

### Locacao

| Tema | Sintese orientativa | Status |
|------|---------------------|--------|
| Tema 1091 | Penhorabilidade do bem de familia do fiador em contrato de locacao — abrange locacao residencial e comercial (RE 1.307.334/SP — STF com RG) | [VERIFICAR tese completa] |

### Usucapiao

| Tema | Sintese orientativa | Status |
|------|---------------------|--------|
| Tema 985 | Usucapiao extraordinaria: area inferior ao modulo urbano minimo nao impede reconhecimento (REsp 1.667.842/SC) | [VERIFICAR tese completa] |

### Como Pesquisar Temas Repetitivos

1. Acesse https://processo.stj.jus.br/repetitivos/
2. Pesquise por numero do tema OU por palavra-chave na tese
3. Verifique o status: JULGADO (tese ja fixada) ou AFETADO (pendente de julgamento)
4. Leia a tese firmada COMPLETA — nao confie em resumos
5. Verifique se houve revisao de tese (art. 927, §4, CPC)

**Dica de busca avancada:** No SCON do STJ, filtrar por "Recurso Repetitivo" no campo "Tipo de Julgamento" para encontrar apenas acordaos em sede de repetitivo.

---

## Estrategias de Pesquisa por Situacao

### Situacao 1: "Preciso de jurisprudencia para fundamentar [tese X]"

**Processo:**
1. Identificar a area do direito e o ponto juridico especifico
2. Mapear palavras-chave: nome da tese, artigo de lei, parte da ementa
3. Sugerir busca nas fontes primarias com os termos corretos
4. Apresentar Sumulas e temas repetitivos conhecidos (com nivel de confianca)
5. Indicar o caminho de verificacao para uso profissional

**Template de output:**
```
PESQUISA JURISPRUDENCIAL — [Tema]

[PALAVRAS-CHAVE SUGERIDAS]
- "[termo 1]" AND "[termo 2]"
- "[artigo X]" AND "[principio]"

[REFERENCIAS CONHECIDAS] (verificar nas fontes antes de usar)
- Sumula XXX/STJ: [sintese] — [VERIFICAR enunciado completo]
- Tema YYY/STJ (Repetitivo): [sintese da tese] — [VERIFICAR]
- RG Tema ZZZ/STF: [sintese] — [VERIFICAR]

[LINKS PARA VERIFICACAO]
- STJ: https://scon.stj.jus.br/SCON/
- STF: https://portal.stf.jus.br/jurisprudencia/

IMPORTANTE: Confirme numero, data e relator antes de usar em
pecas processuais ou decisoes.
```

### Situacao 2: "Preciso identificar divergencia sobre [questao]"

**Processo:**
1. Apresentar as correntes doutrinarias/jurisprudenciais existentes
2. Mapear os tribunais que adotam cada posicao
3. Identificar se STJ/STF ja pacificou (Sumula, repetitivo, RG) ou se ha IRDR pendente
4. Recomendar posicao mais segura para o caso concreto

**Template de output — Divergencia Jurisprudencial:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[DIVERGENCIA] — [Tema da divergencia]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[STATUS DA QUESTAO]
( ) PACIFICADA — Sumula/Repetitivo/RG fixou tese
( ) DIVERGENTE — Correntes coexistem sem pacificacao
( ) EM AFETACAO — Tema afetado para julgamento (pendente)

[CORRENTE 1 — descricao da tese]
- Fundamento: [norma/principio que sustenta]
- Adotada por: [tribunais/turmas/secoes]
- Referencia: [Sumula, Tema, acordao-lider] — [VERIFICAR]

[CORRENTE 2 — descricao da tese]
- Fundamento: [norma/principio que sustenta]
- Adotada por: [tribunais/turmas/secoes]
- Referencia: [acordao-lider, se houver] — [VERIFICAR]

[CORRENTE 3 — se houver]
- [mesma estrutura]

[INCIDENTE PENDENTE]
- IRDR: [numero / tribunal / status] — [VERIFICAR]
- IAC: [numero / tribunal / status] — [VERIFICAR]
- Tema Repetitivo afetado: [numero / status] — [VERIFICAR]
- Repercussao Geral: [Tema / status] — [VERIFICAR]
(Se nenhum: "Nao ha incidente de uniformizacao pendente identificado")

[TENDENCIA ATUAL]
[Qual corrente vem prevalecendo nos julgados mais recentes?
Houve virada recente? Qual a composicao atual do orgao
julgador competente?]

[RECOMENDACAO PARA O CASO]
- Posicao MAIS SEGURA: [Corrente X] — porque [justificativa]
- Risco de adotar Corrente Y: [qual o risco pratico —
  reforma em grau recursal, embargos de divergencia, etc.]

[COMO PESQUISAR A POSICAO ATUALIZADA]
- [link de busca especifico para o tema]
- Termos sugeridos: "[palavras-chave]"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Quando marcar [DIVERGENCIA]:**
- Quando duas ou mais Turmas do STJ divergem sobre o mesmo ponto
- Quando TJs de estados diferentes adotam posicoes opostas
- Quando ha mudanca recente de entendimento sem Sumula/Repetitivo
- Quando a parte invoca precedente que contraria a posicao majoritaria

**IMPORTANTE:** A existencia de divergencia NAO dispensa o juiz de decidir. O marcador [DIVERGENCIA] sinaliza que o tema exige fundamentacao reforçada (art. 489, §1, VI, CPC) e que a decisao pode ser objeto de recurso qualificado (embargos de divergencia, IRDR).

### Situacao 3: "Qual a evolucao jurisprudencial sobre [tema]?"

**Processo:**
1. Marcos temporais relevantes (pre e pos-CPC/2015, pre e pos-CDC, etc.)
2. Reviravolta jurisprudencial — indicar quando houve overruling
3. Estado atual consolidado
4. Tendencias identificadas nos julgamentos recentes

---

## Parametros Indenizatorios — Tabela de Referencia por Tipo de Dano

**ATENCAO:** Os valores abaixo sao faixas ORIENTATIVAS baseadas em tendencias jurisprudenciais. NAO sao vinculantes. SEMPRE verificar os parametros atualizados do tribunal local (TJ do estado) e a jurisprudencia recente do STJ antes de usar como referencia. Os valores devem ser ajustados conforme as circunstancias do caso concreto (art. 944, CC).

### Dano Moral — Faixas por Tipo de Evento

| Tipo de dano | Faixa orientativa | Fatores de ajuste | Status |
|-------------|-------------------|-------------------|--------|
| **Negativacao indevida** (sem preexistente) | R$ 5.000 a R$ 20.000 | Duracao, reincidencia do ofensor, repercussao | [VERIFICAR TJ local + Tema 622/STJ] |
| **Negativacao indevida** (com preexistente) | Indenizacao AFASTADA | Sumula 385/STJ — ressalvado cancelamento | [VERIFICAR Sumula 385/STJ] |
| **Falha em servico essencial** (agua, energia, telecom) | R$ 3.000 a R$ 15.000 | Duracao da falha, dano concreto, vulnerabilidade | [VERIFICAR TJ local] |
| **Plano de saude — negativa de cobertura** | R$ 10.000 a R$ 30.000 | Urgencia do procedimento, risco de vida | [VERIFICAR TJ local + Tema 952/STJ] |
| **Atraso/extravio de bagagem** (aereo) | R$ 5.000 a R$ 15.000 | Duração viagem, itens perdidos, Convenção Montreal | [VERIFICAR STJ + ANAC] |
| **Acidente de transito — lesao leve** | R$ 5.000 a R$ 20.000 | Gravidade da lesao, tempo de recuperacao | [VERIFICAR TJ local] |
| **Acidente de transito — lesao grave/invalidez** | R$ 30.000 a R$ 200.000 | Grau de invalidez, idade, profissao | [VERIFICAR TJ local + STJ] |
| **Morte de familiar** (pai/mae/filho) | R$ 100.000 a R$ 500.000 | Dependencia economica, idade, circunstancias | [VERIFICAR STJ] |
| **Erro medico — dano estetico** | R$ 20.000 a R$ 100.000 | Visibilidade, reversibilidade, parte do corpo | [VERIFICAR TJ local] |
| **Protesto indevido de titulo** | R$ 5.000 a R$ 15.000 | Valor do titulo, repercussao, reincidencia | [VERIFICAR TJ local] |
| **Cobranca vexatoria** (art. 42, CDC) | R$ 3.000 a R$ 10.000 | Local, publicidade, frequencia | [VERIFICAR TJ local] |

### Dano Material — Criterios de Calculo

| Tipo | Criterio | Fundamento |
|------|----------|------------|
| **Danos emergentes** | Valor efetivamente desembolsado | Art. 402, CC — comprovacao documental |
| **Lucros cessantes** | Renda comprovada x periodo de privacao | Art. 402, CC — media mensal comprovada |
| **Pensionamento por morte** | 2/3 da renda do falecido ate 65 anos (ou expectativa de vida) | Jurisprudencia STJ — deduzida parcela pessoal (1/3) |
| **Pensionamento por invalidez** | Proporcional ao grau de reducao da capacidade | Laudo pericial + tabela DPVAT/SUSEP como referencia |

### Criterios de Fixacao (art. 944, CC)

Ao fixar o quantum, fundamentar com base em:
1. **Gravidade da conduta** do ofensor (dolo, culpa grave, culpa leve)
2. **Extensao do dano** sofrido pela vitima
3. **Condicao economica** das partes (vedado enriquecimento sem causa)
4. **Carater pedagogico-preventivo** (especialmente contra reincidentes)
5. **Proporcionalidade e razoabilidade** (parametro constitucional)

**Nota:** O paragrafo unico do art. 944, CC permite ao juiz REDUZIR equitativamente a indenizacao quando houver excessiva desproporcao entre a gravidade da culpa e o dano.

---

## Formato de Ementa Estruturada

Para apresentar jurisprudencia, sempre usar:

```
[AREA DO DIREITO]. [TEMA ESPECIFICO]. [TESE CENTRAL].

[Desenvolvimento: fatos -> questao -> aplicacao da norma -> conclusao]

[Dispositivo legal aplicado]

[Tribunal], [Orgao julgador], [Tipo de recurso] n. [numero],
Rel. Min./Des. [nome], j. [data], [publicacao].
```

---

## Pesquisa Tematica por Artigo de Lei

Quando o usuario informar um artigo, identificar:
- Controversias interpretativas conhecidas
- Sumulas relacionadas (com [VERIFICAR])
- Teses em repercussao geral / recursos repetitivos
- Enunciados do FPPC aplicaveis
- Doutrina majoritaria

---

## Common Mistakes

| Erro | Como evitar |
|------|------------|
| Citar Sumula com descricao inventada pelo LLM | SEMPRE verificar enunciado completo no site do tribunal — LLMs frequentemente atribuem descricoes erradas a numeros corretos |
| Confiar em numero de REsp gerado por IA | Nunca citar numero de processo sem verificar na fonte — usar nivel PROVAVEL ou INCERTO |
| Ignorar superacao de precedente | Verificar se a Sumula/tese ainda e vigente — pode ter sido cancelada ou superada |
| Citar ementa sem ler o acordao | A ementa pode nao refletir a tese completa — verificar ratio decidendi |
| Nao fazer distinguishing | Ao aplicar precedente, demonstrar que os fatos do caso se ajustam (art. 489, §1, V, CPC) |
| Tratar Sumula persuasiva como vinculante | Apenas Sumulas Vinculantes do STF vinculam — Sumulas do STJ sao persuasivas (art. 927, IV, CPC) |
| Banco de Sumulas desatualizado | Sumulas podem ser revogadas a qualquer tempo — sempre verificar data da ultima atualizacao |

---

## Integracao com Outras Skills

| De | Para | Uso |
|----|------|-----|
| `peticao-analyzer` | **jurisprudencia-miner** | Teses identificadas na peca -> pesquisar precedentes |
| **jurisprudencia-miner** | `sentenca-judicial-br` | Precedentes encontrados -> fundamentar decisao |
| **jurisprudencia-miner** | `tese-juridica-validator` | Tese + precedentes -> validar solidez |
| `lex-rag-builder` | **jurisprudencia-miner** | Base vetorial de ementas -> busca semantica |

---

## Checklist de Qualidade da Citacao Juridica

Antes de usar qualquer citacao em peca ou decisao:

- [ ] Numero do processo verificado na fonte oficial
- [ ] Data de julgamento confirmada
- [ ] Relator correto
- [ ] Turma/Secao/Pleno correto
- [ ] Tese fixada fiel ao acordao (nao apenas a ementa)
- [ ] Vigencia confirmada (nao houve superacao do precedente)
- [ ] Aplicabilidade ao caso concreto justificada (distinguishing se necessario)
- [ ] Nivel de confianca (CONFIRMADO/PROVAVEL/INCERTO) declarado

---

## Workflow de Uso

1. **Receber** a questao juridica ou tese a fundamentar
2. **Classificar** a area do direito e o tipo de pesquisa
3. **Consultar** Sumulas e temas repetitivos conhecidos (com nivel de confianca)
4. **Sugerir** termos de busca para fontes primarias
5. **Formatar** o output com ementa estruturada
6. **Aplicar** checklist de qualidade em cada citacao
7. **Encaminhar** para `sentenca-judicial-br` ou `tese-juridica-validator`
