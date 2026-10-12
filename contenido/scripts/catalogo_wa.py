"""Imágenes 1080x1080 para el catálogo de WhatsApp Business."""
import sys, os, base64, subprocess; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR
import mocks as M, pack as P
from carrusel_logos import mono
from mascota import paw, dog

OUT = '/home/user/gold-studio-final/whatsapp-business/catalogo'
EXT = '''
.q{width:1080px;height:1080px;box-sizing:border-box;padding:84px 84px 70px;position:relative;overflow:hidden;display:flex;flex-direction:column;gap:26px;font-family:J;margin-bottom:20px}
.vis{flex:1;display:flex;align-items:center;justify-content:center;min-height:0}
.chips{display:flex;flex-wrap:wrap;gap:12px}
.chips span{border:2px solid var(--line);border-radius:999px;padding:9px 22px;font-size:25px;color:var(--sub)}
.brand{position:absolute;right:84px;top:84px;width:62px;height:62px;color:var(--g)}
'''
img = lambda p: 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
def phone(src, w=300):
    return (f'<div style="width:{w}px;border-radius:{int(w*.13)}px;background:#1C1A17;padding:{int(w*.035)}px;box-shadow:0 40px 70px -36px rgba(0,0,0,.6)">'
            f'<div style="border-radius:{int(w*.1)}px;overflow:hidden;height:{int(w*1.75)}px"><img src="{src}" style="width:100%;display:block"></div></div>')

def card(bg, eb, title, vis, chips):
    return (f'<div class="q {bg}"><div class="brand">{SP}</div><div class="eb">{eb}</div><h1 style="font-size:92px">{title}</h1>'
            f'<div class="vis">{vis}</div><div class="chips">' + ''.join(f'<span>{c}</span>' for c in chips) + '</div></div>')

A = SCR + '/appshots/'
from carogen import F
XF = '@font-face{font-family:XFam;src:url(' + F + 'familjen-grotesk/files/familjen-grotesk-latin-700-normal.woff2)}'
tiles = ''.join(f'<div style="width:190px;height:190px;border-radius:14px;background:{bg};display:grid;place-items:center;color:{fg};font-family:B;font-size:30px;text-align:center;line-height:1.1;box-shadow:0 18px 30px -22px rgba(0,0,0,.5)">{t}</div>'
                for bg, fg, t in [(M.BRANDS['aura']['c'], '#1C1A17', 'Nueva<br>colección'), ('#1C1A17', '#C9A34E', '✦'), ('#FAF6EE', '#1C1A17', 'Hecho<br>a mano'),
                                  ('#F2EADA', '#8A6A22', '<i>Tips</i>'), (M.BRANDS['aura']['c'], '#FAF6EE', 'Aura'), ('#1C1A17', '#FAF6EE', 'Detrás<br>de escena')])
products = ''.join(f'<div style="flex:1;display:flex;flex-direction:column;gap:8px;align-items:center"><div style="width:100%;height:150px;border-radius:12px;background:{c};display:grid;place-items:center">{paw("#2E6B66", 70)}</div>'
                   f'<span style="font-size:18px;color:#2E6B66">{n}</span><span style="background:#2E6B66;color:#fff;font-size:15px;padding:5px 14px;border-radius:999px">Agregar</span></div>'
                   for c, n in [('#CFE8DE', 'Pelotas'), ('#F7D9CF', 'Collares'), ('#E6F1EC', 'Camitas')])
shop = M.browser(f'<div style="padding:26px 30px;background:#FBF7F0;display:flex;flex-direction:column;gap:20px"><div style="display:flex;justify-content:space-between;align-items:center">'
                 f'<span style="display:flex;align-items:center;gap:8px;font-family:XFam;font-size:34px;color:#2E6B66">' + dog('#2E6B66', 54) + 'huellitas</span><span style="font-size:18px;color:#2E6B66">Carrito (2)</span></div>'
                 f'<div style="display:flex;gap:18px">{products}</div></div>', w=880, url='huellitas.com.ar/tienda')
BR = ('<div style="display:flex;gap:30px;align-items:center">'
      '<div style="width:400px;height:470px;border-radius:26px;background:#FAF6EE;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px">'
      + mono(0.9) + '<span style="font-size:20px;letter-spacing:.4em;color:#8A6A22">AURA · JOYERÍA</span></div>'
      '<div style="display:flex;flex-direction:column;gap:14px">' + ''.join(f'<div style="width:150px;height:105px;border-radius:16px;background:{c};border:2px solid #3A342B"></div>' for c in ['#C9A34E', '#FAF6EE', '#8A6A22', '#26221D'])
      + '</div><div style="display:flex;flex-direction:column;gap:6px;color:#FAF6EE"><span style="font-family:B;font-size:120px;line-height:1">Aa</span><span style="font-size:22px;letter-spacing:.2em;color:#BDB2A0">BODONI</span><span style="font-family:J;font-size:76px;line-height:1;margin-top:20px">Aa</span><span style="font-size:22px;letter-spacing:.2em;color:#BDB2A0">JOST</span></div></div>')
CARDS = [
 ('01-pagina-web', card('m', 'Paquete', 'Página <em>web</em>', M.site('aura', 2, 900), ['Diseño a medida', 'Botón a WhatsApp', 'Perfecta en el celular', 'La publico por vos'])),
 ('02-branding', card('n', 'Paquete', 'Branding <em>y logo</em>', BR, ['Logo y variantes', 'Colores y tipografías', 'Foto de perfil', 'Portadas'])),
 ('03-community-manager', card('m', 'Paquete', 'Community <em>manager</em>', f'<div style="display:grid;grid-template-columns:repeat(3,190px);gap:16px;transform:scale(1.25)">{tiles}</div>', ['Plan mensual', 'Posteos e historias', 'Textos', 'Resumen del mes'])),
 ('04-app-a-medida', card('g', 'A medida', 'Apps <em>a medida</em>', f'<div style="display:flex;gap:26px;align-items:flex-end">{phone(img(A+"p-inicio.png"), 290)}{phone(img(A+"p-turnos.png"), 290)}</div>', ['Turnos', 'Clientes con su cuenta', 'Panel para vos', 'Compu y celular'])),
 ('05-tienda-online', card('n', 'A medida', 'Tienda <em>online</em>', shop, ['Catálogo y carrito', 'Pagos online', 'Envíos', 'Fácil de actualizar'])),
]
def _render():
  page = f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXT}{XF}</style>' + ''.join(c for _, c in CARDS)
  work = SCR + '/wa-cat'; os.makedirs(work, exist_ok=True); open(work + '/c.html', 'w').write(page); os.makedirs(OUT, exist_ok=True)
  names = [n for n, _ in CARDS]
  js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1080}}}});
  await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(300);
  const n={names};const els=await p.$$('.q');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{OUT}/'+n[i]+'.png'}});await b.close();}})();'''
  open(work + '/r.js', 'w').write(js)
  subprocess.run(['node', work + '/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
  print(OUT)

if __name__ == "__main__":
  _render()
