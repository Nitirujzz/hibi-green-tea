import { NextResponse } from 'next/server'
import { cookies } from 'next/headers'
import { GameError } from '@/lib/game/service'
import { readSession, SESSION_COOKIE } from '@/lib/game/session'

export async function currentPhone(): Promise<string | null> {
  return readSession((await cookies()).get(SESSION_COOKIE)?.value)
}

export function fail(e: unknown) {
  if (e instanceof GameError) return NextResponse.json({ error: e.message }, { status: e.status })
  console.error('[game]', e)
  return NextResponse.json({ error: 'ระบบขัดข้อง ลองใหม่อีกครั้ง' }, { status: 500 })
}
