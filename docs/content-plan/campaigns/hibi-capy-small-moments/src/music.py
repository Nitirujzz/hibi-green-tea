"""Original, license-free ukulele bed for Small Moments EP1: 96 BPM (bar = 2.5 s), 10 bars = 25 s.
Karplus-Strong plucked ukulele strums (C-Am-F-G), soft glockenspiel melody, shaker, warm sub. -> music.wav"""
import numpy as np, scipy.io.wavfile as wf, os
SR=48000; BPM=96; B=60/BPM; T=25.0; N=int(SR*(T+1.5))
L=np.zeros(N); R=np.zeros(N)
def ks(f,dur,bright=0.5,decay=0.996):
    n=int(SR*dur); p=max(2,int(SR/f)); buf=np.random.uniform(-1,1,p)
    # low-pass the excitation for a nylon tone
    for _ in range(int(3*(1-bright))+1): buf=0.5*(buf+np.roll(buf,1))
    out=np.zeros(n)
    for i in range(n):
        out[i]=buf[i%p]; buf[i%p]=decay*0.5*(buf[i%p]+buf[(i+1)%p])
    return out*np.exp(-np.arange(n)/SR*1.6)
def add(sig,t,g=1.0,pan=0.0):
    i=int(t*SR); j=min(N,i+len(sig)); s=sig[:j-i]*g
    L[i:j]+=s*(1-pan)/1.0; R[i:j]+=s*(1+pan)/1.0
hz=lambda m:440*2**((m-69)/12)
# ukulele voicings (G4 C4 E4 A4 re-entrant style)
CH={"C":[67,60,64,72],"Am":[69,60,64,69],"F":[69,60,65,69],"G":[67,62,71,67]}
PROG=["C","Am","F","G","C","Am","F","G","F","C"]
np.random.seed(7)
cache={}
def note(m,dur,br):
    k=(m,round(dur,2),br)
    if k not in cache: cache[k]=ks(hz(m),dur,br)
    return cache[k]
# strum pattern per bar (beats, direction): D . D U . U D U
PAT=[(0,1),(1,1),(1.5,-1),(2.5,-1),(3,1),(3.5,-1)]
for bar,ch in enumerate(PROG):
    t0=bar*4*B; last=bar==len(PROG)-1
    pat=[(0,1)] if last else PAT
    for b,d in pat:
        strings=CH[ch] if d>0 else CH[ch][::-1]
        for k,m in enumerate(strings):
            dur=3.0 if last else 1.2
            add(note(m,dur,0.55 if d>0 else 0.75),t0+b*B+k*0.012,g=0.16 if d>0 else 0.11,pan=-0.15)
    # warm sub on the root
    root={"C":36,"Am":33,"F":29,"G":31}[ch]; n=int(SR*(4*B if not last else 3.0)); tt=np.arange(n)/SR
    add(0.10*np.sin(2*np.pi*hz(root+12)*tt)*np.exp(-tt*0.8)*(1-np.exp(-tt*40)),t0,pan=0)
# glockenspiel melody (enters bar 3, sweet & sparse)
MEL=[(2,0,76),(2,1,79),(2,2,81),(3,0,79),(3,2,74),(4,0,72),(4,1,76),(4,2,79),(5,0,81),(5,2,76),(6,0,77),(6,1,76),(6,2,72),(7,0,74),(7,2,79),(8,0,77),(8,2,81),(9,0,84)]
for bar,beat,m in MEL:
    n=int(SR*1.6); tt=np.arange(n)/SR; f=hz(m)
    s=(np.sin(2*np.pi*f*tt)+0.35*np.sin(2*np.pi*f*2.76*tt)*np.exp(-tt*6))*np.exp(-tt*2.6)*(1-np.exp(-tt*300))
    add(0.06*s,bar*4*B+beat*B,pan=0.25)
# shaker on 8ths (bars 1-9), very soft
for k in range(int(9*8)):
    n=int(SR*0.07); tt=np.arange(n)/SR; s=np.random.uniform(-1,1,n)*np.exp(-tt*60)
    s=np.diff(np.concatenate([[0],s]))   # brighten
    add(s*(0.018 if k%2 else 0.012),k*B/2+2*4*B*0+0.0,pan=0.3) if k>=8 else None
mix=np.stack([L,R],1)
# simple room: two short echoes
for d,g in ((0.031,0.25),(0.067,0.15)):
    i=int(d*SR); mix[i:]+=g*mix[:-i]
mix=mix[:int(SR*(T+0.6))]
fo=int(SR*0.6); mix[-fo:]*=np.linspace(1,0,fo)[:,None]
mix/=np.max(np.abs(mix))*1.12
wf.write(os.path.join(os.path.dirname(os.path.abspath(__file__)),"music.wav"),SR,(mix*32767).astype(np.int16)); print("music ok", mix.shape[0]/SR)
