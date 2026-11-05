import { NextResponse } from 'next/server'
import { normalizePhone } from '@/lib/game/logic'
import { verifyOtp, getState, GameError } from '@/lib/game/service'
import { sessionCookie } from '@/lib/game/session'
import { fail } from '../../_util'

export async function POST(req: Request) {
  try {
    const { phone, code } = await req.json()
    const p = normalizePhone(String(phone ?? ''))
    if (!p || !/^\d{6}$/.test(String(code ?? ''))) throw new GameError(400, 'กรุณากรอกรหัส 6 หลัก')
    await verifyOtp(p, String(code))
    const res = NextResponse.json({ ok: true, state: await getState(p) })
    const c = sessionCookie(p)
    res.cookies.set(c.name, c.value, c.options)
    return res
  } catch (e) { return fail(e) }
}
