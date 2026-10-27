"""Tight VO timing: every pause found by silencedetect (-42 dB, >=0.10 s) is shrunk,
then the whole voice is sped up 1.1x (pitch kept). m(t) maps ORIGINAL VO seconds -> final timeline."""
import os
D=os.path.dirname(os.path.abspath(__file__))
TEMPO=1.10; PAD=0.04; LEAD=0.08
SECTION_STARTS=[10.95,31.08,42.28,61.30,83.82,104.9]   # ข้อ1..ข้อ5, CTA
_v=[float(x) for x in open(f"{D}/sil.txt").read().split()]
if len(_v)%2: _v.append(121.0)
SIL=list(zip(_v[0::2],_v[1::2]))
def speech():
    out=[];prev=0.0
    for a,b in SIL:
        if a-prev>0.02: out.append((prev,a))
        prev=b
    return out
def gap_len(a,b,nxt):
    if any(abs(nxt-s)<0.5 for s in SECTION_STARTS): return 0.30
    return 0.16 if b-a>0.6 else 0.06
_P=None
def plan():
    global _P
    if _P: return _P
    sp=speech();out=[];t=LEAD
    for i,(a,b) in enumerate(sp):
        a2=max(0,a-PAD);b2=b+PAD
        if i>0: t+=gap_len(sp[i-1][1],a,a)-2*PAD if gap_len(sp[i-1][1],a,a)>2*PAD else 0
        out.append((a2,b2,t));t+=b2-a2
    _P=(out,t)
    return _P
def m_raw(x):
    p,_=plan()
    for a2,b2,t in p:
        if x<=b2: return t+max(0,x-a2)
    a2,b2,t=p[-1];return t+(x-a2)
def m(x): return m_raw(x)/TEMPO
def total(): return plan()[1]/TEMPO+0.9
if __name__=="__main__":
    p,T=plan();print("segments",len(p),"raw",round(T,2),"final",round(total(),2))
