'use client'

import { useState } from 'react'
import ProductGrid from '@/components/products/ProductGrid'
import ProductFilter from '@/components/products/ProductFilter'
import { ProductFilters } from '@/types'

export default function ProductsPage() {
  const [filters, setFilters] = useState<ProductFilters>({
    category: '',
    minPrice: undefined,
    maxPrice: undefined,
    inStock: undefined,
    tags: [],
    search: ''
  })

  const [sortBy, setSortBy] = useState('featured')
  const [viewMode, setViewMode] = useState<'grid' | 'list'>('grid')

  const handleFilterChange = (newFilters: Partial<ProductFilters>) => {
    setFilters(prev => ({ ...prev, ...newFilters }))
  }

  const handleSortChange = (sort: string) => {
    setSortBy(sort)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Page Header */}
      <div className="bg-gradient-to-r from-hibi-500 to-hibi-600 text-white">
        <div className="container mx-auto px-4 py-16">
          <div className="text-center">
            <h1 className="text-4xl lg:text-5xl font-bold mb-4">
              Premium Tea Collection
            </h1>
            <p className="text-xl opacity-90 max-w-3xl mx-auto">
              คัดสรรชาเขียวคุณภาพสูงจากสวนชาชื่อดังในญี่ปุ่น เพื่อประสบการณ์การดื่มชาที่ไม่เหมือนใคร
            </p>
          </div>
        </div>
      </div>

      <div className="container mx-auto px-4 py-8">
        <div className="flex flex-col lg:flex-row gap-8">
          {/* Sidebar Filters */}
          <aside className="lg:w-80 flex-shrink-0">
            <div className="sticky top-8">
              <ProductFilter
                filters={filters}
                onFilterChange={handleFilterChange}
              />
            </div>
          </aside>

          {/* Main Content */}
          <main className="flex-1">
            {/* Toolbar */}
            <div className="bg-white rounded-lg shadow-sm p-6 mb-8">
              <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4">
                {/* Results Info */}
                <div className="text-gray-600">
                  <span className="font-medium">324 products</span> found
                  {filters.search && (
                    <span> for "{filters.search}"</span>
                  )}
                </div>

                {/* Controls */}
                <div className="flex items-center gap-4">
                  {/* Sort Dropdown */}
                  <div className="flex items-center gap-2">
                    <label className="text-sm text-gray-600">Sort by:</label>
                    <select
                      value={sortBy}
                      onChange={(e) => handleSortChange(e.target.value)}
                      className="border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-hibi-500 focus:border-hibi-500"
                    >
                      <option value="featured">Featured</option>
                      <option value="name">Name A-Z</option>
                      <option value="price-low">Price: Low to High</option>
                      <option value="price-high">Price: High to Low</option>
                      <option value="newest">Newest</option>
                      <option value="rating">Highest Rated</option>
                    </select>
                  </div>

                  {/* View Mode Toggle */}
                  <div className="flex border border-gray-200 rounded-lg overflow-hidden">
                    <button
                      onClick={() => setViewMode('grid')}
                      className={`p-2 ${
                        viewMode === 'grid'
                          ? 'bg-hibi-500 text-white'
                          : 'bg-white text-gray-600 hover:bg-gray-50'
                      }`}
                    >
                      <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
                      </svg>
                    </button>
                    <button
                      onClick={() => setViewMode('list')}
                      className={`p-2 ${
                        viewMode === 'list'
                          ? 'bg-hibi-500 text-white'
                          : 'bg-white text-gray-600 hover:bg-gray-50'
                      }`}
                    >
                      <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 10h16M4 14h16M4 18h16" />
                      </svg>
                    </button>
                  </div>
                </div>
              </div>

              {/* Active Filters */}
              {(filters.category || filters.search || filters.tags?.length > 0 || filters.inStock !== undefined) && (
                <div className="flex flex-wrap items-center gap-2 mt-4 pt-4 border-t border-gray-200">
                  <span className="text-sm text-gray-600 mr-2">Active filters:</span>
                  
                  {filters.search && (
                    <span className="inline-flex items-center bg-hibi-100 text-hibi-800 px-3 py-1 rounded-full text-sm">
                      Search: "{filters.search}"
                      <button
                        onClick={() => handleFilterChange({ search: '' })}
                        className="ml-2 text-hibi-600 hover:text-hibi-800"
                      >
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                        </svg>
                      </button>
                    </span>
                  )}

                  {filters.category && (
                    <span className="inline-flex items-center bg-hibi-100 text-hibi-800 px-3 py-1 rounded-full text-sm">
                      Category: {filters.category}
                      <button
                        onClick={() => handleFilterChange({ category: '' })}
                        className="ml-2 text-hibi-600 hover:text-hibi-800"
                      >
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                        </svg>
                      </button>
                    </span>
                  )}

                  {filters.tags && filters.tags.length > 0 && (
                    <>
                      {filters.tags.map(tag => (
                        <span key={tag} className="inline-flex items-center bg-hibi-100 text-hibi-800 px-3 py-1 rounded-full text-sm">
                          Tag: {tag}
                          <button
                            onClick={() => handleFilterChange({ 
                              tags: filters.tags?.filter(t => t !== tag) || [] 
                            })}
                            className="ml-2 text-hibi-600 hover:text-hibi-800"
                          >
                            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                            </svg>
                          </button>
                        </span>
                      ))}
                    </>
                  )}

                  {filters.inStock !== undefined && (
                    <span className="inline-flex items-center bg-hibi-100 text-hibi-800 px-3 py-1 rounded-full text-sm">
                      {filters.inStock ? 'In Stock Only' : 'All Products'}
                      <button
                        onClick={() => handleFilterChange({ inStock: undefined })}
                        className="ml-2 text-hibi-600 hover:text-hibi-800"
                      >
                        <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                        </svg>
                      </button>
                    </span>
                  )}

                  <button
                    onClick={() => setFilters({
                      category: '',
                      minPrice: undefined,
                      maxPrice: undefined,
                      inStock: undefined,
                      tags: [],
                      search: ''
                    })}
                    className="text-sm text-hibi-600 hover:text-hibi-800 font-medium ml-2"
                  >
                    Clear all
                  </button>
                </div>
              )}
            </div>

            {/* Product Grid */}
            <ProductGrid
              filters={filters}
              sortBy={sortBy}
              viewMode={viewMode}
            />
          </main>
        </div>
      </div>
    </div>
  )
}