# Checklist: Segurança Mínima (art. 46-49 LGPD)

> Controles mínimos esperados de qualquer app em produção. Baseado no **Guia de Segurança da Informação para ATPP** da ANPD (jun/2024, atualizado jan/2025). Ter esses controles **antes** do incidente vira **atenuante na dosimetria** (Res. CD/ANPD nº 4/2023).

## 1. Transporte: criptografia em trânsito

- [ ] **HTTPS obrigatório** em todas as rotas (redirect HTTP → HTTPS)
- [ ] **TLS 1.2 mínimo** (preferível 1.3)
- [ ] **HSTS** habilitado com `max-age` ≥ 1 ano
- [ ] Certificado válido renovado automaticamente (Let's Encrypt / Caddy / Vercel)
- [ ] APIs internas entre serviços também via TLS (não confiar na rede privada cegamente)

## 2. Armazenamento: criptografia em repouso

- [ ] **Banco de dados criptografado em repouso** (Postgres com `pgcrypto` ou disco LUKS/AWS RDS encryption)
- [ ] **Backups criptografados** (não basta o banco estar)
- [ ] **Arquivos de mídia** (S3, R2, MinIO) com encryption at rest
- [ ] **Logs** que contêm PII também criptografados / minimizados
- [ ] Discos de VMs com encryption (Hetzner suporta, AWS suporta nativo)

## 3. Autenticação e autorização

### Pra usuários finais
- [ ] Hash de senha forte: **argon2id** (preferido) ou **bcrypt cost ≥ 12**
- [ ] **Nunca armazenar senha em texto claro**, nem em log, nem em erro
- [ ] Política mínima de senha (8+ caracteres, sem máximo absurdo, sem regras burras tipo "obrigado caractere especial")
- [ ] **2FA opcional ao usuário** (TOTP / WebAuthn)
- [ ] **Rate limiting** em login, signup, password reset
- [ ] Lockout após N tentativas (com cuidado pra não virar DoS)
- [ ] Token de sessão com expiração razoável; rotação após login

### Pra admin / staff
- [ ] **2FA obrigatório** em painel admin
- [ ] **2FA obrigatório** em GitHub, GitLab, Vercel, AWS console, Hetzner
- [ ] **2FA obrigatório** em banco (psql tunnel via SSH com chave + 2FA na máquina)
- [ ] **Menor privilégio**, admin só faz o que precisa, dev não tem prod, etc.
- [ ] **Onboarding/offboarding documentado**, revogar acessos ao desligar
- [ ] **Revisão trimestral** de quem tem acesso ao quê

## 4. Gestão de segredos

- [ ] **Nenhum segredo no repo**, `.env` no `.gitignore`, sempre
- [ ] **Secret manager** em prod (AWS Secrets Manager, Vercel env vars, Doppler, etc.)
- [ ] **Rotação periódica** de credenciais críticas (DB, API keys de terceiros)
- [ ] **Auditoria de exposição**: rodar `gitleaks` ou `trufflehog` periodicamente
- [ ] Cuidado especial com `NEXT_PUBLIC_*` (vai pro bundle do cliente, nada secreto aqui!)

## 5. Atualizações e dependências

- [ ] **Dependabot / Renovate** ativo (PRs automáticos)
- [ ] CVE crítico em dep → ação em **24-72h**
- [ ] SO da VM atualizado (`unattended-upgrades` no Ubuntu/Debian)
- [ ] Imagens Docker baseadas em **alpine** ou **distroless** quando possível
- [ ] `npm audit` / `pip audit` / `cargo audit` no CI

## 6. Logs e monitoramento

- [ ] **Logs centralizados** (Logflare, Datadog, BetterStack, Loki): NÃO confiar em `console.log` em prod
- [ ] **Logs de autenticação** (login, logout, falha, password reset)
- [ ] **Logs de alteração de dado pessoal** (quem mudou o quê e quando)
- [ ] **Logs de acesso administrativo** (quem rodou query em prod, quem acessou conta de cliente)
- [ ] **Retenção mínima** de logs por 6 meses (Marco Civil art. 15, provedor de aplicação). Provedor de conexão = 1 ano (art. 13). Pode reter mais com base legal própria (segurança), justificando em RIPD.
- [ ] **Alertas** em eventos anômalos (login de país estranho, picos de erro 500, exfiltração)
- [ ] **NÃO logar PII desnecessária**, minimizar mesmo em log (mascarar e-mail, hash CPF)

## 7. Backup e recuperação

- [ ] **Backup automático** do banco (diário no mínimo, hora-hora pra apps críticos)
- [ ] **Backups armazenados off-site** (não no mesmo provedor / região)
- [ ] **Backups criptografados**
- [ ] **Teste de restore trimestral**, backup que não restaura não é backup
- [ ] **Política de retenção** de backup definida (não guardar pra sempre, purga respeitando matriz de retenção)
- [ ] **Plano de DR (Disaster Recovery)** documentado, mesmo que mínimo

## 8. Network e infraestrutura

- [ ] **Firewall** com porta mínima exposta (80, 443, 22 com restrição de IP)
- [ ] **SSH** apenas por chave, **senha desabilitada**
- [ ] **Fail2ban** ou equivalente em VPS
- [ ] **WAF** em produção (Cloudflare, Vercel Firewall, AWS WAF)
- [ ] **Rate limiting global** no edge (Cloudflare / Vercel)
- [ ] **CORS** configurado restritivo (não `*` em prod)
- [ ] **CSP** (Content Security Policy) restritivo

## 9. Aplicação: boas práticas

- [ ] **Validação de input** server-side (nunca confiar no cliente)
- [ ] **Sanitização** contra XSS (preferir frameworks que escapam por padrão: React, Vue)
- [ ] **Queries parametrizadas** (ORM ou prepared statements): **sem SQL string concat**
- [ ] **CSRF tokens** em forms tradicionais
- [ ] **Cookies**: `HttpOnly`, `Secure`, `SameSite=Lax` ou `Strict`
- [ ] **Sessões expiram** (idle + absoluta)
- [ ] **Headers de segurança**: HSTS, X-Content-Type-Options, X-Frame-Options, Referrer-Policy, Permissions-Policy
- [ ] **Erros não vazam stack trace** em produção
- [ ] **Sentry / Bugsnag** sem PII (configurar `beforeSend` pra mascarar)

## 10. Operadores (terceiros)

- [ ] **DPA assinado** com cada operador que processa PII (AWS, Vercel, Stripe, Mailgun, OpenAI, Sentry, etc.)
- [ ] **SCC da ANPD** anexada nos DPAs de operadores estrangeiros
- [ ] **Lista mantida** de subprocessadores (cascata)
- [ ] **Notificação de mudança** de subprocessador, boa cláusula no DPA

## 11. Pessoas (administrativo)

- [ ] **Termo de confidencialidade** assinado por colaboradores (mesmo freelancers)
- [ ] **Política interna de uso** de equipamento (BYOD: criptografia de disco, bloqueio de tela, etc.)
- [ ] **Treinamento anual** de LGPD pra equipe (mesmo que informal: 1h de workshop com material)
- [ ] **Política de mesa limpa** (não deixar PII em pos-it)
- [ ] **Política de uso de IA** (não jogar dados de cliente em ChatGPT sem DPA)

## 12. Documentação obrigatória

- [ ] **Política de Segurança da Informação (PSI)** publicada (mesmo que simplificada pra ATPP)
- [ ] **Política de Privacidade** pública
- [ ] **Política de Cookies** pública
- [ ] **ROPA** atualizado (interno)
- [ ] **RIPD** pra tratamentos de risco (interno)
- [ ] **Runbook de incidente** atualizado (interno)
- [ ] **Plano de continuidade** mínimo (interno)

## 13. Mobile e dispositivos

- [ ] **MDM** (Mobile Device Management) se há frota corporativa
- [ ] **BYOD policy** se permite dispositivo pessoal
- [ ] **Bloqueio de tela** obrigatório em equipamento de trabalho
- [ ] **Criptografia de disco** em laptops (BitLocker, FileVault, LUKS)
- [ ] **Remote wipe** disponível pra dispositivos perdidos

## 14. Quando algo dá errado

- [ ] **Runbook de incidente** acessível pra equipe
- [ ] **Cadeia de comunicação** definida (quem aciona quem)
- [ ] **SEI!ANPD** configurado e responsável tem Gov.br nível Bronze+
- [ ] **Template de comunicação** ao titular já redigido
- [ ] **Contatos dos operadores** mapeados (canal de incidente de cada um)

---

## Resumo executivo (versão "se eu só fizer 10 coisas")

Pra um app pequeno, o **mínimo viável** é:

1. HTTPS em tudo
2. Senha hash forte + 2FA em admin
3. Banco criptografado em repouso (RDS encryption ou disco LUKS)
4. Backup automático off-site + restore testado
5. Logs centralizados (mínimo 90 dias) com alerta básico
6. Secrets fora do repo (env vars / secret manager)
7. Dependabot/Renovate ativo
8. WAF/Cloudflare no edge + rate limiting
9. DPA + SCC com cada operador estrangeiro
10. Runbook de incidente + acesso configurado no SEI!ANPD

Tudo isso garantido = atenuante grande na dosimetria. Não garantido = se acontecer incidente, multa pesada vira mais provável.
