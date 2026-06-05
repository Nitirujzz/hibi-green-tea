import puppeteer from 'puppeteer';
import path from 'path';
import fs from 'fs';

const outDir = '/home/user/hibi-green-tea/public/ads/exports';
fs.mkdirSync(outDir, { recursive: true });

const browser = await puppeteer.launch({
  headless: true,
  args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu', '--font-render-hinting=none', '--ignore-certificate-errors'],
});

const page = await browser.newPage();
page.on('console', m => console.log('[browser]', m.type(), m.text()));
page.on('pageerror', e => console.error('[page-error]', e.message));
await page.setViewport({ width: 1080, height: 1920, deviceScaleFactor: 1 });

const htmlPath = path.resolve('/home/user/hibi-green-tea/public/ads/clear-okumidori-reels/index.html');
await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle0' });
await new Promise(r => setTimeout(r, 3500));

// Check timeline state
const tlState = await page.evaluate(() => {
  return {
    hasTimelines: !!window.__timelines,
    rootKey: window.__timelines ? Object.keys(window.__timelines) : [],
    gsapLoaded: typeof gsap !== 'undefined',
  };
});
console.log('Timeline state:', JSON.stringify(tlState));

const seekAndShot = async (t, name) => {
  await page.evaluate((time) => {
    const tl = window.__timelines && window.__timelines['root'];
    if (tl) tl.seek(time);
  }, t);
  await new Promise(r => setTimeout(r, 350));
  await page.screenshot({ path: path.join(outDir, name) });
  console.log('✅', name);
};

await seekAndShot(0.8, 'reels-s1-brand.png');
await seekAndShot(3.5, 'reels-s2-hero.png');
await seekAndShot(8.0, 'reels-s3-info.png');
await seekAndShot(11.4, 'reels-s4-price.png');
await seekAndShot(13.8, 'reels-s5-cta.png');

await browser.close();
console.log('Done →', outDir);
