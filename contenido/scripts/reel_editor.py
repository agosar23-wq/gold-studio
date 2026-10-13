"""Reel "¿Necesitás un editor?": antes (video crudo) y después (editado con subtítulos, zooms,
transiciones, etiquetas, línea de tiempo, música). Videos de Pexels (sesión de creadora 124332xx)."""
import sys, os, subprocess, wave, shutil; sys.path.insert(0, '/home/user/gold-studio-contenido')
import numpy as np
import reelgen as R
from reelgen import SCR, SP, LOGO, FPS
from marcas_ejemplo import FONTS as BFONTS
from musica import musica, BEAT, SR
import imageio_ffmpeg

NAME = 'reel-necesitas-un-editor'
VID = SCR + '/vid/full/'          # videos de Pexels (id.mp4, 1080x1920)
FF = imageio_ffmpeg.get_ffmpeg_exe()
DROP = 5.0                        # acá termina el "antes" y entra la música

# escena: clip, segundo de inicio, comienzo y fin en el reel, transición de entrada
SC = [
 dict(id='12433210', cin=1.0, a=0.0, b=2.0, tr=None, kind='hook'),
 dict(id='12433203', cin=2.0, a=2.0, b=5.0, tr='cut', kind='raw'),
 dict(id='12433200', cin=0.5, a=5.0, b=9.0, tr='flash', kind='talk', punch=[7.0],
      subs=[(5.15, 7.0, 'Grabá tu video *como te salga*'), (7.0, 8.95, 'yo me encargo *del resto.*')]),
 dict(id='12433196', cin=2.0, a=9.0, b=11.0, tr='whip', kind='talk', subs=[(9.1, 10.95, 'Cortes y *subtítulos*')], chips=['Cortes', 'Subtítulos']),
 dict(id='12433211', cin=3.0, a=11.0, b=13.0, tr='zoom', kind='edit', subs=[(11.1, 12.95, 'música y *transiciones*')], chips=['Música', 'Transiciones']),
 dict(id='12433260', cin=4.0, a=13.0, b=15.0, tr='slide', kind='export', subs=[(13.1, 14.95, 'listo para *subir.*')]),
 dict(id='12433207', cin=1.0, a=15.0, b=16.0, tr='zoom', kind='talk'),
 dict(id='12433207', cin=2.5, a=16.0, b=20.0, tr='flash', kind='end'),
]
TOTAL = 20.0

def descargar():
    """Baja de Pexels los videos que falten (todos son 1080x1920 a 30 fps)."""
    os.makedirs(VID, exist_ok=True)
    for s in SC:
        f = VID + s['id'] + '.mp4'
        if not os.path.exists(f):
            subprocess.run(['curl', '-sSf', '-o', f, f"https://videos.pexels.com/video-files/{s['id']}/{s['id']}-hd_1080_1920_30fps.mp4"], check=True)

def frames(work):
    for i, s in enumerate(SC):
        d = f'{work}/clips/s{i}'
        if os.path.isdir(d) and os.listdir(d): continue
        os.makedirs(d, exist_ok=True)
        dur = s['b'] - s['a'] + 0.6
        subprocess.run([FF, '-loglevel', 'error', '-y', '-ss', str(s['cin']), '-t', str(dur), '-i', VID + s['id'] + '.mp4',
                        '-vf', 'fps=30,scale=1080:1920', '-q:v', '3', f'{d}/%04d.jpg'], check=True)
        s['n'] = len(os.listdir(d))

def subs_html(i, s):
    out = []
    for j, (a, b, txt) in enumerate(s.get('subs', [])):
        ws, em = [], False
        for k, tok in enumerate(txt.split(' ')):
            if tok.startswith('*'): em = True
            ws.append(f'<span class="sw{" em" if em else ""}" id="s{i}t{j}w{k}">{tok.replace("*", "")}</span>')
            if tok.rstrip('.,?!').endswith('*'): em = False
        out.append(f'<div class="sub" id="s{i}t{j}" data-a="{a}" data-b="{b}" data-n="{len(ws)}">{" ".join(ws)}</div>')
    return ''.join(out)

def scene_html(i, s):
    k = s['kind']; extra = ''
    if k == 'hook':
        extra = (f'<div class="rec" id="s{i}rec"><i></i>REC</div>'
                 f'<div class="hook"><div class="eb" id="s{i}eb">Gold Studio</div><h1 id="s{i}h">¿Necesitás<br>un <em>editor?</em></h1></div>')
    if k == 'raw':
        extra = ('<div class="camui"><span class="tc" id="tc">00:00:02:00</span><span>4K · 30</span></div>'
                 f'<div class="tag gray" id="s{i}tag">ANTES · sin editar</div>'
                 f'<div class="rawtxt" id="s{i}rt">Así llega <em>tu video</em></div>')
    if k in ('talk', 'edit', 'export') and i == 2:
        extra += f'<div class="tag gold" id="s{i}tag">DESPUÉS · editado</div>'
    if s.get('chips'):
        extra += '<div class="chips">' + ''.join(f'<span id="s{i}c{j}">{c}</span>' for j, c in enumerate(s['chips'])) + '</div>'
    if k == 'edit':
        tracks = ''.join(f'<div class="trk"><i style="left:{l}%;width:{w}%;background:{c}" id="s{i}k{n}"></i></div>'
                         for n, (l, w, c) in enumerate([(4, 46, '#C9A34E'), (30, 52, '#E7D3A6'), (10, 70, '#8FB3A0'), (52, 40, '#B9897B')]))
        extra += f'<div class="tl" id="s{i}tl"><div class="tlh"><b>Gold Studio · edición</b><span>00:14</span></div>{tracks}<div class="playhead" id="s{i}ph"></div></div>'
    if k == 'export':
        extra += f'<div class="exp" id="s{i}exp"><div class="expt"><span>Exportando</span><b id="s{i}pc">0%</b></div><div class="bar"><i id="s{i}bar"></i></div></div>'
    if k == 'end':
        extra = (f'<div class="endc"><div class="spk" id="s{i}spk">{SP}</div><h1 id="s{i}h">¿Te edito<br><em>tus reels?</em></h1>'
                 f'<p id="s{i}p">Cortes, subtítulos, música y transiciones.</p><div class="pill" id="s{i}pill">Escribime y lo charlamos</div>'
                 f'<div class="lgw" id="s{i}lg">{LOGO}</div></div>')
    return (f'<div class="sc k-{k}" id="s{i}" data-a="{s["a"]}" data-b="{s["b"]}" data-tr="{s["tr"] or ""}" data-n="{s["n"]}" data-punch="{",".join(map(str, s.get("punch", [])))}">'
            f'<div class="cam" id="s{i}cam"><img id="s{i}img" src="clips/s{i}/0001.jpg"></div><div class="sh"></div>{extra}{subs_html(i, s)}</div>')

CSS = BFONTS + '''
html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#1C1A17;font-family:J}
.sc{position:absolute;inset:0;overflow:hidden;color:#FAF6EE;visibility:hidden}
.cam{position:absolute;inset:0} .cam img{width:100%;height:100%;object-fit:cover;display:block}
.k-raw .cam img{filter:saturate(.75) brightness(.97) contrast(.92)}
.k-talk .cam img,.k-edit .cam img,.k-export .cam img{filter:contrast(1.08) saturate(1.12) sepia(.06) brightness(1.03)}
.k-end .cam img{filter:blur(18px) brightness(.45) saturate(.9);transform:scale(1.1)}
.sh{position:absolute;inset:0}
.k-hook .sh{background:linear-gradient(rgba(28,26,23,.15),rgba(28,26,23,.75))}
.hook{position:absolute;left:90px;right:90px;bottom:330px;display:flex;flex-direction:column;gap:26px}
.eb{font-size:30px;letter-spacing:.4em;text-transform:uppercase;font-weight:500;color:#C9A34E}
h1{font-family:B;font-weight:500;font-size:140px;line-height:1.02;margin:0}
h1 em,.rawtxt em{font-style:italic;color:#C9A34E}
.rec{position:absolute;top:150px;right:110px;display:flex;align-items:center;gap:14px;font-size:34px;letter-spacing:.15em;font-weight:500}
.rec i{width:24px;height:24px;border-radius:50%;background:#E5483D;display:block}
.camui{position:absolute;top:150px;left:100px;right:100px;display:flex;justify-content:space-between;font-family:monospace;font-size:34px;color:#fff;text-shadow:0 2px 6px rgba(0,0,0,.4)}
.tag{position:absolute;top:240px;left:100px;padding:14px 26px;border-radius:999px;font-size:28px;letter-spacing:.2em;font-weight:500}
.tag.gray{background:rgba(255,255,255,.85);color:#555}
.tag.gold{background:#C9A34E;color:#1C1A17}
.rawtxt{position:absolute;left:100px;right:100px;bottom:300px;font-family:B;font-size:96px;line-height:1.05;color:#fff;text-shadow:0 4px 24px rgba(0,0,0,.35)}
.sub{position:absolute;left:70px;right:70px;top:1180px;text-align:center;font-size:76px;font-weight:500;line-height:1.25;opacity:0}
.sw{display:inline-block;padding:2px 14px;border-radius:14px;color:#fff;text-shadow:0 3px 0 rgba(0,0,0,.35),0 0 18px rgba(0,0,0,.35);margin:4px 0}
.sw.on{background:#C9A34E;color:#1C1A17;text-shadow:none}
.sw.em{font-family:B;font-style:italic;font-size:86px;color:#F3D58C}
.sub{font-size:72px}
.chips{position:absolute;top:240px;left:0;right:0;display:flex;gap:18px;justify-content:center}
.chips span{background:rgba(250,246,238,.94);color:#1C1A17;border-radius:999px;padding:16px 30px;font-size:34px;font-weight:500;opacity:0;box-shadow:0 14px 30px -14px rgba(0,0,0,.5)}
.tl{position:absolute;left:70px;right:70px;top:1460px;background:rgba(28,26,23,.88);border-radius:22px;padding:22px 26px;display:flex;flex-direction:column;gap:12px;opacity:0}
.tlh{display:flex;justify-content:space-between;font-size:24px;color:#BDB2A0} .tlh b{color:#FAF6EE;font-weight:500}
.trk{position:relative;height:34px;background:rgba(255,255,255,.06);border-radius:8px}
.trk i{position:absolute;top:4px;bottom:4px;border-radius:6px}
.playhead{position:absolute;top:60px;bottom:16px;width:4px;background:#E5483D;left:26px;border-radius:2px}
.exp{position:absolute;left:120px;right:120px;top:1470px;background:rgba(28,26,23,.88);border-radius:22px;padding:26px 30px;opacity:0}
.expt{display:flex;justify-content:space-between;font-size:32px;margin-bottom:16px} .expt b{color:#C9A34E}
.bar{height:16px;background:rgba(255,255,255,.12);border-radius:8px;overflow:hidden} .bar i{display:block;height:100%;width:0;background:#C9A34E}
.endc{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:34px;padding:0 90px}
.endc p{font-size:44px;color:#E9E0CF;margin:0}
.spk{width:120px;height:120px;color:#C9A34E} .sp{width:100%;height:100%;display:block}
.pill{background:#C9A34E;color:#1C1A17;font-size:42px;padding:28px 56px;border-radius:999px;font-weight:500}
.lgw{width:340px;margin-top:20px;color:#FAF6EE} .logo{width:100%;height:auto;display:block}
#pg{position:absolute;top:0;left:0;height:8px;background:#C9A34E;z-index:60}
#frame{position:absolute;inset:40px;border:2px solid rgba(201,163,78,.65);border-radius:8px;z-index:50}
#flash{position:absolute;inset:0;background:#FFF8EA;opacity:0;z-index:40}
#leak{position:absolute;width:1400px;height:1400px;border-radius:50%;background:radial-gradient(circle,rgba(233,190,110,.8),rgba(201,163,78,.3) 40%,rgba(201,163,78,0) 70%);mix-blend-mode:screen;opacity:0;z-index:41;left:-160px;top:260px}
#grain{position:absolute;inset:-100px;background:url(grain.png);opacity:.06;mix-blend-mode:overlay;z-index:45}
'''

JS = '''
const E=x=>x<0?0:x>1?1:1-Math.pow(1-x,3), EI=x=>x<0?0:x>1?1:x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const B=x=>{x=Math.max(0,Math.min(1,x));const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};
const $=id=>document.getElementById(id); const DROP=%DROP%, BEAT=%BEAT%, TOTAL=%TOTAL%, TR=0.45;
const SC=[...document.querySelectorAll('.sc')];
function up(el,p,d=60,bl=0){if(!el)return;const q=E(p);el.style.opacity=q;el.style.transform=`translateY(${(1-q)*d}px)`;el.style.filter=bl?`blur(${(1-q)*bl}px)`:'';}
function pop(el,p){if(!el)return;const q=B(p);el.style.opacity=E(p*2);el.style.transform=`scale(${0.6+0.4*q})`;}
window.render=async function(t){
  const flash=$('flash'), leak=$('leak'); flash.style.opacity=0; leak.style.opacity=0;
  $('pg').style.width = t>=DROP ? (100*(t-DROP)/(TOTAL-DROP))+'%' : '0';
  $('grain').style.transform=`translate(${(Math.floor(t*24)*37)%100-50}px,${(Math.floor(t*24)*61)%100-50}px)`;
  const bt=(t-DROP)/BEAT, pulse = t>=DROP && t<TOTAL-2 ? Math.exp(-(bt-Math.floor(bt))*BEAT/0.09) : 0;
  const loads=[];
  SC.forEach((s,i)=>{
    const a=+s.dataset.a, b=+s.dataset.b, k=t-a, tr=s.dataset.tr, n=+s.dataset.n;
    const nx=SC[i+1], kn=nx? t-(+nx.dataset.a) : -1, trn=nx?nx.dataset.tr:'';
    const vis = k>=0 && (kn<TR || !nx || trn==='cut' && kn<0);
    const show = k>=0 && (!nx || kn< (trn==='cut'||trn==='flash' ? 0.04 : TR));
    s.style.visibility = show?'visible':'hidden'; if(!show) return;
    s.style.zIndex=i;
    const img=$(`s${i}img`); const f=Math.min(n,Math.max(1,Math.floor(k*30)+1)); const src=`clips/s${i}/${String(f).padStart(4,'0')}.jpg`;
    if(!img.src.endsWith(src)){ img.src=src; loads.push(img.decode().catch(()=>0)); }
    let tf='', fl='', cp='none';
    if(k<TR && tr){ const p=k/TR;
      if(tr==='zoom'){ tf=`scale(${1.45-0.45*E(p)})`; fl=`blur(${(1-E(p))*20}px)`; }
      if(tr==='whip'){ tf=`translateX(${(1-EI(p))*1200}px)`; fl=`blur(${Math.sin(Math.PI*p)*26}px)`; }
      if(tr==='slide'){ tf=`translateY(${(1-EI(p))*1920}px)`; }
      if(tr==='flash'){ flash.style.opacity=Math.max(+flash.style.opacity,1-E(p*1.3)); }
      if(tr!=='flash'&&tr!=='cut'){ leak.style.opacity=Math.max(+leak.style.opacity,Math.sin(Math.PI*p)*0.7); leak.style.transform=`translateX(${(p-0.5)*900}px)`; }
    }
    if(nx && kn>=0){ const p=kn/TR;
      if(trn==='whip'){ tf=`translateX(${-EI(p)*1200}px)`; fl=`blur(${Math.sin(Math.PI*p)*26}px)`; }
      if(trn==='slide'){ tf=`translateY(${-EI(p)*500}px) scale(${1-0.08*EI(p)})`; fl=`brightness(${1-0.5*p})`; }
      if(trn==='zoom'){ tf=`scale(${1+0.25*EI(p)})`; }
    }
    s.style.transform=tf; s.style.filter=fl; s.style.clipPath=cp;
    // cámara: zoom de corte (jump cut) en los "punch" + pulso con el bombo
    let z=1.0; const kind=s.className;
    if(kind.includes('k-talk')||kind.includes('k-edit')||kind.includes('k-export')){ z=1.04+0.03*Math.min(1,k/(b-a)); (s.dataset.punch||'').split(',').filter(Boolean).forEach(pt=>{ if(t>=+pt) z+=0.16; }); z+=0.015*pulse; }
    if(kind.includes('k-hook')) z=1.0+0.06*E(k/2);
    $(`s${i}cam`).style.transform=`scale(${z})`;
    // subtítulos palabra por palabra
    s.querySelectorAll('.sub').forEach(sb=>{ const sa=+sb.dataset.a, sbb=+sb.dataset.b, nw=+sb.dataset.n;
      const on=t>=sa&&t<sbb; sb.style.opacity=on?1:0; if(!on) return; const per=(sbb-sa-0.25)/nw;
      for(let w=0;w<nw;w++){ const el=$(sb.id+'w'+w), kw=t-sa-w*per; el.style.opacity=kw>=0?1:0; el.style.transform=`scale(${kw>=0?0.85+0.15*B(kw/0.18):0.85})`;
        el.classList.toggle('on', kw>=0 && kw<per+0.02 && !el.classList.contains('em')); } });
    // extras
    if(kind.includes('k-hook')){ up($(`s${i}eb`),(k-0.1)/0.4,30); up($(`s${i}h`),(k-0.2)/0.5,80,14); $(`s${i}rec`).querySelector('i').style.opacity=(Math.floor(t*2)%2)?0.25:1; }
    if(kind.includes('k-raw')){ $('tc').textContent='00:00:0'+(2+Math.floor(k))+':'+String(Math.floor((k%1)*30)).padStart(2,'0'); pop($(`s${i}tag`),(k-0.1)/0.4); up($(`s${i}rt`),(k-0.3)/0.5,50); }
    pop($(`s${i}tag`),(k-0.3)/0.4);
    for(let c=0;c<2;c++) pop($(`s${i}c${c}`),(k-0.35-c*0.35)/0.4);
    const tl=$(`s${i}tl`); if(tl){ up(tl,(k-0.2)/0.5,80); $(`s${i}ph`).style.left=(26+E(k/1.9)*900)+'px'; for(let q=0;q<4;q++){const el=$(`s${i}k${q}`); el.style.transform=`scaleX(${E((k-0.3-q*0.12)/0.4)})`; el.style.transformOrigin='left';} }
    const ex=$(`s${i}exp`); if(ex){ up(ex,(k-0.2)/0.5,80); const p=Math.min(1,Math.max(0,(k-0.4)/1.1)); $(`s${i}bar`).style.width=(p*100)+'%'; $(`s${i}pc`).textContent=p>=1?'¡Listo!':Math.round(p*100)+'%'; }
    if(kind.includes('k-end')){ const p=B((k-0.15)/0.55); $(`s${i}spk`).style.transform=`scale(${p*(1+0.08*pulse)}) rotate(${(1-p)*-120+k*20}deg)`;
      up($(`s${i}h`),(k-0.3)/0.5,70,12); up($(`s${i}p`),(k-0.7)/0.5,40); up($(`s${i}pill`),(k-1.0)/0.5,40); up($(`s${i}lg`),(k-1.4)/0.6,30,10); }
  });
  await Promise.all(loads);
};
'''

def build():
    work = f'{SCR}/re-{NAME}'; os.makedirs(work + '/f', exist_ok=True)
    for f in os.listdir(work + '/f'): os.remove(os.path.join(work, 'f', f))
    descargar(); frames(work)
    for i, s in enumerate(SC): s['n'] = len(os.listdir(f'{work}/clips/s{i}'))
    g = f'{SCR}/rfe-reel-todo-lo-que-tu-marca-necesita/grain.png'
    if os.path.exists(g): shutil.copy(g, f'{work}/grain.png')
    js = JS.replace('%DROP%', str(DROP)).replace('%BEAT%', str(BEAT)).replace('%TOTAL%', str(TOTAL))
    page = (f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>' + ''.join(scene_html(i, s) for i, s in enumerate(SC)) +
            '<div id="flash"></div><div id="leak"></div><div id="grain"></div><div id="frame"></div><div id="pg"></div>'
            f'<script>{js}</script>')
    open(f'{work}/r.html', 'w').write(page)
    subprocess.run(['node', f'{SCR}/reel2.js', f'{work}/r.html', str(TOTAL), f'{work}/f'], check=True,
                   env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    audio(f'{work}/a.wav')
    out = f'/home/user/gold-studio-final/reels/{NAME}.mp4'
    subprocess.run([FF, '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{work}/f/%04d.jpg', '-i', f'{work}/a.wav',
                    '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '21', '-preset', 'slow',
                    '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], check=True)
    open(out.replace('.mp4', '.txt'), 'w').write(CAPTION)
    return out

def audio(path):
    n = int(SR * TOTAL)
    beats = int(round((TOTAL - DROP) / BEAT))
    mus = musica(beats, intro=0, outro=4)
    mix = np.zeros(n + SR * 3)
    i0 = int(DROP * SR); mix[i0:i0 + len(mus)] += mus[:len(mix) - i0] * 0.6
    def add(sig, t, g=1.0):
        i = int(max(0, t) * SR); mix[i:i + len(sig)] += g * sig[:len(mix) - i]
    # antes: un "bip" de cámara y ruido de ambiente muy bajito
    room = np.random.default_rng(2).standard_normal(int(SR * DROP)) * 0.012
    mix[:len(room)] += room
    t = R._t(0.12); add(0.25 * np.sin(2 * np.pi * 1760 * t) * np.exp(-t / 0.05), 0.05)
    add(R.boom(0.5), 0.0); add(R.pop(0.3, 900), 0.4)
    add(R.whoosh(0.3, 800, 5000, 0.4), 2.0)
    add(R.riser(1.4, 0.55), DROP - 1.4); add(R.boom(0.9), DROP); add(R.chime(0.4), DROP + 0.05)
    for s in SC:
        if s['tr'] in ('whip', 'slide'): add(R.whoosh(0.45, 300, 5000, 0.7), s['a'] - 0.12)
        if s['tr'] == 'zoom': add(R.whoosh(0.5, 150, 2500, 0.7), s['a'] - 0.2); add(R.boom(0.3), s['a'])
        for a, b, txt in s.get('subs', []): add(R.pop(0.18, 1300), a)
        for j, _ in enumerate(s.get('chips', [])): add(R.pop(0.32, 900 + 200 * j), s['a'] + 0.35 + j * 0.35)
        if s.get('punch'):
            for p in s['punch']: add(R.whoosh(0.15, 1500, 7000, 0.35), p - 0.05)
        if s['kind'] == 'edit':
            for q in range(6): add(R.tick(0.12), s['a'] + 0.3 + q * 0.12)
        if s['kind'] == 'export': add(R.chime(0.4), s['a'] + 1.5)
        if s['kind'] == 'end': add(R.tap(0.4), s['a'] + 1.0); add(R.chime(0.3), s['a'] + 1.4)
    mix = mix[:n]; fade = int(0.5 * SR); mix[-fade:] *= np.linspace(1, 0, fade)
    mix = np.tanh(mix * 1.4) / np.tanh(1.4); mix = mix / (np.abs(mix).max() + 1e-9) * 0.95
    pcm = (mix * 32767).astype('<i2')
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.column_stack([pcm, pcm]).ravel().tobytes())

CAPTION = '''¿Grabás tus videos pero no tenés tiempo (ni ganas) de editarlos?

Mandámelos así como salen y te los devuelvo listos para subir: con cortes, subtítulos, música y transiciones.

Vos te encargás de tu negocio, yo de que tus reels se vean profesionales.

¿Te los edito? Escribime y lo charlamos.

#reels #emprendedoras #edicióndevideo'''

if __name__ == '__main__':
    print(build())
