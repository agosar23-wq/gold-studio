exec(open('posts.py').read().split("slides = {}")[0])
A = 'file:///tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad/appshots/'
screens = [('p-inicio','Para cada paciente','Su próximo turno, <em>siempre a mano</em>'),
           ('p-docs','Biblioteca','Su plan y <em>recetarios</em>'),
           ('p-progreso','Evolución','Su progreso, <em>paso a paso</em>'),
           ('p-mensajes','Consultas','Mensajes <em>directos</em>'),
           ('n-panel','Para la nutricionista','Todo su consultorio <em>en un lugar</em>')]
imgs = ''.join(f'<img src="{A}{s}.png">' for s,_,_ in screens)
caps = ''.join(f'<div class="cap" id="cap{i}"><div class="eb">{e}</div><h1 style="font-size:84px;margin-top:22px">{t}</h1></div>' for i,(_,e,t) in enumerate(screens))
html = f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2);font-weight:500;font-style:italic}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-500-normal.woff2);font-weight:500}}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#1C1A17}}
.sc{{position:absolute;inset:0;opacity:0;font-family:J}}
#s1{{background:#1C1A17;color:#FAF6EE}}
#s2{{background:#FAF6EE;color:#1C1A17}}
#s3{{background:#C9A34E;color:#1C1A17;display:flex;flex-direction:column;align-items:center;justify-content:center}}
h1{{font-family:B;font-weight:500;margin:0;line-height:1.06;letter-spacing:-.01em}}
em{{font-style:italic}}
#s1 em{{color:#C9A34E}} #s2 em{{color:#8A6A22}}
.w{{display:inline-block}}
.eb{{font-size:30px;letter-spacing:.34em;text-transform:uppercase;font-weight:500;color:#8A6A22}}
#s1 .eb{{color:#C9A34E}}
.phone{{position:absolute;width:520px;left:280px;border-radius:72px;padding:16px;background:#0E0D0B;box-shadow:0 60px 120px -40px rgba(0,0,0,.55),0 0 0 3px #3A342B}}
.screen{{border-radius:58px;overflow:hidden;position:relative;aspect-ratio:390/844}}
.strip{{position:absolute;top:0;left:0;height:100%;display:flex}}
.strip img{{height:100%;display:block}}
.cap{{position:absolute;left:110px;right:110px;top:250px;text-align:center;opacity:0}}
.dots{{display:none!important;position:absolute;top:1700px;left:0;right:0;display:flex;justify-content:center;gap:16px}}
.dots i{{width:14px;height:14px;border-radius:50%;background:#E0D3B8;transition:none}}
.sp{{width:100%;height:100%;display:block}}
</style>
<div class="sc" id="s1">
  <div style="position:absolute;left:110px;right:110px;top:300px">
    <div class="eb" id="e1">Trabajo real</div>
    <h1 style="font-size:118px;margin-top:40px"><span class="w" id="a0">Una</span> <span class="w" id="a1">app</span> <span class="w" id="a2">a</span> <span class="w" id="a3">medida</span> <span class="w" id="a4">para</span> <span class="w" id="a5">un</span> <span class="w" id="a6">consultorio</span> <span class="w" id="a7">de</span> <em class="w" id="a8">nutrición</em></h1>
  </div>
  <div class="phone" id="ph1" style="top:1050px"><div class="screen"><img src="{A}login.png" style="width:100%;display:block"></div></div>
</div>
<div class="sc" id="s2">
  {caps}
  <div class="phone" id="ph2" style="top:560px"><div class="screen"><div class="strip" id="strip">{imgs}</div></div></div>
  <div class="dots">{''.join(f'<i id="d{i}"></i>' for i in range(len(screens)))}</div>
</div>
<div class="sc" id="s3">
  <div id="sp3" style="width:150px;height:150px;color:#FAF6EE;margin-bottom:70px">{SP}</div>
  <h1 id="h3" style="font-size:140px;text-align:center">¿Querés una<br>para <em style="color:#FAF6EE">tu negocio?</em></h1>
  <div id="c3" style="margin-top:80px;background:#1C1A17;color:#FAF6EE;font-size:44px;padding:34px 60px;border-radius:999px">Probá la demo ✦ link en la bio</div>
</div>
<script>
const N={len(screens)};
const E=x=>x<0?0:x>1?1:1-Math.pow(1-x,3);
const IO=x=>{{x=Math.max(0,Math.min(1,x));return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;}};
const B=x=>{{x=Math.max(0,Math.min(1,x));const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);}};
const $=id=>document.getElementById(id);
function up(el,p,d=80){{el.style.opacity=E(p);el.style.transform=`translateY(${{(1-E(p))*d}}px)`;}}
function scene(id,t,a){{const o=t>=a?Math.min(1,(t-a)/0.3):0;$(id).style.opacity=o;return t-a;}}
const T2=2.4, STEP=1.3, T3=T2+N*STEP+0.2;
window.render=function(t){{
  let k=scene('s1',t,0);
  up($('e1'),(k-0.1)/0.5,40);
  for(let i=0;i<9;i++) up($('a'+i),(k-0.2-i*0.08)/0.4,90);
  const r=E((k-0.6)/0.8); $('ph1').style.transform=`translateY(${{(1-r)*900}}px) rotate(${{(1-r)*8-4}}deg)`;
  // escena 2: el celular pasa pantallas
  k=scene('s2',t,T2);
  const pr=E(k/0.6); $('ph2').style.transform=`translateY(${{(1-pr)*120}}px) scale(${{0.94+0.06*pr}})`;
  const w=$('ph2').querySelector('.screen').clientWidth;
  let pos=0;
  for(let i=1;i<N;i++) pos+=IO((k-i*STEP+0.4)/0.42);
  $('strip').style.transform=`translateX(${{-pos*w}}px)`;
  for(let i=0;i<N;i++){{
    const c=$('cap'+i); const a=i*STEP-0.2, b=(i+1)*STEP-0.42;
    let o = i===0 ? E((k-0.1)/0.45) : E((k-a)/0.45);
    if(i<N-1) o*=1-E((k-b)/0.3);
    c.style.opacity=o; c.style.transform=`translateY(${{(1-o)*30}}px)`;
    $('d'+i).style.background = Math.round(pos)===i ? '#B8923A' : '#E0D3B8';
  }}
  // escena 3
  k=scene('s3',t,T3);
  const s=B((k-0.1)/0.6); $('sp3').style.transform=`scale(${{s*(1+0.06*Math.sin(k*4))}}) rotate(${{(1-s)*-90}}deg)`;
  up($('h3'),(k-0.2)/0.5,90); up($('c3'),(k-0.6)/0.4,60);
}};
window.DUR=T3+2.6;
</script>'''
open('reel2.html','w').write(html)
print(3.4+5*1.9+0.2+3.2)
