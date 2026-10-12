"""Catálogo completo de WhatsApp Business: varias imágenes 1080x1080 por servicio."""
import sys, os, base64, subprocess, shutil; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR, CHECK, F
import mocks as M
from mascota import paw, dog
from yogi import yogi
from carrusel_logos import mono
import catalogo_wa as C1   # portadas ya armadas (CARDS)

OUT = '/home/user/gold-studio-final/whatsapp-business/catalogo'
EXT = C1.EXT + C1.XF + '''
.inc{display:grid;grid-template-columns:1fr 1fr;gap:30px 40px;margin-top:10px;flex:1;align-content:space-evenly}
.it{display:flex;gap:18px;align-items:flex-start}
.it .ck{width:64px;height:64px;padding:13px;flex:none}
.it b{display:block;font-family:B;font-weight:500;font-size:44px;line-height:1.1}
.it span{display:block;font-size:28px;line-height:1.35;color:var(--sub);margin-top:6px}
.ph{border-radius:44px;background:#1C1A17;padding:12px;box-shadow:0 40px 70px -36px rgba(0,0,0,.6);flex:none}
.ph>div{border-radius:34px;overflow:hidden;background:#fff;position:relative}
.step{display:flex;gap:26px;align-items:flex-start}
.step i{font-family:B;font-style:italic;font-size:70px;line-height:.9;color:var(--g);width:56px;flex:none}
.step b{display:block;font-family:B;font-weight:500;font-size:40px}
.step span{display:block;font-size:26px;color:var(--sub);line-height:1.35;margin-top:4px}
.box{background:var(--box);border-radius:28px;padding:30px 36px;display:flex;justify-content:space-between;align-items:center;gap:20px}
'''
img = C1.img
A = SCR + '/appshots/'
def phone(inner, w=300, h=None):
    h = h or int(w * 2.05)
    return f'<div class="ph" style="width:{w}px"><div style="height:{h - 24}px">{inner}</div></div>'
def shot(p, w=280): return phone(f'<img src="{img(A + p)}" style="width:100%;display:block">', w)

def head(bg, eb, title):
    return f'<div class="q {bg}"><div class="brand">{SP}</div><div class="eb">{eb}</div><h1 style="font-size:80px">{title}</h1>'
def incluye(bg, name, items):
    its = ''.join(f'<div class="it">{CHECK}<div><b>{t}</b><span>{d}</span></div></div>' for t, d in items)
    return head(bg, name, 'Qué <em>incluye</em>') + f'<div class="inc">{its}</div></div>'
def ejemplo(bg, name, title, vis, cap):
    return head(bg, name + ' · Ejemplo', title) + f'<div class="vis">{vis}</div><p style="margin:0;font-size:26px;color:var(--sub)">{cap}</p></div>'

COMO = (head('n', 'Cómo trabajamos', 'Simple y <em>sin vueltas</em>') +
        '<div style="display:flex;flex-direction:column;gap:30px;margin-top:6px">' +
        ''.join(f'<div class="step"><i>{i}</i><div><b>{t}</b><span>{d}</span></div></div>' for i, t, d in [
            (1, 'Charlamos', 'Me contás tu idea y tu negocio, sin tecnicismos.'),
            (2, 'Te muestro una propuesta', 'Con tus colores y tu estilo. Ajustamos hasta que te encante.'),
            (3, 'Lo armo', 'Y te voy mostrando avances para que lo veas crecer.'),
            (4, 'Lo lanzamos', 'Te enseño a usarlo y te sigo acompañando.')]) + '</div>'
        '<div class="box" style="margin-top:auto"><div><div style="font-size:22px;letter-spacing:.3em;color:var(--em);font-weight:500">PRECIO DE LANZAMIENTO</div>'
        '<div style="font-size:28px;margin-top:8px">Los primeros proyectos tienen precio especial.</div></div>'
        '<div class="pill" style="align-self:center;white-space:nowrap">Escribime ✦</div></div></div>')

# ---------- ejemplos ----------
aura = M.BRANDS['aura']
mob_site = (f'<div style="background:{aura["light"]};padding:22px 20px;display:flex;justify-content:space-between;align-items:center"><span style="font-family:B;font-size:30px">Aura</span><span style="font-size:26px">☰</span></div>'
            f'<div style="background:{aura["c"]};color:#FAF6EE;padding:34px 22px;display:flex;flex-direction:column;gap:12px"><span style="font-size:13px;letter-spacing:.3em">JOYERÍA</span>'
            f'<span style="font-family:B;font-size:36px;line-height:1.1">Joyas que<br>brillan con vos</span><span style="align-self:flex-start;background:#1C1A17;padding:9px 18px;border-radius:999px;font-size:14px">Ver colección</span></div>'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:18px">' + ''.join(f'<div style="height:110px;border-radius:12px;background:#FAF6EE;border:2px solid #C9A34E44;display:grid;place-items:center">{mono(.18)}</div>' for _ in range(4)) + '</div>'
            '<div style="position:absolute;right:16px;bottom:18px;width:56px;height:56px;border-radius:50%;background:#25D366"></div>')
web_ex = f'<div style="position:relative;width:900px;height:560px">{M.site("aura", 2, 760)}<div style="position:absolute;right:0;bottom:-40px">{phone(mob_site, 260, 540)}</div></div>'

PR, LAV = '#3E3557', '#D9CFF0'
cell = lambda bg, inner, extra='': f'<div style="background:{bg};border-radius:22px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;position:relative;overflow:hidden;{extra}">{inner}</div>'
lab = lambda t, c: f'<span style="position:absolute;left:18px;top:14px;font-size:16px;letter-spacing:.24em;color:{c};opacity:.8">{t}</span>'
brand_ex = ('<div style="display:grid;grid-template-columns:1.25fr 1fr 1fr;grid-template-rows:280px 280px;gap:18px;width:912px">'
    + cell(PR, lab('LOGO', LAV) + yogi(LAV, 170) + f'<span style="font-family:B;font-size:54px;color:{LAV};line-height:1">Prana</span><span style="font-size:14px;letter-spacing:.4em;color:{LAV}">ESTUDIO DE YOGA</span>', 'grid-row:span 2')
    + cell('#FFFFFF', lab('COLORES', '#555') + '<div style="display:flex;gap:10px">' + ''.join(f'<div style="width:46px;height:120px;border-radius:12px;background:{c};border:1px solid #ddd"></div>' for c in [PR, LAV, '#E8DCC8', '#F7F4EF']) + '</div>')
    + cell('#F7F4EF', lab('TIPOGRAFÍAS', '#555') + f'<span style="font-family:B;font-size:84px;color:{PR};line-height:1">Aa</span><span style="font-size:20px;color:{PR}">Bodoni · Jost</span>')
    + cell(LAV, lab('FOTO DE PERFIL', PR) + f'<div style="width:150px;height:150px;border-radius:50%;background:{PR};display:grid;place-items:center">{yogi(LAV, 110)}</div>')
    + cell('#E8DCC8', lab('TARJETA', PR) + f'<div style="width:220px;height:130px;background:#F7F4EF;border-radius:8px;box-shadow:0 14px 26px -14px rgba(0,0,0,.4);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px">{yogi(PR, 60)}<span style="font-family:B;font-size:24px;color:{PR}">Prana</span></div>')
    + '</div>')

tiles = [(aura['c'], '#1C1A17', 'Nueva<br>colección'), ('#1C1A17', '#C9A34E', '✦'), ('#FAF6EE', '#1C1A17', 'Hecho<br>a mano'),
         ('#F2EADA', '#8A6A22', '<i>Tips</i>'), ('#1C1A17', '#FAF6EE', 'Detrás<br>de escena'), (aura['c'], '#FAF6EE', '<i>Aura</i>'),
         ('#FAF6EE', '#8A6A22', '¿Oro o<br>plata?'), (aura['c'], '#1C1A17', 'Envíos'), ('#1C1A17', '#C9A34E', 'Rese-<br>ñas')]
ig = ('<div style="padding:20px 16px 0;display:flex;gap:16px;align-items:center">'
      f'<div style="width:74px;height:74px;border-radius:50%;background:#FAF6EE;border:2px solid #C9A34E;display:grid;place-items:center">{mono(.16)}</div>'
      '<div style="display:flex;gap:18px;font-size:15px;text-align:center;color:#1C1A17">' + ''.join(f'<div><b style="display:block;font-size:19px">{n}</b>{t}</div>' for n, t in [('128', 'posts'), ('4.210', 'seguidores'), ('310', 'seguidos')]) + '</div></div>'
      '<div style="padding:10px 16px;font-size:15px;line-height:1.35;color:#1C1A17"><b>Aura Joyería</b><br>Joyas hechas a mano ✦ Envíos a todo el país<br><span style="color:#2F4A6D">aura.com.ar</span></div>'
      '<div style="display:flex;gap:10px;padding:4px 16px 12px">' + ''.join(f'<div style="width:46px;height:46px;border-radius:50%;border:2px solid #E6DAC2;background:#FAF6EE"></div>' for _ in range(5)) + '</div>'
      '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px">' + ''.join(f'<div style="aspect-ratio:1;background:{b};color:{f};display:grid;place-items:center;text-align:center;font-family:B;font-size:17px;line-height:1.1">{t}</div>' for b, f, t in tiles) + '</div>')
story = (f'<div style="height:100%;background:{aura["c"]};display:flex;flex-direction:column;justify-content:center;align-items:center;gap:16px;color:#1C1A17;padding:20px;text-align:center">'
         f'<span style="font-size:13px;letter-spacing:.3em">NUEVO</span><span style="font-family:B;font-size:40px;line-height:1.1">Colección<br><i>Otoño</i></span>'
         '<div style="background:#fff;border-radius:16px;padding:12px 18px;font-size:15px;width:80%">¿Cuál te gusta más?<div style="display:flex;gap:8px;margin-top:8px"><span style="flex:1;background:#F2EADA;border-radius:8px;padding:6px">Oro</span><span style="flex:1;background:#F2EADA;border-radius:8px;padding:6px">Plata</span></div></div></div>')
cm_ex = f'<div style="display:flex;gap:40px;align-items:center">{phone(ig, 330, 640)}{phone(story, 280, 560)}</div>'

app_ex = f'<div style="display:flex;gap:24px;align-items:flex-end">{shot("p-inicio.png", 270)}{shot("p-turnos.png", 270)}{shot("p-progreso.png", 270)}</div>'

T, MI = '#2E6B66', '#CFE8DE'
prods = [('#CFE8DE', 'Pelota de tela', '$4.500'), ('#F7D9CF', 'Collar ajustable', '$7.800'), ('#E6F1EC', 'Camita mediana', '$21.000'), ('#F7E9C9', 'Snacks naturales', '$3.200')]
shop_m = (f'<div style="background:#FBF7F0;padding:18px 16px;display:flex;justify-content:space-between;align-items:center">'
          f'<span style="display:flex;align-items:center;gap:6px;font-family:XFam;font-size:24px;color:{T}">{dog(T, 40)}huellitas</span><span style="background:{T};color:#fff;border-radius:999px;padding:5px 12px;font-size:14px">🛒 2</span></div>'
          '<div style="padding:4px 16px 10px;display:flex;gap:8px;font-size:13px">' + ''.join(f'<span style="border:1.5px solid {T};color:{T};border-radius:999px;padding:4px 10px">{c}</span>' for c in ['Perros', 'Gatos', 'Ofertas']) + '</div>'
          '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:0 14px">' +
          ''.join(f'<div style="background:#fff;border-radius:12px;padding:8px;font-size:13px;color:{T}"><div style="height:90px;border-radius:9px;background:{c};display:grid;place-items:center">{paw(T, 42)}</div><div style="margin-top:6px">{n}</div><b>{p}</b></div>' for c, n, p in prods) + '</div>')
checkout = (f'<div style="background:#FBF7F0;height:100%;padding:22px 18px;display:flex;flex-direction:column;gap:14px;color:{T};font-size:15px">'
            '<b style="font-size:22px">Tu carrito</b>' +
            ''.join(f'<div style="display:flex;justify-content:space-between;background:#fff;border-radius:10px;padding:10px">{n}<b>{p}</b></div>' for _, n, p in prods[:2]) +
            '<div style="display:flex;justify-content:space-between;font-size:18px;border-top:1.5px solid #ddd;padding-top:10px">Total<b>$12.300</b></div>'
            '<span style="font-size:13px">Envío a domicilio o retiro</span>'
            f'<div style="background:#009EE3;color:#fff;text-align:center;border-radius:10px;padding:12px;font-weight:500">Pagar con Mercado Pago</div>'
            f'<div style="border:1.5px solid {T};text-align:center;border-radius:10px;padding:10px">Consultar por WhatsApp</div></div>')
shop_ex = f'<div style="display:flex;gap:40px;align-items:center">{phone(shop_m, 320, 620)}{phone(checkout, 300, 580)}</div>'

ITEMS = [
 ('01-pagina-web', 'Página web', 'm', [('Diseño a medida', 'Con tu logo, tus colores y tu estilo.'), ('Las secciones clave', 'Inicio, servicios, trabajos, sobre vos y contacto.'),
   ('Botón a WhatsApp', 'Para que te escriban con un solo toque.'), ('Perfecta en el celular', 'Donde te va a ver la mayoría.'),
   ('La publico por vos', 'Con tu dominio, lista para compartir.'), ('Te acompaño', 'Te enseño a usarla y quedo para lo que necesites.')],
   ('Así se ve <em>en compu y celu</em>', web_ex, 'Ejemplo de página web para una joyería.')),
 ('02-branding', 'Branding y logo', 'n', [('Logo y variantes', 'Versión principal, ícono, clara y oscura.'), ('Paleta de colores', 'Pensada para lo que querés transmitir.'),
   ('Tipografías', 'Una para títulos y otra para textos.'), ('Foto de perfil', 'Lista para Instagram y WhatsApp.'),
   ('Portadas de destacadas', 'Para que tu perfil se vea ordenado.'), ('Guía de uso y archivos', 'PNG, PDF y vector, listos para usar.')],
   ('Una marca <em>completa</em>', brand_ex, 'Ejemplo de identidad para un estudio de yoga.')),
 ('03-community-manager', 'Community manager', 'g', [('Plan mensual', 'Calendario con qué se publica y cuándo.'), ('Posteos y carruseles', 'Con diseño cuidado y tu estética.'),
   ('Historias', 'Encuestas, preguntas y novedades.'), ('Textos', 'Los copys de cada publicación.'),
   ('Feed y destacadas', 'Todo ordenado y con coherencia.'), ('Resumen del mes', 'Cómo le fue a tu cuenta y qué mejorar.')],
   ('Tu perfil, <em>siempre lindo</em>', cm_ex, 'Ejemplo de perfil e historia para una joyería.')),
 ('04-app-a-medida', 'App a medida', 'm', [('Turnos online', 'Tus clientes reservan y vos lo ves todo.'), ('Cuentas para tus clientes', 'Cada uno con su usuario y su info.'),
   ('Panel para vos', 'Manejás todo desde un solo lugar.'), ('Archivos y documentos', 'Planes, PDFs y lo que necesites compartir.'),
   ('Mensajes', 'Hablás con tus clientes dentro de la app.'), ('Compu y celular', 'Funciona en cualquier dispositivo.')],
   ('Una app <em>real</em>', app_ex, 'App hecha para un consultorio de nutrición (datos de prueba).')),
 ('05-tienda-online', 'Tienda online', 'n', [('Catálogo con fotos', 'Tus productos ordenados por categoría.'), ('Carrito de compras', 'Fácil de usar desde el celular.'),
   ('Pagos online', 'Con Mercado Pago, tarjeta o transferencia.'), ('Envíos y retiro', 'Vos elegís cómo entregar.'),
   ('Botón a WhatsApp', 'Para consultas antes de comprar.'), ('Fácil de actualizar', 'Cambiás precios y productos sola.')],
   ('Vendé <em>las 24 horas</em>', shop_ex, 'Ejemplo de tienda para un pet shop.')),
]
def _render():
    covers = dict(C1.CARDS)
    pages, names = [], []
    for key, name, bg, inc, (tt, vis, cap) in ITEMS:
        alt = 'n' if bg != 'n' else 'm'
        for suf, html in [('1-portada', covers[key]), ('2-que-incluye', incluye(alt, name, inc)), ('3-ejemplo', ejemplo('m' if bg == 'g' else bg, name, tt, vis, cap)), ('4-como-trabajamos', COMO)]:
            pages.append(html); names.append(f'{key}/{suf}')
    work = SCR + '/wa-cat2'; os.makedirs(work, exist_ok=True)
    open(work + '/c.html', 'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXT}</style>' + ''.join(pages))
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    for key, *_ in ITEMS: os.makedirs(f'{OUT}/{key}', exist_ok=True)
    js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1080}}}});
    await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(400);
    const n={names};const els=await p.$$('.q');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{OUT}/'+n[i]+'.png'}});await b.close();}})();'''
    open(work + '/r.js', 'w').write(js)
    subprocess.run(['node', work + '/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    print(len(names))

if __name__ == "__main__":
    _render()
