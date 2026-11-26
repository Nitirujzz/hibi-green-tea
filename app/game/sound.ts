'use client'
// Game audio: one looping BGM track (HTMLAudio) + short SFX via Web Audio.
// Browsers only allow sound after a user gesture, so unlock() is called from the first tap.
// The mute choice is remembered per device (localStorage, best-effort).

export type Sfx = 'tap' | 'beat' | 'beat2' | 'shoot' | 'clash' | 'win' | 'lose' | 'tie' | 'coupon' | 'grand'
const SFX: Sfx[] = ['tap', 'beat', 'beat2', 'shoot', 'clash', 'win', 'lose', 'tie', 'coupon', 'grand']
const KEY = 'hibi_game_muted'

class GameAudio {
  private ctx: AudioContext | null = null
  private buffers = new Map<Sfx, AudioBuffer>()
  private bgm: HTMLAudioElement | null = null
  private unlocked = false
  muted = false

  constructor() {
    try { this.muted = typeof window !== 'undefined' && localStorage.getItem(KEY) === '1' } catch { this.muted = false }
  }

  unlock() {
    if (this.unlocked || typeof window === 'undefined') return
    this.unlocked = true
    try {
      const AC = window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext
      this.ctx = new AC()
      void this.ctx.resume()
      SFX.forEach(n => fetch(`/game/sfx/${n}.mp3`).then(r => r.arrayBuffer()).then(b => this.ctx!.decodeAudioData(b)).then(buf => this.buffers.set(n, buf)).catch(() => {}))
    } catch { this.ctx = null }
    this.bgm = new Audio('/game/sfx/bgm.mp3')
    this.bgm.loop = true
    this.bgm.volume = 0.32
    if (!this.muted) void this.bgm.play().catch(() => {})
  }

  play(name: Sfx, volume = 0.8) {
    if (this.muted || !this.ctx) return
    const buf = this.buffers.get(name)
    if (!buf) return
    const src = this.ctx.createBufferSource(), gain = this.ctx.createGain()
    gain.gain.value = volume
    src.buffer = buf
    src.connect(gain).connect(this.ctx.destination)
    src.start()
  }

  /** Briefly lower the music under a big jingle. */
  duck(ms = 2600) {
    if (!this.bgm || this.muted) return
    this.bgm.volume = 0.08
    setTimeout(() => { if (this.bgm) this.bgm.volume = 0.32 }, ms)
  }

  setMuted(m: boolean) {
    this.muted = m
    try { localStorage.setItem(KEY, m ? '1' : '0') } catch {}
    if (!this.bgm) return
    if (m) this.bgm.pause()
    else void this.bgm.play().catch(() => {})
  }
}

let instance: GameAudio | null = null
export function gameAudio(): GameAudio {
  if (!instance) instance = new GameAudio()
  return instance
}
