"""Carruseles con ejemplos visuales: colores con marcas de ejemplo y bio que se va completando."""
import sys, os, subprocess, html as H; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR, emph, foot
from caro_mock import EXTRA

def render(name, slides, extra=''):
    N = len(slides); parts = []
    for i, (bg, inner, style) in enumerate(slides, 1):
        parts.append(f'<div class="s {bg}" style="gap:40px;{style}">{inner}{foot(i, N)}</div>')
    page = f'<!doctype html><meta charset="utf-8"><style>{CSS}{EXTRA}{extra}</style>{"".join(parts)}'
    work = f'{SCR}/ce-{name}'; os.makedirs(work, exist_ok=True); open(f'{work}/c.html', 'w').write(page)
    out = f'/home/user/gold-studio-final/carruseles/{name}'; os.makedirs(out, exist_ok=True)
    for f in os.listdir(out): os.remove(os.path.join(out, f))
    js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1350}}}});
await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(300);
const els=await p.$$('.s');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{out}/'+String(i+1).padStart(2,'0')+'.png'}});await b.close();}})();'''
    open(f'{work}/r.js', 'w').write(js)
    subprocess.run(['node', f'{work}/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    return out

def end(text, pill, bg='n'):
    return (bg, f'<div class="spk">{SP}</div><h1 style="font-size:96px">{emph(text)}</h1><div class="pill">{H.escape(pill)}</div>', '')

# ================= COLORES =================
F = {'serif': "font-family:B", 'sans': "font-family:J;font-weight:500;letter-spacing:.18em;text-transform:uppercase"}
BRANDS = [  # color, fondo claro, texto, nombre, rubro, sensación, tipo de letra, paleta
 ('Dorado', '#C9A34E', '#FAF6EE', '#1C1A17', 'Aura', 'Joyería', 'Elegancia, valor, algo especial.', 'serif', ['#C9A34E', '#FAF6EE', '#1C1A17']),
 ('Negro', '#1C1A17', '#F2F0EC', '#F2F0EC', 'Noir', 'Estudio de tatuajes', 'Lujo, seriedad, sofisticación.', 'sans', ['#1C1A17', '#F2F0EC', '#8C8C8C']),
 ('Verde', '#5E7D5B', '#F1F3EC', '#F1F3EC', 'Raíz', 'Dietética natural', 'Salud, naturaleza, calma.', 'serif', ['#5E7D5B', '#F1F3EC', '#C8B88A']),
 ('Rosa', '#E8B4B8', '#FFF6F4', '#4A2329', 'Dulce Mía', 'Pastelería', 'Cercanía, dulzura, cuidado.', 'serif', ['#E8B4B8', '#FFF6F4', '#4A2329']),
 ('Azul', '#2F4A6D', '#EEF2F6', '#EEF2F6', 'Clara', 'Psicología', 'Confianza, profesionalismo, tranquilidad.', 'sans', ['#2F4A6D', '#EEF2F6', '#A9BCD0']),
 ('Naranja', '#E07A3F', '#FFF4EC', '#2B1A10', 'Mandarina', 'Ropa para chicos', 'Energía, alegría, algo accesible.', 'sans', ['#E07A3F', '#FFF4EC', '#2B1A10']),
]
def board(c, light, ink, name, rubro, font, pal, big=True):
    sc = 1 if big else .42
    card = (f'<div class="bcard" style="background:{c};color:{ink}"><div style="{F[font]};font-size:{64 if font=="serif" else 46}px">{name}</div>'
            f'<div style="font-size:20px;letter-spacing:.3em;text-transform:uppercase;opacity:.8">{rubro}</div></div>')
    post = (f'<div class="post" style="background:{light};color:{c}"><div style="font-size:18px;letter-spacing:.3em;text-transform:uppercase">Nuevo</div>'
            f'<div style="{F[font]};font-size:40px;line-height:1.1;color:{ink if c == "#E8B4B8" else c}">Hecho con amor</div>'
            f'<div class="dot" style="background:{c}"></div></div>')
    sw = '<div class="pal">' + ''.join(f'<i style="background:{x}"></i>' for x in pal) + '</div>'
    return f'<div class="board">{card}<div class="row">{post}{sw}</div></div>'
EXT_COL = '''
.board{display:flex;flex-direction:column;gap:22px;width:820px;align-self:center}
.bcard{height:320px;border-radius:26px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;box-shadow:0 30px 60px -36px rgba(0,0,0,.45)}
.row{display:flex;gap:22px}
.post{width:400px;height:300px;border-radius:22px;padding:30px;box-sizing:border-box;display:flex;flex-direction:column;gap:12px;position:relative;box-shadow:0 20px 40px -30px rgba(0,0,0,.4)}
.post .dot{position:absolute;right:28px;bottom:28px;width:70px;height:70px;border-radius:50%}
.pal{flex:1;display:flex;flex-direction:column;gap:12px}
.pal i{flex:1;border-radius:16px;box-shadow:inset 0 0 0 2px rgba(0,0,0,.06)}
.mini{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;align-self:center;width:880px}
.mini div{height:180px;border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px}
.cname{display:flex;align-items:baseline;gap:22px;flex-wrap:wrap}
.r6{display:flex;height:120px;border-radius:20px;overflow:hidden;width:880px;align-self:center}
.r6 div{display:flex;align-items:flex-end;padding:14px;box-sizing:border-box;font-size:26px;font-weight:500}
'''
colores = []
mini = '<div class="mini">' + ''.join(f'<div style="background:{c};color:{ink}"><span style="{F[f]};font-size:{40 if f=="serif" else 28}px">{n}</span><span style="font-size:14px;letter-spacing:.24em;text-transform:uppercase;opacity:.8">{r}</span></div>' for (_, c, l, ink, n, r, _d, f, _p) in BRANDS) + '</div>'
colores.append(('n', f'<div class="eb">Con ejemplos</div><h1 style="font-size:100px">Qué transmite cada <em>color</em> en tu marca</h1>{mini}', ''))
for (col, c, light, ink, n, r, desc, f, pal) in BRANDS:
    colores.append(('m', f'<div class="cname"><h2 style="font-size:96px">{col}</h2><span class="body" style="font-size:40px">{desc}</span></div>'
                         f'{board(c, light, ink, n, r, f, pal)}<p class="tipline" style="font-size:32px">Ejemplo: <b>{n}</b>, {r.lower()}. Marca inventada.</p>', ''))
colores.append(('m', '<div class="eb">La regla que no falla</div><h2>60% fondo, 30% secundario, <em>10% acento</em></h2>'
                     '<div class="r6"><div style="flex:6;background:#FAF6EE;box-shadow:inset 0 0 0 2px #E6DAC2">60% Marfil</div><div style="flex:3;background:#1C1A17;color:#FAF6EE">30% Negro</div><div style="flex:1.3;background:#C9A34E">10%</div></div>'
                     '<p class="tipline">Así está armada la paleta de <b>Gold Studio</b>: el dorado aparece poquito, por eso brilla.</p>', ''))
colores.append(end('¿Cuál es el color de *tu marca?*', 'Contame en comentarios', 'g'))

# ================= BIO =================
LINES = [('Qué hacés', '🎂 Tortas y mesas dulces personalizadas'),
         ('Para quién', 'Para cumples, bautismos y eventos'),
         ('Dónde estás', '📍 Palermo, CABA · Envíos a todo AMBA'),
         ('Una invitación', '👇 Pedí tu presupuesto por WhatsApp'),
         ('Un link', '🔗 wa.me/dulcemia')]
def bioprofile(n_lines, hl=None, bad=False):
    if bad:
        bio = '<span class="bl">Amo lo dulce 💕✨ vivo la vida 🌸</span>'
    else:
        bio = ''.join(f'<span class="bl{" new" if k == hl else ""}{" link" if t.startswith("🔗") else ""}">{H.escape(t)}</span>' for k, (_, t) in enumerate(LINES[:n_lines]))
        if n_lines == 0: bio = '<span class="bl ph">Tu bio acá…</span>'
    av = '<div class="av2" style="background:#E8B4B8;color:#4A2329"><span style="font-family:B;font-size:30px">Dulce<br>Mía</span></div>'
    return f'''<div class="prof2"><div class="top">{av}<div class="stats"><b>152</b><b>1.240</b><b>380</b></div></div>
<div class="bio2"><strong>Dulce Mía · Pastelería</strong>{bio}</div>
<div class="btns"><span class="b">Seguir</span><span class="b">Mensaje</span></div></div>'''
EXT_BIO = '''
.prof2{width:720px;align-self:center;background:#fff;border-radius:40px;padding:40px 40px 34px;box-shadow:0 30px 60px -36px rgba(28,26,23,.45);color:#1C1A17;font-family:J}
.prof2 .top{gap:34px}.prof2 .stats{gap:34px;font-size:32px}
.av2{width:150px;height:150px;border-radius:50%;display:grid;place-items:center;text-align:center;line-height:1;flex:none}
.bio2{display:flex;flex-direction:column;gap:6px;margin-top:22px;font-size:30px;line-height:1.3}
.bio2 strong{font-weight:600}
.bl{padding:4px 10px;margin-left:-10px;border-radius:10px}
.bl.new{background:#F6EBD0;box-shadow:0 0 0 3px #C9A34E}
.bl.link{color:#2C5A8A}.bl.ph{color:#aaa}
.prof2 .btns{margin-top:22px}.prof2 .btns .b{font-size:26px;padding:14px 0}
.stepl{display:flex;align-items:center;gap:22px}
.pair{display:flex;gap:30px;align-self:center;transform:scale(.62);transform-origin:top center;margin-bottom:-330px;margin-top:10px}
.pair .prof2{position:relative}
.pair .lab{position:absolute;top:-30px;left:30px;font-size:30px;font-weight:500;padding:8px 20px;border-radius:999px}
'''
from carogen import CHECK
bio = []
pair = (f'<div class="pair"><div style="position:relative"><div class="lab" style="position:absolute;top:-30px;left:30px;background:#C0392B;color:#fff;font-size:30px;padding:8px 20px;border-radius:999px;z-index:2">Así no</div>{bioprofile(0, bad=True)}</div>'
        f'<div style="position:relative"><div class="lab" style="position:absolute;top:-30px;left:30px;background:#1C1A17;color:#FAF6EE;font-size:30px;padding:8px 20px;border-radius:999px;z-index:2">Así sí</div>{bioprofile(5)}</div></div>')
bio.append(('g', f'<div class="eb">Checklist</div><h1 style="font-size:96px">Tu bio tiene <em>3 segundos</em> para convencer</h1>{pair}', ''))
for k, (lab, _) in enumerate(LINES):
    bio.append(('m', f'<div class="stepl">{CHECK}<h2 style="font-size:72px">{k+1}. {lab}</h2></div>{bioprofile(k+1, hl=k)}'
                     f'<p class="tipline">{["Que se entienda al toque qué vendés.", "Así la persona sabe si es para ella.", "Clave si hacés envíos o atendés en una zona.", "Decile qué hacer después de leerte.", "Que escribirte sea un solo toque."][k]}</p>', ''))
bio.append(end('Guardalo y *editá tu bio hoy.*', '@goldstudio.ba'))

if __name__ == '__main__':
    print(render('dia04-carrusel-colores-de-tu-marca-v2', colores, EXT_COL))
    print(render('dia06-carrusel-checklist-bio-v2', bio, EXT_BIO))
