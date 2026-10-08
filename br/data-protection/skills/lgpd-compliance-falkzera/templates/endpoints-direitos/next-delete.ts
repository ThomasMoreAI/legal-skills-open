/**
 * DELETE /api/legal/account
 * =====================================================================
 * Direito de eliminação (LGPD art. 18 VI). Respeita exceções do art. 16
 * (dados retidos por obrigação legal).
 *
 * Stack: Next.js 14+ (App Router) + TypeScript.
 * Cole em: app/api/legal/account/route.ts
 *
 * Comportamento:
 *  - exige usuário autenticado + confirmação dupla (segunda autenticação)
 *  - consulta retention_policy pra decidir por categoria:
 *      * hard_delete       → DELETE
 *      * anonymize         → UPDATE c/ valores anonimizados
 *      * retain_with_basis → mantém com flag is_retained
 *  - registra audit_log + cria dsr_request
 *  - envia e-mail de confirmação detalhando o que foi feito
 */

import { NextRequest, NextResponse } from 'next/server';
import { auth } from '@/lib/auth';
import { db } from '@/lib/db';
import { logAudit } from '@/lib/audit';
import { sendDeletionReceipt } from '@/lib/email';
import { z } from 'zod';

export const runtime = 'nodejs';
export const dynamic = 'force-dynamic';

const Body = z.object({
    confirm: z.literal('EXCLUIR PERMANENTEMENTE'),
    password: z.string().min(1), // segunda autenticação
});

export async function DELETE(req: NextRequest) {
    const session = await auth();
    if (!session?.user?.id) {
        return NextResponse.json({ error: 'unauthorized' }, { status: 401 });
    }

    const body = Body.safeParse(await req.json().catch(() => ({})));
    if (!body.success) {
        return NextResponse.json(
            { error: 'invalid_confirmation' },
            { status: 400 }
        );
    }

    const userId = session.user.id;

    // === 1. Reautenticar (proteção contra exclusão por sequestro de sessão)
    const passwordOk = await verifyPassword(userId, body.data.password);
    if (!passwordOk) {
        return NextResponse.json({ error: 'wrong_password' }, { status: 401 });
    }

    // === 2. Criar DSR
    const dsr = await db.dsr_request.create({
        data: {
            user_id: userId,
            requester_email: session.user.email!,
            request_type: 'deletion',
            status: 'in_progress',
            due_at: addDays(new Date(), 15), // ajuste pra 30 se ATPP
        },
    });

    // === 3. Iterar pela retention_policy e decidir por categoria
    const policies = await db.retention_policy.findMany();

    const report: {
        category: string;
        action: 'deleted' | 'anonymized' | 'retained';
        reason: string;
    }[] = [];

    await db.$transaction(async (tx) => {
        for (const p of policies) {
            switch (p.on_delete_action) {
                case 'hard_delete':
                    await deleteCategoryFor(tx, p.data_category, userId);
                    report.push({
                        category: p.data_category,
                        action: 'deleted',
                        reason: p.justification,
                    });
                    break;

                case 'anonymize':
                    await anonymizeCategoryFor(tx, p.data_category, userId);
                    report.push({
                        category: p.data_category,
                        action: 'anonymized',
                        reason: p.justification,
                    });
                    break;

                case 'retain_with_basis':
                    await flagRetention(tx, p.data_category, userId);
                    report.push({
                        category: p.data_category,
                        action: 'retained',
                        reason: p.justification,
                    });
                    break;
            }
        }

        // marcar conta como excluída (pseudonimizar identificadores)
        await tx.users.update({
            where: { id: userId },
            data: {
                is_deleted: true,
                deleted_at: new Date(),
                email: `deleted-${userId}@deleted.invalid`,
                name: '[excluído]',
                phone: null,
                cpf: null,
            },
        });

        await tx.dsr_request.update({
            where: { id: dsr.id },
            data: {
                status: report.some((r) => r.action === 'retained')
                    ? 'partially_completed'
                    : 'completed',
                completed_at: new Date(),
                response: JSON.stringify(report),
                retention_reason: report
                    .filter((r) => r.action === 'retained')
                    .map((r) => `${r.category}: ${r.reason}`)
                    .join('\n'),
            },
        });
    });

    // === 4. Audit
    await logAudit({
        actor_type: 'titular',
        actor_id: userId,
        target_user_id: userId,
        action: 'data_deletion',
        entity: 'user_account',
        metadata: { report },
        ip: req.headers.get('x-forwarded-for') ?? undefined,
        user_agent: req.headers.get('user-agent') ?? undefined,
    });

    // === 5. E-mail de comprovante (pra endereço de cópia ou genérico do DPO)
    await sendDeletionReceipt({
        userId,
        email: session.user.email!,
        report,
    });

    // === 6. Invalidar sessão e responder
    return NextResponse.json(
        {
            status: 'ok',
            message:
                'Sua conta foi excluída. Você receberá um e-mail com o detalhamento.',
            report,
        },
        {
            status: 200,
            headers: {
                'Set-Cookie': 'session=; Max-Age=0; Path=/; HttpOnly; Secure',
            },
        }
    );
}

// === Implementações auxiliares (esqueleto, adapte ao seu ORM) ==============

async function verifyPassword(userId: string, password: string): Promise<boolean> {
    // implementar com argon2/bcrypt
    return false;
}

async function deleteCategoryFor(_tx: unknown, _category: string, _userId: string) {
    // mapear categoria → tabela(s), executar DELETE
}

async function anonymizeCategoryFor(_tx: unknown, _category: string, _userId: string) {
    // UPDATE setando hash irreversível ou nulls em campos identificadores
}

async function flagRetention(_tx: unknown, _category: string, _userId: string) {
    // UPDATE setando is_retained = true; manter por dever legal
}

function addDays(d: Date, n: number): Date {
    const r = new Date(d);
    r.setDate(r.getDate() + n);
    return r;
}
