"""Portadas concepto (no oficiales) para un single nuevo de Mora ('Lavandería') y de Omar Courtz ('Peluche'):
foto de Pexels + tratamiento en el estilo de cada artista. Genera boceto (lápiz) y final, 1500×1500."""
import os, sys, base64, subprocess
import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageEnhance, ImageChops
sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import SCR
A = f'{SCR}/artistas'; OUT = f'{SCR}/portadas'; XF = f'{SCR}/xfonts'
os.makedirs(OUT, exist_ok=True)
N = 1500
rng = np.random.default_rng(5)

def square(path, cx=.5, cy=.5, zoom=1.0):
    im = Image.open(path).convert('RGB'); w, h = im.size; s = int(min(w, h) / zoom)
    x = int((w - s) * cx); y = int((h - s) * cy)
    return im.crop((x, y, x + s, y + s)).resize((N, N), Image.LANCZOS)
def grain(im, amt=18):
    a = np.asarray(im).astype(np.float32)
    g = rng.normal(0, amt, (N, N, 1))
    return Image.fromarray(np.clip(a + g, 0, 255).astype(np.uint8))
def b64(p): return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
def font(n): return f"url(file://{XF}/{n}.woff2)"

A2 = f'{SCR}/artistas2'
def square_pad(path, y0, y1):
    """Recorte vertical [y0, y1] y lo hace cuadrado estirando los costados con la misma foto desenfocada."""
    im = Image.open(path).convert('RGB'); w, h = im.size; side = y1 - y0
    crop = im.crop((0, y0, w, y1)); bg = crop.resize((side, side)).filter(ImageFilter.GaussianBlur(40))
    bg.paste(crop, ((side - w) // 2, 0)) if side >= w else None
    m = Image.new('L', (w, side), 255); edge = 60
    for i in range(edge): m.paste(int(255 * i / edge), (i, 0, i + 1, side)); m.paste(int(255 * i / edge), (w - 1 - i, 0, w - i, side))
    out = bg.copy(); out.paste(crop, ((side - w) // 2, 0), m)
    return out.resize((N, N), Image.LANCZOS)
# ---------- MORA · LAVANDERÍA: foto real de una lavandería de barrio de noche, película y grano ----------
A3 = f'{SCR}/artistas3'
def mora_base():
    im = Image.open(f'{A3}/14556070.jpg').convert('RGB'); w, h = im.size
    im = im.crop((300, 0, 300 + h, h)).resize((N, N), Image.LANCZOS)
    a = np.asarray(im).astype(np.float32) / 255
    a = a ** np.array([.92, .9, 1.0]) * np.array([1.02, 1.04, .9])          # verde/amarillo de película, como sus fotos
    a = np.clip(a, 0, 1) * .9 + .06                                           # negros lavados
    yy, xx = np.mgrid[0:N, 0:N]; v = 1 - .35 * (((xx / N - .5) ** 2 + (yy / N - .5) ** 2) / .5)
    im = Image.fromarray((np.clip(a * v[..., None], 0, 1) * 255).astype(np.uint8))
    halo = im.filter(ImageFilter.GaussianBlur(14)); im = ImageChops.screen(im, ImageEnhance.Brightness(halo).enhance(.3))
    return grain(im, 22)
# ---------- OMAR · MAÑANA SÍ: cielo de día, sol detrás de la nube ----------
def omar_base():
    im = square(f'{A2}/5718410.jpg', .45, .5, 1.0)
    a = np.asarray(im).astype(np.float32) / 255
    a = np.clip((a - .5) * 1.1 + .5, 0, 1) * np.array([.96, 1.0, 1.06])
    im = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
    bloom = im.filter(ImageFilter.GaussianBlur(30)); im = ImageChops.screen(im, ImageEnhance.Brightness(bloom).enhance(.25))
    return grain(im, 6)

def render_overlay(name, html):
    p = f'{OUT}/{name}.html'; open(p, 'w').write(html)
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const pg=await b.newPage({{viewport:{{width:{N},height:{N}}}}});"
          f"await pg.goto('file://{p}');await pg.evaluate(async()=>{{await document.fonts.ready}});await pg.waitForTimeout(400);"
          f"await pg.screenshot({{path:'{OUT}/{name}.png',omitBackground:true}});await b.close();}})();")
    open(f'{OUT}/{name}.js', 'w').write(js)
    subprocess.run(['node', f'{OUT}/{name}.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    return f'{OUT}/{name}.png'

CSSF = f'''@font-face{{font-family:Hand;src:{font("caveat")}}}@font-face{{font-family:Mark;src:{font("permanent-marker")}}}
@font-face{{font-family:Bub;src:{font("rubik-bubbles")}}}@font-face{{font-family:Nun;src:{font("nunito")}}}
body{{margin:0;background:transparent}} .c{{width:{N}px;height:{N}px;position:relative;overflow:hidden}}'''

MORA_TXT = f'''<!doctype html><meta charset="utf-8"><style>{CSSF}
.t{{position:absolute;left:560px;top:250px;font-family:Mark;font-size:92px;color:#FFFFFF;transform:rotate(-5deg);opacity:.92;text-shadow:0 0 18px rgba(255,255,255,.35)}}
.m{{position:absolute;left:580px;top:360px;font-family:Hand;font-size:70px;color:#FFFFFF;transform:rotate(-5deg);opacity:.85}}
</style><div class="c"><div class="t">lavandería</div><div class="m">by Mora</div></div>'''

OMAR_TXT = f'''<!doctype html><meta charset="utf-8"><style>{CSSF}
.t{{position:absolute;left:0;right:0;top:210px;text-align:center;font-family:Bub;font-size:250px;line-height:.9;letter-spacing:4px;
  background:linear-gradient(180deg,#ffffff 0%,#e8f0f8 22%,#8aa2bd 44%,#2d4466 50%,#c8d6e6 62%,#ffffff 80%,#9fb3c9 100%);-webkit-background-clip:text;color:transparent;
  filter:drop-shadow(0 5px 0 #1d3150) drop-shadow(0 0 2px #fff) drop-shadow(0 20px 30px rgba(10,30,70,.5))}}
.n{{position:absolute;left:0;right:0;top:1340px;text-align:center;font-family:Nun;font-weight:900;font-size:56px;letter-spacing:26px;color:#fff;text-shadow:0 2px 20px rgba(20,60,120,.5)}}
</style><div class="c"><div class="n">OMAR COURTZ</div><div class="t">mañana<br>sí</div>
<svg style="position:absolute;inset:0" width="{N}" height="{N}"><g fill="#fff">{''.join(f'<path transform="translate({x} {y}) scale({k})" d="M0 -30 C3 -6 6 -3 30 0 C6 3 3 6 0 30 C-3 6 -6 3 -30 0 C-6 -3 -3 -6 0 -30Z"/>' for x, y, k in [(240,230,1.3),(1260,560,1.6),(1180,180,.8),(330,640,.9)])}</g></svg></div>'''

def sketch(base, notes):
    """Boceto: líneas de lápiz limpias sacadas de la foto + anotaciones a mano."""
    g = ImageOps.autocontrast(ImageOps.grayscale(base), cutoff=2).filter(ImageFilter.GaussianBlur(2.2))
    e = np.asarray(g.filter(ImageFilter.FIND_EDGES)).astype(np.float32)
    e = np.clip((e - 4) * 13, 0, 255)                                         # solo bordes marcados
    e = np.asarray(Image.fromarray(e.astype(np.uint8)).filter(ImageFilter.GaussianBlur(.8))).astype(np.float32)
    paper = np.full((N, N), 246.) + rng.normal(0, 2.2, (N, N))
    shade = np.asarray(g).astype(np.float32); shade = np.clip((110 - shade) * .3, 0, 28)   # sombreado suave
    out = np.clip(paper - e * .8 - shade, 0, 255)
    img = Image.fromarray(out.astype(np.uint8)).convert('RGB')
    ov = Image.open(render_overlay(notes[0], notes[1])).convert('RGBA'); img = img.convert('RGBA'); img.alpha_composite(ov)
    return img.convert('RGB')

def notes_html(title_html, items):
    """Tipografía en lápiz gris + notas de diseñadora con flechas (texto, x, y, flecha hacia (ax, ay))."""
    arrows = ''.join(f'<path d="M{x+20} {y+40} Q{(x+ax)/2+60} {(y+ay)/2-40} {ax} {ay}" /><path d="M{ax} {ay} l-26 -6 M{ax} {ay} l-8 -26"/>' for t, x, y, ax, ay in items)
    labels = ''.join(f'<div class="nt" style="left:{x}px;top:{y}px">{t}</div>' for t, x, y, ax, ay in items)
    return (f'''<!doctype html><meta charset="utf-8"><style>{CSSF}
.nt{{position:absolute;font-family:Hand;font-size:62px;line-height:1;color:#B8923A;transform:rotate(-3deg);white-space:pre-line}}
.pen{{position:absolute;inset:0;color:#555;opacity:.75}}</style><div class="c"><div class="pen">{title_html}</div>
<svg style="position:absolute;inset:0" width="{N}" height="{N}" fill="none" stroke="#B8923A" stroke-width="5" stroke-linecap="round">{arrows}</svg>{labels}</div>''')

NOTES = {
 'mora': [('título a mano,\nescrito en el vidrio', 80, 120, 540, 300), ('lavandería de barrio\nde noche', 960, 640, 1000, 560), ('motos = barrio real', 80, 1150, 300, 1250), ('grano de película', 940, 1200, 1100, 1100)],
 'omar': [('letras cromadas', 900, 760, 1000, 560), ('de noche a de día', 80, 820, 300, 1000), ('brillitos Y2K', 980, 1180, 1250, 600), ('el sol que asoma', 420, 1080, 700, 980)],
}
def build():
    res = {}
    for name, base_fn, txt in [('mora', mora_base, MORA_TXT)]:
        base = base_fn(); base.save(f'{OUT}/{name}-foto.png')
        ov = Image.open(render_overlay(f'{name}-texto', txt)).convert('RGBA')
        final = base.convert('RGBA'); final.alpha_composite(ov); final = final.convert('RGB'); final.save(f'{OUT}/{name}-final.png')
        tg = ov.copy(); al = tg.getchannel('A').point(lambda v: 255 if v > 90 else 0)
        edge = np.asarray(al.filter(ImageFilter.FIND_EDGES)); gray = Image.new('RGBA', ov.size, (60, 60, 60, 0)); gray.putalpha(Image.fromarray(np.clip(edge * 3, 0, 230).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)))
        sk = sketch(base, (f'{name}-notas', notes_html('', NOTES[name])))
        sk = sk.convert('RGBA'); sk.alpha_composite(gray); sk = sk.convert('RGB'); sk.save(f'{OUT}/{name}-boceto.png')
        res[name] = final
    return res

if __name__ == '__main__':
    build(); print(OUT)
