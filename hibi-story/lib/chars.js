// chars.js: Hibi (cream rabbit), Capy (capybara) and the props, drawn in code.
// Every function is pure: (ctx, x, y, scale, pose) paints one drawing, origin at the feet centre.
// Units are local: a character stands ~260 units tall at scale 1.

export const C = {
  green: '#1F3D24',   // dark green: ink, outlines, night backgrounds
  matcha: '#9CC65B',  // matcha green: the one accent
  cream: '#F5F0E4',   // cream: paper, Hibi's fur, milk
  gold: '#E6C47E',    // gold: Capy's fur, blush, highlights
};
const INK = C.green;
const LW = 7;           // outline weight in local units

const shade = (hex, k) => {        // mix toward dark green by k
  const a = parseInt(hex.slice(1), 16), b = parseInt(INK.slice(1), 16);
  const ch = (n, s) => (n >> s) & 255;
  const m = (s) => Math.round(ch(a, s) + (ch(b, s) - ch(a, s)) * k);
  return `rgb(${m(16)},${m(8)},${m(0)})`;
};

function ell(ctx, x, y, rx, ry, rot = 0) { ctx.beginPath(); ctx.ellipse(x, y, Math.abs(rx), Math.abs(ry), rot, 0, Math.PI * 2); }
function paint(ctx, fill, stroke = INK, lw = LW) {
  if (fill) { ctx.fillStyle = fill; ctx.fill(); }
  if (stroke) { ctx.lineWidth = lw; ctx.strokeStyle = stroke; ctx.lineJoin = 'round'; ctx.lineCap = 'round'; ctx.stroke(); }
}
function begin(ctx, x, y, s, pose) {
  ctx.save();
  ctx.translate(x, y);
  ctx.scale(s * (1 + (pose.squash || 0)), s * (1 - (pose.squash || 0)));
  if (pose.flip) ctx.scale(-1, 1);
  ctx.rotate(pose.lean || 0);
}

// eyes: 'open' | 'happy' (^ ^) | 'blink' | 'wide'; look: [-1..1, -1..1] pupil offset
function eyes(ctx, ex, ey, pose, r = 9) {
  const mode = pose.eyes || 'open';
  const [lx, ly] = pose.look || [0, 0];
  for (const sx of [-1, 1]) {
    const x = sx * ex + lx * 5, y = ey + ly * 4;
    if (mode === 'happy') {
      ctx.beginPath(); ctx.arc(x, y + 4, r * 1.1, Math.PI * 1.15, Math.PI * 1.85);
      paint(ctx, null, INK, LW * 0.9);
    } else if (mode === 'blink') {
      ctx.beginPath(); ctx.moveTo(x - r, y); ctx.lineTo(x + r, y); paint(ctx, null, INK, LW * 0.9);
    } else if (mode === 'sleepy') {
      ctx.beginPath(); ctx.arc(x, y - 2, r * 1.05, Math.PI * 0.1, Math.PI * 0.9); paint(ctx, null, INK, LW * 0.9);
    } else {
      const rr = mode === 'wide' ? r * 1.35 : r;
      ell(ctx, x, y, rr, rr * 1.15); paint(ctx, INK, null);
      ell(ctx, x - rr * 0.3, y - rr * 0.4, rr * 0.32, rr * 0.32); paint(ctx, C.cream, null);
    }
  }
}

// ------------------------------------------------------------------ Hibi, the cream rabbit
// pose: { squash, lean, flip, eyes, look, ear: [l, r] extra angle, wave: [l, r] arm angle,
//         mouth: 'w' | 'o' | 'smile', blush, apron: true, hold: fn(ctx) drawn in the right paw }
export function hibi(ctx, x, y, s, pose = {}) {
  begin(ctx, x, y, s, pose);
  const [el, er] = pose.ear || [0, 0];
  // ears (behind the head)
  for (const [sx, ea] of [[-1, el], [1, er]]) {
    ctx.save();
    ctx.translate(sx * 30, -196);
    ctx.rotate(sx * 0.16 + ea);
    ctx.beginPath(); ctx.roundRect(-20, -112, 40, 122, 20); paint(ctx, C.cream);
    ctx.beginPath(); ctx.roundRect(-9, -96, 18, 88, 9); paint(ctx, C.gold, null);
    ctx.restore();
  }
  // feet
  for (const sx of [-1, 1]) { ell(ctx, sx * 24, -8, 22, 12); paint(ctx, C.cream); }
  // body
  ell(ctx, 0, -58, 52, 54); paint(ctx, C.cream);
  if (pose.apron !== false) {
    ctx.save(); ell(ctx, 0, -58, 52, 54); ctx.clip();
    ctx.beginPath(); ctx.roundRect(-30, -78, 60, 80, 14); paint(ctx, C.matcha, INK, LW * 0.8);
    ell(ctx, 0, -46, 9, 9); paint(ctx, C.cream, null);   // a small leaf-dot on the apron
    ctx.restore();
    ell(ctx, 0, -58, 52, 54); paint(ctx, null);
  }
  // arms
  const [wl, wr] = pose.wave || [0, 0];
  for (const [sx, wa] of [[-1, wl], [1, wr]]) {
    ctx.save(); ctx.translate(sx * 46, -84); ctx.rotate(sx * (-0.3 + wa));
    ell(ctx, 0, 22, 13, 24); paint(ctx, C.cream);
    if (sx === 1 && pose.hold) { ctx.translate(0, 44); ctx.rotate(-(-0.3 + wa)); pose.hold(ctx); }
    ctx.restore();
  }
  // head
  ell(ctx, 0, -150, 80, 68); paint(ctx, C.cream);
  // face
  if (pose.blush !== false) { for (const sx of [-1, 1]) { ell(ctx, sx * 50, -128, 13, 8); paint(ctx, C.gold, null); } }
  eyes(ctx, 30, -152, pose, 9);
  const m = pose.mouth || 'w';
  ctx.beginPath();
  if (m === 'o') { ell(ctx, 0, -126, 8, 10); paint(ctx, INK, null); }
  else if (m === 'smile') { ctx.arc(0, -134, 12, Math.PI * 0.15, Math.PI * 0.85); paint(ctx, null, INK, LW * 0.8); }
  else {
    ctx.moveTo(-12, -132); ctx.quadraticCurveTo(-6, -122, 0, -131); ctx.quadraticCurveTo(6, -122, 12, -132);
    paint(ctx, null, INK, LW * 0.75);
  }
  ell(ctx, 0, -138, 6, 4); paint(ctx, INK, null); // nose
  ctx.restore();
}

// ------------------------------------------------------------------ Capy, the capybara
// pose: { squash, lean, flip, eyes ('sleepy' default), look, leaf: angle, glasses, wave, mouth, hold }
export function capy(ctx, x, y, s, pose = {}) {
  begin(ctx, x, y, s, pose);
  const fur = C.gold, dark = shade(C.gold, 0.28), snout = shade(C.gold, 0.12);
  // feet
  for (const sx of [-1, 1]) { ctx.beginPath(); ctx.roundRect(sx * 46 - 22, -26, 44, 28, 12); paint(ctx, dark); }
  // body
  ctx.beginPath(); ctx.roundRect(-92, -150, 184, 136, 64); paint(ctx, fur);
  ell(ctx, 0, -66, 50, 40); paint(ctx, shade(C.cream, 0.05), null); // pale belly
  // arms
  const [wl, wr] = pose.wave || [0, 0];
  for (const [sx, wa] of [[-1, wl], [1, wr]]) {
    ctx.save(); ctx.translate(sx * 80, -110); ctx.rotate(sx * (-0.2 + wa));
    ctx.beginPath(); ctx.roundRect(-15, 0, 30, 52, 15); paint(ctx, fur);
    if (sx === 1 && pose.hold) { ctx.translate(0, 52); ctx.rotate(-(-0.2 + wa)); pose.hold(ctx); }
    ctx.restore();
  }
  // ears
  for (const sx of [-1, 1]) { ell(ctx, sx * 58, -252, 17, 14); paint(ctx, dark); }
  // head: boxy, wide
  ctx.beginPath(); ctx.roundRect(-82, -266, 164, 132, [60, 60, 48, 48]); paint(ctx, fur);
  // snout
  ctx.beginPath(); ctx.roundRect(-52, -196, 104, 64, 30); paint(ctx, snout, INK, LW * 0.8);
  for (const sx of [-1, 1]) { ell(ctx, sx * 16, -176, 6, 4.5); paint(ctx, INK, null); }
  if ((pose.mouth || 'smile') === 'o') { ell(ctx, 0, -150, 7, 8); paint(ctx, INK, null); }
  else { ctx.beginPath(); ctx.moveTo(-10, -152); ctx.quadraticCurveTo(0, -144, 10, -152); paint(ctx, null, INK, LW * 0.7); }
  // eyes
  eyes(ctx, 40, -220, { ...pose, eyes: pose.eyes || 'sleepy' }, 8);
  if (pose.glasses) {
    for (const sx of [-1, 1]) { ell(ctx, sx * 40, -220, 22, 20); paint(ctx, 'rgba(245,240,228,0.25)', INK, LW * 0.75); }
    ctx.beginPath(); ctx.moveTo(-18, -222); ctx.lineTo(18, -222); paint(ctx, null, INK, LW * 0.75);
  }
  // a matcha leaf on the head (Capy's signature)
  ctx.save(); ctx.translate(10, -268); ctx.rotate(-0.4 + (pose.leaf || 0)); leafPath(ctx, 0, 0, 58, 26); paint(ctx, C.matcha, INK, LW * 0.8);
  ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(0, -50); paint(ctx, null, INK, LW * 0.5); ctx.restore();
  ctx.restore();
}

// ------------------------------------------------------------------ props
export function leafPath(ctx, x, y, len, wid) {
  ctx.beginPath();
  ctx.moveTo(x, y);
  ctx.bezierCurveTo(x - wid, y - len * 0.3, x - wid * 0.7, y - len * 0.8, x, y - len);
  ctx.bezierCurveTo(x + wid * 0.7, y - len * 0.8, x + wid, y - len * 0.3, x, y);
}
export function leaf(ctx, x, y, s, rot = 0, fill = C.matcha) {
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(s, s);
  leafPath(ctx, 0, 0, 100, 44); paint(ctx, fill, INK, 6);
  ctx.beginPath(); ctx.moveTo(0, -4); ctx.lineTo(0, -84); paint(ctx, null, INK, 4);
  ctx.restore();
}

// Iced matcha latte in a glass. fill 0..1 = how full; layer 0..1 = matcha share of the drink.
// origin bottom centre, 100 wide x 160 tall at s=1.
export function glass(ctx, x, y, s, { fill = 1, layer = 0.55, straw = true, rot = 0, ice = true } = {}) {
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(s, s);
  const shape = () => { ctx.beginPath(); ctx.moveTo(-50, -160); ctx.lineTo(50, -160); ctx.lineTo(40, -6); ctx.quadraticCurveTo(40, 0, 34, 0); ctx.lineTo(-34, 0); ctx.quadraticCurveTo(-40, 0, -40, -6); ctx.closePath(); };
  if (straw) { ctx.beginPath(); ctx.roundRect(10, -205, 12, 150, 6); ctx.save(); ctx.rotate(0.12); paint(ctx, C.gold, INK, 5); ctx.restore(); }
  shape(); ctx.fillStyle = 'rgba(245,240,228,0.55)'; ctx.fill();
  ctx.save(); shape(); ctx.clip();
  const top = -150 * fill, mid = top * (1 - layer);
  ctx.fillStyle = C.cream; ctx.fillRect(-60, mid, 120, -mid + 2);
  ctx.fillStyle = C.matcha; ctx.fillRect(-60, top, 120, mid - top);
  if (ice && fill > 0.3) for (const [ix, iy, r] of [[-18, top + 18, 0.2], [14, top + 30, -0.3]]) {
    ctx.save(); ctx.translate(ix, iy); ctx.rotate(r); ctx.beginPath(); ctx.roundRect(-13, -13, 26, 26, 6);
    paint(ctx, 'rgba(255,255,255,0.45)', 'rgba(31,61,36,0.35)', 3); ctx.restore();
  }
  ctx.restore();
  shape(); paint(ctx, null, INK, 6);
  ctx.beginPath(); ctx.moveTo(-34, -140); ctx.lineTo(-28, -30); paint(ctx, null, 'rgba(255,255,255,0.7)', 5);
  ctx.restore();
}

// Chawan (tea bowl) with whisked matcha, 180 wide.
export function chawan(ctx, x, y, s, { foam = 1 } = {}) {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
  ctx.beginPath(); ctx.moveTo(-92, -90); ctx.quadraticCurveTo(-88, 0, 0, 0); ctx.quadraticCurveTo(88, 0, 92, -90); ctx.closePath();
  paint(ctx, C.green, INK, 6);
  ctx.beginPath(); ctx.roundRect(-30, -4, 60, 12, 4); paint(ctx, C.green, INK, 5);
  ell(ctx, 0, -90, 92, 18); paint(ctx, C.matcha, INK, 6);
  if (foam > 0) for (let i = 0; i < 9; i++) { ell(ctx, -60 + i * 15, -92 + Math.sin(i * 2.1) * 6, 4 * foam, 3 * foam); paint(ctx, 'rgba(245,240,228,0.7)', null); }
  ctx.restore();
}

// Chasen (bamboo whisk), handle up, 150 tall; origin at the tine tips.
export function whisk(ctx, x, y, s, rot = 0) {
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(s, s);
  ctx.beginPath(); ctx.moveTo(-34, 0); ctx.quadraticCurveTo(-40, -50, -12, -70); ctx.lineTo(12, -70); ctx.quadraticCurveTo(40, -50, 34, 0); ctx.closePath();
  paint(ctx, C.gold, INK, 5);
  for (let i = -3; i <= 3; i++) { ctx.beginPath(); ctx.moveTo(i * 9, -4); ctx.quadraticCurveTo(i * 10, -40, i * 3, -66); paint(ctx, null, shade(C.gold, 0.4), 2.5); }
  ctx.beginPath(); ctx.roundRect(-13, -150, 26, 84, 10); paint(ctx, C.gold, INK, 5);
  ctx.restore();
}

// A price tag on a string. text drawn by caller via label(ctx) in tag-local coords.
export function tag(ctx, x, y, s, rot, fill, label) {
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot); ctx.scale(s, s);
  ctx.beginPath(); ctx.moveTo(0, -60); ctx.lineTo(0, 0); paint(ctx, null, INK, 4);
  ctx.beginPath(); ctx.moveTo(-40, 0); ctx.lineTo(40, 0); ctx.lineTo(90, 40); ctx.lineTo(90, 220); ctx.lineTo(-90, 220); ctx.lineTo(-90, 40); ctx.closePath();
  paint(ctx, fill, INK, 7);
  ell(ctx, 0, 30, 10, 10); paint(ctx, C.cream, INK, 5);
  if (label) label(ctx);
  ctx.restore();
}
