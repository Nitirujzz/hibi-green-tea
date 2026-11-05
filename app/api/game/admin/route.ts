import { NextResponse } from 'next/server'
import { timingSafeEqual } from 'crypto'
import { adminAction, GameError } from '@/lib/game/service'
import { isDemoMode } from '@/lib/game/config'
import { fail } from '../_util'

function pinOk(pin: unknown): boolean {
  const expected = process.env.GAME_ADMIN_PIN ?? (isDemoMode() ? '1234' : '')
  if (!expected || typeof pin !== 'string') return false
  const a = Buffer.from(pin), b = Buffer.from(expected)
  return a.length === b.length && timingSafeEqual(a, b)
}

export async function POST(req: Request) {
  try {
    const { pin, action, code } = await req.json()
    if (!pinOk(pin)) throw new GameError(401, 'PIN ไม่ถูกต้อง')
    return NextResponse.json(await adminAction(String(action), code ? String(code) : undefined))
  } catch (e) { return fail(e) }
}
