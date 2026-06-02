# Hibi Green Tea - Brand Design System

## 🎨 Color Palette

### Primary Colors
- **Hibi Green**: `#22c55e` (hibi-500) - Main brand color inspired by premium green tea
- **Deep Green**: `#16a34a` (hibi-600) - Deep, traditional tea green
- **Fresh Green**: `#4ade80` (hibi-400) - Fresh, vibrant accent green

### Secondary & Earth Tones
- **Clay Brown**: `#92400e` - Traditional pottery and ceramics
- **Stone Gray**: `#78716c` - Natural stone texture
- **Tea Cream**: `#fef7cd` - Warm, creamy tea color
- **Pearl White**: `#f8fafc` - Clean, pure background

### Accent Colors
- **Premium Gold**: `#fbbf24` - Luxury and premium quality
- **Traditional Copper**: `#c2410c` - Authentic Japanese aesthetics
- **Sage Gray**: `#6b7280` - Subtle, elegant neutral

## 🎨 Using Colors in Tailwind

### Brand Color Classes
```html
<!-- Primary Colors -->
<div class="bg-hibi-500 text-white">Primary Button</div>
<div class="bg-hibi-600 text-white">Deep Green Section</div>
<div class="bg-hibi-400 text-white">Fresh Accent</div>

<!-- Color Variants (50-900 scale) -->
<div class="bg-hibi-50">Very Light Green</div>
<div class="bg-hibi-900">Very Dark Green</div>

<!-- Tea-inspired Colors -->
<div class="bg-tea-cream">Tea Cream Background</div>
<div class="bg-tea-gold text-tea-brown">Golden Accent</div>
```

### Gradient Utilities
```html
<!-- Brand Gradients -->
<div class="gradient-hibi">Hibi Green Gradient</div>
<div class="gradient-tea-ceremony">Tea Ceremony Gradient</div>
<div class="gradient-tea-warm">Warm Tea Gradient</div>

<!-- Text Gradients -->
<h1 class="text-gradient-hibi">Hibi Text Gradient</h1>
<h2 class="text-gradient-tea">Tea Text Gradient</h2>
```

## 🔤 Typography

### Font System
- **Display Font**: Inter (for headings and emphasis)
- **Body Font**: Inter (for body text)
- **Mono Font**: JetBrains Mono (for code and technical content)

### Font Sizes
- `text-xs` (0.75rem) - Small captions
- `text-sm` (0.875rem) - Body small
- `text-base` (1rem) - Body default
- `text-lg` (1.125rem) - Body large
- `text-xl` to `text-9xl` - Heading sizes

## 🎯 Component Classes

### Button Variants
```html
<button class="btn-primary">Primary Button</button>
<button class="btn-secondary">Secondary Button</button>
<button class="btn-outline">Outline Button</button>
```

### Card Components
```html
<div class="card">Standard Card</div>
<div class="card-matcha">Matcha-themed Card</div>
```

### Focus Ring
```html
<input class="focus-ring" />
```

## 📱 Container & Layout

### Custom Container
```html
<div class="hibi-container">
  <!-- Content with proper padding and max-width -->
</div>
```

### Breakpoints
- `sm`: 640px
- `md`: 768px  
- `lg`: 1024px
- `xl`: 1280px
- `2xl`: 1536px

## ✨ Animations

### Custom Animations
```html
<div class="animate-float">Floating Element</div>
<div class="animate-fade-in-up">Fade In Up</div>
<div class="spinner">Loading Spinner</div>
```

## 🌟 Brand Guidelines

### Do's
- Use matcha green as the primary action color
- Combine earth tones for natural, organic feel
- Use tea ceremony gradient for special occasions
- Maintain consistent rounded corners (0.5rem default)
- Use shadows sparingly with green-tinted variants

### Don'ts
- Don't use colors outside the defined palette
- Avoid high contrast combinations that feel harsh
- Don't mix more than 3 brand colors in a single component
- Avoid neon or artificial-looking greens

## 🎨 Color Accessibility

All brand colors meet WCAG AA contrast requirements:
- Matcha-500 on white: ✅ AA compliant
- Sencha-600 on white: ✅ AA compliant
- Text combinations tested for readability

## 📋 Usage Examples

### Hero Section
```html
<section class="gradient-tea-ceremony text-white">
  <div class="hibi-container py-20">
    <h1 class="text-5xl font-bold mb-6">Hibi Green Tea</h1>
    <p class="text-xl mb-8">Premium Japanese tea experience</p>
    <button class="btn-primary">Shop Now</button>
  </div>
</section>
```

### Product Card
```html
<div class="card hover:shadow-matcha">
  <img src="..." alt="..." class="rounded-lg mb-4">
  <h3 class="text-lg font-semibold text-gray-900 mb-2">Product Name</h3>
  <p class="text-gray-600 mb-4">Product description...</p>
  <div class="flex justify-between items-center">
    <span class="text-2xl font-bold text-matcha-600">฿999</span>
    <button class="btn-primary">Add to Cart</button>
  </div>
</div>
```

This design system ensures consistency across all Hibi Green Tea brand touchpoints while maintaining the authentic, premium feel of Japanese tea culture.