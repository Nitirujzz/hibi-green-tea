import type { Metadata, Viewport } from 'next'
import './game.css'

export const metadata: Metadata = {
  title: 'เป่ายิ้งฉุบกับ Hibi & Capy · Hibi Matcha Cafe',
  description: 'ชนะ Hibi และ Capy รับส่วนลด 50%',
}
export const viewport: Viewport = { width: 'device-width', initialScale: 1, themeColor: '#fffaf0' }

export default function GameLayout({ children }: { children: React.ReactNode }) {
  return <div className="hg">{children}</div>
}
