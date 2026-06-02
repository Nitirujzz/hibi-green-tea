import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

// Utility functions for handling JSON string arrays in SQLite
export function parseStringArray(jsonString: string): string[] {
  try {
    const parsed = JSON.parse(jsonString)
    return Array.isArray(parsed) ? parsed : []
  } catch {
    return []
  }
}

export function stringifyArray(array: string[]): string {
  return JSON.stringify(array)
}

// Format price for display
export function formatPrice(price: number, currency: string = 'THB'): string {
  return new Intl.NumberFormat('th-TH', {
    style: 'currency',
    currency,
    minimumFractionDigits: 0,
  }).format(price)
}

// Calculate discount percentage
export function calculateDiscountPercentage(
  originalPrice: number,
  discountPrice: number
): number {
  if (!discountPrice || discountPrice >= originalPrice) return 0
  return Math.round(((originalPrice - discountPrice) / originalPrice) * 100)
}

// Validate email
export function isValidEmail(email: string): boolean {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return emailRegex.test(email)
}

// Generate slug from string
export function generateSlug(text: string): string {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9 -]/g, '') // Remove special characters
    .replace(/\s+/g, '-') // Replace spaces with hyphens
    .replace(/-+/g, '-') // Replace multiple hyphens with single hyphen
    .trim()
}

// Format date
export function formatDate(
  date: Date | string,
  locale: string = 'th-TH',
  options?: Intl.DateTimeFormatOptions
): string {
  const dateObj = typeof date === 'string' ? new Date(date) : date
  return new Intl.DateTimeFormat(locale, {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    ...options,
  }).format(dateObj)
}

// Format time
export function formatTime(
  date: Date | string,
  locale: string = 'th-TH'
): string {
  const dateObj = typeof date === 'string' ? new Date(date) : date
  return new Intl.DateTimeFormat(locale, {
    hour: '2-digit',
    minute: '2-digit',
  }).format(dateObj)
}

// Truncate text
export function truncate(text: string, length: number): string {
  if (text.length <= length) return text
  return text.slice(0, length).trim() + '...'
}

// Capitalize first letter
export function capitalize(text: string): string {
  return text.charAt(0).toUpperCase() + text.slice(1)
}

// Check if item is in stock
export function isInStock(stock: number, threshold: number = 0): boolean {
  return stock > threshold
}

// Get stock status
export function getStockStatus(stock: number): {
  status: 'in-stock' | 'low-stock' | 'out-of-stock'
  message: string
  messageEn: string
} {
  if (stock === 0) {
    return {
      status: 'out-of-stock',
      message: 'สินค้าหมด',
      messageEn: 'Out of Stock'
    }
  } else if (stock <= 5) {
    return {
      status: 'low-stock',
      message: `เหลือเพียง ${stock} ชิ้น`,
      messageEn: `Only ${stock} left`
    }
  } else {
    return {
      status: 'in-stock',
      message: 'มีสินค้าพร้อมส่ง',
      messageEn: 'In Stock'
    }
  }
}