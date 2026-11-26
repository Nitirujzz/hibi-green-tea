"""Shot timeline driven by the tightened VO: each shot = VO line + breathing room (no dead air)."""
import os
D=os.path.dirname(os.path.abspath(__file__))
LEAD=0.12; TAIL=0.28
MIN={1:3.0,2:2.2,7:2.6,11:6.4}
def durs():
    d={int(a):float(b) for a,b in (l.split() for l in open(f"{D}/vo/dur.txt") if l.strip())}
    return d
def plan():
    d=durs(); S=[0.0]; vo=[]
    for n in range(1,12):
        L=LEAD+d.get(n,2.5)+TAIL
        if n==11: L=LEAD+d.get(n,2.5)+0.9
        L=max(L,MIN.get(n,0)); vo.append(S[-1]+LEAD); S.append(round(S[-1]+L,3))
    return S,vo
if __name__=="__main__":
    S,vo=plan(); print([round(x,2) for x in S]); print("total",S[-1])
