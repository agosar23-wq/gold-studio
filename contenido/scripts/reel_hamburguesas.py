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
TOTAL = 7.6
def frames():
    out = []
    out += clip(8477334, 3.5, 1.2, fx=.45)                          # llamas con la pinza
    b = clip(8477263, 2.0, 1.6, fx=.5)                             # la parrilla prendida (sigue de fondo en el recuadro)
    out += b[:30]
    ins = clip(8477404, 5.0, .6, fx=.6)                             # armado de las hamburguesas, en un recuadro
    for i in range(18):
        p = i / 17; s = ease(min(1, p * 2.2)); bw, bh = int(560 + 60 * p), int(840 + 90 * p)
        bg = Image.fromarray((b[30 + i].astype(np.float32) * .75).astype(np.uint8))
        im = Image.fromarray(ins[i]).resize((bw, bh))
        bg.paste(im, ((W - bw) // 2, int(H / 2 - bh / 2 + (1 - s) * 260)), Image.new('L', (bw, bh), int(255 * s)))
        out.append(np.asarray(bg))
    out += clip(8477267, 3.0, .4, fx=.55)                           # la bandeja de medallones
    for item in [(8477262, 1.5, .5), (8477405, 3.0, .45), ('foto', 'prod_flota'), 'logo', ('foto', 'prod_manos'), (8477329, 2.0, .4), 'mascota', ('foto', 'prod_bacon')]:
        if isinstance(item, str): out += [np.asarray(L[item].convert('RGB'))] * 4      # ráfaga: 4 cuadros (1/8 s) cada una
        elif item[0] == 'foto':   # fotos de producto que pasó Agos (la misma hamburguesa de bacon y cheddar)
            im = Image.open(f'{SCR}/burger/{item[1]}.jpg').convert('RGB'); iw, ih = im.size; tw = ih * 9 / 16
            im = im.crop((int((iw - tw) / 2), 0, int((iw + tw) / 2), ih)).resize((W, H), Image.LANCZOS)
            out += [grade(np.asarray(im))] * 4
        else: out += clip(item[0], item[1], 4 / FPS, fx=item[2])
    fin = clip(8477410, 3.5, 1.4, fx=.5)                            # hamburguesitas y cerveza + la marca
    for i, f in enumerate(fin): out.append(over(f, L['marca'], ease(min(1, max(0, (i / 41 - .15) / .4)))))
    blank = np.full((H, W, 3), (250, 246, 238), np.uint8)           # cierre de Gold Studio
    for i in range(int(2.0 * FPS)):
        p = i / (2.0 * FPS); s = ease(min(1, p / .18)); out.append(over(blank, L['cierre'], s, int((1 - s) * 140)))
    for i in range(int(1.9 * FPS)):                                 # hook en pantalla desde el segundo 0
        t = i / FPS; al = min(1, t / .25) * (1 if t < 1.6 else max(0, (1.9 - t) / .3))
        out[i] = over(out[i], L['hook'], al)
    return out

# ---------- música: base lo-fi suave (piano eléctrico, bajo y ritmo), sin efectos en los cortes ----------
def audio(path, bpm=120):
    sr = RG.SR; n = int(sr * TOTAL); mix = np.zeros(n); beat = 60 / bpm
    def put(x, t, g=1.0):
        i = int(t * sr)
        if i >= n: return
        x = x[:n - i]; mix[i:i + len(x)] += x * g
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    def keys(notes, d, g=.12):              # piano eléctrico: armónicos con caída suave y un poco de trémolo
        t = np.arange(int(sr * d)) / sr
        env = (1 - np.exp(-t * 60)) * np.exp(-t * 1.4)
        trem = 1 + .08 * np.sin(2 * np.pi * 4.5 * t)
        return sum((np.sin(2 * np.pi * hz(m) * t) + .35 * np.sin(4 * np.pi * hz(m) * t) + .1 * np.sin(6 * np.pi * hz(m) * t)) for m in notes) * env * trem * g
    def bass(m, d, g=.3):
        t = np.arange(int(sr * d)) / sr
        return np.sin(2 * np.pi * hz(m) * t) * (1 - np.exp(-t * 80)) * np.exp(-t * 2.2) * g
    tk = np.arange(int(sr * .3)) / sr
    kick = np.sin(2 * np.pi * (50 + 70 * np.exp(-tk * 35)) * tk) * np.exp(-tk * 12) * .55
    rng = np.random.default_rng(7)
    rim = rng.standard_normal(int(sr * .08)) * np.exp(-np.arange(int(sr * .08)) / sr * 60) * .07
    shk = rng.standard_normal(int(sr * .04)) * np.exp(-np.arange(int(sr * .04)) / sr * 120) * .035
    prog = [([65, 69, 72, 76], 41), ([64, 67, 71, 74], 40), ([62, 65, 69, 72], 38), ([60, 64, 67, 71], 36)]   # Fmaj7 Em7 Dm7 Cmaj7
    bar = 4 * beat; t0 = 0.0; k = 0
    while t0 < TOTAL:
        ch, root = prog[k % 4]
        put(keys(ch, bar + .6), t0); put(keys([ch[-1] + 12], beat * 1.5, .05), t0 + beat * 2.5)
        put(bass(root, beat * 1.8), t0); put(bass(root + 7, beat * 1.2), t0 + beat * 2)
        for q in range(4):
            if q in (0, 2): put(kick, t0 + q * beat)
            else: put(rim, t0 + q * beat)
        for e in range(8): put(shk, t0 + e * beat / 2 + beat / 4, .8 if e % 2 else .5)
        t0 += bar; k += 1
    tt = np.arange(n) / sr
    mix *= np.clip(tt / .3, 0, 1) * np.clip((TOTAL - tt) / .8, 0, 1)
    mix = mix / max(1e-6, np.abs(mix).max()) * .85
    with wave.open(path, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((mix * 32767).astype('<i2').tobytes())

def build(name='reel-dona-rulos-hamburguesas'):
    os.makedirs(OUT, exist_ok=True); wav = f'{WORK}/a.wav'; audio(wav)
    out = f'{OUT}/{name}.mp4'; ff = imageio_ffmpeg.get_ffmpeg_exe()
    proc = subprocess.Popen([ff, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                             '-i', wav, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-preset', 'medium', '-c:a', 'aac', '-b:a', '160k',
                             '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for f in frames():
        proc.stdin.write(np.ascontiguousarray(f).tobytes())
    proc.stdin.close(); proc.wait()
    return out

if __name__ == '__main__':
    print(build())
