import numpy as np, wave
SR = 44100; T2 = 2.4; STEP = 1.3; T3 = T2 + 5 * STEP + 0.2; DUR = T3 + 2.6
out = np.zeros(int(SR * DUR) + SR)
rng = np.random.default_rng(7)
def tt(d): return np.arange(int(SR * d)) / SR
def add(sig, t):
    i = int(t * SR); out[i:i + len(sig)] += sig[:len(out) - i]
def lowpass_sweep(x, f0, f1):
    y = np.zeros_like(x); f = np.linspace(0, 1, len(x)); fc = f0 + (f1 - f0) * np.sin(np.pi * f)  # sube y baja
    a = np.exp(-2 * np.pi * fc / SR); s = 0.0
    for n in range(len(x)): s = a[n] * s + (1 - a[n]) * x[n]; y[n] = s
    return y
def whoosh(d=0.45, f0=250, f1=2800, amp=0.5):
    t = tt(d); n = rng.standard_normal(len(t))
    env = np.sin(np.pi * t / d) ** 2
    y = lowpass_sweep(n, f0, f1) * env
    return amp * y / (np.abs(y).max() + 1e-9)
def tick(amp=0.06):
    t = tt(0.04); return amp * np.sin(2 * np.pi * 1900 * t) * np.exp(-t / 0.008)
def tap(amp=0.35):
    t = tt(0.09)
    body = np.sin(2 * np.pi * 180 * t) * np.exp(-t / 0.018) + 0.5 * np.sin(2 * np.pi * 420 * t) * np.exp(-t / 0.01)
    click = rng.standard_normal(len(t)) * np.exp(-t / 0.002) * 0.3
    return amp * (body + click)
def chime(amp=0.22):
    y = np.zeros(int(SR * 1.8))
    for k, (f, dt) in enumerate([(1318.5, 0), (1975.5, .06), (2637, .12), (3951, .2)]):
        t = tt(1.8 - dt); s = np.sin(2 * np.pi * f * t) * np.exp(-t / (0.5 - k * 0.07)) * (1 - 0.15 * k)
        i = int(dt * SR); y[i:i + len(s)] += s
    return amp * y / np.abs(y).max()

# escena 1: palabras + celular que sube
for i in range(9): add(tick(), 0.2 + i * 0.08)
add(whoosh(0.8, 120, 1200, 0.45), 0.6)
# escena 2
add(whoosh(0.45, 200, 2200, 0.35), T2 - 0.1)
for i in range(1, 5):
    s = T2 + i * STEP
    add(tap(), s - 0.52)
    add(whoosh(0.4, 300, 3200, 0.42), s - 0.42)
# escena 3: brillo final
add(whoosh(0.5, 200, 2200, 0.3), T3 - 0.1)
add(chime(), T3 + 0.15)
add(tap(0.25), T3 + 0.6)

out = out[:int(SR * DUR)]
fade = int(0.3 * SR); out[-fade:] *= np.linspace(1, 0, fade)
out = out / np.abs(out).max() * 0.85
pcm = (out * 32767).astype('<i2')
st = np.column_stack([pcm, pcm]).ravel()
with wave.open('reel2-sfx.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(st.tobytes())
print('ok', len(out) / SR)
