# 10: Formação Válida do Contrato Eletrônico (Clickwrap, Aceite, Versionamento)

> Sem prova de aceite, não tem contrato. Esta referência define **o padrão ouro de aceite eletrônico** no Brasil, baseado em jurisprudência STJ e prática consolidada de mercado.

## Modos de aceite: do mais forte ao mais fraco

| Modo | Definição | Validade no BR |
|---|---|---|
| **Scroll-wrap** | Texto integral rolável + botão "Aceito" só habilita após scroll até o fim | **Mais forte.** Ideal pra serviço de alto risco (financeiro, saúde). |
| **Clickwrap** | Checkbox **vazio** ("Li e concordo com os Termos") + botão "Criar conta" | **Padrão ouro do mercado.** Aceite válido, equivale a assinatura. |
| **Sign-in-wrap** | "Ao clicar em Entrar você concorda com os Termos" colado no botão | **Aceitável** pra fluxos OAuth. Mais frágil que clickwrap. |
| **Browse-wrap** | Link no rodapé "ao usar o site você aceita", sem ato afirmativo | **Frágil.** Sem registro de aceite, cláusulas restritivas dificilmente são opostas em juízo. **EVITAR.** |

### Por que browse-wrap é frágil

- **CDC art. 46:** contrato não obriga consumidor que não teve oportunidade de tomar conhecimento prévio do conteúdo.
- **LGPD art. 8º:** consentimento exige manifestação **inequívoca**.
- Levantamentos americanos: browse-wrap falha em juízo ~86% das vezes. No Brasil, com CDC + LGPD, pior ainda.

### Padrão recomendado

```
[ ] Li e concordo com os Termos de Uso e com a Política de Privacidade.

         [ Criar conta ]    ← desabilitado enquanto checkbox vazio
```

- Checkbox **vazio por padrão** (consentimento ativo, **nunca pré-marcado**).
- Texto curto resumindo + link no próprio texto pra documento integral.
- Botão de submit desabilitado enquanto desmarcado.
- **Duas caixas separadas** pra Termos e Privacidade quando a base legal for consentimento.
- Pra serviços de alto risco, usar **scroll-wrap** (só habilita após scroll completo).

## Prova do aceite: schema canônico

> Implementação técnica completa em `templates/endpoints-direitos/consent-log-schema.sql` (estendida abaixo pra Termos).

```sql
CREATE TABLE IF NOT EXISTS tos_acceptance (
    id              bigserial PRIMARY KEY,
    user_id         uuid REFERENCES users(id) ON DELETE SET NULL,

    document_type   text NOT NULL,    -- 'terms_of_use' | 'privacy_policy' | 'cookies'
    document_version text NOT NULL,   -- ex: '2026-05-24' ou 'v3.2.0'
    document_hash   text NOT NULL,    -- SHA-256 do PDF/HTML imutável arquivado

    accepted_at     timestamptz NOT NULL DEFAULT now(),
    ip_truncated    inet,             -- /24 IPv4 ou /48 IPv6 (LGPD, minimização)
    user_agent      text,
    acceptance_method text NOT NULL,  -- 'clickwrap' | 'scrollwrap' | 'reaccept_modal' | 'sign_in_wrap'

    context         jsonb             -- {flow: 'signup', locale: 'pt-BR', ...}
);

CREATE INDEX IF NOT EXISTS tos_acceptance_user_idx
    ON tos_acceptance (user_id, document_type, accepted_at DESC);
```

### Por que o **hash** é essencial

Sem ele, em disputa o titular alega que aceitou outro texto. O hash do documento aceito garante "**essa exata versão foi vista**".

**Como gerar:**
1. Cada versão dos Termos é arquivada como arquivo imutável (Markdown ou HTML estático).
2. Hash SHA-256 do conteúdo é calculado e armazenado no `tos_acceptance.document_hash`.
3. Versão recebe URL versionada permanente (`/legal/termos/v3.2`).
4. Arquivo é commitado em repo (Git já dá hash de blob, pode usar esse).

### IP truncado: minimização (LGPD)

```python
def truncate_ip(ip: str) -> str:
    if ':' in ip:  # IPv6
        return ':'.join(ip.split(':')[:3]) + '::/48'
    parts = ip.split('.')
    return '.'.join(parts[:3]) + '.0/24'
```

Equilibra auditoria com necessidade. Guardar IP completo é excessivo pra finalidade.

### Retenção

- **Durante toda a relação contratual + 5 anos** após o término (CDC art. 27, prescrição).
- Pra contratos B2B com cláusula de auditoria mais longa, alinhar com prazo contratual.

## Versionamento

### Esquema de versão

| Esquema | Quando usar |
|---|---|
| **Data ISO** (`2026-05-24`) | Documentos voltados a leigos (B2C). Padrão Nubank, iFood, ML. |
| **Semver** (`v3.2.0`) | SaaS B2B com versionamento técnico (RD Station, Hotmart Developers). |

Default recomendado: **data ISO** pra B2C; **semver** quando o app tem API pública versionada.

### Re-aceite obrigatório vs tácito

| Mudança | Re-aceite? |
|---|---|
| Preço, escopo do serviço, política de cancelamento, foro, limitação de responsabilidade, base legal LGPD | **Explícito** (modal blocker antes de continuar usando) |
| Correção de typo, link atualizado, esclarecimento sem alterar direitos | **Tácito** por uso continuado (se notificado com antecedência) |

### Histórico imutável

Armazenar **toda versão que esteve em produção**:
- S3 com Object Lock, OU
- Tabela append-only no DB, OU
- Repo Git com tags por versão (mais leve, dá grátis hash e diff)

Prazo mínimo: 5 anos após sair de vigor. Idealmente enquanto houver consent_log apontando pra ela.

## Comunicação de mudanças: padrão de mercado

Combinação que Nubank, iFood, Mercado Livre seguem (variações):

1. **E-mail com 30 dias de antecedência**, descreve o que muda em linguagem simples ("o que mudou e por quê") + link pro novo texto integral + link pro diff.
2. **In-app banner** persistente nas próximas 2-3 sessões antes da data de vigência.
3. **Na data de vigência**, modal blocker que exige novo aceite (pra mudança material). Sem aceite, usuário consegue ler/exportar dados mas não consegue fazer nova transação, preserva direito de portabilidade da LGPD.
4. **Comunicado público** no blog/centro de ajuda, indexável.

Pra mudanças não-materiais: e-mail informativo + banner discreto + uso continuado = aceite.

## Termos em duas camadas (resumo + detalhe)

Mesmo padrão da Política de Privacidade. Vale a pena também pros Termos.

- **Camada 1: Resumo numa página:** "O que esse serviço faz", "O que você pode e não pode", "Como cancelar", "Como falar com a gente". **Sem força jurídica isolada**, reduz drasticamente "ninguém lê".
- **Camada 2: Documento jurídico integral.**

Referências boas: Google BR (`policies.google.com/terms`) tem "Para você que prefere o resumo" no topo de cada seção; WhatsApp BR adota desde 2021.

**Cláusula expressa obrigatória:** "Este resumo é informativo. Em caso de divergência, prevalecem os Termos de Uso completos."

## Linguagem dos Termos

Padrões consolidados no mercado brasileiro:

- **Formal, mas claro.** Evitar juridiquês desnecessário ("outrossim", "destarte"). Usar "você" em B2C; "Cliente" em B2B.
- **Frases curtas** (média < 25 palavras). Parágrafos curtos. Bullets quando possível.
- **Cabeçalhos em pergunta** ("Como cancelo minha conta?") funcionam em B2C: Nubank, Spotify BR, Netflix BR usam. Em B2B prefira afirmativos neutros ("Cancelamento e rescisão").
- **Nunca** escrever "o usuário renuncia ao direito de...", "fica vedado ao usuário recorrer a...", art. 51 CDC fulmina e documento todo perde credibilidade.
- **Reformular limitações em termos positivos:** em vez de "não nos responsabilizamos por...", "nossa responsabilidade está limitada a [X]".
- **Marcar visualmente seções críticas** (mudanças, cancelamento, custos extras). **CDC art. 54 §4º exige** destaque visual pra cláusulas que limitem direito do consumidor, fonte maior, negrito, caixa destacada.

## Idioma: PT-BR é obrigatório

Quando o serviço é oferecido a brasileiros:
- **CDC art. 31:** informação em **português, ostensiva, clara, precisa**.
- **CDC art. 46:** instrumento não obriga se redigido de modo a dificultar compreensão.
- **Decreto 7.962/2013** (e-commerce): informações claras em português.

Versão em outro idioma é **tradução de cortesia**, sempre incluir cláusula:

> "Em caso de divergência entre versões, prevalece a versão em português brasileiro."

Pra B2B internacional (SaaS com cliente PJ no exterior), MSA em inglês como documento principal vale. **Mas se há qualquer pessoa física brasileira como usuário final, a camada que ela aceita precisa estar em PT-BR.**

## Termos setoriais: o que muda

| Vertical | Lei adicional | O que muda nos Termos |
|---|---|---|
| **Fintech** (instituição de pagamento, conta, crédito) | Circular BCB 3.978/2020 (PLD/FT); Resoluções BCB 96/2021 (Pix), 4.658/2018 (cibersegurança), 4.949/2021 (relacionamento) | Cláusulas KYC, monitoramento, comunicação ao COAF; CET, prazos de liquidação, chargeback, bloqueio cautelar; **proibido usar "banco"/"bank" sem licença** (nov/2025) |
| **Healthtech / Telemedicina** | Lei 14.510/2022; Resolução CFM 2.314/2022 | Sigilo médico expresso; CRM válido + registro do atendimento; **dado sensível** → LGPD art. 11; RIPD obrigatório; consentimento livre e esclarecido pra telessaúde separado dos Termos |
| **Edtech pra menor** | ECA + LGPD art. 14; ECA Digital (Lei 15.211/2025) | Verificação de idade; consentimento parental verificável < 13 anos; notificação parental; transparência sobre algoritmos; restrição de publicidade direcionada |
| **Govtech / serviço público** | Lei 13.460/2017 (Código de Defesa do Usuário); LAI (Lei 12.527/2011) | Gratuidade quando aplicável; canais de manifestação (ouvidoria); prazo de resposta; Carta de Serviços obrigatória; dados abertos |

## Notice & takedown: fluxo completo

Detalhado em `09-termos-mci-stf.md`. Resumo do fluxo interno:

```
Recebimento (formulário público)
      │
      ▼
Triagem em 24h
      │
      ▼
Análise jurídica (48-72h pra maioria; IMEDIATO para Nível 3 STF)
      │
      ├─ Remover (Nível 3, urgência)
      ├─ Notificar publicador + prazo 7 dias contraditório (regra geral)
      └─ Pedir info adicional
      │
      ▼
Decisão final: remover / manter
      │
      ▼
Log imutável + Relatório de transparência anual
```

Template do formulário público em `templates/notice-takedown-form.md`.

## Referências externas

- [STJ (Contrato eletrônico com assinatura digital, mesmo sem testemunhas, é título executivo)](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias-antigas/2018/2018-05-28_14-23_Contrato-eletronico-com-assinatura-digital-mesmo-sem-testemunhas-e-titulo-executivo.aspx)
- [STJ (Validade de assinaturas digitais fora ICP-Brasil (Migalhas))](https://www.migalhas.com.br/quentes/451284/stj-admite-assinaturas-digitais-fora-da-icp-brasil-entenda-o-tema)
- [Lei 14.063/2020 (Assinaturas eletrônicas)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/l14063.htm)
- [MP 2.200-2/2001 (ICP-Brasil)](https://www.planalto.gov.br/ccivil_03/mpv/antigas_2001/2200-2.htm)
- [Decreto 7.962/2013 (E-commerce)](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7962.htm)
- [Termos de Serviço (Google BR)](https://policies.google.com/terms?hl=pt-BR)
- [Termos (Nubank)](https://nubank.com.br/contrato/termos-de-uso/)
- [Termos e Condições (Mercado Livre)](https://www.mercadolivre.com.br/ajuda/termos-e-condicoes_299)
- [Termos (Hotmart)](https://hotmart.com/pt-br/legal)
