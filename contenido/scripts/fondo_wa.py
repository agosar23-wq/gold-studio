"""Fondos de chat de WhatsApp (1170x2532) con el logo de Gold Studio."""
import sys, os, base64, random, subprocess; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR
D = '/home/user/gold-studio-final/'
OUT = D + 'whatsapp-business/fondos'; os.makedirs(OUT, exist_ok=True)
svg = lambda f: 'data:image/svg+xml;base64,' + base64.b64encode(open(D + f, 'rb').read()).decode()
W, H = 1170, 2532
random.seed(7)
pts = []
for row in range(13):
    for col in range(5):
        x = col * 250 + (125 if row % 2 else 0) + random.randint(-30, 30); y = row * 200 + random.randint(-30, 30)
        pts.append((x, y, random.choice([18, 24, 30, 40]), random.choice([.10, .14, .18])))
def wall(bg, gold, logo, ring_op, filt=''):
    sps = ''.join(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;color:{gold};opacity:{o}">{SP}</div>' for x, y, s, o in pts)
    return (f'<div class="w" style="background:{bg}">{sps}'
            f'<div style="position:absolute;left:-260px;top:-200px;width:760px;height:760px;border-radius:50%;border:90px solid {gold};opacity:{ring_op}"></div>'
            f'<div style="position:absolute;right:-300px;bottom:-260px;width:820px;height:820px;border-radius:50%;border:90px solid {gold};opacity:{ring_op}"></div>'
            f'<div style="position:absolute;left:0;right:0;top:1020px;display:flex;justify-content:center;opacity:.3"><img src="{logo}" style="width:760px;{filt}"></div></div>')
V = [('fondo-negro', wall('#1C1A17', '#C9A34E', svg('logo-gold-studio-transparente-blanco.svg'), .10)),
     ('fondo-marfil', wall('#FAF6EE', '#B8923A', svg('logo-gold-studio-transparente.svg'), .12)),
     ('fondo-dorado', wall('#C9A34E', '#FAF6EE', svg('logo-gold-studio-transparente-blanco.svg'), .16, 'filter:brightness(0) invert(1)'))]
work = SCR + '/wa-wall'; os.makedirs(work, exist_ok=True)
open(work + '/c.html', 'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}.w{{width:{W}px;height:{H}px;position:relative;overflow:hidden;margin-bottom:20px}}</style>' + ''.join(h for _, h in V))
js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});
await p.goto('file://{work}/c.html');await p.waitForTimeout(400);
const n={[n for n, _ in V]};const els=await p.$$('.w');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{OUT}/'+n[i]+'.png'}});await b.close();}})();'''
open(work + '/r.js', 'w').write(js)
subprocess.run(['node', work + '/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
