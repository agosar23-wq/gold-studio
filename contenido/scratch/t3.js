const { chromium } = require('playwright');
(async()=>{
 const b = await chromium.launch(); const pg = await b.newPage({viewport:{width:1000,height:700}});
 const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
 await pg.goto('file:///home/user/app-nutri/demo.html');
 await pg.click('text=Entrar como paciente');
 for (const k of ['Frutilla','Cielo']) { await pg.click(`.sw:has-text("${k}")`); await pg.screenshot({path:k+'.png'}); }
 console.log('errors', errs); await b.close();
})();
