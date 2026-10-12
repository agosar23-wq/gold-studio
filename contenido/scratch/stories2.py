exec(open('stories.py').read())          # reutiliza css, logo, SP, st()
S = {}
S['1-un-dia-de-vida'] = st('n', f'''<div class="mid"><div class="spk big">{SP}</div>
  <div class="eb">Dato curioso</div><h1 style="font-size:118px">Gold Studio tiene <em>un día de vida</em></h1>
  <p class="lead">Literal. Se me ocurrió ayer</p></div>''')
S['2-y-ya-tiene-reel'] = st('m', f'''<div class="top"><div class="eb">Y ya tiene</div><h1 style="font-size:110px">su propio <em>reel de presentación</em></h1>
  <p class="lead">Tocalo para verlo</p></div><div class="hole tall">reel</div>''')
S['3-encuesta'] = st('g', f'''<div class="top"><div class="eb">Sincerémonos</div><h1 style="font-size:110px">¿Ya conocías <em>Gold Studio?</em></h1></div>
  <div class="hole">encuesta</div>''')
S['4-compartilo'] = st('n', f'''<div class="mid"><div style="width:620px;color:#FAF6EE">{logo.replace('class="logo"','class="logo" style="color:#FAF6EE"')}</div>
  <h1 style="font-size:96px;margin-top:70px">Si te gustó, <em>compartilo</em></h1>
  <p class="lead">Mandáselo a esa amiga emprendedora.<br>Me ayuda un montón</p>
  <p class="lead" style="color:#C9A34E;font-weight:500;letter-spacing:.12em;margin-top:60px">@goldstudio.ba</p></div>''')
page = '<!doctype html><meta charset="utf-8"><style>'+css+'</style>'+''.join(f'<div id="{k}">{v}</div>' for k,v in S.items())
open('stories2.html','w').write(page)
S2 = {}
S2['juntas-desde-los-5'] = st('n', '''<div class="mid" style="gap:0">
  <h1 style="font-size:116px">Desde los 5 años <em>juntas</em></h1>
  <div style="margin-top:80px;width:880px;border-radius:34px;overflow:hidden;border:4px solid #C9A34E;box-shadow:0 40px 90px -40px rgba(0,0,0,.8)"><img src="file:///home/user/gold-studio-final/historias/mias-orig/chiquitas.jpg" style="display:block;width:100%"></div>
  <p class="lead" style="margin-top:80px;color:#FAF6EE">Angie y yo, toda la vida</p>
  <p class="lead" style="margin-top:6px;font-family:B;font-style:italic;font-size:64px;color:#C9A34E">y ahora, Gold Studio</p></div>''')
page = '<!doctype html><meta charset="utf-8"><style>'+css+'</style>'+''.join(f'<div id="{k}">{v}</div>' for k,v in {**S, **S2}.items())
open('stories2.html','w').write(page)
