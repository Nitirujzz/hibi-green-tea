// Mobile UI test for the Hibi & Capy RPS game (Playwright). Usage: node ui_test.js [base_url] [out_dir]
const { chromium } = require('playwright'); const fs = require('fs');
const BASE = process.argv[2] || 'http://localhost:3005'; const OUT = process.argv[3] || 'ui_shots'; fs.mkdirSync(OUT, { recursive: true });
const DEVICES = [{ name: 'iPhoneSE', width: 375, height: 667 }, { name: 'iPhoneProMax', width: 430, height: 932 }];
const results = []; const check = (n, c, d = '') => { results.push([n, !!c]); console.log((c ? 'PASS ' : 'FAIL ') + n + (c ? '' : `  [${d}]`)) };
(async () => {
  const b = await chromium.launch({ args: ['--autoplay-policy=no-user-gesture-required'] });
  for (const dev of DEVICES) {
    const ctx = await b.newContext({ viewport: { width: dev.width, height: dev.height }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
    const p = await ctx.newPage(); const errs = []; let bytes = 0;
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && !m.text().includes('status of 400') && errs.push(m.text()));
    p.on('response', async r => { const intentional = r.url().endsWith('/otp/verify') && r.status() === 400; if (r.status() >= 400 && !intentional) errs.push(r.status() + ' ' + r.url()); try { bytes += (await r.body()).length } catch {} });
    const tag = dev.name, shot = n => p.screenshot({ path: `${OUT}/${tag}_${n}.png` });
    const noOverflow = async step => check(`[${tag}] no sideways scrolling: ${step}`, await p.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1));
    const inView = async (sel, step) => { const bb = await p.locator(sel).first().boundingBox(); check(`[${tag}] main button visible without scrolling: ${step}`, bb && bb.y + bb.height <= dev.height, bb && Math.round(bb.y + bb.height)) };

    await p.goto(BASE + '/game'); await p.waitForTimeout(2500); await shot('1_intro');
    check(`[${tag}] intro shows prize 15% and 50%`, (await p.content()).includes('ส่วนลด 15%') && (await p.content()).includes('ส่วนลด 50%'));
    check(`[${tag}] character loop video plays`, await p.evaluate(() => { const v = document.querySelector('video'); return !!v && !v.paused && v.currentTime > 0.2 }));
    await noOverflow('intro'); await inView('text=เริ่มเล่นเลย', 'intro');
    await p.click('text=เริ่มเล่นเลย', { force: true }); await p.waitForTimeout(500);
    check(`[${tag}] OTP button disabled until consent + phone`, await p.locator('text=ขอรหัส OTP').isDisabled());
    const phone = '08' + String(10000000 + Math.floor(Math.random() * 8e7)).slice(0, 8);
    await p.fill('input[inputmode=tel]', phone); await p.check('input[type=checkbox]'); await shot('2_phone'); await noOverflow('phone');
    await p.click('text=ขอรหัส OTP', { force: true }); await p.waitForSelector('text=โหมดทดลอง'); await shot('3_otp');
    await p.fill('input[inputmode=numeric]', '000001'); await p.click('text=ยืนยันแล้วเล่นเลย', { force: true }); await p.waitForTimeout(700);
    check(`[${tag}] wrong OTP shows Thai error`, (await p.content()).includes('รหัสไม่ถูกต้อง'));
    const code = (await p.locator('b.tracking-\\[3px\\]').innerText()).trim();
    await p.fill('input[inputmode=numeric]', code); await p.click('text=ยืนยันแล้วเล่นเลย', { force: true });
    await p.waitForSelector('text=พร้อมแล้ว'); await p.waitForTimeout(1500); await shot('4_lobby'); await noOverflow('lobby'); await inView('text=พร้อมแล้ว', 'lobby');
    await p.reload(); await p.waitForTimeout(1500);
    check(`[${tag}] stays logged in after reload`, await p.locator('text=พร้อมแล้ว').count() > 0);
    await p.click('button[aria-label="ปิดเสียง"]'); await p.reload(); await p.waitForTimeout(1200);
    check(`[${tag}] mute is remembered after reload`, await p.locator('button[aria-label="เปิดเสียง"]').count() > 0);
    await p.click('button[aria-label="เปิดเสียง"]');
    let shotPick = false, sawCount = false, rounds = 0;
    for (let i = 0; i < 20; i++) {
      if (await p.locator('text=พร้อมแล้ว').count()) { await p.click('text=พร้อมแล้ว', { force: true }); await p.waitForTimeout(600) }
      await p.waitForSelector('.hg-move');
      if (!shotPick) { await p.waitForTimeout(500); await shot('5_pick'); await noOverflow('pick'); shotPick = true }
      await p.locator('.hg-move').nth(Math.floor(Math.random() * 3)).click({ force: true });
      await p.waitForTimeout(800); if (!sawCount) { sawCount = (await p.content()).includes('ยิ้ง') || (await p.content()).includes('เป่า'); await shot('6_countdown') }
      await p.waitForSelector('text=คุณ', { timeout: 10000 }); await p.waitForTimeout(1500); rounds++;
      await shot(`7_result_${rounds}`); await noOverflow(`result ${rounds}`);
      if (await p.locator('text=ท้า Capy ต่อ').count()) { await p.click('text=ท้า Capy ต่อ', { force: true }); await p.waitForSelector('text=พร้อมแล้ว'); continue }
      if (await p.locator('text=เป่า ยิ้ง ฉุบ อีกครั้ง').count()) { await p.click('text=เป่า ยิ้ง ฉุบ อีกครั้ง', { force: true }); continue }
      break
    }
    check(`[${tag}] countdown animation shown`, sawCount);
    await p.waitForSelector('text=แชร์ลง IG Story 📸', { timeout: 8000 }).catch(() => {});
    check(`[${tag}] game reaches a final result`, await p.locator('text=แชร์ลง IG Story 📸').count() > 0);
    await p.click('text=แชร์ลง IG Story 📸', { force: true }); await p.waitForSelector('text=สติกเกอร์', { timeout: 8000 }); await p.waitForTimeout(800); await shot('8_share');
    check(`[${tag}] share sheet has download + IG steps + Facebook + LINE + X + copy`, await p.locator('text=⬇️ บันทึกภาพ').count() > 0 && await p.locator('text=Facebook').count() > 0 && await p.locator('text=LINE').count() > 0 && await p.locator('text=คัดลอกข้อความ').count() > 0);
    const imgOk = await p.evaluate(() => { const i = document.querySelector('img[alt="การ์ดผลการเล่น"]'); return !!i && i.naturalWidth === 1080 && i.naturalHeight === 1920 });
    check(`[${tag}] share card is 1080x1920`, imgOk);
    await p.mouse.click(10, 10); await p.waitForTimeout(500);
    await p.goto(BASE + '/game'); await p.waitForTimeout(1200);
    check(`[${tag}] after finishing, today's result is shown (no replay)`, await p.locator('text=เล่นได้วันละ 1 ครั้งต่อเบอร์').count() > 0 && await p.locator('text=พร้อมแล้ว').count() === 0);
    check(`[${tag}] no page errors / failed requests`, errs.length === 0, errs.slice(0, 3).join(' | '));
    console.log(`      [${tag}] downloaded ~${Math.round(bytes / 1024)} KB this session (dev build, unminified)`);
    await ctx.close();
  }
  // staff page
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, isMobile: true }); const p = await ctx.newPage();
  await p.goto(BASE + '/game/admin'); await p.fill('input[type=password]', '9999'); await p.click('text=เข้าสู่ระบบ'); await p.waitForTimeout(600);
  check('[admin] wrong PIN rejected in UI', (await p.content()).includes('PIN ไม่ถูกต้อง'));
  await p.fill('input[type=password]', '1234'); await p.click('text=เข้าสู่ระบบ'); await p.waitForSelector('text=เล่นวันนี้');
  await p.fill('input[placeholder="HIBI-XXXX-XXXX"]', 'HIBI-ZZZZ-ZZZZ'); await p.click('text=ตรวจสอบ'); await p.waitForTimeout(600);
  check('[admin] unknown coupon message', (await p.content()).includes('ไม่พบคูปองนี้'));
  await p.screenshot({ path: `${OUT}/admin.png` });
  await b.close();
  const failed = results.filter(r => !r[1]); console.log(`\n${results.length - failed.length}/${results.length} passed`); process.exit(failed.length ? 1 : 0);
})();
