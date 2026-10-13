"""Carruseles 'Así diseñaría la portada del próximo single de…' (Mora y Omar Courtz). Conceptos no oficiales."""
import sys, base64; sys.path.insert(0, '/home/user/gold-studio-contenido')
from caro_ejemplos import render
from carogen import SP, SCR, F
P = f'{SCR}/portadas'; A = f'{SCR}/artistas'
def b(p, m='image/png'): return f'data:{m};base64,' + base64.b64encode(open(p, 'rb').read()).decode()
XF = f'file://{SCR}/xfonts'
EXT = f'''
@font-face{{font-family:Hand;src:url({XF}/caveat.woff2)}}
.ph{{background-size:cover;background-position:center}}
.cover{{box-shadow:0 50px 90px -40px rgba(0,0,0,.65)}}
.kw{{display:flex;flex-wrap:wrap;gap:14px}} .kw span{{border:2px solid var(--g);color:var(--em);border-radius:999px;padding:12px 26px;font-size:28px}}
.sw{{display:flex;gap:14px}} .sw i{{flex:1;height:120px;border-radius:18px}}
.an{{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}} .an div{{background:var(--box);border-radius:24px;padding:26px 28px}}
.an b{{display:block;font-family:B;font-weight:500;font-size:38px;margin-bottom:6px}} .an span{{font-size:26px;color:var(--sub);line-height:1.35}}
.mood{{display:grid;grid-template-columns:1.3fr 1fr;grid-template-rows:330px 330px;gap:14px}} .mood div{{border-radius:20px}}
.hand{{font-family:Hand;font-size:44px;color:var(--em)}}
.player{{width:520px;background:linear-gradient(#2a2a2a,#121212);border-radius:36px;padding:34px;color:#fff;font-family:J;box-shadow:0 50px 90px -40px rgba(0,0,0,.7)}}
.bar{{height:6px;background:#555;border-radius:3px;margin:26px 0 10px;position:relative}} .bar i{{position:absolute;left:0;top:0;bottom:0;width:38%;background:#fff;border-radius:3px}}
.ctrl{{display:flex;justify-content:space-around;align-items:center;margin-top:20px;font-size:40px}}
.vinyl{{width:470px;height:470px;border-radius:50%;background:radial-gradient(circle,#111 0 18%,#2b2b2b 18.5% 19%,#111 19.5% 30%,#1c1c1c 30.5% 31%,#111 31.5% 45%,#1e1e1e 45.5% 46%,#0c0c0c 46.5%);position:relative}}
.vinyl i{{position:absolute;inset:32%;border-radius:50%;background-size:cover;background-position:center}}
'''
PLAY = '<svg width="80" height="80" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12" fill="#fff"/><path d="M9.5 7.5v9l7-4.5z" fill="#111"/></svg>'

def slides(name, artista, cancion, eb_estilo, estilo_items, colores, kws, idea, mood, notas_cierre):
    fin, bos = b(f'{P}/{name}-final.png'), b(f'{P}/{name}-boceto.png')
    S = []
    S.append(('n', f'''<div class="eb">Portada concepto</div><h1 style="font-size:96px">Así diseñaría la portada del próximo single de <em>{artista}</em></h1>
      <div style="position:relative;height:470px;margin-top:10px"><div class="ph cover" style="position:absolute;left:40px;top:30px;width:400px;height:400px;background-image:url({bos});transform:rotate(-6deg)"></div>
      <div class="ph cover" style="position:absolute;left:400px;top:0;width:420px;height:420px;background-image:url({fin});transform:rotate(4deg);filter:blur(14px)"></div>
      <div class="hand" style="position:absolute;left:520px;top:200px;color:#FAF6EE;font-size:60px;transform:rotate(-6deg)">el final al final ;)</div></div>''', 'justify-content:center'))
    S.append(('m', f'''<div class="eb">Paso 1 · Analizo su estilo</div><h2 style="font-size:70px">{eb_estilo}</h2>
      <div class="an">{''.join(f'<div><b>{t}</b><span>{d}</span></div>' for t, d in estilo_items)}</div>
      <div class="sw">{''.join(f'<i style="background:{c}"></i>' for c in colores)}</div><div class="kw">{''.join(f'<span>{k}</span>' for k in kws)}</div>''', 'gap:30px'))
    S.append(('m', f'''<div class="eb">Paso 2 · La idea</div><h2 style="font-size:72px">Un single que se llame <em>“{cancion}”</em></h2>
      <p class="body" style="font-size:34px;margin:0">{idea}</p>
      <div class="mood">{''.join(f'<div class="ph" style="background-image:url({m});{"grid-row:span 2;" if i == 0 else ""}"></div>' for i, m in enumerate(mood))}</div>''', 'gap:30px'))
    S.append(('m', f'''<div class="eb">Paso 3 · El boceto</div><div class="ph cover" style="width:860px;height:860px;align-self:center;background-image:url({bos})"></div>''', 'gap:30px'))
    S.append(('n', f'''<div class="eb">Paso 4 · El final</div><div class="ph cover" style="width:880px;height:880px;align-self:center;background-image:url({fin})"></div>''', 'gap:30px'))
    S.append(('n', f'''<div class="eb">Así se vería</div><div style="display:flex;align-items:center;justify-content:center;gap:0;margin-top:20px">
      <div class="player"><div class="ph" style="width:100%;aspect-ratio:1;border-radius:18px;background-image:url({fin})"></div>
        <div style="margin-top:26px;font-size:40px;font-weight:500">{cancion}</div><div style="font-size:28px;color:#aaa">{artista}</div>
        <div class="bar"><i></i></div><div style="display:flex;justify-content:space-between;font-size:20px;color:#aaa"><span>1:12</span><span>3:08</span></div>
        <div class="ctrl"><span>⏮</span>{PLAY}<span>⏭</span></div></div>
      <div class="vinyl" style="margin-left:-150px;z-index:-0"><i style="background-image:url({fin})"></i></div></div>''', 'gap:30px'))
    S.append(('g', f'''<div class="spk">{SP}</div><h1 style="font-size:92px">¿Qué artista hago <em>la próxima?</em></h1>
      <div class="pill">Contame en comentarios</div><p class="body" style="font-size:28px;margin:0">{notas_cierre}</p>''', ''))
    return S

MORA = slides('mora', 'Mora', 'La luz prendida', 'Nostálgico, de casa y de recuerdos',
    [('Fotos reales', 'Lugares de la casa y de la infancia, nada de estudio.'), ('Letra a mano', 'Títulos escritos o garabateados, como en un cuaderno.'),
     ('Grano de película', 'Colores cálidos y lavados, como foto vieja.'), ('Detalles chiquitos', 'El nombre pequeño, sin gritar.')],
    ['#2A1A12', '#7A3B1E', '#D98A3D', '#F2C27A', '#FFF1D6'], ['Nostalgia', 'Casa', 'Noche', 'Recuerdos'],
    'Una lámpara que queda prendida en un cuarto vacío, como esperando a alguien. Cálida, íntima y con el grano de las fotos de antes.',
    [b(f'{A}/30233121.jpg', 'image/jpeg'), b(f'{A}/30233118.jpg', 'image/jpeg'), b(f'{A}/30233117.jpg', 'image/jpeg')],
    'Concepto hecho por mí para practicar, no es una portada oficial. Fotos de Pexels.')
OMAR = slides('omar', 'Omar Courtz', 'Hadas', 'Neón, noche y mucho brillo',
    [('Azul eléctrico', 'Fondos saturados que se ven de lejos.'), ('Neón rosa y verde', 'Brillos que parecen luz real.'),
     ('Hadas', 'Un símbolo que repite: magia, musas, algo que vuela.'), ('Onda Y2K', 'Letras redondas, brillos y estrellitas.')],
    ['#04083C', '#1432FF', '#FF2FC0', '#22FF90', '#E6F4FF'], ['Neón', 'Noche', 'Magia', 'Y2K'],
    'Una noche de lluvia en la ciudad: una silueta con paraguas, todo azul, y dos hadas de neón que la siguen. Como si la magia apareciera cuando nadie mira.',
    [b(f'{A}/14458037.jpg', 'image/jpeg'), b(f'{A}/14458035.jpg', 'image/jpeg'), b(f'{A}/29501856.jpg', 'image/jpeg')],
    'Concepto hecho por mí para practicar, no es una portada oficial. Fotos de Pexels.')

if __name__ == '__main__':
    print(render('portada-concepto-mora', MORA, EXT))
    print(render('portada-concepto-omar-courtz', OMAR, EXT))
