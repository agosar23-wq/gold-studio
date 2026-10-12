"""Carrusel: el packaging también vende (ejemplo Dulce Mía)."""
import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
from caro_ejemplos import render, end
import pack as P

EXT = '''
.stage{position:relative;display:flex;justify-content:center;align-items:center}
.lab2{font-size:30px;font-weight:500;padding:8px 22px;border-radius:999px;letter-spacing:.06em;align-self:center}
.col{display:flex;flex-direction:column;gap:30px;align-items:center}
.cap{font-size:30px;color:var(--sub);letter-spacing:.04em;text-align:center}
'''
def step(n, title, mock, txt):
    return ('m', f'<div class="eb">{n}</div><h2>{title}</h2><div class="stage" style="flex:1">{mock}</div><p class="body" style="margin:0">{txt}</p>', 'justify-content:flex-start;padding-top:110px')

cover = ('m', '<div class="eb">Packaging</div><h1 style="font-size:112px">El packaging también <em>vende</em></h1>'
         '<div class="stage" style="height:600px;margin-top:20px">'
         f'<div style="position:absolute;left:20px;top:40px;transform:rotate(-5deg)">{P.card(380)}</div>'
         f'<div style="position:absolute;right:10px;top:110px">{P.box(480)}</div>'
         f'<div style="position:absolute;left:300px;top:330px">{P.sticker(230)}</div></div>'
         '<p class="cap" style="text-align:left;margin:0">Ejemplo: Dulce Mía, pastelería</p>', '')
vs = ('m', '<h1 style="font-size:92px">Misma torta. <em>¿Cuál comprarías?</em></h1>'
      '<div style="display:flex;gap:48px;justify-content:center;margin-top:30px">'
      f'<div class="col"><span class="lab2" style="background:#C0392B;color:#fff">Así no</span>{P.box(400, plain=True)}<p class="cap">Caja genérica</p></div>'
      f'<div class="col"><span class="lab2" style="background:#1C1A17;color:#FAF6EE">Así sí</span>{P.box(400)}<p class="cap">Caja con tu marca</p></div></div>'
      '<p class="body" style="margin:10px 0 0">Antes de probar nada, la persona ya decidió si le parece rico.</p>', '')
s1 = step('1 · La caja', 'Lo primero que <em>ven</em>', P.box(660), 'Con tu logo y tus colores, cuenta quién sos antes de abrirla.')
s2 = step('2 · El sticker de cierre', 'El truco <em>más económico</em>', P.sticker(420), 'Una caja lisa y un buen sticker ya se ven de marca.')
s3 = step('3 · La tarjeta', 'Un gracias que <em>hace volver</em>', P.card(680), 'Con tu usuario: así te etiquetan en sus historias.')
s4 = step('4 · La bolsa', 'Tu marca <em>sale a pasear</em>', P.bag(400), 'Cada persona que la lleva te hace publicidad por la calle.')
lineup = ('g', '<div class="eb">Todo junto</div><h1 style="font-size:96px">Así se ve <em>una marca</em></h1>'
          '<div style="display:flex;align-items:flex-end;justify-content:center;gap:28px;margin-top:30px">'
          f'{P.bag(250)}<div class="col" style="gap:24px">{P.cupbox(250)}{P.sticker(170)}</div>{P.box(330)}</div>'
          '<p class="body" style="margin:10px 0 0">Mismos colores, misma letra, mismo dibujo. Por eso la recordás.</p>', '')
slides = [cover, vs, s1, s2, s3, s4, lineup, end('¿Tu packaging cuenta *quién sos?*', 'Escribime y lo diseñamos juntas')]
if __name__ == '__main__':
    print(render('carrusel-packaging', slides, EXT))
