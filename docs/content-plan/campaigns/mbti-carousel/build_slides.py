import os, subprocess, base64, io
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, "out3"); os.makedirs(OUT, exist_ok=True)
_cache = {}
def img(name, folder="cut", maxh=900):
    k = (name, folder)
    if k not in _cache:
        im = Image.open(f"{D}/{folder}/{name}.png")
        if im.size[1] > maxh: im = im.resize((int(im.size[0] * maxh / im.size[1]), maxh), Image.LANCZOS)
        b = io.BytesIO(); im.save(b, "PNG"); _cache[k] = "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()
    return _cache[k]
LOGO = lambda: img("hibi_logo", "assets")

FONTS = "".join(
    f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file:///root/.fonts/{f}-{w}-{s}.woff2') format('woff2');}}"
    for fam, f in [("Prompt", "Prompt"), ("Plex", "IBMPlexSansThai")]
    for w in ([400, 500, 600, 700] if f == "Prompt" else [400, 600])
    for s in ["thai", "latin"])

CAPY = """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="100" cy="158" rx="70" ry="38" fill="#a8744a"/>
<circle cx="62" cy="62" r="13" fill="#946240"/><circle cx="138" cy="62" r="13" fill="#946240"/>
<circle cx="62" cy="62" r="6" fill="#6f4529"/><circle cx="138" cy="62" r="6" fill="#6f4529"/>
<rect x="38" y="52" width="124" height="100" rx="50" fill="#c08a5c"/>
<ellipse cx="100" cy="122" rx="38" ry="25" fill="#a8744a"/>
<rect x="87" y="108" width="26" height="11" rx="5.5" fill="#4a2f1d"/>
<path d="M68 94 q10 8 20 0" stroke="#3b2416" stroke-width="5.5" fill="none" stroke-linecap="round"/>
<path d="M112 94 q10 8 20 0" stroke="#3b2416" stroke-width="5.5" fill="none" stroke-linecap="round"/>
<ellipse cx="58" cy="114" rx="11" ry="6.5" fill="#f2a99a" opacity=".75"/><ellipse cx="142" cy="114" rx="11" ry="6.5" fill="#f2a99a" opacity=".75"/>
<path d="M80 26 L120 26 L114 52 L86 52 Z" fill="#fbf6ec" stroke="#7a5233" stroke-width="2.5" stroke-linejoin="round"/>
<ellipse cx="100" cy="26" rx="20" ry="6" fill="#4e7c3a"/>
</svg>"""

CSS = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{overflow:hidden;background:#f2f9ea;font-family:'Plex',sans-serif;color:#1d2b18;position:relative}
.P{font-family:'Prompt',sans-serif}
.top{position:absolute;top:34px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center;font-family:'Prompt';font-size:22px;color:#243e1b;letter-spacing:1.5px}
.top .pg{background:#243e1b;color:#fff;border-radius:20px;padding:4px 16px;font-size:20px;letter-spacing:0}
.foot{position:absolute;left:0;right:0;top:1270px;height:80px;background:#243e1b;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 56px;font-family:'Prompt';font-size:22px}
.foot .r{opacity:.85}
.swipe{position:absolute;right:56px;top:1205px;font-family:'Prompt';font-weight:500;font-size:22px;color:#4e7c3a}
.av{border-radius:50%;overflow:hidden;display:inline-block;vertical-align:middle}
.av{padding:3px}.av img{width:100%;height:100%;border-radius:50%;display:block;object-fit:cover}
.av.h{background:#4e7c3a}.av.c{background:#a8744a}
.cut{filter:drop-shadow(0 18px 16px rgba(36,62,27,.20))}
"""

def avatar(kind, size):
    # official character art (characters/*_sheet.png) cropped to faces
    k, f = ("h", "hibi_face") if kind == "H" else ("c", "capy_face")
    return f'<span class="av {k}" style="width:{size}px;height:{size}px"><img src="{img(f, "assets")}"></span>'

TOTAL = 8
ART = lambda n: img(n, "art", maxh=1100)

def page(n, body, css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
body{{background:#f3f8ec url('{img("bg_paper", "assets", maxh=1350)}') center/cover}}
.art{{position:absolute;filter:drop-shadow(0 14px 18px rgba(36,62,27,.14))}}
{css}</style></head><body>
<div class="top"><span>HIBI MATCHA CAFE 日々</span><span class="pg">{n}/{TOTAL}</span></div>{body}
<div class="foot"><span>มัทฉะแก้วไหนคือคุณ?</span><span class="r">@hibimatchacafe</span></div></body></html>"""

# ---------- data: เมนูจริง + รายละเอียด MBTI ----------
# (MBTI, ฉายา TH, ฉายา EN, [นิสัย 3 คำ], ไฟล์ภาพแก้ว, ชื่อเมนู EN, TH, ราคา, ความหวาน, หนึ่งบรรทัด)
GROUPS = [
    ("NT", "นักวิเคราะห์", "Analysts", "ใช้เหตุผล · ชอบเรียนรู้ · อยากรู้ว่า “ทำไม”", "ขอของแท้ ไม่ต้องปรุงเยอะ", "#243e1b", "#e3eedb", "nt", [
        ("INTJ", "สถาปนิก", "Architect", ["วางแผนล่วงหน้า", "มีเหตุผล", "ชอบของแท้"], "clear_matcha", "Clear Matcha", "มัทฉะใส", "59.-", "0g", "วางแผนมาแล้ว ขอมัทฉะแท้ ๆ ไม่ต้องหวาน"),
        ("INTP", "นักตรรกะ", "Logician", ["ช่างสงสัย", "ชอบทดลอง", "คิดลึก"], "kirei_yuzu", "Kirei Yuzu Matcha", "มัทฉะยูซุคิเรอิ", "79.-", "3g", "ยูซุ + มัทฉะ เข้ากันได้ไง… ขอทดลองก่อน"),
        ("ENTJ", "ผู้บัญชาการ", "Commander", ["ตัดสินใจไว", "ผู้นำโดยธรรมชาติ", "ขอของดีสุด"], "velvet_whisk", "Velvet Matcha Whisk Latte", "ท็อปโฟมนมเย็น", "129.-", "5g", "เลือกตัวท็อปของร้าน ไม่เสียเวลาลังเล"),
        ("ENTP", "นักโต้วาที", "Debater", ["ไอเดียเยอะ", "ชอบถกเถียง", "กล้าลองของแปลก"], "thai_matcha", "Jasmine Thai Tea × Matcha", "ชาไทยมะลิ × มัทฉะ", "109.-", "สูตรคงที่", "ชาไทยกับมัทฉะเข้ากันไม่ได้? ขอเถียง!"),
    ]),
    ("NF", "นักการทูต", "Diplomats", "ใช้หัวใจ · เข้าใจคน · มีโลกในแบบตัวเอง", "หอม ละมุน มีเรื่องราว", "#4e7c3a", "#e6f1dc", "nf", [
        ("INFJ", "ผู้สนับสนุน", "Advocate", ["ลึกซึ้ง", "อ่านใจคนเก่ง", "มีอุดมการณ์"], "coconut_jasmine", "Clear Matcha Coconut Jasmine", "มัทฉะใสมะพร้าวมะลิ", "79.-", "3g", "หอมมะลิบาง ๆ ลึกหลายชั้น เหมือนใจเรา"),
        ("INFP", "ผู้ไกล่เกลี่ย", "Mediator", ["ช่างฝัน", "อ่อนโยน", "มีโลกส่วนตัว"], "osmanthus", "Osmanthus Honey Coconut", "หอมหมื่นลี้ น้ำผึ้ง มะพร้าว", "เมนูแนะนำ", "ไม่หวานเกิน", "นั่งริมหน้าต่าง ฝันกลางวันได้ทั้งบ่าย"),
        ("ENFJ", "ตัวเอก", "Protagonist", ["ใจดี", "ดูแลทุกคน", "สร้างแรงบันดาลใจ"], "cloud_latte", "Matcha Cloud Latte", "มัทฉะคลาวด์ลาเต้", "79.-", "สูตรคงที่", "นุ่มเหมือนเมฆ อุ่นเหมือนคนที่ดูแลทุกคน"),
        ("ENFP", "นักรณรงค์", "Campaigner", ["สดใส", "ขี้เล่น", "พลังบวกล้น"], "pink_cloud", "Pink Coconut Cloud", "Pink is Fine Collection", "79.-", "10g", "สีชมพู! ถ่าย 30 รูปก่อนจิบคำแรก"),
    ]),
    ("SJ", "ผู้พิทักษ์", "Sentinels", "เป็นระเบียบ · ไว้ใจได้ · ใส่ใจคนรอบตัว", "คลาสสิก ไว้ใจได้ทุกวัน", "#5d7a2a", "#ebf0db", "sj", [
        ("ISTJ", "นักคำนวณ", "Logistician", ["เป๊ะ", "ตรงต่อเวลา", "ซื่อสัตย์"], "matcha_latte", "Matcha Latte (Whisked Milk)", "มัทฉะลาเต้ตีนมราดนม", "79.-", "8g", "เมนูเดิม หวานเดิม สาขาเดิม ทุกวัน"),
        ("ISFJ", "ผู้ปกป้อง", "Defender", ["ใส่ใจรายละเอียด", "ขี้เกรงใจ", "ดูแลคนที่รัก"], "hojicha_latte", "Hojicha Latte", "โฮจิฉะลาเต้ ตีนมราดนม", "79.-", "5g", "ซื้อแก้วตัวเองแล้ว ต้องซื้อฝากที่บ้านด้วย"),
        ("ESTJ", "ผู้บริหาร", "Executive", ["เป็นระเบียบ", "ตรงไปตรงมา", "ทำงานไว"], "cold_whisked", "Cold Whisked Latte", "มัทฉะตีน้ำสไตล์ญี่ปุ่น", "59.-", "5g", "ตีสด เร็ว คุ้ม แล้วไปทำงานต่อ"),
        ("ESFJ", "กงสุล", "Consul", ["เข้าสังคมเก่ง", "อบอุ่น", "จำทุกคนได้"], "strawberry", "Matcha Strawberry Latte", "มัทฉะลาเต้สตรอว์เบอร์รีสด", "89.-", "10g", "แก้วที่ทั้งแก๊งชอบ จำได้ว่าใครหวานเท่าไหร่"),
    ]),
    ("SP", "นักสำรวจ", "Explorers", "ลงมือก่อน · ชอบของใหม่ · ใช้ชีวิตตอนนี้", "ของใหม่ ต้องได้ลองก่อน", "#a06b17", "#f5ecd8", "sp", [
        ("ISTP", "ช่างฝีมือ", "Virtuoso", ["ใจเย็น", "ชอบลงมือทำ", "สาย texture"], "kokoro_honeycomb", "Kokoro Hojicha Honeycomb Velvet", "โฮจิฉะฮันนี่คอมบ์", "159.-", "5g", "กรุบ ๆ honeycomb เคี้ยวไปคิดไป"),
        ("ISFP", "นักผจญภัย", "Adventurer", ["มีสไตล์", "รักความสวยงาม", "ตามใจตัวเอง"], "mango_pandan", "Matcha Mango Pandan Cloud", "มัทฉะมะม่วงใบเตย", "Signature", "8g", "เลือกแก้วจากสี เลือกโต๊ะจากแสง"),
        ("ESTP", "ผู้ประกอบการ", "Entrepreneur", ["กล้าเสี่ยง", "ลุยก่อนคิด", "พลังเยอะ"], "pistachio", "Pistachio Kunafeh Matcha Luxe", "พิสตาชิโอคูนาเฟห์", "Signature", "8g", "เห็นเมนูใหม่ปุ๊บ สั่งปั๊บ ไม่อ่านต่อ"),
        ("ESFP", "ผู้มอบความบันเทิง", "Entertainer", ["สายปาร์ตี้", "ชอบเป็นจุดสนใจ", "สนุกทุกโมเมนต์"], "kokoro_cheesecake", "Kokoro Hojicha Cheesecake Mochi", "โฮจิฉะชีสเค้กโมจิ", "179.-", "10g", "มีโมจิเสียบไม้! ไลฟ์ก่อนกิน"),
    ]),
]

GCSS = """
.hd{position:absolute;top:92px;left:56px;width:610px}
.hd .code{font-family:'Prompt';font-weight:700;font-size:118px;line-height:.95;letter-spacing:-3px}
.hd .nm{font-family:'Prompt';font-weight:600;font-size:46px;line-height:1.1;margin-top:6px}
.hd .nm small{font-size:24px;font-weight:500;opacity:.6;margin-left:10px;letter-spacing:.5px}
.hd .kw{display:inline-block;margin-top:12px;font-family:'Prompt';font-weight:500;font-size:22px;padding:6px 16px;border-radius:24px}
.hd .tg{font-size:23px;color:#4a5a43;margin-top:10px}
.list{position:absolute;top:404px;left:48px;right:48px;display:flex;flex-direction:column;gap:14px}
.row{height:200px;border-radius:30px;background:rgba(255,255,255,.94);position:relative;display:flex;align-items:center;box-shadow:0 10px 26px rgba(36,62,27,.08)}
.row .pic{width:190px;height:200px;flex:none;border-radius:30px 0 0 30px;display:flex;align-items:center;justify-content:center;position:relative}
.row .pic img{max-height:184px;max-width:170px}
.row .tx{flex:1;padding:14px 22px 12px 22px;min-width:0}
.row .l1{display:flex;align-items:baseline;gap:12px}
.row .mb{font-family:'Prompt';font-weight:700;font-size:44px;line-height:1;letter-spacing:-.5px}
.row .nick{font-family:'Prompt';font-weight:600;font-size:25px;color:#1d2b18}
.row .nick small{font-weight:400;font-size:18px;color:#7b8a72;margin-left:4px}
.row .tr{display:flex;gap:6px;margin-top:9px}
.row .tr span{font-family:'Prompt';font-size:16.5px;font-weight:500;padding:3px 11px;border-radius:14px}
.row .en{font-family:'Prompt';font-weight:600;font-size:22px;line-height:1.2;margin-top:10px;color:#1d2b18;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.row .en small{font-family:'Plex';font-weight:400;font-size:17px;color:#66745e;margin-left:8px}
.row .q{font-size:19px;line-height:1.3;margin-top:5px;color:#3a4a33}
.row .tags{position:absolute;right:18px;top:16px;display:flex;gap:7px}
.team{position:absolute;right:16px;bottom:14px;display:inline-flex;align-items:center;gap:7px;font-family:'Prompt';font-weight:500;font-size:17px;padding:3px 13px 3px 3px;border-radius:24px}
.price{font-family:'Prompt';font-weight:600;font-size:22px;color:#fff;border-radius:22px;padding:3px 14px}
.sweet{font-family:'Prompt';font-weight:500;font-size:17px;border-radius:22px;padding:5px 12px;color:#243e1b}
"""

def group_slide(n, g):
    code, name, ename, kw, tag, col, tint, art, items = g
    rows = ""
    for t, nick, enick, traits, a, en, th, price, sw, q in items:
        team = (f'<span class="team" style="background:#e3eedb;color:#243e1b">{avatar("H",30)}ทีม Hibi</span>' if t[0] == "E"
                else f'<span class="team" style="background:#f4ead9;color:#6f4529">{avatar("C",30)}ทีม Capy</span>')
        swtxt = sw if not sw.endswith("g") else f"หวาน {sw}"
        trs = "".join(f'<span style="background:{tint};color:{col}">{x}</span>' for x in traits)
        rows += f"""<div class="row"><div class="pic" style="background:{tint}"><img class="cut" src="{img(a)}"></div>
<div class="tx"><div class="l1"><span class="mb" style="color:{col}">{t}</span><span class="nick">{nick}<small>{enick}</small></span></div>
<div class="tr">{trs}</div>
<div class="en">{en}<small>{th}</small></div><div class="q">“{q}”</div></div>
<div class="tags"><span class="sweet" style="background:{tint}">{swtxt}</span><span class="price" style="background:{col};{'font-size:17px;padding:5px 12px' if not price.endswith('.-') else ''}">{price}</span></div>{team}</div>"""
    body = f"""<div class="hd"><div class="code" style="color:{col}">{code}</div>
<div class="nm" style="color:{col}">{name}<small>{ename}</small></div>
<div class="kw" style="background:{col};color:#fff">{kw}</div>
<div class="tg">🍵 สายมัทฉะแบบนี้: {tag}</div></div>
<img class="art" src="{ART(art)}" style="right:34px;top:64px;width:350px;height:350px;object-fit:contain">
<div class="list">{rows}</div>"""
    return page(n, body, GCSS)

XCSS = """
.h1{position:absolute;top:92px;left:0;right:0;text-align:center;font-family:'Prompt';font-weight:700;font-size:84px;color:#243e1b;line-height:1.05}
.h2{position:absolute;top:196px;left:0;right:0;text-align:center;font-size:27px;color:#3f5236}
.lab{position:absolute;top:470px;font-family:'Prompt';font-weight:600;font-size:22px;padding:6px 16px;border-radius:24px;box-shadow:0 6px 16px rgba(0,0,0,.08)}
.pairs{position:absolute;top:540px;left:48px;right:48px;display:flex;flex-direction:column;gap:12px}
.pr{height:118px;background:rgba(255,255,255,.94);border-radius:26px;display:flex;align-items:center;padding:0 22px;box-shadow:0 8px 22px rgba(36,62,27,.07)}
.pr .s{flex:1;display:flex;align-items:center;gap:14px}
.pr .s.r{flex-direction:row-reverse;text-align:right}
.pr .L{width:74px;height:74px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font-family:'Prompt';font-weight:700;font-size:40px;color:#fff}
.pr .w{font-family:'Prompt';font-weight:600;font-size:24px;color:#1d2b18;line-height:1.15}
.pr .d{font-size:18px;color:#5b6a53;line-height:1.3;margin-top:2px}
.pr .vs{font-family:'Prompt';font-weight:600;font-size:18px;color:#9aa892;padding:0 10px}
.grp{position:absolute;top:1080px;left:48px;right:48px}
.grp .t{font-family:'Prompt';font-weight:600;font-size:22px;color:#243e1b;margin-bottom:10px}
.grp .g{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.grp .c{border-radius:20px;padding:12px 14px;color:#fff;font-family:'Prompt'}
.grp .c b{font-size:30px;font-weight:700;display:block;line-height:1}
.grp .c span{font-size:17px;opacity:.95}
"""

def explain():
    pairs = [("E", "Extrovert · ชาร์จพลังจากคน", "เจอเพื่อนแล้วสดชื่น", "#4e7c3a", "I", "Introvert · ชาร์จพลังคนเดียว", "ขออยู่เงียบ ๆ กับแก้วโปรด", "#a8744a"),
             ("S", "Sensing · ดูของจริงตรงหน้า", "เชื่อสิ่งที่เห็นและลองแล้ว", "#5d7a2a", "N", "Intuition · มองภาพรวม/อนาคต", "ชอบไอเดียใหม่ ๆ", "#243e1b"),
             ("T", "Thinking · ใช้เหตุผล", "ตัดสินจากข้อมูล", "#243e1b", "F", "Feeling · ใช้ความรู้สึก", "ตัดสินจากใจและคนรอบตัว", "#4e7c3a"),
             ("J", "Judging · ชอบวางแผน", "รู้แล้วว่าจะสั่งอะไร", "#5d7a2a", "P", "Perceiving · ยืดหยุ่น", "ไปถึงร้านค่อยเลือก", "#a06b17")]
    rows = "".join(f"""<div class="pr"><div class="s"><div class="L" style="background:{c1}">{a}</div><div><div class="w">{w1}</div><div class="d">{d1}</div></div></div>
<div class="vs">VS</div><div class="s r"><div class="L" style="background:{c2}">{b}</div><div><div class="w">{w2}</div><div class="d">{d2}</div></div></div></div>"""
                   for a, w1, d1, c1, b, w2, d2, c2 in pairs)
    gs = "".join(f'<div class="c" style="background:{c}"><b>{k}</b><span>{t} · สไลด์ {i}</span></div>'
                 for k, t, c, i in [("NT", "นักวิเคราะห์", "#243e1b", 3), ("NF", "นักการทูต", "#4e7c3a", 4), ("SJ", "ผู้พิทักษ์", "#5d7a2a", 5), ("SP", "นักสำรวจ", "#a06b17", 6)])
    body = f"""<div class="h1">MBTI อ่านยังไง?</div><div class="h2">4 ตัวอักษร = 4 คู่นิสัย · เลือกฝั่งที่ “ใช่” ที่สุดของแต่ละคู่</div>
<img class="art" src="{ART('explain')}" style="left:190px;top:240px;width:700px;height:300px;object-fit:contain">
<div class="lab" style="left:120px;background:#e3eedb;color:#243e1b">E = ทีม Hibi 🐰</div>
<div class="lab" style="right:120px;background:#f4ead9;color:#6f4529">I = ทีม Capy 🍊</div>
<div class="pairs">{rows}</div>
<div class="grp"><div class="t">รวมเป็น 4 กลุ่มใหญ่ (ปัดไปหาของคุณ 👉)</div><div class="g">{gs}</div></div>"""
    return page(2, body, XCSS)

SWEET = """
.h1{position:absolute;top:100px;left:56px;font-family:'Prompt';font-weight:700;font-size:80px;color:#243e1b;line-height:1.05}
.h2{position:absolute;top:200px;left:58px;width:640px;font-size:25px;color:#3f5236;line-height:1.35}
.bar{position:absolute;top:330px;left:48px;right:48px;background:rgba(255,255,255,.95);border-radius:32px;padding:30px 26px 24px;box-shadow:0 10px 26px rgba(36,62,27,.08)}
.track{height:16px;border-radius:8px;background:linear-gradient(90deg,#d9ebcb,#243e1b);margin:0 50px 16px}
.dots{display:flex;justify-content:space-between}
.dt{width:155px;text-align:center}
.dt .c{width:88px;height:88px;border-radius:50%;margin:0 auto;display:flex;align-items:center;justify-content:center;font-family:'Prompt';font-weight:600;font-size:29px;color:#fff;box-shadow:0 6px 14px rgba(36,62,27,.15)}
.dt .l{font-family:'Prompt';font-weight:500;font-size:19px;margin-top:10px}
.dt .m{font-size:17px;color:#4e7c3a;margin-top:4px;line-height:1.3}
.cards{position:absolute;top:670px;left:48px;right:48px;display:grid;grid-template-columns:1fr 1fr;gap:20px}
.cd{background:rgba(255,255,255,.95);border-radius:30px;padding:26px 28px;height:410px;box-shadow:0 10px 26px rgba(36,62,27,.08)}
.cd h3{font-family:'Prompt';font-weight:600;font-size:30px;color:#243e1b;margin-bottom:10px}
.cd .r{display:flex;justify-content:space-between;font-size:23px;padding:11px 0;border-bottom:1px solid #edf3e7}
.cd.dk{background:#243e1b;color:#fff}.cd.dk h3{color:#fff;display:flex;align-items:center;gap:12px}
.cd.dk p{font-size:21px;line-height:1.45;margin-bottom:12px}
.save{position:absolute;top:1104px;left:48px;right:48px;height:76px;border-radius:24px;border:3px dashed #4e7c3a;background:rgba(255,255,255,.6);display:flex;align-items:center;justify-content:center;font-family:'Prompt';font-weight:600;font-size:29px;color:#243e1b}
"""

def sweet():
    lv = [("0g", "ไม่หวานเลย", "INTJ", "#bcd9a6"), ("3g", "หวานถึงรสชาติ", "INTP · INFJ", "#9cc683"), ("5g", "หวานเล็กน้อย", "ISFJ · ESTJ\nENTJ · ISTP", "#7fb064"),
          ("8g", "หวานปกติ", "ISTJ · ISFP\nESTP", "#619447"), ("10g", "หวานชื่นใจ", "ENFP · ESFJ\nESFP", "#467334"), ("15g", "หวานจัดเต็ม", "สายหวานจัด", "#243e1b")]
    dots = "".join(f'<div class="dt"><div class="c" style="background:{c}">{g}</div><div class="l">{l}</div><div class="m">{m.replace(chr(10),"<br>")}</div></div>' for g, l, m, c in lv)
    milk = "".join(f'<div class="r"><span>{a}</span><b class="P" style="font-weight:600">{b}</b></div>' for a, b in [("นมสด", "ฟรี"), ("Lactose Free", "+10.-"), ("Oat Milk", "+20.-"), ("Almond Milk", "+25.-")])
    body = f"""<div class="h1">สั่งหวานแค่ไหนดี?</div><div class="h2">ระดับความหวานของ Hibi เลือกได้ทุกแก้ว<br>(ยกเว้นเมนูสูตรคงที่) · ดู MBTI ของคุณใต้แต่ละระดับ</div>
<img class="art" src="{ART('sweet')}" style="right:40px;top:70px;width:290px;height:290px;object-fit:contain">
<div class="bar"><div class="track"></div><div class="dots">{dots}</div></div>
<div class="cards"><div class="cd"><h3>🥛 เปลี่ยนนมได้</h3>{milk}</div>
<div class="cd dk"><h3>{avatar("C",46)}Capy แนะนำ</h3><p>🍵 มือใหม่เริ่ม 5–8g จะได้กลิ่นมัทฉะชัด</p><p>☁️ Cloud Latte / Cream Cheese / Thai Tea × Matcha เป็นสูตรคงที่</p><p>✨ อยากนุ่มขึ้น เพิ่ม Velvet Milk Foam หรือ Milk Mochi</p></div></div>
<div class="save">📌 เซฟสไลด์นี้ไว้ ก่อนสั่งครั้งหน้า</div>"""
    return page(7, body, SWEET)

END = """
.h1{position:absolute;top:96px;left:0;right:0;text-align:center;font-family:'Prompt';font-weight:700;font-size:96px;color:#243e1b;line-height:1.05}
.h2{position:absolute;top:212px;left:0;right:0;text-align:center;font-size:29px;color:#3f5236}
.box{position:absolute;top:640px;left:110px;right:110px;background:#fff;border-radius:30px;padding:26px 34px;box-shadow:0 10px 26px rgba(36,62,27,.09)}
.box .k{font-size:21px;color:#66745e}
.box .v{font-family:'Prompt';font-weight:600;font-size:38px;color:#243e1b;margin-top:4px}
.tag{position:absolute;top:830px;left:0;right:0;text-align:center;font-family:'Prompt';font-weight:600;font-size:31px;color:#4e7c3a}
.br{position:absolute;top:915px;left:48px;right:48px;background:#243e1b;color:#fff;border-radius:30px;padding:26px 30px;text-align:center}
.br .t{font-family:'Prompt';font-weight:600;font-size:28px}
.br .l{font-size:22px;margin-top:8px;line-height:1.5;opacity:.95}
.br .d{font-size:20px;margin-top:8px;color:#cfe6bd}
.disc{position:absolute;top:1214px;left:0;right:0;text-align:center;font-size:17px;color:#7b8a72}
"""

def end():
    body = f"""<div class="h1">คุณคือ MBTI ไหน?</div><div class="h2">บอก Hibi &amp; Capy ในคอมเมนต์หน่อย 👇</div>
<img class="art" src="{ART('end')}" style="left:170px;top:268px;width:740px;height:360px;object-fit:contain">
<div class="box"><div class="k">พิมพ์แบบนี้เลย</div><div class="v">“INFP · ทีม Capy · Osmanthus”</div></div>
<div class="tag">แท็กเพื่อนที่เป็น ENFP ตัวจริง 😆</div>
<div class="br"><div class="t">📍 Hibi Matcha Cafe 5 สาขา</div>
<div class="l">ลาดพร้าว 107 · นาคนิวาส 48 · สะพานควาย · นวมินทร์ 111 · สามย่าน (จุฬาฯ 11)</div>
<div class="d">สั่ง Delivery: LINE MAN · Grab · ShopeeFood</div></div>
<div class="disc">*เพื่อความสนุก ไม่ใช่แบบทดสอบบุคลิกภาพจริง · เมนูและราคาอาจต่างกันในแต่ละสาขา</div>"""
    return page(8, body, END)

# slide 1 (ปก) สร้างด้วย cover_src/build_cover.py
slides = {2: explain(), 3: group_slide(3, GROUPS[0]), 4: group_slide(4, GROUPS[1]), 5: group_slide(5, GROUPS[2]),
          6: group_slide(6, GROUPS[3]), 7: sweet(), 8: end()}
for n, html in slides.items():
    p = f"{OUT}/s{n}.html"; open(p, "w").write(html)
    png = f"{OUT}/HIBI_MBTI_{n:02d}.png"
    subprocess.run(["/opt/pw-browsers/chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--virtual-time-budget=4000", "--force-device-scale-factor=1",
                    f"--screenshot={png}", "--window-size=1080,1500", "file://" + p], check=True, capture_output=True)
    Image.open(png).crop((0, 0, 1080, 1350)).convert("RGB").save(png.replace(".png", ".jpg"), quality=95)
    os.remove(png)
print("done")
