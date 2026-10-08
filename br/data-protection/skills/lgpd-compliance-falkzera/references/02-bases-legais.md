# 02: Bases Legais: matriz das 10 (art. 7º) + 8 (art. 11)

> Sem base legal, o tratamento é ilícito. **Toda finalidade** declarada precisa estar amparada em **uma** das hipóteses abaixo. Registrar essa correspondência no ROPA é obrigação de accountability (art. 6º X).

## Art. 7º: Dados pessoais COMUNS (10 hipóteses)

> *"O tratamento de dados pessoais somente poderá ser realizado nas seguintes hipóteses:"*

### I: Consentimento do titular

- Forma: **livre, informada, inequívoca, específica** (art. 5º XII + art. 8º).
- Por escrito ou outro meio que demonstre a manifestação. Se contrato escrito, **cláusula destacada**.
- Checkbox pré-marcado é **NULO** (manifestação não-inequívoca).
- Revogação **tão fácil quanto** dar consentimento (art. 8º §5º).
- Mudou finalidade ou condições? Informar com destaque específico e permitir nova manifestação (art. 8º §6º).

**Quando usar:**
- Newsletter, marketing direto, push promocional, SMS comercial.
- Cookies analíticos e de publicidade.
- Compartilhamento com terceiros não estritamente necessários ao serviço.
- Tratamento que não cabe nas outras 9 hipóteses.

**Quando NÃO usar:**
- Pra cobrir tratamento essencial à execução do serviço (use V, contrato).
- Pra cobrir obrigações fiscais/legais (use II, obrigação legal).
- Quando há desequilíbrio de poder que vicia o consentimento (ex: empregador → empregado, governo → cidadão dependente de benefício).

### II: Cumprimento de obrigação legal ou regulatória pelo controlador

**Quando usar:**
- Emissão de nota fiscal (Receita Federal, CT-e, NFe).
- Retenção de logs: **1 ano** se provedor de conexão (Marco Civil art. 13); **6 meses** se provedor de aplicação (art. 15).
- Dados trabalhistas, FGTS, INSS.
- KYC bancário (Bacen), compliance PLD-FT (COAF).
- Comunicações obrigatórias a autoridades.

**Cuidado:** a obrigação legal/regulatória precisa existir formalmente, uma resolução, lei, instrução normativa. "É costume do setor" não basta.

### III: Pela administração pública, para execução de políticas públicas previstas em lei ou regulamentos

**Quando usar:**
- Cadastro Único (CadÚnico).
- Bolsa Família / Auxílio Brasil.
- App municipal de saúde, vacinação, escolar.
- Sistemas internos de órgão público (folha, protocolo, gestão orçamentária).

**Específico:** capítulo IV da LGPD trata exclusivamente do tratamento pelo Poder Público (arts. 23-32). Inclui dever de transparência ativa (LAI) e RIPD obrigatório quando há operações com base nesta hipótese (art. 32).

### IV: Realização de estudos por órgão de pesquisa

- Garantida, sempre que possível, a **anonimização**.
- "Órgão de pesquisa" definido no art. 5º XVIII: órgão/entidade da administração pública direta/indireta, OU pessoa jurídica de direito privado sem fins lucrativos, legalmente constituída sob lei brasileira, com sede e foro no País, que inclua em sua missão institucional ou em seu objetivo social ou estatutário a pesquisa básica ou aplicada.

**Quando usar:**
- App de pesquisa acadêmica vinculado a universidade pública (a universidade é o órgão de pesquisa).
- Universidades, FIOCRUZ, IPEA, INSPER, FGV em projetos institucionais.

**Cuidado:** startup com "pesquisa interna de produto" **não** se qualifica. Esta base é restrita.

### V: Execução de contrato ou procedimentos preliminares a pedido do titular

**Quando usar:**
- Cadastro mínimo de e-commerce pra entregar produto comprado.
- Conta de SaaS pra prestar o serviço contratado.
- Entrega de aplicativo (Stripe pra processar pagamento, Twilio pra OTP de login).
- Coleta de endereço pra entrega.

**Limite:** o tratamento precisa ser **necessário** à execução. Pedir "data de nascimento" pra entregar um produto físico não cabe nessa base, só pertinentes e proporcionais.

### VI: Exercício regular de direitos em processo judicial, administrativo ou arbitral

**Quando usar:**
- SaaS jurídico armazenando dados de partes em processo.
- Plataforma de mediação de conflitos.
- Sistema de defesa do consumidor.
- Conservação de provas para litígio iminente ou em curso.

### VII: Proteção da vida ou da incolumidade física do titular ou de terceiro

**Quando usar:**
- App de emergência médica que envia geolocalização ao SAMU.
- Botão de pânico em app antiviolência (ex: 180, Maria da Penha).
- Wearable que detecta queda e aciona contato de emergência.

### VIII: Tutela da saúde, exclusivamente em procedimento realizado por profissionais ou serviços de saúde

**Quando usar:**
- Prontuário eletrônico de clínica.
- Plataforma de telemedicina.
- Sistema interno hospitalar.

**Cuidado:** "tutela da saúde" cobre dado **comum** quando o tratamento é por profissional de saúde. Pra **dado sensível** (que inclui dado de saúde, art. 5º II), usar art. 11 II (f).

### IX: Legítimo interesse do controlador ou de terceiro

> *"...ressalvados os direitos e liberdades fundamentais do titular que exijam a proteção dos dados pessoais"*

**Requisitos (art. 10):**
- Finalidades **legítimas, concretas, demonstráveis**.
- Apoio e promoção de atividades do controlador.
- Proteção do exercício regular de direitos.
- Prestação de serviços que beneficiem o titular.
- Estritamente necessário para a finalidade pretendida.
- Adoção de medidas pra garantir transparência e direitos do titular.
- **RIPD recomendado** (art. 10 §3º, a ANPD pode solicitar).
- **Não cabe pra dado sensível** (apenas art. 11).

**Quando usar:**
- Prevenção a fraude em cadastro/checkout (segurança da plataforma).
- Segurança da rede (firewall, IDS, logs de auth).
- Cobrança de inadimplentes (com limites).
- Marketing direto pra clientes existentes (mais discutido, algumas interpretações exigem consentimento).
- Garantia de propriedade intelectual.

**Teste de balanceamento obrigatório:** documentar (em RIPD) que o interesse legítimo SUPERA o impacto nos direitos do titular, considerando expectativas legítimas, contexto, mitigantes.

### X: Proteção do crédito

**Quando usar:**
- Consulta a Serasa, SPC, Boa Vista antes de aprovar crediário.
- Cadastro positivo (Lei 12.414/2011).
- Análise de risco de inadimplência.

**Específico:** combinada com o art. 18 do CDC e Lei do Cadastro Positivo. Score automatizado aciona o art. 20 (direito de revisão).

## Art. 11: Dados pessoais SENSÍVEIS

Regime estrito. Lista (taxativa):

### I: Consentimento específico e destacado

- Mais rigoroso que o art. 8º: precisa ser **específico** (cada finalidade pede um consentimento), **destacado** (visualmente independente), **prévio**, **informado**.
- Mudou uma finalidade? Novo consentimento.

**Quando usar:**
- App de saúde que quer compartilhar diagnóstico com seguradora.
- Plataforma religiosa coletando filiação.
- Pesquisa eleitoral coletando opinião política.
- Biometria pra autenticação em fintech (KYC).

### II: Sem consentimento, quando indispensável para:

| Alínea | Hipótese | Quando |
|---|---|---|
| **a** | Cumprimento de obrigação legal/regulatória pelo controlador | INSS médico, prontuário SUS |
| **b** | Tratamento compartilhado para execução de políticas públicas | DATASUS, SISVAN, e-SUS |
| **c** | Estudos por órgão de pesquisa, com anonimização sempre que possível | Microdados do SIH-SUS em pesquisa acadêmica |
| **d** | Exercício regular de direitos, inclusive em contrato e processo | Ação trabalhista envolvendo prontuário ocupacional |
| **e** | Proteção da vida do titular ou terceiro | Emergência médica em paciente inconsciente |
| **f** | Tutela da saúde, exclusivamente em procedimento por profissionais/serviços de saúde ou autoridade sanitária | Clínica, hospital, vigilância epidemiológica |
| **g** | Garantia da prevenção à fraude e à segurança do titular, em processos de identificação/autenticação | Biometria facial em e-banking |

### Vedações expressas (art. 11 §§)

- **§4º**: Controladores de dados sensíveis de saúde **não podem comunicá-los entre si** com objetivo de obter vantagem econômica.
- **§5º**: Operadoras de plano de saúde **não podem** tratar dados de saúde para seleção de riscos na contratação ou para exclusão de beneficiários.

> **Importante:** "legítimo interesse" do art. 7º IX **NÃO se aplica** a dado sensível. Foi escolha deliberada do legislador.

## Decisões automatizadas (art. 20): aplica sobre qualquer base

Quando o tratamento envolver **decisão tomada unicamente com base em tratamento automatizado** que afete o titular:

- Direito de **solicitar revisão**.
- Controlador deve fornecer informações claras e adequadas sobre os critérios e procedimentos (resguardados segredos comercial e industrial).
- Recusa em informar → ANPD pode auditar (§2º).

**Casos típicos:**
- Score de crédito.
- Aprovação/recusa automática de cadastro.
- Perfilamento publicitário.
- Algoritmo de recomendação.
- Anti-fraude automatizado.
- Precificação dinâmica baseada em perfil.

## Fluxo de decisão da skill

```
                    ┌──────────────────────────┐
                    │ Há finalidade definida?  │
                    └─────────┬────────────────┘
                              │
                ┌─────────────┴─────────────┐
                ▼                            ▼
        ┌──────────────┐            ┌──────────────────┐
        │ É essencial  │            │ Recusar tratamento│
        │ à finalidade?│            │, finalidade vaga │
        └──────┬───────┘            └──────────────────┘
               │
        ┌──────┴───────┐
        ▼              ▼
  ┌──────────┐  ┌──────────────────────┐
  │ Sensível?│  │ Cabe em obrigação    │
  └────┬─────┘  │ legal, contrato,     │
       │        │ proteção vida, etc?  │
  ┌────┴────┐   └─────┬────────────────┘
  ▼         ▼         │
SIM       NÃO         ▼
│         │     ┌─────────────────┐
│         │     │ SIM: use essa   │
│         │     │ NÃO: legítimo   │
│         │     │   interesse?    │
│         │     │   → faz RIPD    │
│         │     │ Última opção:   │
│         │     │   consentimento │
│         │     │   opt-in        │
│         │     └─────────────────┘
▼         ▼
art.11    art.7º
estrito
```

## Checklist por finalidade no ROPA

Pra cada linha do ROPA (uma finalidade por linha), preencher:

```
Finalidade           : "Envio de newsletter quinzenal"
Dados envolvidos     : e-mail, nome
Categoria            : comum (não sensível)
Base legal           : art. 7º I, consentimento
Mecanismo de coleta  : checkbox opt-in no rodapé
Tempo de retenção    : até revogação ou 2 anos sem abertura
Compartilhamento     : Mailgun (SCC ANPD, EUA)
Direito de revogar   : link no rodapé de cada e-mail + painel privacidade
```

## Referências externas

- [LGPD Art. 7º (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art7)
- [LGPD Art. 11 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art11)
- [LGPD Art. 8º (consentimento) (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art8)
- [LGPD Art. 10 (legítimo interesse) (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art10)
- [LGPD Art. 20 (decisão automatizada) (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art20)
