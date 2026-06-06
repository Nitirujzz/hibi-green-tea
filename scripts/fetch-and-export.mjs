import puppeteer from 'puppeteer';
import path from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.resolve(__dirname, '../public/ads/exports');
fs.mkdirSync(outDir, { recursive: true });

const browser = await puppeteer.launch({
  headless: true,
  args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu', '--ignore-certificate-errors'],
});

// Fetch image via browser (bypasses CDN host restriction)
async function fetchImageAsBase64(url) {
  const page = await browser.newPage();
  await page.setExtraHTTPHeaders({ 'Referer': 'https://higgsfield.ai/' });
  const resp = await page.goto(url, { waitUntil: 'networkidle0', timeout: 30000 });
  const buffer = await resp.buffer();
  await page.close();
  return buffer.toString('base64');
}

const IMG_URL_1 = 'https://d8j0ntlcm91z4.cloudfront.net/user_2z2soR6fvKbksdE2zSx9OqVcnqr/hf_20260605_121242_4cc24f08-3f28-4993-a0d2-b4816376b58f.png';
const IMG_URL_2 = 'https://d8j0ntlcm91z4.cloudfront.net/user_2z2soR6fvKbksdE2zSx9OqVcnqr/hf_20260605_121514_835c4ca4-7b73-4f19-8636-6a1886aa7f10.png';

console.log('Fetching product photos via browser...');
let img1b64 = '', img2b64 = '';

try {
  img1b64 = await fetchImageAsBase64(IMG_URL_1);
  console.log(`✅ Photo 1 fetched (${img1b64.length} chars)`);
} catch (e) {
  console.log('⚠️  Photo 1 failed:', e.message);
}

try {
  img2b64 = await fetchImageAsBase64(IMG_URL_2);
  console.log(`✅ Photo 2 fetched (${img2b64.length} chars)`);
} catch (e) {
  console.log('⚠️  Photo 2 failed:', e.message);
}

// ─── Build full composite HTML ───────────────────────────────────────────────
const compositeHTML = (bgBase64, version) => {
  const hasBg = bgBase64.length > 100;
  const bgStyle = hasBg
    ? `background-image: url('data:image/png;base64,${bgBase64}'); background-size: cover; background-position: center right;`
    : version === 'dark'
      ? 'background: linear-gradient(145deg, #071209 0%, #0d2318 50%, #0a1a0f 100%);'
      : 'background: linear-gradient(160deg, #ffffff 0%, #f0fdf4 50%, #dcfce7 100%);';

  const isDark = version === 'dark';

  return `<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8"/>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,600;0,700;0,900;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&display=swap');
  * { margin:0; padding:0; box-sizing:border-box; }

  .card {
    width: 1080px;
    height: 1080px;
    position: relative;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    ${bgStyle}
  }

  /* Photo overlay: left half opaque-ish, right half bright photo */
  .photo-overlay {
    position: absolute;
    inset: 0;
    background: ${isDark
      ? 'linear-gradient(90deg, rgba(7,18,9,0.92) 0%, rgba(7,18,9,0.75) 45%, rgba(7,18,9,0.1) 70%, transparent 100%)'
      : 'linear-gradient(90deg, rgba(255,255,255,0.97) 0%, rgba(255,255,255,0.88) 42%, rgba(255,255,255,0.3) 65%, transparent 100%)'};
  }

  /* Glow orb */
  .orb {
    position: absolute;
    border-radius: 50%;
    pointer-events: none;
  }
  .orb-1 {
    width: 500px; height: 500px;
    background: radial-gradient(circle, ${isDark ? 'rgba(34,197,94,0.1)' : 'rgba(34,197,94,0.06)'} 0%, transparent 70%);
    top: -100px; left: -100px;
  }
  .orb-2 {
    width: 300px; height: 300px;
    background: radial-gradient(circle, ${isDark ? 'rgba(74,222,128,0.08)' : 'rgba(74,222,128,0.05)'} 0%, transparent 70%);
    bottom: 80px; left: 200px;
  }

  /* Border frame */
  .frame-line {
    position: absolute;
    background: ${isDark ? 'rgba(74,222,128,0.2)' : 'rgba(22,163,74,0.15)'};
  }
  .frame-top { top:48px; left:48px; right:48px; height:1px; }
  .frame-bottom { bottom:48px; left:48px; right:48px; height:1px; }
  .frame-left { top:48px; bottom:48px; left:48px; width:1px; }

  /* Content panel */
  .content {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    padding: 72px 72px 72px 80px;
    width: 600px;
  }

  /* ── Header ── */
  .header { display:flex; justify-content:space-between; align-items:flex-start; }

  .brand { display:flex; flex-direction:column; gap:3px; }
  .brand-name {
    font-size: 11px; font-weight:700; letter-spacing:0.38em; text-transform:uppercase;
    color: ${isDark ? 'rgba(74,222,128,0.95)' : '#16a34a'};
  }
  .brand-jp {
    font-size: 10px; letter-spacing:0.18em;
    color: ${isDark ? 'rgba(255,255,255,0.3)' : 'rgba(22,101,52,0.5)'};
  }

  .grade-badge {
    display:flex; align-items:center; gap:7px;
    border: 1px solid ${isDark ? 'rgba(74,222,128,0.3)' : '#bbf7d0'};
    background: ${isDark ? 'rgba(34,197,94,0.08)' : '#f0fdf4'};
    border-radius:4px; padding:7px 14px;
  }
  .grade-dot { width:5px; height:5px; border-radius:50%; background:#4ade80; flex-shrink:0; }
  .grade-text {
    font-size:9px; font-weight:700; letter-spacing:0.25em; text-transform:uppercase;
    color: ${isDark ? 'rgba(74,222,128,0.85)' : '#16a34a'};
  }

  /* ── Middle: product name area ── */
  .middle { flex:1; display:flex; flex-direction:column; justify-content:center; padding-top:20px; }

  .series-label {
    font-size:10px; font-weight:700; letter-spacing:0.3em; text-transform:uppercase;
    color: ${isDark ? 'rgba(74,222,128,0.6)' : '#16a34a'}; opacity:0.7;
    margin-bottom:12px;
  }

  .title-clear {
    font-family:'Playfair Display', serif;
    font-size:90px; font-weight:700; line-height:0.95;
    color: ${isDark ? '#ffffff' : '#0a2e12'};
    letter-spacing:-0.02em;
  }

  .title-oku {
    font-family:'Playfair Display', serif;
    font-size:58px; font-weight:400; font-style:italic; line-height:1.1;
    color: ${isDark ? 'rgba(255,255,255,0.38)' : 'rgba(10,46,18,0.35)'};
    letter-spacing:-0.01em;
    margin-bottom:24px;
  }

  .key-msg {
    font-size:14px; font-weight:400; line-height:1.7;
    color: ${isDark ? 'rgba(255,255,255,0.55)' : '#4b5563'};
    max-width:460px; margin-bottom:22px;
  }
  .key-msg b { color: ${isDark ? 'rgba(255,255,255,0.9)' : '#0a2e12'}; font-weight:700; }

  .flavor-row { display:flex; gap:7px; flex-wrap:wrap; margin-bottom:8px; }
  .ftag {
    display:flex; align-items:center; gap:5px;
    padding:5px 11px; border-radius:100px;
    border: 1px solid ${isDark ? 'rgba(74,222,128,0.22)' : '#bbf7d0'};
    background: ${isDark ? 'rgba(74,222,128,0.05)' : '#f0fdf4'};
  }
  .ftag-dot { width:4px; height:4px; border-radius:50%; background:#4ade80; }
  .ftag-text {
    font-size:11px; font-weight:500;
    color: ${isDark ? 'rgba(255,255,255,0.6)' : '#166534'};
  }

  /* Origin strip */
  .origin-strip {
    display:flex; align-items:center; gap:16px;
    border-left: 2px solid ${isDark ? 'rgba(74,222,128,0.35)' : '#4ade80'};
    padding-left:14px; margin:20px 0;
  }
  .origin-item { display:flex; flex-direction:column; gap:2px; }
  .origin-label {
    font-size:9px; font-weight:700; letter-spacing:0.22em; text-transform:uppercase;
    color: ${isDark ? 'rgba(74,222,128,0.6)' : '#16a34a'};
  }
  .origin-value {
    font-size:14px; font-weight:600;
    color: ${isDark ? 'rgba(255,255,255,0.85)' : '#111827'};
  }
  .origin-sep { width:1px; height:32px; background:${isDark ? 'rgba(255,255,255,0.1)' : 'rgba(22,163,74,0.2)'}; }

  /* ── Bottom ── */
  .bottom { display:flex; justify-content:space-between; align-items:flex-end; }

  .price-block {}
  .price-label {
    font-size:10px; font-weight:700; letter-spacing:0.22em; text-transform:uppercase;
    color: ${isDark ? 'rgba(74,222,128,0.65)' : '#16a34a'}; margin-bottom:4px;
  }
  .price-main {
    font-size:72px; font-weight:900; line-height:1;
    color: ${isDark ? '#ffffff' : '#0a2e12'}; letter-spacing:-0.03em;
  }
  .price-currency { font-size:32px; font-weight:300; opacity:0.6; }
  .price-sub {
    font-size:11px; color:${isDark ? 'rgba(255,255,255,0.3)' : '#9ca3af'};
    margin-top:5px;
  }
  .price-sub b { color:${isDark ? 'rgba(255,255,255,0.55)' : '#6b7280'}; }

  .cta-col { display:flex; flex-direction:column; align-items:flex-end; gap:10px; }

  .cta-btn {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color:#fff; font-size:12px; font-weight:700;
    letter-spacing:0.18em; text-transform:uppercase;
    padding:15px 30px; border-radius:4px;
    box-shadow: 0 6px 24px rgba(34,197,94,0.35);
    display:inline-block; text-decoration:none;
  }
  .cta-social { display:flex; gap:6px; }
  .cta-hash {
    font-size:10px; font-weight:600;
    color: ${isDark ? 'rgba(74,222,128,0.55)' : '#16a34a'}; opacity:0.75;
  }
</style>
</head>
<body style="margin:0;padding:0">
<div class="card">
  <div class="photo-overlay"></div>
  <div class="orb orb-1"></div>
  <div class="orb orb-2"></div>
  <div class="frame-line frame-top"></div>
  <div class="frame-line frame-bottom"></div>
  <div class="frame-line frame-left"></div>

  <div class="content">
    <!-- HEADER -->
    <div class="header">
      <div class="brand">
        <div class="brand-name">Hibi Matcha</div>
        <div class="brand-jp">日々 抹茶 · Since 2024</div>
      </div>
      <div class="grade-badge">
        <div class="grade-dot"></div>
        <div class="grade-text">Ceremonial Grade</div>
      </div>
    </div>

    <!-- MIDDLE -->
    <div class="middle">
      <div class="series-label">Clear Series · Signature Menu</div>
      <div class="title-clear">Clear</div>
      <div class="title-oku">Okumidori</div>

      <div class="key-msg">
        ความบริสุทธิ์ที่ดื่มได้ — มัทฉะ <b>Ceremonial Grade</b><br>
        สายพันธุ์ <b>Okumidori</b> จากไร่ชาใน <b>Uji, Kyoto</b><br>
        กลิ่นสาหร่ายหอม อูมามิเนียบลึก สดชื่นทุกแก้ว
      </div>

      <div class="flavor-row">
        <div class="ftag"><div class="ftag-dot"></div><div class="ftag-text">หอมสาหร่าย</div></div>
        <div class="ftag"><div class="ftag-dot"></div><div class="ftag-text">อูมามิลึก</div></div>
        <div class="ftag"><div class="ftag-dot"></div><div class="ftag-text">สดชื่นแบบคลีน</div></div>
        <div class="ftag"><div class="ftag-dot"></div><div class="ftag-text">ไม่ขม</div></div>
      </div>

      <div class="origin-strip">
        <div class="origin-item">
          <div class="origin-label">Origin</div>
          <div class="origin-value">Uji, Kyoto 🇯🇵</div>
        </div>
        <div class="origin-sep"></div>
        <div class="origin-item">
          <div class="origin-label">Cultivar</div>
          <div class="origin-value">Okumidori 奥みどり</div>
        </div>
        <div class="origin-sep"></div>
        <div class="origin-item">
          <div class="origin-label">Grade</div>
          <div class="origin-value">Ceremonial ⭐⭐⭐</div>
        </div>
      </div>
    </div>

    <!-- BOTTOM -->
    <div class="bottom">
      <div class="price-block">
        <div class="price-label">ราคา Dine-in</div>
        <div class="price-main"><span class="price-currency">฿</span>235</div>
        <div class="price-sub">Delivery <b>฿255</b> · GrabFood · LINE MAN · Wongnai</div>
      </div>
      <div class="cta-col">
        <a class="cta-btn" href="#">สั่งเลยตอนนี้</a>
        <div class="cta-social">
          <span class="cta-hash">#HibiMatcha</span>
          <span class="cta-hash">#มัทฉะไทย</span>
          <span class="cta-hash">#ชาญี่ปุ่น</span>
        </div>
      </div>
    </div>
  </div>
</div>
</body>
</html>`;
};

// Write HTML files
const htmlDark = compositeHTML(img1b64, 'dark');
const htmlLight = compositeHTML(img2b64, 'light');

const tmpDark = '/tmp/ad-dark.html';
const tmpLight = '/tmp/ad-light.html';
fs.writeFileSync(tmpDark, htmlDark);
fs.writeFileSync(tmpLight, htmlLight);

// Screenshot
const page = await browser.newPage();
await page.setViewport({ width: 1080, height: 1080, deviceScaleFactor: 2 });

await page.goto(`file://${tmpDark}`, { waitUntil: 'networkidle0' });
await new Promise(r => setTimeout(r, 2000));
await page.screenshot({
  path: path.join(outDir, 'v2-dark-premium.png'),
  clip: { x: 0, y: 0, width: 1080, height: 1080 }
});
console.log('✅ Exported: v2-dark-premium.png');

await page.goto(`file://${tmpLight}`, { waitUntil: 'networkidle0' });
await new Promise(r => setTimeout(r, 2000));
await page.screenshot({
  path: path.join(outDir, 'v2-light-minimal.png'),
  clip: { x: 0, y: 0, width: 1080, height: 1080 }
});
console.log('✅ Exported: v2-light-minimal.png');

await browser.close();
console.log('\nAll done! Files:', outDir);
