"""Los 5 posteos que faltaban, hechos sin fotos: día en Gold Studio, nombre de marca, WhatsApp Business, etiquetas, kit."""
import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
from reelgen import build, SCR
from caro_ejemplos import render, end
from carogen import CHECK
import catalogo_wa2 as K, portada_wa4 as D, mocks as M
from semana3_carruseles import igp, EXT as CEXT
from yogi import yogi
PH = lambda inner, w=420, h=820: K.phone(inner, w, h)
CAT = '/home/user/gold-studio-final/whatsapp-business/catalogo/'
PHCSS = '<style>.ph{border-radius:54px;background:#1C1A17;padding:14px;box-shadow:0 40px 70px -36px rgba(0,0,0,.6);flex:none}.ph>div{border-radius:42px;overflow:hidden;background:#fff;position:relative}</style>'
def scene(inner, w=820, h=560, bg='linear-gradient(135deg,#F5EFE4,#EDE4D3)'):
    return f'{PHCSS}<div style="position:relative;width:{w}px;height:{h}px;border-radius:36px;overflow:hidden;background:{bg}">{inner}</div>'
ab = D.ab
# ---------------- 1) Un día en Gold Studio ----------------
lista = ('<div style="width:300px;height:380px;background:#FFFDF8;border-radius:10px;box-shadow:0 30px 50px -20px rgba(60,40,10,.35);padding:30px 26px;font-family:J;color:#1C1A17;display:flex;flex-direction:column;gap:16px">'
         '<b style="font-family:B;font-weight:500;font-size:34px">Hoy</b>' + ''.join(f'<div style="display:flex;gap:12px;align-items:center;font-size:22px"><span style="width:22px;height:22px;border:2px solid #8A6A22;border-radius:6px;{"background:#C9A34E" if d else ""}"></span>{t}</div>' for t, d in [('Diseño web', 1), ('Bocetos logo', 0), ('Contenido redes', 0), ('Responder mensajes', 0)]) + '</div>')
s_cafe = scene(ab(120, 90, lista, -6) + ab(470, 170, D.coffee, 0) + ab(420, 60, D.pencil, 30))
s_web = scene(ab(40, 20, D.laptop, -3).replace('width:600px', 'width:600px;transform:scale(1.15);transform-origin:top left'), h=600)
s_boceto = scene(ab(250, 40, D.note, 4), h=520)
s_redes = scene(ab(270, 20, PH(K.ig, 280, 540), 0), h=600)
chatv = ('<div style="height:100%;background:#EFE7DD;padding:70px 18px 20px;display:flex;flex-direction:column;gap:10px;font-family:J;font-size:17px;color:#1C1A17">'
         '<div style="position:absolute;left:0;right:0;top:0;height:56px;background:#1C1A17;color:#FAF6EE;display:flex;align-items:center;padding:0 18px;font-size:18px">Consultas</div>'
         + ''.join(f'<div style="align-self:{a};background:{b};border-radius:14px;padding:10px 14px;max-width:80%">{t}</div>' for a, b, t in [('flex-start', '#fff', 'Hola! Vi tu página, ¿hacés logos?'), ('flex-end', '#F2E3C0', '¡Hola! Sí, te paso el catálogo ✦'), ('flex-start', '#fff', '¿Y páginas web también?'), ('flex-end', '#F2E3C0', 'También, te cuento todo')]) + '</div>')
s_chat = scene(ab(270, 20, PH(chatv, 280, 540), 0), h=600)
noche = scene(ab(130, 90, '<div style="width:560px;height:340px;border-radius:18px;background:#3A342B;box-shadow:0 30px 50px -20px rgba(0,0,0,.6);display:grid;place-items:center"><div style="width:120px;height:120px;color:#C9A34E">' + K.SP + '</div></div>', -4)
              + ab(600, 330, '<div style="width:120px;height:160px;border-radius:12px;background:#FAF6EE;box-shadow:0 0 60px 20px rgba(201,163,78,.35);display:grid;place-items:center"><div style="width:14px;height:40px;border-radius:50% 50% 40% 40%;background:#E8A33A;margin-top:-90px"></div></div>', 0),
              bg='linear-gradient(135deg,#2A2621,#1C1A17)')
DIA = [
 dict(bg='n', text='Un día en *Gold Studio*', sub='Sin mostrar mi cara'),
 dict(bg='m', eb='9:00', html=s_cafe, html_pos='top', text='Café y la lista *de pendientes.*', fs=96),
 dict(bg='m', eb='10:30', html=s_web, html_pos='top', text='Diseño una *página web.*', fs=104),
 dict(bg='m', eb='13:00', html=s_boceto, html_pos='top', text='Bocetos para *un logo nuevo.*', fs=100),
 dict(bg='m', eb='16:00', html=s_redes, html_pos='top', text='Contenido *para redes.*', fs=104),
 dict(bg='m', eb='18:00', html=s_chat, html_pos='top', text='Respondo *consultas.*', fs=104),
 dict(bg='n', eb='21:00', html=noche, html_pos='top', text='Cierro la compu, *contenta.*', fs=100),
 dict(bg='g', kind='end', text='¿Cómo es *tu día?*', pill='Contame abajo'),
]
# ---------------- 2) Cómo elegir el nombre ----------------
def hoja(lines):
    rows = ''.join(f'<div style="font-family:B;font-style:italic;font-size:48px;color:#3B3122;{"text-decoration:line-through;opacity:.45" if x else ""}">{t}{" ✓" if ok else ""}</div>' for t, x, ok in lines)
    return ('<div style="width:620px;background:#FFFDF8;border-radius:10px 22px 22px 10px;box-shadow:0 30px 50px -20px rgba(60,40,10,.35);padding:40px 50px 40px 80px;position:relative;display:flex;flex-direction:column;gap:14px;'
            'background-image:repeating-linear-gradient(#FFFDF8 0 63px,#EDE5D6 63px 65px)"><div style="position:absolute;left:0;top:0;bottom:0;width:30px;background:#E8DFCF;border-radius:10px 0 0 10px"></div>'
            '<div style="font-size:22px;letter-spacing:.24em;color:#8A6A22;font-family:J">NOMBRES · PANADERÍA</div>' + rows + '</div>')
largo = ('<div style="display:flex;flex-direction:column;gap:30px;align-items:flex-start">'
         '<span style="font-family:J;font-size:56px;color:#1C1A17;opacity:.4;text-decoration:line-through">Panadería Artesanal Los Abuelos</span>'
         '<span style="font-family:B;font-size:160px;line-height:1;color:#1C1A17">Miga ✓</span></div>')
ig = ('<div style="width:640px;background:#fff;border-radius:30px;padding:30px;box-shadow:0 30px 50px -24px rgba(0,0,0,.35);font-family:J;display:flex;flex-direction:column;gap:22px">'
      '<div style="background:#EFEFEF;border-radius:14px;padding:16px 22px;font-size:30px;color:#555">⌕  miga</div>'
      + ''.join(f'<div style="display:flex;justify-content:space-between;align-items:center;font-size:30px"><span><b>@{u}</b></span><span style="color:{c};font-size:26px">{s}</span></div>' for u, s, c in [('miga', 'ocupado', '#C0392B'), ('miga.panaderia', 'disponible ✓', '#2E8B57'), ('somosmiga', 'disponible ✓', '#2E8B57')]) + '</div>')
miga_logo = ('<div style="width:700px;height:460px;border-radius:36px;background:#E9C9A0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:#5A3A1E">'
             '<svg width="150" height="110" viewBox="0 0 150 110" fill="none" stroke="#5A3A1E" stroke-width="5" stroke-linecap="round"><path d="M15 80 C15 30 135 30 135 80 Z"/><path d="M50 50 L58 70 M75 45 L75 68 M100 50 L92 70"/></svg>'
             '<span style="font-family:B;font-size:130px;line-height:1">Miga</span><span style="font-size:24px;letter-spacing:.4em">PANADERÍA</span></div>')
opin = ('<div style="display:flex;flex-direction:column;gap:16px;width:760px;font-family:J">' + ''.join(f'<div style="align-self:flex-start;background:#fff;border-radius:6px 26px 26px 26px;padding:20px 28px;font-size:38px;box-shadow:0 10px 30px -14px rgba(0,0,0,.3)">{t}</div>' for t in ['"Miga" me encanta, es re fácil', 'Suena rico jaja', 'Me lo acuerdo al toque']) + '</div>')
NOMBRE = [
 dict(bg='n', text='Cómo elegir el nombre de *tu marca*'),
 dict(bg='m', eb='1', html=hoja([('Dulces Abuelos', 1, 0), ('La Panera Artesanal', 1, 0), ('Pan y Más', 1, 0), ('Miga', 0, 1)]), html_pos='top', text='Escribí *muchas* opciones.', fs=100),
 dict(bg='m', eb='2', html=largo, html_pos='top', text='Corto y *fácil de decir.*', fs=104),
 dict(bg='m', eb='3', html=ig, html_pos='top', text='Fijate que *esté libre.*', fs=104),
 dict(bg='m', eb='4', kind='reveal', html=miga_logo, html_pos='top', text='Imaginalo *como logo.*', fs=104),
 dict(bg='m', eb='5', html=opin, html_pos='top', text='Decilo en voz alta y preguntá *a 3 personas.*', fs=84),
 dict(bg='g', kind='end', text='¿Cómo elegiste *el nombre de tu marca?*', pill='Miga es una marca de ejemplo'),
]
# ---------------- 3) WhatsApp Business ----------------
def wa(title, body):
    return (f'<div style="height:100%;background:#F4F1EC;font-family:J;color:#1C1A17">'
            f'<div style="height:64px;background:#1C1A17;color:#FAF6EE;display:flex;align-items:center;gap:12px;padding:0 20px;font-size:20px">‹ <b style="font-weight:500">{title}</b></div>{body}</div>')
cat_items = ''.join(f'<div style="display:flex;gap:14px;align-items:center;padding:12px 18px;border-bottom:1px solid #E6DAC2;background:#fff"><img src="file://{CAT}{d}/1-portada.png" style="width:78px;height:78px;border-radius:10px"><div style="font-size:18px"><b style="font-weight:500">{n}</b><div style="color:#8A7F6E;font-size:15px">Consultar precio</div></div></div>'
                    for d, n in [('01-pagina-web', 'Página web'), ('02-branding', 'Branding y logo'), ('03-community-manager', 'Community manager'), ('04-app-a-medida', 'App a medida'), ('05-tienda-online', 'Tienda online')])
w_cat = wa('Catálogo', '<div style="padding:16px 18px;font-size:15px;color:#8A7F6E">5 artículos</div>' + cat_items)
w_quick = wa('Respuestas rápidas', ''.join(f'<div style="padding:14px 20px;border-bottom:1px solid #E6DAC2;background:#fff"><b style="color:#8A6A22;font-size:19px">/{k}</b><div style="font-size:15px;color:#5E5649;margin-top:4px">{t}</div></div>'
                    for k, t in [('precios', 'Cada proyecto es distinto, así que te armo un presupuesto...'), ('proceso', 'Así trabajamos: 1. Charlamos 2. Propuesta...'), ('trabajos', 'Podés ver mis trabajos acá: goldstudio-ba...'), ('datos', 'Para arrancar necesito: nombre de tu marca...'), ('gracias', '¡Gracias por confiar en Gold Studio!')]))
w_away = wa('Mensaje de ausencia', '<div style="padding:20px;display:flex;flex-direction:column;gap:14px;font-size:17px">'
            '<div style="background:#fff;border-radius:14px;padding:16px">¡Hola! Ahora no estoy conectada, pero mañana a primera hora te respondo ✦</div>'
            '<div style="display:flex;justify-content:space-between;background:#fff;border-radius:14px;padding:14px 16px"><span>Enviar</span><b style="font-weight:500;color:#8A6A22">Fuera del horario</b></div>'
            '<div style="display:flex;justify-content:space-between;background:#fff;border-radius:14px;padding:14px 16px"><span>Horario</span><b style="font-weight:500">Lun a vie · 10 a 19 h</b></div></div>')
WAB = [
 dict(bg='n', text='3 cosas que tenés que configurar en tu *WhatsApp Business*', fs=104),
 dict(bg='m', eb='1', html=PHCSS + PH(w_cat, 400, 780), html_pos='top', text='El *catálogo.*', fs=120),
 dict(bg='m', eb='2', html=PHCSS + PH(w_quick, 400, 780), html_pos='top', text='Respuestas *rápidas.*', fs=120),
 dict(bg='m', eb='3', html=PHCSS + PH(w_away, 400, 780), html_pos='top', text='Mensaje de *ausencia.*', fs=120),
 dict(bg='g', kind='end', text='Guardalo y configuralo *hoy*', pill='Si querés, te ayudo'),
]
# ---------------- 4) Kit para arrancar tu marca ----------------
pal = '<div style="display:flex;gap:18px">' + ''.join(f'<i style="width:170px;height:280px;border-radius:28px;background:{c};box-shadow:inset 0 0 0 2px rgba(0,0,0,.06)"></i>' for c in ['#3E3557', '#D9CFF0', '#E8DCC8', '#F7F4EF']) + '</div>'
logo_k = f'<div style="width:700px;height:460px;border-radius:36px;background:#3E3557;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px">{yogi("#D9CFF0", 240)}<span style="font-family:B;font-size:100px;color:#D9CFF0;line-height:1">Prana</span></div>'
plantillas = '<div style="display:flex;gap:16px">' + ''.join(f'<div style="width:250px;height:310px;border-radius:14px;background:{b};color:{f};display:flex;flex-direction:column;justify-content:center;align-items:center;gap:10px;font-family:B;font-size:38px;text-align:center;box-shadow:0 20px 40px -24px rgba(0,0,0,.5)">{t}</div>' for b, f, t in [('#3E3557', '#D9CFF0', 'Clases<br><i>de esta semana</i>'), ('#F7F4EF', '#3E3557', '<i>Tip</i><br>respirá'), ('#D9CFF0', '#3E3557', 'Reservá<br>tu lugar')]) + '</div>'
KIT = [
 dict(bg='n', text='El kit para arrancar *tu marca*'),
 dict(bg='m', eb='1', kind='reveal', html=logo_k, html_pos='top', text='Un logo *con variantes.*', fs=104),
 dict(bg='m', eb='2', html=pal, html_pos='top', text='Tu paleta *de colores.*', fs=104),
 dict(bg='m', eb='3', html=PHCSS + igp(4, 400), html_pos='top', text='Un perfil *ordenado.*', fs=104),
 dict(bg='m', eb='4', html=M.site('clara', 2, 820), html_pos='top', text='Tu *página web.*', fs=110),
 dict(bg='m', eb='5', html=PHCSS + PH(w_cat, 360, 700), html_pos='top', text='WhatsApp Business *con catálogo.*', fs=92),
 dict(bg='m', eb='6', html=plantillas, html_pos='top', text='Plantillas *para redes.*', fs=104),
 dict(bg='g', kind='end', text='¿Cuántas *ya tenés?*', pill='Contame abajo'),
]
# ---------------- 5) Carrusel: la etiqueta de tu producto ----------------
HON, DARK, CRM = '#E3A82B', '#4A3416', '#FFF8E8'
def label(hl=None, w=820, bg=CRM, accent=HON, flavor='Miel pura'):
    s = w / 820
    px = lambda v: int(v * s)
    o = lambda k: f'outline:{px(6)}px solid #C9A34E;outline-offset:{px(6)}px;border-radius:{px(12)}px;' if hl == k else ''
    bee = (f'<svg width="{px(90)}" height="{px(90)}" viewBox="0 0 100 100" fill="none" stroke="{DARK}" stroke-width="4"><path d="M50 15 L80 32 L80 68 L50 85 L20 68 L20 32 Z" fill="{accent}"/>'
           f'<path d="M35 45 H65 M33 55 H67 M37 65 H63"/></svg>')
    return (f'<div style="width:{w}px;height:{px(470)}px;background:{bg};border-radius:{px(26)}px;box-shadow:0 40px 60px -34px rgba(0,0,0,.5);display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:{px(34)}px {px(40)}px;box-sizing:border-box;color:{DARK};font-family:J;border:{px(10)}px solid {accent}">'
            f'<div style="display:flex;flex-direction:column;align-items:center;gap:{px(4)}px;{o("logo")}padding:{px(4)}px {px(14)}px">{bee}<span style="font-family:B;font-size:{px(64)}px;line-height:1">Monte Dulce</span></div>'
            f'<div style="text-align:center;{o("prod")}padding:{px(4)}px {px(14)}px"><div style="font-family:B;font-style:italic;font-size:{px(44)}px">{flavor}</div><div style="font-size:{px(20)}px;letter-spacing:.3em">DE ABEJA · ARTESANAL</div></div>'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-end;width:100%;font-size:{px(17)}px">'
            f'<div style="{o("datos")}padding:{px(6)}px {px(10)}px;line-height:1.5">Contenido neto 500 g<br>Vence: 03/2027 · Lote 0142</div>'
            f'<div style="{o("contacto")}padding:{px(6)}px {px(10)}px;display:flex;gap:{px(12)}px;align-items:center"><span>@montedulce</span><div style="width:{px(64)}px;height:{px(64)}px;background:repeating-conic-gradient({DARK} 0 25%,{bg} 0 50%) 0 0/{px(16)}px {px(16)}px"></div></div></div></div>')
def lstep(n, t, hl, tip):
    return ('m', f'<div class="eb">{n} de 5</div><h2 style="font-size:70px">{t}</h2><div style="display:flex;justify-content:center;margin-top:20px">{label(hl)}</div><p class="tip2">{tip}</p>', 'gap:30px')
variants = '<div style="display:flex;flex-direction:column;gap:18px;align-items:center">' + ''.join(label(None, 560, b, a, f) for b, a, f in [(CRM, HON, 'Miel pura'), ('#F3F0E6', '#8BA35B', 'Miel con limón'), ('#F7ECE6', '#C0663A', 'Miel con canela')]) + '</div>'
ETIQ = [
 ('m', f'<div class="eb">Guardalo</div><h1 style="font-size:92px">Lo que tiene que tener <em>la etiqueta de tu producto</em></h1><div style="display:flex;justify-content:center;margin-top:20px">{label()}</div>', 'gap:30px'),
 lstep(1, 'Tu logo, <em>bien visible</em>', 'logo', 'Es lo que hace que te reconozcan en una góndola o en una foto.'),
 lstep(2, 'Qué es <em>el producto</em>', 'prod', 'Que se entienda en un segundo, aunque no te conozcan.'),
 lstep(3, 'Los <em>datos</em>', 'datos', 'Contenido, vencimiento y lote. Chequeá cuáles te pide tu rubro.'),
 lstep(4, 'Cómo <em>encontrarte</em>', 'contacto', 'Tu usuario o un QR a tu catálogo, para que te vuelvan a comprar.'),
 ('m', f'<div class="eb">5 de 5</div><h2 style="font-size:70px">Una familia <em>que combina</em></h2><div style="transform:scale(.82);transform-origin:top center;height:900px">{variants}</div>', 'gap:20px;justify-content:flex-start;padding-top:90px'),
 end('¿Tu producto tiene *etiqueta propia?*', 'Monte Dulce es una marca de ejemplo'),
]
if __name__ == '__main__':
    what = sys.argv[1:] or ['dia', 'nombre', 'wab', 'kit', 'etiq']
    R = {'dia': ('dia18-reel-un-dia-en-gold-studio', DIA), 'nombre': ('dia25-reel-como-elegir-el-nombre', NOMBRE), 'wab': ('dia26-reel-whatsapp-business', WAB), 'kit': ('dia29-reel-kit-para-arrancar-tu-marca', KIT)}
    for w in what:
        if w in R: print(build(*R[w])[:2])
    if 'etiq' in what: print(render('dia27-carrusel-etiqueta-de-tu-producto', ETIQ, CEXT))
