'use client'

import Image from 'next/image'
import Link from 'next/link'
import Button from '@/components/ui/Button'
import { useState } from 'react'

export default function Hero() {
  const [isPlaying, setIsPlaying] = useState(false)

  return (
    <section className="relative bg-gradient-to-br from-hibi-50 via-white to-tea-cream min-h-[80vh] flex items-center overflow-hidden">
      {/* Background Pattern */}
      <div className="absolute inset-0 opacity-5">
        <div className="absolute top-20 left-20 w-32 h-32 rounded-full bg-hibi-500"></div>
        <div className="absolute top-40 right-32 w-24 h-24 rounded-full bg-tea-gold"></div>
        <div className="absolute bottom-32 left-1/4 w-20 h-20 rounded-full bg-hibi-400"></div>
        <div className="absolute bottom-20 right-20 w-28 h-28 rounded-full bg-hibi-600"></div>
      </div>

      <div className="container mx-auto px-4 py-16 lg:py-24">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="text-center lg:text-left space-y-8">
            {/* Badge */}
            <div className="inline-flex items-center bg-hibi-100 text-hibi-700 px-4 py-2 rounded-full text-sm font-medium">
              <span className="w-2 h-2 bg-hibi-500 rounded-full mr-2"></span>
              Premium Japanese Tea Experience
            </div>

            {/* Main Heading */}
            <div className="space-y-4">
              <h1 className="text-5xl lg:text-7xl font-bold leading-tight">
                <span className="text-gray-900">Hibi</span>{' '}
                <span className="bg-gradient-to-r from-hibi-500 to-hibi-600 bg-clip-text text-transparent">
                  Green Tea
                </span>
              </h1>
              <div className="text-xl lg:text-2xl text-gray-600 max-w-lg">
                <p>วันใหม่ที่ดีกับชาเขียวพรีเมี่ยมจากญี่ปุ่น</p>
                <p className="text-lg mt-2">Discover authentic flavors, traditional ceremonies, and wellness in every cup</p>
              </div>
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start">
              <Link href="/products">
                <Button size="lg" className="w-full sm:w-auto">
                  Shop Premium Tea
                  <svg className="ml-2 w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                  </svg>
                </Button>
              </Link>
              <Link href="/courses">
                <Button variant="outline" size="lg" className="w-full sm:w-auto">
                  Tea Ceremony Classes
                </Button>
              </Link>
            </div>

            {/* Stats */}
            <div className="flex flex-wrap justify-center lg:justify-start gap-8 pt-8 border-t border-gray-200">
              <div className="text-center">
                <div className="text-2xl font-bold text-hibi-600">1000+</div>
                <div className="text-sm text-gray-600">Happy Customers</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-hibi-600">50+</div>
                <div className="text-sm text-gray-600">Premium Teas</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-hibi-600">100%</div>
                <div className="text-sm text-gray-600">Organic</div>
              </div>
            </div>
          </div>

          {/* Right Content - Hero Image */}
          <div className="relative">
            <div className="relative bg-gradient-to-br from-hibi-400 to-hibi-600 rounded-3xl p-8 shadow-2xl">
              {/* Main Product Image */}
              <div className="relative bg-white rounded-2xl p-6 shadow-lg">
                <Image
                  src="/images/hero-tea-set.jpg"
                  alt="Premium Matcha Tea Set"
                  width={500}
                  height={400}
                  className="w-full h-80 object-cover rounded-xl"
                  priority
                />
                
                {/* Floating Elements */}
                <div className="absolute -top-4 -right-4 bg-tea-gold text-tea-brown px-3 py-2 rounded-lg shadow-lg font-semibold">
                  Premium Quality
                </div>
                
                <div className="absolute -bottom-4 -left-4 bg-white shadow-lg rounded-lg p-3">
                  <div className="flex items-center space-x-2">
                    <div className="flex -space-x-2">
                      <div className="w-6 h-6 bg-hibi-200 rounded-full border-2 border-white"></div>
                      <div className="w-6 h-6 bg-hibi-400 rounded-full border-2 border-white"></div>
                      <div className="w-6 h-6 bg-hibi-600 rounded-full border-2 border-white"></div>
                    </div>
                    <span className="text-sm text-gray-600">5.0★ (150 reviews)</span>
                  </div>
                </div>
              </div>

              {/* Video Play Button */}
              <button
                onClick={() => setIsPlaying(!isPlaying)}
                className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white bg-opacity-90 hover:bg-opacity-100 rounded-full p-4 shadow-lg transition-all duration-300 hover:scale-110"
              >
                {isPlaying ? (
                  <svg className="w-8 h-8 text-hibi-600" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M6 4h4v16H6V4zm8 0h4v16h-4V4z"/>
                  </svg>
                ) : (
                  <svg className="w-8 h-8 text-hibi-600 ml-1" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M8 5v14l11-7z"/>
                  </svg>
                )}
              </button>
            </div>

            {/* Decorative Elements */}
            <div className="absolute -z-10 top-8 right-8 w-32 h-32 bg-tea-gold opacity-20 rounded-full blur-xl"></div>
            <div className="absolute -z-10 bottom-8 left-8 w-24 h-24 bg-hibi-500 opacity-20 rounded-full blur-xl"></div>
          </div>
        </div>
      </div>

      {/* Scroll Indicator */}
      <div className="absolute bottom-8 left-1/2 transform -translate-x-1/2">
        <div className="animate-bounce">
          <svg className="w-6 h-6 text-hibi-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
          </svg>
        </div>
      </div>
    </section>
  )
}