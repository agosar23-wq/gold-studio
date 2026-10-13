"""Catálogo de WhatsApp Business con fotos reales de Pexels: 5 servicios x 4 imágenes 1080x1080."""
import sys, os, subprocess, shutil; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR, CHECK
import catalogo_wa as C1
import catalogo_wa2 as C2   # ejemplos (web_ex, brand_ex, cm_ex, app_ex, shop_ex)
from mockups_marcas import OUT as MK   # mockups de las marcas de ejemplo (carrusel_branding)
BRAND_GRID = ('<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;width:900px;height:600px">' +
              ''.join(f'<div style="position:relative;overflow:hidden;border-radius:18px;box-shadow:0 24px 40px -26px rgba(0,0,0,.6)">'
                      f'<img src="file://{MK}{n}.jpg" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{p}"></div>'
                      for n, p in [('almendra-bolsa', '50% 55%'), ('ondina-etiqueta', '50% 50%'), ('nacar-bolsas', '55% 50%'), ('nube-caja', '50% 50%')]) + '</div>')

OUT = '/home/user/gold-studio-final/whatsapp-business/catalogo'
FOTOS = SCR + '/fotos-pexels/'   # fotos de Pexels (licencia libre), nombre = id de la foto
def foto(pid, pos='50% 50%', extra=''):
    return f'<img class="ft" src="file://{FOTOS}{pid}.jpg" style="object-position:{pos};{extra}">'

EXT = C1.EXT + C1.XF + C2.EXT + '''
.q{padding:0;gap:0}
.ft{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.frame{position:absolute;inset:30px;border:1.5px solid rgba(201,163,78,.75);border-radius:6px;pointer-events:none;z-index:3}
.shade{position:absolute;inset:0;z-index:1}
.over{position:absolute;inset:0;z-index:2;padding:84px;display:flex;flex-direction:column;gap:24px;box-sizing:border-box}
.q .brand{z-index:4}
.cov h1{color:#FAF6EE}
.cov .eb{color:#C9A34E}
.cov .chips span{border-color:rgba(250,246,238,.45);color:#FAF6EE;background:rgba(28,26,23,.25);backdrop-filter:blur(6px)}
.tag{align-self:flex-start;display:flex;align-items:center;gap:12px;background:rgba(250,246,238,.92);color:#1C1A17;border-radius:999px;padding:12px 24px 12px 18px;font-size:22px;letter-spacing:.28em;font-weight:500}
.tag i{width:26px;height:26px;color:#B8923A;display:block}
.split{position:absolute;inset:0;display:flex}
.split .pic{position:relative;width:420px;flex:none;overflow:hidden}
.split .txt{flex:1;padding:84px 74px 70px 66px;display:flex;flex-direction:column;gap:22px;position:relative}
.lst{display:flex;flex-direction:column;gap:30px;margin-top:8px}
.lst .it .ck{width:56px;height:56px;padding:11px}
.lst .it b{font-size:36px}
.lst .it span{font-size:24px;margin-top:3px}
.stp{display:flex;flex-direction:column;gap:24px;margin-top:4px}
.stp .step i{font-size:60px;width:46px}
.stp .step b{font-size:34px}
.stp .step span{font-size:23px}
.cap{align-self:flex-start;background:rgba(250,246,238,.94);color:#5E5649;border-radius:999px;padding:12px 26px;font-size:22px}
.exh{background:rgba(250,246,238,.95);color:#1C1A17;border-radius:24px;padding:30px 36px;align-self:flex-start;max-width:640px}
.exh .eb{color:#8A6A22;font-size:20px}
.exh h1{font-size:62px;margin-top:8px}
.exh h1 em{color:#8A6A22}
'''
SPK = f'<i>{SP}</i>'
def brand(): return f'<div class="brand">{SP}</div>'

def portada(pid, pos, eb, title, chips):
    return (f'<div class="q n cov">{foto(pid, pos)}'
            '<div class="shade" style="background:linear-gradient(to top,rgba(28,26,23,.94) 0%,rgba(28,26,23,.72) 34%,rgba(28,26,23,.1) 66%,rgba(28,26,23,0) 100%)"></div>'
            f'<div class="frame"></div>{brand()}<div class="over"><div class="tag">{SPK}GOLD STUDIO</div><div style="flex:1"></div>'
            f'<div class="eb">{eb}</div><h1 style="font-size:104px">{title}</h1>'
            '<div class="chips" style="margin-top:6px">' + ''.join(f'<span>{c}</span>' for c in chips) + '</div></div></div>')

def incluye(pid, pos, name, items):
    its = ''.join(f'<div class="it">{CHECK}<div><b>{t}</b><span>{d}</span></div></div>' for t, d in items)
    return (f'<div class="q m"><div class="split"><div class="pic">{foto(pid, pos)}</div>'
            f'<div class="txt"><div class="eb">{name}</div><h1 style="font-size:76px">Qué <em>incluye</em></h1><div class="lst">{its}</div></div></div>{brand()}</div>')

def ejemplo(pid, pos, name, title, vis, cap, scale=1):
    return (f'<div class="q n">{foto(pid, pos)}<div class="shade" style="background:rgba(28,26,23,.38)"></div><div class="frame"></div>{brand()}'
            f'<div class="over"><div class="exh"><div class="eb">{name} · Ejemplo</div><h1>{title}</h1></div>'
            f'<div class="vis"><div style="transform:scale({scale})">{vis}</div></div><div class="cap">{cap}</div></div></div>')

STEPS = [(1, 'Charlamos', 'Me contás tu idea y tu negocio, sin tecnicismos.'),
         (2, 'Te muestro una propuesta', 'Con tus colores y tu estilo. Ajustamos hasta que te encante.'),
         (3, 'Lo armo', 'Y te voy mostrando avances para que lo veas crecer.'),
         (4, 'Lo lanzamos', 'Te enseño a usarlo y te sigo acompañando.')]
def como(pid, pos):
    st = ''.join(f'<div class="step"><i>{i}</i><div><b>{t}</b><span>{d}</span></div></div>' for i, t, d in STEPS)
    return (f'<div class="q n"><div class="split"><div class="txt" style="padding:84px 60px 70px 84px">'
            f'<div class="eb">Cómo trabajamos</div><h1 style="font-size:70px">Simple y <em>sin vueltas</em></h1><div class="stp">{st}</div>'
            '<div class="box" style="margin-top:auto;padding:24px 28px;flex-direction:column;align-items:flex-start;gap:14px">'
            '<div><div style="font-size:19px;letter-spacing:.3em;color:var(--em);font-weight:500">PRECIO DE LANZAMIENTO</div>'
            '<div style="font-size:24px;margin-top:6px">Los primeros proyectos tienen precio especial.</div></div>'
            '<div class="pill" style="font-size:26px;padding:16px 30px">Escribime ✦</div></div></div>'
            f'<div class="pic">{foto(pid, pos)}<div class="frame" style="inset:24px"></div></div></div></div>')

ITEMS = [  # carpeta, nombre, portada, incluye, ejemplo, como
 ('01-pagina-web', 'Página web',
  ('8472383', '50% 50%', 'Paquete', 'Página <em>web</em>', ['Diseño a medida', 'Botón a WhatsApp', 'Perfecta en el celular', 'La publico por vos']),
  ('3756681', '68% 50%', C2.ITEMS[0][3]),
  ('4402584', '50% 50%', 'Así se ve <em>en compu y celu</em>', C2.web_ex, 'Ejemplo de página web para una joyería (marca inventada).', .86),
  ('5029146', '45% 40%')),
 ('02-branding', 'Branding y logo',
  ('7598017', '50% 50%', 'Paquete', 'Branding <em>y logo</em>', ['Logo y variantes', 'Colores y tipografías', 'Foto de perfil', 'Portadas']),
  ('4466176', '50% 50%', C2.ITEMS[1][3]),
  ('3831861', '50% 50%', 'Una marca <em>completa</em>', BRAND_GRID, 'Logo, colores y packaging de 4 marcas inventadas.', 1),
  ('7598023', '50% 50%')),
 ('03-community-manager', 'Community manager',
  ('17557115', '45% 50%', 'Paquete', 'Community <em>manager</em>', ['Plan mensual', 'Posteos e historias', 'Textos', 'Resumen del mes']),
  ('14920164', '50% 40%', C2.ITEMS[2][3]),
  ('28976909', '50% 50%', 'Tu perfil, <em>siempre lindo</em>', C2.cm_ex, 'Ejemplo de perfil e historia para una joyería (marca inventada).', .86),
  ('3874627', '50% 50%')),
 ('04-app-a-medida', 'App a medida',
  ('20044366', '50% 55%', 'A medida', 'Apps <em>a medida</em>', ['Turnos', 'Clientes con su cuenta', 'Panel para vos', 'Compu y celular']),
  ('4549410', '50% 50%', C2.ITEMS[3][3]),
  ('30234387', '50% 50%', 'Una app <em>real</em>', C2.app_ex, 'App hecha para un consultorio de nutrición (datos de prueba).', .86),
  ('3756679', '62% 50%')),
 ('05-tienda-online', 'Tienda online',
  ('7289733', '50% 30%', 'A medida', 'Tienda <em>online</em>', ['Catálogo y carrito', 'Pagos online', 'Envíos', 'Fácil de actualizar']),
  ('7857523', '72% 50%', C2.ITEMS[4][3]),
  ('6237886', '50% 50%', 'Vendé <em>las 24 horas</em>', C2.shop_ex, 'Ejemplo de tienda para un pet shop (marca inventada).', .86),
  ('7289740', '50% 50%')),
]
CREDITOS = 'Fotos de Pexels (pexels.com/photo/<id>), licencia libre de Pexels.'

def _render():
    pages, names = [], []
    for key, name, pt, inc, ex, co in ITEMS:
        for suf, html in [('1-portada', portada(*pt)), ('2-que-incluye', incluye(inc[0], inc[1], name, inc[2])),
                          ('3-ejemplo', ejemplo(ex[0], ex[1], name, *ex[2:])), ('4-como-trabajamos', como(*co))]:
            pages.append(html); names.append(f'{key}/{suf}')
    work = SCR + '/wa-cat3'; os.makedirs(work, exist_ok=True)
    open(work + '/c.html', 'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXT}</style>' + ''.join(pages))
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    for key, *_ in ITEMS: os.makedirs(f'{OUT}/{key}', exist_ok=True)
    js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1080}}}});
    await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;
    await Promise.all([...document.images].map(i=>i.complete?0:new Promise(r=>{{i.onload=i.onerror=r}})));}});await p.waitForTimeout(500);
    const n={names};const els=await p.$$('.q');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{OUT}/'+n[i]+'.png'}});await b.close();}})();'''
    open(work + '/r.js', 'w').write(js)
    subprocess.run(['node', work + '/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    print(len(names), OUT)

if __name__ == "__main__":
    _render()
