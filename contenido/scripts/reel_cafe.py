"""Reel estilo 'montaje aesthetic' de cafetería para Tostado (marca de ejemplo): tomas lentas, transición con recuadro,
ráfaga de fotos al ritmo y cierre de Gold Studio. Fotos de la misma sesión de Pexels (scratch/hd), 1080×1920 a 30 fps."""
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
WORK = f'{SCR}/reel-cafe'; os.makedirs(WORK, exist_ok=True)
ESP, CRE, MAN = '#2A1A14', '#EFE7DA', '#E6CFA8'

# ---------- capas de texto (HTML -> PNG transparente) ----------
CSS = f'''@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2)}}
@font-face{{font-family:B;font-style:italic;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2)}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2)}}
@font-face{{font-family:P;src:url({F}playfair-display/files/playfair-display-latin-700-normal.woff2)}}
body{{margin:0;background:transparent}} .c{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:J}}'''
nutria = 'data:image/jpeg;base64,' + base64.b64encode(open(f'{SCR}/ilus/nutria-taza.jpg', 'rb').read()).decode()
LAYERS = {
 'hook': '<div class="c"><div style="position:absolute;left:0;right:0;bottom:0;height:900px;background:linear-gradient(transparent,rgba(20,10,6,.62))"></div><div style="position:absolute;left:80px;right:80px;bottom:300px;text-align:center;color:#FFF8EE;font-family:B;font-size:96px;line-height:1.08;text-shadow:0 4px 30px rgba(0,0,0,.55)">Así se vería el reel de <i style="color:#E6CFA8">Tostado.</i></div></div>',
 'marca': f'<div class="c"><div style="position:absolute;left:0;right:0;bottom:250px;text-align:center;color:{CRE};text-shadow:0 4px 30px rgba(0,0,0,.5)"><div style="font-family:P;font-size:150px">Tostado.</div><div style="font-size:30px;letter-spacing:.4em;margin-top:6px;color:{MAN}">CAFÉ DE ESPECIALIDAD</div></div></div>',
 'logo': f'<div class="c" style="background:{ESP};display:flex;flex-direction:column;align-items:center;justify-content:center;color:{CRE}"><div style="font-family:P;font-size:190px">Tostado.</div><div style="font-size:34px;letter-spacing:.4em;color:{MAN}">CAFÉ DE ESPECIALIDAD</div></div>',
 'nutria': f'<div class="c" style="background:#4A2A1C;display:flex;align-items:center;justify-content:center"><img src="{nutria}" style="width:1080px"></div>',
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

# ---------- fotos con el mismo color dorado ----------
def grade(im):
    a = np.asarray(im.convert('RGB')).astype(np.float32) / 255
    a = a * np.array([1.07, 1.0, 0.84]) + np.array([.02, .01, -.01])          # cálido/dorado
    a = np.clip((a - .5) * 1.08 + .5, 0, 1)                                       # un poco de contraste
    yy, xx = np.mgrid[0:a.shape[0], 0:a.shape[1]]
    v = 1 - .35 * (((xx / a.shape[1] - .5) ** 2 + (yy / a.shape[0] - .5) ** 2) / .5)  # viñeta suave
    return Image.fromarray((np.clip(a * v[..., None], 0, 1) * 255).astype('uint8'))
_cache = {}
def photo(pid, fx=.5, fy=.5):
    """Recorte 9:16 grande (para poder hacer zoom) con el color aplicado."""
    key = (pid, fx, fy)
    if key not in _cache:
        im = Image.open(f'{HD}/{pid}.jpg')
        iw, ih = im.size; tw = ih * 9 / 16
        if tw <= iw: box = (int((iw - tw) * fx), 0, int((iw - tw) * fx + tw), ih)
        else:
            th = iw * 16 / 9; box = (0, int((ih - th) * fy), iw, int((ih - th) * fy + th))
        _cache[key] = grade(im.crop(box).resize((int(W * 1.25), int(H * 1.25)), Image.LANCZOS))
    return _cache[key]
def kb(im, p, z0=1.0, z1=1.08, dx=0, dy=0):
    """Ken Burns: zoom de z0 a z1 (p de 0 a 1) con un leve desplazamiento."""
    z = z0 + (z1 - z0) * p
    bw, bh = im.size; cw, ch = W * 1.25 / z / 1.25 * 1.0, H / z
    cw = bw / 1.25 / z; ch = bh / 1.25 / z
    cx = bw / 2 + dx * p * bw; cy = bh / 2 + dy * p * bh
    return im.crop((int(cx - cw / 2), int(cy - ch / 2), int(cx + cw / 2), int(cy + ch / 2))).resize((W, H), Image.BILINEAR)
ease = lambda p: p * p * (3 - 2 * p)

# ---------- línea de tiempo ----------
L = render_layers()
SHOTS = [  # (inicio, fin, tipo, datos)
    (0.00, 1.00, 'kb', dict(pid=4792683, z0=1.0, z1=1.09, dy=-.02)),
    (1.00, 2.00, 'kb', dict(pid=4792700, z0=1.04, z1=1.12, fy=.4)),
    (2.00, 2.62, 'inset', dict(bg=4792700, pid=4792692)),
    (2.62, 3.00, 'kb', dict(pid=4792693, z0=1.0, z1=1.05)),
]
FLASH = [('p', 4792689, .45), ('p', 4792694, .5), ('p', 4792695, .6), ('logo',), ('p', 4792685, .5), ('p', 4792696, .45), ('nutria',), ('p', 4792684, .4)]
for i, f in enumerate(FLASH):
    SHOTS.append((3.0 + i * .125, 3.125 + i * .125, 'flash', f))
SHOTS += [(4.00, 5.40, 'final', dict(pid=4792699)), (5.40, 7.40, 'cierre', {})]
TOTAL = 7.4

def frame(t):
    for (a, b, k, d) in SHOTS:
        if a <= t < b: break
    p = (t - a) / (b - a)
    if k == 'kb':
        img = kb(photo(d['pid'], fy=d.get('fy', .5)), ease(p), d.get('z0', 1), d.get('z1', 1.08), dy=d.get('dy', 0)).convert('RGBA')
    elif k == 'inset':      # la toma siguiente aparece en un recuadro sobre la anterior
        img = kb(photo(d['bg'], fy=.4), 1, 1.12, 1.16).convert('RGBA')
        img = Image.blend(img, Image.new('RGBA', img.size, (20, 12, 8, 255)), .25)
        s = ease(min(1, p * 2.2)); bw, bh = int(560 + 60 * p), int(840 + 90 * p)
        ins = kb(photo(d['pid']), p, 1.05, 1.0).resize((bw, bh))
        y = int(H / 2 - bh / 2 + (1 - s) * 260)
        mask = Image.new('L', (bw, bh), int(255 * s))
        img.paste(ins, ((W - bw) // 2, y), mask)
    elif k == 'flash':
        img = L[d[0]].copy() if d[0] in ('logo', 'nutria') else kb(photo(d[1], fx=d[2]), p, 1.03, 1.06).convert('RGBA')
    elif k == 'final':
        img = kb(photo(d['pid'], fy=.55), ease(p), 1.0, 1.07).convert('RGBA')
        m = L['marca'].copy(); m.putalpha(m.getchannel('A').point(lambda v: int(v * ease(min(1, max(0, (p - .15) / .4))))))
        img.alpha_composite(m)
    else:                   # cierre de Gold Studio: entra desde abajo
        img = Image.new('RGBA', (W, H), (250, 246, 238, 255))
        s = ease(min(1, p / .18)); off = int((1 - s) * 140)
        c = L['cierre'].copy(); c.putalpha(c.getchannel('A').point(lambda v: int(v * s)))
        img.alpha_composite(c, (0, off)) if off else img.alpha_composite(c)
    if t < 1.9:             # hook en pantalla desde el segundo 0
        al = min(1, t / .25) * (1 if t < 1.6 else max(0, (1.9 - t) / .3))
        h = L['hook'].copy(); h.putalpha(h.getchannel('A').point(lambda v: int(v * al)))
        img.alpha_composite(h)
    return img.convert('RGB')

# ---------- sonido: base suave al ritmo + efectos en cada corte ----------
def audio(path):
    sr = RG.SR; n = int(sr * TOTAL); mix = np.zeros(n)
    def put(x, t, g=1.0):
        i = int(t * sr); x = x[:max(0, n - i)]; mix[i:i + len(x)] += x * g
    tt = np.arange(int(sr * .35)) / sr
    kick = np.sin(2 * np.pi * (55 + 90 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9) * .8
    hat = np.random.default_rng(3).standard_normal(int(sr * .05)) * np.exp(-np.arange(int(sr * .05)) / sr * 90) * .12
    for k in range(int(5.4 / .5)): put(kick, k * .5)
    for k in range(int(5.4 / .25)): put(hat, k * .25 + .125)
    put(RG.whoosh(.35), .9); put(RG.whoosh(.4, 300, 2400, .35), 1.9); put(RG.tap(.3), 2.62)
    for i in range(8): put(RG.tick(.09), 3.0 + i * .125)
    put(RG.boom(.6), 4.0); put(RG.whoosh(.45), 5.25); put(RG.chime(.25), 5.5)
    pad_t = np.arange(n) / sr   # colchón cálido de fondo
    pad = sum(np.sin(2 * np.pi * f * pad_t) for f in (130.8, 164.8, 196.0)) * .035 * np.clip(pad_t / .4, 0, 1) * np.clip((TOTAL - pad_t) / .6, 0, 1)
    mix = mix + pad
    mix = mix / max(1e-6, np.abs(mix).max()) * .89
    with wave.open(path, 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((mix * 32767).astype('<i2').tobytes())

def build(name='reel-tostado-cafe'):
    os.makedirs(OUT, exist_ok=True); wav = f'{WORK}/a.wav'; audio(wav)
    out = f'{OUT}/{name}.mp4'; ff = imageio_ffmpeg.get_ffmpeg_exe()
    proc = subprocess.Popen([ff, '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                             '-i', wav, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-preset', 'medium', '-c:a', 'aac', '-b:a', '160k',
                             '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for i in range(int(TOTAL * FPS)):
        proc.stdin.write(frame(i / FPS).tobytes())
    proc.stdin.close(); proc.wait()
    return out

if __name__ == '__main__':
    print(build())
