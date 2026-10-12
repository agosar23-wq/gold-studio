"""Portadas WhatsApp v4: escritorio de estudio (flatlay) y titular de agencia."""
import sys, os, base64, subprocess; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import CSS, SP, SCR
import catalogo_wa2 as K, mocks as M
D = '/home/user/gold-studio-final/'; OUT = D + 'whatsapp-business'
svg = lambda f: 'data:image/svg+xml;base64,' + base64.b64encode(open(D + f, 'rb').read()).decode()
W, H = 1920, 1080
SH = 'box-shadow:0 30px 50px -20px rgba(60,40,10,.35),0 6px 14px -6px rgba(60,40,10,.25)'
def ab(x, y, inner, rot=0, z=1): return f'<div style="position:absolute;left:{x}px;top:{y}px;transform:rotate({rot}deg);z-index:{z}">{inner}</div>'
keys = ''.join(f'<i style="display:block;height:20px;border-radius:4px;background:#2E2A25"></i>' for _ in range(56))
laptop = (f'<div style="width:600px;border-radius:18px;background:#C9C3B8;padding:12px;{SH}">'
          f'<div style="background:#1C1A17;border-radius:10px;padding:14px">{M.site("aura", 2, 548).replace("box-shadow", "x-shadow")}</div>'
          f'<div style="margin-top:12px;background:#B9B2A6;border-radius:10px;padding:16px 18px;display:grid;grid-template-columns:repeat(14,1fr);gap:6px">{keys}</div>'
          f'<div style="width:180px;height:90px;margin:12px auto 0;border-radius:10px;background:#B0A99C"></div></div>')
coffee = (f'<div style="width:220px;height:220px;border-radius:50%;background:#FFFFFF;{SH};display:grid;place-items:center">'
          '<div style="width:150px;height:150px;border-radius:50%;background:#F4F1EC;border:8px solid #fff;box-shadow:inset 0 0 0 2px #E8E2D8;display:grid;place-items:center">'
          '<div style="width:112px;height:112px;border-radius:50%;background:radial-gradient(circle at 50% 45%,#E9D3B4 0 22%,#9A6A3F 23% 100%);"></div></div></div>')
def sw(c, name, code):
    return (f'<div style="width:150px;height:220px;background:#fff;border-radius:6px;{SH};padding:10px;box-sizing:border-box">'
            f'<div style="height:150px;background:{c};border-radius:3px"></div><div style="font-family:J;font-size:15px;color:#1C1A17;margin-top:10px;font-weight:500">{name}</div>'
            f'<div style="font-family:J;font-size:12px;color:#888">{code}</div></div>')
swatches = (f'<div style="position:relative;width:360px;height:260px">' + ab(0, 20, sw('#1C1A17', 'Negro', 'GS 01'), -14) + ab(80, 0, sw('#C9A34E', 'Dorado', 'GS 02'), -4)
            + ab(170, 10, sw('#FAF6EE', 'Marfil', 'GS 03'), 8) + '</div>')
note = (f'<div style="width:330px;height:420px;background:#FFFDF8;border-radius:8px 18px 18px 8px;{SH};position:relative;overflow:hidden">'
        '<div style="position:absolute;left:0;top:0;bottom:0;width:26px;background:#E8DFCF"></div>'
        + ''.join(f'<div style="position:absolute;left:46px;right:20px;top:{60+i*34}px;height:1px;background:#EDE5D6"></div>' for i in range(11)) +
        '<svg style="position:absolute;left:70px;top:60px" width="220" height="200" viewBox="0 0 220 200" fill="none" stroke="#6B6358" stroke-width="2.4" stroke-linecap="round">'
        '<circle cx="80" cy="110" r="46"/><circle cx="80" cy="110" r="30" stroke-dasharray="4 6"/><path d="M128 60 C130 74 132 76 146 78 C132 80 130 82 128 96 C126 82 124 80 110 78 C124 76 126 74 128 60Z"/>'
        '<path d="M20 180 C60 170 120 175 200 168"/></svg>'
        '<div style="position:absolute;left:60px;bottom:40px;font-family:B;font-style:italic;font-size:30px;color:#8A6A22">ideas logo ✦</div></div>')
pencil = '<div style="width:300px;height:16px;border-radius:8px;background:linear-gradient(90deg,#1C1A17 0 8%,#C9A34E 8% 88%,#E8C9A0 88% 96%,#333 96%);box-shadow:0 10px 16px -8px rgba(0,0,0,.4)"></div>'
leaf = lambda w, h, r, c='#6E8B5E': f'<div style="width:{w}px;height:{h}px;border-radius:0 100% 0 100%;background:{c};transform:rotate({r}deg);opacity:.95"></div>'
plant = '<div style="position:relative;width:300px;height:300px">' + ''.join(ab(x, y, leaf(170, 70, r, c)) for x, y, r, c in [(40, 60, 30, '#6E8B5E'), (90, 140, -10, '#5E7D5B'), (20, 170, 70, '#7F9A6C'), (130, 40, 80, '#5E7D5B')]) + '</div>'
phone = K.phone(K.ig, 230, 470)

def desk(bg, logo, tag):
    return (f'<div class="cv" style="background:{bg}">'
            + ab(-120, 560, plant, 0) + ab(1700, 60, plant, 160)
            + ab(60, 170, laptop, -6, 2) + ab(240, 720, swatches, 0, 3) + ab(520, 790, pencil, -18, 4)
            + ab(1270, 190, note, 7, 2) + ab(1560, 250, phone, -8, 3) + ab(1380, 660, coffee, 0, 3)
            + f'<div style="position:absolute;left:0;right:0;top:190px;display:flex;flex-direction:column;align-items:center;gap:12px;z-index:5">'
            f'<img src="{logo}" style="width:330px"><div style="font-family:J;font-size:22px;letter-spacing:.32em;color:{tag};font-weight:500">DISEÑO Y MARKETING DIGITAL</div></div></div>')

def headline(bg, ink, gold, sub, logo):
    return (f'<div class="cv" style="background:{bg};color:{ink}">'
            f'<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 30%,{gold}33,transparent 60%)"></div>'
            f'<div style="position:absolute;left:0;right:0;top:175px;display:flex;flex-direction:column;align-items:center;gap:20px">'
            f'<div style="display:flex;align-items:center;gap:22px"><img src="{logo}" style="width:170px"><span style="width:2px;height:70px;background:{gold}"></span>'
            f'<span style="font-family:J;font-size:22px;letter-spacing:.3em;color:{sub};font-weight:500;text-align:left;line-height:1.5">AGENCIA DE DISEÑO<br>Y MARKETING DIGITAL</span></div>'
            f'<div style="font-family:B;font-size:120px;line-height:1;letter-spacing:-.01em;text-align:center">Hacemos que tu marca <em style="color:{gold}">brille</em></div></div>'
            + ''.join(f'<div style="position:absolute;{side}:120px;top:{y}px;font-family:J;font-size:30px;letter-spacing:.2em;color:{sub};text-align:{side}">{t}</div>'
                      for side, y, t in [('left', 560, 'PÁGINAS WEB'), ('left', 620, 'APPS'), ('left', 680, 'TIENDAS ONLINE'), ('right', 560, 'BRANDING'), ('right', 620, 'LOGOS'), ('right', 680, 'REDES SOCIALES')])
            + f'<div style="position:absolute;left:120px;top:540px;width:60px;height:2px;background:{gold};display:none"></div></div>')

def _render():
    V = [('portada-escritorio-marfil', desk('linear-gradient(135deg,#F5EFE4,#EDE4D3)', svg('logo-gold-studio-transparente.svg'), '#5E5649')),
         ('portada-escritorio-madera', desk('linear-gradient(135deg,#C7A57E,#B48F66)', svg('logo-gold-studio-transparente.svg'), '#3B2A18')),
         ('portada-titular-negra', headline('#1C1A17', '#FAF6EE', '#C9A34E', '#BDB2A0', svg('logo-gold-studio-transparente-blanco.svg'))),
         ('portada-titular-marfil', headline('#FAF6EE', '#1C1A17', '#B8923A', '#5E5649', svg('logo-gold-studio-transparente.svg')))]
    work = SCR + '/wa-cover4'; os.makedirs(work, exist_ok=True)
    open(work + '/c.html', 'w').write(f'<!doctype html><meta charset="utf-8"><style>{CSS}{K.EXT}.cv{{width:{W}px;height:{H}px;position:relative;overflow:hidden;margin-bottom:20px}}</style>' + ''.join(h for _, h in V))
    js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});
    await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(400);
    const n={[n for n, _ in V]};const els=await p.$$('.cv');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{OUT}/'+n[i]+'.png'}});await b.close();}})();'''
    open(work + '/r.js', 'w').write(js)
    subprocess.run(['node', work + '/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))

if __name__ == "__main__":
    _render()
