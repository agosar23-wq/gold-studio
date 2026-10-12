import re
F = 'file:///tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad/logo/node_modules/@fontsource/'
logo = open('/home/user/gold-studio-final/logo-gold-studio-transparente.svg').read()
logo = re.sub(r'<svg [^>]*viewBox="([^"]+)"[^>]*>', r'<svg class="logo" viewBox="\1">', logo, count=1)
logo = logo.replace('fill="#1C1A17"', 'fill="currentColor"').replace('fill="#B8923A"', 'style="fill:var(--g)"').replace('stroke="#B8923A"', 'style="stroke:var(--g)"')
SP = '<svg class="sp" viewBox="0 0 100 100"><path d="M50 0 C54.5 40 60 45.5 100 50 C60 54.5 54.5 60 50 100 C45.5 60 40 54.5 0 50 C40 45.5 45.5 40 50 0Z" fill="currentColor"/></svg>'
IMG = 'file:///home/user/gold-studio-web/img/'
def foot(n, tot, swipe=True):
    r = f'<span>{n}/{tot}</span>' if tot > 1 else ''
    s = '<span class="sw">Deslizá →</span>' if (swipe and n < tot) else r
    return f'<div class="foot"><span>@goldstudio.ba</span>{s}</div>'
def ring(size, stroke, cls=''):
    return f'<div class="ring {cls}" style="width:{size}px;height:{size}px;border-width:{stroke}px"></div>'

slides = {}
# ---------- POST 1: presentación ----------
slides['1-presentacion-1'] = ('m', f'''
  <div class="center col" style="gap:70px;margin-top:40px">
    <div style="width:640px;color:var(--ink)">{logo}</div>
    <div class="col center" style="gap:26px">
      <div class="eb">Estudio de diseño digital</div>
      <h1 style="font-size:96px;text-align:center">Tu marca, con<br><em>brillo propio.</em></h1>
    </div>
  </div>{foot(1,3)}''')
slides['1-presentacion-2'] = ('n', f'''
  <div class="eb" style="margin-top:40px">Qué hago</div>
  <h1 style="font-size:80px;margin:26px 0 60px">Todo para que tu marca <em>brille online.</em></h1>
  <ul class="big">
    <li>{SP}Páginas web</li><li>{SP}Apps a medida</li><li>{SP}Tiendas online</li><li>{SP}Branding y logos</li><li>{SP}Community manager</li>
  </ul>{foot(2,3)}''')
slides['1-presentacion-3'] = ('g', f'''
  <div style="position:absolute;right:-120px;top:-120px">{ring(560,70,'light')}</div>
  <div style="flex:1"></div>
  <h1 style="font-size:104px">¿Arrancamos<br><em>tu proyecto?</em></h1>
  <p class="lead" style="margin:40px 0 50px;max-width:820px">Los primeros proyectos tienen precio especial de lanzamiento ✦</p>
  <div class="pill">Escribime por DM o entrá al link de la bio</div>
  <div style="flex:.35"></div>{foot(3,3)}''')

# ---------- POST 2: trabajo app nutrición ----------
slides['2-trabajo-1'] = ('n', f'''
  <div class="eb" style="margin-top:40px">Trabajo destacado</div>
  <h1 style="font-size:88px;margin-top:26px;max-width:700px">Una app a medida para un consultorio de <em>nutrición</em></h1>
  <div class="phone" style="position:absolute;right:100px;top:500px;width:340px;transform:rotate(-6deg)"><img src="{IMG}paciente.jpg"></div>
  <div style="position:absolute;left:90px;bottom:150px;display:flex;gap:14px;flex-direction:column">
    <span class="chip">Compu y celular</span><span class="chip">Diseño a medida</span><span class="chip">Cuentas privadas</span></div>
  {foot(1,4)}''')
slides['2-trabajo-2'] = ('a', f'''
  <div class="eb" style="margin-top:40px">Para la nutricionista</div>
  <h1 style="font-size:76px;margin:24px 0 60px">Pacientes, turnos y mensajes<br><em>en un solo lugar.</em></h1>
  <div class="browser"><div class="bar"><i></i><i></i><i></i></div><img src="{IMG}nutri.jpg"></div>
  <p class="lead" style="margin-top:46px">Aprueba a cada paciente nuevo, sube planes y recetarios, y responde consultas.</p>
  {foot(2,4)}''')
slides['2-trabajo-3'] = ('m', f'''
  <div style="display:flex;gap:70px;align-items:center;flex:1;margin-top:20px">
    <div class="phone" style="width:400px;flex:none"><img src="{IMG}paciente.jpg"></div>
    <div class="col" style="gap:26px">
      <div class="eb">Para cada paciente</div>
      <h1 style="font-size:66px">Su propia cuenta, <em>siempre a mano.</em></h1>
      <ul class="feats"><li>{SP}Plan alimentario</li><li>{SP}Recetarios</li><li>{SP}Su progreso de peso</li><li>{SP}Próximos turnos</li><li>{SP}Mensajes directos</li></ul>
    </div>
  </div>{foot(3,4)}''')
slides['2-trabajo-4'] = ('g', f'''
  <div style="position:absolute;left:-160px;bottom:-160px">{ring(600,74,'light')}</div>
  <div style="flex:1"></div>
  <h1 style="font-size:100px;text-align:right">¿Querés una<br>para <em>tu negocio?</em></h1>
  <p class="lead" style="margin:40px 0 50px;text-align:right;margin-left:auto;max-width:760px">Turnos, clientes, archivos o ventas: la armo a tu medida.</p>
  <div class="pill" style="align-self:flex-end">Probá la demo · link en la bio</div>
  <div style="flex:.35"></div>{foot(4,4)}''')

# ---------- POST 3: paquetes ----------
slides['3-paquetes-1'] = ('g', f'''
  <div style="position:absolute;right:120px;top:150px">{ring(300,40,'light')}</div>
  <div style="position:absolute;right:70px;top:110px;width:110px;color:var(--bg)">{SP}</div>
  <div style="flex:1"></div>
  <div class="eb" style="color:var(--bg)">Paquetes</div>
  <h1 style="font-size:116px;margin:24px 0 40px">Elegí por dónde <em>empezar.</em></h1>
  <p class="lead" style="max-width:800px">Página web, branding o community manager. Cada uno, pensado para tu marca.</p>
  <div style="flex:.3"></div>{foot(1,4)}''')
def pack(name, n, scheme, desc, items, icon):
    li = ''.join(f'<li>{SP}{i}</li>' for i in items)
    return (scheme, f'''
  <div class="eb" style="margin-top:40px">Paquete {n-1} de 3</div>
  <div class="ico">{icon}</div>
  <h1 style="font-size:104px">{name}</h1>
  <p class="lead" style="margin:24px 0 46px;max-width:820px">{desc}</p>
  <ul class="feats lg">{li}</ul>
  <div style="flex:1"></div>
  <div class="note">{SP}<span>Precio especial de lanzamiento · Consultá por DM</span></div>
  {foot(n,4)}''')
I_WEB = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2.5"/><path d="M3 9h18M7 6.5h.01M10 6.5h.01"/></svg>'
I_BR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="10" cy="13" r="6"/><path d="M17.5 3.5c.4 2 .6 2.2 2.5 2.5-1.9.3-2.1.5-2.5 2.5-.4-2-.6-2.2-2.5-2.5 1.9-.3 2.1-.5 2.5-2.5z"/></svg>'
I_CM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M16.8 7.2h.01"/></svg>'
slides['3-paquetes-2'] = pack('Página web', 2, 'm', 'Para que tus clientes te encuentren, vean lo que hacés y te escriban.', ['Diseño a medida con tu estilo','Tus servicios, trabajos y contacto','Botón directo a WhatsApp','Perfecta en el celular','La publico por vos'], I_WEB)
slides['3-paquetes-3'] = pack('Branding', 3, 'n', 'Para que tu marca se reconozca y se vea igual de linda en todos lados.', ['Logo y sus variantes','Paleta de colores y tipografías','Foto de perfil para redes','Portadas para tus destacadas','Archivos listos para usar'], I_BR)
slides['3-paquetes-4'] = pack('Community<br>manager', 4, 'm', 'Para que tu Instagram tenga una estética linda y constante.', ['Plan de contenido mensual','Diseño de posteos e historias','Textos para cada publicación','Feed y destacadas ordenados','Resumen de cómo le fue a tu cuenta'], I_CM)

css = f'''
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2);font-weight:500;font-style:italic}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-300-normal.woff2);font-weight:300}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-500-normal.woff2);font-weight:500}}
body{{margin:0;background:#888}}
.s{{width:1080px;height:1350px;box-sizing:border-box;padding:90px;position:relative;overflow:hidden;display:flex;flex-direction:column;font-family:J;margin-bottom:20px}}
.m{{--bg:#FAF6EE;--ink:#1C1A17;--ink2:#5A5348;--g:#B8923A;--gi:#8A6A22;--line:#E9DFC8;background:var(--bg);color:var(--ink)}}
.a{{--bg:#F1E8D6;--ink:#1C1A17;--ink2:#5A5348;--g:#B8923A;--gi:#8A6A22;--line:#E2D5BA;background:var(--bg);color:var(--ink)}}
.n{{--bg:#1C1A17;--ink:#FAF6EE;--ink2:#BDB3A2;--g:#C9A34E;--gi:#C9A34E;--line:#3A342B;background:var(--bg);color:var(--ink)}}
.g{{--bg:#FAF6EE;--ink:#1C1A17;--ink2:#3B3122;--g:#FAF6EE;--gi:#FAF6EE;--line:#B8923A;background:#C9A34E;color:var(--ink)}}
.g h1 em{{color:#FAF6EE}}
h1{{font-family:B;font-weight:500;line-height:1.04;margin:0;letter-spacing:-.01em}}
h1 em{{font-style:italic;color:var(--gi)}}
.eb{{font-size:24px;letter-spacing:.34em;text-transform:uppercase;color:var(--gi);font-weight:500}}
.lead{{font-size:38px;line-height:1.4;color:var(--ink2);font-weight:300;margin:0}}
.col{{display:flex;flex-direction:column}} .center{{align-items:center;justify-content:center;flex:1}}
.logo{{width:100%;height:auto;display:block}}
.foot{{position:absolute;left:90px;right:90px;bottom:56px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.12em;color:var(--ink2)}}
.sw{{color:var(--gi);font-weight:500}}
.sp{{width:100%;height:100%}}
ul{{list-style:none;margin:0;padding:0}}
ul.big{{display:flex;flex-direction:column}}
ul.big li{{font-family:B;font-size:62px;display:flex;align-items:center;gap:30px;padding:20px 0;border-top:1px solid var(--line)}}
ul.big li:last-child{{border-bottom:1px solid var(--line)}}
ul.big li .sp,ul.feats li .sp{{width:34px;height:34px;flex:none;color:var(--g)}}
ul.feats{{display:flex;flex-direction:column;gap:22px;font-size:36px}}
ul.feats li{{display:flex;align-items:center;gap:22px}}
ul.feats.lg{{gap:26px;font-size:40px}}
ul.feats li .sp{{width:26px;height:26px}}
.ring{{border-radius:50%;border-style:solid;border-color:#B8923A;box-sizing:border-box}}
.ring.light{{border-color:#FAF6EE}}
.pill{{align-self:flex-start;background:#1C1A17;color:#FAF6EE;font-size:30px;padding:24px 40px;border-radius:999px;letter-spacing:.03em}}
.chip{{align-self:flex-start;font-size:28px;padding:14px 28px;border-radius:999px;border:1.5px solid var(--line);color:var(--ink)}}
.phone{{border-radius:58px;padding:14px;background:#0E0D0B;box-shadow:0 40px 80px -30px rgba(0,0,0,.6),0 0 0 2px #3A342B}}
.phone img{{width:100%;display:block;border-radius:46px}}
.browser{{border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 40px 80px -40px rgba(28,26,23,.45);border:1.5px solid var(--line)}}
.browser .bar{{display:flex;gap:10px;padding:16px 20px;background:#F3ECDD;border-bottom:1.5px solid var(--line)}}
.browser .bar i{{width:14px;height:14px;border-radius:50%;background:#E0D3B8}}
.browser img{{width:100%;display:block}}
.ico{{flex:none;width:110px;height:110px;border-radius:50%;display:grid;place-items:center;background:color-mix(in srgb,var(--g) 18%,transparent);color:var(--gi);margin:44px 0 28px}}
.ico svg{{width:56px;height:56px}}
.note{{display:flex;align-items:center;gap:18px;font-size:28px;color:var(--ink2);padding:26px 0 70px;border-top:1px solid var(--line)}}
.note .sp{{width:30px;height:30px;color:var(--g)}}
'''
html = '<!doctype html><meta charset="utf-8"><style>' + css + '</style>' + ''.join(f'<div class="s {sc}" id="s{k}">{b}</div>' for k, (sc, b) in slides.items())
open('posts.html', 'w').write(html)
print(len(slides))
