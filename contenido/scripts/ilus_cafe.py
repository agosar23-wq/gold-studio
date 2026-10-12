"""Ilustraciones de línea: taza vista desde arriba con personajitos nadando en el café."""
ESP, BOR, CRE, CAR, MAD, MAN = '#2A1A14', '#6E1E17', '#EFE4D6', '#C98A5A', '#7A4A2E', '#F2D3A0'
LS = f'stroke="{ESP}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
L = 'fill="none" ' + LS

def face(x, y, r=10, glasses=False):
    eyes = (f'<path d="M{x-5} {y+1} h10" stroke="{ESP}" stroke-width="1.6"/><rect x="{x-8}" y="{y-2}" width="7" height="5" rx="2" fill="{ESP}"/><rect x="{x+1}" y="{y-2}" width="7" height="5" rx="2" fill="{ESP}"/>'
            if glasses else f'<path d="M{x-6} {y} q2.5 -3 5 0 M{x+1} {y} q2.5 -3 5 0" {L} stroke-width="1.5"/>')
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#F6D9C0" {LS}/>'
            f'<path d="M{x-r} {y-1} C{x-r} {y-r-6} {x+r} {y-r-6} {x+r} {y-2} C{x+4} {y-6} {x-4} {y-7} {x-r} {y-1}Z" fill="{ESP}"/>'
            + eyes + f'<path d="M{x-3} {y+5} q3 3 6 0" {L} stroke-width="1.5"/>'
            f'<circle cx="{x-7}" cy="{y+4}" r="2" fill="#E9A6A0"/><circle cx="{x+7}" cy="{y+4}" r="2" fill="#E9A6A0"/>')

def ripple(x, y, w=26):
    return f'<path d="M{x-w} {y} q{w/2} -6 {w} 0 t{w} 0" {L} stroke="{CRE}" stroke-width="1.5" opacity=".9"/>'

def swimmer_ring(x, y, c=BOR):
    return (ripple(x, y + 14, 22) +
            f'<ellipse cx="{x}" cy="{y+8}" rx="24" ry="11" fill="{c}" {LS}/>'
            f'<path d="M{x-14} {y+1} l3 14 M{x+14} {y+1} l-3 14" stroke="#fff" stroke-width="4"/>'
            f'<ellipse cx="{x}" cy="{y+6}" rx="11" ry="4.5" fill="{CAR}"/>' + face(x, y - 4) +
            f'<path d="M{x-9} {y+4} q-8 2 -14 6 M{x+9} {y+4} q8 2 14 6" {L}/>')

def swimmer_glasses(x, y):
    return (ripple(x, y + 10, 18) + face(x, y, glasses=True) +
            f'<path d="M{x+10} {y+2} C{x+18} {y-4} {x+20} {y-12} {x+18} {y-20}" {L}/><circle cx="{x+18}" cy="{y-22}" r="3.5" fill="#F6D9C0" {LS}/>')

def cookie(x, y):
    dots = ''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="1.8" fill="{ESP}"/>' for dx, dy in [(-7, -2), (4, 4), (8, -5), (-2, 7), (-9, 5)])
    return ripple(x, y + 12, 16) + f'<circle cx="{x}" cy="{y}" r="13" fill="{MAN}" {LS}/>' + dots

def cookie_raft(x, y):
    dots = ''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="2.2" fill="{ESP}"/>' for dx, dy in [(-12, 4), (8, 8), (14, -2), (-4, 10), (-16, -3)])
    return (ripple(x, y + 16, 26) + f'<ellipse cx="{x}" cy="{y+4}" rx="26" ry="13" fill="{MAN}" {LS}/>' + dots +
            f'<path d="M{x-6} {y-2} L{x-8} {y-18} Q{x} {y-24} {x+8} {y-18} L{x+6} {y-2}Z" fill="{BOR}" {LS}/>'
            f'<path d="M{x-4} {y} q-10 2 -14 -2 M{x+4} {y} q10 2 14 -2" {L}/>' + face(x, y - 28, 9) +
            f'<path d="M{x-7} {y-16} q-8 -4 -10 -12 M{x+7} {y-16} q8 -4 10 -12" {L}/>')

def cup(size, swimmers=('ring', 'glasses', 'cookie'), handle=True, saucer=True):
    sw = {'ring': swimmer_ring(82, 96), 'glasses': swimmer_glasses(118, 138), 'cookie': cookie(80, 140), 'ring2': swimmer_ring(136, 80, MAD), 'raft': cookie_raft(122, 74)}
    pos_extra = ''.join(sw[k] for k in swimmers)
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 220 220">'
            + (f'<circle cx="110" cy="110" r="104" fill="{CRE}" {LS}/><circle cx="110" cy="110" r="88" fill="none" stroke="{ESP}" stroke-width="1.4" opacity=".35"/>' if saucer else '')
            + (f'<path d="M180 92 C206 88 210 132 182 128" fill="none" stroke="{ESP}" stroke-width="12" stroke-linecap="round"/><path d="M180 92 C206 88 210 132 182 128" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round"/>' if handle else '')
            + f'<circle cx="110" cy="110" r="74" fill="#fff" {LS}/>'
            f'<circle cx="110" cy="110" r="62" fill="{MAD}"/>'
            f'<circle cx="110" cy="110" r="62" fill="url(#cr)"/>'
            f'<defs><radialGradient id="cr" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="{MAN}"/><stop offset=".55" stop-color="{CAR}"/><stop offset="1" stop-color="{MAD}"/></radialGradient></defs>'
            f'<path d="M78 140 C90 150 130 152 146 132" fill="none" stroke="{CRE}" stroke-width="2" opacity=".6" stroke-linecap="round"/>'
            + pos_extra + '</svg>')

def rim_sitter(size):
    """Personaje sentado en el borde de una taza (vista de costado), con los pies en el café."""
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 220 220">'
            f'<path d="M60 200 h100" {L}/>'
            f'<path d="M50 96 h120 l-10 78 q-4 22 -26 22 h-48 q-22 0 -26 -22 Z" fill="#fff" {LS}/>'
            f'<path d="M168 112 c30 -4 30 44 -4 42" {L} stroke-width="3"/>'
            f'<ellipse cx="110" cy="96" rx="60" ry="10" fill="{CAR}" {LS}/>'
            f'<path d="M72 30 q6 -10 2 -20 M90 34 q6 -10 2 -20" {L} stroke="{MAD}" opacity=".6"/>'
            f'<path d="M98 92 L96 70 Q110 62 124 70 L122 92 Z" fill="{BOR}" {LS}/>'
            f'<path d="M102 92 q-4 8 -2 14 M118 92 q4 8 2 14" {L}/>' + ripple(110, 104, 14) + face(110, 56, 11) +
            f'<path d="M98 76 q-10 6 -12 16 M122 76 q12 2 18 -8" {L}/><path d="M140 66 l6 -6 m-2 10 l8 -2" {L} stroke-width="1.5"/>'
            '</svg>')
