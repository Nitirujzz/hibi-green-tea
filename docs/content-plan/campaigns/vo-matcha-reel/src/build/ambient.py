"""Soft background bed (original, synthesised): warm pad + gentle electric-piano arpeggio + sub bass,
long reverb tail, carved around 1–4 kHz so it sits under the voice. No drums. 80 BPM, Fmaj7–G6–Em7–Am7."""
import numpy as np, wave, timing
from scipy.signal import butter, sosfilt, fftconvolve
SR=48000; BEAT=60/80; T=timing.total()+0.5; N=int(T*SR)
rng=np.random.default_rng(3); L=np.zeros(N); R=np.zeros(N)
def hz(n): return 440*2**((n-69)/12)
def put(buf,s,t,g):
    i=int(t*SR); j=min(N,i+len(s))
    if 0<=i<N: buf[i:j]+=g*s[:j-i]
def pad(f,d):
    t=np.arange(int((d+1.6)*SR))/SR
    env=np.minimum(1,t/1.2)*np.where(t<d,1,np.exp(-(t-d)*2.5))
    s=sum(np.sin(2*np.pi*f*(1+dt)*t+ph) for dt,ph in [(0,0),(0.004,1.3),(-0.004,2.1)])/3
    s+=0.18*np.sin(2*np.pi*2*f*t)+0.06*np.sin(2*np.pi*3*f*t)
    return s*env*(1+0.06*np.sin(2*np.pi*0.25*t))
def ep(f,d=1.6):
    t=np.arange(int(d*SR))/SR; env=np.exp(-t*2.8)*(1-np.exp(-t*150))
    return (np.sin(2*np.pi*f*t)+0.25*np.sin(2*np.pi*2*f*t)*np.exp(-t*5))*env
def sub(f,d):
    t=np.arange(int(d*SR))/SR; env=np.minimum(1,t/0.3)*np.minimum(1,(d-t)/0.4).clip(0)
    return np.sin(2*np.pi*f*t)*env
CH=[[53,57,60,64],[55,59,62,64],[52,55,59,62],[57,60,64,67]]; BS=[41,43,40,45]
bar=4*BEAT; per=2*bar                       # each chord holds 2 bars (6 s) -> calm
for b in range(int(T/per)+1):
    t0=b*per; c=CH[b%4]
    for k,n in enumerate(c):
        put(L,pad(hz(n),per),t0,0.07 if k%2 else 0.05); put(R,pad(hz(n),per),t0,0.05 if k%2 else 0.07)
    put(L,sub(hz(BS[b%4]),per),t0,0.16); put(R,sub(hz(BS[b%4]),per),t0,0.16)
    arp=[c[0]+12,c[2]+12,c[1]+12,c[3]+12,c[2]+12,c[1]+12,c[3]+12,c[2]+12]
    for s in range(16):                    # soft eighth-note arpeggio, slightly humanised
        n=arp[s%8]; ts=t0+s*BEAT/2+rng.uniform(-0.01,0.01); g=0.035*(1.0 if s%4==0 else 0.7)
        put(L if s%2 else R,ep(hz(n)),ts,g); put(R if s%2 else L,ep(hz(n)),ts+0.012,g*0.6)
mix=np.stack([L,R],1)
# reverb: decaying stereo noise IR (2.4 s)
irn=int(2.4*SR); tt=np.arange(irn)/SR; dec=np.exp(-tt*2.6)
sos=butter(2,[200,5000],'band',fs=SR,output='sos')
for ch in range(2):
    ir=sosfilt(sos,rng.standard_normal(irn))*dec; ir/=np.sqrt(np.sum(ir**2))
    mix[:,ch]=mix[:,ch]*0.75+0.45*fftconvolve(mix[:,ch],ir)[:N]
# make room for the voice: gentle low-pass + dip in the speech band
mix=sosfilt(butter(2,4200,'low',fs=SR,output='sos'),mix,axis=0)
band=sosfilt(butter(2,[1000,3800],'band',fs=SR,output='sos'),mix,axis=0)
mix=mix-0.5*band
mix=sosfilt(butter(1,60,'high',fs=SR,output='sos'),mix,axis=0)
fi=int(1.5*SR); mix[:fi]*=np.linspace(0,1,fi)[:,None]
fo=int(2.0*SR); mix[-fo:]*=np.linspace(1,0,fo)[:,None]
mix/=np.max(np.abs(mix))*1.1
with wave.open("ambient.wav","wb") as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype('<i2').tobytes())
print("ok",round(T,1))
