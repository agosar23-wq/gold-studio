"""Carrusel estilo proceso: 'Así diseñaría una marca de hamburguesas' (marca de ejemplo Doña Rulos), con fotos reales de Pexels de una misma parrilla."""
import sys, base64; sys.path.insert(0, '/home/user/gold-studio-contenido')
from caro_ejemplos import render
from carogen import SP, SCR, F

# Fotos de Pexels (Los Muertos Crew, una misma sesión: la misma parrilla, el mismo cocinero y la misma luz): pexels.com/photo/<id>
def _img(i): return 'data:image/jpeg;base64,' + base64.b64encode(open(f'{SCR}/burger/{i}.jpg', 'rb').read()).decode()
PX = {k: _img(i) for k, i in {
    'bandeja': 8477222, 'chispas': 8477224, 'parrilla': 8477292, 'chef': 8477293, 'parrilla2': 8477295, 'humo': 8477301,
    'brindis': 8477346, 'cocinera': 8477348, 'pinza': 8477355, 'cerveza': 8477359, 'sliders_birra': 8477413,
    'mordida': 8477415, 'sliders': 8477416, 'manos': 8477417, 'tabla': 8477420, 'armado': 8477421, 'chef2': 8477422,
}.items()}
# Mascota (ilustración de línea hecha con Canva): la señora de los ruleros sentada arriba de una hamburguesa doble
PX['senora'] = 'data:image/jpeg;base64,' + base64.b64encode(open(f'{SCR}/ilus/senora-burger.jpg', 'rb').read()).decode()
CAR, BOR, MOS, CRE, BRA = '#1C1714', '#7A1F1F', '#E0A526', '#F3ECE2', '#C2502A'

EXT = f'''
@font-face{{font-family:XArchivo;src:url({F}archivo-black/files/archivo-black-latin-400-normal.woff2)}}
.ph{{background-size:cover;background-position:center;background-repeat:no-repeat}}
.step{{display:flex;align-items:baseline;gap:26px}}
.step .num{{font-size:120px}}
.step h2{{font-size:70px}}
.cap{{font-size:30px;color:var(--sub);line-height:1.4;font-weight:300}}
.cap b{{font-weight:500;color:var(--em)}}
.shadow{{box-shadow:0 40px 70px -40px rgba(28,26,23,.55)}}
.post{{width:300px;height:375px;position:relative;overflow:hidden;font-family:J}}
.post .t{{font-family:XArchivo;line-height:1.02;text-transform:uppercase;letter-spacing:.01em}}
.post .shade{{position:absolute;inset:0;background:linear-gradient(transparent 40%,rgba(16,10,8,.85))}}
.mood{{display:grid;grid-template-columns:1.25fr 1fr 1fr;grid-template-rows:330px 330px;gap:16px;align-self:center;width:888px}}
.mood>div{{border-radius:22px}}
.kw{{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}}
.kw span{{border:2px solid var(--g);color:var(--em);border-radius:999px;padding:12px 30px;font-size:30px}}
.pal{{display:grid;grid-template-columns:repeat(5,1fr);gap:18px;width:888px;align-self:center}}
.pal .c{{display:flex;flex-direction:column;gap:12px;align-items:center;font-size:20px;letter-spacing:.12em;color:var(--sub)}}
.pal .dot{{width:150px;height:150px;border-radius:50%;position:relative;box-shadow:0 0 0 2px rgba(28,26,23,.08)}}
.pal .dot i{{position:absolute;right:-12px;bottom:-6px;width:70px;height:70px;border-radius:50%;border:5px solid #FAF6EE;background-size:cover;background-position:center}}
.est{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;width:888px;align-self:center}}
.est>div{{display:flex;flex-direction:column;gap:12px}}
.est .ph{{height:250px;border-radius:20px}}
.est b{{font-family:B;font-weight:500;font-size:32px;line-height:1.1}}
.est span{{font-size:22px;color:var(--sub);line-height:1.3}}
.feed6{{display:grid;grid-template-columns:repeat(3,280px);gap:14px;align-self:center}}
.feed6 .post{{zoom:.9333}}
'''

ph = lambda k, pos='center', extra='': f'background-image:url({PX[k]});background-position:{pos};{extra}'
def logo(c, s=30, sub=None):
    return (f'<span style="display:inline-flex;flex-direction:column;align-items:center;line-height:.95"><span style="font-family:XArchivo;font-size:{s}px;color:{c};letter-spacing:.02em;white-space:nowrap">DOÑA RULOS</span>'
            + (f'<span style="font-size:{s*.2:.0f}px;letter-spacing:.32em;color:{sub};margin-top:{s*.15:.0f}px">HAMBURGUESAS A LA PARRILLA</span>' if sub else '') + '</span>')
PLAY = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6"><rect x="3" y="4" width="18" height="16" rx="4"/><path d="M10 9.5v5l4.2-2.5z" fill="#fff"/></svg>'

# ---- Posteos de Doña Rulos (300×375, se escalan con zoom) ----
def p_reel():
    return (f'<div class="post ph" style="{ph("chispas", "center 35%")}"><div class="shade"></div><div style="position:absolute;right:16px;top:16px">{PLAY}</div>'
            f'<div class="t" style="position:absolute;left:20px;right:20px;bottom:22px;color:{CRE};font-size:30px">Así se prende<br><span style="color:{MOS}">el fuego.</span></div></div>')
def p_frase():
    return (f'<div class="post" style="background:{CRE};display:flex;flex-direction:column;justify-content:center;padding:0 26px;box-sizing:border-box;gap:16px">'
            f'<div class="t" style="font-size:44px;color:{BOR}">Una no<br>alcanza.</div>'
            f'<div class="ph" style="height:120px;border-radius:999px 999px 0 0;{ph("tabla", "center 55%")}"></div>{logo(BOR, 18)}</div>')
def mascota_svg(texto=True):
    t = (f'<text x="60" y="110" font-family="XArchivo" font-size="54" fill="{BOR}">DOÑA RULOS</text>'
         f'<text x="568" y="1310" text-anchor="middle" font-family="XArchivo" font-size="112" fill="{BOR}">PEDÍ LA DOBLE.</text>') if texto else ''
    return (f'<svg viewBox="0 0 1136 1400" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0;width:100%;height:100%">'
            f'<rect width="1136" height="1400" fill="#F3ECE2"/><image href="{PX["senora"]}" x="0" y="0" width="1136" height="1400" preserveAspectRatio="xMidYMid slice"/>{t}</svg>')
def p_mascota():
    return f'<div class="post">{mascota_svg()}</div>'
def p_reco():
    return (f'<div class="post ph" style="{ph("sliders_birra", "center 60%")}"><div class="shade"></div>'
            f'<div style="position:absolute;left:16px;top:16px;background:{MOS};color:{CAR};font-size:14px;letter-spacing:.2em;padding:8px 14px;border-radius:999px;font-weight:500">LA DE LA CASA</div>'
            f'<div class="t" style="position:absolute;left:20px;right:20px;bottom:22px;color:{CRE};font-size:28px">Triple slider<br><span style="color:{MOS}">+ birra tirada</span></div></div>')
def p_lugar():
    return (f'<div class="post ph" style="{ph("brindis", "62% center")}"><div style="position:absolute;left:0;right:0;bottom:0;height:112px;background:{BOR};display:flex;flex-direction:column;justify-content:center;padding:0 20px">'
            f'<div class="t" style="font-size:20px;color:{CRE}">Vení con hambre.<br><span style="color:{MOS}">Volvé con amigos.</span></div></div></div>')
def p_marca():
    return (f'<div class="post ph" style="{ph("humo", "40% center")}"><div style="position:absolute;inset:0;background:rgba(20,12,10,.66)"></div>'
            f'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">{logo(CRE, 34, MOS)}</div></div>')
def p_mordida():
    return (f'<div class="post ph" style="{ph("mordida", "center 45%")}"><div style="position:absolute;left:18px;top:18px;background:{MOS};padding:12px 16px">'
            f'<div class="t" style="font-size:24px;color:{CAR}">Primer<br>mordisco.</div></div></div>')
def p_guia():
    def medallon(n, rosa):
        return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;color:{CRE};font-size:16px">'
                f'<svg width="76" height="48" viewBox="0 0 76 48"><rect x="3" y="6" width="70" height="36" rx="12" fill="#5A2E22" stroke="{CRE}" stroke-width="3"/>'
                f'<rect x="12" y="15" width="52" height="18" rx="8" fill="{rosa}"/></svg>{n}</div>')
    return (f'<div class="post" style="background:{CAR};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px">'
            f'<div style="color:{MOS};font-size:16px;letter-spacing:.28em">GUÍA RÁPIDA</div><div class="t" style="color:{CRE};font-size:34px;text-align:center">Elegí<br><span style="color:{MOS}">tu punto.</span></div>'
            f'<div style="display:flex;gap:10px">{medallon("Jugoso", "#C4534F")}{medallon("A punto", "#B07A5E")}{medallon("Cocido", "#7A4A36")}</div></div>')
def p_cerveza():
    return f'<div class="post ph" style="{ph("cerveza", "center 40%")}"><div style="position:absolute;right:16px;top:16px">{PLAY}</div></div>'

FEED6 = [p_reel(), p_frase(), p_mascota(), p_reco(), p_lugar(), p_marca()]
FEED9 = [p_mordida(), p_guia(), p_cerveza()] + FEED6   # lo más nuevo arriba

def step(n, t): return f'<div class="step"><div class="num">{n}</div><h2>{t}</h2></div>'

# 1. Portada
fan = ''.join(f'<div class="ph shadow" style="position:absolute;width:300px;height:375px;border:12px solid #FAF6EE;{ph(k, p)};left:{x}px;top:{y}px;transform:rotate({r}deg)"></div>'
              for k, p, x, y, r in [('chispas', 'center 35%', 60, 40, -9), ('mordida', 'center 45%', 470, 50, 8), ('tabla', 'center 55%', 250, 0, -1)])
cover = (f'<div class="eb">Proceso de branding</div>'
         f'<h1 style="font-size:104px">Así diseñaría <em>una marca de hamburguesas</em></h1>'
         f'<div style="position:relative;height:440px;width:888px">{fan}</div>')

# 2. Moodboard
mood = (f'<div class="mood"><div class="ph" style="grid-row:span 2;{ph("chispas", "center 40%")}"></div><div class="ph" style="{ph("parrilla", "40% center")}"></div>'
        f'<div class="ph" style="{ph("armado", "center 60%")}"></div><div class="ph" style="{ph("cerveza", "center 30%")}"></div><div class="ph" style="{ph("mordida", "center 40%")}"></div></div>')
s_mood = (f'{step(1, "Buscamos el <em>clima</em>")}{mood}<div class="kw"><span>Fuego</span><span>Callejera</span><span>Generosa</span></div>'
          f'<p class="cap" style="text-align:center;margin:0">Noche, humo y brasas: todo pasa en la misma parrilla.</p>')

# 3. Paleta sacada de las fotos
pal = '<div class="pal">' + ''.join(f'<div class="c"><div class="dot" style="background:{c}"><i style="{ph(k)}"></i></div>{c}</div>'
                                    for c, k in [(CAR, 'humo'), (BOR, 'brindis'), (BRA, 'chispas'), (MOS, 'cerveza'), (CRE, 'tabla')]) + '</div>'
tipo = (f'<div style="display:flex;gap:40px;align-items:center;justify-content:center;background:{CRE};border-radius:28px;padding:40px;width:888px;box-sizing:border-box;align-self:center">'
        f'<div style="text-align:center">{logo(BOR, 64, CAR)}</div>'
        f'<div style="font-size:24px;line-height:1.7;color:{CAR};border-left:2px solid {BRA};padding-left:36px">Títulos · <b>Archivo Black</b><br>Textos · <b>Jost</b></div></div>')
s_pal = (f'{step(2, "Paleta y <em>tipografías</em>")}<p class="cap" style="margin:0">Los colores salen de las mismas fotos: <b>carbón, bordó, brasa, mostaza y crema.</b></p>{pal}{tipo}')

# 4. Estrategia
est = '<div class="est">' + ''.join(f'<div><div class="ph" style="{ph(k, pos)}"></div><b>{t}</b><span>{d}</span></div>' for k, pos, t, d in [
    ('chispas', 'center 40%', 'Reels', 'Fuego, humo y armado'), ('manos', 'center', 'Producto', 'Bien de cerca, que dé hambre'),
    ('parrilla2', 'center', 'Educativo', 'Puntos de cocción y combos'), ('tabla', 'center 55%', 'Recomendación', 'La de la casa'),
    ('brindis', '62% center', 'Experiencia', 'El local y su gente'), ('senora', 'center 40%', 'Marca', 'Mascota y frases propias')]) + '</div>'
s_est = f'{step(3, "Estrategia y <em>contenidos</em>")}{est}'

# 5. Diseños
feed6 = '<div class="feed6">' + ''.join(FEED6) + '</div>'
s_dis = (f'{step(4, "Diseñamos <em>los posteos</em>")}{feed6}<p class="cap" style="margin:0;text-align:center">Fotos de la misma parrilla + una mascota con mucha actitud.</p>')

# 6. Un posteo de cerca, como se ve en Instagram
HEART = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#1C1A17" stroke-width="1.7"><path d="M12 20s-7-4.4-9-8.7C1.6 8.3 3.6 5 6.8 5c2 0 3.4 1.1 4.2 2.4h2C13.8 6.1 15.2 5 17.2 5c3.2 0 5.2 3.3 3.8 6.3-2 4.3-9 8.7-9 8.7z"/></svg>'
BUB = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#1C1A17" stroke-width="1.7"><path d="M20 11.5a8 8 0 0 1-11.6 7.1L4 20l1.4-4.2A8 8 0 1 1 20 11.5z"/></svg>'
SEND = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#1C1A17" stroke-width="1.7"><path d="M21 3 3 10.5l7 3 3 7.5z M10 13.5 21 3"/></svg>'
avatar = lambda d, s: f'<div style="width:{d}px;height:{d}px;border-radius:50%;background:{BOR};display:grid;place-items:center;flex:none;text-align:center;font-family:XArchivo;color:{CRE};font-size:{s}px;line-height:.95">DOÑA<br>RULOS</div>'
big = (f'<div class="shadow" style="width:690px;align-self:center;background:#fff;border-radius:28px;overflow:hidden;color:#1C1A17">'
       f'<div style="display:flex;align-items:center;gap:14px;padding:16px 20px">{avatar(48, 10)}'
       f'<b style="font-size:22px;font-weight:500">donarulos.burgers</b><span style="margin-left:auto;font-size:28px;letter-spacing:2px">···</span></div>'
       f'<div style="height:862px;position:relative;overflow:hidden">{mascota_svg()}</div>'
       f'<div style="display:flex;gap:20px;padding:16px 20px">{HEART}{BUB}{SEND}</div></div>')
s_big = f'<div class="eb" style="text-align:center">De cerca</div>{big}<p class="cap" style="margin:0;text-align:center">Una mascota con actitud: <b>la marca se vuelve un personaje.</b></p>'

# 7. Perfil
prof = ('<div class="shadow" style="width:560px;border-radius:56px;background:#111;padding:14px;align-self:center"><div style="border-radius:44px;overflow:hidden;background:#fff;color:#1C1A17">'
        f'<div style="padding:26px 22px 10px;display:flex;gap:22px;align-items:center">{avatar(96, 19)}'
        '<div style="display:flex;gap:22px;font-size:16px;text-align:center">' + ''.join(f'<div><b style="display:block;font-size:26px;font-weight:500">{a}</b>{b}</div>' for a, b in [('64', 'posts'), ('5.120', 'seguidores'), ('180', 'seguidos')]) + '</div></div>'
        '<div style="padding:0 22px 14px;font-size:17px;line-height:1.45"><b style="font-weight:500">Doña Rulos · Hamburguesas a la parrilla</b><br>Fuego, smash y amigos 🔥<br>Mar a dom · 19 a 1 h</div>'
        '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px">' + ''.join(f'<div style="zoom:.5733">{p}</div>' for p in FEED9) + '</div></div></div>')
s_prof = f'{step(5, "Así queda <em>el perfil</em>")}{prof}'

# 8. Cierre
s_end = (f'<div class="spk">{SP}</div><h1 style="font-size:100px">¿Diseñamos el feed de <em>tu marca?</em></h1>'
         f'<div class="pill">Escribime por DM</div>')

slides = [
    ('n', cover, 'justify-content:center'),
    ('m', s_mood, 'gap:34px'),
    ('m', s_pal, 'gap:40px'),
    ('m', s_est, 'gap:40px'),
    ('n', s_dis, 'gap:34px'),
    ('m', s_big, 'gap:24px;padding-top:60px;padding-bottom:130px'),
    ('n', s_prof, 'gap:30px;padding-top:70px'),
    ('g', s_end, ''),
]
if __name__ == '__main__':
    print(render('carrusel-feed-hamburgueseria', slides, EXT))
