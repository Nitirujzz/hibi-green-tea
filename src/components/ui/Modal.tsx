'use client'

import { Fragment, ReactNode, useEffect } from 'react'
import { createPortal } from 'react-dom'
import { cn } from '@/lib/utils'

export interface ModalProps {
  isOpen: boolean
  onClose: () => void
  children: ReactNode
  size?: 'sm' | 'md' | 'lg' | 'xl' | 'full'
  closeOnOverlayClick?: boolean
  closeOnEsc?: boolean
  className?: string
}

const Modal = ({
  isOpen,
  onClose,
  children,
  size = 'md',
  closeOnOverlayClick = true,
  closeOnEsc = true,
  className
}: ModalProps) => {
  useEffect(() => {
    if (!closeOnEsc) return

    const handleEsc = (event: KeyboardEvent) => {
      if (event.key === 'Escape') {
        onClose()
      }
    }

    if (isOpen) {
      document.addEventListener('keydown', handleEsc)
      document.body.style.overflow = 'hidden'
    }

    return () => {
      document.removeEventListener('keydown', handleEsc)
      document.body.style.overflow = 'unset'
    }
  }, [isOpen, onClose, closeOnEsc])

  if (!isOpen) return null

  const sizeClasses = {
    sm: 'max-w-sm',
    md: 'max-w-md',
    lg: 'max-w-lg',
    xl: 'max-w-xl',
    full: 'max-w-full mx-4'
  }

  const modalContent = (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4">
      {/* Backdrop */}
      <div 
        className="fixed inset-0 bg-black bg-opacity-50 backdrop-blur-sm transition-opacity"
        onClick={closeOnOverlayClick ? onClose : undefined}
        aria-hidden="true"
      />
      
      {/* Modal */}
      <div 
        className={cn(
          'relative bg-white rounded-lg shadow-2xl w-full max-h-[90vh] overflow-y-auto',
          sizeClasses[size],
          className
        )}
        role="dialog"
        aria-modal="true"
      >
        {children}
      </div>
    </div>
  )

  return createPortal(modalContent, document.body)
}

export interface ModalHeaderProps {
  children: ReactNode
  onClose?: () => void
  className?: string
}

const ModalHeader = ({ children, onClose, className }: ModalHeaderProps) => (
  <div className={cn('flex items-center justify-between p-6 border-b border-gray-200', className)}>
    <div className="flex-1">{children}</div>
    {onClose && (
      <button
        onClick={onClose}
        className="ml-4 text-gray-400 hover:text-gray-600 transition-colors p-1 rounded-full hover:bg-gray-100"
        aria-label="Close modal"
      >
        <svg
          className="w-6 h-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
    )}
  </div>
)

export interface ModalTitleProps {
  children: ReactNode
  className?: string
  as?: 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'h6'
}

const ModalTitle = ({ children, className, as: Component = 'h2' }: ModalTitleProps) => (
  <Component className={cn('text-xl font-semibold text-gray-900', className)}>
    {children}
  </Component>
)

export interface ModalBodyProps {
  children: ReactNode
  className?: string
}

const ModalBody = ({ children, className }: ModalBodyProps) => (
  <div className={cn('p-6', className)}>
    {children}
  </div>
)

export interface ModalFooterProps {
  children: ReactNode
  className?: string
}

const ModalFooter = ({ children, className }: ModalFooterProps) => (
  <div className={cn('flex items-center justify-end gap-3 p-6 border-t border-gray-200 bg-gray-50 rounded-b-lg', className)}>
    {children}
  </div>
)

export interface ConfirmModalProps {
  isOpen: boolean
  onClose: () => void
  onConfirm: () => void
  title: string
  message: string
  confirmText?: string
  cancelText?: string
  variant?: 'default' | 'danger'
  loading?: boolean
}

const ConfirmModal = ({
  isOpen,
  onClose,
  onConfirm,
  title,
  message,
  confirmText = 'Confirm',
  cancelText = 'Cancel',
  variant = 'default',
  loading = false
}: ConfirmModalProps) => {
  const confirmButtonClasses = variant === 'danger' 
    ? 'bg-red-500 hover:bg-red-600 text-white'
    : 'bg-hibi-500 hover:bg-hibi-600 text-white'

  return (
    <Modal isOpen={isOpen} onClose={onClose} size="sm">
      <ModalHeader onClose={onClose}>
        <ModalTitle>{title}</ModalTitle>
      </ModalHeader>
      
      <ModalBody>
        <p className="text-gray-700">{message}</p>
      </ModalBody>
      
      <ModalFooter>
        <button
          onClick={onClose}
          disabled={loading}
          className="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-hibi-500 disabled:opacity-50"
        >
          {cancelText}
        </button>
        <button
          onClick={onConfirm}
          disabled={loading}
          className={cn(
            'px-4 py-2 text-sm font-medium rounded-lg transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50',
            confirmButtonClasses,
            variant === 'danger' ? 'focus:ring-red-500' : 'focus:ring-hibi-500'
          )}
        >
          {loading && (
            <svg
              className="inline mr-2 w-4 h-4 animate-spin"
              viewBox="0 0 24 24"
              fill="none"
            >
              <circle
                className="opacity-25"
                cx="12"
                cy="12"
                r="10"
                stroke="currentColor"
                strokeWidth="4"
              />
              <path
                className="opacity-75"
                fill="currentColor"
                d="m4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
              />
            </svg>
          )}
          {confirmText}
        </button>
      </ModalFooter>
    </Modal>
  )
}

export { Modal, ModalHeader, ModalTitle, ModalBody, ModalFooter, ConfirmModal }
export default Modal