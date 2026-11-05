import { NextResponse } from 'next/server'
import { getState } from '@/lib/game/service'
import { maskPhone } from '@/lib/game/logic'
import { GAME_CONFIG } from '@/lib/game/config'
import { currentPhone, fail } from '../_util'

export async function GET() {
  try {
    const phone = await currentPhone()
    if (!phone) return NextResponse.json({ loggedIn: false, prizes: { win1: GAME_CONFIG.win1.label, win2: GAME_CONFIG.win2.label } })
    return NextResponse.json({ loggedIn: true, phone: maskPhone(phone), state: await getState(phone) })
  } catch (e) { return fail(e) }
}
