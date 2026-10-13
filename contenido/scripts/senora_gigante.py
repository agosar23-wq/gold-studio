"""Doña Rulos asomándose detrás de una hamburguesa gigante: cabeza de la ilustración de Canva + hamburguesa dibujada a mano (vector)."""
from PIL import Image, ImageDraw, ImageFilter
import math
import numpy as np
S='/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad'
src = Image.open(f'{S}/ilus/senora-burger.jpg').convert('RGB')
W, H = src.size; K = 3
a = np.asarray(src).astype(int)
BG = tuple(int(v) for v in np.median(a[(a.sum(2) > 650)], 0))
INK = (128, 40, 36)
# 1) borrar todo lo que queda debajo (manos, hamburguesa vieja, brazos) dejando cabeza, rulos y aro
m = Image.new('L', (W, H), 0); md = ImageDraw.Draw(m)
md.rectangle((0, 800, W, H), fill=255)
md.rectangle((392, 676, 450, 696), fill=255)          # resto del pan viejo dentro de la cara
md.polygon([(250,682),(370,682),(370,674),(399,674),(399,700),(401,682),(410,694),(456,684),(472,689),(472,722),(562,722),(600,800),(250,800)], fill=255)
m = m.filter(ImageFilter.GaussianBlur(1.2))
img = Image.composite(Image.new('RGB', (W, H), BG), src, m)
# 2) hamburguesa gigante, prolija
big = Image.new('RGBA', (W*K, H*K), (0,0,0,0)); d = ImageDraw.Draw(big)
P = lambda pts: [(x*K, y*K) for x, y in pts]
def shape(pts, w=8, fill=BG, closed=True):
    pts = P(pts)
    if fill is not None: d.polygon(pts, fill=fill + (255,))
    seq = pts + ([pts[0]] if closed else []); r = w*K/2
    d.line(seq, fill=INK + (255,), width=int(w*K), joint='curve')
    for x, y in (seq[0], seq[-1]): d.ellipse((x-r, y-r, x+r, y+r), fill=INK + (255,))
cx, hw = 505, 330
TOP, BASE = 716, 950                 # cúpula: de 742 (arriba) a 950 (base del pan)
def dome(x): return BASE - (BASE - TOP) * max(0, 1 - ((x - cx) / hw) ** 2) ** 0.62
rng = lambda a_, b_, n: [a_ + (b_ - a_) * i / n for i in range(n + 1)]
# mandíbula: continúa la línea de la cara hasta el pan
shape([(403, 668), (404, 684), (405, 698), (409, 712), (415, 728)], w=6.5, fill=None, closed=False)
# pan de abajo
bb = [(cx - hw + 8, 1112), (cx + hw - 8, 1112)] + [(cx + (hw - 8) * math.cos(math.radians(t)), 1112 + 70 * math.sin(math.radians(t))) for t in rng(0, 180, 60)]
shape(bb)
# medallón (relleno bordó, bordes redondeados) con marcas de parrilla claras
R = 34; L0, R0, T0, B0 = cx - hw - 12, cx + hw + 12, 1030, 1104
pt = ([(L0 + R - R * math.cos(math.radians(t)), T0 + R - R * math.sin(math.radians(t))) for t in rng(0, 90, 10)]
      + [(R0 - R + R * math.cos(math.radians(t)), T0 + R - R * math.sin(math.radians(t))) for t in rng(90, 0, 10)]
      + [(R0 - R + R * math.cos(math.radians(t)), B0 - R + R * math.sin(math.radians(t))) for t in rng(0, 90, 10)]
      + [(L0 + R - R * math.cos(math.radians(t)), B0 - R + R * math.sin(math.radians(t))) for t in rng(90, 0, 10)])
shape(pt, fill=INK)
for i, x in enumerate(rng(cx - hw + 40, cx + hw - 40, 7)):
    y = 1082 if i % 2 == 0 else 1090
    d.line(P([(x - 16, y + 5), (x + 16, y - 5)]), fill=BG + (255,), width=int(5*K))
    for xx, yy in ((x - 16, y + 5), (x + 16, y - 5)):
        r = 2.5*K; d.ellipse((xx*K-r, yy*K-r, xx*K+r, yy*K+r), fill=BG + (255,))
# queso: lámina crema con gotas redondeadas que caen sobre la carne
def cheese_bottom(x):
    y = 1030
    for c, dep, wid in ((cx - 200, 40, 17), (cx - 50, 58, 19), (cx + 110, 34, 15), (cx + 235, 48, 17)):
        u = (x - c) / wid
        if abs(u) < 1: y += (dep - wid) + wid * math.sqrt(1 - u * u)
    return y
ch = [(cx - hw - 26, 998), (cx + hw + 26, 998), (cx + hw + 10, 1030)] + [(x, cheese_bottom(x)) for x in rng(cx + hw - 2, cx - hw + 2, 700)] + [(cx - hw - 10, 1030)]
shape(ch)
# lechuga: borde festoneado
sc = []
n = 9; x0, x1 = cx - hw - 40, cx + hw + 40; step = (x1 - x0) / n
for i in range(n):
    xa = x0 + i * step
    sc += [(xa + step * t, 988 + 24 * math.sin(math.pi * t)) for t in rng(0, 1, 16)]
shape(sc + [(x1, 958), (x0, 958)])
# pan de arriba (cúpula) con brillo y sésamos
top = [(cx - hw - 6, BASE + 8)] + [(x, dome(x)) for x in rng(cx - hw, cx + hw, 240)] + [(cx + hw + 6, BASE + 8)]
shape(top)
d.line(P([(x, dome(x) + 34) for x in rng(cx - hw + 70, cx - hw + 190, 30)]), fill=INK + (255,), width=int(6*K))
for (sx, sy, rot) in [(400,790,-22),(480,770,-6),(560,770,12),(640,792,26),(705,835,38),(320,850,-38),(425,835,-14),(515,825,4),(605,840,18),(685,895,32),(470,895,-6),(365,905,-24),(570,895,12)]:
    w, h = 15*K, 6.5*K; c, s_ = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    pts = [(sx*K + w*math.cos(t)*c - h*math.sin(t)*s_, sy*K + w*math.cos(t)*s_ + h*math.sin(t)*c) for t in [i*math.pi/20 for i in range(41)]]
    d.line(pts, fill=INK + (255,), width=int(5*K), joint='curve')
out = img.convert('RGBA'); out.alpha_composite(big.resize((W, H), Image.LANCZOS)); out = out.convert('RGB')
out.save(f'{S}/ilus/senora-gigante.jpg', quality=95)
out.resize((568, 704)).save(f'{S}/gigante_prev.png')
