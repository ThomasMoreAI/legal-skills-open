# Guia de Registros Corporativos Estaduais — FL, DE, TX

## Por que esses três estados

| Estado  | Razão de relevância para brasileiros               |
|---------|----------------------------------------------------|
| Florida | Maior concentração de brasileiros nos EUA; Miami como hub financeiro e imobiliário; grande número de LLCs e holdings de brasileiros |
| Delaware | Estado de incorporação preferido por offshores e holdings; proteção de anonimato; sem imposto estadual para não-residentes |
| Texas   | Refinarias, petróleo e gás; hub de empresas de energia; Grand Prairie, Houston com comunidade brasileira crescente |

---

## Florida — Sunbiz (Division of Corporations)

### URL e endpoints

- Base: https://search.sunbiz.org/
- Officer/Director search: `https://search.sunbiz.org/Inquiry/CorporationSearch/SearchResults?inquiryType=OfficerDirector&inquiryDirectionType=ForwardList&searchNameOrder=<NOME>&activeOnly=true`
- Entity search: `https://search.sunbiz.org/Inquiry/CorporationSearch/SearchResults?inquiryType=EntityName&inquiryDirectionType=ForwardList&searchNameOrder=<NOME>&activeOnly=false`

### O que a Sunbiz divulga

- Nome da entidade, tipo (Corp, LLC, LP, LLLP, NP etc.)
- Número do documento (ex: `P19000012345`) → usar como `source_id`
- Data de registro e data da última atualização anual
- Status: Active, Inactive, Dissolved
- Endereço principal e endereço para correspondência
- Registered Agent (nome e endereço)
- Officers e Directors com cargo e endereço
- Annual Reports (histórico de alterações de officers)

### Limitações

- Busca por officer retorna apenas resultados exatos por sobrenome
- Nomes com acentos (Álvaro, Águeda) podem estar sem acento no sistema
- Empresas inativas (dissolved) ainda aparecem — verificar status
- Annual Reports são a melhor fonte para timeline de mudanças de officers

### Formato do document number

- `P` = Profit corporation
- `N` = Non-profit
- `L` = LLC
- `A` = Foreign corporation (registrada em outro estado mas operando em FL)

---

## Delaware — Division of Corporations

### URL e endpoints

- Base: https://icis.corp.delaware.gov/
- Entity search: `https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx`
- Entity detail: `https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx` (via formulário POST)

### O que Delaware divulga (muito pouco por design)

Delaware é deliberadamente opaco. O registro público mostra apenas:

- Nome da entidade
- Tipo (Corporation, LLC, LP, Statutory Trust etc.)
- Data de incorporação
- Status (Good Standing, Void etc.)
- Registered Agent (quase sempre escritório de serviço: CT Corporation, Corporation Trust Co., National Registered Agents)
- Número do arquivo (*file number*)

**Delaware NÃO divulga:**
- Officers ou diretores
- Shareholders ou membros da LLC
- Beneficial owners (exceto via FinCEN BOI pós-2024, não público)
- Endereço operacional da empresa

### Como investigar além do registro DE

Para empresas incorporadas em Delaware mas operando em FL ou TX:
1. Buscar na Sunbiz como "foreign corporation" registrada em FL
2. Buscar no SOS/TX como entidade estrangeira
3. Verificar EDGAR (SEC) se a empresa emitiu securities
4. Verificar LDA/FARA se fez lobby

### Formato do file number

Número sequencial de 7 dígitos (ex: `7654321`). Sem prefixo de tipo.

---

## Texas — Secretary of State

### URL e endpoints

- SOS business search: https://www.sos.state.tx.us/corp/businesssearch.shtml
- Franchise Tax / Comptroller: https://mycpa.cpa.state.tx.us/coa/

### O que Texas divulga

**Via SOS (incorporações):**
- Nome legal da entidade
- File number → `source_id`
- Tipo (For-Profit, LLC, LP, Nonprofit etc.)
- Status (In Existence, Forfeited, Dissolved)
- Data de incorporação
- Registered Agent
- Endereço registrado

**Via Comptroller (franchise tax):**
- Taxpayer number → alternativo como `source_id`
- Status de franchise tax (good standing = direito de operar)
- Mailing address
- SIC code (setor econômico)

### O que Texas NÃO divulga

- Officers de LLCs (LLCs em TX não precisam listar membros/managers no registro público)
- Beneficial owners

### Setor de energia em TX

Para investigações de empresas de petróleo e gás no Texas:
- Railroad Commission of Texas tem base separada: https://www.rrc.texas.gov/
- Cobre operadores de poço, transporte e refinamento
- Permite busca por nome de empresa ou operador

---

## Comparação rápida

| Aspecto              | Florida         | Delaware       | Texas          |
|----------------------|-----------------|----------------|----------------|
| Officers públicos?   | Sim             | Não            | Parcialmente   |
| Endereço público?    | Sim             | Apenas agente  | Sim            |
| Busca por officer?   | Sim (Sunbiz)    | Não            | Não            |
| Anonimato possível?  | Baixo           | Alto           | Médio          |
| Custo de registro    | USD 138 (corp)  | USD 89 (corp)  | USD 300 (corp) |
| Tempo para registro  | 1-3 dias        | 1 hora (online)| 2-3 dias       |

---

## Dica investigativa: cruzar estados

Quando uma empresa aparece em Delaware mas com operações reais, ela precisa
se registrar como **foreign entity** no estado onde opera. Sunbiz mostra
"Foreign Profit Corporation" e inclui o estado de incorporação (Delaware).
Isso permite vincular um nome de empresa DE a dados de officers da FL.
