"""Piezas visuales reutilizables (HTML con estilos en línea) para reels y carruseles."""
import html as H

BRANDS = {
    'dulce': dict(name='Dulce Mía', rubro='Pastelería', c='#E8B4B8', light='#FFF6F4', ink='#4A2329', serif=True),
    'raiz': dict(name='Raíz', rubro='Dietética natural', c='#5E7D5B', light='#F1F3EC', ink='#1F2B1E', serif=True),
    'clara': dict(name='Clara', rubro='Psicología', c='#2F4A6D', light='#EEF2F6', ink='#16243A', serif=False),
    'aura': dict(name='Aura', rubro='Joyería', c='#C9A34E', light='#FAF6EE', ink='#1C1A17', serif=True),
}

def _font(b, size):
    return f"font-family:B;font-size:{size}px" if b['serif'] else f"font-family:J;font-weight:500;letter-spacing:.16em;text-transform:uppercase;font-size:{int(size*.7)}px"

def browser(inner, w=820, url='tumarca.com.ar'):
    return (f'<div style="width:{w}px;border-radius:22px;overflow:hidden;background:#fff;box-shadow:0 30px 60px -34px rgba(0,0,0,.5);border:2px solid #E6DAC2">'
            f'<div style="display:flex;gap:9px;align-items:center;padding:14px 18px;background:#F2EADA">'
            f'<i style="width:13px;height:13px;border-radius:50%;background:#E0D3B8"></i><i style="width:13px;height:13px;border-radius:50%;background:#E0D3B8"></i><i style="width:13px;height:13px;border-radius:50%;background:#E0D3B8"></i>'
            f'<span style="margin-left:14px;background:#fff;border-radius:999px;padding:4px 16px;font-size:16px;color:#6b6358">{url}</span></div>{inner}</div>')

def site(key, level=1, w=820):
    """level 1 = página simple, 2 = sitio completo, 3 = con turnos/usuarios."""
    b = BRANDS[key]; s = w / 820
    nav = '' if level == 1 else (f'<div style="display:flex;gap:{int(22*s)}px;font-size:{int(15*s)}px;color:{b["ink"]};opacity:.75">' +
                                 ''.join(f'<span>{t}</span>' for t in (['Inicio', 'Productos', 'Nosotros', 'Contacto'] if level == 2 else ['Inicio', 'Turnos', 'Mi cuenta'])) + '</div>')
    head = (f'<div style="display:flex;justify-content:space-between;align-items:center;padding:{int(18*s)}px {int(28*s)}px;background:{b["light"]}">'
            f'<span style="{_font(b, int(30*s))};color:{b["ink"]}">{b["name"]}</span>{nav}</div>')
    hero = (f'<div style="background:{b["c"]};color:{b["light"] if key != "dulce" else b["ink"]};padding:{int(40*s)}px {int(28*s)}px;display:flex;flex-direction:column;gap:{int(12*s)}px">'
            f'<span style="font-size:{int(13*s)}px;letter-spacing:.3em;text-transform:uppercase;opacity:.85">{b["rubro"]}</span>'
            f'<span style="{_font(b, int(42*s))};line-height:1.1">{"Hecho con amor, para tus momentos" if key == "dulce" else "Bienvenida a " + b["name"]}</span>'
            f'<span style="align-self:flex-start;background:{b["ink"]};color:#fff;font-size:{int(15*s)}px;padding:{int(9*s)}px {int(20*s)}px;border-radius:999px">'
            f'{"Pedí por WhatsApp" if level == 1 else "Reservá tu turno" if level == 3 else "Ver productos"}</span></div>')
    body = ''
    if level >= 2:
        body += (f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:{int(12*s)}px;padding:{int(20*s)}px {int(28*s)}px;background:#fff">' +
                 ''.join(f'<div style="height:{int(90*s)}px;border-radius:{int(12*s)}px;background:{b["light"]};border:2px solid {b["c"]}33"></div>' for _ in range(3)) + '</div>')
    if level == 3:
        days = ''.join(f'<span style="width:{int(44*s)}px;height:{int(44*s)}px;border-radius:50%;display:grid;place-items:center;font-size:{int(15*s)}px;'
                       f'{"background:" + b["c"] + ";color:#fff" if d == 15 else "background:" + b["light"]}">{d}</span>' for d in range(12, 19))
        body += (f'<div style="padding:{int(14*s)}px {int(28*s)}px {int(24*s)}px;background:#fff;display:flex;flex-direction:column;gap:{int(10*s)}px">'
                 f'<span style="font-size:{int(16*s)}px;font-weight:500;color:{b["ink"]}">Elegí tu turno</span><div style="display:flex;gap:{int(10*s)}px">{days}</div></div>')
    if level == 1:
        body += (f'<div style="padding:{int(18*s)}px {int(28*s)}px;background:#fff;display:flex;gap:{int(14*s)}px;align-items:center;font-size:{int(15*s)}px;color:#555">'
                 f'<span style="width:{int(36*s)}px;height:{int(36*s)}px;border-radius:50%;background:#25D366"></span>Escribinos y te respondemos al toque</div>')
    return browser(head + hero + body, w, url=f'{b["name"].lower().replace(" ", "")}.com.ar')

def linktree(key, w=380):
    b = BRANDS[key]
    btns = ''.join(f'<div style="background:#fff;border-radius:999px;padding:14px;text-align:center;font-size:17px;color:#333;box-shadow:0 2px 0 rgba(0,0,0,.06)">{t}</div>'
                   for t in ['Catálogo', 'WhatsApp', 'Instagram', 'Ubicación'])
    return (f'<div style="box-sizing:border-box;width:{w}px;border-radius:36px;background:#E9E6F2;padding:40px 26px;display:flex;flex-direction:column;gap:14px;align-items:stretch;box-shadow:0 30px 60px -34px rgba(0,0,0,.5);font-family:J">'
            f'<div style="width:90px;height:90px;border-radius:50%;background:{b["c"]};align-self:center"></div>'
            f'<div style="text-align:center;font-size:20px;font-weight:600;color:#333">@{b["name"].lower().replace(" ", "")}</div>{btns}'
            f'<div style="text-align:center;font-size:13px;color:#888;margin-top:6px">linktr.ee/{b["name"].lower().replace(" ", "")}</div></div>')

def chat(w=560, scale=1.0):
    msgs = [('in', 'Hola!! me pasás de nuevo el plan? no lo encuentro 🙈', '23:47'),
            ('in', 'Y el turno era el jueves o el viernes??', '23:48'),
            ('in', '📎 plan_final_FINAL_v3.pdf', '23:52'),
            ('in', 'Holaa? 👀', '00:13'),
            ('in', 'Perdón otra vez, cuánto tenía que comer de avena?', '07:02')]
    rows = ''.join(f'<div style="align-self:flex-start;max-width:84%;background:#fff;border-radius:16px;border-top-left-radius:4px;padding:{int(10*scale)}px {int(14*scale)}px;font-size:{int(19*scale)}px;color:#222;box-shadow:0 1px 0 rgba(0,0,0,.08)">{H.escape(t)}<span style="font-size:{int(12*scale)}px;color:#999;margin-left:10px">{h}</span></div>' for _, t, h in msgs)
    return (f'<div style="width:{w}px;border-radius:30px;overflow:hidden;box-shadow:0 30px 60px -34px rgba(0,0,0,.5);font-family:J">'
            f'<div style="background:#075E54;color:#fff;padding:{int(16*scale)}px {int(20*scale)}px;font-size:{int(20*scale)}px;font-weight:500;display:flex;justify-content:space-between">Pacientes 💬<span style="background:#25D366;border-radius:999px;padding:0 12px;font-size:{int(16*scale)}px">47</span></div>'
            f'<div style="background:#ECE5DD;padding:{int(18*scale)}px;display:flex;flex-direction:column;gap:{int(10*scale)}px">{rows}</div></div>')

def logo_card(key='dulce', w=560):
    b = BRANDS[key]
    return (f'<div style="width:{w}px;height:{int(w*0.72)}px;border-radius:30px;background:{b["c"]};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;box-shadow:0 40px 80px -40px rgba(0,0,0,.55)">'
            f'<svg width="{int(w*0.2)}" height="{int(w*0.2)}" viewBox="0 0 100 100" fill="none" stroke="{b["ink"]}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M29 60 L71 60 L64 90 L36 90 Z"/><path d="M43 62 L45 88 M50 62 L50 88 M57 62 L55 88"/>'
            f'<path d="M24 60 C18 52 26 44 33 47 C32 37 44 31 50 38 C56 31 68 37 67 47 C74 44 82 52 76 60 Z"/>'
            f'<path d="M34 52 C42 48 58 48 66 52"/>'
            f'<circle cx="50" cy="27" r="6" fill="{b["ink"]}"/><path d="M51 21 C53 15 57 12 62 11"/></svg>'
            f'<span style="font-family:B;font-size:{int(w*0.15)}px;color:{b["ink"]};line-height:1">{b["name"]}</span>'
            f'<span style="font-size:{int(w*0.032)}px;letter-spacing:.36em;text-transform:uppercase;color:{b["ink"]}">{b["rubro"]}</span></div>')

def moodboard(w=860):
    sw = ''.join(f'<i style="display:block;height:100%;background:{c}"></i>' for c in ['#E8B4B8', '#FFF6F4', '#4A2329', '#C9A34E'])
    return (f'<div style="width:{w}px;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:230px 230px;gap:18px">'
            f'<div style="grid-row:span 2;border-radius:24px;overflow:hidden">{logo_card("dulce", int(w*0.55))}</div>'
            f'<div style="border-radius:24px;overflow:hidden;display:grid;grid-template-columns:repeat(4,1fr);box-shadow:0 20px 40px -30px rgba(0,0,0,.4)">{sw}</div>'
            f'<div style="border-radius:24px;background:#fff;padding:22px;display:flex;flex-direction:column;justify-content:center;gap:4px;box-shadow:0 20px 40px -30px rgba(0,0,0,.4)">'
            f'<span style="font-family:B;font-size:54px;color:#4A2329;line-height:1">Aa</span><span style="font-size:18px;color:#6b6358">Bodoni Moda + Jost</span></div></div>')
