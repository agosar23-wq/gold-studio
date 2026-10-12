"""Personaje de Tostado (chica con flequillo y rodete) nadando en el café, en distintas poses.
Cada pose devuelve SVG en coordenadas locales (cabeza de radio ~22 centrada en 0,0)."""
LN, HAIR, HAIR2, SK, SK2, BLU = '#3A2318', '#3B2418', '#6B4532', '#F8DEC9', '#EDC2A6', '#F2A497'
SUIT, SUIT2, CREAM, GOLD = '#8A3B2A', '#A9503C', '#FFF6EA', '#E0B15C'
W = 2.2
st = lambda w=W, c=LN: f'stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'

def eyes(kind='open'):
    if kind == 'happy':   # ojitos cerrados de felicidad
        return f'<path d="M-12 5 q4 -5 8 0 M4 5 q4 -5 8 0" fill="none" {st(2.4)}/>'
    if kind == 'sun':     # anteojos de sol en forma de corazón
        heart = lambda x: (f'<path d="M{x} 9 C{x-9} 3 {x-9} -3 {x-4.5} -2.5 C{x-2} -2.3 {x} 0 {x} 1.5 C{x} 0 {x+2} -2.3 {x+4.5} -2.5 C{x+9} -3 {x+9} 3 {x} 9Z" fill="{SUIT}" {st(1.8)}/>'
                           f'<path d="M{x-5} 0.5 q1.5 -1.5 3 -1" fill="none" stroke="#fff" stroke-width="1.3" stroke-linecap="round" opacity=".8"/>')
        return heart(-8) + heart(8) + f'<path d="M-3 2 q3 -2 6 0" fill="none" {st(1.8)}/>'
    return ''.join(f'<ellipse cx="{x}" cy="4" rx="3.2" ry="4.2" fill="{LN}"/><circle cx="{x+1}" cy="2.4" r="1.3" fill="#fff"/>'
                   f'<path d="M{x-3.5} -2.5 q3.5 -2.4 7 0" fill="none" {st(1.6)}/>' for x in (-8, 8))

def head(eye='open', mouth='smile', goggles=False):
    m = {'smile': f'<path d="M-3.5 11.5 q3.5 3.5 7 0" fill="none" {st(2)}/>',
         'open': f'<path d="M-4.5 10.5 q4.5 7 9 0 q-4.5 1.5 -9 0Z" fill="#B5574A" {st(1.8)}/><path d="M-2 13.5 q2 1.6 4 0" fill="#F2A497"/>',
         'o': f'<ellipse cx="0" cy="12.5" rx="2.6" ry="3" fill="#B5574A" {st(1.6)}/>'}[mouth]
    g = (f'<path d="M-18 -14 C-10 -22 10 -22 18 -14" fill="none" stroke="{SUIT}" stroke-width="4" stroke-linecap="round"/>'
         + ''.join(f'<ellipse cx="{x}" cy="-16" rx="6" ry="4.6" fill="#BFE3EA" {st(1.8)}/><path d="M{x-3} -17 q2 -2 4 -1" fill="none" stroke="#fff" stroke-width="1.2"/>' for x in (-9, 9))) if goggles else ''
    return (f'<circle cx="2" cy="-30" r="9.5" fill="{HAIR}" {st()}/><path d="M-2 -33 q3 -4 8 -2" fill="none" stroke="{HAIR2}" stroke-width="1.8" stroke-linecap="round"/>'
            f'<path d="M-6 -27 q8 -4 16 0" fill="none" stroke="{GOLD}" stroke-width="3.2" stroke-linecap="round"/>'           # gomita dorada
            f'<path d="M-25 6 C-29 -16 -14 -28 0 -27 C15 -28 29 -16 25 6 C24 13 19 15 16 12 L-16 12 C-19 15 -24 13 -25 6Z" fill="{HAIR}" {st()}/>'
            f'<ellipse cx="0" cy="3" rx="20" ry="18.5" fill="{SK}" {st()}/>'
            f'<path d="M-21 2 C-22 -14 -10 -21 1 -20 C13 -21 22 -13 21 1 C17 -6 12 -9 7 -9 C6 -4 1 -3 -1 -8 C-6 -8 -12 -5 -16 0 C-17 -3 -18 -2 -21 2Z" fill="{HAIR}" {st()}/>'
            f'<path d="M-12 -14 q6 -4 12 -3" fill="none" stroke="{HAIR2}" stroke-width="1.8" stroke-linecap="round"/>'
            + eyes(eye) + f'<ellipse cx="-13" cy="10" rx="4.2" ry="2.6" fill="{BLU}" opacity=".85"/><ellipse cx="13" cy="10" rx="4.2" ry="2.6" fill="{BLU}" opacity=".85"/>'
            + m + g)

def arm(d, w=7.5):
    return (f'<path d="{d}" fill="none" stroke="{LN}" stroke-width="{w+2*W}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{SK}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
def hand(x, y, r=4.6): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SK}" {st()}/>'
def dots(pts, r=1.7): return ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{CREAM}" opacity=".9"/>' for x, y in pts)

def wave(x, y, w, o=.95, sw=2.2):
    return f'<path d="M{x-w} {y} q{w/4} -4 {w/2} 0 t{w/2} 0 t{w/2} 0 t{w/2} 0" fill="none" stroke="{CREAM}" stroke-width="{sw}" stroke-linecap="round" opacity="{o}"/>'
def drops(pts): return ''.join(f'<path d="M{x} {y-r*1.6} C{x+r} {y-r*.2} {x+r} {y+r} {x} {y+r} C{x-r} {y+r} {x-r} {y-r*.2} {x} {y-r*1.6}Z" fill="{CREAM}"/>' for x, y, r in pts)

# --- Pose 1: en un salvavidas inflable a rayas, saludando ---
def salvavidas():
    ring_back = f'<ellipse cx="0" cy="40" rx="44" ry="19" fill="{CREAM}" {st()}/><ellipse cx="0" cy="38" rx="24" ry="8.5" fill="#6B3A22" {st(1.8)}/>'
    torso = (f'<path d="M-15 16 C-17 26 -16 36 -14 42 L14 42 C16 36 17 26 15 16 C8 21 -8 21 -15 16Z" fill="{SUIT}" {st()}/>'
             + dots([(-7, 27), (5, 25), (-1, 34), (9, 35), (-10, 37)], 1.6))
    stripes = ''.join(f'<path d="M{a}" fill="{SUIT}" {st(1.8)}/>' for a in [
        '-44 40 C-44 47 -38 53 -30 56 L-24 45 C-27 43 -25 41 -24 39 Z', '30 56 C38 53 44 47 44 40 L24 39 C25 41 27 43 24 45 Z',
        '-8 59 C-3 60 3 60 8 59 L6 47 C2 47.5 -2 47.5 -6 47 Z'])
    ring_front = (f'<path d="M-44 40 C-44 52 -24 59 0 59 C24 59 44 52 44 40 C44 34 38 30 30 28 C30 33 24 46.5 0 46.5 C-24 46.5 -30 33 -30 28 C-38 30 -44 34 -44 40Z" fill="{CREAM}" {st()}/>'
                  + stripes + f'<path d="M-34 47 q8 5 18 6" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".9"/>')
    arms = (arm('M-14 22 C-24 30 -30 38 -32 45') + hand(-32, 46)
            + arm('M14 21 C24 14 30 2 30 -12') + hand(30, -14, 5.2)
            + f'<path d="M37 -20 q4 -4 6 1 M38 -10 q5 0 6 4" fill="none" {st(1.6)}/>')
    agua = wave(0, 64, 56) + wave(10, 71, 30, .7) + dots([(-52, 50), (54, 46), (-48, 58)])
    return agua, ring_back + torso + ring_front + arms + head('open', 'open')

# --- Pose 2: tirada sobre una medialuna inflable, con anteojos de corazón ---
def grano():
    """Tirada sobre un grano de café inflable, con anteojos de corazón."""
    G = 'M-72 14 C-72 -4 -40 -10 0 -10 C40 -10 74 -4 74 14 C74 32 40 40 0 40 C-40 40 -72 32 -72 14Z'
    bean = (f'<path d="{G}" fill="#6B3A22" {st()}/>'
            f'<path d="M-60 16 C-36 4 -12 26 8 14 C28 2 48 22 64 12" fill="none" stroke="#3A2016" stroke-width="3.2" stroke-linecap="round"/>'
            f'<path d="M-56 4 C-40 -3 -20 -4 -6 -3" fill="none" stroke="#A7684A" stroke-width="3.4" stroke-linecap="round"/>'
            f'<path d="M30 32 C44 30 56 26 62 20" fill="none" stroke="#8E5136" stroke-width="2.6" stroke-linecap="round"/>')
    body = (arm('M-20 2 C-36 -4 -54 -14 -64 -28', 7)
            + f'<path d="M-18 -10 C-4 -15 18 -15 28 -10 C32 -5 32 3 28 7 C18 11 -4 10 -18 4Z" fill="{SUIT}" {st()}/>'
            + dots([(-6, -7), (8, -9), (2, 2), (18, 0)], 1.6)
            + arm('M-12 -4 C-4 6 6 6 12 0', 6.5) + hand(13, 0, 4)
            + arm('M28 -4 C40 -18 50 -26 60 -26', 7.5) + arm('M28 4 C42 -2 50 -12 56 -18', 7.5)
            + f'<ellipse cx="63" cy="-27" rx="5.2" ry="3.6" fill="{SK}" {st()}/><ellipse cx="59" cy="-19" rx="5.2" ry="3.6" fill="{SK}" {st()}/>')
    cara = f'<g transform="translate(-38 -16) rotate(-18) scale(.92)">{head("sun", "smile")}</g>'
    agua = (f'<path d="M-86 30 C-40 54 44 54 90 28" fill="none" stroke="{CREAM}" stroke-width="2.2" stroke-linecap="round"/>'
            + wave(0, 58, 40, .7) + dots([(94, 16), (-90, 18), (84, 38)]))
    return agua, bean + body + cara

# --- Pose 3: nadando con antiparras, brazo afuera y salpicadura ---
def nado():
    body = (f'<path d="M6 12 C16 4 40 4 52 10 C58 14 56 22 48 24 C36 27 16 26 6 20Z" fill="{SUIT}" {st()}/>'
            + dots([(22, 12), (34, 10), (40, 19), (28, 21)], 1.6)
            + arm('M14 10 C10 -14 -12 -26 -32 -16') + hand(-34, -15)
            + arm('M12 22 C4 30 -6 32 -16 30') + f'<path d="M-24 26 q4 8 12 7" fill="none" stroke="{CREAM}" stroke-width="2.2" stroke-linecap="round"/>')
    agua = (wave(10, 30, 46) + wave(30, 38, 26, .7)
            + drops([(-44, -24, 3), (-40, -34, 2.2), (-50, -14, 2.4), (68, 8, 2.6), (74, 0, 2), (64, -2, 1.8)])
            + f'<path d="M58 14 q8 -10 18 -6 M60 22 q10 -2 16 4" fill="none" stroke="{CREAM}" stroke-width="2.2" stroke-linecap="round"/>')
    return agua, body + head('happy', 'open', goggles=True)

POSES = {'salvavidas': salvavidas, 'grano': grano, 'nado': nado}

def sticker_filter(fid='stk', color=CREAM, r=2.2):
    return (f'<filter id="{fid}" x="-30%" y="-30%" width="160%" height="160%"><feMorphology in="SourceAlpha" operator="dilate" radius="{r}" result="d"/>'
            f'<feFlood flood-color="{color}"/><feComposite in2="d" operator="in" result="o"/>'
            f'<feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#1a0d06" flood-opacity=".35" in="o" result="s"/>'
            f'<feMerge><feMergeNode in="s"/><feMergeNode in="o"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')

def place(name, x, y, sc, rot=0, fid='stk'):
    agua, cuerpo = POSES[name]()
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})">{agua}<g filter="url(#{fid})">{cuerpo}</g></g>'
