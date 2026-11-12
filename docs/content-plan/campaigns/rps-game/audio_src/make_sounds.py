"""Original, synthesised game audio (no samples, no third-party music) for the Hibi & Capy RPS game.
Writes public/game/sfx/*.mp3: a seamless cute BGM loop and short SFX."""
import numpy as np, subprocess, wave, os
from scipy.signal import butter, sosfilt, fftconvolve
SR = 44100
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../../../public/game/sfx')
rng = np.random.default_rng(5)
hz = lambda n: 440 * 2 ** ((n - 69) / 12)
def t_(d): return np.arange(int(d * SR)) / SR
def env(d, a=0.005, dec=6.0): t = t_(d); return np.minimum(1, t / a) * np.exp(-t * dec)
def glock(f, d=1.0, dec=4.0):
    t = t_(d); return (np.sin(2*np.pi*f*t) + .35*np.sin(2*np.pi*2.76*f*t)*np.exp(-t*9) + .15*np.sin(2*np.pi*5.4*f*t)*np.exp(-t*16)) * env(d, .002, dec)
def pluck(f, d=0.8):
    n = int(d*SR); p = max(2, int(SR/f)); buf = rng.uniform(-1, 1, p); out = np.zeros(n)
    for i in range(n): out[i] = buf[i % p]; buf[i % p] = .5*(buf[i % p] + buf[(i+1) % p]) * .995
    return out * np.exp(-t_(d)*3)
def noise(d, lo, hi, dec): return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), rng.standard_normal(int(d*SR))) * np.exp(-t_(d)*dec)
def put(buf, s, t, g=1.0):
    i = int(t*SR); j = min(len(buf), i + len(s)); buf[i:j] += g * s[:j-i]
def norm(x, peak=.89): m = np.abs(x).max(); return x / m * peak if m else x
def save(name, x, stereo=False, br='96k'):
    x = norm(x); fn = f'/tmp/{name}.wav'
    ch = 2 if stereo else 1
    data = (np.clip(x, -1, 1) * 32767).astype('<i2')
    with wave.open(fn, 'wb') as w: w.setnchannels(ch); w.setsampwidth(2); w.setframerate(SR); w.writeframes(data.tobytes())
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', fn, '-c:a', 'libmp3lame', '-b:a', br, f'{OUT}/{name}.mp3'], check=True); os.remove(fn)

# ---------- BGM: 96 BPM, 8 bars C–Am–F–G, seamless (reverb wrapped around the loop) ----------
BPM = 96; B = 60 / BPM; bars = 8; L = int(bars * 4 * B * SR)
Lc = np.zeros(L); Rc = np.zeros(L)
CH = [[60, 64, 67], [57, 60, 64], [53, 57, 60], [55, 59, 62]]
MEL = [76, 79, 81, 79, 76, 74, 72, 74,  72, 76, 79, 76, 77, 76, 74, 72,
       76, 79, 84, 83, 81, 79, 77, 76,  74, 76, 77, 79, 76, 74, 72, None]
cache = {}
def pl(n):
    if n not in cache: cache[n] = pluck(hz(n), 0.9)
    return cache[n]
def wrap_put(buf, s, t, g):
    i = int(t*SR) % L
    for k in range(0, len(s)):
        buf[(i+k) % L] += g * s[k]
for b in range(bars):
    t0 = b*4*B; c = CH[b % 4]
    for off, g in [(0, 1), (1, .6), (1.5, .55), (2.5, .55), (3, .7), (3.5, .5)]:
        for j, n in enumerate(c): wrap_put(Lc, pl(n), t0 + off*B + j*.01, .09*g); wrap_put(Rc, pl(n), t0 + off*B + j*.012, .07*g)
    for q in range(4):
        n = MEL[(b*4 + q) % len(MEL)]
        if n: s = glock(hz(n), 1.2, 3.2); wrap_put(Lc, s, t0 + q*B, .06); wrap_put(Rc, s, t0 + q*B + .004, .08)
    bass = np.sin(2*np.pi*hz(c[0]-24)*t_(4*B)) * np.minimum(1, t_(4*B)/.05) * np.exp(-t_(4*B)*.6)
    wrap_put(Lc, bass, t0, .18); wrap_put(Rc, bass, t0, .18)
    for s8 in range(8):
        sh = noise(.06, 5000, 11000, 60); wrap_put(Lc, sh, t0 + s8*B/2, .03 if s8 % 2 else .015); wrap_put(Rc, sh, t0 + s8*B/2 + .003, .03 if s8 % 2 else .015)
mix = np.stack([Lc, Rc], 1)
ir = sosfilt(butter(2, [300, 6000], 'band', fs=SR, output='sos'), rng.standard_normal(int(1.4*SR))) * np.exp(-t_(1.4)*4)
ir /= np.sqrt((ir**2).sum())
for ch in range(2):   # circular reverb so the loop point is seamless
    wet = fftconvolve(np.tile(mix[:, ch], 2), ir)[L:2*L]
    mix[:, ch] = mix[:, ch]*.82 + wet*.28
save('bgm', mix, stereo=True, br='128k')

# ---------- SFX ----------
save('tap', np.concatenate([np.sin(2*np.pi*np.cumsum(900 + 600*np.exp(-t_(.09)*50))/SR) * env(.09, .002, 40)]))
def tick(f, d=.12): return (np.sin(2*np.pi*f*t_(d)) * env(d, .001, 35) + noise(d, 1500, 5000, 60)*.5)
save('beat', tick(880)); save('beat2', tick(1046))
th = np.sin(2*np.pi*np.cumsum(70 + 140*np.exp(-t_(.35)*25))/SR) * env(.35, .002, 9)
tk = np.pad(tick(1318, .2), (0, len(th)))[:len(th)]
save('shoot', th*.9 + tk*.7)
wh = noise(.35, 600, 6000, 0) * np.sin(np.pi*np.linspace(0, 1, int(.35*SR)))**2
cl = noise(.25, 800, 4000, 30)
clp = np.pad(cl, (int(.28*SR), 0))
n = max(len(wh), len(clp)); save('clash', np.pad(wh*.6, (0, n-len(wh))) + np.pad(clp, (0, n-len(clp))))
x = np.zeros(int(1.6*SR))
for i, n in enumerate([72, 76, 79, 84]): put(x, glock(hz(n), 1.1, 3.5), i*.09, 1)
for i in range(6): put(x, glock(hz(96 + rng.integers(0, 5)), .5, 8), .45 + i*.07, .35)
save('win', x)
t = t_(1.3); f = np.concatenate([np.linspace(523, 440, len(t)//2), np.linspace(440, 330, len(t) - len(t)//2)]) * (1 + .03*np.sin(2*np.pi*6*t))
wah = np.sin(2*np.pi*np.cumsum(f)/SR) + .3*np.sin(2*np.pi*2*np.cumsum(f)/SR)
save('lose', wah * np.minimum(1, t/.02) * np.exp(-t*1.6) * (.6 + .4*np.abs(np.sin(2*np.pi*1.5*t))))
t = t_(.6); f = 300 + 250*np.sin(2*np.pi*7*t)*np.exp(-t*5)
save('tie', np.sin(2*np.pi*np.cumsum(f)/SR) * env(.6, .003, 5))
x = np.zeros(int(1.2*SR))
for i in range(9): put(x, glock(hz(88 + rng.integers(0, 9)), .6, 7), i*.06, .5 + .5*rng.random())
save('coupon', x)
x = np.zeros(int(2.6*SR))
for i, n in enumerate([67, 72, 76, 79]): put(x, glock(hz(n), 1.4, 2.5), i*.11, 1)
for n in [72, 76, 79, 84]: put(x, glock(hz(n), 2.0, 1.4), .5, .7)
for i in range(14): put(x, glock(hz(91 + rng.integers(0, 12)), .5, 8), .7 + i*.08, .35)
for i in range(3): put(x, noise(.2, 900, 5000, 25), .5 + i*.18, .5)
save('grand', x)
print('ok', sorted(os.listdir(OUT)))
