"""Carrusel "¿Logo o branding?" (1080x1350) con 4 marcas inventadas y mockups reales."""
import sys, os, subprocess; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR
from marcas_ejemplo import LOGOS, BRANDS, FONTS
from mockups_marcas import OUT as MK, SRC

NAME = 'logo-o-branding'
OUTDIR = f'/home/user/gold-studio-final/carruseles/{NAME}'
mk = lambda n: f'file://{MK}{n}.jpg'
lg = lambda n: f'file://{LOGOS}/{n}.png'
src = lambda n: f'file://{SRC}{n}.jpg'
col = lambda b, i: BRANDS[b]['colores'][i][1]

EXT = FONTS + '''
.s{padding:0;gap:0;justify-content:flex-start}
.pad{position:absolute;inset:0;padding:100px 96px 150px;display:flex;flex-direction:column;gap:34px;box-sizing:border-box}
.ph{position:relative;overflow:hidden}
.ph>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}
.hero{position:absolute;left:0;top:0;right:0;height:640px}
.hero .lg{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;z-index:2}
.duo{position:absolute;left:0;right:0;top:648px;height:620px;display:flex;gap:8px}
.duo .ph{flex:1}
.strip{position:absolute;left:0;right:0;bottom:0;height:82px;background:#FAF6EE;color:#1C1A17;display:flex;align-items:center;justify-content:space-between;padding:0 48px;font-size:23px;letter-spacing:.1em}
.strip b{font-family:B;font-weight:500;font-size:30px;letter-spacing:0}
.strip .r{color:#8A6A22;font-weight:500}
.mos{display:grid;grid-template-columns:1fr 1fr;gap:14px;flex:1;min-height:0}
.mos .ph{border-radius:20px}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:28px;flex:1;min-height:0}
.cmp>div{background:var(--box);border-radius:28px;padding:34px;display:flex;flex-direction:column;gap:18px}
.cmp h3{font-family:B;font-weight:500;font-size:52px;margin:0}
.cmp h3 em{font-style:italic;color:var(--em)}
.cmp p{margin:0;font-size:27px;line-height:1.4;color:var(--sub)}
.cmp .v{flex:1;border-radius:18px;background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative;min-height:0}
.sheet{background:#fff;border-radius:10px;flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:auto auto 1fr;gap:0;overflow:hidden;box-shadow:0 40px 80px -40px rgba(0,0,0,.6)}
.sheet>div{padding:28px 30px;display:flex;flex-direction:column;gap:14px;border-bottom:1px solid #EFE6DD}
.sheet .t{font-size:17px;letter-spacing:.32em;font-weight:500;color:#5B3F37}
.sheet p{margin:0;font-size:18px;line-height:1.45;color:#7A6A63}
.swc{display:flex;gap:10px}
.swc div{flex:1;height:120px;border-radius:10px;display:flex;align-items:flex-end;padding:10px;font-size:14px;box-sizing:border-box}
'''

def foot(i, n, dark=False):
    right = '<span class="sw">Deslizá →</span>' if i == 1 else f'<span>{i}/{n}</span>'
    return f'<div class="foot"><span>@goldstudio.ba</span>{right}</div>'

def strip(b, i, n):
    d = BRANDS[b]
    return f'<div class="strip"><span><b>{d["nombre"]}</b> &nbsp;·&nbsp; {d["rubro"]}</span><span class="r">{i}/{n}</span></div>'

def img(u, pos='50% 50%', extra=''):
    return f'<img src="{u}" style="object-position:{pos};{extra}">'

# ---------- láminas ----------
def portada():
    tiles = ''.join(f'<div class="ph">{img(mk(n), p)}</div>' for n, p in
                    [('almendra-bolsa', '50% 55%'), ('ondina-etiqueta', '50% 50%'), ('nube-caja', '50% 50%'), ('nacar-bolsas', '60% 50%')])
    return ('n', f'<div class="pad"><div class="eb">Guardalo</div><h1 style="font-size:112px">¿Logo o <em>branding</em>?</h1>'
                 '<p class="body" style="margin:0;font-size:38px">Parecen lo mismo, pero no. Te lo muestro con 4 marcas.</p>'
                 f'<div class="mos">{tiles}</div></div>')

def diferencia():
    logo_v = f'<img src="{lg("almendra-word-dark")}" style="width:86%">'
    brand_v = (f'<div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:6px;background:#fff">'
               f'<div class="ph">{img(mk("almendra-bolsa"), "50% 55%")}</div>'
               f'<div style="background:{col("almendra", 0)};display:flex;align-items:center;justify-content:center"><img src="{lg("almendra-iso-light")}" style="width:62%"></div>'
               f'<div style="display:flex;flex-direction:column">' + ''.join(f'<div style="flex:1;background:{c}"></div>' for _, c in BRANDS['almendra']['colores']) + '</div>'
               f'<div class="ph">{img(mk("almendra-vaso"), "50% 45%")}</div></div>')
    return ('m', '<div class="pad"><div class="eb">La diferencia</div><h1 style="font-size:92px">No es lo <em>mismo</em></h1>'
                 '<div class="cmp">'
                 f'<div><h3>El <em>logo</em></h3><p>Es tu firma. Lo que te identifica de un vistazo.</p><div class="v">{logo_v}</div></div>'
                 f'<div><h3>El <em>branding</em></h3><p>Es todo el sistema: colores, letras, packaging y redes.</p><div class="v">{brand_v}</div></div>'
                 '</div><p class="body" style="margin:0;font-size:32px">El logo es una parte. El branding hace que te reconozcan <i>siempre</i>.</p></div>')

def marca(b, hero, a, c):
    return ('n', f'<div class="hero ph">{hero}</div>'
                 f'<div class="duo"><div class="ph">{img(mk(a[0]), a[1])}</div><div class="ph">{img(mk(c[0]), c[1])}</div></div>', b)

HEROS = {
 'almendra': f'{img(src("30403209"), "50% 60%")}<div style="position:absolute;inset:0;background:rgba(74,38,34,.62)"></div><div class="lg"><img src="{lg("almendra-full-light")}" style="width:520px"></div>',
 'ondina': f'{img(src("8774406"), "50% 40%")}<div style="position:absolute;inset:0;background:radial-gradient(ellipse 62% 55% at 50% 50%,rgba(247,243,234,.78),rgba(247,243,234,.15))"></div><div class="lg"><img src="{lg("ondina-full-dark")}" style="width:600px"></div>',
 'nacar': f'{img(src("7795646"), "50% 45%")}<div style="position:absolute;inset:0;background:rgba(91,63,55,.55)"></div><div class="lg"><img src="{lg("nacar-full-light")}" style="width:480px"></div>',
 'nube': (f'<div style="position:absolute;left:0;top:0;bottom:0;width:56%;background:{col("nube", 2)};display:flex;align-items:center;justify-content:center"><img src="{lg("nube-full-dark")}" style="width:430px"></div>'
          f'<div class="ph" style="position:absolute;right:0;top:0;bottom:0;width:44%">{img(src("1294943"), "50% 50%", "transform:scale(1.5);transform-origin:50% 40%")}</div>'),
}

def aplicaciones():
    tiles = ''.join(f'<div class="ph">{img(mk(n), p)}</div>' for n, p in
                    [('almendra-vaso', '50% 45%'), ('ondina-tote-negra', '50% 60%'), ('nacar-tarjetas', '50% 50%'), ('nube-caja', '50% 50%')])
    return ('m', '<div class="pad"><div class="eb">El branding se ve en todo</div><h1 style="font-size:84px">Misma marca, <em>en cada lugar</em></h1>'
                 f'<div class="mos">{tiles}</div></div>')

def manual():
    C = BRANDS['nacar']['colores']
    sw = ''.join(f'<div style="background:{c};color:{"#fff" if i in (0, 1) else "#5B3F37"}">{n}<br>{c}</div>' for i, (n, c) in enumerate(C))
    mono = ''.join(f'<div style="flex:1;background:{bg};display:flex;align-items:center;justify-content:center;height:130px"><img src="{lg("nacar-word-" + v)}" style="width:72%"></div>'
                   for bg, v in [('#1C1A17', 'light'), ('#FFFFFF', 'dark'), (C[1][1], 'light'), (C[2][1], 'dark')])
    return ('n', f'<div class="pad" style="background:{C[0][1]};gap:28px"><div class="eb" style="color:#E9D3C9">Así se entrega</div><h1 style="font-size:96px">Manual de <em style="color:#E9C2B4">marca</em></h1>'
                 '<div class="sheet">'
                 f'<div style="background:{C[2][1]}"><span class="t">LOGOTIPO</span><div style="flex:1;display:flex;align-items:center;justify-content:center;padding:18px 0"><img src="{lg("nacar-full-dark")}" style="width:78%"></div><p>Versión principal. Se usa en todo lo que lleva la marca.</p></div>'
                 f'<div><span class="t">ISOTIPO</span><div style="flex:1;display:flex;align-items:center;justify-content:center;padding:18px 0"><img src="{lg("nacar-iso-accent")}" style="width:46%"></div><p>Para la foto de perfil, sellos y espacios chicos.</p></div>'
                 f'<div><span class="t">COLORES</span><div class="swc">{sw}</div></div>'
                 '<div><span class="t">TIPOGRAFÍAS</span><div style="display:flex;gap:30px;align-items:flex-end;color:#5B3F37">'
                 '<div><div style="font-family:B;font-size:96px;line-height:1">Aa</div><p>Bodoni Moda · títulos</p></div>'
                 '<div><div style="font-family:J;font-size:84px;line-height:1">Aa</div><p>Jost · textos</p></div></div></div>'
                 f'<div style="grid-column:span 2;border:none"><span class="t">MONOCROMÍA Y FONDOS</span><div style="display:flex;gap:10px">{mono}</div>'
                 '</div>'
                 '</div></div>')

def final():
    return ('n', f'<div class="pad" style="justify-content:center"><div class="spk">{SP}</div><h1 style="font-size:100px">¿Querés una marca <em>así de completa</em>?</h1>'
                 '<p class="body" style="margin:0">Logo, colores, tipografías, packaging y todo lo que necesites para tus redes.</p>'
                 '<div class="pill">Escribime y lo charlamos</div></div>')

def slides():
    return [portada(), diferencia(),
            marca('almendra', HEROS['almendra'], ('almendra-bolsa', '50% 52%'), ('almendra-paquete', '50% 50%')),
            marca('ondina', HEROS['ondina'], ('ondina-etiqueta', '45% 50%'), ('ondina-tote', '50% 50%')),
            marca('nacar', HEROS['nacar'], ('nacar-bolsa', '50% 50%'), ('nacar-frascos', '50% 50%')),
            marca('nube', HEROS['nube'], ('nube-vasos', '50% 50%'), ('nube-paquetes', '50% 50%')),
            aplicaciones(), manual(), final()]

CAPTION = '''¿Logo o branding? Parecen lo mismo, pero no.

El logo es tu firma: lo que te identifica de un vistazo.
El branding es todo lo que hay alrededor: colores, tipografías, packaging, papelería y redes. Es lo que hace que te reconozcan aunque no veas el nombre.

Te lo muestro con 4 marcas: Almendra, Ondina, Nácar y Nube.

¿Cuál te gustó más? Contame en los comentarios.
Y si querés una marca así para tu emprendimiento, escribime.

#branding #emprendedoras #diseñodemarca'''

def render():
    S = slides(); N = len(S); parts = []
    for i, s in enumerate(S, 1):
        bg, inner = s[0], s[1]
        tail = strip(s[2], i, N) if len(s) > 2 else foot(i, N)
        parts.append(f'<div class="s {bg}">{inner}{tail}</div>')
    page = f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXT}</style>' + ''.join(parts)
    work = f'{SCR}/cb-{NAME}'; os.makedirs(work, exist_ok=True); open(f'{work}/c.html', 'w').write(page)
    os.makedirs(OUTDIR, exist_ok=True)
    for f in os.listdir(OUTDIR): os.remove(os.path.join(OUTDIR, f))
    js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1350}}}});
    await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;
    await Promise.all([...document.images].map(i=>i.complete?0:new Promise(r=>{{i.onload=i.onerror=r}})));}});await p.waitForTimeout(500);
    const els=await p.$$('.s');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{OUTDIR}/'+String(i+1).padStart(2,'0')+'.png'}});await b.close();}})();'''
    open(f'{work}/r.js', 'w').write(js)
    subprocess.run(['node', f'{work}/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    open(f'{OUTDIR}/texto.txt', 'w').write(CAPTION)
    print(N, OUTDIR)

if __name__ == '__main__':
    render()
