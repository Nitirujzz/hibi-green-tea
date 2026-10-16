// Hibi Brand Story: pure function of time. window.seek(t) paints frame t (see lib/motion.js).
// Timing is in beats (u) on the measured grid (90 bpm, 1 beat = 0.667 s); docs/shotlist.md is the plan.
import * as M from './lib/motion.js';
import { C, hibi, capy, glass, chawan, whisk, leaf, tag } from './lib/chars.js';

const { W, H, E, prog, lerp, clamp, springU, springKeys, SPRING, wobble, ring, font, fill, rrect, shake, mix, hash01, fitSize } = M;

const DISPLAY = 'Display', UI = 'UI', MARK = 'Mark';
const CX = 510;                       // centre of the 9x16 safe area (72 left, 150 right)
const SAFE_TOP = 250, SAFE_BOT = 1490;
const HEAVY = { stiffness: 200, damping: 16 };
const WHIP = { stiffness: 190, damping: 24 };

// ---------------------------------------------------------------- hits: [beat, label, sfx, opts]
const HOPS = [10.5, 11, 11.5, 12, 12.5, 13];
const HOP_NOTES = ['G5', 'A5', 'C6', 'D6', 'F6', 'G6'];
const TILE_FLIPS = [42, 42.5, 43, 43.5, 44.5, 45, 45.5];
const HITS = [
  [0, '日 stamps', 'impact'],
  [1, '々 stamps', 'thud', { pitch: 170, to: 60 }],
  [1.5, 'Hibi reading', 'tick'],
  [2.5, 'Hibi lands on 々', 'boing', { pitch: 260, to: 620 }],
  [4, 'kanji rise', 'whoosh', { len: 0.4, from: 500, to: 2200 }],
  [4.25, '日 = วัน', 'tick'],
  [5.5, '々 = ซ้ำอีกครั้ง', 'tick'],
  [7, 'ทุกๆ วัน', 'pop', { pitch: 'F5' }],
  [7.4, 'underline', 'bell', { pitch: 'C6', gain: 0.2 }],
  [9.7, 'cream wipe', 'whoosh', { len: 0.45 }],
  ...HOPS.map((b, i) => [b, `hop ${i + 1}`, 'tok', { pitch: HOP_NOTES[i], gain: 0.22 }]),
  [14, 'price tag drops', 'thud'],
  [14.2, 'Capy slides in', 'whoosh', { len: 0.3, from: 1800, to: 500, pan: 0.4 }],
  [14.5, 'doubt line 2', 'tick'],
  [15.75, 'whisk wipe', 'whoosh', { len: 0.5, from: 2600, to: 700 }],
  [16, 'DROP: ของดี', 'impact'],
  [17, 'ที่มีคุณภาพ', 'pop', { pitch: 'A5' }],
  [18, 'ไม่จำเป็น', 'pop', { pitch: 'C6' }],
  [19.5, 'ต้องแพง', 'thud', { pitch: 140, to: 45 }],
  [20.5, 'belief pill', 'blip', { pitch: 'F6' }],
  [21.75, 'push to study', 'whoosh', { len: 0.4 }],
  [22.55, 'card 1', 'whoosh', { len: 0.35, from: 900, to: 2600 }],
  [25.65, 'card 2', 'whoosh', { len: 0.35, from: 900, to: 2600 }],
  [28.65, 'card 3', 'whoosh', { len: 0.35, from: 900, to: 2600 }],
  [32, 'into the bowl', 'riser', { len: 0.9 }],
  [32, 'bowl close-up', 'sub', { len: 0.5 }],
  ...[32.5, 33, 33.5, 34, 34.5, 35].map((b) => [b, 'whisk stroke', 'whoosh', { len: 0.14, from: 3000, to: 5200, gain: 0.1 }]),
  [32.5, 'care line', 'tick'],
  [36.25, 'pour', 'whoosh', { len: 1.1, from: 400, to: 900, gain: 0.18 }],
  [36.5, 'line: เพื่อมอบสิ่งดีๆ', 'tick'],
  [38, 'straw drops in', 'pop', { pitch: 'G5' }],
  [39.75, 'push to together', 'whoosh', { len: 0.4 }],
  [40, 'Hibi + Capy in', 'boing', { pitch: 240, to: 560 }],
  [40.75, 'มัทฉะคุณภาพ', 'pop', { pitch: 'A5' }],
  [41.5, 'ในราคาที่จับต้องได้', 'pop', { pitch: 'C6' }],
  ...TILE_FLIPS.map((b) => [b, 'day lights up', 'tick', { pitch: 3200 }]),
  [44, 'clink', 'bell', { pitch: 'E6' }],
  [48, 'end card swell', 'swell', { len: 0.7 }],
  [48, 'logo stamps', 'impact'],
  [48.4, 'wordmark', 'pop', { pitch: 'F5' }],
  [49, 'tagline', 'bell', { pitch: 'C6' }],
  ...[50, 50.5, 51, 51.5, 52].map((b, i) => [b, `branch ${i + 1}`, 'blip', { pitch: ['F5', 'G5', 'A5', 'C6', 'D6'][i] }]),
  [52.5, 'hold', 'bell', { pitch: 'F6', gain: 0.15 }],
];

// ---------------------------------------------------------------- helpers
const blink = (u, seed) => ((u * 0.66 + hash01(seed) * 7) % 5.1) < 0.14;
const eyesOr = (u, seed, mode = 'open') => (blink(u, seed) ? 'blink' : mode);

// One line of type that rises piece by piece out of a mask under its baseline.
// pieces: strings or { t, fam, weight, color }. Returns the line geometry for underlines.
function rise(ctx, u, u0, pieces, x, y, size, o = {}) {
  const { weight = 700, fam = DISPLAY, color = C.green, stagger = 0.12, align = 'center', cfg = SPRING.bouncy, exit = 0, squash = null } = o;
  const items = pieces.map((p) => (typeof p === 'string' ? { t: p } : p));
  const fonts = items.map((p) => font(size, p.weight ?? weight, p.fam ?? fam));
  const widths = items.map((p, i) => { ctx.font = fonts[i]; return ctx.measureText(p.t).width; });
  const total = widths.reduce((a, b) => a + b, 0);
  let px = align === 'center' ? x - total / 2 : x;
  const left = px;
  ctx.save();
  ctx.beginPath(); ctx.rect(0, y - size * 1.35, W, size * 1.9); ctx.clip();
  items.forEach((p, i) => {
    const k = springU(u, u0 + i * stagger, cfg);
    if (k > 0) {
      const dy = (1 - k) * size * 1.5 - exit * size * 1.9;
      ctx.save();
      ctx.translate(px + widths[i] / 2, y + dy);
      if (squash) { const q = squash(i); ctx.scale(1 + q, 1 - q); }
      ctx.font = fonts[i]; ctx.fillStyle = p.color ?? color; ctx.textAlign = 'center';
      ctx.fillText(p.t, 0, 0);
      ctx.restore();
    }
    px += widths[i];
  });
  ctx.restore();
  return { left, width: total, y, size };
}
function underline(ctx, g, p, color, off = 0.24, wt = 0.075) {
  if (p <= 0) return;
  ctx.beginPath();
  ctx.moveTo(g.left, g.y + g.size * off); ctx.lineTo(g.left + g.width * p, g.y + g.size * off);
  ctx.lineCap = 'round'; ctx.lineWidth = g.size * wt; ctx.strokeStyle = color; ctx.stroke();
}
function kanji(ctx, ch, x, y, size, color, s = 1, rot = 0) {
  ctx.save();
  ctx.translate(x, y - size * 0.38); ctx.rotate(rot); ctx.scale(s, s); ctx.translate(0, size * 0.38);
  ctx.font = font(size, 800, MARK); ctx.fillStyle = color; ctx.textAlign = 'center'; ctx.fillText(ch, 0, 0);
  ctx.restore();
}
function hopArc(u, u0, u1, a, b, h) {
  const p = E.inOutCubic(prog(u, u0, u1));
  return [lerp(a[0], b[0], p), lerp(a[1], b[1], p) - Math.sin(Math.PI * p) * h];
}
// the AI disclosure, always on (bigger on the end card)
function aiLabel(ctx, dark) {
  ctx.save();
  ctx.font = font(34, 500, UI); ctx.textAlign = 'left';
  ctx.fillStyle = dark ? 'rgba(245,240,228,0.82)' : 'rgba(31,61,36,0.78)';
  ctx.fillText('ภาพประกอบสร้างด้วย AI', 72, 300);
  ctx.restore();
}

// ---------------------------------------------------------------- S1 + S2: 日々 and its meaning (u 0..10)
const K = 380;
function sceneKanji(ctx, u) {
  fill(ctx, C.green);
  // group transform: big stamp centred low, then rises and shrinks into the header (log zoom)
  const p = E.inOutCubic(prog(u, 4, 5));
  const gs = 1 * (0.5 / 1) ** p;
  const gy = lerp(1080, 540, p);
  ctx.save();
  shake(ctx, u, 0, 18); shake(ctx, u, 1, 12, 7);
  const k1 = springU(u, -0.12, SPRING.bouncy), k2 = springU(u, 0.88, SPRING.bouncy);
  const x1 = CX - 190 * gs, x2 = CX + 190 * gs;
  if (k1 > 0) kanji(ctx, '日', x1, gy, K * gs, C.cream, lerp(1.5, 1, k1), lerp(-0.12, 0, k1));
  if (k2 > 0) kanji(ctx, '々', x2, gy, K * gs, C.cream, lerp(1.5, 1, k2), lerp(0.12, 0, k2));
  // reading under the kanji
  const rk = springU(u, 1.4, SPRING.snappy);
  if (rk > 0) {
    ctx.save(); ctx.font = font(lerp(84, 60, p), 600, DISPLAY); ctx.textAlign = 'center'; ctx.fillStyle = C.matcha;
    ctx.globalAlpha = clamp(rk * 1.5);
    ctx.fillText('Hibi', CX, gy + lerp(130, 80, p) + (1 - rk) * 40);
    ctx.restore();
  }
  ctx.restore();

  // Hibi drops onto the top of 々, then hops down to the bottom right
  const top = [CX + 190, 1080 - K * 0.84];
  if (u >= 2.1) {
    let pos, sc = lerp(0.9, 0.85, p), pose = { eyes: eyesOr(u, 1), mouth: 'w' };
    if (u < 4) {
      const k = springU(u, 2.1, HEAVY);
      pos = [top[0], lerp(-200, top[1], Math.min(1, k))];
      pose.squash = 0.18 * wobble(u - 2.5, 2.4, 4) * (u > 2.5 ? 1 : 0);
      pose.ear = [-0.4 * ring(u - 2.5, 1.8, 2.5), 0.4 * ring(u - 2.5, 1.8, 2.5)];
      if (u > 2.6) { pose.eyes = eyesOr(u, 1, 'happy'); pose.wave = [0, -2.4 * clamp((u - 2.8) * 3) * (u < 3.8 ? 1 : 0)]; }
    } else {
      pos = hopArc(u, 4, 5, top, [840, 1480], 260);
      pose.squash = 0.15 * wobble(u - 5, 2.4, 4) * (u > 5 ? 1 : 0);
      // nods on each new line
      pose.lean = 0.12 * (ring(u - 4.25, 1.2, 3) + ring(u - 5.5, 1.2, 3) + ring(u - 7, 1.2, 3));
      pose.look = [-0.8, -0.6];
      if (u > 7) { pose.eyes = 'happy'; pose.mouth = 'smile'; }
    }
    hibi(ctx, pos[0], pos[1], sc, pose);
  }

  // meaning lines
  if (u >= 4) {
    const L1 = rise(ctx, u, 4.1, [{ t: '日', fam: MARK, weight: 800 }, ' = วัน'], CX, 780, 84, { color: C.cream, stagger: 0.15 });
    const L2 = rise(ctx, u, 5.35, [{ t: '々', fam: MARK, weight: 800 }, ' = ซ้ำอีกครั้ง'], CX, 900, 84, { color: C.cream, stagger: 0.15 });
    rise(ctx, u, 6.75, [{ t: '日々', fam: MARK, weight: 800 }, ' แปลว่า'], CX, 1045, 64, { color: C.cream, weight: 500, stagger: 0.1 });
    const g = rise(ctx, u, 6.9, ['ทุกๆ ', 'วัน'], CX, 1225, 170, { color: C.matcha, stagger: 0.12 });
    underline(ctx, g, E.outCubic(prog(u, 7.3, 8.1)), C.cream, 0.24, 0.055);
  }
}

// ---------------------------------------------------------------- S3 + S4: every day, then the doubt (u 10..16)
const DAYS = ['จ', 'อ', 'พ', 'พฤ', 'ศ', 'ส', 'อา'];
const TW = 196, TH = 220, TGAP = 236, TY = 980;          // tile row (world coords)
const tileX = (i) => 200 + i * TGAP;
function tileDraw(ctx, x, y, w, h, label, on, size = 70) {
  rrect(ctx, x - w / 2 + 10, y + 12, w, h, 30); ctx.fillStyle = C.green; ctx.fill();   // block shadow
  rrect(ctx, x - w / 2, y, w, h, 30);
  ctx.fillStyle = on ? C.matcha : '#FFFDF7'; ctx.fill();
  ctx.lineWidth = 7; ctx.strokeStyle = C.green; ctx.stroke();
  ctx.font = font(size, 600, DISPLAY); ctx.fillStyle = C.green; ctx.textAlign = 'center';
  ctx.fillText(label, x, y + h * 0.62);
}
function hibiHopX(u) {
  const t = clamp((u - 10) / 0.5, 0, 6);
  const i = Math.min(5, Math.floor(t)), f = t - i;
  const p = E.inOutCubic(f);
  return { x: lerp(tileX(i), tileX(i + 1), t >= 6 ? 1 : p), y: TY - (t >= 6 ? 0 : Math.sin(Math.PI * f) * 150), i: t >= 6 ? 6 : i, f: t >= 6 ? 1 : f };
}
function sceneDays(ctx, u) {
  fill(ctx, C.cream);
  const lift = -1100 * springU(u, 13.55, SPRING.snappy);     // the row slides up out of frame for the doubt
  // header
  ctx.save(); ctx.translate(0, lift);
  const g = rise(ctx, u, 9.75, ['ทุกๆ ', 'วัน'], CX, 520, 120, { color: C.green, stagger: 0.1 });
  underline(ctx, g, E.outCubic(prog(u, 10, 10.6)), C.matcha, 0.26, 0.07);
  // camera follows Hibi along the row
  const hp = hibiHopX(u);
  const camX = clamp(hp.x - 420, 0, tileX(6) + TW / 2 - 900);
  ctx.translate(-camX, 0);
  DAYS.forEach((d, i) => {
    const drop = springU(u, 9.45 + i * 0.06, SPRING.bouncy);
    const y = lerp(-400, TY, drop);
    // landing dip on the tile Hibi lands on
    const land = 10 + i * 0.5;
    const dip = i > 0 ? 14 * wobble(u - land, 2.2, 5) * (u > land ? 1 : 0) : 0;
    tileDraw(ctx, tileX(i), y + dip, TW, TH, d, false);
  });
  // a glass pops onto every tile Hibi has left
  DAYS.forEach((d, i) => {
    const t0 = 10.25 + i * 0.5;
    const k = springU(u, t0, SPRING.bouncy);
    if (k > 0 && i < 6) glass(ctx, tileX(i), TY - 6, 0.85 * k, { rot: 0.06 * ring(u - t0, 2, 3) });
    if (i === 6 && u > 13.3) { const k6 = springU(u, 13.3, SPRING.bouncy); glass(ctx, tileX(6) + 62, TY - 6, 0.7 * k6); }
  });
  // Hibi
  const sq = HOPS.reduce((a, b) => a + (u > b ? 0.16 * wobble(u - b, 2.6, 5) : 0), 0);
  const inAir = hp.f > 0.05 && hp.f < 0.95 && u < 13;
  hibi(ctx, hp.x - (hp.i === 6 ? 40 : 0), hp.y, 0.8, {
    squash: inAir ? -0.08 : sq, eyes: inAir ? 'happy' : eyesOr(u, 2), mouth: inAir ? 'o' : 'w',
    ear: inAir ? [0.35, -0.35] : [0, 0], wave: inAir ? [-1.6, -1.6] : [0, 0], lean: inAir ? 0.1 : 0,
  });
  ctx.restore();

  // S4: the doubt
  if (u >= 13.5) {
    const k = springU(u, 13.55, HEAVY);
    const hy = lerp(-420, 560, Math.min(1.05, k));
    const sw = 0.32 * ring(u - 14.1, 0.9, 1.1) + 0.05;
    ctx.save(); ctx.beginPath(); ctx.moveTo(330, 0); ctx.lineTo(330 + Math.sin(sw) * 0, hy); ctx.lineWidth = 4; ctx.strokeStyle = C.green; ctx.stroke(); ctx.restore();
    priceTag(ctx, 330, hy, 1.3, sw);
    rise(ctx, u, 13.95, ['มัทฉะ', 'ดีๆ'], CX, 1010, 104, { color: C.green, stagger: 0.12 });
    rise(ctx, u, 14.45, ['ต้อง', 'แพง', 'เสมอ', '…?'], CX, 1140, 104, { color: C.green, stagger: 0.1, weight: 600 });
    // Hibi peeks from the left, Capy slides in from the right
    const hk = springU(u, 13.7, SPRING.bouncy);
    hibi(ctx, lerp(-200, 210, hk), 1480, 0.88, { eyes: 'wide', mouth: 'o', look: [0.6, -1], ear: [0.4, -0.1], lean: -0.1 });
    const ck = springU(u, 13.95, SPRING.gentle);
    const shakeL = u > 15 ? 0.13 * Math.sin((u - 15) * Math.PI * 4) * Math.exp(-(u - 15) * 1.2) : 0;
    capy(ctx, lerp(1350, 770, ck), 1480, 1.05, { flip: true, lean: lerp(-0.25, 0, ck) + shakeL, eyes: u > 15 ? 'blink' : 'open', look: [-0.8, -1], mouth: u > 15 ? 'smile' : 'o' });
  }
}
function priceTag(ctx, x, y, s, rot) {
  tag(ctx, x, y, s, rot, C.gold, (k) => {
    k.font = font(84, 700, DISPLAY); k.fillStyle = C.green; k.textAlign = 'center'; k.fillText('฿฿฿', 0, 160);
  });
}

// ---------------------------------------------------------------- S5: the belief (u 16..22)
function sceneBelief(ctx, u, exit = 0) {
  fill(ctx, C.matcha);
  shake(ctx, u, 16, 16); shake(ctx, u, 19.5, 20, 5);
  // the price tag, string cut, falls through the frame
  if (u < 16.6) {
    const p = prog(u, 15.5, 16.4);
    priceTag(ctx, 330 - p * 300, 560 + 1700 * p * p, 1.3, 0.05 - p * 1.6);
  }
  const sz1 = Math.min(170, fitSize(ctx, 'ของดี', 700, DISPLAY, 820));
  rise(ctx, u, 15.6, ['ของ', 'ดี'], CX, 640, sz1, { stagger: 0.1 });
  rise(ctx, u, 16.85, ['ที่', 'มี', 'คุณภาพ'], CX, 805, 124, { stagger: 0.08, weight: 600 });
  const g = rise(ctx, u, 17.85, ['ไม่', 'จำเป็น'], CX, 1020, 170, { stagger: 0.1 });
  underline(ctx, g, E.outCubic(prog(u, 18.3, 19)), C.cream, 0.24, 0.06);
  const sz4 = Math.min(210, fitSize(ctx, 'ต้องแพง', 700, DISPLAY, 820));
  rise(ctx, u, 19.32, ['ต้อง', 'แพง'], CX, 1250, sz4, { stagger: 0.08, cfg: HEAVY, squash: (i) => 0.14 * wobble(u - 19.6 - i * 0.08, 2.4, 4) * (u > 19.6 ? 1 : 0) });
  // pill: we believe this
  const pk = springU(u, 20.4, SPRING.bouncy);
  if (pk > 0) {
    ctx.save(); ctx.translate(CX, 1400); ctx.scale(pk, pk);
    ctx.font = font(50, 500, UI); const w = ctx.measureText('เราเชื่อแบบนี้').width + 70;
    rrect(ctx, -w / 2, -48, w, 92, 46); ctx.fillStyle = C.green; ctx.fill();
    ctx.fillStyle = C.cream; ctx.textAlign = 'center'; ctx.fillText('เราเชื่อแบบนี้', 0, 16);
    ctx.restore();
  }
}

// whisk wipe from S4 into S5 (u 15.5..16)
function whiskWipe(ctx, u) {
  const p = E.inOutCubic(prog(u, 15.45, 16.0));
  const edge = lerp(W + 160, -260, p);
  ctx.save();
  ctx.beginPath(); ctx.moveTo(edge, 0);
  for (let y = 0; y <= H; y += 60) ctx.lineTo(edge + 40 * Math.sin(y / 140 + u * 3), y);
  ctx.lineTo(W + 400, H); ctx.lineTo(W + 400, 0); ctx.closePath();
  ctx.clip(); sceneBelief(ctx, u);          // the wipe reveals S5 already in motion
  ctx.restore();
  whisk(ctx, edge + 40, 1020, 3.2, -1.35 + 0.15 * Math.sin(u * 9));
}

// ---------------------------------------------------------------- S6: we study (u 22..32)
const CARD_W = 760, CARD_H = 560, CARD_Y = 560, CARD_GAP = 900;
const CARDS = [
  { title: 'ศึกษาข้อมูล', icon: 'book', n: '01' },
  { title: 'คัดสรรอย่างใส่ใจ', icon: 'leaves', n: '02' },
  { title: 'ชงทุกแก้วอย่างตั้งใจ', icon: 'bowl', n: '03' },
];
const BOWL_ICON = { dx: -60, dy: 330 };      // chawan position inside card 3 (from card centre-top)
function book(ctx, x, y, s) {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
  for (const sx of [-1, 1]) {
    ctx.beginPath(); ctx.moveTo(0, -10); ctx.quadraticCurveTo(sx * 60, -30, sx * 120, -16); ctx.lineTo(sx * 120, 120); ctx.quadraticCurveTo(sx * 60, 106, 0, 126); ctx.closePath();
    ctx.fillStyle = '#FFFDF7'; ctx.fill(); ctx.lineWidth = 6; ctx.strokeStyle = C.green; ctx.lineJoin = 'round'; ctx.stroke();
    for (let i = 0; i < 4; i++) { ctx.beginPath(); ctx.moveTo(sx * 22, 14 + i * 24); ctx.lineTo(sx * 98, 8 + i * 24); ctx.lineWidth = 5; ctx.strokeStyle = i === 1 ? C.matcha : 'rgba(31,61,36,0.45)'; ctx.lineCap = 'round'; ctx.stroke(); }
  }
  ctx.restore();
  leaf(ctx, x + 112 * s, y + 4 * s, 0.6 * s, 0.6);
}
function card(ctx, u, c, x, idx) {
  const y = CARD_Y;
  rrect(ctx, x - CARD_W / 2 + 16, y + 18, CARD_W, CARD_H, 44); ctx.fillStyle = C.green; ctx.fill();
  rrect(ctx, x - CARD_W / 2, y, CARD_W, CARD_H, 44); ctx.fillStyle = '#FFFDF7'; ctx.fill();
  ctx.lineWidth = 8; ctx.strokeStyle = C.green; ctx.stroke();
  // number chip
  rrect(ctx, x - CARD_W / 2 + 40, y + 36, 110, 64, 32); ctx.fillStyle = C.matcha; ctx.fill();
  ctx.font = font(40, 600, UI); ctx.fillStyle = C.green; ctx.textAlign = 'center'; ctx.fillText(c.n, x - CARD_W / 2 + 95, y + 82);
  const land = 22.8 + idx * 3.1;
  const bob = 1 + 0.06 * wobble(u - land, 2, 4) * (u > land ? 1 : 0);
  ctx.save(); ctx.translate(x, y + 250); ctx.scale(bob, bob); ctx.translate(-x, -(y + 250));
  if (c.icon === 'book') book(ctx, x, y + 170, 1.25);
  if (c.icon === 'leaves') { leaf(ctx, x - 70, y + 330, 1.2, -0.55); leaf(ctx, x + 70, y + 330, 1.2, 0.55); leaf(ctx, x, y + 340, 1.45, 0); }
  if (c.icon === 'bowl') { chawan(ctx, x + BOWL_ICON.dx, y + BOWL_ICON.dy, 1.15); whisk(ctx, x + 110, y + 320, 1.0, 0.35); }
  ctx.restore();
  const sz = Math.min(80, fitSize(ctx, c.title, 600, DISPLAY, CARD_W - 90));
  ctx.font = font(sz, 600, DISPLAY); ctx.fillStyle = C.green; ctx.textAlign = 'center';
  ctx.fillText(c.title, x, y + CARD_H - 62);
}
function sceneStudy(ctx, u) {
  fill(ctx, C.cream);
  // zoom into card 3's bowl (match cut into S7)
  const zp = prog(u, 31.1, 32);
  const pos = springKeys(u, [[21.6, -1], [22.3, 0], [25.4, 1], [28.4, 2]], WHIP);
  const bowlX = CX + (2 - pos) * CARD_GAP + BOWL_ICON.dx, bowlY = CARD_Y + BOWL_ICON.dy - 50;
  ctx.save();
  if (zp > 0) M.zoomAbout(ctx, Math.exp(Math.log(30) * E.inCubic(zp)), bowlX, bowlY);
  rise(ctx, u, 21.75, ['เรา', 'ตั้งใจ', 'ศึกษา'], CX, 445, 118, { stagger: 0.14 });
  CARDS.forEach((c, i) => {
    const x = CX + (i - pos) * CARD_GAP;
    if (x > -CARD_W && x < W + CARD_W) card(ctx, u, c, x, i);
  });
  // Capy studying at the bottom
  const ck = springU(u, 22.2, SPRING.gentle);
  const bobL = 0.035 * Math.sin(u * Math.PI);
  const lookUp = [22.8, 25.9, 28.9].some((b) => u > b && u < b + 0.9);
  const cy = lerp(1900, 1490, ck);
  capy(ctx, CX - 20, cy, 1.2, { glasses: true, lean: bobL, look: lookUp ? [0, -0.5] : [0, 1], eyes: lookUp ? 'open' : eyesOr(u, 4, 'open'), leaf: 0.2 * Math.sin(u * Math.PI) });
  // notebook in front
  ctx.save(); ctx.translate(CX - 20, cy - 84); ctx.rotate(-0.08 + bobL * 0.5); ctx.scale(1.2, 1.2);
  rrect(ctx, -90, -55, 180, 120, 12); ctx.fillStyle = '#FFFDF7'; ctx.fill(); ctx.lineWidth = 6; ctx.strokeStyle = C.green; ctx.stroke();
  ctx.beginPath(); ctx.moveTo(0, -55); ctx.lineTo(0, 65); ctx.stroke();
  for (let i = 0; i < 3; i++) for (const sx of [-1, 1]) { ctx.beginPath(); ctx.moveTo(sx * 18, -22 + i * 26); ctx.lineTo(sx * 72, -22 + i * 26); ctx.lineWidth = 4; ctx.strokeStyle = 'rgba(31,61,36,0.4)'; ctx.stroke(); }
  ctx.restore();
  ctx.restore();
}

// ---------------------------------------------------------------- S7: the craft (u 32..40)
function sceneCraft(ctx, u) {
  fill(ctx, C.green);
  const disc = springU(u, 31.85, SPRING.gentle);
  ctx.beginPath(); ctx.arc(CX, 1110, 410 * disc, 0, Math.PI * 2); ctx.fillStyle = C.cream; ctx.fill();
  // text
  const out1 = E.inBack(prog(u, 36.1, 36.45), 1.4);
  if (u < 36.5) rise(ctx, u, 32.35, ['ใส่ใจ', 'ทุก', 'ขั้นตอน'], CX, 470, 104, { color: C.cream, stagger: 0.12, exit: out1 });
  if (u >= 36.3) {
    rise(ctx, u, 36.35, ['เพื่อ', 'มอบ', 'สิ่ง', 'ดีๆ'], CX, 455, 100, { color: C.cream, stagger: 0.1, weight: 600 });
    rise(ctx, u, 36.8, ['ให้', 'ทุกคน'], CX, 610, 136, { color: C.matcha, stagger: 0.12 });
  }
  // bowl: centred and whisked, then lifts to the upper left and pours into the glass
  const mp = springU(u, 35.9, SPRING.gentle);
  const bx = lerp(CX, 360, mp), by = lerp(1250, 1040, mp), bs = lerp(2.3, 1.45, mp), br = lerp(0, 0.85, mp);
  const zin = u < 33 ? Math.exp(Math.log(2.2) * (1 - E.outCubic(prog(u, 32, 33)))) : 1;  // lands from the zoom
  ctx.save(); M.zoomAbout(ctx, zin, CX, 1150);
  ctx.save(); ctx.translate(bx, by); ctx.rotate(br); chawan(ctx, 0, 0, bs, { foam: clamp((u - 32) / 3) }); ctx.restore();
  // whisk: zig-zag strokes on the beat, then lifts away
  const wl = E.inBack(prog(u, 35.4, 35.95), 1.6);
  if (wl < 1) {
    const zz = Math.sin((u - 32) * Math.PI * 2) * 100 * clamp((u - 32.2) * 2);
    whisk(ctx, CX + zz, 1250 - 90 * 2.3 + 30 - wl * 1300, 2.1, -zz * 0.0025);
  }
  ctx.restore();
  // glass of milk on the right
  const gk = springU(u, 35.8, SPRING.bouncy);
  if (gk > 0) {
    const gx = lerp(1300, 680, gk), gy = 1450;
    const fp = E.inOutCubic(prog(u, 36.5, 37.8));
    const straw = springU(u, 37.85, SPRING.bouncy);
    // pour stream from the bowl's lip
    const lip = [bx + Math.cos(br) * 92 * bs + Math.sin(br) * 90 * bs, by + Math.sin(br) * 92 * bs - Math.cos(br) * 90 * bs];
    const target = [gx, gy - 160 * 1.9 * lerp(0.5, 0.95, fp)];
    const head = E.outCubic(prog(u, 36.25, 36.6)), tail = E.inCubic(prog(u, 37.55, 37.95));
    if (head > 0 && tail < 1) {
      const pt = (q) => { const c = [lip[0] + 60, lip[1] - 10]; const a = 1 - q; return [a * a * lip[0] + 2 * a * q * c[0] + q * q * target[0], a * a * lip[1] + 2 * a * q * c[1] + q * q * target[1]]; };
      ctx.beginPath();
      for (let i = 0; i <= 20; i++) { const q = lerp(tail, head, i / 20); const [px, py] = pt(q); i ? ctx.lineTo(px, py) : ctx.moveTo(px, py); }
      ctx.lineWidth = 24; ctx.lineCap = 'round'; ctx.strokeStyle = C.matcha; ctx.stroke();
    }
    glass(ctx, gx, gy, 1.9, { fill: lerp(0.5, 0.95, fp), layer: lerp(0, 0.5, fp), straw: false, ice: fp > 0.6, rot: 0.04 * ring(u - 37.9, 2, 3) });
    if (straw > 0) { ctx.save(); ctx.beginPath(); ctx.rect(0, 0, W, gy - 160 * 1.9 + 4); ctx.clip(); ctx.translate(gx + 20, gy - 160 * 1.9 + 60 - 280 * (1 - straw)); ctx.rotate(0.12); rrect(ctx, -12, -150, 24, 200, 12); ctx.fillStyle = C.gold; ctx.fill(); ctx.lineWidth = 7; ctx.strokeStyle = C.green; ctx.stroke(); ctx.restore(); }
  }
}

// ---------------------------------------------------------------- S8: every day, together (u 40..48)
function sceneTogether(ctx, u) {
  fill(ctx, C.cream);
  // the week returns along the top and lights up day by day
  DAYS.forEach((d, i) => {
    const x = 132 + i * 126, y = 330;
    const k = springU(u, 39.55 + i * 0.05, SPRING.bouncy);
    const ft = TILE_FLIPS[i];
    const fp = prog(u, ft - 0.2, ft + 0.2);
    const sx = Math.abs(Math.cos(fp * Math.PI)) || 0.001;
    ctx.save(); ctx.translate(x, y + 60); ctx.scale(sx * k, k); ctx.translate(-x, -(y + 60));
    tileDraw(ctx, x, y, 108, 124, d, fp > 0.5, 46);
    ctx.restore();
  });
  const g1 = rise(ctx, u, 40.55, ['มัทฉะ', 'คุณภาพ'], CX, 680, 124, { stagger: 0.12 });
  const g2 = rise(ctx, u, 41.35, ['ในราคา', 'ที่', 'จับต้องได้'], CX, 820, 84, { stagger: 0.1, weight: 600 });
  underline(ctx, g2, E.outCubic(prog(u, 41.9, 42.6)), C.matcha, 0.26, 0.08);
  // Hibi and Capy, glasses up, clink on beat 44
  const hk = springU(u, 39.6, SPRING.bouncy), ck = springU(u, 39.8, SPRING.bouncy);
  const reach = E.inOutCubic(prog(u, 43.3, 44)) - E.inOutCubic(prog(u, 44.6, 45.4)) * 0.6;
  const after = u > 44;
  const cheer = after ? 0.1 * ring(u - 44, 1.6, 2.5) : 0;
  hibi(ctx, lerp(-260, 345, hk), 1490, 1.2, {
    eyes: after ? 'happy' : eyesOr(u, 5), mouth: after ? 'smile' : 'w', lean: 0.12 * reach + cheer,
    wave: [0, lerp(-0.5, -1.25, reach)], ear: [-0.3 * ring(u - 44, 2, 3), 0.3 * ring(u - 44, 2, 3)],
    hold: (k) => glass(k, 0, 0, 0.62, { rot: lerp(0, 0.35, reach) }),
  });
  capy(ctx, lerp(1360, 705, ck), 1490, 1.15, {
    flip: true, eyes: after ? 'happy' : eyesOr(u, 6, 'sleepy'), lean: -0.1 * reach - cheer,
    wave: [0, lerp(-0.4, -1.2, reach)], leaf: 0.4 * ring(u - 44, 2, 2.5),
    hold: (k) => glass(k, 0, 0, 0.65, { rot: lerp(0, 0.35, reach) }),
  });
  // clink sparkle: three short gold strokes
  const sp = prog(u, 44, 44.8);
  if (sp > 0 && sp < 1) {
    for (let i = 0; i < 3; i++) {
      const a = -Math.PI / 2 + (i - 1) * 0.7, r0 = 60 + 60 * E.outCubic(sp), r1 = r0 + 50 * (1 - sp);
      ctx.beginPath(); ctx.moveTo(CLINK[0] + Math.cos(a) * r0, CLINK[1] + Math.sin(a) * r0); ctx.lineTo(CLINK[0] + Math.cos(a) * r1, CLINK[1] + Math.sin(a) * r1);
      ctx.lineWidth = 12; ctx.lineCap = 'round'; ctx.strokeStyle = C.gold; ctx.stroke();
    }
  }
}
const CLINK = [525, 1215];

// ---------------------------------------------------------------- S9: end card (u 48..56)
const BRANCHES = ['ลาดพร้าว 107', 'นาคนิวาส 48', 'สะพานควาย', 'นวมินทร์ 111', 'สามย่าน (จุฬาฯ 11)'];
function sceneEnd(ctx, u) {
  fill(ctx, C.green);
  ctx.save(); shake(ctx, u, 48, 14);
  // logo mark (placeholder until the real logo file arrives)
  const lk = springU(u, 47.8, SPRING.bouncy);
  const LY = 590, LR = 150;
  if (lk > 0) {
    ctx.save(); ctx.translate(CX, LY); ctx.scale(lerp(1.6, 1, lk), lerp(1.6, 1, lk)); ctx.rotate(lerp(-0.2, 0, lk));
    ctx.beginPath(); ctx.arc(0, 0, LR + 14, 0, Math.PI * 2); ctx.fillStyle = C.gold; ctx.fill();
    ctx.beginPath(); ctx.arc(0, 0, LR, 0, Math.PI * 2); ctx.fillStyle = C.cream; ctx.fill();
    ctx.font = font(150, 800, MARK); ctx.fillStyle = C.green; ctx.textAlign = 'center'; ctx.fillText('日々', 0, 52);
    ctx.restore();
  }
  rise(ctx, u, 48.25, ['Hibi'], CX, 880, 130, { color: C.cream });
  const mk = springU(u, 48.5, SPRING.snappy);
  if (mk > 0) {
    ctx.save(); ctx.globalAlpha = clamp(mk); ctx.font = font(42, 500, UI); ctx.letterSpacing = '12px'; ctx.fillStyle = C.gold; ctx.textAlign = 'center';
    ctx.fillText('MATCHA CAFE', CX + 6, 945 + (1 - mk) * 20); ctx.letterSpacing = '0px'; ctx.restore();
  }
  // tagline wipes on
  const tp = E.inOutCubic(prog(u, 48.9, 49.6));
  if (tp > 0) {
    const sz = Math.min(76, fitSize(ctx, 'มัทฉะคุณภาพ ดื่มได้ทุกวัน', 600, DISPLAY, 840));
    ctx.save(); ctx.font = font(sz, 600, DISPLAY); const w = ctx.measureText('มัทฉะคุณภาพ ดื่มได้ทุกวัน').width;
    ctx.beginPath(); ctx.rect(CX - w / 2 - 10, 960, (w + 20) * tp, 140); ctx.clip();
    ctx.fillStyle = C.matcha; ctx.textAlign = 'center'; ctx.fillText('มัทฉะคุณภาพ ดื่มได้ทุกวัน', CX, 1065);
    ctx.restore();
  }
  // branches as pills: 2 + 2 + 1
  const hk = springU(u, 49.7, SPRING.snappy);
  if (hk > 0) {
    ctx.save(); ctx.globalAlpha = clamp(hk); ctx.font = font(40, 600, UI); ctx.fillStyle = C.gold; ctx.textAlign = 'center';
    ctx.fillText('5 สาขา', CX, 1150 + (1 - hk) * 16); ctx.restore();
  }
  const rows = [[0, 1], [2, 3], [4]];
  ctx.font = font(44, 500, UI);
  rows.forEach((r, ri) => {
    const ws = r.map((i) => { ctx.font = font(44, 500, UI); return ctx.measureText(BRANCHES[i]).width + 56; });
    const tot = ws.reduce((a, b) => a + b, 0) + (r.length - 1) * 18;
    let x = CX - tot / 2;
    r.forEach((i, j) => {
      const k = springU(u, 49.9 + i * 0.5, SPRING.bouncy);
      const y = 1180 + ri * 96;
      if (k > 0) {
        ctx.save(); ctx.translate(x + ws[j] / 2, y + 38); ctx.scale(k, k);
        rrect(ctx, -ws[j] / 2, -38, ws[j], 76, 38); ctx.lineWidth = 4; ctx.strokeStyle = C.matcha; ctx.stroke();
        ctx.fillStyle = 'rgba(156,198,91,0.12)'; ctx.fill();
        ctx.font = font(44, 500, UI); ctx.fillStyle = C.cream; ctx.textAlign = 'center'; ctx.fillText(BRANCHES[i], 0, 15);
        ctx.restore();
      }
      x += ws[j] + 18;
    });
  });
  ctx.restore();
  // mascots peek up from the bottom edge
  const pk = springU(u, 50.5, SPRING.bouncy), qk = springU(u, 51, SPRING.bouncy);
  hibi(ctx, 230, lerp(2200, 1960, pk), 1.0, { eyes: eyesOr(u, 7, 'open'), lean: 0.12 + 0.03 * Math.sin(u * Math.PI), look: [0.5, -0.5], wave: [0, -2.3 * clamp((u - 52) * 2)] });
  capy(ctx, 840, lerp(2250, 2010, qk), 1.0, { flip: true, eyes: eyesOr(u, 8, 'sleepy'), lean: -0.1 - 0.03 * Math.sin(u * Math.PI), leaf: 0.2 * Math.sin(u * Math.PI * 0.5) });
  // AI disclosure, clear on the end card
  ctx.font = font(36, 500, UI); ctx.fillStyle = 'rgba(245,240,228,0.85)'; ctx.textAlign = 'center';
  ctx.fillText('ภาพประกอบในคลิปนี้สร้างด้วย AI', CX, 360);
}

// ---------------------------------------------------------------- grain (post, after motion blur)
let GRAIN = [];
function makeGrain() {
  GRAIN = [0, 1, 2, 3].map((s) => {
    const c = document.createElement('canvas'); c.width = 360; c.height = 640;
    const g = c.getContext('2d'); const im = g.createImageData(360, 640); const r = M.mulberry32(97 + s * 13);
    for (let i = 0; i < im.data.length; i += 4) { const v = r() * 255; im.data[i] = im.data[i + 1] = im.data[i + 2] = v; im.data[i + 3] = 255; }
    g.putImageData(im, 0, 0); return c;
  });
}

M.film({
  fonts: [font(100, 700, DISPLAY), font(100, 600, DISPLAY), font(100, 500, DISPLAY), font(40, 500, UI), font(40, 600, UI), font(100, 800, MARK)],
  hits: HITS,
  samples: 12,
  async init(ctx) {
    // make sure both the Thai and the Latin subsets of each face are loaded
    for (const f of [font(100, 700, DISPLAY), font(100, 600, DISPLAY), font(100, 500, DISPLAY), font(40, 500, UI), font(40, 600, UI)]) await document.fonts.load(f, 'ทุกวัน Hibi 107 …?฿');
    await document.fonts.load(font(100, 800, MARK), '日々');
    makeGrain();
  },
  draw(ctx, u) {
    let dark = true;
    if (u < 9.5) { sceneKanji(ctx, u); }
    else if (u < 10) {           // cream wipes up from the bottom, tiles riding on it
      sceneKanji(ctx, u);
      const p = E.inOutCubic(prog(u, 9.5, 10));
      ctx.save(); ctx.beginPath(); ctx.rect(0, H * (1 - p), W, H); ctx.clip(); sceneDays(ctx, u); ctx.restore();
      dark = p < 0.6;
    }
    else if (u < 16) {
      sceneDays(ctx, u); dark = false;
      if (u >= 15.45) whiskWipe(ctx, u);
    }
    else if (u < 21.5) { sceneBelief(ctx, u); dark = false; }
    else if (u < 22) {           // push: S5 up, S6 in from below
      const p = E.inOutCubic(prog(u, 21.5, 22));
      ctx.save(); ctx.translate(0, -H * p); sceneBelief(ctx, u); ctx.restore();
      ctx.save(); ctx.translate(0, H * (1 - p)); sceneStudy(ctx, u); ctx.restore();
      dark = false;
    }
    else if (u < 32) { sceneStudy(ctx, u); dark = u > 31.6; }
    else if (u < 39.5) { sceneCraft(ctx, u); }
    else if (u < 40) {           // push: S7 left, S8 in from the right
      const p = E.inOutCubic(prog(u, 39.5, 40));
      ctx.save(); ctx.translate(-W * p, 0); sceneCraft(ctx, u); ctx.restore();
      ctx.save(); ctx.translate(W * (1 - p), 0); ctx.beginPath(); ctx.rect(0, 0, W, H); ctx.clip(); sceneTogether(ctx, u); ctx.restore();
      dark = p < 0.5;
    }
    else if (u < 48) {
      sceneTogether(ctx, u); dark = false;
      const r = 2400 * E.inCubic(prog(u, 47.2, 48));
      if (r > 0) { ctx.beginPath(); ctx.arc(CLINK[0], CLINK[1], r, 0, Math.PI * 2); ctx.fillStyle = C.green; ctx.fill(); dark = r > 900; }
    }
    else { sceneEnd(ctx, u); }
    if (u < 47.8) aiLabel(ctx, dark);
  },
  post(ctx, u, t) {
    if (!GRAIN.length) return;
    const g = GRAIN[Math.floor(t * 24) % 4];
    ctx.save(); ctx.globalAlpha = 0.045; ctx.globalCompositeOperation = 'overlay';
    ctx.drawImage(g, 0, 0, W, H); ctx.restore();
  },
});
