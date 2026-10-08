---
name: persecucao-patrimonial-twalkingse
title: Persecução Patrimonial de Criptoativos — Brasil
description: Orienta estratégias jurídicas e técnicas para localização, apreensão, custódia  e alienação de criptoativos no contexto brasileiro. Use quando o contexto  envolver busca e apreensão de cripto, bloqueio em exchange, cooperação com  Receita Federal (IN 1.888/2019), Sisbajud, Marco Legal dos Criptoativos  (Lei 14.478/2022), alienação antecipada (Lei 9.613/1998), cadeia de custódia  digital, requisição judicial a exchanges, blacklist de stablecoins, apreensão  de hardware wallet/seed phrase, ou destinação de ativos apreendidos.
author: TWalkingSE
author_url: https://github.com/TWalkingSE/crypto-investigator/tree/main/.github/skills/persecucao-patrimonial
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: br
practice: general
language: pt
---

# Persecução Patrimonial de Criptoativos — Brasil

## ⚠️ Salvaguarda Permanente

Esta orientação é **estritamente educacional** e baseada em legislação e práticas documentadas. **Não constitui assessoria jurídica**. Para casos concretos, recomenda-se acompanhamento de advogado especializado e perito em criptoativos.

## Fluxo Completo de Persecução Patrimonial

```
┌─────────────────────────────────────────────────────────────┐
│                      LOCALIZAÇÃO                            │
├─────────────────────────────────────────────────────────────┤
│ • Receita Federal (IN 1.888/2019) — exchanges reportam      │
│ • Requisição judicial a exchanges brasileiras               │
│ • Sisbajud — algumas exchanges integradas                   │
│ • Análise on-chain a partir de endereço conhecido           │
│ • Busca presencial: dispositivos, seeds, hardware wallets   │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│             CONSTRIÇÃO (Bloqueio / Apreensão)               │
├─────────────────────────────────────────────────────────────┤
│ • Bloqueio em exchange (ordem judicial)                     │
│ • Blacklist de stablecoin (Tether/Circle — coop. int.)      │
│ • Apreensão direta para carteira institucional              │
│ • Apreensão de seed phrases e dispositivos                  │
│                                                             │
│ ⚠️ DOCUMENTAR: hash, endereços, valor exato, timestamp      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                       CUSTÓDIA                              │
├─────────────────────────────────────────────────────────────┤
│ • Carteira institucional (cold wallet do órgão)             │
│ • Exchange custodiante (por determinação judicial)          │
│ • Depositário judicial                                      │
│                                                             │
│ ⚠️ Capturar: endereço de custódia, hash de transferência,   │
│    saldo no momento da apreensão, capturas de tela          │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      DESTINAÇÃO                             │
├─────────────────────────────────────────────────────────────┤
│ • Alienação antecipada (Lei 9.613/1998, art. 4º-A)          │
│   — mitiga volatilidade                                     │
│ • Manutenção em custódia até decisão final                  │
│ • Restituição (absolvição/liberação)                        │
└─────────────────────────────────────────────────────────────┘
```

## Localização de Ativos

### Via Receita Federal — IN RFB 1.888/2019

A IN 1.888/2019 obriga:
- Exchanges brasileiras a reportar operações mensalmente
- Pessoas físicas e jurídicas a declarar operações acima de R$ 30.000/mês (quando a exchange é estrangeira ou peer-to-peer)

**Uso investigativo:**
- Requisição formal à Receita Federal com base legal (processo criminal, lavagem, etc.)
- Cruzar CPF/CNPJ do investigado
- Obter lista de operações, exchanges utilizadas, valores e datas

### Via Exchanges Brasileiras

Exchanges registradas no Brasil (Mercado Bitcoin, Foxbit, Binance Brasil, NovaDAX, etc.) devem responder a requisições judiciais.

**Dados solicitáveis:**
- Cadastro completo (nome, CPF, endereço, telefone)
- KYC completo (documentos, foto, comprovante de residência)
- Histórico de operações
- Endereços de depósito e saque
- IPs de acesso
- Saldos atuais
- Métodos de pagamento vinculados (PIX, TED, cartão)

**Base legal:**
- CPP arts. 13, 240 e seguintes
- Marco Civil da Internet (Lei 12.965/2014)
- Lei 14.478/2022 (Marco Legal dos Criptoativos)

### Via Sisbajud

O Sistema de Busca de Ativos do Poder Judiciário (Sisbajud) já integra algumas exchanges brasileiras. Permite bloqueio direto via ordem judicial, similar ao bloqueio em bancos.

**Limitações:**
- Nem todas as exchanges estão integradas (verificar atualização)
- Não alcança exchanges estrangeiras
- Não alcança carteiras pessoais (non-custodial)

### Via Análise On-Chain

Se já possui endereço do investigado:
1. Rastrear para onde os fundos foram (skills `/account-tracing`, `/utxo-tracing`)
2. Identificar exchanges de destino
3. Solicitar dados da exchange de destino
4. Identificar hot wallets e cold wallets de exchanges conhecidas

### Via Busca Presencial

Em busca domiciliar ou empresarial, procurar:
- **Hardware wallets**: Ledger (Nano S/X), Trezor (One/Model T), Coldcard, BitBox
- **Seed phrases**: anotações em papel, placas de metal (Cryptosteel, Billfodl), cartões
- **Software wallets**: arquivos em computador (wallet.dat, keystore)
- **Dispositivos**: celulares com apps (Trust Wallet, MetaMask, Exodus)
- **Pendrives e HDs**: podem conter backups de seeds
- **Documentação**: e-mails com confirmações, extratos, prints de carteiras

**⚠️ Cuidados:**
- Não tentar acessar carteiras sem perícia adequada (risco de autodestruição, PINs bloqueantes)
- Documentar cada item fotograficamente antes de manipular
- Cadeia de custódia rigorosa

## Constrição

### Bloqueio em Exchange

Ordem judicial determinando congelamento da conta. A exchange bloqueia:
- Movimentação de saldos (fiat e cripto)
- Saques
- Transferências internas

**Tempo:** imediato após recebimento da ordem. Algumas exchanges exigem notificação via canal oficial (API de compliance, e-mail específico).

### Blacklist de Stablecoins

Tether (USDT) e Circle (USDC) podem adicionar endereços a blacklists on-chain, congelando efetivamente os fundos em tokens. Já foi usado em casos reais.

**Procedimento:**
1. Cooperação internacional (via MLAT ou canal informal de compliance)
2. Tether: tether.to — canal de compliance
3. Circle: circle.com — canal de compliance
4. Requer documentação sólida (ordem judicial, caso criminal)

**Como verificar se endereço está congelado:**
- No Etherscan, ir ao contrato do token (USDT: `0xdAC17F958D2ee523a2206206994597C13D831ec7`)
- Aba "Read Contract" → função `isBlacklisted(address)`

### Apreensão Direta (Transferência para Carteira Institucional)

Quando o Estado consegue acessar a chave privada (via seed apreendida, via cooperação do investigado, via decisão que obriga exchange a entregar):

1. Criar carteira institucional (cold wallet, preferencialmente hardware wallet dedicada)
2. Transferir TODOS os ativos do endereço apreendido
3. **Documentar rigorosamente:**
   - Endereço de origem
   - Endereço de destino (carteira institucional)
   - Hash de cada transação
   - Valor exato (em cripto e em valor estimado BRL na data)
   - Timestamp
   - Capturas de tela antes e depois da transferência
4. Gerar laudo pericial descrevendo o procedimento

**⚠️ CUIDADOS:**
- NUNCA expor chave privada publicamente ou em canais não-seguros
- Usar equipamento air-gapped quando possível
- Múltiplas testemunhas/peritos
- Gravação em vídeo do procedimento

### Apreensão de Seeds/Chaves

Seed phrase apreendida deve ser:
- Fotografada e documentada em laudo
- Armazenada em cofre com acesso restrito
- Nunca digitada em dispositivo comum (risco de malware/keylogger)
- Reconstruída em carteira institucional para transferência

## Custódia

### Opções de Custódia

| Opção | Vantagem | Desvantagem |
|---|---|---|
| **Cold wallet institucional** | Controle total, offline | Requer perícia técnica do órgão |
| **Exchange custodiante** | Gestão profissional, seguro | Dependência de terceiro, risco de falência/hack |
| **Depositário judicial especializado** | Expertise técnica | Custo, escolha criteriosa |
| **Multi-sig institucional** | Múltiplos aprovadores, segurança máxima | Complexidade operacional |

### Documentação Mínima

Para cada ativo em custódia, registrar:
- Tipo de ativo e quantidade
- Valor estimado em BRL (atualizado periodicamente)
- Endereço de custódia
- Hash da transação que depositou na custódia
- Responsável pela chave privada
- Local físico do dispositivo (se hardware wallet)
- Backups da seed (se houver) e seu local

## Destinação

### Alienação Antecipada (Lei 9.613/1998, art. 4º-A)

**Quando aplicar:**
- Risco de desvalorização (cripto é volátil)
- Custos de manutenção (hardware wallet, depositário)
- Fundamentação técnica no pedido

**Procedimento:**
1. Pedido do MP ou autoridade ao juízo competente
2. Avaliação por perito
3. Decisão judicial autorizando
4. Venda em plataforma autorizada (leilão público, exchange via ordem judicial)
5. Valor em BRL depositado em conta judicial
6. Laudo de alienação

**Benefício:** Se houver condenação e perdimento, o valor já está preservado em BRL sem sofrer com volatilidade.

### Manutenção em Custódia

Para ativos específicos (NFTs raros, moedas de nicho sem liquidez) ou quando a alienação antecipada for contra-indicada.

### Restituição

Em caso de absolvição ou determinação judicial:
- Transferência de volta ao titular
- Ou conversão em BRL se foi alienado

## Referências Legais Essenciais

| Norma | Escopo |
|---|---|
| **Lei 14.478/2022** | Marco Legal dos Criptoativos — VASPs e supervisão |
| **IN RFB 1.888/2019** | Obrigação de declaração de operações com cripto |
| **Resolução BCB 314/2023** | Regulamentação de prestadoras de serviços de ativos virtuais |
| **Lei 9.613/1998** | Lavagem de dinheiro — alienação antecipada (art. 4º-A) |
| **Lei 12.850/2013** | Organizações criminosas — meios de prova |
| **Enunciados 162 e 209 CJF** | Persecução patrimonial de ativos digitais |
| **CPP arts. 240-250** | Busca e apreensão |
| **Marco Civil da Internet (12.965/2014)** | Requisição de dados a provedores |
| **LGPD (13.709/2018)** | Tratamento de dados pessoais na investigação |

## Cooperação Internacional

Investigações cross-border frequentemente envolvem:
- **MLAT** (Tratado de Assistência Jurídica Mútua) — via autoridade central (MJ)
- **Canal Interpol** — para rastreamento e localização
- **Europol** — cooperação UE
- **Cooperação com FBI, IRS-CI** — EUA têm jurisdição sobre USDT, USDC, exchanges americanas
- **DOJ Cryptocurrency Seizure Guide** — guia público

## Integração com outros skills

- Localizar endereços do investigado: `/utxo-tracing` ou `/account-tracing`
- Rastrear cross-chain (ofuscação comum em casos complexos): `/cross-chain-tracing`
- Identificar padrão de lavagem: `/on-chain-patterns`
- Identificar esquema (ponzi, rug pull): `/scam-patterns`
- Gerar laudo/relatório: `/investigation-report`
