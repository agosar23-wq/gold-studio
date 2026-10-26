"""Posteo informativo de Sunekos Performa (1290x1290), con el mismo diseño que la pieza de Profhilo del consultorio."""
import sys, os, subprocess, base64; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import SCR, F

FOTO = SCR + '/sunekos/foto.jpg'      # foto del consultorio (producto sobre mármol)
OUT = '/home/user/gold-studio-final/consultorio/sunekos-performa.png'
B64 = lambda p: 'data:image/jpeg;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

G, INK, TX, IV, LN = '#3A9FD8', '#3A2E28', '#6B5E55', '#F6F1EA', '#E4D8C6'   # como la pieza de Profhilo, con celeste (de la caja) en vez de dorado
NAVY = '#1F3A6B'
PNG64 = lambda p: 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()
LOGO = SCR + '/sunekos/logo_taupe.png'     # logo real del consultorio, en su color
PACK = SCR + '/sunekos/pack_final.png'     # producto recortado
PARED = SCR + '/sunekos/bg/4207776.jpg'    # pared beige con sombra de hojas (Pexels)
ESCENA = SCR + '/sunekos/escena.png'      # foto del producto sobre mármol (la que mandó Agos)
MONO = (f'<svg width="96" height="140" viewBox="0 0 96 140" fill="none" stroke="#8F857C" stroke-width="2.4">'
        '<path d="M8 62 V48 a40 40 0 0 1 80 0 V62 M8 78 V92 a40 40 0 0 0 80 0 V78"/>'
        '<text x="40" y="100" font-family="J" font-weight="300" font-size="62" fill="none" stroke="#8F857C" stroke-width="1.6" text-anchor="middle">S</text>'
        '<text x="58" y="88" font-family="J" font-weight="300" font-size="50" fill="none" stroke="#8F857C" stroke-width="1.6" text-anchor="middle">C</text></svg>')
def icon(kind):
    s = {  # íconos de línea fina, dibujados en una grilla de 64
     'mol': '<circle cx="32" cy="32" r="7"/><circle cx="14" cy="18" r="5"/><circle cx="50" cy="18" r="5"/><circle cx="14" cy="46" r="5"/><circle cx="50" cy="46" r="5"/>'
            '<path d="M18.3 20.6 L26.2 27.8 M45.7 20.6 L37.8 27.8 M18.3 43.4 L26.2 36.2 M45.7 43.4 L37.8 36.2"/>',
     'spark': '<path d="M30 12 C31.6 25 35 28.4 48 30 C35 31.6 31.6 35 30 48 C28.4 35 25 31.6 12 30 C25 28.4 28.4 25 30 12Z"/>'
              '<path d="M48 40 C48.6 45 50 46.4 55 47 C50 47.6 48.6 49 48 54 C47.4 49 46 47.6 41 47 C46 46.4 47.4 45 48 40Z"/>',
     'drop': '<path d="M32 9 C25 19 17 28 17 38 a15 15 0 0 0 30 0 C47 28 39 19 32 9Z"/><path d="M25 39 a8 8 0 0 0 6 7"/>',
     'line': '<path d="M12 50 H52"/><path d="M14 42 C22 42 24 30 31 30 S40 36 47 20"/><path d="M41 19 L47.5 18.5 L48.5 25"/>',
     'face': '<path d="M30 11 C19 11 13 20 13 31 C13 43 21 53 30 53 C39 53 47 43 47 31 C47 20 41 11 30 11Z"/>'
             '<path d="M21 30 q3.5 3 7 0 M32 30 q3.5 3 7 0"/><path d="M25 41 q5 4 10 0"/>'
             '<path d="M52 9 C52.5 13 53.5 14 57 14.5 C53.5 15 52.5 16 52 20 C51.5 16 50.5 15 47 14.5 C50.5 14 51.5 13 52 9Z"/>'}[kind]
    return (f'<div class="ic"><svg viewBox="0 0 64 64" width="62" height="62" fill="none" stroke="currentColor" stroke-width="2.3" '
            f'stroke-linecap="round" stroke-linejoin="round">{s}</svg></div>')
STAR = f'<svg width="22" height="22" viewBox="0 0 100 100"><path d="M50 0 C54.5 40 60 45.5 100 50 C60 54.5 54.5 60 50 100 C45.5 60 40 54.5 0 50 C40 45.5 45.5 40 50 0Z" fill="{G}"/></svg>'
ORN = f'<div class="orn"><i></i>{STAR}<i></i></div>'

ITEMS = [('mol', 'Ácido hialurónico + aminoácidos', 'Fórmula patentada que le da a la piel los nutrientes que necesita para regenerarse.'),
         ('spark', 'Estimula colágeno y elastina', 'Activa la producción natural de la piel para recuperar firmeza y elasticidad.'),
         ('drop', 'Hidratación y luminosidad', 'Mejora la textura, suaviza las líneas finas y devuelve la luz a la piel.'),
         ('line', 'Resultados naturales', 'Sin cambiar tus rasgos: la piel se ve mejor sesión a sesión.')]

def html():
    items = ''.join(f'<div class="it">{icon(k)}<div><b>{t}</b><span>{d}</span></div></div>' for k, t, d in ITEMS)
    return f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-300-normal.woff2);font-weight:300}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2);font-weight:500}}
body{{margin:0;background:#EFE8DE}}
.p{{width:1290px;height:1290px;background:#EFE8DE;position:relative;font-family:J;color:{INK};box-sizing:border-box;padding:14px;display:flex;gap:14px}}
.l{{width:528px;background:{IV};border:1.5px solid {LN};border-radius:26px;padding:36px 46px 34px;box-sizing:border-box;display:flex;flex-direction:column;align-items:center}}
.brand{{font-family:J;font-weight:500;font-size:64px;letter-spacing:.06em;line-height:1;margin-top:14px;color:{INK}}}
.brand sup{{font-size:20px;vertical-align:top;margin-left:2px}}
.perf{{font-size:24px;letter-spacing:.62em;padding-left:.62em;color:{G};font-weight:500;margin-top:10px}}
.orn{{display:flex;align-items:center;gap:12px;width:100%;margin:20px 0 18px}} .orn i{{flex:1;height:1px;background:{LN}}}
.lead{{text-align:center;font-size:22px;letter-spacing:.06em;line-height:1.45;text-transform:uppercase;font-weight:500;color:{INK}}}
.lead em{{font-style:normal;color:{G}}}
.its{{display:flex;flex-direction:column;gap:22px;width:100%;margin-top:6px}}
.it{{display:flex;gap:22px;align-items:center}}
.ic{{width:92px;height:92px;border-radius:50%;color:#2E8FCB;display:grid;place-items:center;flex:none;position:relative;background:radial-gradient(circle at 35% 30%,#FFFFFF,#E7F3FB 70%);box-shadow:0 0 0 1.5px rgba(58,159,216,.55),0 0 0 7px #F6F1EA,0 0 0 8px rgba(58,159,216,.18),0 10px 18px -10px rgba(46,143,203,.45)}}
.it b{{display:block;font-size:19px;letter-spacing:.06em;text-transform:uppercase;color:{G};font-weight:500;margin-bottom:5px}}
.it span{{display:block;font-size:18.5px;line-height:1.42;color:{TX}}}
.box{{margin-top:auto;width:100%;border:1.5px solid {LN};border-radius:18px;padding:16px 22px;display:flex;gap:20px;align-items:center;box-sizing:border-box;background:#FBF8F3}}
.mono{{width:92px;margin-top:4px}}
.brand sup{{color:{G}}}
.box .ic{{width:74px;height:74px;box-shadow:0 0 0 1.5px rgba(58,159,216,.55),0 0 0 6px #FBF8F3,0 0 0 7px rgba(58,159,216,.18)}} .box .ic svg{{width:50px;height:50px}}
.r{{flex:1;border-radius:26px;overflow:hidden;position:relative}}
.ph{{position:absolute;inset:0;background:url({B64(PARED)}) 50% 30%/cover;filter:sepia(.25) saturate(.85) brightness(1.22) contrast(.82)}}
.floor{{position:absolute;left:0;right:0;bottom:0;height:300px;background:linear-gradient(#E3D7C7,#D8CAB8);box-shadow:0 -1px 0 rgba(255,255,255,.4)}}
.floor::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 70% 60% at 30% 0%,rgba(255,255,255,.35),rgba(255,255,255,0))}}
.ped{{position:absolute;left:50%;transform:translateX(-50%);bottom:130px;width:660px;height:270px}}
.ped .side{{position:absolute;left:0;right:0;top:62px;bottom:0;border-radius:0 0 330px 330px/0 0 60px 60px;background:linear-gradient(90deg,#C9BBA8,#E9E0D3 30%,#F2EBE1 48%,#DCD0C0 75%,#BFB09C)}}
.ped .top{{position:absolute;left:0;right:0;top:0;height:124px;border-radius:50%;background:radial-gradient(ellipse at 45% 40%,#F7F2EA,#E8DFD2 70%,#DCD1C2)}}
.ped .tex{{position:absolute;inset:0;background:url(grain.png);opacity:.18;mix-blend-mode:multiply;border-radius:0 0 330px 330px/0 0 60px 60px;top:62px}}
.pshadow{{position:absolute;left:50%;bottom:100px;width:760px;height:80px;transform:translateX(-50%);border-radius:50%;background:rgba(80,60,40,.35);filter:blur(22px)}}
.prod{{position:absolute;left:50%;bottom:322px;width:470px;transform:translateX(-50%)}}
.prod img{{width:100%;display:block;position:relative;filter:drop-shadow(-24px 18px 26px rgba(70,50,30,.28))}}
.cs{{position:absolute;border-radius:50%;background:rgba(40,28,18,.55);filter:blur(9px)}}
.eb2{{position:absolute;inset:0;background:radial-gradient(ellipse 80% 45% at 70% 8%,rgba(255,244,226,.55),rgba(255,244,226,0)),linear-gradient(#E6D6BE,#D9C5A8 30%,#CEB897 38%)}}
.shot{{position:absolute;bottom:0;left:-163px;height:800px;-webkit-mask-image:linear-gradient(transparent 0%,#000 16%);mask-image:linear-gradient(transparent 0%,#000 16%)}}
.veil{{position:absolute;inset:0;background:linear-gradient(rgba(250,245,238,.45),rgba(250,245,238,0) 40%)}}
.tag{{position:absolute;top:118px;left:0;right:0;text-align:center;font-size:31px;letter-spacing:.2em;line-height:1.55;color:#4A3C34;font-weight:400}}
.tag .orn i{{background:#B9A88F}}
.tag .orn{{width:180px;margin:18px auto 0}}
</style><div class="p">
<div class="l"><img class="mono" src="{PNG64(LOGO)}"><div class="brand">SUNEKOS<sup>®</sup></div><div class="perf">PERFORMA</div>{ORN}
<div class="lead">Regeneración de la piel para<br>un rostro más firme,<br><em>elástico y luminoso.</em></div>{ORN}
<div class="its">{items}</div>
<div class="box">{icon('face')}<div><b style="display:block;font-size:19px;letter-spacing:.06em;color:{G};font-weight:500;margin-bottom:4px">NO ES UN RELLENO</b>
<span style="font-size:18px;line-height:1.4;color:{TX}">Mejora la calidad de la piel sin agregar volumen. Rostro, cuello y escote.</span></div></div>
</div>
<div class="r"><div class="eb2"></div><img class="shot" src="{PNG64(ESCENA)}"><div class="veil"></div><div class="tag">CIENCIA QUE REGENERA<br>TU PIEL{ORN}</div></div>
</div>'''

def render():
    work = SCR + '/sunekos'; open(work + '/p.html', 'w').write(html()); os.makedirs(os.path.dirname(OUT), exist_ok=True)
    js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1290,height:1290}}}});
    await p.goto('file://{work}/p.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(400);
    await (await p.$('.p')).screenshot({{path:'{OUT}'}});await b.close();}})();'''
    open(work + '/r.js', 'w').write(js)
    subprocess.run(['node', work + '/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    print(OUT)

if __name__ == '__main__':
    render()
