"""Cuatro marcas inventadas (para mostrar branding) y sus logos en PNG transparente.
Almendra (pastelería), Ondina (moda), Nácar (estética y spa), Nube (heladería)."""
import sys, os, subprocess; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import SCR, F

LOGOS = SCR + '/mock/logos'
FONTS = f'''
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2);font-weight:500;font-style:italic}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:P;src:url({F}playfair-display/files/playfair-display-latin-500-italic.woff2);font-weight:500;font-style:italic}}
@font-face{{font-family:P;src:url({F}playfair-display/files/playfair-display-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:AB;src:url({F}archivo-black/files/archivo-black-latin-400-normal.woff2)}}
'''

BRANDS = {
 'almendra': dict(nombre='Almendra', rubro='Pastelería', tipo='Playfair Display + Jost',
                  colores=[('Cacao', '#4A2622'), ('Almendra', '#C89B6D'), ('Crema', '#F4E9DA'), ('Rosa té', '#E6C3B8')]),
 'ondina':   dict(nombre='Ondina', rubro='Moda', tipo='Jost',
                  colores=[('Oliva', '#4B5537'), ('Terracota', '#B86B45'), ('Arena', '#E8DFCC'), ('Hueso', '#F7F3EA')]),
 'nacar':    dict(nombre='Nácar', rubro='Estética y spa', tipo='Bodoni Moda + Jost',
                  colores=[('Café', '#5B3F37'), ('Nude', '#B9897B'), ('Perla', '#F5EDE7'), ('Salvia', '#A7B09A')]),
 'nube':     dict(nombre='Nube', rubro='Heladería', tipo='Archivo Black + Jost',
                  colores=[('Azul noche', '#22346B'), ('Frutilla', '#F0A9A0'), ('Manteca', '#F6E3A1'), ('Leche', '#FFFBF2')]),
}

# ---------- isotipos (SVG, usan currentColor) ----------
def iso(b, s=200):
    if b == 'almendra':   # sello circular con texto alrededor
        return (f'<svg width="{s}" height="{s}" viewBox="0 0 200 200" fill="currentColor"><defs><path id="ca" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"/></defs>'
                '<circle cx="100" cy="100" r="96" fill="none" stroke="currentColor" stroke-width="2.5"/>'
                '<text font-family="J" font-size="15" font-weight="500" letter-spacing="5.2"><textPath href="#ca">PASTELERÍA · ALMENDRA · PASTELERÍA · ALMENDRA ·</textPath></text>'
                '<text x="100" y="128" text-anchor="middle" font-family="P" font-style="italic" font-weight="500" font-size="88">A</text></svg>')
    if b == 'ondina':     # tres ondas
        w = ''.join(f'<path d="M30 {y} C 55 {y-22}, 80 {y-22}, 100 {y} S 145 {y+22}, 170 {y}" fill="none" stroke="currentColor" stroke-width="9" stroke-linecap="round"/>' for y in (72, 100, 128))
        return f'<svg width="{s}" height="{s}" viewBox="0 0 200 200">{w}</svg>'
    if b == 'nacar':      # concha en abanico
        rays = ''.join(f'<path d="M100 160 L {100 + 84 * __import__("math").cos(a)} {160 - 84 * __import__("math").sin(a)}" stroke="currentColor" stroke-width="5" stroke-linecap="round"/>'
                       for a in [__import__('math').radians(d) for d in range(20, 161, 20)])
        return (f'<svg width="{s}" height="{s}" viewBox="0 0 200 200" fill="none"><path d="M12 160 A 88 88 0 0 1 188 160 Z" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/>{rays}'
                '<circle cx="100" cy="160" r="10" fill="currentColor"/></svg>')
    if b == 'nube':       # nube con la n
        return (f'<svg width="{s}" height="{s}" viewBox="0 0 200 200"><path fill="currentColor" d="M52 150 a34 34 0 0 1 -4 -67 a44 44 0 0 1 84 -18 a36 36 0 0 1 44 46 a26 26 0 0 1 -12 39 Z"/>'
                '<text x="104" y="135" text-anchor="middle" font-family="AB" font-size="74" fill="var(--bg,#fff)">n</text></svg>')

def word(b, c, s=1.0):
    if b == 'almendra':
        return (f'<div style="display:flex;flex-direction:column;align-items:center;white-space:nowrap;color:{c}"><span style="font-family:P;font-style:italic;font-weight:500;font-size:{150*s}px;line-height:1">Almendra</span>'
                f'<span style="font-family:J;font-weight:500;font-size:{24*s}px;letter-spacing:.55em;margin-top:{14*s}px;padding-left:.55em">PASTELERÍA</span></div>')
    if b == 'ondina':
        return (f'<div style="display:flex;flex-direction:column;align-items:center;white-space:nowrap;color:{c}"><span style="font-family:J;font-weight:400;font-size:{120*s}px;letter-spacing:.32em;padding-left:.32em;line-height:1">ONDINA</span>'
                f'<span style="font-family:J;font-weight:500;font-size:{26*s}px;letter-spacing:.6em;padding-left:.6em;margin-top:{20*s}px">MODA ESTUDIO</span></div>')
    if b == 'nacar':
        return (f'<div style="display:flex;flex-direction:column;align-items:center;white-space:nowrap;color:{c}"><span style="font-family:B;font-weight:500;font-size:{150*s}px;line-height:1;letter-spacing:.02em">Nácar</span>'
                f'<span style="font-family:J;font-weight:500;font-size:{22*s}px;letter-spacing:.55em;padding-left:.55em;margin-top:{16*s}px">ESTÉTICA &amp; SPA</span></div>')
    if b == 'nube':
        return (f'<div style="display:flex;flex-direction:column;align-items:center;white-space:nowrap;color:{c}"><span style="font-family:AB;font-size:{170*s}px;line-height:.9;letter-spacing:-.03em">nube</span>'
                f'<span style="font-family:J;font-weight:500;font-size:{24*s}px;letter-spacing:.5em;padding-left:.5em;margin-top:{18*s}px">HELADERÍA ARTESANAL</span></div>')

def full(b, c, bg='#fff'):
    """Isotipo arriba + logotipo."""
    return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:26px;color:{c};--bg:{bg}">{iso(b, 170)}{word(b, c)}</div>')

def badge(b, c, bg):
    """Logo dentro de un círculo de color (para vasos y stickers)."""
    return (f'<div style="width:420px;height:420px;border-radius:50%;background:{bg};display:flex;align-items:center;justify-content:center;color:{c};--bg:{bg}">'
            f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px">{iso(b, 150)}<div style="transform:scale(.62);margin-top:-30px">{word(b, c, .9)}</div></div></div>')

def variants():
    V = {}
    for b, d in BRANDS.items():
        dark, accent, light = d['colores'][0][1], d['colores'][1][1], d['colores'][2][1]
        V[f'{b}-word-dark'] = word(b, dark); V[f'{b}-word-light'] = word(b, light); V[f'{b}-word-accent'] = word(b, accent)
        V[f'{b}-full-dark'] = full(b, dark, light); V[f'{b}-full-light'] = full(b, light, dark)
        V[f'{b}-iso-dark'] = f'<div style="color:{dark};--bg:{light}">{iso(b, 400)}</div>'
        V[f'{b}-iso-light'] = f'<div style="color:{light};--bg:{dark}">{iso(b, 400)}</div>'
        V[f'{b}-iso-accent'] = f'<div style="color:{accent};--bg:{light}">{iso(b, 400)}</div>'
        V[f'{b}-badge'] = badge(b, light, dark)
    return V

def render():
    os.makedirs(LOGOS, exist_ok=True)
    V = variants(); names = list(V)
    html = f'<!doctype html><meta charset="utf-8"><style>{FONTS}body{{margin:0;background:transparent}}.l{{display:inline-block;padding:20px}}</style>' + ''.join(f'<div class="l">{V[n]}</div><br>' for n in names)
    work = SCR + '/mock/lw'; os.makedirs(work, exist_ok=True); open(work + '/l.html', 'w').write(html)
    js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1400,height:900}},deviceScaleFactor:2}});
    await p.goto('file://{work}/l.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(300);
    const n={names};const els=await p.$$('.l');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{LOGOS}/'+n[i]+'.png',omitBackground:true}});await b.close();}})();'''
    open(work + '/r.js', 'w').write(js)
    subprocess.run(['node', work + '/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    print(len(names), LOGOS)

if __name__ == '__main__':
    render()
