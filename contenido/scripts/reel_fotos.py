"""Reel con fotos a pantalla completa: "Todo lo que tu marca necesita" (branding, web, redes, tienda).
Fotos de Pexels sin personas + mockups de las marcas + los ejemplos en celular de ejemplos_fotos."""
import sys, os, subprocess, wave; sys.path.insert(0, '/home/user/gold-studio-contenido')
import numpy as np
import reelgen as R
from reelgen import SCR, F, SP, LOGO, FPS
from marcas_ejemplo import FONTS as BFONTS
from mockups_marcas import OUT as MK
import ejemplos_fotos as E

NAME = 'reel-todo-lo-que-tu-marca-necesita'
RF = SCR + '/reelfotos/'           # fotos de Pexels en alta (alto 2200)
ph = lambda i: f'file://{RF}{i}.jpg'
mk = lambda n: f'file://{MK}{n}.jpg'

def cel(inner, w, h, scale):
    return f'<div style="transform:scale({scale});transform-origin:50% 0">{E.phone(inner, w, h)}</div>'

# img, posición, eyebrow, texto, celular (html) o None, duración
SCENES = [
 dict(img=ph('30234391'), pos='50% 60%', eb='Gold Studio', text='Todo lo que tu marca *necesita*', dur=3.0),
 dict(img=mk('almendra-bolsa'), pos='50% 50%', eb='Branding', text='Una marca *que se recuerde.*', dur=2.8),
 dict(img=mk('nacar-tarjetas-alta'), pos='50% 50%', eb='Branding', text='Linda *en cada detalle.*', top=True, txstyle='top:130px;gap:18px', dur=2.6),
 dict(img=ph('30234378'), pos='50% 50%', eb='Página web', text='Tu página, *lista para vender.*', phone=cel(E.mob_a, 250, 520, 2.1), dur=3.2),
 dict(img=ph('6177685'), pos='50% 50%', eb='Redes', text='Tus redes, *siempre lindas.*', phone=cel(E.ig_n, 340, 650, 1.62), dur=3.2),
 dict(img=ph('5706275'), pos='50% 50%', eb='Tienda online', text='Vendé *las 24 horas.*', phone=cel(E.shop_o, 330, 640, 1.65), dur=3.2),
 dict(img=ph('30234389'), pos='50% 50%', end=True, text='¿Arrancamos con *tu marca?*', pill='Escribime y lo charlamos', dur=3.6),
]

def words(text, sid):
    out, em = [], False
    for j, tok in enumerate(text.split(' ')):
        if tok.startswith('*'): em = True
        cls = 'w em' if em else 'w'
        out.append(f'<span class="{cls}" id="{sid}w{j}">{tok.replace("*", "")}</span>')
        if tok.rstrip('.,?!').endswith('*'): em = False
    return ' '.join(out), len(out)

def build():
    starts, t = [], 0.0
    for s in SCENES: starts.append(t); t += s['dur']
    total = round(t + 0.1, 2); parts = []
    for i, s in enumerate(SCENES):
        wh, nw = words(s['text'], f's{i}')
        top = bool(s.get('phone') or s.get('top'))
        shade = ('linear-gradient(rgba(28,26,23,.82),rgba(28,26,23,.35) 32%,rgba(28,26,23,0) 50%)' if top else
                 'rgba(28,26,23,.62)' if s.get('end') else
                 'linear-gradient(rgba(28,26,23,0) 42%,rgba(28,26,23,.55) 64%,rgba(28,26,23,.9))')
        txt = (f'<div class="tx {"top" if top else "end" if s.get("end") else "bot"}" style="{s.get("txstyle", "")}">'
               + (f'<div class="spk" id="s{i}spk">{SP}</div>' if s.get('end') else '')
               + (f'<div class="eb" id="s{i}eb">{s["eb"]}</div>' if s.get('eb') else '')
               + f'<h1>{wh}</h1>'
               + (f'<div class="pill" id="s{i}pill">{s["pill"]}</div>' if s.get('pill') else '')
               + (f'<div class="lgw" id="s{i}lg">{LOGO}</div>' if s.get('end') else '') + '</div>')
        phone = f'<div class="ph" id="s{i}ph">{s["phone"]}</div>' if s.get('phone') else ''
        parts.append(f'<div class="sc" id="s{i}" data-start="{starts[i]}" data-dur="{s["dur"]}" data-nw="{nw}">'
                     f'<img class="bg" id="s{i}bg" src="{s["img"]}" style="object-position:{s["pos"]}"><div class="sh" style="background:{shade}"></div>'
                     f'{phone}{txt}<div class="frame"></div></div>')
    css = BFONTS + f'''
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#1C1A17}}
.sc{{position:absolute;inset:0;opacity:0;overflow:hidden;font-family:J;color:#FAF6EE}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;will-change:transform}}
.sh{{position:absolute;inset:0}}
.frame{{position:absolute;inset:40px;border:2px solid rgba(201,163,78,.7);border-radius:8px}}
.tx{{position:absolute;left:100px;right:100px;display:flex;flex-direction:column;gap:30px}}
.tx.bot{{bottom:260px}} .tx.top{{top:200px}} .tx.end{{top:0;bottom:0;justify-content:center;align-items:center;text-align:center}}
.eb{{font-size:30px;letter-spacing:.4em;text-transform:uppercase;font-weight:500;color:#C9A34E}}
h1{{font-family:B;font-weight:500;font-size:118px;line-height:1.06;margin:0;letter-spacing:-.01em}}
.tx.top h1{{font-size:96px}} .tx[style*='130px'] h1{{font-size:86px}}
.w{{display:inline-block}} .em{{font-style:italic;color:#C9A34E}}
.ph{{position:absolute;left:0;right:0;top:640px;display:flex;justify-content:center}}
.spk{{width:120px;height:120px;color:#C9A34E}} .sp{{width:100%;height:100%;display:block}}
.pill{{background:#C9A34E;color:#1C1A17;font-size:40px;padding:28px 54px;border-radius:999px;font-weight:500}}
.lgw{{width:360px;margin-top:40px;color:#FAF6EE}} .logo{{width:100%;height:auto;display:block}}
'''
    js = '''
const E=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
const B=x=>{x=Math.max(0,Math.min(1,x));const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};
const $=id=>document.getElementById(id);
function up(el,p,d=70){if(!el)return;el.style.opacity=E(p);el.style.transform=`translateY(${(1-E(p))*d}px)`;}
const SC=[...document.querySelectorAll('.sc')];
window.render=function(t){
  SC.forEach((s,i)=>{
    const a=+s.dataset.start, d=+s.dataset.dur, k=t-a, nw=+s.dataset.nw;
    s.style.opacity = i===0 ? 1 : (k>=0?Math.min(1,k/0.35):0);
    if(k<0||k>d+0.5) return;
    const z=1.14-0.12*Math.min(1,k/(d+0.35)), dx=(i%2?1:-1)*20*Math.min(1,k/d);
    $(`s${i}bg`).style.transform=`scale(${z}) translateX(${dx}px)`;
    up($(`s${i}eb`),(k-0.15)/0.4,40);
    for(let j=0;j<nw;j++) up($(`s${i}w${j}`),(k-0.3-j*0.06)/0.45,80);
    const ph=$(`s${i}ph`); if(ph){const p=E((k-0.2)/0.8);ph.style.opacity=Math.min(1,p*2);ph.style.transform=`translateY(${(1-p)*700}px) rotate(${(1-p)*5}deg)`;}
    const spk=$(`s${i}spk`); if(spk){const p=B((k-0.1)/0.55);spk.style.transform=`scale(${p}) rotate(${(1-p)*-90}deg)`;}
    up($(`s${i}pill`),(k-0.3-nw*0.06-0.3)/0.45,50); up($(`s${i}lg`),(k-1.2)/0.5,30);
  });
};
'''
    page = f'<!doctype html><meta charset="utf-8"><style>{css}</style>{"".join(parts)}<script>{js}</script>'
    work = f'{SCR}/rf-{NAME}'; os.makedirs(work + '/f', exist_ok=True)
    for f in os.listdir(work + '/f'): os.remove(os.path.join(work, 'f', f))
    open(f'{work}/r.html', 'w').write(page)
    subprocess.run(['node', f'{SCR}/reel.js', f'{work}/r.html', str(total), f'{work}/f'], check=True,
                   env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    sonido(starts, total, f'{work}/a.wav')
    import imageio_ffmpeg
    out_dir = '/home/user/gold-studio-final/reels'; os.makedirs(out_dir, exist_ok=True); out = f'{out_dir}/{NAME}.mp4'
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{work}/f/%04d.jpg', '-i', f'{work}/a.wav',
                    '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-preset', 'slow',
                    '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], check=True)
    open(out.replace('.mp4', '.txt'), 'w').write(CAPTION)
    return out, total

def sonido(starts, total, path):
    SR = R.SR; out = np.zeros(int(SR * (total + 2)))
    def add(sig, t):
        i = int(max(0, t) * SR); out[i:i + len(sig)] += sig[:len(out) - i]
    for i, s in enumerate(SCENES):
        a = starts[i]; nw = len(s['text'].split())
        if i == 0: add(R.boom(), a + 0.02)
        else: add(R.whoosh(0.45, 300, 3800, 0.7), a - 0.2)
        for j in range(nw): add(R.tick(0.1), a + 0.3 + j * 0.06)
        add(R.pop(0.35, 1000 + 120 * (i % 3)), a + 0.3 + nw * 0.06 + 0.1)
        if s.get('phone'): add(R.whoosh(0.6, 150, 1600, 0.6), a + 0.2)
        if s.get('end'):
            add(R.riser(0.6, 0.45), a - 0.6); add(R.boom(0.6), a); add(R.chime(0.5), a + 0.15)
            add(R.tap(0.4), a + 0.3 + nw * 0.06 + 0.35); add(R.chime(0.35), a + 1.3)
    out = out[:int(SR * total)]; fade = int(0.25 * SR); out[-fade:] *= np.linspace(1, 0, fade)
    out = np.tanh(out * 1.6) / np.tanh(1.6); out = out / (np.abs(out).max() + 1e-9) * 0.95
    pcm = (out * 32767).astype('<i2')
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.column_stack([pcm, pcm]).ravel().tobytes())

CAPTION = '''Todo lo que tu marca necesita, en un solo lugar.

Branding para que te recuerden. Una página lista para vender. Redes siempre lindas. Y una tienda que vende mientras dormís.

Todo con la misma línea, para que tu marca se vea profesional en cada lugar.

¿Arrancamos con la tuya? Escribime y lo charlamos.

#branding #emprendedoras #diseñoweb'''

if __name__ == '__main__':
    print(*build())
