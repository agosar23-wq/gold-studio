"""Portada de WhatsApp Business con el logo de Gold Studio (1920x1080, franja visible al centro)."""
import sys, os, base64, subprocess; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR
D = '/home/user/gold-studio-final/'; OUT = D + 'whatsapp-business'
svg = lambda f: 'data:image/svg+xml;base64,' + base64.b64encode(open(D + f, 'rb').read()).decode()
W, H = 1920, 1080
def cover(bg, gold, sub, logo, filt=''):
    sp = lambda x, y, s, o=1: f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;color:{gold};opacity:{o}">{SP}</div>'
    return (f'<div class="cv" style="background:{bg}">'
            f'<div style="position:absolute;left:-240px;bottom:-160px;width:640px;height:640px;border-radius:50%;border:70px solid {gold};opacity:.18"></div>'
            f'<div style="position:absolute;right:-240px;top:-200px;width:620px;height:620px;border-radius:50%;border:70px solid {gold};opacity:.18"></div>'
            + sp(420, 330, 54) + sp(360, 440, 24, .7) + sp(1450, 560, 60) + sp(1540, 500, 26, .7) + sp(300, 640, 34, .5) + sp(1620, 330, 30, .5) +
            f'<div style="position:absolute;left:0;right:0;top:185px;display:flex;justify-content:center"><img src="{logo}" style="width:600px;{filt}"></div>'
            f'<div style="position:absolute;left:150px;bottom:250px;font-family:J;font-size:34px;letter-spacing:.24em;color:{sub}">DISEÑO WEB</div>'
            f'<div style="position:absolute;right:150px;bottom:250px;font-family:J;font-size:34px;letter-spacing:.24em;color:{sub}">BRANDING</div></div>')
V = [('portada-logo-negra', cover('#1C1A17', '#C9A34E', '#BDB2A0', svg('logo-gold-studio-transparente-blanco.svg'))),
     ('portada-logo-marfil', cover('#FAF6EE', '#B8923A', '#5E5649', svg('logo-gold-studio-transparente.svg'))),
     ('portada-logo-dorada', cover('#C9A34E', '#FAF6EE', '#1C1A17', svg('logo-gold-studio-transparente-blanco.svg'), 'filter:brightness(0) invert(1)'))]
work = SCR + '/wa-cover2'; os.makedirs(work, exist_ok=True)
open(work + '/c.html', 'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}.cv{{width:{W}px;height:{H}px;position:relative;overflow:hidden;margin-bottom:20px}}</style>' + ''.join(h for _, h in V))
js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});
await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(400);
const n={[n for n, _ in V]};const els=await p.$$('.cv');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{OUT}/'+n[i]+'.png'}});await b.close();}})();'''
open(work + '/r.js', 'w').write(js)
subprocess.run(['node', work + '/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
