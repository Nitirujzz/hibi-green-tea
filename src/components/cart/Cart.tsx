'use client'

import { Fragment } from 'react'
import { Dialog, Transition } from '@headlessui/react'
import { XMarkIcon, ShoppingBagIcon, MinusIcon, PlusIcon } from '@heroicons/react/24/outline'
import Link from 'next/link'
import Image from 'next/image'
import { formatPrice } from '@/lib/utils'

interface CartItem {
  id: string
  productId: string
  name: string
  nameEn?: string
  image: string
  price: number
  quantity: number
  stock: number
}

interface CartProps {
  open: boolean
  setOpen: (open: boolean) => void
  locale?: string
}

// Mock cart data - replace with real cart state management
const mockCartItems: CartItem[] = [
  {
    id: '1',
    productId: '1',
    name: 'ผงมัทฉะเกรดเซเรโมนี',
    nameEn: 'Ceremonial Grade Matcha Powder',
    image: '/images/products/matcha-powder-1.jpg',
    price: 999,
    quantity: 1,
    stock: 50
  },
  {
    id: '2',
    productId: '2',
    name: 'เซนฉะออร์แกนิค',
    nameEn: 'Organic Sencha Green Tea',
    image: '/images/products/sencha-1.jpg',
    price: 850,
    quantity: 2,
    stock: 75
  }
]

export function Cart({ open, setOpen, locale = 'th' }: CartProps) {
  const getText = (thai: string, english: string) => {
    return locale === 'en' ? english : thai
  }

  const cartItems = mockCartItems // Replace with actual cart state
  const subtotal = cartItems.reduce((total, item) => total + (item.price * item.quantity), 0)
  const shipping = subtotal > 1000 ? 0 : 100 // Free shipping over 1000 THB
  const total = subtotal + shipping

  const updateQuantity = (itemId: string, newQuantity: number) => {
    // TODO: Implement cart update logic
    console.log('Update quantity:', itemId, newQuantity)
  }

  const removeItem = (itemId: string) => {
    // TODO: Implement cart remove logic
    console.log('Remove item:', itemId)
  }

  return (
    <Transition.Root show={open} as={Fragment}>
      <Dialog as="div" className="relative z-50" onClose={setOpen}>
        <Transition.Child
          as={Fragment}
          enter="ease-in-out duration-500"
          enterFrom="opacity-0"
          enterTo="opacity-100"
          leave="ease-in-out duration-500"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
        >
          <div className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
        </Transition.Child>

        <div className="fixed inset-0 overflow-hidden">
          <div className="absolute inset-0 overflow-hidden">
            <div className="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10">
              <Transition.Child
                as={Fragment}
                enter="transform transition ease-in-out duration-500 sm:duration-700"
                enterFrom="translate-x-full"
                enterTo="translate-x-0"
                leave="transform transition ease-in-out duration-500 sm:duration-700"
                leaveFrom="translate-x-0"
                leaveTo="translate-x-full"
              >
                <Dialog.Panel className="pointer-events-auto w-screen max-w-md">
                  <div className="flex h-full flex-col overflow-y-scroll bg-white shadow-xl">
                    {/* Header */}
                    <div className="flex-1 overflow-y-auto px-4 py-6 sm:px-6">
                      <div className="flex items-start justify-between">
                        <Dialog.Title className="text-lg font-medium text-gray-900">
                          <div className="flex items-center space-x-2">
                            <ShoppingBagIcon className="h-6 w-6 text-hibi-600" />
                            <span>{getText('ตระกร้าสินค้า', 'Shopping Cart')}</span>
                          </div>
                        </Dialog.Title>
                        <div className="ml-3 flex h-7 items-center">
                          <button
                            type="button"
                            className="relative -m-2 p-2 text-gray-400 hover:text-gray-500 transition-colors"
                            onClick={() => setOpen(false)}
                          >
                            <span className="absolute -inset-0.5" />
                            <span className="sr-only">Close panel</span>
                            <XMarkIcon className="h-6 w-6" aria-hidden="true" />
                          </button>
                        </div>
                      </div>

                      {/* Cart Items */}
                      <div className="mt-8">
                        <div className="flow-root">
                          {cartItems.length === 0 ? (
                            <div className="text-center py-12">
                              <ShoppingBagIcon className="mx-auto h-12 w-12 text-gray-400" />
                              <h3 className="mt-2 text-sm font-medium text-gray-900">
                                {getText('ตะกร้าว่างเปล่า', 'Your cart is empty')}
                              </h3>
                              <p className="mt-1 text-sm text-gray-500">
                                {getText('เริ่มเลือกซื้อสินค้ากันเลย', 'Start shopping to add items to your cart')}
                              </p>
                            </div>
                          ) : (
                            <ul role="list" className="-my-6 divide-y divide-gray-200">
                              {cartItems.map((item) => (
                                <li key={item.id} className="flex py-6">
                                  <div className="h-24 w-24 flex-shrink-0 overflow-hidden rounded-md border border-gray-200">
                                    <Image
                                      src={item.image}
                                      alt={getText(item.name, item.nameEn || item.name)}
                                      width={96}
                                      height={96}
                                      className="h-full w-full object-cover object-center"
                                      onError={(e) => {
                                        // Fallback image
                                        const target = e.target as HTMLImageElement
                                        target.src = '/images/placeholder-product.jpg'
                                      }}
                                    />
                                  </div>

                                  <div className="ml-4 flex flex-1 flex-col">
                                    <div>
                                      <div className="flex justify-between text-base font-medium text-gray-900">
                                        <h3>
                                          <Link 
                                            href={`/products/${item.productId}`}
                                            onClick={() => setOpen(false)}
                                            className="hover:text-hibi-600 transition-colors"
                                          >
                                            {getText(item.name, item.nameEn || item.name)}
                                          </Link>
                                        </h3>
                                        <p className="ml-4 text-hibi-600 font-semibold">
                                          {formatPrice(item.price * item.quantity)}
                                        </p>
                                      </div>
                                      <p className="mt-1 text-sm text-gray-500">
                                        {formatPrice(item.price)} {getText('ต่อชิ้น', 'each')}
                                      </p>
                                    </div>
                                    <div className="flex flex-1 items-end justify-between text-sm">
                                      <div className="flex items-center space-x-2">
                                        <span className="text-gray-500">
                                          {getText('จำนวน:', 'Qty:')}
                                        </span>
                                        <div className="flex items-center border border-gray-300 rounded">
                                          <button
                                            onClick={() => updateQuantity(item.id, Math.max(1, item.quantity - 1))}
                                            className="p-1 hover:bg-gray-100 transition-colors"
                                            disabled={item.quantity <= 1}
                                          >
                                            <MinusIcon className="h-4 w-4" />
                                          </button>
                                          <span className="px-2 py-1 min-w-[2rem] text-center">
                                            {item.quantity}
                                          </span>
                                          <button
                                            onClick={() => updateQuantity(item.id, item.quantity + 1)}
                                            className="p-1 hover:bg-gray-100 transition-colors"
                                            disabled={item.quantity >= item.stock}
                                          >
                                            <PlusIcon className="h-4 w-4" />
                                          </button>
                                        </div>
                                      </div>

                                      <div className="flex">
                                        <button
                                          type="button"
                                          onClick={() => removeItem(item.id)}
                                          className="font-medium text-red-600 hover:text-red-500 transition-colors"
                                        >
                                          {getText('ลบ', 'Remove')}
                                        </button>
                                      </div>
                                    </div>
                                  </div>
                                </li>
                              ))}
                            </ul>
                          )}
                        </div>
                      </div>
                    </div>

                    {/* Footer */}
                    {cartItems.length > 0 && (
                      <div className="border-t border-gray-200 px-4 py-6 sm:px-6">
                        {/* Order Summary */}
                        <div className="space-y-2 text-sm">
                          <div className="flex justify-between text-gray-600">
                            <span>{getText('ยอดรวม:', 'Subtotal:')}</span>
                            <span>{formatPrice(subtotal)}</span>
                          </div>
                          <div className="flex justify-between text-gray-600">
                            <span>{getText('ค่าจัดส่ง:', 'Shipping:')}</span>
                            <span>
                              {shipping === 0 
                                ? getText('ฟรี', 'Free')
                                : formatPrice(shipping)
                              }
                            </span>
                          </div>
                          {shipping === 0 && subtotal < 1000 && (
                            <p className="text-xs text-gray-500">
                              {getText(
                                'ซื้อเพิ่ม ฿' + (1000 - subtotal) + ' เพื่อได้ฟรีค่าจัดส่ง',
                                'Add ฿' + (1000 - subtotal) + ' more for free shipping'
                              )}
                            </p>
                          )}
                          <div className="flex justify-between text-base font-medium text-gray-900 pt-2 border-t">
                            <span>{getText('ยอดรวมทั้งสิ้น:', 'Total:')}</span>
                            <span className="text-hibi-600">{formatPrice(total)}</span>
                          </div>
                        </div>

                        <p className="mt-0.5 text-xs text-gray-500">
                          {getText('ราคารวมภาษีแล้ว ค่าจัดส่งคำนวณเมื่อชำระเงิน', 'Shipping and taxes calculated at checkout.')}
                        </p>
                        
                        <div className="mt-6 space-y-3">
                          <Link
                            href="/checkout"
                            onClick={() => setOpen(false)}
                            className="btn-primary w-full text-center block"
                          >
                            {getText('สั่งซื้อเลย', 'Checkout')}
                          </Link>
                          <button
                            type="button"
                            className="btn-outline w-full"
                            onClick={() => setOpen(false)}
                          >
                            {getText('เลือกซื้อต่อ', 'Continue Shopping')}
                          </button>
                        </div>

                        <div className="mt-6 flex justify-center text-center text-sm text-gray-500">
                          <p>
                            {getText('หรือ ', 'or ')}
                            <Link
                              href="/products"
                              className="font-medium text-hibi-600 hover:text-hibi-500"
                              onClick={() => setOpen(false)}
                            >
                              {getText('ดูสินค้าทั้งหมด', 'Continue Shopping')}
                              <span aria-hidden="true"> &rarr;</span>
                            </Link>
                          </p>
                        </div>
                      </div>
                    )}
                  </div>
                </Dialog.Panel>
              </Transition.Child>
            </div>
          </div>
        </div>
      </Dialog>
    </Transition.Root>
  )
}