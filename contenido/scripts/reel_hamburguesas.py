"""Reel estilo 'montaje aesthetic' para la hamburguesería Doña Rulos (marca de ejemplo): clips cortos de video, transición con recuadro,
ráfaga al ritmo y cierre de Gold Studio. Clips de la misma sesión de Pexels (Los Muertos Crew, scratch/bclips), 1080×1920 a 30 fps."""
import os, sys, base64, subprocess, wave
import numpy as np
from PIL import Image, ImageFilter
sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import SCR, F, SP
import imageio_ffmpeg
import reelgen as RG

W, H, FPS = 1080, 1920, 30
HD = f'{SCR}/hd'
OUT = '/home/user/gold-studio-final/reels'
WORK = f'{SCR}/reel-burger'; os.makedirs(WORK, exist_ok=True)
ESP, CRE, MAN = '#2A1A14', '#EFE7DA', '#E6CFA8'

# ---------- capas de texto (HTML -> PNG transparente) ----------
CSS = f'''@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2)}}
@font-face{{font-family:B;font-style:italic;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2)}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2)}}
@font-face{{font-family:A;src:url({F}archivo-black/files/archivo-black-latin-400-normal.woff2)}}
body{{margin:0;background:transparent}} .c{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:J}}'''
BOR, MOS, CREB = '#7A1F1F', '#E0A526', '#F3ECE2'
senora = 'data:image/jpeg;base64,' + base64.b64encode(open(f'{SCR}/ilus/senora-burger.jpg', 'rb').read()).decode()
LAYERS = {
 'hook': '<div class="c"><div style="position:absolute;left:0;right:0;bottom:0;height:900px;background:linear-gradient(transparent,rgba(12,6,4,.66))"></div><div style="position:absolute;left:80px;right:80px;bottom:300px;text-align:center;color:#FFF8EE;font-family:B;font-size:96px;line-height:1.08;text-shadow:0 4px 30px rgba(0,0,0,.55)">Así se vería el reel de <i style="color:#E0A526">Doña Rulos.</i></div></div>',
 'marca': f'<div class="c"><div style="position:absolute;left:0;right:0;bottom:250px;text-align:center;color:{CREB};text-shadow:0 4px 30px rgba(0,0,0,.6)"><div style="font-family:A;font-size:118px;line-height:1;white-space:nowrap">DOÑA RULOS</div><div style="font-size:30px;letter-spacing:.4em;margin-top:18px;color:{MOS}">HAMBURGUESAS A LA PARRILLA</div></div></div>',
 'logo': f'<div class="c" style="background:{BOR};display:flex;flex-direction:column;align-items:center;justify-content:center;color:{CREB}"><div style="font-family:A;font-size:118px;line-height:1;white-space:nowrap">DOÑA RULOS</div><div style="font-size:32px;letter-spacing:.4em;color:{MOS};margin-top:20px">HAMBURGUESAS A LA PARRILLA</div></div>',
 'mascota': f'<div class="c" style="background:{CREB};display:flex;align-items:center;justify-content:center"><img src="{senora}" style="width:1080px;height:1350px;object-fit:cover"></div>',
 **{f'w_{w.lower()}': f'<div class="c"><div style="position:absolute;left:0;right:0;top:{y}px;text-align:center;font-family:A;font-size:150px;line-height:1;color:{CREB};text-shadow:0 7px 0 {BOR},0 10px 40px rgba(0,0,0,.6)">{w}.</div></div>'
    for w, y in [('BACON', 1250), ('CHEDDAR', 1420), ('FUEGO', 1590)]},
 'cierre': (f'<div class="c" style="background:#FAF6EE;color:#1C1A17;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:50px;padding:0 90px;box-sizing:border-box">'
            f'<div style="width:120px;height:120px;color:#C9A34E">{SP}</div>'
            f'<div style="font-family:B;font-size:112px;line-height:1.06">¿Querés un reel así para <i style="color:#8A6A22">tu marca?</i></div>'
            f'<div style="background:#1C1A17;color:#FAF6EE;border-radius:999px;padding:26px 50px;font-size:40px">Escribime · @goldstudio.ba</div></div>'),
}
def render_layers():
    html = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>' + ''.join(f'<div id="{k}" style="width:{W}px;height:{H}px">{v}</div>' for k, v in LAYERS.items())
    open(f'{WORK}/l.html', 'w').write(html)
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});"
          f"await p.goto('file://{WORK}/l.html');await p.evaluate(async()=>{{await document.fonts.ready}});await p.waitForTimeout(300);"
          + ''.join(f"await (await p.$('#{k}')).screenshot({{path:'{WORK}/{k}.png',omitBackground:true}});" for k in LAYERS) + "await b.close();})();")
    open(f'{WORK}/l.js', 'w').write(js)
    subprocess.run(['node', f'{WORK}/l.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    return {k: Image.open(f'{WORK}/{k}.png').convert('RGBA') for k in LAYERS}

# ---------- clips de video con el mismo color dorado ----------
CL = f'{SCR}/bclips'
FFX = imageio_ffmpeg.get_ffmpeg_exe()
_yy, _xx = np.mgrid[0:H, 0:W]
VIG = (1 - .35 * (((_xx / W - .5) ** 2 + (_yy / H - .5) ** 2) / .5))[..., None].astype(np.float32)
def grade(a):
    a = a.astype(np.float32) / 255
    a = a * np.array([1.07, 1.0, 0.84], np.float32) + np.array([.02, .01, -.01], np.float32)
    a = np.clip((a - .5) * 1.08 + .5, 0, 1) * VIG
    return (a * 255).astype(np.uint8)
def clip(cid, start, dur, fx=.5, zoom=1.0):
    """Lee un tramo del clip ya recortado a 9:16 (fx = dónde cortar en los horizontales) y con el color aplicado."""
    n = int(round(dur * FPS))
    sw, sh = int(W * zoom), int(H * zoom)
    vf = (f"scale='if(gt(a,{W}/{H}),-2,{sw})':'if(gt(a,{W}/{H}),{sh},-2)',"
          f"crop={sw}:{sh}:'(in_w-{sw})*{fx}':'(in_h-{sh})/2',scale={W}:{H},fps={FPS}")
    raw = subprocess.run([FFX, '-loglevel', 'error', '-ss', str(start), '-i', f'{CL}/{cid}.mp4', '-t', str(dur + .2), '-vf', vf,
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True, check=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)[:n]
    if len(fr) < n: fr = np.concatenate([fr, np.repeat(fr[-1:], n - len(fr), 0)])
    return [grade(f) for f in fr]
ease = lambda p: p * p * (3 - 2 * p)
def over(base, layer, alpha=1.0, dy=0):
    im = Image.fromarray(base).convert('RGBA'); l = layer
    if alpha < 1: l = layer.copy(); l.putalpha(l.getchannel('A').point(lambda v: int(v * alpha)))
    im.alpha_composite(l, (0, dy)) if dy >= 0 else im.alpha_composite(l.crop((0, -dy, W, H)), (0, 0))
    return np.asarray(im.convert('RGB'))

# ---------- línea de tiempo (como el video de referencia) ----------
L = render_layers()
BEAT = 60 / 100                                                    # 100 bpm: un corte por golpe
TOTAL = 8.6
def punch(fr, k=.07):
    """Golpe de zoom al entrar cada toma (arranca un poco más cerca y se acomoda)."""
    out = []
    for i, f in enumerate(fr):
        z = 1 + k * max(0, 1 - i / 6) ** 2
        if z > 1.001:
            im = Image.fromarray(f); cw, ch = int(W / z), int(H / z)
            f = np.asarray(im.crop(((W - cw) // 2, (H - ch) // 2, (W - cw) // 2 + cw, (H - ch) // 2 + ch)).resize((W, H)))
        out.append(f)
    return out
def foto(name, n, z0=1.0, z1=1.0):
    im = Image.open(f'{SCR}/burger/{name}.jpg').convert('RGB'); iw, ih = im.size; tw = ih * 9 / 16
    im = grade(np.asarray(im.crop((int((iw - tw) / 2), 0, int((iw + tw) / 2), ih)).resize((W, H), Image.LANCZOS)))
    if z0 == z1: return [im] * n
    out = []
    for i in range(n):
        z = z0 + (z1 - z0) * i / max(1, n - 1); cw, ch = int(W / z), int(H / z)
        out.append(np.asarray(Image.fromarray(im).crop(((W - cw) // 2, (H - ch) // 2, (W - cw) // 2 + cw, (H - ch) // 2 + ch)).resize((W, H))))
    return out
def frames():
    nb = lambda b: int(round(b * BEAT * FPS))                          # cuadros de b golpes
    out = []
    out += punch(clip(8477334, 3.5, 2 * BEAT, fx=.45))                # llamas con la pinza (2 golpes)
    out += punch(clip(8477329, 2.0, BEAT, fx=.4))                     # la parrilla con la carne
    out += punch(clip(8477267, 3.0, BEAT, fx=.55))                    # la bandeja de medallones
    out += punch(clip(8477404, 5.0, BEAT, fx=.6))                     # el armado
    out += punch(clip(8477405, 3.0, BEAT, fx=.45))                    # la rúcula arriba
    r = []                                                             # ráfaga: 8 tomas en 2 golpes
    for item in [('foto', 'prod_flota'), (8477262, 1.5, .5), ('foto', 'prod_manos'), 'logo', (8477403, 2.0, .5), 'mascota', ('foto', 'prod_bacon'), (8477408, 11.0, .5)]:
        n = nb(.25)
        if isinstance(item, str): r += [np.asarray(L[item].convert('RGB'))] * n
        elif item[0] == 'foto': r += foto(item[1], n)
        else: r += clip(item[0], item[1], n / FPS, fx=item[2])
    out += r
    hero = foto('prod_flota', nb(3), 1.0, 1.1)                         # la hamburguesa flotando + palabras al golpe
    words = ['w_bacon', 'w_cheddar', 'w_fuego']
    for i, f in enumerate(hero):
        for k, w in enumerate(words):
            t0 = nb(k)
            if i >= t0:
                p = min(1, (i - t0) / 3); dy = int((1 - ease(p)) * -60)
                f = over(f, L[w], ease(p), dy)
        out.append(f)
    fin = punch(clip(8477410, 3.5, 2 * BEAT, fx=.5))                  # hamburguesitas y cerveza + la marca
    for i, f in enumerate(fin): out.append(over(f, L['marca'], ease(min(1, i / 8))))
    blank = np.full((H, W, 3), (250, 246, 238), np.uint8)              # cierre de Gold Studio
    n_end = int(TOTAL * FPS) - len(out)
    for i in range(n_end):
        p = i / n_end; s = ease(min(1, p / .15)); out.append(over(blank, L['cierre'], s, int((1 - s) * 140)))
    for i in range(int(1.8 * FPS)):                                    # hook en pantalla desde el segundo 0
        t = i / FPS; al = min(1, t / .2) * (1 if t < 1.5 else max(0, (1.8 - t) / .3))
        out[i] = over(out[i], L['hook'], al)
    return out

# ---------- música: beat de hip hop con onda (bombo, aplauso, hi-hats, bajo y un riff), sube en la ráfaga y explota en el final ----------
def audio(path, bpm=100):
    sr = RG.SR; n = int(sr * TOTAL); mix = np.zeros((n, 2)); b = 60 / bpm
    rng = np.random.default_rng(11)
    def put(x, t, g=1.0, pan=0.0):
        i = int(t * sr)
        if i >= n or t < 0: return
        x = x[:n - i] * g; mix[i:i + len(x), 0] += x * (1 - pan) ; mix[i:i + len(x), 1] += x * (1 + pan)
    T = lambda d: np.arange(int(sr * d)) / sr
    t = T(.45); kick = np.tanh(2.2 * np.sin(2 * np.pi * (48 + 110 * np.exp(-t * 28)) * t) * np.exp(-t * 7)) * .9
    t = T(.25); clap = sum(rng.standard_normal(len(t)) * np.exp(-(t - d).clip(0) * 38) * (t >= d) for d in (0, .008, .017)) * .16
    t = T(.06); hat = rng.standard_normal(len(t)) * np.exp(-t * 90) * .07
    t = T(.35); ohat = rng.standard_normal(len(t)) * np.exp(-t * 14) * .045
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    def bass(m, d):
        t = T(d); f = hz(m)
        return np.tanh(1.8 * (np.sin(2 * np.pi * f * t) + .3 * np.sin(4 * np.pi * f * t))) * (1 - np.exp(-t * 90)) * np.exp(-t * 2.4) * .42
    def stab(ms, d=.22):                                                 # acorde tipo bronces/órgano, cortito
        t = T(d); env = (1 - np.exp(-t * 200)) * np.exp(-t * 9)
        return sum(np.sign(np.sin(2 * np.pi * hz(m) * t)) * .25 + np.sin(2 * np.pi * hz(m) * t) for m in ms) * env * .045
    riff = [(0, 40), (.75, 40), (1.5, 43), (2.5, 45), (3, 43), (3.5, 38)]   # en golpes: un bajo con swing (Mi menor)
    bar = 4 * b; t0 = 0.0; k = 0
    while t0 < TOTAL - 2.0:
        for q in range(4):
            if q in (0, 2): put(kick, t0 + q * b)
            if q in (1, 3): put(clap, t0 + q * b, 1.0, .1)
        put(kick, t0 + 2.5 * b, .7)
        for e in range(8): put(hat, t0 + e * b / 2 + (.06 if e % 2 else 0), .9 if e % 2 else 1.2, -.25)
        put(ohat, t0 + 3.5 * b, 1, .25)
        for bt, m in riff: put(bass(m, b * .7), t0 + bt * b)
        for bt in (.5, 2.0, 3.0): put(stab([64, 67, 71] if k % 2 == 0 else [62, 66, 69]), t0 + bt * b, 1, .3)
        t0 += bar; k += 1
    r0 = 3.6 - 2 * b; t = T(2 * b)                                       # subida antes de la ráfaga
    put(rng.standard_normal(len(t)) * (t / t[-1]) ** 2 * .1, r0, 1, 0)
    for i in range(8): put(hat, 3.6 + i * b / 4, 1.4)                     # hi-hats rápidos en la ráfaga
    for i in range(3): put(kick, 4.8 + i * b, 1.2); put(bass(28, b * .9), 4.8 + i * b, 1.1)   # golpes de las palabras
    t = T(1.8); put(np.sin(2 * np.pi * hz(52) * t) * np.exp(-t * 2) * .2 + stab([64, 67, 71, 76], 1.8) * 2, 6.6)   # final
    crackle = (rng.random(n) > .9993) * rng.standard_normal(n) * .08     # un poco de vinilo
    mix[:, 0] += crackle; mix[:, 1] += crackle
    tt = np.arange(n) / sr; env = np.clip(tt / .05, 0, 1) * np.clip((TOTAL - tt) / .7, 0, 1)
    mix *= env[:, None]; mix = mix / max(1e-6, np.abs(mix).max()) * .89
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((mix * 32767).astype('<i2').tobytes())

def build(name='reel-dona-rulos-hamburguesas'):
    os.makedirs(OUT, exist_ok=True); wav = f'{WORK}/a.wav'; audio(wav)
    out = f'{OUT}/{name}.mp4'; ff = imageio_ffmpeg.get_ffmpeg_exe()
    proc = subprocess.Popen([ff, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                             '-i', wav, '-c:v', 'libx264', '-profile:v', 'main', '-level', '4.1', '-pix_fmt', 'yuv420p', '-crf', '21', '-preset', 'medium', '-c:a', 'aac', '-b:a', '160k', '-ac', '2', '-ar', '48000',
                             '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for f in frames():
        proc.stdin.write(np.ascontiguousarray(f).tobytes())
    proc.stdin.close(); proc.wait()
    return out

if __name__ == '__main__':
    print(build())
