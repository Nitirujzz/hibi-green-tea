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

/** Draw centred text, shrinking the font until it fits the given width. */
function fitText(g: CanvasRenderingContext2D, text: string, y: number, weight: number, size: number, family: string, maxW: number) {
  let sz = size
  do { g.font = `${weight} ${sz}px ${family}, sans-serif`; sz -= 2 } while (g.measureText(text).width > maxW && sz > 20)
  g.fillText(text, g.canvas.width / 2, y)
}

export async function buildCard(kind: ShareKind): Promise<Blob> {
  const c = COPY[kind], W = 1080, H = 1920
  await Promise.all(['700 80px Prompt, sans-serif', '600 40px Plex, sans-serif'].map(f => document.fonts.load(f).catch(() => {})))
  const cv = document.createElement('canvas'); cv.width = W; cv.height = H
  const g = cv.getContext('2d')!
  const bg = g.createLinearGradient(0, 0, 0, H); bg.addColorStop(0, '#fff3c4'); bg.addColorStop(0.55, '#fffaf0'); bg.addColorStop(1, '#ffe0ea')
  g.fillStyle = bg; g.fillRect(0, 0, W, H)
  for (let i = 0; i < 26; i++) {   // soft confetti dots
    g.fillStyle = ['#ff7aa2', '#ffd23f', '#a8d48a', '#e07b39'][i % 4] + '99'
    g.beginPath(); g.arc((i * 397) % W, (i * 811) % H, 10 + (i % 3) * 6, 0, Math.PI * 2); g.fill()
  }
  g.textAlign = 'center'
  g.fillStyle = '#243e1b'; g.font = '700 46px Prompt, sans-serif'; g.fillText('Hibi Matcha Cafe', W / 2, 150)
  g.fillStyle = '#9a9578'; g.font = '600 36px Plex, sans-serif'; g.fillText('เป่ายิ้งฉุบกับ Hibi & Capy', W / 2, 205)
  const img = await loadImg(c.img)
  const s = Math.min(760 / img.width, 760 / img.height)
  g.drawImage(img, (W - img.width * s) / 2, 300 + (760 - img.height * s) / 2, img.width * s, img.height * s)
  g.fillStyle = '#243e1b'; fitText(g, c.title, 1200, 700, 92, 'Prompt', W - 120)
  g.fillStyle = kind === 'grand' ? '#e5484d' : '#3f8f3a'; fitText(g, c.sub, 1290, 700, 54, 'Prompt', W - 140)
  roundRect(g, 120, 1400, W - 240, 300, 48); g.fillStyle = '#ffffff'; g.fill()
  g.strokeStyle = '#ffd23f'; g.lineWidth = 6; g.stroke()
  g.fillStyle = '#243e1b'; g.font = '700 52px Prompt, sans-serif'; g.fillText('มาท้าดวลกันได้ที่ 👇', W / 2, 1495)
  g.fillStyle = '#3f8f3a'; fitText(g, window.location.host + '/game', 1575, 700, 48, 'Prompt', W - 320)
  g.fillStyle = '#6b6a55'; g.font = '600 34px Plex, sans-serif'; g.fillText('ชนะทั้งคู่ รับส่วนลด 50% · 5 สาขา', W / 2, 1640)
  g.fillStyle = '#9a9578'; g.font = '600 34px Plex, sans-serif'; g.fillText('#HibiMatcha #HibiAndCapy', W / 2, 1810)
  return new Promise(res => cv.toBlob(b => res(b!), 'image/png'))
}
