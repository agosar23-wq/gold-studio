"""Genera reels de texto animado con la marca Gold Studio (HTML -> frames -> MP4 con efectos de sonido)."""
import re, os, subprocess, wave, html as H
import numpy as np

SCR = '/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad'
F = f'file://{SCR}/logo/node_modules/@fontsource/'
SP = '<svg class="sp" viewBox="0 0 100 100"><path d="M50 0 C54.5 40 60 45.5 100 50 C60 54.5 54.5 60 50 100 C45.5 60 40 54.5 0 50 C40 45.5 45.5 40 50 0Z" fill="currentColor"/></svg>'
_logo = open('/home/user/gold-studio-final/logo-gold-studio-transparente.svg').read()
LOGO = re.sub(r'<svg [^>]*viewBox="([^"]+)"[^>]*>', r'<svg class="logo" viewBox="\1">', _logo, count=1) \
    .replace('fill="#1C1A17"', 'fill="currentColor"').replace('fill="#B8923A"', 'style="fill:#B8923A"').replace('stroke="#B8923A"', 'style="stroke:#B8923A"')
FPS = 30


def words_html(text, base_id):
    """'Hola *mundo* lindo' -> spans por palabra; las palabras entre * van en itálica dorada."""
    out, em, i = [], False, 0
    for tok in text.split(' '):
        start = tok.startswith('*'); end = tok.rstrip('.,?!:;').endswith('*') or tok.endswith('*')
        if start: em = True
        clean = tok.replace('*', '')
        cls = 'w em' if em else 'w'
        out.append(f'<span class="{cls}" id="{base_id}w{i}">{H.escape(clean)}</span>')
        i += 1
        if end: em = False
    return ' '.join(out), i


def scene_dur(s):
    if 'dur' in s: return s['dur']
    n = len(re.sub(r'\*', '', s.get('text', '')).split()) + len(s.get('sub', '').split())
    base = {'end': 2.8, 'logo': 3.0, 'reveal': 3.2, 'phone': 2.8, 'strike': 2.4}.get(s.get('kind'), 0)
    if s.get('html'): base = max(base, 3.0)
    return max(base, min(3.6, 1.3 + 0.17 * n))


DECO = {
    'swatches': '<div class="deco sw">' + ''.join(f'<i style="background:{c}"></i>' for c in ['#E8505B', '#3BB0E8', '#F6C744', '#6BCB77', '#9B5DE5', '#FF8FAB']) + '</div>',
    'fonts': '<div class="deco fonts">' + ''.join(f'<span style="font-family:{f}">Marca</span>' for f in ['XArchivo', 'XPlayfair', 'XNotoSerif', 'XFamiljen', 'J']) + '</div>',
    'avatar': '<div class="deco av"><div class="big"><span>mi emprendimiento de tortas artesanales</span></div><div class="arrow">→</div><div class="small"><span>mi emprendimiento de tortas artesanales</span></div></div>',
}


def build(name, scenes, out_dir='/home/user/gold-studio-final/reels'):
    starts, t = [], 0.0
    for s in scenes:
        starts.append(t); t += scene_dur(s)
    total = round(t + 0.2, 2)
    parts = []
    for i, s in enumerate(scenes):
        k = s.get('kind', 'text'); bg = s.get('bg', 'm')
        wh, nw = words_html(s.get('text', ''), f's{i}')
        n_chars = len(re.sub(r'\*', '', s.get('text', '')))
        fs = s.get('fs') or (170 if n_chars <= 22 else 140 if n_chars <= 40 else 116 if n_chars <= 70 else 98)
        if i == 0 and not s.get('fs'): fs = int(fs * 1.1)
        inner = ''
        if k == 'end':
            inner += f'<div class="spk" id="s{i}spk">{SP}</div>'
        if s.get('eb'):
            inner += f'<div class="eb" id="s{i}eb">{H.escape(s["eb"])}</div>'
        if k == 'strike':
            inner += f'<div class="strike" id="s{i}st">{s["strike"]}<div class="line" id="s{i}ln"></div></div>'
        if k == 'logo':
            inner += f'''<div class="lg"><svg width="460" height="460" viewBox="0 0 560 560"><circle id="s{i}ring" cx="280" cy="280" r="220" fill="none" stroke="#B8923A" stroke-width="70" stroke-dasharray="1382.3" stroke-dashoffset="1382.3" transform="rotate(-90 280 280)"/></svg>
              <div class="lgsp" id="s{i}lsp">{SP}</div></div><div class="lgw" id="s{i}lgw">{LOGO}</div>'''
        if s.get('html') and s.get('html_pos') == 'top':
            inner += f'<div id="s{i}dc" class="deco hx">{s["html"]}</div>'
        inner += f'<h1 style="font-size:{fs}px">{wh}</h1>'
        if s.get('sub'):
            inner += f'<p class="sub" id="s{i}sub">{H.escape(s["sub"])}</p>'
        if s.get('deco'):
            inner += DECO[s['deco']].replace('class="deco', f'id="s{i}dc" class="deco')
        if s.get('html') and s.get('html_pos') != 'top':
            inner += f'<div id="s{i}dc" class="deco hx">{s["html"]}</div>'
        if k == 'phone':
            inner += f'<div class="phone" id="s{i}ph"><img src="{s["img"]}"></div>'
        if k == 'end' and s.get('pill'):
            inner += f'<div class="pill" id="s{i}pill">{H.escape(s["pill"])}</div>'
        parts.append(f'<div class="sc {bg} k-{k}" id="s{i}" data-start="{starts[i]}" data-nw="{nw}" data-kind="{k}">'
                     f'<div class="brand">GOLD STUDIO</div><div class="box">{inner}</div></div>')

    css = f'''
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2);font-weight:500;font-style:italic}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:XArchivo;src:url({F}archivo-black/files/archivo-black-latin-400-normal.woff2)}}
@font-face{{font-family:XPlayfair;src:url({F}playfair-display/files/playfair-display-latin-700-normal.woff2)}}
@font-face{{font-family:XNotoSerif;src:url({F}noto-serif/files/noto-serif-latin-900-normal.woff2)}}
@font-face{{font-family:XFamiljen;src:url({F}familjen-grotesk/files/familjen-grotesk-latin-700-normal.woff2)}}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#1C1A17}}
.sc{{position:absolute;inset:0;opacity:0;font-family:J}}
.m{{background:#FAF6EE;color:#1C1A17;--em:#8A6A22;--sub:#5E5649;--g:#B8923A}}
.n{{background:#1C1A17;color:#FAF6EE;--em:#C9A34E;--sub:#BDB2A0;--g:#C9A34E}}
.g{{background:#C9A34E;color:#1C1A17;--em:#FAF6EE;--sub:#3B3122;--g:#FAF6EE}}
.brand{{position:absolute;top:190px;left:0;right:0;text-align:center;font-size:24px;letter-spacing:.5em;padding-left:.5em;color:var(--sub);font-weight:500}}
.box{{position:absolute;left:100px;right:100px;top:330px;bottom:430px;display:flex;flex-direction:column;justify-content:center;gap:34px}}
.k-end .box,.k-logo .box{{align-items:center;text-align:center}}
h1{{font-family:B;font-weight:500;line-height:1.08;margin:0;letter-spacing:-.01em}}
.w{{display:inline-block}} .em{{font-style:italic;color:var(--em)}}
.eb{{font-size:30px;letter-spacing:.32em;text-transform:uppercase;font-weight:500;color:var(--em)}}
.sub{{font-size:52px;line-height:1.35;color:var(--sub);margin:0}}
.sp{{width:100%;height:100%;display:block}}
.spk{{width:140px;height:140px;color:var(--g)}}
.pill{{background:#1C1A17;color:#FAF6EE;font-size:40px;padding:30px 54px;border-radius:999px}}
.g .pill{{background:#1C1A17}} .n .pill{{background:#C9A34E;color:#1C1A17}}
.deco.sw{{display:flex;gap:18px;flex-wrap:wrap}} .deco.sw i{{width:120px;height:120px;border-radius:50%}}
.deco.fonts{{display:flex;flex-direction:column;gap:4px;font-size:84px;line-height:1.05}}
.deco.av{{display:flex;align-items:center;gap:50px}}
.av .big{{width:300px;height:300px;border-radius:50%;background:#E9DFC8;display:grid;place-items:center;text-align:center;padding:40px;box-sizing:border-box;font-size:30px;color:#5E5649}}
.av .small{{width:90px;height:90px;border-radius:50%;background:#E9DFC8;display:grid;place-items:center;text-align:center;padding:10px;box-sizing:border-box;font-size:9px;color:#5E5649;overflow:hidden}}
.av .arrow{{font-size:80px;color:var(--em)}}
.strike{{position:relative;align-self:flex-start;font-family:XFamiljen;font-size:120px;line-height:1}}
.strike img{{height:260px;display:block}}
.strike .line{{position:absolute;left:-20px;top:50%;height:12px;width:0;background:#C0392B;border-radius:6px;transform:rotate(-6deg)}}
.lg{{position:relative;width:460px;height:460px}}
.lgsp{{position:absolute;right:-70px;top:-60px;width:150px;height:150px;color:#B8923A}}
.lgw{{width:520px;opacity:0}} .logo{{width:100%;height:auto;display:block}}
.deco.hx{{align-self:center}}
.phone{{width:360px;align-self:center;border-radius:62px;padding:14px;background:#0E0D0B;box-shadow:0 50px 100px -40px rgba(0,0,0,.5),0 0 0 3px #3A342B}}
.phone img{{width:100%;display:block;border-radius:50px}}
'''
    js = '''
const E=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
const B=x=>{x=Math.max(0,Math.min(1,x));const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};
const $=id=>document.getElementById(id);
function up(el,p,d=70){if(!el)return;el.style.opacity=E(p);el.style.transform=`translateY(${(1-E(p))*d}px)`;}
const SC=[...document.querySelectorAll('.sc')];
window.render=function(t){
  SC.forEach((s,i)=>{
    const a=+s.dataset.start, k=t-a, nw=+s.dataset.nw, kind=s.dataset.kind;
    s.style.opacity = i===0 ? 1 : (k>=0?Math.min(1,k/0.28):0);
    if(k<0) return;
    up($(`s${i}eb`),(k-0.05)/0.4,40);
    let w0 = kind==='logo'?1.3:kind==='reveal'?1.1:kind==='end'?0.35:kind==='strike'?0.1:0.12; if(s.querySelector('.hx+h1')) w0=0.45;
    if(kind==='strike'){ up($(`s${i}st`),(k-0.05)/0.4,60); const ln=$(`s${i}ln`); if(ln) ln.style.width=(E((k-0.75)/0.35)*110)+'%'; w0=1.0; }
    for(let j=0;j<nw;j++) up($(`s${i}w${j}`),(k-w0-j*0.045)/0.4,80);
    const after=w0+nw*0.045;
    up($(`s${i}sub`),(k-after-0.15)/0.45,50);
    const dc=$(`s${i}dc`); if(dc){ if(kind==='reveal'){const p=E((k-0.25)/0.9);dc.style.opacity=E((k-0.25)/0.5);dc.style.transform=`scale(${0.7+0.3*p}) rotate(${(1-p)*-4}deg)`;dc.style.filter=`blur(${(1-p)*14}px)`;}
      else {const t0=dc.classList.contains('hx')&&s.querySelector('.hx+h1')?0.05:after+0.2;const p=B((k-t0)/0.5);dc.style.opacity=E((k-t0)/0.3);dc.style.transform=`scale(${0.85+0.15*p})`;} }
    const ph=$(`s${i}ph`); if(ph){const p=E((k-0.1)/0.7);ph.style.opacity=Math.min(1,p*2);ph.style.transform=`translateY(${(1-p)*500}px) rotate(${(1-p)*6-2}deg)`;}
    const spk=$(`s${i}spk`); if(spk){const p=B((k-0.1)/0.55);spk.style.transform=`scale(${p*(1+0.06*Math.sin(k*4))}) rotate(${(1-p)*-90}deg)`;}
    const pill=$(`s${i}pill`); up(pill,(k-after-0.25)/0.45,50);
    const ring=$(`s${i}ring`); if(ring){ring.style.strokeDashoffset=1382.3*(1-E((k-0.05)/0.9));
      const p=B((k-0.85)/0.5);$(`s${i}lsp`).style.transform=`scale(${p}) rotate(${(1-p)*-90}deg)`;up($(`s${i}lgw`),(k-1.0)/0.5,40);}
  });
};
'''
    page = f'<!doctype html><meta charset="utf-8"><style>{css}</style>{"".join(parts)}<script>{js}</script>'
    work = f'{SCR}/rg-{name}'; os.makedirs(work + '/f', exist_ok=True)
    for f in os.listdir(work + '/f'): os.remove(os.path.join(work, 'f', f))
    open(f'{work}/r.html', 'w').write(page)
    env = dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules')
    subprocess.run(['node', f'{SCR}/reel.js', f'{work}/r.html', str(total), f'{work}/f'], check=True, env=env)
    sfx(scenes, starts, total, f'{work}/a.wav')
    import imageio_ffmpeg
    FF = imageio_ffmpeg.get_ffmpeg_exe()
    os.makedirs(out_dir, exist_ok=True)
    out = f'{out_dir}/{name}.mp4'
    subprocess.run([FF, '-y', '-loglevel', 'error', '-framerate', str(FPS), '-i', f'{work}/f/%04d.jpg', '-i', f'{work}/a.wav',
                    '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '19', '-preset', 'slow',
                    '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', out], check=True)
    return out, total, work


# ---------------- sonido ----------------
SR = 44100
rng = np.random.default_rng(3)
def _t(d): return np.arange(int(SR * d)) / SR
def _lp(x, f0, f1):
    y = np.zeros_like(x); f = np.linspace(0, 1, len(x)); fc = f0 + (f1 - f0) * np.sin(np.pi * f)
    a = np.exp(-2 * np.pi * fc / SR); s = 0.0
    for n in range(len(x)): s = a[n] * s + (1 - a[n]) * x[n]; y[n] = s
    return y
def whoosh(d=0.4, f0=250, f1=2800, amp=0.4):
    t = _t(d); y = _lp(rng.standard_normal(len(t)), f0, f1) * np.sin(np.pi * t / d) ** 2
    return amp * y / (np.abs(y).max() + 1e-9)
def tick(amp=0.05):
    t = _t(0.04); return amp * np.sin(2 * np.pi * 1900 * t) * np.exp(-t / 0.008)
def tap(amp=0.3):
    t = _t(0.09)
    return amp * (np.sin(2 * np.pi * 180 * t) * np.exp(-t / 0.018) + 0.5 * np.sin(2 * np.pi * 420 * t) * np.exp(-t / 0.01) + rng.standard_normal(len(t)) * np.exp(-t / 0.002) * 0.3)
def chime(amp=0.22):
    y = np.zeros(int(SR * 1.8))
    for k, (f, dt) in enumerate([(1318.5, 0), (1975.5, .06), (2637, .12), (3951, .2)]):
        t = _t(1.8 - dt); s = np.sin(2 * np.pi * f * t) * np.exp(-t / (0.5 - k * 0.07)) * (1 - 0.15 * k)
        i = int(dt * SR); y[i:i + len(s)] += s
    return amp * y / np.abs(y).max()

def boom(amp=0.9):
    t = _t(0.45); f = 110 * np.exp(-t / 0.08) + 45
    return amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.16)
def pop(amp=0.35, f0=900):
    t = _t(0.07); f = f0 * np.exp(-t / 0.02) + 300
    return amp * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.02)
def riser(d=0.6, amp=0.4):
    t = _t(d); y = _lp(rng.standard_normal(len(t)), 300, 6000) * (t / d) ** 2
    return amp * y / (np.abs(y).max() + 1e-9)

def sfx(scenes, starts, total, path):
    out = np.zeros(int(SR * (total + 2)))
    def add(sig, t):
        i = int(max(0, t) * SR); out[i:i + len(sig)] += sig[:len(out) - i]
    for i, s in enumerate(scenes):
        a = starts[i]; k = s.get('kind', 'text')
        nw = len(s.get('text', '').split())
        w0 = {'logo': 1.3, 'reveal': 1.1, 'end': 0.35, 'strike': 1.0}.get(k, 0.12); ST = 0.045
        if s.get('html_pos') == 'top': w0 = 0.45
        if i == 0:
            add(boom(), a + 0.02)
            for j in range(nw): add(tick(0.12), a + w0 + j * ST)
        else:
            add(whoosh(0.4, 400, 4200, 0.7), a - 0.15)
            add(pop(0.38, 1000 + 120 * (i % 3)), a + w0 + 0.2)
        if s.get('sub'): add(pop(0.25, 1400), a + w0 + nw * ST + 0.2)
        if k == 'strike': add(whoosh(0.2, 2000, 7000, 0.6), a + 0.75)
        if k == 'logo':
            add(riser(0.75, 0.35), a + 0.15); add(chime(0.45), a + 0.88)
        if k == 'phone': add(whoosh(0.6, 150, 1600, 0.6), a + 0.1)
        if s.get('deco') or (s.get('html') and k != 'reveal'): add(pop(0.4, 700), a + (0.1 if s.get('html_pos') == 'top' else w0 + nw * ST + 0.3))
        if k == 'reveal': add(riser(0.6, 0.3), a + 0.1); add(chime(0.5), a + 0.75)
        if k == 'end':
            add(riser(0.6, 0.45), a - 0.6)
            add(boom(0.6), a)
            add(chime(0.5), a + 0.15)
            add(tap(0.4), a + w0 + nw * ST + 0.35)
    out = out[:int(SR * total)]
    fade = int(0.2 * SR); out[-fade:] *= np.linspace(1, 0, fade)
    out = np.tanh(out * 1.6) / np.tanh(1.6)          # comprime un poco: todo suena más presente
    out = out / (np.abs(out).max() + 1e-9) * 0.95
    pcm = (out * 32767).astype('<i2')
    with wave.open(path, 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(np.column_stack([pcm, pcm]).ravel().tobytes())
