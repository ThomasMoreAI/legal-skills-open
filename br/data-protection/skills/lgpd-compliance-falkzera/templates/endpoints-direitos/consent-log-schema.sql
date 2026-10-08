-- =============================================================================
-- consent_log + audit_log schema, lgpd-compliance
-- =============================================================================
-- Persistência de consentimentos (art. 8º) e trilha de auditoria de
-- atendimento aos direitos do titular (art. 18), Postgres.
--
-- Aplicar com:  psql -f schema-consent-log.sql
-- =============================================================================

-- Extensões úteis -------------------------------------------------------------
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- =============================================================================
-- 1. consent_log, registro imutável de TODA decisão de consentimento
-- =============================================================================
-- Uma linha por evento de consentimento (concedido OU revogado), por finalidade.
-- Tabela append-only, nunca UPDATE/DELETE; valores corrigidos = novo registro.

CREATE TABLE IF NOT EXISTS consent_log (
    id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    -- titular (pode ser anônimo no primeiro consentimento de cookies)
    user_id         uuid REFERENCES users(id) ON DELETE SET NULL,
    anonymous_id    text,                       -- ID do cookie pré-login

    -- categoria do consentimento
    purpose         text NOT NULL,              -- ex: 'cookies_analytics', 'newsletter', 'marketing_push'

    -- decisão
    granted         boolean NOT NULL,           -- true = concedido, false = revogado
    policy_version  text NOT NULL,              -- versão da política aceita (ex: '2026-05-24')

    -- contexto da coleta (mínimo necessário, sem excesso)
    collected_via   text NOT NULL,              -- 'cookie_banner', 'checkbox_signup', 'settings_page', 'api'
    ip_truncated    inet,                       -- IP mascarado (último octeto/64 zerados)
    user_agent      text,

    -- timestamp imutável
    created_at      timestamptz NOT NULL DEFAULT now(),

    -- garantia de imutabilidade lógica
    CONSTRAINT consent_log_anon_xor_user CHECK (
        user_id IS NOT NULL OR anonymous_id IS NOT NULL
    )
);

CREATE INDEX IF NOT EXISTS consent_log_user_idx
    ON consent_log (user_id, purpose, created_at DESC);

CREATE INDEX IF NOT EXISTS consent_log_anon_idx
    ON consent_log (anonymous_id, purpose, created_at DESC)
    WHERE anonymous_id IS NOT NULL;

COMMENT ON TABLE consent_log IS
    'Registro append-only de consentimentos do titular (LGPD art. 8º). Nunca atualizar nem deletar.';

-- View de "estado atual" do consentimento (último evento por user × purpose)
CREATE OR REPLACE VIEW consent_current AS
SELECT DISTINCT ON (COALESCE(user_id::text, anonymous_id), purpose)
    user_id,
    anonymous_id,
    purpose,
    granted,
    policy_version,
    created_at AS last_change_at
FROM consent_log
ORDER BY
    COALESCE(user_id::text, anonymous_id),
    purpose,
    created_at DESC;

-- =============================================================================
-- 2. dsr_request, Data Subject Request (pedidos do art. 18)
-- =============================================================================

CREATE TYPE dsr_type AS ENUM (
    'confirmation',     -- art. 18 I
    'access',           -- art. 18 II
    'correction',       -- art. 18 III
    'anonymization',    -- art. 18 IV
    'portability',      -- art. 18 V
    'deletion',         -- art. 18 VI
    'sharing_info',     -- art. 18 VII
    'consent_info',     -- art. 18 VIII
    'consent_revoke',   -- art. 18 IX
    'auto_decision_review'  -- art. 20
);

CREATE TYPE dsr_status AS ENUM (
    'received',
    'verifying_identity',
    'in_progress',
    'completed',
    'rejected',         -- com justificativa
    'partially_completed' -- ex: parte excluída, parte retida por obrigação legal
);

CREATE TABLE IF NOT EXISTS dsr_request (
    id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    user_id         uuid REFERENCES users(id) ON DELETE SET NULL,
    requester_email text NOT NULL,              -- pode pedir mesmo sem conta

    request_type    dsr_type NOT NULL,
    status          dsr_status NOT NULL DEFAULT 'received',

    -- conteúdo livre do pedido (sanitizar antes de exibir)
    notes           text,

    -- atendimento
    handled_by      text,                       -- quem (e-mail do operador)
    response        text,                       -- resposta formal enviada
    response_sent_at timestamptz,

    -- SLAs
    received_at     timestamptz NOT NULL DEFAULT now(),
    due_at          timestamptz NOT NULL,       -- regime geral = +15d; ATPP = +30d
    completed_at    timestamptz,

    -- audit
    rejection_reason text,                      -- preencher se rejected
    retention_reason text                       -- preencher se partially_completed
);

CREATE INDEX IF NOT EXISTS dsr_request_status_idx
    ON dsr_request (status, due_at);

CREATE INDEX IF NOT EXISTS dsr_request_user_idx
    ON dsr_request (user_id, received_at DESC);

COMMENT ON TABLE dsr_request IS
    'Pedidos de exercício de direitos do titular (LGPD art. 18). SLA: regime geral 15d, ATPP 30d.';

-- =============================================================================
-- 3. audit_log, toda ação sobre dado pessoal
-- =============================================================================

CREATE TYPE audit_action AS ENUM (
    'data_export',
    'data_correction',
    'data_anonymization',
    'data_deletion',
    'consent_change',
    'admin_data_access',
    'auto_decision',
    'auto_decision_review'
);

CREATE TABLE IF NOT EXISTS audit_log (
    id              bigserial PRIMARY KEY,

    actor_type      text NOT NULL,              -- 'titular', 'admin', 'system', 'cron'
    actor_id        text,                       -- user_id ou e-mail do admin
    target_user_id  uuid REFERENCES users(id) ON DELETE SET NULL,

    action          audit_action NOT NULL,
    entity          text NOT NULL,              -- tabela ou recurso afetado
    entity_id       text,

    -- detalhes (idealmente sem PII, mas se PII for inevitável, mascarar)
    before_value    jsonb,
    after_value     jsonb,
    metadata        jsonb,

    ip_truncated    inet,
    user_agent      text,

    created_at      timestamptz NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS audit_log_target_idx
    ON audit_log (target_user_id, created_at DESC);

CREATE INDEX IF NOT EXISTS audit_log_action_idx
    ON audit_log (action, created_at DESC);

COMMENT ON TABLE audit_log IS
    'Trilha de auditoria de operações sobre dados pessoais. Retenção mínima recomendada: 12 meses (Marco Civil).';

-- =============================================================================
-- 4. retention_policy, matriz "dado × base × prazo"
-- =============================================================================

CREATE TYPE retention_action AS ENUM (
    'hard_delete',
    'anonymize',
    'retain_with_basis'
);

CREATE TABLE IF NOT EXISTS retention_policy (
    data_category    text PRIMARY KEY,          -- ex: 'profile_basic', 'nfe', 'log_acesso'
    legal_basis      text NOT NULL,             -- ex: 'lgpd_art7_V_contrato'
    legal_source     text NOT NULL,             -- ex: 'Lei 12.965/2014 art. 13'
    retention_days   integer,                   -- NULL = enquanto durar a relação
    on_delete_action retention_action NOT NULL,
    justification    text NOT NULL,             -- texto exibido ao titular na exclusão

    updated_at       timestamptz NOT NULL DEFAULT now()
);

-- Seed inicial (ajustar por projeto)
INSERT INTO retention_policy (data_category, legal_basis, legal_source, retention_days, on_delete_action, justification)
VALUES
    ('profile_basic',
     'lgpd_art7_V_contrato',
     'LGPD art. 7º V',
     180,
     'hard_delete',
     'Excluído. Mantemos por 180 dias apenas em caso de recuperação solicitada por você.'),

    ('nota_fiscal',
     'lgpd_art7_II_obrigacao_legal',
     'Decreto 7.212/2010 art. 447; CTN art. 173',
     365 * 5,
     'retain_with_basis',
     'Retido por 5 anos para cumprimento de obrigação fiscal (Decreto 7.212/2010).'),

    ('log_acesso_aplicacao',
     'lgpd_art7_II_obrigacao_legal',
     'Marco Civil, Lei 12.965/2014 art. 15',
     180,
     'retain_with_basis',
     'Retido por 6 meses (Marco Civil art. 15, provedor de aplicação).'),

    ('log_conexao',
     'lgpd_art7_II_obrigacao_legal',
     'Marco Civil, Lei 12.965/2014 art. 13',
     365,
     'retain_with_basis',
     'Retido por 1 ano (Marco Civil art. 13, só se aplica a provedor de conexão).'),

    ('newsletter_consent',
     'lgpd_art7_I_consentimento',
     'LGPD art. 7º I + art. 8º §5º',
     NULL,
     'hard_delete',
     'Excluído ao revogar consentimento.')
ON CONFLICT (data_category) DO NOTHING;

COMMENT ON TABLE retention_policy IS
    'Matriz dado × base × prazo. Consultada por rotina de exclusão automática e pelo fluxo "Excluir conta".';

-- =============================================================================
-- 5. Função de truncamento de IP (privacy-friendly)
-- =============================================================================
-- Use ao inserir IP em consent_log/audit_log. Zera último octeto IPv4 e
-- últimos 64 bits IPv6, perde precisão de host, mantém prefixo de rede.

CREATE OR REPLACE FUNCTION truncate_ip(ip inet)
RETURNS inet AS $$
BEGIN
    IF family(ip) = 4 THEN
        RETURN set_masklen(ip, 24);
    ELSE
        RETURN set_masklen(ip, 64);
    END IF;
END;
$$ LANGUAGE plpgsql IMMUTABLE;

-- =============================================================================
-- 6. tos_acceptance, registro de aceite de Termos de Uso e demais documentos
-- =============================================================================
-- Prova jurídica do clickwrap. Append-only.
-- Cada VERSÃO aceita gera uma linha. Re-aceite por mudança material = nova linha.

CREATE TABLE IF NOT EXISTS tos_acceptance (
    id              bigserial PRIMARY KEY,

    user_id         uuid REFERENCES users(id) ON DELETE SET NULL,

    -- qual documento
    document_type   text NOT NULL,         -- 'terms_of_use' | 'privacy_policy' | 'cookies' | 'dpa' | ...
    document_version text NOT NULL,        -- '2026-05-24' ou 'v3.2.0'
    document_hash   text NOT NULL,         -- SHA-256 do conteúdo imutável arquivado

    -- prova do ato
    accepted_at     timestamptz NOT NULL DEFAULT now(),
    ip_truncated    inet,                  -- /24 IPv4 ou /48 IPv6 (LGPD minimização)
    user_agent      text,
    acceptance_method text NOT NULL,       -- 'clickwrap' | 'scrollwrap' | 'reaccept_modal' | 'sign_in_wrap'

    -- contexto (sem PII desnecessária)
    context         jsonb                  -- {flow: 'signup', locale: 'pt-BR', ...}
);

CREATE INDEX IF NOT EXISTS tos_acceptance_user_idx
    ON tos_acceptance (user_id, document_type, accepted_at DESC);

CREATE INDEX IF NOT EXISTS tos_acceptance_version_idx
    ON tos_acceptance (document_type, document_version);

COMMENT ON TABLE tos_acceptance IS
    'Prova jurídica do aceite de Termos de Uso, Política de Privacidade, etc. Append-only. Retenção: durante relação contratual + 5 anos (CDC art. 27).';

-- View útil pra saber a versão mais recente aceita por cada usuário
CREATE OR REPLACE VIEW tos_current_acceptance AS
SELECT DISTINCT ON (user_id, document_type)
    user_id,
    document_type,
    document_version,
    document_hash,
    accepted_at,
    acceptance_method
FROM tos_acceptance
ORDER BY user_id, document_type, accepted_at DESC;

-- =============================================================================
-- 7. tos_versions, registro imutável das versões de cada documento publicado
-- =============================================================================
-- Permite reconstituir, em juízo, qual o conteúdo aceito por um usuário em uma data.
-- Conteúdo arquivado idealmente em storage imutável (S3 Object Lock, Git tag, etc.)
-- referenciado por document_url. Hash garante integridade.

CREATE TABLE IF NOT EXISTS tos_versions (
    document_type    text NOT NULL,        -- 'terms_of_use' | 'privacy_policy' | ...
    document_version text NOT NULL,        -- '2026-05-24' ou 'v3.2.0'
    document_hash    text NOT NULL UNIQUE, -- SHA-256
    document_url     text NOT NULL,        -- URL versionada permanente
    effective_from   timestamptz NOT NULL,
    effective_to     timestamptz,          -- NULL = atual; preenchido ao publicar nova
    changelog        text,                 -- resumo das mudanças
    is_material      boolean NOT NULL DEFAULT false, -- exige re-aceite ativo?
    created_at       timestamptz NOT NULL DEFAULT now(),

    PRIMARY KEY (document_type, document_version)
);

COMMENT ON TABLE tos_versions IS
    'Histórico imutável de versões publicadas. Documento físico arquivado em document_url. Retenção: 5+ anos após sair de vigor, ou enquanto houver tos_acceptance apontando.';

-- =============================================================================
-- 8. notice_takedown, registro de notificações extrajudiciais (Marco Civil)
-- =============================================================================
-- Para apps com UGC. Base: arts. 19-21 MCI + Tema 987 STF (2025).

CREATE TYPE takedown_category AS ENUM (
    'crime_honra',            -- requer ordem judicial (Nível 1 STF)
    'ilicito_geral',          -- art. 21 expandido (Nível 2)
    'dever_cuidado',          -- terrorismo, racismo, CSAM, etc (Nível 3)
    'nudez_nao_consentida',   -- art. 21 original
    'direito_autoral',
    'marca',
    'privacidade'
);

CREATE TYPE takedown_status AS ENUM (
    'received',
    'in_review',
    'awaiting_publisher_response',
    'removed',
    'denied',
    'counter_notified',
    'restored'
);

CREATE TABLE IF NOT EXISTS notice_takedown (
    id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),

    -- notificante
    notifier_name   text NOT NULL,
    notifier_doc    text NOT NULL,         -- CPF/CNPJ
    notifier_email  text NOT NULL,
    is_representative boolean NOT NULL DEFAULT false,
    requested_anonymity boolean NOT NULL DEFAULT false,
    anonymity_justification text,

    -- conteúdo
    content_url     text NOT NULL,
    content_internal_id text,
    publisher_user_id uuid REFERENCES users(id) ON DELETE SET NULL,
    publication_date timestamptz,

    -- fundamento
    category        takedown_category NOT NULL,
    fundamentation  text NOT NULL,         -- texto livre

    -- workflow
    status          takedown_status NOT NULL DEFAULT 'received',
    received_at     timestamptz NOT NULL DEFAULT now(),
    sla_due_at      timestamptz NOT NULL,  -- 24h urgência, 48-72h padrão
    resolved_at     timestamptz,
    resolution_notes text,

    -- contraditório
    publisher_notified_at timestamptz,
    publisher_response_due timestamptz,
    publisher_response text
);

CREATE INDEX IF NOT EXISTS notice_takedown_status_idx
    ON notice_takedown (status, sla_due_at);

CREATE INDEX IF NOT EXISTS notice_takedown_category_idx
    ON notice_takedown (category, received_at DESC);

COMMENT ON TABLE notice_takedown IS
    'Notificações extrajudiciais de conteúdo (Marco Civil arts. 19-21 + Tema 987 STF 2025). Base do relatório de transparência anual.';

-- =============================================================================
-- 9. Rotina de purga periódica (chamar via pg_cron / Airflow / Supabase Cron)
-- =============================================================================
-- Idéia: executar diariamente, eliminando consent_log de usuários anônimos
-- antigos (>2 anos) e audit_log conforme política de retenção.

-- Exemplo (ajustar):
-- DELETE FROM consent_log
--  WHERE user_id IS NULL
--    AND created_at < now() - interval '2 years';
--
-- DELETE FROM audit_log
--  WHERE created_at < now() - interval '12 months';
