# 13: Transparência sobre IA/ML em Apps

> Que o app declara HOJE (2026) sobre uso de IA. Cobre 3 camadas regulatórias **simultâneas**: LGPD art. 20 (decisões automatizadas), PL 2.338/2023 (Marco Legal da IA, tramitando na Câmara), EU AI Act (Reg. UE 2024/1689, vigente desde 01/08/2024).

## 1. Cenário regulatório (maio/2026)

| Norma | Status | O que vale |
|---|---|---|
| **LGPD** | **Vigente** | Art. 20 (decisão automatizada), art. 6º IX (não discriminação), art. 9º (transparência), art. 18 (direitos do titular) |
| **PL 2.338/2023: Marco Legal da IA** | Aprovado Senado 10/12/2024; tramitando Câmara 2026 (rel. dep. Aguinaldo Ribeiro) | Modelo europeu (classificação por risco), sanções até R$ 50M, autoridade competente será **SIA** (Sistema Nacional de Regulação e Governança de IA); ANPD residual. **Ainda não é lei**, mas prep antecipada vale |
| **EU AI Act (Reg. UE 2024/1689)** | Em vigor desde 01/08/2024; plenamente aplicável 02/08/2026; GPAI desde 02/08/2025 | Vale pra app BR com usuário UE (extraterritorialidade) |
| **ANPD** | Tomada de Subsídios IA (resultados maio/2025); sandbox regulatório em 2026 | Regula PII em IA enquanto SIA não existe |

## 2. App usa API de IA de terceiro: o que declarar

### 2.1 Identificação do modelo

- Nome do provedor (Anthropic, OpenAI, Google, Mistral)
- Modelo específico (Claude Opus 4.x, GPT-5, Gemini 2.5 Pro)
- Finalidade exata ("resumir documento enviado", "sugerir resposta a e-mail", "moderar comentário")
- Se há **fallback** entre provedores → listar todos

### 2.2 Quais dados saem do app

O ponto que 99% dos devs ignora. **O prompt em si é PII** quando contém PII.

- "Enviamos ao provedor X o conteúdo que você digita em [campo Y]"
- "O prompt pode conter dados que você inseriu antes (nome, e-mail, perfil)"
- Se manda **arquivos** (PDF, imagem), declarar explicitamente

### 2.3 Política de retenção/treinamento por provedor (status maio/2026)

| Provedor | Tipo | Treinamento? | Retenção |
|---|---|---|---|
| **OpenAI API** | Padrão | **Não treina** | até **30 dias** (abuse detection); **Zero Data Retention** disponível pra Enterprise |
| **Anthropic Claude API** | Padrão | **Nunca treina inputs/outputs da API** | **7 dias** desde 14/09/2025 (era 30) |
| **Anthropic Claude consumer** (Free/Pro/Max) | - | **Treina se opt-in** (mudança 28/08/2025); retenção 5 anos se opt-in, 30d se opt-out | varia |
| **Google Gemini API, tier pago / Vertex AI** | Padrão | **Não treina** | conforme contrato |
| **Google Gemini API, free tier** | Padrão | **TREINA + revisão humana possível** | **indefinido** |

**Implicação:** se app usa **Gemini free tier**, está mandando dado do usuário pra **treinar modelo do Google + revisor humano ler**. Precisa estar na Política, com consentimento específico, OU migrar pro tier pago. Sem meio termo.

### 2.4 Transferência internacional

OpenAI, Anthropic, Google processam nos EUA (e às vezes UE/Ásia). LGPD art. 33. **Anthropic/OpenAI/Google têm DPAs** que controlador BR precisa **assinar**, não basta clicar nos termos.

Pós-**Res. CD/ANPD nº 32/2026** (UE = país adequado), preferir endpoints/regiões UE quando disponíveis.

### 2.5 Sanitização antes de enviar

Declare o que **você não manda**:
- "Removemos CPF, e-mail e telefone do prompt antes de enviar ao modelo" (se for verdade)
- Se não faz, **declare que não faz** e oriente o usuário

PII Redaction é estado-da-arte. Libs: **Microsoft Presidio**, regex caseiro pra docs BR. Resolve 80% dos casos.

---

## 3. Decisão automatizada: art. 20 LGPD

Aplica quando decisão **afeta interesse do titular sem intervenção humana significativa**.

### Casos típicos no Brasil

- Score de crédito, anti-fraude bancário
- Recomendação de feed/produto (sim, vale)
- Perfilamento pra publicidade comportamental
- Precificação dinâmica (Uber-style)
- Moderação automática (banimento, shadow ban)
- Triagem de currículo, avaliação de desempenho
- Diagnóstico médico assistido, recomendação de tratamento

### Obrigações que o app precisa expor

1. **Direito de revisão**, botão visível "Contestar esta decisão". ANPD na consulta pública 2025 ainda não fechou se revisão pode ser por outro algoritmo ou exige humano; **PL 2338 exige humano em alto risco**. **Posição segura: humano em decisão sensível** (crédito, emprego, saúde, justiça).

2. **Direito à explicação**, não é o código-fonte. É: critérios usados, dados que pesaram, lógica geral. Respeita segredo comercial (LGPD art. 20 §1º). Formato: card no app, linguagem leiga, exemplos.

3. **Canal de contestação no app**, endpoint `POST /decisoes/{id}/contestar`, prazo declarado (sugestão: 15 dias úteis), log auditável.

---

## 4. PL 2338/2023: o que muda quando virar lei

Classificação por risco (cópia atenuada do EU AI Act):

| Categoria | O que é | Obrigações |
|---|---|---|
| **Risco excessivo (proibido)** | Social scoring, manipulação subliminar, biometria em tempo real público (exceto segurança pública) | Proibido |
| **Alto risco** | Emprego, crédito, educação, saúde, segurança pública, justiça, infra crítica, biometria | AIA (Avaliação de Impacto Algorítmico) público; documentação técnica completa; governança interna; **supervisão humana significativa** com determinação final humana em decisão irreversível; reportar incidente grave ao SIA |
| **Risco baixo/moderado** | Resto | Transparência básica |

**Direitos do afetado:**
- Antes da interação: saber que é IA, finalidade, dados coletados, operador/desenvolvedor
- Depois da decisão: explicação técnica e compreensível, critérios, dados relevantes, lógica geral

**Sanções:** até R$ 50M ou 2% do faturamento por infração (texto Senado).

---

## 5. EU AI Act como benchmark: Article 50 (transparência)

Vale pra app BR com usuário UE:

- **Chatbot** deve informar que é IA (exceto se óbvio)
- **Conteúdo sintético** (imagem, áudio, vídeo, texto) deve ser **marcado em formato machine-readable** (C2PA, watermark, metadado)
- **Deepfake** de pessoa real deve ser declarado explicitamente
- **Conteúdo informativo de interesse público** gerado por IA deve ser declarado

Watermarks: **SynthID** (Google), **AudioSeal** (Meta) + manifest **C2PA 2.1** (Adobe, Microsoft, OpenAI, Meta, Google, Leica, Sony, Nikon, Canon implementam).

---

## 6. Se o app FAZ próprio modelo ou fine-tuning

Risco multiplicado.

### Procedência dos dados
- **Direito autoral:** Lei 9.610/98 art. 29 exige autorização prévia e expressa. Brasil **não tem exceção de text and data mining** (UE tem: Diretiva 2019/790). Treinar com obra protegida = risco de processo. TJSC já decidiu pela cobrança em IA derivativa.
- **Scraping:** ver Termos da fonte, robots.txt, LGPD se há PII.

### Consentimento + base legal
- Dataset com PII → qual base? Consentimento específico, ou legítimo interesse com **LIA documentada**. ANPD sinalizou ceticismo em 2025 com legítimo interesse pra treinamento massivo.

### Anonimização
- Pseudonimização ≠ anonimização. Teste de re-identificação (k-anonymity, l-diversity) obrigatório.
- Dado sintético gerado **a partir** de PII real **ainda pode ser PII** se permite re-identificação.

### Direito de remoção
- LGPD art. 18 IV/VI permite pedir anonimização/eliminação. **Problema técnico:** tirar dado de modelo já treinado é caro (machine unlearning é pesquisa). Mitigação: documentar trade-off, oferecer re-treino periódico, registrar exclusão no dataset-fonte.

---

## 7. Model cards traduzidos pro leigo BR

Adapte página `/transparencia/ia` no app. Estrutura mínima:

1. **Qual IA está aqui?** (modelo, versão, provedor)
2. **Pra que serve neste app?** (1 frase)
3. **O que ela faz bem** (3 exemplos)
4. **O que ela faz mal** (3 limitações reais, não disclaimer genérico)
5. **Onde NÃO usar** (diagnóstico médico, parecer jurídico, decisão financeira sem revisão)
6. **Como reportar erro** (link)
7. **Quando o modelo foi treinado** (cutoff)
8. **Link pro system card oficial do provedor**

Linguagem leiga. "Modelo de linguagem grande treinado em corpus multilíngue" → **"Programa que aprendeu a escrever lendo muito texto da internet."**

---

## 8. Riscos específicos no Brasil

### Discriminação algorítmica
LGPD art. 6º IX veda tratamento pra fins discriminatórios. **Testar viés** antes de soltar e periodicamente: raça, gênero, classe, região, faixa etária. Documentar. PL 2338 vai exigir pra alto risco.

### Alucinação
**Não é bug, é característica.** STJ multou advogado em mai/2025 (REsp 2.207.929/MG) por peça com jurisprudência inventada por IA. **Disclaimer não basta**: precisa validação de fato pra output factual sensível (RAG com citação, verificação cruzada).

### Prompt injection
Janeiro-Fevereiro/2026: 1 em 31 interações de GenAI em rede corporativa teve potencial alto de vazamento. Defesas:
- Separar instrução de input (system vs user message)
- Sanitizar saída antes de exibir/executar
- Agente sem permissões além do necessário
- Não confiar em output de IA pra autorizar ação destrutiva

**Vazamento por prompt injection = incidente LGPD** com notificação à ANPD.

### Vendor lock-in
OpenAI fora do ar = seu app para? LGPD art. 6º VI (continuidade). Mitigação: abstração de provedor (LiteLLM, Vercel AI SDK), fallback configurado.

---

## 9. UX de transparência: boas práticas

1. **Label visível** em todo output: "Gerado por IA" (ícone + texto), template em `templates/transparencia/ai-disclosure.tsx`
2. **Disclaimer de incerteza** em casos sensíveis: "Esta resposta pode conter imprecisões. Confirme em fonte oficial."
3. **Limites explícitos**: lista do que app **não** se propõe (diagnóstico, parecer, decisão financeira)
4. **Botão de feedback** sempre visível (thumbs up/down + campo livre)
5. **Botão de contestação** quando há decisão automatizada
6. **Tooltip "Por que isso?"** em recomendações, direito à explicação aplicado
7. **Indicador de processamento externo** quando prompt sai do servidor: "Sua mensagem foi processada por [provedor]"

---

## 10. Conteúdo gerado por IA: autoria e marcação

**Autoria:** Lei 9.610/98 só reconhece pessoa física como autora. Output puro de IA, no Brasil, **não tem proteção autoral**. Output com intervenção humana significativa pode ter, linha confusa. Documentar quem foi autor humano e quanto a IA contribuiu.

**Marca d'água:** imagens geradas devem ter SynthID (Google), C2PA manifest (Adobe Firefly, DALL-E) ou watermark visível. PL 2338 prevê obrigação de marcação de deepfake; EU AI Act art. 50 já obriga.

**Deepfake de pessoa real:** além da marcação, precisa de **consentimento da pessoa retratada** (direito de imagem, CC art. 20). Sem consentimento = ilícito civil + possível crime (Lei 14.811/2024).

---

## 11. Dados sintéticos

Dado sintético derivado de PII real:
- Se permite re-identificação → **ainda é PII** (LGPD art. 5º I e III)
- Teste obrigatório: tentativas de re-identificação com dados auxiliares públicos
- Documentar pipeline de geração + teste de privacidade
- **Differential privacy** em SDG (Synthetic Data Generation) é estado-da-arte com custo de utilidade

Sintético "do zero" (sem PII de base) é tranquilo, mas **alucina estatísticas**, útil pra teste, perigoso pra treinar modelo de produção.

---

## Checklist final pra publicar no app (2026)

- [ ] Política lista cada provedor de IA: modelo, finalidade, retenção, treinamento (sim/não), país de processamento
- [ ] DPA assinado com cada provedor de IA
- [ ] Página `/transparencia/ia` (model card simplificado) acessível do rodapé
- [ ] Banner/label "Gerado por IA" em todo output
- [ ] Botão de feedback + botão de contestação visíveis
- [ ] Canal de exercício do art. 20 (revisão de decisão) implementado
- [ ] Sanitização de PII antes de enviar ao provedor (ou declaração de que não faz)
- [ ] Logs de consent_log e de decisões (retenção compatível com prazo de contestação)
- [ ] Teste de viés documentado (se há decisão que afeta grupo)
- [ ] Plano de continuidade se provedor sair do ar
- [ ] Marca d'água/C2PA em conteúdo sintético (imagem/áudio/vídeo)
- [ ] Disclaimer de "não usar pra diagnóstico/parecer/decisão financeira" se aplicável
- [ ] Runbook de incidente cobrindo vazamento por prompt injection
- [ ] Monitoramento do PL 2338 (votação Câmara 2026) pra ajustar quando virar lei

## Referências externas

- [PL 2338/2023 (Senado)](https://www25.senado.leg.br/web/atividade/materias/-/materia/157233)
- [EU AI Act (texto PT (Reg. UE 2024/1689))](https://eur-lex.europa.eu/legal-content/PT/TXT/PDF/?uri=OJ:L_202401689)
- [EU AI Act Article 50](https://artificialintelligenceact.eu/article/50/)
- [ANPD (Tomada de Subsídios sobre IA (resultados 2025))](https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-apresenta-resultados-da-tomada-de-subsidios-sobre-tratamento-automatizado-de-dados-pessoais)
- [OpenAI Enterprise Privacy (ZDR)](https://openai.com/enterprise-privacy/)
- [Anthropic Privacy Center (data usage)](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training)
- [Gemini API privacy (BSWEN análise)](https://docs.bswen.com/blog/2026-03-23-gemini-free-tier-data-privacy/)
- [C2PA Content Credentials](https://c2pa.org/)
- [LGPD Art. 20 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art20)
- [Microsoft Presidio (PII redaction)](https://microsoft.github.io/presidio/)
