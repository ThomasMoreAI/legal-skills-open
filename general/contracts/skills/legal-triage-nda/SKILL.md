---
name: legal-triage-nda
title: legal-triage-nda — Pré-triagem de NDA
description: Triagem rápida de um NDA recebido e classificação como VERDE (aprovação padrão), AMARELO (revisão de assessoria) ou VERMELHO (revisão jurídica completa). Use quando um novo NDA chegar de vendas ou desenvolvimento de negócios, ao verificar cláusulas de não-solicitação, não-concorrência ou carveouts ausentes embutidos, ou ao decidir se um NDA pode ser assinado sob delegação padrão.
author: evolution-foundation
author_url: https://github.com/evolution-foundation/evo-nexus/tree/main/.claude/skills/legal-triage-nda
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: pt
---

# legal-triage-nda — Pré-triagem de NDA

> **Este documento não constitui aconselhamento jurídico — consulte o assessor jurídico habilitado antes de tomar decisões com base nesta análise.**
> Contatos legais: **Thaís Menezes** (contratos Brius/Etus) | **Vitor Lacerda** (jurídico Etus)

Triagem rápida de NDAs recebidos contra critérios de triagem padrão. Classificar o NDA para roteamento: aprovação padrão, revisão de assessoria ou revisão jurídica completa.

## Acionamento

User executa `/legal-triage-nda` ou solicita triar, verificar ou classificar um NDA.

## Fluxo de Trabalho

### Passo 1: Aceitar o NDA

Aceitar o NDA em qualquer formato:
- **Upload de arquivo**: PDF, DOCX ou outro formato de documento
- **Arquivo local / Notion**: Link para o NDA em armazenamento local ou página Notion
- **Texto colado**: Texto do NDA colado diretamente

Se nenhum NDA for fornecido, solicitar ao usuário que o forneça.

### Passo 2: Carregar Playbook de NDA

Buscar critérios de triagem de NDA nas configurações locais (ex: `legal.local.md`).

O playbook de NDA deve definir:
- Requisitos de mútuo vs. unilateral
- Prazos aceitáveis
- Carveouts obrigatórios
- Disposições proibidas
- Requisitos específicos da organização

**Se nenhum playbook de NDA estiver configurado:**
- Prosseguir com padrões razoáveis de mercado como defaults
- Registrar claramente que os defaults estão sendo usados
- Defaults aplicados:
  - Obrigações mútuas exigidas (a menos que a organização seja apenas a parte divulgadora)
  - Prazo: 2-3 anos padrão, até 5 anos para segredos de negócio (conforme Código Civil Brasileiro)
  - Carveouts padrão obrigatórios: desenvolvido independentemente, disponível publicamente, recebido legitimamente de terceiro, exigido por lei
  - Sem disposições de não-solicitação ou não-concorrência
  - Sem cláusula de residuals (ou com escopo estreito se presente)
  - Lei aplicável brasileira — foro preferencial em São Paulo ou Belo Horizonte

### Passo 3: Triagem Rápida

Avaliar o NDA contra cada critério de triagem sistematicamente.

#### 1. Estrutura do Acordo
- [ ] **Tipo identificado**: NDA Mútuo, Unilateral (parte divulgadora) ou Unilateral (parte receptora)
- [ ] **Adequado para o contexto**: O tipo de NDA é adequado para a relação de negócios?
- [ ] **Acordo autônomo**: Confirmar que o NDA é um acordo autônomo, não uma seção de confidencialidade embutida em um acordo comercial maior

#### 2. Definição de Informação Confidencial
- [ ] **Escopo razoável**: Não muito amplo (evitar "toda e qualquer informação independentemente de marcação")
- [ ] **Requisitos de marcação**: Se marcação for exigida, é praticável? (marcação escrita em 30 dias após divulgação oral é padrão)
- [ ] **Exclusões presentes**: Exclusões padrão definidas (ver Carveouts Padrão abaixo)
- [ ] **Sem inclusões problemáticas**: Não define informações publicamente disponíveis ou materiais desenvolvidos independentemente como confidenciais

#### 3. Obrigações da Parte Receptora
- [ ] **Padrão de cuidado**: Cuidado razoável ou pelo menos o mesmo cuidado aplicado à própria informação confidencial
- [ ] **Restrição de uso**: Limitado à finalidade declarada
- [ ] **Restrição de divulgação**: Limitado àqueles com necessidade de saber que estão vinculados por obrigações similares
- [ ] **Sem obrigações onerosas**: Sem requisitos impraticáveis (ex: encriptar todas as comunicações, manter logs físicos)

#### 4. Carveouts Padrão
Todos os seguintes carveouts devem estar presentes:
- [ ] **Conhecimento público**: Informação que é ou se torna publicamente disponível sem culpa da parte receptora
- [ ] **Posse prévia**: Informação já conhecida pela parte receptora antes da divulgação
- [ ] **Desenvolvimento independente**: Informação desenvolvida independentemente sem uso ou referência à informação confidencial
- [ ] **Recebimento de terceiros**: Informação legitimamente recebida de terceiro sem restrição
- [ ] **Compulsão legal**: Direito de divulgar quando exigido por lei, regulamentação ou processo legal (com aviso à parte divulgadora quando legalmente permitido — ex: intimação judicial, solicitação do MP, ANPD, BCB, etc.)

#### 5. Divulgações Permitidas
- [ ] **Funcionários**: Pode compartilhar com funcionários que precisam saber
- [ ] **Prestadores/assessores**: Pode compartilhar com prestadores, assessores e consultores profissionais sob obrigações similares de confidencialidade
- [ ] **Afiliadas**: Pode compartilhar com afiliadas (se necessário para a finalidade de negócio)
- [ ] **Legal/regulatório**: Pode divulgar conforme exigido por lei ou regulamentação

#### 6. Prazo e Duração
- [ ] **Prazo do acordo**: Período razoável para a relação de negócio (1-3 anos é padrão no Brasil)
- [ ] **Sobrevivência da confidencialidade**: Obrigações sobrevivem por período razoável após rescisão (2-5 anos é padrão; segredos de negócio podem ser mais longos — conforme art. 195 Lei de Propriedade Industrial)
- [ ] **Não perpétuo**: Evitar obrigações de confidencialidade indefinidas ou perpétuas (exceção: segredos de negócio, que podem justificar proteção mais longa)

#### 7. Devolução e Destruição
- [ ] **Obrigação acionada**: Na rescisão ou mediante solicitação
- [ ] **Escopo razoável**: Devolver ou destruir informação confidencial e todas as cópias
- [ ] **Exceção de retenção**: Permite retenção de cópias exigidas por lei, regulamentação ou políticas internas de conformidade/backup
- [ ] **Certificação**: Certificação de destruição é razoável; declaração notarial juramentada é onerosa

#### 8. Remédios
- [ ] **Tutela inibitória**: Reconhecimento de que a violação pode causar dano irreparável e que medida judicial urgente (tutela antecipada) pode ser apropriada (art. 300 CPC)
- [ ] **Sem danos pré-determinados excessivos**: Evitar cláusulas de multa punitiva desproporcional em NDAs (art. 412 CC)
- [ ] **Não unilateral**: Disposições de remédios se aplicam igualmente a ambas as partes (em NDAs mútuos)

#### 9. Disposições Problemáticas a Sinalizar
- [ ] **Sem não-solicitação**: NDA não deve conter disposições de não-solicitação de funcionários
- [ ] **Sem não-concorrência**: NDA não deve conter disposições de não-concorrência (atenção: não-concorrência de empregado exige requisitos específicos da CLT; em contratos comerciais, precisa ser razoável em escopo e duração)
- [ ] **Sem exclusividade**: NDA não deve impedir qualquer das partes de firmar discussões similares com outros
- [ ] **Sem standstill**: NDA não deve conter standstill ou disposições restritivas similares (exceto em contexto de M&A)
- [ ] **Sem cláusula de residuals** (ou com escopo estreito): Se presente, deve ser limitado a ideias gerais, conceitos, know-how ou técnicas retidas na memória não auxiliada de indivíduos e não deve se aplicar a segredos de negócio ou informações patenteáveis
- [ ] **Sem cessão ou licença de PI**: NDA não deve conceder nenhum direito de propriedade intelectual
- [ ] **Sem direitos de auditoria**: Incomum em NDAs padrão

#### 10. Lei Aplicável e Jurisdição
- [ ] **Jurisdição razoável**: Preferencialmente lei brasileira e foro no Brasil
- [ ] **Consistente**: Lei aplicável e jurisdição devem estar na mesma ou em jurisdições relacionadas
- [ ] **Sem arbitragem mandatória** (em NDAs padrão): Litígio é geralmente preferido para disputas de NDA de baixo valor; arbitragem pode ser adequada para NDAs corporativos de alto valor

### Passo 4: Classificar

Com base nos resultados da triagem, atribuir uma classificação:

#### VERDE — Aprovação Padrão

**Todos** os seguintes devem ser verdadeiros:
- NDA é mútuo (ou unilateral na direção adequada)
- Todos os carveouts padrão estão presentes
- Prazo está dentro do alcance padrão (1-3 anos, sobrevivência 2-5 anos)
- Sem não-solicitação, não-concorrência ou exclusividade
- Sem cláusula de residuals, ou cláusula de residuals com escopo estreito
- Lei aplicável brasileira ou outra jurisdição razoável e conhecida
- Remédios padrão (sem multa punitiva excessiva)
- Divulgações permitidas incluem funcionários, prestadores e assessores
- Disposições de devolução/destruição incluem exceção de retenção legal/compliance
- Definição de informação confidencial com escopo razoável

**Roteamento**: Aprovar via delegação padrão de autoridade. Não requer revisão de assessoria.
- **Ação**: Prosseguir para assinatura com delegação padrão de autoridade

#### AMARELO — Revisão de Assessoria Necessária

**Um ou mais** dos seguintes estão presentes, mas o NDA não é fundamentalmente problemático:
- Definição de informação confidencial é mais ampla do que o preferido mas não é irrazoável
- Prazo é mais longo do que o padrão mas dentro da faixa de mercado (ex: 5 anos para prazo do acordo, 7 anos para sobrevivência)
- Falta um carveout padrão que poderia ser adicionado sem dificuldade
- Cláusula de residuals presente mas com escopo estreito à memória não auxiliada
- Lei aplicável em jurisdição aceitável mas não preferida (ex: lei estrangeira com reciprocidade)
- Assimetria menor em NDA mútuo (ex: uma parte tem divulgações permitidas ligeiramente mais amplas)
- Requisitos de marcação presentes mas praticáveis
- Devolução/destruição sem exceção explícita de retenção (provavelmente implícita mas deve ser adicionada)
- Disposições incomuns mas não prejudiciais (ex: obrigação de notificar potencial violação)

**Roteamento**: Sinalizar questões específicas para Thaís Menezes revisar. Pode ser resolvido provavelmente com redlines menores em uma única rodada de revisão.
- **Ação**: Thaís pode provavelmente resolver em uma única rodada de revisão

#### VERMELHO — Questões Significativas

**Um ou mais** dos seguintes estão presentes:
- **Unilateral quando mútuo é necessário** (ou direção errada para a relação)
- **Carveouts críticos ausentes** (especialmente desenvolvimento independente ou compulsão legal)
- **Não-solicitação ou não-concorrência** embutidos no NDA
- **Exclusividade ou standstill** sem contexto adequado de negócios
- **Prazo irrazoável** (10+ anos, ou perpétuo sem justificativa de segredo de negócio)
- **Definição excessivamente ampla** que poderia capturar informações públicas ou materiais desenvolvidos independentemente
- **Cláusula de residuals ampla** que efetivamente cria uma licença para usar a informação confidencial
- **Cessão ou licença de PI** escondida no NDA
- **Multa punitiva excessiva** desproporcional ao dano esperado
- **Direitos de auditoria** sem escopo razoável ou requisitos de aviso prévio
- **Jurisdição estrangeira altamente desfavorável** com arbitragem mandatória onerosa
- **O documento não é realmente um NDA** (contém termos comerciais substantivos, exclusividade ou outras obrigações além da confidencialidade)

**Roteamento**: Revisão jurídica completa necessária. Não assinar. Requer negociação, contraproposta com o formulário padrão de NDA da organização, ou rejeição. Encaminhar para Thaís Menezes ou Vitor Lacerda.
- **Ação**: Não assinar; requer negociação ou contraproposta

### Passo 5: Gerar Relatório de Triagem

```
## Relatório de Triagem de NDA

**Classificação**: [VERDE / AMARELO / VERMELHO]
**Partes**: [nomes das partes]
**Tipo**: [Mútuo / Unilateral (divulgadora) / Unilateral (receptora)]
**Prazo**: [duração]
**Lei Aplicável**: [jurisdição]
**Base da Revisão**: [Playbook / Padrões Default]

## Resultados da Triagem

| Critério | Status | Observações |
|----------|--------|-------------|
| Obrigações Mútuas | [PASSOU/ALERTA/FALHOU] | [detalhes] |
| Escopo da Definição | [PASSOU/ALERTA/FALHOU] | [detalhes] |
| Prazo | [PASSOU/ALERTA/FALHOU] | [detalhes] |
| Carveouts Padrão | [PASSOU/ALERTA/FALHOU] | [detalhes] |
| [etc.] | | |

## Questões Encontradas

### [Questão 1 — AMARELO/VERMELHO]
**O que é**: [descrição]
**Risco**: [o que pode dar errado]
**Correção Sugerida**: [linguagem específica ou abordagem]

[Repetir para cada questão]

## Recomendação

[Próximo passo específico: aprovar, enviar para revisão com notas específicas, ou rejeitar/contraporpor]

## Próximos Passos

1. [Item de ação 1]
2. [Item de ação 2]
```

### Passo 6: Sugestão de Roteamento

| Classificação | Ação Recomendada | Prazo Típico |
|---|---|---|
| VERDE | Aprovar e encaminhar para assinatura per delegação de autoridade | Mesmo dia |
| AMARELO | Enviar para Thaís Menezes com questões específicas sinalizadas | 1-2 dias úteis |
| VERMELHO | Engajar Thaís Menezes ou Vitor Lacerda para revisão completa; preparar contraproposta ou formulário padrão | 3-5 dias úteis |

## Questões Comuns de NDA e Posições Padrão

### Questão: Definição Excessivamente Ampla de Informação Confidencial
**Posição padrão**: Informação confidencial deve ser limitada a informação não-pública divulgada em conexão com a finalidade declarada, com exclusões claras.
**Abordagem de redline**: Restringir a definição à informação marcada ou identificada como confidencial, ou que uma pessoa razoável entenderia ser confidencial dada a natureza e as circunstâncias.

### Questão: Carveout de Desenvolvimento Independente Ausente
**Posição padrão**: Deve incluir um carveout para informação desenvolvida independentemente sem referência ou uso da informação confidencial da parte divulgadora.
**Risco se ausente**: Poderia criar alegações de que produtos ou funcionalidades desenvolvidos internamente derivaram da informação confidencial da contraparte.
**Abordagem de redline**: Adicionar carveout padrão de desenvolvimento independente.

### Questão: Não-Solicitação de Funcionários
**Posição padrão**: Disposições de não-solicitação não pertencem a NDAs. São adequadas em contratos de trabalho, acordos de M&A ou acordos comerciais específicos.
**Abordagem de redline**: Excluir a disposição inteiramente. Se a contraparte insistir, limitar à solicitação direcionada (não recrutamento geral) e estabelecer prazo curto (12 meses).

### Questão: Cláusula de Residuals Ampla
**Posição padrão**: Resistir a cláusulas de residuals. Se exigido, limitar a: (a) ideias gerais, conceitos, know-how ou técnicas retidas na memória não auxiliada de indivíduos com acesso autorizado; (b) excluir explicitamente segredos de negócio e informações patenteáveis; (c) sem concessão de licença de PI.
**Risco se muito amplo**: Efetivamente concede uma licença para usar a informação confidencial da parte divulgadora para qualquer finalidade.

### Questão: Obrigação de Confidencialidade Perpétua
**Posição padrão**: 2-5 anos após a divulgação ou rescisão, o que ocorrer depois. Segredos de negócio podem justificar proteção enquanto permanecerem como segredos de negócio (Lei 9.279/96, art. 195).
**Abordagem de redline**: Substituir obrigação perpétua por prazo definido. Oferecer carveout de segredo de negócio para proteção mais longa de informações qualificadas.

## Notas

- Se o documento não é realmente um NDA (ex: está rotulado como NDA mas contém termos comerciais substantivos), sinalizar isso imediatamente como VERMELHO e recomendar revisão completa de contrato
- Para NDAs que fazem parte de um acordo maior (ex: seção de confidencialidade em um MSA), registrar que o contexto do acordo mais amplo pode afetar a análise
- Sempre registrar que esta é uma ferramenta de triagem e Thaís Menezes ou Vitor Lacerda devem revisar quaisquer itens sobre os quais o usuário tenha incerteza
- **Este documento não constitui aconselhamento jurídico.**
