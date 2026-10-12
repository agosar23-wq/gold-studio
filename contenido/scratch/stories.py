import re, html as H
exec(open('posts.py').read().split("slides = {}")[0])   # F, logo, SP
C = 'file:///home/user/gold-studio-final/carruseles/caso-real-branding-consultorio/01.png'
SAFE = ''  # zonas: arriba 250px y abajo 340px quedan libres para la interfaz de Instagram
def st(cls, inner): return f'<div class="st {cls}">{inner}</div>'
S = {}
# ---------- secuencia de lanzamiento (hoy) ----------
S['hoy-1-arranca'] = st('n', f'''<div class="mid"><div class="spk big">{SP}</div>
  <div class="eb">Hoy arranca algo nuevo</div><h1>Algo que soñé <em>mucho tiempo</em>…</h1></div>''')
S['hoy-2-presento'] = st('m', f'''<div class="mid"><div class="eb">Les presento</div><div style="width:760px;color:#1C1A17">{logo}</div>
  <p class="lead">Mi estudio de diseño digital ✦</p></div>''')
S['hoy-3-que-hago'] = st('m', f'''<div class="mid left"><div class="eb">Qué hago</div><h1 style="font-size:104px">Ayudo a que tu marca <em>brille</em></h1>
  <ul>{''.join(f'<li><i>{SP}</i>{t}</li>' for t in ['Páginas web','Apps a medida','Tiendas online','Branding y logos','Community manager'])}</ul></div>''')
S['hoy-4-encuesta'] = st('g', f'''<div class="top"><div class="eb">Ayudame a elegir</div><h1 style="font-size:104px">¿Qué te gustaría ver <em>por acá?</em></h1>
  <p class="lead">Votá abajo 👇</p></div><div class="hole">Poné acá la encuesta</div>''')
S['hoy-5-nuevo-posteo'] = st('n', f'''<div class="top"><div class="eb">Nuevo posteo ✦</div><h1 style="font-size:96px">Mi primer <em>caso real</em></h1></div>
  <div class="card"><img src="{C}"></div><p class="lead foot2">Tocá para verlo 👆</p>''')
S['hoy-6-escribime'] = st('m', f'''<div class="mid"><div class="spk">{SP}</div><h1 style="font-size:110px">¿Tenés una idea? <em>Escribime</em></h1>
  <p class="lead">Los primeros proyectos tienen precio especial de lanzamiento 💛</p><div class="hole small">Poné acá el link</div></div>''')
# ---------- plantillas para reusar ----------
S['plantilla-nuevo-posteo'] = st('n', f'''<div class="top"><div class="eb">Nuevo posteo ✦</div><h1 style="font-size:110px">No te lo <em>pierdas</em></h1></div>
  <div class="hole tall">Poné acá el posteo compartido</div>''')
S['plantilla-pregunta'] = st('m', f'''<div class="top"><div class="eb">Preguntame lo que quieras</div><h1 style="font-size:110px">¿Dudas sobre <em>tu marca?</em></h1></div>
  <div class="hole">Poné acá la cajita de preguntas</div>''')
S['plantilla-respuesta'] = st('g', f'''<div class="top"><div class="eb">Me preguntaron</div></div><div class="hole">Poné acá la pregunta que te hicieron</div>
  <div class="ans"><div class="eb" style="color:#1C1A17">Mi respuesta</div><div style="height:160px"></div></div>''')
S['plantilla-detras-de-escena'] = st('m', f'''<div class="top"><div class="eb">Detrás de escena</div><h1 style="font-size:104px">Hoy estoy <em>trabajando en…</em></h1></div>
  <div class="hole tall">Poné acá una captura de lo que estás diseñando</div>''')
S['plantilla-lanzamiento'] = st('n', f'''<div class="mid"><div class="spk">{SP}</div><div class="eb">Precio de lanzamiento</div>
  <h1 style="font-size:112px">Pocos lugares <em>este mes</em></h1><p class="lead">Escribime “ORO” por DM y te cuento 💛</p></div>''')

css = f'''
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2);font-weight:500;font-style:italic}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-300-normal.woff2);font-weight:300}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-500-normal.woff2);font-weight:500}}
body{{margin:0;background:#888}}
.st{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:J;margin-bottom:20px;box-sizing:border-box;padding:260px 100px 360px;display:flex;flex-direction:column}}
.m{{background:#FAF6EE;color:#1C1A17;--em:#8A6A22;--sub:#5E5649;--g:#B8923A}}
.n{{background:#1C1A17;color:#FAF6EE;--em:#C9A34E;--sub:#BDB2A0;--g:#C9A34E}}
.g{{background:#C9A34E;color:#1C1A17;--em:#FAF6EE;--sub:#3B3122;--g:#FAF6EE}}
h1{{font-family:B;font-weight:500;font-size:124px;line-height:1.05;margin:0;letter-spacing:-.01em}} h1 em{{font-style:italic;color:var(--em)}}
.eb{{font-size:30px;letter-spacing:.34em;text-transform:uppercase;color:var(--em);font-weight:500;margin-bottom:30px}}
.lead{{font-size:46px;line-height:1.35;color:var(--sub);font-weight:300;margin:40px 0 0}}
.mid{{flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}}
.mid.left{{align-items:flex-start;text-align:left}}
.top{{display:flex;flex-direction:column}}
.spk{{width:120px;height:120px;color:var(--g);margin-bottom:50px}} .spk.big{{width:200px;height:200px}}
.sp{{width:100%;height:100%;display:block}} .logo{{width:100%;height:auto;display:block}}
ul{{list-style:none;padding:0;margin:60px 0 0;display:flex;flex-direction:column;gap:30px}}
li{{font-family:B;font-size:70px;display:flex;align-items:center;gap:30px}} li i{{width:40px;height:40px;color:var(--g);display:block}}
.hole{{margin-top:auto;height:420px;color:transparent;font-size:1px}}
.hole.small{{height:200px;width:640px;margin-top:70px}} .hole.tall{{height:900px;margin-top:60px}}
.card{{margin:60px auto 0;width:680px;border-radius:30px;overflow:hidden;box-shadow:0 40px 80px -30px rgba(0,0,0,.7);transform:rotate(-2deg)}} .card img{{display:block;width:100%}}
.foot2{{text-align:center;margin-top:50px}}
.ans{{margin-top:50px;background:#FAF6EE;border-radius:36px;padding:50px}}
'''
page = '<!doctype html><meta charset="utf-8"><style>'+css+'</style>'+''.join(f'<div id="{k}">{v}</div>' for k,v in S.items())
open('stories.html','w').write(page)
print(len(S))
