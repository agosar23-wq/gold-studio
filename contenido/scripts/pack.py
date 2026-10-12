"""Packaging dibujado (HTML) para la pastelería de ejemplo Dulce Mía."""
PINK, CREAM, CHOC, GOLD = '#E8B4B8', '#FFF6F4', '#4A2329', '#C9A34E'

def cup(color, size):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 100" fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M29 60 L71 60 L64 90 L36 90 Z"/><path d="M43 62 L45 88 M50 62 L50 88 M57 62 L55 88"/>'
            '<path d="M24 60 C18 52 26 44 33 47 C32 37 44 31 50 38 C56 31 68 37 67 47 C74 44 82 52 76 60 Z"/>'
            f'<circle cx="50" cy="27" r="6" fill="{color}"/><path d="M51 21 C53 15 57 12 62 11"/></svg>')

def mark(color, s=1.0, sub=True):
    return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:{int(6*s)}px;color:{color}">{cup(color, int(70*s))}'
            f'<span style="font-family:B;font-size:{int(54*s)}px;line-height:1">Dulce Mía</span>'
            + (f'<span style="font-family:J;font-size:{int(15*s)}px;letter-spacing:.32em">PASTELERÍA</span>' if sub else '') + '</div>')

SH = 'box-shadow:0 40px 70px -34px rgba(0,0,0,.55)'

def box(w=520, bg=PINK, ink=CHOC, plain=False, lid=None):
    h = int(w * 0.72); lid = lid or ink
    if plain:
        return (f'<div style="width:{w}px;height:{h}px;position:relative;{SH}">'
                f'<div style="position:absolute;inset:0;background:#E9E4DC"></div>'
                f'<div style="position:absolute;left:0;right:0;top:0;height:{int(h*.22)}px;background:#DDD6CB"></div>'
                f'<div style="position:absolute;left:50%;top:58%;transform:translate(-50%,-50%);background:#fff;border:2px solid #ccc;padding:{int(w*.03)}px {int(w*.06)}px;font-family:Arial;font-size:{int(w*.045)}px;color:#777">Pastelería</div></div>')
    return (f'<div style="width:{w}px;height:{h}px;position:relative;{SH}">'
            f'<div style="position:absolute;inset:0;background:{bg}"></div>'
            f'<div style="position:absolute;left:0;right:0;top:0;height:{int(h*.22)}px;background:{lid}"></div>'
            f'<div style="position:absolute;left:{int(w*.47)}px;width:{int(w*.06)}px;top:0;bottom:0;background:{GOLD};opacity:.9"></div>'
            f'<div style="position:absolute;left:{int(w*.5)}px;top:{int(h*.22)}px;transform:translate(-50%,-50%);width:{int(w*.2)}px;height:{int(w*.2)}px;border-radius:50%;background:{CREAM};display:grid;place-items:center">{cup(CHOC if ink == CREAM else ink, int(w*.12))}</div>'
            f'<div style="position:absolute;left:0;right:0;top:{int(h*.5)}px;display:flex;justify-content:center">'
            f'<span style="font-family:B;font-size:{int(w*.11)}px;color:{ink};background:{bg};padding:0 {int(w*.03)}px;line-height:1.1">Dulce Mía</span></div></div>')

def sticker(d=300, bg=CHOC, ink=CREAM):
    return (f'<div style="width:{d}px;height:{d}px;border-radius:50%;background:{bg};display:grid;place-items:center;{SH};border:{int(d*.03)}px solid {GOLD}">'
            f'<div style="text-align:center;color:{ink}"><div style="font-family:B;font-size:{int(d*.16)}px;line-height:1">Dulce Mía</div>'
            f'<div style="font-family:B;font-style:italic;font-size:{int(d*.09)}px;color:{GOLD};margin-top:{int(d*.03)}px">hecho con amor</div></div></div>')

def card(w=520):
    h = int(w * 0.66)
    return (f'<div style="width:{w}px;height:{h}px;background:{CREAM};border:2px solid {PINK};{SH};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:{int(w*.025)}px;color:{CHOC};text-align:center;padding:{int(w*.06)}px;box-sizing:border-box">'
            f'{cup(CHOC, int(w*.11))}<div style="font-family:B;font-style:italic;font-size:{int(w*.085)}px;line-height:1.1">¡Gracias por elegirnos!</div>'
            f'<div style="font-family:J;font-size:{int(w*.04)}px;color:#7A5A5E;line-height:1.4">Esperamos que lo disfrutes tanto como nosotras al hacerlo</div>'
            f'<div style="font-family:J;font-weight:500;font-size:{int(w*.04)}px;letter-spacing:.08em;color:{CHOC}">@dulcemia</div></div>')

def bag(w=400, bg=PINK, ink=CHOC):
    h = int(w * 1.15)
    return (f'<div style="width:{w}px;height:{int(h*1.22)}px;position:relative">'
            f'<div style="position:absolute;left:{int(w*.25)}px;top:0;width:{int(w*.5)}px;height:{int(h*.4)}px;border:{int(w*.03)}px solid {ink};border-bottom:none;border-radius:{int(w*.25)}px {int(w*.25)}px 0 0;box-sizing:border-box"></div>'
            f'<div style="position:absolute;left:0;bottom:0;width:{w}px;height:{h}px;background:{bg};{SH};display:grid;place-items:center">{mark(ink, w/520)}</div></div>')

def cupbox(w=380):
    return (f'<div style="width:{w}px;height:{w}px;background:{CREAM};{SH};position:relative;border:2px solid {PINK}">'
            f'<div style="position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);width:{int(w*.55)}px;height:{int(w*.55)}px;border-radius:50%;background:#F7E6E4;border:3px solid {PINK};display:grid;place-items:center">{cup(CHOC, int(w*.36))}</div>'
            f'<div style="position:absolute;left:0;right:0;bottom:{int(w*.07)}px;text-align:center;font-family:B;font-size:{int(w*.11)}px;color:{CHOC}">Dulce Mía</div></div>')
