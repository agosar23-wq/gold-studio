exec(open('stories.py').read())     # css, SP, st()
O = 'file:///home/user/gold-studio-final/historias/mias-orig/'
extra = '''
.ph{position:absolute;inset:0;overflow:hidden}
.ph img{position:absolute;display:block}
.shade{position:absolute;left:0;right:0}
.ttl{position:absolute;left:0;right:0;text-align:center}
.co{position:absolute;left:690px;font-family:J;color:#FAF6EE;text-shadow:0 2px 14px rgba(0,0,0,.55)}
.co small{display:block;font-size:34px;color:#E2C277;font-weight:500}
.co b{display:block;font-size:42px;font-weight:400;line-height:1.15}
.dot{position:absolute;width:26px;height:26px;border-radius:50%;background:#E2C277;border:3px solid #FAF6EE;box-shadow:0 0 12px rgba(0,0,0,.5)}
.pol{position:absolute;background:#FAF6EE;padding:22px 22px 70px;box-shadow:0 40px 80px -30px rgba(0,0,0,.85)}
.pol img{display:block;width:100%}
'''
def line(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#FAF6EE" stroke-width="3"/>'
# --- 1 · Hola, soy Agos ---
pts = [(548,845,'estudio','Ingeniería Industrial',740),(585,960,'amo','organizar todo',880),(592,1075,'soy','community manager',1020),(598,1238,'me encanta diseñar','y el mundo digital',1160),(540,1310,'pilates','mi momento',1300)]
lines = ''.join(line(x+13,y+13,672,ty+40) for x,y,_,_,ty in pts)
dots = ''.join(f'<i class="dot" style="left:{x}px;top:{y}px"></i>' for x,y,_,_,_ in pts)
cos = ''.join(f'<div class="co" style="top:{ty}px"><small>{a}</small><b>{b}</b></div>' for _,_,a,b,ty in pts)
agos = f'''<div class="st n" style="padding:0">
 <div class="ph"><img src="{O}agos.png" style="height:1920px;left:-100px;top:0"></div>
 <div class="shade" style="top:0;height:700px;background:linear-gradient(180deg,rgba(10,14,40,.75),rgba(10,14,40,0))"></div>
 <div class="ttl" style="top:250px"><h1 style="font-size:132px;color:#FAF6EE">Hola, soy <em style="color:#E2C277">Agos</em></h1>
 <p style="font-family:J;font-size:40px;letter-spacing:.22em;text-transform:uppercase;color:#FAF6EE;margin:26px 0 0;font-weight:500">creadora de Gold Studio</p></div>
 <div style="position:absolute;left:480px;right:-200px;top:600px;height:980px;background:radial-gradient(ellipse at 55% 50%,rgba(12,12,20,.66),rgba(12,12,20,.45) 40%,rgba(12,12,20,0) 70%)"></div>
 <svg style="position:absolute;inset:0" width="1080" height="1920">{lines}</svg>{dots}{cos}</div>'''
# --- 2 · Y no estoy sola en esto ---
angie = f'''<div class="st n" style="padding:0">
 <div class="ph"><img src="{O}angie.jpg" style="height:1920px;left:-65px;top:0"></div>
 <div class="shade" style="top:0;height:900px;background:linear-gradient(180deg,rgba(20,18,22,.7),rgba(20,18,22,0))"></div>
 <div class="ttl" style="top:280px;padding:0 90px"><h1 style="font-size:124px;color:#FAF6EE">Y no estoy <em style="color:#E2C277">sola en esto</em></h1>
 <p style="font-family:J;font-size:44px;line-height:1.35;color:#FAF6EE;margin:40px 0 0;font-weight:300">Angie me acompaña<br>en cada paso de Gold Studio</p></div></div>'''
# --- 3 · Desde los 5 años juntas ---
cinco = f'''<div class="st n" style="padding:0">
 <div class="ttl" style="top:260px"><h1 style="font-size:120px;color:#FAF6EE">Desde los 5 años <em style="color:#C9A34E">juntas</em></h1></div>
 <div class="pol" style="left:90px;top:560px;width:640px;transform:rotate(-5deg)"><img src="{O}chiquitas-hd.jpg"></div>
 <div class="pol" style="left:380px;top:1010px;width:620px;transform:rotate(4deg)"><img src="{O}cole.jpg"></div>
 <div class="ttl" style="top:1560px"><p style="font-family:J;font-size:44px;color:#FAF6EE;margin:0;font-weight:300">Angie y yo, toda la vida</p>
 <p style="font-family:B;font-style:italic;font-size:68px;color:#C9A34E;margin:8px 0 0">y ahora, Gold Studio</p></div></div>'''
S = {'1-hola-soy-agos': agos, '2-no-estoy-sola': angie, '3-desde-los-5': cinco}
page = '<!doctype html><meta charset="utf-8"><style>'+css+extra+'</style>'+''.join(f'<div id="{k}">{v}</div>' for k,v in S.items())
open('stories3.html','w').write(page)
