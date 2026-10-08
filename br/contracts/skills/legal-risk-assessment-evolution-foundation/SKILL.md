---
name: legal-risk-assessment-evolution-foundation
title: legal-risk-assessment — Avaliação de Risco Jurídico
description: Avaliar e classificar riscos jurídicos usando um framework de severidade por probabilidade com critérios de escalação. Use ao avaliar risco contratual, ao estimar exposição de negócio, ao classificar questões por severidade, ou ao determinar se uma questão precisa de assessoria sênior ou revisão jurídica externa.
author: evolution-foundation
author_url: https://github.com/evolution-foundation/evo-nexus/tree/main/.claude/skills/legal-risk-assessment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# legal-risk-assessment — Avaliação de Risco Jurídico

> **Este documento não constitui aconselhamento jurídico — consulte o assessor jurídico habilitado antes de tomar decisões com base nesta análise.**
> Contatos legais: **Thaís Menezes** (contratos Brius/Etus) | **Vitor Lacerda** (jurídico Etus)

Avaliar, classificar e documentar riscos jurídicos usando um framework estruturado baseado em severidade e probabilidade.

O framework fornecido é um ponto de partida que organizações devem customizar para seu apetite de risco e contexto da indústria.

## Acionamento

User executa `/legal-risk-assessment` ou solicita avaliar, classificar ou analisar risco jurídico.

## Framework de Avaliação de Risco

### Matriz Severidade x Probabilidade

Riscos jurídicos são avaliados em duas dimensões:

**Severidade** (impacto se o risco se materializar):

| Nível | Rótulo | Descrição |
|---|---|---|
| 1 | **Negligível** | Inconveniência menor; sem impacto financeiro, operacional ou reputacional material. Pode ser tratado dentro das operações normais. |
| 2 | **Baixa** | Impacto limitado; exposição financeira menor (< 1% do valor do contrato/negócio relevante); interrupção operacional menor; sem atenção pública. |
| 3 | **Moderada** | Impacto significativo; exposição financeira material (1-5% do valor relevante); interrupção operacional perceptível; potencial de atenção pública limitada. |
| 4 | **Alta** | Impacto substancial; exposição financeira substancial (5-25% do valor relevante); interrupção operacional significativa; atenção pública provável; potencial escrutínio regulatório. |
| 5 | **Crítica** | Impacto severo; exposição financeira maior (> 25% do valor relevante); interrupção fundamental dos negócios; dano reputacional significativo; ação regulatória provável; potencial responsabilidade pessoal para diretores/sócios. |

**Probabilidade** (chance de o risco se materializar):

| Nível | Rótulo | Descrição |
|---|---|---|
| 1 | **Remota** | Altamente improvável; nenhum precedente conhecido em situações similares; exigiria circunstâncias excepcionais. |
| 2 | **Improvável** | Poderia ocorrer mas não é esperado; precedente limitado; exigiria eventos gatilho específicos. |
| 3 | **Possível** | Pode ocorrer; algum precedente existe; eventos gatilho são previsíveis. |
| 4 | **Provável** | Provavelmente ocorrerá; precedente claro; eventos gatilho são comuns em situações similares. |
| 5 | **Quase Certo** | Esperado que ocorra; forte precedente ou padrão; eventos gatilho estão presentes ou iminentes. |

### Cálculo do Escore de Risco

**Escore de Risco = Severidade x Probabilidade**

| Faixa de Escore | Nível de Risco | Cor |
|---|---|---|
| 1-4 | **Risco Baixo** | VERDE |
| 5-9 | **Risco Médio** | AMARELO |
| 10-15 | **Risco Alto** | LARANJA |
| 16-25 | **Risco Crítico** | VERMELHO |

### Visualização da Matriz de Risco

```
                    PROBABILIDADE
                Remota  Improvável  Possível  Provável  Quase Certo
                  (1)     (2)         (3)      (4)        (5)
SEVERIDADE
Crítica  (5)  |   5    |   10     |   15   |   20   |     25     |
Alta     (4)  |   4    |    8     |   12   |   16   |     20     |
Moderada (3)  |   3    |    6     |    9   |   12   |     15     |
Baixa    (2)  |   2    |    4     |    6   |    8   |     10     |
Negligível(1) |   1    |    2     |    3   |    4   |      5     |
```

## Níveis de Classificação de Risco com Ações Recomendadas

### VERDE — Risco Baixo (Escore 1-4)

**Características**:
- Questões menores que têm pouca probabilidade de se materializarem
- Riscos de negócios padrão dentro dos parâmetros operacionais normais
- Riscos bem compreendidos com mitigações estabelecidas em vigor

**Ações Recomendadas**:
- **Aceitar**: Reconhecer o risco e prosseguir com controles padrão
- **Documentar**: Registrar no registro de riscos para acompanhamento
- **Monitorar**: Incluir em revisões periódicas (trimestralmente ou anualmente)
- **Sem escalação necessária**: Pode ser gerido pelo membro da equipe responsável

**Exemplos**:
- Contrato com fornecedor com desvio menor dos termos padrão em área não crítica
- NDA rotineiro com contraparte conhecida em jurisdição padrão brasileira
- Tarefa administrativa menor de conformidade com prazo claro e responsável

### AMARELO — Risco Médio (Escore 5-9)

**Características**:
- Questões moderadas que poderiam se materializar em circunstâncias previsíveis
- Riscos que merecem atenção mas não requerem ação imediata
- Questões com precedente estabelecido para gestão

**Ações Recomendadas**:
- **Mitigar**: Implementar controles específicos ou negociar para reduzir a exposição
- **Monitorar ativamente**: Revisar em intervalos regulares (mensalmente ou quando gatilhos ocorrerem)
- **Documentar minuciosamente**: Registrar risco, mitigações e fundamentos no registro de riscos
- **Designar responsável**: Garantir que uma pessoa específica seja responsável pelo monitoramento e mitigação
- **Briefar stakeholders**: Informar os stakeholders de negócios relevantes sobre o risco e plano de mitigação
- **Escalar se as condições mudarem**: Definir eventos gatilho que elevariam o nível de risco

**Exemplos**:
- Contrato com teto de responsabilidade abaixo do padrão mas dentro da faixa negociável
- Fornecedor processando dados pessoais em jurisdição sem determinação clara de adequação pela ANPD
- Desenvolvimento regulatório que pode afetar uma atividade de negócio no médio prazo
- Disposição de PI mais ampla do que o preferido mas comum no mercado

### LARANJA — Risco Alto (Escore 10-15)

**Características**:
- Questões significativas com probabilidade significativa de se materializarem
- Riscos que poderiam resultar em impacto financeiro, operacional ou reputacional substancial
- Questões que requerem atenção sênior e esforços de mitigação dedicados

**Ações Recomendadas**:
- **Escalar para assessoria sênior**: Briefar Thaís Menezes ou Vitor Lacerda
- **Desenvolver plano de mitigação**: Criar um plano específico e acionável para reduzir o risco
- **Briefar liderança**: Informar os líderes de negócios relevantes sobre o risco e abordagem recomendada
- **Definir cadência de revisão**: Revisar semanalmente ou em marcos definidos
- **Considerar advogado externo**: Engajar assessoria externa para aconselhamento especializado se necessário
- **Documentar em detalhe**: Memorando completo de risco com análise, opções e recomendações
- **Definir plano de contingência**: O que a organização fará se o risco se materializar?

**Exemplos**:
- Contrato com indenização ilimitada em área material
- Atividade de processamento de dados que pode violar requisito regulatório da LGPD se não reestruturada
- Ameaça de litígio de contraparte significativa
- Alegação de infração de PI com fundamento plausível
- Consulta regulatória da ANPD, PROCON, MP, Receita Federal

### VERMELHO — Risco Crítico (Escore 16-25)

**Características**:
- Questões graves que provavelmente ou certamente se materializarão
- Riscos que poderiam impactar fundamentalmente o negócio, seus dirigentes ou seus stakeholders
- Questões requerendo atenção executiva imediata e resposta rápida

**Ações Recomendadas**:
- **Escalação imediata**: Briefar Davidson Gomes (CEO), Thaís Menezes e/ou Vitor Lacerda conforme adequado
- **Engajar advogado externo**: Contratar assessoria externa especializada imediatamente
- **Estabelecer equipe de resposta**: Equipe dedicada para gerenciar o risco com papéis claros
- **Considerar notificação de seguro**: Notificar seguradores se aplicável
- **Gestão de crise**: Ativar protocolos de gestão de crise se risco reputacional estiver envolvido
- **Preservar evidências**: Implementar hold judicial se procedimentos legais forem possíveis
- **Revisão diária ou mais frequente**: Gestão ativa até que o risco seja resolvido ou reduzido
- **Notificações regulatórias**: Fazer quaisquer notificações regulatórias obrigatórias (ANPD, CVM, BCB, etc.)

**Exemplos**:
- Litígio ativo com exposição significativa
- Incidente de segurança afetando dados pessoais regulados (LGPD art. 48)
- Ação de enforcement regulatório (ANPD, CADE, PROCON)
- Violação material de contrato pela ou contra a organização
- Investigação governamental
- Reclamação plausível de infração de PI contra produto ou serviço principal

## Padrões de Documentação para Avaliações de Risco

### Formato de Memorando de Avaliação de Risco

Toda avaliação formal de risco deve ser documentada usando a seguinte estrutura:

```
## Avaliação de Risco Jurídico

**Data**: [data da avaliação]
**Avaliador**: [pessoa conduzindo a avaliação]
**Questão**: [descrição da questão sendo avaliada]
**Privilegiado**: [Sim/Não — marcar como privilegiado advogado-cliente se aplicável]

### 1. Descrição do Risco
[Descrição clara e concisa do risco jurídico]

### 2. Contexto e Antecedentes
[Fatos relevantes, histórico e contexto de negócios]

### 3. Análise de Risco

#### Avaliação de Severidade: [1-5] — [Rótulo]
[Fundamentos para a classificação de severidade, incluindo exposição financeira potencial, impacto operacional e considerações reputacionais]

#### Avaliação de Probabilidade: [1-5] — [Rótulo]
[Fundamentos para a classificação de probabilidade, incluindo precedente, eventos gatilho e condições atuais]

#### Escore de Risco: [Escore] — [VERDE/AMARELO/LARANJA/VERMELHO]

### 4. Fatores Contribuintes
[O que aumenta o risco]

### 5. Fatores Mitigantes
[O que diminui o risco ou limita a exposição]

### 6. Opções de Mitigação

| Opção | Eficácia | Custo/Esforço | Recomendado? |
|---|---|---|---|
| [Opção 1] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Sim/Não] |
| [Opção 2] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Sim/Não] |

### 7. Abordagem Recomendada
[Curso de ação específico recomendado com fundamentos]

### 8. Risco Residual
[Nível de risco esperado após implementar as mitigações recomendadas]

### 9. Plano de Monitoramento
[Como e com que frequência o risco será monitorado; eventos gatilho para reavaliação]

### 10. Próximos Passos
1. [Item de ação 1 — Responsável — Prazo]
2. [Item de ação 2 — Responsável — Prazo]
```

### Entrada no Registro de Riscos

Para acompanhamento no registro de riscos da equipe:

| Campo | Conteúdo |
|---|---|
| ID do Risco | Identificador único |
| Data Identificada | Quando o risco foi identificado pela primeira vez |
| Descrição | Breve descrição |
| Categoria | Contratual, Regulatório, Litígio, PI, Privacidade de Dados, Trabalhista, Societário, Outro |
| Severidade | 1-5 com rótulo |
| Probabilidade | 1-5 com rótulo |
| Escore de Risco | Escore calculado |
| Nível de Risco | VERDE / AMARELO / LARANJA / VERMELHO |
| Responsável | Pessoa responsável pelo monitoramento |
| Mitigações | Controles atuais em vigor |
| Status | Aberto / Mitigado / Aceito / Fechado |
| Data de Revisão | Próxima revisão agendada |
| Notas | Contexto adicional |

## Quando Engajar Advogado Externo

Engajar assessoria externa quando:

### Engajamento Obrigatório
- **Litígio ativo**: Qualquer ação judicial movida contra ou pela organização
- **Investigação governamental**: Qualquer consulta de agência governamental, regulador (ANPD, CVM, BCB, CADE, PROCON, MP, TCU) ou autoridade policial
- **Exposição criminal**: Qualquer questão com potencial responsabilidade criminal para a organização ou seus dirigentes
- **Questões societárias/CVM**: Qualquer questão que possa afetar divulgações ou arquivamentos societários
- **Questões de conselho**: Qualquer questão requerendo notificação ou aprovação do conselho — escalar para Davidson Gomes

### Engajamento Fortemente Recomendado
- **Questões jurídicas novas**: Questões de primeira impressão ou direito incerto onde a posição da organização poderia criar precedente
- **Complexidade jurisdicional**: Questões envolvendo jurisdições desconhecidas ou requisitos legais conflitantes
- **Exposição financeira material**: Riscos com exposição potencial excedendo os limites de tolerância de risco da organização
- **Expertise especializada necessária**: Questões requerendo expertise profunda em domínio não disponível internamente (antitruste, FCPA, propriedade industrial, etc.)
- **Mudanças regulatórias**: Novas regulamentações que afetam materialmente o negócio e requerem desenvolvimento de programa de conformidade
- **Transações de M&A**: Due diligence, estruturação e aprovações regulatórias para transações significativas

### Considerar Engajamento
- **Disputas contratuais complexas**: Desacordos significativos sobre interpretação de contrato com contrapartes materiais
- **Questões trabalhistas**: Reclamações ou reclamações potenciais envolvendo discriminação, assédio, rescisão indireta ou proteções de whistleblower (CLT)
- **Incidentes de dados**: Potenciais violações de dados que podem acionar obrigações de notificação (LGPD art. 48)
- **Disputas de PI**: Alegações de infração (recebidas ou contempladas) envolvendo produtos ou serviços materiais
- **Disputas de cobertura de seguro**: Desacordos com seguradores sobre cobertura de reclamações materiais

### Selecionando Advogado Externo

Ao recomendar engajamento de advogado externo, sugerir ao usuário considerar:
- Expertise em direito brasileiro relevante (LGPD, CLT, Código Civil, propriedade industrial, etc.)
- Experiência na jurisdição aplicável (estadual, federal, arbitragem)
- Entendimento da indústria de tecnologia e SaaS no Brasil
- Verificação de conflito de interesses
- Expectativas de orçamento e arranjos de honorários (por hora, honorário fixo, honorário de êxito — regulado pela OAB)
- Relacionamentos existentes (Thaís Menezes para contratos/Brius, Vitor Lacerda para questões Etus)
- Certificações e especializações da OAB

> **Este documento não constitui aconselhamento jurídico.** Contatos: Thaís Menezes | Vitor Lacerda
