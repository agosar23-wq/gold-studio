"""Reels semana 3 (26 oct a 4 nov): Prana antes/después, web por dentro, Halloween, POV propuesta."""
import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
from reelgen import build, SCR
from yogi import yogi
from mascota import dog, paw
from carrusel_logos import mono
import mocks as M
W = f'file://{SCR}/webshots/'
PR, LAV, SAND, OFF = '#3E3557', '#D9CFF0', '#E8DCC8', '#F7F4EF'

# ---------- Prana: antes y después ----------
antes = ('<div style="width:820px;height:520px;background:#fff;border:2px solid #ddd;border-radius:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px">'
         '<div style="width:140px;height:140px;border-radius:50%;background:linear-gradient(135deg,#7FD1F7,#E36CF0);"></div>'
         '<span style="font-family:Arial;font-weight:bold;font-size:84px;color:#222">Yoga Prana</span><span style="font-family:\'Comic Sans MS\',cursive;font-size:36px;color:#E36CF0">clases de yoga!!</span></div>')
pal = '<div style="display:flex;gap:20px">' + ''.join(f'<i style="width:180px;height:300px;border-radius:30px;background:{c};box-shadow:inset 0 0 0 2px rgba(0,0,0,.06)"></i>' for c in [PR, LAV, SAND, OFF]) + '</div>'
fonts = ('<div style="display:flex;flex-direction:column;gap:8px;font-size:120px;line-height:1.05;color:' + PR + '">'
         '<span style="font-family:Arial;font-weight:bold;opacity:.3;text-decoration:line-through">Prana</span>'
         '<span style="font-family:XArchivo;opacity:.3;text-decoration:line-through">Prana</span><span style="font-family:B">Prana ✓</span></div>')
logo_p = (f'<div style="width:820px;height:640px;border-radius:40px;background:{PR};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px">'
          f'{yogi(LAV, 300)}<span style="font-family:B;font-size:120px;color:{LAV};line-height:1">Prana</span><span style="font-size:26px;letter-spacing:.4em;color:{LAV}">ESTUDIO DE YOGA</span></div>')
aplic = ('<div style="display:flex;gap:40px;align-items:center;justify-content:center">'
         f'<div style="width:420px;height:250px;background:{OFF};border-radius:14px;box-shadow:0 30px 50px -24px rgba(0,0,0,.5);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px">{yogi(PR, 110)}<span style="font-family:B;font-size:48px;color:{PR}">Prana</span></div>'
         f'<div style="width:300px;height:300px;border-radius:50%;background:{PR};display:grid;place-items:center;box-shadow:0 30px 50px -24px rgba(0,0,0,.5)">{yogi(LAV, 210)}</div></div>')
# ---------- Halloween ----------
five = ('<div style="display:flex;flex-direction:column;gap:4px;font-size:110px;line-height:1.05">'
        '<span style="font-family:XArchivo">Marca</span><span style="font-family:XPlayfair">Marca</span><span style="font-family:XNotoSerif">Marca</span>'
        '<span style="font-family:XFamiljen">Marca</span><span style="font-family:\'Comic Sans MS\',cursive">Marca</span></div>')
pix = f'<div style="width:820px;height:520px;background:#fff;border-radius:30px;display:grid;place-items:center"><img src="file://{SCR}/logo-tiny.png" style="width:640px;image-rendering:pixelated"></div>'
nobio = ('<div style="width:620px;background:#fff;border-radius:36px;padding:34px;box-shadow:0 30px 60px -30px rgba(0,0,0,.4);color:#1C1A17;font-family:J">'
         '<div style="display:flex;gap:26px;align-items:center"><div style="width:130px;height:130px;border-radius:50%;background:#ddd"></div>'
         '<div style="display:flex;gap:24px;font-size:24px;text-align:center"><div><b style="display:block;font-size:32px">3</b>posts</div><div><b style="display:block;font-size:32px">41</b>seguidores</div></div></div>'
         '<div style="margin-top:22px;font-size:30px;font-weight:500">user12345678</div>'
         '<div style="margin-top:10px;height:22px;width:60%;border:3px dashed #C0392B;border-radius:8px"></div>'
         '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px;margin-top:24px">' + ''.join('<div style="aspect-ratio:1;background:#eee"></div>' for _ in range(3)) + '</div></div>')
e404 = M.browser('<div style="height:420px;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:#444;font-family:Arial">'
                 '<b style="font-size:120px">404</b><span style="font-size:32px">Página no encontrada</span></div>', 820, 'linktr.ee/mimarca-viejo')
feed = '<div style="display:grid;grid-template-columns:repeat(3,250px);gap:8px">' + ''.join(f'<div style="height:250px;background:{c}"></div>' for c in ['#FF3B30', '#34C759', '#FFCC00', '#AF52DE', '#FF9500', '#00C7BE', '#FF2D55', '#5856D6', '#A2845E']) + '</div>'
# ---------- POV propuesta (Huellitas) ----------
T, MI, CO = '#2E6B66', '#CFE8DE', '#F29C7E'
h_logo = (f'<div style="width:820px;height:640px;border-radius:40px;background:{T};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px">'
          f'{dog("#fff", 400)}<span style="font-family:XFamiljen;font-size:96px;color:#fff;line-height:1">huellitas</span></div>')
h_pal = '<div style="display:flex;gap:20px">' + ''.join(f'<i style="width:180px;height:300px;border-radius:30px;background:{c};box-shadow:inset 0 0 0 2px rgba(0,0,0,.06)"></i>' for c in [T, MI, CO, '#FBF7F0']) + '</div>'
h_pat = (f'<div style="width:820px;height:520px;border-radius:40px;background:{MI};position:relative;overflow:hidden">' +
         ''.join(f'<span style="position:absolute;left:{x}px;top:{y}px">{paw(T, 80, r)}</span>' for x, y, r in [(60,50,-20),(260,30,25),(470,80,-35),(660,40,15),(150,200,30),(380,210,-15),(600,230,40),(60,360,10),(280,380,-30),(500,400,20),(700,370,0)]) + '</div>')
h_apl = ('<div style="display:flex;gap:40px;align-items:flex-end;justify-content:center">'
         f'<div style="width:330px;height:420px;background:{CO};border-radius:10px;box-shadow:0 30px 50px -24px rgba(0,0,0,.5);display:flex;flex-direction:column;align-items:center;justify-content:center">{dog(T, 240)}<span style="font-family:XFamiljen;font-size:46px;color:{T}">huellitas</span></div>'
         f'<div style="width:300px;height:300px;border-radius:50%;background:{T};display:grid;place-items:center;box-shadow:0 30px 50px -24px rgba(0,0,0,.5)">{dog("#fff", 220)}</div></div>')
wa = ('<div style="display:flex;flex-direction:column;gap:18px;width:820px;font-family:J">'
      '<div style="align-self:flex-start;background:#fff;border-radius:6px 30px 30px 30px;padding:26px 34px;font-size:46px;color:#1C1A17;box-shadow:0 10px 30px -14px rgba(0,0,0,.3)">AMIGAAA</div>'
      '<div style="align-self:flex-start;background:#fff;border-radius:6px 30px 30px 30px;padding:26px 34px;font-size:46px;color:#1C1A17;box-shadow:0 10px 30px -14px rgba(0,0,0,.3)">me encanta, es exactamente lo que quería</div>'
      '<div style="align-self:flex-start;background:#fff;border-radius:6px 30px 30px 30px;padding:26px 34px;font-size:46px;color:#1C1A17;box-shadow:0 10px 30px -14px rgba(0,0,0,.3)">¿cuándo lo usamos?</div></div>')

REELS = {
 'dia19-reel-prana-antes-despues': [
   dict(bg='n', text='Le cambié la cara a una marca *en 30 segundos*'),
   dict(bg='m', eb='Antes', html=antes, html_pos='top', text='Colores al azar y *nada de personalidad.*', fs=84),
   dict(bg='m', html=pal, html_pos='top', text='Primero, *los colores.*', fs=110),
   dict(bg='m', html=fonts, html_pos='top', text='Después, *la tipografía.*', fs=110),
   dict(bg='m', kind='reveal', eb='Después', html=logo_p, html_pos='top', text='Y el logo *final.*', fs=110),
   dict(bg='m', html=aplic, html_pos='top', text='Aplicado *en todo.*', fs=110),
   dict(bg='g', kind='end', text='¿Tu marca necesita *un cambio así?*', pill='Escribime · marca de ejemplo'),
 ],
 'dia21-reel-mi-web-por-dentro': [
   dict(bg='n', text='Así se ve mi página web *por dentro*'),
   dict(bg='m', kind='phone', img=W + 'inicio.png', text='Lo primero: *qué hago* y un botón para escribirme.', fs=76),
   dict(bg='m', kind='phone', img=W + 'servicios.png', text='Todos mis *servicios,* claros.', fs=88),
   dict(bg='m', kind='phone', img=W + 'trabajos.png', text='Un trabajo real que *podés probar.*', fs=86),
   dict(bg='m', kind='phone', img=W + 'paquetes.png', text='Los paquetes, para que sepas *por dónde empezar.*', fs=76),
   dict(bg='m', kind='phone', img=W + 'contacto.png', text='Y escribirme es *un solo toque.*', fs=86),
   dict(bg='g', kind='end', text='¿Tu marca tiene *su página?*', pill='El link está en mi bio'),
 ],
 'dia24-reel-halloween-marcas-que-dan-miedo': [
   dict(bg='n', text='Cosas que dan *miedo* en una marca'),
   dict(bg='m', eb='1', html=five, html_pos='top', text='Cinco tipografías *juntas.*', fs=100),
   dict(bg='m', eb='2', html=pix, html_pos='top', text='Un logo *pixelado.*', fs=110),
   dict(bg='m', eb='3', html=nobio, html_pos='top', text='Un perfil *sin bio.*', fs=110),
   dict(bg='m', eb='4', html=e404, html_pos='top', text='El link de la bio *roto.*', fs=100),
   dict(bg='m', eb='5', html=feed, html_pos='top', text='Un feed de *mil colores.*', fs=100),
   dict(bg='g', kind='end', text='¿Cuántas tenía *tu marca?*', pill='Contame sin miedo'),
 ],
 'dia27-reel-pov-propuesta': [
   dict(bg='n', text='POV: le mostrás la propuesta *a tu clienta*'),
   dict(bg='m', kind='reveal', html=h_logo, html_pos='top', text='El logo, *con su personaje.*', fs=96),
   dict(bg='m', html=h_pal, html_pos='top', text='Los colores *de la marca.*', fs=104),
   dict(bg='m', html=h_pat, html_pos='top', text='Un patrón para *todo lo demás.*', fs=96),
   dict(bg='m', html=h_apl, html_pos='top', text='Cómo se ve *en la vida real.*', fs=96),
   dict(bg='m', html=wa, html_pos='top', text='Y después *llega esto.*', fs=110),
   dict(bg='g', kind='end', text='Por esto hago *lo que hago.*', pill='Marca de ejemplo · @goldstudio.ba'),
 ],
}
if __name__ == '__main__':
    for n in (sys.argv[1:] or list(REELS)):
        out, total, work = build(n, REELS[n]); print(n, total)
