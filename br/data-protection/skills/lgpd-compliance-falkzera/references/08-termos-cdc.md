# 08: Termos de Uso: CDC, Cláusulas Abusivas, Jurisprudência

> Base canônica pra redigir Termos que **sobrevivem em juízo brasileiro**. Foco: art. 51 CDC (cláusulas nulas de pleno direito), limitação de responsabilidade, foro, arbitragem, alteração unilateral, jurisprudência STJ sobre plataformas digitais.

## Aplicabilidade do CDC

### Quem é consumidor (art. 2º e 3º)

| Situação | CDC aplica? |
|---|---|
| Pessoa física usando app como destinatário final (Netflix, Spotify, Notion pessoal, banco) | **Sim, sempre, sem discussão.** Vulnerabilidade presumida. |
| Pessoa jurídica usando SaaS como **insumo** da própria atividade (agência usando Figma, escritório usando MS365) | **Não, por padrão.** STJ usa **teoria finalista mitigada**: só aplica CDC se a PJ provar **vulnerabilidade técnica, jurídica, fática ou econômica**. Ônus de quem pleiteia. |
| App "gratuito" monetizado por ads, dados, freemium, cross-sell | **Sim.** Remuneração indireta basta (jurisprudência STJ consolidada). Google, Meta, X, todos sob CDC. |
| Software 100% open-source sem qualquer retorno econômico | **Não.** Fora do CDC. |

**Implicação pra Termos:** o mesmo documento pode ter regime jurídico diferente conforme o usuário. SaaS misto (B2C + B2B) precisa redigir cláusulas com ressalva, limitações mais agressivas só valem efetivamente contra clientes empresariais não-vulneráveis. Boa prática: ter **versão B2C neutra** + **MSA empresarial separado** para clientes PJ sofisticados.

## Art. 51 CDC: 16 hipóteses de cláusula abusiva

> Cláusulas **nulas de pleno direito**. Juiz declara de ofício (mesmo sem provocação). O "li e aceito" do clickwrap **não convalida** cláusula abusiva. §1º traz cláusula geral antiabuso ("desvantagem exagerada"); §2º mantém o resto do contrato válido sem a cláusula nula.

| # | Hipótese | O que proíbe em Termos de Uso |
|---|---|---|
| **I** | Exoneração/atenuação de responsabilidade por vícios | "Não nos responsabilizamos por bugs, indisponibilidade ou perda de dados" → NULA em B2C. Em B2B não-consumidor, limitação válida (parte final). |
| **II** | Subtrair opção de reembolso | "Pagamentos não são reembolsáveis em nenhuma hipótese" → NULA. Tem que oferecer reembolso, substituição ou abatimento. |
| **III** | Transferir responsabilidade a terceiros | "Use o parceiro X por sua conta e risco" quando o app integra/intermedia → NULA. Marketplace responde solidariamente quando aufere vantagem econômica direta/indireta. |
| **IV** | Desvantagem exagerada (cláusula coringa) | §1º: viola sistema de proteção, restringe direitos essenciais ou é excessivamente onerosa. Captura tudo que escapa dos demais incisos. |
| **V** | Inversão do ônus da prova em prejuízo do consumidor | "Cabe ao usuário provar que o serviço estava indisponível" → NULA. |
| **VI** | Compromisso arbitral compulsório | Combinado com Lei 9.307/96 art. 4º §2º. Ver seção "Arbitragem". |
| **VII** | Imposição de representante | Não pode obrigar usuário a ser representado por preposto da plataforma. |
| **VIII** | Negócio entregue ao exclusivo critério do fornecedor | Problemática se já houve relação contratual em curso. |
| **IX** | Variar preço unilateralmente | "Podemos alterar o preço a qualquer tempo" → NULA. Reajuste tem que ter índice objetivo e período mínimo (Lei 10.192/2001, anual). |
| **X** | Cancelar unilateralmente sem igual direito ao consumidor | Suspensão/banimento sem critério objetivo, sem contraditório, sem possibilidade simétrica → NULA. **STJ 2024 consolidou: mesmo em violação grave, plataforma deve garantir defesa antes ou após.** |
| **XI** | Ressarcimento unilateral de custos de cobrança | "Em inadimplência cobramos honorários de 20%" sem direito recíproco → NULA. |
| **XII** | Renúncia ou disposição de direitos | "Você renuncia ao direito de pleitear danos morais" → NULA. Direitos do consumidor são **irrenunciáveis**. |
| **XIII** | Modificação unilateral do contrato após celebração | Ver "Alteração". |
| **XIV** | Infração a normas ambientais | Raríssimo em SaaS. |
| **XV** | Desacordo com sistema de proteção ao consumidor | Cláusula residual. |
| **XVI** | Renúncia de indenização por benfeitorias necessárias | Resquício de locação. |

## Limitação de responsabilidade: até onde dá

### B2C (consumidor)

- **Art. 25 CDC:** vedada cláusula que **impossibilite, exonere ou atenue** a obrigação de indenizar prevista nas seções de responsabilidade por fato e por vício.
- Combinado com art. 51 I e II → **cap monetário fechado em valor pago** (ex: "responsabilidade limitada aos últimos 12 meses pagos") é **NULA contra consumidor**. Jurisprudência pacífica.
- **O que dá pra fazer:** SLA objetivo (uptime, tempo de resposta), oferecer crédito proporcional à indisponibilidade, distinguir danos diretos de indiretos **com cautela**. **Nunca zerar nem teto fechado em valor pago.**

### B2B não-consumidor

- Liberdade contratual prevalece (CC art. 421-422). Cap = 12 meses pagos, exclusão de lucros cessantes e danos indiretos, exclusão por força maior e ato de terceiro → **válido**, desde que negociado de boa-fé e sem dolo/culpa grave (CC art. 393).

### Boa prática

Default **B2C neutro**: sem cap monetário; afasta apenas lucros cessantes e danos indiretos onde a lei permite; mantém responsabilidade por vícios e danos diretos. Mais defensável em juízo brasileiro. Quando o projeto for B2B com cliente sofisticado, ramificar.

**Redação sugerida (B2C neutro):**

> "Na máxima extensão permitida pela legislação aplicável, e **sem prejuízo das garantias legais asseguradas ao consumidor pelo Código de Defesa do Consumidor**, a [Empresa] responde pelos danos diretos comprovadamente decorrentes de falha imputável ao Serviço, ficando excluídos lucros cessantes e danos indiretos quando a exclusão for legalmente cabível. Esta limitação **não se aplica** a casos de dolo, culpa grave, danos a direitos da personalidade ou hipóteses de responsabilidade objetiva legalmente atribuídas."

## Foro de eleição

### Regra geral
- **Súmula 335 STF:** válida cláusula de eleição de foro em contrato.

### Em contrato de adesão e relação de consumo
- **CDC art. 101 I:** ação contra o fornecedor pode ser proposta no **domicílio do consumidor**. Foro do consumidor = competência absoluta em seu favor.
- **CPC art. 63 §3º:** em contrato de adesão, **juiz pode declarar nula de ofício** a cláusula de eleição de foro abusiva, antes da citação, remetendo ao domicílio do réu (consumidor).
- STJ consolidou: cláusula em adesão **não prevalece quando distante do consumidor** ou dificulta acesso à Justiça. Em B2C, prejuízo é praticamente presumido.

### Redação executável

- **B2C:** "Fica eleito o foro do domicílio do Usuário consumidor, nos termos do art. 101, I, do CDC."
- **B2B:** "Para Usuários corporativos (PJ), fica eleito o foro da Comarca de [Cidade/UF]."

## Arbitragem

**Proibida pra consumidor** pela combinação:
- **CDC art. 51 VII:** nula cláusula que determine arbitragem compulsória.
- **Lei 9.307/96 art. 4º §2º:** em contrato de adesão, a cláusula compromissória só tem eficácia se o aderente **tomar a iniciativa** de instituir a arbitragem ou concordar **expressamente, por escrito em documento anexo ou em negrito**, com assinatura específica para essa cláusula.

**Interpretação STJ:** arbitragem **pode** existir em consumo, mas **só vale se o consumidor tomar a iniciativa** ou concordar **após o conflito**. Cláusula prévia que obriga arbitragem antes da disputa = nula.

**Boa prática:** em B2C, **não colocar** cláusula de arbitragem. Em B2B com hipossuficiência potencial, destacar visualmente e exigir aceite específico.

## Alteração unilateral dos Termos

**Art. 51 XIII** veda autorizar o fornecedor a "modificar unilateralmente o conteúdo ou a qualidade do contrato após sua celebração".

**Como fazer corretamente, padrão mercado:**

1. **Comunicação prévia e individualizada** (e-mail + push + banner in-app). Mero "está publicado no site" é browse-wrap fraco.
2. **Prazo razoável** entre comunicação e vigência. **30 dias** é o padrão de mercado (Nubank, iFood, ML, Magalu).
3. **Destacar o que mudou** (changelog ou diff visual). Trocar termos sem explicação é prática abusiva.
4. **Direito de rescindir sem ônus** pra quem discordar. Silêncio do usuário pode ser aceitação **se** notificação efetiva ocorreu e ele teve chance real de sair, ônus de provar a notificação é do fornecedor.
5. **Versionamento** com data de vigência (v3.2, v3.3...) e versões anteriores acessíveis.
6. **Mudanças materiais** (preço, escopo, política de cancelamento, foro, limitação de responsabilidade, base legal LGPD) → **modal blocker** que exige novo aceite ativo na próxima sessão.

Alterações que afetam **dados pessoais** disparam regras adicionais da LGPD (novo consentimento se base for consentimento, atualização do ROPA, comunicação à ANPD em casos sensíveis).

## Direito de arrependimento (art. 49 CDC)

**Texto:** consumidor pode desistir em **7 dias corridos** "a contar de sua assinatura ou do ato de recebimento do produto ou serviço, sempre que a contratação de fornecimento ocorrer fora do estabelecimento comercial, especialmente por telefone ou a domicílio".

**Aplica a SaaS?** **Sim**, doutrina e jurisprudência aplicam pacificamente a streaming, cursos online, apps com assinatura, licenças. **Restituição integral**, imediata, monetariamente atualizada, **sem ônus** (parágrafo único).

**Quando NÃO aplica:**
- Consumo já realizado e **informado destacadamente** antes da compra (ex: ebook baixado integralmente).
- Bens sob medida (raro em SaaS).
- B2B (sem consumidor).

**Implementação no fluxo:**
- Checkout permite cancelamento self-service por 7 dias com reembolso automático.
- Trial gratuito antes da cobrança neutraliza o problema.
- Pra conteúdo de consumo imediato (curso, ebook), **destacar avisos pré-compra** e registrar aceite específico.

## Jurisprudência STJ relevante: plataformas digitais

### Marketplaces (Mercado Livre, OLX, Amazon, Magalu)

- **Responsabilidade solidária e objetiva** quando a plataforma aufere vantagem econômica direta ou indireta E participa da cadeia de fornecimento (oferta, pagamento, logística).
- **STJ abr/2021:** site **não responde por fraude FORA da plataforma** (transação desviada pra WhatsApp/PIX direto).
- **STJ set/2024:** Mercado Livre **não é obrigado** a excluir anúncio denunciado por violação de termos próprios, aplicação dos próprios termos é discricionária, **desde que não cause dano a terceiro**.

### Apps de transporte: relação com motorista (Uber, 99)

- **STJ jul/2024 (REsp 2.135.783, 2.018.788):** relação plataforma↔motorista é **civil/comercial**, NÃO consumerista nem trabalhista, salvo prova de vulnerabilidade.
- **Plataforma pode suspender imediatamente** motorista por ato grave, mas **deve garantir defesa e revisão** (devido processo informal).

### Reflexo direto pros Termos

Termos de qualquer plataforma com banimento precisam prever:
- **Canal de contestação** explícito.
- **Prazo de resposta** (5-15 dias úteis).
- **Justificativa** da suspensão/exclusão.
- **Direito de exportar dados** antes da exclusão (LGPD art. 18 V).

### Clickwrap vs Browse-wrap (validade)

- **Clickwrap** (checkbox + botão "Aceito"): aceite válido, equivale a assinatura (MP 2.200-2/2001 + MCI + Lei 14.063/2020).
- **Browse-wrap** (link no rodapé "ao usar você aceita"): aceite **frágil**. Sem registro de aceite explícito, cláusulas restritivas dificilmente são opostas ao usuário.
- Boa prática: **clickwrap com timestamp, IP, versão dos termos, hash do documento, user-agent**. Cláusulas onerosas em **destaque** (negrito + aceite específico) → art. 54 §4º CDC.

## Termos vs Política de Privacidade: separar

**Por que separar (documentos independentes):**

1. **Natureza distinta:** Termos = contrato (CDC + CC + MCI). Política = declaração de transparência (LGPD art. 9º + MCI art. 7º).
2. **Atualização independente:** Política muda toda vez que entra novo processador; Termos mudam por motivo comercial.
3. **Auditoria/ANPD:** ANPD avalia Política isoladamente; misturar vira evidência ruim.
4. **Bases legais distintas:** aceite de Termos é manifestação contratual; consentimento LGPD tem requisitos próprios (livre, informado, específico, destacado, revogável, art. 8º LGPD). Misturar num único "li e aceito" pode invalidar o consentimento.
5. **UX:** dois links distintos no rodapé e no cadastro, com checkbox separado pra cada quando a base for consentimento.

**Stack completa recomendada:**
- `legal/termos.md`, contrato
- `legal/privacidade.md`: LGPD art. 9º
- `legal/cookies.md`, política de cookies
- `legal/dpa.md`: DPA pra clientes B2B (quando aplicável)
- `legal/comunidade.md`, código de conduta (se houver UGC)

## Referências externas

- [Lei 8.078/1990 (CDC (Planalto))](https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm), arts. 2, 3, 25, 49, 51, 54, 101
- [Lei 9.307/1996 (Arbitragem)](https://www.planalto.gov.br/ccivil_03/leis/l9307.htm), art. 4º §2º
- [Lei 13.105/2015 (CPC)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13105.htm), art. 63 §3º
- [STJ (Teoria finalista mitigada e vulnerabilidade)](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2024/08092024-Consumidor-pessoa-juridica-quando-as-empresas-podem-ter-a-protecao-do-CDC.aspx)
- [STJ (Mercado Livre e moderação de anúncios (set/2024))](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2024/16092024-Mercado-Livre-nao-e-obrigado-a-excluir-anuncios-denunciados-por-violacao-dos-termos-de-uso-do-site.aspx)
- [STJ (Suspensão de motorista de app exige defesa (jul/2024))](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2024/15072024-Motorista-de-aplicativo-pode-ser-suspenso-imediatamente-por-ato-grave--mas-plataforma-deve-garantir-defesa.aspx)
- [TJDFT (Cláusulas abusivas)](https://www.tjdft.jus.br/institucional/imprensa/campanhas-e-produtos/direito-facil/edicao-semanal/clausulas-abusivas-ao-consumidor-sao-nulas)
- [Decreto 7.962/2013 (E-commerce)](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7962.htm)
