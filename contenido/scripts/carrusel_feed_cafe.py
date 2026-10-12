"""Carrusel estilo proceso: 'Diseñemos juntas el feed para una cafetería' (marca de ejemplo Tostado)."""
import sys, base64; sys.path.insert(0, '/home/user/gold-studio-contenido')
from caro_ejemplos import render, end
from carogen import SP, F
import ilus_cafe as I
P = '/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad/pyimg/coffee.png'
PHOTO = 'data:image/png;base64,' + base64.b64encode(open(P, 'rb').read()).decode()
LOGO = 'data:image/svg+xml;base64,' + base64.b64encode(open('/home/user/gold-studio-final/logo-gold-studio-transparente-blanco.svg', 'rb').read()).decode()
ESP, BOR, CRE, CAR, MAD, MAN = '#2A1A14', '#6E1E17', '#EFE4D6', '#C98A5A', '#7A4A2E', '#F2D3A0'
EXT = f'''
@font-face{{font-family:XPlayfair;src:url({F}playfair-display/files/playfair-display-latin-700-normal.woff2)}}
@font-face{{font-family:XArchivo;src:url({F}archivo-black/files/archivo-black-latin-400-normal.woff2)}}
.cf{{background:#1A1210;color:#FAF6EE}}
.cf .foot{{display:none}}
.bgp{{position:absolute;inset:0;background:radial-gradient(circle at 20% 15%,#6E3A24 0,transparent 45%),radial-gradient(circle at 85% 80%,#5A2A1C 0,transparent 50%),radial-gradient(circle at 70% 30%,#3A2018 0,transparent 40%),#24160F;z-index:0}}
.cf>*:not(.bgp){{position:relative;z-index:1}}
.topl{{position:absolute!important;left:96px;right:96px;top:70px;display:flex;justify-content:space-between;align-items:center;font-size:30px;padding-bottom:22px;border-bottom:2px solid rgba(250,246,238,.8)}}
.botl{{position:absolute!important;left:96px;right:96px;bottom:60px;display:flex;justify-content:center;padding-top:26px;border-top:2px solid rgba(250,246,238,.8)}}
.botl img{{height:96px}}
.stept{{font-size:40px;text-align:center}}
.stept b{{font-style:italic;font-weight:500}}
.tabs{{display:flex;justify-content:space-around;width:700px;align-self:center;color:#FAF6EE;opacity:.9}}
.g3{{display:grid;grid-template-columns:repeat(3,220px);grid-auto-rows:280px;gap:14px;align-self:center}}
.g3>div{{overflow:hidden;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
'''
ico = {'grid': '<path d="M4 4h16v16H4zM4 9.3h16M4 14.6h16M9.3 4v16M14.6 4v16"/>',
       'reel': '<rect x="3" y="4" width="18" height="16" rx="4"/><path d="M3 9h18M8 4l3 5M13 4l3 5M10 12.5v4.5l4-2.2z"/>',
       'tag': '<rect x="4" y="4" width="16" height="16" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M7 18c1-3 3-4 5-4s4 1 5 4M10 4l2 -2 2 2"/>'}
tabs = '<div class="tabs">' + ''.join(f'<svg width="54" height="54" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linejoin="round">{ico[k]}</svg>' for k in ['grid', 'reel', 'tag']) + '</div>'
frame = lambda n: (f'<div class="bgp"></div><div class="topl"><span>Versión Gold Studio.</span><span style="font-size:36px">→</span></div>'
                   f'<div class="botl"><img src="{LOGO}"></div>')
def slide(inner, n): return ('cf', frame(n) + inner, 'justify-content:center;gap:34px;padding-top:150px;padding-bottom:200px')
ph = lambda pos='center', zoom=180, extra='': f'<div style="position:absolute;inset:0;background:url({PHOTO}) {pos}/{zoom}% no-repeat;{extra}"></div>'
tostado = lambda c, s=30: f'<span style="font-family:B;font-size:{s}px;color:{c};letter-spacing:.02em">Tostado.</span>'

# 1. Paleta y tipografías
sw = '<div class="g3">' + ''.join(f'<div style="background:{c}"><span style="position:absolute;left:14px;bottom:12px;font-size:18px;color:{t};letter-spacing:.08em">{h}</span></div>' for c, t, h in [(ESP, '#C9B8A8', '#2A1A14'), (BOR, '#E9C3BB', '#6E1E17'), (CRE, '#7A4A2E', '#EFE4D6'), (MAD, '#F2D3A0', '#7A4A2E'), (CAR, '#2A1A14', '#C98A5A'), (MAN, '#7A4A2E', '#F2D3A0')]) + '</div>'
fonts = (f'<div style="display:flex;justify-content:center;gap:60px;align-items:baseline"><span style="font-family:XPlayfair;font-size:84px">Aa</span>'
         f'<span style="font-family:J;font-size:30px;letter-spacing:.3em;opacity:.85">TÍTULOS · PLAYFAIR<br>TEXTOS · JOST</span></div>')
# 2. Estrategia
est = '<div class="g3">' + ''.join(f'<div style="background:{c};color:{t};font-size:28px;line-height:1.2;padding:16px">{x}</div>' for c, t, x in [
    (ESP, CRE, 'Reel:<br>preparación<br>y momentos.'), (BOR, CRE, 'Producto<br>en detalle.'), (CRE, ESP, 'Educativo:<br>tipos de café.'),
    (MAD, CRE, 'Recomendación<br>de la casa.'), (CAR, ESP, 'Experiencia<br>en el local.'), (MAN, MAD, 'Refuerzo<br>de marca.')]) + '</div>'
# 3. Diseños
posts = [
  f'<div style="background:{CRE};position:absolute;inset:0"></div><div style="position:relative;margin-top:-24px">{I.cup(210, ("cookie", "ring2", "ring", "glasses"))}</div><div style="position:absolute;bottom:12px">{tostado(ESP, 24)}</div>',
  f'<div style="background:{CRE};position:absolute;inset:0"></div><div style="position:relative;font-family:XPlayfair;font-size:30px;color:{ESP};line-height:1.15;padding:0 18px">Tu primer café<br>del día merece ser<br><i style="color:{BOR}">especial.</i></div><div style="position:absolute;bottom:12px">{tostado(BOR, 20)}</div>',
  f'<div style="background:{BOR};position:absolute;inset:0"></div><div style="position:relative;color:{CRE};font-size:18px;letter-spacing:.2em">GUÍA RÁPIDA</div><div style="position:relative;display:flex;gap:16px;margin-top:14px">'
  + ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;color:{CRE};font-size:17px"><div style="width:62px;height:62px;border-radius:50%;border:3px solid {CRE};background:linear-gradient({CRE} {100-p}%,{CAR} {100-p}%)"></div>{n}</div>' for n, p in [('Ristretto', 35), ('Espresso', 55), ('Lungo', 85)]) + '</div>',
  f'<div style="background:{MAN};position:absolute;inset:0"></div><div style="position:relative;margin-top:-30px">{I.rim_sitter(200)}</div><div style="position:absolute;left:14px;right:14px;bottom:14px;color:{ESP};font-family:XPlayfair;font-size:22px">Recomendación:<br><i style="color:{BOR}">cortado</i></div>',
  f'<div style="background:{BOR};position:absolute;inset:0"></div><div style="position:relative;margin-top:-20px">{I.cup(190, ("ring",), saucer=False)}</div><div style="position:relative;font-family:XPlayfair;font-size:24px;color:{CRE};margin-top:-6px">Vení a tu<br><i>lugar favorito</i></div>',
  f'<div style="background:{ESP};position:absolute;inset:0"></div><div style="position:relative;display:flex;flex-direction:column;align-items:center;gap:8px">'
  f'<svg width="70" height="90" viewBox="0 0 70 90"><ellipse cx="35" cy="45" rx="26" ry="40" fill="{CAR}"/><path d="M35 8 C22 30 48 60 35 82" stroke="{ESP}" stroke-width="5" fill="none"/></svg>{tostado(CRE, 44)}<span style="font-size:14px;letter-spacing:.3em;color:{MAN}">CAFÉ DE ESPECIALIDAD</span></div>',
]
dis = '<div class="g3">' + ''.join(f'<div>{p}</div>' for p in posts) + '</div>'
# 4. Post destacado (taza con la foto adentro)
cup_clip = 'clip-path:polygon(14% 0,86% 0,76% 100%,24% 100%)'
big = (f'<div style="position:relative;width:888px;height:900px;align-self:center;background:{CRE};overflow:hidden">'
       f'<div style="position:absolute;left:40px;right:40px;top:44px;display:flex;justify-content:space-between;font-family:XArchivo;font-size:58px;color:{BOR}"><span>TOSTADO</span><span>CAFÉ</span></div>'
       f'<div style="position:absolute;left:94px;top:120px">{I.cup(700, ("cookie", "ring2", "ring", "glasses"))}</div>'
       f'<div style="position:absolute;left:0;right:0;bottom:40px;text-align:center;font-family:XArchivo;font-size:52px;color:{BOR}">NADÁ EN SABOR</div></div>')
# 5. Perfil completo
grid9 = posts + [posts[1].replace(CRE, MAN).replace('Tu primer café<br>del día merece ser<br>', 'Lunes de<br>').replace('especial.', 'medialunas.'), posts[0].replace(CRE, MAN), posts[2].replace(BOR, MAD)]
prof = ('<div style="width:440px;border-radius:48px;background:#111;padding:12px;align-self:center;box-shadow:0 40px 70px -30px rgba(0,0,0,.8)"><div style="border-radius:44px;overflow:hidden;background:#fff;color:#1C1A17;font-family:J">'
        f'<div style="padding:20px 18px 8px;display:flex;gap:16px;align-items:center"><div style="width:80px;height:80px;border-radius:50%;background:{ESP};display:grid;place-items:center">{tostado(CRE, 19)}</div>'
        '<div style="display:flex;gap:14px;font-size:14px;text-align:center">' + ''.join(f'<div><b style="display:block;font-size:22px">{a}</b>{b}</div>' for a, b in [('48', 'posts'), ('2.380', 'seguidores'), ('210', 'seguidos')]) + '</div></div>'
        '<div style="padding:0 18px 10px;font-size:14px;line-height:1.4"><b>Tostado · Café de especialidad</b><br>Tu lugar favorito del barrio<br>Lun a sáb · 8 a 20 h</div>'
        '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:3px">' + ''.join(f'<div style="aspect-ratio:4/5;position:relative;overflow:hidden;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;zoom:.6">{p}</div>' for p in grid9) + '</div></div></div>')

slides = [
 ('cf', frame(0) + f'<div style="text-align:center;display:flex;flex-direction:column;align-items:center;gap:10px"><div style="font-family:J;font-size:76px;font-weight:400">Diseñemos juntas</div>'
  f'<div style="font-family:B;font-style:italic;font-size:150px;line-height:1;white-space:nowrap">el feed para</div><div style="background:#FAF6EE;color:#1C1A17;border-radius:999px;padding:8px 60px;font-size:54px;margin-top:-10px">una cafetería.</div></div>', 'justify-content:center'),
 slide(f'<div class="stept">1. Definimos <b>paleta de colores y tipografías</b></div>{tabs}{sw}{fonts}', 1),
 slide(f'<div class="stept">2. Definimos <b>estrategia y contenidos</b></div>{tabs}{est}', 2),
 slide(f'<div class="stept">3. Diseñamos <b>y presentamos</b></div>{tabs}{dis}', 3),
 ('cf', f'<div class="bgp"></div>{big}<div style="text-align:center;font-size:28px;opacity:.85">Un posteo de marca, con su ilustración</div>', 'justify-content:center;gap:24px'),
 slide(f'<div class="stept">4. Así queda <b>el perfil</b></div>{prof}', 5),
 ('cf', frame(6) + '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:30px"><div style="width:110px;height:110px;color:#C9A34E">' + SP + '</div><h1 style="font-size:104px">¿Diseñamos el feed de <em style="color:#C9A34E">tu marca?</em></h1><div class="pill" style="align-self:center;background:#FAF6EE;color:#1C1A17">Escribime · Tostado es una marca de ejemplo</div></div>', 'justify-content:center'),
]
if __name__ == '__main__':
    print(render('carrusel-feed-cafeteria', slides, EXT))
