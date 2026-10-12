"""Carruseles 1080x1350 con la marca Gold Studio, a partir de las láminas del plan."""
import re, os, subprocess, html as H
SCR = '/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad'
F = f'file://{SCR}/logo/node_modules/@fontsource/'
SP = '<svg class="sp" viewBox="0 0 100 100"><path d="M50 0 C54.5 40 60 45.5 100 50 C60 54.5 54.5 60 50 100 C45.5 60 40 54.5 0 50 C40 45.5 45.5 40 50 0Z" fill="currentColor"/></svg>'
CHECK = '<svg class="ck" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12.5l5 5L20 6.5"/></svg>'

def clean(t):
    t = t.replace('✦', '§SP§')
    t = re.sub('[\U0001F000-\U0001FAFF☀-➿⬀-⯿]️?', '', t)
    return re.sub(r'\s+', ' ', t).replace('§SP§', '✦').strip()

def emph(t):
    """Texto entre paréntesis o tras ':' lo dejamos normal; *x* -> itálica dorada."""
    return re.sub(r'\*(.+?)\*', r'<em>\1</em>', H.escape(t))

CSS = f'''
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2);font-weight:500;font-style:italic}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-300-normal.woff2);font-weight:300}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-500-normal.woff2);font-weight:500}}
body{{margin:0;background:#888}}
.s{{width:1080px;height:1350px;box-sizing:border-box;padding:100px 96px 150px;position:relative;overflow:hidden;display:flex;flex-direction:column;justify-content:center;gap:36px;font-family:J;margin-bottom:20px}}
.m{{background:#FAF6EE;color:#1C1A17;--em:#8A6A22;--sub:#5E5649;--g:#B8923A;--line:#E6DAC2;--box:#F2EADA}}
.n{{background:#1C1A17;color:#FAF6EE;--em:#C9A34E;--sub:#BDB2A0;--g:#C9A34E;--line:#3A342B;--box:#26221D}}
.g{{background:#C9A34E;color:#1C1A17;--em:#FAF6EE;--sub:#3B3122;--g:#FAF6EE;--line:#B8923A;--box:#D4B263}}
h1{{font-family:B;font-weight:500;line-height:1.06;margin:0;letter-spacing:-.01em}}
h1 em,h2 em{{font-style:italic;color:var(--em)}}
h2{{font-family:B;font-weight:500;line-height:1.1;margin:0;font-size:76px}}
.eb{{font-size:26px;letter-spacing:.32em;text-transform:uppercase;font-weight:500;color:var(--em)}}
.num{{font-family:B;font-style:italic;font-size:150px;line-height:.8;color:var(--g)}}
.tip{{background:var(--box);border-radius:28px;padding:36px 40px;font-size:40px;line-height:1.4}}
.tip small{{display:block;font-size:22px;letter-spacing:.28em;text-transform:uppercase;color:var(--em);font-weight:500;margin-bottom:10px}}
.body{{font-size:44px;line-height:1.4;color:var(--sub);font-weight:300}}
.quote{{font-family:B;font-style:italic;font-size:58px;line-height:1.25;border-left:6px solid var(--g);padding-left:36px}}
.foot{{position:absolute;left:96px;right:96px;bottom:64px;display:flex;justify-content:space-between;font-size:24px;letter-spacing:.12em;color:var(--sub)}}
.foot .sw{{color:var(--em);font-weight:500}}
.sp{{width:100%;height:100%;display:block}}
.spk{{width:110px;height:110px;color:var(--g)}}
.ck{{width:90px;height:90px;color:var(--g);background:color-mix(in srgb,var(--g) 16%,transparent);border-radius:50%;padding:18px;box-sizing:border-box}}
.ring{{position:absolute;border-radius:50%;border:56px solid var(--g);opacity:.9}}
.pill{{align-self:flex-start;background:#1C1A17;color:#FAF6EE;font-size:32px;padding:24px 40px;border-radius:999px}}
.n .pill{{background:#C9A34E;color:#1C1A17}}
.s[style*="background"] .foot{{color:inherit;opacity:.75}}
'''

def foot(i, n):
    right = '<span class="sw">Deslizá →</span>' if i == 1 else f'<span>{i}/{n}</span>'
    return f'<div class="foot"><span>@goldstudio.ba</span>{right}</div>'

def render(name, slides, out_root='/home/user/gold-studio-final/carruseles'):
    """slides: lista de dicts {bg, kind, ...} ya armados."""
    N = len(slides); html = []
    for i, s in enumerate(slides, 1):
        bg = s.get('bg', 'm'); k = s['kind']; style = s.get('style', '')
        if k == 'cover':
            inner = (f'<div class="ring" style="width:420px;height:420px;right:-130px;top:-130px"></div>'
                     f'<div class="eb">{H.escape(s.get("eb", "Guardalo"))}</div><h1 style="font-size:{s.get("fs", 104)}px">{emph(s["text"])}</h1>'
                     + (f'<p class="body">{emph(s["sub"])}</p>' if s.get('sub') else ''))
        elif k == 'item':
            inner = (f'<div class="num">{s["n"]}</div><h2>{emph(s["title"])}</h2>'
                     + (f'<div class="tip"><small>{H.escape(s.get("tiplabel", "Cómo arreglarlo"))}</small>{emph(s["tip"])}</div>' if s.get('tip') else ''))
        elif k == 'check':
            inner = f'{CHECK}<h2 style="font-size:84px">{emph(s["title"])}</h2>' + (f'<p class="body">{emph(s["sub"])}</p>' if s.get('sub') else '')
        elif k == 'color':
            inner = f'<div class="eb" style="color:inherit;opacity:.75">Transmite</div><h1 style="font-size:150px">{H.escape(s["title"])}</h1><p class="body" style="color:inherit;opacity:.9;font-size:56px">{H.escape(s["tip"])}</p>'
        elif k == 'text':
            inner = (f'<div class="eb">{H.escape(s.get("eb", ""))}</div>' if s.get('eb') else '') + f'<h2>{emph(s["title"])}</h2>' + (f'<p class="body">{emph(s["sub"])}</p>' if s.get('sub') else '')
        elif k == 'quote':
            inner = f'<div class="eb">{H.escape(s.get("eb", "Ejemplo"))}</div><div class="quote">{emph(s["text"])}</div>'
        elif k == 'end':
            inner = f'<div class="spk">{SP}</div><h1 style="font-size:96px">{emph(s["text"])}</h1>' + (f'<div class="pill">{H.escape(s["pill"])}</div>' if s.get('pill') else '')
        html.append(f'<div class="s {bg}" style="{style}">{inner}{foot(i, N)}</div>')
    page = f'<!doctype html><meta charset="utf-8"><style>{CSS}</style>{"".join(html)}'
    work = f'{SCR}/cg-{name}'; os.makedirs(work, exist_ok=True)
    open(f'{work}/c.html', 'w').write(page)
    out = f'{out_root}/{name}'; os.makedirs(out, exist_ok=True)
    for f in os.listdir(out):
        if f.endswith('.png'): os.remove(os.path.join(out, f))
    js = f'''const {{ chromium }} = require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:1350}}}});
await p.goto('file://{work}/c.html');await p.evaluate(async()=>{{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;}});await p.waitForTimeout(300);
const els=await p.$$('.s');for(let i=0;i<els.length;i++)await els[i].screenshot({{path:'{out}/'+String(i+1).padStart(2,'0')+'.png'}});await b.close();}})();'''
    open(f'{work}/r.js', 'w').write(js)
    subprocess.run(['node', f'{work}/r.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
    return out
