'use client'

import Link from 'next/link'
import { useState } from 'react'
import { 
  MapPinIcon, 
  PhoneIcon, 
  EnvelopeIcon,
  ClockIcon
} from '@heroicons/react/24/outline'
import { 
  FacebookIcon, 
  InstagramIcon, 
  TwitterIcon,
  LineIcon 
} from '../icons/SocialIcons'

const navigation = {
  products: [
    { name: 'ชาเขียวมัทฉะ', nameEn: 'Matcha Green Tea', href: '/products/matcha' },
    { name: 'ชาเขียวญี่ปุ่น', nameEn: 'Japanese Green Tea', href: '/products/japanese-tea' },
    { name: 'ชาเขียวออร์แกนิค', nameEn: 'Organic Green Tea', href: '/products/organic' },
    { name: 'ชุดของขวัญ', nameEn: 'Gift Sets', href: '/products/gift-sets' },
  ],
  company: [
    { name: 'เกี่ยวกับเรา', nameEn: 'About Us', href: '/about' },
    { name: 'เรื่องราวของเรา', nameEn: 'Our Story', href: '/story' },
    { name: 'บล็อก', nameEn: 'Blog', href: '/blog' },
    { name: 'ข่าวสาร', nameEn: 'News', href: '/news' },
  ],
  support: [
    { name: 'ติดต่อเรา', nameEn: 'Contact Us', href: '/contact' },
    { name: 'การจัดส่ง', nameEn: 'Shipping', href: '/shipping' },
    { name: 'การคืนสินค้า', nameEn: 'Returns', href: '/returns' },
    { name: 'FAQ', nameEn: 'FAQ', href: '/faq' },
  ],
  legal: [
    { name: 'นิโยบายความเป็นส่วนตัว', nameEn: 'Privacy Policy', href: '/privacy' },
    { name: 'เงื่อนไขการใช้งาน', nameEn: 'Terms of Service', href: '/terms' },
    { name: 'นโยบายคุกกี้', nameEn: 'Cookie Policy', href: '/cookies' },
  ],
}

const socialLinks = [
  {
    name: 'Facebook',
    href: '#',
    icon: FacebookIcon,
  },
  {
    name: 'Instagram',
    href: '#',
    icon: InstagramIcon,
  },
  {
    name: 'Twitter',
    href: '#',
    icon: TwitterIcon,
  },
  {
    name: 'Line',
    href: '#',
    icon: LineIcon,
  },
]

interface FooterProps {
  locale?: string
}

export default function Footer({ locale = 'th' }: FooterProps) {
  const [email, setEmail] = useState('')
  const [subscribed, setSubscribed] = useState(false)

  const handleNewsletterSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    // TODO: Implement newsletter subscription
    console.log('Subscribing email:', email)
    setSubscribed(true)
    setEmail('')
    setTimeout(() => setSubscribed(false), 3000)
  }

  const getText = (thai: string, english: string) => {
    return locale === 'en' ? english : thai
  }

  return (
    <footer className="bg-gray-900 text-white">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        {/* Main Footer Content */}
        <div className="py-16">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            {/* Company Info */}
            <div className="lg:col-span-2">
              <div className="flex items-center space-x-2 mb-6">
                <div className="w-10 h-10 bg-hibi-600 rounded-full flex items-center justify-center">
                  <span className="text-white font-bold">H</span>
                </div>
                <span className="text-2xl font-bold">Hibi Green Tea</span>
              </div>
              
              <p className="text-gray-300 mb-6 max-w-md">
                {getText(
                  'ค้นพบรสชาติอันเป็นเอกลักษณ์ของชาเขียวคุณภาพพรีเมียมจากญี่ปุ่น พร้อมประสบการณ์การชงชาที่ไม่เหมือนใคร',
                  'Discover the unique taste of premium Japanese green tea with an unparalleled tea brewing experience.'
                )}
              </p>

              {/* Contact Info */}
              <div className="space-y-4">
                <div className="flex items-center space-x-3">
                  <MapPinIcon className="h-5 w-5 text-hibi-500 flex-shrink-0" />
                  <span className="text-gray-300">
                    {getText(
                      '123 ถนนสุขุมวิท แขวงคลองเตย เขตคลองเตย กรุงเทพมหานคร 10110',
                      '123 Sukhumvit Road, Khlong Toei, Bangkok 10110, Thailand'
                    )}
                  </span>
                </div>
                
                <div className="flex items-center space-x-3">
                  <PhoneIcon className="h-5 w-5 text-hibi-500 flex-shrink-0" />
                  <span className="text-gray-300">+66 2 123 4567</span>
                </div>
                
                <div className="flex items-center space-x-3">
                  <EnvelopeIcon className="h-5 w-5 text-hibi-500 flex-shrink-0" />
                  <span className="text-gray-300">info@hibigreentea.com</span>
                </div>
                
                <div className="flex items-center space-x-3">
                  <ClockIcon className="h-5 w-5 text-hibi-500 flex-shrink-0" />
                  <span className="text-gray-300">
                    {getText('จันทร์ - ศุกร์: 9:00 - 18:00', 'Mon - Fri: 9:00 - 18:00')}
                  </span>
                </div>
              </div>

              {/* Social Links */}
              <div className="flex space-x-6 mt-8">
                {socialLinks.map((item) => (
                  <a
                    key={item.name}
                    href={item.href}
                    className="text-gray-400 hover:text-hibi-500 transition-colors"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    <span className="sr-only">{item.name}</span>
                    <item.icon className="h-6 w-6" />
                  </a>
                ))}
              </div>
            </div>

            {/* Quick Links */}
            <div>
              <h3 className="text-lg font-semibold mb-6">
                {getText('สินค้า', 'Products')}
              </h3>
              <ul className="space-y-4">
                {navigation.products.map((item) => (
                  <li key={item.name}>
                    <Link
                      href={item.href}
                      className="text-gray-300 hover:text-hibi-500 transition-colors"
                    >
                      {getText(item.name, item.nameEn)}
                    </Link>
                  </li>
                ))}
              </ul>

              <h3 className="text-lg font-semibold mb-6 mt-8">
                {getText('บริษัท', 'Company')}
              </h3>
              <ul className="space-y-4">
                {navigation.company.map((item) => (
                  <li key={item.name}>
                    <Link
                      href={item.href}
                      className="text-gray-300 hover:text-hibi-500 transition-colors"
                    >
                      {getText(item.name, item.nameEn)}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>

            {/* Newsletter & Support */}
            <div>
              <h3 className="text-lg font-semibold mb-6">
                {getText('รับข่าวสารจากเรา', 'Newsletter')}
              </h3>
              
              <p className="text-gray-300 mb-4">
                {getText(
                  'สมัครรับข่าวสารและโปรโมชั่นพิเศษจากเรา',
                  'Subscribe to get special offers and updates'
                )}
              </p>

              <form onSubmit={handleNewsletterSubmit} className="mb-8">
                <div className="flex flex-col sm:flex-row gap-2">
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder={getText('อีเมลของคุณ', 'Your email')}
                    className="flex-1 px-4 py-2 bg-gray-800 border border-gray-700 rounded-md text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-hibi-500 focus:border-transparent"
                    required
                  />
                  <button
                    type="submit"
                    className="btn-primary"
                  >
                    {getText('สมัคร', 'Subscribe')}
                  </button>
                </div>
                {subscribed && (
                  <p className="text-hibi-500 text-sm mt-2">
                    {getText('ขอบคุณที่สมัครรับข่าวสาร!', 'Thank you for subscribing!')}
                  </p>
                )}
              </form>

              <h3 className="text-lg font-semibold mb-6">
                {getText('ช่วยเหลือ', 'Support')}
              </h3>
              <ul className="space-y-4">
                {navigation.support.map((item) => (
                  <li key={item.name}>
                    <Link
                      href={item.href}
                      className="text-gray-300 hover:text-hibi-500 transition-colors"
                    >
                      {getText(item.name, item.nameEn)}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="border-t border-gray-800 py-8">
          <div className="flex flex-col md:flex-row justify-between items-center">
            <div className="text-gray-400 text-sm">
              <p>
                © 2024 Hibi Green Tea. {getText('สงวนลิขสิทธิ์', 'All rights reserved.')}
              </p>
            </div>
            
            <div className="flex flex-wrap justify-center md:justify-end gap-6 mt-4 md:mt-0">
              {navigation.legal.map((item) => (
                <Link
                  key={item.name}
                  href={item.href}
                  className="text-gray-400 hover:text-hibi-500 text-sm transition-colors"
                >
                  {getText(item.name, item.nameEn)}
                </Link>
              ))}
            </div>
          </div>

          {/* Payment Methods */}
          <div className="flex justify-center md:justify-end mt-6">
            <div className="flex items-center space-x-4">
              <span className="text-gray-400 text-sm">
                {getText('ช่องทางการชำระเงิน:', 'Payment Methods:')}
              </span>
              <div className="flex space-x-2">
                <div className="w-8 h-5 bg-blue-600 rounded flex items-center justify-center text-white text-xs font-bold">
                  VISA
                </div>
                <div className="w-8 h-5 bg-red-600 rounded flex items-center justify-center text-white text-xs font-bold">
                  MC
                </div>
                <div className="w-8 h-5 bg-hibi-600 rounded flex items-center justify-center text-white text-xs font-bold">
                  LN
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  )
}