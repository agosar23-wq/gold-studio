"""Versión editada del reel con fotos: música original, cortes a tiempo, transiciones variadas,
pulso al ritmo, destellos dorados y grano. Usa el contenido de reel_fotos (fotos, textos y celulares)."""
import sys, os, subprocess, wave; sys.path.insert(0, '/home/user/gold-studio-contenido')
import numpy as np
from PIL import Image
import reelgen as R
from reelgen import SCR, SP, LOGO, FPS
from marcas_ejemplo import FONTS as BFONTS
import reel_fotos as RF
from musica import musica, BEAT, SR

NAME = 'reel-todo-lo-que-tu-marca-necesita'
# tiempos (en beats de 0,5 s) y transición de entrada de cada escena
BEATS = [6, 6, 6, 6, 6, 6, 8]
TRANS = [None, 'zoom', 'whip', 'wipe', 'slide', 'diag', 'flash']
INTRO = 2   # la batería entra en el beat 2 (cuando arranca el texto)

def grain(path):
    if os.path.exists(path): return
    n = (np.random.default_rng(1).standard_normal((540, 540)) * 40 + 128).clip(0, 255).astype('uint8')
    Image.fromarray(n, 'L').save(path)

def build():
    scenes = RF.SCENES
    starts, t = [], 0.0
    for b in BEATS: starts.append(t); t += b * BEAT
    total = round(t + 1.2, 2)
    work = f'{SCR}/rfe-{NAME}'; os.makedirs(work + '/f', exist_ok=True)
    for f in os.listdir(work + '/f'): os.remove(os.path.join(work, 'f', f))
    grain(f'{work}/grain.png')
    parts = []
    for i, s in enumerate(scenes):
        wh, nw = RF.words(s['text'], f's{i}')
        top = bool(s.get('phone') or s.get('top'))
        shade = ('linear-gradient(rgba(28,26,23,.82),rgba(28,26,23,.35) 32%,rgba(28,26,23,0) 50%)' if top else
                 'rgba(28,26,23,.62)' if s.get('end') else
                 'linear-gradient(rgba(28,26,23,0) 42%,rgba(28,26,23,.55) 64%,rgba(28,26,23,.9))')
        txt = (f'<div class="tx {"top" if top else "end" if s.get("end") else "bot"}" style="{s.get("txstyle", "")}">'
               + (f'<div class="spk" id="s{i}spk">{SP}</div>' if s.get('end') else '')
               + (f'<div class="eb" id="s{i}eb"><i id="s{i}ln"></i>{s["eb"]}</div>' if s.get('eb') else '')
               + f'<h1>{wh}</h1>'
               + (f'<div class="pill" id="s{i}pill">{s["pill"]}</div>' if s.get('pill') else '')
               + (f'<div class="lgw" id="s{i}lg">{LOGO}</div>' if s.get('end') else '') + '</div>')
        phone = f'<div class="ph" id="s{i}ph">{s["phone"]}</div>' if s.get('phone') else ''
        parts.append(f'<div class="sc" id="s{i}" data-start="{starts[i]}" data-dur="{BEATS[i] * BEAT}" data-nw="{nw}" data-tr="{TRANS[i] or ""}">'
                     f'<div class="cam" id="s{i}cam"><img class="bg" id="s{i}bg" src="{s["img"]}" style="object-position:{s["pos"]}"></div>'
                     f'<div class="sh" style="background:{shade}"></div>{phone}{txt}</div>')
    css = BFONTS + f'''
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#1C1A17}}
.sc{{position:absolute;inset:0;overflow:hidden;font-family:J;color:#FAF6EE;visibility:hidden}}
.cam{{position:absolute;inset:-60px}}
.bg{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}}
.sh{{position:absolute;inset:0}}
.tx{{position:absolute;left:100px;right:100px;display:flex;flex-direction:column;gap:30px}}
.tx.bot{{bottom:260px}} .tx.top{{top:200px}} .tx.end{{top:0;bottom:0;justify-content:center;align-items:center;text-align:center}}
.eb{{font-size:30px;letter-spacing:.4em;text-transform:uppercase;font-weight:500;color:#C9A34E;display:flex;align-items:center;gap:22px}}
.eb i{{display:block;height:2px;width:0;background:#C9A34E}}
.tx.end .eb i{{display:none}}
h1{{font-family:B;font-weight:500;font-size:118px;line-height:1.06;margin:0;letter-spacing:-.01em}}
.tx.top h1{{font-size:96px}} .tx[style*='130px'] h1{{font-size:86px}}
.w{{display:inline-block}} .em{{font-style:italic;color:#C9A34E}}
.ph{{position:absolute;left:0;right:0;top:640px;display:flex;justify-content:center}}
.spk{{width:120px;height:120px;color:#C9A34E}} .sp{{width:100%;height:100%;display:block}}
.pill{{background:#C9A34E;color:#1C1A17;font-size:40px;padding:28px 54px;border-radius:999px;font-weight:500}}
.lgw{{width:360px;margin-top:40px;color:#FAF6EE}} .logo{{width:100%;height:auto;display:block}}
#frame{{position:absolute;inset:40px;border:2px solid rgba(201,163,78,.7);border-radius:8px;z-index:50;pointer-events:none}}
#flash{{position:absolute;inset:0;background:#FFF8EA;opacity:0;z-index:40}}
#leak{{position:absolute;width:1400px;height:1400px;border-radius:50%;background:radial-gradient(circle,rgba(233,190,110,.85),rgba(201,163,78,.35) 40%,rgba(201,163,78,0) 70%);
      mix-blend-mode:screen;opacity:0;z-index:41;left:-160px;top:260px}}
#grain{{position:absolute;inset:-100px;background:url(grain.png);opacity:.07;mix-blend-mode:overlay;z-index:45}}
#vig{{position:absolute;inset:0;background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,0) 55%,rgba(0,0,0,.35));z-index:44}}
'''
    js = '''
const E=x=>x<0?0:x>1?1:1-Math.pow(1-x,3), EI=x=>x<0?0:x>1?1:x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const B=x=>{x=Math.max(0,Math.min(1,x));const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};
const $=id=>document.getElementById(id); const BEAT=%BEAT%, INTRO=%INTRO%, TOTALB=%TOTALB%;
const SC=[...document.querySelectorAll('.sc')], TR=0.5;
function up(el,p,d=70,bl=0){if(!el)return;const q=E(p);el.style.opacity=q;el.style.transform=`translateY(${(1-q)*d}px)`;el.style.filter=bl?`blur(${(1-q)*bl}px)`:'';}
window.render=function(t){
  const flash=$('flash'), leak=$('leak'); flash.style.opacity=0; leak.style.opacity=0;
  // pulso con el bombo
  const b=t/BEAT, inDr=b>=INTRO&&b<TOTALB-4, ph=b-Math.floor(b), pulse=inDr?Math.exp(-ph*BEAT/0.09):0;
  $('grain').style.transform=`translate(${(Math.floor(t*24)*37)%100-50}px,${(Math.floor(t*24)*61)%100-50}px)`;
  SC.forEach((s,i)=>{
    const a=+s.dataset.start, d=+s.dataset.dur, k=t-a, nw=+s.dataset.nw, tr=s.dataset.tr;
    const nx=SC[i+1], kn=nx? t-(+nx.dataset.start) : -1, trn=nx?nx.dataset.tr:'';
    const vis = k>=0 && (kn<TR || !nx);
    s.style.visibility = vis?'visible':'hidden'; if(!vis) return;
    s.style.zIndex=i; let tf='', fl='', cp='none', op=1;
    // entrada
    if(k<TR){ const p=k/TR;
      if(tr==='zoom'){ tf=`scale(${1.5-0.5*E(p)})`; fl=`blur(${(1-E(p))*22}px)`; op=Math.min(1,p*3); }
      if(tr==='whip'){ tf=`translateX(${(1-EI(p))*1200}px)`; fl=`blur(${Math.sin(Math.PI*Math.min(1,p))*26}px)`; }
      if(tr==='wipe'){ cp=`circle(${E(p)*120}% at 50% 62%)`; }
      if(tr==='slide'){ tf=`translateY(${(1-EI(p))*1920}px)`; }
      if(tr==='diag'){ const x=EI(p)*260-60; cp=`polygon(0 0,${x}% 0,${x-60}% 100%,0 100%)`; }
      if(tr==='flash'){ flash.style.opacity=Math.max(+flash.style.opacity,1-E(p*1.4)); }
      if(tr && tr!=='flash'){ leak.style.opacity=Math.max(+leak.style.opacity,Math.sin(Math.PI*p)*0.75); leak.style.transform=`translateX(${(p-0.5)*900}px)`; }
    }
    // salida (cuando entra la siguiente)
    if(nx && kn>=0){ const p=kn/TR;
      if(trn==='whip'){ tf=`translateX(${-EI(p)*1200}px)`; fl=`blur(${Math.sin(Math.PI*p)*26}px)`; }
      if(trn==='slide'){ tf=`translateY(${-EI(p)*500}px) scale(${1-0.08*EI(p)})`; fl=`brightness(${1-0.5*p})`; }
      if(trn==='zoom'){ tf=`scale(${1+0.25*EI(p)})`; }
      if(trn==='flash' && p>0.05){ op=0; }
    }
    s.style.transform=tf; s.style.filter=fl; s.style.clipPath=cp; s.style.opacity=op;
    // cámara lenta sobre la foto + pulso
    const z=1.12-0.10*Math.min(1,k/(d+TR))+0.018*pulse, dx=(i%2?1:-1)*24*Math.min(1,k/d);
    $(`s${i}cam`).style.transform=`scale(${z}) translateX(${dx}px)`;
    // textos
    const t0=i===0?BEAT*INTRO-0.15:0.32;
    up($(`s${i}eb`),(k-t0+0.1)/0.4,30); const ln=$(`s${i}ln`); if(ln) ln.style.width=E((k-t0)/0.5)*70+'px';
    for(let j=0;j<nw;j++) up($(`s${i}w${j}`),(k-t0-0.12-j*0.07)/0.45,90,16);
    const phn=$(`s${i}ph`); if(phn){const p=E((k-0.35)/0.8);phn.style.opacity=Math.min(1,p*2);phn.style.transform=`translateY(${(1-p)*800}px) rotate(${(1-p)*7}deg) scale(${1+0.01*pulse})`;}
    const spk=$(`s${i}spk`); if(spk){const p=B((k-0.15)/0.55);spk.style.transform=`scale(${p*(1+0.08*pulse)}) rotate(${(1-p)*-120+k*20}deg)`;}
    up($(`s${i}pill`),(k-t0-0.12-nw*0.07-0.3)/0.45,50); up($(`s${i}lg`),(k-1.4)/0.6,30,10);
  });
};
'''.replace('%BEAT%', str(BEAT)).replace('%INTRO%', str(INTRO)).replace('%TOTALB%', str(sum(BEATS)))
    page = (f'<!doctype html><meta charset="utf-8"><style>{css}</style>{"".join(parts)}'
            '<div id="vig"></div><div id="flash"></div><div id="leak"></div><div id="grain"></div><div id="frame"></div>'
            f'<script>{js}</script>')
    open(f'{work}/r.html', 'w').write(page)
    subprocess.run(['node', f'{SCR}/reel.js', f'{work}/r.html', str(total), f'{work}/f'], check=True,
                   env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    audio(starts, total, f'{work}/a.wav')
    import imageio_ffmpeg
    out = f'/home/user/gold-studio-final/reels/{NAME}.mp4'
    subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{work}/f/%04d.jpg', '-i', f'{work}/a.wav',
                    '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-preset', 'slow',
                    '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], check=True)
    open(out.replace('.mp4', '.txt'), 'w').write(RF.CAPTION)
    return out, total

def audio(starts, total, path):
    n = int(SR * total)
    mus = musica(sum(BEATS), intro=INTRO)[:n]; mus = np.pad(mus, (0, max(0, n - len(mus))))
    fx = np.zeros(n + SR * 2)
    def add(sig, t, g=1.0):
        i = int(max(0, t) * SR); fx[i:i + len(sig)] += g * sig[:len(fx) - i]
    add(R.boom(0.9), 0.0); add(R.riser(BEAT * INTRO, 0.35), 0.0)
    for i, tr in enumerate(TRANS):
        if not tr: continue
        a = starts[i]
        if tr in ('whip', 'slide', 'diag'): add(R.whoosh(0.45, 300, 5000, 0.8), a - 0.12)
        if tr == 'zoom': add(R.whoosh(0.5, 150, 2500, 0.8), a - 0.2); add(R.boom(0.35), a)
        if tr == 'wipe': add(R.whoosh(0.5, 600, 6000, 0.6), a - 0.1)
        if tr == 'flash': add(R.riser(1.0, 0.5), a - 1.0); add(R.boom(0.8), a); add(R.chime(0.45), a + 0.1)
        if RF.SCENES[i].get('phone'): add(R.whoosh(0.6, 150, 1400, 0.4), a + 0.35)
    end = starts[-1]; add(R.tap(0.35), end + 1.6); add(R.chime(0.3), end + 1.45)
    fx = fx[:n]
    mix = mus * 0.62 + fx * 0.55
    fade = int(0.6 * SR); mix[-fade:] *= np.linspace(1, 0, fade)
    mix = np.tanh(mix * 1.4) / np.tanh(1.4); mix = mix / (np.abs(mix).max() + 1e-9) * 0.95
    pcm = (mix * 32767).astype('<i2')
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.column_stack([pcm, pcm]).ravel().tobytes())

if __name__ == '__main__':
    print(*build())
