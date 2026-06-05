import puppeteer from 'puppeteer';
import path from 'path';
import { fileURLToPath } from 'url';
import fs from 'fs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlFile = path.resolve(__dirname, '../public/ads/clear-okumidori-instagram.html');
const outDir = path.resolve(__dirname, '../public/ads/exports');

fs.mkdirSync(outDir, { recursive: true });

const browser = await puppeteer.launch({
  headless: true,
  args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu'],
});

const page = await browser.newPage();

// Load the HTML file
await page.goto(`file://${htmlFile}`, { waitUntil: 'networkidle0' });

// Wait for fonts / layout
await new Promise(r => setTimeout(r, 1500));

// ─── Version A — Dark Premium ─────────────────────────────
const cardA = await page.$('#version-a');
await cardA.screenshot({
  path: path.join(outDir, 'clear-okumidori-dark-premium.png'),
  omitBackground: false,
});
console.log('✅ Exported: clear-okumidori-dark-premium.png');

// ─── Version B — Light Minimal ─────────────────────────────
const cardB = await page.$('#version-b');
await cardB.screenshot({
  path: path.join(outDir, 'clear-okumidori-light-minimal.png'),
  omitBackground: false,
});
console.log('✅ Exported: clear-okumidori-light-minimal.png');

await browser.close();
console.log('\nDone! Files saved to:', outDir);
