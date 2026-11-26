import potrace, numpy as np, sys
from PIL import Image, ImageFilter
def trace(src, box, out, scale=8, thr=110):
    im=Image.open(src).convert('L').crop(box)
    im=im.resize((im.width*scale,im.height*scale),Image.LANCZOS).filter(ImageFilter.GaussianBlur(scale*1.1))
    a=np.array(im)>=thr
    bm=potrace.Bitmap(a); path=bm.trace(turdsize=200, alphamax=1.25, opticurve=True, opttolerance=0.2)
    d=[]
    for c in path:
        s=c.start_point; d.append(f"M{s.x:.1f},{s.y:.1f}")
        for seg in c.segments:
            if seg.is_corner: d.append(f"L{seg.c.x:.1f},{seg.c.y:.1f}L{seg.end_point.x:.1f},{seg.end_point.y:.1f}")
            else: d.append(f"C{seg.c1.x:.1f},{seg.c1.y:.1f} {seg.c2.x:.1f},{seg.c2.y:.1f} {seg.end_point.x:.1f},{seg.end_point.y:.1f}")
        d.append("Z")
    w,h=im.size
    open(out,'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"><path fill-rule="evenodd" d="{" ".join(d)}"/></svg>')
    print(out,w,h,len(path))
S='/tmp/claude-0/-home-user-hibi-green-tea/0cebb280-b8ff-52d0-9853-651cb60dec31/images/2.png'
trace(S,(470,235,640,430),'mark.svg')          # bunny mark from the cream logo
trace(S,(135,365,235,470),'text.svg',thr=120)   # "Hibi 日々"
