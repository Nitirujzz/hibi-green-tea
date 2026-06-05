import { PrismaClient, TeaGrade } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  console.log('🍵 Seeding Hibi Matcha menu data...')

  // ─── 1. TEA CULTIVARS ────────────────────────────────────────────────────────
  const cultivars = [
    { code: 'M01', name: 'Kagoshima Asanoka', supplierName: 'Kagoshima Chiran "Asanoka"', grade: TeaGrade.CEREMONIAL_ORGANIC, origin: 'Kagoshima', flavorNotes: 'Clean, sweet, umami', isOrganic: true },
    { code: 'M02', name: 'Kagoshima Shinju', supplierName: 'Kagoshima First Harvest "Shinju"', grade: TeaGrade.CEREMONIAL, origin: 'Kagoshima', flavorNotes: 'Rich, creamy, first flush' },
    { code: 'M03', name: 'Uji Kazen', supplierName: 'Uji tencha (Kyoto) "Kazen"', grade: TeaGrade.CEREMONIAL, origin: 'Kyoto', flavorNotes: 'หอมดอกไม้และข้าวคั่ว ขมนุ่ม สดชื่นสะอาด' },
    { code: 'M04', name: 'Uji Samidori', supplierName: 'Uji (Kyoto) "Samidori"', grade: TeaGrade.CEREMONIAL, origin: 'Kyoto', flavorNotes: 'หวานละมุน ไม่ขม หอมกลิ่นถั่วและเต้าหู้ขาว' },
    { code: 'M05', name: 'Kagoshima Hikari', supplierName: 'Kagoshima Organic "Hikari"', grade: TeaGrade.CEREMONIAL_ORGANIC, origin: 'Kagoshima', isOrganic: true },
    { code: 'M06', name: 'Uji Okumidori', supplierName: 'Uji (Kyoto) "Okumidori"', grade: TeaGrade.CEREMONIAL, origin: 'Kyoto', flavorNotes: 'หอมสาหร่าย ลึก อูมามิแน่น' },
    { code: 'M07', name: 'Mie Matcha Seian', supplierName: 'Mie Matcha "Seian"', grade: TeaGrade.PREMIUM, origin: 'Mie', flavorNotes: 'กลิ่นชาใส ถั่วอ่อน ละมุน' },
    { code: 'M08', name: 'Gyokuro Yame', supplierName: 'Yame Gyokuro FD', grade: TeaGrade.CEREMONIAL, origin: 'Yame Fukuoka', flavorNotes: 'ซุปดาชิ สาหร่ายคอมบุ อูมามิสูงสุด' },
    { code: 'M09', name: 'Organic Yabukita', supplierName: 'Organic Yabukita', grade: TeaGrade.CEREMONIAL_ORGANIC, origin: 'Yame Fukuoka', isOrganic: true },
    { code: 'M10', name: 'Yame Saemidori', supplierName: 'Saemidori', grade: TeaGrade.PREMIUM, origin: 'Yame Fukuoka', flavorNotes: 'หอมถั่วและเต้าหู้' },
    { code: 'M11', name: 'Yame Okumidori', supplierName: 'Okumidori', grade: TeaGrade.PREMIUM, origin: 'Yame Fukuoka', flavorNotes: 'หอมสาหร่าย ถั่วคั่ว' },
    { code: 'M12', name: 'Yame First Harvest', supplierName: '1st Flush', grade: TeaGrade.PREMIUM, origin: 'Yame Fukuoka' },
    { code: 'M15', name: 'Yame Hojun', supplierName: 'Nutty blend', grade: TeaGrade.PREMIUM_LATTE, origin: 'Yame Fukuoka', flavorNotes: 'หอมถั่ว เข้มข้น เหมาะกับลาเต้' },
    { code: 'M16', name: 'Yame Saeakari', grade: TeaGrade.PREMIUM, origin: 'Yame Fukuoka' },
    { code: 'M17', name: 'Yame Fukamushi', grade: TeaGrade.PREMIUM, origin: 'Yame Fukuoka', flavorNotes: 'Deep steamed, rich umami' },
    { code: 'M18', name: 'Hibi Daichi Blend', supplierName: 'Hibi Daichi Blend', grade: TeaGrade.PREMIUM, origin: 'Hibi Signature', flavorNotes: 'หอมอโวคาโด ปลายอูมามิชัด' },
    { code: 'M19', name: 'Hibi Tsuchi Blend', supplierName: 'Hibi Tsuchi Blend', grade: TeaGrade.PREMIUM, origin: 'Hibi Signature', flavorNotes: 'สดชื่น โทนไม้ ซิตรัส' },
    { code: 'M20', name: 'Hibi Kumo Blend', supplierName: 'Hibi Kumo Blend', grade: TeaGrade.PREMIUM, origin: 'Hibi Signature', flavorNotes: 'หอมข้าวโพด และอโวคาโด' },
    { code: 'M21', name: 'Hibi Sayaka', grade: TeaGrade.PREMIUM, origin: 'Oriental Blend' },
    { code: 'M22', name: 'Hibi Shizuku', grade: TeaGrade.PREMIUM, origin: 'Oriental Blend' },
    { code: 'M23', name: 'Hibi Noko', supplierName: 'FTC', grade: TeaGrade.PREMIUM, origin: 'Unkyō (雲郷)' },
    { code: 'M26', name: 'Kagoshima Okumidori', grade: TeaGrade.CEREMONIAL_ORGANIC, origin: 'Kagoshima', isOrganic: true },
    { code: 'M29', name: 'Noko Sen', supplierName: 'Hibi Noko Sen', grade: TeaGrade.PREMIUM, origin: 'Organic Premium', isOrganic: true },
    { code: 'M30', name: 'Kagoshima Loishi', grade: TeaGrade.CEREMONIAL_ORGANIC, origin: 'Kagoshima', isOrganic: true, flavorNotes: 'Ceremonial organic, smooth' },
    { code: 'M31', name: 'Kagoshima Hiri', grade: TeaGrade.PREMIUM, origin: 'Kagoshima', isOrganic: true },
    { code: 'M32', name: 'Kagoshima Saemidori Baisen', grade: TeaGrade.PREMIUM, origin: 'Kagoshima', flavorNotes: 'Roasted Saemidori' },
    { code: 'M33', name: 'Kagoshima Kanayamidori Baisen', grade: TeaGrade.PREMIUM, origin: 'Kagoshima', flavorNotes: 'Roasted Kanayamidori' },
    { code: 'M34', name: 'Kagoshima Okumidori Baisen', grade: TeaGrade.PREMIUM_LATTE, origin: 'Kagoshima', flavorNotes: 'Roasted Okumidori' },
    { code: 'M37', name: 'Exhibit No.1 Yuzuru', grade: TeaGrade.CEREMONIAL, origin: 'Japan', flavorNotes: 'Ultra premium, Master Piece' },
    { code: 'M39', name: 'Exhibit No.2 Rin / Yumemi', grade: TeaGrade.CEREMONIAL, origin: 'Japan', flavorNotes: 'Premium ceremonial collection' },
    { code: 'M40', name: 'O-Matcha Sou', supplierName: 'Shizuoka Cha no Niwa', grade: TeaGrade.CEREMONIAL, origin: 'Shizuoka' },
    { code: 'M41', name: 'Kakegawa Fukamushi-cha', supplierName: 'Fukamushi-cha Powder', grade: TeaGrade.PREMIUM, origin: 'Kakegawa' },
    { code: 'M42', name: 'Fuji Yabukita Second Flush', grade: TeaGrade.PREMIUM, origin: 'Fuji' },
    { code: 'H01', name: 'Hojicha Kaori', supplierName: 'Hōjicha Kaori', grade: TeaGrade.PREMIUM, origin: 'Yame Fukuoka', flavorNotes: 'หอมคั่ว ละมุน เบา' },
    { code: 'H02', name: 'Hojicha Kokoro', supplierName: 'Hōjicha Kokoro', grade: TeaGrade.CEREMONIAL, origin: 'Yame Fukuoka', flavorNotes: 'Almond, caramel, toasted notes' },
    { code: 'H03', name: 'Hojicha Roast Aroma', grade: TeaGrade.PREMIUM, origin: 'EU Grade', flavorNotes: 'Base hojicha for drinks' },
    { code: 'H04', name: 'Kōbashii Hōjicha', grade: TeaGrade.PREMIUM, origin: 'Japan', flavorNotes: 'กลิ่นคั่วหอม ชัด' },
    { code: 'H05', name: 'Shizuoka Maple Fumi Hojicha', grade: TeaGrade.PREMIUM, origin: 'Shizuoka', flavorNotes: 'Maple, smoky, soft' },
    { code: 'H06', name: 'Hojicha Shinbai', grade: TeaGrade.PREMIUM, origin: 'Japan', flavorNotes: 'Rich roasted' },
    { code: 'G01', name: 'Genmaicha Uguisu', grade: TeaGrade.PREMIUM, origin: 'Japan', flavorNotes: 'Rice aroma, light green tea' },
    { code: 'T01', name: 'Jasmine Thai Tea', grade: TeaGrade.CULINARY, origin: 'Thailand', flavorNotes: 'Jasmine, milk tea base' },
  ]

  for (const c of cultivars) {
    await prisma.teaCultivar.upsert({
      where: { code: c.code },
      update: { ...c },
      create: { ...c },
    })
  }
  console.log(`✅ Upserted ${cultivars.length} tea cultivars`)

  // ─── 2. BRANCHES ─────────────────────────────────────────────────────────────
  const branches = [
    { name: 'ลาดพร้าว 107', nameEn: 'Ladprao 107', slug: 'ladprao-107', district: 'ลาดพร้าว' },
    { name: 'สามย่าน', nameEn: 'Samyan', slug: 'samyan', district: 'สามย่าน (ปากซอยจุฬา)', address: 'ปากซอยจุฬา' },
    { name: 'นวมินทร์ 111', nameEn: 'Nawamin 111', slug: 'nawamin-111', district: 'นวมินทร์' },
    { name: 'นาคนิวาส 48', nameEn: 'Nakniwat 48', slug: 'nakniwat-48', district: 'นาคนิวาส' },
    { name: 'สะพานควาย', nameEn: 'Saphankwai', slug: 'saphankwai', district: 'สะพานควาย' },
  ]

  for (const b of branches) {
    await prisma.branch.upsert({
      where: { slug: b.slug },
      update: { ...b },
      create: { ...b },
    })
  }
  console.log(`✅ Upserted ${branches.length} branches`)

  // ─── 3. MENU CATEGORIES ──────────────────────────────────────────────────────
  const categories = [
    { slug: 'matcha-classic', name: 'Matcha Classic', nameEn: 'Matcha Classic', description: 'มัทฉะคลาสสิก เลือกสายพันธุ์ได้' },
    { slug: 'hojicha', name: 'โฮจิฉะ', nameEn: 'Hojicha', description: 'ชาคั่วญี่ปุ่นแท้' },
    { slug: 'genmaicha', name: 'เก็นไมฉะ', nameEn: 'Genmaicha', description: 'ชาข้าวญี่ปุ่น' },
    { slug: 'refresher', name: 'Refresher', nameEn: 'Matcha Refresher', description: 'เครื่องดื่มมัทฉะใสเย็นสดชื่น' },
    { slug: 'latte', name: 'Matcha Latte', nameEn: 'Matcha Milk & Latte', description: 'ลาเต้มัทฉะ นุ่มละมุน' },
    { slug: 'fixed-recipe', name: 'Fixed Recipe', nameEn: 'Fixed Recipe', description: 'เมนูตายตัว สูตรพิเศษ' },
    { slug: 'signature', name: 'Hibi Craft Matcha', nameEn: 'Hibi Craft Matcha (Signature)', description: 'เมนู Signature สร้างสรรค์พิเศษ' },
    { slug: 'dessert', name: 'Fusion Dessert', nameEn: 'Fusion Dessert', description: 'ของหวาน Fusion สไตล์ญี่ปุ่น' },
    { slug: 'non-matcha', name: 'Non Matcha', nameEn: 'Non Matcha', description: 'เครื่องดื่มสำหรับคนไม่ดื่มมัทฉะ' },
    { slug: 'tea-for-home', name: 'Tea for Home', nameEn: 'Tea for Home', description: 'ผงมัทฉะสำหรับชงเอง' },
  ]

  const catMap: Record<string, string> = {}
  for (const cat of categories) {
    const result = await prisma.productCategory.upsert({
      where: { slug: cat.slug },
      update: { name: cat.name, nameEn: cat.nameEn, description: cat.description },
      create: { ...cat, image: `/images/categories/${cat.slug}.jpg`, isActive: true },
    })
    catMap[cat.slug] = result.id
  }
  console.log(`✅ Upserted ${categories.length} menu categories`)

  // ─── 4. MENU OPTIONS ─────────────────────────────────────────────────────────
  const options = [
    { code: 'A1-STANDARD', name: 'Standard (พร้อมดื่ม)', groupName: 'Packing', priceAdjust: 0 },
    { code: 'A1-COOLPACK', name: 'Cool Pack (แยกน้ำแข็ง)', groupName: 'Packing', priceAdjust: 5 },
    { code: 'B1-COLD', name: 'Cold (เย็น)', groupName: 'Temperature', priceAdjust: 0 },
    { code: 'B1-HOT', name: 'Hot (ร้อน)', groupName: 'Temperature', priceAdjust: 0 },
    { code: 'C1-EXTRA-MATCHA', name: 'Extra Matcha (+1 tsp)', groupName: 'Extra', priceAdjust: 30 },
    { code: 'D1-NO-SUGAR', name: 'ไม่หวาน (No Sugar)', groupName: 'Sweetness', priceAdjust: 0 },
    { code: 'D1-LESS-SUGAR', name: 'หวานน้อย (Less Sugar)', groupName: 'Sweetness', priceAdjust: 0 },
    { code: 'D1-NORMAL-SUGAR', name: 'หวานปกติ (Normal)', groupName: 'Sweetness', priceAdjust: 0 },
    { code: 'E2-OAT-MILK', name: 'Oat Milk', groupName: 'Milk', priceAdjust: 20 },
    { code: 'E2-ALMOND-MILK', name: 'Almond Milk', groupName: 'Milk', priceAdjust: 20 },
    { code: 'F1-MOCHI', name: 'Add Mochi', groupName: 'Topping', priceAdjust: 25 },
    { code: 'F1-RED-BEAN', name: 'Add Red Bean', groupName: 'Topping', priceAdjust: 20 },
    { code: 'F1-TARO', name: 'Add Taro', groupName: 'Topping', priceAdjust: 20 },
  ]

  for (const opt of options) {
    await prisma.menuOption.upsert({
      where: { code: opt.code },
      update: { ...opt },
      create: { ...opt, isActive: true },
    })
  }
  console.log(`✅ Upserted ${options.length} menu options`)

  // ─── 5. PRODUCTS — MATCHA CLASSIC ────────────────────────────────────────────
  const matchaClassicItems = [
    // Master Piece Collection
    { sku: 'HBC01M37C', name: 'Classic Clear Matcha Exhibit No.1 Yuzuru', price: 845, deliveryPrice: 1235, description: 'มัทฉะระดับ Master Piece สายพันธุ์ Yuzuru เกรดพิธีการหายากที่สุด', cultivarCode: 'M37', tags: '["masterpiece","ceremonial","premium"]' },
    { sku: 'HBC01M39C', name: 'Classic Clear Matcha Exhibit No.2 Rin', price: 595, deliveryPrice: 650, description: 'มัทฉะใสสายพันธุ์ Rin คอลเลกชัน Exhibit พิเศษ', cultivarCode: 'M39', tags: '["masterpiece","ceremonial"]' },
    { sku: 'HBC01M39L', name: 'Classic Matcha Latte Exhibit No.3 Yumemi', price: 450, deliveryPrice: 490, description: 'มัทฉะลาเต้สายพันธุ์ Yumemi', cultivarCode: 'M39', tags: '["masterpiece","latte"]' },
    // Premium Ceremonial
    { sku: 'HBC01M08C', name: 'Classic Clear Matcha Gyokuro Yame', price: 315, deliveryPrice: 390, description: 'มัทฉะใสจากชาเกรดพิเศษสำหรับเมนูคลาสสิก เผยรสอูมามิแท้และความหอมบริสุทธิ์ของชาเขียว ดื่มสดชื่นแบบคลีน', cultivarCode: 'M08', tags: '["ceremonial","premium","gyokuro"]' },
    { sku: 'HBC01M04C', name: 'Classic Clear Matcha Uji Samidori', price: 304, deliveryPrice: 325, description: 'หวานละมุน ไม่ขม หอมกลิ่นถั่วและเต้าหู้ขาว', cultivarCode: 'M04', tags: '["ceremonial","uji"]' },
    { sku: 'HBC01M04L', name: 'Classic Matcha Latte Uji Samidori', price: 445, deliveryPrice: 480, description: 'ลาเต้ Uji Samidori นุ่มละมุน', cultivarCode: 'M04', tags: '["ceremonial","uji","latte"]' },
    { sku: 'HBC01M06C', name: 'Classic Clear Matcha Uji Okumidori', price: 235, deliveryPrice: 255, description: 'หอมสาหร่าย ลึก อูมามิแน่น สายพันธุ์ Okumidori จาก Uji', cultivarCode: 'M06', tags: '["ceremonial","uji"]' },
    { sku: 'HBC01M06L', name: 'Classic Matcha Latte Uji Okumidori', price: 340, deliveryPrice: 365, description: 'ลาเต้ Uji Okumidori', cultivarCode: 'M06', tags: '["ceremonial","uji","latte"]' },
    { sku: 'HBC01M03C', name: 'Classic Clear Matcha Uji Kazen', price: 210, deliveryPrice: 229, description: 'หอมดอกไม้และข้าวคั่ว ขมนุ่ม สดชื่นสะอาด', cultivarCode: 'M03', tags: '["ceremonial","uji"]' },
    // Ceremonial Grade
    { sku: 'HBC01M01C', name: 'Classic Clear Matcha Kagoshima Asanoka', price: 130, deliveryPrice: 149, description: 'ออร์แกนิค หอมสะอาด คลีน อูมามิกลางๆ', cultivarCode: 'M01', tags: '["ceremonial","organic","kagoshima"]' },
    { sku: 'HBC01M01L', name: 'Classic Matcha Latte Kagoshima Asanoka', price: 195, deliveryPrice: 219, description: 'ลาเต้ออร์แกนิค Kagoshima Asanoka', cultivarCode: 'M01', tags: '["ceremonial","organic","kagoshima","latte"]' },
    { sku: 'HBC01M02C', name: 'Classic Clear Matcha Kagoshima Shinju', price: 180, deliveryPrice: 199, description: 'Kagoshima First Harvest Shinju หอมครีมมี่ ฟลัชแรก', cultivarCode: 'M02', tags: '["ceremonial","kagoshima"]' },
    { sku: 'HBC01M26C', name: 'Classic Clear Matcha Kagoshima Okumidori', price: 145, deliveryPrice: 165, description: 'ออร์แกนิค Okumidori จาก Kagoshima', cultivarCode: 'M26', tags: '["ceremonial","organic","kagoshima"]' },
    { sku: 'HBC01M26L', name: 'Classic Matcha Latte Kagoshima Okumidori', price: 205, deliveryPrice: 225, description: 'ลาเต้ออร์แกนิค Kagoshima Okumidori', cultivarCode: 'M26', tags: '["ceremonial","organic","latte"]' },
    { sku: 'HBC01M09C', name: 'Classic Clear Matcha Organic Yabukita', price: 180, deliveryPrice: 199, description: 'Organic Yabukita จาก Yame Fukuoka บริสุทธิ์ 100%', cultivarCode: 'M09', tags: '["ceremonial","organic","yame"]' },
    { sku: 'HBC01M10C', name: 'Classic Clear Matcha Yame Saemidori', price: 105, deliveryPrice: 119, description: 'หอมถั่วและเต้าหู้ Saemidori ระดับพรีเมียมจาก Yame', cultivarCode: 'M10', tags: '["premium","yame"]' },
    { sku: 'HBC01M10L', name: 'Classic Matcha Latte Yame Saemidori', price: 145, deliveryPrice: 165, description: 'ลาเต้ Yame Saemidori', cultivarCode: 'M10', tags: '["premium","yame","latte"]' },
    { sku: 'HBC01M12C', name: 'Classic Clear Matcha Yame First Harvest', price: 80, deliveryPrice: 95, description: 'Yame First Harvest ชาฤดูกาลแรก', cultivarCode: 'M12', tags: '["premium","yame"]' },
    { sku: 'HBC01M30C', name: 'Classic Clear Matcha Kagoshima Loishi', price: 115, deliveryPrice: 129, description: 'ออร์แกนิค Loishi จาก Kagoshima นุ่มสะอาด', cultivarCode: 'M30', tags: '["ceremonial","organic","kagoshima"]' },
    { sku: 'HBC01M30L', name: 'Classic Matcha Latte Kagoshima Loishi', price: 165, deliveryPrice: 185, description: 'ลาเต้ออร์แกนิค Kagoshima Loishi', cultivarCode: 'M30', tags: '["ceremonial","organic","latte"]' },
    { sku: 'HBC01M40C', name: 'Classic Clear Matcha O-Matcha Sou', price: 99, deliveryPrice: 115, description: 'Shizuoka Cha no Niwa O-Matcha Sou สดชื่น', cultivarCode: 'M40', tags: '["ceremonial","shizuoka"]' },
    { sku: 'HBC01M40L', name: 'Classic Matcha Latte O-Matcha Sou', price: 155, deliveryPrice: 175, description: 'ลาเต้ O-Matcha Sou จาก Shizuoka', cultivarCode: 'M40', tags: '["ceremonial","shizuoka","latte"]' },
    { sku: 'HBC01M42C', name: 'Classic Clear Matcha Fuji Yabukita 2nd Flush', price: 100, deliveryPrice: 119, description: 'Fuji Yabukita Second Flush ฤดูที่สอง', cultivarCode: 'M42', tags: '["premium","fuji"]' },
    // Hibi Blends
    { sku: 'HBC01M19C', name: 'Classic Clear Matcha Hibi Tsuchi Blend', price: 69, deliveryPrice: 79, description: 'สดชื่น โทนไม้ ซิตรัส เข้าง่าย เหมาะสำหรับผู้เริ่มต้น', cultivarCode: 'M19', tags: '["premium","blend","hibi"]' },
    { sku: 'HBC01M19L', name: 'Classic Matcha Latte Hibi Tsuchi Blend', price: 80, deliveryPrice: 95, description: 'ลาเต้ Hibi Tsuchi Blend นุ่มละมุน', cultivarCode: 'M19', tags: '["premium","blend","hibi","latte"]' },
    { sku: 'HBC01M20C', name: 'Classic Clear Matcha Hibi Kumo Blend', price: 79, deliveryPrice: 89, description: 'หอมข้าวโพด และอโวคาโด Hibi Kumo Blend', cultivarCode: 'M20', tags: '["premium","blend","hibi"]' },
    { sku: 'HBC01M20L', name: 'Classic Matcha Latte Hibi Kumo Blend', price: 95, deliveryPrice: 109, description: 'ลาเต้ Hibi Kumo Blend', cultivarCode: 'M20', tags: '["premium","blend","hibi","latte"]' },
    { sku: 'HBC01M21C', name: 'Classic Clear Matcha Hibi Sayaka', price: 79, deliveryPrice: 89, description: 'Hibi Sayaka กลิ่นชาสดชื่น', cultivarCode: 'M21', tags: '["premium","blend","hibi"]' },
    { sku: 'HBC01M22C', name: 'Classic Clear Matcha Hibi Shizuku', price: 79, deliveryPrice: 89, description: 'Hibi Shizuku หยดชาแท้', cultivarCode: 'M22', tags: '["premium","blend","hibi"]' },
    { sku: 'HBC01M23C', name: 'Classic Clear Matcha Hibi Noko', price: 69, deliveryPrice: 79, description: 'Hibi Noko จาก Unkyō (雲郷)', cultivarCode: 'M23', tags: '["premium","blend","hibi"]' },
    // Baisen (Roasted)
    { sku: 'HBC01M32C', name: 'Classic Clear Matcha Kagoshima Saemidori Baisen', price: 95, deliveryPrice: 109, description: 'Saemidori คั่วพิเศษ รสชาติเข้มข้นขึ้น', cultivarCode: 'M32', tags: '["premium","baisen","kagoshima"]' },
    { sku: 'HBC01M32L', name: 'Classic Matcha Latte Kagoshima Saemidori Baisen', price: 135, deliveryPrice: 155, description: 'ลาเต้ Saemidori Baisen', cultivarCode: 'M32', tags: '["premium","baisen","latte"]' },
    { sku: 'HBC01M33C', name: 'Classic Clear Matcha Kagoshima Kanayamidori Baisen', price: 95, deliveryPrice: 109, description: 'Kanayamidori คั่วพิเศษ', cultivarCode: 'M33', tags: '["premium","baisen","kagoshima"]' },
    { sku: 'HBC01M34L', name: 'Classic Matcha Latte Kagoshima Okumidori Baisen', price: 135, deliveryPrice: 155, description: 'ลาเต้ Okumidori Baisen', cultivarCode: 'M34', tags: '["premium","baisen","latte"]' },
  ]

  for (const item of matchaClassicItems) {
    const cultivar = item.cultivarCode
      ? await prisma.teaCultivar.findUnique({ where: { code: item.cultivarCode } })
      : null

    await prisma.product.upsert({
      where: { sku: item.sku },
      update: {
        price: item.price,
        deliveryPrice: item.deliveryPrice,
        description: item.description,
        tags: item.tags,
        cultivarId: cultivar?.id,
      },
      create: {
        sku: item.sku,
        name: item.name,
        nameEn: item.name,
        description: item.description,
        price: item.price,
        deliveryPrice: item.deliveryPrice,
        image: '/images/menu/matcha-classic.jpg',
        categoryId: catMap['matcha-classic'],
        cultivarId: cultivar?.id,
        isActive: true,
        tags: item.tags,
        stock: 999,
      },
    })
  }
  console.log(`✅ Upserted ${matchaClassicItems.length} Matcha Classic items`)

  // ─── 6. PRODUCTS — HOJICHA ───────────────────────────────────────────────────
  const hojichaItems = [
    { sku: 'HBC02H02C', name: 'Classic Clear Hojicha Kokoro', price: 80, deliveryPrice: 95, description: 'Hojicha Kokoro เกรดพิธีการ หอมอัลมอนด์ คาราเมล กลิ่นคั่วธรรมชาติ', cultivarCode: 'H02', tags: '["ceremonial","hojicha"]' },
    { sku: 'HBC02H02L', name: 'Classic Hojicha Latte Kokoro', price: 105, deliveryPrice: 119, description: 'ลาเต้ Hojicha Kokoro นุ่มหอม', cultivarCode: 'H02', tags: '["ceremonial","hojicha","latte"]' },
    { sku: 'HBC02H01C', name: 'Classic Clear Hojicha Kaori', price: 70, deliveryPrice: 85, description: 'Hojicha Kaori หอมคั่ว ละมุน เบา ดื่มง่ายทุกวัน', cultivarCode: 'H01', tags: '["premium","hojicha"]' },
    { sku: 'HBC02H01L', name: 'Classic Hojicha Latte Kaori', price: 95, deliveryPrice: 109, description: 'ลาเต้ Hojicha Kaori', cultivarCode: 'H01', tags: '["premium","hojicha","latte"]' },
    { sku: 'HBC02H04C', name: 'Classic Clear Kōbashii Hōjicha', price: 80, deliveryPrice: 95, description: 'กลิ่นคั่วหอม ชัดเจน อบอุ่นแบบธรรมชาติ', cultivarCode: 'H04', tags: '["premium","hojicha"]' },
    { sku: 'HBC02H04L', name: 'Classic Kōbashii Hōjicha Latte', price: 95, deliveryPrice: 109, description: 'ลาเต้ Kōbashii Hōjicha', cultivarCode: 'H04', tags: '["premium","hojicha","latte"]' },
    { sku: 'HBC02H05C', name: 'Classic Clear Shizuoka Maple Fumi Hojicha', price: 60, deliveryPrice: 79, description: 'Shizuoka Maple Fumi นุ่ม หอม Maple เบาๆ', cultivarCode: 'H05', tags: '["premium","hojicha","shizuoka"]' },
    { sku: 'HBC02H05L', name: 'Classic Shizuoka Maple Fumi Hojicha Latte', price: 80, deliveryPrice: 95, description: 'ลาเต้ Shizuoka Maple Fumi', cultivarCode: 'H05', tags: '["premium","hojicha","latte"]' },
    { sku: 'HBC02H06C', name: 'Classic Clear Hojicha Shinbai', price: 85, deliveryPrice: 99, description: 'Hojicha Shinbai เข้มข้น หอมคั่ว', cultivarCode: 'H06', tags: '["premium","hojicha"]' },
    { sku: 'HBC02H06L', name: 'Classic Hojicha Latte Shinbai', price: 120, deliveryPrice: 139, description: 'ลาเต้ Hojicha Shinbai', cultivarCode: 'H06', tags: '["premium","hojicha","latte"]' },
  ]

  for (const item of hojichaItems) {
    const cultivar = item.cultivarCode
      ? await prisma.teaCultivar.findUnique({ where: { code: item.cultivarCode } })
      : null
    await prisma.product.upsert({
      where: { sku: item.sku },
      update: { price: item.price, deliveryPrice: item.deliveryPrice, cultivarId: cultivar?.id },
      create: {
        sku: item.sku, name: item.name, nameEn: item.name,
        description: item.description, price: item.price, deliveryPrice: item.deliveryPrice,
        image: '/images/menu/hojicha.jpg', categoryId: catMap['hojicha'],
        cultivarId: cultivar?.id, isActive: true, tags: item.tags, stock: 999,
      },
    })
  }
  console.log(`✅ Upserted ${hojichaItems.length} Hojicha items`)

  // ─── 7. PRODUCTS — GENMAICHA ─────────────────────────────────────────────────
  await prisma.product.upsert({
    where: { sku: 'HBC03G01C' },
    update: { price: 65, deliveryPrice: 79 },
    create: {
      sku: 'HBC03G01C', name: 'Classic Clear Genmaicha Uguisu', nameEn: 'Classic Clear Genmaicha Uguisu',
      description: 'เก็นไมฉะ หอมข้าวคั่ว ชาเขียวเบาๆ สดชื่น ดื่มง่าย',
      price: 65, deliveryPrice: 79, image: '/images/menu/genmaicha.jpg',
      categoryId: catMap['genmaicha'],
      cultivarId: (await prisma.teaCultivar.findUnique({ where: { code: 'G01' } }))?.id,
      isActive: true, tags: '["genmaicha","rice-tea"]', stock: 999,
    },
  })
  await prisma.product.upsert({
    where: { sku: 'HBC03G01L' },
    update: { price: 75, deliveryPrice: 89 },
    create: {
      sku: 'HBC03G01L', name: 'Classic Genmaicha Latte Uguisu', nameEn: 'Classic Genmaicha Latte Uguisu',
      description: 'เก็นไมฉะลาเต้ หอมข้าวคั่ว นุ่มละมุน',
      price: 75, deliveryPrice: 89, image: '/images/menu/genmaicha.jpg',
      categoryId: catMap['genmaicha'], isActive: true, tags: '["genmaicha","latte"]', stock: 999,
    },
  })

  // ─── 8. PRODUCTS — REFRESHERS ────────────────────────────────────────────────
  const refreshers = [
    { sku: 'HBR01M21C', name: 'Clear Matcha', price: 69, deliveryPrice: 79, description: 'มัทฉะใสสดชื่น เรียบง่าย คลีน' },
    { sku: 'HBR02M21C', name: 'Matcha Honey Lemon', price: 89, deliveryPrice: 99, description: 'มัทฉะน้ำผึ้งมะนาว Homemade' },
    { sku: 'HBR03M21C', name: 'Matcha Honey Lime', price: 89, deliveryPrice: 99, description: 'มัทฉะน้ำผึ้งไลม์ Homemade' },
    { sku: 'HBR04M21C', name: 'Kirei Yuzu Matcha', price: 89, deliveryPrice: 99, description: 'มัทฉะยูสุ คลีน หอมซิตรัส' },
    { sku: 'HBR05M21C', name: 'Kori Osmanthus Matcha', price: 89, deliveryPrice: 99, description: 'มัทฉะดอกออสมันธัส หอมละมุน' },
    { sku: 'HBR06M21C', name: 'Clear Matcha Coconut Jasmine Tea', price: 89, deliveryPrice: 99, description: 'มัทฉะมะพร้าวชามะลิ สดชื่น' },
    { sku: 'HBR07M21C', name: 'Clear Matcha Coconut', price: 79, deliveryPrice: 89, description: 'มัทฉะใสมะพร้าว คลีน เย็นสดชื่น' },
    { sku: 'HBR08H03C', name: 'Clear Hojicha', price: 69, deliveryPrice: 79, description: 'โฮจิฉะใส หอมคั่ว เบา สดชื่น' },
    { sku: 'HBR09M21C', name: 'Clear Matcha Chrysanthemum', price: 79, deliveryPrice: 89, description: 'มัทฉะใสเบญจมาศ หอมดอกไม้ สดชื่น' },
  ]

  for (const item of refreshers) {
    await prisma.product.upsert({
      where: { sku: item.sku },
      update: { price: item.price, deliveryPrice: item.deliveryPrice },
      create: {
        ...item, nameEn: item.name, image: '/images/menu/refresher.jpg',
        categoryId: catMap['refresher'], isActive: true, tags: '["refresher","cold"]', stock: 999,
      },
    })
  }
  console.log(`✅ Upserted ${refreshers.length} Refresher items`)

  // ─── 9. PRODUCTS — LATTE (MILK & RICH) ──────────────────────────────────────
  const lattes = [
    { sku: 'HBM09M19L', name: 'Hibi Cold Whisk Latte', price: 59, deliveryPrice: 79, description: 'Whisk Latte แบบ Cold เบสมัทฉะ Hibi Tsuchi ราคาเข้าถึงง่าย' },
    { sku: 'HBM01M18L', name: 'Matcha Latte (Milk Whisk)', price: 79, deliveryPrice: 89, description: 'ลาเต้มัทฉะ Whisk สไตล์ญี่ปุ่น ไมโครโฟมนุ่มละเอียด' },
    { sku: 'HBM02M18L', name: 'Matcha Latte Milk Mochi', price: 105, deliveryPrice: 129, description: 'ลาเต้มัทฉะ + โมจิ นุ่มหนึบ' },
    { sku: 'HBM03M18L', name: 'Osmanthus Matcha Latte', price: 99, deliveryPrice: 109, description: 'ลาเต้มัทฉะดอกออสมันธัส หอมหวาน' },
    { sku: 'HBM04M18L', name: 'Matcha Mango Latte', price: 99, deliveryPrice: 109, description: 'ลาเต้มัทฉะมะม่วง ฤดูร้อน' },
    { sku: 'HBM05M18L', name: 'Matcha Strawberry Latte', price: 89, deliveryPrice: 109, description: 'ลาเต้มัทฉะสตรอว์เบอร์รี' },
    { sku: 'HBM06M18L', name: 'Matcha Milk Mochi Taro Latte', price: 125, deliveryPrice: 149, description: 'ลาเต้มัทฉะโมจิเผือก' },
    { sku: 'HBM07M18L', name: 'Matcha Milk Mochi Red Bean Latte', price: 125, deliveryPrice: 149, description: 'ลาเต้มัทฉะโมจิถั่วแดง' },
    { sku: 'HBM08H03L', name: 'Hojicha Latte (Milk Whisk)', price: 79, deliveryPrice: 89, description: 'ลาเต้โฮจิฉะ Whisk Style นุ่มหอมคั่ว' },
  ]

  for (const item of lattes) {
    await prisma.product.upsert({
      where: { sku: item.sku },
      update: { price: item.price, deliveryPrice: item.deliveryPrice },
      create: {
        ...item, nameEn: item.name, image: '/images/menu/latte.jpg',
        categoryId: catMap['latte'], isActive: true, tags: '["latte","milk"]', stock: 999,
      },
    })
  }
  console.log(`✅ Upserted ${lattes.length} Latte items`)

  // ─── 10. PRODUCTS — FIXED RECIPE ─────────────────────────────────────────────
  const fixedRecipes = [
    { sku: 'HBF01', name: 'Coconut on Cloud', price: 79, deliveryPrice: 99, description: 'เมนูมะพร้าวบนก้อนเมฆ เนื้อสัมผัสพิเศษ' },
    { sku: 'HBF02M18L', name: 'Coconut Milk Whisk Latte', price: 79, deliveryPrice: 99, description: 'ลาเต้มะพร้าว Whisk Style' },
    { sku: 'HBF03', name: 'Matcha Cloud Latte', price: 79, deliveryPrice: 99, description: 'ลาเต้มัทฉะกลุ่มเมฆ เนื้อครีมนุ่ม' },
    { sku: 'HBF04', name: 'Matcha Cheesecake Cloud', price: 99, deliveryPrice: 129, description: 'ลาเต้มัทฉะชีสเค้กก้อนเมฆ ฮิตมาก' },
    { sku: 'HBF05M18L', name: 'Matcha Cream Cheese Latte', price: 99, deliveryPrice: 119, description: 'ลาเต้มัทฉะครีมชีส เข้มข้น' },
    { sku: 'HBF06M18L', name: 'Jasmine Thai Tea x Matcha Latte', price: 109, deliveryPrice: 119, description: 'ชามะลิไทยผสมมัทฉะลาเต้ Fusion สไตล์ไทย-ญี่ปุ่น' },
  ]

  for (const item of fixedRecipes) {
    await prisma.product.upsert({
      where: { sku: item.sku },
      update: { price: item.price, deliveryPrice: item.deliveryPrice },
      create: {
        ...item, nameEn: item.name, image: '/images/menu/fixed-recipe.jpg',
        categoryId: catMap['fixed-recipe'], isActive: true, tags: '["fixed","special"]', stock: 999,
      },
    })
  }
  console.log(`✅ Upserted ${fixedRecipes.length} Fixed Recipe items`)

  // ─── 11. PRODUCTS — SIGNATURE ────────────────────────────────────────────────
  const signatureItems = [
    { sku: 'HBCS01', name: 'Matcha Mango Pandan Cloud', price: 169, deliveryPrice: 189, description: 'มัทฉะมะม่วงใบเตยก้อนเมฆ — Hibi Craft Signature' },
    { sku: 'HBCS02', name: 'Pandan Coconut Matcha Velvet', price: 159, deliveryPrice: 179, description: 'ใบเตยมะพร้าวมัทฉะ Velvet สูตร Signature' },
    { sku: 'HBCS03', name: 'Pistachio Kunafa Matcha Luxe', price: 189, deliveryPrice: 199, description: 'พิสตาชิโอ Kunafa มัทฉะ Luxe — เมนูพรีเมียมสุด' },
    { sku: 'HBCS04', name: 'Matcha Tiramisu Lady', price: 179, deliveryPrice: 189, description: 'ทิรามิสุมัทฉะ Lady สไตล์ Hibi' },
    { sku: 'HBCS05', name: 'Kokoro Hojicha Honeycomb Velvet', price: 159, deliveryPrice: 179, description: 'โฮจิฉะ Kokoro รวงผึ้ง Velvet' },
    { sku: 'HBCS06', name: 'Matcha Cheesecake Mochi Skewer', price: 159, deliveryPrice: 179, description: 'ไม้เสียบชีสเค้กมัทฉะโมจิ — Instagrammable' },
    { sku: 'HBCS07', name: 'Kokoro Hojicha Cheesecake Mochi', price: 179, deliveryPrice: 199, description: 'โฮจิฉะ Kokoro ชีสเค้กโมจิ' },
    { sku: 'HBCS08', name: 'Matcha Velvet Whisk Latte', price: 129, deliveryPrice: 149, description: 'Whisk Latte Velvet มัทฉะ Cold Foam' },
  ]

  for (const item of signatureItems) {
    await prisma.product.upsert({
      where: { sku: item.sku },
      update: { price: item.price, deliveryPrice: item.deliveryPrice },
      create: {
        ...item, nameEn: item.name, image: '/images/menu/signature.jpg',
        categoryId: catMap['signature'], isActive: true, tags: '["signature","craft","premium"]', stock: 999,
      },
    })
  }
  console.log(`✅ Upserted ${signatureItems.length} Signature items`)

  // ─── 12. PRODUCTS — FUSION DESSERT ───────────────────────────────────────────
  const desserts = [
    { sku: 'HBD01', name: 'Truffle Noir Basque Cheesecake', price: 89, deliveryPrice: 99, description: 'Basque Cheesecake ทรัฟเฟิล Noir' },
    { sku: 'HBD02M29', name: 'Basque Matcha Azuki Mochi Cheesecake', price: 89, deliveryPrice: 99, description: 'Basque Cheesecake มัทฉะถั่วแดงโมจิ' },
    { sku: 'HBD03', name: 'Shiro Tofu Cheesecake', price: 69, deliveryPrice: 79, description: 'ชีสเค้กเต้าหู้ขาว เบา นุ่มละมุน' },
    { sku: 'HBD04A', name: 'Black Truffle Financier', price: 35, deliveryPrice: 45, description: 'Financier ทรัฟเฟิลดำ' },
    { sku: 'HBD04B', name: 'Citrus Noisette Financier', price: 35, deliveryPrice: 40, description: 'Financier ซิตรัส Noisette' },
    { sku: 'HBD04C', name: 'Matcha Yuzu Financier', price: 39, deliveryPrice: 45, description: 'Financier มัทฉะยูสุ' },
    { sku: 'HBD04D', name: 'Matcha Noisette Financier', price: 35, deliveryPrice: 40, description: 'Financier มัทฉะ Noisette' },
    { sku: 'HBD04E', name: 'Noisette Financier', price: 30, deliveryPrice: 35, description: 'Financier Noisette คลาสสิก' },
    { sku: 'HBD06A', name: 'Tiramisu Matcha (Homemade)', price: 69, deliveryPrice: 79, description: 'ทิรามิสุมัทฉะ Homemade' },
    { sku: 'HBD06C', name: 'Classic Tiramisu (Homemade)', price: 69, deliveryPrice: 79, description: 'ทิรามิสุคลาสสิก Homemade' },
    { sku: 'HBD07A', name: 'Matcha Milk Mochi Brown Sugar Azuki', price: 69, deliveryPrice: 79, description: 'โมจิน้ำนมมัทฉะน้ำตาลทรายแดงถั่วแดง' },
    { sku: 'HBD07B', name: 'Matcha Milk Mochi Brown Sugar Taro', price: 69, deliveryPrice: 79, description: 'โมจิน้ำนมมัทฉะน้ำตาลทรายแดงเผือก' },
    { sku: 'HBD11', name: 'Mochi Butter Bun', price: 39, deliveryPrice: 49, description: 'ขนมปังโมจิเนย' },
    { sku: 'HBD11M', name: 'Matcha Mochi Butter Bun', price: 49, deliveryPrice: 59, description: 'ขนมปังโมจิมัทฉะเนย' },
    { sku: 'HBD20', name: 'Matcha Mochi Kinako Caramel', price: 79, deliveryPrice: 89, description: 'โมจิมัทฉะ Kinako คาราเมล' },
  ]

  for (const item of desserts) {
    await prisma.product.upsert({
      where: { sku: item.sku },
      update: { price: item.price, deliveryPrice: item.deliveryPrice },
      create: {
        ...item, nameEn: item.name, image: '/images/menu/dessert.jpg',
        categoryId: catMap['dessert'], isActive: true, tags: '["dessert","fusion"]', stock: 999,
      },
    })
  }
  console.log(`✅ Upserted ${desserts.length} Dessert items`)

  // ─── 13. PRODUCTS — NON MATCHA ───────────────────────────────────────────────
  const nonMatchaItems = [
    { sku: 'HBN01A', name: 'Honey Lime Soda', price: 69, deliveryPrice: 79, description: 'โซดาน้ำผึ้งมะนาว สดชื่น' },
    { sku: 'HBN01B', name: 'Honey Lemon Soda', price: 69, deliveryPrice: 79, description: 'โซดาน้ำผึ้งเลมอน' },
    { sku: 'HBN02', name: 'Honey Lime Plum Soda', price: 79, deliveryPrice: 89, description: 'โซดาน้ำผึ้งมะนาวบ๊วย' },
    { sku: 'HBN03', name: 'Ichigo Ume Refresher', price: 79, deliveryPrice: 89, description: 'Refresher สตรอว์เบอร์รีอุเมะ' },
    { sku: 'HBN04', name: 'Osmanthus Honey Coconut', price: 69, deliveryPrice: 79, description: 'ดอกออสมันธัสน้ำผึ้งมะพร้าว' },
    { sku: 'HBN05', name: 'Orange Yuzu Soda', price: 69, deliveryPrice: 79, description: 'โซดาส้มยูสุ' },
    { sku: 'HBN06', name: 'Jasmine Thai Tea', price: 69, deliveryPrice: 79, description: 'ชาไทยมะลิ หอมละมุน' },
    { sku: 'HBN07', name: 'Jasmine Thai Tea Mochi', price: 99, deliveryPrice: 109, description: 'ชาไทยมะลิ + โมจิ' },
    { sku: 'HBN08', name: 'Jasmine Taro Milk Tea Mochi', price: 129, deliveryPrice: 139, description: 'ชานมไทยมะลิเผือกโมจิ' },
    { sku: 'HBN09', name: 'Pandan Mango Mochi Cream Cheese', price: 139, deliveryPrice: 159, description: 'ใบเตยมะม่วงโมจิครีมชีส' },
    { sku: 'HBN10', name: 'Pandan Mochi Caramel Coconut Milk', price: 129, deliveryPrice: 149, description: 'ใบเตยโมจิคาราเมลกะทิ' },
  ]

  for (const item of nonMatchaItems) {
    await prisma.product.upsert({
      where: { sku: item.sku },
      update: { price: item.price, deliveryPrice: item.deliveryPrice },
      create: {
        ...item, nameEn: item.name, image: '/images/menu/non-matcha.jpg',
        categoryId: catMap['non-matcha'], isActive: true, tags: '["non-matcha","drink"]', stock: 999,
      },
    })
  }
  console.log(`✅ Upserted ${nonMatchaItems.length} Non-Matcha items`)

  // ─── 14. PRODUCTS — TEA FOR HOME ─────────────────────────────────────────────
  const teaForHome = [
    { sku: 'TH-M08-20G', name: 'Gyokuro Yame Matcha Powder 20g', price: 1600, description: 'ผงมัทฉะ Gyokuro Yame 20g สำหรับชงเองที่บ้าน เกรดพิธีการ' },
    { sku: 'TH-M10-20G', name: 'Yame Saemidori Matcha Powder 20g', price: 450, description: 'ผงมัทฉะ Yame Saemidori 20g' },
    { sku: 'TH-M18-100G', name: 'Hibi Daichi Blend Matcha 100g', price: 850, description: 'ผงมัทฉะ Hibi Daichi Blend 100g เหมาะสำหรับทำขนมและชง' },
    { sku: 'TH-H01-100G', name: 'Hojicha Kaori Powder 100g', price: 490, description: 'ผงโฮจิฉะ Kaori 100g สำหรับชงเอง' },
    { sku: 'TH-M19-50G', name: 'Hibi Tsuchi Blend Matcha 50g', price: 350, description: 'ผงมัทฉะ Hibi Tsuchi Blend 50g' },
  ]

  for (const item of teaForHome) {
    await prisma.product.upsert({
      where: { sku: item.sku },
      update: { price: item.price },
      create: {
        ...item, nameEn: item.name, deliveryPrice: item.price + 50,
        image: '/images/menu/tea-for-home.jpg', categoryId: catMap['tea-for-home'],
        isActive: true, tags: '["retail","powder","home"]', stock: 50,
      },
    })
  }
  console.log(`✅ Upserted ${teaForHome.length} Tea for Home items`)

  // ─── Summary ─────────────────────────────────────────────────────────────────
  const totalProducts = await prisma.product.count()
  const totalCultivars = await prisma.teaCultivar.count()
  const totalBranches = await prisma.branch.count()
  const totalOptions = await prisma.menuOption.count()

  console.log('\n🎉 Seed Complete!')
  console.log(`   Products: ${totalProducts}`)
  console.log(`   Tea Cultivars: ${totalCultivars}`)
  console.log(`   Branches: ${totalBranches}`)
  console.log(`   Menu Options: ${totalOptions}`)
}

main()
  .catch(console.error)
  .finally(() => prisma.$disconnect())
