// User and Authentication Types
export interface User {
  id: string
  email: string
  name?: string
  image?: string
  role: UserRole
  phone?: string
  address?: string
  createdAt: Date
  updatedAt: Date
}

export enum UserRole {
  USER = 'USER',
  ADMIN = 'ADMIN'
}

// Product Types
export interface Product {
  id: string
  name: string
  nameEn?: string
  description: string
  descriptionEn?: string
  price: number
  discountPrice?: number
  image: string
  images: string[]
  category: ProductCategory
  stock: number
  isActive: boolean
  tags?: string[]
  nutritionFacts?: NutritionFacts
  createdAt: Date
  updatedAt: Date
}

export interface ProductCategory {
  id: string
  name: string
  nameEn?: string
  slug: string
  description?: string
  image?: string
  parentId?: string
  isActive: boolean
  createdAt: Date
  updatedAt: Date
}

export interface NutritionFacts {
  calories: number
  protein: number
  carbs: number
  fat: number
  fiber?: number
  sugar?: number
  sodium?: number
  caffeine?: number
}

// Order Types
export interface Order {
  id: string
  userId: string
  user: User
  items: OrderItem[]
  status: OrderStatus
  paymentStatus: PaymentStatus
  totalAmount: number
  shippingAddress: Address
  billingAddress?: Address
  shippingMethod: ShippingMethod
  paymentMethod: PaymentMethod
  stripePaymentIntentId?: string
  notes?: string
  createdAt: Date
  updatedAt: Date
}

export interface OrderItem {
  id: string
  orderId: string
  productId: string
  product: Product
  quantity: number
  price: number
  totalPrice: number
}

export enum OrderStatus {
  PENDING = 'PENDING',
  CONFIRMED = 'CONFIRMED',
  PREPARING = 'PREPARING',
  SHIPPED = 'SHIPPED',
  DELIVERED = 'DELIVERED',
  CANCELLED = 'CANCELLED'
}

export enum PaymentStatus {
  PENDING = 'PENDING',
  PAID = 'PAID',
  FAILED = 'FAILED',
  REFUNDED = 'REFUNDED'
}

export enum ShippingMethod {
  STANDARD = 'STANDARD',
  EXPRESS = 'EXPRESS',
  PICKUP = 'PICKUP'
}

export enum PaymentMethod {
  STRIPE = 'STRIPE',
  CASH_ON_DELIVERY = 'CASH_ON_DELIVERY',
  BANK_TRANSFER = 'BANK_TRANSFER'
}

// Address Type
export interface Address {
  id?: string
  firstName: string
  lastName: string
  company?: string
  addressLine1: string
  addressLine2?: string
  city: string
  state: string
  postalCode: string
  country: string
  phone?: string
}

// Booking Types (for tea workshops/classes)
export interface Booking {
  id: string
  userId: string
  user: User
  sessionId: string
  session: Session
  status: BookingStatus
  participants: number
  totalAmount: number
  paymentStatus: PaymentStatus
  stripePaymentIntentId?: string
  notes?: string
  createdAt: Date
  updatedAt: Date
}

export interface Session {
  id: string
  title: string
  titleEn?: string
  description: string
  descriptionEn?: string
  instructor: string
  duration: number // in minutes
  maxParticipants: number
  price: number
  image: string
  tags?: string[]
  startDateTime: Date
  endDateTime: Date
  isActive: boolean
  createdAt: Date
  updatedAt: Date
}

export enum BookingStatus {
  PENDING = 'PENDING',
  CONFIRMED = 'CONFIRMED',
  CANCELLED = 'CANCELLED',
  COMPLETED = 'COMPLETED'
}

// Cart Types
export interface CartItem {
  id: string
  productId: string
  product: Product
  quantity: number
  price: number
  totalPrice: number
}

export interface Cart {
  items: CartItem[]
  totalItems: number
  totalAmount: number
}

// Form Types
export interface ContactForm {
  name: string
  email: string
  phone?: string
  subject: string
  message: string
}

export interface NewsletterSubscription {
  email: string
  isActive: boolean
  subscribedAt: Date
}

// API Response Types
export interface ApiResponse<T = unknown> {
  success: boolean
  data?: T
  error?: string
  message?: string
}

export interface PaginationMeta {
  page: number
  limit: number
  total: number
  totalPages: number
  hasNextPage: boolean
  hasPrevPage: boolean
}

export interface PaginatedResponse<T> extends ApiResponse<T[]> {
  meta: PaginationMeta
}

// Search and Filter Types
export interface ProductFilters {
  category?: string
  minPrice?: number
  maxPrice?: number
  inStock?: boolean
  tags?: string[]
  search?: string
}

export interface SortOption {
  value: string
  label: string
  labelEn?: string
}

// Component Props Types
export interface SEOProps {
  title?: string
  description?: string
  keywords?: string[]
  ogImage?: string
  canonical?: string
}

export interface BreadcrumbItem {
  label: string
  href?: string
  current?: boolean
}

// Utility Types
export type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>
export type CreateProductInput = Omit<Product, 'id' | 'createdAt' | 'updatedAt'>
export type UpdateProductInput = Partial<CreateProductInput>
export type CreateOrderInput = Omit<Order, 'id' | 'user' | 'items' | 'createdAt' | 'updatedAt'>
export type CreateBookingInput = Omit<Booking, 'id' | 'user' | 'session' | 'createdAt' | 'updatedAt'>