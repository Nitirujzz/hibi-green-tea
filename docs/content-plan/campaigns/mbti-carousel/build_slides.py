import os, subprocess, base64
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, "out"); os.makedirs(OUT, exist_ok=True)

def img(name):
    return "data:image/png;base64," + base64.b64encode(open(f"{D}/assets/{name}.png", "rb").read()).decode()

FONTS = "".join(
    f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file:///root/.fonts/{f}-{w}-{s}.woff2') format('woff2');}}"
    for fam, f in [("Prompt", "Prompt"), ("Plex", "IBMPlexSansThai")]
    for w in ([400, 500, 600, 700] if f == "Prompt" else [400, 600])
    for s in ["thai", "latin"]
)

CAPY = """<svg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
<ellipse cx="100" cy="150" rx="72" ry="44" fill="#a8744a"/>
<circle cx="64" cy="58" r="12" fill="#946240"/><circle cx="136" cy="58" r="12" fill="#946240"/>
<ellipse cx="100" cy="98" rx="62" ry="50" fill="#c08a5c"/>
<ellipse cx="100" cy="116" rx="36" ry="24" fill="#a8744a"/>
<rect x="88" y="104" width="24" height="10" rx="5" fill="#4a2f1d"/>
<path d="M70 90 q9 7 18 0" stroke="#3b2416" stroke-width="5" fill="none" stroke-linecap="round"/>
<path d="M112 90 q9 7 18 0" stroke="#3b2416" stroke-width="5" fill="none" stroke-linecap="round"/>
<ellipse cx="62" cy="108" rx="10" ry="6" fill="#f2a99a" opacity=".7"/><ellipse cx="138" cy="108" rx="10" ry="6" fill="#f2a99a" opacity=".7"/>
<path d="M82 30 L118 30 L113 52 L87 52 Z" fill="#f6efe0" stroke="#7a5233" stroke-width="2"/>
<ellipse cx="100" cy="30" rx="18" ry="5" fill="#4e7c3a"/>
</svg>"""

BASE_CSS = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;}body{overflow:hidden;background:#f3fbe9;font-family:'Plex',sans-serif;color:#1f2d1a;position:relative}
.h{font-family:'Prompt',sans-serif}
.foot{position:absolute;left:0;right:0;top:1272px;height:78px;background:#243e1b;color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 48px;font-family:'Prompt';font-size:22px;letter-spacing:.5px}
.foot b{font-weight:500}
.pg{position:absolute;top:36px;right:48px;font-family:'Prompt';font-size:22px;color:#4e7c3a}
.brand{position:absolute;top:36px;left:48px;font-family:'Prompt';font-size:22px;color:#243e1b;letter-spacing:1px}
.capy{width:100%;height:100%}
"""

def page(body, idx, extra_css=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{extra_css}</style></head>
<body><div class="brand">HIBI MATCHA CAFE 日々</div><div class="pg">{idx}/7</div>{body}
<div class="foot"><span><b>16 บุคลิก × Hibi &amp; Capy</b></span><span>@hibimatchacafe</span></div></body></html>"""

def host_badge(t):
    if t[0] == "E":
        return f'<div class="badge" style="background:#4e7c3a"><img src="{img("hibi_logo")}" style="width:100%;height:100%;border-radius:50%"></div>'
    return f'<div class="badge" style="background:#efe3d2">{CAPY}</div>'

GROUPS = [
    ("NT", "นักวิเคราะห์", "ขอของแท้ ไม่ต้องปรุงเยอะ", "#243e1b", [
        ("INTJ", "clear_matcha", "Clear Matcha", "มัทฉะใส · 59.-", "หวาน 0g", "วางแผนมาแล้ว ขอรสมัทฉะแท้ ๆ ไม่ต้องหวาน"),
        ("INTP", "kirei_yuzu", "Kirei Yuzu Matcha", "มัทฉะยูซุคิเรอิ · 79.-", "หวาน 3g", "ยูซุ + มัทฉะ เข้ากันได้ไง… ขอทดลองก่อน"),
        ("ENTJ", "velvet_whisk", "Velvet Matcha Whisk Latte", "Cold Foam · 129.-", "หวาน 5g", "เลือกตัวท็อปของร้าน ไม่เสียเวลาลังเล"),
        ("ENTP", "thai_matcha", "Jasmine Thai Tea × Matcha", "ชาไทย × มัทฉะ · 109.-", "สูตรคงที่", "ชาไทยกับมัทฉะเข้ากันไม่ได้? ขอเถียง!"),
    ]),
    ("NF", "นักการทูต", "หอม ละมุน มีเรื่องราว", "#4e7c3a", [
        ("INFJ", "coconut_jasmine", "Clear Matcha Coconut Jasmine", "มัทฉะใสมะพร้าวมะลิ · 79.-", "หวาน 3g", "หอมมะลิบาง ๆ ลึกหลายชั้น เหมือนใจเรา"),
        ("INFP", "osmanthus", "Osmanthus Honey Coconut", "หอมหมื่นลี้ น้ำผึ้ง มะพร้าว", "ไม่หวานเกิน", "หอมหมื่นลี้ นั่งริมหน้าต่าง ฝันได้ทั้งบ่าย"),
        ("ENFJ", "cloud_latte", "Matcha Cloud Latte", "มัทฉะคลาวด์ลาเต้ · 79.-", "สูตรคงที่", "นุ่มเหมือนเมฆ อุ่นเหมือนคนที่ดูแลทุกคน"),
        ("ENFP", "pink_cloud", "Pink Coconut Cloud", "Pink is Fine · 79.-", "หวาน 10g", "สีชมพู! ถ่าย 30 รูปก่อนจิบคำแรก"),
    ]),
    ("SJ", "ผู้พิทักษ์", "คลาสสิก ไว้ใจได้ทุกวัน", "#5f7a2e", [
        ("ISTJ", "matcha_latte", "Matcha Latte (Whisked Milk)", "มัทฉะลาเต้ตีนมราดนม · 79.-", "หวาน 8g", "เมนูเดิม หวานเดิม สาขาเดิม ทุกวัน"),
        ("ISFJ", "hojicha_latte", "Hojicha Latte", "โฮจิฉะลาเต้ · 79.-", "หวาน 5g", "ซื้อแก้วตัวเองแล้ว ต้องซื้อฝากที่บ้านด้วย"),
        ("ESTJ", "cold_whisked", "Cold Whisked Latte", "มัทฉะตีสไตล์ญี่ปุ่น · 59.-", "หวาน 5g", "ตีสด เร็ว คุ้ม แล้วไปทำงานต่อ"),
        ("ESFJ", "strawberry", "Matcha Strawberry Latte", "มัทฉะสตรอว์เบอร์รีสด · 89.-", "หวาน 10g", "แก้วที่ทั้งแก๊งชอบ จำได้ว่าใครหวานเท่าไหร่"),
    ]),
    ("SP", "นักสำรวจ", "ของใหม่ ต้องได้ลองก่อน", "#a8721c", [
        ("ISTP", "kokoro_honeycomb", "Kokoro Hojicha Honeycomb Velvet", "โฮจิฉะฮันนี่คอมบ์ · 159.-", "หวาน 5g", "กรุบ ๆ honeycomb เคี้ยวไปคิดไป สาย texture"),
        ("ISFP", "mango_pandan", "Matcha Mango Pandan Cloud", "มัทฉะมะม่วงใบเตย", "หวาน 8g", "เลือกแก้วจากสี เลือกโต๊ะจากแสง"),
        ("ESTP", "pistachio", "Pistachio Kunafeh Matcha Luxe", "พิสตาชิโอคูนาเฟห์", "หวาน 8g", "เห็นเมนูใหม่ปุ๊บ สั่งปั๊บ ไม่อ่านต่อ"),
        ("ESFP", "kokoro_cheesecake", "Kokoro Hojicha Cheesecake Mochi", "โฮจิฉะชีสเค้กโมจิ · 179.-", "หวาน 10g", "มีโมจิเสียบไม้! ไลฟ์ก่อนกิน"),
    ]),
]

GROUP_CSS = """
.band{position:absolute;top:96px;left:48px;right:48px;height:150px;border-radius:28px;color:#fff;padding:26px 36px;display:flex;align-items:center;justify-content:space-between}
.band .code{font-family:'Prompt';font-weight:700;font-size:76px;line-height:1}
.band .t1{font-family:'Prompt';font-weight:600;font-size:40px;text-align:right}
.band .t2{font-size:24px;opacity:.9;text-align:right;margin-top:4px}
.grid{position:absolute;top:272px;left:48px;right:48px;display:grid;grid-template-columns:1fr 1fr;gap:24px}
.card{background:#fff;border-radius:26px;height:478px;padding:20px 24px;position:relative;box-shadow:0 6px 18px rgba(36,62,27,.08)}
.ph{height:196px;display:flex;align-items:flex-end;justify-content:center}
.ph img{max-height:192px;max-width:100%;object-fit:contain;mix-blend-mode:multiply}
.mb{font-family:'Prompt';font-weight:700;font-size:50px;line-height:1;margin-top:10px}
.nm{font-family:'Prompt';font-weight:600;font-size:21px;color:#243e1b;margin-top:6px;line-height:1.2;min-height:26px}
.th{font-size:18px;color:#5d6b55;margin-top:2px}
.sw{display:inline-block;margin-top:8px;font-size:17px;padding:3px 12px;border-radius:20px;background:#eef6e6;color:#243e1b}
.ol{font-size:19px;line-height:1.35;margin-top:8px;color:#1f2d1a}
.badge{position:absolute;top:16px;right:16px;width:66px;height:66px;border-radius:50%;padding:4px;overflow:hidden}
.legend{position:absolute;bottom:96px;left:48px;right:48px;font-size:18px;color:#5d6b55;text-align:center}
"""

def group_slide(i, g):
    code, name, tag, color, items = g
    cards = ""
    for t, a, en, th, sw, ol in items:
        cards += f"""<div class="card">{host_badge(t)}<div class="ph"><img src="{img(a)}"></div>
<div class="mb" style="color:{color}">{t}</div><div class="nm">{en}</div><div class="th">{th}</div>
<span class="sw">{sw}</span><div class="ol">“{ol}”</div></div>"""
    body = f"""<div class="band" style="background:{color}"><div class="code">{code}</div>
<div><div class="t1">{name}</div><div class="t2">{tag}</div></div></div>
<div class="grid">{cards}</div>
"""
    return page(body, i, GROUP_CSS)

COVER_CSS = """
.title{position:absolute;top:120px;left:0;right:0;text-align:center}
.kick{display:inline-block;background:#4e7c3a;color:#fff;font-family:'Prompt';font-weight:500;font-size:28px;padding:8px 26px;border-radius:30px}
.big{font-family:'Prompt';font-weight:700;font-size:118px;line-height:1.08;color:#243e1b;margin-top:22px}
.sub{font-size:30px;color:#4e7c3a;margin-top:12px}
.stage{position:absolute;left:40px;right:40px;top:600px;height:440px}
.leaf{position:absolute;left:90px;right:90px;bottom:18px;height:110px;background:#4e7c3a;border-radius:50%;z-index:0}
.cups{position:absolute;left:0;right:0;bottom:52px;display:flex;justify-content:center;align-items:flex-end;gap:6px}
.cups img{height:250px;mix-blend-mode:multiply}
.chr{position:absolute;bottom:10px;width:180px;height:180px;z-index:2}
.cta{position:absolute;top:1150px;left:48px;right:48px;height:96px;background:#243e1b;color:#fff;border-radius:24px;display:flex;align-items:center;justify-content:center;font-family:'Prompt';font-weight:500;font-size:34px}
"""

def cover():
    cups = "".join(f'<img src="{img(a)}">' for a in ["clear_matcha", "osmanthus", "matcha_latte", "kokoro_cheesecake"])
    body = f"""<div class="title"><span class="kick">16 บุคลิก × Hibi &amp; Capy</span>
<div class="big h">มัทฉะแก้วไหน<br>คือคุณ?</div><div class="sub">ทาย MBTI จากแก้วโปรด 🍵</div></div>
<div class="stage"><div class="leaf"></div><div class="cups">{cups}</div>
<div class="chr" style="left:0;background:#4e7c3a;border-radius:50%;padding:10px"><img src="{img('hibi_logo')}" style="width:100%;border-radius:50%"></div>
<div class="chr" style="right:0;background:#efe3d2;border-radius:50%;padding:12px">{CAPY}</div></div>
<div class="cta">ปัดหาตัวเอง → แล้วแท็กเพื่อนที่ “ใช่เลย”</div><div style="position:absolute;top:1100px;left:0;right:0;text-align:center;font-size:22px;color:#4e7c3a">Capy ดูแลสาย I (ชิล) · Hibi ดูแลสาย E (พลังเยอะ)</div>"""
    return page(body, 1, COVER_CSS)

SWEET_CSS = """
.hd{position:absolute;top:110px;left:48px;right:48px}
.hd .a{font-family:'Prompt';font-weight:700;font-size:72px;color:#243e1b;line-height:1.1}
.hd .b{font-size:28px;color:#4e7c3a;margin-top:8px}
.bar{position:absolute;top:340px;left:48px;right:48px;background:#fff;border-radius:28px;padding:36px 28px}
.dots{display:flex;justify-content:space-between}
.dot{width:140px;text-align:center}
.dot .c{width:96px;height:96px;border-radius:50%;margin:0 auto;display:flex;align-items:center;justify-content:center;font-family:'Prompt';font-weight:600;font-size:30px;color:#fff}
.dot .l{font-size:19px;margin-top:10px;line-height:1.3}
.dot .m{font-family:'Prompt';font-size:18px;color:#4e7c3a;margin-top:6px}
.milk{position:absolute;top:720px;left:48px;width:470px;background:#fff;border-radius:28px;padding:30px 32px}
.milk h3,.tip h3{font-family:'Prompt';font-weight:600;font-size:30px;color:#243e1b;margin-bottom:14px}
.milk div{display:flex;justify-content:space-between;font-size:24px;padding:8px 0;border-bottom:1px solid #eef3e8}
.tip{position:absolute;top:720px;right:48px;width:470px;background:#243e1b;color:#fff;border-radius:28px;padding:30px 32px}
.tip h3{color:#fff}.tip p{font-size:22px;line-height:1.5;margin-bottom:10px}
.save{position:absolute;bottom:110px;left:48px;right:48px;text-align:center;font-family:'Prompt';font-weight:600;font-size:34px;color:#243e1b}
"""

def sweet():
    lv = [("0g", "ไม่หวานเลย", "INTJ", "#cfe3c0"), ("3g", "หวานถึงรสชาติ", "INTP · INFJ", "#a9cd93"), ("5g", "หวานเล็กน้อย", "ISFJ · ESTJ", "#86b56d"),
          ("8g", "หวานปกติ", "ISTJ · ISFP", "#6a9a50"), ("10g", "หวานชื่นใจ", "ENFP · ESFJ", "#4e7c3a"), ("15g", "หวานในเกิน100", "สายหวานจัด", "#243e1b")]
    dots = "".join(f'<div class="dot"><div class="c" style="background:{c}">{g}</div><div class="l">{l}</div><div class="m">{m}</div></div>' for g, l, m, c in lv)
    milk = "".join(f"<div><span>{a}</span><span>{b}</span></div>" for a, b in [("Milk", "Free"), ("Lactose Free Milk", "+10.-"), ("Oat Milk", "+20.-"), ("Almond Milk", "+25.-")])
    body = f"""<div class="hd"><div class="a">สั่งหวานแค่ไหนดี?</div><div class="b">ระดับความหวานของ Hibi · เลือกได้ทุกแก้ว (ยกเว้นสูตรคงที่)</div></div>
<div class="bar"><div class="dots">{dots}</div></div>
<div class="milk"><h3>เปลี่ยนนมได้</h3>{milk}</div>
<div class="tip"><h3>Capy แนะนำ</h3><p>🍵 มือใหม่เริ่ม 5–8g จะได้กลิ่นมัทฉะชัด</p><p>☁️ Fixed Recipe (Cloud / Cream Cheese / Thai Tea × Matcha) เปลี่ยนสูตรไม่ได้</p><p>✨ เพิ่มท็อปปิ้ง Velvet Milk Foam / Milk Mochi ได้</p></div>
<div class="save">📌 เซฟไว้ก่อนไปสั่งครั้งหน้า</div>"""
    return page(body, 6, SWEET_CSS)

END_CSS = """
.q{position:absolute;top:130px;left:0;right:0;text-align:center}
.q .a{font-family:'Prompt';font-weight:700;font-size:96px;color:#243e1b;line-height:1.1}
.q .b{font-size:32px;color:#4e7c3a;margin-top:16px}
.duo{position:absolute;top:470px;left:0;right:0;display:flex;justify-content:center;gap:60px}
.duo .c{width:260px;height:260px;border-radius:50%}
.bubble{position:absolute;top:780px;left:110px;right:110px;background:#fff;border-radius:30px;padding:30px;text-align:center;font-family:'Prompt';font-weight:500;font-size:34px;color:#243e1b}
.br{position:absolute;top:940px;left:48px;right:48px;text-align:center}
.br .t{font-family:'Prompt';font-weight:600;font-size:28px;color:#243e1b}
.br .l{font-size:24px;color:#1f2d1a;margin-top:10px;line-height:1.5}
.br .d{font-size:22px;color:#4e7c3a;margin-top:10px}
.disc{position:absolute;bottom:96px;left:0;right:0;text-align:center;font-size:18px;color:#7b8a72}
"""

def end():
    body = f"""<div class="q"><div class="a">คุณคือ MBTI ไหน?</div><div class="b">คอมเมนต์บอก Hibi &amp; Capy หน่อย 👇</div></div>
<div class="duo"><div class="c" style="background:#4e7c3a;padding:6px"><img src="{img('hibi_logo')}" style="width:100%;border-radius:50%"></div>
<div class="c" style="background:#efe3d2;padding:22px">{CAPY}</div></div>
<div class="bubble">แท็กเพื่อนที่เป็น ENFP ตัวจริง 😆<br>แล้วชวนมาสั่ง “แก้วของตัวเอง”</div>
<div class="br"><div class="t">📍 Hibi Matcha Cafe 5 สาขา</div>
<div class="l">ลาดพร้าว 107 · นาคนิวาส 48 · สะพานควาย<br>นวมินทร์ 111 · สามย่าน (จุฬาฯ 11)</div>
<div class="d">สั่ง Delivery ได้ทาง LINE MAN · Grab · ShopeeFood</div></div>
<div class="disc">*เพื่อความสนุก ไม่ใช่แบบทดสอบบุคลิกภาพจริง · เมนูอาจต่างกันในแต่ละสาขา</div>"""
    return page(body, 7, END_CSS)

slides = [cover()] + [group_slide(i + 2, g) for i, g in enumerate(GROUPS)] + [sweet(), end()]
for n, html in enumerate(slides, 1):
    p = f"{OUT}/slide{n}.html"; open(p, "w").write(html)
    subprocess.run(["/opt/pw-browsers/chromium", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--allow-file-access-from-files", "--virtual-time-budget=3000",
                    f"--screenshot={OUT}/HIBI_MBTI_S{n:02d}.png", "--window-size=1080,1500", "file://" + p],
                   check=True, capture_output=True)
from PIL import Image
for n in range(1, len(slides)+1):
    f=f"{OUT}/HIBI_MBTI_S{n:02d}.png"; Image.open(f).crop((0,0,1080,1350)).save(f)
print("done")
