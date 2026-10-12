import sys, html as H; sys.path.insert(0, '/home/user/gold-studio-contenido')
from caro_ejemplos import render, end
from carogen import CHECK, SP, emph
from mocks import site, browser, linktree, BRANDS

CROSS = '<svg class="ck x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
EXT = '''
.row3{display:flex;gap:24px;justify-content:center;align-items:flex-start}
.cap{font-size:26px;letter-spacing:.2em;text-transform:uppercase;color:var(--em);font-weight:500;text-align:center;margin-top:14px}
.sc{transform-origin:top left}
.list{display:flex;flex-direction:column;gap:18px;font-size:40px}
.list div{display:flex;align-items:center;gap:20px}
.list .ck{width:62px;height:62px;padding:13px;flex:none}
.ck.x{color:#C0392B;background:#C0392B22}
.split{display:flex;gap:44px;align-items:center}
.urlbar{display:flex;align-items:center;gap:20px;background:#fff;border-radius:999px;padding:24px 34px;font-size:40px;box-shadow:0 20px 40px -30px rgba(0,0,0,.4);color:#333}
.urlbar.bad{text-decoration:line-through;color:#999}
.icon{width:120px;height:120px;border-radius:30px;display:grid;place-items:center;font-family:B;font-size:56px;color:#FAF6EE}
.tiles{display:flex;gap:22px;justify-content:center}
.app{display:flex;align-items:center;gap:26px}
.app .icon{width:110px;height:110px;flex:none}
'''

def scaled(html, k, w, h):
    """Escala un bloque y reserva el espacio que ocupa."""
    return f'<div style="flex:none;width:{int(w*k)}px;height:{int(h*k)}px"><div class="sc" style="transform:scale({k});width:{w}px">{html}</div></div>'

# ================= DÍA 9 · cuánto cuesta =================
def template_site(w=820):
    inner = ('<div style="padding:18px 28px;background:#f4f4f4;font-size:22px;color:#999">Mi sitio</div>'
             '<div style="background:#ddd;padding:40px 28px;display:flex;flex-direction:column;gap:12px"><span style="font-size:34px;color:#888">Título de ejemplo</span>'
             '<span style="font-size:18px;color:#999">Escribí acá una descripción de tu negocio.</span><span style="align-self:flex-start;background:#aaa;color:#fff;padding:9px 20px;border-radius:6px;font-size:15px">Botón</span></div>'
             '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:20px 28px;background:#fff">' + '<div style="height:90px;background:#eee"></div>' * 3 + '</div>')
    return browser(inner, w, 'misitio.plantilla.com')

d9 = []
three = ''.join(f'<div>{scaled(site(k, lv), .38, 820, 520)}<div class="cap">{lab}</div></div>' for k, lv, lab in [('dulce', 1, 'Simple'), ('raiz', 2, 'Completa'), ('clara', 3, 'Con turnos')])
d9.append(('g', f'<div class="eb">Sin vueltas</div><h1 style="font-size:104px">¿Cuánto cuesta una <em>página web?</em></h1><p class="body">Te muestro por qué hay precios tan distintos.</p><div class="row3">{three}</div>', ''))
d9.append(('m', f'<div class="eb">Depende de 4 cosas</div><h2>No es lo mismo una página <em>que otra</em></h2><div class="row3">{three}</div><p class="tipline">Cuanto más hace tu página, más trabajo lleva. Mirá 👉</p>', ''))
d9.append(('m', '<div class="eb">1 · Cuántas secciones</div><h2>Una sola página o <em>un sitio completo</em></h2>'
               f'<div class="row3"><div>{scaled(site("dulce", 1), .52, 820, 470)}<div class="cap">1 sección</div></div><div>{scaled(site("raiz", 2), .52, 820, 560)}<div class="cap">Varias secciones</div></div></div>', ''))
d9.append(('m', '<div class="eb">2 · Plantilla o a medida</div><h2>¿Igual a mil páginas o <em>pensada para vos?</em></h2>'
               f'<div class="row3"><div>{scaled(template_site(), .52, 820, 470)}<div class="cap" style="color:#C0392B">Plantilla</div></div><div>{scaled(site("dulce", 2), .52, 820, 560)}<div class="cap">A medida</div></div></div>', ''))
d9.append(('m', '<div class="eb">3 · Funciones</div><h2>Turnos, pagos o <em>cuentas de usuarios</em></h2>'
               f'<div class="row3">{scaled(site("clara", 3), .95, 820, 600)}</div><p class="tipline">Cada función suma trabajo, y también <b>te ahorra un montón de tiempo.</b></p>', ''))
d9.append(('m', '<div class="eb">4 · Dominio propio</div><h2>Tu dirección dice mucho <em>de tu marca</em></h2>'
               f'<div class="list" style="gap:30px"><div>{CROSS}<span class="urlbar bad">dulcemia.sitiogratis.com/inicio</span></div><div>{CHECK}<span class="urlbar">dulcemia.com.ar</span></div></div>'
               '<p class="tipline">Y preguntá <b>quién la mantiene</b> después de publicarla.</p>', ''))
d9.append(('m', '<div class="eb">Ojo con lo muy barato</div><h2>Antes de pagar, <em>preguntá esto</em></h2>'
               f'<div class="list"><div>{CHECK}¿Qué incluye exactamente?</div><div>{CHECK}¿La puedo editar yo después?</div><div>{CHECK}¿El dominio queda a mi nombre?</div><div>{CHECK}¿Se ve bien en el celular?</div></div>', ''))
d9.append(end('¿Querés saber cuánto costaría *la tuya?*', 'Escribime por DM, sin compromiso'))

# ================= DÍA 11 · apps gratis =================
def icon(ch, bg): return f'<div class="icon" style="background:{bg}">{ch}</div>'
ICONS = [('C', '#8B5CF6'), ('▶', '#1C1A17'), ('◐', '#E07A3F'), ('Aa', '#2F4A6D'), ('✂', '#5E7D5B')]
def apphead(n, name, what, ic):
    return f'<div class="app">{icon(*ic)}<div><div class="eb">{n} de 5 · Gratis</div><h2 style="font-size:84px">{name}</h2></div></div><p class="body" style="font-size:40px">{what}</p>'
b = BRANDS['dulce']
post = (f'<div style="width:400px;height:400px;background:{b["c"]};border-radius:24px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:10px;color:{b["ink"]};box-shadow:0 30px 60px -34px rgba(0,0,0,.5)">'
        f'<span style="font-size:20px;letter-spacing:.3em">NUEVO</span><span style="font-family:B;font-size:56px;text-align:center;line-height:1.05">Torta<br><em>frutos rojos</em></span><span style="background:{b["ink"]};color:#fff;font-size:18px;padding:8px 18px;border-radius:999px">Pedila 👇</span></div>')
story = (f'<div style="width:225px;height:400px;background:{b["light"]};border-radius:24px;border:3px solid {b["c"]};display:flex;flex-direction:column;justify-content:center;align-items:center;gap:12px;color:{b["ink"]}">'
         f'<span style="font-family:B;font-size:34px">Dulce Mía</span><span style="font-size:18px">¿Cuál preferís?</span><span style="background:#fff;border-radius:12px;padding:8px 14px;font-size:16px">🍓 vs 🍫</span></div>')
video = (f'<div style="display:flex;flex-direction:column;gap:16px;align-items:center"><div style="width:360px;height:560px;border-radius:28px;background:linear-gradient(160deg,{b["c"]},{b["ink"]});position:relative;box-shadow:0 30px 60px -34px rgba(0,0,0,.5)">'
         f'<span style="position:absolute;left:24px;right:24px;bottom:70px;background:#fff;color:#1C1A17;font-size:26px;font-weight:600;padding:10px 14px;border-radius:10px;text-align:center">y así quedó la torta 🎂</span></div>'
         '<div style="display:flex;gap:6px;width:560px">' + ''.join(f'<i style="flex:{w};height:44px;border-radius:8px;background:{c}"></i>' for w, c in [(3, '#E8B4B8'), (2, '#C9A34E'), (4, '#4A2329'), (2, '#E8B4B8')]) + '</div>'
         '<div style="display:flex;gap:6px;width:560px">' + ''.join(f'<i style="flex:{w};height:26px;border-radius:6px;background:#FFF0A8;border:2px solid #E6D27A"></i>' for w in (2, 3, 2, 4)) + '</div></div>')
pal = '<div style="display:flex;width:880px;height:420px;border-radius:26px;overflow:hidden;box-shadow:0 30px 60px -34px rgba(0,0,0,.4)">' + ''.join(
    f'<div style="flex:1;background:{c};display:flex;align-items:flex-end;justify-content:center;padding-bottom:20px;font-size:24px;font-weight:500;color:{t}">{c[1:]}</div>'
    for c, t in [('#E8B4B8', '#4A2329'), ('#FFF6F4', '#4A2329'), ('#4A2329', '#FFF6F4'), ('#C9A34E', '#1C1A17'), ('#8FA68C', '#1C1A17')]) + '</div>'
fonts = ('<div style="display:flex;flex-direction:column;gap:20px;background:#fff;border-radius:26px;padding:40px 46px;box-shadow:0 30px 60px -34px rgba(0,0,0,.4)">'
         '<div><span style="font-size:20px;color:#888">Bodoni Moda</span><div style="font-family:B;font-size:80px;line-height:1.1">Dulce Mía</div></div>'
         '<div><span style="font-size:20px;color:#888">Jost</span><div style="font-family:J;font-weight:500;font-size:64px;letter-spacing:.12em">DULCE MÍA</div></div>'
         '<div><span style="font-size:20px;color:#888">Bodoni Moda Itálica</span><div style="font-family:B;font-style:italic;font-size:80px;line-height:1.1">hecho con amor</div></div></div>')
cake = ('<svg width="300" height="300" viewBox="0 0 100 100"><rect x="18" y="52" width="64" height="30" rx="4" fill="#E8B4B8"/><rect x="24" y="34" width="52" height="20" rx="4" fill="#FFF6F4" stroke="#E8B4B8" stroke-width="2"/>'
        '<circle cx="40" cy="30" r="5" fill="#C0392B"/><circle cx="52" cy="28" r="5" fill="#C0392B"/><circle cx="62" cy="31" r="5" fill="#C0392B"/><rect x="12" y="81" width="76" height="5" rx="2" fill="#C9A34E"/></svg>')
before = f'<div style="width:400px;height:400px;border-radius:24px;background:linear-gradient(135deg,#8d8d8d 0 30%,#b9a68c 30% 55%,#6f7d8c 55%);display:grid;place-items:center">{cake}</div>'
after = f'<div style="width:400px;height:400px;border-radius:24px;background:repeating-conic-gradient(#eee 0 25%,#fff 0 50%) 0 0/40px 40px;display:grid;place-items:center">{cake}</div>'
bars = '<div style="display:flex;align-items:flex-end;gap:10px;height:360px;background:#fff;border-radius:26px;padding:30px 36px 20px;box-shadow:0 30px 60px -34px rgba(0,0,0,.4)">' + ''.join(
    f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px"><i style="width:44px;height:{int(v*2.6)}px;border-radius:8px;background:{"#C9A34E" if h in (10, 18) else "#E6DAC2"}"></i><span style="font-size:18px;color:{"#8A6A22" if h in (10, 18) else "#999"};font-weight:{600 if h in (10, 18) else 400}">{h}h</span></div>'
    for h, v in [(8, 45), (9, 70), (10, 100), (11, 90), (12, 88), (14, 66), (16, 68), (18, 92), (20, 50), (22, 22)]) + '</div>'
d11 = []
d11.append(('n', f'<div class="eb">Guardalo</div><h1 style="font-size:104px">5 apps <em>gratis</em> para que tu marca se vea profesional</h1><div class="tiles">{"".join(icon(*i) for i in ICONS)}</div>', ''))
d11.append(('m', apphead(1, 'Canva', 'Para diseñar posteos e historias con tus colores.', ICONS[0]) + f'<div class="row3" style="align-items:center">{post}{story}</div>', ''))
d11.append(('m', apphead(2, 'CapCut', 'Para editar reels con subtítulos automáticos.', ICONS[1]) + f'<div class="row3">{video}</div>', ''))
d11.append(('m', apphead(3, 'Coolors', 'Para encontrar paletas de colores que combinan.', ICONS[2]) + pal, ''))
d11.append(('m', apphead(4, 'Google Fonts', 'Tipografías lindas, gratis y para usar en todos lados.', ICONS[3]) + fonts, ''))
d11.append(('m', apphead(5, 'Remove.bg', 'Para sacarle el fondo a tus fotos en un clic.', ICONS[4]) + f'<div class="row3" style="align-items:center">{before}<span style="font-size:70px;color:#8A6A22">→</span>{after}</div>', ''))
d11.append(('m', f'<div class="eb">Bonus</div><h2>Metricool: a qué hora <em>está conectada tu gente</em></h2>{bars}<p class="tipline">Así sabés cuándo publicar para que te vean más.</p>', ''))
d11.append(end('¿Cuál *no conocías?*', 'Guardalo para después'))

# ================= DÍA 13 · página web vs linktree =================
lt = linktree('dulce', 380); web = scaled(site('dulce', 2), .62, 820, 560)
d13 = []
d13.append(('g', f'<div class="eb">Te ayudo a elegir</div><h1 style="font-size:110px">¿Página web o <em>Linktree?</em></h1><div class="row3" style="align-items:center">{scaled(lt, .78, 380, 640)}<span style="font-family:B;font-size:70px;font-style:italic">vs</span>{scaled(site("dulce", 2), .5, 820, 560)}</div>', ''))
d13.append(('m', f'<div class="split">{scaled(lt, .95, 380, 640)}<div style="display:flex;flex-direction:column;gap:26px"><div class="eb">Linktree</div><h2 style="font-size:70px">Lo bueno</h2>'
                 f'<div class="list"><div>{CHECK}Es gratis</div><div>{CHECK}Lo armás en minutos</div><div>{CHECK}Ideal para arrancar</div></div></div></div>', ''))
d13.append(('m', f'<div class="split"><div style="opacity:.45">{scaled(lt, .95, 380, 640)}</div><div style="display:flex;flex-direction:column;gap:26px"><div class="eb">Linktree</div><h2 style="font-size:70px">Lo no tan bueno</h2>'
                 f'<div class="list"><div>{CROSS}Todas se ven iguales</div><div>{CROSS}No aparece en Google</div><div>{CROSS}No es tuyo</div></div></div></div>', ''))
d13.append(('m', f'<div class="eb">Página web</div><h2>Lo bueno</h2>{web}<div class="list" style="flex-direction:row;flex-wrap:wrap;gap:16px 34px;font-size:36px"><div>{CHECK}Tu diseño</div><div>{CHECK}Tu dominio</div><div>{CHECK}Aparece en Google</div></div>', ''))
d13.append(('m', f'<div class="eb">Página web</div><h2>Lo no tan bueno</h2><div style="opacity:.45">{web}</div><div class="list" style="font-size:36px"><div>{CROSS}Lleva más trabajo armarla (o contratar a alguien, jaja)</div></div>', ''))
d13.append(('m', '<div class="eb">Mi consejo</div><h2>Depende de <em>tu etapa</em></h2>'
                 '<div style="display:flex;flex-direction:column;gap:22px">'
                 '<div class="urlbar" style="justify-content:space-between"><span>Recién arrancás</span><span style="color:#8A6A22;font-weight:500">→ Linktree</span></div>'
                 '<div class="urlbar" style="justify-content:space-between;background:#1C1A17;color:#FAF6EE"><span>Querés crecer</span><span style="color:#C9A34E;font-weight:500">→ Página web ✦</span></div></div>', ''))
d13.append(end('¿Cuál usás *vos?*', 'Contame en comentarios', 'g'))

if __name__ == '__main__':
    for name, sl in [('dia09-carrusel-cuanto-cuesta-una-pagina', d9), ('dia11-carrusel-5-apps-gratis', d11), ('dia13-carrusel-pagina-web-vs-linktree', d13)]:
        print(render(name, sl, EXT))
