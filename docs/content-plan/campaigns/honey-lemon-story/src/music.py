"""Original warm/cute bed for the Honey Lemon reel: ukulele-style plucks (Karplus-Strong), glockenspiel melody,
soft pad + light shaker/kick. 100 BPM, C major (C–G–Am–F). Builds at the hero pour, gentle outro."""
import numpy as np, wave
from scipy.signal import butter, sosfilt, fftconvolve
SR=48000; BPM=100; B=60/BPM; T=40.5; N=int(T*SR); rng=np.random.default_rng(11)
L=np.zeros(N); R=np.zeros(N)
def hz(n): return 440*2**((n-69)/12)
def put(s,t,g,pan=0.0):
    i=int(t*SR); j=min(N,i+len(s))
    if 0<=i<N: L[i:j]+=g*(1-pan)*s[:j-i]; R[i:j]+=g*(1+pan)*s[:j-i]
def pluck(f,d=1.2):
    n=int(d*SR); p=int(SR/f); buf=rng.uniform(-1,1,p); out=np.zeros(n)
    for i in range(n):
        out[i]=buf[i%p]; buf[i%p]=0.5*(buf[i%p]+buf[(i+1)%p])*0.996
    return out*np.exp(-np.arange(n)/SR*2.5)
def glock(f,d=1.6):
    t=np.arange(int(d*SR))/SR
    return (np.sin(2*np.pi*f*t)+0.3*np.sin(2*np.pi*2.76*f*t)*np.exp(-t*8)+0.12*np.sin(2*np.pi*5.4*f*t)*np.exp(-t*14))*np.exp(-t*3.2)*(1-np.exp(-t*400))
def pad(f,d):
    t=np.arange(int((d+1)*SR))/SR; env=np.minimum(1,t/0.8)*np.where(t<d,1,np.exp(-(t-d)*3))
    return sum(np.sin(2*np.pi*f*(1+k)*t) for k in (0,0.003,-0.003))/3*env
def kick():
    t=np.arange(int(0.25*SR))/SR; return np.sin(2*np.pi*np.cumsum(55+70*np.exp(-t*35))/SR)*np.exp(-t*12)
def shaker():
    n=rng.standard_normal(int(0.07*SR)); return sosfilt(butter(2,[5000,11000],'band',fs=SR,output='sos'),n)*np.exp(-np.arange(len(n))/SR*55)
CH=[[60,64,67],[55,59,62,67],[57,60,64],[53,57,60,65]]
BASS=[48,43,45,41]
MEL=[76,79,81,79, 76,74,72,74, 72,76,79,76, 77,76,74,72]   # 8th-note-ish motif per bar (4 notes/bar = quarter notes)
bars=int(T/(4*B))+1; hero=26.0; outro=36.0
_cache={}
def pl(n):
    if n not in _cache: _cache[n]=pluck(hz(n))
    return _cache[n]
for b in range(bars):
    t0=b*4*B; c=CH[b%4]
    # ukulele strum pattern: D . D U . U D U
    for k,(off,g) in enumerate([(0,1),(1,0.7),(1.5,0.6),(2.5,0.6),(3,0.8),(3.5,0.6)]):
        for j,n in enumerate(c):
            put(pl(n),t0+off*B+j*0.012,0.10*g,pan=-0.3)
    put(pad(hz(c[0]-12),4*B),t0,0.05); put(pad(hz(c[1]-12),4*B),t0,0.04)
    put(pad(hz(BASS[b%4]-12),4*B),t0,0.07)
    if t0>=2.0:   # glock melody enters after the first beats
        for q in range(4):
            n=MEL[(b%4)*4+q]; put(glock(hz(n)),t0+q*B,0.07 if t0<hero else 0.09,pan=0.35)
    if 3.0<=t0<outro:
        for s in range(8): put(shaker(),t0+s*B/2,0.05 if s%2 else 0.03,pan=0.2)
        put(kick(),t0,0.35); put(kick(),t0+2*B,0.3)
        if t0>=hero: put(kick(),t0+2.5*B,0.2)
mix=np.stack([L,R],1)
ir_n=int(1.6*SR); tt=np.arange(ir_n)/SR
for ch in range(2):
    ir=sosfilt(butter(2,[300,6000],'band',fs=SR,output='sos'),rng.standard_normal(ir_n))*np.exp(-tt*3.5); ir/=np.sqrt((ir**2).sum())
    mix[:,ch]=mix[:,ch]*0.8+0.3*fftconvolve(mix[:,ch],ir)[:N]
fi=int(0.4*SR); mix[:fi]*=np.linspace(0,1,fi)[:,None]; fo=int(2.5*SR); mix[-fo:]*=np.linspace(1,0,fo)[:,None]
mix/=np.abs(mix).max()*1.1
with wave.open("music.wav","wb") as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype('<i2').tobytes())
print("ok")
