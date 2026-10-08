# Análise Financeira em Investigações Policiais

## Metodologia de Análise Financeira

### 1. Coleta e Organização dos Dados

#### Fontes Primárias
- **Extratos bancários**: Movimentação detalhada de todas as contas
- **RIF/COAF (UIF)**: Relatórios de Inteligência Financeira
- **Declarações de IR**: Patrimônio declarado e renda informada
- **Registros cartoriais**: Imóveis, veículos, empresas
- **Dados da Receita Federal**: QSA, CNAE, situação cadastral
- **SIMBA/SISBAJUD**: Dados de ordens judiciais bancárias
- **INFOSEG/SINESP**: Antecedentes e registros policiais

#### Organização Padrão
```
Para cada investigado/pessoa de interesse:
├── Dados pessoais e cadastrais
├── Empresas vinculadas (CNPJ)
├── Contas bancárias identificadas
├── Movimentação financeira (por conta, por período)
├── Patrimônio identificado
├── Renda declarada
└── Operações atípicas sinalizadas
```

### 2. Análise de Compatibilidade Patrimonial

**Objetivo**: Verificar se o patrimônio e gastos são compatíveis com a renda declarada.

#### Fórmula Básica
```
EVOLUÇÃO PATRIMONIAL = Patrimônio Final - Patrimônio Inicial
GASTOS DO PERÍODO = Despesas comprovadas + Consumo estimado
RENDA DECLARADA = Rendimentos informados à Receita Federal

Se (EVOLUÇÃO + GASTOS) > RENDA DECLARADA → PATRIMÔNIO INCOMPATÍVEL
Diferença = Excedente não justificado = Possível produto de crime
```

#### Checklist de Compatibilidade
- [ ] Levantar renda declarada no período investigado
- [ ] Identificar todo patrimônio (início e fim do período)
- [ ] Calcular evolução patrimonial
- [ ] Estimar gastos do período
- [ ] Comparar: renda vs. (evolução + gastos)
- [ ] Documentar excedente não justificado

### 3. Análise de Fluxo Financeiro

#### Mapeamento de Fluxo
Para cada conta bancária:
1. **Entradas**: Origem de cada crédito (salário, transferência, depósito em espécie, DOC/TED)
2. **Saídas**: Destino de cada débito (transferência, saque, pagamento, investimento)
3. **Saldo médio**: Comportamento ao longo do tempo
4. **Picos**: Movimentações atípicas (valores, frequência, horários)

#### Identificação de Operações Atípicas (Tipologias COAF/UIF)

| Tipologia | Indicadores | Red Flag |
|-----------|-------------|----------|
| **Fracionamento (smurfing)** | Múltiplos depósitos abaixo do limiar de comunicação (R$2.000 em espécie / R$50.000 em cheques) | Mesmo dia, mesma agência, valores "redondos" |
| **Estruturação** | Operações fragmentadas para evitar registro | Padrão repetitivo, valores próximos ao limiar |
| **Triangulação** | Dinheiro passa por múltiplas contas antes do destino | Transações rápidas entre contas de terceiros |
| **Empresas de fachada** | PJ sem operação real movimenta grandes valores | Sem empregados, sem sede real, CNAE genérico |
| **Conta de passagem** | Conta que recebe e transfere rapidamente | Saldo próximo de zero, alta rotatividade |
| **Ida e volta** | Empréstimos fictícios entre pessoas/empresas | Valores idênticos em direções opostas |
| **Dólar-cabo** | Transferência informal de valores internacionais | Depósitos em espécie + transferência exterior |
| **Laranjas** | Uso de terceiros para movimentar valores | Renda incompatível, múltiplas contas |

### 4. Análise de Vínculos Financeiros

#### Mapa de Transferências
```
Investigado A --[R$ X]--> Conta Y (Empresa de fachada)
Conta Y --[R$ X-comissão]--> Conta Z (Laranja)
Conta Z --[saque em espécie]--> ???

IDENTIFICAR:
- Padrão de transferências
- Valores recorrentes
- Timing das operações
- Destino final dos recursos
```

#### Análise Societária
- Verificar participação em empresas (QSA da Receita)
- Identificar sócios em comum entre empresas investigadas
- Mapear empresas criadas no período dos fatos
- Verificar endereços comuns entre empresas
- Identificar familiares como sócios/administradores

### 5. Análise de Dados Telefônicos/Telemáticos

#### ERBs (Estações Rádio Base)
- Mapear posicionamento do investigado por horário
- Verificar presença em locais dos fatos
- Identificar padrões de deslocamento
- Cruzar com informações de depoimentos

#### Registros de Chamadas (CDR)
- Frequência de contatos entre investigados
- Contatos antes/depois de eventos relevantes
- Números não identificados recorrentes
- Alterações no padrão de comunicação

#### Dados de Aplicativos de Mensagens
- Conteúdo de mensagens (quando autorizado judicialmente)
- Metadados: datas, horários, destinatários
- Mídias compartilhadas (fotos, documentos, localizações)
- Grupos com múltiplos investigados

### 6. Formatação para o Relatório Final

#### Seção de Análise Financeira no Relatório
Estruturar assim:

```
A) RESUMO DA MOVIMENTAÇÃO FINANCEIRA
   - Período analisado
   - Contas identificadas
   - Volume total movimentado
   - Valor do excedente não justificado

B) DETALHAMENTO DAS OPERAÇÕES ATÍPICAS
   - Descrição de cada operação
   - Indicadores de atipicidade
   - Nexo causal com os fatos investigados

C) ANÁLISE DE COMPATIBILIDADE PATRIMONIAL
   - Renda declarada
   - Patrimônio identificado
   - Gastos comprovados
   - Excedente apurado

D) CONCLUSÃO DA ANÁLISE FINANCEIRA
   - Vinculação dos valores à atividade criminosa
   - Valor total do possível produto do crime
   - Sugestão de bloqueio/sequestro de bens
```

### 7. Medidas Cautelares Patrimoniais

#### Sequestro de Bens (Art. 125-132, CPP)
- Bens adquiridos com proventos da infração
- Não confundir com arresto

#### Arresto (Art. 137, CPP)
- Bens lícitos do acusado para garantir reparação
- Medida subsidiária ao sequestro

#### Bloqueio de Contas (SISBAJUD)
- Contas com valores identificados como produto do crime
- Fundamentação específica necessária

#### Perdimento de Bens (Art. 91, II, CP)
- Instrumentos do crime
- Produto do crime ou qualquer bem/valor que constitua proveito

### 8. Colaboração Premiada e Lavagem

Se houver delação/colaboração premiada:
- Verificar valor dos bens indicados vs. movimentação apurada
- Conferir consistência das informações prestadas
- Identificar ativos não declarados pelo colaborador
- Avaliar eficácia da colaboração para a investigação
