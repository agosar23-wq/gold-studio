import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
from caro_ejemplos import render, end
D = 'file:///home/user/gold-studio-final/caso-sc/'
EXT = '''
.ph{border-radius:36px;overflow:hidden;box-shadow:0 30px 60px -30px rgba(0,0,0,.55);background:#000}
.ph img{display:block;width:100%}
.pair2{display:flex;gap:30px;justify-content:center;align-items:flex-start}
.tag2{display:inline-block;font-size:24px;font-weight:500;padding:6px 18px;border-radius:999px;margin-bottom:14px}
.t-no{background:#C0392B;color:#fff}.t-si{background:#1C1A17;color:#FAF6EE}
.col{display:flex;flex-direction:column;align-items:center}
.lg img{display:block;width:100%;border-radius:30px;box-shadow:0 30px 60px -36px rgba(0,0,0,.35)}
.jar{display:block}
.trio{display:flex;gap:24px;align-items:center;justify-content:center}
.lbl{display:block;border-radius:10px;box-shadow:0 26px 50px -24px rgba(28,26,23,.45),0 2px 6px rgba(28,26,23,.12)}
'''
def ph(src, w, crop_h=None):
    st = f'height:{crop_h}px' if crop_h else ''
    return f'<div class="ph" style="width:{w}px;{st}"><img src="{D}{src}"></div>'
S = []
S.append(('n', f'<div class="eb">Caso real ✦ Consultorio de estética</div><h1 style="font-size:112px">La marca que siempre soñaste <em>puede ser real</em></h1>'
               f'<div class="trio"><div class="lg" style="width:260px"><img src="{D}logo-recorte.png"></div>'
               f'<img class="lbl" src="{D}orig/etiqueta-nueva.png" style="width:330px;transform:rotate(-3deg)">{ph("catalogo-despues.jpg", 250, 330)}</div>', ''))
S.append(('m', f'<div class="eb">El punto de partida</div><h2>Así estaba <em>antes</em></h2><div class="pair2">{ph("catalogo-antes.jpg", 560, 640)}</div>'
               '<p class="tipline">Fotos sueltas y sin identidad. <b>Podía ser cualquier consultorio.</b></p>', ''))
S.append(('m', f'<div class="eb">1 · Logo</div><h2>Una identidad <em>propia</em></h2><div class="lg" style="width:520px;align-self:center"><img src="{D}logo-recorte.png"></div>'
               '<p class="tipline">Línea fina, femenina y elegante: <b>piel, cuidado y bienestar</b> en un solo trazo.</p>', ''))
S.append(('m', f'<div class="eb">2 · Catálogo de WhatsApp</div><h2>Antes / <em>Después</em></h2>'
               f'<div class="pair2"><div class="col"><span class="tag2 t-no">Antes</span>{ph("catalogo-antes.jpg", 420, 720)}</div>'
               f'<div class="col"><span class="tag2 t-si">Después</span>{ph("catalogo-despues.jpg", 420, 720)}</div></div>', ''))
S.append(('m', '<div class="eb">2 · Catálogo de WhatsApp</div><h2>Cada servicio con <em>su propia ficha</em></h2>'
               f'<div class="pair2">{ph("catalogo-categorias.jpg", 520, 680)}</div><p class="tipline">Mismo estilo, mismos colores y el logo en todo. <b>Se ve como una clínica premium.</b></p>', ''))
S.append(('m', f'<div class="eb">3 · Diseño de etiquetas</div><h2>Etiquetas con <em>identidad</em></h2><img class="lbl" src="{D}orig/etiqueta-nueva.png" style="width:860px;align-self:center;transform:rotate(-1.5deg)">'
               '<p class="tipline">Tipografía premium, mucho aire y una molécula que dice <b>"ciencia"</b> sin palabras.</p>', ''))
S.append(('n', f'<div class="eb">El resultado</div><h1 style="font-size:84px">Una marca que se ve <em>igual de linda en todos lados</em></h1>'
               f'<div class="trio"><div class="lg" style="width:260px"><img src="{D}logo-recorte.png"></div>'
               f'<img class="lbl" src="{D}orig/etiqueta-nueva.png" style="width:330px;transform:rotate(-3deg)">{ph("catalogo-despues.jpg", 250, 330)}</div>', ''))
S.append(end('¿Tu marca necesita un *cambio así?*', 'Escribime por DM ✦ @goldstudio.ba', 'g'))
if __name__ == '__main__':
    print(render('caso-real-branding-consultorio', S, EXT))
