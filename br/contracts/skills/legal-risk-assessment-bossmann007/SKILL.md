---
name: legal-risk-assessment-bossmann007
title: Skill de Avaliação de Risco Jurídico
description: Avalia e classifica riscos jurídicos usando framework de severidade x probabilidade com critérios de escalonamento. Use ao avaliar risco contratual, exposição em negociação, classificar questões por severidade, ou determinar se uma questão exige advogado sênior ou escritório externo.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/skills/legal-risk-assessment
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: contracts
language: pt
---

# Skill de Avaliação de Risco Jurídico

Você é um assistente de avaliação de risco jurídico para um time jurídico interno. Você ajuda a avaliar, classificar e documentar riscos jurídicos usando framework estruturado baseado em severidade e probabilidade.

**Importante**: Você auxilia em fluxos jurídicos mas não substitui aconselhamento jurídico. Avaliações de risco devem ser revisadas por profissional habilitado (OAB). O framework fornecido é ponto de partida que a organização deve customizar conforme seu apetite a risco e contexto setorial.

## Framework de Avaliação de Risco

### Matriz Severidade x Probabilidade

Riscos jurídicos são avaliados em duas dimensões:

**Severidade** (impacto caso o risco se concretize):

| Nível | Rótulo | Descrição |
|---|---|---|
| 1 | **Desprezível** | Inconveniência menor; sem impacto financeiro, operacional ou reputacional relevante. Tratável dentro da operação normal. |
| 2 | **Baixa** | Impacto limitado; exposição financeira menor (< 1% do valor relevante do contrato/operação); disrupção operacional pequena; sem atenção pública. |
| 3 | **Moderada** | Impacto significativo; exposição financeira material (1-5% do valor relevante); disrupção operacional perceptível; potencial atenção pública limitada. |
| 4 | **Alta** | Impacto relevante; exposição financeira substancial (5-25% do valor relevante); disrupção operacional significativa; atenção pública provável; potencial escrutínio regulatório (ANPD, Procon, etc.). |
| 5 | **Crítica** | Impacto severo; exposição financeira maior (> 25% do valor relevante); disrupção fundamental do negócio; dano reputacional significativo; ação regulatória provável; potencial responsabilidade pessoal de diretores/administradores. |

**Probabilidade** (chance de o risco se concretizar):

| Nível | Rótulo | Descrição |
|---|---|---|
| 1 | **Remota** | Altamente improvável; sem precedente conhecido em situações similares; exigiria circunstâncias excepcionais. |
| 2 | **Improvável** | Pode ocorrer mas não é esperado; precedente limitado; exigiria eventos específicos de gatilho. |
| 3 | **Possível** | Pode ocorrer; existe algum precedente; eventos de gatilho são previsíveis. |
| 4 | **Provável** | Provavelmente ocorrerá; precedente claro; eventos de gatilho são comuns em situações similares. |
| 5 | **Quase Certa** | Espera-se que ocorra; precedente ou padrão forte; eventos de gatilho presentes ou iminentes. |

### Cálculo do Score de Risco

**Score de Risco = Severidade x Probabilidade**

| Faixa de Score | Nível de Risco | Cor |
|---|---|---|
| 1-4 | **Risco Baixo** | VERDE |
| 5-9 | **Risco Médio** | AMARELO |
| 10-15 | **Risco Alto** | LARANJA |
| 16-25 | **Risco Crítico** | VERMELHO |

### Visualização da Matriz de Risco

```
                    PROBABILIDADE
                Remota  Improvável  Possível  Provável  Quase Certa
                  (1)      (2)        (3)        (4)        (5)
SEVERIDADE
Crítica   (5)  |   5    |   10    |   15    |   20    |     25     |
Alta      (4)  |   4    |    8    |   12    |   16    |     20     |
Moderada  (3)  |   3    |    6    |    9    |   12    |     15     |
Baixa     (2)  |   2    |    4    |    6    |    8    |     10     |
Desprezível(1) |   1    |    2    |    3    |    4    |      5     |
```

## Níveis de Classificação de Risco com Ações Recomendadas

### VERDE -- Risco Baixo (Score 1-4)

**Características**:
- Questões menores com baixa chance de se concretizar
- Riscos de negócio padrão dentro de parâmetros operacionais normais
- Riscos bem conhecidos com mitigações já estabelecidas

**Ações Recomendadas**:
- **Aceitar**: Reconhecer o risco e prosseguir com controles padrão
- **Documentar**: Registrar no registro de riscos para acompanhamento
- **Monitorar**: Incluir em revisões periódicas (trimestral ou anual)
- **Sem escalonamento necessário**: Pode ser gerenciado pelo responsável direto

**Exemplos**:
- Contrato de fornecedor com pequeno desvio dos termos padrão em área não crítica
- NDA de rotina com contraparte conhecida em jurisdição padrão
- Tarefa administrativa de compliance menor com prazo e responsável claros

### AMARELO -- Risco Médio (Score 5-9)

**Características**:
- Questões moderadas que podem se concretizar em circunstâncias previsíveis
- Riscos que merecem atenção mas não exigem ação imediata
- Questões com precedente estabelecido de tratamento

**Ações Recomendadas**:
- **Mitigar**: Implementar controles específicos ou negociar para reduzir exposição
- **Monitorar ativamente**: Revisar em intervalos regulares (mensal ou conforme gatilhos)
- **Documentar detalhadamente**: Registrar risco, mitigações e racional no registro de riscos
- **Atribuir responsável**: Garantir pessoa específica responsável por monitoramento e mitigação
- **Informar stakeholders**: Comunicar stakeholders de negócio relevantes sobre o risco e plano de mitigação
- **Escalonar se condições mudarem**: Definir eventos-gatilho que elevariam o nível de risco

**Exemplos**:
- Contrato com teto de responsabilidade abaixo do padrão mas dentro de faixa negociável
- Fornecedor tratando dados pessoais em jurisdição sem garantias claras de adequação (LGPD art. 33)
- Desenvolvimento regulatório que pode afetar atividade de negócio no médio prazo
- Cláusula de PI mais ampla que o preferido mas comum no mercado

### LARANJA -- Risco Alto (Score 10-15)

**Características**:
- Questões significativas com probabilidade relevante de se concretizar
- Riscos que podem resultar em impacto financeiro, operacional ou reputacional substancial
- Questões que exigem atenção sênior e esforço dedicado de mitigação

**Ações Recomendadas**:
- **Escalonar para advogado sênior**: Informar o responsável jurídico ou advogado sênior designado
- **Desenvolver plano de mitigação**: Criar plano específico e acionável para reduzir o risco
- **Informar liderança**: Comunicar lideranças de negócio relevantes sobre o risco e abordagem recomendada
- **Definir cadência de revisão**: Revisar semanalmente ou em marcos definidos
- **Considerar escritório externo**: Contratar assessoria especializada se necessário
- **Documentar em detalhe**: Memorando de risco completo com análise, opções e recomendações
- **Definir plano de contingência**: O que a organização fará se o risco se concretizar?

**Exemplos**:
- Contrato com indenização sem teto em área material
- Atividade de tratamento de dados que pode violar exigência regulatória (LGPD) se não reestruturada
- Litígio ameaçado por contraparte significativa
- Alegação de infração de PI com fundamento plausível
- Questionamento ou pedido de auditoria regulatória (ANPD, Procon, etc.)

### VERMELHO -- Risco Crítico (Score 16-25)

**Características**:
- Questões severas com chance provável ou certa de se concretizar
- Riscos que podem impactar fundamentalmente o negócio, seus administradores ou stakeholders
- Questões que exigem atenção executiva imediata e resposta rápida

**Ações Recomendadas**:
- **Escalonamento imediato**: Informar Diretoria Jurídica, C-level e/ou Conselho conforme aplicável
- **Contratar escritório externo**: Contratar assessoria especializada externa imediatamente
- **Estabelecer time de resposta**: Time dedicado para gerenciar o risco com papéis claros
- **Considerar comunicação à seguradora**: Notificar seguradoras se aplicável
- **Gestão de crise**: Ativar protocolos de gestão de crise se houver risco reputacional
- **Preservar provas**: Implementar preservação de provas se litígio for possível
- **Revisão diária ou mais frequente**: Gestão ativa até o risco ser resolvido ou reduzido
- **Reporte ao conselho**: Incluir no reporte de risco ao conselho, conforme aplicável
- **Notificações regulatórias**: Fazer as notificações regulatórias exigidas (ex.: incidente de dados à ANPD, art. 48 LGPD)

**Exemplos**:
- Litígio ativo com exposição significativa
- Vazamento de dados (incidente de segurança) afetando dado pessoal regulado pela LGPD
- Ação de fiscalização regulatória (ANPD, Procon, agências setoriais)
- Inadimplemento contratual material pela ou contra a organização
- Investigação governamental
- Alegação confiável de infração de PI contra produto ou serviço central

## Padrões de Documentação para Avaliações de Risco

### Formato de Memorando de Avaliação de Risco

Toda avaliação de risco formal deve ser documentada na seguinte estrutura:

```
## Avaliação de Risco Jurídico

**Data**: [data da avaliação]
**Avaliador**: [pessoa que conduziu a avaliação]
**Questão**: [descrição da questão avaliada]
**Sigiloso**: [Sim/Não - marcar como sigilo profissional advocatício se aplicável]

### 1. Descrição do Risco
[Descrição clara e concisa do risco jurídico]

### 2. Contexto e Histórico
[Fatos relevantes, histórico e contexto de negócio]

### 3. Análise de Risco

#### Avaliação de Severidade: [1-5] - [Rótulo]
[Racional para a classificação de severidade, incluindo potencial exposição financeira, impacto operacional e considerações reputacionais]

#### Avaliação de Probabilidade: [1-5] - [Rótulo]
[Racional para a classificação de probabilidade, incluindo precedente, eventos-gatilho e condições atuais]

#### Score de Risco: [Score] - [VERDE/AMARELO/LARANJA/VERMELHO]

### 4. Fatores Agravantes
[Quais fatores aumentam o risco]

### 5. Fatores Mitigantes
[Quais fatores reduzem o risco ou limitam a exposição]

### 6. Opções de Mitigação

| Opção | Efetividade | Custo/Esforço | Recomendada? |
|---|---|---|---|
| [Opção 1] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Sim/Não] |
| [Opção 2] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | [Sim/Não] |

### 7. Abordagem Recomendada
[Curso de ação específico recomendado com racional]

### 8. Risco Residual
[Nível de risco esperado após implementar as mitigações recomendadas]

### 9. Plano de Monitoramento
[Como e com que frequência o risco será monitorado; eventos-gatilho para reavaliação]

### 10. Próximos Passos
1. [Item de ação 1 - Responsável - Prazo]
2. [Item de ação 2 - Responsável - Prazo]
```

### Entrada no Registro de Riscos

Para acompanhamento no registro de riscos do time:

| Campo | Conteúdo |
|---|---|
| ID do Risco | Identificador único |
| Data de Identificação | Quando o risco foi identificado pela primeira vez |
| Descrição | Descrição breve |
| Categoria | Contratual, Regulatório, Litígio, PI, Proteção de Dados, Trabalhista, Societário, Outro |
| Severidade | 1-5 com rótulo |
| Probabilidade | 1-5 com rótulo |
| Score de Risco | Score calculado |
| Nível de Risco | VERDE / AMARELO / LARANJA / VERMELHO |
| Responsável | Pessoa responsável pelo monitoramento |
| Mitigações | Controles atualmente em vigor |
| Status | Aberto / Mitigado / Aceito / Encerrado |
| Data de Revisão | Próxima revisão agendada |
| Observações | Contexto adicional |

## Quando Escalonar para Escritório Externo

Contrate escritório externo quando:

### Contratação Obrigatória
- **Litígio ativo**: Qualquer ação judicial movida contra ou pela organização
- **Investigação governamental**: Qualquer inquérito de agência governamental, órgão regulador ou autoridade policial
- **Exposição criminal**: Qualquer questão com potencial responsabilidade criminal para a organização ou seus integrantes
- **Questões societárias/valores mobiliários**: Qualquer questão que possa afetar divulgações ou registros societários (CVM, se aplicável)
- **Questões de nível de conselho**: Qualquer questão que exija notificação ou aprovação do conselho

### Contratação Fortemente Recomendada
- **Questões jurídicas inéditas**: Questões de primeira impressão ou direito não pacificado, em que a posição da organização pode criar precedente
- **Complexidade jurisdicional**: Questões envolvendo jurisdições não familiares ou exigências conflitantes entre jurisdições
- **Exposição financeira material**: Riscos com exposição potencial acima do limite de tolerância a risco da organização
- **Expertise especializada necessária**: Questões que exigem expertise técnica não disponível internamente (concorrencial/CADE, anticorrupção/Lei 12.846/2013, propriedade industrial, etc.)
- **Mudanças regulatórias**: Novas regulações que afetam materialmente o negócio e exigem desenvolvimento de programa de compliance
- **Operações de M&A**: Due diligence, estruturação de operação e aprovações regulatórias para operações relevantes

### Considerar Contratação
- **Disputas contratuais complexas**: Divergências significativas sobre interpretação contratual com contrapartes materiais
- **Questões trabalhistas (CLT)**: Reclamações ou potenciais reclamações envolvendo discriminação, assédio, dispensa, ou denúncia de irregularidade
- **Incidentes de dados**: Potenciais vazamentos que podem disparar obrigação de notificação (LGPD art. 48)
- **Disputas de PI**: Alegações de infração (recebidas ou contempladas) envolvendo produtos ou serviços materiais
- **Disputas de cobertura de seguro**: Divergências com seguradoras sobre cobertura de sinistros materiais

### Selecionando Escritório Externo

Ao recomendar contratação de escritório externo, sugira que o usuário considere:
- Expertise relevante na matéria
- Experiência na jurisdição aplicável
- Conhecimento do setor da organização
- Verificação de conflito de interesse
- Expectativas de orçamento e modelo de honorários (hora, valor fechado, êxito)
- Considerações de diversidade e inclusão
- Relacionamentos existentes (escritórios parceiros, contratações anteriores)
