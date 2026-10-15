"""Mora · 'Boleto' (concepto no oficial): foto (Canva) tal cual + título a mano en blanco. Boceto y final 1500×1500."""
import sys, subprocess, os; sys.path.insert(0, '/home/user/gold-studio-contenido')
import numpy as np
from PIL import Image, ImageFilter
import portadas_artistas as PA
from carogen import SCR
OUT = f'{SCR}/portadas'; N = 1500
base = Image.open(f'{SCR}/mora-boleto-canva.jpg').convert('RGB').resize((N, N), Image.LANCZOS)
TXT = f'''<!doctype html><meta charset="utf-8"><style>{PA.CSSF}
.t{{position:absolute;left:110px;top:120px;font-family:Mark;font-size:150px;color:#FFFFFF;transform:rotate(-6deg);text-shadow:0 2px 14px rgba(120,60,40,.35)}}
.u{{position:absolute;left:120px;top:300px;width:430px;height:14px;border-radius:7px;background:#fff;transform:rotate(-6deg);opacity:.9}}
.m{{position:absolute;right:110px;bottom:90px;font-family:Mark;font-size:64px;color:#FFFFFF;letter-spacing:3px;transform:rotate(-3deg);opacity:.95}}
</style><div class="c"><div class="t">boleto</div><div class="u"></div><div class="m">MORA</div></div>'''
ov = Image.open(PA.render_overlay('mora-boleto2-texto', TXT)).convert('RGBA')
fin = base.convert('RGBA'); fin.alpha_composite(ov); fin.convert('RGB').save(f'{OUT}/mora-final.png')
NOTES = [('título a mano,\ncomo garabato', 640, 120, 600, 220), ('foto real, color natural', 70, 560, 380, 700),
         ('una persona sola,\nesperando', 1000, 560, 860, 760), ('composición centrada', 560, 1250, 760, 1060)]
sk = PA.sketch(base, ('mora-notas', PA.notes_html('', NOTES))).convert('RGBA')
al = ov.getchannel('A').point(lambda v: 255 if v > 150 else 0)
edge = np.asarray(al.filter(ImageFilter.FIND_EDGES)); gray = Image.new('RGBA', (N, N), (60, 60, 60, 0))
gray.putalpha(Image.fromarray(np.clip(edge * 3, 0, 230).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)))
sk.alpha_composite(gray); sk.convert('RGB').save(f'{OUT}/mora-boceto.png')
fin = Image.open(f'{OUT}/mora-final.png')
fin.crop((560, 600, 900, 1060)).save(f'{OUT}/mora-det-persona.png'); fin.crop((0, 0, 900, 700)).save(f'{OUT}/mora-det-titulo.png'); fin.crop((900, 200, 1500, 1100)).save(f'{OUT}/mora-det-barrio.png')
