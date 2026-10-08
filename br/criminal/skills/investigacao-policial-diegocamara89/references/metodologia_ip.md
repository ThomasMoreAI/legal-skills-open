# Metodologia de Analise de IP para Investigacao Policial

Referencia tecnica para analise e requisicao de dados de enderecos IP no contexto de investigacoes de fraudes digitais.

## Sumario

1. [Conceitos Basicos: IPv4 e IPv6](#1-conceitos-basicos)
2. [NAT e Suas Implicacoes](#2-nat-e-suas-implicacoes)
3. [Protocolos de Requisicao por Tipo de IP](#3-protocolos-de-requisicao)
4. [Campos Obrigatorios em Oficios](#4-campos-obrigatorios)
5. [Fontes de IP e O Que Cada Uma Fornece](#5-fontes-de-ip)
6. [Cruzamento Multi-Fonte](#6-cruzamento-multi-fonte)
7. [Erros Comuns que Invalidam Requisicoes](#7-erros-comuns)

---

## 1. Conceitos Basicos

### IPv4
Formato tradicional com quatro grupos numericos: `187.34.56.78`

- Volume limitado de enderecos disponiveis
- Frequentemente **compartilhado** entre multiplos usuarios via NAT
- Para individualizar: precisa do IP + **porta logica** + timestamp exato

### IPv6
Formato avancado com endereco muito maior: `2801:82:1200:113e:abcd:ef12:1234:5678`

- Cada dispositivo recebe um endereco unico
- **Individualiza** o dispositivo por natureza — nao depende de porta logica
- Maior precisao na identificacao

### Quadro Comparativo

| Caracteristica | IPv4 | IPv6 |
|---------------|------|------|
| Formato | 4 grupos numericos (ex: 187.34.56.78) | 8 grupos hexadecimais (ex: 2801:82:...) |
| Individualizacao | NAO individualiza sozinho (NAT) | Individualiza por natureza |
| Porta logica | Necessaria para individualizar | Desnecessaria |
| Requisicao a operadora | 2 horarios distintos (sem porta) | 1 horario basta |
| Predominancia | Ainda muito comum | Crescente |

---

## 2. NAT e Suas Implicacoes

**NAT (Network Address Translation)**: mecanismo onde multiplos usuarios compartilham o mesmo IPv4 na internet. Cada usuario e diferenciado por uma **porta logica** (ex: `187.34.56.78:34812`).

### Por que isso importa para a investigacao

Um unico IPv4 sem porta logica pode estar sendo usado por **dezenas ou centenas** de pessoas ao mesmo tempo. Se voce requisitar a operadora "quem usava o IP 187.34.56.78 no dia X as Y horas", a operadora pode retornar uma lista com muitos titulares.

### Como resolver

1. **Solicitar porta logica ao provedor de origem** (Meta, banco, Google): "Informar o IP completo **com porta logica** dos acessos no periodo X a Y"
2. **Se nao for possivel obter a porta**: requisitar a operadora os dados em **dois horarios distintos** do mesmo IP — se o mesmo titular aparece nos dois horarios, aumenta a confianca
3. **Preferir IPv6 quando disponivel**: sempre perguntar se o provedor registrou tambem o IPv6

---

## 3. Protocolos de Requisicao por Tipo de IP

### Cenario A — IPv4 somente (sem porta)

A operadora nao consegue individualizar com certeza. Procedimento:

1. Solicitar dados do IP em **dois momentos distintos** (ex: 14:32:17 e 16:45:03 do mesmo dia)
2. No oficio, pedir: "lista de todos os assinantes conectados ao IP [endereco] nos horarios [H1] e [H2], com data, hora, minuto, segundo e fuso horario"
3. Se o mesmo titular aparece em ambos os horarios: indicio forte

### Cenario B — IPv4 + Porta logica

A porta permite individualizar o usuario dentro do NAT. Procedimento:

1. Um unico timestamp e suficiente
2. No oficio: "Identificar o assinante que utilizava o IP [endereco] na porta [porta] em [data] as [hora:min:seg] no fuso [fuso]"

### Cenario C — IPv6

O endereco ja individualiza o dispositivo. Procedimento:

1. Um unico timestamp e suficiente
2. No oficio: "Identificar o assinante titular do endereco IPv6 [endereco completo] em [data] as [hora:min:seg] no fuso [fuso]"

### Quadro Resumo

| Tipo | Exemplo | Individualiza? | Timestamps necessarios | Porta necessaria |
|------|---------|----------------|----------------------|-----------------|
| IPv4 apenas | 187.34.56.78 | NAO | 2 horarios distintos | Pedir ao provedor |
| IPv4 + porta | 187.34.56.78:34812 | SIM | 1 basta | Ja inclusa |
| IPv6 | 2801:82:1200:... | SIM | 1 basta | Desnecessaria |

---

## 4. Campos Obrigatorios em Oficios

Todo oficio de requisicao de identificacao de titular de IP **deve conter obrigatoriamente**:

| Campo | Exemplo | Motivo |
|-------|---------|--------|
| Endereco IP completo | 187.34.56.78 ou 2801:82:... | Identificar a conexao |
| Data | 15/03/2025 | Localizar no tempo |
| Hora | 14 | Precisao temporal |
| Minuto | 32 | Precisao temporal |
| Segundo | 17 | Diferenciar usuarios NAT |
| Fuso horario | America/Fortaleza (BRT, UTC-3) | Evitar ambiguidade |
| Porta logica (se IPv4) | 34812 | Individualizar no NAT |

**A ausencia de qualquer desses campos pode resultar em resposta inutilizavel da operadora.** Especialmente o fuso horario — sem ele, a operadora pode interpretar o horario como UTC e retornar o titular errado.

---

## 5. Fontes de IP e O Que Cada Uma Fornece

### WhatsApp (via Meta/Facebook)
- **Como obter**: quebra de sigilo telematico via ordem judicial
- **Dados retornados**: IPs de acesso, datas/horarios de login, tipo de dispositivo
- **Uso investigativo**: identificar o operador real da conta. Analisar recorrencia, dispositivos, geolocalizacao, horarios. Cruzar com dados bancarios e do TJRN

### Bancos (contas receptoras, apps, transferencias)
- **Como obter**: requisicao via ordem judicial as instituicoes financeiras
- **Dados retornados**: IPs de acesso a transacoes, datas, dispositivos, localizacao
- **Uso investigativo**: vincular movimentacoes a dispositivos/acessos usados em outras fraudes. Titular pode ser "laranja". Focar na comparacao de IP e dispositivo entre registros

### Tribunal de Justica / PJe / e-SAJ
- **Como obter**: requisicao direta ao TJ para logs de acesso no PJe/e-SAJ
- **Dados retornados**: IPs de todos os acessos ao processo, data/hora, usuario logado
- **Uso investigativo**: verificar quem, quando e de qual terminal acessou o processo. Critico para determinar se o terceiro e intermediario ou fraudador real
- **ALERTA**: o terceiro identificado no acesso ao processo **nem sempre e o fraudador** — pode ser intermediario. Investigar antes de concluir

### Operadoras de Telefonia
- **Como obter**: quebra de sigilo telefonico e de dados via ordem judicial
- **Dados retornados**: IMEI, dados cadastrais do titular, logs de conexao
- **Uso investigativo**: cruzar IMEI com IPs e dados bancarios para confirmar ou descartar vinculo entre titular da linha e fraude

### Email (Google, Microsoft, outros)
- **Como obter**: quebra de sigilo telematico via ordem judicial
- **Dados retornados**: IPs de criacao e acesso, telefones vinculados a conta
- **Uso investigativo**: uso suplementar em casos de engenharia social, emails comprometidos, cadastros em servicos diversos

---

## 6. Cruzamento Multi-Fonte

O cruzamento e o instrumento decisivo para individualizacao correta da autoria.

### Logica do cruzamento

```
Para cada IP obtido de uma fonte:
  1. Verificar se o mesmo IP aparece em outra fonte
  2. Comparar timestamps — proximidade temporal aumenta confianca
  3. Identificar titular via operadora
  4. Comparar titular com dados de outras fontes (banco, linha, IMEI)
  5. Se multiplas fontes convergem no mesmo nome → indicio robusto
```

### O que constitui convergencia

| Nivel | Descricao | Confianca |
|-------|-----------|-----------|
| Forte | Mesmo IP em 3+ fontes, timestamps proximos, titular confirmado | Alta |
| Moderada | Mesmo IP em 2 fontes, ou mesmo bloco/operadora com titular confirmado | Media |
| Fraca | Mesmo bloco de IP sem confirmacao de titular, ou fonte unica | Baixa |

### Precaucoes

- Nem toda coincidencia de IP e prova de autoria — pode ser WiFi publica, NAT compartilhado
- Sempre buscar **multiplas convergencias** antes de concluir
- Documentar cada convergencia com fonte, timestamp e metodo de verificacao

---

## 7. Erros Comuns que Invalidam Requisicoes

| Erro | Consequencia | Como evitar |
|------|-------------|-------------|
| Omitir fuso horario | Operadora interpreta como UTC — titular errado | Sempre informar America/Fortaleza ou UTC |
| Omitir segundos | Imprecisao — pode retornar multiplos titulares | Copiar timestamp completo do log |
| Enviar IPv4 sem porta e pedir "o titular" | Operadora retorna lista enorme ou recusa | Pedir porta ao provedor OU usar 2 horarios |
| Confundir IPv4 com IPv6 | Protocolo de requisicao errado | Contar os grupos: 4 = IPv4, 8 = IPv6 |
| Nao pedir porta logica ao provedor de origem | Perder a chance de individualizar | Sempre incluir no oficio ao Meta/banco |
| Concluir autoria com base em IP unico | Risco de atribuicao errada (NAT, WiFi publica) | Exigir convergencia de multiplas fontes |
| Nao verificar acesso ao PJe separadamente | Atribuir fraude a quem so consultou o processo | Lembrar que acesso ≠ autoria do golpe |
