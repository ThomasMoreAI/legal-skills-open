/**
 * GET /api/legal/export
 * =====================================================================
 * Direito de portabilidade (LGPD art. 18 V) + acesso (art. 18 II).
 *
 * Stack: Next.js 14+ (App Router) + TypeScript.
 * Cole em: app/api/legal/export/route.ts
 *
 * Comportamento:
 *  - exige usuário autenticado (sessão / JWT)
 *  - retorna JSON estruturado com TUDO que o app sabe sobre o titular
 *  - NÃO inclui dados inferidos por algoritmo (segredo industrial, art. 18 V)
 *  - registra audit_log da operação
 *  - SLA: imediato (regime geral) ou até 15 dias se precisar enriquecer
 *    de fontes assíncronas
 */

import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';     // ajuste pra seu provedor de sessão
import { db } from '@/lib/db';
import { logAudit } from '@/lib/audit';

export const runtime = 'nodejs';
export const dynamic = 'force-dynamic';

export async function GET(req: NextRequest) {
    const session = await auth();
    if (!session?.user?.id) {
        return NextResponse.json({ error: 'unauthorized' }, { status: 401 });
    }

    const userId = session.user.id;

    // === 1. Coletar tudo que pertence ao titular =============================
    const [
        profile,
        consents,
        transactions,
        supportTickets,
        deviceLogins,
    ] = await Promise.all([
        db.users.findUnique({
            where: { id: userId },
            select: {
                id: true,
                email: true,
                name: true,
                phone: true,
                cpf: true,
                created_at: true,
                updated_at: true,
                // ATENÇÃO: NÃO selecionar password_hash, MFA secret, etc.
            },
        }),
        db.consent_log.findMany({
            where: { user_id: userId },
            select: {
                purpose: true,
                granted: true,
                policy_version: true,
                collected_via: true,
                created_at: true,
            },
            orderBy: { created_at: 'desc' },
        }),
        db.transactions.findMany({
            where: { user_id: userId },
            select: {
                id: true,
                amount: true,
                status: true,
                created_at: true,
            },
            orderBy: { created_at: 'desc' },
        }),
        db.support_tickets.findMany({
            where: { user_id: userId },
            select: { id: true, subject: true, created_at: true },
            orderBy: { created_at: 'desc' },
        }),
        db.audit_log.findMany({
            where: { target_user_id: userId, action: 'admin_data_access' },
            select: {
                actor_type: true,
                action: true,
                entity: true,
                created_at: true,
            },
            orderBy: { created_at: 'desc' },
            take: 200,
        }),
    ]);

    // === 2. Montar payload com schema documentado ============================
    const payload = {
        $schema: 'https://example.com/schemas/lgpd-export/v1.json',
        $generated_at: new Date().toISOString(),
        $about: {
            controller: process.env.NEXT_PUBLIC_CONTROLLER_NAME,
            controller_doc: process.env.NEXT_PUBLIC_CONTROLLER_DOC,
            dpo_contact: process.env.NEXT_PUBLIC_DPO_CONTACT,
            legal_basis: 'LGPD art. 18 V (portabilidade) e art. 18 II (acesso)',
            scope:
                'Inclui dados que você forneceu e que coletamos objetivamente. NÃO inclui inferências algorítmicas (segredo industrial).',
        },
        profile,
        consents,
        transactions,
        supportTickets,
        adminAccessLogs: deviceLogins,
    };

    // === 3. Registrar audit ==================================================
    await logAudit({
        actor_type: 'titular',
        actor_id: userId,
        target_user_id: userId,
        action: 'data_export',
        entity: 'lgpd_export',
        ip: req.headers.get('x-forwarded-for') ?? undefined,
        user_agent: req.headers.get('user-agent') ?? undefined,
    });

    // === 4. Retornar como download ==========================================
    return new NextResponse(JSON.stringify(payload, null, 2), {
        status: 200,
        headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'Content-Disposition': `attachment; filename="meus-dados-${userId}-${new Date()
                .toISOString()
                .slice(0, 10)}.json"`,
            'Cache-Control': 'no-store',
        },
    });
}
