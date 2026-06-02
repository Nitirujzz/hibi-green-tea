import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  // Create categories
  const matchaCategory = await prisma.productCategory.upsert({
    where: { slug: 'matcha' },
    update: {},
    create: {
      name: 'ชาเขียวมัทฉะ',
      nameEn: 'Matcha Green Tea',
      slug: 'matcha',
      description: 'ชาเขียวมัทฉะคุณภาพพรีเมียมจากญี่ปุ่น',
      descriptionEn: 'Premium matcha green tea from Japan',
      image: '/images/categories/matcha.jpg',
      isActive: true,
    },
  })

  const organicCategory = await prisma.productCategory.upsert({
    where: { slug: 'organic' },
    update: {},
    create: {
      name: 'ชาเขียวออร์แกนิค',
      nameEn: 'Organic Green Tea',
      slug: 'organic',
      description: 'ชาเขียวออร์แกนิคปลอดสารเคมี',
      descriptionEn: 'Chemical-free organic green tea',
      image: '/images/categories/organic.jpg',
      isActive: true,
    },
  })

  const giftCategory = await prisma.productCategory.upsert({
    where: { slug: 'gift-sets' },
    update: {},
    create: {
      name: 'ชุดของขวัญ',
      nameEn: 'Gift Sets',
      slug: 'gift-sets',
      description: 'ชุดของขวัญชาเขียวสำหรับคนพิเศษ',
      descriptionEn: 'Green tea gift sets for special occasions',
      image: '/images/categories/gift-sets.jpg',
      isActive: true,
    },
  })

  // Create products
  const matchaPowder = await prisma.product.create({
    data: {
      name: 'ผงมัทฉะเกรดเซเรโมนี',
      nameEn: 'Ceremonial Grade Matcha Powder',
      description: 'ผงมัทฉะเกรดเซเรโมนีคุณภาพสูงจากอุจิ ประเทศญี่ปุ่น มีรสชาติหวานธรรมชาติและกลิ่นหอมเข้มข้น',
      descriptionEn: 'Premium ceremonial grade matcha powder from Uji, Japan. Features natural sweetness and intense aroma.',
      price: 1200,
      discountPrice: 999,
      image: '/images/products/matcha-powder-1.jpg',
      images: '[\"/images/products/matcha-powder-1.jpg\", \"/images/products/matcha-powder-2.jpg\"]',
      categoryId: matchaCategory.id,
      stock: 50,
      isActive: true,
      tags: '[\"matcha\", \"premium\", \"ceremony\", \"japan\"]',
      nutritionFacts: {
        calories: 5,
        protein: 1,
        carbs: 1,
        fat: 0,
        fiber: 1,
        caffeine: 35
      },
    },
  })

  const organicSencha = await prisma.product.create({
    data: {
      name: 'เซนฉะออร์แกนิค',
      nameEn: 'Organic Sencha Green Tea',
      description: 'ใบชาเขียวเซนฉะออร์แกนิคจากฟาร์มชาในภูเขาฟูจิ รสชาติสดชื่นและมีประโยชน์ต่อสุขภาพ',
      descriptionEn: 'Organic sencha green tea leaves from Mount Fuji tea farms. Fresh taste with health benefits.',
      price: 850,
      image: '/images/products/sencha-1.jpg',
      images: '[\"/images/products/sencha-1.jpg\", \"/images/products/sencha-2.jpg\"]',
      categoryId: organicCategory.id,
      stock: 75,
      isActive: true,
      tags: '[\"sencha\", \"organic\", \"healthy\", \"fresh\"]',
      nutritionFacts: {
        calories: 2,
        protein: 0,
        carbs: 0,
        fat: 0,
        fiber: 0,
        caffeine: 25
      },
    },
  })

  const giftSet = await prisma.product.create({
    data: {
      name: 'ชุดของขวัญมัทฉะพรีเมียม',
      nameEn: 'Premium Matcha Gift Set',
      description: 'ชุดของขวัญที่สมบูรณ์แบบ ประกอบด้วย ผงมัทฉะ ชาม แปรงชง และคู่มือการชง',
      descriptionEn: 'Complete gift set including matcha powder, bowl, whisk, and brewing guide.',
      price: 2500,
      discountPrice: 1999,
      image: '/images/products/gift-set-1.jpg',
      images: '[\"/images/products/gift-set-1.jpg\", \"/images/products/gift-set-2.jpg\"]',
      categoryId: giftCategory.id,
      stock: 25,
      isActive: true,
      tags: '[\"gift\", \"matcha\", \"complete\", \"premium\"]',
    },
  })

  // Create tea sessions
  const matchaWorkshop = await prisma.teaSession.create({
    data: {
      title: 'เวิร์กช็อปการชงมัทฉะ',
      titleEn: 'Matcha Brewing Workshop',
      description: 'เรียนรู้ศิลปะการชงมัทฉะแบบดั้งเดิมของญี่ปุ่น ตั้งแต่การเลือกผงมัทฉะ การชง และการดื่มอย่างถูกวิธี',
      descriptionEn: 'Learn the traditional Japanese art of matcha brewing, from selecting matcha powder to proper brewing and drinking techniques.',
      instructor: 'อาจารย์ซาโตะ นากามูระ',
      duration: 120, // 2 hours
      maxParticipants: 8,
      price: 1500,
      image: '/images/sessions/matcha-workshop.jpg',
      tags: '[\"matcha\", \"workshop\", \"traditional\", \"japanese\"]',
      startDateTime: new Date('2024-12-15T10:00:00Z'),
      endDateTime: new Date('2024-12-15T12:00:00Z'),
      isActive: true,
    },
  })

  const teaCeremony = await prisma.teaSession.create({
    data: {
      title: 'พิธีชาญี่ปุ่น (ชาโนะยุ)',
      titleEn: 'Japanese Tea Ceremony (Chanoyu)',
      description: 'สัมผัสประสบการณ์พิธีชาญี่ปุ่นแบบดั้งเดิม เรียนรู้จิตวิญญาณ และปรัชญาของการดื่มชา',
      descriptionEn: 'Experience the traditional Japanese tea ceremony and learn the spirit and philosophy of tea drinking.',
      instructor: 'อาจารย์ฮานาโกะ ซูซูกิ',
      duration: 180, // 3 hours
      maxParticipants: 6,
      price: 2500,
      image: '/images/sessions/tea-ceremony.jpg',
      tags: '[\"ceremony\", \"traditional\", \"culture\", \"meditation\"]',
      startDateTime: new Date('2024-12-20T14:00:00Z'),
      endDateTime: new Date('2024-12-20T17:00:00Z'),
      isActive: true,
    },
  })

  // Create admin user
  const adminUser = await prisma.user.create({
    data: {
      name: 'Admin',
      email: 'admin@hibigreentea.com',
      role: 'ADMIN',
      emailVerified: new Date(),
    },
  })

  console.log('Database seeded successfully!')
  console.log({
    categories: 3,
    products: 3,
    sessions: 2,
    users: 1,
  })
}

main()
  .then(async () => {
    await prisma.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await prisma.$disconnect()
    process.exit(1)
  })