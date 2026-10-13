"""Redibuja prolija la hamburguesa que muerde Doña Rulos sobre la ilustración de Canva (senora-burger.jpg -> senora-burger-fix.jpg)."""
from PIL import Image, ImageDraw, ImageFilter
from collections import deque
import math
import numpy as np
S='/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad'
src = Image.open(f'{S}/ilus/senora-burger.jpg').convert('RGB')
W, H = src.size; K = 4
a = np.asarray(src).astype(int)
BG = tuple(int(v) for v in np.median(a[(a.sum(2) > 650)], 0))
INK = (128, 40, 36); LW = 6.2

# 1) borrar manchitas sueltas (componentes chicos de tinta) en el pan, al costado izquierdo y debajo de la hamburguesa
ink = (a[..., 0] - a[..., 2] > 40) & (a.sum(2) < 560)
zone = Image.new('L', (W, H), 0); zd = ImageDraw.Draw(zone)
zd.polygon([(318,722),(350,700),(420,694),(452,700),(470,742),(468,790),(440,806),(340,804),(318,790),(310,750)], fill=255)  # pan de arriba
zd.rectangle((278, 815, 308, 885), fill=255)          # restos de panceta a la izquierda
zd.rectangle((300, 935, 545, 978), fill=255)          # restos debajo del pan
zd.rectangle((440, 700, 510, 748), fill=255)          # manchitas junto a la boca
zone = np.asarray(zone) > 0
x0, y0, x1, y1 = 270, 680, 580, 1000
seen = np.zeros_like(ink); clean = np.asarray(src).copy()
for y in range(y0, y1):
    for x in range(x0, x1):
        if ink[y, x] and not seen[y, x]:
            q = deque([(y, x)]); seen[y, x] = True; comp = []
            while q:
                cy, cx2 = q.popleft(); comp.append((cy, cx2))
                for dy, dx in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
                    ny, nx = cy + dy, cx2 + dx
                    if y0 <= ny < y1 and x0 <= nx < x1 and ink[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True; q.append((ny, nx))
            if len(comp) < 1200 and all(zone[p] for p in comp):
                for (py, px) in comp: clean[py-2:py+3, px-2:px+3] = BG
src = Image.fromarray(clean)

# 2) tapar la parte de abajo vieja (panceta, queso, pan) y dibujar capas nuevas
erase_extra = [(428,946),(458,946),(458,968),(428,968)]
erase = [(306,814),(340,820),(420,824),(500,820),(538,814),(544,850),(544,905),(505,942),(425,956),(335,950),(304,912),(302,860)]
m = Image.new('L', (W, H), 0); ImageDraw.Draw(m).polygon(erase, fill=255); ImageDraw.Draw(m).polygon(erase_extra, fill=255); m = m.filter(ImageFilter.GaussianBlur(1.5))
base = Image.composite(Image.new('RGB', (W, H), BG), src, m)
big = Image.new('RGBA', (W*K, H*K), (0,0,0,0)); d = ImageDraw.Draw(big)
P = lambda pts: [(x*K, y*K) for x, y in pts]
def line(pts, w=LW):
    pts = P(pts); r = w*K/2
    d.line(pts, fill=INK + (255,), width=int(w*K), joint='curve')
    for x, y in pts: d.ellipse((x-r, y-r, x+r, y+r), fill=INK + (255,))
cx, hw = 425, 118
bow = lambda x, b: b * (1 - ((x - cx) / hw) ** 2)
xs = lambda x0, x1, st=2: [x0 + i*st for i in range(int(abs(x1 - x0) / abs(st)) + 1)] if st > 0 else [x0 - i*abs(st) for i in range(int(abs(x1 - x0) / abs(st)) + 1)]
line([(x, 826 + bow(x, 8) + 5*math.sin((x - 300) / 9)) for x in xs(298, 552)])               # lechuga
def cheese_y(x):
    y = 842 + bow(x, 10)
    for c, dep, wid in ((362, 30, 8), (440, 42, 9), (505, 22, 7)):                              # gotas en U
        u = (x - c) / wid
        if abs(u) < 1: y += (dep - wid) + wid * math.sqrt(1 - u*u)
    return y
line([(x, cheese_y(x)) for x in xs(306, 544, .5)])
left = [(316 - 9*math.sin(math.pi*t/20), 846 + 38*t/20) for t in range(21)]
right = [(534 + 9*math.sin(math.pi*t/20), 846 + 38*t/20) for t in range(21)]
line(left); line(right); line([(x, 884 + bow(x, 12)) for x in xs(534, 316, -2)])              # medallón
for x0, y0 in ((335, 872), (390, 881), (470, 881), (520, 870)):
    line([(x0, y0), (x0 + 13, y0 - 2)], w=4.5)
line([(x, 892 + bow(x, 12)) for x in xs(318, 532)])                                           # pan de abajo
bb = [(cx + 112*math.cos(math.radians(t)), 908 + 34*math.sin(math.radians(t))) for t in range(0, 181, 3)]
line([(318, 892), (312, 900)] + bb[::-1] + [(538, 900), (532, 892)])
# 3) sésamos parejos en el pan de arriba
for (sx, sy, rot) in [(352,722,-15),(392,714,8),(428,722,-12),(378,744,-20),(416,750,18),(450,760,-8),(362,776,5),(400,776,-12),(438,786,10)]:
    w, h = 9*K, 4.6*K; c, s_ = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    pts = [(sx*K + w*math.cos(t)*c - h*math.sin(t)*s_, sy*K + w*math.cos(t)*s_ + h*math.sin(t)*c) for t in [i*math.pi/18 for i in range(37)]]
    d.line(pts, fill=INK + (255,), width=int(3.6*K), joint='curve')
out = base.convert('RGBA'); out.alpha_composite(big.resize((W, H), Image.LANCZOS)); out = out.convert('RGB')
out.save(f'{S}/ilus/senora-burger-fix.jpg', quality=95)
out.crop((240, 640, 600, 1010)).resize((720, 740)).save(f'{S}/fixprev.png')
out.resize((568, 704)).save(f'{S}/fixfull.png')
