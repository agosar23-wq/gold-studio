"""Reemplaza el corazón oscuro con error (arriba a la izquierda) por una copia de uno bien hecho, con máscara en forma de corazón."""
import cv2, numpy as np, sys
S='/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad'
src_path = sys.argv[1] if len(sys.argv) > 1 else f'{S}/omar-orig.jpg'
im = cv2.imread(src_path); H, W = im.shape[:2]
def heart_mask(cx, top, w, h):
    m = np.zeros((H, W), np.uint8); r = w // 4
    cv2.circle(m, (cx - r, top + r), r, 255, -1); cv2.circle(m, (cx + r, top + r), r, 255, -1)
    pts = np.array([[cx - 2 * r, top + r], [cx + 2 * r, top + r], [cx, top + h]], np.int32); cv2.fillPoly(m, [pts], 255)
    return m
# corazón fuente (bien hecho) y destino (con error), centro x, borde de arriba, ancho, alto
SX, ST, SW, SH = 706, 776, 140, 120
DX, DT, DW, DH = 281, 776, 134, 116
M = cv2.translate = None
shift = np.float32([[1, 0, DX - SX], [0, 1, DT - ST]])
moved = cv2.warpAffine(im, shift, (W, H))
mask = heart_mask(DX, DT, DW, DH)
mask[:, 350:] = 0                                  # no tocar el gorro
mask[842:, :] = 0                                  # ni el corazón verde de abajo
mask = cv2.GaussianBlur(cv2.erode(mask, np.ones((5, 5), np.uint8)), (5, 5), 0).astype(np.float32)[..., None] / 255
out = (moved * mask + im * (1 - mask)).astype(np.uint8)
b, g, r = [out[..., i].astype(int) for i in range(3)]
red = ((r - g > 50) & (r - b > 30) & (r > 120)).astype(np.uint8) * 255   # marca roja de la captura (si la hay)
if red.any():
    out = cv2.inpaint(out, cv2.dilate(red, np.ones((7, 7), np.uint8)), 4, cv2.INPAINT_NS)
cv2.imwrite(f'{S}/omar-fix.png', out)
cv2.imwrite(f'{S}/omar-fix-zoom.png', cv2.resize(out[690:900, 180:470], (870, 630)))
