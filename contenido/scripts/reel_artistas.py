"""Reels 'boceto → final' de las portadas concepto de Mora y Omar Courtz (1080×1920, 30 fps, solo música)."""
import os, sys, subprocess, base64
import numpy as np
from PIL import Image, ImageFilter
sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import SCR, F, SP
import imageio_ffmpeg
W, H, FPS = 1080, 1920, 30
P = f'{SCR}/portadas'; WORK = f'{SCR}/reel-artistas'; os.makedirs(WORK, exist_ok=True)
OUT = '/home/user/gold-studio-final/reels'
ease = lambda p: p * p * (3 - 2 * p)

CSS = f'''@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2)}}
@font-face{{font-family:B;font-style:italic;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2)}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2)}}
@font-face{{font-family:Hand;src:url(file://{SCR}/xfonts/caveat.woff2)}}
body{{margin:0;background:transparent}} .c{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:J}}
.t{{position:absolute;left:80px;right:80px;text-align:center;font-family:B;color:#FAF6EE;text-shadow:0 4px 30px rgba(0,0,0,.6)}} .t i{{color:#E3C276}}
.h{{position:absolute;left:0;right:0;text-align:center;font-family:Hand;color:#E3C276;font-size:84px}}'''
def layers(artista, cancion):
    L = {
     'hook': f'<div class="c"><div class="t" style="top:170px;font-size:90px;line-height:1.06">Así diseñaría la portada del próximo single de <i>{artista}</i></div></div>',
     'boceto': '<div class="c"><div class="h" style="top:330px">primero, el boceto…</div></div>',
     'final': '<div class="c"><div class="h" style="top:330px">y así queda</div></div>',
     'player': f'<div class="c"><div class="t" style="top:300px;font-size:74px"><i>“{cancion}”</i><br><span style="font-family:J;font-size:40px;letter-spacing:.3em;color:#ddd">{artista.upper()}</span></div></div>',
     'cierre': (f'<div class="c" style="background:#FAF6EE;color:#1C1A17;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:50px;padding:0 90px;box-sizing:border-box">'
                f'<div style="width:120px;height:120px;color:#C9A34E">{SP}</div><div style="font-family:B;font-size:104px;line-height:1.06">¿Qué artista hago <i style="color:#8A6A22">la próxima?</i></div>'
                f'<div style="background:#1C1A17;color:#FAF6EE;border-radius:999px;padding:26px 50px;font-size:40px">@goldstudio.ba</div>'
                f'</div>'),
    }
    html = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>' + ''.join(f'<div id="{k}" style="width:{W}px;height:{H}px">{v}</div>' for k, v in L.items())
    open(f'{WORK}/l.html', 'w').write(html)
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});"
          f"await p.goto('file://{WORK}/l.html');await p.evaluate(async()=>{{await document.fonts.ready}});await p.waitForTimeout(300);"
          + ''.join(f"await (await p.$('#{k}')).screenshot({{path:'{WORK}/{k}.png',omitBackground:true}});" for k in L) + "await b.close();})();")
    open(f'{WORK}/l.js', 'w').write(js)
    subprocess.run(['node', f'{WORK}/l.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    return {k: Image.open(f'{WORK}/{k}.png').convert('RGBA') for k in L}

def comp(bg, cover, scale=1.0, dy=0, layer=None, alpha=1.0, rot=0):
    im = bg.copy().convert('RGBA'); s = int(900 * scale)
    c = cover.resize((s, s), Image.LANCZOS).convert('RGBA')
    if rot: c = c.rotate(rot, expand=True, resample=Image.BICUBIC)
    sh = Image.new('RGBA', c.size, (0, 0, 0, 0)); sh.putalpha(c.getchannel('A').point(lambda v: int(v * .55)))
    sh = sh.filter(ImageFilter.GaussianBlur(30)); im.alpha_composite(sh, ((W - c.width) // 2, (H - c.height) // 2 + 120 + dy + 40))
    im.alpha_composite(c, ((W - c.width) // 2, (H - c.height) // 2 + 120 + dy))
    if layer is not None:
        l = layer if alpha >= 1 else layer.copy()
        if alpha < 1: l.putalpha(l.getchannel('A').point(lambda v: int(v * alpha)))
        im.alpha_composite(l)
    return im.convert('RGB')

def frames(name, artista, cancion):
    L = layers(artista, cancion)
    fin = Image.open(f'{P}/{name}-final.png').convert('RGB'); bos = Image.open(f'{P}/{name}-boceto.png').convert('RGB')
    bgfin = fin.resize((H, H)).crop(((H - W) // 2, 0, (H + W) // 2, H)).filter(ImageFilter.GaussianBlur(40))
    bgfin = Image.blend(bgfin, Image.new('RGB', (W, H), (12, 10, 9)), .45)
    out = []
    n = lambda s: int(s * FPS)
    for i in range(n(1.8)):                                   # hook sobre la portada borrosa
        p = i / n(1.8); out.append(comp(bgfin, bos, .92 + .04 * p, 0, L['hook'], min(1, p * 4), -3 + 2 * p))
    for i in range(n(1.6)):                                   # el boceto
        p = i / n(1.6); out.append(comp(bgfin, bos, .96 + .03 * p, 0, L['boceto'], min(1, p * 4)))
    for i in range(n(1.3)):                                   # barrido boceto → final
        p = ease(i / n(1.3)); x = int(1500 * p)
        mix = bos.copy(); mix.paste(fin.crop((0, 0, max(1, x), 1500)), (0, 0))
        out.append(comp(bgfin, mix, .99, 0, L['final'], min(1, p * 2)))
    for i in range(n(1.8)):                                   # el final, zoom lento
        p = i / n(1.8); out.append(comp(bgfin, fin, 1.0 + .08 * p, 0, L['final'], 1))
    for i in range(n(1.6)):                                   # título de la canción
        p = i / n(1.6); out.append(comp(bgfin, fin, 1.08 - .2 * ease(min(1, p * 2)), 60, L['player'], min(1, p * 3)))
    blank = Image.new('RGB', (W, H), (250, 246, 238))
    for i in range(n(2.0)):
        p = i / n(2.0); s = ease(min(1, p / .2)); im = blank.convert('RGBA'); c = L['cierre'].copy(); c.putalpha(c.getchannel('A').point(lambda v: int(v * s))); im.alpha_composite(c); out.append(im.convert('RGB'))
    return out

def build(name, artista, cancion, music):
    fr = frames(name, artista, cancion); total = len(fr) / FPS
    wav = f'{WORK}/{name}.wav'
    mod = __import__(music); mod.TOTAL = total; mod.audio(wav)
    out = f'{OUT}/reel-portada-{name}.mp4'
    p = subprocess.Popen([imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-i', wav, '-c:v', 'libx264', '-profile:v', 'main', '-level', '4.1', '-pix_fmt', 'yuv420p', '-crf', '21', '-c:a', 'aac', '-b:a', '160k', '-ac', '2', '-ar', '48000',
                          '-shortest', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for f in fr: p.stdin.write(np.asarray(f).tobytes())
    p.stdin.close(); p.wait(); return out

if __name__ == '__main__':
    print(build('mora', 'Mora', 'Boleto', 'reel_cafe'))
    print(build('omar', 'Omar Courtz', 'Otra vuelta', 'reel_hamburguesas'))
