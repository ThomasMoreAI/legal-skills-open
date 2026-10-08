# 06: Cookies e Banner de Consentimento (Guia ANPD)

> Fonte canônica: **Guia Orientativo "Cookies e Proteção de Dados Pessoais"**: ANPD, 22/11/2024, atualizado em 23/01/2025. PDF: [gov.br/anpd/.../guia-orientativo-cookies](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf).

## Classificação de cookies (ANPD)

### Por entidade
- **Próprios (first-party):** definidos pelo domínio que o usuário visita.
- **Terceiros (third-party):** definidos por outro domínio (Google, Meta, Hotjar). Maior exposição → tratar com mais cautela.

### Por persistência
- **Sessão:** expiram ao fechar o navegador.
- **Persistentes:** ficam por X dias/meses/anos.

### Por finalidade: **classificação que decide se precisa de consentimento**

| Categoria | Função | Exemplo | Consentimento? |
|---|---|---|---|
| **Estritamente necessários** | Funcionamento básico: sessão, carrinho, segurança CSRF, balanceamento | `session_id`, `csrf_token`, `__Host-cart` | **NÃO** (base: art. 7º V execução de contrato ou IX legítimo interesse) |
| **Funcionais / preferência** | Lembrar idioma, tema, layout | `lang=pt-BR`, `theme=dark` | **SIM** (estritamente, são opcionais) |
| **Analíticos / desempenho** | GA4, Hotjar, métricas de uso | `_ga`, `_hjSession` | **SIM** (ANPD recomenda; alguns escritórios admitem legítimo interesse pra analytics anonimizados) |
| **Publicidade / marketing / rastreio cross-site** | Meta Pixel, Google Ads, remarketing | `_fbp`, `_gcl_au`, `IDE` | **SIM, obrigatoriamente**, consentimento livre, informado, inequívoco |

## Requisitos do BANNER (ANPD)

1. **Quando é obrigatório:** sempre que houver cookie não-essencial. Site **só com cookies estritamente necessários** não precisa de banner, mas continua precisando de **política de cookies** (princípio da transparência).
2. **Padrão: cookies não-essenciais DESATIVADOS**, proibido pré-marcar checkboxes ou contar visita como consentimento.
3. **Botão "Rejeitar" tão visível quanto "Aceitar"**, mesma cor, tamanho, posição. Proibido esconder "rejeitar" atrás de "configurar" enquanto "aceitar" é grande e chamativo (**dark pattern** explicitamente vedado pela ANPD).
4. **Estrutura em 2 camadas:**
   - **1ª camada (banner):** botões equivalentes "Aceitar todos", "Rejeitar não-essenciais" e "Configurar/Gerenciar".
   - **2ª camada (modal):** granularidade por categoria, com descrição clara e toggle individual.
5. **Granularidade equilibrada:** nem botão único (proibido), nem lista de 200 cookies que causa fadiga (desencorajado).
6. **Revogação tão fácil quanto consentir** (art. 8º §5º). Botão "Gerenciar preferências" sempre acessível no rodapé.
7. **Idioma:** política em **português brasileiro**. Oferecer só em outro idioma é prática a evitar.
8. **Granular por finalidade, não por cookie individual.**
9. **Sem walls:** não condicionar o acesso ao site ao aceite de cookies não-essenciais (**cookie wall** problemático).

## Padrões VEDADOS pela ANPD

| Anti-padrão | Por quê é proibido |
|---|---|
| Checkbox pré-marcado | Manifestação não-inequívoca; art. 8º §3º |
| "Aceitar e continuar" sem alternativa simétrica | Vicia o consentimento; viola art. 8º caput |
| Botão "Rejeitar" em link de rodapé enquanto "Aceitar" é botão grande | Falta de paridade; dark pattern |
| Banner que precisa scroll pra ver "rejeitar" | Idem |
| Cookie wall (bloquear acesso sem aceite de não-essenciais) | Condiciona uso a consentimento desnecessário |
| Consentimento por mera continuação da navegação | Não é manifestação afirmativa |
| Fluxo de revogação mais complexo que o de consentir | Viola art. 8º §5º |

## O que a POLÍTICA DE COOKIES deve conter

1. Definição clara do que são cookies (linguagem acessível).
2. **Lista das categorias usadas** e finalidade de cada uma.
3. **Identificação dos cookies de terceiros** com link pra política do terceiro (Google, Meta).
4. **Tempo de retenção** por cookie (sessão vs persistente, com dias/meses).
5. **Como gerenciar/revogar** no próprio site e nas configurações do navegador (links pra Chrome, Firefox, Safari, Edge).
6. **Base legal** de cada categoria.
7. **Data da última atualização** + histórico de versões.

## Estrutura do componente banner: Next.js / React (conceito)

> Template completo em `templates/banner-cookies.tsx`.

```tsx
<CookieBanner>
  {/* 1ª camada */}
  <p>
    Usamos cookies estritamente necessários para o funcionamento deste site.
    Cookies opcionais (analíticos e de marketing) só serão usados com seu consentimento.
    <Link href="/legal/cookies">Saiba mais</Link>
  </p>
  <Button onClick={acceptAll}>Aceitar todos</Button>
  <Button onClick={rejectNonEssential}>Rejeitar opcionais</Button>
  <Button onClick={openPreferences}>Configurar</Button>
</CookieBanner>

{/* 2ª camada (modal) */}
<PreferencesModal>
  <Toggle name="essential" disabled value={true}>
    Estritamente necessários (sempre ativos)
  </Toggle>
  <Toggle name="functional">Funcionais</Toggle>
  <Toggle name="analytics">Analíticos</Toggle>
  <Toggle name="marketing">Publicidade</Toggle>

  <Button onClick={saveAndClose}>Salvar preferências</Button>
</PreferencesModal>
```

### Comportamento esperado

1. Antes do consentimento: **nenhum cookie não-essencial é setado**.
2. Após "Aceitar todos": setar todos, registrar em `consent_log` (timestamp, IP truncado, versão do termo).
3. Após "Rejeitar opcionais": setar APENAS essenciais. Idem registro.
4. Após "Configurar + Salvar": setar conforme toggles. Idem registro.
5. Rodapé sempre tem link "Gerenciar preferências de cookies" → reabre modal.
6. Banner reaparece se a **política for atualizada** com mudança material.

### Persistência do consentimento

- Guardar em **cookie próprio first-party** (`__cookie_consent`) com:
  ```json
  {
    "v": "2026-05-24",            // versão da política
    "ts": "2026-05-24T14:32:11Z", // timestamp do consentimento
    "essential": true,
    "functional": false,
    "analytics": true,
    "marketing": false
  }
  ```
- Backend: row em `consent_log` (schema em `templates/endpoints-direitos/consent-log-schema.sql`).

## Cookies em servidor / SSR (Next.js App Router)

- Cookies setados via `Set-Cookie` no response devem respeitar a mesma classificação.
- Se o site faz **SSR**, o servidor precisa saber o estado de consentimento ANTES de injetar tags de analytics no HTML. Padrão: ler o cookie `__cookie_consent` no Server Component / middleware e renderizar condicionalmente `<Script>` do GA4 / Meta Pixel.
- **NÃO injetar `<script>` de tracking se o consentimento estiver ausente ou negado.**

## Auditoria periódica

A cada release que toque o frontend:
- [ ] Inspecionar `document.cookie` em modo anônimo, antes de consentimento. Deve haver **só essenciais**.
- [ ] Após "Rejeitar opcionais": confirmar que GA4/Meta/Hotjar não foram carregados.
- [ ] Após "Aceitar": confirmar que carregaram conforme declarado na política.
- [ ] Verificar se há cookies não listados na política (drift).

Ferramentas úteis: **Cookiebot Scanner**, **OneTrust Cookie Audit**, ou simples `Application > Cookies` do DevTools.

## Referências externas

- [Guia Orientativo Cookies (ANPD (PDF))](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf)
- [Página oficial do Guia](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_orientativo_cookies_e_protecao_de_dados_pessoais)
- [LGPD Art. 8º (consentimento) (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm#art8)
