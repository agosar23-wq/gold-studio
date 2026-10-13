"""Música original para reels (sin derechos): house suave a 120 BPM con bajo, acordes, arpegio y batería.
musica(beats, intro=2) -> np.array mono 44.1 kHz. Todo sintetizado con numpy."""
import numpy as np

SR = 44100
BPM = 120
BEAT = 60 / BPM
rng = np.random.default_rng(7)

def _t(d): return np.arange(int(SR * d)) / SR
def hz(n): return 440 * 2 ** ((n - 69) / 12)          # nota MIDI -> Hz

def lowpass(x, fc):
    a = np.exp(-2 * np.pi * fc / SR); y = np.empty_like(x); s = 0.0
    for i in range(len(x)): s = a * s + (1 - a) * x[i]; y[i] = s
    return y

def kick():
    t = _t(0.35); f = 50 + 110 * np.exp(-t / 0.035)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.13) + 0.15 * np.sin(2 * np.pi * 1800 * t) * np.exp(-t / 0.004)
def clap():
    t = _t(0.2); n = rng.standard_normal(len(t)); n = n - lowpass(n, 900); n = lowpass(n, 5000)
    env = np.exp(-t / 0.05) * (1 + 0.6 * np.exp(-((t - 0.012) / 0.003) ** 2) + 0.5 * np.exp(-((t - 0.024) / 0.003) ** 2))
    return n * env * 1.6
def hat(open_=False):
    d = 0.18 if open_ else 0.05; t = _t(d); n = rng.standard_normal(len(t)); n = n - lowpass(n, 7000)
    return n * np.exp(-t / (0.06 if open_ else 0.012))
def bass(n, d):
    t = _t(d); f = hz(n)
    y = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)
    return y * np.minimum(1, t / 0.008) * np.exp(-t / (d * 0.9))
def pad(notes, d):
    t = _t(d); y = np.zeros(len(t))
    for n in notes:
        for det in (-0.08, 0.0, 0.08):
            f = hz(n + det)
            y += np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t + 1) + 0.12 * np.sin(6 * np.pi * f * t + 2)
    env = np.minimum(1, t / 0.25) * np.minimum(1, (d - t) / 0.3)
    return y * env / (3 * len(notes))
def pluck(n, d=0.35):
    t = _t(d); f = hz(n)
    y = np.sin(2 * np.pi * f * t) + 0.5 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.05) + 0.25 * np.sin(6 * np.pi * f * t) * np.exp(-t / 0.03)
    return y * np.exp(-t / 0.12) * np.minimum(1, t / 0.003)

# Am - F - C - G (suave y luminoso)
CHORDS = [(57, [69, 72, 76]), (53, [65, 69, 72]), (48, [64, 67, 72]), (55, [67, 71, 74])]

def musica(beats, intro=2, outro=4):
    """beats: largo total en tiempos. intro: tiempos sin batería al principio. outro: últimos tiempos solo acordes."""
    total = int(SR * (beats * BEAT + 2.5)); L = {k: np.zeros(total) for k in ('drums', 'bass', 'pad', 'arp')}
    def add(trk, sig, t, g=1.0):
        i = int(t * SR); L[trk][i:i + len(sig)] += g * sig[:max(0, total - i)]
    K, C, H, HO = kick(), clap(), hat(), hat(True)
    for b in range(beats + 4):
        t = b * BEAT; bar = b // 4; root, notes = CHORDS[bar % 4]
        drums = intro <= b < beats - outro
        if b % 4 == 0 and b < beats: add('pad', pad(notes, 4 * BEAT + 0.4), t, 0.9)
        if drums:
            add('drums', K, t, 1.0)
            if b % 2 == 1: add('drums', C, t, 0.35)
            add('drums', H, t + BEAT / 2, 0.22); add('drums', H, t + BEAT / 4, 0.08); add('drums', H, t + 3 * BEAT / 4, 0.08)
            if b % 4 == 3: add('drums', HO, t + BEAT / 2, 0.15)
            add('bass', bass(root - 12, BEAT * 0.45), t + BEAT / 2, 0.6)      # bajo en el contratiempo
            if b % 2 == 0: add('bass', bass(root, BEAT * 0.3), t + 3 * BEAT / 4, 0.3)
        if b < beats:
            arp = [notes[0] + 12, notes[1] + 12, notes[2] + 12, notes[1] + 12]
            for j in range(4):
                if intro <= b or j % 2 == 0: add('arp', pluck(arp[j]), t + j * BEAT / 4, 0.16 if drums else 0.12)
    # sidechain: los acordes y el bajo "respiran" con el bombo
    duck = np.ones(total)
    for b in range(intro, beats - outro):
        i = int(b * BEAT * SR); n = int(0.22 * SR); duck[i:i + n] = np.minimum(duck[i:i + n], 0.35 + 0.65 * (np.arange(n) / n) ** 0.7)
    mix = L['drums'] * 0.9 + (L['bass'] * 0.8 + L['pad'] * 0.55 + L['arp'] * 0.8) * duck
    # final: deja sonar el último acorde y se apaga
    end = int(beats * BEAT * SR); fade = int(2.5 * SR)
    mix[end:end + fade] *= np.linspace(1, 0, len(mix[end:end + fade]))
    mix[end + fade:] = 0
    return mix / (np.abs(mix).max() + 1e-9)

if __name__ == '__main__':
    import wave, sys
    m = musica(44)
    pcm = (m * 0.9 * 32767).astype('<i2')
    with wave.open(sys.argv[1] if len(sys.argv) > 1 else '/tmp/m.wav', 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
