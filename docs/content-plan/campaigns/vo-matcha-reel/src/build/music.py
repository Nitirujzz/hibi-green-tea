"""Original royalty-free lo-fi/cafe-pop bed (synthesised here, no samples). 100 BPM.
Intro (hook): keys + shaker, low-passed -> full beat drops at ข้อ 1 -> drums out for the recap."""
import numpy as np, timing
from scipy.signal import butter, sosfilt
SR=48000; BPM=100; BEAT=60/BPM; T=timing.total()+0.5
N=int(T*SR); L=np.zeros(N); R=np.zeros(N)
rng=np.random.default_rng(7)
def midi(n): return 440*2**((n-69)/12)
def put(buf,sig,t,g=1.0):
    i=int(t*SR); j=min(N,i+len(sig))
    if i<N: buf[i:j]+=g*sig[:j-i]
def ep(f,d):          # electric-piano-ish tone
    t=np.arange(int(d*SR))/SR
    env=np.exp(-t*2.2)*(1-np.exp(-t*200))
    s=np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*2*f*t)*np.exp(-t*6)+0.08*np.sin(2*np.pi*3*f*t)*np.exp(-t*9)
    return s*env*(1+0.15*np.sin(2*np.pi*4.5*t))
def bass(f,d):
    t=np.arange(int(d*SR))/SR; env=np.minimum(1,t*60)*np.exp(-t*1.5)
    return (np.sin(2*np.pi*f*t)+0.2*np.sin(2*np.pi*2*f*t))*env
def kick():
    t=np.arange(int(0.35*SR))/SR; f=50+90*np.exp(-t*30)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*9)
def noise(d,lo,hi,dec):
    n=rng.standard_normal(int(d*SR)); sos=butter(2,[lo,hi],'band',fs=SR,output='sos')
    t=np.arange(len(n))/SR; return sosfilt(sos,n)*np.exp(-t*dec)
CH=[[53,57,60,64],[55,59,62,64],[52,55,59,62],[57,60,64,67]]   # Fmaj7 G6 Em7 Am7
BS=[41,43,40,45]
drop=timing.m(10.95)-0.05; outro=timing.m(111.0)
bar=4*BEAT; nb=int(T/bar)+1
for b in range(nb):
    t0=b*bar; c=CH[b%4]
    for k,n in enumerate(c): # strum + off-beat restrike
        put(L,ep(midi(n),bar),t0+k*0.012,0.10 if k%2 else 0.08); put(R,ep(midi(n),bar),t0+k*0.015,0.08 if k%2 else 0.10)
        put(L,ep(midi(n+12),BEAT*1.5),t0+2.5*BEAT,0.025); put(R,ep(midi(n+12),BEAT*1.5),t0+2.5*BEAT+0.01,0.025)
    full = drop<=t0<outro
    if full:
        put(L,bass(midi(BS[b%4]),BEAT*1.8),t0,0.32); put(R,bass(midi(BS[b%4]),BEAT*1.8),t0,0.32)
        put(L,bass(midi(BS[b%4]),BEAT*1.2),t0+2.5*BEAT,0.22); put(R,bass(midi(BS[b%4]),BEAT*1.2),t0+2.5*BEAT,0.22)
    for s in range(8):
        ts=t0+s*BEAT/2
        hh=noise(0.06,6000,12000,60)
        put(L,hh,ts,0.05 if s%2 else 0.03); put(R,hh,ts+0.004,0.05 if s%2 else 0.03)
        if full:
            if s in (0,5): k_=kick(); put(L,k_,ts,0.55); put(R,k_,ts,0.55)
            if s in (2,6): sn=noise(0.2,900,5000,18); put(L,sn,ts,0.16); put(R,sn,ts+0.006,0.16)
# riser into the drop
d=1.2; t=np.arange(int(d*SR))/SR; rs=noise(d,800,9000,0)*(t/d)**2
put(L,rs,drop-d,0.12); put(R,rs,drop-d,0.12)
mix=np.stack([L,R],1)
# intro: muffled (low-pass) until the drop; gentle tape warmth
sos=butter(2,1400,'low',fs=SR,output='sos'); i=int(drop*SR)
mix[:i]=sosfilt(sos,mix[:i],axis=0)*1.3
mix+=0.004*rng.standard_normal(mix.shape)              # vinyl hiss
mix=np.tanh(mix*1.2)/1.2
fo=int(1.5*SR); mix[-fo:]*=np.linspace(1,0,fo)[:,None]
mix/=np.max(np.abs(mix))*1.12
import wave
with wave.open("music.wav","wb") as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype('<i2').tobytes())
print("music",round(T,1),"drop",round(drop,2),"outro",round(outro,2))
