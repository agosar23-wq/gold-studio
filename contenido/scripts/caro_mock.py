"""Carrusel 'Así no / Así sí' con mini perfiles de Instagram dibujados."""
import sys, os, subprocess; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR, emph, foot
import html as H
AV_GOOD = open('/home/user/gold-studio-final/perfil-dorado.svg').read().replace('width="1080" height="1080"', 'width="100%" height="100%"')

def profile(good, focus):
    dim = lambda part: '' if focus in (part, 'none') else ' dim'
    ring = lambda part: ' focus' if focus == part else ''
    if good:
        av = f'<div class="av{dim("av")}{ring("av")}">{AV_GOOD}</div>'
        name = 'Gold Studio'; bio = 'Diseño páginas web y marcas para emprendedores ✦ Buenos Aires'; link = '🔗 goldstudio-ba.vercel.app'
        hl = ''.join(f'<i style="background:#FAF6EE;border:3px solid #C9A34E"><b style="background:#C9A34E"></b></i>' for _ in range(4))
        grid = ''.join(f'<i style="background:{c}"></i>' for c in ['#C9A34E', '#1C1A17', '#FAF6EE', '#1C1A17', '#FAF6EE', '#C9A34E', '#FAF6EE', '#C9A34E', '#1C1A17'])
        btn = '<span class="b">Mensaje</span><span class="b gold">WhatsApp</span>'
    else:
        av = f'<div class="av bad{dim("av")}{ring("av")}"><span>mi emprendimiento de diseño y otras cosas lindas</span></div>'
        name = 'mi_marca_oficial_2024'; bio = 'Amo el café ☕🌸✨ vivo la vida 💫'; link = ''
        hl = ''.join(f'<i style="background:{c}"></i>' for c in ['#7FB3D5', '#F5B7B1', '#82E0AA', '#F9E79F'])
        grid = ''.join(f'<i style="background:{c}"></i>' for c in ['#E74C3C', '#3498DB', '#F1C40F', '#9B59B6', '#1ABC9C', '#E67E22', '#FF8FAB', '#2ECC71', '#34495E'])
        btn = '<span class="b">Seguir</span>'
    return f'''<div class="prof {'good' if good else 'bad'}">
  <div class="lab">{'Así sí' if good else 'Así no'}</div>
  <div class="top">{av}<div class="stats{dim('x')}"><b>48</b><b>320</b><b>210</b></div></div>
  <div class="bio{dim('bio')}{ring('bio')}"><strong>{name}</strong><span>{H.escape(bio)}</span>{f'<em>{link}</em>' if link else ''}</div>
  <div class="btns{dim('btn')}{ring('btn')}">{btn}</div>
  <div class="hl{dim('hl')}{ring('hl')}">{hl}</div>
  <div class="grid{dim('grid')}{ring('grid')}">{grid}</div>
</div>'''

EXTRA = '''
.mocks{display:flex;gap:36px;justify-content:center}
.prof{width:400px;background:#fff;border-radius:34px;padding:26px 22px 22px;box-shadow:0 30px 60px -36px rgba(28,26,23,.45);position:relative;font-family:J;color:#1C1A17}
.prof .lab{position:absolute;top:-22px;left:22px;font-size:22px;font-weight:500;padding:6px 16px;border-radius:999px;letter-spacing:.06em}
.prof.bad .lab{background:#C0392B;color:#fff} .prof.good .lab{background:#1C1A17;color:#FAF6EE}
.top{display:flex;align-items:center;gap:18px}
.av{width:104px;height:104px;border-radius:50%;overflow:hidden;flex:none}
.av.bad{background:#F5CBA7;display:grid;place-items:center;text-align:center;font-size:9px;padding:12px;box-sizing:border-box;color:#555}
.av svg{display:block}
.stats{display:flex;gap:18px;font-size:22px} .stats b{font-weight:600}
.bio{margin-top:14px;display:flex;flex-direction:column;gap:4px;font-size:19px;line-height:1.3;padding:6px;border-radius:14px}
.bio strong{font-weight:600} .bio em{font-style:normal;color:#2C5A8A}
.btns{display:flex;gap:8px;margin-top:10px;padding:4px;border-radius:14px}
.btns .b{flex:1;text-align:center;background:#EFEFEF;border-radius:10px;padding:9px 0;font-size:18px;font-weight:500}
.btns .b.gold{background:#C9A34E;color:#1C1A17}
.hl{display:flex;gap:16px;margin-top:14px;padding:6px;border-radius:14px}
.hl i{width:58px;height:58px;border-radius:50%;display:grid;place-items:center}
.hl i b{width:22px;height:22px;border-radius:50%}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;margin-top:14px;padding:4px;border-radius:12px}
.grid i{aspect-ratio:1;display:block}
.dim{opacity:.28}
.focus{outline:5px solid #C9A34E;outline-offset:4px}
.av.focus{outline-offset:5px}
.tipline{font-size:38px;line-height:1.35;text-align:center;color:var(--sub);max-width:820px;align-self:center}
.tipline b{color:var(--em);font-weight:500}
.hd{display:flex;align-items:baseline;gap:26px}
.hd .num{font-size:120px}
'''

def build(name, slides):
    N = len(slides); parts = []
    for i, s in enumerate(slides, 1):
        bg = s.get('bg', 'm')
        if s['kind'] == 'cover':
            inner = (f'<div class="eb">{H.escape(s["eb"])}</div><h1 style="font-size:100px">{emph(s["text"])}</h1>'
                     f'<div class="mocks" style="transform:scale(.7);transform-origin:top center;margin-bottom:-250px">{profile(False, "none")}{profile(True, "none")}</div>')
        elif s['kind'] == 'err':
            inner = (f'<div class="hd"><div class="num">{s["n"]}</div><h2 style="font-size:64px">{emph(s["title"])}</h2></div>'
                     f'<div class="mocks">{profile(False, s["focus"])}{profile(True, s["focus"])}</div>'
                     f'<p class="tipline">{s["tip"]}</p>')
        else:
            inner = f'<div class="spk">{SP}</div><h1 style="font-size:96px">{emph(s["text"])}</h1><div class="pill">{H.escape(s["pill"])}</div>'
        parts.append(f'<div class="s {bg}" style="gap:44px">{inner}{foot(i, N)}</div>')
    page = f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXTRA}</style>{"".join(parts)}'
    work = f'{SCR}/cm-{name}'; os.makedirs(work, exist_ok=True); open(f'{work}/c.html', 'w').write(page)
    out = f'/home/user/gold-studio-final/carruseles/{name}'; os.makedirs(out, exist_ok=True)
    for f in os.listdir(out): os.remove(os.path.join(out, f))
    js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1350}}}});
await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(300);
const els=await p.$$('.s');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{out}/'+String(i+1).padStart(2,'0')+'.png'}});await b.close();}})();'''
    open(f'{work}/r.js', 'w').write(js)
    subprocess.run(['node', f'{work}/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    return out

S = [
 dict(kind='cover', bg='g', eb='Así no / Así sí', text='5 errores que hacen que tu Instagram parezca *poco profesional*'),
 dict(kind='err', n=1, focus='av', title='Foto de perfil que *no se lee*', tip='En chiquito no se entiende nada. <b>Usá un ícono simple o tu logo.</b>'),
 dict(kind='err', n=2, focus='bio', title='Una bio que *no dice qué hacés*', tip='Que en 3 segundos se entienda <b>qué hacés, para quién y dónde.</b>'),
 dict(kind='err', n=3, focus='grid', title='Colores distintos *en cada posteo*', tip='Elegí <b>3 colores</b> y repetilos siempre. Así te reconocen al toque.'),
 dict(kind='err', n=4, focus='hl', title='Destacadas *sin portada*', tip='Con <b>portadas iguales</b> tu perfil se ve ordenado en un segundo.'),
 dict(kind='err', n=5, focus='btn', title='No hay forma de *contactarte*', tip='Sumá el <b>botón de WhatsApp</b> o un link. Que escribirte sea fácil.'),
 dict(kind='end', bg='n', text='¿Cuántos tenías? *Todo tiene arreglo.*', pill='Guardalo y mandáselo a una amiga'),
]
if __name__ == '__main__':
    print(build('dia02-carrusel-5-errores-instagram-v2', S))
