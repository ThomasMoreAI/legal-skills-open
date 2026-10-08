# Expansao de Rede — Metodologia de 7 Passos

Metodologia para expandir a rede de suspeitos a partir de um dado inicial (chave Pix, telefone, email, IMEI). Cada dado novo gera mais dados — como puxar um fio que revela toda a trama.

## Sumario

1. [Passo 1 — Chave Pix Destino](#passo-1)
2. [Passo 2 — Expansao por Email](#passo-2)
3. [Passo 3 — Analise de Telefones](#passo-3)
4. [Passo 4 — Expansao por IMEI](#passo-4)
5. [Passo 5 — Filtragem de Linhas](#passo-5)
6. [Passo 6 — Verificacao das Linhas Filtradas](#passo-6)
7. [Passo 7 — Cruzamento de Dispositivos](#passo-7)

---

## Fluxo Visual

```
Chave Pix destino
    |
    v
Todas as chaves Pix da mesma conta
    |
    v
Se chave = email --> requisitar logs ao provedor (Google/Microsoft)
    |
    v
Telefones obtidos (da chave Pix, do email, do banco)
    |
    v
Para cada telefone --> requisitar IMEI a operadora
    |
    v
Para cada IMEI --> encontrar TODAS as linhas que usaram esse aparelho
    |
    v
Filtrar: pos-pago + linha antiga = maior credibilidade
    |
    v
Cruzar modelo do aparelho entre fontes (banco, email, operadora)
```

---

## Passo 1 — Chave Pix Destino

**Ponto de partida**: a chave Pix para onde o dinheiro foi transferido.

Independente do tipo de chave (telefone, email, CPF, chave aleatoria), o primeiro passo e:

1. Requisitar ao banco (via BACENJUD ou oficio judicial) **todas as outras chaves Pix vinculadas a mesma conta**
2. Isso revela se ha telefones, emails ou CPFs adicionais vinculados

**O que requisitar no oficio ao banco**:
- Dados cadastrais do titular da conta
- Todas as chaves Pix ativas e inativas vinculadas
- Dados de abertura da conta (data, IP, dispositivo, selfie biometrica)
- Extrato do periodo investigado

---

## Passo 2 — Expansao por Email

**Quando aplicar**: se uma das chaves Pix e um endereco de email, ou se um email foi usado na fraude (contato com vitima, cadastro em plataforma).

1. Identificar o provedor do email (Gmail = Google, Outlook/Hotmail = Microsoft, etc.)
2. Requisitar via oficio judicial (quebra de sigilo telematico):
   - IPs de criacao da conta
   - IPs de acesso no periodo investigado
   - Telefone(s) vinculado(s) a conta de email
   - Dados cadastrais informados na criacao
   - Dispositivos que acessaram a conta (modelo, SO)
3. O telefone vinculado ao email e especialmente valioso — alimenta o Passo 3

---

## Passo 3 — Analise de Telefones

**Quando aplicar**: para cada numero de telefone obtido (via chave Pix, email, contato com vitima, ou qualquer outra fonte).

1. Consultar os dados cadastrais do titular da linha junto a operadora
2. Verificar se a linha e **pre-paga** ou **pos-paga** (pos-paga tem cadastro mais confiavel)
3. Requisitar o(s) **IMEI(s)** vinculado(s) a essa linha no periodo investigado

**O que requisitar no oficio a operadora**:
- Dados cadastrais atuais do titular
- Historico de IMEIs utilizados na linha no periodo [data inicio] a [data fim]
- Tipo de plano (pre/pos)
- Data de ativacao da linha

---

## Passo 4 — Expansao por IMEI

**Logica**: um aparelho celular (IMEI) pode ter sido usado com **multiplas linhas** (chips). Encontrar todas as linhas que usaram o mesmo aparelho pode revelar outros numeros do suspeito.

1. Para cada IMEI obtido no Passo 3, requisitar a operadora:
   - **Todas as linhas telefonicas** que utilizaram esse IMEI no periodo investigado
   - Dados cadastrais de cada titular

2. Se o IMEI apareceu em mais de uma operadora (ex: Claro e Vivo), requisitar a ambas

3. Resultado esperado: uma lista de linhas que usaram o mesmo aparelho — se ha linhas em nomes diferentes usando o mesmo IMEI, isso sugere uso de "laranjas" ou multiplas identidades

---

## Passo 5 — Filtragem de Linhas

**Problema**: a expansao por IMEI pode gerar uma lista grande de linhas. Nem todas sao igualmente relevantes.

**Criterios de priorizacao** (da mais para a menos credivel):

| Criterio | Por que priorizar |
|----------|-------------------|
| Linha **pos-paga** | Cadastro verificado com CPF e endereco — vinculo mais forte com pessoa real |
| Linha **mais antiga** em uso | Menos provavel de ser "laranja" descartavel — indica uso continuado |
| Linha com **mesmo titular** que aparece em outra fonte | Convergencia de nomes entre operadora e banco reforça vinculo |
| Linha **pre-paga recente** | Menor credibilidade — pode ser chip descartavel, prioridade mais baixa |

**Acao**: selecionar as linhas de maior prioridade para aprofundamento no Passo 6.

---

## Passo 6 — Verificacao das Linhas Filtradas

Para cada linha selecionada no Passo 5:

### 6.1 — Dados cadastrais atualizados
Emitir novo oficio a operadora pedindo dados cadastrais atuais (podem ter mudado desde a ultima consulta).

### 6.2 — Chaves Pix vinculadas
Verificar se o numero de telefone da linha filtrada esta registrado como chave Pix em alguma conta bancaria. Se sim:
- Essa conta aparece em **outros BOs ou investigacoes**?
- Isso reforça o corpo probatorio (reincidencia ou padrao)

### 6.3 — Consulta a base de dados policial
Verificar se o titular da linha tem registros em:
- INFOSEG
- Base estadual de ocorrencias
- Outras investigacoes em andamento

### 6.4 — Cruzamento com IPs
Se ja temos IPs do WhatsApp/banco/TJRN:
- Requisitar a operadora quem era o titular do IP no horario do crime
- Verificar se o resultado bate com o titular da linha filtrada

---

## Passo 7 — Cruzamento de Dispositivos

**Objetivo final**: verificar se o **modelo do aparelho** e consistente entre todas as fontes. Se o banco diz que o acesso foi feito de um "Samsung Galaxy A54", o Google diz que o email foi acessado de um "Samsung Galaxy A54", e a operadora diz que o IMEI corresponde a um "Samsung Galaxy A54" — isso e convergencia forte.

### Fontes de modelo de dispositivo

| Fonte | Como obtem o modelo |
|-------|-------------------|
| Banco | User-agent do app movel / dados do dispositivo na abertura da conta |
| Google/Microsoft | User-agent dos acessos ao email |
| Operadora | IMEI → TAC (primeiros 8 digitos) → modelo do aparelho |
| Meta/WhatsApp | Tipo de dispositivo nos logs de acesso |

### O que comparar

1. O modelo informado por cada fonte e **compativel**? (mesmo fabricante, mesmo modelo)
2. O IMEI bate com o modelo informado?
3. Se ha inconsistencia (ex: banco diz iPhone, operadora diz Samsung), investigar:
   - Pode ser uso de multiplos aparelhos
   - Pode ser fraude de IMEI
   - Pode indicar que nao e o mesmo individuo

---

## Quando Parar a Expansao

A expansao deve parar quando:
- As novas linhas/contas encontradas ja sao conhecidas (circularidade)
- O custo operacional de novas requisicoes supera o beneficio
- A convergencia de autoria ja esta estabelecida por 3+ fontes independentes
- O delegado orientou o encerramento da fase investigativa
