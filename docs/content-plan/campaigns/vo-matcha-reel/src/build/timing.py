# speech segments (orig seconds) from silencedetect on vo_clean.wav
SEGS=[(1.6,10.3),(10.9,11.4),(11.9,15.7),(17.0,19.1),(19.8,22.8),(23.3,24.5),(24.9,25.5),(25.9,29.5),(30.7,31.7),(32.4,34.0),(34.6,40.0),(40.4,41.0),(42.0,42.9),(44.0,44.5),(44.9,46.2),(47.0,50.6),(52.0,56.5),(56.9,58.7),(60.8,61.9),(62.4,64.6),(65.0,67.8),(68.8,70.4),(71.1,77.0),(77.9,82.8),(83.7,88.5),(88.9,91.2),(91.7,93.5),(94.0,95.5),(96.1,102.2),(103.5,103.9),(104.7,105.5),(106.7,111.1),(111.5,120.1)]
PAD=0.12          # keep a little air around each segment
SECTION_STARTS={10.9,30.7,42.0,60.8,83.7,103.5}   # new section -> slightly longer breath
def plan():
    out=[];t=0.25
    for i,(a,b) in enumerate(SEGS):
        a2=max(0,a-PAD);b2=b+PAD
        if i>0:
            gap=0.55 if a in SECTION_STARTS else 0.22
            t+=gap
        out.append((a2,b2,t));t+=b2-a2
    return out,t+0.6
def m(x):
    """map original time -> new time"""
    p,_=plan()
    for a2,b2,t in p:
        if x<=b2: return t+max(0,x-a2)
    a2,b2,t=p[-1];return t+(x-a2)
if __name__=="__main__":
    p,T=plan();print("new length",round(T,2))
