const { chromium } = require('playwright');
(async()=>{ const b=await chromium.launch(); const out='/tmp/claude-0/-home-user/3d6a0a2e-a980-5532-8595-cde247c8de79/scratchpad/appshots/';
 const url='file:///home/user/gold-studio-web/demo-anon.html';
 let p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2});
 await p.goto(url); await p.addStyleTag({content:'.demo-bar{display:none!important}'}); await p.waitForTimeout(500);
 await p.screenshot({path:out+'login.png'});
 await p.click('[data-u="lucia@ejemplo.com"]'); await p.waitForTimeout(500);
 await p.screenshot({path:out+'p-inicio.png'});
 await p.screenshot({path:out+'p-inicio-full.png',fullPage:true});
 for (const k of ['docs','progreso','turnos','mensajes']) { const s=`[data-action="pac"][data-k="${k}"]`; await p.locator(s).locator("visible=true").first().click(); await p.waitForTimeout(400); await p.screenshot({path:out+'p-'+k+'.png'}); }
 p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2});
 await p.goto(url); await p.evaluate(()=>{try{localStorage.clear()}catch(e){}}); await p.goto(url); await p.addStyleTag({content:'.demo-bar{display:none!important}'});
 await p.click('[data-u="nutri@ejemplo.com"]'); await p.waitForTimeout(500);
 await p.screenshot({path:out+'n-panel.png'});
 for (const k of ['pacientes','mensajes']) { await p.locator(`[data-action="nv"][data-k="${k}"]`).locator("visible=true").first().click(); await p.waitForTimeout(400); await p.screenshot({path:out+'n-'+k+'.png'}); }
 await b.close(); })();
