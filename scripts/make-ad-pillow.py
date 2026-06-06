#!/usr/bin/env python3
"""
Hibi Matcha — Clear Okumidori Instagram Ad
Composite image creator using Pillow + FC Minimal font
Output: 1080x1080px PNG
"""
import math, os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT_DIR = "/home/user/hibi-green-tea/public/ads/exports"
os.makedirs(OUT_DIR, exist_ok=True)

FONTS_DIR = "/home/user/hibi-green-tea/public/fonts/fc-minimal"
DEJAVU    = "/usr/share/fonts/truetype/dejavu"
SERIF     = "/usr/share/fonts/truetype/liberation"

def font(path, size):
    return ImageFont.truetype(path, size)

FC_REG  = f"{FONTS_DIR}/FCMinimal-Regular.ttf"
FC_BOLD = f"{FONTS_DIR}/FCMinimal-Bold.ttf"
FC_IT   = f"{FONTS_DIR}/FCMinimal-Italic.ttf"
DV_SANS = f"{DEJAVU}/DejaVuSans.ttf"
DV_BOLD = f"{DEJAVU}/DejaVuSans-Bold.ttf"
SER_BOLD= f"{SERIF}/LiberationSerif-Bold.ttf"
SER_IT  = f"{SERIF}/LiberationSerif-Italic.ttf"

W, H = 1080, 1080

# ── Color palette ────────────────────────────────────────────────────────────
BG_DARK   = (7,  18,  9)
BG_MID    = (13, 35, 18)
BG_LIGHT  = (15, 45, 22)
GREEN_500 = (34, 197, 94)
GREEN_400 = (74, 222, 128)
GREEN_600 = (22, 163, 74)
GREEN_800 = (22, 101, 52)
WHITE     = (255, 255, 255)
WHITE_90  = (255, 255, 255, 230)
WHITE_60  = (255, 255, 255, 153)
WHITE_35  = (255, 255, 255, 89)
WHITE_20  = (255, 255, 255, 51)
MINT_60   = (74, 222, 128, 153)
MINT_90   = (74, 222, 128, 229)

def hex2rgb(h): r=int(h[1:3],16); g=int(h[3:5],16); b=int(h[5:7],16); return (r,g,b)

# ── Build background gradient ────────────────────────────────────────────────
def make_gradient(w, h, stops):
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        t = y / (h - 1)
        c = [0, 0, 0]
        for i in range(len(stops) - 1):
            t0, c0 = stops[i]
            t1, c1 = stops[i+1]
            if t0 <= t <= t1:
                f = (t - t0) / (t1 - t0)
                c = [int(c0[j] + f * (c1[j] - c0[j])) for j in range(3)]
                break
        for x in range(w):
            px[x, y] = tuple(c)
    return img

def make_radial_orb(size, color_rgb, alpha_center=0.15):
    img = Image.new("RGBA", (size, size), (0,0,0,0))
    px = img.load()
    cx = cy = size // 2
    for y in range(size):
        for x in range(size):
            d = math.sqrt((x-cx)**2 + (y-cy)**2)
            r = size // 2
            if d < r:
                a = alpha_center * (1 - d/r) ** 2
                img.putpixel((x,y), (*color_rgb, int(a*255)))
    return img

# ── Draw rounded rectangle ───────────────────────────────────────────────────
def rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    x1, y1, x2, y2 = xy
    if fill:
        draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill)
    if outline:
        draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, outline=outline, width=width)

# ── Draw pill tag ────────────────────────────────────────────────────────────
def pill_tag(draw, img, x, y, text, fnt, text_color, border_color, bg_color):
    tw = draw.textlength(text, font=fnt)
    pw, ph = int(tw + 28), 32
    # Draw bg on separate layer
    pill = Image.new("RGBA", (pw, ph), (0,0,0,0))
    pd = ImageDraw.Draw(pill)
    pd.rounded_rectangle([0,0,pw-1,ph-1], radius=ph//2,
                          fill=(*bg_color[:3], 25), outline=(*border_color[:3], 70), width=1)
    # green dot
    pd.ellipse([10,ph//2-4, 18, ph//2+4], fill=(74,222,128,220))
    # text
    pd.text((24, ph//2), text, font=fnt, fill=(*text_color[:3], 200), anchor="lm")
    img.alpha_composite(pill, (x, y))
    return pw + 10

# ── Main canvas ───────────────────────────────────────────────────────────────
canvas_rgb = make_gradient(W, H, [
    (0.0, BG_DARK),
    (0.4, BG_MID),
    (0.7, BG_LIGHT),
    (1.0, BG_DARK),
])

canvas = canvas_rgb.convert("RGBA")

# Orbs
orb1 = make_radial_orb(700, GREEN_500, 0.10)
canvas.alpha_composite(orb1, (-80, -120))

orb2 = make_radial_orb(400, GREEN_400, 0.07)
canvas.alpha_composite(orb2, (300, 650))

orb3 = make_radial_orb(250, GREEN_600, 0.12)
canvas.alpha_composite(orb3, (800, 100))

# ── Glass illustration (right side) ─────────────────────────────────────────
# We'll use SVG-like layering via Pillow shapes

GX, GY = 640, 130   # glass origin (top center)
GW, GH = 300, 740   # glass width, height

# Glass body (tapered from top GW → GW-30 bottom)
glass_layer = Image.new("RGBA", (W, H), (0,0,0,0))
gd = ImageDraw.Draw(glass_layer)

# Body outline shape (trapezoid)
body_pts = [
    (GX - GW//2,       GY),
    (GX + GW//2,       GY),
    (GX + GW//2 - 20,  GY + GH),
    (GX - GW//2 + 20,  GY + GH),
]
gd.polygon(body_pts, fill=(255,255,255,15), outline=(255,255,255,40))

# Matcha liquid fill
liquid_top = GY + 180
liquid_pts = [
    (GX - GW//2 + 5,           liquid_top),
    (GX + GW//2 - 5,           liquid_top),
    (GX + GW//2 - 22,          GY + GH - 4),
    (GX - GW//2 + 22,          GY + GH - 4),
]
# Layer gradient effect for liquid
for i, pts in enumerate([liquid_pts]):
    liq = Image.new("RGBA", (W, H), (0,0,0,0))
    ld = ImageDraw.Draw(liq)
    ld.polygon(pts, fill=(34,197,94,210))
    canvas.alpha_composite(liq)

# Liquid surface highlight
surf_layer = Image.new("RGBA", (W, H), (0,0,0,0))
sd = ImageDraw.Draw(surf_layer)
sd.ellipse([GX-GW//2+5, liquid_top-15, GX+GW//2-5, liquid_top+15], fill=(74,222,128,90))
canvas.alpha_composite(surf_layer)

# Ice cubes
ice_layer = Image.new("RGBA", (W, H), (0,0,0,0))
id_ = ImageDraw.Draw(ice_layer)
ice_blocks = [
    (GX-100, liquid_top+20, GX-20, liquid_top+90, -8),
    (GX+10,  liquid_top+35, GX+95, liquid_top+100, 5),
    (GX-70,  liquid_top+95, GX+20, liquid_top+175, -3),
    (GX+5,   liquid_top+130,GX+90, liquid_top+205, 7),
]
for (x1,y1,x2,y2,angle) in ice_blocks:
    # Rotated rectangle via polygon
    cx, cy = (x1+x2)//2, (y1+y2)//2
    hw, hh = (x2-x1)//2, (y2-y1)//2
    rad = math.radians(angle)
    cos_a, sin_a = math.cos(rad), math.sin(rad)
    pts = []
    for dx, dy in [(-hw,-hh),(hw,-hh),(hw,hh),(-hw,hh)]:
        pts.append((cx + dx*cos_a - dy*sin_a, cy + dx*sin_a + dy*cos_a))
    id_.polygon(pts, fill=(255,255,255,55), outline=(255,255,255,130))
canvas.alpha_composite(ice_layer)

# Glass highlight (left edge)
hl_layer = Image.new("RGBA", (W, H), (0,0,0,0))
hd = ImageDraw.Draw(hl_layer)
for i in range(8):
    alpha = int(60 * (1 - i/8))
    hd.line([(GX-GW//2+i, GY+20), (GX-GW//2+10+i, GY+GH-20)],
            fill=(255,255,255,alpha), width=1)
canvas.alpha_composite(hl_layer)

# Condensation dots
cond_layer = Image.new("RGBA", (W, H), (0,0,0,0))
cd = ImageDraw.Draw(cond_layer)
import random; random.seed(42)
for _ in range(80):
    cx_ = random.randint(GX-GW//2+5, GX+GW//2-15)
    cy_ = random.randint(liquid_top+20, GY+GH-30)
    r_ = random.randint(1, 4)
    a_ = random.randint(40, 110)
    cd.ellipse([cx_-r_,cy_-r_,cx_+r_,cy_+r_], fill=(255,255,255,a_))
canvas.alpha_composite(cond_layer)

# Glass body composite
canvas.alpha_composite(glass_layer)

# Rim top
rim_layer = Image.new("RGBA", (W, H), (0,0,0,0))
rd = ImageDraw.Draw(rim_layer)
rd.line([(GX-GW//2, GY), (GX+GW//2, GY)], fill=(255,255,255,120), width=3)
canvas.alpha_composite(rim_layer)

# Straw
straw_layer = Image.new("RGBA", (W, H), (0,0,0,0))
std = ImageDraw.Draw(straw_layer)
sx = GX + 60
std.rounded_rectangle([sx-6, GY-30, sx+6, GY+GH//2], radius=6,
                       fill=(255,255,255,50), outline=(255,255,255,100), width=1)
canvas.alpha_composite(straw_layer)

# Glow under glass
glow = Image.new("RGBA", (W, H), (0,0,0,0))
gd2 = ImageDraw.Draw(glow)
gd2.ellipse([GX-160, GY+GH-40, GX+160, GY+GH+40], fill=(34,197,94,30))
glow = glow.filter(ImageFilter.GaussianBlur(30))
canvas.alpha_composite(glow)

# ── Left-side text gradient overlay ─────────────────────────────────────────
overlay = Image.new("RGBA", (W, H), (0,0,0,0))
od = ImageDraw.Draw(overlay)
# Gradient left → transparent (for legibility)
for x in range(620):
    t = x / 620
    a = int(200 * (1 - t**1.5))
    od.line([(x, 0), (x, H)], fill=(7,18,9,a))
canvas.alpha_composite(overlay)

# ── Frame lines ──────────────────────────────────────────────────────────────
frame = Image.new("RGBA", (W, H), (0,0,0,0))
fd = ImageDraw.Draw(frame)
PAD = 44
# Top line
for x in range(PAD, W-PAD):
    t = (x - PAD) / (W - 2*PAD)
    a = int(100 * math.sin(t * math.pi))
    fd.point((x, PAD), fill=(74,222,128,a))
# Bottom line
for x in range(PAD, W-PAD):
    t = (x - PAD) / (W - 2*PAD)
    a = int(100 * math.sin(t * math.pi))
    fd.point((x, H-PAD), fill=(74,222,128,a))
# Left line
for y in range(PAD, H-PAD):
    t = (y - PAD) / (H - 2*PAD)
    a = int(80 * math.sin(t * math.pi))
    fd.point((PAD, y), fill=(74,222,128,a))
canvas.alpha_composite(frame)

# ── Typography ───────────────────────────────────────────────────────────────
txt = Image.new("RGBA", (W, H), (0,0,0,0))
td = ImageDraw.Draw(txt)

# Brand name
f_brand   = font(FC_BOLD, 22)
f_brand_s = font(FC_REG, 18)
f_grade   = font(DV_BOLD, 17)
f_series  = font(FC_BOLD, 18)
f_title_l = font(SER_BOLD, 108)
f_title_s = font(SER_IT,   64)
f_body    = font(FC_REG, 28)
f_body_s  = font(FC_REG, 22)
f_tag     = font(FC_REG, 21)
f_price_l = font(DV_BOLD, 92)
f_price_s = font(FC_REG, 24)
f_cta     = font(FC_BOLD, 22)
f_hash    = font(FC_REG, 19)

X = 72  # left margin

# ── HEADER ────────────────────────────────────────────────────────────────
Y = 72
td.text((X, Y), "HIBI MATCHA", font=f_brand, fill=(74,222,128,240))
td.text((X, Y+28), "日々 抹茶  ·  Since 2024", font=f_brand_s, fill=(255,255,255,80))

# Grade badge
badge_x = X + 280
badge_w, badge_h = 200, 34
rounded_rect(td, (badge_x, Y-2, badge_x+badge_w, Y+badge_h),
             radius=5, fill=(34,197,94,22), outline=(74,222,128,70), width=1)
td.ellipse([badge_x+12, Y+9, badge_x+22, Y+19], fill=(74,222,128,220))
td.text((badge_x+30, Y+badge_h//2-2), "CEREMONIAL GRADE",
        font=font(DV_BOLD, 14), fill=(74,222,128,210), anchor="lm")

# ── SERIES LABEL ──────────────────────────────────────────────────────────
Y = 170
td.text((X, Y), "CLEAR SERIES  ·  SIGNATURE MENU",
        font=f_series, fill=(74,222,128,130))

# ── PRODUCT TITLE ─────────────────────────────────────────────────────────
Y = 210
td.text((X-4, Y), "Clear", font=f_title_l, fill=(255,255,255,255))
Y = 302
td.text((X, Y), "Okumidori", font=f_title_s, fill=(255,255,255,85))

# ── KEY MESSAGE ───────────────────────────────────────────────────────────
Y = 400
lines = [
    "ความบริสุทธิ์ที่ดื่มได้",
    "มัทฉะ Ceremonial Grade สายพันธุ์ Okumidori",
    "จาก Uji, Kyoto  กลิ่นสาหร่ายหอม อูมามิลึก",
]
line_colors = [(255,255,255,230), (255,255,255,150), (255,255,255,120)]
for i, (line, col) in enumerate(zip(lines, line_colors)):
    td.text((X, Y + i * 36), line, font=f_body_s if i > 0 else f_body, fill=col)

# ── FLAVOR TAGS ───────────────────────────────────────────────────────────
Y = 536
tags = ["หอมสาหร่าย", "อูมามิลึก", "สดชื่น", "ไม่ขม", "Iced · Pure"]
tx = X
for tag in tags:
    tw = int(td.textlength(tag, font=f_tag))
    pw, ph = tw + 30, 34
    pill = Image.new("RGBA", (pw, ph), (0,0,0,0))
    pd2 = ImageDraw.Draw(pill)
    pd2.rounded_rectangle([0,0,pw-1,ph-1], radius=ph//2,
                           fill=(74,222,128,18), outline=(74,222,128,65), width=1)
    pd2.ellipse([9, ph//2-4, 17, ph//2+4], fill=(74,222,128,180))
    pd2.text((22, ph//2), tag, font=f_tag, fill=(255,255,255,180), anchor="lm")
    txt.alpha_composite(pill, (tx, Y))
    tx += pw + 8

# ── ORIGIN STRIP ──────────────────────────────────────────────────────────
Y = 606
# Left accent bar
for dy in range(68):
    a = int(180 * math.sin(dy / 67 * math.pi))
    txt.putpixel((X, Y + dy), (74,222,128,a))
txt.putpixel((X+1, Y), (74,222,128,120))
txt.putpixel((X+1, Y+67), (74,222,128,120))

f_olabel = font(DV_BOLD, 17)
f_oval   = font(FC_BOLD, 26)

items = [("ORIGIN", "Uji, Kyoto 🇯🇵"), ("CULTIVAR", "Okumidori 奥みどり"), ("GRADE", "Ceremonial ⭐⭐⭐")]
ix = X + 16
for label, value in items:
    td.text((ix, Y+2),  label, font=f_olabel, fill=(74,222,128,160))
    td.text((ix, Y+24), value, font=f_oval,   fill=(255,255,255,210))
    ix += 185
    if label != "GRADE":
        for dy2 in range(60):
            a2 = int(80 * math.sin(dy2/59 * math.pi))
            txt.putpixel((ix-10, Y+4+dy2), (255,255,255,a2))

# ── PRICE ─────────────────────────────────────────────────────────────────
Y = 718
td.text((X, Y), "ราคา DINE-IN", font=font(FC_BOLD, 20), fill=(74,222,128,170))
# Currency symbol
td.text((X-2, Y+36), "฿", font=font(DV_BOLD, 52), fill=(255,255,255,160))
td.text((X+44, Y+28), "235", font=f_price_l, fill=(255,255,255,255))
# Delivery
td.text((X, Y+130), "Delivery  ฿255  ·  GrabFood  ·  LINE MAN  ·  Wongnai",
        font=f_price_s, fill=(255,255,255,100))

# ── CTA BUTTON ────────────────────────────────────────────────────────────
btn_x, btn_y = X + 390, Y + 28
btn_w, btn_h = 170, 52

# Glow behind button
btn_glow = Image.new("RGBA", (W, H), (0,0,0,0))
bg2 = ImageDraw.Draw(btn_glow)
bg2.rounded_rectangle([btn_x-8, btn_y-8, btn_x+btn_w+8, btn_y+btn_h+8],
                       radius=12, fill=(34,197,94,40))
btn_glow = btn_glow.filter(ImageFilter.GaussianBlur(12))
txt.alpha_composite(btn_glow)

td.rounded_rectangle([btn_x, btn_y, btn_x+btn_w, btn_y+btn_h],
                      radius=6, fill=(22,163,74,255))
td.rounded_rectangle([btn_x, btn_y, btn_x+btn_w, btn_y+btn_h//2],
                      radius=6, fill=(34,197,94,40))
btext = "สั่งเลยตอนนี้"
btw = int(td.textlength(btext, font=f_cta))
td.text((btn_x + (btn_w - btw)//2, btn_y + btn_h//2 - 2),
        btext, font=f_cta, fill=(255,255,255,255), anchor="lm")

# ── HASHTAGS ──────────────────────────────────────────────────────────────
Y = 910
hashes = "#HibiMatcha   #มัทฉะไทย   #ชาญี่ปุ่น   #ClearOkumidori"
td.text((X, Y), hashes, font=f_hash, fill=(74,222,128,120))

# Composite text layer
canvas.alpha_composite(txt)

# Final output
out_path = f"{OUT_DIR}/v3-pillow-dark.png"
canvas.convert("RGB").save(out_path, "PNG", quality=95)
print(f"✅  Saved: {out_path}")
print(f"   Size: {os.path.getsize(out_path)//1024}KB")
