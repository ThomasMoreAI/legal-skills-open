# Checklist: Auditoria de App (LGPD)

> Questionário aplicado pela skill no projeto-alvo. Perguntar ao responsável pelo projeto (ou inspecionar o repo). Saída alimenta a classificação e a geração de todos os artefatos.

## 1. Identificação do controlador

- [ ] **Nome legal / razão social:** _____________
- [ ] **CNPJ ou CPF:** _____________
- [ ] **Endereço completo:** _____________
- [ ] **Site oficial / URL do app:** _____________
- [ ] **E-mail principal de contato:** _____________

## 2. Encarregado (DPO): art. 41

- [ ] Vai indicar DPO **pessoa nomeada** ou **canal genérico** (`privacidade@`)?
- [ ] Se pessoa nomeada: **nome, e-mail, telefone**
- [ ] Se canal genérico: **endereço de e-mail dedicado**
- [ ] **Onde será publicado?** (footer do site, página `/privacidade`, ambos)

## 3. Enquadramento como Pequeno Porte (Res. 2/2022)

Cruzar com `references/07-pequeno-porte.md`:

- [ ] Tipo de pessoa: ☐ Natural ☐ MEI ☐ ME ☐ EPP ☐ Startup (LC 182) ☐ Sem fins lucrativos ☐ Outro
- [ ] Faturamento anual (estimado): _____________
- [ ] Integra grupo econômico que estoura limites? ☐ Sim ☐ Não
- [ ] **Faz tratamento de alto risco?** Marcar TODOS aplicáveis:
  - [ ] Larga escala (muitos titulares ou volume significativo)
  - [ ] Decisões automatizadas que afetam direitos
  - [ ] Vigilância sistemática (geo contínua, biometria, monitoramento)
  - [ ] Dados sensíveis em qualquer escala
  - [ ] Dados de crianças, adolescentes ou idosos
  - [ ] IA/ML que infere algo sobre o usuário
  - [ ] Tecnologia emergente/inovadora
- [ ] **Conclusão:** ☐ ATPP (regime simplificado) ☐ Regime geral

## 4. Inventário de DADOS coletados

Pra **cada categoria** abaixo, marcar se coleta + listar quais campos:

### Dados cadastrais (comuns)
- [ ] Nome completo
- [ ] E-mail
- [ ] Telefone
- [ ] CPF / CNPJ
- [ ] Data de nascimento
- [ ] Endereço (rua, número, cidade, estado, CEP)
- [ ] Gênero declarado
- [ ] Foto de perfil

### Dados de autenticação
- [ ] Senha (sempre hash com bcrypt/argon2, nunca claro!)
- [ ] Tokens OAuth (Google, Apple)
- [ ] Biometria (digital, facial, voz): **SENSÍVEL** (art. 11)

### Dados financeiros / fiscais
- [ ] Dados de cartão (PCI-DSS, preferir tokenização via Stripe/Pagar.me)
- [ ] Dados bancários (conta, agência)
- [ ] PIX (chave)
- [ ] Histórico de transações
- [ ] Renda declarada
- [ ] Score de crédito

### Dados sensíveis (art. 11)
- [ ] Origem racial / étnica
- [ ] Convicção religiosa
- [ ] Opinião política
- [ ] Filiação sindical / partidária
- [ ] Dados de saúde (incluindo plano, condição médica, medicação)
- [ ] Vida sexual ou orientação
- [ ] Dado genético
- [ ] Dado biométrico

### Dados do dispositivo / telemetria
- [ ] IP
- [ ] User-Agent (browser, OS, modelo)
- [ ] Device ID / Advertising ID
- [ ] Fingerprint (canvas, fonts, etc.)
- [ ] Versão do app
- [ ] Crashes (Sentry, Crashlytics)

### Geolocalização
- [ ] GPS preciso (latitude/longitude)
- [ ] Geo aproximado por IP
- [ ] Localização declarada (CEP, cidade)

### Conteúdo do usuário (UGC)
- [ ] Texto (comentários, posts)
- [ ] Imagens enviadas
- [ ] Áudio
- [ ] Vídeo
- [ ] Arquivos

### Comportamento / uso
- [ ] Cliques, scrolls, hover (heatmap)
- [ ] Histórico de buscas
- [ ] Histórico de navegação interna
- [ ] Histórico de compras / consumo

### Cookies
- [ ] Estritamente necessários (sempre)
- [ ] Funcionais (preferência)
- [ ] Analíticos (GA4, Plausible, Hotjar)
- [ ] Marketing (Meta Pixel, Google Ads, remarketing)

## 5. Finalidades: uma por linha

> Pra cada finalidade, atribuir base legal (`references/02-bases-legais.md`).

| Finalidade | Dados envolvidos | Base legal | Retenção |
|---|---|---|---|
| Ex: Cadastro pra usar o app | nome, e-mail, senha | Art. 7º V (contrato) | Enquanto durar conta + 6 meses |
| Ex: Cobrança e nota fiscal | CPF, endereço | Art. 7º II (obrigação legal) | 5 anos (CTN) |
| Ex: Newsletter quinzenal | e-mail | Art. 7º I (consentimento) | Até revogação |
| ... | | | |

## 6. Compartilhamento com terceiros (operadores)

Pra **cada** ferramenta SaaS / API externa que recebe dados pessoais:

| Terceiro | Dado enviado | Finalidade | País de processamento | DPA + SCC assinado? |
|---|---|---|---|---|
| Ex: Stripe | nome, e-mail, valor | Processar pagamento | EUA | ☐ |
| Ex: Vercel | logs, IP visitante | Hospedagem | EUA / Global | ☐ |
| Ex: Mailgun | e-mail, conteúdo | Envio transacional | EUA | ☐ |
| Ex: AWS sa-east-1 | tudo do banco | Storage primário | Brasil | N/A (interno) |
| Ex: OpenAI API | prompts (podem ter PII) | Geração de texto | EUA | ☐ |
| ... | | | | |

**Listar TODOS os subprocessadores** declarados pelos seus operadores também (cascata).

## 7. Transferência internacional (art. 33 + Res. 19/2024)

- [ ] Há dados processados fora do Brasil? Se sim, listar destinos: ___________
- [ ] Para cada um: ☐ SCC da ANPD assinada ☐ Outra base ___________
- [ ] **Lembrar:** desde **Resolução CD/ANPD nº 32/2026**, **União Europeia tem decisão de adequação** (dispensa SCC). Demais países ainda exigem SCC. Preferir processadores com região UE quando disponível.

## 8. Decisões automatizadas (art. 20)

- [ ] Há feature que toma decisão sobre o usuário automaticamente? (score, anti-fraude, recomendação, perfil, precificação dinâmica)
- [ ] Se sim, descrever cada uma: ___________
- [ ] Existe canal de contestação humana? ___________

## 9. Tratamento de crianças / adolescentes (art. 14)

- [ ] O app pode ser usado por menor de 18 anos? ☐ Sim ☐ Não
- [ ] Verifica idade no onboarding? ☐ Sim ☐ Não
- [ ] Fluxo de consentimento parental verificável existe? ☐ Sim ☐ Não ☐ N/A

## 10. Segurança técnica

Cruzar com `checklists/seguranca-minima.md`:

- [ ] HTTPS / TLS 1.2+ em produção
- [ ] 2FA disponível pra usuários
- [ ] 2FA obrigatório pra admin / DB / cloud
- [ ] Senhas com hash forte (bcrypt/argon2)
- [ ] Criptografia em repouso no banco
- [ ] Backups automáticos + testados
- [ ] Logs centralizados de auth/admin
- [ ] Dependências atualizadas (dependabot / renovate)
- [ ] Secrets fora do repo (env vars / secret manager)
- [ ] DPA com cada operador estrangeiro

## 11. Política de segurança e governança

- [ ] Política de Privacidade pública (vamos gerar)
- [ ] Política de Cookies (vamos gerar, se houver tracking)
- [ ] ROPA preenchido (vamos gerar)
- [ ] RIPD elaborado (gerar se alto risco, legítimo interesse, IA, dados sensíveis, crianças)
- [ ] Runbook de incidente (vamos gerar)
- [ ] Termo de confidencialidade com colaboradores (se houver equipe)
- [ ] Treinamento de equipe (mínimo anual)

## 12. Plano de incidente

- [ ] Quem detecta? ___________
- [ ] Quem decide comunicar? ___________
- [ ] Quem fala com a ANPD? ___________ (precisa ter conta Gov.br)
- [ ] Quem comunica os titulares? ___________
- [ ] Lista de contatos de incidente dos operadores está mapeada? ___________

## 13. Outputs esperados da auditoria

Com base nas respostas acima, a skill gera em `<projeto>/legal/`:

| Sempre |
|---|
| `politica-privacidade.md` |
| `ropa.csv` |
| `runbook-incidente.md` |
| `schema-consent-log.sql` |
| `endpoints-direitos/` |
| `agent.md` |

| Condicional |
|---|
| `politica-cookies.md`, se houver cookies não-essenciais |
| `components/CookieBanner.tsx`, se for Next.js/React com cookies |
| `ripd.md`, se alto risco (4.3 do SKILL.md) |
| `dpa-clausulas-pt.md`, se houver subcontratação como operador |
