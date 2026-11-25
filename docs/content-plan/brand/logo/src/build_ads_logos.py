"""Google Ads logo assets from the vectorized Hibi mark: 1:1 (1200x1200) x3 and 4:1 (1200x300). HTML -> Chromium PNG."""
import subprocess, os
D=os.path.abspath(os.path.join(os.path.dirname(__file__),"..")); O=f"{D}/google-ads"; os.makedirs(O,exist_ok=True)
G="#273d28"; CREAM="#f6f1ed"; MATCHA="#4e7c3a"
mark=open(f"{D}/hibi_mark.svg").read(); word=open(f"{D}/hibi_wordmark_jp.svg").read()
recolor=lambda svg,c: svg.replace('fill="#273d28"',f'fill="{c}"')
F="".join(f"@font-face{{font-family:P;font-weight:{w};src:url('file:///root/.fonts/Prompt-{w}-latin.woff2')}}" for w in (500,600))
def shot(name,w,h,body,bg):
    p=f"{O}/{name}.html"
    open(p,"w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{F}*{{margin:0;padding:0}}body{{width:{w}px;height:{h}px;background:{bg};position:relative;overflow:hidden;font-family:P}}svg{{display:block}}</style></head><body>{body}</body></html>")
    subprocess.run(["/opt/pw-browsers/chromium","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--allow-file-access-from-files","--virtual-time-budget=3000",
                    f"--screenshot={O}/{name}.png",f"--window-size={w},{h}","file://"+p],check=True,capture_output=True); os.remove(p)
box=lambda svg,x,y,h:f'<div style="position:absolute;left:{x}px;top:{y}px;height:{h}px">{svg.replace("<svg ",f"<svg height={h} ")}</div>'
# 1:1 A · dark mark on cream (matches the current cream logo) — mark inside the central 70% so circle crops stay safe
shot("hibi_logo_1x1_cream",1200,1200,f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{mark.replace("<svg ","<svg height=700 ")}</div>',CREAM)
# 1:1 B · white mark on matcha-green (high contrast in feeds / dark mode)
shot("hibi_logo_1x1_green",1200,1200,f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{recolor(mark,"#ffffff").replace("<svg ","<svg height=700 ")}</div>',G)
# 1:1 C · mark + wordmark lockup
shot("hibi_logo_1x1_lockup",1200,1200,f'''<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px">
 {mark.replace("<svg ","<svg height=520 ")}
 <div style="font-weight:600;font-size:64px;letter-spacing:16px;color:{G};margin-right:-16px">HIBI MATCHA CAFE</div></div>''',CREAM)
# 4:1 landscape · mark + name (Google Ads landscape logo 1200x300)
shot("hibi_logo_4x1",1200,300,f'''<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:40px">
 {mark.replace("<svg ","<svg height=210 ")}
 <div><div style="font-weight:600;font-size:78px;letter-spacing:8px;color:{G};line-height:1">HIBI</div>
 <div style="font-weight:500;font-size:40px;letter-spacing:10px;color:{MATCHA};margin-top:10px">MATCHA CAFE</div></div></div>''',CREAM)
print("ok")
