import datetime, html, json
exec(open('/home/user/gold-studio-contenido/plan_data.py').read())

DIAS = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
DCORTO = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
MESES = ['', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
start = datetime.date.fromisoformat(INICIO)
e = html.escape

items = []
for i, p in enumerate(P):
    d = start + datetime.timedelta(days=i)
    items.append(dict(p, n=i + 1, fecha=d, dia=DIAS[d.weekday()], corto=DCORTO[d.weekday()], hora=HORARIOS[d.weekday()]))

# ---------- calendario ----------
cal = []
for w in range(5):
    cells = []
    for wd in range(7):
        idx = w * 7 + wd
        if idx >= len(items):
            cells.append('<div class="cell empty" aria-hidden="true"></div>')
            continue
        it = items[idx]
        cells.append(f'''<a class="cell f-{it['formato'].lower()}" href="#d{it['n']}" data-n="{it['n']}">
  <span class="c-top"><span class="c-date">{it['corto']} {it['fecha'].day}</span><span class="c-time">{it['hora']}</span></span>
  <span class="c-fmt">{it['formato']}</span>
  <span class="c-hook">{e(it['hook'])}</span>
  <span class="c-done" aria-hidden="true">✓</span>
</a>''')
    cal.append(f'<div class="week"><div class="wk">Semana {w+1}</div><div class="cells">{"".join(cells)}</div></div>')

# ---------- tarjetas ----------
cards = []
for it in items:
    if it['formato'] == 'Reel':
        body = '<ol class="slides">' + ''.join(f'<li><span class="t">{k+1}</span>{e(l)}</li>' for k, l in enumerate(it['escenas'])) + '</ol>'
        label = 'Texto en pantalla, escena por escena'
    else:
        body = '<ol class="slides">' + ''.join(
            f'<li><span class="t">{k+1}</span>{e(l)}</li>' for k, l in enumerate(it['laminas'])) + '</ol>'
        label = 'Láminas'
    cards.append(f'''<article class="card f-{it['formato'].lower()}" id="d{it['n']}" data-fmt="{it['formato']}" data-pilar="{it['pilar']}">
  <header class="card-h">
    <div class="meta"><span class="day">Día {it['n']} · {it['dia']} {it['fecha'].day} de {MESES[it['fecha'].month]}</span><span class="time">{it['hora']} h</span></div>
    <div class="tags"><span class="tag fmt">{it['formato']}</span><span class="tag">{it['pilar']}</span></div>
  </header>
  <p class="eyebrow">Hook</p>
  <h3 class="hook">{e(it['hook'])}</h3>
  <div class="block"><p class="eyebrow">Cómo se ve</p><p>{e(it['visual'])}</p></div>
  <div class="block"><p class="eyebrow">{label}</p>{body}</div>
  <div class="row2">
    <div class="block"><p class="eyebrow">Llamada a la acción</p><p>{e(it['cta'])}</p></div>
    <div class="block why"><p class="eyebrow">Por qué funciona</p><p>{e(it['porque'])}</p></div>
  </div>
  <div class="block caption"><p class="eyebrow">Texto para el posteo</p><p class="cap-text" id="cap{it['n']}">{e(it['caption'])}</p>
    <div class="actions"><button type="button" class="btn" data-copy="cap{it['n']}">Copiar texto</button>
    <label class="done"><input type="checkbox" id="done{it['n']}" data-n="{it['n']}"> Publicado</label></div></div>
</article>''')

page = f'''<title>Plan Gold Studio · 30 días</title>
<meta name="description" content="Calendario y guiones de 30 días para @goldstudio.ba">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..600;1,6..96,400..600&family=Jost:wght@300;400;500;600&display=swap">
<style>
/* Layout: cabecera editorial, calendario de 5 semanas, luego las 30 fichas en columna */
:root{{
  --bg:#FAF6EE; --bg2:#F2EADA; --card:#FFFDF8; --ink:#1C1A17; --ink2:#5E5649; --line:#E6DAC2;
  --gold:#B8923A; --gold-ink:#8A6A22; --on-gold:#FFFDF8; --reel:#1C1A17; --on-reel:#FAF6EE; --ok:#4E7A4A;
  --serif:'Bodoni Moda', Georgia, serif; --sans:'Jost', system-ui, -apple-system, 'Segoe UI', sans-serif;
}}
@media (prefers-color-scheme: dark){{ :root:not([data-theme="light"]){{
  --bg:#171512; --bg2:#1F1C17; --card:#24201B; --ink:#F4EEE2; --ink2:#BDB2A0; --line:#3A3329;
  --gold:#C9A34E; --gold-ink:#D8B661; --on-gold:#1C1A17; --reel:#F4EEE2; --on-reel:#1C1A17; --ok:#8DBB85; color-scheme:dark }} }}
:root[data-theme="dark"]{{
  --bg:#171512; --bg2:#1F1C17; --card:#24201B; --ink:#F4EEE2; --ink2:#BDB2A0; --line:#3A3329;
  --gold:#C9A34E; --gold-ink:#D8B661; --on-gold:#1C1A17; --reel:#F4EEE2; --on-reel:#1C1A17; --ok:#8DBB85; color-scheme:dark }}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--ink);font:400 16px/1.6 var(--sans);margin:0}}
.wrap{{max-width:1120px;margin:0 auto;padding-inline:20px;padding-block:40px 80px}}
h1,h2,h3{{font-family:var(--serif);font-weight:500;line-height:1.1;margin:0;text-wrap:balance}}
h1{{font-size:clamp(38px,6vw,64px)}} h1 em{{color:var(--gold-ink)}}
h2{{font-size:clamp(28px,4vw,38px);margin-bottom:18px}}
.eyebrow{{font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--gold-ink);font-weight:500;margin:0 0 6px}}
.lead{{font-size:18px;color:var(--ink2);max-width:62ch;font-weight:300;margin:16px 0 0}}
section{{margin-top:56px}}
.info{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:28px}}
.box{{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;min-width:0}}
.box b{{font-family:var(--serif);font-size:22px;font-weight:500;display:block;margin-bottom:4px}}
.box p{{margin:0;color:var(--ink2);font-size:15px}}
.hours{{display:grid;grid-template-columns:repeat(auto-fill,minmax(58px,1fr));gap:6px;margin-top:10px;font-variant-numeric:tabular-nums}}
.hours span{{display:flex;flex-direction:column;align-items:center;font-size:12px;color:var(--ink2);background:var(--bg2);border-radius:10px;padding:6px 2px}}
.hours span b{{font-family:var(--sans);font-size:14px;font-weight:600;color:var(--ink);margin:0}}
.week{{display:grid;grid-template-columns:90px minmax(0,1fr);gap:12px;align-items:start;margin-bottom:12px}}
.wk{{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink2);padding-top:12px}}
.cells{{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:8px}}
.cell{{position:relative;display:flex;flex-direction:column;gap:6px;min-height:150px;padding:10px;border-radius:14px;text-decoration:none;color:var(--ink);background:var(--card);border:1px solid var(--line);transition:transform .15s,border-color .15s;min-width:0}}
.cell:hover{{transform:translateY(-2px);border-color:var(--gold)}}
.cell.empty{{background:transparent;border:1px dashed var(--line)}}
.c-top{{display:flex;justify-content:space-between;font-size:12px;color:var(--ink2);font-variant-numeric:tabular-nums}}
.c-date{{font-weight:600;color:var(--ink)}}
.c-fmt{{align-self:flex-start;font-size:11px;letter-spacing:.08em;text-transform:uppercase;padding:2px 8px;border-radius:999px}}
.f-reel .c-fmt{{background:var(--reel);color:var(--on-reel)}}
.f-carrusel .c-fmt{{background:var(--gold);color:var(--on-gold)}}
.c-hook{{font-size:13px;line-height:1.35;overflow:hidden;display:-webkit-box;-webkit-line-clamp:5;-webkit-box-orient:vertical}}
.c-done{{display:none;position:absolute;right:8px;bottom:6px;color:var(--ok);font-weight:700}}
.cell.is-done{{opacity:.6}} .cell.is-done .c-done{{display:block}}
.filters{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:22px}}
.filters button{{font:500 14px var(--sans);padding:8px 16px;border-radius:999px;border:1px solid var(--line);background:var(--card);color:var(--ink);cursor:pointer}}
.filters button[aria-pressed="true"]{{background:var(--ink);color:var(--bg);border-color:var(--ink)}}
.cards{{display:grid;gap:20px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:26px 28px;scroll-margin-top:20px;min-width:0}}
.card:target{{border-color:var(--gold);box-shadow:0 0 0 3px color-mix(in srgb,var(--gold) 25%,transparent)}}
.card-h{{display:flex;justify-content:space-between;align-items:flex-start;gap:12px;flex-wrap:wrap;margin-bottom:16px;padding-bottom:14px;border-bottom:1px solid var(--line)}}
.meta{{display:flex;gap:14px;flex-wrap:wrap;align-items:baseline}}
.day{{font-weight:500}} .time{{font-variant-numeric:tabular-nums;color:var(--gold-ink);font-weight:600}}
.tags{{display:flex;gap:6px}}
.tag{{font-size:12px;padding:3px 10px;border-radius:999px;border:1px solid var(--line);color:var(--ink2)}}
.f-reel .tag.fmt{{background:var(--reel);color:var(--on-reel);border-color:var(--reel)}}
.f-carrusel .tag.fmt{{background:var(--gold);color:var(--on-gold);border-color:var(--gold)}}
.hook{{font-size:clamp(24px,3vw,32px);margin-bottom:18px}}
.block{{margin-top:16px;min-width:0}} .block p{{margin:0}}
.script,.slides{{list-style:none;margin:6px 0 0;padding:0;display:grid;gap:8px}}
.script li,.slides li{{display:grid;grid-template-columns:62px minmax(0,1fr);gap:10px;align-items:baseline}}
.script li.note{{display:block;color:var(--ink2);font-style:italic}}
.t{{font-size:12px;font-variant-numeric:tabular-nums;color:var(--gold-ink);font-weight:600;background:var(--bg2);border-radius:8px;padding:2px 6px;text-align:center}}
.row2{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.why p{{color:var(--ink2)}}
.caption{{background:var(--bg2);border-radius:14px;padding:16px 18px}}
.actions{{display:flex;gap:14px;align-items:center;flex-wrap:wrap;margin-top:12px}}
.btn{{font:500 14px var(--sans);padding:9px 18px;border-radius:999px;border:0;background:var(--gold);color:var(--on-gold);cursor:pointer}}
.done{{display:inline-flex;gap:8px;align-items:center;font-size:14px;color:var(--ink2);cursor:pointer}}
.done input{{accent-color:var(--gold);width:18px;height:18px}}
:focus-visible{{outline:2px solid var(--gold);outline-offset:3px}}
.toast{{position:fixed;left:50%;bottom:calc(20px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);background:var(--ink);color:var(--bg);padding:10px 18px;border-radius:999px;font-size:14px;opacity:0;transition:opacity .2s;pointer-events:none}}
.toast.show{{opacity:1}}
.tips{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}}
.tips ul{{margin:8px 0 0;padding-left:18px;color:var(--ink2)}} .tips li{{margin-bottom:4px}}
@media (max-width:860px){{
  .info,.tips,.row2{{grid-template-columns:1fr}}
  .week{{grid-template-columns:1fr;gap:6px}} .wk{{padding-top:0}}
  .cells{{grid-template-columns:1fr 1fr}}
  .cell{{min-height:0}} .cell.empty{{display:none}}
  .card{{padding:20px 18px}}
}}
@media (prefers-reduced-motion:reduce){{.cell{{transition:none}}}}
</style>
<div class="wrap">
  <p class="eyebrow">@goldstudio.ba · 12 de octubre → 10 de noviembre</p>
  <h1>30 días de contenido <em>con brillo propio</em></h1>
  <p class="lead">Un posteo por día y no tenés que grabar nada: los reels son animaciones de texto con tus colores y efectos de sonido, y los carruseles van listos para subir. Cada uno trae su hook, el texto para el posteo y por qué funciona.</p>

  <div class="info">
    <div class="box"><b>17 reels · 13 carruseles</b><p>Los reels te muestran a gente nueva. Los carruseles hacen que te guarden y confíen en vos.</p></div>
    <div class="box"><b>Cuándo publicar</b><p>Tu público se conecta más a las <strong>10 h</strong> y a las <strong>18 h</strong>. Reels a la mañana, carruseles a la tarde.</p>
      <div class="hours">{''.join(f'<span>{DCORTO[i]}<b>{HORARIOS[i]}</b></span>' for i in range(7))}</div></div>
    <div class="box"><b>Sin grabar nada</b><p>Te mando cada reel animado y cada carrusel listo. Vos le sumás un audio en tendencia en Instagram y publicás.</p></div>
  </div>

  <section aria-labelledby="cal-t">
    <h2 id="cal-t">Calendario</h2>
    {''.join(cal)}
  </section>

  <section aria-labelledby="g-t">
    <h2 id="g-t">Guiones</h2>
    <div class="filters" role="group" aria-label="Filtrar guiones">
      <button type="button" data-f="all" aria-pressed="true">Todos</button>
      <button type="button" data-f="Reel" aria-pressed="false">Reels</button>
      <button type="button" data-f="Carrusel" aria-pressed="false">Carruseles</button>
    </div>
    <div class="cards">{''.join(cards)}</div>
  </section>

  <section aria-labelledby="t-t">
    <h2 id="t-t">Para publicar</h2>
    <div class="tips">
      <div class="box"><b>Cómo subir un reel</b><ul>
        <li>Guardá el video en tu celu y en Instagram tocá <em>+ → Reel</em>.</li>
        <li>Tocá <em>Audio 🎵</em> y elegí una canción con flechita ↗ (en tendencia).</li>
        <li>En <em>Volumen</em>: audio original alto (los efectos) y música entre 30 y 50.</li>
        <li>Copiá el texto desde acá con el botón y activá <em>Compartir también en el feed</em>.</li></ul></div>
      <div class="box"><b>Después de publicar</b><ul>
        <li>Compartilo en tus historias apenas lo subas.</li>
        <li>Respondé los comentarios en la primera hora.</li>
        <li>A las 2 semanas mirá en Estadísticas → Seguidores → Momentos de más actividad, y ajustá los horarios.</li>
        <li>Conectá @goldstudio.ba a Metricool para tener tus propios datos.</li></ul></div>
    </div>
  </section>
</div>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script>
(function(){{
  var toast=document.getElementById('toast'),tt;
  function say(t){{toast.textContent=t;toast.classList.add('show');clearTimeout(tt);tt=setTimeout(function(){{toast.classList.remove('show')}},1800)}}
  document.querySelectorAll('[data-copy]').forEach(function(b){{b.addEventListener('click',function(){{
    var el=document.getElementById(b.dataset.copy),txt=el.textContent;
    function sel(){{var r=document.createRange();r.selectNodeContents(el);var s=getSelection();s.removeAllRanges();s.addRange(r);say('Texto seleccionado: copialo')}}
    try{{navigator.clipboard.writeText(txt).then(function(){{say('Copiado ✓')}},sel)}}catch(e){{sel()}}
  }})}});
  var KEY='gs-plan-hechos'; var done={{}};
  try{{done=JSON.parse(localStorage.getItem(KEY)||'{{}}')}}catch(e){{}}
  function paint(n){{var c=document.querySelector('.cell[data-n="'+n+'"]');if(c)c.classList.toggle('is-done',!!done[n])}}
  document.querySelectorAll('.done input').forEach(function(i){{var n=i.dataset.n;i.checked=!!done[n];paint(n);
    i.addEventListener('change',function(){{done[n]=i.checked;paint(n);try{{localStorage.setItem(KEY,JSON.stringify(done))}}catch(e){{}}}})}});
  var btns=document.querySelectorAll('.filters button');
  btns.forEach(function(b){{b.addEventListener('click',function(){{btns.forEach(function(x){{x.setAttribute('aria-pressed',x===b)}});
    document.querySelectorAll('.card').forEach(function(c){{c.hidden=!(b.dataset.f==='all'||c.dataset.fmt===b.dataset.f)}})}})}});
}})();
</script>'''
open('/home/user/gold-studio-contenido/plan-30-dias.html', 'w').write(page)

# ---------- markdown (para el skill y para descargar) ----------
md = ['# Plan de 30 días · @goldstudio.ba', '',
      f'Del {start.day} de {MESES[start.month]} al {items[-1]["fecha"].day} de {MESES[items[-1]["fecha"].month]} de {start.year}. Reels a las 10 h, carruseles a las 18 h.', '']
for it in items:
    md += [f'## Día {it["n"]} · {it["dia"]} {it["fecha"].day}/{it["fecha"].month} · {it["hora"]} h · {it["formato"]} · {it["pilar"]}', '',
           f'**Hook:** {it["hook"]}', '', f'**Cómo se ve:** {it["visual"]}', '']
    if it['formato'] == 'Reel':
        md += ['**Texto en pantalla (escenas):**'] + [f'{k+1}. {l}' for k, l in enumerate(it['escenas'])]
    else:
        md += ['**Láminas:**'] + [f'{k+1}. {l}' for k, l in enumerate(it['laminas'])]
    md += ['', f'**CTA:** {it["cta"]}', '', f'**Texto:** {it["caption"]}', '', f'**Por qué funciona:** {it["porque"]}', '']
open('/home/user/gold-studio-contenido/plan-30-dias.md', 'w').write('\n'.join(md))
print('ok')
