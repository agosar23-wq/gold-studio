"""Portadas concepto (no oficiales) para un single nuevo de Mora ('La luz prendida') y de Omar Courtz ('Hadas'):
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

# ---------- MORA: foto cálida, grano de película, tinta a mano ----------
def mora_base():
    im = square(f'{A}/30233120.jpg', .5, .62, 1.0)
    a = np.asarray(im).astype(np.float32) / 255
    a = a * np.array([1.06, .98, .86]) + np.array([.03, .015, 0])          # cálido
    a = np.clip(a, 0, 1) ** np.array([.95, 1.0, 1.08])
    a = a * .92 + .05                                                      # negros lavados (film)
    yy, xx = np.mgrid[0:N, 0:N]; v = 1 - .45 * (((xx / N - .5) ** 2 + (yy / N - .5) ** 2) / .5)
    im = Image.fromarray((np.clip(a * v[..., None], 0, 1) * 255).astype(np.uint8))
    halo = im.filter(ImageFilter.GaussianBlur(18)); im = ImageChops.screen(im, ImageEnhance.Brightness(halo).enhance(.35))
    return grain(im, 16)
# ---------- OMAR: duotono azul eléctrico + neón ----------
def omar_base():
    im = square(f'{A}/29501856.jpg', .42, .55, 1.25)
    g = np.asarray(ImageOps.grayscale(im)).astype(np.float32) / 255
    g = np.clip((g - .05) / .9, 0, 1) ** .9
    dark, mid, light = np.array([4, 8, 60.]), np.array([20, 50, 255.]), np.array([190, 230, 255.])
    t = g[..., None]
    a = np.where(t < .5, dark + (mid - dark) * (t / .5), mid + (light - mid) * ((t - .5) / .5))
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    top = im.crop((0, 0, N, 520)).filter(ImageFilter.GaussianBlur(14)); m = Image.linear_gradient('L').resize((N, 520)).point(lambda v: 255 - v)
    im.paste(top, (0, 0), m)
    bloom = im.filter(ImageFilter.GaussianBlur(25)); im = ImageChops.screen(im, ImageEnhance.Brightness(bloom).enhance(.5))
    return grain(im, 10)

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
.t{{position:absolute;left:110px;top:120px;font-family:Mark;font-size:150px;line-height:.95;color:#FFF3DC;transform:rotate(-4deg);text-shadow:0 0 30px rgba(255,190,90,.35)}}
.s{{position:absolute;left:120px;top:440px;font-family:Hand;font-size:84px;color:#FFE2B0;transform:rotate(-3deg)}}
.d{{position:absolute;right:90px;bottom:80px;font-family:'Courier New',monospace;font-weight:bold;font-size:58px;color:#FF8A1E;letter-spacing:6px;text-shadow:0 0 12px rgba(255,120,0,.8)}}
.m{{position:absolute;left:110px;bottom:90px;font-family:Mark;font-size:96px;color:#FFF3DC;transform:rotate(3deg)}}
</style><div class="c"><div class="t">la luz<br>prendida</div>
<svg style="position:absolute;inset:0" width="{N}" height="{N}" fill="none" stroke="#FFE2B0" stroke-width="7" stroke-linecap="round">

<path d="M118 610 C300 590 470 600 640 588" opacity=".75"/><path d="M955 1080 l25 -60 l25 60 l-65 -38 h80 z" opacity=".8"/>
</svg>
<div class="m">MORA</div><div class="d">'26 10 12</div></div>'''

OMAR_TXT = f'''<!doctype html><meta charset="utf-8"><style>{CSSF}
.t{{position:absolute;left:0;right:0;top:90px;text-align:center;font-family:Bub;font-size:270px;color:#FF5CD2;letter-spacing:6px;
  text-shadow:0 0 10px #FF8BE0,0 0 40px #FF2FC0,0 0 90px #FF2FC0}}
.n{{position:absolute;left:0;right:0;bottom:90px;text-align:center;font-family:Nun;font-weight:900;font-size:64px;letter-spacing:22px;color:#E6FFF0;
  text-shadow:0 0 12px #5CFFB0,0 0 36px #22FF90}}
</style><div class="c"><div class="t">hadas</div>
<svg style="position:absolute;inset:0" width="{N}" height="{N}">
<defs><filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<g filter="url(#glow)" fill="none" stroke-linecap="round" stroke-linejoin="round">
 <g transform="translate(1110 560) rotate(-12)" stroke="#7CFFC0" stroke-width="5">
  <ellipse cx="0" cy="0" rx="9" ry="26" fill="#C8FFE4"/><circle cx="0" cy="-38" r="11" fill="#C8FFE4"/>
  <path d="M-6 -12 C-70 -90 -110 -40 -60 -6 C-90 10 -70 50 -8 8"/><path d="M6 -12 C70 -90 110 -40 60 -6 C90 10 70 50 8 8"/>
  <path d="M0 26 C-10 60 10 80 -6 120" stroke-dasharray="2 14" stroke-width="6"/></g>
 <g transform="translate(400 760) rotate(14) scale(.8)" stroke="#FF6FD8" stroke-width="5">
  <ellipse cx="0" cy="0" rx="9" ry="26" fill="#FFD0F3"/><circle cx="0" cy="-38" r="11" fill="#FFD0F3"/>
  <path d="M-6 -12 C-70 -90 -110 -40 -60 -6 C-90 10 -70 50 -8 8"/><path d="M6 -12 C70 -90 110 -40 60 -6 C90 10 70 50 8 8"/>
  <path d="M0 26 C10 60 -10 80 6 120" stroke-dasharray="2 14" stroke-width="6"/></g>
 <path d="M720 980 C700 940 650 950 650 990 C650 1030 720 1060 720 1080 C720 1060 790 1030 790 990 C790 950 740 940 720 980Z" stroke="#FF6FD8" stroke-width="7" opacity=".9"/>
 <g fill="#FFFFFF" stroke="none">{''.join(f'<circle cx="{x}" cy="{y}" r="{r}"/>' for x, y, r in [(260,520,4),(1250,420,5),(1180,820,3),(330,1060,4),(980,330,3),(560,640,3),(1300,980,4)])}</g>
</g></svg><div class="n">OMAR COURTZ</div></div>'''

def sketch(base, notes):
    """Boceto: líneas de lápiz limpias sacadas de la foto + anotaciones a mano."""
    g = ImageOps.autocontrast(ImageOps.grayscale(base), cutoff=2).filter(ImageFilter.GaussianBlur(2.2))
    e = np.asarray(g.filter(ImageFilter.FIND_EDGES)).astype(np.float32)
    e = np.clip((e - 2.5) * 16, 0, 255)                                         # solo bordes marcados
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
.nt{{position:absolute;font-family:Hand;font-size:62px;color:#B8923A;transform:rotate(-3deg);white-space:nowrap}}
.pen{{position:absolute;inset:0;color:#555;opacity:.75}}</style><div class="c"><div class="pen">{title_html}</div>
<svg style="position:absolute;inset:0" width="{N}" height="{N}" fill="none" stroke="#B8923A" stroke-width="5" stroke-linecap="round">{arrows}</svg>{labels}</div>''')

NOTES = {
 'mora': [('título a mano', 760, 150, 640, 230), ('grano de película', 900, 760, 820, 640), ('fecha de cámara vieja', 820, 1180, 1180, 1370), ('luz cálida', 120, 760, 520, 600)],
 'omar': [('neón rosa', 1020, 470, 900, 300), ('hadas que brillan', 80, 560, 330, 720), ('todo en azul eléctrico', 760, 1180, 900, 1050), ('humo = misterio', 90, 1180, 520, 1000)],
}
def build():
    res = {}
    for name, base_fn, txt in [('mora', mora_base, MORA_TXT), ('omar', omar_base, OMAR_TXT)]:
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
