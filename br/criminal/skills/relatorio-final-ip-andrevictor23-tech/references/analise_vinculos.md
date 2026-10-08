# Análise de Vínculos em Investigações Policiais

## Conceito

Análise de vínculos é a técnica investigativa que mapeia e visualiza relações entre entidades (pessoas, empresas, contas, telefones, endereços, veículos) para identificar padrões, hierarquias e conexões ocultas em organizações criminosas.

## Tipos de Vínculos a Identificar

### 1. Vínculos Pessoais
- **Parentesco**: Cônjuges, filhos, pais, irmãos, primos
- **Afinidade**: Amizade, relacionamento amoroso, vizinhança
- **Profissional**: Empregado/empregador, sócio, colega de trabalho
- **Criminal**: Coautoria anterior, comparsas, mentor/aprendiz

### 2. Vínculos Empresariais
- **Societários**: Sócios em comum entre empresas
- **Administração**: Mesmo administrador/representante legal
- **Endereço**: Mesmo endereço entre empresas diferentes
- **Contabilidade**: Mesmo contador entre empresas
- **Fornecimento**: Relações comerciais entre empresas investigadas
- **Sucessão**: Empresas abertas para substituir outras encerradas

### 3. Vínculos Financeiros
- **Transferências bancárias**: Fluxo de valores entre contas
- **PIX recorrente**: Pagamentos regulares entre investigados
- **Empréstimos**: Mútuos entre envolvidos
- **Avalistas/fiadores**: Garantias cruzadas
- **Investimentos comuns**: Aplicações financeiras compartilhadas

### 4. Vínculos de Comunicação
- **Telefone**: Frequência e padrão de ligações/mensagens
- **E-mail**: Comunicações entre investigados
- **Redes sociais**: Conexões, grupos, interações
- **Aplicativos**: WhatsApp, Telegram, Signal

### 5. Vínculos Geográficos
- **Endereços comuns**: Residencial, comercial, correspondência
- **ERBs coincidentes**: Mesma localização em mesmos horários
- **Viagens conjuntas**: Registros de voos, hospedagem, pedágios
- **Câmeras de segurança**: Flagrantes de encontros

## Metodologia de Construção do Mapa de Vínculos

### Etapa 1: Coleta de Entidades
```
Para cada entidade, registrar:
PESSOAS:
  - Nome completo, CPF, data de nascimento
  - Endereços (residencial, comercial)
  - Telefones
  - Empresas vinculadas
  - Contas bancárias
  - Veículos
  - Antecedentes

EMPRESAS:
  - Razão social, CNPJ, CNAE
  - Endereço sede
  - Sócios e administradores (QSA)
  - Contas bancárias
  - Faturamento declarado
  - Empregados registrados
  - Data de abertura/encerramento

CONTAS BANCÁRIAS:
  - Banco, agência, conta
  - Titular (CPF/CNPJ)
  - Data de abertura
  - Volume de movimentação
  - Operações atípicas

TELEFONES:
  - Número, operadora
  - Titular
  - IMEI vinculado
  - Período de uso
```

### Etapa 2: Mapeamento de Conexões
```
Para cada par de entidades, verificar:
- Existe conexão direta?
- Qual o tipo de conexão?
- Qual a força da conexão (frequência, volume)?
- Qual o período da conexão?
- A conexão é relevante para a investigação?
```

### Etapa 3: Construção da Matriz de Vínculos
```
| DE → PARA | Pessoa A | Pessoa B | Empresa X | Conta Y |
|-----------|----------|----------|-----------|---------|
| Pessoa A  | —        | Sócio    | Sócio     | Titular |
| Pessoa B  | Sócio    | —        | —         | Procurador |
| Empresa X | Sócio A  | —        | —         | Titular |
| Conta Y   | —        | Procurador| Titular  | —       |
```

### Etapa 4: Identificação de Padrões

**Padrões de Hub (Concentrador)**:
- Uma pessoa/empresa com muitas conexões = possível líder/organizador
- Uma conta com muitas origens/destinos = possível conta de passagem

**Padrões de Cadeia**:
- Sequência de transferências A → B → C → D = possível lavagem
- Cadeia de empresas: investigar interpostas pessoas

**Padrões de Cluster (Grupo)**:
- Grupo de pessoas/empresas fortemente interconectado
- Pode indicar núcleo de organização criminosa
- Verificar se há hierarquia interna

**Padrões Temporais**:
- Conexões que surgem em período específico = ação coordenada
- Conexões que cessam após evento específico = tentativa de se distanciar
- Ativação de novas contas/empresas = adaptação do modus operandi

### Etapa 5: Hierarquização

Identificar papéis na estrutura:
1. **Líder/Organizador**: Maior concentração de vínculos estratégicos
2. **Operadores financeiros**: Controlam fluxo de recursos
3. **Laranjas**: Cederam documentos/contas, vínculos passivos
4. **Executores**: Realizaram atos materiais
5. **Facilitadores**: Forneceram meios, informações ou cobertura

## Apresentação no Relatório Final

### Descrição Textual de Vínculos

No relatório, apresentar os vínculos de forma textual estruturada:

```
ANÁLISE DE VÍNCULOS IDENTIFICADOS:

1. VÍNCULO ENTRE [PESSOA A] E [PESSOA B]:
   - Natureza: Societária (sócios na empresa X Ltda, CNPJ XX)
   - Período: [data de constituição da sociedade]
   - Relevância: Ambos participaram das decisões que geraram [crime]
   - Prova: [folhas dos autos]

2. VÍNCULO FINANCEIRO ENTRE [PESSOA A] E [CONTA Y]:
   - Natureza: Transferências bancárias reiteradas
   - Volume: R$ XX.XXX,XX no período de [data] a [data]
   - Padrão: Valores fracionados, sempre abaixo de R$ [limiar]
   - Relevância: Compatível com tipologia de [smurfing/triangulação]
   - Prova: Extratos bancários às fls. [XX-XX]
```

### Tabela Resumo de Vínculos

Incluir tabela consolidada no relatório:

```
| Entidade 1 | Entidade 2 | Tipo de Vínculo | Período | Relevância | Prova (fls.) |
|-----------|-----------|----------------|---------|------------|-------------|
| João Silva | Maria Santos | Societário (Empresa X) | 2020-2024 | Alta | 45-48 |
| João Silva | Conta 12345-6 | Titular | 2021-atual | Média | 56 |
| Empresa X | Empresa Y | Mesmo endereço | 2022-2023 | Alta | 67-68 |
```

## Fontes para Identificação de Vínculos

| Fonte | Dados Obtidos | Como Acessar |
|-------|---------------|-------------|
| Receita Federal (CNPJ) | QSA, endereço, CNAE, situação | Consulta pública ou ofício |
| JUCESP/Juntas Comerciais | Contratos sociais, alterações | Certidão ou sistema |
| Cartórios de Imóveis | Propriedade, ônus reais | Ofício ao cartório |
| DETRAN | Veículos, endereço | Sistema INFOSEG/SINESP |
| Operadoras de telefonia | Titularidade, CDR | Ordem judicial |
| Bancos/instituições financeiras | Contas, movimentação | Ordem judicial (sigilo) |
| COAF/UIF | Operações comunicadas | RIF via delegacia/MP |
| Redes sociais | Conexões, grupos, perfis | Análise de fontes abertas |
| SISCOAF | Comunicações de operações | Acesso institucional |
| CCS (Cadastro de Clientes do SFN) | Todas as contas do investigado | Ordem judicial via Bacen |

## Cuidados na Análise de Vínculos

1. **Nem todo vínculo é criminal**: Relações legítimas devem ser descartadas ou contextualizadas
2. **Proporcionalidade**: Mapear apenas vínculos relevantes para a investigação
3. **Fundamentação**: Todo vínculo apontado deve estar provado nos autos
4. **Cadeia de custódia**: Dados digitais devem ter origem documentada
5. **Atualização**: Verificar se vínculos são atuais ou históricos
6. **Dupla verificação**: Cruzar fontes para confirmar vínculos
