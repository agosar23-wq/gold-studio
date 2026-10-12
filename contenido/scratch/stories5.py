exec(open('stories.py').read())     # css, SP, logo, st()
import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
import catalogo_wa2 as K, portada_wa4 as D
SCRP = '/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad'
extra = '''
.ph{border-radius:56px;background:#1C1A17;padding:14px;box-shadow:0 40px 70px -36px rgba(0,0,0,.6);flex:none}
.ph>div{border-radius:44px;overflow:hidden;background:#fff}
.n .ph{background:#4A433A}
.vis{display:flex;justify-content:center;margin-top:50px}
.cd{background:#FFFDF8;border-radius:26px;padding:28px 40px;font-size:42px}
.n .cd{background:#26221D}
.stack{display:flex;flex-direction:column;gap:22px;margin-top:50px}
.num{font-family:B;font-style:italic;font-size:90px;color:var(--em);line-height:1}
'''
img = lambda p, w, h: K.phone(f'<img src="file://{p}" style="width:100%;display:block">', w, h)
deskv = ('<div style="position:relative;width:880px;height:640px;border-radius:36px;overflow:hidden;background:linear-gradient(135deg,#F5EFE4,#EDE4D3)">'
         + D.ab(-30, 40, D.laptop, -6, 2) + D.ab(560, 30, D.note, 8, 2) + D.ab(600, 400, D.coffee, 0, 3) + D.ab(40, 470, D.swatches, 0, 3) + '</div>')
sketch = f'<div style="transform:scale(1.5);transform-origin:top center;height:640px">{D.note}</div>'
hole = lambda h=420: f'<div class="hole" style="height:{h}px">x</div>'
S = {}
# LUN 19
S['lun19-1-app-tia'] = st('n', f'<div class="top"><div class="eb">Nuevo reel</div><h1 style="font-size:96px">Hoy les cuento qué pasó cuando le hice una app <em>a mi tía</em></h1><div class="vis">{img(SCRP + "/appshots/p-inicio.png", 470, 900)}</div></div>')
S['lun19-2-reel'] = st('m', '<div class="top"><div class="eb">Ya está arriba</div><h1 style="font-size:110px">El reel <em>completo</em></h1></div><div class="hole tall">x</div>')
S['lun19-3-encuesta'] = st('g', '<div class="top"><div class="eb">Contame</div><h1 style="font-size:116px">¿Te gustaría una app para <em>tu negocio?</em></h1></div>' + hole())
# MAR 20
S['mar20-1-apps'] = st('m', f'<div class="top"><div class="eb">Nuevo carrusel</div><h1 style="font-size:104px">Las apps que uso <em>todos los días</em></h1><div class="vis">{deskv}</div></div>')
S['mar20-2-quiz'] = st('n', '<div class="top"><div class="eb">Quiz</div><h1 style="font-size:120px">¿Cuál usás <em>más?</em></h1><p class="lead">Canva, CapCut, Notion o Pinterest</p></div>' + hole(560))
S['mar20-3-carrusel'] = st('m', '<div class="top"><div class="eb">Guardalo</div><h1 style="font-size:110px">5 apps gratis para <em>tu marca</em></h1></div><div class="hole tall">x</div>')
# MIÉ 21
S['mie21-1-preguntas'] = st('g', '<div class="top"><div class="eb">Caja de preguntas</div><h1 style="font-size:108px">¿A qué te dedicás? Te digo qué le sumaría <em>a tu marca</em></h1></div>' + hole())
S['mie21-2-reel'] = st('m', '<div class="top"><div class="eb">Nuevo reel</div><h1 style="font-size:100px">Si sos nutri, psicóloga o entrenadora, <em>esto es para vos</em></h1></div><div class="hole tall">x</div>')
S['mie21-3-respuesta'] = st('n', '<div class="top"><div class="eb">Me preguntaron</div></div>' + hole(380) + '<div class="cd" style="margin-top:40px"><div class="eb" style="margin-bottom:14px">Mi respuesta</div><div style="height:200px"></div></div>')
# JUE 22
S['jue22-1-web'] = st('m', f'<div class="top"><div class="eb">Mirá</div><h1 style="font-size:104px">Así se ve mi página <em>por dentro</em></h1><div class="vis">{img(SCRP + "/webshots/inicio.png", 470, 900)}</div></div>')
S['jue22-2-encuesta'] = st('n', '<div class="top"><div class="eb">Encuesta</div><h1 style="font-size:124px">¿Tenés <em>página web?</em></h1><p class="lead">Sí, no o uso Linktree</p></div>' + hole(560))
S['jue22-3-carrusel'] = st('m', '<div class="top"><div class="eb">Nuevo carrusel</div><h1 style="font-size:110px">¿Página web <em>o Linktree?</em></h1></div><div class="hole tall">x</div>')
# VIE 23
S['vie23-1-boceto'] = st('m', f'<div class="top"><div class="eb">Detrás de escena</div><h1 style="font-size:116px">Todo logo empieza <em>así</em></h1><div class="vis">{sketch}</div></div>')
S['vie23-2-slider'] = st('g', '<div class="top"><div class="eb">Del 1 al 10</div><h1 style="font-size:112px">¿Cuánto te gusta ver <em>procesos de diseño?</em></h1></div>' + hole(300))
S['vie23-3-reel'] = st('n', '<div class="top"><div class="eb">Nuevo reel</div><h1 style="font-size:112px">POV: el logo <em>final</em></h1></div><div class="hole tall">x</div>')
# SÁB 24
S['sab24-1-agenda'] = st('n', f'<div class="top"><div class="eb">Novedades</div><h1 style="font-size:112px">Abro agenda para <em>noviembre</em></h1><div class="vis">{deskv}</div></div>')
S['sab24-2-pocos'] = st('m', '<div class="top"><div class="eb">Cómo trabajo</div><h1 style="font-size:96px">Tomo pocos proyectos por mes para dedicarle <em>tiempo a cada uno</em></h1><div class="stack">'
                        + ''.join(f'<div class="cd">{t}</div>' for t in ['Páginas web', 'Branding y logos', 'Community manager']) + '</div></div>')
S['sab24-3-catalogo'] = st('g', '<div class="top"><div class="eb">Precio de lanzamiento</div><h1 style="font-size:112px">Mirá los paquetes en mi <em>catálogo</em></h1></div>' + hole(360))
# DOM 25
LOGOW = logo.replace('class="logo"', 'class="logo" style="color:#FAF6EE"')
S['dom25-1-semana'] = st('n', '<div class="mid"><div style="width:600px">' + LOGOW + '</div><div class="eb" style="margin-top:80px">Domingo</div><h1 style="font-size:124px">Así fue <em>mi semana</em></h1></div>')
S['dom25-2-aprendi'] = st('m', '<div class="top"><div class="eb">Lo que aprendí esta semana</div><div class="stack">' + ''.join(
    f'<div style="display:flex;gap:34px;align-items:flex-start"><span class="num">{i}</span><p class="lead" style="margin:6px 0 0;color:#1C1A17;font-size:50px">{t}</p></div>'
    for i, t in [(1, 'Mostrar el proceso conecta más que mostrar el resultado.'), (2, 'Sus preguntas me dan las mejores ideas.'), (3, 'Ir de a poco también es avanzar.')]) + '</div></div>')
S['dom25-3-que-ver'] = st('g', '<div class="top"><div class="eb">La semana que viene</div><h1 style="font-size:116px">¿Qué te gustaría <em>ver por acá?</em></h1></div>' + hole())
page = '<!doctype html><meta charset="utf-8"><style>' + css + extra + '</style>' + ''.join(f'<div id="{k}">{v}</div>' for k, v in S.items())
open('stories5.html', 'w').write(page)
print(len(S))
