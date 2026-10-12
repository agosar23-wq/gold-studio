exec(open('stories.py').read())     # css, SP, logo, st()
FS = F
extra = f'''
@font-face{{font-family:XArchivo;src:url({FS}archivo-black/files/archivo-black-latin-400-normal.woff2)}}
@font-face{{font-family:XPlayfair;src:url({FS}playfair-display/files/playfair-display-latin-700-normal.woff2)}}
@font-face{{font-family:XNoto;src:url({FS}noto-serif/files/noto-serif-latin-900-normal.woff2)}}
@font-face{{font-family:XFam;src:url({FS}familjen-grotesk/files/familjen-grotesk-latin-700-normal.woff2)}}
.ab{{display:flex;gap:30px;margin-top:70px}}
.opt{{flex:1;display:flex;flex-direction:column;gap:18px;align-items:center}}
.tag{{font-family:B;font-size:72px;line-height:1;color:var(--em)}}
.pal{{width:100%;height:400px;border-radius:30px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 30px 60px -30px rgba(0,0,0,.5)}}
.pal i{{flex:1;display:block}}
.lg{{width:100%;height:440px;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;box-shadow:0 30px 60px -30px rgba(0,0,0,.5)}}
.cd{{background:#FFFDF8;border-radius:30px;padding:44px 48px;display:flex;flex-direction:column;gap:12px}}
.n .cd{{background:#26221D}}
.cd h3{{font-family:B;font-weight:500;font-size:56px;margin:0;color:var(--em)}}
.cd p{{font-size:40px;margin:0;line-height:1.35;color:var(--sub);font-weight:300}}
.stack{{display:flex;flex-direction:column;gap:26px;margin-top:60px}}
.fonts{{display:flex;flex-direction:column;gap:10px;font-size:120px;line-height:1.05;margin-top:60px}}
.no{{display:inline-block;align-self:flex-start;background:#C0392B;color:#fff;font-size:30px;font-weight:500;padding:8px 22px;border-radius:999px;margin-bottom:30px;letter-spacing:.08em}}
.si{{display:inline-block;align-self:flex-start;background:#1C1A17;color:#FAF6EE;font-size:30px;font-weight:500;padding:8px 22px;border-radius:999px;margin-bottom:30px;letter-spacing:.08em}}
.num{{font-family:B;font-style:italic;font-size:90px;color:var(--em);line-height:1}}
'''
CUP = '<svg width="100%" height="100%" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M29 60 L71 60 L64 90 L36 90 Z"/><path d="M43 62 L45 88 M50 62 L50 88 M57 62 L55 88"/><path d="M24 60 C18 52 26 44 33 47 C32 37 44 31 50 38 C56 31 68 37 67 47 C74 44 82 52 76 60 Z"/><circle cx="50" cy="27" r="6" fill="currentColor"/><path d="M51 21 C53 15 57 12 62 11"/></svg>'
S = {}
# ---- SÁB 10 · preguntas ----
S['sab10-1-preguntame'] = st('m', '''<div class="top"><div class="eb">Conoceme un poco más</div>
 <h1 style="font-size:116px">Preguntame <em>lo que quieras</em></h1><p class="lead">Sobre mí, sobre diseño o sobre Gold Studio. Respondo todo mañana.</p></div><div class="hole">x</div>''')
# ---- DOM 11 · respuestas ----
S['dom11-1-respondo'] = st('g', f'''<div class="mid"><div class="spk big">{SP}</div><div class="eb">Domingo de respuestas</div>
 <h1 style="font-size:124px">Respondo <em>sus preguntas</em></h1><p class="lead">Seguí pasando</p></div>''')
# ---- LUN 12 · ¿cuál elegís? ----
S['lun12-1-juguemos'] = 'PLACEHOLDER'
pa = '<div class="pal">'+''.join(f'<i style="background:{c}"></i>' for c in ['#E8B4B8','#FFF6F4','#4A2329'])+'</div>'
pb = '<div class="pal">'+''.join(f'<i style="background:{c}"></i>' for c in ['#C9A34E','#FAF6EE','#5E7D5B'])+'</div>'
PALS = [('A','#E8B4B8','#FFF6F4','#4A2329'),('B','#C9A34E','#FAF6EE','#5E7D5B'),('C','#C7B6E0','#CDE8DA','#3F3A5A'),('D','#C96F4A','#F5E9DA','#5A3A2A')]
grid = ''.join(f'<div class="opt" style="flex-direction:row;gap:22px"><span class="tag" style="color:#C9A34E;width:56px">{t}</span><div class="pal" style="height:250px;flex-direction:row">'+''.join(f'<i style="background:{c}"></i>' for c in cs)+'</div></div>' for t,*cs in PALS)
S['lun12-1-juguemos'] = st('n', '<div class="top"><div class="eb">Juguemos</div><h1 style="font-size:100px">Si tuvieras que armar la marca de una <em>pastelería</em>…</h1><p class="lead" style="margin-top:24px">¿Qué colores elegirías?</p>'
  + f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px 34px;margin-top:50px">{grid}</div></div><div class="hole" style="height:300px">x</div>')
S['lun12-2-paleta'] = st('m', f'''<div class="top"><div class="eb">Ronda 1 · Colores</div><h1 style="font-size:104px">¿Qué paleta <em>elegís?</em></h1></div>
 <div class="ab"><div class="opt"><span class="tag">A</span>{pa}<p class="lead" style="margin:0;font-size:36px">Rosa y chocolate</p></div>
 <div class="opt"><span class="tag">B</span>{pb}<p class="lead" style="margin:0;font-size:36px">Dorado y verde</p></div></div><div class="hole" style="height:300px">x</div>''')
la = f'<div class="lg" style="background:#E8B4B8;color:#4A2329">{CUP}<span style="font-family:B;font-size:84px;line-height:1">Dulce Mía</span><span style="font-size:22px;letter-spacing:.3em">PASTELERÍA</span></div>'
lb = f'<div class="lg" style="background:#4A2329;color:#FFF6F4"><span style="font-family:J;font-weight:500;font-size:60px;letter-spacing:.2em">DULCE MÍA</span><span style="font-family:B;font-style:italic;font-size:40px;color:#E8B4B8">pastelería</span></div>'
S['lun12-3-logo'] = st('m', f'''<div class="top"><div class="eb">Ronda 2 · Logo</div><h1 style="font-size:104px">¿Y qué <em>logo?</em></h1></div>
 <div class="ab"><div class="opt"><span class="tag">A</span>{la}<p class="lead" style="margin:0;font-size:36px">Clásico, con dibujo</p></div>
 <div class="opt"><span class="tag">B</span>{lb}<p class="lead" style="margin:0;font-size:36px">Moderno, solo letras</p></div></div><div class="hole" style="height:300px">x</div>''')
import sys; sys.path.insert(0,'/home/user/gold-studio-contenido')
import pack
BOXES = [('A', pack.box(400, pack.PINK, pack.CHOC), 'Rosa y chocolate'),
         ('B', pack.box(400, pack.CHOC, pack.CREAM, lid=pack.PINK), 'Chocolate y rosa'),
         ('C', pack.box(400, pack.CREAM, pack.CHOC, lid=pack.GOLD), 'Crema y dorado')]
S['lun12-4-packaging'] = st('m', '<div class="top"><div class="eb">Ronda 3 · Packaging</div><h1 style="font-size:100px">¿En qué caja te <em>la llevarías?</em></h1><div class="stack" style="gap:44px;margin-top:56px">'
  + ''.join(f'<div style="display:flex;align-items:center;gap:40px"><span class="tag" style="width:60px">{t}</span>{b}<p class="lead" style="margin:0;font-size:36px">{l}</p></div>' for t,b,l in BOXES)
  + '</div></div><div class="hole" style="height:260px">x</div>')
# ---- MAR 13 · resultados ----
S['mar13-1-eligieron'] = st('g', '''<div class="top"><div class="eb">Los resultados</div><h1 style="font-size:124px">Ustedes eligieron <em>esto:</em></h1></div><div class="hole tall">x</div>''')
S['mar13-2-que-significa'] = st('n', f'''<div class="mid"><div class="spk big">{SP}</div><div class="eb">Hoy a las 18 h</div>
 <h1 style="font-size:112px">Les cuento qué transmite <em>cada color</em></h1><p class="lead">Y por qué elegirlo bien cambia toda tu marca.</p></div>''')
S['mar13-3-nuevo-posteo'] = st('m', '''<div class="top"><div class="eb">Nuevo posteo</div><h1 style="font-size:112px">Qué transmite <em>cada color</em> en tu marca</h1></div><div class="hole tall">x</div>''')
# ---- MIÉ 14 · tip tipografías ----
S['mie14-1-error'] = st('n', f'''<div class="mid"><div class="spk">{SP}</div><div class="eb">Un error que veo mucho</div>
 <h1 style="font-size:124px">Usar <em>demasiadas</em> tipografías</h1></div>''')
S['mie14-2-asi-no'] = st('m', '''<div class="top"><span class="no">ASÍ NO</span><h1 style="font-size:96px">Cinco letras distintas en una marca</h1>
 <div class="fonts"><span style="font-family:XArchivo">Marca</span><span style="font-family:XPlayfair">Marca</span><span style="font-family:XNoto">Marca</span><span style="font-family:XFam">Marca</span><span style="font-family:J">Marca</span></div>
 <p class="lead">Tu cerebro no sabe qué mirar, y la marca parece improvisada.</p></div>''')
S['mie14-3-asi-si'] = st('m', '''<div class="top"><span class="si">ASÍ SÍ</span><h1 style="font-size:96px">Dos tipografías <em>y listo</em></h1>
 <div class="stack"><div class="cd"><p style="font-size:28px;letter-spacing:.2em;text-transform:uppercase;color:#8A6A22;font-weight:500">Para títulos</p><span style="font-family:B;font-size:100px;line-height:1.05">Gold Studio</span></div>
 <div class="cd"><p style="font-size:28px;letter-spacing:.2em;text-transform:uppercase;color:#8A6A22;font-weight:500">Para textos</p><span style="font-family:J;font-size:46px;line-height:1.35;color:#4E473D">Una simple y fácil de leer, para todo lo demás.</span></div></div>
 <p class="lead">¿Te pasaba? Contame abajo.</p></div><div class="hole" style="height:200px">x</div>''')
# ---- JUE 15 · equipo ----
S['jue15-1-como-nos-dividimos'] = st('n', '''<div class="top"><div class="eb">El equipo</div><h1 style="font-size:104px">Cómo nos dividimos en <em>Gold Studio</em></h1>
 <div class="stack"><div class="cd"><h3>Agos</h3><p>Páginas web, apps y redes</p></div>
 <div class="cd"><h3>Angie</h3><p>Diseño gráfico</p></div>
 <div class="cd" style="background:#C9A34E"><h3 style="color:#1C1A17">Juntas</h3><p style="color:#3B3122">Branding, ideas y cada detalle</p></div></div></div>''')
S['jue15-2-mejor-amiga'] = st('g', '''<div class="top"><div class="eb">Pregunta seria</div><h1 style="font-size:120px">¿Trabajarías con <em>tu mejor amiga?</em></h1></div><div class="hole">x</div>''')
# ---- VIE 16 · venta suave ----
S['vie16-1-senal'] = st('n', f'''<div class="mid"><div class="spk big">{SP}</div>
 <h1 style="font-size:124px">Si estabas esperando <em>una señal</em></h1><p class="lead">para arrancar tu marca...</p></div>''')
S['vie16-2-lugares'] = st('m', '''<div class="top"><div class="eb">Precio de lanzamiento</div><h1 style="font-size:112px">Este mes tomo <em>pocos proyectos</em></h1>
 <div class="stack" style="gap:18px">'''+''.join(f'<div class="cd" style="padding:30px 44px"><p style="font-size:44px;color:#1C1A17;font-weight:400">{t}</p></div>' for t in ['Páginas web','Branding y logos','Community manager'])+'''</div>
 <p class="lead">Escribime y te cuento cómo arrancamos.</p></div><div class="hole" style="height:220px">x</div>''')
# ---- DOM 18 · resumen ----
S['dom18-1-primera-semana'] = st('n', f'''<div class="mid"><div style="width:620px">{logo.replace('class="logo"','class="logo" style="color:#FAF6EE"')}</div>
 <div class="eb" style="margin-top:80px">Primera semana</div><h1 style="font-size:120px"><em>Gracias</em> por estar</h1>
 <p class="lead">Cada mensaje, cada voto y cada compartido me ayudó un montón.</p></div>''')
S['dom18-2-aprendi'] = st('m', '''<div class="top"><div class="eb">Lo que aprendí esta semana</div>
 <div class="stack">'''+''.join(f'<div style="display:flex;gap:34px;align-items:flex-start"><span class="num">{i}</span><p class="lead" style="margin:6px 0 0;color:#1C1A17;font-size:50px">{t}</p></div>' for i,t in [(1,'Empezar es más importante que tenerlo todo perfecto.'),(2,'Mostrarme conecta más de lo que pensaba.'),(3,'Con buena compañía todo es más lindo.')])+'''</div></div>''')
S['dom18-3-que-ver'] = st('g', '''<div class="top"><div class="eb">La semana que viene</div><h1 style="font-size:116px">¿Qué te gustaría <em>ver por acá?</em></h1></div><div class="hole">x</div>''')
page = '<!doctype html><meta charset="utf-8"><style>'+css+extra+'</style>'+''.join(f'<div id="{k}">{v}</div>' for k,v in S.items())
open('stories4.html','w').write(page)
print(len(S))
