'use client'

import { useState, useEffect } from 'react'
import ProductCard from './ProductCard'
import { ProductFilters, Product } from '@/types'

interface ProductGridProps {
  filters: ProductFilters
  sortBy: string
  viewMode: 'grid' | 'list'
}

// Mock products data - in real app, this would come from API
const mockProducts: Product[] = [
  {
    id: '1',
    name: 'Premium Matcha Ceremonial',
    nameEn: 'Premium Matcha Ceremonial',
    description: 'ชาเขียวมัทฉะเกรดพิธีกรรมจากอุจิ ประเทศญี่ปุ่น',
    descriptionEn: 'Ceremonial grade matcha from Uji, Japan',
    price: 1299,
    discountPrice: 999,
    image: '/images/matcha-premium.jpg',
    images: ['/images/matcha-premium.jpg'],
    category: {
      id: '1',
      name: 'Matcha',
      slug: 'matcha',
      isActive: true,
      createdAt: new Date(),
      updatedAt: new Date()
    },
    stock: 25,
    isActive: true,
    tags: ['Premium', 'Ceremonial', 'Organic'],
    createdAt: new Date(),
    updatedAt: new Date()
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
    images: ['/images/sencha-organic.jpg'],
    category: {
      id: '2',
      name: 'Sencha',
      slug: 'sencha',
      isActive: true,
      createdAt: new Date(),
      updatedAt: new Date()
    },
    stock: 42,
    isActive: true,
    tags: ['Organic', 'Premium'],
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    id: '3',
    name: 'Gyokuro Imperial',
    nameEn: 'Gyokuro Imperial',
    description: 'ชาเขียวกโยคุโระระดับจักรพรรดิ หายาก',
    descriptionEn: 'Imperial grade Gyokuro, rare and exquisite',
    price: 2499,
    image: '/images/gyokuro-imperial.jpg',
    images: ['/images/gyokuro-imperial.jpg'],
    category: {
      id: '3',
      name: 'Gyokuro',
      slug: 'gyokuro',
      isActive: true,
      createdAt: new Date(),
      updatedAt: new Date()
    },
    stock: 8,
    isActive: true,
    tags: ['Imperial', 'Rare', 'Premium'],
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    id: '4',
    name: 'Hojicha Roasted Premium',
    nameEn: 'Hojicha Roasted Premium',
    description: 'ชาเขียวโฮจิฉะคั่วหอมกรุ่น',
    descriptionEn: 'Aromatic roasted hojicha tea',
    price: 749,
    discountPrice: 599,
    image: '/images/hojicha-roasted.jpg',
    images: ['/images/hojicha-roasted.jpg'],
    category: {
      id: '4',
      name: 'Hojicha',
      slug: 'hojicha',
      isActive: true,
      createdAt: new Date(),
      updatedAt: new Date()
    },
    stock: 0,
    isActive: true,
    tags: ['Roasted', 'Aromatic'],
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    id: '5',
    name: 'Genmaicha Brown Rice',
    nameEn: 'Genmaicha Brown Rice',
    description: 'ชาเขียวเก็นไมฉะผสมข้าวกล้องคั่ว',
    descriptionEn: 'Green tea with roasted brown rice',
    price: 649,
    image: '/images/genmaicha-rice.jpg',
    images: ['/images/genmaicha-rice.jpg'],
    category: {
      id: '5',
      name: 'Genmaicha',
      slug: 'genmaicha',
      isActive: true,
      createdAt: new Date(),
      updatedAt: new Date()
    },
    stock: 35,
    isActive: true,
    tags: ['Traditional', 'Rice'],
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    id: '6',
    name: 'Tea Ceremony Set Complete',
    nameEn: 'Tea Ceremony Set Complete',
    description: 'ชุดชงชาพิธีกรรมญี่ปุ่นสมบูรณ์',
    descriptionEn: 'Complete Japanese tea ceremony set',
    price: 3999,
    discountPrice: 2999,
    image: '/images/tea-ceremony-set.jpg',
    images: ['/images/tea-ceremony-set.jpg'],
    category: {
      id: '6',
      name: 'Sets',
      slug: 'sets',
      isActive: true,
      createdAt: new Date(),
      updatedAt: new Date()
    },
    stock: 15,
    isActive: true,
    tags: ['Ceremony', 'Complete', 'Traditional'],
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    id: '7',
    name: 'Kukicha Twig Tea',
    nameEn: 'Kukicha Twig Tea',
    description: 'ชากิ่งไผ่คุกิฉะ รสชาติหวานธรรมชาติ',
    descriptionEn: 'Natural sweet twig tea',
    price: 549,
    image: '/images/kukicha-twig.jpg',
    images: ['/images/kukicha-twig.jpg'],
    category: {
      id: '7',
      name: 'Kukicha',
      slug: 'kukicha',
      isActive: true,
      createdAt: new Date(),
      updatedAt: new Date()
    },
    stock: 28,
    isActive: true,
    tags: ['Sweet', 'Natural', 'Twig'],
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    id: '8',
    name: 'Kabusecha Shade Grown',
    nameEn: 'Kabusecha Shade Grown',
    description: 'ชาเขียวคาบุเซฉะปลูกในร่มเงา',
    descriptionEn: 'Premium shade-grown kabusecha',
    price: 1199,
    discountPrice: 899,
    image: '/images/kabusecha-shade.jpg',
    images: ['/images/kabusecha-shade.jpg'],
    category: {
      id: '8',
      name: 'Kabusecha',
      slug: 'kabusecha',
      isActive: true,
      createdAt: new Date(),
      updatedAt: new Date()
    },
    stock: 18,
    isActive: true,
    tags: ['Shade-grown', 'Premium'],
    createdAt: new Date(),
    updatedAt: new Date()
  }
]

export default function ProductGrid({ filters, sortBy, viewMode }: ProductGridProps) {
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Simulate API call
    const fetchProducts = async () => {
      setLoading(true)
      
      // Simulate delay
      await new Promise(resolve => setTimeout(resolve, 500))
      
      let filteredProducts = [...mockProducts]

      // Apply filters
      if (filters.search) {
        const searchTerm = filters.search.toLowerCase()
        filteredProducts = filteredProducts.filter(product =>
          product.name.toLowerCase().includes(searchTerm) ||
          product.description.toLowerCase().includes(searchTerm) ||
          product.tags?.some(tag => tag.toLowerCase().includes(searchTerm))
        )
      }

      if (filters.category) {
        filteredProducts = filteredProducts.filter(product =>
          product.category.name.toLowerCase() === filters.category?.toLowerCase()
        )
      }

      if (filters.minPrice !== undefined) {
        filteredProducts = filteredProducts.filter(product => {
          const price = product.discountPrice || product.price
          return price >= filters.minPrice!
        })
      }

      if (filters.maxPrice !== undefined) {
        filteredProducts = filteredProducts.filter(product => {
          const price = product.discountPrice || product.price
          return price <= filters.maxPrice!
        })
      }

      if (filters.inStock === true) {
        filteredProducts = filteredProducts.filter(product => product.stock > 0)
      }

      if (filters.tags && filters.tags.length > 0) {
        filteredProducts = filteredProducts.filter(product =>
          product.tags?.some(tag => filters.tags?.includes(tag))
        )
      }

      // Apply sorting
      switch (sortBy) {
        case 'name':
          filteredProducts.sort((a, b) => a.name.localeCompare(b.name))
          break
        case 'price-low':
          filteredProducts.sort((a, b) => {
            const priceA = a.discountPrice || a.price
            const priceB = b.discountPrice || b.price
            return priceA - priceB
          })
          break
        case 'price-high':
          filteredProducts.sort((a, b) => {
            const priceA = a.discountPrice || a.price
            const priceB = b.discountPrice || b.price
            return priceB - priceA
          })
          break
        case 'newest':
          filteredProducts.sort((a, b) => b.createdAt.getTime() - a.createdAt.getTime())
          break
        case 'featured':
        default:
          // Keep default order for featured
          break
      }

      setProducts(filteredProducts)
      setLoading(false)
    }

    fetchProducts()
  }, [filters, sortBy])

  if (loading) {
    return (
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        {[...Array(6)].map((_, index) => (
          <div key={index} className="animate-pulse">
            <div className="bg-gray-200 aspect-square rounded-lg mb-4"></div>
            <div className="h-4 bg-gray-200 rounded mb-2"></div>
            <div className="h-4 bg-gray-200 rounded w-2/3 mb-2"></div>
            <div className="h-6 bg-gray-200 rounded w-1/3"></div>
          </div>
        ))}
      </div>
    )
  }

  if (products.length === 0) {
    return (
      <div className="text-center py-16">
        <svg className="w-24 h-24 mx-auto text-gray-300 mb-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z" />
        </svg>
        <h3 className="text-xl font-semibold text-gray-900 mb-2">No products found</h3>
        <p className="text-gray-600 mb-6">
          Try adjusting your filters or search terms to find what you're looking for.
        </p>
      </div>
    )
  }

  return (
    <div className={viewMode === 'grid' ? 'grid md:grid-cols-2 lg:grid-cols-3 gap-8' : 'space-y-6'}>
      {products.map((product) => (
        <ProductCard
          key={product.id}
          product={product}
          viewMode={viewMode}
        />
      ))}
    </div>
  )
}