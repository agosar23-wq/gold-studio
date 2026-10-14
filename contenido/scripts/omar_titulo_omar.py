import base64, subprocess, os, sys
from PIL import Image
S='/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad'
img = sys.argv[1] if len(sys.argv) > 1 else f'{S}/omar-fix.png'
N = 1264
html = f'''<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:Mark;src:url(file://{S}/xfonts/permanent-marker.woff2)}}
body{{margin:0;background:transparent}} .c{{width:{N}px;height:{N}px;position:relative}}
.t{{position:absolute;left:0;right:0;top:70px;text-align:center;font-family:Mark;font-size:178px;line-height:1;color:#FFFDE8;transform:rotate(-4deg);
  text-shadow:0 0 6px #fff,0 0 18px #F4FF7A,0 0 40px #D8FF2E,0 0 80px #B6E60A}}
.n{{position:absolute;right:120px;top:270px;font-family:Mark;font-size:52px;color:#FFFDE8;transform:rotate(-4deg);text-shadow:0 0 10px #D8FF2E,0 0 26px #B6E60A}}
</style><div class="c"><div class="t">otra vuelta</div><div class="n">omar courtz</div></div>'''
open(f'{S}/tit.html','w').write(html)
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:{N},height:{N}}}}});await p.goto('file://{S}/tit.html');await p.evaluate(async()=>{{await document.fonts.ready}});await p.waitForTimeout(300);await p.screenshot({{path:'{S}/tit.png',omitBackground:true}});await b.close();}})();"""
open(f'{S}/tit.js','w').write(js)
subprocess.run(['node', f'{S}/tit.js'], check=True, env=dict(os.environ, NODE_PATH='/opt/node22/lib/node_modules'))
base = Image.open(img).convert('RGBA').resize((N, N)); base.alpha_composite(Image.open(f'{S}/tit.png').convert('RGBA'))
base.convert('RGB').save(f'{S}/portadas/omar-otra-vuelta-final.png')
