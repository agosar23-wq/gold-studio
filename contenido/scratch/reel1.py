import re
exec(open('posts.py').read().split("slides = {}")[0])  # reutiliza F, logo, SP
css = open('posts.py').read()  # not used
html = f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-normal.woff2);font-weight:500}}
@font-face{{font-family:B;src:url({F}bodoni-moda/files/bodoni-moda-latin-500-italic.woff2);font-weight:500;font-style:italic}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-300-normal.woff2);font-weight:300}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-400-normal.woff2);font-weight:400}}
@font-face{{font-family:J;src:url({F}jost/files/jost-latin-500-normal.woff2);font-weight:500}}
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden}}
.sc{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;font-family:J}}
#s1{{background:#FAF6EE;--g:#B8923A;color:#1C1A17}}
#s2{{background:#1C1A17;color:#FAF6EE}}
#s3{{background:#FAF6EE;color:#1C1A17;align-items:flex-start;padding:0 120px}}
#s4{{background:#C9A34E;color:#1C1A17}}
h1{{font-family:B;font-weight:500;margin:0;line-height:1.05;letter-spacing:-.01em}}
em{{font-style:italic}}
.w{{display:inline-block}}
.eb{{font-size:30px;letter-spacing:.34em;text-transform:uppercase;font-weight:500}}
.sp{{width:100%;height:100%;display:block}}
.li{{font-family:B;font-size:96px;display:flex;align-items:center;gap:40px;padding:26px 0}}
.li .b{{width:46px;height:46px;color:#B8923A;flex:none}}
.logo{{width:100%;height:auto;display:block}}
</style>
<div class="sc" id="s1">
  <svg id="ringsvg" width="560" height="560" viewBox="0 0 560 560" style="position:absolute;top:470px;left:260px">
    <circle id="ring" cx="280" cy="280" r="220" fill="none" stroke="#B8923A" stroke-width="70" stroke-dasharray="1382.3" stroke-dashoffset="1382.3" transform="rotate(-90 280 280)"/>
  </svg>
  <div id="sp1" style="position:absolute;top:400px;left:760px;width:200px;height:200px;color:#B8923A">{SP}</div>
  <div id="logo1" style="position:absolute;top:1180px;left:240px;width:600px;opacity:0">{logo}</div>
</div>
<div class="sc" id="s2">
  <div class="eb" id="e2" style="color:#C9A34E;margin-bottom:60px">Estudio de diseño digital</div>
  <h1 style="font-size:150px;text-align:center"><span class="w" id="w1">Tu</span> <span class="w" id="w2">marca,</span><br><span class="w" id="w3">con</span> <em class="w" id="w4" style="color:#C9A34E">brillo</em><br><em class="w" id="w5" style="color:#C9A34E">propio.</em></h1>
</div>
<div class="sc" id="s3">
  <div class="eb" id="e3" style="color:#8A6A22;margin-bottom:50px">Qué hago</div>
  <div class="li" id="l0"><div class="b">{SP}</div>Páginas web</div>
  <div class="li" id="l1"><div class="b">{SP}</div>Apps a medida</div>
  <div class="li" id="l2"><div class="b">{SP}</div>Tiendas online</div>
  <div class="li" id="l3"><div class="b">{SP}</div>Branding</div>
  <div class="li" id="l4"><div class="b">{SP}</div>Community<br>manager</div>
</div>
<div class="sc" id="s4">
  <div id="sp4" style="width:150px;height:150px;color:#FAF6EE;margin-bottom:70px">{SP}</div>
  <h1 id="h4" style="font-size:150px;text-align:center">¿Arrancamos<br><em style="color:#FAF6EE">tu proyecto?</em></h1>
  <div id="c4" style="margin-top:80px;background:#1C1A17;color:#FAF6EE;font-size:44px;padding:34px 60px;border-radius:999px">Link en la bio ✦ @goldstudio.ba</div>
</div>
<script>
const E=(x)=>x<0?0:x>1?1:1-Math.pow(1-x,3);           // easeOutCubic con clamp
const B=(x)=>{{x=Math.max(0,Math.min(1,x));const c=1.70158;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);}} // easeOutBack
const $=id=>document.getElementById(id);
function up(el,p,d=80){{el.style.opacity=E(p);el.style.transform=`translateY(${{(1-E(p))*d}}px)`;}}
function scene(id,t,a,b){{const s=$(id);let o=0;if(t>=a){{o=Math.min(1,(t-a)/0.3);}} s.style.opacity=o; return t-a;}}
window.render=function(t){{
  // escena 1: 0–3.2
  let k=scene('s1',t,0,3.2);
  $('ring').style.strokeDashoffset=1382.3*(1-E((k-0.2)/1.2));
  const sp=B((k-1.3)/0.5); $('sp1').style.transform=`scale(${{sp}}) rotate(${{(1-sp)*-90 + Math.sin(k*3)*4}}deg)`;
  up($('logo1'),(k-1.8)/0.6,60);
  // escena 2: 3.2–6.2
  k=scene('s2',t,3.2,6.2);
  up($('e2'),(k-0.1)/0.5,40);
  ['w1','w2','w3','w4','w5'].forEach((w,i)=>up($(w),(k-0.3-i*0.22)/0.5,90));
  // escena 3: 6.2–9.6
  k=scene('s3',t,6.2,9.6);
  up($('e3'),(k-0.1)/0.4,40);
  for(let i=0;i<5;i++){{const el=$('l'+i),p=(k-0.35-i*0.42)/0.45;el.style.opacity=E(p);el.style.transform=`translateX(${{(1-E(p))*-120}}px)`;
    el.querySelector('.b').style.transform=`scale(${{B(p)}}) rotate(${{(1-E(p))*-120}}deg)`;}}
  // escena 4: 9.6–13
  k=scene('s4',t,9.6,13.01);
  const s4=B((k-0.1)/0.6); $('sp4').style.transform=`scale(${{s4*(1+0.06*Math.sin(k*4))}}) rotate(${{(1-s4)*-90}}deg)`;
  up($('h4'),(k-0.3)/0.6,90); up($('c4'),(k-0.9)/0.5,60);
}};
</script>'''
open('reel1.html','w').write(html)
