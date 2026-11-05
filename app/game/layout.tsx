import type { Metadata, Viewport } from 'next'
import './game.css'

const title = 'เป่ายิ้งฉุบกับ Hibi & Capy · Hibi Matcha Cafe'
const description = 'ชนะ Hibi รับส่วนลด 15% · ชนะทั้ง Hibi และ Capy รับส่วนลด 50%! เล่นฟรีวันละครั้ง'

export const metadata: Metadata = {
  // Set NEXT_PUBLIC_SITE_URL to the live domain so link previews use absolute image URLs.
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL ?? 'http://localhost:3000'),
  title,
  description,
  openGraph: { title, description, type: 'website', locale: 'th_TH', images: [{ url: '/game/og.jpg', width: 1200, height: 630, alt: 'เป่ายิ้งฉุบกับ Hibi & Capy' }] },
  twitter: { card: 'summary_large_image', title, description, images: ['/game/og.jpg'] },
}
export const viewport: Viewport = { width: 'device-width', initialScale: 1, themeColor: '#fffaf0' }

export default function GameLayout({ children }: { children: React.ReactNode }) {
  return <div className="hg">{children}</div>
}
