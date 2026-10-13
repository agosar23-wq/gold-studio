"""Limpia la ilustración de Canva (senora-trofeo-orig.png): saca rayitas clarito y puntitos sueltos y deja el trazo parejo."""
from PIL import Image, ImageFilter
from collections import deque
import numpy as np
S='/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad'
im = Image.open(f'{S}/ilus/senora-trofeo-orig.png').convert('RGB')
a = np.asarray(im).astype(np.float32)
H, W = a.shape[:2]
BG = np.median(a[a.sum(2) > 690], 0)
INK = np.array([139., 22., 22.])
# cuánto "tinta" tiene cada pixel (0 = fondo, 1 = línea llena), según la distancia en el eje fondo→tinta
v = INK - BG; t = ((a - BG) @ v) / (v @ v); t = np.clip(t, 0, 1)
# 1) sacar lo clarito (rayitas grises): por debajo de .38 es fondo, por arriba de .62 es línea
alpha = np.clip((t - .38) / .24, 0, 1)
# 2) sacar componentes chicos sueltos (puntitos)
ink = alpha > .5; seen = np.zeros_like(ink); keep = np.ones_like(ink)
for y in range(H):
    for x in range(W):
        if ink[y, x] and not seen[y, x]:
            q = deque([(y, x)]); seen[y, x] = True; comp = []
            while q:
                cy, cx = q.popleft(); comp.append((cy, cx))
                for dy in (-1, 0, 1):
                    for dx in (-1, 0, 1):
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < H and 0 <= nx < W and ink[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True; q.append((ny, nx))
            if len(comp) < 18:
                for (py, px) in comp: keep[py, px] = False
keep = np.asarray(Image.fromarray((keep * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3))) > 0
alpha = alpha * keep
OBG, OINK = np.array([243., 236., 226.]), np.array([122., 31., 31.])   # colores de Doña Rulos
out = OBG * (1 - alpha[..., None]) + OINK * alpha[..., None]
Image.fromarray(out.astype(np.uint8)).save(f'{S}/ilus/senora-trofeo.png')
