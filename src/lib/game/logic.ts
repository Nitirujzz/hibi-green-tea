import { randomInt } from 'crypto'
import { MOVES, type Move } from './config'

export type Outcome = 'win' | 'lose' | 'tie'

const BEATS: Record<Move, Move> = { rock: 'scissors', paper: 'rock', scissors: 'paper' }

const LOSES_TO: Record<Move, Move> = { rock: 'paper', paper: 'scissors', scissors: 'rock' }

/**
 * The opponent's move, decided on the server only. A third of throws tie (and are replayed);
 * a decided round goes to the player with probability `winChance` (0..1).
 */
export function opponentMove(player: Move, winChance: number, tieChance = 1 / 3): Move {
  const r = randomInt(1_000_000) / 1_000_000
  if (r < tieChance) return player
  const p = Math.min(1, Math.max(0, winChance))
  return (r - tieChance) / (1 - tieChance) < p ? BEATS[player] : LOSES_TO[player]
}

/** Outcome from the player's point of view. */
export function judge(player: Move, opponent: Move): Outcome {
  if (player === opponent) return 'tie'
  return BEATS[player] === opponent ? 'win' : 'lose'
}

export function isMove(v: unknown): v is Move {
  return typeof v === 'string' && (MOVES as string[]).includes(v)
}

/** Thai mobile numbers: 10 digits starting 06/08/09; +66 form is normalised. */
export function normalizePhone(input: string): string | null {
  let p = input.replace(/[\s-]/g, '')
  if (p.startsWith('+66')) p = '0' + p.slice(3)
  else if (p.startsWith('66') && p.length === 11) p = '0' + p.slice(2)
  return /^0[689]\d{8}$/.test(p) ? p : null
}

export function maskPhone(p: string): string {
  return `${p.slice(0, 3)}-xxx-${p.slice(6)}`
}

/** Coupon codes avoid look-alike characters so staff can type them. */
export function couponCode(): string {
  const A = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'
  const part = () => Array.from({ length: 4 }, () => A[randomInt(A.length)]).join('')
  return `HIBI-${part()}-${part()}`
}
