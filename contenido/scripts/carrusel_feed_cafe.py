"""Carrusel estilo proceso: 'Así diseñaría una marca de café' (marca de ejemplo Tostado), con fotos reales de Pexels de un mismo café."""
import sys, base64; sys.path.insert(0, '/home/user/gold-studio-contenido')
from caro_ejemplos import render
from carogen import SP, SCR, F

# Fotos de Pexels (licencia libre, sin atribución obligatoria): pexels.com/photo/<id>
def _img(i): return 'data:image/jpeg;base64,' + base64.b64encode(open(f'{SCR}/pexels/{i}.jpg', 'rb').read()).decode()
# Todas de la misma sesión (cottonbro studio): el mismo café, la misma barista y la misma luz, para que el feed tenga continuidad.
PX = {k: _img(i) for k, i in {
    'maquina': 4792683, 'barista': 4792684, 'jarra': 4792685, 'barra_taza': 4792686, 'vapor': 4792687,
    'latte_arte': 4792689, 'latte_arriba': 4792692, 'tamper': 4792693, 'local': 4792694, 'portafiltro': 4792695,
    'entrega': 4792696, 'mano_taza': 4792699, 'vertido': 4792700,
}.items()}
ESP, BOR, CRE, CAR, MAD, MAN, GRI = '#2A1A14', '#8A3B2A', '#EFE7DA', '#B4743F', '#6B4A33', '#E6CFA8', '#9A9C98'
import ilus_cafe as I

EXT = f'''
@font-face{{font-family:XPlayfair;src:url({F}playfair-display/files/playfair-display-latin-700-normal.woff2)}}
.ph{{background-size:cover;background-position:center;background-repeat:no-repeat}}
.step{{display:flex;align-items:baseline;gap:26px}}
.step .num{{font-size:120px}}
.step h2{{font-size:70px}}
.cap{{font-size:30px;color:var(--sub);line-height:1.4;font-weight:300}}
.cap b{{font-weight:500;color:var(--em)}}
.shadow{{box-shadow:0 40px 70px -40px rgba(28,26,23,.55)}}
.post{{width:300px;height:375px;position:relative;overflow:hidden;font-family:J}}
.post .t{{font-family:XPlayfair;line-height:1.1}}
.post .shade{{position:absolute;inset:0;background:linear-gradient(transparent 45%,rgba(30,18,12,.78))}}
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
tostado = lambda c, s=30: f'<span style="font-family:XPlayfair;font-size:{s}px;color:{c};letter-spacing:.01em">Tostado.</span>'
PLAY = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.6"><rect x="3" y="4" width="18" height="16" rx="4"/><path d="M10 9.5v5l4.2-2.5z" fill="#fff"/></svg>'

# ---- Posteos de Tostado (300×375, se escalan con zoom) ----
def p_reel():
    return (f'<div class="post ph" style="{ph("vapor", "40% center")}"><div class="shade"></div><div style="position:absolute;right:16px;top:16px">{PLAY}</div>'
            f'<div class="t" style="position:absolute;left:20px;right:20px;bottom:22px;color:#fff;font-size:30px">Así nace<br>tu espresso.</div></div>')
def p_frase():
    return (f'<div class="post" style="background:{CRE};display:flex;flex-direction:column;justify-content:center;padding:0 28px;box-sizing:border-box;gap:18px">'
            f'<div class="t" style="font-size:34px;color:{ESP}">Tu primer café del día merece ser <i style="color:{BOR}">especial.</i></div>'
            f'<div class="ph" style="height:120px;border-radius:999px 999px 0 0;{ph("latte_arriba", "center 45%")}"></div>{tostado(BOR, 22)}</div>')
def p_guia():
    cups = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;color:{CRE};font-size:17px"><div style="width:62px;height:62px;border-radius:50%;border:3px solid {CRE};background:linear-gradient({BOR} {100-p}%,{CAR} {100-p}%)"></div>{n}</div>' for n, p in [('Ristretto', 35), ('Espresso', 55), ('Lungo', 85)])
    return (f'<div class="post" style="background:{BOR};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px">'
            f'<div style="color:{MAN};font-size:16px;letter-spacing:.28em">GUÍA RÁPIDA</div><div class="t" style="color:{CRE};font-size:32px;text-align:center">¿Cuánta agua<br>lleva tu café?</div>'
            f'<div style="display:flex;gap:16px">{cups}</div></div>')
def p_reco():
    return (f'<div class="post ph" style="{ph("latte_arte", "center 60%")}"><div class="shade"></div>'
            f'<div style="position:absolute;left:16px;top:16px;background:{MAN};color:{ESP};font-size:14px;letter-spacing:.2em;padding:8px 14px;border-radius:999px">LA DE LA CASA</div>'
            f'<div class="t" style="position:absolute;left:20px;right:20px;bottom:22px;color:#fff;font-size:28px">Flat white<br><i style="color:{MAN}">con leche de almendras</i></div></div>')
def p_lugar():
    return (f'<div class="post ph" style="{ph("local", "center 40%")}"><div style="position:absolute;left:0;right:0;bottom:0;height:110px;background:{CRE};display:flex;flex-direction:column;justify-content:center;padding:0 20px">'
            f'<div class="t" style="font-size:26px;color:{ESP}">Tu lugar del barrio<br><i style="color:{BOR}">te está esperando.</i></div></div></div>')
def p_marca():
    return (f'<div class="post ph" style="{ph("tamper")}"><div style="position:absolute;inset:0;background:rgba(42,26,20,.7)"></div>'
            f'<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px">{tostado(CRE, 52)}'
            f'<span style="font-size:14px;letter-spacing:.3em;color:{MAN}">CAFÉ DE ESPECIALIDAD</span></div></div>')
def p_nada():
    taza = I.cup(250, ()).replace('</svg>', '<g transform="translate(110 108) scale(1.75) translate(-110 -104)">' + I.swimmer_ring(110, 104, BOR) + '</g></svg>')
    return (f'<div class="post" style="background:{MAN}"><div style="position:absolute;left:25px;top:28px">{taza}</div>'
            f'<div class="t" style="position:absolute;left:0;right:0;bottom:20px;text-align:center;font-size:30px;color:{BOR}">Nadá en <i>sabor.</i></div></div>')
def p_entrega():
    return (f'<div class="post ph" style="{ph("entrega", "center 40%")}"><div style="position:absolute;left:18px;top:18px;background:{CRE};padding:14px 18px">'
            f'<div class="t" style="font-size:24px;color:{ESP}">Para vos,<br><i style="color:{BOR}">recién hecho.</i></div></div></div>')
def p_barista():
    return (f'<div class="post ph" style="{ph("barista", "center 30%")}"><div class="shade"></div>'
            f'<div style="position:absolute;left:20px;right:20px;bottom:22px;color:#fff"><div style="font-size:14px;letter-spacing:.28em;color:{MAN}">DETRÁS DE LA BARRA</div>'
            f'<div class="t" style="font-size:28px;margin-top:6px">Conocé a Fran.</div></div></div>')
def p_vertido():
    return f'<div class="post ph" style="{ph("vertido", "center 40%")}"><div style="position:absolute;right:16px;top:16px">{PLAY}</div></div>'

FEED6 = [p_reel(), p_frase(), p_nada(), p_reco(), p_lugar(), p_marca()]
FEED9 = [p_entrega(), p_guia(), p_vertido()] + FEED6   # lo más nuevo arriba

def step(n, t): return f'<div class="step"><div class="num">{n}</div><h2>{t}</h2></div>'

# 1. Portada
fan = ''.join(f'<div class="ph shadow" style="position:absolute;width:300px;height:375px;border:12px solid #FAF6EE;{ph(k)};left:{x}px;top:{y}px;transform:rotate({r}deg)"></div>'
              for k, x, y, r in [('barista', 60, 40, -9), ('latte_arriba', 470, 50, 8), ('latte_arte', 250, 0, -1)])
cover = (f'<div class="eb">Proceso de branding</div>'
         f'<h1 style="font-size:104px">Así diseñaría <em>una marca de café</em></h1>'
         f'<div style="position:relative;height:440px;width:888px">{fan}</div>')

# 2. Moodboard
mood = (f'<div class="mood"><div class="ph" style="grid-row:span 2;{ph("latte_arte", "center 85%")}"></div><div class="ph" style="{ph("tamper")}"></div>'
        f'<div class="ph" style="{ph("local")}"></div><div class="ph" style="{ph("latte_arriba")}"></div><div class="ph" style="{ph("vapor", "40% center")}"></div></div>')
s_mood = (f'{step(1, "Buscamos el <em>clima</em>")}{mood}<div class="kw"><span>Cálida</span><span>Artesanal</span><span>Urbana</span></div>'
          f'<p class="cap" style="text-align:center;margin:0">Una sola barra, una barista, luz natural: el feed cuenta una historia.</p>')

# 3. Paleta sacada de las fotos
pal = '<div class="pal">' + ''.join(f'<div class="c"><div class="dot" style="background:{c}"><i style="{ph(k)}"></i></div>{c}</div>'
                                    for c, k in [(ESP, 'tamper'), (BOR, 'vapor'), (CAR, 'barista'), (GRI, 'latte_arriba'), (CRE, 'mano_taza')]) + '</div>'
tipo = (f'<div style="display:flex;gap:40px;align-items:center;justify-content:center;background:{CRE};border-radius:28px;padding:40px;width:888px;box-sizing:border-box;align-self:center">'
        f'<div style="text-align:center">{tostado(ESP, 92)}<div style="font-size:18px;letter-spacing:.3em;color:{MAD};margin-top:6px">CAFÉ DE ESPECIALIDAD</div></div>'
        f'<div style="font-size:24px;line-height:1.7;color:{MAD};border-left:2px solid {CAR};padding-left:36px">Títulos · <b>Playfair Display</b><br>Textos · <b>Jost</b></div></div>')
s_pal = (f'{step(2, "Paleta y <em>tipografías</em>")}<p class="cap" style="margin:0">Los colores salen de las mismas fotos: <b>espresso, ladrillo, cuero, cemento y crema.</b></p>{pal}{tipo}')

# 4. Estrategia
est = '<div class="est">' + ''.join(f'<div><div class="ph" style="{ph(k, pos)}"></div><b>{t}</b><span>{d}</span></div>' for k, pos, t, d in [
    ('vapor', '40% center', 'Reels', 'Preparación y momentos'), ('latte_arriba', 'center', 'Producto', 'En detalle, bien de cerca'),
    ('tamper', 'center', 'Educativo', 'Tipos de café, sin vueltas'), ('latte_arte', 'center 80%', 'Recomendación', 'La de la casa'),
    ('local', 'center', 'Experiencia', 'El local y su gente'), ('barista', 'center 30%', 'Marca', 'Ilustración y frases propias')]) + '</div>'
s_est = f'{step(3, "Estrategia y <em>contenidos</em>")}{est}'

# 5. Diseños
feed6 = '<div class="feed6">' + ''.join(FEED6) + '</div>'
s_dis = (f'{step(4, "Diseñamos <em>los posteos</em>")}{feed6}<p class="cap" style="margin:0;text-align:center">Fotos del mismo lugar + una ilustración propia que le da personalidad.</p>')

# 6. Un posteo de cerca, como se ve en Instagram
HEART = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#1C1A17" stroke-width="1.7"><path d="M12 20s-7-4.4-9-8.7C1.6 8.3 3.6 5 6.8 5c2 0 3.4 1.1 4.2 2.4h2C13.8 6.1 15.2 5 17.2 5c3.2 0 5.2 3.3 3.8 6.3-2 4.3-9 8.7-9 8.7z"/></svg>'
BUB = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#1C1A17" stroke-width="1.7"><path d="M20 11.5a8 8 0 0 1-11.6 7.1L4 20l1.4-4.2A8 8 0 1 1 20 11.5z"/></svg>'
SEND = '<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="#1C1A17" stroke-width="1.7"><path d="M21 3 3 10.5l7 3 3 7.5z M10 13.5 21 3"/></svg>'
big = (f'<div class="shadow" style="width:760px;align-self:center;background:#fff;border-radius:28px;overflow:hidden;color:#1C1A17">'
       f'<div style="display:flex;align-items:center;gap:14px;padding:16px 20px"><div style="width:48px;height:48px;border-radius:50%;background:{ESP};display:grid;place-items:center">{tostado(CRE, 11)}</div>'
       f'<b style="font-size:22px;font-weight:500">tostado.cafe</b><span style="margin-left:auto;font-size:28px;letter-spacing:2px">···</span></div>'
       f'<div class="ph" style="height:820px;position:relative;{ph("mano_taza", "center 70%")}"><div style="position:absolute;inset:0;background:linear-gradient(rgba(30,18,12,.5),transparent 45%)"></div>'
       f'<div style="position:absolute;left:44px;right:44px;top:44px;font-family:XPlayfair;font-size:64px;line-height:1.1;color:#fff">Tu primer café del día merece ser <i style="color:{MAN}">especial.</i></div>'
       f'<div style="position:absolute;right:30px;bottom:26px">{tostado("#fff", 30)}</div></div>'
       f'<div style="display:flex;gap:20px;padding:16px 20px">{HEART}{BUB}{SEND}</div></div>')
s_big = f'<div class="eb" style="text-align:center">De cerca</div>{big}<p class="cap" style="margin:0;text-align:center">La foto cuenta, la frase <b>engancha.</b></p>'

# 7. Perfil
prof = ('<div class="shadow" style="width:560px;border-radius:56px;background:#111;padding:14px;align-self:center"><div style="border-radius:44px;overflow:hidden;background:#fff;color:#1C1A17">'
        f'<div style="padding:26px 22px 10px;display:flex;gap:22px;align-items:center"><div style="width:96px;height:96px;border-radius:50%;background:{ESP};display:grid;place-items:center;flex:none">{tostado(CRE, 22)}</div>'
        '<div style="display:flex;gap:22px;font-size:16px;text-align:center">' + ''.join(f'<div><b style="display:block;font-size:26px;font-weight:500">{a}</b>{b}</div>' for a, b in [('48', 'posts'), ('2.380', 'seguidores'), ('210', 'seguidos')]) + '</div></div>'
        '<div style="padding:0 22px 14px;font-size:17px;line-height:1.45"><b style="font-weight:500">Tostado · Café de especialidad</b><br>Tu lugar favorito del barrio<br>Lun a sáb · 8 a 20 h</div>'
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
    print(render('carrusel-feed-cafeteria', slides, EXT))
