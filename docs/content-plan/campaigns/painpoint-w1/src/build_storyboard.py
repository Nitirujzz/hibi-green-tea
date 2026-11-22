"""Storyboard: Pain-point week 1 · P1 'มัทฉะไม่ได้ต้องขม' + P4 'หวาน 0g–15g' (reuses Matcha Lab #1 page CSS)."""
import subprocess, os
from PIL import Image
_src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../../matcha-lab-01-shade/src/build_storyboard.py"),encoding="utf-8").read()
exec(_src.split("SH=[")[0])
CSS+=""".vo{background:#eef4ff;color:#26406b} .p .ost{top:10%} .tagp{display:inline-block;font-family:Prompt;font-weight:700;font-size:17px;padding:2px 10px;border-radius:10px;color:#fff;margin-bottom:4px}"""
img=lambda f:f"url('file://{F}/{f}.png')"
# (no, time, title, frame, picture, camera, sound, on-screen text, footage note)
P1=[(1,"0:00–0:02","HOOK","f01","คนจิบมัทฉะร้อนแล้วหน้าเหย","Close-up · ซูมกระแทกตอนหน้าเหย","“อึ๋ย” + บีตเริ่ม","มัทฉะไม่ได้ต้องขม…<br>คุณแค่เจอแก้วที่ชงพลาด","🎥 ถ่ายจริง: พนักงาน/ลูกค้าแสดง (ขออนุญาต)"),
    (2,"0:02–0:05","แก้วไหนขม?","f02","2 ถ้วย: ซ้ายเหลืองขุ่นมีก้อน · ขวาเขียวฟองเนียน","Top-down · ซูมเข้าซ้าย→ขวา","“ติ๊ง”","แก้วไหนขม? 👀","🎥 ถ่ายจริงได้ (ตั้งใจชงพลาด 1 ถ้วย)"),
    (3,"0:05–0:09","① น้ำเดือด","f03","เทน้ำเดือดไอพุ่งลงผงชา","Close · slow-mo","เสียงน้ำเดือด","① น้ำเดือด ❌<br>ใช้ 70–80°C ✅","🎥 ถ่ายจริง + ตัวเลขอุณหภูมิ"),
    (4,"0:09–0:13","② ผงจับก้อน","f04","ร่อนผงผ่านตะแกรง ผงร่วงเหมือนหิมะ","Macro · slow-mo","เสียงร่อน ASMR","② ไม่ร่อน = จับก้อน<br>ร่อนก่อนชง ✅","🎥 ถ่ายจริง ASMR"),
    (5,"0:13–0:17","③ ตีไม่ทั่ว","f05","ตีแปรงซิกแซกตัว M ฟองเนียน","Top-down · speed ramp","เสียงตีแปรง","③ ตีวนเป็นวงกลม ❌<br>ตีตัว M 15–20 วิ ✅","🎥 ถ่ายจริง (บาริสต้า)"),
    (6,"0:17–0:22","ยังกลัวขม?","f06","ยิ้มหลังจิบมัทฉะลาเต้","Medium · push-in","เพลงสดใสขึ้น","ยังกลัวขม?<br>ลองลาเต้ หวาน 3–5g ก่อน","🎥 ถ่ายจริง + แก้วจริงของร้าน"),
    (7,"0:22–0:25","จบ + คำถาม","f02","การ์ดคำถามบนภาพเบลอ","ภาพนิ่ง","—","คุณเคยเจอมัทฉะขมแบบไหน?<br>คอมเมนต์ 1 / 2 / 3 👇","กราฟิก")]
P4=[(1,"0:00–0:02","HOOK","f07","6 แก้วหน้าตาเหมือนกันเรียงแถว","Wide · ซูมกระแทก","บีตเริ่ม","หวาน 0g ถึง 15g<br>ต่างกันแค่ไหน? 🤔","🎥 ถ่ายจริง 6 แก้ว (ชงจริงทุกระดับ)"),
    (2,"0:02–0:09","ป้ายเด้งทีละแก้ว","f07","แพนทีละแก้ว ป้ายตัวเลขเด้ง","Pan ซ้าย→ขวา · 1.1 วิ/แก้ว","“ป๊อป” × 6","0g ไม่หวานเลย · 3g หวานถึงรสชาติ<br>5g หวานเล็กน้อย · 8g หวานปกติ<br>10g หวานชื่นใจ · 15g หวานจัดเต็ม","กราฟิก (ระดับหวานจริงของร้าน)"),
    (3,"0:09–0:12","ไม่แน่ใจ?","f08","มือหยิบ 1 แก้วออกจากแถว","Close · push-in","“ติ๊ง”","ไม่แน่ใจ? เริ่ม 5g<br>แล้วค่อยปรับครั้งหน้า","🎥 ถ่ายจริง"),
    (4,"0:12–0:15","จบ + คำถาม","f07","การ์ดตัวเลขให้เลือก","ภาพนิ่ง","—","คุณสั่งกี่กรัม?<br>คอมเมนต์ตัวเลข 0–15 👇","กราฟิก")]
HOOKS={"P1":[("A","ความเชื่อผิด","มัทฉะไม่ได้ต้องขม… คุณแค่เจอแก้วที่ชงพลาด"),("B","ความผิดพลาด","3 อย่างที่ทำให้มัทฉะขม ข้อ 1 คนทำกันทุกบ้าน"),("C","POV","POV: คนเกลียดมัทฉะ จิบแก้วนี้ครั้งแรก")],
       "P4":[("A","ตัวเลข","หวาน 0g ถึง 15g ต่างกันแค่ไหน? ดูทีเดียวจบ"),("B","คำถาม","คุณสั่งหวานกี่กรัม? ส่วนใหญ่สั่งผิดระดับ"),("C","ความผิดพลาด","อย่าสั่ง ‘หวานน้อย’ ถ้ายังไม่รู้ว่าน้อยของร้านคือกี่กรัม")]}
def panel(s):
    n,tc,tt,f,a,cam,snd,ost,note=s
    blur=' ;filter:blur(6px) brightness(1.05)' if (tt.startswith("จบ")) else ''
    return (f'<div class="p"><div class="im" style="background-image:{img(f)}{blur}"></div>'
                        f'<div class="tx"><div class="tt">{n:02d} · {tt} <span style="font-size:17px;color:#6b6a55">{tc}</span></div><div>{a}</div>'
            f'<div class="k"><b>🎥</b><span>{cam}</span></div><div class="k"><b>🔊</b><span>{snd}</span></div>'
            f'<div class="vo" style="font-family:Prompt;font-weight:600">🅣 {ost.replace("<br>"," / ")}</div><div style="font-size:15px;color:#6b6a55;margin-top:6px">{note}</div></div></div>')
def page(name,body):
    p=f"{O}/{name}.html"; open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files",
        "--virtual-time-budget=4000",f"--screenshot={O}/{name}_raw.png",f"--window-size={W},{H+150}","file://"+p],check=True,capture_output=True)
    Image.open(f"{O}/{name}_raw.png").crop((0,0,W,H)).convert("RGB").save(f"{O}/{name}.jpg",quality=92); os.remove(f"{O}/{name}_raw.png"); os.remove(p)
HD=lambda t,pg:(f'<div class="hd"><h1>{t}</h1><div class="meta">Storyboard · Short Video 9:16 · Pain-point สัปดาห์ 1<span class="pill">หน้า {pg}/3</span></div></div>')
FT='<div class="ft"><span>Pain-point W1 · Storyboard v1 · 23 พ.ย. 2026</span><span>ภาพประกอบ: Higgsfield (ภาพตัวอย่าง → ถ่ายจริงแทนตามโน้ต 🎥)</span></div>'
def hookbox(k,title,dur,why):
    rows="".join(f'<div style="display:flex;gap:12px;align-items:flex-start;margin-top:10px"><span class="tagp" style="background:{c}">{a}</span><div><div style="font-size:15px;color:#6b6a55">{t}</div><div style="font-family:Prompt;font-weight:600;font-size:23px;line-height:1.3">“{h}”</div></div></div>'
                 for (a,t,h),c in zip(HOOKS[k],["#3f8f3a","#e0a526","#7a2a44"]))
    return (f'<div class="p" style="padding:24px 26px"><div class="tt" style="font-size:30px">{title}</div><div style="font-size:19px;color:#6b6a55">{dur}</div>'
            f'<div style="font-size:19px;margin-top:8px;line-height:1.45">{why}</div><div style="margin-top:10px;font-family:Prompt;font-weight:700;font-size:21px;color:#4e7c3a">Hook 3 แบบ (ทดสอบ A/B)</div>{rows}</div>')
thumbs=lambda S:"".join(f'<div style="flex:1"><div style="aspect-ratio:9/16;border-radius:10px;background:{img(s[3])} center/cover"></div><div style="font-size:13px;text-align:center;margin-top:4px">{s[0]:02d} {s[2]}</div></div>' for s in S)
cover=HD("Pain-point คลิปสั้น · สัปดาห์ 1",1)+f'''
<div class="row" style="top:160px">
 {hookbox("P1","P1 · มัทฉะไม่ได้ต้องขม","~25 วิ · ความรู้ + ร้าน","ลูกค้ากลัวขมจนไม่กล้าลอง → ชี้ 3 สาเหตุที่แก้ได้ แล้วชวนเริ่มจากลาเต้หวาน 3–5g")}
 {hookbox("P4","P4 · หวาน 0g–15g ต่างกันแค่ไหน","~15 วิ · ช่วยเลือก","คนสั่ง “หวานน้อย” แล้วไม่ถูกใจ → โชว์ 6 ระดับจริงของร้าน แล้วชวนคอมเมนต์ตัวเลข")}
 <div class="p" style="padding:24px 26px;font-size:19px;line-height:1.5"><div class="tt" style="font-size:28px">📐 สูตรที่ใช้</div>
  <div>• วิแรก: ภาพเคลื่อนไหว + ตัวหนังสือ ≤ 8 คำ</div><div>• พูดกับ “คุณ” · สัญญาคำตอบแล้วเฉลยจริง</div><div>• ตัดทุก 2–4 วิ · ตัวหนังสือใน safe zone</div><div>• จบด้วยคำถามที่ตอบได้ 1 คำ/ตัวเลข</div>
  <div style="margin-top:10px;padding:10px 14px;border-radius:14px;background:#fff3c4"><b>A/B:</b> TikTok ใช้ Hook A · IG ใช้ Hook B<br>ดู “% ดูเกิน 3 วิ” หลัง 48 ชม. → เก็บแบบที่ชนะ</div>
  <div style="margin-top:10px;padding:10px 14px;border-radius:14px;background:#ecf8e6"><b>⚠️</b> ไม่อ้างสุขภาพ · ระดับหวานตามเมนูจริง · คนในคลิปต้องขออนุญาต</div></div>
</div>
<div style="position:absolute;left:80px;right:80px;top:850px;display:flex;gap:10px">{thumbs(P1)}<div style="width:30px"></div>{thumbs(P4)}</div>'''+FT
page("SB_01_overview",cover)
page("SB_02_P1",HD("P1 · มัทฉะไม่ได้ต้องขม (~25 วิ)",2)+'<div class="row" style="gap:14px">'+"".join(panel(s) for s in P1)+'</div>'+FT)
notes=('<div class="p" style="padding:22px 20px;font-size:18.5px;line-height:1.5;background:#fbfdf6"><div class="tt" style="font-size:26px">📝 การผลิต</div>'
 '<div><b>แนะนำ:</b> ถ่ายจริงในร้าน 1 รอบ (~40 นาที) ใช้ได้ทั้ง 2 คลิป</div>'
 '<div style="margin-top:8px"><b>ช็อตที่ต้องถ่าย:</b> หน้าเหย/ยิ้ม · ถ้วยดี vs พลาด · เทน้ำเดือด · ร่อน · ตีตัว M · 6 แก้วระดับหวาน · มือหยิบแก้ว</div>'
 '<div style="margin-top:8px"><b>ถ้ายังไม่มีฟุตเทจ:</b> ใช้ภาพ AI ชุดนี้ + Seedance ขยับ ~8 ช็อต (~550 เครดิต) แล้วแทนด้วยของจริงทีหลัง</div>'
 '<div style="margin-top:8px"><b>ตัดต่อ:</b> ตัวหนังสือเด้งตามบีต · เพลงสดใสที่แต่งเอง · ไม่มีเสียงพากย์ (หรือพนักงานพูดเองได้)</div></div>')
page("SB_03_P4",HD("P4 · หวาน 0g–15g ต่างกันแค่ไหน (~15 วิ)",3)+'<div class="row" style="gap:14px">'+"".join(panel(s) for s in P4)+notes+'</div>'+FT)
ims=[Image.open(f"{O}/{n}.jpg").convert("RGB") for n in ["SB_01_overview","SB_02_P1","SB_03_P4"]]
ims[0].save(f"{O}/PainPoint_W1_P1_P4_Storyboard.pdf",save_all=True,append_images=ims[1:],resolution=150); print("ok")
