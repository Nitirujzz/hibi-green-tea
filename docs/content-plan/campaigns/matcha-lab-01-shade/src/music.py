"""Original 'lab' bed (synthesised): airy pad + glassy pluck arpeggio + soft pulse + sub, no drums,
carved around the speech band so it sits under the VO. 84 BPM, Am9–Fmaj7–Cmaj7–G6."""
import numpy as np, wave, sys
from scipy.signal import butter, sosfilt, fftconvolve
import timeline
SR=48000; BEAT=60/84; T=timeline.plan()[0][-1]+0.3; N=int(T*SR)
rng=np.random.default_rng(7); L=np.zeros(N); R=np.zeros(N)
hz=lambda n:440*2**((n-69)/12)
def put(b,s,t,g):
    i=int(t*SR); j=min(N,i+len(s))
    if 0<=i<N: b[i:j]+=g*s[:j-i]
def pad(f,d):
    t=np.arange(int((d+1.5)*SR))/SR; env=np.minimum(1,t/1.5)*np.where(t<d,1,np.exp(-(t-d)*2.5))
    s=sum(np.sin(2*np.pi*f*(1+dt)*t+ph) for dt,ph in [(0,0),(0.005,1.1),(-0.005,2.3)])/3
    return (s+0.12*np.sin(2*np.pi*2*f*t))*env*(1+0.08*np.sin(2*np.pi*0.2*t))
def glass(f,d=1.4):   # glassy FM pluck (lab/bubble feel)
    t=np.arange(int(d*SR))/SR; env=np.exp(-t*4)*(1-np.exp(-t*300))
    return np.sin(2*np.pi*f*t+1.2*np.exp(-t*8)*np.sin(2*np.pi*f*3.5*t))*env
def sub(f,d):
    t=np.arange(int(d*SR))/SR; return np.sin(2*np.pi*f*t)*np.minimum(1,t/0.4)*np.clip((d-t)/0.4,0,1)
CH=[[57,60,64,71],[53,57,60,64],[48,55,59,64],[55,59,62,64]]; BS=[45,41,48,43]
per=8*BEAT
for b in range(int(T/per)+1):
    t0=b*per; c=CH[b%4]
    for k,n in enumerate(c):
        put(L,pad(hz(n),per),t0,0.05+0.02*(k%2)); put(R,pad(hz(n),per),t0,0.07-0.02*(k%2))
    put(L,sub(hz(BS[b%4]),per),t0,0.14); put(R,sub(hz(BS[b%4]),per),t0,0.14)
    arp=[c[0]+24,c[2]+12,c[3]+12,c[1]+24,c[2]+24,c[3]+12,c[1]+24,c[2]+12]
    for s in range(16):
        ts=t0+s*BEAT/2+rng.uniform(-0.008,0.008); g=0.028*(1.0 if s%4==0 else 0.6)
        if s%8==7 and rng.random()<0.5: continue
        put(L if s%2 else R,glass(hz(arp[s%8])),ts,g); put(R if s%2 else L,glass(hz(arp[s%8])),ts+0.015,g*0.5)
    for s in range(8):  # soft heartbeat pulse on the beat (filtered, very low)
        t=np.arange(int(0.25*SR))/SR; k=np.sin(2*np.pi*(70+60*np.exp(-t*30))*t)*np.exp(-t*14)
        put(L,k,t0+s*BEAT,0.05); put(R,k,t0+s*BEAT,0.05)
mix=np.stack([L,R],1)
irn=int(2.6*SR); tt=np.arange(irn)/SR
for ch in range(2):
    ir=sosfilt(butter(2,[250,6000],'band',fs=SR,output='sos'),rng.standard_normal(irn))*np.exp(-tt*2.4); ir/=np.sqrt(np.sum(ir**2))
    mix[:,ch]=mix[:,ch]*0.7+0.5*fftconvolve(mix[:,ch],ir)[:N]
mix=sosfilt(butter(2,5000,'low',fs=SR,output='sos'),mix,axis=0)
mix=mix-0.45*sosfilt(butter(2,[1000,3800],'band',fs=SR,output='sos'),mix,axis=0)
mix=sosfilt(butter(1,50,'high',fs=SR,output='sos'),mix,axis=0)
fi=int(0.6*SR); mix[:fi]*=np.linspace(0,1,fi)[:,None]; fo=int(2.0*SR); mix[-fo:]*=np.linspace(1,0,fo)[:,None]
mix/=np.max(np.abs(mix))*1.1
with wave.open("music.wav","wb") as w:
    w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype('<i2').tobytes())
print("ok",round(T,1))
