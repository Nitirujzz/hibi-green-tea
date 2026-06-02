'use client'

import { Fragment, useState } from 'react'
import Link from 'next/link'
import { useSession } from 'next-auth/react'
import { Disclosure, Menu, Transition } from '@headlessui/react'
import { 
  Bars3Icon, 
  XMarkIcon, 
  ShoppingBagIcon,
  UserIcon,
  MagnifyingGlassIcon
} from '@heroicons/react/24/outline'
import { Cart } from '../cart/Cart'

const navigation = [
  { name: 'หน้าแรก', nameEn: 'Home', href: '/' },
  { name: 'สินค้า', nameEn: 'Products', href: '/products' },
  { name: 'คอร์สชงชา', nameEn: 'Tea Classes', href: '/classes' },
  { name: 'เกี่ยวกับเรา', nameEn: 'About', href: '/about' },
  { name: 'ติดต่อ', nameEn: 'Contact', href: '/contact' },
]

const userNavigation = [
  { name: 'โปรไฟล์', nameEn: 'Profile', href: '/profile' },
  { name: 'ออเดอร์', nameEn: 'Orders', href: '/orders' },
  { name: 'การจอง', nameEn: 'Bookings', href: '/bookings' },
  { name: 'ออกจากระบบ', nameEn: 'Sign out', href: '#' },
]

function classNames(...classes: string[]) {
  return classes.filter(Boolean).join(' ')
}

interface HeaderProps {
  locale?: string
}

export default function Header({ locale = 'th' }: HeaderProps) {
  const { data: session, status } = useSession()
  const [cartOpen, setCartOpen] = useState(false)
  const [searchQuery, setSearchQuery] = useState('')

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    if (searchQuery.trim()) {
      window.location.href = `/products?search=${encodeURIComponent(searchQuery)}`
    }
  }

  const getText = (thai: string, english: string) => {
    return locale === 'en' ? english : thai
  }

  return (
    <>
      <Disclosure as="nav" className="bg-white shadow-lg sticky top-0 z-50">
        {({ open }) => (
          <>
            <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
              <div className="flex h-16 justify-between items-center">
                {/* Logo */}
                <div className="flex items-center">
                  <Link href="/" className="flex-shrink-0">
                    <div className="flex items-center space-x-2">
                      <div className="w-8 h-8 bg-green-600 rounded-full flex items-center justify-center">
                        <span className="text-white font-bold text-sm">H</span>
                      </div>
                      <span className="text-xl font-bold text-gray-900">
                        Hibi Green Tea
                      </span>
                    </div>
                  </Link>
                </div>

                {/* Desktop Navigation */}
                <div className="hidden md:block">
                  <div className="ml-10 flex items-baseline space-x-4">
                    {navigation.map((item) => (
                      <Link
                        key={item.name}
                        href={item.href}
                        className="nav-link"
                      >
                        {getText(item.name, item.nameEn)}
                      </Link>
                    ))}
                  </div>
                </div>

                {/* Search Bar */}
                <div className="hidden md:block flex-1 max-w-lg mx-8">
                  <form onSubmit={handleSearch} className="relative">
                    <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                      <MagnifyingGlassIcon className="h-5 w-5 text-gray-400" />
                    </div>
                    <input
                      type="search"
                      name="search"
                      value={searchQuery}
                      onChange={(e) => setSearchQuery(e.target.value)}
                      className="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-green-500 focus:border-green-500"
                      placeholder={getText('ค้นหาสินค้า...', 'Search products...')}
                    />
                  </form>
                </div>

                {/* Right Side Actions */}
                <div className="hidden md:block">
                  <div className="ml-4 flex items-center md:ml-6 space-x-4">
                    {/* Cart Button */}
                    <button
                      onClick={() => setCartOpen(true)}
                      className="relative p-2 text-gray-700 hover:text-hibi-700 transition-colors focus-ring"
                    >
                      <ShoppingBagIcon className="h-6 w-6" />
                      <span className="absolute -top-1 -right-1 bg-hibi-600 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
                        0
                      </span>
                    </button>

                    {/* User Menu */}
                    {status === 'loading' ? (
                      <div className="animate-pulse bg-gray-300 rounded-full h-8 w-8"></div>
                    ) : session ? (
                      <Menu as="div" className="relative ml-3">
                        <div>
                          <Menu.Button className="flex max-w-xs items-center rounded-full bg-white text-sm focus:outline-none focus:ring-2 focus:ring-hibi-500 focus:ring-offset-2">
                            <span className="sr-only">Open user menu</span>
                            {session.user?.image ? (
                              <img
                                className="h-8 w-8 rounded-full"
                                src={session.user.image}
                                alt=""
                              />
                            ) : (
                              <div className="h-8 w-8 rounded-full bg-hibi-600 flex items-center justify-center">
                                <UserIcon className="h-5 w-5 text-white" />
                              </div>
                            )}
                          </Menu.Button>
                        </div>
                        <Transition
                          as={Fragment}
                          enter="transition ease-out duration-100"
                          enterFrom="transform opacity-0 scale-95"
                          enterTo="transform opacity-100 scale-100"
                          leave="transition ease-in duration-75"
                          leaveFrom="transform opacity-100 scale-100"
                          leaveTo="transform opacity-0 scale-95"
                        >
                          <Menu.Items className="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                            {userNavigation.map((item) => (
                              <Menu.Item key={item.name}>
                                {({ active }) => (
                                  <Link
                                    href={item.href}
                                    className={classNames(
                                      active ? 'bg-gray-100' : '',
                                      'block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100'
                                    )}
                                  >
                                    {getText(item.name, item.nameEn)}
                                  </Link>
                                )}
                              </Menu.Item>
                            ))}
                          </Menu.Items>
                        </Transition>
                      </Menu>
                    ) : (
                      <div className="flex items-center space-x-4">
                        <Link
                          href="/auth/signin"
                          className="nav-link"
                        >
                          {getText('เข้าสู่ระบบ', 'Sign In')}
                        </Link>
                        <Link
                          href="/auth/signup"
                          className="btn-primary text-sm"
                        >
                          {getText('สมัครสมาชิก', 'Sign Up')}
                        </Link>
                      </div>
                    )}
                  </div>
                </div>

                {/* Mobile menu button */}
                <div className="md:hidden flex items-center space-x-2">
                  <button
                    onClick={() => setCartOpen(true)}
                    className="relative p-2 text-gray-700 hover:text-hibi-700 focus-ring"
                  >
                    <ShoppingBagIcon className="h-6 w-6" />
                    <span className="absolute -top-1 -right-1 bg-hibi-600 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center">
                      0
                    </span>
                  </button>
                  
                  <Disclosure.Button className="inline-flex items-center justify-center rounded-md p-2 text-gray-700 hover:bg-hibi-50 hover:text-hibi-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-hibi-500">
                    <span className="sr-only">Open main menu</span>
                    {open ? (
                      <XMarkIcon className="block h-6 w-6" aria-hidden="true" />
                    ) : (
                      <Bars3Icon className="block h-6 w-6" aria-hidden="true" />
                    )}
                  </Disclosure.Button>
                </div>
              </div>
            </div>

            {/* Mobile menu */}
            <Disclosure.Panel className="md:hidden">
              <div className="space-y-1 px-2 pb-3 pt-2 sm:px-3 bg-white border-t">
                {/* Mobile Search */}
                <form onSubmit={handleSearch} className="relative mb-4">
                  <div className="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                    <MagnifyingGlassIcon className="h-5 w-5 text-gray-400" />
                  </div>
                  <input
                    type="search"
                    name="search"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-md leading-5 bg-white placeholder-gray-500 focus:outline-none focus:placeholder-gray-400 focus:ring-1 focus:ring-green-500 focus:border-green-500"
                    placeholder={getText('ค้นหาสินค้า...', 'Search products...')}
                  />
                </form>

                {/* Mobile Navigation */}
                {navigation.map((item) => (
                  <Disclosure.Button
                    key={item.name}
                    as={Link}
                    href={item.href}
                    className="nav-link block"
                  >
                    {getText(item.name, item.nameEn)}
                  </Disclosure.Button>
                ))}

                {/* Mobile User Menu */}
                <div className="border-t pt-4 pb-3">
                  {session ? (
                    <>
                      <div className="flex items-center px-5">
                        <div className="flex-shrink-0">
                          {session.user?.image ? (
                            <img
                              className="h-10 w-10 rounded-full"
                              src={session.user.image}
                              alt=""
                            />
                          ) : (
                            <div className="h-10 w-10 rounded-full bg-green-600 flex items-center justify-center">
                              <UserIcon className="h-6 w-6 text-white" />
                            </div>
                          )}
                        </div>
                        <div className="ml-3">
                          <div className="text-base font-medium leading-none text-gray-900">
                            {session.user?.name}
                          </div>
                          <div className="text-sm font-medium leading-none text-gray-500">
                            {session.user?.email}
                          </div>
                        </div>
                      </div>
                      <div className="mt-3 space-y-1 px-2">
                        {userNavigation.map((item) => (
                          <Disclosure.Button
                            key={item.name}
                            as={Link}
                            href={item.href}
                            className="nav-link block"
                          >
                            {getText(item.name, item.nameEn)}
                          </Disclosure.Button>
                        ))}
                      </div>
                    </>
                  ) : (
                    <div className="px-2 space-y-1">
                      <Link
                        href="/auth/signin"
                        className="nav-link block"
                      >
                        {getText('เข้าสู่ระบบ', 'Sign In')}
                      </Link>
                      <Link
                        href="/auth/signup"
                        className="btn-primary block text-center"
                      >
                        {getText('สมัครสมาชิก', 'Sign Up')}
                      </Link>
                    </div>
                  )}
                </div>
              </div>
            </Disclosure.Panel>
          </>
        )}
      </Disclosure>

      {/* Cart Sidebar */}
      <Cart open={cartOpen} setOpen={setCartOpen} />
    </>
  )
}