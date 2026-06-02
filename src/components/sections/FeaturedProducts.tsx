'use client'

import Image from 'next/image'
import Link from 'next/link'
import { Card, CardContent, CardFooter } from '@/components/ui/Card'
import Button from '@/components/ui/Button'
import { formatPrice, calculateDiscountPercentage } from '@/lib/utils'

const featuredProducts = [
  {
    id: '1',
    name: 'Premium Matcha Ceremonial',
    nameEn: 'Premium Matcha Ceremonial',
    description: 'ชาเขียวมัทฉะเกรดพิธีกรรมจากอุจิ ประเทศญี่ปุ่น',
    descriptionEn: 'Ceremonial grade matcha from Uji, Japan',
    price: 1299,
    discountPrice: 999,
    image: '/images/matcha-premium.jpg',
    category: 'Matcha',
    inStock: true,
    rating: 4.9,
    reviews: 124
  },
  {
    id: '2',
    name: 'Organic Sencha Premium',
    nameEn: 'Organic Sencha Premium', 
    description: 'ใบชาเขียวเซนฉะออร์แกนิกจากภูเขาฟูจิ',
    descriptionEn: 'Organic sencha tea leaves from Mount Fuji',
    price: 899,
    discountPrice: 699,
    image: '/images/sencha-organic.jpg',
    category: 'Sencha',
    inStock: true,
    rating: 4.8,
    reviews: 89
  },
  {
    id: '3',
    name: 'Gyokuro Imperial',
    nameEn: 'Gyokuro Imperial',
    description: 'ชาเขียวกโยคุโระระดับจักรพรรดิ หายาก',
    descriptionEn: 'Imperial grade Gyokuro, rare and exquisite',
    price: 2499,
    image: '/images/gyokuro-imperial.jpg',
    category: 'Gyokuro',
    inStock: true,
    rating: 5.0,
    reviews: 45
  },
  {
    id: '4',
    name: 'Tea Ceremony Set Complete',
    nameEn: 'Tea Ceremony Set Complete',
    description: 'ชุดชงชาพิธีกรรมญี่ปุ่นสมบูรณ์',
    descriptionEn: 'Complete Japanese tea ceremony set',
    price: 3999,
    discountPrice: 2999,
    image: '/images/tea-ceremony-set.jpg',
    category: 'Sets',
    inStock: false,
    rating: 4.9,
    reviews: 67
  }
]

export default function FeaturedProducts() {
  return (
    <section className="py-16 lg:py-24 bg-gray-50">
      <div className="container mx-auto px-4">
        {/* Section Header */}
        <div className="text-center mb-16">
          <div className="inline-flex items-center bg-hibi-100 text-hibi-700 px-4 py-2 rounded-full text-sm font-medium mb-6">
            <span className="w-2 h-2 bg-hibi-500 rounded-full mr-2"></span>
            สินค้าแนะนำ • Featured Products
          </div>
          
          <h2 className="text-4xl lg:text-5xl font-bold text-gray-900 mb-4">
            Premium Tea Collection
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            คัดสรรชาเขียวคุณภาพสูงจากสวนชาชื่อดังในญี่ปุ่น เพื่อประสบการณ์การดื่มชาที่ไม่เหมือนใคร
          </p>
        </div>

        {/* Products Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
          {featuredProducts.map((product, index) => (
            <Card 
              key={product.id} 
              variant="product" 
              className="group transform transition-all duration-300 hover:scale-105"
            >
              {/* Product Image */}
              <div className="relative aspect-square overflow-hidden rounded-lg mb-4">
                <Image
                  src={product.image}
                  alt={product.name}
                  fill
                  className="object-cover group-hover:scale-110 transition-transform duration-500"
                />
                
                {/* Badges */}
                <div className="absolute top-3 left-3 flex flex-col gap-2">
                  {product.discountPrice && (
                    <span className="bg-red-500 text-white px-2 py-1 rounded text-sm font-medium">
                      -{calculateDiscountPercentage(product.price, product.discountPrice)}%
                    </span>
                  )}
                  {!product.inStock && (
                    <span className="bg-gray-500 text-white px-2 py-1 rounded text-sm font-medium">
                      หมด • Sold Out
                    </span>
                  )}
                </div>

                {/* Category */}
                <div className="absolute top-3 right-3">
                  <span className="bg-hibi-500 text-white px-2 py-1 rounded text-sm font-medium">
                    {product.category}
                  </span>
                </div>

                {/* Quick View Button */}
                <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-20 transition-all duration-300 flex items-center justify-center">
                  <Button 
                    variant="outline" 
                    className="opacity-0 group-hover:opacity-100 transform translate-y-4 group-hover:translate-y-0 transition-all duration-300 bg-white"
                  >
                    Quick View
                  </Button>
                </div>
              </div>

              <CardContent className="p-0">
                {/* Product Info */}
                <div className="mb-4">
                  <h3 className="font-semibold text-lg text-gray-900 mb-1 line-clamp-1">
                    {product.name}
                  </h3>
                  <p className="text-gray-600 text-sm line-clamp-2 mb-3">
                    {product.description}
                  </p>
                  
                  {/* Rating */}
                  <div className="flex items-center mb-3">
                    <div className="flex text-yellow-400">
                      {[...Array(5)].map((_, i) => (
                        <svg 
                          key={i} 
                          className={`w-4 h-4 ${i < Math.floor(product.rating) ? 'fill-current' : 'fill-gray-200'}`} 
                          viewBox="0 0 24 24"
                        >
                          <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                        </svg>
                      ))}
                    </div>
                    <span className="text-sm text-gray-500 ml-2">
                      ({product.reviews})
                    </span>
                  </div>

                  {/* Price */}
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                      {product.discountPrice ? (
                        <>
                          <span className="text-xl font-bold text-hibi-600">
                            {formatPrice(product.discountPrice)}
                          </span>
                          <span className="text-sm text-gray-500 line-through">
                            {formatPrice(product.price)}
                          </span>
                        </>
                      ) : (
                        <span className="text-xl font-bold text-hibi-600">
                          {formatPrice(product.price)}
                        </span>
                      )}
                    </div>
                  </div>
                </div>
              </CardContent>

              <CardFooter className="p-0 pt-4 border-t">
                <div className="w-full space-y-2">
                  <Button 
                    className="w-full" 
                    disabled={!product.inStock}
                  >
                    {product.inStock ? 'Add to Cart' : 'Notify When Available'}
                  </Button>
                  <Button 
                    variant="ghost" 
                    size="sm" 
                    className="w-full text-xs"
                  >
                    <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                    </svg>
                    Add to Wishlist
                  </Button>
                </div>
              </CardFooter>
            </Card>
          ))}
        </div>

        {/* View All Products CTA */}
        <div className="text-center">
          <Link href="/products">
            <Button size="lg" variant="outline" className="group">
              View All Products
              <svg className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </Button>
          </Link>
        </div>
      </div>

      {/* Background Decoration */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 -right-32 w-64 h-64 bg-hibi-200 opacity-10 rounded-full blur-3xl"></div>
        <div className="absolute bottom-1/4 -left-32 w-48 h-48 bg-tea-gold opacity-10 rounded-full blur-3xl"></div>
      </div>
    </section>
  )
}