"""Reel "Así se ve una marca completa": Almendra paso a paso (logo, colores, letras, packaging) y las otras marcas."""
import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
from reelgen import build, F
from marcas_ejemplo import LOGOS, BRANDS
from mockups_marcas import OUT as MK

lg = lambda n: f'file://{LOGOS}/{n}.png'
mk = lambda n: f'file://{MK}{n}.jpg'
C = BRANDS['almendra']['colores']
CA, CR = C[0][1], C[2][1]
FONT_P = f'<style>@font-face{{font-family:P;src:url({F}playfair-display/files/playfair-display-latin-500-italic.woff2);font-style:italic;font-weight:500}}</style>'

def foto(n, w=820, h=760, pos='50% 50%'):
    return (f'<div style="width:{w}px;height:{h}px;border-radius:36px;overflow:hidden;box-shadow:0 50px 90px -40px rgba(0,0,0,.55)">'
            f'<img src="{mk(n)}" style="width:100%;height:100%;object-fit:cover;object-position:{pos};display:block"></div>')

logo = (f'<div style="width:820px;height:700px;border-radius:40px;background:{CR};display:flex;align-items:center;justify-content:center;box-shadow:0 50px 90px -40px rgba(0,0,0,.4)">'
        f'<img src="{lg("almendra-full-dark")}" style="width:560px"></div>')
colores = ('<div style="display:flex;gap:18px">' +
           ''.join(f'<div style="width:190px;height:420px;border-radius:30px;background:{c};display:flex;flex-direction:column;justify-content:flex-end;padding:20px;box-sizing:border-box;'
                   f'font-size:26px;line-height:1.3;color:{"#FAF6EE" if i < 2 else CA};box-shadow:inset 0 0 0 2px rgba(0,0,0,.05)">{n}<br><span style="font-size:20px;opacity:.8">{c}</span></div>'
                   for i, (n, c) in enumerate(C)) + '</div>')
letras = (FONT_P + f'<div style="width:820px;border-radius:40px;background:#fff;padding:50px 60px;box-sizing:border-box;color:{CA};display:flex;flex-direction:column;gap:30px;box-shadow:0 50px 90px -40px rgba(0,0,0,.35)">'
          '<div><div style="font-family:P;font-style:italic;font-size:170px;line-height:1">Aa</div><div style="font-size:30px;letter-spacing:.3em;margin-top:10px">PLAYFAIR · TÍTULOS</div></div>'
          '<div style="height:2px;background:#EFE4D6"></div>'
          '<div><div style="font-family:J;font-size:150px;line-height:1">Aa</div><div style="font-size:30px;letter-spacing:.3em;margin-top:10px">JOST · TEXTOS</div></div></div>')
detalle = f'<div style="display:flex;gap:24px">{foto("almendra-vaso", 400, 640, "50% 45%")}{foto("almendra-paquete", 400, 640, "50% 50%")}</div>'
rubros = ('<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;width:840px">' +
          ''.join(f'<div style="height:400px;border-radius:28px;overflow:hidden"><img src="{mk(n)}" style="width:100%;height:100%;object-fit:cover;object-position:{p};display:block"></div>'
                  for n, p in [('ondina-etiqueta', '50% 50%'), ('nacar-bolsa', '50% 50%'), ('nube-caja', '50% 50%'), ('ondina-tote-negra', '50% 60%')]) + '</div>')

NAME = 'reel-marca-completa'
SCENES = [
    dict(bg='n', text='Así se ve una marca *completa*'),
    dict(bg='m', kind='reveal', html=logo, html_pos='top', text='Primero, *el logo.*', fs=110),
    dict(bg='m', html=colores, html_pos='top', text='Los colores *de la marca.*', fs=104),
    dict(bg='m', html=letras, html_pos='top', text='Las *tipografías.*', fs=110),
    dict(bg='m', html=foto('almendra-bolsa', 820, 820, '50% 50%'), html_pos='top', text='En el *packaging.*', fs=110),
    dict(bg='m', html=detalle, html_pos='top', text='Y en cada *detalle.*', fs=110),
    dict(bg='n', html=rubros, html_pos='top', text='Funciona para *cualquier rubro.*', fs=96),
    dict(bg='g', kind='end', text='¿Querés tu marca *así de linda?*', pill='Escribime y lo charlamos'),
]
CAPTION = '''Así se ve una marca completa.

No es solo el logo: son los colores, las tipografías y cómo se ve en todo lo que tocan tus clientes. El packaging, el vaso, la bolsa, tus redes.

Cuando todo sigue la misma línea, tu marca se reconoce al toque.

¿Querés la tuya? Escribime y lo charlamos.

#branding #emprendedoras #diseñodemarca'''

if __name__ == '__main__':
    out, total, work = build(NAME, SCENES)
    open(out.replace('.mp4', '.txt'), 'w').write(CAPTION)
    print(out, total)
