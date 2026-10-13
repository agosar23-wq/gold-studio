"""Mockups reales: pega los logos de marcas_ejemplo sobre fotos de Pexels de productos en blanco."""
import sys, os; sys.path.insert(0, '/home/user/gold-studio-contenido')
import numpy as np
from PIL import Image, ImageDraw
from carogen import SCR
from marcas_ejemplo import LOGOS, BRANDS

SRC = SCR + '/mock/src/'          # fotos de Pexels (nombre = id)
OUT = SCR + '/mock/out/'

def logo(name):
    im = Image.open(f'{LOGOS}/{name}.png').convert('RGBA')
    return im.crop(im.getchannel('A').getbbox())

def coeffs(dst, src):
    """Coeficientes PERSPECTIVE de PIL: para cada punto de salida (dst) da el de entrada (src)."""
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; B += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()

def cylinder(im, ang=0.95):
    """Curva el logo como si estuviera impreso en un vaso."""
    a = np.asarray(im); h, w = a.shape[:2]
    x = np.linspace(-1, 1, w)
    src = np.arcsin(np.clip(x * np.sin(ang), -1, 1)) / ang          # -1..1
    idx = np.clip(((src + 1) / 2 * (w - 1)).round().astype(int), 0, w - 1)
    return Image.fromarray(a[:, idx])

def fit(lg, quad, pad=0.0):
    """Ajusta el logo al cuadrilátero manteniendo proporción (lo centra)."""
    q = np.array(quad, float)
    qw = (np.linalg.norm(q[1] - q[0]) + np.linalg.norm(q[2] - q[3])) / 2
    qh = (np.linalg.norm(q[3] - q[0]) + np.linalg.norm(q[2] - q[1])) / 2
    w, h = lg.size; ra, rq = w / h, qw / qh
    W, H = (w, int(w / rq)) if ra > rq else (int(h * rq), h)
    W, H = int(W * (1 + pad)), int(H * (1 + pad))
    c = Image.new('RGBA', (W, H), (0, 0, 0, 0)); c.paste(lg, ((W - w) // 2, (H - h) // 2)); return c

def warp(lg, quad, size):
    w, h = lg.size
    return lg.transform(size, Image.PERSPECTIVE, coeffs(quad, [(0, 0), (w, 0), (w, h), (0, h)]), Image.BICUBIC)

def blend(photo, layer, mode='multiply', opacity=1.0):
    p = np.asarray(photo, float) / 255; l = np.asarray(layer, float) / 255
    a = l[..., 3:4] * opacity; c = l[..., :3]
    if mode == 'multiply':
        r = p * (1 - a + a * c)
    else:   # tinta clara: toma la luz y sombra de la foto
        lum = p.mean(axis=2, keepdims=True); ref = np.percentile(lum[a[..., 0] > .5], 70) if (a > .5).any() else lum.mean()
        shade = np.clip(lum / max(ref, 1e-3), .55, 1.15)
        r = p * (1 - a) + np.clip(c * shade, 0, 1) * a
    return Image.fromarray((np.clip(r, 0, 1) * 255).astype('uint8'))

def put(photo, name, quad, mode='multiply', pad=.0, cyl=0, opacity=.96):
    lg = logo(name)
    if cyl: lg = cylinder(fit(lg, quad, pad), cyl)
    else: lg = fit(lg, quad, pad)
    return blend(photo, warp(lg, quad, photo.size), mode, opacity)

def fill(photo, poly, color, opacity=1.0, blur=1.5):
    from PIL import ImageFilter
    m = Image.new('L', photo.size, 0); ImageDraw.Draw(m).polygon([tuple(p) for p in poly], fill=255); m = m.filter(ImageFilter.GaussianBlur(blur))
    lay = Image.new('RGBA', photo.size, color); lay.putalpha(m)
    return blend(photo, lay, 'multiply', opacity)

def tag_quad(A, B, C, D, u0, u1, v0, v1):
    """A,D: borde de arriba (de la punta de abajo a la del agujero); B,C: borde de abajo."""
    A, B, C, D = map(np.array, (A, B, C, D))
    P = lambda u, v: (A + (D - A) * u) * (1 - v) + (B + (C - B) * u) * v
    return [tuple(P(u0, v0)), tuple(P(u1, v0)), tuple(P(u1, v1)), tuple(P(u0, v1))]

CROP = {  # recorte sobre el producto (x0, y0, x1, y1)
 'almendra-bolsa': (200, 100, 1500, 1900), 'almendra-paquete': (300, 0, 1300, 1067), 'almendra-vaso': (300, 900, 1300, 2150),
 'ondina-etiqueta': (100, 0, 1500, 1066), 'ondina-tote': (500, 50, 1400, 900), 'ondina-tote-negra': (150, 150, 1150, 1600),
 'nacar-frascos': (400, 250, 1200, 950), 'nacar-bolsas': (250, 180, 1400, 1000), 'nacar-tarjetas': (200, 450, 1450, 2100),
 'nube-vasos': (280, 160, 980, 980), 'nube-caja': (200, 150, 1400, 950), 'nube-paquetes': (330, 30, 1270, 1063), 'nacar-bolsa': (760, 230, 1310, 900)}

def col(b, i): return BRANDS[b]['colores'][i][1]

def build():
    os.makedirs(OUT, exist_ok=True)
    def ph(i): return Image.open(SRC + f'{i}.jpg').convert('RGB')
    M = {}
    # ---------- Almendra (pastelería) ----------
    im = put(ph('8490370'), 'almendra-full-dark', [(700, 860), (1150, 845), (1168, 1390), (712, 1405)], pad=.05)
    M['almendra-bolsa'] = im
    im = put(ph('12039675'), 'almendra-full-dark', [(640, 390), (950, 390), (950, 820), (640, 820)], pad=.08)
    M['almendra-paquete'] = im
    im = put(ph('8015715'), 'almendra-word-dark', [(620, 1470), (1000, 1470), (995, 1660), (628, 1660)], pad=.04, cyl=.95)
    M['almendra-vaso'] = im
    # ---------- Ondina (moda) ----------
    q = tag_quad((282, 698), (535, 982), (1150, 398), (905, 163), .12, .74, .2, .8)
    M['ondina-etiqueta'] = put(ph('11485130'), 'ondina-word-dark', q, pad=.02, opacity=.92)
    M['ondina-tote'] = put(ph('6787035'), 'ondina-full-dark', [(830, 420), (1105, 420), (1112, 710), (822, 710)], pad=.1)
    M['ondina-tote-negra'] = put(ph('1214212'), 'ondina-full-light', [(455, 900), (870, 875), (874, 1330), (459, 1355)], mode='ink', pad=.12)
    # ---------- Nácar (estética y spa) ----------
    im = ph('12024942')
    im = put(im, 'nacar-full-dark', [(888, 520), (1032, 520), (1032, 760), (888, 760)], pad=.06)
    im = put(im, 'nacar-iso-accent', [(598, 470), (702, 470), (700, 560), (600, 560)], pad=.0)
    M['nacar-frascos'] = im
    im = ph('12024975')
    im = fill(im, [(823, 331), (1245, 331), (1245, 893), (823, 893)], col('nacar', 1), .95)
    im = put(im, 'nacar-full-light', [(880, 480), (1190, 480), (1190, 760), (880, 760)], mode='ink', pad=.1)
    im = put(im, 'nacar-full-dark', [(410, 610), (690, 610), (690, 820), (410, 820)], pad=.15)
    M['nacar-bolsas'] = im; M['nacar-bolsa'] = im
    im = ph('4466176')
    im = fill(im, [(392, 598), (1242, 592), (1252, 1162), (388, 1174)], col('nacar', 0), 1)
    im = put(im, 'nacar-full-light', [(560, 700), (1080, 698), (1084, 1070), (562, 1074)], mode='ink', pad=.1)
    im = put(im, 'nacar-iso-dark', [(700, 1500), (990, 1498), (992, 1800), (702, 1802)], pad=.1)
    M['nacar-tarjetas'] = im
    # ---------- Nube (heladería) ----------
    im = ph('8015718')
    for cx, cy in [(431, 553), (800, 550)]:
        im = put(im, 'nube-badge', [(cx - 84, cy - 86), (cx + 84, cy - 86), (cx + 84, cy + 86), (cx - 84, cy + 86)], mode='ink', cyl=.5, opacity=1)
    M['nube-vasos'] = im
    im = ph('12039676')
    im = fill(im, [(336, 250), (1266, 250), (1268, 806), (336, 806)], col('nube', 2), 1)
    im = put(im, 'nube-full-dark', [(560, 330), (1040, 330), (1040, 730), (560, 730)], pad=.06)
    M['nube-caja'] = im
    im = ph('12024976')
    im = put(im, 'nube-full-dark', [(445, 430), (715, 430), (712, 760), (448, 760)], pad=.12)
    im = put(im, 'nube-iso-dark', [(900, 470), (1140, 470), (1138, 700), (902, 700)], pad=.1)
    M['nube-paquetes'] = im
    for k, v in M.items(): v.crop(CROP[k]).save(OUT + k + '.jpg', quality=90)
    print(len(M), OUT)

if __name__ == '__main__':
    build()
