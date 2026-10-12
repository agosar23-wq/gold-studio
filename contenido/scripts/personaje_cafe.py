"""Personas relajando en salvavidas dentro del café: ilustración de línea, proporciones adultas (estilo editorial).
Cada pose devuelve (agua, figura) en coordenadas locales: el agujero del salvavidas está centrado en 0,0."""
LN, FILL, HAIR, DARK, LIP = '#2E1C14', '#FFFBF4', '#3A2418', '#2E1C14', '#9C4A3A'
W = 0.9
st = lambda w=W, c=LN: f'stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"'

def limb(d, w=3.0):
    return (f'<path d="{d}" fill="none" stroke="{LN}" stroke-width="{w + 1.3}" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" fill="none" stroke="{FILL}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
def line(d, w=W, o=1): return f'<path d="{d}" fill="none" {st(w)} opacity="{o}"/>'

def face(rot=0, glasses=True, lips=True):
    """Cara adulta chiquita, centrada en 0,0 (alto ~15)."""
    g = (f'<path d="M-5.6 -1.6 h4.4 a.6 .6 0 0 1 .6 .6 v1.6 a2 2 0 0 1 -2 2 h-1.6 a2 2 0 0 1 -2 -2 v-1.6 a.6 .6 0 0 1 .6 -.6Z" fill="{DARK}"/>'
         f'<path d="M1 -1.6 h4.4 a.6 .6 0 0 1 .6 .6 v1.6 a2 2 0 0 1 -2 2 h-1.6 a2 2 0 0 1 -2 -2 v-1.6 a.6 .6 0 0 1 .6 -.6Z" fill="{DARK}"/>'
         f'<path d="M-.6 -1 q.6 -.5 1.2 0" fill="none" {st(.7)}/><path d="M-4.6 -.8 l1 -.4 M2 -.8 l1 -.4" stroke="#fff" stroke-width=".5" opacity=".7"/>') if glasses else \
        f'<path d="M-4.4 -.2 q1.4 .9 2.8 0 M1.6 -.2 q1.4 .9 2.8 0" fill="none" {st(.8)}/><path d="M-4.6 -2.6 q1.6 -.8 3 -.2 M1.6 -2.8 q1.6 -.6 3 .2" fill="none" {st(.6)}/>'
    return (f'<g transform="rotate({rot})">'
            f'<path d="M-6 -3 C-6.2 -9 6.2 -9 6 -3 C5.9 2.5 3.4 7.4 0 7.6 C-3.4 7.4 -5.9 2.5 -6 -3Z" fill="{FILL}" {st()}/>'
            + g + line('M.2 .6 q.8 2 -.5 2.6', .7)
            + (f'<path d="M-1.8 4.6 q1.8 -.8 3.6 0 q-1.8 1.4 -3.6 0Z" fill="{LIP}" {st(.5)}/>' if lips else '') + '</g>')

SHADE = '#E6DACB'
def tube(rx=27, ry=11.5, hx=12.5, hy=5):
    """Salvavidas blanco inflado: (parte de atrás, parte de adelante) para meter a la persona en el medio."""
    ring = f'M{-rx} 0 A{rx} {ry} 0 1 1 {rx} 0 A{rx} {ry} 0 1 1 {-rx} 0Z M{-hx} 0 A{hx} {hy} 0 1 0 {hx} 0 A{hx} {hy} 0 1 0 {-hx} 0Z'
    back = (f'<path d="{ring}" fill="{FILL}" fill-rule="evenodd"/>'
            f'<path d="M{-hx} 0 A{hx} {hy} 0 0 1 {hx} 0 C{hx*.7} {-hy*.3} {-hx*.7} {-hy*.3} {-hx} 0Z" fill="{SHADE}"/>'
            + line(f'M{-rx} 0 A{rx} {ry} 0 0 1 {rx} 0') + line(f'M{-hx} 0 A{hx} {hy} 0 0 1 {hx} 0')
            + line(f'M{-rx*.7} {-ry*.45} C{-rx*.35} {-ry*.82} {rx*.35} {-ry*.82} {rx*.7} {-ry*.45}', .5, .45))
    front = (f'<path d="M{-rx} 0 A{rx} {ry} 0 0 0 {rx} 0 L{hx} 0 A{hx} {hy} 0 0 1 {-hx} 0Z" fill="{FILL}"/>'
             f'<path d="M{-rx} 0 A{rx} {ry} 0 0 0 {rx} 0 C{rx*.9} {ry*.55} {-rx*.9} {ry*.55} {-rx} 0Z" fill="{SHADE}" opacity=".8"/>'
             + line(f'M{-rx} 0 A{rx} {ry} 0 0 0 {rx} 0') + line(f'M{hx} 0 A{hx} {hy} 0 0 1 {-hx} 0'))
    return back, front

def ripples(rx=27, ry=11.5, k=3):
    out = ''
    for i in range(1, k + 1):
        a, b = rx + 5 * i, ry + 3 * i
        out += (f'<path d="M{-a} 1 A{a} {b} 0 0 0 {-a*.1} {b+.5}" fill="none" stroke="#FFF3E2" stroke-width=".7" stroke-linecap="round" opacity="{.8 - .2*i}"/>'
                f'<path d="M{a*.35} {b*.95} A{a} {b} 0 0 0 {a} 0" fill="none" stroke="#FFF3E2" stroke-width=".7" stroke-linecap="round" opacity="{.7 - .18*i}"/>')
    return out

def head(hair='bun', rot=0, glasses=True, lips=True):
    """Cabeza adulta (alto ~10) centrada en 0,0, con cuello hacia abajo."""
    f = f'<g transform="scale(.62)">{face(0, glasses, lips)}</g>'
    H = {
     'bun': (f'<path d="M-4.2 -1.2 C-5.2 -7.4 5.2 -7.4 4.2 -1.2 C3.7 -4 1.8 -5 0 -5 C-1.8 -5 -3.7 -4 -4.2 -1.2Z" fill="{HAIR}" {st(.6)}/>'
             f'<path d="M.6 -9.4 c-2.8 -.4 -3.8 1.8 -2 3.2 c1.6 1.1 4 .1 3.8 -1.7 c-.2 -1 -.9 -1.4 -1.8 -1.5Z" fill="{HAIR}" {st(.6)}/>'
             + line('M-2.4 -4.2 q2 -1.2 4.2 -.4', .35, .6)),
     'short': (f'<path d="M-4.2 -1.6 C-5.2 -6.6 -1.4 -8 1 -7.4 C3.8 -7.2 5.4 -5.2 4.2 -1.6 C3.6 -3.8 2.2 -4.4 .8 -4.4 C-.8 -5.4 -3 -4.2 -4.2 -1.6Z" fill="{HAIR}" {st(.6)}/>'
               + line('M-1.8 -6.2 q1.6 -.8 3.4 -.2', .35, .6)),
     'long': (f'<path d="M-4.4 -.8 C-5.6 -7.6 5.6 -7.6 4.4 -.8 C5.2 1.8 6.2 4.4 5.4 7 C6.4 9 5.6 11 4 11.6 C4.6 9.6 3.6 8.4 3.4 6.4 C3.2 3.6 3 -1 1.2 -3.8 C-.6 -3 -2.8 -1.6 -3.4 1.4 C-3.6 4 -3.4 6 -4.6 8.4 C-5.6 10.2 -6.6 10.4 -7.4 9.6 C-5.8 8.6 -6.4 6.6 -5.4 4.6 C-4.8 2.8 -4.8 1 -4.4 -.8Z" fill="{HAIR}" {st(.6)}/>'
              + line('M-2 -5.4 q2 -1 4 0 M4.2 2 q.8 2.4 .2 4.6 M-4.4 3 q-.6 2 -.4 4', .35, .55)),
    }[hair]
    return f'<g transform="rotate({rot})">{f}{H}</g>'

def torso(swim='bikini'):
    """Hombros y pecho, recostados: arranca en el cuello (0,-7) y entra al agujero (y≈3)."""
    t = (f'<path d="M-2 -7.4 C-5 -7.2 -7.4 -6.6 -8 -4.8 C-8.2 -2.6 -7 -.6 -5.6 1 C-5 2 -5.4 3 -5.8 3.8 L5.8 3.8 C5.4 3 5 2 5.6 1 C7 -.6 8.2 -2.6 8 -4.8 C7.4 -6.6 5 -7.2 2 -7.4Z" fill="{FILL}" {st(.7)}/>')
    if swim == 'bikini':
        t += (f'<path d="M-5.6 -3.4 C-5 -.8 -2.2 -.4 -.5 -2 C-1.2 -4 -3.4 -4.6 -5.6 -3.4Z M5.6 -3.4 C5 -.8 2.2 -.4 .5 -2 C1.2 -4 3.4 -4.6 5.6 -3.4Z" fill="{DARK}"/>'
              + line('M-5 -3.6 L-2.8 -7.2 M5 -3.6 L2.8 -7.2', .4))
    else:
        t += line('M-4.6 -2.4 q2.4 1.2 4.2 .2 M4.6 -2.4 q-2.4 1.2 -4.2 .2', .35, .55)
    return t

def legs(cross=False, swim='bikini'):
    """Muslos que pasan por arriba del borde de adelante y piernas que se meten en el café."""
    if cross:   # una pierna cruzada sobre la otra
        l = (limb('M2.4 3 C2.8 6.4 3.6 9.4 4.4 12', 2.7) + limb('M4.4 12 C4.2 14.2 3.8 16 3.4 17.8', 2.1)
             + limb('M-2.4 3 C-1.4 6.4 1 9.2 3.8 10.6', 2.7) + limb('M3.8 10.6 C5.8 12 7.4 14 8.2 16.6', 2.1))
    else:       # rodillas dobladas sobre el borde
        l = (limb('M-2.6 3 C-3.6 6.2 -4.8 9 -5.6 11.6', 2.7) + limb('M-5.6 11.6 C-5.2 13.8 -4.6 15.8 -4 17.6', 2.1)
             + limb('M2.6 3 C3.4 6.2 4.6 9.2 5 11.8', 2.7) + limb('M5 11.8 C5 14 4.8 15.8 4.4 17.6', 2.1))
    bottom = (f'<path d="M-5.8 3 C-5.4 5.4 5.4 5.4 5.8 3Z" fill="{DARK}"/>')
    water = f'<path d="M-8 17.4 q2.2 -1.4 4.4 0 t4.4 0 t4.4 0 t4.4 0" fill="none" stroke="#FFF3E2" stroke-width=".8" stroke-linecap="round"/>'
    return bottom + l + water

def arm_rim(side):
    """Brazo apoyado sobre el salvavidas."""
    s = side
    return limb(f'M{8*s} -4.6 C{11*s} -3.2 {14*s} -2.6 {17*s} -2.6 C{19*s} -2.6 {21*s} -1.4 {22.4*s} .2', 1.9) + \
        f'<ellipse cx="{23.2*s}" cy="1" rx="1.5" ry="1" fill="{FILL}" {st(.6)}/>'

# --- Pose A: mujer con rodete, recostada, brindando ---
def brindis():
    back, front = tube()
    arm = (limb('M8 -4.8 C11.6 -4 13.6 -5 13.8 -9.6', 2.3) + f'<ellipse cx="13.8" cy="-10.6" rx="1.1" ry="1.4" fill="{FILL}" {st(.6)}/>'
           + f'<path d="M12.2 -17.2 L15.6 -17.2 L15 -11 L12.8 -11Z" fill="#E7C08E" {st(.6)}/><path d="M12.4 -14.6 h3" stroke="{LN}" stroke-width=".4"/>'
           + line('M14.6 -17 L16.4 -20', .55))
    fig = back + arm_rim(-1) + torso() + f'<g transform="translate(-.6 -11.6)">{head("bun", -8)}</g>' + front + legs() + arm
    return ripples(), fig

# --- Pose B: hombre con las manos detrás de la cabeza y las piernas cruzadas ---
def relax():
    back, front = tube()
    elbows = (limb('M-7.6 -5.6 C-10.6 -8 -11.4 -12 -9 -14.6 C-7.6 -16 -5.4 -15.6 -4 -14', 2.4)
              + limb('M7.6 -5.6 C10.6 -8 11.4 -12 9 -14.6 C7.6 -16 5.4 -15.6 4 -14', 2))
    fig = back + elbows + torso('man') + f'<g transform="translate(0 -11.6)">{head("short", 4, lips=False)}</g>' + front + legs()
    return ripples(), fig

# --- Pose C: mujer de pelo largo, una mano en el agua ---
def mano_agua():
    back, front = tube()
    hand_water = (limb('M8 -4.6 C12 -3 15 -1 17 2.6 C18.4 5.6 20 9 21.4 13', 1.9)
                  + f'<path d="M18 13.6 q1.8 -1.2 3.6 0 t3.6 0" fill="none" stroke="#FFF3E2" stroke-width=".8" stroke-linecap="round"/>')
    fig = back + arm_rim(-1) + torso() + f'<g transform="translate(.4 -11.4)">{head("long", 10)}</g>' + front + legs() + hand_water
    return ripples(), fig

POSES = {'brindis': brindis, 'relax': relax, 'mano_agua': mano_agua}

def sticker_filter(fid='stk'):
    """Sombra muy suave para asentar la ilustración sobre la foto."""
    return (f'<filter id="{fid}" x="-30%" y="-30%" width="160%" height="160%">'
            f'<feDropShadow dx="0" dy="1.4" stdDeviation="1.4" flood-color="#1a0d06" flood-opacity=".35"/></filter>')

def place(name, x, y, sc, rot=0, fid='stk'):
    agua, figura = POSES[name]()
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({sc})">{agua}<g filter="url(#{fid})">{figura}</g></g>'
