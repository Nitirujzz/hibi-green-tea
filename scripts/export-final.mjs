import puppeteer from 'puppeteer';
import path from 'path';
import fs from 'fs';

const outDir = '/home/user/hibi-green-tea/public/ads/exports';
fs.mkdirSync(outDir, { recursive: true });

const browser = await puppeteer.launch({
  headless: true,
  args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu', '--font-render-hinting=none'],
});

const page = await browser.newPage();

// 2x device pixel ratio = crisp 1080x1080 from a 540x540 viewport
await page.setViewport({ width: 1080, height: 1080, deviceScaleFactor: 1 });

await page.goto('file:///tmp/ad-final.html', { waitUntil: 'networkidle0' });
await new Promise(r => setTimeout(r, 2500)); // wait for fonts + rendering

const el = await page.$('.ad');
await el.screenshot({
  path: path.join(outDir, 'v4-final-dark.png'),
  omitBackground: false,
});
console.log('✅ v4-final-dark.png');

await browser.close();
console.log('Done →', outDir);
