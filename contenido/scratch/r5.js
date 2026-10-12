const { chromium } = require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
await p.goto('file://'+process.cwd()+'/stories5.html');await p.evaluate(async()=>{await Promise.all([...document.fonts].map(f=>f.load().catch(()=>0)));await document.fonts.ready;});await p.waitForTimeout(300);
for(const id of process.argv.slice(2)){const el=await p.$('#'+id+' .st');await el.screenshot({path:'/home/user/gold-studio-final/historias/semana2/'+id+'.png'});}await b.close();})();
