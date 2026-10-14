"""Omar Courtz · 'Otra vuelta' (concepto no oficial): ilustración (Canva, corregida) + título a mano con brillo. Genera boceto y final 1500×1500."""
import sys; sys.path.insert(0, '/home/user/gold-studio-contenido')
import numpy as np
from PIL import Image, ImageFilter
import portadas_artistas as PA
from carogen import SCR
OUT = f'{SCR}/portadas'; N = 1500
fin = Image.open(f'{OUT}/omar-otra-vuelta-final.png').convert('RGB').resize((N, N), Image.LANCZOS); fin.save(f'{OUT}/omar-final.png')
base = Image.open(f'{SCR}/omar-fix.png').convert('RGB').resize((N, N), Image.LANCZOS)
tit = Image.open(f'{SCR}/tit.png').convert('RGBA').resize((N, N), Image.LANCZOS)
NOTES = [('título a mano\ncon brillo', 60, 420, 300, 300), ('el único corazón\nque brilla', 1020, 560, 900, 760),
         ('los demás: sin cara,\nparejos', 1000, 1250, 1050, 1120), ('personaje de\nespaldas', 60, 1220, 300, 1150)]
sk = PA.sketch(base, ('omar-notas', PA.notes_html('', NOTES))).convert('RGBA')
al = tit.getchannel('A').point(lambda v: 255 if v > 150 else 0)
edge = np.asarray(al.filter(ImageFilter.FIND_EDGES)); gray = Image.new('RGBA', (N, N), (60, 60, 60, 0))
gray.putalpha(Image.fromarray(np.clip(edge * 3, 0, 230).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)))
sk.alpha_composite(gray); sk.convert('RGB').save(f'{OUT}/omar-boceto.png')
