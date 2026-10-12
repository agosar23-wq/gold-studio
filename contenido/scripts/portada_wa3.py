"""Portada de agencia para WhatsApp Business: logo + mockups de trabajos a los costados."""
import sys, os, base64, subprocess; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR
import catalogo_wa2 as K, mocks as M
D = '/home/user/gold-studio-final/'; OUT = D + 'whatsapp-business'
svg = lambda f: 'data:image/svg+xml;base64,' + base64.b64encode(open(D + f, 'rb').read()).decode()
W, H = 1920, 1080
def sp(x, y, s, c, o=1): return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;color:{c};opacity:{o}">{SP}</div>'
def cover(bg, gold, ink, sub, logo):
    left = (f'<div style="position:absolute;left:40px;top:330px;transform:rotate(-4deg)">{M.site("aura", 2, 480)}</div>'
            f'<div style="position:absolute;left:410px;top:290px;transform:rotate(5deg)">{K.phone(K.mob_site, 170, 360)}</div>')
    right = (f'<div style="position:absolute;right:290px;top:290px;transform:rotate(-5deg)">{K.phone(K.ig, 200, 400)}</div>'
             f'<div style="position:absolute;right:50px;top:330px;transform:rotate(4deg)">{K.shot("p-inicio.png", 180)}</div>')
    return (f'<div class="cv{" dk" if bg == "#1C1A17" else ""}" style="background:{bg}">{left}{right}'
            + sp(660, 180, 34, gold) + sp(1250, 690, 30, gold, .8) + sp(690, 760, 22, gold, .6) +
            f'<div style="position:absolute;left:0;right:0;top:175px;display:flex;flex-direction:column;align-items:center;gap:14px">'
            f'<img src="{logo}" style="width:400px">'
            f'<div style="font-family:J;font-size:24px;letter-spacing:.3em;color:{sub};font-weight:500">DISEÑO Y MARKETING DIGITAL</div>'
            f'<div style="font-family:B;font-style:italic;font-size:36px;color:{gold}">Páginas web · Branding · Redes</div></div></div>')
V = [('portada-agencia-negra', cover('#1C1A17', '#C9A34E', '#FAF6EE', '#BDB2A0', svg('logo-gold-studio-transparente-blanco.svg'))),
     ('portada-agencia-marfil', cover('#FAF6EE', '#B8923A', '#1C1A17', '#5E5649', svg('logo-gold-studio-transparente.svg')))]
work = SCR + '/wa-cover3'; os.makedirs(work, exist_ok=True)
open(work + '/c.html', 'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}{K.EXT}.dk .ph{{background:#4A433A}}.cv{{width:{W}px;height:{H}px;position:relative;overflow:hidden;margin-bottom:20px}}</style>' + ''.join(h for _, h in V))
js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});
await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(400);
const n={[n for n, _ in V]};const els=await p.$$('.cv');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{OUT}/'+n[i]+'.png'}});await b.close();}})();'''
open(work + '/r.js', 'w').write(js)
subprocess.run(['node', work + '/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
