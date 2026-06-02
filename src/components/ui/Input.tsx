'use client'

import { InputHTMLAttributes, forwardRef, useState } from 'react'
import { cn } from '@/lib/utils'

export interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string
  error?: string
  helperText?: string
  variant?: 'default' | 'hibi'
}

const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ 
    className, 
    type = 'text', 
    label, 
    error, 
    helperText, 
    variant = 'default',
    id,
    ...props 
  }, ref) => {
    const [focused, setFocused] = useState(false)
    
    const inputId = id || `input-${Math.random().toString(36).substr(2, 9)}`
    
    const baseClasses = 'w-full px-4 py-3 rounded-lg border transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed placeholder:text-gray-400'
    
    const variants = {
      default: cn(
        'border-gray-200 bg-white text-gray-900',
        'focus:border-hibi-500 focus:ring-hibi-500',
        error && 'border-red-300 focus:border-red-500 focus:ring-red-500',
        focused && !error && 'border-hibi-500'
      ),
      hibi: cn(
        'border-hibi-200 bg-hibi-50 text-hibi-900',
        'focus:border-hibi-500 focus:ring-hibi-500 focus:bg-white',
        error && 'border-red-300 focus:border-red-500 focus:ring-red-500',
        focused && !error && 'border-hibi-500 bg-white'
      )
    }

    return (
      <div className="space-y-1">
        {label && (
          <label
            htmlFor={inputId}
            className={cn(
              'block text-sm font-medium',
              error ? 'text-red-700' : 'text-gray-700'
            )}
          >
            {label}
            {props.required && <span className="text-red-500 ml-1">*</span>}
          </label>
        )}
        
        <div className="relative">
          <input
            ref={ref}
            type={type}
            id={inputId}
            className={cn(
              baseClasses,
              variants[variant],
              className
            )}
            onFocus={(e) => {
              setFocused(true)
              props.onFocus?.(e)
            }}
            onBlur={(e) => {
              setFocused(false)
              props.onBlur?.(e)
            }}
            {...props}
          />
        </div>
        
        {(error || helperText) && (
          <div className="text-sm">
            {error ? (
              <p className="text-red-600 flex items-center">
                <svg
                  className="w-4 h-4 mr-1 flex-shrink-0"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    fillRule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clipRule="evenodd"
                  />
                </svg>
                {error}
              </p>
            ) : (
              <p className="text-gray-500">{helperText}</p>
            )}
          </div>
        )}
      </div>
    )
  }
)

Input.displayName = 'Input'

export interface TextareaProps extends InputHTMLAttributes<HTMLTextAreaElement> {
  label?: string
  error?: string
  helperText?: string
  variant?: 'default' | 'hibi'
  rows?: number
}

const Textarea = forwardRef<HTMLTextAreaElement, TextareaProps>(
  ({ 
    className, 
    label, 
    error, 
    helperText, 
    variant = 'default',
    rows = 4,
    id,
    ...props 
  }, ref) => {
    const [focused, setFocused] = useState(false)
    
    const inputId = id || `textarea-${Math.random().toString(36).substr(2, 9)}`
    
    const baseClasses = 'w-full px-4 py-3 rounded-lg border transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed placeholder:text-gray-400 resize-vertical'
    
    const variants = {
      default: cn(
        'border-gray-200 bg-white text-gray-900',
        'focus:border-hibi-500 focus:ring-hibi-500',
        error && 'border-red-300 focus:border-red-500 focus:ring-red-500',
        focused && !error && 'border-hibi-500'
      ),
      hibi: cn(
        'border-hibi-200 bg-hibi-50 text-hibi-900',
        'focus:border-hibi-500 focus:ring-hibi-500 focus:bg-white',
        error && 'border-red-300 focus:border-red-500 focus:ring-red-500',
        focused && !error && 'border-hibi-500 bg-white'
      )
    }

    return (
      <div className="space-y-1">
        {label && (
          <label
            htmlFor={inputId}
            className={cn(
              'block text-sm font-medium',
              error ? 'text-red-700' : 'text-gray-700'
            )}
          >
            {label}
            {props.required && <span className="text-red-500 ml-1">*</span>}
          </label>
        )}
        
        <div className="relative">
          <textarea
            ref={ref}
            id={inputId}
            rows={rows}
            className={cn(
              baseClasses,
              variants[variant],
              className
            )}
            onFocus={(e) => {
              setFocused(true)
              props.onFocus?.(e as any)
            }}
            onBlur={(e) => {
              setFocused(false)
              props.onBlur?.(e as any)
            }}
            {...props}
          />
        </div>
        
        {(error || helperText) && (
          <div className="text-sm">
            {error ? (
              <p className="text-red-600 flex items-center">
                <svg
                  className="w-4 h-4 mr-1 flex-shrink-0"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                >
                  <path
                    fillRule="evenodd"
                    d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z"
                    clipRule="evenodd"
                  />
                </svg>
                {error}
              </p>
            ) : (
              <p className="text-gray-500">{helperText}</p>
            )}
          </div>
        )}
      </div>
    )
  }
)

Textarea.displayName = 'Textarea'

export { Input, Textarea }
export default Input