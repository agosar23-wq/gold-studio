"""Carruseles semana 3: antes y después de un feed, qué tiene que tener tu web, qué necesito para arrancar."""
import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
from caro_ejemplos import render, end
from carogen import F, CHECK
import mocks as M, portada_wa4 as D

EXT = f'''
@font-face{{font-family:XArchivo;src:url({F}archivo-black/files/archivo-black-latin-400-normal.woff2)}}
.ph{{border-radius:54px;background:#1C1A17;padding:14px;box-shadow:0 40px 70px -36px rgba(0,0,0,.6);flex:none}}
.ph>div{{border-radius:42px;overflow:hidden;background:#fff}}
.lab2{{display:inline-block;font-size:26px;font-weight:500;padding:7px 20px;border-radius:999px;letter-spacing:.06em}}
.tip2{{text-align:left;font-size:34px;line-height:1.35;color:var(--sub);font-weight:300;margin:0}}
.hl{{outline:5px solid #C9A34E;outline-offset:6px;border-radius:12px}}
'''
# ================= FEED ANTES / DESPUÉS (Brisa, ropa de lino) =================
SAGE, SAND, BARK, CREAM = '#9DAE94', '#E9E1D3', '#6B5B4B', '#F7F3EC'
def igp(stage, w=520, hl=None):
    s = w / 520
    px = lambda v: int(v * s)
    mark = lambda k: ' class="hl"' if hl == k else ''
    av = (f'<div{mark("av")} style="width:{px(120)}px;height:{px(120)}px;border-radius:50%;background:{SAGE};display:grid;place-items:center;font-family:B;font-size:{px(40)}px;color:{CREAM};flex:none">brisa</div>'
          if stage >= 1 else f'<div style="width:{px(120)}px;height:{px(120)}px;border-radius:50%;background:radial-gradient(circle at 40% 35%,#c9c3bb,#8d877f);filter:blur({px(2)}px);flex:none"></div>')
    stats = ''.join(f'<div style="text-align:center"><b style="display:block;font-size:{px(26)}px">{n}</b>{t}</div>' for n, t in [('86', 'posts'), ('1.204', 'seguidores'), ('180', 'seguidos')])
    if stage >= 2:
        bio = (f'<div{mark("bio")} style="font-size:{px(19)}px;line-height:1.4;padding:{px(4)}px"><b>Brisa · Ropa de lino</b><br>Prendas de lino hechas en Argentina<br>Envíos a todo el país<br>'
               f'Pedidos por WhatsApp<br><span style="color:#2F4A6D">brisa.com.ar</span></div>')
    else:
        bio = f'<div style="font-size:{px(19)}px;line-height:1.4"><b>brisa_ropa_ok</b><br>ropa linda!! consultas x md<br>no hacemos cambios</div>'
    if stage >= 3:
        hls = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:{px(6)}px;font-size:{px(14)}px"><div style="width:{px(70)}px;height:{px(70)}px;border-radius:50%;background:{c};border:{px(3)}px solid #fff;box-shadow:0 0 0 {px(2)}px #ddd;display:grid;place-items:center;font-family:B;color:{CREAM};font-size:{px(24)}px">{i}</div>{t}</div>'
                      for c, i, t in [(SAGE, '✦', 'Nuevo'), (BARK, 'T', 'Talles'), (SAND, '↗', 'Envíos'), (SAGE, '♡', 'Opiniones')])
        hls = f'<div{mark("hl")} style="display:flex;gap:{px(18)}px;padding:{px(4)}px">{hls}</div>'
    else:
        hls = ''.join(f'<div style="width:{px(70)}px;height:{px(70)}px;border-radius:50%;background:{c};border:{px(3)}px solid #fff;box-shadow:0 0 0 {px(2)}px #ddd"></div>' for c in ['#FF6B6B', '#4D96FF', '#333'])
        hls = f'<div style="display:flex;gap:{px(18)}px">{hls}</div>'
    if stage >= 4:
        T = [(SAGE, CREAM, 'Nueva<br>colección'), (SAND, BARK, '<i>Lino</i>'), (BARK, CREAM, '✦'), (CREAM, BARK, 'Talles'), (SAGE, CREAM, '<i>Verano</i>'), (SAND, BARK, 'Envíos'),
             (BARK, CREAM, 'Opiniones'), (CREAM, SAGE, '✦'), (SAGE, CREAM, 'Hecho<br>acá')]
        grid = ''.join(f'<div style="aspect-ratio:1;background:{b};color:{f};display:grid;place-items:center;text-align:center;font-family:B;font-size:{px(22)}px;line-height:1.1">{t}</div>' for b, f, t in T)
    else:
        grid = ''.join(f'<div style="aspect-ratio:1;background:{c}"></div>' for c in ['#FF6B6B', '#F4D35E', '#2EC4B6', '#9B5DE5', '#333', '#F15BB5', '#00BBF9', '#FEE440', '#8AC926'])
    grid = f'<div{mark("grid")} style="display:grid;grid-template-columns:repeat(3,1fr);gap:{px(3)}px">{grid}</div>'
    inner = (f'<div style="padding:{px(26)}px {px(20)}px {px(12)}px;display:flex;flex-direction:column;gap:{px(14)}px;font-family:J;color:#1C1A17">'
             f'<div style="display:flex;gap:{px(24)}px;align-items:center">{av}<div style="display:flex;gap:{px(20)}px;font-size:{px(16)}px">{stats}</div></div>{bio}{hls}</div>{grid}')
    return f'<div class="ph" style="width:{w}px"><div>{inner}</div></div>'
pair = lambda w: (f'<div style="display:flex;gap:40px;justify-content:center;align-items:flex-start">'
                  f'<div style="display:flex;flex-direction:column;gap:16px;align-items:center"><span class="lab2" style="background:#C0392B;color:#fff">Antes</span>{igp(0, w)}</div>'
                  f'<div style="display:flex;flex-direction:column;gap:16px;align-items:center"><span class="lab2" style="background:#1C1A17;color:#FAF6EE">Después</span>{igp(4, w)}</div></div>')
def fstep(n, t, stage, hl, tip):
    return ('m', f'<div class="eb">Paso {n}</div><h2 style="font-size:66px">{t}</h2><div style="display:flex;justify-content:center">{igp(stage, 470, hl)}</div><p class="tip2">{tip}</p>', 'justify-content:flex-start;padding-top:90px;gap:26px')
feed = [
 ('m', f'<div class="eb">Ejemplo real de cómo ordeno un perfil</div><h1 style="font-size:92px">Antes y después de <em>un feed</em></h1>{pair(400)}', 'gap:30px'),
 fstep(1, 'La foto de <em>perfil</em>', 1, 'av', 'Tu logo, no una foto borrosa. Es lo primero que se ve.'),
 fstep(2, 'La <em>bio</em>', 2, 'bio', 'Qué vendés, para quién, dónde y cómo comprarte.'),
 fstep(3, 'Las <em>destacadas</em>', 3, 'hl', 'Portadas iguales y temas útiles: talles, envíos, opiniones.'),
 fstep(4, 'La <em>grilla</em>', 4, 'grid', 'Tres o cuatro colores que se repiten. Así se ve como una marca.'),
 ('g', f'<h1 style="font-size:96px">Mismas fotos, <em>otra marca</em></h1>{pair(400)}', 'gap:30px'),
 end('¿Querés que ordenemos *el tuyo?*', 'Escribime · marca de ejemplo'),
]

# ================= LO QUE TIENE QUE TENER TU WEB (Clara, psicología) =================
CL = M.BRANDS['clara']
def secs(k):
    S = [
     ('Inicio', f'<div style="background:{CL["c"]};color:{CL["light"]};padding:34px 30px;display:flex;flex-direction:column;gap:12px"><span style="font-size:15px;letter-spacing:.3em">PSICOLOGÍA</span>'
                f'<span style="font-family:B;font-size:40px;line-height:1.1">Terapia online para adultos que quieren sentirse mejor</span><span style="align-self:flex-start;background:#fff;color:{CL["c"]};font-size:17px;padding:9px 20px;border-radius:999px">Pedí tu primera sesión</span></div>'),
     ('Servicios', '<div style="padding:22px 30px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;background:#fff">' + ''.join(f'<div style="border:2px solid {CL["c"]}33;border-radius:12px;padding:14px;font-size:17px;color:{CL["ink"]}"><b style="display:block;font-family:B;font-weight:500;font-size:22px">{t}</b>{d}</div>' for t, d in [('Individual', '50 min, online'), ('Pareja', '60 min, online'), ('Talleres', 'Grupales')]) + '</div>'),
     ('Sobre mí', f'<div style="padding:22px 30px;display:flex;gap:20px;align-items:center;background:{CL["light"]}"><div style="width:96px;height:96px;border-radius:50%;background:{CL["c"]}55;flex:none"></div><div style="font-size:17px;color:{CL["ink"]}"><b style="font-family:B;font-weight:500;font-size:24px;display:block">Lic. Clara Méndez</b>Psicóloga, matrícula y enfoque. Para que te conozcan antes de escribirte.</div></div>'),
     ('Opiniones', '<div style="padding:22px 30px;display:grid;grid-template-columns:1fr 1fr;gap:14px;background:#fff">' + ''.join(f'<div style="background:{CL["light"]};border-radius:12px;padding:14px;font-size:16px;color:{CL["ink"]}"><span style="color:#C9A34E">★★★★★</span><br>{t}</div>' for t in ['"Me sentí escuchada desde la primera sesión."', '"Muy clara y cálida. La recomiendo."']) + '</div>'),
     ('Contacto', f'<div style="padding:22px 30px;background:{CL["light"]};display:flex;justify-content:space-between;align-items:center;font-size:17px;color:{CL["ink"]}"><span>Turnos de lunes a viernes</span><span style="background:#25D366;color:#fff;padding:10px 20px;border-radius:999px;font-weight:500">Escribime por WhatsApp</span></div>'),
    ]
    head = f'<div style="display:flex;justify-content:space-between;align-items:center;padding:16px 30px;background:#fff;border-bottom:1px solid #eee"><span style="font-family:J;font-weight:500;letter-spacing:.16em;font-size:22px;color:{CL["ink"]}">CLARA</span><span style="font-size:15px;color:{CL["ink"]};opacity:.7">Inicio · Servicios · Sobre mí · Contacto</span></div>'
    body = ''.join((f'<div style="outline:5px solid #C9A34E;outline-offset:-5px">{h}</div>' if i == k - 1 else h) for i, (_, h) in enumerate(S[:k]))
    return M.browser(head + body, 860, 'clarapsicologia.com.ar')
def wstep(k, t, tip):
    return ('m', f'<div class="eb">{k} de 5</div><h2 style="font-size:66px">{t}</h2><div>{secs(k)}</div><p class="tip2">{tip}</p>', 'justify-content:flex-start;padding-top:90px;gap:26px')
web = [
 ('n', f'<div class="eb">Guardalo</div><h1 style="font-size:100px">Lo que tiene que tener <em>tu página web</em></h1><div style="transform:scale(.8);transform-origin:top left">{secs(5)}</div>', 'justify-content:flex-start;padding-top:110px'),
 wstep(1, 'Un inicio <em>que se entienda</em>', 'Qué hacés y para quién, en una frase. Y un botón para dar el primer paso.'),
 wstep(2, 'Tus <em>servicios</em>', 'Claros y cortitos. Que nadie tenga que preguntarte qué ofrecés.'),
 wstep(3, 'Quién está <em>detrás</em>', 'La gente le compra a personas. Contá quién sos.'),
 wstep(4, 'Lo que dicen <em>tus clientes</em>', 'Dos o tres opiniones reales valen más que cualquier texto.'),
 wstep(5, 'Un contacto <em>fácil</em>', 'Botón a WhatsApp siempre a mano. Escribirte tiene que ser un toque.'),
 end('¿A tu web le falta *alguna?*', 'Escribime y la armamos'),
]

# ================= QUÉ NECESITO PARA ARRANCAR =================
desk = (f'<div style="position:relative;width:888px;height:560px;border-radius:30px;overflow:hidden;background:linear-gradient(135deg,#F5EFE4,#EDE4D3)">'
        + D.ab(-60, 40, D.laptop, -6, 2).replace('<div style="width:600px', '<div style="transform:scale(.8);transform-origin:top left;width:600px')
        + D.ab(520, 40, D.note, 7, 2).replace('width:330px;height:420px', 'width:280px;height:360px') + D.ab(600, 330, D.coffee, 0, 3) + '</div>')
def card(title, body): return f'<div style="background:#FFFDF8;border:2px solid #E6DAC2;border-radius:24px;padding:30px 34px;display:flex;flex-direction:column;gap:10px"><b style="font-family:B;font-weight:500;font-size:40px">{title}</b><span style="font-size:30px;color:#5E5649;line-height:1.4">{body}</span></div>'
bub = lambda t: f'<div style="align-self:flex-start;background:#fff;border-radius:6px 28px 28px 28px;padding:20px 28px;font-size:32px;box-shadow:0 10px 30px -14px rgba(0,0,0,.3);max-width:760px">{t}</div>'
have = '<div style="display:flex;flex-direction:column;gap:18px">' + ''.join(f'<div style="display:flex;gap:20px;align-items:center;font-size:36px">{CHECK}<span>{t}</span></div>' for t in ['Tu logo, si ya tenés', 'Tus colores o fotos de marca', 'Tus redes y tu página, si existen']) + '</div>'
cal = ('<div style="background:#fff;border-radius:24px;padding:26px;box-shadow:0 30px 50px -30px rgba(0,0,0,.4);width:560px"><div style="font-family:B;font-size:36px;margin-bottom:16px">Noviembre</div>'
       '<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:10px;text-align:center;font-size:24px">' + ''.join(f'<span style="padding:8px 0;border-radius:50%;{"background:#C9A34E;color:#fff" if d == 20 else ""}">{d}</span>' for d in range(1, 31)) + '</div></div>')
stepsx = '<div style="display:flex;flex-direction:column;gap:22px">' + ''.join(f'<div style="display:flex;gap:26px;align-items:baseline"><span style="font-family:B;font-style:italic;font-size:80px;color:#B8923A;width:60px">{i}</span><div><b style="font-family:B;font-weight:500;font-size:44px">{t}</b><div style="font-size:30px;color:#5E5649">{d}</div></div></div>' for i, t, d in [(1, 'Te paso un presupuesto', 'Según lo que necesitás.'), (2, 'Te muestro la propuesta', 'Y ajustamos hasta que te encante.'), (3, 'Te entrego todo', 'Listo para usar, y te sigo acompañando.')]) + '</div>'
MOOD = ('<div style="display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:150px;gap:12px;width:888px">'
  '<div style="grid-row:span 2;border-radius:18px;background:linear-gradient(160deg,#E9DCC9,#C9B79C)"></div>'
  '<div style="border-radius:18px;background:#3E3557"></div><div style="border-radius:18px;background:#D9CFF0"></div>'
  '<div style="grid-row:span 2;border-radius:18px;background:#F7F4EF;display:grid;place-items:center;font-family:B;font-size:70px;color:#3E3557">Aa</div>'
  '<div style="grid-column:span 2;border-radius:18px;background:repeating-linear-gradient(45deg,#E8DCC8 0 18px,#F7F4EF 18px 36px)"></div>'
  '<div style="border-radius:18px;background:#9DAE94"></div><div style="grid-column:span 2;border-radius:18px;background:#fff;border:2px dashed #C9A34E;display:grid;place-items:center;font-size:26px;color:#8A6A22">tu inspiración de Pinterest</div>'
  '<div style="border-radius:18px;background:#C9A34E"></div></div>')
start = [
 ('m', f'<div class="eb">Antes de empezar</div><h1 style="font-size:96px">Qué necesito para <em>arrancar tu proyecto</em></h1>{desk}', 'gap:30px'),
 ('m', f'<div class="eb">1</div><h2>Que me cuentes <em>tu marca</em></h2>{bub("Hola! Tengo una pastelería en Palermo")}{bub("Vendo tortas por encargo y quiero que se vea más profesional")}<p class="tip2">Qué hacés, a quién le vendés y qué te gustaría lograr.</p>', ''),
 ('m', f'<div class="eb">2</div><h2>Lo que <em>ya tenés</em></h2>{have}<p class="tip2">Si no tenés nada, no pasa nada: lo armamos desde cero.</p>', ''),
 ('m', f'<div class="eb">3</div><h2>Ejemplos que <em>te gusten</em></h2>{MOOD}<p class="tip2">Marcas, colores o cuentas que te inspiren. Me ayudan a entender tu estilo.</p>', ''),
 ('m', f'<div class="eb">4</div><h2>Para <em>cuándo</em> lo necesitás</h2><div style="display:flex;justify-content:center">{cal}</div><p class="tip2">Si tenés una fecha especial, como un lanzamiento, contámela.</p>', ''),
 ('n', f'<div class="eb">Y después</div><h2>Cómo <em>seguimos</em></h2>{stepsx}', ''),
 end('¿Arrancamos con *tu marca?*', 'Escribime · catálogo en el link de la bio'),
]
if __name__ == '__main__':
    print(render('dia25-carrusel-antes-despues-feed', feed, EXT))
    print(render('dia28-carrusel-que-tiene-que-tener-tu-web', web, EXT))
    print(render('dia30-carrusel-que-necesito-para-arrancar', start, EXT))
