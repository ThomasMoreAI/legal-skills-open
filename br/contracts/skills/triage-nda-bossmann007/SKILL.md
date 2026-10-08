---
name: triage-nda-bossmann007
title: /triage-nda -- Pré-Triagem de NDA
description: Faz a triagem rápida de um Acordo de Confidencialidade (NDA) recebido e o classifica como VERDE (aprovação padrão), AMARELO (revisão jurídica) ou VERMELHO (revisão jurídica completa). Use quando um novo NDA chegar do comercial ou desenvolvimento de negócios, ao buscar cláusulas de não aliciamento, não concorrência ou exceções ausentes, ou ao decidir se o NDA pode ser assinado sob delegação padrão.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/skills/triage-nda
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# /triage-nda -- Pré-Triagem de NDA

> Se você encontrar placeholders desconhecidos ou precisar checar quais ferramentas estão conectadas, veja [CONNECTORS.md](../../CONNECTORS.md).

Faça a triagem do NDA: @$1

Faça a triagem rápida de Acordos de Confidencialidade recebidos contra critérios padrão. Classifique o NDA para encaminhamento: aprovação padrão, revisão jurídica ou revisão jurídica completa.

**Importante**: você auxilia em fluxos jurídicos mas não fornece aconselhamento jurídico. Toda análise deve ser revisada por advogado antes de embasar decisões.

## Invocação

```
/triage-nda
```

## Fluxo

### Etapa 1: Receber o NDA

Aceite o NDA em qualquer formato:
- **Upload de arquivo**: PDF, DOCX ou outro formato
- **URL**: link para o NDA em um sistema de documentos
- **Texto colado**: texto do NDA colado diretamente

Se nenhum NDA for fornecido, peça ao usuário que envie um.

### Etapa 2: Carregar o Playbook de NDA

Procure critérios de triagem de NDA nas configurações locais (ex.: `legal.local.md`).

O playbook de NDA deve definir:
- Exigência de obrigações mútuas vs. unilaterais
- Prazos aceitáveis
- Exceções (carveouts) exigidas
- Cláusulas proibidas
- Requisitos específicos da organização

**Se nenhum playbook de NDA estiver configurado:**
- Prossiga com padrões de mercado razoáveis
- Deixe claro que padrões estão sendo usados
- Padrões aplicados:
  - Obrigações mútuas exigidas (salvo se a organização apenas divulga)
  - Prazo: 2-3 anos padrão, até 5 anos para segredo de negócio (Lei 9.279/1996, art. 195 — concorrência desleal)
  - Exceções padrão exigidas: desenvolvido independentemente, de domínio público, recebido legitimamente de terceiro, exigido por lei
  - Sem cláusulas de não aliciamento ou não concorrência
  - Sem cláusula de resíduos (ou de escopo restrito, se presente)
  - Lei aplicável e foro em praça comercial razoável no Brasil

### Etapa 3: Triagem Rápida

Avalie o NDA contra cada critério sistematicamente.

#### 1. Estrutura do Acordo
- [ ] **Tipo identificado**: NDA mútuo, unilateral (parte reveladora) ou unilateral (parte receptora)
- [ ] **Adequado ao contexto**: o tipo de NDA é adequado à relação de negócio? (ex.: mútuo para discussões exploratórias, unilateral para divulgação em uma só via)
- [ ] **Acordo autônomo**: confirme que o NDA é um acordo autônomo, não uma cláusula de confidencialidade embutida em contrato comercial maior

#### 2. Definição de Informação Confidencial
- [ ] **Escopo razoável**: não excessivamente amplo (evite "toda e qualquer informação, marcada ou não como confidencial")
- [ ] **Requisitos de marcação**: se exigida marcação, ela é viável? (marcação por escrito em até 30 dias após divulgação oral é padrão)
- [ ] **Exclusões presentes**: exclusões padrão definidas (ver Exceções Padrão abaixo)
- [ ] **Sem inclusões problemáticas**: não define informação pública ou desenvolvida independentemente como confidencial

#### 3. Obrigações da Parte Receptora
- [ ] **Padrão de cuidado**: cuidado razoável, ou ao menos o mesmo cuidado dado às próprias informações confidenciais
- [ ] **Restrição de uso**: limitada à finalidade declarada
- [ ] **Restrição de divulgação**: limitada a quem precisa conhecer e está vinculado a obrigação similar
- [ ] **Sem obrigações onerosas**: sem exigências impraticáveis (ex.: criptografar todas as comunicações, manter registros físicos)

#### 4. Exceções Padrão (Carveouts)
Todas as exceções a seguir devem estar presentes:
- [ ] **Conhecimento público**: informação que é ou se torna pública sem culpa da parte receptora
- [ ] **Posse prévia**: informação já conhecida pela parte receptora antes da divulgação
- [ ] **Desenvolvimento independente**: informação desenvolvida independentemente, sem uso ou referência à informação confidencial
- [ ] **Recebimento de terceiro**: informação legitimamente recebida de terceiro sem restrição
- [ ] **Determinação legal**: direito de divulgar quando exigido por lei, regulação ou processo legal (com aviso à parte reveladora quando legalmente permitido)

#### 5. Divulgações Permitidas
- [ ] **Empregados**: pode compartilhar com empregados que precisam conhecer (CLT)
- [ ] **Contratados/consultores**: pode compartilhar com prestadores e consultores sob obrigação de confidencialidade similar
- [ ] **Afiliadas**: pode compartilhar com afiliadas (se necessário à finalidade do negócio)
- [ ] **Jurídico/regulatório**: pode divulgar conforme exigido por lei ou regulação (inclusive LGPD, quando aplicável)

#### 6. Prazo e Duração
- [ ] **Vigência do acordo**: período razoável para a relação de negócio (1-3 anos é padrão)
- [ ] **Sobrevivência da confidencialidade**: obrigações sobrevivem por período razoável após a rescisão (2-5 anos é padrão; segredo de negócio pode ser mais longo)
- [ ] **Não perpétua**: evite obrigações de confidencialidade indefinidas ou perpétuas (exceção: segredo de negócio, que pode justificar proteção mais longa)

#### 7. Devolução e Destruição
- [ ] **Gatilho da obrigação**: na rescisão ou mediante solicitação
- [ ] **Escopo razoável**: devolver ou destruir a informação confidencial e todas as cópias
- [ ] **Exceção de retenção**: permite retenção de cópias exigidas por lei, regulação ou políticas internas de compliance/backup (e.g. obrigações de guarda da LGPD)
- [ ] **Certificação**: certificação de destruição é razoável; declaração com firma reconhecida é onerosa

#### 8. Remédios
- [ ] **Tutela de urgência**: reconhecimento de que a violação pode causar dano irreparável e que medidas cautelares/tutela específica podem ser cabíveis (CPC, arts. 297 e 497) é padrão
- [ ] **Sem indenização pré-fixada**: evite cláusula penal em NDAs
- [ ] **Sem unilateralidade**: disposições sobre remédios aplicam-se igualmente a ambas as partes (em NDAs mútuos)

#### 9. Cláusulas Problemáticas a Sinalizar
- [ ] **Sem não aliciamento**: o NDA não deve conter cláusula de não aliciamento de empregados
- [ ] **Sem não concorrência**: o NDA não deve conter cláusula de não concorrência
- [ ] **Sem exclusividade**: o NDA não deve restringir nenhuma das partes de manter discussões similares com outros
- [ ] **Sem standstill**: o NDA não deve conter cláusula de standstill ou similar (salvo em contexto de M&A)
- [ ] **Sem cláusula de resíduos ampla** (ou de escopo restrito): se presente, deve se limitar a informação retida na memória não assistida de indivíduos, sem abranger segredo de negócio ou matéria patenteável
- [ ] **Sem cessão ou licença de PI**: o NDA não deve conceder direitos de propriedade intelectual
- [ ] **Sem direito de auditoria**: incomum em NDAs padrão

#### 10. Lei Aplicável e Foro
- [ ] **Foro razoável**: comarca comercial bem estabelecida no Brasil (ou jurisdição estrangeira justificada pelo contexto)
- [ ] **Consistência**: lei aplicável e foro devem ser coerentes entre si
- [ ] **Sem arbitragem obrigatória** (em NDAs padrão): litígio judicial é geralmente preferível para disputas de NDA, salvo cláusula compromissória já praticada pela organização

### Etapa 4: Classificar

Com base nos resultados da triagem, atribua uma classificação:

#### VERDE -- Aprovação Padrão

**Todos** os itens a seguir devem ser verdadeiros:
- NDA é mútuo (ou unilateral na direção apropriada)
- Todas as exceções padrão estão presentes
- Prazo dentro da faixa padrão (1-3 anos, sobrevivência 2-5 anos)
- Sem cláusulas de não aliciamento, não concorrência ou exclusividade
- Sem cláusula de resíduos, ou de escopo restrito
- Lei aplicável e foro razoáveis
- Remédios padrão (sem cláusula penal)
- Divulgações permitidas incluem empregados, prestadores e consultores
- Devolução/destruição inclui exceção de retenção para fins legais/compliance
- Definição de informação confidencial com escopo razoável

**Encaminhamento**: aprovar via delegação padrão de alçada. Sem necessidade de revisão jurídica.
- **Ação**: prosseguir para assinatura com delegação padrão de alçada

#### AMARELO -- Necessita Revisão Jurídica

**Um ou mais** dos itens a seguir estão presentes, mas o NDA não é fundamentalmente problemático:
- Definição de informação confidencial mais ampla que o preferido, mas não irrazoável
- Prazo mais longo que o padrão, mas dentro da faixa de mercado (ex.: 5 anos de vigência, 7 anos de sobrevivência)
- Falta uma exceção padrão que pode ser adicionada sem dificuldade
- Cláusula de resíduos presente, mas restrita à memória não assistida
- Lei aplicável e foro em jurisdição aceitável, mas não preferida
- Assimetria menor em NDA mútuo (ex.: uma parte com divulgações permitidas ligeiramente mais amplas)
- Requisitos de marcação presentes mas viáveis
- Devolução/destruição sem exceção explícita de retenção (provavelmente implícita, mas deve ser adicionada)
- Cláusulas incomuns mas não prejudiciais (ex.: obrigação de notificar potencial violação)

**Encaminhamento**: sinalizar pontos específicos para revisão jurídica. O jurídico provavelmente resolve com redlines pequenos em uma única rodada.
- **Ação**: jurídico provavelmente resolve em uma única rodada de revisão

#### VERMELHO -- Problemas Relevantes

**Um ou mais** dos itens a seguir estão presentes:
- **Unilateral quando mútuo é exigido** (ou direção errada para a relação)
- **Exceções críticas ausentes** (especialmente desenvolvimento independente ou determinação legal)
- **Cláusulas de não aliciamento ou não concorrência** embutidas no NDA
- **Cláusulas de exclusividade ou standstill** sem contexto de negócio apropriado
- **Prazo irrazoável** (10+ anos, ou perpétuo sem justificativa de segredo de negócio)
- **Definição excessivamente ampla** que poderia abranger informação pública ou desenvolvida independentemente
- **Cláusula de resíduos ampla** que na prática cria licença de uso da informação confidencial
- **Cessão ou licença de PI** escondida no NDA
- **Cláusula penal ou indenização pré-fixada**
- **Direitos de auditoria** sem escopo ou aviso razoáveis
- **Foro altamente desfavorável** com arbitragem obrigatória
- **O documento não é de fato um NDA** (contém termos comerciais substantivos, exclusividade ou outras obrigações além de confidencialidade)

**Encaminhamento**: revisão jurídica completa necessária. Não assinar. Requer negociação, contraproposta com a minuta padrão da organização, ou rejeição.
- **Ação**: não assinar; requer negociação ou contraproposta

### Etapa 5: Gerar Relatório de Triagem

Gere um relatório estruturado:

```
## Relatório de Triagem de NDA

**Classificação**: [VERDE / AMARELO / VERMELHO]
**Partes**: [nomes das partes]
**Tipo**: [Mútuo / Unilateral (reveladora) / Unilateral (receptora)]
**Prazo**: [duração]
**Lei Aplicável / Foro**: [jurisdição]
**Base da Revisão**: [Playbook / Padrões Default]

## Resultado da Triagem

| Critério | Status | Notas |
|-----------|--------|-------|
| Obrigações Mútuas | [OK/SINALIZADO/FALHA] | [detalhes] |
| Escopo da Definição | [OK/SINALIZADO/FALHA] | [detalhes] |
| Prazo | [OK/SINALIZADO/FALHA] | [detalhes] |
| Exceções Padrão | [OK/SINALIZADO/FALHA] | [detalhes] |
| [etc.] | | |

## Problemas Encontrados

### [Problema 1 -- AMARELO/VERMELHO]
**O quê**: [descrição]
**Risco**: [o que pode dar errado]
**Sugestão de Ajuste**: [redação ou abordagem específica]

[Repita para cada problema]

## Recomendação

[Próximo passo específico: aprovar, enviar para revisão com notas específicas, ou rejeitar/contrapropor]

## Próximos Passos

1. [Ação 1]
2. [Ação 2]
```

### Etapa 6: Sugestão de Encaminhamento

Com base na classificação, recomende o próximo passo apropriado:

| Classificação | Ação Recomendada | Prazo Típico |
|---|---|---|
| VERDE | Aprovar e encaminhar para assinatura conforme alçada | Mesmo dia |
| AMARELO | Enviar ao revisor designado com pontos específicos sinalizados | 1-2 dias úteis |
| VERMELHO | Acionar jurídico para revisão completa; preparar contraproposta ou minuta padrão | 3-5 dias úteis |

Para classificações AMARELO e VERMELHO:
- Identifique a pessoa ou função que deve revisar (se a organização tiver regras de encaminhamento definidas)
- Inclua um resumo breve dos problemas para que o revisor entenda rapidamente os pontos-chave
- Se a organização tiver minuta padrão de NDA, recomende enviá-la como contraproposta para NDAs classificados VERMELHO

## Problemas Comuns e Posições Padrão

### Problema: Definição Excessivamente Ampla de Informação Confidencial
**Posição padrão**: informação confidencial deve se limitar a informação não pública divulgada em conexão com a finalidade declarada, com exclusões claras.
**Abordagem de redline**: restrinja a definição a informação marcada ou identificada como confidencial, ou que uma pessoa razoável entenderia como confidencial dada a natureza da informação e as circunstâncias da divulgação.

### Problema: Ausência de Exceção de Desenvolvimento Independente
**Posição padrão**: deve incluir exceção para informação desenvolvida independentemente, sem referência ou uso da informação confidencial da parte reveladora.
**Risco se ausente**: pode gerar alegações de que produtos ou funcionalidades desenvolvidos internamente derivaram de informação confidencial da contraparte.
**Abordagem de redline**: adicionar a exceção padrão de desenvolvimento independente.

### Problema: Não Aliciamento de Empregados
**Posição padrão**: cláusulas de não aliciamento não pertencem a NDAs. São apropriadas em contratos de trabalho (CLT), acordos de M&A ou contratos comerciais específicos.
**Abordagem de redline**: excluir a cláusula por completo. Se a contraparte insistir, limitar a aliciamento direcionado (não recrutamento geral) e prazo curto (12 meses).

### Problema: Cláusula de Resíduos Ampla
**Posição padrão**: resistir a cláusulas de resíduos. Se exigida, limitar a: (a) ideias gerais, conceitos, know-how ou técnicas retidas na memória não assistida de indivíduos com acesso autorizado; (b) excluir explicitamente segredo de negócio e matéria patenteável; (c) não conceder licença de PI.
**Risco se ampla demais**: na prática concede licença de uso da informação confidencial da parte reveladora para qualquer finalidade.

### Problema: Obrigação de Confidencialidade Perpétua
**Posição padrão**: 2-5 anos a partir da divulgação ou rescisão, o que ocorrer por último. Segredo de negócio pode justificar proteção enquanto permanecer como tal (Lei 9.279/1996).
**Abordagem de redline**: substituir a obrigação perpétua por prazo definido. Oferecer exceção de segredo de negócio para proteção mais longa de informação qualificada.

## Observações

- Se o documento não for de fato um NDA (ex.: rotulado como NDA mas contendo termos comerciais substantivos), sinalize imediatamente como VERMELHO e recomende revisão contratual completa
- Para NDAs que fazem parte de um acordo maior (ex.: cláusula de confidencialidade em um contrato de prestação de serviços), observe que o contexto do acordo mais amplo pode afetar a análise
- Sempre destaque que esta é uma ferramenta de triagem e que o jurídico deve revisar quaisquer itens sobre os quais o usuário tenha dúvida
