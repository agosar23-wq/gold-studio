"""Historias de Gold Studio (1080×1920): portadas de destacadas, historias para cada destacada e historias creativas.
Sin emojis y con espacio libre para stickers (encuestas, preguntas, links), como pide Agos."""
import sys, os, base64, subprocess, re
sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import SCR, F, SP

OUT = '/home/user/gold-studio-final/historias'
WORK = f'{SCR}/historias-gs'; os.makedirs(WORK, exist_ok=True)
REPO = '/home/user/gold-studio'
def b64(p, mime): return f'data:{mime};base64,' + base64.b64encode(open(p, 'rb').read()).decode()
LOGO = re.sub(r'<svg [^>]*viewBox="([^"]+)"[^>]*>', r'<svg class="logo" viewBox="\1">', open('/home/user/gold-studio-final/logo-gold-studio-transparente.svg').read(), count=1)
LOGO_W = re.sub(r'<svg [^>]*viewBox="([^"]+)"[^>]*>', r'<svg class="logo" viewBox="\1">', open('/home/user/gold-studio-final/logo-gold-studio-transparente-blanco.svg').read(), count=1)
APP = b64(f'{REPO}/img/paciente.jpg', 'image/jpeg')
PANEL = b64(f'{REPO}/img/nutri.jpg', 'image/jpeg')
CAFE = [b64(f'{REPO}/contenido/carruseles/feed-cafeteria/0{i}.png', 'image/png') for i in (1, 6)]
BURG = [b64(f'{REPO}/contenido/carruseles/feed-hamburgueseria/0{i}.png', 'image/png') for i in (1, 6)]
NUTRIA = b64(f'{SCR}/ilus/nutria-taza.jpg', 'image/jpeg')
SENORA0 = b64(f'{SCR}/ilus/senora-taza.jpg', 'image/jpeg')
SENORA = b64(f'{SCR}/ilus/senora-trofeo.png', 'image/png')

# ---------- íconos de línea para las portadas (viewBox 0 0 100 100) ----------
ICON = {
 'servicios': '<path d="M50 14 C53 38 62 47 86 50 C62 53 53 62 50 86 C47 62 38 53 14 50 C38 47 47 38 50 14Z"/>',
 'trabajos':  '<rect x="14" y="22" width="72" height="50" rx="6"/><path d="M14 32 H86 M22 27 h2 M29 27 h2 M36 27 h2 M40 80 H60 M50 72 V80"/>',
 'proceso':   '<path d="M20 78 L22 64 L64 22 L78 36 L36 78 Z M56 30 L70 44 M20 78 L34 76"/>',
 'paquetes':  '<rect x="18" y="40" width="64" height="44" rx="4"/><path d="M14 30 H86 V40 H14 Z M50 30 V84 M50 30 C42 18 28 20 32 28 C35 32 50 30 50 30 C50 30 65 32 68 28 C72 20 58 18 50 30"/>',
 'sobre':     '<circle cx="50" cy="36" r="15"/><path d="M22 84 C24 64 36 56 50 56 C64 56 76 64 78 84"/>',
 'ejemplos':  '<path d="M50 16 C28 16 14 32 14 50 C14 70 30 84 46 84 C54 84 54 76 50 72 C46 66 52 60 58 62 C72 66 86 60 86 46 C86 28 70 16 50 16Z"/><circle cx="34" cy="44" r="5"/><circle cx="48" cy="30" r="5"/><circle cx="66" cy="34" r="5"/>',
 'contacto':  '<path d="M18 22 H82 a6 6 0 0 1 6 6 V62 a6 6 0 0 1 -6 6 H44 L28 80 V68 H18 a6 6 0 0 1 -6 -6 V28 a6 6 0 0 1 6 -6Z"/><path d="M30 40 H70 M30 52 H58"/>',
}
NAMES = {'servicios': 'Servicios', 'trabajos': 'Trabajos', 'proceso': 'Proceso', 'paquetes': 'Paquetes', 'sobre': 'Sobre mí', 'ejemplos': 'Ejemplos', 'contacto': 'Contacto'}
def icon(k, color, w=7):
    return f'<svg viewBox="0 0 100 100" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" style="width:100%;height:100%">{ICON[k]}</svg>'
def cover(k, bg, ring, ink):
    # Instagram recorta un círculo del centro: el ícono va centrado y chico, con un aro fino dorado
    return (f'<div class="st" style="background:{bg};padding:0;align-items:center;justify-content:center">'
            f'<div style="width:620px;height:620px;border-radius:50%;border:6px solid {ring};display:grid;place-items:center">'
            f'<div style="width:300px;height:300px">{icon(k, ink)}</div></div></div>')

# ---------- piezas comunes ----------
def st(cls, inner, style=''): return f'<div class="st {cls}" style="{style}">{inner}</div>'
def hole(h, label='', w=None):   # espacio libre para el sticker (no se ve nada en la historia)
    return f'<div class="hole" style="height:{h}px;{f"width:{w}px;" if w else ""}"></div>'
def phone(img, w=520, rot=0):
    return (f'<div style="width:{w}px;border-radius:{w*.12:.0f}px;background:#111;padding:{w*.03:.0f}px;transform:rotate({rot}deg);'
            f'box-shadow:0 50px 90px -40px rgba(0,0,0,.6)"><div style="border-radius:{w*.1:.0f}px;overflow:hidden"><img src="{img}" style="display:block;width:100%"></div></div>')
def card(img, w=560, rot=0):
    return f'<div style="width:{w}px;transform:rotate({rot}deg);box-shadow:0 40px 80px -36px rgba(0,0,0,.55);border-radius:18px;overflow:hidden"><img src="{img}" style="display:block;width:100%"></div>'
def num(n): return f'<div class="num">{n}</div>'

S = {}
# ---------- portadas de destacadas (dos versiones de color) ----------
for k in ICON:
    S[f'portada-marfil-{k}'] = cover(k, '#FAF6EE', '#C9A34E', '#B8923A')
    S[f'portada-negra-{k}'] = cover(k, '#1C1A17', '#C9A34E', '#C9A34E')

# ---------- historias para cada destacada ----------
SERV = [('Páginas web', 'Para que te encuentren y te escriban.'), ('Apps a medida', 'Turnos, clientes y archivos en un lugar.'),
        ('Tiendas online', 'Tu catálogo vendiendo las 24 horas.'), ('Branding y logos', 'Una identidad que se recuerda.'),
        ('Community manager', 'Tus redes lindas y constantes.')]
S['servicios-1'] = st('m', f'''<div class="eb">Servicios</div><h1>Todo lo que tu marca necesita para <em>brillar.</em></h1>
  <div class="list">{''.join(f'<div class="it"><i>{SP}</i><div><b>{a}</b><span>{b}</span></div></div>' for a, b in SERV)}</div>''')
S['servicios-2'] = st('n', f'''<div class="eb">Contame</div><h1>¿Qué necesita <em>tu marca</em> hoy?</h1>
  <p class="lead">Votá y te cuento por dónde empezar.</p>{hole(520)}''')
S['trabajos-1'] = st('m', f'''<div class="eb">Trabajo destacado</div><h1>Una app a medida para un <em>consultorio de nutrición.</em></h1>
  <div class="row" style="margin-top:70px;justify-content:center">{phone(APP, 470, -3)}</div>''')
S['trabajos-2'] = st('n', f'''<div class="eb">Qué hace</div><h1 style="font-size:96px">Cada paciente tiene <em>su cuenta.</em></h1>
  <div class="chips">{''.join(f'<span>{t}</span>' for t in ['Planes en PDF', 'Recetarios', 'Seguimiento de peso', 'Turnos', 'Mensajes', 'Cuentas privadas'])}</div>
  <div style="margin-top:60px">{card(PANEL, 880)}</div><p class="small">Las capturas usan datos inventados.</p>''')
S['trabajos-3'] = st('g', f'''<div class="mid"><div class="spk">{SP}</div><h1>¿Querés ver <em>la demo?</em></h1>
  <p class="lead">Tocá el link y probala vos.</p>{hole(220, w=640)}</div>''')
PASOS = [('Charlamos', 'Me contás tu idea y tu negocio. Sin tecnicismos.'), ('Diseño', 'Te muestro una propuesta con tus colores y tu estilo.'),
         ('Lo construyo', 'Te voy mostrando avances para que lo veas crecer.'), ('Lo lanzamos', 'Lo publico, te enseño a usarlo y te acompaño.')]
S['proceso-1'] = st('m', f'''<div class="eb">Cómo trabajo</div><h1>Simple, cercano y <em>sin vueltas.</em></h1>
  <div class="steps">{''.join(f'<div class="stp">{num(i+1)}<div><b>{a}</b><span>{b}</span></div></div>' for i, (a, b) in enumerate(PASOS))}</div>''')
S['proceso-2'] = st('n', f'''<div class="eb">Preguntame</div><h1>¿Tenés dudas de <em>cómo es trabajar conmigo?</em></h1>{hole(560)}''')
PAQ = [('Página web', 'Para que tus clientes te encuentren, vean lo que hacés y te escriban.',
        ['Diseño a medida con tu estilo', 'Servicios, trabajos y contacto', 'Botón directo a WhatsApp', 'Perfecta en el celular', 'La publico por vos']),
       ('Branding', 'Para que tu marca se reconozca y se vea linda en todos lados.',
        ['Logo y sus variantes', 'Paleta y tipografías', 'Foto de perfil', 'Portadas de destacadas', 'Archivos listos para usar']),
       ('Community manager', 'Para que tu Instagram sea lindo y constante, sin que te ocupe tiempo.',
        ['Plan de contenido mensual', 'Posteos e historias', 'Textos para cada publicación', 'Feed y destacadas ordenados', 'Resumen de cómo le fue a tu cuenta'])]
for i, (t, d, items) in enumerate(PAQ):
    S[f'paquetes-{i+1}'] = st(['m', 'n', 'm'][i], f'''<div class="eb">Paquete {i+1} de 3</div><h1 style="font-size:116px"><em>{t}</em></h1>
  <p class="lead" style="margin-top:30px">{d}</p>
  <div class="box">{''.join(f'<div class="ck"><i>{SP}</i>{x}</div>' for x in items)}</div>{hole(200, w=640)}''')
S['paquetes-4'] = st('g', f'''<div class="mid"><div class="eb" style="color:#1C1A17">Precio de lanzamiento</div>
  <h1>Los primeros proyectos tienen <em>precio especial.</em></h1><p class="lead">Escribime y te armo un presupuesto según lo que necesites.</p>{hole(220, w=640)}</div>''')
S['sobre-1'] = st('n', f'''<div class="mid"><div style="width:700px">{LOGO_W}</div>
  <h1 style="font-size:96px;margin-top:80px">Cada marca tiene algo que la hace brillar. <em>Mi trabajo es que se note.</em></h1></div>''')
S['sobre-2'] = st('m', f'''<div class="eb">Cómo soy trabajando</div>
  <div class="vals">{''.join(f'<div class="v"><i>{SP}</i><b>{a}</b><span>{b}</span></div>' for a, b in [('A medida', 'Nada de plantillas iguales a todas.'), ('Cercana', 'Me escribís y te respondo yo.'), ('Con detalle', 'Lo lindo también tiene que funcionar.')])}</div>''')
S['ejemplos-1'] = st('n', f'''<div class="eb">Ejemplos de diseño</div><h1 style="font-size:104px">Así diseñaría <em>una cafetería.</em></h1>
  <div class="duo">{card(CAFE[0], 440, -4)}{card(CAFE[1], 440, 4)}</div><p class="lead">Deslizá el carrusel en el feed.</p>{hole(160, w=600)}''')
S['ejemplos-2'] = st('n', f'''<div class="eb">Ejemplos de diseño</div><h1 style="font-size:104px">Así diseñaría <em>una hamburguesería.</em></h1>
  <div class="duo">{card(BURG[0], 440, -4)}{card(BURG[1], 440, 4)}</div><p class="lead">Deslizá el carrusel en el feed.</p>{hole(160, w=600)}''')
S['contacto-1'] = st('m', f'''<div class="mid"><div class="spk">{SP}</div><h1>¿Arrancamos <em>tu proyecto?</em></h1>
  <div class="ct">{''.join(f'<div><span>{a}</span><b>{b}</b></div>' for a, b in [('WhatsApp', '+54 9 11 7136-1309'), ('Instagram', '@goldstudio.ba'), ('Mail', 'goldstudio.ba@gmail.com')])}</div>
  <p class="lead">Te respondo en menos de 24 horas.</p>{hole(200, w=640)}</div>''')

# ---------- historias creativas ----------
PAL = lambda cs: '<div class="pal">' + ''.join(f'<i style="background:{c}"></i>' for c in cs) + '</div>'
S['creativa-esto-o-aquello'] = st('m', f'''<div class="eb">Esto o aquello</div><h1 style="font-size:104px">¿Con cuál paleta te <em>quedás?</em></h1>
  <div class="vs"><div><b>A</b>{PAL(['#2A1A14', '#8A3B2A', '#B4743F', '#E6CFA8', '#EFE7DA'])}<span>Cálida y tranquila</span></div>
  <div><b>B</b>{PAL(['#1C1714', '#7A1F1F', '#C2502A', '#E0A526', '#F3ECE2'])}<span>Intensa y con fuego</span></div></div>{hole(300)}''')
FONTS = [('A', "font-family:B;font-style:italic", 'Café de especialidad'), ('B', "font-family:XA;text-transform:uppercase", 'Café de especialidad'), ('C', "font-family:J;font-weight:300;letter-spacing:.06em", 'Café de especialidad')]
S['creativa-quiz-letra'] = st('n', f'''<div class="eb">Quiz de diseño</div><h1 style="font-size:100px">¿Qué letra usarías para una <em>cafetería cálida?</em></h1>
  <div class="opts">{''.join(f'<div><b>{a}</b><span style="{s}">{t}</span></div>' for a, s, t in FONTS)}</div>{hole(380)}''')
S['creativa-quiz-respuesta'] = st('m', f'''<div class="eb">Respuesta</div><h1 style="font-size:104px">La <em>A</em> es la más cálida.</h1>
  <p class="lead">Una letra con serifa y en itálica se siente artesanal y cercana. La B grita (ideal para hamburguesas) y la C es más fría y moderna.</p>
  <div style="margin-top:70px;align-self:center">{card(CAFE[1], 560, -2)}</div>''')
S['creativa-adivina'] = st('g', f'''<div class="eb" style="color:#1C1A17">Adiviná el rubro</div><h1>Esta paleta, ¿de qué <em>negocio</em> es?</h1>
  {PAL(['#2F4A6D', '#A9BCD0', '#EEF2F6', '#C9A34E']).replace('class="pal"', 'class="pal big"')}<p class="lead" style="color:#3B3122">Respuesta en la próxima historia.</p>{hole(360)}''')
S['creativa-adivina-respuesta'] = st('m', f'''<div class="eb">Respuesta</div><h1>Un <em>consultorio de psicología.</em></h1>
  <p class="lead">El azul da confianza y calma, y el dorado le suma un toque cálido y profesional. Los colores también comunican.</p>
  {PAL(['#2F4A6D', '#A9BCD0', '#EEF2F6', '#C9A34E']).replace('class="pal"', 'class="pal big"')}''')
S['creativa-detras-de-escena'] = st('n', f'''<div class="eb">Detrás de escena</div><h1 style="font-size:100px">Así nació <em>Doña Rulos.</em></h1>
  <div class="ba"><div><span>Primer boceto</span>{card(SENORA0, 400, -3)}</div><div><span>Versión final</span>{card(SENORA, 400, 3)}</div></div>
  <p class="lead">Probé poses hasta que la hamburguesa quedó como un trofeo.</p>{hole(160, w=600)}''')
S['creativa-completa'] = st('m', f'''<div class="eb">Completá la frase</div><h1>Si mi marca fuera una persona, <em>sería…</em></h1>{hole(520)}''')
S['creativa-slider'] = st('n', f'''<div class="mid"><div class="spk">{SP}</div><h1>¿Cuánto te gusta <em>tu feed</em> hoy?</h1>
  <p class="lead">Con sinceridad, nadie te juzga.</p>{hole(240, w=760)}</div>''')
S['creativa-personaje'] = st('m', f'''<div class="eb">Tu marca con personaje</div><h1 style="font-size:100px">¿Te imaginás a tu marca con <em>un personaje así?</em></h1>
  <div class="duo">{card(NUTRIA, 420, -4)}{card(SENORA, 420, 4)}</div>{hole(300)}''')
S['creativa-cuenta-regresiva'] = st('g', f'''<div class="mid"><div class="spk" style="color:#1C1A17">{SP}</div><div class="eb" style="color:#1C1A17">Se viene algo nuevo</div>
  <h1>Activá el <em>recordatorio.</em></h1>{hole(260, w=760)}</div>''')

CSS = f'''
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2);font-weight:500;font-style:italic}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-300-normal.woff2);font-weight:300}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:XA;src:url({F}archivo-black/files/archivo-black-latin-400-normal.woff2)}}
body{{margin:0;background:#888}}
.st{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:J;box-sizing:border-box;padding:250px 96px 340px;display:flex;flex-direction:column}}
.m{{background:#FAF6EE;color:#1C1A17;--em:#8A6A22;--sub:#5E5649;--g:#B8923A;--box:#F2EADA}}
.n{{background:#1C1A17;color:#FAF6EE;--em:#C9A34E;--sub:#BDB2A0;--g:#C9A34E;--box:#26221D}}
.g{{background:#C9A34E;color:#1C1A17;--em:#FAF6EE;--sub:#3B3122;--g:#FAF6EE;--box:#D4B263}}
h1{{font-family:B;font-weight:500;font-size:118px;line-height:1.05;margin:0;letter-spacing:-.01em}} h1 em{{font-style:italic;color:var(--em)}}
.eb{{font-size:30px;letter-spacing:.34em;text-transform:uppercase;color:var(--em);font-weight:500;margin-bottom:34px}}
.lead{{font-size:44px;line-height:1.35;color:var(--sub);font-weight:300;margin:44px 0 0}}
.small{{font-size:26px;color:var(--sub);margin-top:26px;text-align:center}}
.mid{{flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}}
.spk{{width:120px;height:120px;color:var(--g);margin-bottom:50px}} .sp{{width:100%;height:100%;display:block}} .logo{{width:100%;height:auto;display:block}}
.hole{{margin-top:auto;align-self:center;width:100%}}
.mid .hole{{margin-top:70px}}
.list{{margin-top:70px;display:flex;flex-direction:column;gap:40px}}
.it{{display:flex;gap:30px;align-items:flex-start}} .it i{{width:44px;height:44px;color:var(--g);flex:none;margin-top:14px}}
.it b{{display:block;font-family:B;font-weight:500;font-size:64px;line-height:1.1}} .it span{{font-size:36px;color:var(--sub);font-weight:300}}
.row{{display:flex}}
.chips{{display:flex;flex-wrap:wrap;gap:16px;margin-top:50px}} .chips span{{border:2px solid var(--g);color:var(--em);border-radius:999px;padding:14px 30px;font-size:32px}}
.steps{{margin-top:70px;display:flex;flex-direction:column;gap:46px}}
.stp{{display:flex;gap:34px;align-items:flex-start}} .num{{font-family:B;font-style:italic;font-size:120px;line-height:.8;color:var(--g);width:90px;flex:none}}
.stp b{{display:block;font-family:B;font-weight:500;font-size:66px;line-height:1.1}} .stp span{{font-size:38px;color:var(--sub);font-weight:300;line-height:1.3}}
.box{{margin-top:60px;background:var(--box);border-radius:36px;padding:50px 54px;display:flex;flex-direction:column;gap:28px}}
.ck{{display:flex;gap:24px;align-items:center;font-size:42px}} .ck i{{width:34px;height:34px;color:var(--g);flex:none}}
.vals{{display:flex;flex-direction:column;gap:70px;margin-top:40px;flex:1;justify-content:center}}
.v i{{display:block;width:70px;height:70px;color:var(--g);margin-bottom:24px}} .v b{{display:block;font-family:B;font-weight:500;font-size:96px;line-height:1}} .v span{{font-size:44px;color:var(--sub);font-weight:300}}
.duo{{display:flex;justify-content:center;gap:10px;margin-top:70px}}
.ct{{display:flex;flex-direction:column;gap:34px;margin-top:70px}} .ct span{{display:block;font-size:28px;letter-spacing:.3em;text-transform:uppercase;color:var(--em)}} .ct b{{font-size:52px;font-weight:400}}
.pal{{display:flex;height:150px;border-radius:24px;overflow:hidden;margin:20px 0}} .pal i{{flex:1}} .pal.big{{height:260px;margin-top:80px}}
.vs{{display:flex;flex-direction:column;gap:60px;margin-top:80px}} .vs b{{font-family:B;font-style:italic;font-size:80px;color:var(--g)}} .vs span{{font-size:38px;color:var(--sub)}}
.opts{{display:flex;flex-direction:column;gap:30px;margin-top:70px}} .opts div{{background:var(--box);border-radius:28px;padding:34px 44px;display:flex;align-items:center;gap:40px}}
.opts b{{font-family:B;font-style:italic;font-size:70px;color:var(--g);width:60px}} .opts span{{font-size:60px}}
.ba{{display:flex;justify-content:center;gap:24px;margin-top:70px}} .ba > div{{display:flex;flex-direction:column;align-items:center;gap:24px}} .ba > div > span{{font-size:28px;letter-spacing:.3em;text-transform:uppercase;color:var(--em)}}
'''

def render():
    if os.path.isdir(OUT):
        for root, _, files in os.walk(OUT):
            for f in files:
                if f.endswith('.png'): os.remove(os.path.join(root, f))
    page = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>' + ''.join(f'<div id="{k}">{v}</div>' for k, v in S.items())
    open(f'{WORK}/h.html', 'w').write(page)
    def dest(k):
        sub = 'portadas-destacadas' if k.startswith('portada') else 'creativas' if k.startswith('creativa') else 'destacadas'
        os.makedirs(f'{OUT}/{sub}', exist_ok=True); return f'{OUT}/{sub}/{k}.png'
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1920}}}});"
          f"await p.goto('file://{WORK}/h.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready}});await p.waitForTimeout(400);"
          + ''.join(f"await (await p.$('#{k} > .st')).screenshot({{path:'{dest(k)}'}});" for k in S) + "await b.close();})();")
    open(f'{WORK}/h.js', 'w').write(js)
    subprocess.run(['node', f'{WORK}/h.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    return OUT

if __name__ == '__main__':
    print(render(), len(S))
