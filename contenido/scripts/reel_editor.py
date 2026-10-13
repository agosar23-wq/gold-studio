"""Reel "¿Necesitás un editor?" (versión con más edición): antes crudo / después editado con
jump cuts, cámara lenta que acelera, antes-después en pantalla dividida, imagen congelada con palabra gigante,
falla digital, pantalla en tres, montaje rápido, subtítulos palabra por palabra, música y efectos.
Videos de Pexels (sesión de creadora 124332xx, 1080x1920 a 30 fps)."""
import sys, os, subprocess, wave, shutil, json; sys.path.insert(0, '/home/user/gold-studio-contenido')
import numpy as np
import reelgen as R
from reelgen import SCR, SP, LOGO, FPS
from marcas_ejemplo import FONTS as BFONTS
from musica import musica, BEAT, SR
import imageio_ffmpeg

NAME = 'reel-necesitas-un-editor'
VID = SCR + '/vid/full/'
FF = imageio_ffmpeg.get_ffmpeg_exe()
DROP = 5.0
TOTAL = 22.0

# capa: (id del video, segundo de inicio)
SC = [
 dict(a=0.0, b=2.0, tr=None, kind='hook', L=[('12433210', 1.0)]),
 dict(a=2.0, b=5.0, tr='cut', kind='raw', L=[('12433203', 2.0)]),
 dict(a=5.0, b=8.0, tr='flash', kind='talk', L=[('12433200', 0.5)], tag='DESPUÉS · editado',
      jumps=[(6.0, 0.3, 1.18), (7.0, 0.3, 1.0), (7.5, 0.2, 1.26)],
      subs=[(5.15, 6.5, 'Grabá tu video *como te salga*'), (6.5, 7.98, 'yo me encargo *del resto.*')]),
 dict(a=8.0, b=9.5, tr='glitch', kind='split', L=[('12433200', 3.6)]),
 dict(a=9.5, b=10.5, tr='cut', kind='word', L=[('12433196', 2.0)], word='Cortes.'),
 dict(a=10.5, b=12.0, tr='zoom', kind='talk', L=[('12433196', 2.0)], ramp=[(0.6, 0.35), (9, 1.9)],
      subs=[(10.6, 11.95, 'y *subtítulos*')], chips=['Cortes', 'Subtítulos']),
 dict(a=12.0, b=14.0, tr='whip', kind='edit', L=[('12433211', 3.0)], subs=[(12.1, 13.95, 'música y *transiciones*')], chips=['Música', 'Transiciones']),
 dict(a=14.0, b=15.5, tr='glitch', kind='tri', L=[('12433204', 1.0), ('12433207', 4.0), ('12433260', 1.0)]),
 dict(a=15.5, b=17.0, tr='slide', kind='export', L=[('12433260', 4.0)], subs=[(15.6, 16.95, 'listo para *subir.*')]),
 dict(a=17.0, b=18.0, tr='cut', kind='montage', L=[('12433196', 4.0), ('12433200', 2.0), ('12433207', 6.0), ('12433210', 3.0)]),
 dict(a=18.0, b=22.0, tr='flash', kind='end', L=[('12433207', 2.5)]),
]

def key(l): return f'{l[0]}_{l[1]:.1f}'

def descargar():
    os.makedirs(VID, exist_ok=True)
    for s in SC:
        for vid, _ in s['L']:
            f = VID + vid + '.mp4'
            if not os.path.exists(f):
                subprocess.run(['curl', '-sSf', '-o', f, f'https://videos.pexels.com/video-files/{vid}/{vid}-hd_1080_1920_30fps.mp4'], check=True)

def frames(work):
    """Extrae a JPG cada tramo de video usado. Devuelve {clave: cantidad de cuadros}."""
    need = {}
    for s in SC:
        for l in s['L']: need[key(l)] = max(need.get(key(l), 0), s['b'] - s['a'] + 1.6)
    counts = {}
    for k, dur in need.items():
        vid, cin = k.split('_'); d = f'{work}/clips/{k}'
        if not (os.path.isdir(d) and os.listdir(d)):
            os.makedirs(d, exist_ok=True)
            subprocess.run([FF, '-loglevel', 'error', '-y', '-ss', cin, '-t', str(dur), '-i', VID + vid + '.mp4',
                            '-vf', 'fps=30,scale=1080:1920', '-q:v', '3', f'{d}/%04d.jpg'], check=True)
        counts[k] = len(os.listdir(d))
    return counts

def words_html(i, s):
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
    k = s['kind']
    imgs = ''.join(f'<div class="cam l{j}" id="s{i}c{j}"><img id="s{i}L{j}"></div>' for j in range(len(s['L'])))
    if k == 'split':
        imgs = (f'<div class="cam" id="s{i}c0"><img id="s{i}L0" class="graded"></div>'
                f'<div class="cam raw" id="s{i}c1"><img id="s{i}L1"></div><div class="divider" id="s{i}dv"></div>'
                '<div class="sl a">ANTES</div><div class="sl b">DESPUÉS</div>')
    if k == 'tri':
        imgs = ''.join(f'<div class="panel" id="s{i}p{j}" style="top:{j * 640}px"><img id="s{i}L{j}" style="object-position:50% {p}"></div>' for j, p in enumerate(['6%', '30%', '22%'])) + \
               f'<div class="band" id="s{i}band"><span>a tu <em>ritmo</em></span></div>'
    extra = ''
    if k == 'hook':
        extra = (f'<div class="rec"><i id="recdot"></i>REC</div>'
                 f'<div class="hook"><div class="eb" id="s{i}eb">Gold Studio</div><h1 id="s{i}h">¿Necesitás<br>un <em>editor?</em></h1></div>')
    if k == 'raw':
        extra = ('<div class="camui"><span id="tc">00:00:02:00</span><span>4K · 30</span></div>'
                 f'<div class="tag gray" id="s{i}tag">ANTES · sin editar</div><div class="rawtxt" id="s{i}rt">Así llega <em>tu video</em></div>')
    if s.get('tag'): extra += f'<div class="tag gold" id="s{i}tag">{s["tag"]}</div>'
    if k == 'word': extra += f'<div class="bigw" id="s{i}w">{s["word"]}</div>'
    if s.get('chips'): extra += '<div class="chips">' + ''.join(f'<span id="s{i}ch{j}">{c}</span>' for j, c in enumerate(s['chips'])) + '</div>'
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
    return f'<div class="sc k-{k}" id="s{i}">{imgs}<div class="sh"></div>{extra}{words_html(i, s)}</div>'

CSS = BFONTS + '''
html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#1C1A17;font-family:J}
.sc{position:absolute;inset:0;overflow:hidden;color:#FAF6EE;visibility:hidden}
.cam{position:absolute;inset:0} .cam img,.panel img{width:100%;height:100%;object-fit:cover;display:block}
.graded,.k-talk img,.k-edit img,.k-export img,.k-montage img,.k-tri img{filter:contrast(1.08) saturate(1.14) sepia(.06) brightness(1.03)}
.k-raw img,.cam.raw img{filter:saturate(.7) brightness(.96) contrast(.9)}
.k-word img{filter:grayscale(1) contrast(1.25) brightness(.8)}
.k-end img{filter:blur(18px) brightness(.45);transform:scale(1.1)}
.cam.raw{clip-path:inset(0 50% 0 0)}
.divider{position:absolute;top:0;bottom:0;width:6px;background:#FAF6EE;left:50%;margin-left:-3px;box-shadow:0 0 20px rgba(0,0,0,.4)}
.sl{position:absolute;top:240px;padding:12px 24px;border-radius:999px;font-size:28px;letter-spacing:.2em;font-weight:500}
.sl.a{left:90px;background:rgba(255,255,255,.85);color:#555} .sl.b{right:90px;background:#C9A34E;color:#1C1A17}
.panel{position:absolute;left:0;right:0;height:632px;overflow:hidden;border-bottom:8px solid #1C1A17}
.band{position:absolute;left:0;right:0;top:860px;height:200px;display:flex;align-items:center;justify-content:center;font-family:B;font-size:110px;background:rgba(28,26,23,.82);color:#FAF6EE;opacity:0}
.band em,h1 em,.rawtxt em{font-style:italic;color:#C9A34E}
.sh{position:absolute;inset:0;pointer-events:none}
.k-hook .sh{background:linear-gradient(rgba(28,26,23,.15),rgba(28,26,23,.75))}
.hook{position:absolute;left:90px;right:90px;bottom:330px;display:flex;flex-direction:column;gap:26px}
.eb{font-size:30px;letter-spacing:.4em;text-transform:uppercase;font-weight:500;color:#C9A34E}
h1{font-family:B;font-weight:500;font-size:140px;line-height:1.02;margin:0}
.rec{position:absolute;top:150px;right:110px;display:flex;align-items:center;gap:14px;font-size:34px;letter-spacing:.15em;font-weight:500}
.rec i{width:24px;height:24px;border-radius:50%;background:#E5483D;display:block}
.camui{position:absolute;top:150px;left:100px;right:100px;display:flex;justify-content:space-between;font-family:monospace;font-size:34px;color:#fff;text-shadow:0 2px 6px rgba(0,0,0,.4)}
.tag{position:absolute;top:240px;left:100px;padding:14px 26px;border-radius:999px;font-size:28px;letter-spacing:.2em;font-weight:500}
.tag.gray{background:rgba(255,255,255,.85);color:#555} .tag.gold{background:#C9A34E;color:#1C1A17}
.rawtxt{position:absolute;left:100px;right:100px;bottom:300px;font-family:B;font-size:96px;line-height:1.05;color:#fff;text-shadow:0 4px 24px rgba(0,0,0,.35)}
.bigw{position:absolute;left:0;right:0;top:720px;text-align:center;font-family:B;font-style:italic;font-size:260px;color:#C9A34E;text-shadow:0 10px 40px rgba(0,0,0,.5)}
.sub{position:absolute;left:70px;right:70px;top:1180px;text-align:center;font-size:72px;font-weight:500;line-height:1.25;opacity:0}
.sw{display:inline-block;padding:2px 14px;border-radius:14px;color:#fff;text-shadow:0 3px 0 rgba(0,0,0,.35),0 0 18px rgba(0,0,0,.35);margin:4px 0}
.sw.on{background:#C9A34E;color:#1C1A17;text-shadow:none}
.sw.em{font-family:B;font-style:italic;font-size:86px;color:#F3D58C}
.chips{position:absolute;top:240px;left:0;right:0;display:flex;gap:18px;justify-content:center}
.chips span{background:rgba(250,246,238,.94);color:#1C1A17;border-radius:999px;padding:16px 30px;font-size:34px;font-weight:500;opacity:0;box-shadow:0 14px 30px -14px rgba(0,0,0,.5)}
.tl{position:absolute;left:70px;right:70px;top:1460px;background:rgba(28,26,23,.88);border-radius:22px;padding:22px 26px;display:flex;flex-direction:column;gap:12px;opacity:0}
.tlh{display:flex;justify-content:space-between;font-size:24px;color:#BDB2A0} .tlh b{color:#FAF6EE;font-weight:500}
.trk{position:relative;height:34px;background:rgba(255,255,255,.06);border-radius:8px} .trk i{position:absolute;top:4px;bottom:4px;border-radius:6px}
.playhead{position:absolute;top:60px;bottom:16px;width:4px;background:#E5483D;left:26px;border-radius:2px}
.exp{position:absolute;left:120px;right:120px;top:1470px;background:rgba(28,26,23,.88);border-radius:22px;padding:26px 30px;opacity:0}
.expt{display:flex;justify-content:space-between;font-size:32px;margin-bottom:16px} .expt b{color:#C9A34E}
.bar{height:16px;background:rgba(255,255,255,.12);border-radius:8px;overflow:hidden} .bar i{display:block;height:100%;width:0;background:#C9A34E}
.endc{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:34px;padding:0 90px}
.endc p{font-size:44px;color:#E9E0CF;margin:0}
.spk{width:120px;height:120px;color:#C9A34E} .sp{width:100%;height:100%;display:block}
.pill{background:#C9A34E;color:#1C1A17;font-size:42px;padding:28px 56px;border-radius:999px;font-weight:500}
.lgw{width:340px;margin-top:20px;color:#FAF6EE} .logo{width:100%;height:auto;display:block}
#stage{position:absolute;inset:0}
#pg{position:absolute;top:0;left:0;height:8px;background:#C9A34E;z-index:60}
#frame{position:absolute;inset:40px;border:2px solid rgba(201,163,78,.65);border-radius:8px;z-index:50}
#flash{position:absolute;inset:0;background:#FFF8EA;opacity:0;z-index:40}
#leak{position:absolute;width:1400px;height:1400px;border-radius:50%;background:radial-gradient(circle,rgba(233,190,110,.8),rgba(201,163,78,.3) 40%,rgba(201,163,78,0) 70%);mix-blend-mode:screen;opacity:0;z-index:41;left:-160px;top:260px}
#grain{position:absolute;inset:-100px;background:url(grain.png);opacity:.06;mix-blend-mode:overlay;z-index:45}
#gl{position:absolute;inset:0;z-index:42;pointer-events:none}
#gl i{position:absolute;left:0;right:0;display:block;mix-blend-mode:screen}
#lb1,#lb2{position:absolute;left:0;right:0;height:0;background:#000;z-index:43}
#lb1{top:0} #lb2{bottom:0}
'''

JS = r'''
const D=%DATA%; const DROP=%DROP%, BEAT=%BEAT%, TOTAL=%TOTAL%, TR=0.45;
const E=x=>x<0?0:x>1?1:1-Math.pow(1-x,3), EI=x=>x<0?0:x>1?1:x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const B=x=>{x=Math.max(0,Math.min(1,x));const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};
const $=id=>document.getElementById(id);
const rnd=n=>{const x=Math.sin(n*127.1+311.7)*43758.5453;return x-Math.floor(x);};
function up(el,p,d=60,bl=0){if(!el)return;const q=E(p);el.style.opacity=q;el.style.transform=`translateY(${(1-q)*d}px)`;el.style.filter=bl?`blur(${(1-q)*bl}px)`:'';}
function pop(el,p){if(!el)return;const q=B(p);el.style.opacity=E(p*2);el.style.transform=`scale(${0.6+0.4*q})`;}
const GL=$('gl'); for(let g=0;g<10;g++){const i=document.createElement('i');GL.appendChild(i);}
function cliptime(s,k){ let ct=k;
  if(s.ramp){ ct=0; let prev=0; for(const [kend,rate] of s.ramp){ const seg=Math.min(k,kend)-prev; if(seg<=0) break; ct+=seg*rate; prev=kend; } }
  if(s.jumps) for(const [ta,skip] of s.jumps) if(s.a+k>=ta) ct+=skip;
  if(s.kind==='word') ct=0.35;
  return ct; }
function setimg(img,key,ct,loads){ const n=D.counts[key]; const f=Math.min(n,Math.max(1,Math.floor(ct*30)+1)); const src=`clips/${key}/${String(f).padStart(4,'0')}.jpg`;
  if(!img.getAttribute('src')||!img.getAttribute('src').endsWith(src)){ img.setAttribute('src',src); loads.push(img.decode().catch(()=>0)); } }
window.render=async function(t){
  const flash=$('flash'), leak=$('leak'); flash.style.opacity=0; leak.style.opacity=0;
  let glitch=0, shake=0;
  $('pg').style.width = t>=DROP ? (100*(t-DROP)/(TOTAL-DROP))+'%' : '0';
  $('grain').style.transform=`translate(${(Math.floor(t*24)*37)%100-50}px,${(Math.floor(t*24)*61)%100-50}px)`;
  const bt=(t-DROP)/BEAT, pulse = t>=DROP && t<TOTAL-2 ? Math.exp(-(bt-Math.floor(bt))*BEAT/0.09) : 0;
  const loads=[]; const SC=D.sc;
  SC.forEach((s,i)=>{
    const el=$('s'+i), k=t-s.a, nx=SC[i+1], kn=nx? t-nx.a : -1;
    const hard = nx && (nx.tr==='cut'||nx.tr==='flash'||nx.tr==='glitch');
    const show = k>=0 && (!nx || kn < (hard?0:TR));
    el.style.visibility = show?'visible':'hidden'; if(!show) return;
    el.style.zIndex=i;
    // imágenes
    if(s.kind==='montage'){ const idx=Math.min(3,Math.floor(k/0.25)); s.L.forEach((l,j)=>{ const c=$(`s${i}c${j}`); c.style.visibility=j===idx?'visible':'hidden'; if(j===idx) setimg($(`s${i}L${j}`),l,(k-idx*0.25)+0.1,loads); });
      const kk=k-idx*0.25; if(kk<0.06) flash.style.opacity=Math.max(+flash.style.opacity,0.55); shake=Math.max(shake,1-kk/0.2); }
    else if(s.kind==='split'){ setimg($(`s${i}L0`),s.L[0],k,loads); setimg($(`s${i}L1`),s.L[0],k,loads);
      const x=50+38*Math.sin((k-0.2)/1.2*Math.PI*1.0)*(k>0.2?1:0); $(`s${i}c1`).style.clipPath=`inset(0 ${100-x}% 0 0)`; $(`s${i}dv`).style.left=x+'%'; }
    else s.L.forEach((l,j)=>setimg($(`s${i}L${j}`),l,cliptime(s,k),loads));
    // transición de entrada / salida
    let tf='', fl='';
    if(k<TR && s.tr){ const p=k/TR;
      if(s.tr==='zoom'){ tf=`scale(${1.45-0.45*E(p)})`; fl=`blur(${(1-E(p))*20}px)`; }
      if(s.tr==='whip'){ tf=`translateX(${(1-EI(p))*1200}px)`; fl=`blur(${Math.sin(Math.PI*p)*26}px)`; }
      if(s.tr==='slide'){ tf=`translateY(${(1-EI(p))*1920}px)`; }
      if(s.tr==='flash'){ flash.style.opacity=Math.max(+flash.style.opacity,1-E(p*1.3)); }
      if(s.tr==='glitch' && k<0.32){ glitch=1-k/0.32; }
      if(s.tr==='cut' && s.kind==='word'){ shake=Math.max(shake,1-k/0.35); }
      if(['zoom','whip','slide'].includes(s.tr)){ leak.style.opacity=Math.max(+leak.style.opacity,Math.sin(Math.PI*p)*0.7); leak.style.transform=`translateX(${(p-0.5)*900}px)`; }
    }
    if(nx && kn>=0){ const p=kn/TR;
      if(nx.tr==='whip'){ tf=`translateX(${-EI(p)*1200}px)`; fl=`blur(${Math.sin(Math.PI*p)*26}px)`; }
      if(nx.tr==='slide'){ tf=`translateY(${-EI(p)*500}px) scale(${1-0.08*EI(p)})`; fl=`brightness(${1-0.5*p})`; }
      if(nx.tr==='zoom'){ tf=`scale(${1+0.25*EI(p)})`; }
    }
    if(nx && nx.tr==='glitch' && kn>-0.12 && kn<0){ glitch=Math.max(glitch,(kn+0.12)/0.12); }
    el.style.transform=tf; el.style.filter=fl;
    // cámara: jump cuts con zoom, pulso, cámara lenta
    let z=1.03+0.03*Math.min(1,k/(s.b-s.a));
    if(s.jumps){ let zz=1; for(const [ta,,zm] of s.jumps) if(t>=ta) zz=zm; z*=zz; }
    if(['talk','edit','export','montage','tri'].includes(s.kind)) z+=0.016*pulse;
    if(s.kind==='hook') z=1+0.06*E(k/2);
    if(s.kind==='word') z=1.12+0.08*E(k/1);
    if(s.ramp && k<0.6) z+=0.08*(k/0.6);
    for(let j=0;j<s.L.length;j++){ const c=$(`s${i}c${j}`); if(c) c.style.transform=`scale(${z})`; }
    // pantalla en tres
    if(s.kind==='tri'){ for(let j=0;j<3;j++){ const p=E((k-j*0.12)/0.45); $(`s${i}p${j}`).style.transform=`translateX(${(1-p)*(j%2?1:-1)*1100}px)`; } pop($(`s${i}band`),(k-0.5)/0.4); }
    // subtítulos
    el.querySelectorAll('.sub').forEach(sb=>{ const sa=+sb.dataset.a, sbb=+sb.dataset.b, nw=+sb.dataset.n;
      const on=t>=sa&&t<sbb; sb.style.opacity=on?1:0; if(!on) return; const per=(sbb-sa-0.25)/nw;
      for(let w=0;w<nw;w++){ const e=$(sb.id+'w'+w), kw=t-sa-w*per; e.style.opacity=kw>=0?1:0; e.style.transform=`scale(${kw>=0?0.8+0.2*B(kw/0.16):0.8}) rotate(${kw>=0&&kw<0.12?(rnd(w+i)-.5)*6:0}deg)`;
        e.classList.toggle('on', kw>=0 && kw<per+0.02 && !e.classList.contains('em')); } });
    // extras
    if(s.kind==='hook'){ up($(`s${i}eb`),(k-0.1)/0.4,30); const h=$(`s${i}h`); up(h,(k-0.2)/0.5,80,14);
      if(k>0.25&&k<0.55){ const g=Math.floor(k*30); h.style.transform+=` translateX(${(rnd(g)-.5)*30}px)`; h.style.textShadow=`${(rnd(g+1)-.5)*16}px 0 #E5483D, ${(rnd(g+2)-.5)*16}px 0 #3BB0E8`; } else h.style.textShadow='none';
      $('recdot').style.opacity=(Math.floor(t*2)%2)?0.25:1; }
    if(s.kind==='raw'){ $('tc').textContent='00:00:0'+(2+Math.floor(k))+':'+String(Math.floor((k%1)*30)).padStart(2,'0'); up($(`s${i}rt`),(k-0.3)/0.5,50); }
    pop($(`s${i}tag`),(k-0.15)/0.4);
    if(s.kind==='word'){ const w=$(`s${i}w`); const p=B(k/0.3); w.style.transform=`scale(${1.6-0.6*p})`; w.style.opacity=E(k/0.12); }
    for(let c=0;c<2;c++) pop($(`s${i}ch${c}`),(k-0.3-c*0.3)/0.4);
    const tl=$(`s${i}tl`); if(tl){ up(tl,(k-0.2)/0.5,80); $(`s${i}ph`).style.left=(26+E(k/1.9)*900)+'px'; for(let q=0;q<4;q++){const e=$(`s${i}k${q}`); e.style.transform=`scaleX(${E((k-0.3-q*0.12)/0.4)})`; e.style.transformOrigin='left';} }
    const ex=$(`s${i}exp`); if(ex){ up(ex,(k-0.2)/0.5,80); const p=Math.min(1,Math.max(0,(k-0.35)/0.9)); $(`s${i}bar`).style.width=(p*100)+'%'; $(`s${i}pc`).textContent=p>=1?'¡Listo!':Math.round(p*100)+'%'; }
    if(s.kind==='end'){ const p=B((k-0.15)/0.55); $(`s${i}spk`).style.transform=`scale(${p*(1+0.08*pulse)}) rotate(${(1-p)*-120+k*20}deg)`;
      up($(`s${i}h`),(k-0.3)/0.5,70,12); up($(`s${i}p`),(k-0.7)/0.5,40); up($(`s${i}pill`),(k-1.0)/0.5,40); up($(`s${i}lg`),(k-1.4)/0.6,30,10); }
  });
  // falla digital, sacudida y franjas de cine
  const st=$('stage'), g=Math.floor(t*30);
  if(glitch>0){ st.style.filter=`contrast(1.35) saturate(1.7) hue-rotate(${(rnd(g)-.5)*60}deg)`; st.style.transform=`translateX(${(rnd(g+3)-.5)*90*glitch}px)`;
    [...GL.children].forEach((e,q)=>{ e.style.top=(rnd(g*7+q)*1900)+'px'; e.style.height=(8+rnd(g*3+q)*70)+'px'; e.style.background=q%2?'rgba(59,176,232,.55)':'rgba(229,72,61,.5)'; e.style.transform=`translateX(${(rnd(g+q)-.5)*300}px)`; e.style.opacity=glitch; }); }
  else { st.style.filter=''; st.style.transform=shake>0?`translate(${(rnd(g)-.5)*40*shake}px,${(rnd(g+9)-.5)*40*shake}px) rotate(${(rnd(g+5)-.5)*2*shake}deg)`:''; [...GL.children].forEach(e=>e.style.opacity=0); }
  const lb = t>=9.5&&t<10.5 ? 120*E((t-9.5)/0.2) : 0; $('lb1').style.height=$('lb2').style.height=lb+'px';
  await Promise.all(loads);
};
'''

def build():
    work = f'{SCR}/re-{NAME}'; os.makedirs(work + '/f', exist_ok=True)
    for f in os.listdir(work + '/f'): os.remove(os.path.join(work, 'f', f))
    descargar(); counts = frames(work)
    g = f'{SCR}/rfe-reel-todo-lo-que-tu-marca-necesita/grain.png'
    if not os.path.exists(f'{work}/grain.png'):
        if os.path.exists(g): shutil.copy(g, f'{work}/grain.png')
        else:
            from PIL import Image
            Image.fromarray((np.random.default_rng(1).standard_normal((540, 540)) * 40 + 128).clip(0, 255).astype('uint8'), 'L').save(f'{work}/grain.png')
    data = dict(counts=counts, sc=[dict(a=s['a'], b=s['b'], tr=s['tr'], kind=s['kind'], L=[key(l) for l in s['L']],
                                        jumps=s.get('jumps'), ramp=s.get('ramp')) for s in SC])
    js = JS.replace('%DATA%', json.dumps(data)).replace('%DROP%', str(DROP)).replace('%BEAT%', str(BEAT)).replace('%TOTAL%', str(TOTAL))
    page = (f'<!doctype html><meta charset="utf-8"><style>{CSS}</style><div id="stage">' + ''.join(scene_html(i, s) for i, s in enumerate(SC)) +
            '<div id="gl"></div><div id="lb1"></div><div id="lb2"></div></div>'
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

def glitch_snd(d=0.3, amp=0.35):
    t = R._t(d); n = np.random.default_rng(5).standard_normal(len(t))
    gate = (np.sin(2 * np.pi * 37 * t) > 0).astype(float)
    return amp * n * gate * np.exp(-t / 0.15) + amp * 0.6 * np.sign(np.sin(2 * np.pi * 220 * t)) * gate * np.exp(-t / 0.08)

def shutter(amp=0.45):
    t = R._t(0.12); n = np.random.default_rng(6).standard_normal(len(t))
    return amp * n * (np.exp(-t / 0.01) + 0.6 * np.exp(-((t - 0.06) / 0.008) ** 2))

def audio(path):
    n = int(SR * TOTAL)
    beats = int(round((TOTAL - DROP) / BEAT))
    mus = musica(beats, intro=0, outro=4)
    mix = np.zeros(n + SR * 3)
    i0 = int(DROP * SR); mix[i0:i0 + len(mus)] += mus[:len(mix) - i0] * 0.6
    # el "Cortes." congela todo: la música se corta un momento
    a, b = int(9.5 * SR), int(10.45 * SR); mix[a:b] *= np.linspace(0.15, 0.6, b - a)
    def add(sig, t, g=1.0):
        i = int(max(0, t) * SR); mix[i:i + len(sig)] += g * sig[:len(mix) - i]
    room = np.random.default_rng(2).standard_normal(int(SR * DROP)) * 0.012; mix[:len(room)] += room
    t = R._t(0.12); add(0.25 * np.sin(2 * np.pi * 1760 * t) * np.exp(-t / 0.05), 0.05)
    add(R.boom(0.5), 0.0); add(glitch_snd(0.25, 0.25), 0.25)
    add(R.whoosh(0.3, 800, 5000, 0.4), 2.0)
    add(R.riser(1.4, 0.55), DROP - 1.4); add(R.boom(0.9), DROP); add(R.chime(0.4), DROP + 0.05)
    for s in SC:
        a0 = s['a']
        if s['tr'] in ('whip', 'slide'): add(R.whoosh(0.45, 300, 5000, 0.7), a0 - 0.12)
        if s['tr'] == 'zoom': add(R.whoosh(0.5, 150, 2500, 0.7), a0 - 0.2); add(R.boom(0.3), a0)
        if s['tr'] == 'glitch': add(glitch_snd(), a0 - 0.08)
        if s['kind'] == 'word': add(shutter(), a0); add(R.boom(0.7), a0)
        if s.get('ramp'): add(R.riser(0.6, 0.3), a0 + 0.1); add(R.whoosh(0.3, 1000, 6000, 0.5), a0 + 0.55)
        for (sa, sb, txt) in s.get('subs', []): add(R.pop(0.16, 1300), sa)
        for j, _ in enumerate(s.get('chips', [])): add(R.pop(0.32, 900 + 200 * j), a0 + 0.3 + j * 0.3)
        for (ta, _, _) in s.get('jumps', []): add(R.whoosh(0.15, 1500, 7000, 0.4), ta - 0.05); add(R.pop(0.2, 600), ta)
        if s['kind'] == 'split': add(R.whoosh(1.2, 200, 2500, 0.35), a0 + 0.2)
        if s['kind'] == 'tri':
            for j in range(3): add(R.whoosh(0.3, 400, 4000, 0.4), a0 + j * 0.12)
        if s['kind'] == 'edit':
            for q in range(6): add(R.tick(0.12), a0 + 0.3 + q * 0.12)
        if s['kind'] == 'export': add(R.chime(0.4), a0 + 1.25)
        if s['kind'] == 'montage':
            for q in range(4): add(R.boom(0.35), a0 + q * 0.25); add(shutter(0.25), a0 + q * 0.25)
        if s['kind'] == 'end': add(R.tap(0.4), a0 + 1.0); add(R.chime(0.3), a0 + 1.4)
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
