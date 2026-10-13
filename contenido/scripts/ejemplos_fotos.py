"""Ejemplos del catálogo con fotos reales y las marcas de marcas_ejemplo:
página web de Almendra, Instagram de Nácar y tienda online de Ondina."""
import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import SCR
from marcas_ejemplo import LOGOS, BRANDS
from mockups_marcas import OUT as MK, SRC

FOT = SCR + '/fotos-pexels/'
foto = lambda i: f'file://{FOT}{i}.jpg'
mk = lambda n: f'file://{MK}{n}.jpg'
lg = lambda n: f'file://{LOGOS}/{n}.png'
col = lambda b, i: BRANDS[b]['colores'][i][1]

def bgimg(u, pos='50% 50%', extra=''):
    return f'background:url({u}) {pos}/cover no-repeat;{extra}'

def phone(inner, w=300, h=600):
    return (f'<div style="width:{w}px;border-radius:44px;background:#1C1A17;padding:11px;box-shadow:0 40px 70px -30px rgba(0,0,0,.7);flex:none">'
            f'<div style="height:{h - 22}px;border-radius:34px;overflow:hidden;background:#fff;position:relative">{inner}</div></div>')

def browser(inner, w=780, url=''):
    dots = ''.join(f'<i style="width:11px;height:11px;border-radius:50%;background:{c};display:block"></i>' for c in ('#E5A39A', '#E8CB86', '#A9C79B'))
    return (f'<div style="width:{w}px;border-radius:14px;overflow:hidden;background:#fff;box-shadow:0 40px 80px -36px rgba(0,0,0,.7);flex:none">'
            f'<div style="height:34px;background:#EFEAE2;display:flex;align-items:center;gap:7px;padding:0 14px">{dots}'
            f'<span style="margin-left:14px;background:#fff;border-radius:6px;padding:3px 14px;font-size:12px;color:#7A7166">{url}</span></div>{inner}</div>')

# ---------------- Página web: Almendra ----------------
CA, AL, CR = col('almendra', 0), col('almendra', 1), col('almendra', 2)
PRODS_A = [('1775034', 'Medialunas de manteca', '$1.200'), ('2000498', 'Pan brioche', '$4.500'), ('192933', 'Facturas surtidas', '$9.800')]
desk_a = (f'<div style="background:{CR};font-family:J">'
          f'<div style="display:flex;align-items:center;justify-content:space-between;padding:14px 30px">'
          f'<img src="{lg("almendra-word-dark")}" style="height:40px">'
          f'<div style="display:flex;gap:22px;font-size:13px;color:{CA};letter-spacing:.08em">Inicio<span>Productos</span><span>Nosotros</span><span>Contacto</span></div>'
          f'<span style="background:{CA};color:{CR};border-radius:999px;padding:7px 16px;font-size:12px">Pedí por WhatsApp</span></div>'
          f'<div style="height:250px;position:relative;{bgimg(foto("30403209"), "50% 55%")}">'
          f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(74,38,34,.85),rgba(74,38,34,.25) 70%)"></div>'
          f'<div style="position:absolute;left:40px;top:50px;color:{CR};display:flex;flex-direction:column;gap:12px">'
          f'<span style="font-size:11px;letter-spacing:.4em">PASTELERÍA DE AUTOR</span>'
          f'<span style="font-family:P;font-style:italic;font-size:46px;line-height:1.05">Hecho a mano,<br>cada mañana</span>'
          f'<span style="align-self:flex-start;background:{CR};color:{CA};border-radius:999px;padding:8px 18px;font-size:12px;margin-top:6px">Ver productos</span></div></div>'
          f'<div style="padding:18px 30px 22px"><div style="font-family:P;font-style:italic;font-size:24px;color:{CA};margin-bottom:12px">Nuestros favoritos</div>'
          '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px">' +
          ''.join(f'<div style="background:#fff;border-radius:10px;overflow:hidden"><div style="height:96px;{bgimg(foto(i))}"></div>'
                  f'<div style="padding:8px 10px;font-size:12px;color:{CA};display:flex;justify-content:space-between"><span>{n}</span><b>{p}</b></div></div>' for i, n, p in PRODS_A) +
          '</div></div></div>')
mob_a = (f'<div style="background:{CR};height:100%;font-family:J;position:relative">'
         f'<div style="display:flex;justify-content:space-between;align-items:center;padding:16px 16px 10px"><img src="{lg("almendra-word-dark")}" style="height:30px"><span style="font-size:20px;color:{CA}">☰</span></div>'
         f'<div style="height:220px;position:relative;{bgimg(foto("30403209"), "50% 50%")}"><div style="position:absolute;inset:0;background:rgba(74,38,34,.5)"></div>'
         f'<div style="position:absolute;left:16px;bottom:18px;color:{CR}"><div style="font-size:9px;letter-spacing:.35em">PASTELERÍA DE AUTOR</div>'
         f'<div style="font-family:P;font-style:italic;font-size:28px;line-height:1.05;margin-top:6px">Hecho a mano,<br>cada mañana</div></div></div>'
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:14px">' +
         ''.join(f'<div style="background:#fff;border-radius:10px;overflow:hidden"><div style="height:92px;{bgimg(foto(i))}"></div><div style="padding:6px 8px;font-size:10px;color:{CA}">{n}<br><b>{p}</b></div></div>' for i, n, p in PRODS_A[:2]) +
         '</div><div style="position:absolute;right:14px;bottom:16px;width:50px;height:50px;border-radius:50%;background:#25D366;box-shadow:0 8px 16px -6px rgba(0,0,0,.4)"></div></div>')
web_ex = (f'<div style="position:relative;width:900px;height:600px">{browser(desk_a, 760, "almendrapasteleria.com.ar")}'
          f'<div style="position:absolute;right:0;bottom:-10px">{phone(mob_a, 250, 520)}</div></div>')

# ---------------- Instagram: Nácar ----------------
NC, NN, NP = col('nacar', 0), col('nacar', 1), col('nacar', 2)
def tile_txt(bg, fg, t, small=''):
    return (f'<div style="aspect-ratio:1;background:{bg};color:{fg};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:6px">'
            f'<span style="font-family:B;font-size:16px;line-height:1.1">{t}</span>' + (f'<span style="font-size:7px;letter-spacing:.25em;margin-top:5px">{small}</span>' if small else '') + '</div>')
def tile_img(u, pos='50% 50%'): return f'<div style="aspect-ratio:1;{bgimg(u, pos)}"></div>'
grid_n = [tile_img(mk('nacar-bolsa')), tile_txt(NC, NP, 'Tu momento<br><i>de calma</i>'), tile_img(f'file://{SRC}7795646.jpg', '50% 40%'),
          tile_img(mk('nacar-frascos')), tile_img(mk('nacar-tarjetas'), '50% 30%'), tile_txt(NN, '#fff', 'Turnos<br>abiertos', 'OCTUBRE'),
          tile_txt(NP, NC, '3 tips para<br><i>tu piel</i>'), tile_img(mk('nacar-bolsas'), '60% 50%'), tile_img(f'file://{SRC}7795646.jpg', '50% 85%')]
hl = [(NC, 'iso-light', 'Servicios'), (NN, 'iso-light', 'Turnos'), (NP, 'iso-dark', 'Clientas'), (NC, 'iso-light', 'Tips')]
ig_n = ('<div style="font-family:J;color:#1C1A17;background:#fff;height:100%">'
        '<div style="padding:16px 14px 0;display:flex;gap:16px;align-items:center">'
        f'<div style="width:72px;height:72px;border-radius:50%;background:{NC};display:grid;place-items:center;border:2px solid #fff;box-shadow:0 0 0 2px {NN}"><img src="{lg("nacar-iso-light")}" style="width:44px"></div>'
        '<div style="display:flex;gap:16px;font-size:12px;text-align:center">' + ''.join(f'<div><b style="display:block;font-size:16px">{n}</b>{t}</div>' for n, t in [('186', 'posts'), ('5.320', 'seguidores'), ('214', 'seguidos')]) + '</div></div>'
        '<div style="padding:8px 14px;font-size:12px;line-height:1.4"><b>Nácar · Estética & Spa</b><br>Faciales, masajes y rituales de calma.<br>Turnos por WhatsApp</div>'
        '<div style="display:flex;gap:6px;padding:0 14px 8px"><span style="flex:1;background:#EFEFEF;border-radius:8px;padding:6px;font-size:11px;text-align:center"><b>Seguir</b></span><span style="flex:1;background:#EFEFEF;border-radius:8px;padding:6px;font-size:11px;text-align:center"><b>Mensaje</b></span></div>'
        '<div style="display:flex;gap:12px;padding:2px 14px 10px">' +
        ''.join(f'<div style="text-align:center;font-size:9px"><div style="width:46px;height:46px;border-radius:50%;background:{b};display:grid;place-items:center;border:2px solid #fff;box-shadow:0 0 0 1.5px #ddd"><img src="{lg("nacar-" + v)}" style="width:26px"></div>{t}</div>' for b, v, t in hl) +
        '</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:2px">' + ''.join(grid_n) + '</div></div>')
story_n = (f'<div style="height:100%;position:relative;{bgimg(f'file://{SRC}7795646.jpg', "50% 40%")}"><div style="position:absolute;inset:0;background:linear-gradient(rgba(91,63,55,.25),rgba(91,63,55,.75))"></div>'
           '<div style="position:absolute;left:12px;right:12px;top:12px;display:flex;gap:4px">' + ''.join('<i style="flex:1;height:3px;border-radius:2px;background:rgba(255,255,255,.7);display:block"></i>' for _ in range(3)) + '</div>'
           f'<div style="position:absolute;left:0;right:0;bottom:46px;display:flex;flex-direction:column;align-items:center;gap:12px;color:{NP};text-align:center;font-family:J">'
           f'<img src="{lg("nacar-iso-light")}" style="width:46px"><span style="font-size:10px;letter-spacing:.35em">NUEVO</span>'
           '<span style="font-family:B;font-size:32px;line-height:1.05">Ritual<br><i>facial</i></span>'
           '<div style="background:#fff;color:#1C1A17;border-radius:14px;padding:10px 12px;font-size:11px;width:72%">¿Te gustaría probarlo?'
           '<div style="display:flex;gap:6px;margin-top:8px"><span style="flex:1;background:#F3ECE7;border-radius:8px;padding:6px">¡Sí!</span><span style="flex:1;background:#F3ECE7;border-radius:8px;padding:6px">Contame más</span></div></div></div></div>')
cm_ex = f'<div style="display:flex;gap:40px;align-items:center">{phone(ig_n, 340, 650)}{phone(story_n, 280, 560)}</div>'

# ---------------- Tienda online: Ondina ----------------
OV, OT, OA = col('ondina', 0), col('ondina', 1), col('ondina', 2)
PRODS_O = [(foto('5706274'), '50% 40%', 'Vestido Lino', '$38.900'), (foto('5706268'), '50% 60%', 'Cartera Teja', '$45.500'),
           (mk('ondina-tote'), '50% 50%', 'Tote Ondina', '$12.000'), (foto('5706273'), '50% 50%', 'Camisa Arena', '$29.900')]
shop_o = (f'<div style="background:#FBF8F2;height:100%;font-family:J;color:{OV}">'
          f'<div style="display:flex;justify-content:space-between;align-items:center;padding:16px 14px 10px"><span style="font-size:17px">☰</span>'
          f'<img src="{lg("ondina-word-dark")}" style="height:26px"><span style="background:{OV};color:#fff;border-radius:999px;padding:3px 9px;font-size:11px">2</span></div>'
          f'<div style="margin:0 12px;height:140px;border-radius:12px;position:relative;overflow:hidden;{bgimg(foto("5706277"), "50% 50%")}">'
          f'<div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(75,85,55,.7),rgba(75,85,55,0) 75%)"></div>'
          '<div style="position:absolute;left:14px;top:30px;color:#fff"><div style="font-size:9px;letter-spacing:.3em">NUEVA COLECCIÓN</div>'
          '<div style="font-size:22px;letter-spacing:.12em;margin-top:6px">OTOÑO</div><div style="margin-top:10px;background:#fff;color:#4B5537;border-radius:999px;padding:4px 10px;font-size:10px;display:inline-block">Ver todo</div></div></div>'
          '<div style="display:flex;gap:6px;padding:12px 12px 8px;font-size:10px">' + ''.join(f'<span style="border:1.4px solid {OV};border-radius:999px;padding:3px 10px;{"background:" + OV + ";color:#fff" if k == 0 else ""}">{c}</span>' for k, c in enumerate(['Todo', 'Vestidos', 'Camisas', 'Accesorios'])) + '</div>'
          '<div style="display:grid;grid-template-columns:1fr 1fr;gap:9px;padding:0 12px">' +
          ''.join(f'<div style="background:#fff;border-radius:10px;overflow:hidden;font-size:10px"><div style="height:108px;{bgimg(u, p)}"></div><div style="padding:6px 8px">{n}<br><b>{pr}</b></div></div>' for u, p, n, pr in PRODS_O) +
          '</div></div>')
check_o = (f'<div style="background:#FBF8F2;height:100%;padding:20px 16px;box-sizing:border-box;display:flex;flex-direction:column;gap:12px;font-family:J;color:{OV};font-size:12px">'
           '<b style="font-size:18px;letter-spacing:.06em">Tu carrito</b>' +
           ''.join(f'<div style="display:flex;gap:10px;align-items:center;background:#fff;border-radius:10px;padding:8px"><div style="width:50px;height:50px;border-radius:8px;flex:none;{bgimg(u, p)}"></div>'
                   f'<div style="flex:1">{n}<br><span style="font-size:10px;opacity:.7">Talle M · x1</span></div><b>{pr}</b></div>' for u, p, n, pr in PRODS_O[:2]) +
           '<div style="display:flex;justify-content:space-between;font-size:15px;border-top:1.5px solid #E2DACB;padding-top:10px">Total<b>$84.400</b></div>'
           '<span style="font-size:10px">Envío gratis a todo el país · 3 cuotas sin interés</span>'
           '<div style="background:#009EE3;color:#fff;text-align:center;border-radius:10px;padding:11px;font-weight:500">Pagar con Mercado Pago</div>'
           f'<div style="border:1.5px solid {OV};text-align:center;border-radius:10px;padding:9px">Consultar por WhatsApp</div></div>')
shop_ex = f'<div style="display:flex;gap:40px;align-items:center">{phone(shop_o, 330, 640)}{phone(check_o, 290, 580)}</div>'
