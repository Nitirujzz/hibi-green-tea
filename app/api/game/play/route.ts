import { NextResponse } from 'next/server'
import { isMove } from '@/lib/game/logic'
import { play, GameError } from '@/lib/game/service'
import { currentPhone, fail } from '../_util'

export async function POST(req: Request) {
  try {
    const phone = await currentPhone()
    if (!phone) throw new GameError(401, 'กรุณายืนยันเบอร์มือถือก่อนเล่น')
    const { move } = await req.json()
    if (!isMove(move)) throw new GameError(400, 'เลือก ค้อน กระดาษ หรือ กรรไกร')
    return NextResponse.json(await play(phone, move))
  } catch (e) { return fail(e) }
}
