"""Portada para el perfil de WhatsApp Business (la foto de perfil tapa el centro de abajo)."""
import sys, os, subprocess; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR
OUT = '/home/user/gold-studio-final/whatsapp-business'
W, H = 1920, 1080
def cover(bg, ink, em, sub, ring):
    sp = lambda x, y, s, o=1: f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;color:{em};opacity:{o}">{SP}</div>'
    return (f'<div class="cv" style="background:{bg};color:{ink}">'
            f'<div style="position:absolute;left:-240px;bottom:-200px;width:620px;height:620px;border-radius:50%;border:60px solid {ring};opacity:.35"></div>'
            f'<div style="position:absolute;right:-330px;top:-290px;width:560px;height:560px;border-radius:50%;border:56px solid {ring};opacity:.35"></div>'
            + sp(430, 470, 50) + sp(1460, 470, 66) + sp(1560, 430, 28, .7) + sp(370, 530, 26, .7) +
            f'<div style="position:absolute;left:0;right:0;top:250px;text-align:center">'
            f'<div style="font-size:30px;letter-spacing:.42em;color:{em};font-weight:500">GOLD STUDIO</div>'
            f'<div style="font-family:B;font-size:118px;line-height:1.05;margin-top:16px">Tu marca, con <em style="color:{em}">brillo propio</em></div></div>'
            f'<div style="position:absolute;left:150px;bottom:250px;font-size:36px;line-height:1.7;letter-spacing:.06em;color:{sub}">Páginas web<br>Apps a medida</div>'
            f'<div style="position:absolute;right:150px;bottom:250px;font-size:36px;line-height:1.7;letter-spacing:.06em;color:{sub};text-align:right">Branding<br>Community manager</div></div>')
EXT = f'.cv{{width:{W}px;height:{H}px;position:relative;overflow:hidden;font-family:J;margin-bottom:20px}}'
V = [('portada-negra', cover('#1C1A17', '#FAF6EE', '#C9A34E', '#BDB2A0', '#C9A34E')),
     ('portada-marfil', cover('#FAF6EE', '#1C1A17', '#B8923A', '#5E5649', '#C9A34E'))]
work = SCR + '/wa-cover'; os.makedirs(work, exist_ok=True)
open(work + '/c.html', 'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXT}</style>' + ''.join(h for _, h in V))
js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});
await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(300);
const n={[n for n, _ in V]};const els=await p.$$('.cv');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{OUT}/'+n[i]+'.png'}});await b.close();}})();'''
open(work + '/r.js', 'w').write(js)
subprocess.run(['node', work + '/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
