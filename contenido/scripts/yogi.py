"""Ícono de ejemplo: flor de loto geométrica (línea fina)."""
def yogi(c, size, sw=2.2):
    P = 'M0 0 C-20 -28 -20 -66 0 -96 C20 -66 20 -28 0 0 Z'
    petals = ''.join(f'<path d="{P}" transform="translate(100 150) rotate({r}) scale({k})"/>' for r, k in [(-68, .62), (68, .62), (-36, .82), (36, .82), (0, 1)])
    return (f'<svg width="{size}" height="{size}" viewBox="20 30 160 150" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">'
            f'{petals}<path d="M44 160 Q100 176 156 160"/><path d="M62 170 Q100 180 138 170"/>'
            f'<circle cx="100" cy="40" r="3.2" fill="{c}" stroke="none"/></svg>')
