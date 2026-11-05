import { NextResponse } from 'next/server'
import { normalizePhone } from '@/lib/game/logic'
import { requestOtp, GameError } from '@/lib/game/service'
import { fail } from '../../_util'

export async function POST(req: Request) {
  try {
    const { phone, consent } = await req.json()
    const p = normalizePhone(String(phone ?? ''))
    if (!p) throw new GameError(400, 'กรุณากรอกเบอร์มือถือ 10 หลักให้ถูกต้อง')
    if (consent !== true) throw new GameError(400, 'กรุณายอมรับนโยบายข้อมูลส่วนบุคคลก่อน')
    return NextResponse.json({ ok: true, phone: p, ...(await requestOtp(p)) })
  } catch (e) { return fail(e) }
}
