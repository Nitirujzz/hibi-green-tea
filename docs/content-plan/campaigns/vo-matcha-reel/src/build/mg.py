"""Motion-graphics layer (transparent 1080x1920 @30fps) for the VO reel.
All cue times are ORIGINAL VO seconds, mapped through timing.m() onto the tightened VO."""
import json, os
from timing import m, total
D=os.path.dirname(os.path.abspath(__file__))
T=total()
FONTS="".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file:///root/.fonts/{f}-{w}-{s}.woff2') format('woff2');}}"
  for fam,f in [("Prompt","Prompt"),("Plex","IBMPlexSansThai")] for w in ([400,500,600,700] if f=="Prompt" else [400,600]) for s in ["thai","latin"])
X='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><circle cx="12" cy="12" r="12" fill="#e5484d"/><path d="M8 8l8 8M16 8l-8 8" stroke="#fff" stroke-width="3" stroke-linecap="round"/></svg>'
V='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><circle cx="12" cy="12" r="12" fill="#3f8f3a"/><path d="M6.5 12.5l3.6 3.6 7.4-8" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>'
PIN='<svg viewBox="0 0 24 24" width="{s}" height="{s}"><path d="M14.5 2l7.5 7.5-2.2.6-3.6 3.6.3 4.6-2.1 2.1-4.2-4.2L4.4 22 2 19.6l5.8-5.8L3.6 9.6l2.1-2.1 4.6.3 3.6-3.6z" fill="#e5484d"/></svg>'
WIND='<svg viewBox="0 0 48 48" width="96" height="96"><path d="M6 18h26a6 6 0 1 0-6-6M6 26h34a6 6 0 1 1-6 6M6 34h16" stroke="#243e1b" stroke-width="4" fill="none" stroke-linecap="round"/></svg>'
SUN='<svg viewBox="0 0 48 48" width="96" height="96"><circle cx="24" cy="24" r="9" fill="#f2b632"/><g stroke="#f2b632" stroke-width="4" stroke-linecap="round"><path d="M24 4v6M24 38v6M4 24h6M38 24h6M10 10l4 4M34 34l4 4M38 10l-4 4M14 34l-4 4"/></g></svg>'
FIRE='<svg viewBox="0 0 48 48" width="96" height="96"><path d="M24 4c2 8 12 12 12 24a12 12 0 0 1-24 0c0-6 3-9 5-12 0 4 2 6 4 6-1-8 1-13 3-18z" fill="#ef6a32"/><path d="M24 26c1 3 5 5 5 9a5 5 0 0 1-10 0c0-3 3-5 5-9z" fill="#ffd166"/></svg>'

CSS=FONTS+"""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;background:transparent;overflow:hidden;font-family:'Prompt'}
.e{position:absolute;opacity:0;will-change:transform}
.card{background:rgba(255,252,244,.95);border-radius:34px;box-shadow:0 14px 34px rgba(0,0,0,.22)}
.hk{left:60px;width:960px;text-align:center;font-weight:700;color:#fff;text-shadow:0 4px 0 #243e1b,0 8px 24px rgba(0,0,0,.45);white-space:nowrap}
.prog{left:70px;top:190px;width:880px;display:flex;gap:12px}
.prog .s{flex:1;height:44px;border-radius:22px;background:rgba(36,62,27,.45);position:relative;overflow:hidden;backdrop-filter:blur(4px)}
.prog .s b{position:absolute;inset:0;width:0;background:#a8d48a}
.prog .s span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:26px;color:#fff;letter-spacing:1px}
.prog .s.done b{width:100%}.prog .s.done span,.prog .s.on span{color:#243e1b}
.hdr{left:70px;top:256px;width:880px;display:flex;align-items:center;gap:26px;padding:20px 30px}
.num{width:104px;height:104px;border-radius:50%;background:#243e1b;color:#fff;font-weight:700;font-size:62px;display:flex;align-items:center;justify-content:center;flex:none}
.ht{font-weight:700;font-size:60px;color:#243e1b;line-height:1.05;white-space:nowrap}.hs{font-family:'Plex';font-weight:600;font-size:28px;color:#c0392b;margin-top:2px}
.tag{left:70px;top:1150px;width:880px;display:flex;align-items:center;gap:22px;padding:26px 32px}
.tag.bad{background:rgba(255,236,234,.96)}.tag.good{background:rgba(236,248,230,.96)}
.tag .t1{font-weight:700;font-size:50px;line-height:1.12;white-space:nowrap}.tag.bad .t1{color:#b3261e}.tag.good .t1{color:#245b1f}
.tag .t2{font-family:'Plex';font-weight:600;font-size:32px;color:#4a4a4a;margin-top:4px;white-space:nowrap}
.big{left:70px;width:880px;text-align:center;font-weight:700;white-space:nowrap}
.chip{padding:14px 30px;border-radius:40px;font-family:'Plex';font-weight:600;font-size:34px;white-space:nowrap}
.warn{left:160px;top:440px;width:760px;text-align:center;background:#ffd23f;color:#3a2a00;font-weight:700;font-size:54px;padding:18px 0;border-radius:24px;box-shadow:0 10px 26px rgba(0,0,0,.25);border:5px solid #3a2a00}
.ico{top:600px;width:150px;height:150px;border-radius:50%;background:#fffaf0;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 24px rgba(0,0,0,.22)}
.flash{left:0;top:0;width:1080px;height:1920px;background:#fff}
.recap{left:70px;top:230px;width:880px;padding:40px 44px 34px}
.recap h1{font-size:64px;font-weight:700;color:#243e1b;line-height:1.1}.recap h2{font-family:'Plex';font-weight:600;font-size:30px;color:#4e7c3a;margin:6px 0 22px}
.row{display:flex;align-items:center;gap:20px;padding:16px 0;border-top:2px dashed #d9e6cf;opacity:0}
.row .n{width:64px;height:64px;border-radius:50%;background:#243e1b;color:#fff;font-weight:700;font-size:36px;display:flex;align-items:center;justify-content:center;flex:none}
.row .a{font-weight:700;font-size:40px;color:#243e1b;line-height:1.1;white-space:nowrap}.row .b{font-family:'Plex';font-size:28px;color:#b3261e;white-space:nowrap}
.save{left:70px;top:1215px;width:880px;display:flex;align-items:center;justify-content:center;gap:16px;background:#243e1b;color:#fff;font-weight:700;font-size:46px;padding:26px 0;border-radius:30px;box-shadow:0 12px 30px rgba(0,0,0,.3)}
.foot{left:70px;top:1355px;width:880px;text-align:center;font-family:'Plex';font-weight:600;font-size:30px;color:#fff;text-shadow:0 2px 10px rgba(0,0,0,.6)}
"""
H=[];CUES=[]
def el(cls,html,a,b,anim="pop",style="",eid=None):
    i=len(CUES);CUES.append(dict(id=f"e{i}",a=round(a,3),b=round(b,3),anim=anim))
    H.append(f'<div id="e{i}" class="e {cls}" style="{style}">{html}</div>');return f"e{i}"

# ---------- HOOK ----------
el("hk","ชงมัทฉะเองแล้ว<span style='color:#ffd23f'>ขม?</span>",m(1.6)-0.1,m(10.3)+0.15,"slam","top:300px;font-size:96px")
el("hk","คุณอาจพลาด <span style='color:#a8d48a;font-size:120px'>5</span> ข้อนี้อยู่",m(5.6),m(10.3)+0.15,"up","top:430px;font-size:76px")
el("chip",PIN.format(s=36)+" เซฟไว้ก่อนชงครั้งหน้า",m(7.4),m(10.3)+0.15,"wobble","left:300px;top:1330px;background:#fffaf0;color:#243e1b;display:flex;gap:10px;align-items:center")

# ---------- SECTIONS ----------
SEC=[(10.9,30.1,"ใช้น้ำเดือด","น้ำร้อนจัด = ดึงความขม"),(30.7,41.5,"ไม่ร่อนผง","ผงจับก้อน ละลายไม่หมด"),
     (42.0,59.7,"ตีวนเป็นวงกลม","ฟองไม่ขึ้น รสไม่เนียน"),(60.8,83.2,"ใส่ผงเยอะเกิน","ไม่เข้มขึ้น แต่ฝาดขึ้น"),(83.7,103.2,"เก็บผงผิดวิธี","อากาศ แสง ความร้อน")]
PROG=dict(a=m(10.9)-0.1,b=m(103.5)-0.1,secs=[(m(a)-0.1,m(b)) for a,b,_,_ in SEC])
H.append('<div id="prog" class="e prog">'+"".join(f'<div class="s"><b></b><span>ข้อ {k+1}</span></div>' for k in range(5))+'</div>')
for k,(a,b,t,s) in enumerate(SEC):
    el("card hdr",f'<div class="num">{k+1}</div><div><div class="ht">{t}</div><div class="hs">✕ ความผิดพลาดที่ทำให้ขม</div></div>',m(a)-0.1,m(b),"slide")
    el("flash","",m(a)-0.12,m(a)+0.1,"flash")

def bad(t1,t2,a,b,top=1150): return el("card tag bad",X.format(s=84)+f'<div><div class="t1">{t1}</div><div class="t2">{t2}</div></div>',a,b,"pop",f"top:{top}px")
def good(t1,t2,a,b,top=1150): return el("card tag good",V.format(s=84)+f'<div><div class="t1">{t1}</div><div class="t2">{t2}</div></div>',a,b,"pop",f"top:{top}px")

# 1 temperature
bad("น้ำเดือด 100°C","ดึงความขมออกมาเต็ม ๆ",m(11.9),m(16.7))
bad("คาเทชินออกมาเยอะ","ยิ่งร้อน ยิ่งขม ยิ่งฝาด",m(16.9),m(24.6))
el("big",'<span id="cnt" style="font-size:190px;color:#fff;text-shadow:0 6px 0 #245b1f,0 10px 30px rgba(0,0,0,.4)">70–80°C</span>',m(24.9),m(29.9),"slam","top:560px")
good("น้ำอุ่น 70–80°C","ไม่มีปรอท? ต้มเดือดแล้วพัก 2–3 นาที",m(25.2),m(29.9))
# 2 sift
bad("ผงจับเป็นก้อน","ละลายไม่หมด เจอเม็ดขมเต็มปาก",m(32.4),m(38.3))
good("ร่อนผ่านตะแกรงทุกครั้ง","ไม่มีตะแกรง? ใช้กระชอนตาถี่แทน",m(38.4),m(41.3))
# 3 whisk
el("warn","⚠ ข้อนี้คนพลาดเยอะที่สุด!",m(42.4),m(46.6),"shake")
bad("ตีวนเป็นวงกลม","ฟองไม่ขึ้น ไม่ได้ฟองเนียนด้านบน",m(47.0),m(51.2))
good("ตีซิกแซกรูปตัว M","เร็ว ๆ ใช้ข้อมือ ~15–20 วิ",m(52.0),m(59.4))
el("","<svg width='620' height='420' viewBox='0 0 620 420'><path id='mpath' d='M40 380 L150 60 L310 300 L470 60 L580 380' fill='none' stroke='#ffd23f' stroke-width='22' stroke-linecap='round' stroke-linejoin='round' stroke-dasharray='1400' stroke-dashoffset='1400' style='filter:drop-shadow(0 6px 10px rgba(0,0,0,.45))'/></svg>",m(52.3),m(59.2),"fade","left:230px;top:560px")
# 4 amount
bad("ใส่ผงพูน ๆ หลายช้อน","คิดว่าจะเข้มขึ้น…",m(62.4),m(68.6))
bad("ไม่ได้เข้มขึ้น แต่ฝาดขึ้น!","ผงเยอะเกิน = ฝาด + ขม",m(68.8),m(70.9))
el("big",'<div style="display:inline-block;background:rgba(255,252,244,.95);border-radius:36px;padding:26px 46px;box-shadow:0 14px 34px rgba(0,0,0,.25)"><span style="font-size:130px;color:#245b1f">2 g</span><span style="font-size:70px;color:#7a9a6a"> : </span><span style="font-size:100px;color:#245b1f">60–70 ml</span><div style="font-family:Plex;font-weight:600;font-size:32px;color:#4a4a4a">ผงมัทฉะ : น้ำ (เริ่มต้นตรงนี้)</div></div>',m(71.1),m(77.3),"slam","top:1080px")
el("chip","ปรับเข้ม–อ่อนได้ตามชอบ ☺",m(77.9),m(83.0),"up","left:250px;top:1180px;background:#fffaf0;color:#243e1b")
# 5 storage
bad("เปิดถุงทิ้งไว้","ข้างเตา · โดนแดด",m(84.0),m(88.6))
for j,(ic,lb) in enumerate([(WIND,"อากาศ"),(SUN,"แสง"),(FIRE,"ความร้อน")]):
    el("ico",ic,m(85.8)+j*0.45,m(95.5),"pop",f"left:{150+j*300}px")
    el("chip",lb,m(85.8)+j*0.45+0.1,m(95.5),"up",f"left:{150+j*300+75}px;top:770px;transform-origin:center;background:#243e1b;color:#fff;translate:-50% 0")
bad("สีหมอง กลิ่นหาย รสขม","ผงมัทฉะเสื่อมเร็วมาก",m(89.0),m(95.5))
good("โถปิดสนิท · ที่เย็น · มืด","เก็บในตู้เย็นยิ่งดี ใช้ให้หมดเร็ว",m(96.1),m(103.0))
# ---------- CTA ----------
el("card big",'<div style="padding:30px 0"><div style="font-size:64px;color:#243e1b">ขี้เกียจชงเอง?</div><div style="font-size:76px;color:#3f8f3a">ให้ Hibi ชงให้ 🍵</div><div style="font-family:Plex;font-weight:600;font-size:32px;color:#4a4a4a;margin-top:6px">ตัก · ร่อน · ตี · เท ทุกขั้นตอนทุกแก้ว</div></div>',m(104.7),m(111.3),"pop","top:300px")
el("foot","📍 Hibi Matcha Cafe ทั้ง 5 สาขา",m(106.7),m(111.3),"up","top:1360px;font-size:40px")
RA=m(111.4)
rows=[("น้ำอุ่น 70–80°C","ไม่ใช่น้ำเดือด"),("ร่อนผงทุกครั้ง","ไม่ให้จับก้อน"),("ตีซิกแซกรูปตัว M","ไม่ตีวนวงกลม"),("~2 g : น้ำ 60–70 ml","ไม่ใส่ผงพูน"),("โถปิดสนิท ที่เย็น","ไม่เปิดถุงทิ้งไว้")]
H.append(f'<div id="recap" class="e card recap"><h1>ชงมัทฉะไม่ขม<br>ฉบับ Hibi</h1><h2>5 ข้อ จำง่าย · เซฟไว้ใช้ตอนชง</h2>'+
  "".join(f'<div class="row" id="r{k}"><div class="n">{k+1}</div><div><div class="a">{a}</div><div class="b">✕ {b}</div></div></div>' for k,(a,b) in enumerate(rows))+'</div>')
CUES.append(dict(id="recap",a=round(RA,3),b=T+1,anim="slide"))
for k in range(5): CUES.append(dict(id=f"r{k}",a=round(RA+0.5+k*0.35,3),b=T+1,anim="row"))
el("save",PIN.format(s=48).replace('#e5484d','#ffd23f')+" เซฟไว้ · ส่งให้เพื่อนที่ชงมัทฉะขม",RA+2.6,T+1,"wobble")
el("foot","Hibi Matcha Cafe 5 สาขา · LINE MAN · Grab · ShopeeFood",RA+3.0,T+1,"up")

JS="""
const C=__C__, P=__P__;
const ease=x=>1-Math.pow(1-x,3), back=x=>{const c=1.9;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const cl=x=>Math.max(0,Math.min(1,x));
function render(t){
 for(const c of C){const e=document.getElementById(c.id); if(!e) continue;
  if(t<c.a||t>c.b){e.style.opacity=0;continue}
  const i=cl((t-c.a)/0.35), o=cl((c.b-t)/0.2); let op=Math.min(1,o), tr='';
  switch(c.anim){
   case 'pop': op*=cl(i*2.5); tr=`scale(${0.7+0.3*back(i)})`; break;
   case 'slam': op*=cl(i*3); tr=`scale(${1.6-0.6*ease(cl((t-c.a)/0.22))})`; break;
   case 'up': op*=ease(i); tr=`translateY(${50*(1-ease(i))}px)`; break;
   case 'slide': op*=ease(i); tr=`translateX(${-120*(1-ease(i))}px)`; break;
   case 'row': op*=ease(i); tr=`translateX(${60*(1-ease(i))}px)`; break;
   case 'fade': op*=ease(i); break;
   case 'flash': op=0.55*Math.max(0,1-Math.abs(t-(c.a+0.12))/0.12); break;
   case 'wobble': op*=cl(i*2.5); tr=`scale(${0.7+0.3*back(i)}) rotate(${-3+2.5*Math.sin((t-c.a)*5)}deg)`; break;
   case 'shake': op*=cl(i*3); tr=`scale(${0.7+0.3*back(i)}) rotate(${(t-c.a)<1.2?6*Math.sin((t-c.a)*40)*Math.max(0,1-(t-c.a)/1.2):0}deg)`; break;
  }
  if(c.anim!=='flash' && o<1) tr+=` scale(${0.94+0.06*o})`;
  e.style.opacity=op; e.style.transform=tr;
 }
 // progress bar
 const pg=document.getElementById('prog');
 if(t<P.a||t>P.b){pg.style.opacity=0}else{pg.style.opacity=ease(cl((t-P.a)/0.3))*cl((P.b-t)/0.2);
  [...pg.children].forEach((s,k)=>{const [a,b]=P.secs[k];const f=cl((t-a)/(b-a));
   s.className='s'+(t>=b?' done':(t>=a?' on':''));s.firstChild.style.width=(f*100)+'%';
   s.style.transform=(t>=a&&t<a+0.4)?`scale(${1+0.15*Math.sin(Math.PI*(t-a)/0.4)})`:''});}
 // M path draw loop
 const mp=document.getElementById('mpath'); if(mp){const c=C.find(x=>x.anim==='fade'); const k=((t-c.a)%1.6)/1.2; mp.style.strokeDashoffset=1400*(1-cl(k));}
 // count-up 70->80
 const cn=document.getElementById('cnt'); if(cn){const c=C.find(x=>x.id===cn.parentElement.id); const k=cl((t-c.a)/0.9);
   cn.textContent=(k<1? Math.round(20+50*ease(k))+'°C' : '70–80°C');}
}
""".replace("__C__",json.dumps(CUES)).replace("__P__",json.dumps(PROG))
open(f"{D}/mg.html","w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(H)}<script>{JS}</script></body></html>")
json.dump(dict(T=T),open(f"{D}/mg_meta.json","w"))
print("cues",len(CUES),"T",round(T,2))
