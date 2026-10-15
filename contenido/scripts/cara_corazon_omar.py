"""Omar · rehace la cara del corazón (la de Canva salió despareja): borra ojos/boca y dibuja una cara simétrica y prolija."""
import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter
from carogen import SCR

def arreglar(src, dst):
    im = Image.open(src).convert('RGB'); W = im.size[0]; k = W / 1500
    a = np.array(im)
    x0, y0, x1, y1 = [int(v * k) for v in (705, 740, 880, 865)]
    roi = a[y0:y1, x0:x1].astype(int)
    fondo = cv2.medianBlur(a, 31)[y0:y1, x0:x1].astype(int)
    dif = np.abs(roi - fondo).sum(2)
    lum = roi.sum(2)
    m = ((dif > 70) | (lum < 260) | (roi[..., 0] > roi[..., 1] + 15)).astype(np.uint8) * 255
    mask = np.zeros(a.shape[:2], np.uint8); mask[y0:y1, x0:x1] = m
    mask = cv2.dilate(mask, np.ones((7, 7), np.uint8))
    a = cv2.inpaint(a, mask, 9, cv2.INPAINT_TELEA)
    base = Image.fromarray(a)
    # cara nueva, dibujada a 4x y reducida
    S = 4; L = Image.new('RGBA', (W * S, W * S), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    P = lambda x, y: (x * k * S, y * k * S)
    def elipse(cx, cy, rx, ry, fill):
        d.ellipse([*P(cx - rx, cy - ry), *P(cx + rx, cy + ry)], fill=fill)
    for cx in (750, 832):
        cy = 800
        elipse(cx, cy, 19, 24, (28, 22, 10, 255))           # ojo
        elipse(cx, cy + 9, 13, 11, (92, 78, 28, 255))        # reflejo cálido abajo
        elipse(cx - 5, cy - 9, 7, 7.5, (255, 252, 230, 255)) # brillo grande
        elipse(cx + 7, cy + 9, 3, 3, (255, 252, 230, 235))   # brillo chico
        b = Image.new('RGBA', L.size, (0, 0, 0, 0)); ImageDraw.Draw(b).ellipse([*P(cx - 15, cy + 30), *P(cx + 15, cy + 41)], fill=(240, 110, 60, 170))
        L.alpha_composite(b.filter(ImageFilter.GaussianBlur(6 * S * k)))
    # sonrisa
    d.chord([*P(776, 818), *P(806, 846)], 0, 180, fill=(40, 22, 10, 255))
    d.chord([*P(782, 830), *P(800, 844)], 0, 180, fill=(210, 95, 80, 255))
    L = L.resize((W, W), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.7))
    out = base.convert('RGBA'); out.alpha_composite(L); out.convert('RGB').save(dst)

if __name__ == '__main__':
    for f in ['portadas/omar-otra-vuelta-final.png', 'omar-fix.png']:
        arreglar(f'{SCR}/{f[:-4]}.orig.png'.replace('portadas/', ''), f'{SCR}/{f}')  # siempre desde la original de Canva
