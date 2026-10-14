"""Portadas concepto (no oficiales) para un disco nuevo de Mora: foto real con color natural (sin filtro) y título tipo sticker.
'Medio tiempo' (amigos tirados en la cancha) y 'Boleto' (parada de colectivo). Boceto + final, 1500×1500."""
import os, sys, subprocess
import numpy as np
from PIL import Image, ImageFilter, ImageOps
sys.path.insert(0, '/home/user/gold-studio-contenido')
from carogen import SCR
import portadas_artistas as PA
N = 1500; M = f'{SCR}/mora2'; OUT = f'{SCR}/portadas'
def crop_sq(path, cx=.5, cy=.5):
    im = Image.open(path).convert('RGB'); w, h = im.size; s = min(w, h)
    return im.crop((int((w - s) * cx), int((h - s) * cy), int((w - s) * cx) + s, int((h - s) * cy) + s)).resize((N, N), Image.LANCZOS)
F = PA.CSSF
TIEMPO = f'''<!doctype html><meta charset="utf-8"><style>{F}
.st{{position:absolute;left:470px;top:560px;transform:rotate(-8deg);text-align:center}}
.st b{{display:block;font-family:Bub;font-size:150px;line-height:.85;color:#FF6B2C;-webkit-text-stroke:10px #fff;paint-order:stroke fill;letter-spacing:2px;
  filter:drop-shadow(0 10px 12px rgba(0,0,0,.35))}}
.m{{position:absolute;left:1110px;top:1330px;font-family:Mark;font-size:80px;color:#fff;transform:rotate(-6deg);text-shadow:0 4px 12px rgba(0,0,0,.4)}}
</style><div class="c"><div class="st"><b>medio</b><b>tiempo</b></div><div class="m">mora</div></div>'''
BOLETO = f'''<!doctype html><meta charset="utf-8"><style>{F}
.tk{{position:absolute;left:880px;top:180px;width:470px;padding:34px 30px 30px;background:#F3D34A;transform:rotate(6deg);box-shadow:0 18px 30px rgba(0,0,0,.35);
  -webkit-mask:radial-gradient(circle 16px at 0 50%,transparent 98%,#000) left/51% 100% no-repeat,radial-gradient(circle 16px at 100% 50%,transparent 98%,#000) right/51% 100% no-repeat}}
.tk small{{display:block;font-family:'Courier New',monospace;font-weight:bold;font-size:24px;letter-spacing:4px;color:#2A2A2A}}
.tk b{{display:block;font-family:Shr,serif;font-size:118px;line-height:1;color:#1E2A6E;margin:10px 0 8px}}
.tk span{{display:flex;justify-content:space-between;font-family:'Courier New',monospace;font-weight:bold;font-size:24px;color:#2A2A2A;border-top:3px dashed #2A2A2A;padding-top:12px}}
</style><div class="c"><div class="tk"><small>LÍNEA 7 · IDA</small><b>Boleto</b><span><i>MORA</i><i>Nº 0026</i></span></div></div>'''
F2 = "@font-face{font-family:Shr;src:url(file://%s/xfonts/shrikhand.woff2)}" % SCR
BOLETO = BOLETO.replace('<style>', '<style>' + F2, 1)
NOTES = {'tiempo': [('foto real, color\nnatural, sin filtro', 80, 90, 380, 300), ('amigos = el barrio', 1000, 160, 1100, 420),
                    ('logo tipo sticker,\ncomo Microdosis', 80, 1080, 480, 880), ('nombre chiquito\na mano', 900, 1180, 1120, 1320)],
         'boleto': [('el título es\nun boleto', 520, 140, 860, 300), ('gente esperando =\nla vida de todos los días', 60, 980, 420, 820),
                    ('color natural', 940, 1220, 1050, 1100), ('foto de la calle', 80, 160, 380, 420)]}
B = f'{SCR}/bol'
# opciones de foto para 'Boleto' (posición del boleto-sticker según la foto)
BOLETO_OPC = {'boleto-a': (f'{B}/4485230.jpg', .5, .5, 'left:880px;top:150px'),      # tres chicos sentados en la parada, de frente
              'boleto-b': (f'{B}/18262969.jpg', .5, .62, 'left:90px;top:180px'),      # pareja esperando, llega el colectivo
              'boleto-c': (f'{B}/18262971.jpg', .62, .5, 'left:880px;top:900px')}     # comprando el boleto en la máquina
def build():
    for name, (path, cx, cy, pos) in BOLETO_OPC.items():
        img = crop_sq(path, cx, cy); img.save(f'{OUT}/mora-{name}-foto.png')
        ov = Image.open(PA.render_overlay(f'mora-{name}-texto', BOLETO.replace('left:880px;top:180px', pos))).convert('RGBA')
        fin = img.convert('RGBA'); fin.alpha_composite(ov); fin.convert('RGB').save(f'{OUT}/mora-{name}-final.png')
    return
    for name, img, txt in [('tiempo', crop_sq(f'{M}/8695273.jpg', .5, .55), TIEMPO), ('boleto', crop_sq(f'{M}/19515119.jpg', .5, .7), BOLETO)]:
        img.save(f'{OUT}/mora-{name}-foto.png')
        ov = Image.open(PA.render_overlay(f'mora-{name}-texto', txt)).convert('RGBA')
        fin = img.convert('RGBA'); fin.alpha_composite(ov); fin.convert('RGB').save(f'{OUT}/mora-{name}-final.png')
        al = ov.getchannel('A').point(lambda v: 255 if v > 90 else 0)
        edge = np.asarray(al.filter(ImageFilter.FIND_EDGES)); gray = Image.new('RGBA', ov.size, (60, 60, 60, 0))
        gray.putalpha(Image.fromarray(np.clip(edge * 3, 0, 230).astype(np.uint8)).filter(ImageFilter.MaxFilter(3)))
        sk = PA.sketch(img, (f'mora-{name}-notas', PA.notes_html('', NOTES[name]))).convert('RGBA'); sk.alpha_composite(gray)
        sk.convert('RGB').save(f'{OUT}/mora-{name}-boceto.png')
if __name__ == '__main__':
    build()
