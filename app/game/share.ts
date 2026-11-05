'use client'
// Builds a 1080x1920 "story" share card on a canvas and shares it.
// The card never shows the coupon code (it is personal) - only the result.

export type ShareKind = 'grand' | 'beat_hibi' | 'lost_hibi' | 'lost_capy'

const COPY: Record<ShareKind, { title: string; sub: string; img: string; text: string }> = {
  grand: { title: 'ฉันชนะ Hibi & Capy! 🏆', sub: 'ได้ส่วนลด 50% ไปเลย!', img: '/game/both_cheer.webp', text: 'ฉันชนะทั้ง Hibi & Capy ได้ส่วนลด 50% 🏆 มาท้าดวลเป่ายิ้งฉุบกันที่ Hibi Matcha Cafe!' },
  beat_hibi: { title: 'ฉันชนะ Hibi! 🎉', sub: 'ได้ส่วนลด 15% · Capy รอบหน้าเจอกัน!', img: '/game/hibi_lose.webp', text: 'ฉันชนะ Hibi ได้ส่วนลด 15% 🎉 ใครจะชนะ Capy ได้บ้าง? มาลองที่ Hibi Matcha Cafe!' },
  lost_capy: { title: 'ชนะ Hibi แต่แพ้ Capy 😆', sub: 'Capy ใจเย็นเกินไปแล้ว… ใครจะแก้แค้นให้?', img: '/game/capy_win.webp', text: 'ฉันชนะ Hibi แต่แพ้ Capy 😆 ใครจะมาแก้แค้นให้? เป่ายิ้งฉุบกับ Hibi & Capy ที่ Hibi Matcha Cafe!' },
  lost_hibi: { title: 'Hibi ชนะฉันไปได้ 😝', sub: 'ใครจะมาแก้แค้นให้ฉันบ้าง?', img: '/game/hibi_win.webp', text: 'Hibi ชนะฉันไปได้ 😝 ใครจะมาแก้แค้นให้? เป่ายิ้งฉุบกับ Hibi & Capy ลุ้นส่วนลด 50% ที่ Hibi Matcha Cafe!' },
}

export function shareUrl(): string {
  return `${window.location.origin}/game?ref=share`
}

export function shareText(kind: ShareKind): string {
  return COPY[kind].text
}

function loadImg(src: string): Promise<HTMLImageElement> {
  return new Promise((res, rej) => { const i = new Image(); i.onload = () => res(i); i.onerror = rej; i.src = src })
}

function roundRect(g: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number) {
  g.beginPath(); g.moveTo(x + r, y); g.arcTo(x + w, y, x + w, y + h, r); g.arcTo(x + w, y + h, x, y + h, r); g.arcTo(x, y + h, x, y, r); g.arcTo(x, y, x + w, y, r); g.closePath()
}

type Ink = { t: HTMLCanvasElement; L: number; w: number; base: number }

/**
 * Render text on a scratch canvas and find its real inked left/right edges. Used for both fitting
 * and centring, because iOS Safari mis-measures (and mis-aligns) Thai text in canvas.
 */
function ink(font: string, fill: string | CanvasGradient | CanvasPattern, text: string, W: number): Ink | null {
  const px = Number(/(\d+)px/.exec(font)?.[1] ?? 48)
  const t = document.createElement('canvas'); t.width = W * 2; t.height = Math.ceil(px * 2)
  const s = t.getContext('2d', { willReadFrequently: true })!
  s.font = font; s.fillStyle = fill; s.textAlign = 'left'; s.textBaseline = 'alphabetic'
  const base = Math.ceil(px * 1.4)
  s.fillText(text, px / 2, base)
  const d = s.getImageData(0, 0, t.width, t.height).data, w = t.width, h = t.height
  const hit = (x: number) => { for (let y = 0; y < h; y++) if (d[(y * w + x) * 4 + 3] > 8) return true; return false }
  let L = 0; while (L < w && !hit(L)) L++
  if (L >= w) return null
  let R = w - 1; while (R > L && !hit(R)) R--
  return { t, L, w: R - L + 1, base }
}

function drawInk(g: CanvasRenderingContext2D, k: Ink, y: number) {
  const W = g.canvas.width
  g.drawImage(k.t, k.L, 0, k.w, k.t.height, (W - k.w) / 2, y - k.base, k.w, k.t.height)
}

/** Draw centred text, shrinking the font until its inked width fits maxW. */
function fitText(g: CanvasRenderingContext2D, text: string, y: number, weight: number, size: number, family: string, maxW: number) {
  const W = g.canvas.width
  for (let sz = size; sz >= 20; sz -= 3) {
    const k = ink(`${weight} ${sz}px ${family}, sans-serif`, g.fillStyle, text, W)
    if (!k) break
    if (k.w <= maxW || sz - 3 < 20) { drawInk(g, k, y); return }
  }
  g.font = `${weight} ${size}px ${family}, sans-serif`; g.textAlign = 'center'; g.fillText(text, W / 2, y)
}

function text(g: CanvasRenderingContext2D, font: string, t: string, y: number) {
  const W = g.canvas.width, k = ink(font, g.fillStyle, t, W)
  if (k) drawInk(g, k, y); else { g.font = font; g.textAlign = 'center'; g.fillText(t, W / 2, y) }
}

export async function buildCard(kind: ShareKind): Promise<Blob> {
  const c = COPY[kind], W = 1080, H = 1920
  // FontFace.load only fetches the unicode-range subsets the sample text needs: pass every drawn string (Thai included).
  const sample = [c.title, c.sub, 'Hibi Matcha Cafe เป่ายิ้งฉุบกับ Hibi & Capy มาท้าดวลกันได้ที่ ชนะทั้งคู่ รับส่วนลด 50% · 5 สาขา #HibiMatcha', window.location.host].join(' ')
  await Promise.all(['700 80px Prompt', '600 40px Plex'].map(f => document.fonts.load(f, sample).catch(() => {})))
  await document.fonts.ready
  const cv = document.createElement('canvas'); cv.width = W; cv.height = H
  const g = cv.getContext('2d')!
  const bg = g.createLinearGradient(0, 0, 0, H); bg.addColorStop(0, '#fff3c4'); bg.addColorStop(0.55, '#fffaf0'); bg.addColorStop(1, '#ffe0ea')
  g.fillStyle = bg; g.fillRect(0, 0, W, H)
  for (let i = 0; i < 26; i++) {   // soft confetti dots
    g.fillStyle = ['#ff7aa2', '#ffd23f', '#a8d48a', '#e07b39'][i % 4] + '99'
    g.beginPath(); g.arc((i * 397) % W, (i * 811) % H, 10 + (i % 3) * 6, 0, Math.PI * 2); g.fill()
  }
    g.fillStyle = '#243e1b'; text(g, '700 46px Prompt, sans-serif', 'Hibi Matcha Cafe', 150)
  g.fillStyle = '#9a9578'; text(g, '600 36px Plex, sans-serif', 'เป่ายิ้งฉุบกับ Hibi & Capy', 205)
  const img = await loadImg(c.img)
  const s = Math.min(760 / img.width, 760 / img.height)
  g.drawImage(img, (W - img.width * s) / 2, 300 + (760 - img.height * s) / 2, img.width * s, img.height * s)
  g.fillStyle = '#243e1b'; fitText(g, c.title, 1200, 700, 92, 'Prompt', W - 120)
  g.fillStyle = kind === 'grand' ? '#e5484d' : '#3f8f3a'; fitText(g, c.sub, 1290, 700, 54, 'Prompt', W - 140)
  roundRect(g, 120, 1400, W - 240, 300, 48); g.fillStyle = '#ffffff'; g.fill()
  g.strokeStyle = '#ffd23f'; g.lineWidth = 6; g.stroke()
  g.fillStyle = '#243e1b'; text(g, '700 52px Prompt, sans-serif', 'มาท้าดวลกันได้ที่ 👇', 1495)
  g.fillStyle = '#3f8f3a'; fitText(g, window.location.host + '/game', 1575, 700, 48, 'Prompt', W - 320)
  g.fillStyle = '#6b6a55'; text(g, '600 34px Plex, sans-serif', 'ชนะทั้งคู่ รับส่วนลด 50% · 5 สาขา', 1640)
  g.fillStyle = '#9a9578'; text(g, '600 34px Plex, sans-serif', '#HibiMatcha #HibiAndCapy', 1810)
  return new Promise((res, rej) => cv.toBlob(b => (b ? res(b) : rej(new Error('card'))), 'image/jpeg', 0.92))
}
