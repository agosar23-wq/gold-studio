"""Carrusel: tipos de logo + identidad de marca (marcas de ejemplo)."""
import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
from caro_ejemplos import render, end
from carogen import F, SP
import pack as P

BLUE, SKY, PINKC = '#2E6B66', '#CFE8DE', '#F29C7E'
EXT = f'''
@font-face{{font-family:XArchivo;src:url({F}archivo-black/files/archivo-black-latin-400-normal.woff2)}}
@font-face{{font-family:XPlayfair;src:url({F}playfair-display/files/playfair-display-latin-700-normal.woff2)}}
@font-face{{font-family:XNoto;src:url({F}noto-serif/files/noto-serif-latin-900-normal.woff2)}}
@font-face{{font-family:XFam;src:url({F}familjen-grotesk/files/familjen-grotesk-latin-700-normal.woff2)}}
.lcard{{width:888px;height:600px;border-radius:36px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;box-shadow:0 40px 70px -40px rgba(0,0,0,.5)}}
.cap{{font-size:28px;color:var(--sub);letter-spacing:.04em;margin:0}}
.bgrid{{display:grid;grid-template-columns:1fr 1fr;gap:20px;width:888px}}
.bgrid>div{{border-radius:26px;overflow:hidden;height:250px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:10px;position:relative}}
.bl{{position:absolute;left:22px;top:18px;font-size:20px;letter-spacing:.24em;text-transform:uppercase;font-weight:500;opacity:.75}}
.posts{{display:flex;gap:22px}}
.posts>div{{width:270px;height:270px;border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;text-align:center;box-shadow:0 20px 40px -26px rgba(0,0,0,.5)}}
.lab2{{display:inline-block;align-self:flex-start;font-size:28px;font-weight:500;padding:8px 22px;border-radius:999px;letter-spacing:.06em}}
'''

from mascota import dog, paw
from yogi import yogi
def mascot(color, size, bg=None):
    return dog(color, size, bg or (BLUE if color == '#fff' else '#FBF7F0'))

MAREA = ('<svg width="{s}" height="{s}" viewBox="0 0 100 100" fill="none" stroke-linecap="round">'
         '<path d="M26 52 A24 24 0 0 1 74 52 Z" fill="#F2C38B"/>'
         '<path d="M14 62 q9 -7 18 0 t18 0 t18 0 t18 0 M14 74 q9 -7 18 0 t18 0 t18 0 t18 0 M24 86 q9 -7 18 0 t18 0 t18 0" stroke="#F4EDE2" stroke-width="4.5"/></svg>')

YOGI = ('<svg width="{s}" height="{s}" viewBox="0 0 100 100" fill="none" stroke="{c}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">'
        '<circle cx="50" cy="19" r="7.5" fill="{c}" stroke="none"/>'
        '<path d="M50 29 C44 29 39 31 38 35 C37 43 42 50 44 62 M50 29 C56 29 61 31 62 35 C63 43 58 50 56 62"/>'
        '<path d="M38 35 C33 41 31 48 32 53 C33 58 27 61 23 63 M62 35 C67 41 69 48 68 53 C67 58 73 61 77 63"/>'
        '<path d="M25 63 q-2 3 1 4 M75 63 q2 3 -1 4"/>'
        '<path d="M14 70 C24 60 40 60 50 66 C60 60 76 60 86 70 C74 78 60 78 50 72 C40 78 26 78 14 70 Z"/>'
        '<path d="M44 26 q6 3 12 0" stroke-width="0"/>'
        '<path d="M22 12 l1.2 3 l3 1.2 l-3 1.2 l-1.2 3 l-1.2 -3 l-3 -1.2 l3 -1.2 Z M78 10 l1 2.4 l2.4 1 l-2.4 1 l-1 2.4 l-1 -2.4 l-2.4 -1 l2.4 -1 Z" fill="{c}" stroke="none"/></svg>')

LEAF = ('<svg width="{s}" height="{s}" viewBox="0 0 100 100"><path d="M50 8 C82 24 86 66 50 92 C14 66 18 24 50 8 Z" fill="{c}"/>'
        '<path d="M50 22 L50 90 M50 44 L36 34 M50 44 L64 34 M50 62 L34 50 M50 62 L66 50" stroke="{l}" stroke-width="3" stroke-linecap="round" fill="none"/></svg>')

def mono(s=1.0, c='#B8923A'):
    w, h = int(300*s), int(420*s)
    return (f'<div style="width:{w}px;height:{h}px;border:{max(2,int(4*s))}px solid {c};border-radius:{w}px;display:grid;place-items:center;position:relative">'
            f'<div style="position:absolute;inset:{int(16*s)}px;border:{max(1,int(2*s))}px solid {c};border-radius:{w}px"></div>'
            f'<span style="font-family:B;font-style:italic;font-size:{int(250*s)}px;line-height:1;color:{c};margin-top:-{int(20*s)}px">A</span></div>')

def ex(txt): return f'<p class="cap">Ejemplo: {txt}</p>'
def tipo(n, name, title, card, txt, exm):
    return ('m', f'<div class="eb">Tipo {n} · {name}</div><h2>{title}</h2>{card}<p class="body" style="margin:0">{txt}</p>{ex(exm)}', 'gap:30px')

lumbre = '<div class="lcard" style="background:#FBF0E6"><span style="font-family:XPlayfair;font-size:150px;color:#B5562F;letter-spacing:.01em">Lumbre</span><span style="font-size:24px;letter-spacing:.5em;color:#B5562F">VELAS</span></div>'
marea = f'<div class="lcard" style="background:#1F3B4D">{MAREA.format(s=360)}</div>'
luna = f'<div class="lcard" style="background:#3E3557;color:#D9CFF0">{yogi("#D9CFF0", 270)}<span style="font-family:B;font-size:110px;line-height:1;letter-spacing:.04em">Prana</span><span style="font-size:22px;letter-spacing:.4em">ESTUDIO DE YOGA</span></div>'
aura = f'<div class="lcard" style="background:#FAF6EE;border:2px solid #E6DAC2">{mono(1.0)}<span style="font-size:24px;letter-spacing:.4em;color:#8A6A22">AURA · JOYERÍA</span></div>'
grano = f'<div class="lcard" style="background:{BLUE};color:#fff">{mascot("#fff", 380)}<span style="font-family:XFam;font-size:60px;color:#fff;margin-top:6px">huellitas</span></div>'

# --- portada: logo suelto vs identidad completa
cover = ('m', '<div class="eb">Branding</div><h1 style="font-size:104px">Tener un logo no es tener <em>una marca</em></h1>'
         '<div style="display:flex;align-items:center;gap:30px;margin-top:20px">'
         f'<div style="width:300px;height:300px;border-radius:26px;background:#fff;display:grid;place-items:center;box-shadow:0 30px 60px -36px rgba(0,0,0,.5)">{mascot(BLUE, 230, "#fff")}</div>'
         '<span style="font-family:B;font-size:110px;color:#8A6A22">≠</span>'
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;width:440px">'
         f'<div style="height:180px;border-radius:18px;background:{BLUE};display:grid;place-items:center">{mascot("#fff", 140)}</div>'
         f'<div style="height:180px;border-radius:18px;overflow:hidden;display:flex"><i style="flex:1;background:{BLUE}"></i><i style="flex:1;background:{SKY}"></i><i style="flex:1;background:{PINKC}"></i><i style="flex:1;background:#FBF7F0;border:2px solid #E6E1D6;border-left:none"></i></div>'
         f'<div style="height:180px;border-radius:18px;background:{SKY};display:grid;place-items:center;font-family:XFam;font-size:84px;color:{BLUE}">Aa</div>'
         f'<div style="height:180px;border-radius:18px;background:#FBF7F0;display:grid;place-items:center">{mascot(BLUE, 70)}<span style="font-family:XFam;font-size:26px;color:{BLUE};margin-top:-30px">huellitas</span></div>'
         '</div></div><p class="body" style="margin:0">Primero, los 5 tipos de logo. Después, lo que lo convierte en marca.</p>', '')

types = [
    tipo(1, 'Logotipo', 'Solo <em>letras</em>', lumbre, 'Funciona cuando el nombre es corto y fácil de recordar.', 'Lumbre, velas artesanales'),
    tipo(2, 'Isotipo', 'Solo <em>el dibujo</em>', marea, 'Ideal para la foto de perfil o cuando la marca ya es conocida.', 'Marea, trajes de baño'),
    tipo(3, 'Imagotipo', 'Dibujo <em>+ nombre</em>', luna, 'El más usado: se entiende aunque nadie te conozca todavía.', 'Prana, estudio de yoga'),
    tipo(4, 'Monograma', 'Tus <em>iniciales</em>', aura, 'Elegante y perfecto para marcas personales o de lujo.', 'Aura, joyería'),
    tipo(5, 'Mascota', 'Un <em>personaje</em>', grano, 'Le da personalidad y cercanía. Es lo que más se recuerda.', 'Huellitas, tienda de mascotas'),
]

# --- identidad completa de Grano
pattern = ''.join(f'<span style="position:absolute;left:{x}px;top:{y}px">{paw(BLUE, 36, r)}</span>'
                  for x, y, r in [(40,50,-20),(150,36,25),(260,70,-35),(360,40,15),(80,140,30),(200,130,-15),(310,160,40),(390,120,-25),(30,205,10),(150,200,-30),(260,215,20),(380,200,0)])
board = ('m', '<div class="eb">Identidad de marca</div><h2>El logo es <em>solo una parte</em></h2><div class="bgrid">'
         f'<div style="background:{BLUE};color:#fff"><span class="bl">Logo</span>{mascot("#fff", 170)}<span style="font-family:XFam;font-size:34px;margin-top:0">huellitas</span></div>'
         f'<div style="flex-direction:row;gap:0;align-items:stretch"><i style="flex:1;background:{BLUE}"></i><i style="flex:1;background:{SKY}"></i><i style="flex:1;background:{PINKC}"></i><i style="flex:1;background:#FBF7F0;border:2px solid #E6E1D6;border-left:none"></i><span class="bl" style="color:#fff">Colores</span></div>'
         f'<div style="background:#FBF7F0;color:{BLUE};border:2px solid #E6E1D6"><span class="bl">Tipografías</span><span style="font-family:XFam;font-size:60px;line-height:1">Aa Huellitas</span><span style="font-family:J;font-size:30px">Para los textos, una simple</span></div>'
         f'<div style="background:{SKY}"><span class="bl" style="color:{BLUE};z-index:2">Patrón</span>{pattern}</div>'
         f'<div style="background:{SKY};color:{BLUE}"><span class="bl">Aplicaciones</span><div style="display:flex;gap:26px;align-items:flex-end">'
         f'<div style="width:96px;height:130px;background:#fff;border-radius:6px 6px 22px 22px;display:grid;place-items:center">{mascot(BLUE, 80, "#fff")}</div>'
         f'<div style="width:150px;height:96px;background:{BLUE};border-radius:8px;display:grid;place-items:center;font-family:XFam;font-size:30px;color:#fff">huellitas</div></div></div>'
         f'<div style="background:#FBF7F0;color:{BLUE};border:2px solid #E6E1D6"><span class="bl">Su voz</span><span style="font-family:B;font-style:italic;font-size:44px;text-align:center;line-height:1.15;padding:0 30px">"Todo para tu<br>mejor amigo"</span></div>'
         '</div><p class="body" style="margin:0">Colores, letras, patrón, aplicaciones y forma de hablar. Todo junto es la identidad.</p>', 'gap:28px')

def post(bg, fg, font, txt, art=''):
    return f'<div style="background:{bg};color:{fg}">{art}<span style="font-family:{font};font-size:34px;line-height:1.1;padding:0 18px">{txt}</span></div>'
mal = (post('#D64545', '#fff', 'XPlayfair', 'Promo de hoy') + post('#2E8B57', '#FFE14D', 'XArchivo', 'LLEGÓ LO NUEVO') + post('#F2D14B', '#6A2C91', 'XNoto', 'Turnos de baño'))
bien = (post(BLUE, '#fff', 'XFam', 'Promo de hoy', mascot('#fff', 130)) + post(SKY, BLUE, 'XFam', 'Llegó lo nuevo', mascot(BLUE, 130, SKY)) + post('#FBF7F0', BLUE, 'XFam', 'Turnos de baño', mascot(BLUE, 130)))
consist = ('m', '<h2>La misma marca, <em>¿se reconoce?</em></h2>'
           f'<span class="lab2" style="background:#C0392B;color:#fff">Así no</span><div class="posts">{mal}</div>'
           f'<span class="lab2" style="background:#1C1A17;color:#FAF6EE">Así sí</span><div class="posts">{bien}</div>'
           '<p class="body" style="margin:0">Sin identidad, cada posteo parece de una marca distinta.</p>', 'gap:26px')

slides = [cover] + types + [board, consist, end('¿Tu marca tiene *identidad* o solo un logo?', 'Escribime y la armamos juntas')]
if __name__ == '__main__':
    print(render('carrusel-logos-e-identidad', slides, EXT))
