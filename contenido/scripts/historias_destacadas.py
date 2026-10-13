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

# ---------- fotos y capturas ----------
EST = lambda i: b64(f'{SCR}/estudio/{i}.jpg', 'image/jpeg')       # Pexels: escritorio de diseñadora, sin caras
F_TECLADO, F_TABLET, F_TABLET2, F_ESPALDA, F_PLANTAS, F_PARED = EST(7015029), EST(7015034), EST(7015038), EST(7015031), EST(7015024), EST(7015037)
WEB_M, WEB_D = b64(f'{SCR}/web/movil.png', 'image/png'), b64(f'{SCR}/web/compu.png', 'image/png')
CAFE7, BURG7, CAFE3, BURG3 = (b64(f'{REPO}/contenido/carruseles/feed-{n}/0{i}.png', 'image/png') for n, i in [('cafeteria', 7), ('hamburgueseria', 7), ('cafeteria', 3), ('hamburgueseria', 3)])
CAFE_F = [b64(f'{SCR}/pexels/{i}.jpg', 'image/jpeg') for i in (4792689, 4792687, 4792692)]
BURG_F = [b64(f'{SCR}/burger/{i}.jpg', 'image/jpeg') for i in ('prod_flota', 8477224, 'prod_bacon')]

def bgphoto(img, pos='center', dark=.55, grad=True):
    sh = (f'linear-gradient(rgba(20,16,12,{min(.92, dark+.2)}),rgba(20,16,12,{dark*.75}) 45%,rgba(20,16,12,{min(.92, dark+.15)}) 85%)' if grad
          else f'linear-gradient(rgba(20,16,12,{dark}),rgba(20,16,12,{dark}))')
    return f'<div style="position:absolute;inset:0;background:{sh},url({img}) {pos}/cover no-repeat;z-index:0"></div>'
def ph(img, h, pos='center', r=28, extra=''):
    return f'<div style="height:{h}px;border-radius:{r}px;background:url({img}) {pos}/cover no-repeat;{extra}"></div>'
def laptop(img, w=760):
    return (f'<div style="width:{w}px"><div style="background:#1b1b1b;border-radius:{w*.03:.0f}px {w*.03:.0f}px 0 0;padding:{w*.022:.0f}px">'
            f'<div style="aspect-ratio:16/10;background:url({img}) top/cover"></div></div>'
            f'<div style="height:{w*.035:.0f}px;background:linear-gradient(#cfcac2,#a9a49c);border-radius:0 0 {w*.04:.0f}px {w*.04:.0f}px;margin:0 -{w*.06:.0f}px"></div></div>')
def phone2(img, w=300, rot=0, pos='top'):
    return (f'<div style="width:{w}px;border-radius:{w*.14:.0f}px;background:#111;padding:{w*.035:.0f}px;transform:rotate({rot}deg);box-shadow:0 40px 80px -30px rgba(0,0,0,.55)">'
            f'<div style="border-radius:{w*.11:.0f}px;aspect-ratio:9/19.5;background:url({img}) {pos}/cover"></div></div>')
def sticker(txt, rot=-4):
    return f'<div class="stk" style="transform:rotate({rot}deg)">{txt}</div>'

SERV = [('Páginas web', 'Para que te encuentren y te escriban.', WEB_D, '70% top'), ('Apps a medida', 'Turnos, clientes y archivos en un lugar.', APP, 'top'),
        ('Tiendas online', 'Tu catálogo vendiendo las 24 horas.', BURG_F[2], 'center'), ('Branding y logos', 'Una identidad que se recuerda.', CAFE3, 'center 60%'),
        ('Community manager', 'Tus redes lindas y constantes.', CAFE7, 'center 70%')]
S['servicios-1'] = st('m', f'''<div class="eb">Servicios</div><h1 style="font-size:100px">Todo lo que tu marca necesita para <em>brillar.</em></h1>
  <div class="list2">{''.join(f'<div class="it2">{ph(img, 150, pos, 22, "width:150px;flex:none")}<div><b>{a}</b><span>{b}</span></div></div>' for a, b, img, pos in SERV)}</div>''')
S['servicios-2'] = st('n', f'''{bgphoto(F_TABLET, "center 60%", .7)}<div class="z"><div class="eb">Contame</div><h1>¿Qué necesita <em>tu marca</em> hoy?</h1>
  <p class="lead">Votá y te cuento por dónde empezar.</p></div>''')
S['trabajos-1'] = st('m', f'''<div class="eb">Trabajo destacado</div><h1 style="font-size:100px">Una app a medida para un <em>consultorio de nutrición.</em></h1>
  <div style="position:relative;margin-top:90px;height:820px">
    <div style="position:absolute;left:-10px;top:60px">{laptop(PANEL, 820)}</div>
    <div style="position:absolute;right:-20px;top:170px">{phone2(APP, 290, 4)}</div>
    <div style="position:absolute;left:20px;top:600px">{sticker("Compu y celular", -5)}</div></div>''')
S['trabajos-2'] = st('n', f'''<div class="eb">Qué hace</div><h1 style="font-size:96px">Cada paciente tiene <em>su cuenta.</em></h1>
  <div style="display:flex;gap:40px;margin-top:70px;align-items:flex-start">{phone2(APP, 360, -3)}
  <div class="feat">{''.join(f'<div><i>{SP}</i>{t}</div>' for t in ['Planes en PDF', 'Recetarios', 'Seguimiento de peso', 'Turnos', 'Mensajes', 'Cuentas privadas'])}</div></div>
  <p class="small" style="margin-top:50px">Las capturas usan datos inventados.</p>''')
S['trabajos-3'] = st('n', f'''{bgphoto(F_TECLADO, "center 40%", .62)}<div class="z mid"><div class="spk">{SP}</div><h1>¿Querés ver <em>la demo?</em></h1>
  <p class="lead" style="color:#EFE7DA">Tocá el link y probala vos.</p>{hole(220, w=640)}</div>''')
PASOS = [('Charlamos', 'Me contás tu idea y tu negocio. Sin tecnicismos.', F_TECLADO, 'center 60%'),
         ('Diseño', 'Te muestro una propuesta con tus colores y tu estilo.', F_TABLET, 'center 65%'),
         ('Lo construyo', 'Te voy mostrando avances para que lo veas crecer.', F_TABLET2, 'center 40%'),
         ('Lo lanzamos', 'Lo publico, te enseño a usarlo y te acompaño.', WEB_D, '70% top')]
S['proceso-1'] = st('m', f'''<div class="eb">Cómo trabajo</div><h1 style="font-size:100px">Simple, cercano y <em>sin vueltas.</em></h1>
  <div class="tl">{''.join(f'<div class="tli">{ph(img, 200, pos, 24, "width:200px;flex:none")}<div><div class="n2">0{i+1}</div><b>{a}</b><span>{b}</span></div></div>' for i, (a, b, img, pos) in enumerate(PASOS))}</div>''')
S['proceso-2'] = st('n', f'''{bgphoto(F_ESPALDA, "center 30%", .72)}<div class="z"><div class="eb">Preguntame</div><h1>¿Tenés dudas de <em>cómo es trabajar conmigo?</em></h1></div>''')
PAQ = [('Página web', 'Para que tus clientes te encuentren, vean lo que hacés y te escriban.',
        ['Diseño a medida con tu estilo', 'Servicios, trabajos y contacto', 'Botón directo a WhatsApp', 'Perfecta en el celular', 'La publico por vos'],
        f'<div style="position:relative;height:560px"><div style="position:absolute;left:0;top:30px">{laptop(WEB_D, 700)}</div><div style="position:absolute;right:0;top:0">{phone2(WEB_M, 250, 5)}</div></div>'),
       ('Branding', 'Para que tu marca se reconozca y se vea linda en todos lados.',
        ['Logo y sus variantes', 'Paleta y tipografías', 'Foto de perfil', 'Portadas de destacadas', 'Archivos listos para usar'],
        f'<div style="display:flex;justify-content:center;gap:24px">{card(CAFE3, 400, -3)}{card(BURG3, 400, 3)}</div>'),
       ('Community manager', 'Para que tu Instagram sea lindo y constante, sin que te ocupe tiempo.',
        ['Plan de contenido mensual', 'Posteos e historias', 'Textos para cada publicación', 'Feed y destacadas ordenados', 'Resumen de cómo le fue a tu cuenta'],
        f'<div style="display:flex;justify-content:center;gap:24px">{card(CAFE7, 400, -3)}{card(BURG7, 400, 3)}</div>')]
for i, (t, d, items, vis) in enumerate(PAQ):
    S[f'paquetes-{i+1}'] = st(['m', 'n', 'm'][i], f'''<div class="eb">Paquete {i+1} de 3</div><h1 style="font-size:110px"><em>{t}</em></h1>
  <p class="lead" style="margin-top:24px;font-size:40px">{d}</p><div style="margin-top:50px">{vis}</div>
  <div class="box" style="margin-top:50px;padding:40px 50px;gap:20px">{''.join(f'<div class="ck" style="font-size:38px"><i>{SP}</i>{x}</div>' for x in items)}</div>''')
S['paquetes-4'] = st('g', f'''{bgphoto(F_TABLET2, "center 50%", .25, grad=False)}<div class="z mid" style="background:#C9A34E;border-radius:44px;padding:80px 60px;margin:auto 0">
  <div class="eb" style="color:#1C1A17">Precio de lanzamiento</div><h1 style="font-size:104px">Los primeros proyectos tienen <em>precio especial.</em></h1>
  <p class="lead" style="color:#3B3122">Escribime y te armo un presupuesto según lo que necesites.</p></div>''')
S['sobre-1'] = st('n', f'''{bgphoto(F_ESPALDA, "center 35%", .78)}<div class="z mid"><div style="width:640px">{LOGO_W}</div>
  <h1 style="font-size:92px;margin-top:80px">Cada marca tiene algo que la hace brillar. <em>Mi trabajo es que se note.</em></h1></div>''')
VALS = [('A medida', 'Nada de plantillas iguales a todas.', F_TABLET), ('Cercana', 'Me escribís y te respondo yo.', F_TECLADO), ('Con detalle', 'Lo lindo también tiene que funcionar.', F_PLANTAS)]
S['sobre-2'] = st('m', f'''<div class="eb">Cómo soy trabajando</div>
  <div class="vals2">{''.join(f'<div>{ph(img, 300, "center", 28)}<b>{a}</b><span>{b}</span></div>' for a, b, img in VALS)}</div>''')
for k, (nm, slides, fotos) in {'ejemplos-1': ('una cafetería', CAFE, CAFE_F), 'ejemplos-2': ('una hamburguesería', BURG, BURG_F)}.items():
    S[k] = st('n', f'''<div class="eb">Ejemplos de diseño</div><h1 style="font-size:100px">Así diseñaría <em>{nm}.</em></h1>
  <div class="strip">{''.join(ph(f, 260, 'center', 20) for f in fotos)}</div>
  <div class="duo" style="margin-top:50px">{card(slides[0], 430, -4)}{card(slides[1], 430, 4)}</div><p class="lead" style="text-align:center">Deslizá el carrusel en el feed.</p>''')
S['contacto-1'] = st('n', f'''{bgphoto(F_TECLADO, "center 60%", .7)}<div class="z mid"><div class="spk">{SP}</div><h1>¿Arrancamos <em>tu proyecto?</em></h1>
  <div class="ct glass">{''.join(f'<div><span>{a}</span><b>{b}</b></div>' for a, b in [('WhatsApp', '+54 9 11 7136-1309'), ('Instagram', '@goldstudio.ba'), ('Mail', 'goldstudio.ba@gmail.com')])}</div>
  <p class="lead" style="color:#EFE7DA">Te respondo en menos de 24 horas.</p>{hole(180, w=640)}</div>''')

# ---------- historias creativas ----------
PAL = lambda cs: '<div class="pal">' + ''.join(f'<i style="background:{c}"></i>' for c in cs) + '</div>'
S['creativa-esto-o-aquello'] = st('m', f'''<div class="eb">Esto o aquello</div><h1 style="font-size:100px">¿Con cuál estilo te <em>quedás?</em></h1>
  <div class="vs2"><div><b>A</b><div class="mini">{''.join(ph(f, 230, 'center', 16) for f in CAFE_F)}</div>{PAL(['#2A1A14', '#8A3B2A', '#B4743F', '#E6CFA8', '#EFE7DA'])}<span>Cálido y tranquilo</span></div>
  <div><b>B</b><div class="mini">{''.join(ph(f, 230, 'center', 16) for f in BURG_F)}</div>{PAL(['#1C1714', '#7A1F1F', '#C2502A', '#E0A526', '#F3ECE2'])}<span>Intenso y con fuego</span></div></div>''')
FONTS = [('A', "font-family:B;font-style:italic", 'Café de especialidad'), ('B', "font-family:XA;text-transform:uppercase", 'Café de especialidad'), ('C', "font-family:J;font-weight:300;letter-spacing:.06em", 'Café de especialidad')]
S['creativa-quiz-letra'] = st('n', f'''{bgphoto(CAFE_F[0], "center", .72, grad=False)}<div class="z"><div class="eb">Quiz de diseño</div><h1 style="font-size:96px">¿Qué letra usarías para una <em>cafetería cálida?</em></h1>
  <div class="opts">{''.join(f'<div><b>{a}</b><span style="{s}">{t}</span></div>' for a, s, t in FONTS)}</div></div>''')
S['creativa-quiz-respuesta'] = st('m', f'''<div class="eb">Respuesta</div><h1 style="font-size:104px">La <em>A</em> es la más cálida.</h1>
  <p class="lead">Una letra con serifa y en itálica se siente artesanal y cercana. La B grita (ideal para hamburguesas) y la C es más fría y moderna.</p>
  <div style="margin-top:70px;align-self:center">{card(CAFE[1], 560, -2)}</div>''')
PSI = ['#2F4A6D', '#A9BCD0', '#EEF2F6', '#C9A34E']
S['creativa-adivina'] = st('g', f'''<div class="eb" style="color:#1C1A17">Adiviná el rubro</div><h1>Esta paleta, ¿de qué <em>negocio</em> es?</h1>
  <div class="sw">{''.join(f'<div><i style="background:{c}"></i><span>{c}</span></div>' for c in PSI)}</div><p class="lead" style="color:#3B3122">Respuesta en la próxima historia.</p>''')
S['creativa-adivina-respuesta'] = st('m', f'''<div class="eb">Respuesta</div><h1 style="font-size:104px">Un <em>consultorio de psicología.</em></h1>
  <p class="lead">El azul da confianza y calma, y el dorado le suma un toque cálido y profesional.</p>
  <div class="brand"><div class="bc" style="background:#2F4A6D;color:#EEF2F6"><span style="font-family:J;letter-spacing:.3em;font-size:22px">CONSULTORIO</span><b style="font-family:B;font-style:italic;font-size:88px;font-weight:500">Clara</b><span style="font-size:24px;color:#C9A34E;letter-spacing:.3em">PSICOLOGÍA</span></div>
  <div class="bp" style="background:#EEF2F6;color:#2F4A6D"><b style="font-family:B;font-size:46px;font-weight:500;line-height:1.1">Hablar también es <i style="color:#C9A34E">cuidarte.</i></b></div>
  {PAL(PSI)}</div><p class="small">Marca inventada para el ejemplo.</p>''')
S['creativa-detras-de-escena'] = st('n', f'''<div class="eb">Detrás de escena</div><h1 style="font-size:100px">Así nació <em>Doña Rulos.</em></h1>
  <div class="ba"><div><span>Primer boceto</span>{card(SENORA0, 400, -3)}</div><div><span>Versión final</span>{card(SENORA, 400, 3)}</div></div>
  <div style="display:flex;justify-content:center;margin-top:40px">{card(BURG[1], 360, -2)}</div>''')
S['creativa-completa'] = st('m', f'''{bgphoto(F_PLANTAS, "center", .0, grad=False)}<div class="z" style="background:#FAF6EE;border-radius:40px;padding:60px"><div class="eb">Completá la frase</div><h1 style="font-size:100px">Si mi marca fuera una persona, <em>sería…</em></h1></div>''')
S['creativa-slider'] = st('n', f'''{bgphoto(F_PARED, "center 30%", .7)}<div class="z mid"><div class="spk">{SP}</div><h1>¿Cuánto te gusta <em>tu feed</em> hoy?</h1>
  <p class="lead" style="color:#EFE7DA">Con sinceridad, nadie te juzga.</p>{hole(240, w=760)}</div>''')
S['creativa-personaje'] = st('m', f'''<div class="eb">Tu marca con personaje</div><h1 style="font-size:96px">¿Te imaginás a tu marca con <em>un personaje así?</em></h1>
  <div class="duo">{card(CAFE[1], 430, -4)}{card(BURG[1], 430, 4)}</div>''')
S['creativa-cuenta-regresiva'] = st('g', f'''{bgphoto(F_TABLET2, "center 45%", .15, grad=False)}<div class="z mid" style="background:#C9A34E;border-radius:44px;padding:80px 50px;margin:auto 0"><div class="spk" style="color:#1C1A17">{SP}</div><div class="eb" style="color:#1C1A17">Se viene algo nuevo</div>
  <h1>Activá el <em>recordatorio.</em></h1>{hole(240, w=700)}</div>''')

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
.z{{position:relative;z-index:1}} .n .z h1 em{{color:#E3C276}} .st > .z:not(.mid){{display:flex;flex-direction:column}}
.list2{{margin-top:60px;display:flex;flex-direction:column;gap:30px}} .it2{{display:flex;gap:34px;align-items:center}}
.it2 b{{display:block;font-family:B;font-weight:500;font-size:58px;line-height:1.1}} .it2 span{{font-size:34px;color:var(--sub);font-weight:300}}
.stk{{background:#C9A34E;color:#1C1A17;font-size:34px;font-weight:500;padding:18px 34px;border-radius:999px;box-shadow:0 20px 40px -20px rgba(0,0,0,.5)}}
.feat{{display:flex;flex-direction:column;gap:30px;padding-top:30px}} .feat div{{display:flex;gap:20px;align-items:center;font-size:40px}} .feat i{{width:32px;height:32px;color:var(--g);flex:none}}
.tl{{margin-top:60px;display:flex;flex-direction:column;gap:34px}} .tli{{display:flex;gap:36px;align-items:center}}
.n2{{font-family:B;font-style:italic;font-size:44px;color:var(--g)}} .tli b{{display:block;font-family:B;font-weight:500;font-size:58px;line-height:1.05}} .tli span{{font-size:34px;color:var(--sub);font-weight:300;line-height:1.3}}
.vals2{{display:flex;flex-direction:column;gap:44px;margin-top:20px}} .vals2 > div{{display:grid;grid-template-columns:330px 1fr;grid-template-rows:auto auto;column-gap:40px;align-items:end}}
.vals2 > div > div{{grid-row:span 2}} .vals2 b{{font-family:B;font-weight:500;font-size:76px;line-height:1;align-self:end}} .vals2 span{{font-size:38px;color:var(--sub);font-weight:300;align-self:start;margin-top:14px}}
.strip{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:60px}}
.glass{{background:rgba(250,246,238,.12);border:1px solid rgba(250,246,238,.3);border-radius:36px;padding:50px 60px}}
.vs2{{display:flex;flex-direction:column;gap:50px;margin-top:60px}} .vs2 b{{font-family:B;font-style:italic;font-size:76px;color:var(--g)}} .vs2 span{{font-size:36px;color:var(--sub)}}
.mini{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:10px 0}} .vs2 .pal{{height:70px;border-radius:16px;margin:12px 0}}
.sw{{display:grid;grid-template-columns:repeat(2,1fr);gap:24px;margin-top:70px}} .sw i{{display:block;height:280px;border-radius:28px;box-shadow:inset 0 0 0 3px rgba(28,26,23,.25)}} .sw span{{display:block;margin-top:12px;font-size:30px;letter-spacing:.12em;color:#3B3122}}
.brand{{display:grid;grid-template-columns:1.1fr 1fr;gap:20px;margin-top:60px}} .bc{{border-radius:28px;height:380px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px}}
.bp{{border-radius:28px;height:380px;padding:40px;box-sizing:border-box;display:flex;align-items:center}} .brand .pal{{grid-column:span 2;height:110px;margin:0}}
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
