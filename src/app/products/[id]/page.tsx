'use client'

import { useState } from 'react'
import { useParams } from 'next/navigation'
import Image from 'next/image'
import Link from 'next/link'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card'
import Button from '@/components/ui/Button'
import { Input } from '@/components/ui/Input'
import { formatPrice, calculateDiscountPercentage, getStockStatus } from '@/lib/utils'

// Mock product data - in real app, this would come from API
const getProductById = (id: string) => {
  const products = [
    {
      id: '1',
      name: 'Premium Matcha Ceremonial',
      nameEn: 'Premium Matcha Ceremonial',
      description: 'ชาเขียวมัทฉะเกรดพิธีกรรมจากอุจิ ประเทศญี่ปุ่น คัดสรรจากใบชาอ่อนที่ปลูกในร่มเงา ให้รสชาติเข้มข้นและหวานธรรมชาติ',
      descriptionEn: 'Ceremonial grade matcha from Uji, Japan. Selected from shade-grown tender leaves for intense flavor and natural sweetness.',
      price: 1299,
      discountPrice: 999,
      image: '/images/matcha-premium-1.jpg',
      images: [
        '/images/matcha-premium-1.jpg',
        '/images/matcha-premium-2.jpg',
        '/images/matcha-premium-3.jpg',
        '/images/matcha-premium-4.jpg'
      ],
      category: 'Matcha',
      stock: 25,
      isActive: true,
      tags: ['Premium', 'Ceremonial', 'Organic'],
      nutritionFacts: {
        calories: 5,
        protein: 1,
        carbs: 1,
        fat: 0,
        fiber: 1,
        caffeine: 70
      },
      rating: 4.9,
      reviews: 124,
      origin: 'Uji, Japan',
      weight: '30g',
      servings: '15 servings',
      storage: 'Store in cool, dry place away from direct sunlight',
      brewing: {
        temperature: '70-80°C',
        steepTime: '1-2 minutes',
        ratio: '1 tsp per cup'
      }
    }
  ]
  
  return products.find(p => p.id === id)
}

const relatedProducts = [
  {
    id: '2',
    name: 'Organic Sencha Premium',
    price: 899,
    discountPrice: 699,
    image: '/images/sencha-organic.jpg',
    rating: 4.8
  },
  {
    id: '3',
    name: 'Gyokuro Imperial',
    price: 2499,
    image: '/images/gyokuro-imperial.jpg',
    rating: 5.0
  },
  {
    id: '4',
    name: 'Hojicha Roasted',
    price: 749,
    image: '/images/hojicha-roasted.jpg',
    rating: 4.7
  }
]

export default function ProductDetailPage() {
  const params = useParams()
  const productId = params.id as string
  
  const [selectedImage, setSelectedImage] = useState(0)
  const [quantity, setQuantity] = useState(1)
  const [activeTab, setActiveTab] = useState('description')

  const product = getProductById(productId)

  if (!product) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-2xl font-bold text-gray-900 mb-4">Product Not Found</h1>
          <Link href="/products">
            <Button>Back to Products</Button>
          </Link>
        </div>
      </div>
    )
  }

  const stockStatus = getStockStatus(product.stock)
  const discountPercent = product.discountPrice ? calculateDiscountPercentage(product.price, product.discountPrice) : 0

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Breadcrumb */}
      <div className="bg-white border-b">
        <div className="container mx-auto px-4 py-4">
          <nav className="flex items-center space-x-2 text-sm text-gray-600">
            <Link href="/" className="hover:text-hibi-600">Home</Link>
            <span>/</span>
            <Link href="/products" className="hover:text-hibi-600">Products</Link>
            <span>/</span>
            <span className="text-gray-900">{product.name}</span>
          </nav>
        </div>
      </div>

      <div className="container mx-auto px-4 py-8">
        <div className="grid lg:grid-cols-2 gap-12 mb-12">
          {/* Product Images */}
          <div className="space-y-4">
            {/* Main Image */}
            <div className="aspect-square bg-white rounded-lg overflow-hidden shadow-lg">
              <Image
                src={product.images[selectedImage]}
                alt={product.name}
                width={600}
                height={600}
                className="w-full h-full object-cover"
              />
            </div>

            {/* Thumbnail Images */}
            <div className="grid grid-cols-4 gap-4">
              {product.images.map((image, index) => (
                <button
                  key={index}
                  onClick={() => setSelectedImage(index)}
                  className={`aspect-square rounded-lg overflow-hidden border-2 transition-all ${
                    selectedImage === index
                      ? 'border-hibi-500 ring-2 ring-hibi-200'
                      : 'border-gray-200 hover:border-hibi-300'
                  }`}
                >
                  <Image
                    src={image}
                    alt={`${product.name} ${index + 1}`}
                    width={150}
                    height={150}
                    className="w-full h-full object-cover"
                  />
                </button>
              ))}
            </div>
          </div>

          {/* Product Info */}
          <div className="space-y-6">
            {/* Title & Rating */}
            <div>
              <h1 className="text-3xl font-bold text-gray-900 mb-2">{product.name}</h1>
              <div className="flex items-center space-x-4 mb-4">
                <div className="flex items-center">
                  <div className="flex text-yellow-400">
                    {[...Array(5)].map((_, i) => (
                      <svg 
                        key={i} 
                        className={`w-5 h-5 ${i < Math.floor(product.rating) ? 'fill-current' : 'fill-gray-200'}`} 
                        viewBox="0 0 24 24"
                      >
                        <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                      </svg>
                    ))}
                  </div>
                  <span className="ml-2 text-sm text-gray-600">
                    {product.rating} ({product.reviews} reviews)
                  </span>
                </div>
                <span className="text-sm text-hibi-600 font-medium">{product.category}</span>
              </div>
            </div>

            {/* Price */}
            <div className="flex items-center space-x-4">
              {product.discountPrice ? (
                <>
                  <span className="text-3xl font-bold text-hibi-600">
                    {formatPrice(product.discountPrice)}
                  </span>
                  <span className="text-xl text-gray-500 line-through">
                    {formatPrice(product.price)}
                  </span>
                  <span className="bg-red-100 text-red-800 px-2 py-1 rounded text-sm font-medium">
                    Save {discountPercent}%
                  </span>
                </>
              ) : (
                <span className="text-3xl font-bold text-hibi-600">
                  {formatPrice(product.price)}
                </span>
              )}
            </div>

            {/* Stock Status */}
            <div className="flex items-center space-x-2">
              <div className={`w-3 h-3 rounded-full ${
                stockStatus.status === 'in-stock' ? 'bg-green-500' :
                stockStatus.status === 'low-stock' ? 'bg-yellow-500' : 'bg-red-500'
              }`} />
              <span className={`font-medium ${
                stockStatus.status === 'in-stock' ? 'text-green-700' :
                stockStatus.status === 'low-stock' ? 'text-yellow-700' : 'text-red-700'
              }`}>
                {stockStatus.message}
              </span>
            </div>

            {/* Quick Info */}
            <div className="grid grid-cols-2 gap-4 p-4 bg-hibi-50 rounded-lg">
              <div className="text-center">
                <div className="text-2xl font-bold text-hibi-600">{product.weight}</div>
                <div className="text-sm text-gray-600">Weight</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-hibi-600">{product.servings}</div>
                <div className="text-sm text-gray-600">Servings</div>
              </div>
            </div>

            {/* Quantity & Add to Cart */}
            <div className="space-y-4">
              <div className="flex items-center space-x-4">
                <label className="text-sm font-medium text-gray-700">Quantity:</label>
                <div className="flex items-center">
                  <button
                    onClick={() => setQuantity(Math.max(1, quantity - 1))}
                    className="w-10 h-10 border border-gray-300 rounded-l-lg flex items-center justify-center hover:bg-gray-50"
                  >
                    -
                  </button>
                  <Input
                    type="number"
                    min="1"
                    max={product.stock}
                    value={quantity}
                    onChange={(e) => setQuantity(Math.max(1, Math.min(product.stock, parseInt(e.target.value) || 1)))}
                    className="w-20 text-center rounded-none border-l-0 border-r-0"
                  />
                  <button
                    onClick={() => setQuantity(Math.min(product.stock, quantity + 1))}
                    className="w-10 h-10 border border-gray-300 rounded-r-lg flex items-center justify-center hover:bg-gray-50"
                  >
                    +
                  </button>
                </div>
              </div>

              <div className="flex space-x-4">
                <Button 
                  size="lg" 
                  className="flex-1"
                  disabled={product.stock === 0}
                >
                  <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 3h2l.4 2M7 13h10l4-8H5.4m0 0L7 13m0 0l-1.5 6M7 13l-1.5 6m0 0h9.5M17 13l1.5 6m-1.5-6h.01" />
                  </svg>
                  Add to Cart
                </Button>
                <Button variant="outline" size="lg">
                  <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                  </svg>
                </Button>
              </div>
            </div>

            {/* Tags */}
            <div className="flex flex-wrap gap-2">
              {product.tags.map((tag, index) => (
                <span 
                  key={index}
                  className="bg-hibi-100 text-hibi-700 px-3 py-1 rounded-full text-sm font-medium"
                >
                  {tag}
                </span>
              ))}
            </div>
          </div>
        </div>

        {/* Product Details Tabs */}
        <div className="bg-white rounded-lg shadow-sm mb-12">
          <div className="border-b">
            <div className="flex space-x-8 px-6">
              {['description', 'brewing', 'nutrition', 'reviews'].map((tab) => (
                <button
                  key={tab}
                  onClick={() => setActiveTab(tab)}
                  className={`py-4 font-medium capitalize border-b-2 transition-colors ${
                    activeTab === tab
                      ? 'border-hibi-500 text-hibi-600'
                      : 'border-transparent text-gray-600 hover:text-gray-900'
                  }`}
                >
                  {tab}
                </button>
              ))}
            </div>
          </div>

          <div className="p-6">
            {activeTab === 'description' && (
              <div className="prose max-w-none">
                <p className="text-gray-700 mb-4">{product.description}</p>
                <p className="text-gray-600 mb-6">{product.descriptionEn}</p>
                
                <div className="grid md:grid-cols-2 gap-6">
                  <div>
                    <h4 className="font-semibold text-gray-900 mb-3">Product Details</h4>
                    <ul className="space-y-2 text-sm text-gray-600">
                      <li><strong>Origin:</strong> {product.origin}</li>
                      <li><strong>Weight:</strong> {product.weight}</li>
                      <li><strong>Servings:</strong> {product.servings}</li>
                      <li><strong>Category:</strong> {product.category}</li>
                    </ul>
                  </div>
                  
                  <div>
                    <h4 className="font-semibold text-gray-900 mb-3">Storage</h4>
                    <p className="text-sm text-gray-600">{product.storage}</p>
                  </div>
                </div>
              </div>
            )}

            {activeTab === 'brewing' && (
              <div className="grid md:grid-cols-3 gap-6">
                <Card>
                  <CardHeader>
                    <CardTitle className="text-lg flex items-center">
                      <svg className="w-5 h-5 mr-2 text-hibi-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707" />
                      </svg>
                      Temperature
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="text-2xl font-bold text-hibi-600">{product.brewing.temperature}</div>
                  </CardContent>
                </Card>

                <Card>
                  <CardHeader>
                    <CardTitle className="text-lg flex items-center">
                      <svg className="w-5 h-5 mr-2 text-hibi-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                      Steep Time
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="text-2xl font-bold text-hibi-600">{product.brewing.steepTime}</div>
                  </CardContent>
                </Card>

                <Card>
                  <CardHeader>
                    <CardTitle className="text-lg flex items-center">
                      <svg className="w-5 h-5 mr-2 text-hibi-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M7 4V2a1 1 0 011-1h3a1 1 0 011 1v2m4 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                      </svg>
                      Ratio
                    </CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="text-2xl font-bold text-hibi-600">{product.brewing.ratio}</div>
                  </CardContent>
                </Card>
              </div>
            )}

            {activeTab === 'nutrition' && (
              <div className="grid md:grid-cols-3 gap-6">
                <Card>
                  <CardHeader>
                    <CardTitle>Per Serving</CardTitle>
                  </CardHeader>
                  <CardContent className="space-y-3">
                    <div className="flex justify-between">
                      <span>Calories</span>
                      <span className="font-medium">{product.nutritionFacts.calories}</span>
                    </div>
                    <div className="flex justify-between">
                      <span>Protein</span>
                      <span className="font-medium">{product.nutritionFacts.protein}g</span>
                    </div>
                    <div className="flex justify-between">
                      <span>Carbs</span>
                      <span className="font-medium">{product.nutritionFacts.carbs}g</span>
                    </div>
                    <div className="flex justify-between">
                      <span>Fat</span>
                      <span className="font-medium">{product.nutritionFacts.fat}g</span>
                    </div>
                    <div className="flex justify-between">
                      <span>Fiber</span>
                      <span className="font-medium">{product.nutritionFacts.fiber}g</span>
                    </div>
                    <div className="flex justify-between border-t pt-2">
                      <span className="font-medium">Caffeine</span>
                      <span className="font-bold text-hibi-600">{product.nutritionFacts.caffeine}mg</span>
                    </div>
                  </CardContent>
                </Card>
              </div>
            )}

            {activeTab === 'reviews' && (
              <div>
                <div className="text-center py-12">
                  <div className="text-4xl font-bold text-hibi-600 mb-2">{product.rating}</div>
                  <div className="flex justify-center text-yellow-400 mb-2">
                    {[...Array(5)].map((_, i) => (
                      <svg 
                        key={i} 
                        className={`w-6 h-6 ${i < Math.floor(product.rating) ? 'fill-current' : 'fill-gray-200'}`} 
                        viewBox="0 0 24 24"
                      >
                        <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                      </svg>
                    ))}
                  </div>
                  <div className="text-gray-600">Based on {product.reviews} reviews</div>
                  
                  <div className="mt-8">
                    <Button variant="outline">Write a Review</Button>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Related Products */}
        <div>
          <h2 className="text-2xl font-bold text-gray-900 mb-8 text-center">You Might Also Like</h2>
          <div className="grid md:grid-cols-3 gap-8">
            {relatedProducts.map((relatedProduct) => (
              <Card key={relatedProduct.id} variant="product" className="group hover:shadow-lg transition-shadow">
                <div className="aspect-square overflow-hidden rounded-lg mb-4">
                  <Image
                    src={relatedProduct.image}
                    alt={relatedProduct.name}
                    width={300}
                    height={300}
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                  />
                </div>
                <CardContent className="p-0">
                  <h3 className="font-semibold text-lg mb-2 line-clamp-1">{relatedProduct.name}</h3>
                  <div className="flex items-center space-x-2 mb-3">
                    {relatedProduct.discountPrice ? (
                      <>
                        <span className="text-xl font-bold text-hibi-600">
                          {formatPrice(relatedProduct.discountPrice)}
                        </span>
                        <span className="text-sm text-gray-500 line-through">
                          {formatPrice(relatedProduct.price)}
                        </span>
                      </>
                    ) : (
                      <span className="text-xl font-bold text-hibi-600">
                        {formatPrice(relatedProduct.price)}
                      </span>
                    )}
                  </div>
                  <div className="flex items-center text-sm text-gray-600">
                    <div className="flex text-yellow-400 mr-2">
                      {[...Array(5)].map((_, i) => (
                        <svg 
                          key={i} 
                          className={`w-4 h-4 ${i < Math.floor(relatedProduct.rating) ? 'fill-current' : 'fill-gray-200'}`} 
                          viewBox="0 0 24 24"
                        >
                          <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                        </svg>
                      ))}
                    </div>
                    <span>{relatedProduct.rating}</span>
                  </div>
                </CardContent>
                <div className="mt-4">
                  <Link href={`/products/${relatedProduct.id}`}>
                    <Button className="w-full" variant="outline">View Product</Button>
                  </Link>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}