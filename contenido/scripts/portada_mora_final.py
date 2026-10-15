"""Mora · 'Boleto': foto (Canva) tal cual + título a mano en bordó (con MORA al lado). Boceto y final 1500×1500."""
import sys, subprocess, os; sys.path.insert(0, '/home/user/gold-studio-contenido')
import numpy as np
from PIL import Image, ImageFilter
import portadas_artistas as PA
from carogen import SCR
OUT = f'{SCR}/portadas'; N = 1500
base = Image.open(f'{SCR}/mora-boleto-canva.jpg').convert('RGB').resize((N, N), Image.LANCZOS)
TXT = f'''<!doctype html><meta charset="utf-8"><style>{PA.CSSF}
.t{{position:absolute;left:110px;top:120px;font-family:Mark;font-size:150px;color:#3B1424;transform:rotate(-6deg);text-shadow:0 3px 12px rgba(255,240,230,.55)}}
.u{{position:absolute;left:120px;top:300px;width:430px;height:14px;border-radius:7px;background:#3B1424;transform:rotate(-6deg);opacity:.9}}
.m{{position:absolute;left:640px;top:205px;font-family:Mark;font-size:62px;color:#3B1424;letter-spacing:3px;transform:rotate(-6deg);text-shadow:0 3px 12px rgba(255,240,230,.55)}}
</style><div class="c"><div class="t">boleto</div><div class="u"></div><div class="m">MORA</div></div>'''
ov = Image.open(PA.render_overlay('mora-boleto2-texto', TXT)).convert('RGBA')
fin = base.convert('RGBA'); fin.alpha_composite(ov); fin.convert('RGB').save(f'{OUT}/mora-final.png')
# (texto, x, y, flecha desde (sx, sy) hasta (ax, ay)) - notas en zonas libres y con fondo papel para que nada tape las letras
NOTES = [('título a mano, como garabato', 640, 60, 640, 100, 560, 165), ('foto real,\ncolor natural', 30, 420, 300, 550, 520, 640),
         ('una persona sola,\nesperando', 60, 1290, 330, 1290, 600, 1060), ('composición centrada', 800, 1240, 820, 1240, 760, 1150)]
arr = ''.join(f'<path d="M{sx} {sy} Q{(sx+ax)/2+40} {(sy+ay)/2-40} {ax} {ay}"/>' for t, x, y, sx, sy, ax, ay in NOTES)
def head(sx, sy, ax, ay):
    import math; a = math.atan2(ay - sy, ax - sx); L = 28
    return ''.join(f'<path d="M{ax} {ay} l{L*math.cos(a+math.pi-d):.1f} {L*math.sin(a+math.pi-d):.1f}"/>' for d in (.45, -.45))
arr += ''.join(head(sx, sy, ax, ay) for t, x, y, sx, sy, ax, ay in NOTES)
lab = ''.join(f'<div class="nt" style="left:{x}px;top:{y}px">{t}</div>' for t, x, y, *_ in NOTES)
NOTAS = f'''<!doctype html><meta charset="utf-8"><style>{PA.CSSF}
.nt{{position:absolute;font-family:Hand;font-size:58px;line-height:1.05;color:#9A7426;white-space:pre-line;background:rgba(250,247,240,.92);padding:4px 14px 8px;border-radius:10px}}</style><div class="c">
<svg style="position:absolute;inset:0" width="{N}" height="{N}" fill="none" stroke="#B8923A" stroke-width="5" stroke-linecap="round">{arr}</svg>{lab}</div>'''
sk = PA.sketch(base, ('mora-notas', NOTAS)).convert('RGBA')
al = ov.getchannel('A').point(lambda v: 255 if v > 150 else 0)
edge = np.asarray(al.filter(ImageFilter.FIND_EDGES)); gray = Image.new('RGBA', (N, N), (60, 60, 60, 0))
gray.putalpha(Image.fromarray(np.clip(edge * 3, 0, 230).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)))
sk.alpha_composite(gray); sk.convert('RGB').save(f'{OUT}/mora-boceto.png')
fin = Image.open(f'{OUT}/mora-final.png')
fin.crop((560, 600, 900, 1060)).save(f'{OUT}/mora-det-persona.png'); fin.crop((0, 0, 900, 700)).save(f'{OUT}/mora-det-titulo.png'); fin.crop((900, 200, 1500, 1100)).save(f'{OUT}/mora-det-barrio.png')
