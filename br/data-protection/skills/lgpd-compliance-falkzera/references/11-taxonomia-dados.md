# 11: Taxonomia Técnica de Dados Pessoais

> Mapa pragmático das **12 categorias canônicas** de dados pessoais que um app pode coletar. Pra dev marcar checkbox no inventário público + detectar no código + escolher base legal. Baseado em Apple App Privacy Details, Google Play Data Safety, Mozilla Lean Data, LGPD arts. 5º e 11.

## Como usar esta referência

Pra cada categoria, leia: **(a)** o que cai aqui, **(b)** como detectar no código (palavras-chave pra `rg`), **(c)** sensibilidade típica, **(d)** base legal default, **(e)** riscos, **(f)** como declarar, **(g)** como minimizar.

A skill cruza essa taxonomia com o código do projeto pra gerar o **inventário público** (ver `references/12-transparencia-radical.md`).

---

## 1. Dados de identidade e contato

**O que cai aqui:** nome, nome social, e-mail, telefone, endereço, CEP, CPF, RG, CNH, passaporte, data de nascimento, foto de perfil, login social.

**Detecção:**
- Schema: `name`, `email`, `phone`, `cpf`, `tax_id`, `birth_date`, `avatar_url`
- Form: `<input type="email">`, `inputmode="numeric"`, máscara CPF, `react-input-mask`, `brazilian-values`
- APIs: ViaCEP, Serpro Datavalid, Receita Federal CNPJ
- Login social: `next-auth` providers, Firebase Auth, Supabase Auth, Clerk

**Login social, granularidade:**

| Provider | Sempre exposto | Sob escopo extra | Risco |
|---|---|---|---|
| Google (OIDC) | `sub`, `email`, `name`, `picture`, `locale` | calendar, contacts, drive | Acesso a Gmail é high-risk |
| Apple Sign In | `sub`, `email` (real ou relay), `name` (só 1º login!) | - | Mais privacy-friendly |
| Facebook | `id`, `name`, `email` | friends, posts, location | `user_friends` raramente aprovado |
| GitHub | `id`, `login`, `avatar_url`, `email` | `repo`, organizations | Token de repo é poderoso |
| LinkedIn | `id`, `name`, `email`, `profile_url` | conexões, currículo | Dado profissional sensível em contexto |

- **Sensibilidade:** média. CPF merece atenção (não logar, não expor em URL).
- **Base legal:** execução de contrato (art. 7º V) pra essencial; consentimento (art. 7º I) pra opcionais.
- **Riscos:** spam, phishing, fraude com CPF, golpe de identidade.
- **Declarar:** "Identificação cadastral, nome, e-mail, telefone, CPF. Necessários pra emissão de NF / autenticação / atendimento."
- **Minimizar:** não pedir CPF se não emite NF; usar Apple Sign In relay; aceitar nome social; não expor e-mail em URL pública (use slug separado).

---

## 2. Dados de autenticação

**O que cai aqui:** senha (hash+salt), tokens (session, refresh, JWT, API key), 2FA TOTP, backup codes, magic links, biometria, passkeys.

**Detecção:**
- Tabelas: `users.password_hash`, `sessions`, `refresh_tokens`, `api_keys`, `totp_secrets`, `webauthn_credentials`, `recovery_codes`
- Libs: `bcrypt`, `argon2`, `scrypt`, `jose`, `jsonwebtoken`, `otplib`, `speakeasy`, `@simplewebauthn/server`
- Web: `navigator.credentials.create({publicKey})`, `.get`
- Mobile: `LocalAuthentication` (Expo), `BiometricPrompt`, `LAContext`

**Biometria, distinção crítica:**
- **Touch ID / Face ID nativos** NÃO expõem template ao app, só retornam `success`. **Não é coleta de biometria** legalmente; só "uso de biometria do dispositivo".
- **WebAuthn / Passkey** guarda chave pública; privado fica no Secure Enclave. **Não é biometria** legalmente.
- **App que captura foto pra liveness/KYC** (Caixa Tem, Open Finance), aí **SIM** coleta biometria **sensível** (LGPD art. 11), exige consentimento específico.

- **Sensibilidade:** crítica. Vazamento de hash+salt = brute-force offline; TOTP secret = bypass do 2FA.
- **Base legal:** execução de contrato + segurança (art. 7º X, proteção do crédito).
- **Riscos:** account takeover, lateral movement, fraude.
- **Declarar:** "Credenciais, armazenadas com hash criptográfico (argon2id). Tokens de sessão expiram em X."
- **Minimizar:** argon2id ou bcrypt cost ≥12; rotacionar refresh tokens; TTL curto; 2FA obrigatório em conta sensível; preferir passkey a senha.

---

## 3. Dados financeiros

**O que cai aqui:** PAN (número do cartão), CVV, validade, conta+agência, chave PIX, histórico de transações, valores, contrapartes, renda, score, perfil de consumo.

**Detecção:**
- Gateways: `stripe`, `mercadopago`, `pagar.me`, `iugu`, `asaas`, `pagseguro`
- Tabelas: `transactions`, `invoices`, `subscriptions`, `payment_methods`, `pix_keys`, `bank_accounts`
- Open Finance: Belvo, Pluggy, OAuth BCB
- Score: Serasa, Boa Vista, Quod APIs

**Regra de ouro PCI-DSS:** **NUNCA armazenar PAN+CVV.** Usa tokenização do gateway, guarda só `tok_visa_xxxx`, `last4`, `brand`, `exp_month`. Tocar em PAN cru = PCI-DSS Level 1-4 com auditoria anual.

- **Sensibilidade:** alta. Alvo preferido de incidente.
- **Base legal:** execução de contrato + obrigação legal (fiscal, 5 anos).
- **Riscos:** fraude, clonagem, golpe, perfilamento abusivo, score sem revisão = art. 20 LGPD.
- **Declarar:** "Pagamentos processados pelo [gateway, link política]. Armazenamos apenas últimos 4 dígitos e tipo de cartão. Histórico por 5 anos (Decreto 7.212/2010)."
- **Minimizar:** tokenização sempre; não logar webhook payload (vem com PAN); separar banco fiscal do operacional; agregar histórico antigo.

---

## 4. Identificadores de dispositivo e técnicos

A categoria mais sub-declarada por devs brasileiros. **Tudo aqui é PII** sob LGPD se permite re-identificação.

### 4.1 Rede
- IP (v4, v6), `req.headers['x-forwarded-for']`, `req.ip`
- ASN/ISP, derivável via MaxMind, IPinfo

### 4.2 User-Agent e Client Hints
- `User-Agent`, `Accept-Language`, `Sec-CH-UA`, `Sec-CH-UA-Platform`, `DNT`, `Sec-GPC`

### 4.3 IDs persistentes
- Web: cookie `_ga`, `_fbp`, `_gcl_au`, qualquer cookie persistente
- iOS: **IDFA** (App Tracking Transparency exige opt-in desde iOS 14.5), **IDFV** (por vendor, sem opt-in)
- Android: **AAID** (`com.google.android.gms.ads.identifier`), Android ID (`Settings.Secure.ANDROID_ID`)
- Push: APNs token, FCM token, OneSignal player ID
- MAC: bloqueado em iOS/Android modernos

### 4.4 Fingerprint passivo (browser)
- Canvas fingerprint (`canvas.toDataURL()`)
- WebGL renderer/vendor (`gl.getParameter(gl.RENDERER)`)
- AudioContext fingerprint (`OfflineAudioContext` + FFT)
- Fontes instaladas (medindo `offsetWidth`)
- Plugins, MIME types
- `screen.width/height`, `devicePixelRatio`, `colorDepth`
- `Intl.DateTimeFormat().resolvedOptions().timeZone`
- `navigator.language(s)`, `navigator.hardwareConcurrency`, `navigator.deviceMemory`
- `navigator.connection.effectiveType` (Network Information API)
- Battery API (deprecada), Permissions API state

**Detecção de libs:** `@fingerprintjs/fingerprintjs`, `clientjs`, `fingerprint2`, qualquer `canvas.toDataURL` sem motivo claro.

### 4.5 Storage persistente
- `localStorage`, `sessionStorage`, IndexedDB, Cache API, cookies, BroadcastChannel, Service Worker

- **Sensibilidade:** média individualmente, **alta combinada**. EFF Panopticlick, fingerprint identifica 1 em 286 mil.
- **Base legal:** legítimo interesse (analytics próprio essencial), consentimento (3rd party).
- **Riscos:** tracking cross-site sem opt-in, re-identificação pós-logout, perfilamento sem ciência.
- **Declarar:** "Identificadores técnicos: IP, user-agent, ID de dispositivo. Usados pra segurança e analytics agregado. Retidos por 90 dias em logs brutos, depois agregados."
- **Minimizar:** **truncar IP** (zerar último octeto /24 IPv4, /64 IPv6); IDFV em vez de IDFA; respeitar `Sec-GPC` e `DNT`; **NÃO** rodar FingerprintJS sem consentimento (App Store rejeita).

---

## 5. Geolocalização

**O que cai aqui:**
- GPS preciso (lat/lng < 100m)
- Geo aproximado (cidade, via IP)
- WiFi BSSIDs triangulados
- Bluetooth beacons (iBeacon, Eddystone)
- Declarada (CEP, cidade no cadastro)
- **Histórico de localizações**, sensível por inferência: revela casa, trabalho, médico, religião

**Detecção:**
- Web: `navigator.geolocation.getCurrentPosition`, `watchPosition`
- iOS: `CLLocationManager`, `requestWhenInUseAuthorization`, `requestAlwaysAuthorization` (**red flag**)
- Android: `FusedLocationProviderClient`, `ACCESS_FINE_LOCATION`, `ACCESS_BACKGROUND_LOCATION` (**red flag**)
- Server: MaxMind GeoIP, IPinfo, ipapi

- **Sensibilidade:** alta. Histórico de geo é **dado sensível por inferência** (templo = religião; hospital = saúde; sede de partido = política). ANPD/MPF já trataram como tal (caso Serasa, Hariexpress).
- **Base legal:** **consentimento específico** (art. 7º I + permissão SO). NUNCA legítimo interesse pra geo precisa contínua.
- **Riscos:** stalking, doxxing, dedução de hábitos íntimos, sequestro express.
- **Declarar:** "Localização precisa (GPS), apenas quando você toca em 'usar localização'. Não armazenada. Aproximada por IP, exibir conteúdo regional, X dias."
- **Minimizar:** pedir só quando essencial; preferir `requestWhenInUseAuthorization`; arredondar coordenadas (2 casas decimais ≈ 1km); NUNCA background location se não for app de delivery; oferecer CEP manual como alternativa.

---

## 6. Mídia e arquivos

**O que cai aqui:** fotos, vídeos, áudios, PDFs, planilhas, qualquer upload.

**Detecção:**
- `<input type="file">`, `accept="image/*"`
- Libs: `react-dropzone`, `multer`, `formidable`, `busboy`, `@uploadthing/react`
- Storage: S3, R2, Supabase Storage, Vercel Blob, Firebase Storage

**EXIF, o trap silencioso:** foto de celular traz `GPSLatitude/Longitude`, `Make`, `Model`, `Software`, `DateTimeOriginal`, `LensModel`. PDFs guardam `Author`, `Creator`, `Producer`, às vezes versões anteriores (bug histórico).

- **Sensibilidade:** variável. Selfie + EXIF = casa do titular. PDF com revisão = vazamento corporativo.
- **Base legal:** execução de contrato (fotolog), consentimento (perfil opcional).
- **Riscos:** doxxing por EXIF, vazamento de revisões PDF, deepfake, malware em PDF/SVG.
- **Declarar:** "Arquivos enviados, armazenados em [provider, região]. Metadados de localização (EXIF) removidos no upload."
- **Minimizar:** strip EXIF (`sharp().rotate().toBuffer()` já remove); redimensionar (não guarde 4K se exibe 800px); validar MIME server-side; sanitizar SVG (`DOMPurify`); antivírus (ClamAV em queue).

---

## 7. Conteúdo do usuário (UGC)

**O que cai aqui:** texto livre (posts, comentários, DMs, bios, reviews), reações, follows, listas, coleções.

**Detecção:** `<textarea>`, editor rico (Tiptap, Lexical, Slate), DM/chat, comentários.

**Subtlety crítica:** texto livre pode conter QUALQUER outra categoria, usuário cola CPF no chat, foto de RG no DM, dados de saúde em "fale com seu médico". Você é controlador desses dados mesmo sem coletar diretamente.

- **Sensibilidade:** variável. Mensagem médico-paciente é saúde sensível mesmo o app sendo genérico.
- **Base legal:** execução de contrato.
- **Riscos:** vazamento expõe vida íntima, opinião política; e2e-encryption muda enquadramento.
- **Declarar:** "Conteúdo que você cria, guardado enquanto sua conta existir. Exclusão em até 30 dias após apagar."
- **Minimizar:** exclusão real (não soft delete eterno); rate-limit; e2e onde fizer sentido (Signal protocol).

---

## 8. Dados comportamentais (analytics)

**O que cai aqui:** pageview, clique, scroll, hover, sessão, busca interna, histórico de compra, padrão temporal.

**Detecção:**
- Libs: `gtag`, `@vercel/analytics`, `posthog-js`, `mixpanel`, `amplitude`, `plausible`, `umami`, `hotjar`, `clarity`, `fullstory`, `logrocket`
- Pixel: `<img src="https://facebook.com/tr?...">`, GTM containers
- Server: middleware logando `req.url + userId`

**Distinção crítica:**

| Tipo | Base legal típica | Risco |
|---|---|---|
| Agregado próprio (Plausible, Umami, PostHog sem replay) | Legítimo interesse defensável | Baixo |
| Pixel de terceiro (Meta, Google Ads, TikTok) | **Consentimento obrigatório** | Alto, cross-site |
| Session replay (Hotjar, Clarity, FullStory) | Consentimento + masking | **Crítico**, grava tela |

- **Sensibilidade:** média (agregado), alta (com userId), crítica (replay).
- **Riscos:** perfilamento, leak de senha por session replay mal configurado (já aconteceu em Twitter, T-Mobile), shadow profile.
- **Declarar:** lista cada ferramenta nominalmente.
- **Minimizar:** desligar IP no GA4; mask `data-private` em replay; analytics first-party self-hosted; não setar cookie antes do consent.

Detalhe ferramenta-a-ferramenta em `references/14-analytics-tracking.md`.

---

## 9. Dados sensíveis (LGPD art. 11)

Categoria especial, exige **consentimento específico e destacado** (não embutido nos termos) OU hipótese específica do art. 11 II.

**Subcategorias e detecção:**

| Subcategoria | Detecção típica |
|---|---|
| Origem racial/étnica | Campo de autodeclaração (PNAD, vestibular, vagas afirmativas) |
| Religião | Restrição alimentar (kosher/halal/jejum), calendário religioso |
| Política | Doação, filiação, posts |
| Sindical | Desconto em folha |
| Saúde | Wearable (Apple Health, Google Fit), agendamento médico, medicação, plano de saúde |
| Vida sexual/orientação | Tinder, Grindr, OnlyFans; campo gênero extenso |
| Genético | 23andMe-like; raro no BR |
| Biométrico (vinculado a pessoa) | Reconhecimento facial contínuo, voz pra autenticação, digital server-side |

**Detecção no schema:** `health_*`, `medical_*`, `ethnicity`, `religion`, `political_party`, `sexual_orientation`, `gender_identity`; integração com HealthKit/Google Fit; permissions `BODY_SENSORS`, `ACTIVITY_RECOGNITION`.

- **Sensibilidade:** sempre alta. Vazamento gera dano moral presumido; multa LGPD agravada (até R$ 50M).
- **Base legal:** consentimento específico e destacado (art. 11 §1º I) ou hipóteses estritas (saúde por profissional, proteção da vida, prevenção a fraude com biometria).
- **Riscos:** discriminação, chantagem, dano reputacional, criminal.
- **Declarar:** em seção PRÓPRIA da política, separada. "Dados sensíveis, coletamos [X] com sua autorização específica em [tela Y]. Pode revogar em [link Z]."
- **Minimizar:** se possível, **NÃO COLETE**; oferecer "prefiro não dizer"; criptografar at-rest com chave dedicada (envelope encryption); log de acesso (audit trail); RBAC apertado.

---

## 10. Dados inferidos por algoritmo

A categoria mais ignorada e mais perigosa pra disputa judicial. **LGPD art. 20 garante revisão de decisão automatizada.**

**Tipos:**
- Score de crédito interno
- Persona inferida ("usuário de baixa renda", "interessado em viagem")
- Categoria de risco (fraude, churn, inadimplência)
- Preferências derivadas (gênero musical, faixa etária estimada)
- Predições (próxima compra, evasão, doença em healthtech)
- Embeddings/vetores: **sim, vetor é PII** se mapeia pra pessoa
- Output de LLM sobre dados do usuário

**Detecção:** pipelines de ML, `*_score`, `*_segment`, `*_cluster`, `embedding`, `vector`, jobs de scoring, Vertex AI, SageMaker, OpenAI Embeddings, pgvector.

- **Sensibilidade:** alta. Inferência pode revelar categoria sensível sem coletar diretamente (orientação sexual inferida de padrão de navegação, caso real).
- **Base legal:** depende da base do dado original + propósito. Pra decisão automatizada com impacto: exige base + direito à revisão.
- **Riscos:** discriminação algorítmica, bolha de filtro, decisão sem explicabilidade.
- **Declarar:** "Geramos perfis automatizados pra [finalidade]. Você pode solicitar revisão humana em [canal]." Listar decisões automatizadas.
- **Minimizar:** documentar modelo (model card); explicabilidade (SHAP, LIME); human-in-the-loop pra decisão de alto impacto; auditar viés periodicamente; permitir opt-out de personalização.

Detalhe em `references/13-ia-ml-transparencia.md`.

---

## 11. Metadados de comunicação

Quem fala com quem, quando, frequência, duração: **sem conteúdo**.

**O que cai aqui:**
- Grafo social (contatos, follows, friends)
- Frequência de troca
- "Last seen", presença (`isOnline`, `lastActiveAt`)
- Read receipts
- Duração de chamada
- Padrão temporal

**Detecção:** tabelas `messages` com timestamps, `presence`, `last_seen_at`, `read_at`, `call_logs`, `friendships`, `follows`.

- **Sensibilidade:** alta por inferência. Metadado é o pão de cada dia de inteligência (Snowden, "we kill people based on metadata").
- **Base legal:** execução de contrato pra básico; consentimento pra opcionais (read receipt configurável).
- **Riscos:** vazamento de grafo social, doxxing por presença, perseguição doméstica.
- **Declarar:** "Metadados de mensagens, guardados pra entrega. Você pode desativar 'visto por último' e confirmação de leitura."
- **Minimizar:** opt-out de last seen; minimização de logs (não logar quem-pra-quem em debug); TTL em mensagens (padrão Stories).

---

## 12. Dados de terceiros sobre o titular

A categoria mais traiçoeira, você coleta dado de quem **não é** seu usuário.

**Tipos:**
- Lista de contatos importada (cada contato = PII)
- Convites (`fulano@email.com` foi convidado)
- Menções (post falando de outra pessoa)
- Endereços de cobrança/entrega de terceiros
- Beneficiários (seguro, PIX favorito, dependente)
- Fotos com pessoas que não usam o app (reconhecimento facial)
- Webhook de terceiros (Stripe, Mercado Pago) mandando dados

**Detecção:** features "convidar amigos", `contacts` permission, import CSV, "compartilhar com..."

- **Sensibilidade:** alta legalmente. Você é controlador de dado de quem NÃO consentiu.
- **Base legal:** difícil. Legítimo interesse pra convite pontual (1 mensagem, opt-out fácil); **proibido** pra perfilamento de não-usuário.
- **Riscos:** ANPD multa pesado (caso TIM/Pegasus); titular não-usuário pode exercer direito sem ter aceitado nada.
- **Declarar:** "Quando você convida alguém, usamos o e-mail/telefone APENAS pra enviar o convite. Não armazenamos pra outro fim. A pessoa pode pedir exclusão em [canal público]."
- **Minimizar:** **NÃO importe lista inteira**, peça contato específico via picker nativo; não construa shadow profile; oferecer canal público pra titular não-usuário (LGPD vale pra ele).

---

## Como a skill usa essa taxonomia

Pra cada projeto, a skill cruza o código contra cada categoria (`rg` por palavras-chave) e gera inventário no formato:

```yaml
- category: "1. Identidade e contato"
  items: ["email", "name", "cpf"]
  detected_in:
    - "supabase/migrations/001_users.sql"
    - "app/(auth)/signup/page.tsx"
  sensitivity: "média"
  legal_basis: "execução de contrato (art. 7º V)"
  retention: "conta ativa + 5 anos (fiscal)"
  minimization: ["cpf opcional", "apple relay aceito"]
  public_declaration: "..."
```

Detalhe da geração programática em `references/12-transparencia-radical.md` seção 10.

## Referências externas

- [Apple App Privacy Details](https://developer.apple.com/app-store/app-privacy-details/)
- [Google Play Data Safety](https://support.google.com/googleplay/android-developer/answer/10787469)
- [Mozilla Lean Data Practices](https://www.mozilla.org/en-US/about/policy/lean-data/)
- [EFF Cover Your Tracks](https://coveryourtracks.eff.org/)
- [W3C Privacy Threat Model](https://www.w3.org/TR/privacy-threat-model/)
- [LGPD arts. 5º e 11 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm)
