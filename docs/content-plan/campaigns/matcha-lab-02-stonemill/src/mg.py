"""Motion graphics for Matcha Lab #2 (stone mill) (transparent 1080x1920). Timing from timeline.py. Safe zone x 70–950 · y 190–1440."""
import json, os, timeline
D=os.path.dirname(os.path.abspath(__file__))
S,VO=timeline.plan(); T=S[-1]
FONTS="".join(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file:///root/.fonts/{f}-{w}-{s}.woff2') format('woff2');}}"
  for fam,f in [("Prompt","Prompt"),("Plex","IBMPlexSansThai")] for w in ([400,500,600,700] if f=="Prompt" else [400,600]) for s in ["thai","latin"])
CSS=FONTS+"""*{margin:0;padding:0;box-sizing:border-box}html,body{width:1080px;height:1920px;background:transparent;overflow:hidden;font-family:'Prompt'}
.e{position:absolute;opacity:0}
.tag{left:80px;top:200px;background:rgba(20,40,14,.72);color:#e9f5df;font-weight:600;font-size:34px;padding:8px 22px;border-radius:40px;letter-spacing:.5px}
.scrim{left:0;top:0;width:1080px;height:900px;background:linear-gradient(rgba(0,0,0,.55),rgba(0,0,0,0))}
.hook{left:70px;width:880px;top:330px;text-align:center;color:#fff;font-weight:700;font-size:92px;line-height:1.16;text-shadow:0 6px 24px rgba(0,0,0,.55)}
.hook b{color:#ffd23f}
.pill{left:510px;top:1210px;translate:-50% 0;width:max-content;max-width:880px;text-align:center;background:rgba(255,252,244,.95);color:#243e1b;font-weight:700;font-size:52px;line-height:1.25;padding:18px 40px;border-radius:44px;box-shadow:0 12px 30px rgba(0,0,0,.28);border:4px solid #a8d48a}
.pill .s{display:block;font-family:Plex;font-weight:600;font-size:36px;color:#4e7c3a}
.chip{font-weight:700;font-size:46px;padding:12px 30px;border-radius:40px;box-shadow:0 10px 26px rgba(0,0,0,.35);white-space:nowrap}
.gold{background:linear-gradient(#ffe48a,#f2b632);color:#4a3200;border:3px solid #fff3c4}
.grey{background:linear-gradient(#e4e6ea,#9aa0a8);color:#2b2f35;border:3px solid #f4f5f7}
.arrow{font-size:70px;color:#fff;text-shadow:0 4px 14px rgba(0,0,0,.5)}
.leaf{top:1330px;translate:-50% 0;background:rgba(36,62,27,.9);color:#fff;font-weight:700;font-size:44px;padding:10px 28px;border-radius:30px}
.board{left:590px;top:380px;width:350px;color:#243e1b}
.board .h{font-weight:700;font-size:46px;line-height:1.1;margin-bottom:18px}
.row{margin-bottom:16px;opacity:0}
.row .n{font-weight:700;font-size:40px;line-height:1.1}
.row .d{font-family:Plex;font-weight:600;font-size:32px;color:#6b6a55}
.row.hi .n{color:#3f8f3a}
.badge{width:64px;height:64px;margin:-32px 0 0 -32px;border-radius:50%;background:#243e1b;color:#fff;font-weight:700;font-size:32px;display:flex;align-items:center;justify-content:center;border:4px solid #fff;box-shadow:0 6px 16px rgba(0,0,0,.3)}
.sim{right:120px;top:300px;background:rgba(20,40,14,.7);color:#e9f5df;font-family:Plex;font-weight:600;font-size:28px;padding:6px 18px;border-radius:24px}
.end{left:90px;width:900px;top:300px;background:rgba(255,252,244,.97);border-radius:48px;padding:48px 44px 40px;text-align:center;box-shadow:0 18px 44px rgba(0,0,0,.25);border:5px solid #a8d48a}
.tip{display:flex;align-items:center;gap:20px;margin-top:20px;text-align:left}
.tip i{flex:none;font-style:normal;width:66px;height:66px;border-radius:50%;background:#243e1b;color:#fff;font-size:38px;font-weight:700;display:flex;align-items:center;justify-content:center}
.tip span{font-size:42px;color:#243e1b;line-height:1.2;font-weight:600}
#fx{position:absolute;inset:0}
"""
H=[];C=[]
def el(cls,html,a,b,anim="pop",style=""):
    i=len(C);C.append(dict(id=f"e{i}",a=a,b=b,anim=anim));H.append(f'<div id="e{i}" class="e {cls}" style="{style}">{html}</div>')
el("scrim","",0,S[1]-0.1,"fade")
el("tag","Matcha Lab 🔬 #2",0.2,S[10],"fade")
el("hook","หินโม่หมุน <b>1 ชั่วโมง</b>…<br>ได้มัทฉะแค่ <b>~40 กรัม</b> ⏳",0.0,S[1]-0.12,"slam")
P={2:"ทำไมช้าขนาดนี้? 🔬",3:"เทนฉะ = ใบชาอบแห้ง<span class='s'>แยกก้านและเส้นใบออกแล้ว</span>",
   4:"ใส่ทีละน้อย<span class='s'>ลงรูกลางหินโม่</span>",5:"ใบชาเดินจากกลาง → ขอบหิน<span class='s'>ผ่านร่องหิน ละเอียดขึ้นเรื่อย ๆ</span>",
   6:"หมุนช้า = ไม่ร้อนจากแรงเสียดทาน<span class='s'>ถนอมสีเขียวและกลิ่นหอม</span>",7:"ผงละเอียดราว 5–10 ไมครอน<span class='s'>เล็กกว่าเส้นผมหลายเท่า</span>",
   9:"ผงละเอียดมาก จับเป็นก้อนง่าย<span class='s'>→ ร่อนก่อนชงทุกครั้ง</span>"}
for i,t in P.items(): el("pill",t,S[i-1]+0.15,S[i]-0.08,"slam" if i in (6,9) else "pop")
el("sim","ภาพจำลอง",S[4]+0.2,S[5]-0.1,"fade")
el("sim","ภาพจำลอง",S[6]+0.2,S[7]-0.1,"fade")
XS=[167,424,679,938]; YS=[292,640,978,1323,1680]   # bowl centres measured from frames/s08.png
for k in range(20):
    el("badge",str(k+1),S[7]+0.5+k*0.12,S[8]-0.08,"pop",f"left:{XS[k%4]}px;top:{YS[k//4]}px")
el("pill","40 กรัม ≈ มัทฉะ ~20 ถ้วย<span class='s'>(ถ้วยละ ~2 กรัม)</span>",S[7]+3.0,S[8]-0.08,"slam","top:820px")
rows=[("⏳ 1 ชม.","≈ 30–40 กรัม",""),("🔬 ผงละเอียด","~5–10 ไมครอน",""),("🌡️ หมุนช้า","กันร้อน ถนอมสี/กลิ่น",""),("🍵 40 กรัม","≈ ~20 ถ้วย","hi")]
rh="".join(f'<div class="row {c}" id="r{k}"><div class="n">{n}</div><div class="d">{d}</div></div>' for k,(n,d,c) in enumerate(rows))
el("board",f'<div class="h">หินโม่<br>1 ตัว</div>{rh}',S[9]+0.1,S[10]-0.08,"fade")
tips="".join(f'<div class="tip"><i>{k}</i><span>{t}</span></div>' for k,t in [(1,"หินโม่ 1 ชม. ≈ 30–40 กรัม"),(2,"หมุนช้า = ไม่ร้อน<br>ถนอมสีและกลิ่น"),(3,"ผงละเอียดมาก → ร่อนก่อนชง")])
el("end",'<div style="font-weight:700;font-size:58px;color:#e5484d">📌 เซฟไว้</div><div style="font-weight:700;font-size:74px;color:#243e1b;line-height:1.08">ทำไมมัทฉะ<br>ต้องโม่ช้า?</div>'
   f'<div style="padding:4px 6px 0">{tips}</div>'
   '<div style="font-family:Plex;font-size:34px;color:#6b6a55;margin-top:30px;padding-top:22px;border-top:3px dashed #d8e3c8">ตอนหน้า 🔬 น้ำเดือดทำให้มัทฉะขม จริงไหม?</div>'
   '<div style="font-family:Plex;font-size:28px;color:#9a9578;margin-top:14px">Matcha Lab · @hibimatchacafe · ตัวเลขเป็นค่าประมาณ</div>',S[10]+0.15,T+1,"pop")
FX=[dict(kind="spark",a=S[0],b=S[1]),dict(kind="spark",a=S[6],b=S[7]),dict(kind="spark",a=S[8],b=S[9]),dict(kind="spark",a=S[10],b=T)]
ROWS=[dict(id=f"r{k}",a=S[9]+0.6+k*0.75) for k in range(4)]
JS="""
const C=__C__, FX=__FX__, ROWS=__R__;
const ease=x=>1-Math.pow(1-x,3), back=x=>{const c=1.9;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2)}, cl=x=>Math.max(0,Math.min(1,x));
function rnd(i){const x=Math.sin(i*127.1+311.7)*43758.5453;return x-Math.floor(x)}
const SPARK='<svg viewBox="0 0 24 24" width="100%" height="100%"><path d="M12 0l2.6 9.4L24 12l-9.4 2.6L12 24l-2.6-9.4L0 12l9.4-2.6z" fill="#fff6b0"/></svg>';
const fx=document.getElementById('fx'); const parts=[];
FX.forEach((f,k)=>{for(let i=0;i<14;i++){const d=document.createElement('div');d.style.cssText='position:absolute;opacity:0';d.innerHTML=SPARK;fx.appendChild(d);parts.push({d,f,i,k})}});
function render(t){
 for(const c of C){const e=document.getElementById(c.id);
  if(t<c.a||t>c.b){e.style.opacity=0;continue}
  const i=cl((t-c.a)/0.35),o=cl((c.b-t)/0.2);let op=o,tr='';
  if(c.anim=='pop'){op*=cl(i*2.5);tr=`scale(${0.7+0.3*back(i)})`}
  else if(c.anim=='slam'){op*=cl(i*3);tr=`scale(${1.4-0.4*ease(cl((t-c.a)/0.25))})`}
  else if(c.anim=='fade'){op*=cl(i*2)}
  e.style.opacity=op;e.style.transform=tr+(o<1&&c.anim!='fade'?` scale(${0.94+0.06*o})`:'');}
 for(const r of ROWS){const e=document.getElementById(r.id);const u=cl((t-r.a)/0.3);e.style.opacity=u;e.style.transform=`translateX(${(1-ease(u))*40}px)`;}
 for(const p of parts){const {f,i,d}=p;const life=f.b-f.a;const st=f.a+rnd(i+p.k*31)*life*0.7;const u=(t-st)/1.0;
  if(t<f.a||t>f.b||u<0||u>1){d.style.opacity=0;continue}
  const x=90+rnd(i*7+p.k)*880, y=280+rnd(i*13+p.k)*1100, sz=26+rnd(i*5)*40;
  d.style.left=x+'px';d.style.top=y+'px';d.style.width=sz+'px';d.style.height=sz+'px';d.style.opacity=Math.sin(Math.PI*u)*0.9;
  d.style.transform=`translate(-50%,-50%) scale(${0.4+Math.sin(Math.PI*u)}) rotate(${u*90}deg)`;}
}
""".replace("__C__",json.dumps(C)).replace("__FX__",json.dumps(FX)).replace("__R__",json.dumps(ROWS))
open(f"{D}/mg.html","w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body><div id='fx'></div>{''.join(H)}<script>{JS}</script></body></html>")
print("ok",round(T,2))
